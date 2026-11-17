# Evaluation: Atrisa

*As of 2026-04-06. Mode: summary. AI Agents for Analog Circuit Design*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A deep tech chip design agent company with a real expert labor wedge, likely to get a seed and then test whether analog automation works.**

**Chance of getting into YC:** 95% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $6M–$15M | 14% | Unlikely | 13% | Unlikely |
| Seed | $2.5M–$6M | $15M–$38M | 28% | Reasonable | 26% | Reasonable |
| Seed | $8M–$18M | $50M–$110M | 14% | Unlikely | 13% | Unlikely |
| Series A | $4M–$9M | $22M–$45M | 5.0% | Very unlikely | 4.7% | Very unlikely |
| Series A | $11M–$20M | $55M–$110M | 8.2% | Unlikely | 7.8% | Unlikely |
| Series A | $24M–$45M | $150M–$320M | 3.3% | Very unlikely | 3.1% | Very unlikely |
| Series B | $14M–$28M | $70M–$140M | 1.4% | Very unlikely | 1.3% | Very unlikely |
| Series B | $32M–$55M | $170M–$330M | 2.3% | Very unlikely | 2.2% | Very unlikely |
| Series B | $65M–$130M | $450M–$1.1B | 0.9% | Very unlikely | 0.9% | Very unlikely |
| Series C+ | $35M–$70M | $220M–$450M | 0.3% | Very unlikely | 0.3% | Very unlikely |
| Series C+ | $80M–$140M | $550M–$1.1B | 0.6% | Very unlikely | 0.5% | Very unlikely |
| Series C+ | $180M–$450M | $1.5B–$4.5B | 0.2% | Very unlikely | 0.2% | Very unlikely |

## General assessment

Atrisa builds agents for analog circuit design, a field where experts are scarce and incumbents Cadence and Synopsys dominate. The three person team is typical for YC. Peers in chip design AI show a mixed picture: Silimate raised a small seed, Diode reached a Series A, and others stalled. The seed is roughly a coin flip above the YC check, and later steps follow the B2B anchors because the technical risk is high and the market is narrow. The estimates are anchored on the 2023 to 2025 B2B cohort and adjusted only with the stated reasons, keeping each step within 0.75 times its anchor. Reaching a later round years after the batch is common for companies with paying customers, and a pivot followed by a raise is part of the upside band, so the ladder asks whether a round is reached and not how fast.

## Round by round: where and why it fails

### Getting into YC: 95%

**How we got the number.** Blind test: the company is already accepted to YC for its batch, so the acceptance estimate is a placeholder near certainty rather than a forecast. The unconditional prior for a random applicant is about 1 percent (0.6 to 2 percent, third party figures in yc_acceptance.md).

**Why it fails here.** Not applicable in this test because the company was accepted. Had it been assessed as an applicant, the most plausible reason for a no would be a very small team with a research heavy product and no customer proof. The founders would also need to show in the interview that they can ship quickly and have a specific first customer in mind, since YC weighs team speed and clear user need over market size.

### Seed: P(reach this round | in YC) = 55% after the previous step; 55% cumulative if in YC; 52% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $6M–$15M | 25% | 14% | Unlikely | 13% | Unlikely | Thin case for Atrisa at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $2.5M–$6M | $15M–$38M | 50% | 28% | Reasonable | 26% | Reasonable | Typical case for Atrisa at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $8M–$18M | $50M–$110M | 25% | 14% | Unlikely | 13% | Unlikely | Hot case for Atrisa at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** The likely stopper is proof. Analog design is hard to automate because circuits depend on process design kits, layout parasitics and designer taste, and a three person team may only show demos on textbook blocks. Investors in chip design AI such as those behind Silimate funded digital verification first, and Silogy only shows a 500K check, so a larger seed needs a named fab or design house pilot.

