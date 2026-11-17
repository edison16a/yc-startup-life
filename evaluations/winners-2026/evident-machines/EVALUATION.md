# Evaluation: Evident Machines

*As of 2026-10-05. Mode: summary. Real-world benchmarks and RL environments for electrical engineering*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A narrow but timely hardware benchmark and RL environment vendor that can likely raise a seed and then must prove labs keep paying.**

**Chance of getting into YC:** 95% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $6M–$18M | 12% | Unlikely | 11% | Unlikely |
| Seed | $3M–$8M | $20M–$50M | 30% | Reasonable | 28% | Reasonable |
| Seed | $10M–$25M | $60M–$160M | 18% | Unlikely | 17% | Unlikely |
| Series A | $4M–$9M | $22M–$45M | 4.5% | Very unlikely | 4.3% | Very unlikely |
| Series A | $11M–$20M | $55M–$110M | 7.5% | Unlikely | 7.1% | Unlikely |
| Series A | $24M–$45M | $150M–$320M | 3.0% | Very unlikely | 2.8% | Very unlikely |
| Series B | $14M–$28M | $70M–$140M | 1.0% | Very unlikely | 0.9% | Very unlikely |
| Series B | $32M–$55M | $170M–$330M | 1.7% | Very unlikely | 1.6% | Very unlikely |
| Series B | $65M–$130M | $450M–$1.1B | 0.7% | Very unlikely | 0.6% | Very unlikely |
| Series C+ | $35M–$70M | $220M–$450M | 0.2% | Very unlikely | 0.2% | Very unlikely |
| Series C+ | $80M–$140M | $550M–$1.1B | 0.4% | Very unlikely | 0.3% | Very unlikely |
| Series C+ | $180M–$450M | $1.5B–$4.5B | 0.1% | Very unlikely | 0.1% | Very unlikely |

## General assessment

Evident Machines sells electrical engineering benchmarks and RL environments to frontier labs. RL environment startups drew many small seeds in 2025 and buyer concentration is the main danger. The physical lab is a differentiator and a cost. The ladder sits near the B2B anchors with a higher seed because lab budgets are large and the founders can sell a narrow dataset quickly. The estimates are anchored on the 2023 to 2025 B2B cohort and adjusted only with the stated reasons, keeping each step within 0.75 times its anchor. Reaching a later round years after the batch is common for companies with paying customers, and a pivot followed by a raise is part of the upside band, so the ladder asks whether a round is reached and not how fast.

## Round by round: where and why it fails

### Getting into YC: 95%

**How we got the number.** Blind test: the company is already accepted to YC for its batch, so the acceptance estimate is a placeholder near certainty rather than a forecast. The unconditional prior for a random applicant is about 1 percent (0.6 to 2 percent, third party figures in yc_acceptance.md).

**Why it fails here.** Not applicable in this test because the company was accepted. Had it been assessed as an applicant, the most plausible reason for a no would be a tiny team in a crowded RL environment market with a capital heavy lab. The founders would also need to show in the interview that they can ship quickly and have a specific first customer in mind, since YC weighs team speed and clear user need over market size.

### Seed: P(reach this round | in YC) = 60% after the previous step; 60% cumulative if in YC; 57% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $6M–$18M | 20% | 12% | Unlikely | 11% | Unlikely | Thin case for Evident Machines at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $3M–$8M | $20M–$50M | 50% | 30% | Reasonable | 28% | Reasonable | Typical case for Evident Machines at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $10M–$25M | $60M–$160M | 30% | 18% | Unlikely | 17% | Unlikely | Hot case for Evident Machines at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** The likely stopper is buyer concentration. Frontier labs buy environments but have many vendors and in house teams, and a two person company with a physical lab has high cost per task. Klavis recorded only 500K and Sherpa Labs only 500K, so a round above that needs a signed lab customer or a standout benchmark.

