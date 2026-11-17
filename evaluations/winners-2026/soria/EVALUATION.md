# Evaluation: Soria

*As of 2026-04-06. Mode: summary. AI Financial Research Terminal built for Healthcare (and beyond)*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Real budgets but a crowded buyer market; a seed is plausible and later rounds depend on a proprietary data edge.**

**Chance of getting into YC:** 10% (range 5.0%–15%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $8M–$16M | 14% | Unlikely | 1.4% | Very unlikely |
| Seed | $2M–$5M | $16M–$35M | 32% | Reasonable | 3.2% | Very unlikely |
| Seed | $5M–$10M | $35M–$70M | 12% | Unlikely | 1.2% | Very unlikely |
| Series A | $4M–$8M | $25M–$45M | 3.8% | Very unlikely | 0.4% | Very unlikely |
| Series A | $10M–$20M | $50M–$120M | 8.3% | Unlikely | 0.8% | Very unlikely |
| Series A | $20M–$40M | $120M–$300M | 3.0% | Very unlikely | 0.3% | Very unlikely |
| Series B | $15M–$30M | $80M–$170M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $170M–$450M | 1.2% | Very unlikely | 0.1% | Very unlikely |
| Series B | $60M–$120M | $450M–$1B | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$70M | $250M–$600M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $70M–$150M | $600M–$1.5B | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$350M | $1.5B–$4B | 0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Soria sells an AI research terminal to sector funds, starting in healthcare. Funds pay well and AI research is a funded category, so a seed is more likely than not. The weak points are a three person team, strong incumbents and similar YC peers that stalled after seed. If the proprietary data layer proves real and two or three funds pay, the path to a Series A is credible. The forecast treats the day one description as the best case, anchors on the 2022 to 2024 cohort of researched YC companies, and widens the uncertainty because funding data for recent batches is incomplete and right censored.

## Round by round: where and why it fails

### Getting into YC: 10%

**How we got the number.** Note only: already accepted to YC Spring 2026. Prior of about 1 percent for a random applicant (yc_acceptance.md) is not informative, so the real work is in the ladder.

**Why it fails here.** Not applicable because the company was accepted. A reviewer would most plausibly worry that the product pitch is broad, that AlphaSense, Bloomberg and many AI research startups already sell to funds, and that a three person team cannot build a proprietary data layer. Because acceptance is already a fact in this test, the estimate is a placeholder and the forecast value sits in the funding ladder that follows.

### Seed: P(reach this round | in YC) = 58% after the previous step; 58% cumulative if in YC; 5.8% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $8M–$16M | 25% | 14% | Unlikely | 1.4% | Very unlikely | Small round while hunting first paying funds. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $2M–$5M | $16M–$35M | 55% | 32% | Reasonable | 3.2% | Very unlikely | Core: AI financial research with early fund pilots, in line with 3.3M B2B seed median. |
| $5M–$10M | $35M–$70M | 20% | 12% | Unlikely | 1.2% | Very unlikely | Upside if two or three recognizable funds sign. |

**Why it fails here.** Seed stalls if funds only pilot and do not pay, because buyers are slow and demand evidence of accuracy. Analogs Trata and Dataglade show years without a confirmed round after their batches. Domain expert review adds cost that may scare seed investors. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series A: P(reach this round | in YC) = 26% after the previous step; 15% cumulative if in YC; 1.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $25M–$45M | 25% | 3.8% | Very unlikely | 0.4% | Very unlikely | Thin round on a handful of fund contracts. |
| $10M–$20M | $50M–$120M | 55% | 8.3% | Unlikely | 0.8% | Very unlikely | Core: terminal products with sticky budgets raise 10 to 20M. |
| $20M–$40M | $120M–$300M | 20% | 3.0% | Very unlikely | 0.3% | Very unlikely | Upside if it becomes a standard sector terminal. |

**Why it fails here.** Series A fails if annual contract value stays under about 50K per fund and sales cycles are long, so recurring revenue does not reach the 1M bar. Expert review and data licensing costs may keep gross margin low, and AlphaSense and model labs can bundle similar features.

### Series B: P(reach this round | in YC) = 16% after the previous step; 2.4% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$170M | 30% | 0.7% | Very unlikely | <0.1% | Very unlikely | Modest round on slow growth. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $30M–$60M | $170M–$450M | 50% | 1.2% | Very unlikely | 0.1% | Very unlikely | Core growth round. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $60M–$120M | $450M–$1B | 20% | 0.5% | Very unlikely | <0.1% | Very unlikely | Upside as a multi sector platform. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Series B fails when expansion sector by sector proves slow, since each sector needs its own data and experts, and when large incumbents or competitors cut price. Growth stays linear instead of compounding. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series C+: P(reach this round | in YC) = 30% after the previous step; 0.7% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$70M | $250M–$600M | 40% | 0.3% | Very unlikely | <0.1% | Very unlikely | Growth round at moderate scale. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $70M–$150M | $600M–$1.5B | 40% | 0.3% | Very unlikely | <0.1% | Very unlikely | Core. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $150M–$350M | $1.5B–$4B | 20% | 0.1% | Very unlikely | <0.1% | Very unlikely | Upside if it becomes a rival to AlphaSense. |

**Why it fails here.** Fails if the product stays a point solution in one or two sectors, or if general AI agents let funds build their own research stack, ending growth before a late stage round. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 95% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 28% | Reasonable | 2.8% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 17% | Unlikely | 1.7% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 5.0% | Unlikely | 0.5% | Very unlikely |

**Why it fails here.** Most likely a stall or an acquisition by a data provider such as a larger research platform, because buyers consolidate vendors and a three person team faces large incumbents with distribution. A meaningful exit needs a durable lead in a category where rivals can copy features and raise more money, and most companies in the reference cohort stay small, are acquired cheaply or stop operating before that point.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | AlphaSense, Bloomberg and AI research startups win the buyer | 40% | AlphaSense was valued at 2.5B in 2024 and well funded rivals sell AI research to the same funds. | Trata (trata), Dataglade (dataglade) | Own a proprietary sector data layer and sell to a narrow healthcare niche first. |
| 2 | Funds are slow buyers and pilots do not convert | 30% | Hedge funds demand verification, security reviews and long trials before paying for new tools. | Constant (constant), Finbar (finbar) | Pick two funds with founder network access and charge from day one. |
| 3 | Data cost and expert review keep margins thin with a three person team | 25% | Licensed sources and expert reviewers cost money for each sector expansion. | Bayesline (bayesline) | Automate review and expand only when contracts pay for a sector. |

## Pros

- **Funds pay high prices for research tools.**: AlphaSense scale and valuation. (https://malaysia.news.yahoo.com/ai-startup-alphasense-valued-2-120438909.html)
- **Multiple delivery channels (MCP, API, warehouse sync) fit how quant and AI teams buy data.**: Listed in the product description. (https://www.soriaanalytics.com/)

## Roadmap

### Get into YC

Land paying funds.

1. Sign two healthcare funds on paid pilots
2. Publish accuracy against analyst models

You know it worked when: First 25K annual contracts.

### Reach Seed

Raise above 500K in 12 months.

1. Show weekly active analysts
2. Expand to a second healthcare subsector

You know it worked when: Recurring revenue of 15K a month or more.

### Reach Series A

Repeatable sector expansion.

1. Launch a second sector
2. Cut cost per model with automation

You know it worked when: About 1M annual recurring revenue.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 1 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Ingestion pipelines and agents over filings are buildable by a small team. Building accurate sector models, licensing private sources and passing fund security reviews is hard and expensive, and reliability matters because mistakes cost money. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Soria: Short coined names are common for YC finance companies and rarely decide outcomes; sales quality and data trust matter far more, as in the research terminal category. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by AlphaSense, Bloomberg, FactSet, Anthropic and OpenAI finance products within ~12 months. Incumbents have data and distribution and model labs are adding finance agents; a bundled copy could arrive within a year, so the proprietary data layer must be the defense. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| AlphaSense | AI market intelligence for financial firms. | Valued at 2.5B after a 2024 round. | https://malaysia.news.yahoo.com/ai-startup-alphasense-valued-2-120438909.html |
| Hebbia | AI research platform for finance. | Reported over 100M raised. | https://www.tamradar.com/funding-rounds/alphasense-350m-7-5b-valuation |
| Bloomberg terminal and status quo analyst spreadsheets | Incumbent terminal and manual models. | Dominant seat base among funds. | https://www.bloomberg.com/professional/ |

### Demand evidence

- AlphaSense reached a multi billion dollar valuation selling AI research to financial firms, showing spend. (https://malaysia.news.yahoo.com/ai-startup-alphasense-valued-2-120438909.html)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Trata (trata) | Winter 2025 | Active | AI research desk for hedge funds with a hedge fund founder, Winter 2025. | Seed only, six people, no later round found. |
| Dataglade (dataglade) | Winter 2023 | Active | AI research for investment professionals, Winter 2023. | Active but no funding found. |
| Constant (constant) | Winter 2023 | Active | AI analysts for the buy side, Winter 2023. | Active with two people and no funding found. |
| Finbar (finbar) | Winter 2025 | Active | Financial intelligence from proprietary filings, Winter 2025. | Active with hedge fund customers, funding unclear. |
| Bayesline (bayesline) | Summer 2024 | Active | Analytics for asset managers by ex Bloomberg and BlackRock quants. | Seed, still early. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 70% | 58% | python3 -I scripts/base_rates.py --years 2020-2024 --industry Fintech --calibration-only: seed cond 70% (n=33), series_a cond 26% (n=23), series_b cond 17% (n=6); broad B2B 2022-2024: seed 61%, A 33%, B 17%; series_c all-year cond 36% (n=55) | 0.83x of the fintech anchor. Hot AI demand and sector expert reviewers help, but a team of three, a crowded space and a long enterprise sales cycle with funds lower odds. |
| Series A | 26% | 26% | python3 -I scripts/base_rates.py --years 2020-2024 --industry Fintech --calibration-only: seed cond 70% (n=33), series_a cond 26% (n=23), series_b cond 17% (n=6); broad B2B 2022-2024: seed 61%, A 33%, B 17%; series_c all-year cond 36% (n=55) | At the anchor. Financial data buyers pay well, but analogs Constant and Dataglade show no Series A. |
| Series B | 17% | 16% | python3 -I scripts/base_rates.py --years 2020-2024 --industry Fintech --calibration-only: seed cond 70% (n=33), series_a cond 26% (n=23), series_b cond 17% (n=6); broad B2B 2022-2024: seed 61%, A 33%, B 17%; series_c all-year cond 36% (n=55) | At the anchor. |
| Series C+ | 36% | 30% | python3 -I scripts/base_rates.py --years 2020-2024 --industry Fintech --calibration-only: seed cond 70% (n=33), series_a cond 26% (n=23), series_b cond 17% (n=6); broad B2B 2022-2024: seed 61%, A 33%, B 17%; series_c all-year cond 36% (n=55) | Below the anchor because few comparable companies got here. |

## Assumptions and limits

- Pretend date is 2026-04-06 and only the input file describes the company.
- Seed means a round above about 500K within about 12 months of batch start.
- AlphaSense figures cited are from 2024, before the as of date; later news was ignored.

## Sources

- https://malaysia.news.yahoo.com/ai-startup-alphasense-valued-2-120438909.html
- https://www.soriaanalytics.com/
