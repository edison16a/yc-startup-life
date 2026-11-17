# Evaluation: OnDeck AI

*As of 2025-07-07. Mode: summary. Analyze any footage, without training a model*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Real early customers but a fast moving field; 45 percent for a seed above $1M in 16 months.**

**Chance of getting into YC:** 97% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$2.9M | $8M–$20M | 9.9% | Unlikely | 9.6% | Unlikely |
| Seed | $3M–$6M | $15M–$35M | 16% | Unlikely | 16% | Unlikely |
| Seed | $6M–$12M | $30M–$70M | 14% | Unlikely | 13% | Unlikely |
| Seed | $12M–$25M | $60M–$150M | 5.4% | Unlikely | 5.2% | Unlikely |
| Series A | $4M–$8M | $20M–$45M | 0.6% | Very unlikely | 0.6% | Very unlikely |
| Series A | $8M–$18M | $40M–$100M | 1.6% | Very unlikely | 1.5% | Very unlikely |
| Series A | $18M–$40M | $100M–$250M | 0.9% | Very unlikely | 0.9% | Very unlikely |
| Series B | $15M–$30M | $80M–$180M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $180M–$450M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $450M–$1B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

OnDeck sells a vision language model engine for video, with early defense and industrial customers and a six person team. The market is large, and a model that needs no training data is attractive, but frontier labs are improving video understanding quickly and procurement is slow. Inside a 16 month window a seed above $1M is slightly under the cohort anchor, adjusted down only for the window, and a Series A in the window is unlikely. The ladder does not rank this company above others. The biggest failure path is that general models become good enough that buyers see this as a feature.

## Round by round: where and why it fails

### Getting into YC: 97%

**How we got the number.** The input file places this company in the Summer 2025 batch, so acceptance is already known and this figure is reported for completeness only. The starting prior for a random applicant is about 1 percent (references/yc_acceptance.md, 0.6 to 2 percent third party range); the near certainty comes from the stated batch, not from a model of the company.

**Why it fails here.** YC is already past, so the only residual risk is a data error in the input about batch membership. Had the company been an ordinary applicant, the most plausible rejection reason would be: A crowded computer vision field where Gemini style models improve monthly, and a claim of beating the best VLMs that cannot be checked from the application.

### Seed: P(reach this round | in YC) = 45% after the previous step; 45% cumulative if in YC; 44% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$2.9M | $8M–$20M | 22% | 9.9% | Unlikely | 9.6% | Unlikely | Small post YC round of $1M to $3M, usually angels or a small seed fund. Canadian and defense angels often start with a $1M to $3M check. |
| $3M–$6M | $15M–$35M | 36% | 16% | Unlikely | 16% | Unlikely | Institutional seed of $3M to $6M, the modal outcome in 2022 and later data (median $3.5M to $4.1M in round_benchmarks.csv, which mixes in the YC deal). The central case is a $3M to $6M seed from an AI or defense tech fund. |
| $6M–$12M | $30M–$70M | 30% | 14% | Unlikely | 13% | Unlikely | Larger seed of $6M to $12M, where 42 percent of confirmed 2026 raises above $1M fell in the winners test. A defense contract plus a benchmark win over Gemini could pull a $6M to $12M round. |
| $12M–$25M | $60M–$150M | 12% | 5.4% | Unlikely | 5.2% | Unlikely | Upside band above $12M, reserved for a standout demo with a named lead. Requires a government contract or a large enterprise win. |

**Why it fails here.** Window of 16 months. The most likely miss is that general VLMs from Google and OpenAI improve quickly and make a specialised video model look like a feature, while defense and port customers move slowly through procurement. Visual One (AI for cameras) stopped at the YC cheque, and Traces and Aura Vision show small video AI firms that took years to raise more than $1M.

### Series A: P(reach this round | in YC) = 7.0% after the previous step; 3.2% cumulative if in YC; 3.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $20M–$45M | 20% | 0.6% | Very unlikely | 0.6% | Very unlikely | Thin or bridge style Series A below the 2022 and later median of $14M to $15M, the down or flat band. |
| $8M–$18M | $40M–$100M | 50% | 1.6% | Very unlikely | 1.5% | Very unlikely | Typical Series A near the 2022 and later quartiles ($11M to $21M raise). |
| $18M–$40M | $100M–$250M | 30% | 0.9% | Very unlikely | 0.9% | Very unlikely | Upside Series A led by a top tier fund once revenue is visible; current US medians are about $17M raise on $60M pre money. |

