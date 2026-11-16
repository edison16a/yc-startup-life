#!/usr/bin/env python3
"""Write <dir>/report.html: one standalone, animated HTML report for an evaluation.

  python3 -I scripts/render_html.py evaluations/<name> [--no-logos]

Reads evaluation_input.json, recomputes the odds with evalcore, joins each analog with its researched record
(data/enrichment/<slug>.json) and directory row, and fills scripts/report_template.html. The output has no
external dependencies: data, styles, scripts and (when reachable) company logos are embedded. Logos are fetched
once from the public YC directory image URLs and embedded as data URIs; if a logo cannot be fetched the page falls
back to a letter badge, and the remote URL is kept so it shows when the file is opened online.
Never edit report.html by hand: edit evaluation_input.json and re-run render_eval.py (it calls this script).
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import base64, csv, datetime, json, re, urllib.request
import evalcore
from common import ROOT, DATA, KNOW, load_companies, parse_date, batch_start, months_between

TEMPLATE = _pl.Path(__file__).resolve().parent / "report_template.html"
DEFAULT_MONTHS = {"seed": 8, "series_a": 26, "series_b": 44, "series_c_plus": 66}  # months after YC, used only if no table/override
STAGE_TITLE = evalcore.STAGE_TITLE
LOGO_CACHE = ROOT / "data" / "logo_cache"
ROUND_STAGE_LABEL = {"pre_seed": "Pre-seed", "seed": "Seed", "series_a": "Series A", "series_b": "Series B", "series_c": "Series C",
                     "series_d_plus": "Series D+", "growth": "Growth", "debt": "Debt", "grant": "Grant", "other": "Other"}


def load_raw_logos():
    p = DATA / "raw" / "yc_all.json"
    if not p.exists():
        return {}
    return {x["slug"]: x.get("small_logo_thumb_url") for x in json.loads(p.read_text())}


def fetch_logo(slug, url):
    """Return a data URI for the logo, using data/logo_cache/<slug>.png; None if unreachable."""
    if not url:
        return None
    LOGO_CACHE.mkdir(parents=True, exist_ok=True)
    f = LOGO_CACHE / f"{slug}.png"
    if not f.exists():
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "yc-startup-engine-report/1.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = r.read(400_000)
            if len(data) < 100:
                return None
            f.write_bytes(data)
        except Exception:
            return None
    return "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode()


def month_offset(d, start):
    m = months_between(start, d)
    return None if m is None else round(m, 1)


def analog_series(slug, a, row, enr, now, logos, want_logos):
    start = batch_start(row.get("batch")) if row else None
    name = (row or {}).get("name", slug)
    out = {"slug": slug, "name": name, "batch": (row or {}).get("batch", ""), "status": (row or {}).get("status", ""),
           "relevance": a.get("relevance", ""), "summary": a.get("outcome_summary", ""),
           "url": (row or {}).get("yc_url", ""), "logo": fetch_logo(slug, logos.get(slug)) if want_logos else None,
           "logo_url": logos.get(slug), "valuation": [], "raised": [], "end": None, "has_record": bool(enr)}
    if not start:
        return out
    cum = 0.0
    rounds = sorted((r for r in (enr or {}).get("rounds", []) if parse_date(r.get("date"))), key=lambda r: parse_date(r["date"]))
    for r in rounds:
        m = max(0.0, month_offset(parse_date(r["date"]), start))
        lab = ROUND_STAGE_LABEL.get(r.get("stage"), "Round")
        if isinstance(r.get("amount_usd"), (int, float)):
            cum += r["amount_usd"]
            out["raised"].append([m, cum, lab])
        if isinstance(r.get("post_money_usd"), (int, float)):
            out["valuation"].append([m, r["post_money_usd"], lab])
    last = max([p[0] for p in out["valuation"] + out["raised"]] or [0.0])
    ex = (enr or {}).get("exit") or {}
    t, st = ex.get("type"), (row or {}).get("status")
    exit_m = month_offset(parse_date(ex.get("date")), start) if ex.get("date") else None
    if t in ("acquisition", "merger") or (t in (None, "unknown", "none") and st == "Acquired"):
        out["end"] = {"kind": "acquired", "month": max(exit_m if exit_m is not None else last, last), "dated": exit_m is not None}
    elif t in ("ipo", "spac") or (t in (None, "unknown", "none") and st == "Public"):
        out["end"] = {"kind": "ipo", "month": max(exit_m if exit_m is not None else last, last), "dated": exit_m is not None}
    elif t == "shutdown" or (t in (None, "unknown", "none") and st == "Inactive"):
        out["end"] = {"kind": "dead", "month": max(exit_m if exit_m is not None else last, last), "dated": exit_m is not None}
    else:
        out["end"] = {"kind": "active", "month": max(month_offset(now, start) or last, last), "dated": True}
    return out


def most_likely(comp):
    """Where the company most likely stops if accepted into YC, from the stage-reach probabilities."""
    cums = [1.0] + [s["p_stage_given_yc"] for s in comp["stages"]]
    names = ["No priced round"] + [STAGE_TITLE[s["stage"]] for s in comp["stages"]]
    stop = [cums[i] - (cums[i + 1] if i + 1 < len(cums) else 0.0) for i in range(len(cums))]
    k = max(range(len(stop)), key=lambda i: stop[i])
    credible = max([i for i in range(1, len(cums)) if cums[i] >= 0.20] or [0])
    def band(i):
        if i == 0:
            return None
        bs = comp["stages"][i - 1]["bands"]
        b = max(bs, key=lambda b: b["p_band"])
        return {"raise": b["raise_usd"], "post": b["post_money_usd"], "p_band": b["p_band"]}
    return {"stop_index": k, "stop_name": names[k], "stop_p": stop[k], "stop_dist": [{"name": n, "p": p} for n, p in zip(names, stop)],
            "stop_band": band(k), "credible_index": credible, "credible_name": names[credible], "credible_p": cums[credible], "credible_band": band(credible)}


def build_data(inp, comp, want_logos=True):
    companies = load_companies()
    logos = load_raw_logos()
    enr = {}
    for a in inp["analogs"]:
        p = DATA / "enrichment" / f"{a['slug']}.json"
        enr[a["slug"]] = json.loads(p.read_text()) if p.exists() else None
    as_of = parse_date(inp["startup"].get("as_of")) or datetime.date.today()
    analogs = [analog_series(a["slug"], a, companies.get(a["slug"]), enr[a["slug"]], as_of, logos, want_logos) for a in inp["analogs"][:10]]
    months = {st["stage"]: st.get("months_after_yc") or DEFAULT_MONTHS[st["stage"]] for st in inp["ladder"]}
    stages = []
    for st, raw in zip(comp["stages"], inp["ladder"]):
        stages.append({"key": st["stage"], "title": STAGE_TITLE[st["stage"]], "months": months[st["stage"]],
                       "p_reach_prev": st["p_reach_given_prev"], "p_given_yc": st["p_stage_given_yc"], "label_given_yc": st["label_stage_given_yc"],
                       "p_today": st["p_stage_from_today"], "label_today": st["label_stage_from_today"], "why": raw["why_it_fails"],
                       "anchor": raw["anchors"], "bands": [{"raise": b["raise_usd"], "post": b["post_money_usd"], "p_band": b["p_band"], "p_given_yc": b["p_given_yc"],
                                                          "label": b["label_given_yc"], "rationale": b["rationale"]} for b in st["bands"]]})
    ml = most_likely(comp)
    killers = sorted(inp["killers"], key=lambda k: -k["p"])
    killers = [{**k, "analog_names": [(companies.get(a) or {}).get("name", a) for a in k["analogs"]]} for k in killers]
    dd = (inp["narrative"].get("deep_dive") or {})
    total = len(analogs)
    dead = sum(1 for a in analogs if (a["end"] or {}).get("kind") == "dead")
    acq = sum(1 for a in analogs if (a["end"] or {}).get("kind") in ("acquired", "ipo"))
    br = inp["brand"]
    return {
        "mode": inp["mode"], "startup": inp["startup"], "headline": inp["narrative"]["headline"], "summary": inp["narrative"]["general_summary"],
        "yc": {**inp["yc_acceptance"], "label": comp["label_yc"]}, "stages": stages,
        "outcomes": [{"name": o["name"], "value": o.get("value_usd"), "failure": bool(o.get("is_failure")), "p_given_yc": o["p_given_yc"], "label_given_yc": o["label_given_yc"],
                      "p_today": o["p_from_today"], "label_today": o["label_from_today"]} for o in comp["outcomes"]],
        "outcomes_why": inp["outcomes"]["why_it_fails"], "most_likely": ml,
        "scores": {"need": inp["market_need_now"]["rating"], "technical": inp["technical_complexity"]["rating"],
                   "takeover": inp["takeover_risk"]["rating"], "brand": br["rating"]},
        "insights": {"need": inp["market_need_now"], "competition": inp["competition_now"], "technical": inp["technical_complexity"], "takeover": inp["takeover_risk"],
                     "brand": br, "deep_dive": dd},
        "pros": inp.get("pros", []), "cons": killers, "analogs": analogs,
        "comp_summary": {"total": total, "dead": dead, "exited": acq, "active": total - dead - acq},
        "assumptions": inp["assumptions"], "sources": inp["sources"],
    }


def render_html(inp, comp, want_logos=True):
    data = build_data(inp, comp, want_logos)
    blob = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = TEMPLATE.read_text(encoding="utf-8")
    title = f"{data['startup']['name']}: YC evaluation"
    return html.replace("/*__TITLE__*/", re.sub(r"[<>&]", "", title)).replace("/*__DATA__*/", blob)


def main():
    args = [a for a in _sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__); return 1
    d = _pl.Path(args[0])
    inp = evalcore.load_input(d)
    err, _ = evalcore.validate(inp)
    if err:
        for e in err:
            print("ERROR:", e)
        return 1
    comp = evalcore.compute(inp)
    out = d / "report.html"
    out.write_text(render_html(inp, comp, "--no-logos" not in _sys.argv), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
