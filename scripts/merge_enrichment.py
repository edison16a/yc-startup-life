#!/usr/bin/env python3
"""Validate enrichment records, merge them with the directory data, and write analysis tables.

  python3 -I scripts/merge_enrichment.py            validate everything, write the CSV tables + coverage report
  python3 -I scripts/merge_enrichment.py --check data/enrichment/foo.json [...]   validate specific files (for researchers)

Outputs: data/companies_enriched.csv, data/rounds.csv, data/competitors.csv, data/founders.csv,
         knowledge/coverage.md, data/merge_warnings.txt. Exit code 1 if any record is invalid.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, collections, csv, datetime, json, pathlib, sys
from common import DATA, KNOW, load_companies, load_unresearchable, derive, STAGE_RANK, num
from schema import validate_record

ENR = DATA / "enrichment"


def j(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(str(x) for x in v if x not in (None, ""))
    return str(v)


def write_csv(path, header, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", nargs="+")
    a = ap.parse_args()
    companies = load_companies()

    if a.check:
        bad = 0
        for p in a.check:
            try:
                e = json.loads(pathlib.Path(p).read_text())
                err, warn = validate_record(e, companies.get(e.get("slug")))
                if e.get("slug") != pathlib.Path(p).stem:
                    err.append("file name must be <slug>.json")
                if e.get("slug") not in companies:
                    err.append("unknown slug (not in data/companies.csv)")
            except Exception as ex:
                err, warn = [f"unreadable: {ex}"], []
            for m in err:
                print(f"ERROR {p}: {m}")
            for m in warn:
                print(f"warn  {p}: {m}")
            if not err:
                print(f"ok    {p}")
            bad += bool(err)
        return 1 if bad else 0

    records, errors, warnings = {}, [], []
    for p in sorted(ENR.glob("*.json")):
        try:
            e = json.loads(p.read_text())
            row = companies.get(e.get("slug"))
            err, warn = validate_record(e, row)
            if e.get("slug") != p.stem or row is None:
                err.append("file name must equal slug and slug must exist in data/companies.csv")
        except Exception as ex:
            err, warn = [f"unreadable: {ex}"], []
        errors += [(p.name, m) for m in err]
        warnings += [(p.name, m) for m in warn]
        if not err:
            records[e["slug"]] = e

    base_cols = list(next(iter(companies.values())).keys())
    extra = ["depth", "confidence", "target_customer", "problem", "business_model", "product_category",
             "founded_year", "funding_data_coverage", "highest_post_yc_round", "n_rounds", "total_raised_known_usd",
             "months_to_seed", "months_to_series_a", "months_to_series_b", "months_to_series_c",
             "exit_type", "exit_date", "exit_amount_usd", "exit_months_since_batch", "outcome_class",
             "founder_count", "founder_names", "technical_founder_count", "any_prior_startup", "founder_ages",
             "competitors_at_founding", "competition_as_of", "technical_complexity", "defensibility",
             "takeover_risk_then", "market_need_then", "pivot_count", "success_factors", "failure_factors",
             "outcome_analysis", "sources"]
    rows_out, rounds, comps, founders = [], [], [], []
    rank_names = {v: k for k, v in STAGE_RANK.items() if k != "growth"}
    for slug, row in companies.items():
        e = records.get(slug)
        if not e:
            rows_out.append(dict(row)); continue
        r = dict(row)
        r.update({"depth": e["depth"], "confidence": e["confidence"], "target_customer": e["target_customer"],
                  "problem": e["problem"], "business_model": e["business_model"],
                  "product_category": e.get("product_category")})
        if e["depth"] == 2:
            d = derive(e, row)
            fs = e["founders"]
            ex = e["exit"]
            rr = d["rounds"]
            known = [num(x.get("amount_usd")) for x in rr if num(x.get("amount_usd")) is not None]
            r.update({
                "founded_year": e["founded_year"], "funding_data_coverage": e["funding_data_coverage"],
                "highest_post_yc_round": rank_names.get(d["highest_post_yc_rank"], "none") if d["highest_post_yc_rank"] else "none",
                "n_rounds": len(rr), "total_raised_known_usd": int(sum(known)) if known else "",
                "months_to_seed": d["first_months_by_rank"][1], "months_to_series_a": d["first_months_by_rank"][2],
                "months_to_series_b": d["first_months_by_rank"][3], "months_to_series_c": d["first_months_by_rank"][4],
                "exit_type": ex.get("type"), "exit_date": ex.get("date"), "exit_amount_usd": ex.get("amount_usd"),
                "exit_months_since_batch": d["exit_months"], "outcome_class": d["outcome_class"],
                "founder_count": len(fs), "founder_names": j([f.get("name") for f in fs]),
                "technical_founder_count": sum(1 for f in fs if f.get("technical") is True),
                "any_prior_startup": any(bool(f.get("previous_startups")) for f in fs),
                "founder_ages": j([f"{f['name']}: {f['age_at_founding']}" for f in fs if f.get("age_at_founding") is not None]),
                "competitors_at_founding": j([c.get("name") for c in e["competition_at_founding"]["competitors"]]),
                "competition_as_of": e["competition_at_founding"].get("as_of"),
                "technical_complexity": e["technical_complexity"].get("rating"),
                "defensibility": e["defensibility"].get("rating"),
                "takeover_risk_then": e["takeover_risk_then"].get("rating"),
                "market_need_then": e["market_need_then"], "pivot_count": len(e["pivots"]),
                "success_factors": j(e["success_factors"]), "failure_factors": j(e["failure_factors"]),
                "outcome_analysis": e["outcome_analysis"], "sources": j(e["sources"]),
            })
            for x in rr:
                rounds.append({"slug": slug, "stage": x.get("stage"), "date": x.get("date"),
                               "months_since_batch": x["months_since_batch"], "post_yc": x["post_yc"],
                               "amount_usd": x.get("amount_usd"), "post_money_usd": x.get("post_money_usd"),
                               "valuation_basis": x.get("valuation_basis"), "investors": j(x.get("investors")),
                               "source_url": x.get("source_url")})
            for c in e["competition_at_founding"]["competitors"]:
                comps.append({"slug": slug, "as_of": e["competition_at_founding"].get("as_of"), "name": c.get("name"),
                              "what": c.get("what"), "traction_then": c.get("traction_then"),
                              "funding_then": c.get("funding_then"), "source_date": c.get("source_date"),
                              "source_url": c.get("source_url")})
            for f in fs:
                founders.append({"slug": slug, "name": f.get("name"), "role": f.get("role"),
                                 "prior_employers": j(f.get("prior_employers")), "education": j(f.get("education")),
                                 "technical": f.get("technical"), "previous_startups": j(f.get("previous_startups")),
                                 "age_at_founding": f.get("age_at_founding"), "age_source": f.get("age_source")})
        rows_out.append(r)

    write_csv(DATA / "companies_enriched.csv", base_cols + extra, rows_out)
    write_csv(DATA / "rounds.csv", ["slug", "stage", "date", "months_since_batch", "post_yc", "amount_usd",
                                    "post_money_usd", "valuation_basis", "investors", "source_url"], rounds)
    write_csv(DATA / "competitors.csv", ["slug", "as_of", "name", "what", "traction_then", "funding_then",
                                         "source_date", "source_url"], comps)
    write_csv(DATA / "founders.csv", ["slug", "name", "role", "prior_employers", "education", "technical",
                                      "previous_startups", "age_at_founding", "age_source"], founders)
    (DATA / "merge_warnings.txt").write_text("\n".join(f"{f}: {m}" for f, m in warnings))

    # ---- coverage report ----
    unres = load_unresearchable()
    cal = []
    cp = DATA / "calibration_sample.csv"
    if cp.exists():
        cal = [r["slug"] for r in csv.DictReader(cp.open())]
    d2 = {s for s, e in records.items() if e["depth"] == 2}
    cov = collections.Counter(records[s]["funding_data_coverage"] for s in d2)
    conf = collections.Counter(records[s]["confidence"] for s in d2)
    ages = sum(1 for s in d2 for f in records[s]["founders"] if f.get("age_at_founding") is not None)
    ncomp = sum(len(records[s]["competition_at_founding"]["competitors"]) for s in d2)
    nround = sum(len(records[s]["rounds"]) for s in d2)
    cal_done = sum(1 for s in cal if s in d2 or s in unres)
    total = len(companies)
    KNOW.mkdir(exist_ok=True)
    (KNOW / "coverage.md").write_text(
        f"# Coverage report\n\nGenerated {datetime.date.today()}.\n\n"
        f"- Companies in directory: {total}\n"
        f"- Depth 2 (fully researched): {len(d2)} ({len(d2) / total:.1%})\n"
        f"- Marked unresearchable (with reason): {len(unres)}\n"
        f"- Remaining: {total - len(d2) - len(unres)}\n"
        f"- Calibration sample (unbiased base rates): {cal_done}/{len(cal)} done\n"
        f"- Funding data coverage among researched: complete {cov['complete']}, partial {cov['partial']}, none found {cov['none_found']}\n"
        f"- Funding rounds recorded: {nround}; competitors at founding recorded: {ncomp}\n"
        f"- Founders with a publicly sourced age: {ages}\n"
        f"- Confidence: high {conf['high']}, medium {conf['medium']}, low {conf['low']}\n"
        f"- Invalid records: {len(errors)}; warnings: {len(warnings)} (see data/merge_warnings.txt)\n")
    print((KNOW / "coverage.md").read_text())
    for f, m in errors:
        print(f"INVALID {f}: {m}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
