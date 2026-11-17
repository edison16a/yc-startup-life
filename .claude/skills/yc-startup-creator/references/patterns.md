# Patterns: winners versus failures

Sources: knowledge/tables/*.csv built from the calibration sample (663 companies, 662 fully researched, one marked unresearchable), scripts/base_rates.py with --calibration-only, and the advice notes in knowledge/advice/. Every figure below is from one of those. Sample sizes are given as n.

## Biases to keep in mind
Survivorship: dead companies leave fewer public traces, so their records are thinner. Aggregator coverage gaps: funding data coverage among the 662 researched is complete 14, partial 349, none found 299. Missing funding is not zero, so the tables report a lower, a known-only and an upper bound for every stage. Recent batches have unresolved outcomes: the directory shows 89 percent Active for the 2022+ era (n=3201) against 17 percent for 2005-2012 (n=460), so era comparisons mix age with quality. Industry and era are confounded. Causes of success and failure are the researcher's reading of sources, not measured. Advice notes are one partner's or one founder's reading of survivors.

## Outcome base rates
Calibration sample, n=663 in the directory: 453 Active (68 percent), 125 Inactive (19 percent), 83 Acquired (13 percent), 2 Public. Among the 662 researched, 115 shutdowns, 101 acquisitions, 445 alive, 1 public. Funding ladder (known-only, with the 95 percent interval): seed 77 percent (72 to 81), Series A 35 percent (30 to 40), Series B 15 percent (12 to 19), Series C 6 percent (4 to 8), Series D or later 2 percent (1 to 4). The upper bound for Series A is 64 percent, so the true value lies between 19 and 64 percent and the known-only figure is probably low. Conditional on the previous stage: A given seed 45 percent (n=279), B given A 44 percent (n=126), C given B 36 percent (n=55).

## What winners had in common
Success factors tagged in the records (share of 148 companies with a success tag, success_factor_counts.csv): founder market fit 34 percent (n=51), timing tailwind 26 percent (n=39), strong product market fit 22 percent (n=33), technical moat 15 percent (n=22), successful pivot 11 percent (n=16), enterprise sales engine, large market growth, capital efficiency and strong team execution about 8 to 9 percent each. Network effects (n=4) and proprietary data (n=2) are rare, so the folk wisdom about data and network moats is thinly supported here.

Defensibility is the strongest single separator in factor_outcomes.csv. Rated 1 (n=98): 50 percent shut down and 4 percent of those with known funding reached Series A. Rated 2 (n=395): 14 percent shut down, 30 percent reached A. Rated 3 (n=149): 5 percent shut down, 48 percent reached A, 23 percent reached B. Rated 4 (n=16): none shut down, 54 percent reached A. Ratings are the researcher's, which inflates the link to outcomes, but the gradient is steep.

Founders: technical founder true (n=488) shut down 14 percent against 28 percent when false (n=174). Prior startup experience made no difference to shutdown (17 percent both, n=230 and 432). Solo founders (n=102) shut down 21 percent, two founders (n=405) 17 percent, three (n=131) 13 percent. Pivoted companies (n=194) reached Series A 40 percent versus 32 percent for those that did not (n=468), among known funding.

Industry and model: Consumer (n=892) is 35 percent Inactive versus B2B 15 percent (n=3250), Fintech 14 percent (n=672), Healthcare 14 percent (n=713), Industrials 10 percent (n=515). Among models with n of 14 or more, enterprise (n=19) shut down 5 percent, usage-based (n=22) 5 percent, B2B (n=194) 10 percent, SaaS (n=22) 27 percent, consumer (n=41) 27 percent, freemium (n=19) 26 percent, marketplace (n=14) 43 percent, hardware (n=18) 28 percent. Model labels are free text and many have n of 1 to 3, so ignore those.

Competition at founding: zero competitors (n=380) shut down 18 percent, 1 to 2 (n=201) 15 percent, 3 to 5 (n=81) 19 percent. Competitor count alone barely moves outcomes, which matches Paul Graham's view that crowded markets are usually not fatal (note p1-pg-startup-ideas). Takeover risk rated 4 (n=199) reached Series A 27 percent versus 42 percent at rating 2 (n=163), among known funding.

Technical complexity: rating 3 (n=318) shut down 12 percent, rating 2 (n=174) 23 percent, rating 4 (n=118) 19 percent, rating 5 (n=41) 15 percent. Very easy products fail somewhat more, but the extremes have small n.

## What the failures had in common
Failure factors are covered in failure_modes.md. In short: running out of road without a next round, losing to a competitor, and unit economics together account for most tagged shutdowns, usually after about three to four years.

## Scoring rubric, 0 to 5 per criterion
Score each criterion from evidence. Zero means evidence of a fatal problem, 3 means plausible but unproven, 5 means strong direct evidence. Total out of 50 is a ranking aid, not a probability.

1. Pain severity. 0 nobody notices the problem. 1 mild annoyance. 2 real but tolerated. 3 recurring pain that people already work around with spreadsheets or staff. 4 costly and urgent for a named group. 5 customers have already asked, paid or built it themselves. Graham: build what you noticed, not brainstormed (p1-pg-startup-ideas).
2. Willingness to pay. 0 users expect free. 1 only ad or free models fit. 2 small payments from individuals. 3 a budget line exists but must be created. 4 buyers pay today for a worse solution. 5 paid pilots or prepaid contracts. Weak willingness to pay appears in 3 shutdowns, free models in the table shut down 43 percent (n=14).
3. Market size. 0 under a few million dollars ever. 2 a niche that could support a small business. 3 a niche with a believable path to a larger neighbor. 4 a large market with a narrow wedge. 5 a market that restructures an industry. Market too small appears in 3 shutdowns, so size matters but is rarely the cause.
4. Why now. 0 nothing changed. 2 mild trend. 3 one clear shift. 4 a shift plus a new cost curve. 5 a shift only the last year enabled. Timing tailwind is the second most common success tag (26 percent), market timing late appears in 1 shutdown.
5. Whitespace. Judge competition as of founding. 0 a dominant incumbent with the same product. 3 many weak or adjacent players. 5 nobody serves the buyer. Because competitor count has weak predictive power, weight whitespace by incumbent strength, not by count.
6. Wedge and moat. Use the defensibility gradient: 1 copyable in weeks (50 percent shut down), 2 some switching cost, 3 clear lock in or regulation or hard technology (5 percent shut down), 4 to 5 compounding data, network or licenses.
7. Small-team feasibility. 0 needs large capital before first revenue. 3 a team of two or three can ship and sell in six months. 5 one person can serve the first fifty customers. Hardware and regulated models score lower on average.
8. Distribution path. 0 no known channel. 2 paid ads only. 3 one repeatable channel guessed. 4 a channel the founders already control. 5 built in virality or an existing audience. Distribution failure appears in 4 shutdowns, and Graham says do things that do not scale first (p1-pg-dont-scale).
9. Technical complexity fit. Score fit to the team, not difficulty. 0 the team cannot build it. 3 they can build it with effort. 5 hard enough to be a head start and well within their skill. Technical founders shut down half as often as non-technical ones in this sample.
10. Takeover resistance. 0 an incumbent can copy it in a quarter and has the distribution. 3 incumbents would need to rebuild. 5 incumbents are structurally unable to copy. Takeover risk 4 or 5 reached Series A less often (27 and 17 percent versus 42 percent at 2), with small n at 5.

Calibration: the data cannot validate these weights. Treat scores of 8 or more on defensibility, willingness to pay and distribution as the best-supported.
