# Backtest of the evaluator

Six companies from the calibration sample were forecast in summary mode as if it were the start of their YC batch, by agents told not to open the company's own record or search for its later fate. Each folder is in `evaluations/backtest-<slug>/`. Six is a small sample, so read the lessons as direction, not as measured error rates. The YC acceptance step cannot be tested this way, because every company in the sample got in.

## Forecast against outcome

| Company (batch) | Forecast: seed / A / B / C+ given the previous step | What happened | Verdict |
|---|---|---|---|
| Assorted Bits (S12) | 55% / 30% / 45% / 25%; shut down or stalled 72% | Shut down. No funding found. | Good. The stall call was right. |
| Termius (W19) | 75% / 28% / 35% / 40%; shut down or stalled 45% | Seed of $2.7M in 2019, still active with about 35 staff, no later round found. | Good. Seed yes, Series A no. |
| Scope AR (S15) | 82% / 45% / 35% / 25%; small exit 30% | Seeds, then a Series A in 2019, then a small undisclosed sale in 2026. | Good, but the exit took 11 years. |
| Yoshi Mobility (S16) | 78% / 38% / 40% / 35%; shut down or stalled 55% | Series A 2018, Series B 2020, Series C 2024, about $65M raised. | Too pessimistic at every step after seed. |
| Eden (S18) | 72% / 45% / 45% / 35%; shut down or stalled 55% | Pivoted to radiology software in 2021, then a Series A in 2025. | Right on A. The pivot was not forecastable. |
| Submittable (S12) | 65% / 30% / 45% / 40%; small exit 41% | Seed in 2012, Series A only in 2017, Series C in 2022, independent and profitable. | Too pessimistic on A, and the path skipped a Series B. |

## What the misses teach

1. **Discounts below the anchor were too harsh when the story sounded niche.** Submittable ("tiny market"), Yoshi ("asset heavy") and Eden (healthcare friction) all got Series A odds well under the cohort anchor, and all three reached a Series A. Termius, the one with a niche story that did not reach A, is the only support for the discount. Across the four companies that got a seed, the agents set Series A at 28% to 45% while the cohort anchors were 50% to 62%. Rule: do not set a step below 0.75 times its anchor unless a named analog shows the same fatal problem.
2. **Slow and profitable is a path.** Submittable took five years to its Series A and then skipped a Series B. Scope AR took eleven years to a small exit. The ladder asks about reaching a round, not when, and the report should say that reaching a round years later is common for companies with paying customers.
3. **Pivots drive upside.** Eden's growth came after a rebuild around a different product. Add a pivot-then-raise path to the upside band and do not treat the day-one description as the company.
4. **Boring B2B with paying customers survives longer than the odds suggest.** All four B2B companies were still alive or exited well after three years. The two that stalled or died were a consumer calendar app and a small developer tool.
5. **Small sample, wide uncertainty.** Probabilities for Series B and C+ could not be tested here, since only Yoshi reached them.

## Tooling findings

Three of six agents saw their own company's outcome by accident, through `yc_overlap.py`, which prints status and outcome. It now has `--exclude`, and the evaluator skill tells backtests to use it. `comps.py` and `base_rates.py` cohorts still include later outcomes of other companies, which is allowed, and `base_rates.py` includes the backtest company inside broad cohorts, a small effect. Two agents also noted that a cohort tag such as Consumer returned zero companies, so the industry field should be used instead of the tag.
