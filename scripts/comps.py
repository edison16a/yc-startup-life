#!/usr/bin/env python3
"""Find the past YC companies most similar to a startup description, with their outcomes and competition then.

  python3 -I scripts/comps.py "AI phone agents that call insurers to verify dental benefits" --k 12
  python3 -I scripts/comps.py "..." --all      include companies that have not been researched yet (text match only)
  python3 -I scripts/comps.py "..." --json

Similarity is TF-IDF cosine over the description, tags, industry, problem, customer and business model.
Use it to pick analogs for the evaluator and to check whitespace for the creator. It does not decide anything:
read the analog records (data/enrichment/<slug>.json) before relying on them.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, collections, json, math, re
from common import load_companies, load_enrichment, derive, RANK_NAME, test_blocklist

STOP = set("the and for with that this from are was our their they them its has have had will can all any into more most "
           "than then over out who how what when where which your you not but one two use used using new help helps make "
           "makes built build builds company companies platform software service services solution solutions based".split())


def toks(s):
    return [w for w in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(w) >= 3 and w not in STOP]


def doc_text(row, e):
    parts = [row["name"], row["one_liner"], row["long_description"], row["tags"], row["industry"], row["subindustry"]]
    if e:
        parts += [e.get("problem"), e.get("target_customer"), e.get("business_model"), e.get("product_category")]
    return " ".join(p for p in parts if p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--exclude", nargs="*", action="extend", default=[], help="slugs to leave out (use for backtests so a company is not its own analog)")
    a = ap.parse_args()
    a.exclude = set(a.exclude) | test_blocklist()
    companies = load_companies()
    enr = load_enrichment(min_depth=1)
    pool = [s for s in companies if s not in a.exclude and (a.all or (s in enr and enr[s]["depth"] == 2))]
    if not pool:
        print("No researched companies yet. Re-run with --all to search the directory text, or run the extractor skill.")
        return 1
    docs = {s: collections.Counter(toks(doc_text(companies[s], enr.get(s)))) for s in pool}
    df = collections.Counter(t for d in docs.values() for t in d)
    N = len(docs)
    idf = lambda t: math.log((N + 1) / (df.get(t, 0) + 1)) + 1

    def vec(c):
        v = {t: (1 + math.log(n)) * idf(t) for t, n in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        return {t: x / norm for t, x in v.items()}

    q = vec(collections.Counter(toks(a.query)))
    scored = []
    for s, c in docs.items():
        v = vec(c)
        scored.append((sum(w * v.get(t, 0) for t, w in q.items()), s))
    scored.sort(reverse=True)
    out = []
    for sim, s in scored[: a.k]:
        row, e = companies[s], enr.get(s)
        item = {"slug": s, "name": row["name"], "batch": row["batch"], "status": row["status"],
                "similarity": round(sim, 3), "one_liner": row["one_liner"]}
        if e and e["depth"] == 2:
            d = derive(e, row)
            item.update({
                "outcome_class": d["outcome_class"],
                "highest_post_yc_round": RANK_NAME.get(d["highest_post_yc_rank"], "none"),
                "technical_complexity": e["technical_complexity"].get("rating"),
                "takeover_risk_then": e["takeover_risk_then"].get("rating"),
                "competitors_then": [c["name"] for c in e["competition_at_founding"]["competitors"]][:6],
                "failure_factors": e["failure_factors"], "success_factors": e["success_factors"],
                "outcome_analysis": e["outcome_analysis"]})
        out.append(item)
    if a.json:
        print(json.dumps(out, indent=1))
        return 0
    for it in out:
        print(f"{it['similarity']:.2f}  {it['name']} [{it['slug']}] {it['batch']}, {it['status']}: {it['one_liner']}")
        if "outcome_class" in it:
            print(f"      outcome: {it['outcome_class']}, highest post-YC round: {it['highest_post_yc_round']}; "
                  f"complexity {it['technical_complexity']}, takeover risk then {it['takeover_risk_then']}")
            print(f"      competitors then: {', '.join(it['competitors_then']) or 'none recorded'}")
            fx = it["failure_factors"] or it["success_factors"]
            print(f"      factors: {', '.join(fx)}")
            print(f"      why: {it['outcome_analysis'][:260]}")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
