# Stage benchmarks: round sizes, valuations and timing

Built on 2026-11-17 from knowledge/tables/round_benchmarks.csv, time_to_milestones.csv, a base_rates.py run with --calibration-only, the YC deal note in knowledge/advice/p1-yc-standard-deal.md, and two public market reports cited below. Every dollar figure from the YC data is the median (p50) of rounds we found for researched companies. Read the caveats section before using any number.

## Post YC funding ladder (calibration sample, 663 companies, 662 researched)

The base_rates.py run reports each stage as lower bound, known only, and upper bound, because funding coverage is incomplete (complete 14, partial 349, none found 299). Seed was reached by 42 percent at the lower bound, 77 percent known only, 87 percent upper bound. Series A: 19, 35 and 64 percent. Series B: 8, 15 and 53 percent. Series C: 3, 6 and 48 percent. Series D or later: 1, 2 and 46 percent. The known only column is biased low where records are missing, and the upper column is biased high. The truth sits between them, and the wide gap at later stages is a statement about our coverage, not about startups. Conditional rates among those known to have the previous stage: seed 77 percent (n=363), A 45 percent (n=279), B 44 percent (n=126), C 36 percent (n=55), D plus 40 percent (n=20).

## Round sizes by era of the round

Amounts are US dollars. Era is the year the round closed, not the YC batch year.

| Stage | Era | n | p25 | p50 | p75 |
|---|---|---|---|---|---|
| Seed | 2005-2012 | 7 | 0.475M | 1.1M | 1.2M |
| Seed | 2013-2017 | 31 | 1.5M | 2.1M | 2.5M |
| Seed | 2018-2021 | 64 | 1.675M | 2.55M | 4.525M |
| Seed | 2022+ | 99 | 2.8M | 4.1M | 6.5M |
| Series A | 2005-2012 | 3 | 3.5M | 6.0M | 9.95M |
| Series A | 2013-2017 | 16 | 5.675M | 7.0M | 10.0M |
| Series A | 2018-2021 | 41 | 8.0M | 10.0M | 15.0M |
| Series A | 2022+ | 52 | 10.0M | 14.15M | 20.25M |
| Series B | 2013-2017 | 8 | 12.25M | 22.0M | 27.0M |
| Series B | 2018-2021 | 16 | 17.25M | 29.0M | 37.0M |
| Series B | 2022+ | 22 | 25.0M | 37.0M | 57.0M |
| Series C | 2013-2017 | 2 | 65M | 80M | 95M |
| Series C | 2018-2021 | 6 | 52.5M | 63.75M | 73.1M |
| Series C | 2022+ | 9 | 35M | 45M | 52.5M |
| Series D plus | 2018-2021 | 3 | 101M | 150M | 575M |
| Series D plus | 2022+ | 6 | 71M | 97.5M | 225M |

Series B and later in older eras have n under 10 and should be treated as anecdotes. No series B exists for 2005-2012 in the table.

## Valuations

Post money valuations are almost absent: only 1 to 2 rounds per cell at seed, A, B and C, and 5 for D plus 2022+. Most companies do not disclose them. The few values are seed 2022+ median 25M post (n=2), series A 2022+ 50.5M (n=2), series B 2018-2021 850M (n=2) and 2022+ 775M (n=2), series C 2022+ 2.15B (n=2), series D plus 2022+ 1.4B (n=5). Do not build a valuation model from these. Use the public benchmarks below for valuation and use the YC data for raise size and timing. Disclosed valuations are also survivorship biased toward companies that announced them because they were proud of them.

## Time between milestones (months from batch start, calibration sample)

| Milestone | n | p25 | p50 | p75 |
|---|---|---|---|---|
| Seed | 279 | 5.0 | 10.0 | 22.0 |
| Series A | 126 | 19.0 | 27.5 | 46.5 |
| Series B | 55 | 31.5 | 46.0 | 69.0 |
| Series C | 20 | 50.75 | 66.5 | 96.0 |
| Exit | 88 | 27.0 | 41.0 | 66.0 |
| Shutdown | 25 | 24.5 | 42.0 | 52.0 |

By era of the batch, median months to seed were 14 (2005-2012, n=22), 11 (2013-2017, n=50), 12 (2018-2021, n=111) and 8 (2022+, n=96). Median months to series A were 36.5, 29, 26 and 29 (n=15, 31, 55, 25). The 2022+ cohort is right censored: batches from 2024 and 2025 have not had time to reach series A, so the companies counted are the fast ones, and later medians will grow. Median months to series B for 2022+ rests on n=3. By industry, B2B median months to seed was 9 (n=143), Consumer 13 (n=39), Fintech 10 (n=33), Industrials 6 (n=17), Healthcare 19 (n=31). Healthcare is slow to seed and to series A (29.5, n=16). Shutdown medians are 22 months in 2005-2012 (n=8) and 49 in 2018-2021 (n=9), so recent failures were slower, though both cells are small and recent batches have not finished failing.

