"""Shared helpers for the YC startup engine scripts (stdlib only)."""
import csv, datetime, json, math, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
KNOW = ROOT / "knowledge"
CONFIG = json.loads((ROOT / "config.json").read_text())

STAGES = ["pre_seed", "seed", "series_a", "series_b", "series_c", "series_d_plus", "growth", "debt", "grant", "other"]
STAGE_RANK = {"pre_seed": 0, "seed": 1, "series_a": 2, "series_b": 3, "series_c": 4, "series_d_plus": 5, "growth": 5}
RANK_NAME = {1: "seed", 2: "series_a", 3: "series_b", 4: "series_c", 5: "series_d_plus"}
EXIT_TYPES = ["none", "acquisition", "merger", "ipo", "spac", "shutdown", "unknown"]
FUNDING_COVERAGE = ["complete", "partial", "none_found"]

SUCCESS_FACTORS = [
    "strong_pmf", "large_market_growth", "timing_tailwind", "distribution_advantage", "network_effects",
    "technical_moat", "regulatory_moat", "switching_costs", "proprietary_data", "founder_market_fit",
    "strong_team_execution", "capital_efficiency", "successful_pivot", "incumbent_weakness",
    "product_led_growth", "enterprise_sales_engine", "other",
]
FAILURE_FACTORS = [
    "no_market_need", "weak_willingness_to_pay", "market_too_small", "market_timing_early",
    "market_timing_late", "ran_out_of_money", "could_not_raise_next_round", "competition_won",
    "incumbent_copied", "platform_dependency", "regulatory_blocked", "unit_economics",
    "distribution_failed", "tech_unsolved", "scaling_failed", "founder_conflict", "pivot_failed",
    "acquihire_soft_landing", "fraud_or_legal", "macro_downturn", "other",
]

SEASON = {"winter": (1, 15), "spring": (4, 1), "summer": (6, 15), "fall": (9, 15)}


def parse_date(s):
    """YYYY, YYYY-MM or YYYY-MM-DD -> date (year only = July 1, month only = the 15th); else None."""
    if s is None or str(s).strip() == "":
        return None
    m = re.fullmatch(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", str(s).strip())
    if not m:
        return None
    y = int(m.group(1))
    mo = int(m.group(2) or 7)
    d = int(m.group(3) or (15 if m.group(2) else 1))
    try:
        return datetime.date(y, mo, d)
    except ValueError:
        return None


def batch_start(batch):
    m = re.match(r"(?i)\s*(winter|spring|summer|fall)\s+(\d{4})", batch or "")
    if not m:
        return None
    mo, d = SEASON[m.group(1).lower()]
    return datetime.date(int(m.group(2)), mo, d)


def months_between(a, b):
    if not a or not b:
        return None
    return round((b.year - a.year) * 12 + (b.month - a.month) + (b.day - a.day) / 30.4, 1)


def era(year):
    try:
        y = int(year)
    except (TypeError, ValueError):
        return "unknown"
    if y <= 2012:
        return "2005-2012"
    if y <= 2017:
        return "2013-2017"
    if y <= 2021:
        return "2018-2021"
    return "2022+"


def percentile(vals, p):
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    k = (len(v) - 1) * p
    lo, hi = math.floor(k), math.ceil(k)
    return v[lo] if lo == hi else v[lo] + (v[hi] - v[lo]) * (k - lo)


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    s = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - s) / d, (c + s) / d)


def load_companies():
    rows = {}
    with (DATA / "companies.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows[r["slug"]] = r
    return rows


def load_enrichment(min_depth=1):
    out = {}
    for p in sorted((DATA / "enrichment").glob("*.json")):
        try:
            e = json.loads(p.read_text())
            if int(e.get("depth", 1)) >= min_depth:
                out[e["slug"]] = e
        except Exception:
            continue
    return out


def load_unresearchable():
    p = DATA / "unresearchable.csv"
    if not p.exists():
        return {}
    with p.open(encoding="utf-8") as f:
        return {r["slug"]: r.get("reason", "") for r in csv.DictReader(f)}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def derive(e, row):
    """Computed facts for one researched company: timeline in months since batch start, highest post-YC round, outcome class."""
    bs = batch_start(row.get("batch"))
    rounds = []
    for r in e.get("rounds") or []:
        d = parse_date(r.get("date"))
        mo = months_between(bs, d)
        rounds.append({**r, "months_since_batch": mo,
                       "post_yc": None if mo is None else mo >= -1.0})
    post = [r for r in rounds if r.get("post_yc") and r.get("stage") in STAGE_RANK]
    highest = max((STAGE_RANK[r["stage"]] for r in post), default=0)
    first = {}
    for rank in range(1, 6):
        ms = [r["months_since_batch"] for r in post if STAGE_RANK[r["stage"]] >= rank]
        first[rank] = min(ms) if ms else None
    ex = e.get("exit") or {}
    exit_months = months_between(bs, parse_date(ex.get("date")))
    et = ex.get("type")
    status = row.get("status")
    if et in ("acquisition", "merger") or status == "Acquired":
        oc = "acquired"
    elif et in ("ipo", "spac") or status == "Public":
        oc = "public"
    elif et == "shutdown" or status == "Inactive":
        oc = "shutdown"
    else:
        oc = "alive"
    return {"rounds": rounds, "highest_post_yc_rank": highest, "first_months_by_rank": first,
            "exit_months": exit_months, "outcome_class": oc, "batch_start": bs}
