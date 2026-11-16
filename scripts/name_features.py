#!/usr/bin/env python3
"""Name features for every YC company, joined to outcomes: the data side of the name skill.

  python3 -I scripts/name_features.py --write            data/name_features.csv (one row per company)
  python3 -I scripts/name_features.py --write-tables     knowledge/tables/name_outcomes.csv (outcome rates by name feature and era)
  python3 -I scripts/name_features.py --score "Capy"     features of a candidate name and how its feature cohorts did
  python3 -I scripts/name_features.py --score "Capy" --era 2022+

Everything here is computed from the name text alone. It is a screening aid, not a verdict: it cannot see logo,
mascot, voice, domain or story, which the per-company `branding` research records capture. Outcome proxies come
from the directory (status, YC's `top_company` flag), so they exist for all companies, not only researched ones.
Caveats the output repeats: status is survivorship-shaped, older batches have had longer to fail, and names
correlate with industry and era, so cohort rates are context and never causal.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, collections, csv, re
from common import DATA, KNOW, era, wilson, load_companies

VOWELS = set("aeiouy")
# Words that describe the product category. A name built from these is descriptive, not distinctive.
DESCRIPTIVE = {"ai", "labs", "lab", "health", "bio", "pay", "payments", "data", "cloud", "tech", "technologies", "systems",
               "software", "robotics", "analytics", "security", "finance", "financial", "capital", "medical", "therapeutics",
               "pharma", "energy", "solutions", "network", "networks", "platform", "digital", "mobile", "app", "apps",
               "hq", "io", "inc", "co", "works", "studio", "studios", "group", "intelligence", "automation"}
SUFFIXES = ["ify", "ly", "ium", "ia", "io", "ai", "ex", "ix", "ox", "zy", "ster", "hub", "base", "flow", "wise", "sync", "stack", "kit", "pad", "bit", "box"]


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    return max(n, 1)


def max_consonant_run(word):
    runs = re.findall(r"[^aeiouy]+", re.sub(r"[^a-z]", "", word.lower()))
    return max((len(r) for r in runs), default=0)


def common_words(rows, min_count=8):
    """English-ish vocabulary from the directory's own descriptions: no external word list needed."""
    c = collections.Counter()
    for r in rows:
        c.update(w for w in re.findall(r"[a-z]{3,}", (r["long_description"] + " " + r["one_liner"]).lower()))
    return {w for w, n in c.items() if n >= min_count}


def features(name, vocab):
    raw = name.strip()
    clean = re.sub(r"\.(com|io|ai|co|app|dev|so|sh|fm|ly|xyz)$", "", raw, flags=re.I)
    tokens = [t for t in re.split(r"[\s\-_.]+", re.sub(r"(?<=[a-z])(?=[A-Z])", " ", clean)) if t]
    alpha = re.sub(r"[^A-Za-z]", "", clean).lower()
    n_words = len(tokens)
    syl = sum(syllables(t) for t in tokens)
    low_tokens = [t.lower() for t in tokens]
    descriptive_hits = [t for t in low_tokens if t in DESCRIPTIVE]
    is_real_word = n_words == 1 and alpha in vocab
    ends_suffix = next((s for s in SUFFIXES if n_words == 1 and len(alpha) > len(s) + 2 and alpha.endswith(s)), "")
    if descriptive_hits and len(descriptive_hits) == n_words:
        kind = "descriptive"
    elif n_words >= 2 and any(t in vocab for t in low_tokens) and not descriptive_hits:
        kind = "compound_words"
    elif descriptive_hits:
        kind = "name_plus_descriptor"
    elif is_real_word:
        kind = "real_word"
    elif ends_suffix:
        kind = "suffix_coinage"
    else:
        kind = "invented_or_proper"
    length = len(alpha)
    return {
        "chars": length,
        "words": n_words,
        "syllables": syl,
        "length_bucket": "<=4" if length <= 4 else "5-6" if length <= 6 else "7-8" if length <= 8 else "9-11" if length <= 11 else "12+",
        "syllable_bucket": "1" if syl <= 1 else "2" if syl == 2 else "3" if syl == 3 else "4+",
        "has_digit": int(bool(re.search(r"\d", raw))),
        "has_hyphen_or_dot": int(bool(re.search(r"[-.]", clean))),
        "camel_case": int(bool(re.search(r"[a-z][A-Z]", clean))),
        "all_caps": int(raw.isupper() and len(alpha) > 1),
        "max_consonant_run": max_consonant_run(alpha),
        "vowel_ratio": round(sum(ch in VOWELS for ch in alpha) / length, 2) if length else 0,
        "repeated_letter_pair": int(bool(re.search(r"(.)\1", alpha))),
        "ends_with_suffix": ends_suffix,
        "kind": kind,
        "descriptor_words": ";".join(descriptive_hits),
    }


