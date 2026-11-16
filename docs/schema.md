# Enrichment record schema (v2)

One file per company: `data/enrichment/<slug>.json`. `slug` matches `data/companies.csv` and the file name. Validate with
`python3 -I scripts/merge_enrichment.py --check data/enrichment/<slug>.json`.

Rules that apply to every field:
- **Never guess.** Use `null`, `[]` or `{}` for what you cannot find. Put every URL you relied on in `sources` (and in the `source_url` of the specific round or competitor).
- **Time accounting.** Every fact about the company's history carries a date. The analysis is "what was true when", not "what is true now".
- **Competition is dated.** `competition_at_founding` lists who competed **around the time of founding** (the YC batch), from sources dated then (launch coverage, early product pages, Web Archive snapshots, contemporaneous reviews). Competitors that emerged later do not belong there; record later entrants in `outcome_analysis` instead.
- **Unknown is not zero.** If you cannot find a funding history, say so with `funding_data_coverage`. Do not record "no rounds" unless sources support it.

```json
{
  "slug": "example",
  "depth": 2,
  "confidence": "medium",
  "target_customer": "who exactly pays",
  "problem": "the painful job, one or two sentences",
  "business_model": "B2B SaaS per seat | marketplace take rate | usage-based API | ...",
  "product_category": "free text category",
  "founded_year": 2018,

  "founders": [
    {"name": "Full Name", "role": "CEO", "prior_employers": ["Company A"], "education": ["School, degree or dropped out"],
     "technical": true, "previous_startups": ["Earlier startup (outcome)"],
     "age_at_founding": null, "age_source": null, "background_notes": "optional"}
  ],

  "funding_data_coverage": "complete | partial | none_found",
  "rounds": [
    {"stage": "seed", "date": "2018-09", "amount_usd": 2500000, "post_money_usd": 12000000,
     "valuation_basis": "reported | estimated | null", "investors": ["Fund X"], "source_url": "https://..."}
  ],
  "exit": {"type": "none | acquisition | merger | ipo | spac | shutdown | unknown", "date": "2023-05",
           "amount_usd": null, "acquirer": null, "reason": "for shutdowns, as stated by the company", "source_url": "https://..."},

  "competition_at_founding": {
    "as_of": "2018-03",
    "competitors": [
      {"name": "Competitor", "what": "what they did", "traction_then": "customers/revenue/users at the time",
       "funding_then": "raised by then", "source_date": "2018-02", "source_url": "https://..."}
    ]
  },
  "technical_complexity": {"rating": 3, "rationale": "what was hard for a small team at that time (1 trivial ... 5 research-grade)"},
  "defensibility": {"rating": 2, "moat_types": ["switching_costs"], "rationale": "why copying it was easy or hard (1 none ... 5 very strong)"},
  "takeover_risk_then": {"rating": 4, "incumbents": ["BigCo"], "outcome": "what the incumbents actually did (copied it? bought it? ignored it?) and when"},
  "market_need_then": "evidence of demand at the time of founding: pain, spend, complaints, regulation, technology shift",

  "branding": {
    "name_origin": "where the name comes from and why it was chosen, if a source says (else null)",
    "name_type": "real_word | invented | compound | descriptive | acronym | person_or_place | suffix_coinage | other",
    "name_qualities": ["short", "easy_to_spell", "easy_to_say", "evocative", "distinctive", "friendly_tone"],
    "name_problems": ["hard_to_spell", "generic", "confusable", "unpronounceable", "negative_connotation", "outgrown_by_pivot"],
    "domain_note": "how they got their domain (exact .com, prefix/suffix, bought for $X) with date, or null",
    "identity": {"logo": "short description", "mascot_or_character": null, "visual_style": "...", "voice_and_tone": "..."},
    "brand_signature": "the one memorable brand asset (mascot, phrase, color, community ritual), or null",
    "rebrands": [{"date": "2021-03", "from": "Old Name", "to": "New Name", "why": "reason, if sourced"}],
    "community_and_virality": "evidence people talk about, meme, wear or share the brand (merch, fan accounts, press on the brand itself), or null",
    "brand_strength": {"rating": 4, "rationale": "evidence for how strong the brand was at its peak and how much it helped or hurt (1 forgettable or damaging ... 5 iconic and a real driver of growth)"},
    "brand_effect_on_outcome": "helped | neutral | hurt | unclear",
    "sources": ["https://..."]
  },
  "pivots": [{"date": "2019-06", "from": "original idea", "to": "new idea", "why": "reason"}],
  "success_factors": ["strong_pmf"],
  "failure_factors": [],
  "outcome_analysis": "One paragraph (25+ words): why this company succeeded, stalled or failed, in terms of the factors above and the timeline.",
  "sources": ["https://..."],
  "notes": "caveats, conflicting sources"
}
```

## Field notes

| Field | Rule |
|---|---|
| `depth` | `2` = fully researched (the target for every company). `1` = text-only classification; allowed only with `target_customer`, `problem`, `business_model`, `confidence`, `sources`. |
| `rounds[].stage` | `pre_seed, seed, series_a, series_b, series_c, series_d_plus, growth, debt, grant, other`. Rounds before the batch start (more than a month before) are kept but flagged `post_yc: false` in the tables. YC's own standard deal is not a round; record it as `other` only if the amount is reported. |
| `rounds[].date` | `YYYY`, `YYYY-MM` or `YYYY-MM-DD`. |
| `valuation_basis` | `reported` = a source states the valuation; `estimated` = a source's estimate (e.g. a database); `null` = unknown. Never compute your own. |
| `funding_data_coverage` | `complete` = sources credibly cover the whole history (company states total raised, or a shutdown post-mortem, or full database entry); `partial` = some rounds known, others may be missing; `none_found` = no public funding info found. Needed to avoid mistaking missing data for failure. |
| `exit.type` | Must agree with the directory `status` (Inactive = shutdown, Acquired, Public) or explain the conflict in `notes`. |
| `age_at_founding` | Integer only if a source states age or birth year; `age_source` is then required. Never estimate. |
| `technical_complexity.rating` | 1 = a weekend of CRUD; 3 = standard engineering with some hard parts; 5 = research-grade or requires hardware/regulatory breakthroughs. Rate for the time of founding. |
| `defensibility.rating` | 1 = copyable in weeks; 5 = structurally hard to replicate (data, regulation, network effects, deep integration). |
| `takeover_risk_then.rating` | 1 = no one with resources cared; 5 = well-resourced players were already building or buying the same wedge. `outcome` records what really happened. |
| `confidence` | `high` = founders, competition and funding all sourced; `medium` = two of three; `low` otherwise. Merge warns if `high` is claimed with gaps. |
| `branding` | Required for new depth-2 records (older records get a merge warning until backfilled). Rate only what sources show: press about the brand, the company's own brand pages, founder interviews, community posts. `brand_strength` is 1-5 at the brand's peak; `brand_effect_on_outcome` is your judgment and must be `unclear` if no source supports a view. Never infer a name's origin: unknown is `null`. Name text features are computed separately by `scripts/name_features.py`, so do not spend research time counting letters. |
| `success_factors` / `failure_factors` | Codes from `docs/taxonomy.md`. Failure factors for companies that shut down or stalled; success factors for companies that raised well or exited. May be empty for companies with no clear story. |
