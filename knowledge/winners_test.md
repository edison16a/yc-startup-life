# Winners test: 117 blind forecasts on 2026 YC companies

## What was done

I picked 97 companies from the Winter, Spring, Summer and Fall 2026 batches that our own records showed with a post YC round above $1M from a press, company or investor source, plus 20 ordinary 2026 companies with no such round as a guard. The guard matters because tuning on winners alone only teaches an evaluator to be optimistic. Each company was forecast blind by an agent running the evaluator in summary mode, as if it were the first day of the batch. The agent saw only the name, one liner, description, tags and team size. Separate agents then looked up what each company actually raised. Files are in `evaluations/winners-2026/` (one folder per company, plus `_test/` with the pool, truth, leak log, scores and both prompts). The scorer is `scripts/winners_score.py`.

## What went wrong and how it was handled

- The first launch leaked. `comps.py --exclude` takes a space separated list, so repeating the flag silently kept only the last slug and several forecasters saw their own company's record, including a raise. All outputs from that launch were deleted. `comps.py` and `yc_overlap.py` now accept repeated flags, and during the test they read `data/test_blocklist.txt` (removed again afterwards).
- Even after the fix, 17 forecasts are flagged: web searches about the market returned pages naming the company, or the description copied from the live YC page stated a raise. Forecasts with a flag had a mean seed probability of 0.71 against 0.63 for the rest, so a leak that the agent says it ignored still moves the number. Scores below are given for all forecasts and for the 100 without flags; trust the second.
- The ground truth is thinner than hoped. The first pass used one search per company. A second pass of 44 companies was more careful in one batch (9 confirmed as YC deal only) and admitted to 1 to 2 searches in the other, so I counted only its upgrades to a confirmed raise and ignored its "nothing found" claims. Final truth: 77 confirmed raises, 13 confirmed YC deal only, 27 unresolved. Alive status was taken from the YC directory and not checked.
- 20 of the 97 pool companies (21 percent) were not confirmed as raising above $1M after their batch started. Five were confirmed YC deal only and several had rounds dated before the batch. So rounds above $1M in our 2026 records, when they rest on databases, are wrong or misdated about one time in five.

## Results

| Measure | All 117 | 100 without leak flags |
|---|---|---|
| Confirmed raised / confirmed none / unresolved | 77 / 13 / 27 | 63 / 12 / 25 |
| Mean seed probability, raised | 0.65 | 0.63 |
| Mean seed probability, confirmed none | 0.62 | 0.62 |
| Area under the curve, raised against none | 0.59 | 0.53 |
| Share of confirmed raises landing in some forecast band | 90% | 87% |
| Median actual raise over the central band midpoint | 2.0 | 1.8 |

Reading: the seed probabilities carry no demonstrable skill. Companies that raised and companies that did not got almost the same number. That is a small test (13 confirmed negatives), so it shows no evidence of skill and does not prove there is none. On size, the confirmed raises had median $6.0M, with quartiles $4.3M and $10M. The forecasts put about 40 percent of their probability below $3M, where only 11 percent of real rounds fell, and 19 percent in the $6M to $12M range, where 42 percent fell. Higher seed probabilities did go with bigger rounds (median $9.0M in the top third against $5.2M in the bottom third).

Selection caveat: winners were chosen because a press source reported a round, and press covers large rounds more than small ones. The true median seed for all 2026 companies is lower than $6.0M, and we cannot tell by how much from this sample.

## What was changed

Only the evaluator skill (`.claude/skills/yc-startup-evaluator/SKILL.md`, section "Calibration rules from the 2026 winners test"):

1. Stop lifting seed odds above the cohort anchor for team size or traction claims, capped at 1.25 times without a named analog.
2. State the time window and use the time to milestone table when a window is claimed.
3. Split seed bands into the YC deal only, a small round under $3M and an institutional seed, because the benchmark seed row mixes them.
4. A band shape for AI native companies with a live product and a team of 8 or more (20 / 35 / 30 / 15 percent over $3M, $3M to $6M, $6M to $12M and above $12M).
5. Blind test hygiene (blocklist, strip funding language from inputs, drop flagged runs).

Not changed: the overall stage odds and the knowledge tables. A uniform 1.5 times shift on all bands was tested by splitting the confirmed raises in half 300 times; it gained only 0.04 on held out halves and 2 times made things worse, so no blanket rescale was applied.

## What this test cannot tell us

- Whether the evaluator discriminates, until there are more confirmed negatives. The next test should draw a random sample of 2026 companies without choosing winners and spend the research on confirming what each one raised.
- Anything about Series A and later steps. No company here has had time to reach them.
- Whether the changes help. The rules were fitted on this set, so the next check must use new companies.

## Round 2: a random held-out sample (120 companies)

Design: 20 random companies from each of six batches (Winter 2025 to Spring 2026), none from round 1, with the live page text stripped of any sentence about funding or investors. Each was forecast blind with the tuned evaluator and a stated window from its batch start to 2026-11-17, where seed means an outside round above $1M that closes inside the window. Twelve verification agents then ran at least four searches per company. Of 120 outcomes, 19 are confirmed raises above $1M, 49 are confirmed no raise beyond the YC deal, and 52 are unresolved (mostly low confidence). A second reading counts low confidence "nothing found" as no raise (82 no raise, 19 unresolved). Nine forecasts were flagged for web leaks and dropped from the clean scores. Files are in `evaluations/winners-r2/` and `_test/`.

| Measure | Confirmed only | Low confidence counted as no raise |
|---|---|---|
| Raised / none (clean, no leak flags) | 15 / 47 | 15 / 78 |
| Mean seed probability | 0.42 | 0.41 |
| Actual rate | 0.24 | 0.16 |
| Area under the curve, raised against none | 0.74 | 0.77 |
| Brier score | 0.198 | 0.183 |
| Brier of a constant guess at the sample rate | 0.183 | 0.135 |
| Raised in the low, mid and high probability bins | 0%, 25%, 35% | 0%, 17%, 29% |

Reading: the ranking is better than round 1 (area under the curve 0.74 to 0.77 against 0.59) and the bins rise steadily, so the odds do carry some signal. The level is too high, and without a correction the Brier score is no better than a constant guess. Raise sizes were forecast well: all 19 raises fell in a band and the median raise was 0.97 times the central band midpoint.

Change made: a 0.6 multiplier on the windowed seed probability (rule 6 in the skill). Chosen on this same sample, it beat no correction in 85 percent of random half splits and moves the Brier score below the constant guess (0.171 against 0.183 confirmed only; 0.1325 against 0.1353 in the lenient reading). It must be checked on a new sample.

Limits: only 15 to 19 confirmed raises, so every number here has wide uncertainty. 52 outcomes are unresolved and companies this young may raise later. Sizes are judged on raises that press covered. Web leaks were reduced, not removed: market searches still returned pages dated after a batch start, and I counted only ones naming the company. Series A and later steps still cannot be tested.