FEATURE_COLUMNS = ["kind", "length_bucket", "syllable_bucket", "words", "has_digit", "has_hyphen_or_dot", "camel_case", "ends_with_suffix"]


def build(rows):
    vocab = common_words(rows)
    out = []
    for r in rows:
        f = features(r["name"], vocab)
        out.append({"slug": r["slug"], "name": r["name"], "batch_year": r["batch_year"], "era": era(r["batch_year"]),
                    "status": r["status"], "top_company": r["top_company"], **f})
    return out, vocab


def rates(group):
    n = len(group)
    alive = sum(1 for g in group if g["status"] != "Inactive")
    exited = sum(1 for g in group if g["status"] in ("Acquired", "Public"))
    top = sum(1 for g in group if g["top_company"] == "True")
    lo, hi = wilson(alive, n)
    return {"n": n, "alive_pct": round(100 * alive / n, 1), "alive_ci": f"{round(100*lo)}-{round(100*hi)}" if lo is not None else "",
            "exit_pct": round(100 * exited / n, 1), "top_pct": round(100 * top / n, 1)}


def write_tables(feats):
    KNOW.joinpath("tables").mkdir(parents=True, exist_ok=True)
    out = KNOW / "tables" / "name_outcomes.csv"
    cols = ["era", "feature", "value", "n", "alive_pct", "alive_ci", "exit_pct", "top_pct"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for e in ["all"] + sorted({x["era"] for x in feats if x["era"] != "unknown"}):
            pool = [x for x in feats if (e == "all" or x["era"] == e) and x["slug"] != "y-combinator"]
            for col in FEATURE_COLUMNS:
                by = collections.defaultdict(list)
                for x in pool:
                    by[str(x[col])].append(x)
                for val, g in sorted(by.items()):
                    if len(g) >= 15:
                        w.writerow({"era": e, "feature": col, "value": val, **rates(g)})
    print(f"wrote {out}")


def score(name, feats, vocab, want_era):
    f = features(name, vocab)
    print(f"Name: {name}")
    for k in ("chars", "words", "syllables", "kind", "ends_with_suffix", "descriptor_words", "max_consonant_run", "vowel_ratio", "has_digit", "has_hyphen_or_dot", "camel_case"):
        print(f"  {k}: {f[k]}")
    flags = []
    if f["chars"] > 11: flags.append("long (12+ chars): harder to say, type and remember")
    if f["syllables"] >= 4: flags.append("4+ syllables")
    if f["max_consonant_run"] >= 4: flags.append("hard consonant cluster: check it is pronounceable aloud")
    if f["has_digit"]: flags.append("contains a digit: spelling and voice-search ambiguity")
    if f["has_hyphen_or_dot"]: flags.append("hyphen or dot in the name")
    if f["kind"] == "descriptive": flags.append("purely descriptive: hard to own, hard to trademark")
    if f["kind"] == "name_plus_descriptor": flags.append("distinctive part carries a category word (Labs, AI, Health...): fine, but the descriptor is not part of the brand")
    print("  flags: " + ("; ".join(flags) if flags else "none from the text screen"))
    pool = [x for x in feats if x["slug"] != "y-combinator" and (not want_era or x["era"] == want_era)]
    print(f"\nCohort context (era: {want_era or 'all'}). alive% = not shut down, exit% = acquired or public, top% = YC top-company flag.")
    for col in ("kind", "length_bucket", "syllable_bucket"):
        g = [x for x in pool if str(x[col]) == str(f[col])]
        if len(g) >= 15:
            r = rates(g)
            base = rates(pool)
            print(f"  {col}={f[col]}: n={r['n']} alive {r['alive_pct']}% (95% CI {r['alive_ci']}), exit {r['exit_pct']}%, top {r['top_pct']}%   [all: alive {base['alive_pct']}%, exit {base['exit_pct']}%, top {base['top_pct']}%]")
    print("\nCaveat: name-only cohorts are confounded with industry and era and are survivorship-shaped. Use them to catch outliers, not to pick winners.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--write-tables", action="store_true")
    ap.add_argument("--score")
    ap.add_argument("--era", default=None, help="2005-2012 | 2013-2017 | 2018-2021 | 2022+")
    a = ap.parse_args()
    rows = list(load_companies().values())
    feats, vocab = build(rows)
    if a.write:
        out = DATA / "name_features.csv"
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(feats[0].keys()))
            w.writeheader(); w.writerows(feats)
        print(f"wrote {out} ({len(feats)} rows)")
    if a.write_tables:
        write_tables(feats)
    if a.score:
        score(a.score, feats, vocab, a.era)
    if not (a.write or a.write_tables or a.score):
        ap.print_help()


if __name__ == "__main__":
    main()