## Translating older eras to today

Within our data the era to era step in median raise size is: seed 2.1M (2013-2017) to 4.1M (2022+), about 2.0 times; seed 2.55M (2018-2021) to 4.1M, about 1.6 times; series A 7.0M to 14.15M, about 2.0 times, and 10.0M to 14.15M, about 1.4 times; series B 22M to 37M, about 1.7 times, and 29M to 37M, about 1.3 times. These ratios are our arithmetic on the table. Series C moves the other way (63.75M in 2018-2021, n=6, to 45M in 2022+, n=9), which is a small sample effect and not a real decline. For a company from before 2013 scale seed and A figures by the era ratios and expect large error.

Current public benchmarks. Equidam, summarizing the PitchBook NVCA Venture Monitor through 30 September 2026, reports US medians of pre money 18.3M at seed, 60.3M at series A, 187.0M at series B and 500.0M at series C, with deal sizes of 3.0M seed, 17.4M series A, 39.5M series B and 77.0M series C (secondary summary, https://www.equidam.com/?p=32620; I could not open the PitchBook PDF, https://pitchbook.brightspotcdn.com/0d/6f/a177ca2443a1a687153e0346a4f5/q2-2026-pitchbook-nvca-venture-monitor.pdf is the Q2 edition). Press coverage of the Q1 2026 monitor gives series A pre money near 62M, series A deal size 19.6M, series C pre money 579M and seed pre money 18.4M, versus 21M for series A in 2020 (https://gamesbeat.com/q1-2026-hit-big-vc-records-but-top-5-ai-deals-were-most-of-the-funding-pitchbook-nvca/). Carta reports through Q3 2026 a median seed valuation of 19.7M (basis not stated), seed round size up 50 percent and series A round size up 25 percent versus 2021, and series B pre money up 25 percent from 2025 (https://carta.com/data/state-of-private-markets-q3-2026-full-report/). Carta Q4 2025 post money medians were 24M at seed and 78.7M at series A, per a search summary I could not verify on the source page. Figures differ by quarter and sample (one source shows 165M series B pre money for Q1 against 187.0M year to date), so quote them as ranges.

Comparison with our 2022+ YC medians: seed raise 4.1M versus 3.0M market (YC companies raise about 1.4 times more, plausible since our sample counts rounds that were publicly announced), series A 14.15M versus 17.4M (0.8 times), series B 37M versus 39.5M (0.9 times), series C 45M versus 77M (0.6 times, n=9). Our 2022+ data therefore roughly matches the market at A and B, and announced seed rounds skew large. For a forecast today, use the current public pre money and deal sizes for the headline number and the YC era ratios only to translate historical comps.

## Current YC deal terms

From YC's own terms page (https://www.ycombinator.com/deal, fetched 2026-11-17, page undated): 500,000 dollars in total. 125,000 dollars is a post money SAFE that converts into 7 percent of the company including any existing option pool. 375,000 dollars is an uncapped MFN SAFE that converts on the terms of the lowest capped SAFE or other better terms issued between the MFN start date and the priced round. At a 15M post money cap the MFN part equals 2.5 percent. YC gets a pro rata right, with no fees and no milestones. An applicant account from 2022 (Relate) describes the same 7 percent for 125,000 plus 375,000 shape, so it has been stable since about 2022. Older eras used smaller checks and larger equity, so do not apply these terms to pre 2022 companies.

## Data coverage caveats

Researched companies are 662 of 6,399 (10.3 percent), all from the calibration sample, which is the unbiased subset. Everything here is on that sample only. Funding data is complete for 14, partial for 349 and absent for 299 companies. Missing funding is not zero: absent rounds mean we did not find them, and aggregators such as Crunchbase and PitchBook miss small and non US rounds. Rounds that were found are survivorship biased toward companies that announced raises, and toward successful ones. Round sizes are for the rounds recorded, so a company with an undisclosed seed contributes nothing. Valuation cells are tiny. Era is attached to the round date, but the milestone table uses batch era. Recent batches (2024 onward) are mostly unresolved, which compresses their timing and suppresses their series B and later counts. Confidence in the underlying records: high 34, medium 381, low 247.
