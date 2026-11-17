# Evaluation: TensorPool

*As of 2025-01-06. Mode: summary. Vercel For GPUs*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A real cost pain in a funded niche, but a commodity resale position makes margin and moat the question; a seed in 22 months is about even odds.**

**Chance of getting into YC:** 3.0% (range 1.0%–7.8%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$16M | 12% | Unlikely | 0.4% | Very unlikely |
| Seed | $3M–$6M | $16M–$32M | 19% | Unlikely | 0.6% | Very unlikely |
| Seed | $6M–$12M | $30M–$60M | 14% | Unlikely | 0.4% | Very unlikely |
| Seed | $12M–$20M | $60M–$110M | 5.0% | Unlikely | 0.1% | Very unlikely |
| Series A | $6M–$10M | $30M–$50M | 1.0% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$18M | $50M–$90M | 2.3% | Very unlikely | <0.1% | Very unlikely |
| Series A | $18M–$30M | $90M–$160M | 1.4% | Very unlikely | <0.1% | Very unlikely |
| Series A | $30M–$60M | $200M–$450M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$25M | $70M–$130M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$45M | $130M–$300M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series B | $45M–$90M | $300M–$700M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series B | $90M–$150M | $700M–$1.5B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$60M | $200M–$500M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $60M–$120M | $500M–$1.2B | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $120M–$300M | $1.2B–$3B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $300M–$600M | $3B–$8B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

TensorPool wraps GPU capacity from other clouds in a CLI that promises about half the price of major clouds. Demand is real, since ML teams pay a lot for GPUs and serverless GPU companies raised money, but the product depends on supplier pricing that is falling and rivals like Modal and open source SkyPilot already cover the convenience. The anchor for developer tools is 67 percent ever for a seed; with a 22 month window and a thin moat I use 50 percent. The odds do not rank this company against others. Series A inside the window is about 10 percent. The biggest killers are margin compression and customers going direct to suppliers. An upside path is a scheduler or utilization layer that earns margin regardless of supplier price.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Start from the roughly 1 percent applicant prior (band 0.6 to 2 percent). Adjust up about 2.5x for an infrastructure developer tool with a clear price claim, a technical three person team and fit with YC's interest in AI infrastructure. Adjust down for the commodity nature of GPU resale, and many funded rivals. Net about 3 percent.

**Why it fails here.** YC would most plausibly say a GPU orchestration CLI that resells cloud capacity has no obvious moat: suppliers set the cost, SkyPilot is open source, and Modal and similar serverless GPU platforms already sell the same developer convenience. The application gives no usage numbers, so partners cannot see pull from real ML teams.

### Seed: P(reach this round | in YC) = 50% after the previous step; 50% cumulative if in YC; 1.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$16M | 25% | 12% | Unlikely | 0.4% | Very unlikely | Small post YC round under $3M from angels and a micro fund. Common for a team of two to four before a customer logo is public; the 2022 and later seed row has p25 of $2.8M, so this is the lower quartile. |
| $3M–$6M | $16M–$32M | 38% | 19% | Unlikely | 0.6% | Very unlikely | Institutional seed at the center of the 2022 and later table (median $3.5M to $4.1M) shifted up a little for AI native B2B. Most likely if two or three paying design partners are visible. |
| $6M–$12M | $30M–$60M | 27% | 14% | Unlikely | 0.4% | Very unlikely | Large AI seed. Among confirmed 2026 raises above $1M the median was $6.0M, but press covers big rounds more, so this band is kept below the central one. |
| $12M–$20M | $60M–$110M | 10% | 5.0% | Unlikely | 0.1% | Very unlikely | Upside: a hot category plus fast revenue and a lead from a multi stage fund. Rare in the YC data. |

**Why it fails here.** Investors often balk at GPU resale because gross margin depends on supplier prices that fell through 2024 and are set by others. Trainy, a Summer 2023 GPU cluster management company, shows only a $500K YC round on record, and Cedana, a deep GPU technology team, shows no verified round beyond YC either.

### Series A: P(reach this round | in YC) = 10% after the previous step; 5.0% cumulative if in YC; 0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $30M–$50M | 20% | 1.0% | Very unlikely | <0.1% | Very unlikely | Thin or bridge style A under $10M, a down or flat round relative to the seed. |
| $10M–$18M | $50M–$90M | 45% | 2.3% | Very unlikely | <0.1% | Very unlikely | Central band: 2022 and later series A median $14.15M, with market medians near $17M. |
| $18M–$30M | $90M–$160M | 27% | 1.4% | Very unlikely | <0.1% | Very unlikely | Strong A led by a top fund after clear revenue growth. |
| $30M–$60M | $200M–$450M | 8.0% | 0.4% | Very unlikely | <0.1% | Very unlikely | Upside: breakout category leader, AI infrastructure style round. |

**Why it fails here.** A Series A needs a recurring revenue base that is not just pass through compute spend, with gross margins investors respect. A half price GPU claim invites customers to price shop, so retention is weak; Shadeform, a GPU marketplace that grew to 22 staff, shows no public A in the record, and FloydHub, an earlier ML platform, shut down in 2021 after the clouds copied it.

### Series B: P(reach this round | in YC) = 33% after the previous step; 1.7% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$25M | $70M–$130M | 25% | 0.4% | Very unlikely | <0.1% | Very unlikely | Small or extension B: growth slowed after the A, so the round is modest or flat to the prior valuation. |
| $25M–$45M | $130M–$300M | 45% | 0.7% | Very unlikely | <0.1% | Very unlikely | Typical B, 2022 and later median about $37M to $40M. |
| $45M–$90M | $300M–$700M | 22% | 0.4% | Very unlikely | <0.1% | Very unlikely | Large B for a category leader with strong revenue growth and a top tier lead investor. |
| $90M–$150M | $700M–$1.5B | 8.0% | 0.1% | Very unlikely | <0.1% | Very unlikely | Upside round if the company becomes the clear category winner with outsized growth. |

**Why it fails here.** A Series B requires infrastructure revenue at scale with defensible margins, and this business depends on capacity suppliers who can sell direct. The likely failure is that large customers go straight to neoclouds and hyperscalers, leaving a small developer segment that does not support a B valuation.

### Series C+: P(reach this round | in YC) = 33% after the previous step; 0.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$60M | $200M–$500M | 30% | 0.2% | Very unlikely | <0.1% | Very unlikely | Modest C with a flat valuation to the B, reflecting slower growth and tougher market multiples. |
| $60M–$120M | $500M–$1.2B | 45% | 0.2% | Very unlikely | <0.1% | Very unlikely | Typical C or D, 2022 and later median $74M to $150M. |
| $120M–$300M | $1.2B–$3B | 20% | 0.1% | Very unlikely | <0.1% | Very unlikely | Large growth round for a company with strong enterprise revenue and expanding margins. |
| $300M–$600M | $3B–$8B | 5.0% | <0.1% | Very unlikely | <0.1% | Very unlikely | Category winner raising a very large round on a premium valuation. |

**Why it fails here.** A Series C requires a durable platform with large recurring spend. The common outcome is an acquisition by a neocloud that wants software on top of its capacity, at a price below C valuations, or a plateau once GPU prices fall and customers go direct.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 57% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 25% | Reasonable | 0.8% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 15% | Unlikely | 0.4% | Very unlikely |
| Acquired or IPO over $1B | $1B–$6B | 3.0% | Very unlikely | <0.1% | Very unlikely |

**Why it fails here.** GPU access wrappers see their economics set by supplier prices that move against them; FloydHub's shutdown in 2021 after cloud vendors served the same developers is the pattern. Large outcomes require owning infrastructure or a proprietary scheduler that cuts utilization costs, and neither Trainy nor Cedana, both Summer 2023 GPU infrastructure companies, shows a verified round past YC so far.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Thin margin from reselling third party GPU capacity | 40% | Costs are set by suppliers, and public price indexes in the market show neocloud H100 rates falling, shrinking the half price spread over big clouds. | Shadeform (shadeform), FloydHub (floydhub) | Move up the stack with a scheduler or checkpointing that saves customers money regardless of supplier price. |
| 2 | Developer convenience copied by serverless GPU platforms and open source | 35% | Modal raised $16M in a Series A in Oct 2023 for serverless GPU compute, and SkyPilot is open source for multi cloud ML jobs. | FloydHub (floydhub), Cedana (cedana) | Pick the training niche where setup pain is highest and own the CLI workflow. |
| 3 | Customers go direct to neoclouds once they scale | 30% | Larger ML teams negotiate reserved capacity directly with providers, which cuts out the reseller. | Trainy (trainy), Shadeform (shadeform) | Lock in with reproducibility and cost tracking tools that stay valuable at scale. |

## Pros

- **Clear value proposition with a number: half the cost**: Hyperscaler on demand GPU prices run well above neocloud rates in market price indexes. (https://vessl.ai/en/blog/hyperscalers-vs-neoclouds-2026-en)
- **Technical team in a funded category**: Serverless GPU and ML infra drew rounds such as Modal's $16M Series A in 2023. (https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/)

## Roadmap

### Get into YC

Show ML teams using the CLI for real training jobs.

1. Get 20 active weekly users with at least 10 GPU hours each.
2. Publish cost per job comparison against AWS with receipts.

You know it worked when: Paid usage from five teams and a measured 40 percent or larger saving.

### Reach Seed

Turn savings into margin and recurring spend.

1. Sign committed capacity deals with two suppliers.
2. Add team billing and spend commitments.

You know it worked when: $30K monthly gross profit and 3 teams spending over $5K a month.

### Reach Series A

Prove a platform beyond resale.

1. Ship a scheduler that raises utilization and cuts failed jobs.
2. Build enterprise controls.

You know it worked when: $1.5M annualized revenue at 50 percent or higher gross margin.

### Reach Series B

Scale to large ML customers.

1. Add inference and fine tuning workflows.
2. Offer reserved capacity management.

You know it worked when: $10M annual recurring revenue.

### Reach Series C and beyond

Be the default software layer over GPU suppliers.

1. Integrate with all neoclouds.
2. Add global regions.

You know it worked when: $40M or more annual recurring revenue.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A job description to execution flow with provisioning across multiple GPU suppliers, data transfer, retries and cost tracking is feasible for three engineers in three months using supplier APIs. The hard part is reliability across heterogeneous providers and getting capacity at a real discount, which depends on supplier deals and not on code. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | TensorPool: Compound descriptive names are common in infrastructure, like FloydHub or Shadeform, and help developers understand the product, but they are not ownable; effect neutral. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Modal, SkyPilot, Lambda, CoreWeave, Together AI within ~6 months. Suppliers can offer their own CLI and workflows, and open source SkyPilot already covers much of the orchestration. A rival can match the CLI in under six months; the discount is the actual product. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Modal | Serverless GPU compute for AI developers. | Raised $16M Series A in October 2023 led by Redpoint. | https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/ |
| SkyPilot | Open source framework to run ML jobs across clouds at lower cost. | Widely used open source project from Berkeley researchers. | https://skypilot.co |
| Lambda, RunPod and CoreWeave | GPU clouds selling raw capacity. | Large neoclouds that are also the likely suppliers. | https://lambda.ai |
| AWS SageMaker and Google Vertex | Hyperscaler managed training. | The default for enterprise ML teams despite higher prices. | https://aws.amazon.com/sagemaker/ |

### Demand evidence

- Serverless GPU compute drew venture funding, with Modal raising a $16M Series A in 2023. (https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/)
- Hyperscaler on demand GPU prices are well above neocloud prices, so a savings pitch has an audience. (https://vessl.ai/en/blog/hyperscalers-vs-neoclouds-2026-en)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Shadeform (shadeform) | Summer 2023 | Active | GPU cloud marketplace, Summer 2023. | Grew to about 22 staff and over 30 provider clouds; funding is not clearly public, so the marketplace path needs scale first. |
| Trainy (trainy) | Summer 2023 | Active | GPU cluster management and scheduling for training, Summer 2023. | Small company, $500K YC level funding on record, claims customer logos; no later round found. |
| Cedana (cedana) | Summer 2023 | Active | GPU live migration for AI workloads, Summer 2023. | Deeply technical small team with a marketplace listing; no verified round past YC, and large vendors moved in. |
| FloydHub (floydhub) | Winter 2017 | Inactive | Heroku for deep learning, Winter 2017: the same idea in an earlier era. | Showed early usage and raised a seed but shut down in August 2021; specialist GPU clouds and big clouds served the same developers. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 67% | 50% | python3 -I scripts/base_rates.py --calibration-only --tag "Developer Tools": seed cond 67 percent (n=54); --tag AI: 64 percent (n=183). Window is 22 months from 2025-01-06 to 2026-11-17; time_to_milestones.csv 2022+ months_to_seed median 6, p75 14.2. | Anchors are for ever reaching a seed; a 22 month window covers most reachers, so the number is the anchor times about 0.75 (0.5), not lifted for the GPU boom, since the winners test shows lifts do not rank companies. Seed means an outside round above about $1M, not the YC deal. These odds do not rank this company against others. |
| Series A | 47% | 10% | python3 -I scripts/base_rates.py --calibration-only --tag "Developer Tools": series_a cond 47 percent (n=36). time_to_milestones.csv 2022+ months_to_series_a p25 19.4, median 28.0. | Window anchored: 22 months sits at the p25 to median of time to A, so roughly a third of eventual A companies show it; 0.47 times about 0.2 gives about 0.10, over 2x below the ever anchor because of time and not quality. |
| Series B | 41% | 33% | python3 -I scripts/base_rates.py --calibration-only --tag "Developer Tools": series_b cond 41 percent (n=17). | Below the anchor (0.8x) because infrastructure resale margins are thin and the later stage is crowded with neoclouds. |
| Series C+ | 43% | 33% | python3 -I scripts/base_rates.py --calibration-only --tag "Developer Tools": series_c cond 43 percent (n=7), a tiny sample. | Below the anchor (0.77x) because the sample is only 7 and GPU compute is capital heavy. |

## Assumptions and limits

- Only the as of date input was used: description, tags, team of 3, San Francisco.
- Window is 22 months from 2025-01-06 to 2026-11-17; seed means an outside round above about $1M, not the YC deal.
- Customer count, revenue and supplier terms are unknown.
- Records and web results dated after 2025-01-06 were ignored, including 2026 GPU price pages cited by search results.
- Funding data for 2022+ analogs is partial and right censored.

## Sources

- https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/
- https://skypilot.co
- https://lambda.ai
- https://aws.amazon.com/sagemaker/
- https://vessl.ai/en/blog/hyperscalers-vs-neoclouds-2026-en
