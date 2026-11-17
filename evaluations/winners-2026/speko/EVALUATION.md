# Evaluation: Speko

*As of 2026-07-06. Mode: summary. OpenRouter for Voice AI: one API, every call on the best speech model*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A sharp but thin voice routing layer with real founder experience, likely to raise a small seed and then fight platform absorption.**

**Chance of getting into YC:** 95% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $6M–$15M | 15% | Unlikely | 14% | Unlikely |
| Seed | $2.5M–$6M | $15M–$38M | 30% | Reasonable | 28% | Reasonable |
| Seed | $8M–$16M | $45M–$100M | 15% | Unlikely | 14% | Unlikely |
| Series A | $4M–$9M | $22M–$45M | 4.0% | Very unlikely | 3.8% | Very unlikely |
| Series A | $11M–$20M | $55M–$110M | 6.6% | Unlikely | 6.3% | Unlikely |
| Series A | $24M–$45M | $150M–$320M | 2.6% | Very unlikely | 2.5% | Very unlikely |
| Series B | $14M–$28M | $70M–$140M | 0.9% | Very unlikely | 0.8% | Very unlikely |
| Series B | $32M–$55M | $170M–$330M | 1.5% | Very unlikely | 1.4% | Very unlikely |
| Series B | $65M–$130M | $450M–$1.1B | 0.6% | Very unlikely | 0.6% | Very unlikely |
| Series C+ | $35M–$70M | $220M–$450M | 0.2% | Very unlikely | 0.2% | Very unlikely |
| Series C+ | $80M–$140M | $550M–$1.1B | 0.3% | Very unlikely | 0.3% | Very unlikely |
| Series C+ | $180M–$450M | $1.5B–$4.5B | 0.1% | Very unlikely | 0.1% | Very unlikely |

## General assessment

Speko routes voice calls to the best speech model using public benchmarks. The founders have four years of production experience, and voice AI developer tools have raised seeds quickly. The risk is that routing is a feature: voice platforms and model vendors can copy it, and vendor pricing caps margin. The ladder follows B2B anchors with a higher seed and flat later steps, and exits by platform acquisition are the common path. The estimates are anchored on the 2023 to 2025 B2B cohort and adjusted only with the stated reasons, keeping each step within 0.75 times its anchor. Reaching a later round years after the batch is common for companies with paying customers, and a pivot followed by a raise is part of the upside band, so the ladder asks whether a round is reached and not how fast.

## Round by round: where and why it fails

### Getting into YC: 95%

**How we got the number.** Blind test: the company is already accepted to YC for its batch, so the acceptance estimate is a placeholder near certainty rather than a forecast. The unconditional prior for a random applicant is about 1 percent (0.6 to 2 percent, third party figures in yc_acceptance.md).

**Why it fails here.** Not applicable in this test because the company was accepted. Had it been assessed as an applicant, the most plausible reason for a no would be a thin routing layer with no clear moat against voice platforms. The founders would also need to show in the interview that they can ship quickly and have a specific first customer in mind, since YC weighs team speed and clear user need over market size.

### Seed: P(reach this round | in YC) = 60% after the previous step; 60% cumulative if in YC; 57% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $6M–$15M | 25% | 15% | Unlikely | 14% | Unlikely | Thin case for Speko at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $2.5M–$6M | $15M–$38M | 50% | 30% | Reasonable | 28% | Reasonable | Typical case for Speko at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $8M–$16M | $45M–$100M | 25% | 15% | Unlikely | 14% | Unlikely | Hot case for Speko at seed. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** The most plausible stop is that routing looks like a feature. Investors saw Vocode and Vapi raise small seeds and then face model vendors who give their own bundles, and a router that sits between customers and vendors has little pricing power. If the founders cannot show real traffic and a margin per call, a round above the YC check is hard.

