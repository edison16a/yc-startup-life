# evaluation_input.json

Created by `scripts/new_eval.py`; turned into `EVALUATION.md` by `scripts/render_eval.py`. See `docs/eval-input-template.json` for the full shape. The agent supplies judgments; the scripts compute cumulative odds, labels and the report, and reject inconsistent input.

## Top level
`mode` (`full` | `summary`), `startup`, `yc_acceptance`, `ladder`, `outcomes`, `analogs`, `killers`, `competition_now`, `technical_complexity`, `takeover_risk`, `market_need_now`, `roadmap`, `pros`, `brand`, `narrative`, `assumptions`, `sources`.

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

## `brand`

Required in both modes. Comes from the `yc-name-creator` skill in evaluate mode. `name`; `rating` (integer 1-5, 5 = iconic and a real growth driver); `effect_on_success` (`helps | neutral | hurts | unclear`); `name_check` (the `scripts/name_features.py --score` command run and its headline result); `strengths[]`; `weaknesses[]` (at least one in full mode); `rationale` (30+ words full, 12+ summary, citing past YC brand cases where relevant); `better_names[]` (optional). Brand is a factor in success but a secondary one: a weak name rarely sinks a good company, so it moves the ladder only through the stated adjustment reasons.

## `pros`

The honest strengths, shown in green on the report's Pros and cons tab (the cons are the `killers`). At least 3 in full mode, 2 in summary mode. Each has `point`, `evidence` and, where possible, `source_url`. Do not pad: a weak startup has few real pros.

## `roadmap`

What to do to reach each step, shown on the report's Roadmap tab and linked from the end of the Walkthrough. Each entry: `phase` (`before_yc`, `seed`, `series_a`, `series_b`, `series_c_plus`; the phase is the step you are trying to reach), `goal` (what must be true), `actions` (2 or more concrete actions, ordered), `proof` (the number or event that shows it worked). Full mode covers all five phases, summary mode at least two. Base each phase on the killers and the `why_it_fails` paragraph for that step: the roadmap is how to avoid that failure.
