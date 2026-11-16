# evaluation_input.json

Created by `scripts/new_eval.py`; turned into `EVALUATION.md` by `scripts/render_eval.py`. See `docs/eval-input-template.json` for the full shape. The agent supplies judgments; the scripts compute cumulative odds, labels and the report, and reject inconsistent input.

## Top level
`mode` (`full` | `summary`), `startup`, `yc_acceptance`, `ladder`, `outcomes`, `analogs`, `killers`, `competition_now`, `technical_complexity`, `takeover_risk`, `market_need_now`, `narrative`, `assumptions`, `sources`.

## Probabilities
- `yc_acceptance.p`: chance this startup is accepted to YC (with `p_low`, `p_high`).
- `ladder[]`: stages `seed, series_a, series_b, series_c_plus` in order. `p_reach_given_prev` is the chance of reaching that round **given the previous step** (seed is conditional on being in YC).
- `ladder[].bands[]`: how the round could look **if reached**: `raise_usd [lo, hi]`, `post_money_usd [lo, hi]`, `p_band`. Band probabilities per stage must sum to 1.00 (include a thin or down-round band).
- `ladder[].anchors`: `base_rate` (from `scripts/base_rates.py` for the closest cohort), `source` (the command and result), `adjustment_reason` (required if our probability is more than 2x from the base rate, or there is no base rate).
- `outcomes.bands[]`: partition of final results: exactly one with `is_failure: true` (shuts down or stalls), the others with `value_usd [lo, hi]`. They sum to 1.00.

## Computed by the scripts
Cumulative odds if in YC and from today, and the labels (cut-offs in `config.json`). "From today" multiplies by the YC odds and ignores funding paths outside YC.

## Required prose (checked for length)
`why_it_fails` paragraph (45+ words) for the YC step, every stage and the outcomes; `killers[]` (5+ in full mode) each with evidence, real analog slugs and a mitigation; `narrative.general_summary`; in full mode, `narrative.deep_dive` sections: `market_need, competition, technical_complexity, takeover, economics_and_distribution, team, yc_specific`.

## Analogs
Every `analogs[].slug` and every slug in `killers[].analogs` must exist in `data/companies.csv`. Find them with `scripts/comps.py`.