### Series A: P(reach this round | in YC) = 22% after the previous step; 13% cumulative if in YC; 13% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$9M | $22M–$45M | 30% | 4.0% | Very unlikely | 3.8% | Very unlikely | Thin or flat case for Speko at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $11M–$20M | $55M–$110M | 50% | 6.6% | Unlikely | 6.3% | Unlikely | Typical case for Speko at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $24M–$45M | $150M–$320M | 20% | 2.6% | Very unlikely | 2.5% | Very unlikely | Upside case for Speko at series_a. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series A needs a few hundred thousand dollars of annual revenue and proof that customers stay when the routing gain is small. The likely miss is that voice platforms like Vapi and LiveKit add multi model routing themselves, and benchmarks are easy to copy, so the company cannot show a lasting edge.

### Series B: P(reach this round | in YC) = 22% after the previous step; 2.9% cumulative if in YC; 2.8% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $14M–$28M | $70M–$140M | 30% | 0.9% | Very unlikely | 0.8% | Very unlikely | Thin or flat case for Speko at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $32M–$55M | $170M–$330M | 50% | 1.5% | Very unlikely | 1.4% | Very unlikely | Typical case for Speko at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $65M–$130M | $450M–$1.1B | 20% | 0.6% | Very unlikely | 0.6% | Very unlikely | Upside case for Speko at series_b. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series B needs scale in voice minutes and gross margin after paying model vendors. The likely stop is that vendors cut prices or bundle, or that a platform acquires the router, so independence ends before a B. Past voice companies such as Vocode and PlayAI were acquired instead.

### Series C+: P(reach this round | in YC) = 22% after the previous step; 0.6% cumulative if in YC; 0.6% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $35M–$70M | $220M–$450M | 30% | 0.2% | Very unlikely | 0.2% | Very unlikely | Thin or flat case for Speko at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $80M–$140M | $550M–$1.1B | 50% | 0.3% | Very unlikely | 0.3% | Very unlikely | Typical case for Speko at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |
| $180M–$450M | $1.5B–$4.5B | 20% | 0.1% | Very unlikely | 0.1% | Very unlikely | Upside case for Speko at series_c_plus. Sized from the 2022+ YC round medians in stage_benchmarks.md and the current PitchBook and Carta ranges quoted there, with raise and post money set to what a company of this type and traction would plausibly price. |

**Why it fails here.** Series C requires a durable infrastructure position, such as becoming the default voice gateway. Few infrastructure routers reach that scale, and the likely end is acquisition by a voice platform or cloud vendor. The records show very few comparable companies reaching this stage, and those that did had durable revenue and a defensible position, which this company would need to show well before then.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 52% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 33% | Reasonable | 31% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 14% | Unlikely | 13% | Unlikely |
| Acquired or IPO over $1B | $1B–$5B | 3.0% | Very unlikely | 2.8% | Very unlikely |

**Why it fails here.** Most likely the company ends as an acquired feature or a small independent tool. Voice platforms control the customer and can add routing, while model vendors control price. Analogs such as Vocode and PlayAI exited by acquisition after a seed, and Lyrebird was also acquired, so the common path is a sale to a platform before a large round.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Routing is a feature that voice platforms and model vendors absorb. | 40% | Platforms like Vapi already select models and vendors publish their own bundles. | Vocode (vocode), Vapi (vapi) | Own the benchmark data and sell to enterprises that need vendor neutrality. |
| 2 | Margins are squeezed because model vendors set the cost. | 30% | Routers pay per minute to vendors and cannot control price. | AssemblyAI (assemblyai), PlayAI (playai) | Charge for evaluation and observability, not just usage. |
| 3 | Benchmarks are easy to copy and customers build their own evaluation. | 25% | Open evaluation tools for speech models already exist. and this was visible from the market at the batch start date. | Vocode (vocode) | Maintain proprietary language and domain test sets and ship new model results within a day. |

## Pros

