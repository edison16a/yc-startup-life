#!/usr/bin/env python3
"""Base rates from the researched YC companies: how far companies got, how fast, for how much, and why they failed.

  python3 -I scripts/base_rates.py                          overall
  python3 -I scripts/base_rates.py --industry Fintech --years 2018-2024 --calibration-only
  python3 -I scripts/base_rates.py --tag "AI" --model B2B --json
  python3 -I scripts/base_rates.py --write-tables           write knowledge/tables/*.csv for standard cohorts

Filters: --industry/--tag match the directory fields; --model matches business_model (researched companies only);
--years A-B filters by batch year; --calibration-only restricts to the random calibration sample.

How to read the ladder. Funding history is often not public, so each stage shows three numbers:
  lower  = reached / all researched (unknown counted as "did not reach")
  known  = reached / companies whose funding history is complete or partial
  upper  = (reached + companies with no funding data found) / all researched
The truth is usually between lower and upper. "known" is biased upward because companies with documented
funding are the ones that raised. Use the calibration sample for unbiased cohort rates, and report the range.
The status mix always comes from the directory for every company, researched or not.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, collections, csv, json
from common import (DATA, KNOW, load_companies, load_enrichment, load_unresearchable, derive, era, percentile,
                    wilson, num, STAGE_RANK, RANK_NAME, FAILURE_FACTORS, SUCCESS_FACTORS)

STAGE_LABEL = {1: "seed", 2: "series_a", 3: "series_b", 4: "series_c", 5: "series_d_plus"}


def calibration_set():
    p = DATA / "calibration_sample.csv"
    return {r["slug"] for r in csv.DictReader(p.open())} if p.exists() else set()


def select(companies, enr, years=None, industry=None, tag=None, model=None, cal_only=False):
    cal = calibration_set() if cal_only else None
    out = []
    for slug, row in companies.items():
        yr = int(row["batch_year"]) if row["batch_year"] else None
        if years and (yr is None or not years[0] <= yr <= years[1]):
            continue
        if industry and industry.lower() not in f"{row['industry']} {row['subindustry']}".lower():
            continue
        if tag and tag.lower() not in row["tags"].lower():
            continue
        if cal is not None and slug not in cal:
            continue
        if model:
            e = enr.get(slug)
            if not e or model.lower() not in e["business_model"].lower():
                continue
        out.append(slug)
    return out


def quart(vals):
    v = [x for x in vals if x is not None]
    return {"n": len(v), "p25": percentile(v, .25), "p50": percentile(v, .5), "p75": percentile(v, .75)}


def analyze(companies, enr, slugs):
    res = {"n_directory": len(slugs)}
    st = collections.Counter(companies[s]["status"] for s in slugs)
    res["status_mix"] = {k: {"n": v, "share": v / len(slugs) if slugs else None} for k, v in st.items()}
    d2 = [s for s in slugs if s in enr and enr[s]["depth"] == 2]
    res["n_researched"] = len(d2)
    if not d2:
        res.update(ladder=[], time={}, outcome_mix={}, rounds=[], failure_factors={}, success_factors={})
        return res
    dv = {s: derive(enr[s], companies[s]) for s in d2}
    cov = {s: enr[s]["funding_data_coverage"] for s in d2}
    known = [s for s in d2 if cov[s] in ("complete", "partial")]
    none_found = [s for s in d2 if cov[s] == "none_found"]
    res["funding_coverage"] = {"complete": sum(cov[s] == "complete" for s in d2),
                               "partial": sum(cov[s] == "partial" for s in d2), "none_found": len(none_found)}
    ladder = []
    for r in range(1, 6):
        reached_all = sum(dv[s]["highest_post_yc_rank"] >= r for s in d2)
        reached_known = sum(dv[s]["highest_post_yc_rank"] >= r for s in known)
        lo_ci, hi_ci = wilson(reached_known, len(known))
        prev_pool = [s for s in known if dv[s]["highest_post_yc_rank"] >= r - 1] if r > 1 else known
        cond = sum(dv[s]["highest_post_yc_rank"] >= r for s in prev_pool)
        ladder.append({
            "stage": STAGE_LABEL[r], "reached": reached_all,
            "lower": reached_all / len(d2), "known": reached_known / len(known) if known else None,
            "upper": (reached_all + len([s for s in none_found if dv[s]["highest_post_yc_rank"] < r])) / len(d2),
            "ci_low": lo_ci, "ci_high": hi_ci,
            "conditional_on_prev": cond / len(prev_pool) if prev_pool else None, "conditional_n": len(prev_pool)})
    res["ladder"] = ladder
    oc = collections.Counter(dv[s]["outcome_class"] for s in d2)
    res["outcome_mix"] = {k: {"n": v, "share": v / len(d2)} for k, v in oc.items()}

    t = {}
    for r in range(1, 5):
        t[f"months_to_{STAGE_LABEL[r]}"] = quart([dv[s]["first_months_by_rank"][r] for s in d2])
    t["months_to_exit"] = quart([dv[s]["exit_months"] for s in d2 if enr[s]["exit"].get("type") in ("acquisition", "merger", "ipo", "spac")])
    t["months_to_shutdown"] = quart([dv[s]["exit_months"] for s in d2 if enr[s]["exit"].get("type") == "shutdown"])
    res["time"] = t

    rb = collections.defaultdict(lambda: {"amt": [], "post": []})
    for s in d2:
        for r in dv[s]["rounds"]:
            if r.get("post_yc") and r.get("stage") in STAGE_RANK and STAGE_RANK[r["stage"]] >= 1:
                d = r.get("date") or ""
                key = (STAGE_LABEL[STAGE_RANK[r["stage"]]], era(d[:4]) if d[:4].isdigit() else "unknown")
                rb[key]["amt"].append(num(r.get("amount_usd")))
                rb[key]["post"].append(num(r.get("post_money_usd")))
    res["rounds"] = [{"stage": k[0], "round_era": k[1], "amount": quart(v["amt"]), "post_money": quart(v["post"])}
                     for k, v in sorted(rb.items())]
    res["failure_factors"] = dict(collections.Counter(
        f for s in d2 if dv[s]["outcome_class"] == "shutdown" for f in enr[s]["failure_factors"]))
    winners = [s for s in d2 if dv[s]["outcome_class"] in ("acquired", "public") or dv[s]["highest_post_yc_rank"] >= 3]
    res["n_winners"] = len(winners)
    res["success_factors"] = dict(collections.Counter(f for s in winners for f in enr[s]["success_factors"]))
    res["n_shutdown"] = sum(dv[s]["outcome_class"] == "shutdown" for s in d2)
    return res


def factor_outcomes(companies, enr, slugs):
    """Outcome rates by feature value (technical complexity, takeover risk, moat, competitor count, founders...)."""
    d2 = [s for s in slugs if s in enr and enr[s]["depth"] == 2]
    dv = {s: derive(enr[s], companies[s]) for s in d2}

    def bucket_comp(n):
        return "0" if n == 0 else "1-2" if n <= 2 else "3-5" if n <= 5 else "6+"

    feats = {
        "technical_complexity": lambda e, s: e["technical_complexity"].get("rating"),
        "defensibility": lambda e, s: e["defensibility"].get("rating"),
        "takeover_risk_then": lambda e, s: e["takeover_risk_then"].get("rating"),
        "competitors_at_founding": lambda e, s: bucket_comp(len(e["competition_at_founding"]["competitors"])),
        "technical_founder": lambda e, s: any(f.get("technical") is True for f in e["founders"]),
        "prior_startup_founder": lambda e, s: any(bool(f.get("previous_startups")) for f in e["founders"]),
        "founder_count": lambda e, s: min(len(e["founders"]), 4),
        "pivoted": lambda e, s: len(e["pivots"]) > 0,
        "business_model": lambda e, s: e["business_model"].split(" ")[0].strip(",;()").lower(),
    }
    rows = []
    for name, fn in feats.items():
        groups = collections.defaultdict(list)
        for s in d2:
            v = fn(enr[s], s)
            if v is not None:
                groups[v].append(s)
        for v, ss in sorted(groups.items(), key=lambda kv: str(kv[0])):
            kn = [s for s in ss if enr[s]["funding_data_coverage"] != "none_found"]
            n = len(ss)
            rows.append({
                "feature": name, "value": v, "n": n,
                "share_shutdown": sum(dv[s]["outcome_class"] == "shutdown" for s in ss) / n,
                "share_acquired_or_public": sum(dv[s]["outcome_class"] in ("acquired", "public") for s in ss) / n,
                "n_known_funding": len(kn),
                "share_reached_series_a_known": (sum(dv[s]["highest_post_yc_rank"] >= 2 for s in kn) / len(kn)) if kn else "",
                "share_reached_series_b_known": (sum(dv[s]["highest_post_yc_rank"] >= 3 for s in kn) / len(kn)) if kn else ""})
    return rows


def pct(x):
    return "n/a" if x is None else f"{x:.0%}"


def money(x):
    if x is None:
        return "n/a"
    return f"${x / 1e9:.1f}B" if x >= 1e9 else f"${x / 1e6:.1f}M" if x >= 1e6 else f"${x / 1e3:.0f}K"


def render(res, title):
    L = [f"## {title}", f"Directory companies in cohort: {res['n_directory']}; fully researched: {res['n_researched']}"]
    if res["n_directory"]:
        L.append("Status mix (directory, all companies): " + ", ".join(
            f"{k} {v['n']} ({pct(v['share'])})" for k, v in sorted(res["status_mix"].items())))
    if not res["n_researched"]:
        L.append("(no researched companies in this cohort yet)")
        return "\n".join(L)
    if res["n_researched"] < 30:
        L.append(f"WARNING: only {res['n_researched']} researched companies; treat rates as anecdotes, not base rates.")
    fc = res["funding_coverage"]
    L.append(f"Funding data coverage: complete {fc['complete']}, partial {fc['partial']}, none found {fc['none_found']}")
    L.append("\nPost-YC funding ladder (lower / known-only / upper; 95% CI on known-only; P(stage | previous stage)):")
    for r in res["ladder"]:
        L.append(f"  {r['stage']:<14} {pct(r['lower']):>4} / {pct(r['known']):>4} / {pct(r['upper']):>4}   "
                 f"CI {pct(r['ci_low'])}-{pct(r['ci_high'])}   cond {pct(r['conditional_on_prev'])} (n={r['conditional_n']})")
    L.append("\nOutcome mix (researched): " + ", ".join(f"{k} {v['n']} ({pct(v['share'])})" for k, v in sorted(res["outcome_mix"].items())))
    L.append("\nMonths from batch start (p25 / median / p75, n):")
    for k, q in res["time"].items():
        if q["n"]:
            L.append(f"  {k:<22} {q['p25']:.0f} / {q['p50']:.0f} / {q['p75']:.0f}  (n={q['n']})")
    L.append("\nRound sizes (p25 / median / p75), by era of the round:")
    for r in res["rounds"]:
        a, p = r["amount"], r["post_money"]
        L.append(f"  {r['stage']:<14} {r['round_era']:<10} raise {money(a['p25'])}/{money(a['p50'])}/{money(a['p75'])} (n={a['n']})   "
                 f"post {money(p['p25'])}/{money(p['p50'])}/{money(p['p75'])} (n={p['n']})")
    if res["failure_factors"]:
        L.append(f"\nFailure factors among {res['n_shutdown']} shutdowns: " + ", ".join(
            f"{k} {v}" for k, v in sorted(res["failure_factors"].items(), key=lambda kv: -kv[1])[:8]))
    if res["success_factors"]:
        L.append(f"Success factors among {res['n_winners']} winners: " + ", ".join(
            f"{k} {v}" for k, v in sorted(res["success_factors"].items(), key=lambda kv: -kv[1])[:8]))
    return "\n".join(L)


def write_tables(companies, enr):
    out = KNOW / "tables"
    out.mkdir(parents=True, exist_ok=True)
    allslugs = list(companies)
    cohorts = {"overall": allslugs,
               "calibration_sample": select(companies, enr, cal_only=True)}
    for e in ("2005-2012", "2013-2017", "2018-2021", "2022+"):
        cohorts[f"era:{e}"] = [s for s in allslugs if era(companies[s]["batch_year"]) == e]
    inds = collections.Counter(companies[s]["industry"] for s in allslugs if s in enr)
    for ind, n in inds.items():
        if n >= 30 and ind:
            cohorts[f"industry:{ind}"] = [s for s in allslugs if companies[s]["industry"] == ind]
    prog, mix, tms = [], [], []
    for name, slugs in cohorts.items():
        r = analyze(companies, enr, slugs)
        for k, v in r["status_mix"].items():
            mix.append({"cohort": name, "status": k, "n": v["n"], "share": v["share"], "n_cohort": r["n_directory"]})
        for l in r["ladder"]:
            prog.append({"cohort": name, "n_researched": r["n_researched"], **l})
        for k, q in r["time"].items():
            tms.append({"cohort": name, "milestone": k, **q})

    def w(fname, rows):
        if not rows:
            (out / fname).write_text("")
            return
        with (out / fname).open("w", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            wr.writeheader(); wr.writerows(rows)

    w("status_mix.csv", mix)
    w("stage_progression.csv", prog)
    w("time_to_milestones.csv", tms)
    overall = analyze(companies, enr, allslugs)
    rb = []
    for r in overall["rounds"]:
        rb.append({"stage": r["stage"], "round_era": r["round_era"],
                   **{f"amount_{k}": v for k, v in r["amount"].items()},
                   **{f"post_money_{k}": v for k, v in r["post_money"].items()}})
    w("round_benchmarks.csv", rb)
    w("failure_factor_counts.csv", [{"factor": k, "n": v, "share_of_shutdowns": v / overall["n_shutdown"]}
                                    for k, v in sorted(overall["failure_factors"].items(), key=lambda kv: -kv[1])] if overall.get("n_shutdown") else [])
    w("success_factor_counts.csv", [{"factor": k, "n": v, "share_of_winners": v / overall["n_winners"]}
                                    for k, v in sorted(overall["success_factors"].items(), key=lambda kv: -kv[1])] if overall.get("n_winners") else [])
    w("factor_outcomes.csv", factor_outcomes(companies, enr, allslugs))
    print(f"wrote tables to {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years")
    ap.add_argument("--industry")
    ap.add_argument("--tag")
    ap.add_argument("--model")
    ap.add_argument("--calibration-only", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--write-tables", action="store_true")
    a = ap.parse_args()
    companies = load_companies()
    enr = load_enrichment(min_depth=1)
    if a.write_tables:
        write_tables(companies, enr)
        return 0
    years = tuple(int(x) for x in a.years.split("-")) if a.years else None
    slugs = select(companies, enr, years, a.industry, a.tag, a.model, a.calibration_only)
    res = analyze(companies, enr, slugs)
    if a.json:
        print(json.dumps(res, indent=1, default=str))
    else:
        desc = ", ".join(f"{k}={v}" for k, v in (("industry", a.industry), ("tag", a.tag), ("model", a.model),
                         ("years", a.years), ("calibration_only", a.calibration_only or None)) if v) or "all companies"
        print(render(res, f"Cohort: {desc}"))
    return 0


if __name__ == "__main__":
    _sys.exit(main())
