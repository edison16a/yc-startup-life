# Evaluation: Interfaze

*As of 2026-04-06. Mode: summary. AI model built for high accuracy deterministic tasks*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Technically credible team in a crowded but real market, likely to raise a seed and then face commoditization pressure.**

**Chance of getting into YC:** 10% (range 5.0%–18%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$1.2M | $6M–$10M | 9.8% | Unlikely | 1.0% | Very unlikely |
| Seed | $1.5M–$3.5M | $12M–$25M | 32% | Reasonable | 3.2% | Very unlikely |
| Seed | $4M–$8M | $25M–$50M | 23% | Reasonable | 2.3% | Very unlikely |
| Series A | $8M–$12M | $40M–$70M | 6.4% | Unlikely | 0.6% | Very unlikely |
| Series A | $12M–$22M | $60M–$110M | 11% | Unlikely | 1.1% | Very unlikely |
| Series A | $25M–$40M | $150M–$300M | 4.3% | Very unlikely | 0.4% | Very unlikely |
| Series B | $20M–$35M | $150M–$250M | 1.9% | Very unlikely | 0.2% | Very unlikely |
| Series B | $35M–$60M | $250M–$500M | 3.2% | Very unlikely | 0.3% | Very unlikely |
| Series B | $70M–$120M | $600M–$1.2B | 1.3% | Very unlikely | 0.1% | Very unlikely |
| Series C+ | $50M–$80M | $500M–$900M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $900M–$2B | 0.9% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$300M | $2B–$5B | 0.4% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Interfaze is an API model for deterministic tasks such as document extraction. A research paper and open benchmarks make it a good fit for fast AI infrastructure seeds in 2026. The risk is commoditization: cloud services and frontier models keep improving, benchmarks are vendor authored and customers can switch easily. The document AI analogs show the category funds a few winners and leaves others small. A seed is likelier than not, Series A is roughly one in three and the base case is a small acquisition or a narrower pivot.

## Round by round: where and why it fails

### Getting into YC: 10%

**How we got the number.** Test note: the company was accepted, so this is an if accepted view. A blind prior starts near 1 percent, and the factors in the YC acceptance table are applied loosely here. Not part of the scored test.

**Why it fails here.** YC might decline because the claim to beat frontier models on benchmarks the company chose is easy to doubt, and document extraction is crowded with funded startups and cloud giants. Interviewers may see no clear buyer or revenue and a wedge that general models improve into.

### Seed: P(reach this round | in YC) = 65% after the previous step; 65% cumulative if in YC; 6.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$1.2M | $6M–$10M | 15% | 9.8% | Unlikely | 1.0% | Very unlikely | Small round just above the YC check, mostly angels, if traction is thin. |
| $1.5M–$3.5M | $12M–$25M | 50% | 32% | Reasonable | 3.2% | Very unlikely | Typical 2022+ B2B seed with about 3.2M median in the cohort and market seed pre money near 18M. |
| $4M–$8M | $25M–$50M | 35% | 23% | Reasonable | 2.3% | Very unlikely | Hot round led by a top fund on strong credentials and a fast demo. |

**Why it fails here.** A round above the YC check fails if developers try the API and stay on cheaper frontier models, or if benchmark wins are not reproduced on customers' own documents. Analogs like pulse-3 and extend raised only with paying customers, so an AI infrastructure story without revenue could stall.

### Series A: P(reach this round | in YC) = 33% after the previous step; 21% cumulative if in YC; 2.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $8M–$12M | $40M–$70M | 30% | 6.4% | Unlikely | 0.6% | Very unlikely | Modest Series A at current medians near 17M raise and 60M pre, shaded down for slower sales. |
| $12M–$22M | $60M–$110M | 50% | 11% | Unlikely | 1.1% | Very unlikely | Core case, 2022+ B2B cohort median Series A of about 15M. |
| $25M–$40M | $150M–$300M | 20% | 4.3% | Very unlikely | 0.4% | Very unlikely | Breakout traction earns a premium Series A in a hot category. |

**Why it fails here.** Series A fails if usage stays low volume and pricing falls with token costs. Frontier labs add structured outputs and cheaper vision models every quarter, and the narrow accuracy edge may close before the company builds a moat in customer data or workflows. Peers in document AI such as pulse-3, extend and veryfi-inc show that revenue and customer references, not benchmark scores alone, decide who raises the next round.

### Series B: P(reach this round | in YC) = 30% after the previous step; 6.4% cumulative if in YC; 0.6% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$35M | $150M–$250M | 30% | 1.9% | Very unlikely | 0.2% | Very unlikely | Flat or modest Series B, a thin round after growth slows, near the low end of 2022+ medians. |
| $35M–$60M | $250M–$500M | 50% | 3.2% | Very unlikely | 0.3% | Very unlikely | Median 2022+ Series B of about 45M in the cohort, matching current market deal sizes near 40M. |
| $70M–$120M | $600M–$1.2B | 20% | 1.3% | Very unlikely | 0.1% | Very unlikely | Category leader premium round when growth is clearly outpacing peers in a hot market. |

**Why it fails here.** Series B fails if the product stays an API commodity competing on price with Google, Microsoft and Mistral. Investors want revenue near ten million and enterprise contracts, and customers can switch easily. Peers in document AI such as pulse-3, extend and veryfi-inc show that revenue and customer references, not benchmark scores alone, decide who raises the next round.

### Series C+: P(reach this round | in YC) = 30% after the previous step; 1.9% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $50M–$80M | $500M–$900M | 35% | 0.7% | Very unlikely | <0.1% | Very unlikely | Standard Series C near the 2022+ median of about 45M to 80M raise for researched companies. |
| $80M–$150M | $900M–$2B | 45% | 0.9% | Very unlikely | <0.1% | Very unlikely | Leader round with a larger raise as the company becomes a category name. |
| $150M–$300M | $2B–$5B | 20% | 0.4% | Very unlikely | <0.1% | Very unlikely | Hypergrowth premium round with a very large valuation, rare in the researched data. |

**Why it fails here.** Series C fails if the model market commoditizes and the company never owns data or distribution. Only a few AI infrastructure companies reach C, and valuations depend on breakout growth. Peers in document AI such as pulse-3, extend and veryfi-inc show that revenue and customer references, not benchmark scores alone, decide who raises the next round.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 95% | Very likely |
| Acquired or IPO under $100M | $10M–$100M | 25% | Reasonable | 2.5% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 18% | Unlikely | 1.8% | Very unlikely |
| Acquired or IPO over $1B | $1B–$5B | 7.0% | Unlikely | 0.7% | Very unlikely |

**Why it fails here.** The most likely failure is that general models and cloud document services catch up on accuracy and drive price down, so a small team cannot defend margin. An acquisition by a larger AI platform for the team and model is a common middle result. Peers in document AI such as pulse-3, extend and veryfi-inc show that revenue and customer references, not benchmark scores alone, decide who raises the next round.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Frontier models and cloud services close the accuracy gap | 45% | Mistral OCR, Google Document AI and Gemini vision all improve and cut price, and benchmark vendors disagree on rankings. | Nyckel (nyckel), Theta (theta) | Focus on determinism and per customer fine tuning. |
| 2 | Benchmarks chosen by the company do not convince buyers | 30% | Most OCR benchmarks are vendor authored and failure rate or determinism is rarely measured independently. | Pulse (pulse-3) | Offer bake offs on customer documents. |
| 3 | Commodity API pricing falls | 30% | Reported per page prices range widely, from near zero to several dollars per thousand pages. | Veryfi, Inc. (veryfi-inc) | Move up to workflows and vertical solutions. |
| 4 | Unclear go to market for a general model across many tasks | 25% | The description spans documents, objects and audio with no single buyer. | Theta (theta) | Pick one wedge such as document extraction. |

## Pros

- **Technical depth with a public architecture paper and open benchmarks**: The YC text links an arXiv paper and public leaderboards. (https://interfaze.ai)
- **Real paid demand for accurate document extraction**: Many funded vendors and cloud services compete in this market. (https://reducto.ai/blog/best-ocr-apis-complex-documents-2026)

## Roadmap

### Get into YC

Show independent evidence of the accuracy edge.

1. Publish reproducible benchmarks
2. Collect user quotes

You know it worked when: Third party reproduction of results

### Reach Seed

Convert API trials to paying usage.

1. Offer free bake offs
2. Add self serve billing

You know it worked when: 20 paying developers and 20K MRR

### Reach Series A

Build revenue and a moat beyond accuracy.

1. Pick one vertical
2. Add customer fine tuning

You know it worked when: 1M ARR and low churn

### Reach Series B

Move up to enterprise contracts.

1. Add compliance
2. Hire sales

You know it worked when: 10M ARR

### Reach Series C and beyond

Become infrastructure standard for deterministic AI.

1. Expand modalities
2. Partner with clouds

You know it worked when: 50M ARR

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Merging specialized vision and audio models with transformers into one API that is accurate and consistent needs real research and training data, which the paper suggests the team has. A five person team can build a competitive document model but scaling across many tasks is hard. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Interfaze: Invented names are the largest group in the name tables with no outcome penalty. It suggests an interface to models, which fits an API, and it is easy to say. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Google, Mistral, OpenAI, Reducto within ~9 months. Labs and cloud vendors already ship OCR and structured extraction, and a well funded rival could match the accuracy in a few quarters. Incentive is high since document processing is a large enterprise workload. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Reducto | Document parsing API with published table benchmark. | Funded leader per its own materials. | https://reducto.ai/blog/best-ocr-apis-complex-documents-2026 |
| Google Document AI, Azure, AWS Textract | Cloud document extraction services. | Broadly deployed by enterprises. | https://reducto.ai/compare/reducto-vs-google-document-ai |
| Mistral OCR and frontier vision models | LLM based OCR. | Widely used by developers. | https://artificialanalysis.ai/agents/ocr |

### Demand evidence

- Enterprises pay for document processing, with many vendors competing on accuracy and price per thousand pages. (https://reducto.ai/blog/best-ocr-apis-complex-documents-2026)
- Accuracy and consistency are open problems across vendors and not independently benchmarked. (https://artificialanalysis.ai/agents/ocr)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Pulse (pulse-3) | Summer 2024 | Active | Production grade document extraction API. | Active; competes with large and small vendors in the same wedge. |
| Extend (extend) | Winter 2023 | Active | Production ready document processing. | Active and raised venture rounds after its batch, a sign document AI can fund. |
| Veryfi, Inc. (veryfi-inc) | Winter 2017 | Active | Document AI API founded in 2017. | Still active, slow and steady, showing the market supports multiple vendors. |
| Nyckel (nyckel) | Winter 2022 | Active | Classify anything API. | Active small company; shows classification APIs struggled to become large. |
| Theta (theta) | Spring 2025 | Active | Specialized AI for every job. | Active without a large public round, showing specialized model pitches face a hard sell. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 65% | Ran python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed 49 / 59 / 65 percent (lower, known, upper), series A 13 / 15 / 29 with cond 26 percent (n=74), series B cond 16 percent (n=19), series C cond 0 percent (n=3, too small). Broad cohort also checked with --industry B2B --years 2018-2021: seed cond 81, A cond 32, B cond 39, C cond 57 percent. | Set above the 59 percent anchor because a five person team with a research paper and open benchmarks in AI infrastructure is the kind that raised quickly in 2025 and 2026. The seed step here means a round above the standard 500K YC deal within about 12 months, and the anchor is for any seed ever, so the 12 month window pulls it down while a hot category pushes it up. |
| Series A | 26% | 33% | Ran python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed 49 / 59 / 65 percent (lower, known, upper), series A 13 / 15 / 29 with cond 26 percent (n=74), series B cond 16 percent (n=19), series C cond 0 percent (n=3, too small). Broad cohort also checked with --industry B2B --years 2018-2021: seed cond 81, A cond 32, B cond 39, C cond 57 percent. | Set above the 26 percent cohort conditional because the team shows technical depth and AI infrastructure A rounds were frequent, with document AI peers like extend raising. |
| Series B | 16% | 30% | Ran python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed 49 / 59 / 65 percent (lower, known, upper), series A 13 / 15 / 29 with cond 26 percent (n=74), series B cond 16 percent (n=19), series C cond 0 percent (n=3, too small). Broad cohort also checked with --industry B2B --years 2018-2021: seed cond 81, A cond 32, B cond 39, C cond 57 percent. Series B cond 16 percent for B2B 2022+. | Above recent cohort because the older cohort is about 39 percent and infrastructure leaders raise large B rounds. |
| Series C+ | 5.0% | 30% | Ran python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed 49 / 59 / 65 percent (lower, known, upper), series A 13 / 15 / 29 with cond 26 percent (n=74), series B cond 16 percent (n=19), series C cond 0 percent (n=3, too small). Broad cohort also checked with --industry B2B --years 2018-2021: seed cond 81, A cond 32, B cond 39, C cond 57 percent. No usable C sample. | Anchor unusable; broader all industry conditional about 36 percent, discounted for commodity risk. The step is set above a thin and censored cohort number because companies with paying customers often raise years later, and the broader conditional rate is higher. |

## Assumptions and limits

- Blind test: only the YC listing text was used for the company itself.
- Seed means more than 500K within about 12 months of batch start; cohort anchors are for any seed ever.
- Recent batches are right censored in the base rates.
- Web results dated after the batch start were ignored.

## Sources

- https://reducto.ai/blog/best-ocr-apis-complex-documents-2026
- https://reducto.ai/compare/reducto-vs-google-document-ai
- https://artificialanalysis.ai/agents/ocr
- https://interfaze.ai