- **Founders ran the same bake off for four years in production.**: Stated in the description input. (https://vapi.ai)
- **Voice AI is a fast growing category with funded peers.**: Seeds for Vapi, Vocode and Freya. (https://vapi.ai)

## Roadmap

### Get into YC

Arrive at the batch with a sharp wedge and one named paying design partner.

1. Pick one narrow customer and workflow and write down the measurable result it should produce.
2. Sign a letter of intent or paid pilot before demo day.

You know it worked when: At least one pilot signed with a named buyer.

### Reach Seed

Prove routing beats a fixed vendor on cost or quality for paying customers.

1. Publish the benchmarks and track wins per language.
2. Convert three voice agent builders to paid usage.

You know it worked when: A seed above the YC check with call volume disclosed.

### Reach Series A

Show revenue growth with positive gross margin after vendor costs.

1. Add evaluation and observability products.
2. Sign an enterprise contract that needs vendor neutrality.

You know it worked when: Monthly recurring revenue at or above 100K dollars.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Calling many speech APIs and measuring them is straightforward for a small team. The hard part is fair benchmarks across languages, latency under real calls and reliability of fallback. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Speko: Speko is short and hints at speech, a pattern used by Vapi and Vocode. It is easy to say and register. The name helps a little for a developer audience. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Vapi, LiveKit, ElevenLabs, Cloud vendors within ~6 months. Voice platforms have customers and can add routing in months, and the router depends on vendor APIs. A well resourced rival would need roughly the stated time and would have the incentive if the category proves valuable. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| OpenRouter | Model router for text LLMs, the template for the pitch. | Large developer usage and funding. | https://openrouter.ai |
| Vapi | Voice agent platform that lets users pick models. | Series A in late 2024. | https://vapi.ai |
| Deepgram and ElevenLabs | Speech vendors who sell direct APIs and bundles. | Well funded model providers. | https://elevenlabs.io |

### Demand evidence

- Voice agent usage is growing quickly and teams struggle to choose between many speech models. (https://vapi.ai)
- Text LLM routing shows developers pay for model choice and fallback. (https://openrouter.ai)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Vocode (vocode) | Winter 2023 | Acquired | Open source voice agent tooling, same buyers. | Winter 2023 batch, 3.25M seed in 2024, later acquired. |
| Vapi (vapi) | Winter 2021 | Active | Voice AI developer platform, a likely competitor and customer. | Winter 2021 batch, 2.1M seed in 2023 and 20M Series A in late 2024. |
| PlayAI (playai) | Winter 2023 | Acquired | Voice AI models and API. | Winter 2023 batch, 21M seed in 2024, later acquired. |
| AssemblyAI (assemblyai) | Summer 2017 | Active | Speech to text API company. | Summer 2017 batch, Series A in 2022 and Series B after. |
| Freya (freya) | Summer 2025 | Active | Voice AI for enterprises. | Summer 2025 batch, 3.5M seed in late 2025. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 49% | 60% | python3 -I scripts/base_rates.py --years 2023-2025 --industry B2B : seed 42% / 49% / 56% (lower / known / upper), cond 49% (n=950) | Above the 49 percent anchor but within 1.25x: developer tools in voice AI raise well (Vapi 2.1M seed, Vocode 3.25M, Freya 3.5M), and four years of production experience is real founder market fit. |
| Series A | 22% | 22% | same command: series_a 9% / 11% / 23%, cond 22% (n=465) | At the 22 percent anchor: a router tends to win usage quickly but gross margin pressure and model vendor moves cap Series A size. |
| Series B | 20% | 22% | same command: series_b 2% / 2% / 16%, cond 20% (n=101) | Near the 20 percent anchor; routers rarely get past A because they are thin layers. |
| Series C+ | 25% | 22% | same command: series_c 0% / 1% / 15%, cond 25% (n=20) | Near the 25 percent anchor; very few infrastructure layers of this type reach C. |

## Assumptions and limits

- Benchmark and traction claims are founder statements.
- Blind test: only the batch input file and market web searches were used; no company specific records. The seed step is read as a round above the standard YC deal of about 500K dollars within roughly 12 months of batch start.
- Extraction coverage is 662 of 6,399 companies researched in the calibration sample, plus recent cohort records; later cohorts are right censored, so base rates for 2023 to 2025 batches understate eventual progress.

## Sources

- https://www.ycombinator.com/deal
- https://www.equidam.com/?p=32620
- https://openrouter.ai
- https://vapi.ai
- https://elevenlabs.io
