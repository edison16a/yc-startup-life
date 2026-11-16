"""Validation for enrichment records (docs/schema.md is the human-readable spec)."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import re
from common import (STAGES, EXIT_TYPES, FUNDING_COVERAGE, SUCCESS_FACTORS, FAILURE_FACTORS,
                    parse_date, batch_start, num)

REQ1 = ["slug", "depth", "target_customer", "problem", "business_model", "confidence"]
REQ2 = REQ1 + ["founded_year", "funding_data_coverage", "rounds", "exit", "founders",
               "competition_at_founding", "technical_complexity", "defensibility",
               "takeover_risk_then", "market_need_then", "pivots", "success_factors",
               "failure_factors", "outcome_analysis", "sources"]


def words(s):
    return len(re.findall(r"\w+", s or ""))


def rating_ok(v):
    return v is None or (isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 5)


NAME_TYPES = ["real_word", "invented", "compound", "descriptive", "acronym", "person_or_place", "suffix_coinage", "other"]
BRAND_EFFECTS = ["helped", "neutral", "hurt", "unclear"]


def validate_branding(b, err, warn):
    if not isinstance(b, dict):
        err.append("branding must be an object (see docs/schema.md)"); return
    if b.get("name_type") not in NAME_TYPES:
        err.append(f"branding.name_type must be one of {NAME_TYPES}")
    for k in ("name_qualities", "name_problems", "rebrands", "sources"):
        if not isinstance(b.get(k, []), list):
            err.append(f"branding.{k} must be a list")
    bs = b.get("brand_strength")
    if not isinstance(bs, dict) or not rating_ok(bs.get("rating")) or not bs.get("rationale"):
        err.append("branding.brand_strength needs rating (1-5 or null) and rationale")
    if b.get("brand_effect_on_outcome") not in BRAND_EFFECTS:
        err.append(f"branding.brand_effect_on_outcome must be one of {BRAND_EFFECTS}")
    elif b.get("brand_effect_on_outcome") != "unclear" and not b.get("sources"):
        warn.append("branding claims an effect on the outcome but lists no sources (use 'unclear' if unsupported)")
    if b.get("name_origin") and not b.get("sources"):
        warn.append("branding.name_origin has no supporting source")


def validate_record(e, row=None):
    """Return (errors, warnings). Errors block the merge; warnings are reported."""
    err, warn = [], []
    if not isinstance(e, dict):
        return ["record is not a JSON object"], []
    depth = e.get("depth")
    if depth not in (1, 2):
        err.append("depth must be 1 or 2")
        return err, warn
    for k in (REQ2 if depth == 2 else REQ1):
        if k not in e:
            err.append(f"missing key: {k}")
    if err:
        return err, warn
    for k in ("slug", "target_customer", "problem", "business_model"):
        if not isinstance(e[k], str) or not e[k].strip():
            err.append(f"{k} must be a non-empty string")
    if e["confidence"] not in ("high", "medium", "low"):
        err.append("confidence must be high|medium|low")
    if row is not None and e["slug"] != row["slug"]:
        err.append("slug does not match file / company")
    if depth == 1:
        return err, warn

    # ---- depth 2 ----
    if e["funding_data_coverage"] not in FUNDING_COVERAGE:
        err.append(f"funding_data_coverage must be one of {FUNDING_COVERAGE}")
    if e["founded_year"] is not None and not (isinstance(e["founded_year"], int) and 1990 <= e["founded_year"] <= 2100):
        err.append("founded_year must be an integer year or null")
    for k in ("rounds", "founders", "pivots", "success_factors", "failure_factors", "sources"):
        if not isinstance(e[k], list):
            err.append(f"{k} must be a list")
    if err:
        return err, warn
    if not e["sources"]:
        err.append("sources must list at least one URL")
    if words(e["outcome_analysis"]) < 25:
        err.append("outcome_analysis must be a paragraph (>= 25 words) on why this company succeeded, stalled or failed")
    if not isinstance(e["market_need_then"], str) or words(e["market_need_then"]) < 8:
        err.append("market_need_then must be a sentence or more on demand/need at the time of founding")

    bs = batch_start(row.get("batch")) if row else None

    for i, r in enumerate(e["rounds"]):
        if not isinstance(r, dict):
            err.append(f"rounds[{i}] not an object"); continue
        if r.get("stage") not in STAGES:
            err.append(f"rounds[{i}].stage must be one of {STAGES}")
        if r.get("date") not in (None, "") and parse_date(r.get("date")) is None:
            err.append(f"rounds[{i}].date must be YYYY, YYYY-MM or YYYY-MM-DD")
        for k in ("amount_usd", "post_money_usd"):
            if r.get(k) is not None and num(r.get(k)) is None:
                err.append(f"rounds[{i}].{k} must be a number or null")
        if r.get("valuation_basis") not in (None, "reported", "estimated"):
            err.append(f"rounds[{i}].valuation_basis must be reported|estimated|null")
        if not r.get("source_url"):
            warn.append(f"rounds[{i}] has no source_url")
        if r.get("post_money_usd") is not None and r.get("valuation_basis") is None:
            warn.append(f"rounds[{i}] has post_money_usd but no valuation_basis")

    ex = e["exit"]
    if not isinstance(ex, dict) or ex.get("type") not in EXIT_TYPES:
        err.append(f"exit.type must be one of {EXIT_TYPES}")
    else:
        if ex.get("date") not in (None, "") and parse_date(ex.get("date")) is None:
            err.append("exit.date must be YYYY, YYYY-MM or YYYY-MM-DD")
        if ex.get("amount_usd") is not None and num(ex.get("amount_usd")) is None:
            err.append("exit.amount_usd must be a number or null")
        if row:
            st, t = row.get("status"), ex.get("type")
            if st == "Inactive" and t not in ("shutdown", "unknown"):
                warn.append("directory says Inactive but exit.type is not shutdown/unknown")
            if st == "Acquired" and t not in ("acquisition", "merger", "unknown"):
                warn.append("directory says Acquired but exit.type is not acquisition/merger/unknown")
            if st == "Public" and t not in ("ipo", "spac", "unknown"):
                warn.append("directory says Public but exit.type is not ipo/spac/unknown")
            if st == "Inactive" and not e["failure_factors"]:
                warn.append("Inactive company with no failure_factors")

    for i, f in enumerate(e["founders"]):
        if not isinstance(f, dict) or not f.get("name"):
            err.append(f"founders[{i}] needs a name"); continue
        a = f.get("age_at_founding")
        if a is not None and (not isinstance(a, int) or not f.get("age_source")):
            err.append(f"founders[{i}]: age_at_founding must be an integer and needs age_source")

    caf = e["competition_at_founding"]
    if not isinstance(caf, dict) or "as_of" not in caf or not isinstance(caf.get("competitors"), list):
        err.append("competition_at_founding needs as_of (YYYY-MM) and a competitors list")
    else:
        asof = parse_date(caf.get("as_of"))
        if asof is None:
            err.append("competition_at_founding.as_of must be YYYY or YYYY-MM")
        elif bs and (asof - bs).days > 183:
            warn.append("competition_at_founding.as_of is more than 6 months after the batch start")
        for i, c in enumerate(caf["competitors"]):
            if not isinstance(c, dict) or not c.get("name"):
                err.append(f"competitors[{i}] needs a name"); continue
            sd = parse_date(c.get("source_date"))
            if sd is None:
                warn.append(f"competitors[{i}] ({c.get('name')}) has no source_date, so contemporaneousness is unverified")
            elif bs and (sd - bs).days > 548:
                warn.append(f"competitors[{i}] ({c.get('name')}) source is >18 months after the batch: may not reflect the time of founding")
            if not c.get("source_url"):
                warn.append(f"competitors[{i}] ({c.get('name')}) has no source_url")

    tc = e["technical_complexity"]
    if not isinstance(tc, dict) or not rating_ok(tc.get("rating")) or not tc.get("rationale"):
        err.append("technical_complexity needs rating (1-5 or null) and rationale")
    df = e["defensibility"]
    if not isinstance(df, dict) or not rating_ok(df.get("rating")) or not isinstance(df.get("moat_types"), list) or not df.get("rationale"):
        err.append("defensibility needs rating (1-5 or null), moat_types (list) and rationale")
    tr = e["takeover_risk_then"]
    if not isinstance(tr, dict) or not rating_ok(tr.get("rating")) or not isinstance(tr.get("incumbents"), list) or "outcome" not in tr:
        err.append("takeover_risk_then needs rating (1-5 or null), incumbents (list) and outcome")

    if "branding" in e:
        validate_branding(e["branding"], err, warn)
    else:
        warn.append("no branding block (required for new depth-2 records; see docs/schema.md)")

    for i, p in enumerate(e["pivots"]):
        if not isinstance(p, dict) or not p.get("to"):
            err.append(f"pivots[{i}] needs from/to/date")
    for k, allowed in (("success_factors", SUCCESS_FACTORS), ("failure_factors", FAILURE_FACTORS)):
        for c in e[k]:
            if c not in allowed:
                warn.append(f"{k}: unknown code '{c}' (see docs/taxonomy.md)")
    if e["confidence"] == "high":
        missing = []
        if e["funding_data_coverage"] == "none_found":
            missing.append("funding history")
        if not e["founders"]:
            missing.append("founders")
        if not e["competition_at_founding"].get("competitors"):
            missing.append("competitors at founding")
        if missing:
            warn.append("confidence is high but missing: " + ", ".join(missing))
    return err, warn
