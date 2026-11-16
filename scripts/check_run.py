#!/usr/bin/env python3
"""Check that a creator run is complete and its verdict stands up. Exit 0 = OK.

  python3 -I scripts/check_run.py runs/<run-id>

Complete = FINAL.md has every required section AND the idea it presents has a judge record
(debate/<idea>/judge.json) with verdict INVEST and conviction >= min_conviction, a passing full evaluation in
<run>/evaluation/, and the investor/doubter/evidence files; OR state.json says "cap_reached" and FINAL.md is
labelled "best found".
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import json
from common import CONFIG
import check_eval

CFG = CONFIG["creator"]
SECTIONS = [
    "One-liner and verdict", "Customer and pain", "Why now", "Product and MVP scope",
    "Pricing and business model", "Market size (bottom-up)", "Competition and whitespace evidence",
    "Technical complexity and takeover risk", "Fit with YC patterns", "Funding outlook (evaluator)",
    "Name and brand", "Go-to-market", "Founder profile needed", "First 30 days: experiments", "Risks",
    "Investor / Doubter / Judge summary", "Runners-up and why they lost", "YC application draft",
    "Research limits", "Sources",
]
JUDGE_KEYS = {"idea", "verdict", "conviction", "reasons", "risks", "rubric_scores", "cycle"}


def main():
    if len(_sys.argv) != 2:
        print(__doc__); return 1
    run = _pl.Path(_sys.argv[1])
    problems = []
    final = run / "FINAL.md"
    if not final.exists():
        print("FINAL.md missing"); return 1
    text = final.read_text()
    for s in SECTIONS:
        if f"## {s}" not in text:
            problems.append(f"FINAL.md missing section: ## {s}")
    judges = []
    for p in sorted((run / "debate").glob("*/judge.json")):
        try:
            j = json.loads(p.read_text())
            miss = JUDGE_KEYS - set(j)
            if miss:
                problems.append(f"{p}: missing keys {sorted(miss)}")
            judges.append(j)
        except Exception as e:
            problems.append(f"{p}: unreadable ({e})")
    if not judges:
        problems.append("no debate/*/judge.json records found")
    try:
        state = json.loads((run / "state.json").read_text())
    except Exception:
        state = {}
        problems.append("state.json missing or unreadable")
    winners = [j for j in judges if j.get("verdict") == "INVEST" and int(j.get("conviction", 0)) >= CFG["min_conviction"]]
    if winners:
        top = max(winners, key=lambda j: int(j["conviction"]))
        print(f"winning idea: {top['idea']} (conviction {top['conviction']})")
        if top["idea"].lower() not in text.lower():
            problems.append("FINAL.md does not mention the winning idea by name")
        for sub in ("investor.md", "doubter.md"):
            if not (run / "debate" / top["idea"] / sub).exists():
                problems.append(f"debate/{top['idea']}/{sub} missing")
        if not (run / "evidence" / f"{top['idea']}.md").exists():
            problems.append(f"evidence/{top['idea']}.md missing")
        hf = top.get("hard_filters_checked") or {}
        if not all(hf.get(k) for k in ("money_evidence", "size_arithmetic", "whitespace_evidence", "takeover_assessed")):
            problems.append("judge.json hard_filters_checked must be true for money_evidence, size_arithmetic, whitespace_evidence, takeover_assessed")
        problems += [f"evaluation: {p}" for p in check_eval.check(run / "evaluation")]
    elif state.get("status") == "cap_reached":
        if "best found" not in text.lower():
            problems.append("cap reached but FINAL.md is not labelled 'best found'")
    else:
        problems.append(f"no INVEST verdict with conviction >= {CFG['min_conviction']} and cap not reached: keep going")
    for p in problems:
        print("PROBLEM:", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    _sys.exit(main())