**Why it fails here.** A Series A inside 16 months needs repeat enterprise revenue beyond pilots; the median time to Series A is about 28 months. Tenyks raised a $3.4M seed and still sold into restaurants years later, and long government sales cycles delay the round. Investors will also want proof that revenue repeats rather than comes from one defense pilot, which a company only 16 months old rarely has.

### Series B: P(reach this round | in YC) = 1.5% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$180M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Flat or small Series B, near the 2018 to 2021 median of $32M but with a lower valuation. |
| $30M–$60M | $180M–$450M | 50% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series B, in line with the 2022 and later median of about $40M. |
| $60M–$120M | $450M–$1B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside Series B for a category leader; 2022 and later posts reach $600M to $1B. |

**Why it fails here.** A Series B inside 16 months would need enterprise revenue and a Series A first, and the median B2B path takes about three years from batch start (B2B median months to series B 47). Rescale, a simulation platform, took years of enterprise selling before its Series B. The likely failure is timing rather than a verdict on the idea.

### Series C+: P(reach this round | in YC) = 4.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series C at the 2022 and later median of $74M. |
| $80M–$150M | $700M–$2B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Growth round for a scaled leader, near the 2022 and later p75 of $103M. |
| $150M–$400M | $2B–$6B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside round for a breakout company; only a few percent of YC companies get here. |

**Why it fails here.** Series C inside 16 months is almost outside the data: the median is about five years after batch start, and only 8 companies in the 2022 and later cohort have reached it. Failing here means the company has not scaled past a niche or the window closed first, not that the idea is bad.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 56% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 23% | Reasonable | 22% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 16% | Unlikely | 16% | Unlikely |
| Acquired or IPO over $1B | $1B–$10B | 6.0% | Unlikely | 5.8% | Unlikely |

**Why it fails here.** Most paths end in a stall or a small sale because frontier labs and camera platform vendors can fold video understanding into broad products. Visual One and Sublime Black show small AI security firms that went inactive, while Tenyks and Aura Vision stayed independent and small.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Frontier VLMs from Google and OpenAI absorb the capability, leaving no moat for a specialised layer. | 40% | The description itself compares against Gemini, and general models improve quickly on video benchmarks. | Tenyks (tenyks), Visual One (visual-one) | Own the deployment layer for long footage and on premise defense use. |
| 2 | Defense and port customers have slow procurement so revenue stays at pilots. | 30% | National defense customers are listed, and procurement is long; AI video analytics is a $5B to $15B market but fragmented. | Traces (traces), Aura Vision (aura-vision) | Sign paid pilots with a prime contractor. |
| 3 | Camera platform vendors bundle analytics for free. | 25% | Security camera vendors and video platforms embed analytics in hardware. | Visual One (visual-one), Sublime Black (sublime-black) | Focus on the hard long video events they cannot detect. |

## Pros