### Series A: P(reach this round | in YC) = 25% after the previous step; 15% cumulative if in YC; 14% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$9M | $22M–$45M | 30% | 4.5% | Very unlikely | 4.3% | Very unlikely | Thin or flat case for Evident Machines at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $11M–$20M | $55M–$110M | 50% | 7.5% | Unlikely | 7.1% | Unlikely | Typical case for Evident Machines at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $24M–$45M | $150M–$320M | 20% | 3.0% | Very unlikely | 2.8% | Very unlikely | Upside case for Evident Machines at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series A needs repeat revenue from several labs and proof the data improves model scores. The likely miss is that labs run one off pilots, pay low prices for environments, and then bring electrical engineering data collection in house or buy from larger vendors like Scale and Surge.

### Series B: P(reach this round | in YC) = 22% after the previous step; 3.3% cumulative if in YC; 3.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $14M–$28M | $70M–$140M | 30% | 1.0% | Very unlikely | 0.9% | Very unlikely | Thin or flat case for Evident Machines at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $32M–$55M | $170M–$330M | 50% | 1.7% | Very unlikely | 1.6% | Very unlikely | Typical case for Evident Machines at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $65M–$130M | $450M–$1.1B | 20% | 0.7% | Very unlikely | 0.6% | Very unlikely | Upside case for Evident Machines at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series B needs a product beyond bespoke data, such as a standard benchmark that labs license annually. The likely stop is that the RL environment market commoditises, buyers consolidate, and the physical lab model does not scale like software environments. The analogs in the records suggest only a minority of companies in this cohort that reach a seed ever reach this round, and the company would need clear paying customers and improving margins to be among them.

### Series C+: P(reach this round | in YC) = 22% after the previous step; 0.7% cumulative if in YC; 0.7% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $35M–$70M | $220M–$450M | 30% | 0.2% | Very unlikely | 0.2% | Very unlikely | Thin or flat case for Evident Machines at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $80M–$140M | $550M–$1.1B | 50% | 0.4% | Very unlikely | 0.3% | Very unlikely | Typical case for Evident Machines at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $180M–$450M | $1.5B–$4.5B | 20% | 0.1% | Very unlikely | 0.1% | Very unlikely | Upside case for Evident Machines at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series C needs a platform position. Likely the company ends as a services style data vendor or is acquired by a lab or a data company, since no vendor of this type has reached C in the YC records. The records show very few comparable companies reaching this stage, and those that did had durable revenue and a defensible position, which this company would need to show well before then.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 58% | Likely | 60% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 28% | Reasonable | 27% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 11% | Unlikely | 10% | Unlikely |
| Acquired or IPO over $1B | $1B–$5B | 3.0% | Very unlikely | 2.8% | Very unlikely |

**Why it fails here.** Most likely the company stalls as a niche data vendor or is absorbed. The buyers are a handful of frontier labs that can switch or build in house, and many RL environment startups chase the same budgets. Analogs such as Klavis, Sherpa Labs and Refresh show small recorded rounds and no verified later raises.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Few buyers and in house teams cap demand. | 40% | Frontier labs are a handful of customers and run their own data teams. | Klavis AI (klavis-ai), Sherpa Labs (sherpa-labs) | Sign two or three labs on multi quarter contracts early. |
| 2 | Physical lab experiments are slow and costly, so unit economics fail versus simulation based environments. | 30% | Software environments scale at zero marginal cost while a lab needs equipment and staff. | Aviro (aviro) | Use simulation for most tasks and the lab for verified gold labels. |
| 3 | Larger data vendors add electrical engineering. | 25% | Scale AI and others sell expert data across domains. and this was visible from the market at the batch start date. | AfterQuery (afterquery) | Specialise on hardware in the loop tasks others cannot run. |

## Pros

