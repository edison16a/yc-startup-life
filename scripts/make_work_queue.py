#!/usr/bin/env python3
"""Build the research queue: shards of companies that still need depth-2 research.

Order: (1) calibration sample first, (2) everything else by priority tier.
  The calibration sample is a deterministic random sample (config.extraction.calibration_fraction of every
  batch, at least one per batch). It is researched first because base rates computed on a hand-picked
  list of winners would be biased; a random sample gives unbiased base rates early.
Tiers for the rest: 0 public or YC "top company"; 1 acquired; 2 active, last 4 years; 3 other active; 4 inactive.

Usage: python3 -I scripts/make_work_queue.py [--only calibration|rest] [--shard-size N] [--limit N] [--depth 2]
Calibration shards are named cal_NNNN.json, the rest shard_NNNN.json, in data/queue/.
A company is done when data/enrichment/<slug>.json exists with depth >= the queue depth, or it is listed
in data/unresearchable.csv (columns: slug,reason).
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, csv, datetime, hashlib, json, math, shutil, collections
from common import DATA, CONFIG, load_unresearchable

CSV = DATA / "companies.csv"
ENR = DATA / "enrichment"
QUEUE = DATA / "queue"
CAL = DATA / "calibration_sample.csv"


def tier(r, this_year):
    if r["status"] == "Public" or r["top_company"] == "True":
        return 0
    if r["status"] == "Acquired":
        return 1
    year = int(r["batch_year"]) if r["batch_year"] else 0
    if r["status"] == "Active" and year >= this_year - 4:
        return 2
    return 3 if r["status"] == "Active" else 4


def calibration_slugs(rows, frac, seed):
    by_batch = collections.defaultdict(list)
    for r in rows:
        by_batch[r["batch"]].append(r["slug"])
    chosen = []
    for batch, slugs in by_batch.items():
        slugs.sort(key=lambda s: hashlib.sha256(f"{seed}:{s}".encode()).hexdigest())
        chosen += [(s, batch) for s in slugs[: max(1, math.ceil(frac * len(slugs)))]]
    chosen.sort(key=lambda x: hashlib.sha256(f"{seed}:order:{x[0]}".encode()).hexdigest())
    return chosen


def done(slug, depth):
    p = ENR / f"{slug}.json"
    if not p.exists():
        return False
    try:
        return int(json.loads(p.read_text()).get("depth", 1)) >= depth
    except Exception:
        return False


def main():
    ex = CONFIG["extraction"]
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=2, choices=[1, 2])
    ap.add_argument("--shard-size", type=int, default=ex["shard_size"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", choices=["calibration", "rest"])
    a = ap.parse_args()

    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    by_slug = {r["slug"]: r for r in rows}
    cal = calibration_slugs(rows, ex["calibration_fraction"], ex["calibration_seed"])
    with CAL.open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["slug", "batch"]); w.writerows(cal)
    cal_set = {s for s, _ in cal}
    skip = set(load_unresearchable())
    year = datetime.date.today().year

    cal_todo = [by_slug[s] for s, _ in cal if s not in skip and not done(s, a.depth)]
    rest = [r for r in rows if r["slug"] not in cal_set and r["slug"] not in skip and not done(r["slug"], a.depth)]
    rest.sort(key=lambda r: (tier(r, year), -(int(r["batch_year"]) if r["batch_year"] else 0), r["name"] or ""))
    if a.only == "calibration":
        rest = []
    if a.only == "rest":
        cal_todo = []
    if a.limit:
        cal_todo = cal_todo[: a.limit]
        rest = rest[: max(0, a.limit - len(cal_todo))]

    if QUEUE.exists():
        shutil.rmtree(QUEUE)
    QUEUE.mkdir(parents=True)
    keep = ["slug", "name", "batch", "status", "stage", "industry", "tags", "one_liner",
            "long_description", "website", "yc_url", "team_size", "top_company", "all_locations", "launched_at"]
    counts = {}
    for prefix, items, is_cal in (("cal", cal_todo, True), ("shard", rest, False)):
        n = 0
        for i in range(0, len(items), a.shard_size):
            chunk = [{**{k: r[k] for k in keep}, "tier": tier(r, year), "calibration": is_cal}
                     for r in items[i:i + a.shard_size]]
            n += 1
            (QUEUE / f"{prefix}_{n:04d}.json").write_text(json.dumps(
                {"depth": a.depth, "calibration": is_cal, "companies": chunk}, ensure_ascii=False, indent=1))
        counts[prefix] = (len(items), n)
    print(f"calibration sample: {len(cal)} companies ({counts['cal'][0]} still to do, {counts['cal'][1]} shards)")
    print(f"rest: {counts['shard'][0]} still to do in {counts['shard'][1]} shards -> {QUEUE}")


if __name__ == "__main__":
    main()