- **Named enterprise and defense customers at batch start.**: Description lists defense, robotics, security and port monitoring customers. (https://www.polarismarketresearch.com/industry-analysis/video-analytics-market)
- **A research paper and a working model, with six people.**: NeurIPS workshop paper is stated in the input. (https://www.marketsandmarkets.com/Market-Reports/ai-in-video-surveillance-market-84216922.html)

## Roadmap

### Get into YC

A public benchmark win on long video understanding.

1. Publish results against Gemini on a named dataset.
2. Open a demo for defense and port teams.

You know it worked when: A benchmark table and two letters of intent.

### Reach Seed

Paid pilots that support a $3M to $6M seed.

1. Convert a defense or port pilot to paid.
2. Record per hour inference cost.

You know it worked when: Two paid pilots, about $200K ARR.

### Reach Series A

Repeat enterprise revenue.

1. Add a self serve API.
2. Get a security accreditation for government work.

You know it worked when: About $1M ARR across five customers.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Long video understanding with VLMs at low cost needs both model work and efficient inference; six people can ship a working engine but lag frontier labs in scale of training and evaluation. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 2 | OnDeck AI: The AI suffix is a generic tag many YC names use; the name collides with other companies called OnDeck in search, a real cost for findability, but B2B buyers weigh proof over names. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Google (Gemini), OpenAI, Axis and other camera makers, NVIDIA within ~9 months. General multimodal models already read video, so a competing feature within 9 months is plausible; the startup differs through long footage handling and deployment in sensitive settings. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Video analytics vendors and camera makers | Established analytics sold with cameras. | AI video analytics estimated at about $5B to $15B in 2025 depending on definition. | https://www.polarismarketresearch.com/industry-analysis/video-analytics-market |
| AI in video surveillance suppliers | Surveillance analytics with detection models that need training data. | Large market with many regional vendors. | https://www.marketsandmarkets.com/Market-Reports/ai-in-video-surveillance-market-84216922.html |
| Status quo: trained custom vision models | Teams collect data and train a model per task. | Takes months, the pain the company cites. | https://www.polarismarketresearch.com/industry-analysis/video-analytics-market |

### Demand evidence

- AI video analytics is estimated between about $5B and $15B in 2025 by different reports. (https://www.polarismarketresearch.com/industry-analysis/video-analytics-market)
- Zero shot detection is described as letting operators search in plain language instead of labeling data, a single vendor estimate of a small but fast growing niche. (https://marketintelo.com/report/vision-language-model-zero-shot-surveillance-analytics-market)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Aura Vision (aura-vision) | Winter 2019 | Active | Computer vision analytics sold to retailers, spun out of research. | Raised about 1.1M in 2019 after YC and later won enterprise chains, staying small and independent. |
| Tenyks (tenyks) | Summer 2021 | Active | Computer vision and video answering engine from a research team. | Raised a 3.4M seed in March 2022, then changed markets, showing that VLM style tools find buyers slowly. |
| Visual One (visual-one) | Winter 2020 | Inactive | AI for security cameras. | Only the 150K YC entry was found and it went inactive; depended on third party camera hardware. |
| Traces (traces) | Summer 2019 | Active | AI video monitoring for security. | Stayed active about ten staff with no priced round beyond YC found. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 45% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: seed known-only 61% (lower 50%, upper 68%), cond 61% (n=88). Median months to seed 9 (p25 4, p75 19); time_to_milestones.csv era 2022+ p75 is 14 months.  | Window is 16 months from the as_of date to 2026-11-17. The ever anchor of 61% counts the YC deal as a seed, but this forecast counts only a financing above about $1M from outside investors that closes inside the window, so the anchor is cut to cover only rounds above $1M and only the share that close within 16 months (about 75 to 80 percent of eventual seed raisers close by month 14 to 20). Customers in defense and industry are listed in the description, which is a mild positive, but I do not lift above the anchor; the Vancouver base slightly lowers US seed access, so the net stays near 0.75 of the ever anchor. Odds are not lifted for team or hot sector, per the winners test, and do not rank this company against others. |
| Series A | 33% | 7.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_a cond 33% (n=54), known-only 20%; months to series A median 30 (p25 22, p75 39). | The ever anchor is 33 percent, but only about a quarter of eventual Series A raisers have closed it by month 16 (p25 is 19 to 22 months from batch start), so the windowed value is much lower. Reaching a Series A in later years is common for companies with paying customers, but it falls outside this window. |
| Series B | 17% | 1.5% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_b cond 17% (n=18); median months to series B 46 overall, 35.5 for 2022 and later (n=40). | Median time to a Series B is about three years from batch start, so inside a 16 month window almost only extreme outliers get there; windowed probability is far below the 17 percent ever anchor. |
| Series C+ | 30% | 4.0% | python3 -I scripts/base_rates.py --calibration-only: series_c cond 36% (n=55) overall; B2B 2022-2024 cohort has 0 of 3 at Series C. Median months to series C about 61. | Series C normally lands about five years after the batch, so a window of 16 months makes it very unlikely; the ever anchor is cut to a token value. |

## Assumptions and limits

- Customer list and the benchmark claim come from the company description and are unverified.
- Blind forecast made as of 2025-07-07 for the window to 2026-11-17 (16 months). Seed means an outside round above about $1M closing in the window, not the standard YC deal of about $500K.
- Coverage limit: 662 of 6,399 companies are researched, and the B2B 2022-2024 cohort has 107 companies, so cohort rates are wide.
- Probabilities do not rank this company against others; the winners test found no separation between raisers and non-raisers.

## Sources

- https://www.polarismarketresearch.com/industry-analysis/video-analytics-market
- https://www.marketsandmarkets.com/Market-Reports/ai-in-video-surveillance-market-84216922.html
