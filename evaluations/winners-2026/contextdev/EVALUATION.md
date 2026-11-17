# Evaluation: Context.dev

*As of 2026-07-06. Mode: summary. Web data API for agents*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Strong early pull in a crowded and well funded category; seed is likely, later rounds depend on beating Firecrawl and Exa.**

**Chance of getting into YC:** 10% (range 5.0%–15%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $8M–$15M | 11% | Unlikely | 1.1% | Very unlikely |
| Seed | $2M–$5M | $15M–$35M | 41% | Reasonable | 4.1% | Very unlikely |
| Seed | $5M–$12M | $35M–$90M | 22% | Reasonable | 2.2% | Very unlikely |
| Series A | $5M–$9M | $30M–$60M | 5.0% | Very unlikely | 0.5% | Very unlikely |
| Series A | $10M–$22M | $60M–$150M | 14% | Unlikely | 1.4% | Very unlikely |
| Series A | $22M–$40M | $150M–$350M | 6.2% | Unlikely | 0.6% | Very unlikely |
| Series B | $20M–$35M | $100M–$220M | 1.3% | Very unlikely | 0.1% | Very unlikely |
| Series B | $35M–$70M | $220M–$600M | 2.1% | Very unlikely | 0.2% | Very unlikely |
| Series B | $70M–$150M | $600M–$1.5B | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$160M | $700M–$1.8B | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $160M–$400M | $1.8B–$5B | 0.3% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Context.dev starts the batch with claimed usage by hundreds of companies, which is unusual and lifts seed odds above the cohort. The category is hot, but the leaders have raised far more and model providers can bundle web access. The outcome hinges on whether it carves out structured data and reliability as a distinct product. The forecast treats the day one description as the best case, anchors on the 2022 to 2024 cohort of researched YC companies, and widens the uncertainty because funding data for recent batches is incomplete and right censored.

## Round by round: where and why it fails

### Getting into YC: 10%

**How we got the number.** Note only: already accepted to YC Summer 2026, so this is not a forecast. Prior for a random applicant is about 1 percent (yc_acceptance.md). Claimed 800 plus customers is strong traction.

**Why it fails here.** Not applicable since the company was accepted. YC would most plausibly worry that web data APIs are crowded by Firecrawl, Exa, Apify and Bright Data, and that the customer count lacks revenue depth. Because acceptance is already a fact in this test, the estimate is a placeholder and the forecast value sits in the funding ladder that follows.

### Seed: P(reach this round | in YC) = 75% after the previous step; 75% cumulative if in YC; 7.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $8M–$15M | 15% | 11% | Unlikely | 1.1% | Very unlikely | Small round, possible for a lean usage business. |
| $2M–$5M | $15M–$35M | 55% | 41% | Reasonable | 4.1% | Very unlikely | Core: AI developer infrastructure with logos. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $5M–$12M | $35M–$90M | 30% | 22% | Reasonable | 2.2% | Very unlikely | Upside seen at peers like Firecrawl and Exa that raised at fast growth. |

**Why it fails here.** Seed stalls if the 800 customers are mostly free or very small and revenue stays low, or if the team of six is distracted. Dashblock, a website to API company from 2019, shut down, and Anakin raised only a 2M seed before slow growth. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series A: P(reach this round | in YC) = 33% after the previous step; 25% cumulative if in YC; 2.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$9M | $30M–$60M | 20% | 5.0% | Very unlikely | 0.5% | Very unlikely | Thin round on modest revenue. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $10M–$22M | $60M–$150M | 55% | 14% | Unlikely | 1.4% | Very unlikely | Core, in line with the B2B median near 15M and Firecrawl's 14.5M Series A in 2025. |
| $22M–$40M | $150M–$350M | 25% | 6.2% | Unlikely | 0.6% | Very unlikely | Upside with fast usage growth. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Series A fails when usage stays small, the best customers churn to Firecrawl or build their own scrapers, or gross margin suffers from proxy and browser cost. Anakin and Newscatcher show profitable but slow growth that never became a priced Series A. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series B: P(reach this round | in YC) = 17% after the previous step; 4.2% cumulative if in YC; 0.4% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$35M | $100M–$220M | 30% | 1.3% | Very unlikely | 0.1% | Very unlikely | Flat step up. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $35M–$70M | $220M–$600M | 50% | 2.1% | Very unlikely | 0.2% | Very unlikely | Typical for developer infrastructure at scale. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $70M–$150M | $600M–$1.5B | 20% | 0.8% | Very unlikely | <0.1% | Very unlikely | Upside, as seen for category leaders. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Series B fails if the market consolidates around two or three leaders and Context.dev stays a niche option. It also fails when legal pressure on scraping, blocked access and rising anti bot costs weaken the product. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series C+: P(reach this round | in YC) = 33% after the previous step; 1.4% cumulative if in YC; 0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | 0.6% | Very unlikely | <0.1% | Very unlikely | Modest growth round. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $80M–$160M | $700M–$1.8B | 40% | 0.6% | Very unlikely | <0.1% | Very unlikely | Core. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $160M–$400M | $1.8B–$5B | 20% | 0.3% | Very unlikely | <0.1% | Very unlikely | Upside as agent data infrastructure. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Fails if open source tools and model providers' built in browsing remove the need for a separate API, so growth stalls before a late stage round, as with many tooling companies that stay mid size. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 45% | Likely | 94% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 30% | Reasonable | 3.0% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 20% | Reasonable | 2.0% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 5.0% | Unlikely | 0.5% | Very unlikely |

**Why it fails here.** The most common ends are a small acquisition by a data or developer platform, or a stall as search and browsing become features of model providers. A large exit needs category leadership. A meaningful exit needs a durable lead in a category where rivals can copy features and raise more money, and most companies in the reference cohort stay small, are acquired cheaply or stop operating before that point.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Firecrawl, Exa and others win the category | 40% | Exa raised a large Series C in May 2026 and Firecrawl raised a Series A in 2025 with many developers. | Firecrawl (firecrawl), Anakin (anakin) | Focus on structured outputs and reliability for named verticals. |
| 2 | Models and agent platforms add built in web access | 30% | Search and browsing tools already ship inside major model APIs, which reduces the need for a separate vendor. | Dashblock (dashblock) | Offer freshness, schemas and guarantees that general tools lack. |
| 3 | Anti bot and legal pressure raise costs | 20% | Scraping at scale depends on proxies and on site tolerance, and blocking raises cost per request. | NewsCatcher (newscatcher) | Build licensed data partnerships and caching. |

## Pros

- **Claimed 800 plus customers and named logos at the start of the batch.**: Stated in the company description. (https://context.dev)
- **Category is the hottest for AI infrastructure funding.**: Exa and Firecrawl raised large rounds. (https://builtin.com/articles/firecrawl-raises-14m-series-a-20250820)

## Roadmap

### Get into YC

Prove paid usage.

1. Report paying customers and monthly revenue
2. Show retention by cohort

You know it worked when: Paid customers above 100 with growing usage.

### Reach Seed

Raise above 500K quickly.

1. Publish benchmarks versus Firecrawl
2. Land two logos paying over 2K a month

You know it worked when: Monthly revenue above 30K.

### Reach Series A

Be a top three web data API.

1. Launch structured schemas by vertical
2. Add enterprise plans

You know it worked when: Over 1M annual recurring revenue with strong retention.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Scraping, extraction with models and caching are buildable by a small team. The hard part is staying reliable against blocking at scale and keeping cost per request low. |
| Name and brand (5 = iconic, drives growth; effect on success: helps) | 3 | Context.dev: Descriptive developer brand names such as Firecrawl and Browserbase work when the product is strong, and a .dev style name signals a developer audience, a small plus. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Firecrawl, Exa, model providers within ~6 months. Funded rivals can match features in months and model providers can bundle browsing; the defense is customer lock in via structured schemas and integrations. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Firecrawl | Open source web to LLM data API. | Series A of 14.5M in August 2025. | https://builtin.com/articles/firecrawl-raises-14m-series-a-20250820 |
| Exa | Web search API for AI. | Raised 250M Series C in May 2026 at a reported 2.2B valuation. | https://www.cbinsights.com/compare/metaphor-1-vs-sideguide-1 |
| Browserbase | Browser infrastructure for agents. | 67.5M total raised, 1,000 plus customers. | https://www.cbinsights.com/investor/browserbase |

### Demand evidence

- Investors fund the category heavily, with Exa, Firecrawl and Browserbase raising rounds. (https://www.cbinsights.com/investor/browserbase)
- Agent builders need live web data, shown by the many vendors listed in the category. (https://builtin.com/articles/firecrawl-raises-14m-series-a-20250820)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Firecrawl (firecrawl) | Summer 2022 | Active | Web data API for agents. | Pivoted from Mendable and reached Series A in 2025 and later rounds; leader of the category. |
| Anakin (anakin) | Summer 2021 | Active | One API for web data. | 2M seed in 2021, still active with about 70 people, no later round found. |
| Dashblock (dashblock) | Summer 2019 | Inactive | Turn any website into an API, Summer 2019. | Shut down by about 2022 with about 150K raised. |
| NewsCatcher (newscatcher) | Summer 2022 | Active | Web to structured events data. | Active with enterprise customers, no priced round beyond YC and TinySeed. |
| Skyvern (skyvern) | Summer 2023 | Active | Agent API for browser workflows. | Seed of 2.7M late in 2025. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 75% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | 1.2x the anchor: 800 plus claimed customers and named logos show pull, and the AI agent data wave is the hottest category for seed. |
| Series A | 33% | 33% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | At the anchor. Pull is strong but Firecrawl and Exa already hold investor attention, which lowers the odds for a fourth entrant. |
| Series B | 17% | 17% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | At the anchor. |
| Series C+ | 36% | 33% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | Slightly below the anchor for a crowded category. |

## Assumptions and limits

- Pretend date is 2026-07-06 and only the input file describes the company.
- Seed means a round above about 500K within about 12 months of batch start.
- The 800 customer claim is taken as stated but not verified, and may include free users.

## Sources

- https://builtin.com/articles/firecrawl-raises-14m-series-a-20250820
- https://www.cbinsights.com/investor/browserbase
- https://www.cbinsights.com/compare/metaphor-1-vs-sideguide-1
