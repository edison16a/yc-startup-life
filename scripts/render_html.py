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


def sniff_image(data):
    """Return the image media type from magic bytes, or None if it is not a PNG, JPEG, GIF or WebP."""
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def fetch_logo(slug, url):
    """Return a data URI for the logo, cached in data/logo_cache/<slug>.img; None if unreachable or not an image."""
    if not url or not str(url).startswith("https://") or not re.fullmatch(r"[a-z0-9\-_.]+", slug):
        return None
    LOGO_CACHE.mkdir(parents=True, exist_ok=True)
    f = LOGO_CACHE / f"{slug}.img"
    old = LOGO_CACHE / f"{slug}.png"
    if not f.exists() and old.exists():
        old.rename(f)
    if not f.exists():
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "yc-startup-engine-report/1.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read(400_000)
            if len(data) < 100 or not sniff_image(data):
                return None
            f.write_bytes(data)
        except Exception:
            return None
    data = f.read_bytes()
    mt = sniff_image(data)
    return f"data:{mt};base64," + base64.b64encode(data).decode() if mt else None


def month_offset(d, start):
    m = months_between(start, d)
    return None if m is None else round(m, 1)


def clip(x, n=1400):
    x = (x or "").strip() if isinstance(x, str) else x
    return x if not isinstance(x, str) or len(x) <= n else x[: n - 1].rstrip() + "..."


def analog_detail(enr):
    """The researched facts shown when a company card is expanded. None if the company has no record yet."""
    if not enr:
        return None
    ex = enr.get("exit") or {}
    caf = enr.get("competition_at_founding") or {}
    br = enr.get("branding") or {}
    def rating(k):
        v = enr.get(k) or {}
        return {"rating": v.get("rating"), "text": clip(v.get("rationale") or v.get("outcome"), 500)}
    return {
        "depth": enr.get("depth"), "confidence": enr.get("confidence"), "funding_coverage": enr.get("funding_data_coverage"),
        "outcome": clip(enr.get("outcome_analysis")),
        "target_customer": clip(enr.get("target_customer"), 300), "business_model": clip(enr.get("business_model"), 200),
        "rounds": [{"date": r.get("date"), "stage": ROUND_STAGE_LABEL.get(r.get("stage"), "Round"), "amount": r.get("amount_usd"), "post": r.get("post_money_usd"),
                    "basis": r.get("valuation_basis"), "investors": (r.get("investors") or [])[:5], "url": r.get("source_url")} for r in (enr.get("rounds") or [])],
        "exit": {"type": ex.get("type"), "date": ex.get("date"), "acquirer": ex.get("acquirer"), "amount": ex.get("amount_usd"), "reason": clip(ex.get("reason"), 300), "url": ex.get("source_url")},
        "founders": [{"name": f.get("name"), "role": f.get("role"), "background": clip("; ".join(filter(None, [", ".join(f.get("prior_employers") or []), ", ".join(f.get("education") or [])])), 240)} for f in (enr.get("founders") or [])[:5]],
        "competitors_as_of": caf.get("as_of"),
        "competitors": [{"name": c.get("name"), "what": clip(c.get("what"), 200), "traction": clip(c.get("traction_then"), 200), "url": c.get("source_url")} for c in (caf.get("competitors") or [])[:6]],
        "market_need": clip(enr.get("market_need_then"), 500),
        "technical": rating("technical_complexity"), "defensibility": rating("defensibility"), "takeover": rating("takeover_risk_then"),
        "success": enr.get("success_factors") or [], "failure": enr.get("failure_factors") or [],
        "pivots": [{"date": p.get("date"), "to": clip(p.get("to"), 200), "why": clip(p.get("why"), 200)} for p in (enr.get("pivots") or [])[:4]],
        "brand": {"rating": (br.get("brand_strength") or {}).get("rating"), "origin": clip(br.get("name_origin"), 300), "signature": clip(br.get("brand_signature"), 200),
                  "effect": br.get("brand_effect_on_outcome"), "rebrands": [{"date": r.get("date"), "to": r.get("to")} for r in (br.get("rebrands") or [])[:3]]} if br else None,
        "notes": clip(enr.get("notes"), 900), "sources": [u for u in (enr.get("sources") or []) if isinstance(u, str)][:6],
    }


def analog_series(slug, a, row, enr, now, logos, want_logos):
    start = batch_start(row.get("batch")) if row else None
    name = (row or {}).get("name", slug)
    out = {"slug": slug, "name": name, "batch": (row or {}).get("batch", ""), "status": (row or {}).get("status", ""),
           "relevance": a.get("relevance", ""), "summary": a.get("outcome_summary", ""),
           "url": (row or {}).get("yc_url", ""), "logo": fetch_logo(slug, logos.get(slug)) if want_logos else None,
           "logo_url": logos.get(slug) if str(logos.get(slug) or "").startswith("https://") else None,
           "one_liner": (row or {}).get("one_liner", ""), "website": (row or {}).get("website", ""), "detail": analog_detail(enr),
           "valuation": [], "raised": [], "end": None, "has_record": bool(enr)}
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
    fallback = t in (None, "unknown", "none")  # no usable exit in the record: use the YC directory status, and say so
    end_m = max(exit_m if exit_m is not None else last, last)
    if t in ("acquisition", "merger") or (fallback and st == "Acquired"):
        kind = "acquired"
    elif t in ("ipo", "spac") or (fallback and st == "Public"):
        kind = "ipo"
    elif t == "shutdown" or (fallback and st == "Inactive"):
        kind = "dead"
    else:
        kind = "active"
    if kind == "active":
        nm = month_offset(now, start)
        out["end"] = {"kind": "active", "month": max(nm if nm is not None else last, last), "dated": True, "src": "record"}
    else:
        out["end"] = {"kind": kind, "month": end_m, "dated": exit_m is not None, "src": "directory" if fallback else "record"}
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
        "mode": inp["mode"], "startup": inp["startup"], "thresholds": evalcore.CFG["label_thresholds"], "headline": inp["narrative"]["headline"], "summary": inp["narrative"]["general_summary"],
        "yc": {**inp["yc_acceptance"], "label": comp["label_yc"]}, "stages": stages,
        "outcomes": [{"name": o["name"], "value": o.get("value_usd"), "failure": bool(o.get("is_failure")), "p_given_yc": o["p_given_yc"], "label_given_yc": o["label_given_yc"],
                      "p_today": o["p_from_today"], "label_today": o["label_from_today"]} for o in comp["outcomes"]],
        "outcomes_why": inp["outcomes"]["why_it_fails"], "most_likely": ml,
        "scores": {"need": inp["market_need_now"]["rating"], "technical": inp["technical_complexity"]["rating"],
                   "takeover": inp["takeover_risk"]["rating"], "brand": br["rating"]},
        "insights": {"need": inp["market_need_now"], "competition": inp["competition_now"], "technical": inp["technical_complexity"], "takeover": inp["takeover_risk"],
                     "brand": br, "deep_dive": dd},
        "roadmap": inp.get("roadmap", []), "pros": inp.get("pros", []), "cons": killers, "analogs": analogs,
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
