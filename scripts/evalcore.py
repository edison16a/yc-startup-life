"""Evaluation engine: validate an evaluation_input.json, compute the cumulative odds and labels, render EVALUATION.md.

The agent supplies judgments (conditional probabilities, bands, prose). This module does the arithmetic and the
labelling so the written report cannot contradict its own numbers.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import datetime, json
from common import CONFIG, load_companies, parse_date
from schema import words

CFG = CONFIG["evaluator"]
STAGE_TITLE = {"seed": "Seed", "series_a": "Series A", "series_b": "Series B", "series_c_plus": "Series C+"}
DEEP_KEYS = ["market_need", "competition", "technical_complexity", "takeover", "economics_and_distribution", "team", "yc_specific"]
DEEP_TITLE = {"market_need": "Is there real need today?", "competition": "Competition now, and what competition looked like for the analogs",
              "technical_complexity": "Technical complexity", "takeover": "Likelihood another company takes it over",
              "economics_and_distribution": "Unit economics and distribution", "team": "Team and founder-market fit",
              "yc_specific": "Why YC may say no"}


def label(p):
    for t in sorted(CFG["label_thresholds"], key=lambda t: -t["min"]):
        if p >= t["min"]:
            return t["label"]
    return CFG["label_thresholds"][-1]["label"]


def usd(x):
    if x is None:
        return "n/a"
    if x >= 1e9:
        return f"${x / 1e9:.2f}".rstrip("0").rstrip(".") + "B"
    if x >= 1e6:
        return f"${x / 1e6:.2f}".rstrip("0").rstrip(".") + "M"
    return f"${x / 1e3:.0f}K"


def rng(r):
    if not r:
        return "n/a"
    return usd(r[0]) if r[0] == r[1] else f"{usd(r[0])}–{usd(r[1])}"


def pf(p):
    if 0 < p < 0.001:
        return "<0.1%"
    return f"{p * 100:.0f}%" if p >= 0.10 else f"{p * 100:.1f}%"


def isnum(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def prob_ok(x):
    return isnum(x) and 0 <= x <= 1


def pair_ok(r):
    return isinstance(r, list) and len(r) == 2 and all(isnum(v) and v >= 0 for v in r) and r[0] <= r[1]


def validate(inp, slugs=None):
    """Return (errors, warnings). slugs = set of valid company slugs for analog checks (default: from the directory)."""
    err, warn = [], []
    slugs = slugs if slugs is not None else set(load_companies())
    mode = inp.get("mode")
    if mode not in ("full", "summary"):
        return ["mode must be 'full' or 'summary'"], warn
    full = mode == "full"
    mw = CFG["min_why_fail_words"]

    s = inp.get("startup") or {}
    for k in ("name", "one_liner", "description"):
        if not isinstance(s.get(k), str) or not s[k].strip():
            err.append(f"startup.{k} missing")
    if parse_date(s.get("as_of")) is None:
        err.append("startup.as_of must be a date (YYYY-MM-DD)")

    yc = inp.get("yc_acceptance") or {}
    if not all(prob_ok(yc.get(k)) for k in ("p", "p_low", "p_high")):
        err.append("yc_acceptance needs p, p_low, p_high in [0,1]")
    elif not yc["p_low"] <= yc["p"] <= yc["p_high"]:
        err.append("yc_acceptance: need p_low <= p <= p_high")
    elif yc["p"] > 0.15:
        warn.append("yc_acceptance.p above 15%: YC's overall acceptance rate is low, so justify this in basis")
    if words(yc.get("basis")) < 25:
        err.append("yc_acceptance.basis must explain the estimate (>= 25 words): published acceptance rate, adjustments")
    if words(yc.get("why_it_fails")) < mw:
        err.append(f"yc_acceptance.why_it_fails must be a paragraph of >= {mw} words")

    lad = inp.get("ladder")
    want = CFG["ladder_stages"]
    if not isinstance(lad, list) or [x.get("stage") for x in lad] != want:
        err.append(f"ladder must list exactly these stages in order: {want}")
        lad = []
    for st in lad:
        n = st["stage"]
        if not prob_ok(st.get("p_reach_given_prev")):
            err.append(f"{n}: p_reach_given_prev must be in [0,1]")
        an = st.get("anchors") or {}
        if not an.get("source"):
            err.append(f"{n}: anchors.source required (e.g. the base_rates.py command and result used)")
        br = an.get("base_rate")
        if br is not None and not prob_ok(br):
            err.append(f"{n}: anchors.base_rate must be in [0,1] or null")
        elif br and prob_ok(st.get("p_reach_given_prev")) and st["p_reach_given_prev"] > 0:
            ratio = st["p_reach_given_prev"] / br
            lim = CFG["anchor_ratio_limit"]
            if (ratio > lim or ratio < 1 / lim) and words(an.get("adjustment_reason")) < CFG["min_adjustment_words"]:
                err.append(f"{n}: p_reach_given_prev differs from the base-rate anchor by more than {lim}x; "
                           f"anchors.adjustment_reason needs >= {CFG['min_adjustment_words']} words")
        if br is None and words(an.get("adjustment_reason")) < CFG["min_adjustment_words"]:
            err.append(f"{n}: no base-rate anchor, so anchors.adjustment_reason must explain where the number comes from")
        bands = st.get("bands")
        if not isinstance(bands, list) or not bands:
            err.append(f"{n}: bands required"); continue
        tot = 0
        for i, b in enumerate(bands):
            if not pair_ok(b.get("raise_usd")) or not pair_ok(b.get("post_money_usd")):
                err.append(f"{n}.bands[{i}]: raise_usd and post_money_usd must be [low, high] dollar pairs")
            elif b["post_money_usd"][0] < b["raise_usd"][0]:
                err.append(f"{n}.bands[{i}]: post-money cannot be below the raise")
            if not prob_ok(b.get("p_band")):
                err.append(f"{n}.bands[{i}]: p_band must be in [0,1]")
            else:
                tot += b["p_band"]
            if words(b.get("rationale")) < 8:
                err.append(f"{n}.bands[{i}]: rationale too short")
        if abs(tot - 1) > 0.02:
            err.append(f"{n}: band probabilities sum to {tot:.2f}, must be 1.00 (bands partition the outcomes if the stage is reached)")
        if words(st.get("why_it_fails")) < mw:
            err.append(f"{n}: why_it_fails must be a paragraph of >= {mw} words")

    out = inp.get("outcomes") or {}
    ob = out.get("bands")
    if not isinstance(ob, list) or len(ob) < 2:
        err.append("outcomes.bands needs at least 2 bands")
    else:
        tot, nfail = 0, 0
        for i, b in enumerate(ob):
            if not b.get("name") or not prob_ok(b.get("p")):
                err.append(f"outcomes.bands[{i}] needs name and p in [0,1]")
            else:
                tot += b["p"]
            if b.get("is_failure"):
                nfail += 1
            elif not pair_ok(b.get("value_usd")):
                err.append(f"outcomes.bands[{i}]: non-failure bands need value_usd [low, high]")
        if abs(tot - 1) > 0.02:
            err.append(f"outcomes band probabilities sum to {tot:.2f}, must be 1.00")
        if nfail != 1:
            err.append("outcomes.bands: exactly one band must have is_failure true (shuts down or stalls)")
    if words(out.get("why_it_fails")) < mw:
        err.append(f"outcomes.why_it_fails must be a paragraph of >= {mw} words")

    an = inp.get("analogs")
    min_an = 5 if full else 3
    if not isinstance(an, list) or len(an) < min_an:
        err.append(f"analogs needs at least {min_an} past YC companies (use scripts/comps.py)")
    else:
        for i, a in enumerate(an):
            if a.get("slug") not in slugs:
                err.append(f"analogs[{i}]: '{a.get('slug')}' is not a company in data/companies.csv")
            if not a.get("relevance") or not a.get("outcome_summary"):
                err.append(f"analogs[{i}] needs relevance and outcome_summary")

    ks = inp.get("killers")
    min_k = CFG["min_killers_full"] if full else CFG["min_killers_summary"]
    if not isinstance(ks, list) or len(ks) < min_k:
        err.append(f"killers needs at least {min_k} entries")
    else:
        for i, k in enumerate(ks):
            if not k.get("risk") or not prob_ok(k.get("p")) or words(k.get("evidence")) < 10 or not k.get("mitigation"):
                err.append(f"killers[{i}] needs risk, p in [0,1], evidence (>=10 words) and mitigation")
            al = k.get("analogs")
            if not isinstance(al, list) or not al or any(a not in slugs for a in al):
                err.append(f"killers[{i}]: analogs must be a non-empty list of real company slugs")

    cn = inp.get("competition_now")
    if not isinstance(cn, list) or len(cn) < (3 if full else 1) or any(not (c.get("name") and c.get("what") and c.get("source_url")) for c in cn):
        err.append(f"competition_now needs at least {3 if full else 1} competitors, each with name, what, source_url")
    for key, extra in (("technical_complexity", None), ("takeover_risk", "who"), ("market_need_now", "evidence")):
        d = inp.get(key) or {}
        if not (isinstance(d.get("rating"), int) and 1 <= d["rating"] <= 5):
            err.append(f"{key}.rating must be an integer 1-5")
        if key != "market_need_now" and words(d.get("rationale")) < 20:
            err.append(f"{key}.rationale must be >= 20 words")
    if not (inp.get("takeover_risk") or {}).get("who"):
        err.append("takeover_risk.who must list the companies/platforms that could absorb or copy this")
    if not isnum((inp.get("takeover_risk") or {}).get("timeline_months")):
        err.append("takeover_risk.timeline_months must be a number (how fast a well-resourced rival could ship a substitute)")
    ev = (inp.get("market_need_now") or {}).get("evidence")
    if not isinstance(ev, list) or len(ev) < (2 if full else 1) or any(not (x.get("claim") and x.get("source_url")) for x in ev):
        err.append("market_need_now.evidence needs claims each with a source_url")

    pros = inp.get("pros")
    if not isinstance(pros, list) or len(pros) < (3 if full else 2) or any(not (x.get("point") and x.get("evidence")) for x in pros):
        err.append(f"pros needs at least {3 if full else 2} items, each with point and evidence (the honest strengths, with sources where possible)")
    br = inp.get("brand")
    if not isinstance(br, dict):
        err.append("brand block missing (name and brand assessment from the yc-name-creator skill; see docs/eval-input-schema.md)")
    else:
        if not (isinstance(br.get("rating"), int) and 1 <= br["rating"] <= 5):
            err.append("brand.rating must be an integer 1-5")
        if not br.get("name"):
            err.append("brand.name missing")
        if words(br.get("rationale")) < (30 if full else 12):
            err.append(f"brand.rationale must be >= {30 if full else 12} words")
        if not br.get("name_check"):
            err.append("brand.name_check must record the scripts/name_features.py --score command run and its headline result")
        if full and (not isinstance(br.get("weaknesses"), list) or not br["weaknesses"]):
            err.append("brand.weaknesses must list at least one concrete weakness in full mode")
        if br.get("effect_on_success") not in ("helps", "neutral", "hurts", "unclear"):
            err.append("brand.effect_on_success must be helps|neutral|hurts|unclear")

    nar = inp.get("narrative") or {}
    if not nar.get("headline"):
        err.append("narrative.headline missing")
    if words(nar.get("general_summary")) < 80:
        err.append("narrative.general_summary must be >= 80 words")
    if full:
        dd = nar.get("deep_dive") or {}
        for k in DEEP_KEYS:
            if words(dd.get(k)) < 60:
                err.append(f"narrative.deep_dive.{k} must be >= 60 words")
    if not inp.get("assumptions"):
        err.append("assumptions must list at least one")
    if not isinstance(inp.get("sources"), list) or len(inp["sources"]) < (3 if full else 1):
        err.append("sources needs more URLs")
    return err, warn


def compute(inp):
    p_yc = inp["yc_acceptance"]["p"]
    cum, stages = 1.0, []
    for st in inp["ladder"]:
        cum *= st["p_reach_given_prev"]
        bands = []
        for b in st["bands"]:
            g = cum * b["p_band"]
            bands.append({**b, "p_given_yc": g, "label_given_yc": label(g),
                          "p_from_today": p_yc * g, "label_from_today": label(p_yc * g)})
        stages.append({"stage": st["stage"], "p_reach_given_prev": st["p_reach_given_prev"],
                       "p_stage_given_yc": cum, "label_stage_given_yc": label(cum),
                       "p_stage_from_today": p_yc * cum, "label_stage_from_today": label(p_yc * cum), "bands": bands})
    ob = inp["outcomes"]["bands"]
    others = sum(b["p"] for b in ob if not b.get("is_failure"))
    outs = []
    for b in ob:
        fy = b["p"]
        ft = (1 - p_yc * others) if b.get("is_failure") else p_yc * b["p"]
        outs.append({**b, "p_given_yc": fy, "label_given_yc": label(fy), "p_from_today": ft, "label_from_today": label(ft)})
    return {"p_yc": p_yc, "label_yc": label(p_yc), "stages": stages, "outcomes": outs}


def render(inp, comp, companies=None):
    companies = companies if companies is not None else load_companies()
    s, yc = inp["startup"], inp["yc_acceptance"]
    full = inp["mode"] == "full"
    L = [f"# Evaluation: {s['name']}", "",
         f"*As of {s['as_of']}. Mode: {inp['mode']}. {s['one_liner']}*", "",
         "> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. "
         "Read the anchors table and the assumptions before relying on any number.", "",
         "## Verdict at a glance", "", f"**{inp['narrative']['headline']}**", "",
         f"**Chance of getting into YC:** {pf(yc['p'])} (range {pf(yc['p_low'])}–{pf(yc['p_high'])}), {comp['label_yc'].lower()}.", "",
         f"Labels use these cut-offs: " + ", ".join(f"{t['label']} ≥ {t['min']:.0%}" for t in sorted(CFG["label_thresholds"], key=lambda t: -t['min'])[:-1])
         + f", otherwise {CFG['label_thresholds'][-1]['label']}. "
         "\"If in YC\" assumes acceptance; \"from today\" multiplies by the YC odds and ignores funding paths outside YC.", "",
         "| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |", "|---|---|---|---|---|---|---|"]
    for st in comp["stages"]:
        for b in st["bands"]:
            L.append(f"| {STAGE_TITLE[st['stage']]} | {rng(b['raise_usd'])} | {rng(b['post_money_usd'])} | {pf(b['p_given_yc'])} | "
                     f"{b['label_given_yc']} | {pf(b['p_from_today'])} | {b['label_from_today']} |")
    L += ["", "## General assessment", "", inp["narrative"]["general_summary"].strip(), "",
          "## Round by round: where and why it fails", "",
          f"### Getting into YC: {pf(yc['p'])}", "", f"**How we got the number.** {yc['basis'].strip()}", "",
          f"**Why it fails here.** {yc['why_it_fails'].strip()}", ""]
    for st, raw in zip(comp["stages"], inp["ladder"]):
        L += [f"### {STAGE_TITLE[st['stage']]}: P(reach this round | in YC) = {pf(st['p_reach_given_prev'])}"
              f" after the previous step; {pf(st['p_stage_given_yc'])} cumulative if in YC; {pf(st['p_stage_from_today'])} from today", "",
              "| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |",
              "|---|---|---|---|---|---|---|---|"]
        for b in st["bands"]:
            L.append(f"| {rng(b['raise_usd'])} | {rng(b['post_money_usd'])} | {pf(b['p_band'])} | {pf(b['p_given_yc'])} | "
                     f"{b['label_given_yc']} | {pf(b['p_from_today'])} | {b['label_from_today']} | {b['rationale'].strip()} |")
        L += ["", f"**Why it fails here.** {raw['why_it_fails'].strip()}", ""]
    L += ["### Final outcomes", "", "| Outcome | Value | P if in YC | Label | P from today | Label |", "|---|---|---|---|---|---|"]
    for b in comp["outcomes"]:
        L.append(f"| {b['name']} | {rng(b.get('value_usd')) if not b.get('is_failure') else 'n/a'} | {pf(b['p_given_yc'])} | "
                 f"{b['label_given_yc']} | {pf(b['p_from_today'])} | {b['label_from_today']} |")
    L += ["", f"**Why it fails here.** {inp['outcomes']['why_it_fails'].strip()}", ""]

    L += ["## Why this company may not work: the killers", "",
          "| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |", "|---|---|---|---|---|---|"]
    for i, k in enumerate(sorted(inp["killers"], key=lambda k: -k["p"]), 1):
        names = ", ".join(f"{companies[a]['name']} ({a})" if a in companies else a for a in k["analogs"])
        L.append(f"| {i} | {k['risk']} | {pf(k['p'])} | {k['evidence'].strip()} | {names} | {k['mitigation'].strip()} |")
    L.append("")
    if full:
        L += ["## Deep dive", ""]
        for k in DEEP_KEYS:
            L += [f"### {DEEP_TITLE[k]}", "", inp["narrative"]["deep_dive"][k].strip(), ""]
    tr, tc, mn = inp["takeover_risk"], inp["technical_complexity"], inp["market_need_now"]
    L += ["## Scorecard", "",
          "| Factor | Rating (1-5) | Notes |", "|---|---|---|",
          f"| Market need today (5 = urgent, paid) | {mn['rating']} | {len(mn['evidence'])} sourced evidence items |",
          f"| Technical complexity (5 = very hard) | {tc['rating']} | {tc['rationale'].strip()} |",
          f"| Name and brand (5 = iconic, drives growth; effect on success: {inp['brand']['effect_on_success']}) | {inp['brand']['rating']} | {inp['brand']['name']}: {inp['brand']['rationale'].strip()} |",
          f"| Takeover/copy risk (5 = very likely) | {tr['rating']} | Could be built or absorbed by {', '.join(tr['who'])} within ~{tr['timeline_months']:g} months. {tr['rationale'].strip()} |", "",
          "### Competition today", "", "| Competitor | What they do | Traction | Source |", "|---|---|---|---|"]
    for c in inp["competition_now"]:
        L.append(f"| {c['name']} | {c['what']} | {c.get('traction', 'unknown')} | {c['source_url']} |")
    L += ["", "### Demand evidence", ""] + [f"- {x['claim']} ({x['source_url']})" for x in mn["evidence"]]
    L += ["", "## Evidence from past YC companies", "", "| Company | Batch | Directory status | Why it is relevant | What happened |", "|---|---|---|---|---|"]
    for a in inp["analogs"]:
        c = companies.get(a["slug"], {})
        L.append(f"| {c.get('name', a['slug'])} ({a['slug']}) | {c.get('batch', '')} | {c.get('status', '')} | {a['relevance']} | {a['outcome_summary']} |")
    L += ["", "### Base-rate anchors", "", "| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |", "|---|---|---|---|---|"]
    for raw in inp["ladder"]:
        an = raw["anchors"]
        L.append(f"| {STAGE_TITLE[raw['stage']]} | {pf(an['base_rate']) if an.get('base_rate') is not None else 'none'} | "
                 f"{pf(raw['p_reach_given_prev'])} | {an['source']} | {(an.get('adjustment_reason') or '').strip()} |")
    L += ["", "## Assumptions and limits", ""] + [f"- {a}" for a in inp["assumptions"]]
    L += ["", "## Sources", ""] + [f"- {u}" for u in inp["sources"]] + [""]
    return "\n".join(L)


def load_input(d):
    return json.loads((_pl.Path(d) / "evaluation_input.json").read_text())
