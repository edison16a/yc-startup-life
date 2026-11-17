#!/usr/bin/env python3
"""Keyword search over every past YC company (whitespace check against YC itself).

  python3 -I scripts/yc_overlap.py "dental" "insurance" --all --limit 20

Matches keywords (case-insensitive) in name, one-liner, description and tags. Without --all a company
matches if ANY keyword hits; with --all it needs every keyword. Uses data/companies_enriched.csv when present.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, csv
from common import DATA, test_blocklist


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--exclude", nargs="*", action="extend", default=[], help="slugs to leave out (use for backtests so a company does not see its own outcome)")
    a = ap.parse_args()
    a.exclude = set(a.exclude) | test_blocklist()
    path = DATA / "companies_enriched.csv"
    if not path.exists():
        path = DATA / "companies.csv"
    kws = [k.lower() for k in a.keywords]
    hits = []
    for r in csv.DictReader(path.open(encoding="utf-8")):
        if r["slug"] in a.exclude:
            continue
        hay = " ".join((r.get(f) or "") for f in ("name", "one_liner", "long_description", "tags")).lower()
        found = [k for k in kws if k in hay]
        if (len(found) == len(kws)) if a.all else bool(found):
            hits.append((len(found), r))
    hits.sort(key=lambda x: (-x[0], x[1].get("batch_year") or "", x[1]["name"]))
    print(f"{len(hits)} matching YC companies (showing {min(len(hits), a.limit)}) from {path.name}")
    for n, r in hits[: a.limit]:
        extra = f" | outcome: {r['outcome_class']}" if r.get("outcome_class") else ""
        print(f"- {r['name']} [{r['slug']}] ({r['batch']}, {r['status']}): {r['one_liner']}{extra}")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