### Series A: P(reach this round | in YC) = 30% after the previous step; 16% cumulative if in YC; 16% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$9M | $22M–$45M | 30% | 5.0% | Very unlikely | 4.7% | Very unlikely | Thin or flat case for Atrisa at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $11M–$20M | $55M–$110M | 50% | 8.2% | Unlikely | 7.8% | Unlikely | Typical case for Atrisa at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $24M–$45M | $150M–$320M | 20% | 3.3% | Very unlikely | 3.1% | Very unlikely | Upside case for Atrisa at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series A needs paying design teams and evidence that agent output is accepted in tape out flows. The likely miss is that foundry PDKs are locked under NDA, customers will not share netlists with a startup, and pilots stay free. Silogy and Bronco show chip AI companies with no verified round beyond early funding, while Diode only reached A with a clear board design wedge.

### Series B: P(reach this round | in YC) = 28% after the previous step; 4.6% cumulative if in YC; 4.4% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $14M–$28M | $70M–$140M | 30% | 1.4% | Very unlikely | 1.3% | Very unlikely | Thin or flat case for Atrisa at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $32M–$55M | $170M–$330M | 50% | 2.3% | Very unlikely | 2.2% | Very unlikely | Typical case for Atrisa at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $65M–$130M | $450M–$1.1B | 20% | 0.9% | Very unlikely | 0.9% | Very unlikely | Upside case for Atrisa at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series B needs enterprise expansion across multiple customers and a defensible data moat. The likely stop is that Cadence and Synopsys ship agent features inside their tools, and analog customers are a small market of a few thousand teams, so growth flattens and the company becomes an acquisition target.

### Series C+: P(reach this round | in YC) = 25% after the previous step; 1.2% cumulative if in YC; 1.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $35M–$70M | $220M–$450M | 30% | 0.3% | Very unlikely | 0.3% | Very unlikely | Thin or flat case for Atrisa at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $80M–$140M | $550M–$1.1B | 50% | 0.6% | Very unlikely | 0.5% | Very unlikely | Typical case for Atrisa at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $180M–$450M | $1.5B–$4.5B | 20% | 0.2% | Very unlikely | 0.2% | Very unlikely | Upside case for Atrisa at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series C is a stretch in a niche tool market. The likely path ends with an acquisition by an EDA incumbent or a chip company, since customers buy through Cadence and Synopsys suites and few point tools grow past B. The records show very few comparable companies reaching this stage, and those that did had durable revenue and a defensible position, which this company would need to show well before then.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 57% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 30% | Reasonable | 28% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 12% | Unlikely | 11% | Unlikely |
| Acquired or IPO over $1B | $1B–$5B | 3.0% | Very unlikely | 2.8% | Very unlikely |

**Why it fails here.** The most common ending is a tools company that never gets past pilots, or a small acquisition by an EDA vendor. Analog design is a narrow market with slow sales, and the incumbents control the design flow and the licences. Analogs such as Silimate, Silogy and Bronco AI were Active but with no verified round beyond seed, while Rain Neuromorphics was acquired.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Analog design resists automation and agent output is not trusted for tape out. | 40% | Analog layout depends on process data and designer judgment that large language models handle poorly. | Silimate (silimate), Bronco AI (bronco-ai) | Start with a narrow verifiable task such as testbench generation and sizing for a single block family. |
| 2 | Cadence and Synopsys add agents inside their analog tools and control distribution. | 30% | Both incumbents have already announced AI features for design flows. | Silogy (silogy), JITX (jitx) | Partner with a foundry or design house and integrate into the incumbent flow rather than replace it. |
| 3 | Customers cannot share PDKs and netlists, so pilots stall. | 25% | Foundry design kits sit under NDA and chip teams are secretive. | Silogy (silogy) | Run on premise or in a customer virtual private cloud and use open PDKs for demos. |

## Pros

