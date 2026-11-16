# judge.json

One per finalist at `runs/<run-id>/debate/<idea-slug>/judge.json`. `idea` equals the folder name.

```json
{
  "idea": "idea-slug",
  "verdict": "INVEST",
  "conviction": 8,
  "reasons": ["strongest reason 1", "reason 2", "reason 3"],
  "risks": ["risk 1", "risk 2", "risk 3"],
  "rubric_scores": {
    "pain_severity": 4, "willingness_to_pay": 4, "market_size": 3, "why_now": 5, "whitespace": 4,
    "wedge_moat": 3, "small_team_feasibility": 5, "distribution_path": 3,
    "technical_complexity_fit": 4, "takeover_resistance": 3
  },
  "cycle": 2,
  "hard_filters_checked": {"money_evidence": true, "size_arithmetic": true, "whitespace_evidence": true, "takeover_assessed": true},
  "sources_reverified": ["https://..."]
}
```

`verdict` is `INVEST`, `PASS` or `REVISE`. `conviction` is an integer 1-10, meaningful for INVEST. The rubric names are the defaults; use the ones in `knowledge/patterns.md` if they differ.
