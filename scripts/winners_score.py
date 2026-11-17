#!/usr/bin/env python3
"""Score the blind forecasts in evaluations/winners-2026 against a ground truth file.

  python3 -I scripts/winners_score.py --truth DIR_WITH_TRUTH_JSON --kinds KINDS.json [--leaks LEAKS.txt] [--json OUT]

truth DIR: files 1.json .. N.json, each a list of {slug, confidence, rounds_after_batch_start, standard_yc_deal_only,
largest_nonYC_round_usd, ...}. kinds: {slug: 'winner_press'|'winner_database'|'unselected'}.
Outcome classes (only high/medium confidence truth counts as known):
  raised  = a post batch round above 1M with a press, company, investor or filing source (or any source at medium+)
  none    = standard_yc_deal_only true with medium or high confidence
  unknown = everything else (left out of the scores)
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))
import argparse, glob, json, math, statistics
from common import ROOT


def load_truth(d):
    out = {}
    for f in sorted(_pl.Path(d).glob("*.json")):
        for r in json.loads(f.read_text()):
            out[r["slug"]] = r
    return out


def outcome(t):
    conf = (t.get("confidence") or "low").lower()
    amt = t.get("largest_nonYC_round_usd")
    rounds = t.get("rounds_after_batch_start") or []
    good_src = any(r.get("source_type") in ("press", "company", "investor", "filing") for r in rounds)
    if amt and amt >= 1_000_000 and (conf in ("high", "medium") or good_src):
        return "raised", amt
    if t.get("standard_yc_deal_only") is True and conf in ("high", "medium"):
        return "none", None
    return "unknown", amt


def forecast(slug):
    p = ROOT / "evaluations" / "winners-2026" / slug / "evaluation_input.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    lad = {s["stage"]: s for s in d.get("ladder", [])}
    seed, a = lad.get("seed"), lad.get("series_a")
    if not seed:
        return None
    return {"p_seed": seed["p_reach_given_prev"], "p_a": a["p_reach_given_prev"] if a else None, "bands": seed.get("bands", [])}


def band_hit(bands, amt):
    for b in bands:
        lo, hi = b["raise_usd"]
        if lo <= amt <= hi:
            return b["p_band"]
    return 0.0


def auc(pos, neg):
    if not pos or not neg:
        return None
    w = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return w / (len(pos) * len(neg))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--truth", required=True); ap.add_argument("--kinds", required=True)
    ap.add_argument("--leaks"); ap.add_argument("--json")
    a = ap.parse_args()
    truth = load_truth(a.truth)
    kinds = {i["slug"]: i["kind"] for i in json.loads(open(a.kinds).read())}
    leaked = set()
    if a.leaks:
        for l in open(a.leaks):
            if l.strip():
                leaked.add(l.split()[0])
    rows = []
    for s, t in truth.items():
        f = forecast(s)
        if not f:
            continue
        o, amt = outcome(t)
        rows.append({"slug": s, "kind": kinds.get(s), "outcome": o, "amount": amt, "leak": s in leaked, **f})
    def summarize(rs, label):
        raised = [r for r in rs if r["outcome"] == "raised"]
        none = [r for r in rs if r["outcome"] == "none"]
        known = raised + none
        res = {"label": label, "n_forecasts": len(rs), "n_raised": len(raised), "n_none": len(none), "n_unknown": len(rs) - len(known)}
        if known:
            res["mean_p_seed_raised"] = statistics.mean(r["p_seed"] for r in raised) if raised else None
            res["mean_p_seed_none"] = statistics.mean(r["p_seed"] for r in none) if none else None
            res["brier_seed"] = statistics.mean((r["p_seed"] - (1 if r["outcome"] == "raised" else 0)) ** 2 for r in known)
            res["auc_raised_vs_none"] = auc([r["p_seed"] for r in raised], [r["p_seed"] for r in none])
            res["share_raised_of_known"] = len(raised) / len(known)
        if raised:
            hits = [band_hit(r["bands"], r["amount"]) for r in raised]
            res["band_coverage"] = sum(h > 0 for h in hits) / len(hits)
            res["mean_p_band_on_actual"] = statistics.mean(hits)
            amts = [r["amount"] for r in raised]
            mids = []
            for r in raised:
                top = max(r["bands"], key=lambda b: b["p_band"])
                mids.append(math.sqrt(max(top["raise_usd"][0], 1.0) * max(top["raise_usd"][1], 1.0)))
            ratios = [x / m for x, m in zip(amts, mids)]
            res["median_actual_over_forecast_mode_band_mid"] = statistics.median(ratios)
            res["share_actual_above_top_band"] = sum(r["amount"] > max(b["raise_usd"][1] for b in r["bands"]) for r in raised) / len(raised)
            res["share_actual_above_all_band_hi_or_below_lo"] = sum(hits_i == 0 for hits_i in hits) / len(hits)
        return res
    out = {"all": summarize(rows, "all known"), "no_leak_flags": summarize([r for r in rows if not r["leak"]], "no leak flags"),
           "winners": summarize([r for r in rows if (r["kind"] or "").startswith("winner")], "winners"),
           "controls": summarize([r for r in rows if r["kind"] == "unselected"], "controls")}
    out["rows"] = rows
    if a.json:
        open(a.json, "w").write(json.dumps(out, indent=1))
    for k in ("all", "no_leak_flags", "winners", "controls"):
        print(json.dumps(out[k], indent=1))
    return 0


if __name__ == "__main__":
    _sys.exit(main())