- **A scarce skill with expensive labor makes a clear value case.**: Analog designers are hard to hire. (https://www.cadence.com)
- **Investors already fund chip design AI.**: Silimate seed and Diode Series A. (https://www.ycombinator.com/companies/silimate)

## Roadmap

### Get into YC

Arrive at the batch with a sharp wedge and one named paying design partner.

1. Pick one narrow customer and workflow and write down the measurable result it should produce.
2. Sign a letter of intent or paid pilot before demo day.

You know it worked when: At least one pilot signed with a named buyer.

### Reach Seed

Show an agent that sizes and verifies a real analog block with a design partner.

1. Pick one circuit family such as op amps or bandgaps.
2. Work on open PDKs and publish benchmark results against expert designs.

You know it worked when: A seed round above the YC check from chip focused investors.

### Reach Series A

Convert pilots into paid annual contracts at two or more design teams.

1. Integrate with Cadence Virtuoso flows.
2. Hire a senior analog designer to review outputs.

You know it worked when: Two paid customers with measured designer hours saved.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 5 | Analog circuits need accurate simulation, layout awareness and foundry data. A three person team can build a narrow demo but producing production ready designs is a research problem. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Atrisa: Atrisa is an invented name with three syllables that is easy to spell and own, like many YC infrastructure names. It carries no meaning, which is fine for a tools company in a niche. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Cadence, Synopsys, Siemens EDA within ~18 months. The incumbents own the design environment and the foundry relationships and have the incentive to ship agents, but analog is hard enough that startups can lead for a time. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Cadence | Dominant analog and custom design suite with AI optimisation features. | Public EDA leader. | https://www.cadence.com |
| Synopsys | EDA leader with AI assisted design tools. | Public EDA leader. | https://www.synopsys.com |
| Silimate | YC agents for chip design and debug. | 2M seed in 2023. | https://www.ycombinator.com/companies/silimate |

### Demand evidence

- Analog designers are scarce and expensive, and chip design cycles are long, so tools that save engineer time have paying buyers. (https://www.cadence.com)
- Venture funding has flowed into AI chip design startups since 2023. (https://www.ycombinator.com/companies/silimate)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Silimate (silimate) | Summer 2023 | Active | Agents for chip design and debug, closest peer. | Summer 2023 batch, 2M seed in 2023, active with no later round in the record. |
| Silogy (silogy) | Winter 2024 | Active | AI debug platform for chip developers. | Winter 2024 batch, 500K recorded, no later round. |
| Diode Computers, Inc. (diode-computers-inc) | Summer 2024 | Active | AI circuit board design. | Summer 2024 batch, 11.4M Series A in 2025. |
| Bronco AI (bronco-ai) | Summer 2023 | Active | AI for ASIC verification. | Summer 2023 batch, pre seed only recorded. |
| JITX (jitx) | Summer 2018 | Active | Automatic circuit board design, early EDA player. | Summer 2018 batch, 12M Series A in 2022, four years after the batch. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 49% | 55% | python3 -I scripts/base_rates.py --years 2023-2025 --industry B2B : seed 42% / 49% / 56% (lower / known / upper), cond 49% (n=950) | Close to the 49 percent B2B anchor. Chip design AI is a funded theme (Silimate raised a 2M seed, Diode a 11.4M Series A) but a team of three with a deep technical product has a long path to a first demo. |
| Series A | 22% | 30% | same command: series_a 9% / 11% / 23%, cond 22% (n=465) | Slightly above the 22 percent anchor, within 1.4x: analog is a scarce specialty with expensive engineers, and acquirers such as Cadence and Synopsys pay for it, but sales cycles are long. |
| Series B | 20% | 28% | same command: series_b 2% / 2% / 16%, cond 20% (n=101) | Near the 20 percent anchor; chip design tools that reach A tend to keep growing through enterprise contracts. |
| Series C+ | 25% | 25% | same command: series_c 0% / 1% / 15%, cond 25% (n=20) | Near the 25 percent anchor; few EDA startups scale beyond B without being acquired. |

## Assumptions and limits

- No team background was given, so founder market fit is treated as unknown.
- Blind test: only the batch input file and market web searches were used; no company specific records. The seed step is read as a round above the standard YC deal of about 500K dollars within roughly 12 months of batch start.
- Extraction coverage is 662 of 6,399 companies researched in the calibration sample, plus recent cohort records; later cohorts are right censored, so base rates for 2023 to 2025 batches understate eventual progress.

## Sources

- https://www.ycombinator.com/deal
- https://www.equidam.com/?p=32620
- https://www.cadence.com
- https://www.synopsys.com
- https://www.ycombinator.com/companies/silimate
