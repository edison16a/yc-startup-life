# Evaluation: .Wave

*As of 2025-01-06. Mode: summary. Inference for real-time AI*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A credible two person inference team in a capital heavy category; seed in 22 months is near a coin flip.**

**Chance of getting into YC:** 3.0% (range 1.5%–6.6%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $10M–$22M | 14% | Unlikely | 0.4% | Very unlikely |
| Seed | $3M–$6M | $18M–$40M | 17% | Unlikely | 0.5% | Very unlikely |
| Seed | $6M–$12M | $35M–$80M | 9.9% | Unlikely | 0.3% | Very unlikely |
| Seed | $12M–$25M | $70M–$150M | 4.5% | Very unlikely | 0.1% | Very unlikely |
| Series A | $6M–$10M | $35M–$60M | 1.6% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$20M | $60M–$120M | 2.8% | Very unlikely | <0.1% | Very unlikely |
| Series A | $20M–$40M | $120M–$250M | 1.9% | Very unlikely | <0.1% | Very unlikely |
| Series B | $20M–$35M | $120M–$220M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series B | $35M–$70M | $220M–$500M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $70M–$150M | $500M–$1.2B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$200M | $700M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $200M–$500M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

.Wave offers dedicated and scheduled inference capacity for real time voice workloads, plus streaming speech models on its own engine, from a two person Paris team. The need is real since voice agents live and die on tail latency, but the field includes Deepgram, AssemblyAI, the clouds and funded inference providers, and GPU heavy models need capital. For the 22 month window I put the seed at 0.45, near the window adjusted anchor of about 0.45, with no lift because the winners test showed hot sectors did not separate outcomes. If it raises, a $3M to $6M seed is most likely. A Series A inside the window is 0.14 because 22 months is nearly the median time to an A. The key risks are margin squeeze and a two person team serving production traffic.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Already in the Winter 2025 batch, so this is the prior for a random applicant. YC cites about 1 percent acceptance with a third party range of 0.6 to 2 percent. I put it at 3 percent for a technical two person team building an inference engine in a hot infrastructure area, offset by the capital needs and by many applicants proposing GPU or inference products.

**Why it fails here.** YC would most plausibly decline because inference infrastructure was among the most crowded and capital hungry categories in late 2024, with Together, Fireworks, Baseten and cloud vendors, and a two person team without public usage numbers must show why it beats them on latency and price, not only claim it.

### Seed: P(reach this round | in YC) = 45% after the previous step; 45% cumulative if in YC; 1.4% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $10M–$22M | 30% | 14% | Unlikely | 0.4% | Very unlikely | Small post YC round: a $1M to $3M check from angels, a pre-seed fund or a YC partner fund, the usual outcome when the product is early and a team is small. |
| $3M–$6M | $18M–$40M | 38% | 17% | Unlikely | 0.5% | Very unlikely | Institutional seed from a dev or AI focused fund, the cohort median region for 2022 and later seed rounds ($3.1M median, quartiles $2.0M and $4.2M in the Developer Tools cohort). |
| $6M–$12M | $35M–$80M | 22% | 9.9% | Unlikely | 0.3% | Very unlikely | Larger institutional seed on strong early usage or a hot category; among confirmed 2026 raises above $1M the median was $6.0M, so this band is realistic but press skewed. |
| $12M–$25M | $70M–$150M | 10% | 4.5% | Very unlikely | 0.1% | Very unlikely | Upside seed or seed plus led by a top tier fund on fast growth; rare and usually tied to revenue or breakout open source or product adoption. |

**Why it fails here.** Seed means a round above $1M from outside investors within 22 months. It most likely fails if the dedicated capacity model reads as a GPU reseller with thin margins next to Together, Fireworks, Baseten and the clouds, and the speech API looks like one more voice model next to Deepgram and AssemblyAI. Pipeshift and Shadeform raised only small seeds, so investors may see few comparable breakouts.

### Series A: P(reach this round | in YC) = 14% after the previous step; 6.3% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $35M–$60M | 25% | 1.6% | Very unlikely | <0.1% | Very unlikely | Thin or flat Series A under $10M, common when growth is real but revenue is early and the lead wants a smaller bet. |
| $10M–$20M | $60M–$120M | 45% | 2.8% | Very unlikely | <0.1% | Very unlikely | Typical 2022 and later Series A: the Developer Tools cohort median raise is $17.5M and the B2B cohort median $15.0M. |
| $20M–$40M | $120M–$250M | 30% | 1.9% | Very unlikely | <0.1% | Very unlikely | Upside Series A led by a large fund when the product is a visible category leader with fast revenue, as seen for the best AI infrastructure and developer rounds of 2024 and 2025. |

**Why it fails here.** A Series A inside 22 months needs usage revenue large enough to show a path to tens of millions, in a market where Deepgram, AssemblyAI and the model labs set the price per minute and GPU costs eat margin. Vapi and Deepgram had product market fit with developers before their rounds; a two person team must show reserved capacity contracts that are recurring and profitable.

### Series B: P(reach this round | in YC) = 8.0% after the previous step; 0.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$35M | $120M–$220M | 30% | 0.2% | Very unlikely | <0.1% | Very unlikely | Modest Series B on steady growth, below the Developer Tools median of $50M because few companies in the cohort have reached this round. |
| $35M–$70M | $220M–$500M | 50% | 0.3% | Very unlikely | <0.1% | Very unlikely | Typical 2022 and later Series B: $45M to $50M medians with valuations near $550M to $600M in the few cohort cases with data. |
| $70M–$150M | $500M–$1.2B | 20% | 0.1% | Very unlikely | <0.1% | Very unlikely | Breakout round for a category leader growing several times a year. |

**Why it fails here.** A Series B inside the window would need a Series A and rapid scaling of reserved capacity customers. Infrastructure companies with Series B rounds in the cohort had large revenue and GPU commitments, and a two person team would need to triple its headcount twice in two years while holding gross margin against hyperscalers.

### Series C+: P(reach this round | in YC) = 5.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Ordinary growth round for a company that has found a repeatable sales motion. |
| $80M–$200M | $700M–$2B | 45% | <0.1% | Very unlikely | <0.1% | Very unlikely | Large growth round from crossover or late stage funds in a hot AI category. |
| $200M–$500M | $2B–$6B | 15% | <0.1% | Very unlikely | <0.1% | Very unlikely | Category defining round, seen only for the top few AI companies. |

**Why it fails here.** A Series C inside two years of a batch would require a breakout like the largest inference providers. Capital intensity and price competition from clouds and model labs make that very unlikely for a two person start, and only a handful of AI infrastructure companies have done it that fast.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $10M–$100M | 22% | Reasonable | 0.7% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 17% | Unlikely | 0.5% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 6.0% | Unlikely | 0.2% | Very unlikely |

**Why it fails here.** The usual end is a GPU capacity business squeezed on margin: hyperscalers and funded inference clouds undercut reserved capacity, and model providers ship their own real-time APIs. Pipeshift raised a small seed and PlayAI sold into the voice model market, so a partial acquisition or acqui-hire is a more likely good result than a standalone win.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Margin squeeze from GPU clouds and inference rivals | 45% | Reserved GPU capacity is a commodity sold by hyperscalers and inference clouds, so a two person team has little pricing power unless its engine is much faster. | Shadeform (shadeform), Pipeshift (pipeshift) | Publish latency and cost benchmarks on streaming speech that beat the clouds and lock customers with scheduled capacity contracts. |
| 2 | Speech and voice API competition from larger vendors | 35% | Deepgram and AssemblyAI each reached Series C selling speech APIs, and cloud providers and model labs sell streaming speech at low prices. | Deepgram (deepgram), AssemblyAI (assemblyai) | Position as the infrastructure under voice agents and sell dedicated lanes, not per-minute transcription. |
| 3 | Capital intensity before revenue | 30% | Dedicated inference needs GPU commitments before customers sign, so a seed is both required and harder to raise without revenue. | Shadeform (shadeform), Vapi (vapi) | Use customer prepayments and spot capacity partners to avoid owning GPUs. |
| 4 | Two person team can't serve production customers | 25% | Real-time workloads need 24 hour support and operations, which a two person team in Paris cannot sustain at scale. | Pipeshift (pipeshift), PlayAI (playai) | Hire an infrastructure engineer and a sales lead after the first design partners. |

## Pros

- **A concrete pricing wedge**: Paying only for reserved windows removes idle GPU cost, which is a real pain for voice workloads with daily peaks.
- **Technical depth**: The team ships its own inference engine rather than wrapping a third party model, which gives room for a performance edge.

## Roadmap

### Get into YC

Show a latency and cost advantage on a real voice workload.

1. Run a head to head benchmark against two cloud speech APIs.
2. Sign two voice agent companies as design partners.

You know it worked when: Measured p99 latency and cost per hour better than cloud endpoints at a design partner.

### Reach Seed

Turn design partners into recurring reserved capacity contracts.

1. Sell scheduled capacity with a three month minimum.
2. Reach positive gross margin on each lane.

You know it worked when: $40K or more monthly recurring revenue from reserved capacity with gross margin above 40 percent.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 5 | Building a custom inference engine for streaming speech and full duplex voice, scheduling capacity across lanes and keeping tail latency low is genuinely hard. A two person team with strong inference skills can build a demo in three months, but production grade reliability across customers and GPU supply is a risk. |
| Name and brand (5 = iconic, drives growth; effect on success: hurts) | 2 | .Wave: A short real word links to audio, which suits speech, but the leading dot hurts search, email and domain use and the word wave is crowded; dotwave.ai is the working domain. Short plain names such as Vapi worked because they are easy to say and type. A mild drag on discovery. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Deepgram, AWS, Google and Azure speech services, OpenAI realtime API, Together and Fireworks within ~9 months. Model labs and clouds already ship real-time voice APIs and could add reserved capacity pricing. A specialist needs about nine months to match a narrow offering, so the moat is engine performance and contract structure. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Deepgram | Streaming speech recognition and voice agent APIs. | Series C stage with a public price list per minute. | https://deepgram.com/pricing |
| AssemblyAI | Speech to text API for developers. | Series C stage per the repo records. | https://www.assemblyai.com/ |
| Cloud GPU and inference providers | Shared and dedicated GPU endpoints from hyperscalers and inference clouds. | Vendors claim shared pools have tail latency problems that dedicated endpoints fix. | https://www.gmicloud.ai/en/blog/low-latency-inference-for-speech-and-audio-applications |

### Demand evidence

- Real-time voice agents need low and predictable latency, and vendors argue shared GPU pools cannot bound tail latency, which supports demand for dedicated capacity. (https://www.gmicloud.ai/en/blog/low-latency-inference-for-speech-and-audio-applications)
- Streaming speech recognition is sold per minute by Deepgram, showing paid demand and price pressure. (https://deepgram.com/pricing)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Deepgram (deepgram) | Winter 2016 | Active | Speech recognition infrastructure and the incumbent in streaming ASR. | Winter 2016, reached Series C after years of enterprise and developer revenue; shows the scale and time needed. |
| AssemblyAI (assemblyai) | Summer 2017 | Active | Speech to text API company. | Summer 2017, reached Series C, a long path with heavy model investment. |
| Pipeshift (pipeshift) | Summer 2024 | Active | Inference for real-time agents, Summer 2024, a very close wedge. | Raised a small seed by the as_of date, showing what peers raise. |
| Shadeform (shadeform) | Summer 2023 | Active | GPU cloud marketplace, a capacity reseller. | Summer 2023, a seed, shows capacity marketplaces raise small rounds. |
| Vapi (vapi) | Winter 2021 | Active | Voice AI for developers, a likely customer. | Winter 2021, grew fast on developer demand and had a Series A and B; shows the voice pull for infrastructure. |
| PlayAI (playai) | Winter 2023 | Acquired | Voice AI models, Winter 2023. | Raised a seed; a model company that depended on selling into the voice market. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 56% | 45% | python3 -I scripts/base_rates.py --tag Infrastructure --years 2022-2025 --calibration-only: seed 45% / 56% / 64% (n=9, thin); python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed 59% known-only (n=126). Timing from knowledge/tables/time_to_milestones.csv era 2022+: months_to_seed p25 3, p50 6, p75 14.2 (n=1146). | Window is about 22 months (2025-01-06 to 2026-11-17). Roughly 80 percent of eventual seeds close within 22 months on the 2022 and later timing table, so the window anchor is about 0.45 from the 0.56 infrastructure figure. I keep it at 0.45 with no lift: a two person team in Paris with deep inference work is credible, but GPU heavy infrastructure needs capital that makes a seed more necessary and also harder to justify. The odds do not rank this company against others. |
| Series A | 20% | 14% | python3 -I scripts/base_rates.py --tag Infrastructure --years 2022-2025 --calibration-only: series_a cond 20% (n=5, thin); B2B 2022-2025 calibration only: series_a cond 26% (n=74). Timing, era 2022+: months_to_series_a p25 19.4, p50 28, p75 38.4 (n=216). | The anchor is the chance of ever reaching Series A, with a median of 28 months after batch start; the window is 22 months so most Series As are still ahead, and a seed is needed first. I cut the anchor by about 30 percent, which stays inside the limit; infrastructure companies with real revenue from usage can raise an A within two years, as speech API leaders did. |
| Series B | 16% | 8.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: series_b cond 16% (n=19), range 2% to 18% across lower, known and upper. | The anchor is the chance of ever reaching Series B. In a window that ends about 13 to 22 months after the batch starts, the time to milestone table gives a median of about 35 months for Series B in the 2022 and later era, so only a small share of eventual Series B companies get there inside the window; I cut the anchor roughly in half and say the number is a window number. |
| Series C+ | none | 5.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: series_c 0% known-only, 16% upper (n=3), so there is no usable rate for the cohort. | The cohort has almost no Series C companies, so I use a small number tied to the window length: reaching Series C within about two years of a YC batch has happened only for a handful of breakout companies in the 2022 and later era, and the time to milestone table shows a median of about 37 months. |

## Assumptions and limits

- Blind forecast as of 2025-01-06 for about 22 months to 2026-11-17; seed means above about $1M from outside investors.
- Only the input file was used for the company; market searches returned pages after the as_of date and these were ignored.
- The Infrastructure tag cohort has only 9 calibration companies, so I leaned on the B2B cohort and timing table.
- Company already in YC; the YC odds are the prior for a random applicant.
- The input description mentions dedicated lanes and a streaming API; I assume they were available around the as_of date.

## Sources

- https://deepgram.com/pricing
- https://www.gmicloud.ai/en/blog/low-latency-inference-for-speech-and-audio-applications
- https://www.assemblyai.com/