- **Hardware focus is rare among RL environment vendors.**: Most comparable startups target software tasks. (https://scale.com)
- **Labs have large budgets for data.**: Data vendor revenue reported across 2025. (https://surgehq.ai)

## Roadmap

### Get into YC

Arrive at the batch with a sharp wedge and one named paying design partner.

1. Pick one narrow customer and workflow and write down the measurable result it should produce.
2. Sign a letter of intent or paid pilot before demo day.

You know it worked when: At least one pilot signed with a named buyer.

### Reach Seed

Sign a lab customer for a first benchmark or environment pack.

1. Publish an open electrical engineering benchmark.
2. Deliver a paid pilot dataset to one frontier lab.

You know it worked when: A seed above the YC check with a named lab customer.

### Reach Series A

Show repeat purchases from several labs and score gains from the data.

1. Build simulation backed environments that scale.
2. Add a licensing model for the benchmark.

You know it worked when: Three paying labs with renewals.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Building valid benchmarks that link simulation to physical measurements needs electrical engineering depth and lab equipment. A two person team can start with narrow tasks. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Evident Machines: Evident Machines is a descriptive compound that fits a benchmark brand, where trust in the measurement matters. It is longer than most YC names but acceptable for a B2B data vendor. |
| Takeover/copy risk (5 = very likely) | 3 | Could be built or absorbed by Scale AI, Surge AI, Mercor, Frontier labs in house within ~12 months. Data vendors can add an electrical engineering domain with expert hires, but physical experiments are harder to copy. A well resourced rival would need roughly the stated time and would have the incentive if the category proves valuable. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Scale AI | Expert data and evaluations for labs. | Largest data vendor. | https://scale.com |
| Surge AI | High quality expert data for frontier labs. | Large revenue reported in the press. | https://surgehq.ai |
| Mercor | Expert marketplace supplying domain data for labs. | Rapid growth in 2025. | https://mercor.com |

### Demand evidence

- Frontier labs pay for expert training data and RL environments across domains. (https://scale.com)
- Hardware and electrical engineering are weak spots for current models, creating demand for evaluations. (https://surgehq.ai)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Klavis AI (klavis-ai) | Spring 2025 | Active | RL environments and training data for labs. | Spring 2025 batch, 500K seed in 2025, no later round in the record. |
| Sherpa Labs (sherpa-labs) | Winter 2025 | Active | Frontier data vendor. | Winter 2025 batch, 500K pre seed recorded. |
| AfterQuery (afterquery) | Winter 2025 | Active | Applied research lab curating data for foundation models. | Winter 2025 batch, Series A of 30M recorded in April 2026. |
| Aviro (aviro) | Spring 2025 | Active | RL environments for long horizon work. | Spring 2025 batch, active, no verified round. |
| Diode Computers, Inc. (diode-computers-inc) | Summer 2024 | Active | Electronics focus with a funded outcome. | Summer 2024 batch, 11.4M Series A in 2025. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 49% | 60% | python3 -I scripts/base_rates.py --years 2023-2025 --industry B2B : seed 42% / 49% / 56% (lower / known / upper), cond 49% (n=950) | Above the 49 percent anchor within 1.25x: RL environment and data companies drew early funding in 2025 (Klavis, Cartpole, Aviro, Refresh) and two founders can sell a narrow lab dataset fast, but the buyer list is small. |
| Series A | 22% | 25% | same command: series_a 9% / 11% / 23%, cond 22% (n=465) | Near the 22 percent anchor, slightly higher at 25 percent only if revenue from one or two labs is real; otherwise concentration risk lowers it. |
| Series B | 20% | 22% | same command: series_b 2% / 2% / 16%, cond 20% (n=101) | Near the 20 percent anchor; environment vendors depend on a few buyers and labs may build in house. |
| Series C+ | 25% | 22% | same command: series_c 0% / 1% / 15%, cond 25% (n=20) | Near the 25 percent anchor; few vendors in this category will survive to C. |

## Assumptions and limits

- Founder backgrounds were not given.
- Blind test: only the batch input file and market web searches were used; no company specific records. The seed step is read as a round above the standard YC deal of about 500K dollars within roughly 12 months of batch start.
- Extraction coverage is 662 of 6,399 companies researched in the calibration sample, plus recent cohort records; later cohorts are right censored, so base rates for 2023 to 2025 batches understate eventual progress.

## Sources

- https://www.ycombinator.com/deal
- https://www.equidam.com/?p=32620
- https://scale.com
- https://surgehq.ai
- https://mercor.com
