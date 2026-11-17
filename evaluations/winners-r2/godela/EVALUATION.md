# Evaluation: Godela

*As of 2025-04-07. Mode: summary. AI Physics Engine to replace simulations and prototypes*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A credible but crowded physics AI bet whose seed depends on trust in accuracy; 46 percent for a seed above $1M inside 19 months.**

**Chance of getting into YC:** 97% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$2.9M | $8M–$20M | 10% | Unlikely | 9.8% | Unlikely |
| Seed | $3M–$6M | $15M–$35M | 17% | Unlikely | 16% | Unlikely |
| Seed | $6M–$12M | $30M–$70M | 14% | Unlikely | 13% | Unlikely |
| Seed | $12M–$25M | $60M–$150M | 5.5% | Unlikely | 5.4% | Unlikely |
| Series A | $4M–$8M | $20M–$45M | 0.9% | Very unlikely | 0.9% | Very unlikely |
| Series A | $8M–$18M | $40M–$100M | 2.3% | Very unlikely | 2.2% | Very unlikely |
| Series A | $18M–$40M | $100M–$250M | 1.4% | Very unlikely | 1.3% | Very unlikely |
| Series B | $15M–$30M | $80M–$180M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $180M–$450M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $450M–$1B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Godela sells an AI physics engine to engineers. The market is large and incumbents are adding AI, so need is real, but trust and a funded field make progress slow. Over a window of 19 months a seed above $1M is a bit under even odds, in line with the B2B cohort, and a Series A in the window is unlikely because the median time is about 28 months. The ladder does not rank this company above others. The most likely single failure is that engineers will not swap a certified solver for an AI estimate, so the company must win one narrow vertical with published accuracy before it widens.

## Round by round: where and why it fails

### Getting into YC: 97%

**How we got the number.** The input file places this company in the Spring 2025 batch, so acceptance is already known and this figure is reported for completeness only. The starting prior for a random applicant is about 1 percent (references/yc_acceptance.md, 0.6 to 2 percent third party range); the near certainty comes from the stated batch, not from a model of the company.

**Why it fails here.** YC is already past, so the only residual risk is a data error in the input about batch membership. Had the company been an ordinary applicant, the most plausible rejection reason would be: Founders with no verified domain pedigree proposing to replace certified simulation solvers with AI, a technically heavy claim with crowded funded rivals and no stated customers.

### Seed: P(reach this round | in YC) = 46% after the previous step; 46% cumulative if in YC; 45% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$2.9M | $8M–$20M | 22% | 10% | Unlikely | 9.8% | Unlikely | Small post YC round of $1M to $3M, usually angels or a small seed fund. Hard tech investors often write a first $1M to $3M check while waiting for customer data. |
| $3M–$6M | $15M–$35M | 36% | 17% | Unlikely | 16% | Unlikely | Institutional seed of $3M to $6M, the modal outcome in 2022 and later data (median $3.5M to $4.1M in round_benchmarks.csv, which mixes in the YC deal). Physics AI is a funded category, so a $3M to $6M seed from a deep tech fund is the central case. |
| $6M–$12M | $30M–$70M | 30% | 14% | Unlikely | 13% | Unlikely | Larger seed of $6M to $12M, where 42 percent of confirmed 2026 raises above $1M fell in the winners test. A 10 person team with a working engine could attract a $6M to $12M round from a top fund. |
| $12M–$25M | $60M–$150M | 12% | 5.5% | Unlikely | 5.4% | Unlikely | Upside band above $12M, reserved for a standout demo with a named lead. Only with a named aerospace customer and strong accuracy benchmarks. |

**Why it fails here.** Window of 19 months. The most likely miss is that investors want proof that engineers trust AI results in place of certified solvers such as Ansys, and a spring batch company has about four months of evidence by demo day. Pathmind (shutdown after a Series A) and Vorticity (Series A only three years after batch) show that simulation tooling raises slowly and on technical proof. A raise can also slip past the window.

### Series A: P(reach this round | in YC) = 10% after the previous step; 4.6% cumulative if in YC; 4.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $20M–$45M | 20% | 0.9% | Very unlikely | 0.9% | Very unlikely | Thin or bridge style Series A below the 2022 and later median of $14M to $15M, the down or flat band. |
| $8M–$18M | $40M–$100M | 50% | 2.3% | Very unlikely | 2.2% | Very unlikely | Typical Series A near the 2022 and later quartiles ($11M to $21M raise). |
| $18M–$40M | $100M–$250M | 30% | 1.4% | Very unlikely | 1.3% | Very unlikely | Upside Series A led by a top tier fund once revenue is visible; current US medians are about $17M raise on $60M pre money. |

**Why it fails here.** A Series A inside 19 months needs paying engineering customers and validation against solver ground truth. Median time to Series A is about 28 months from batch start, and Rescale reached its B only after years of enterprise sales. Investors will ask whether surrogate accuracy holds outside the training set, and an unmet accuracy bar ends the round.

### Series B: P(reach this round | in YC) = 2.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$180M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Flat or small Series B, near the 2018 to 2021 median of $32M but with a lower valuation. |
| $30M–$60M | $180M–$450M | 50% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series B, in line with the 2022 and later median of about $40M. |
| $60M–$120M | $450M–$1B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside Series B for a category leader; 2022 and later posts reach $600M to $1B. |

**Why it fails here.** A Series B within the window would need an enterprise revenue base far beyond what a 2025 batch company shows after 19 months. Rescale raised its first priced rounds years after batch, and the typical B2B company needs about three years. The likely failure is simple timing: the round is not due yet.

### Series C+: P(reach this round | in YC) = 5.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series C at the 2022 and later median of $74M. |
| $80M–$150M | $700M–$2B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Growth round for a scaled leader, near the 2022 and later p75 of $103M. |
| $150M–$400M | $2B–$6B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside round for a breakout company; only a few percent of YC companies get here. |

**Why it fails here.** Series C inside 19 months is essentially outside the data: the median is about five years from batch start, and the 2022 and later cohort has only 8 Series C cases. Failing here means only that the company has not scaled past a mid sized niche or the window ended first.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 56% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 22% | Reasonable | 21% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 17% | Unlikely | 16% | Unlikely |
| Acquired or IPO over $1B | $1B–$10B | 6.0% | Unlikely | 5.8% | Unlikely |

**Why it fails here.** Most paths end in a stall or small sale because surrogate physics models face a trust gap and platform vendors (Ansys SimAI, Altair) can bundle similar features. Pathmind shows a well funded simulation startup folding after a Series A, and Vorticity shows slow progress. Only a company that becomes the default design tool in one vertical reaches a large exit.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Engineers do not trust AI surrogates in place of certified solvers, so sales stall in pilots. | 35% | Ansys frames AI as augmenting rather than replacing physics, and its own blog stresses screening designs before high fidelity runs. | Pathmind (pathmind), Rescale (rescale) | Publish accuracy benchmarks against solver ground truth and sell as a pre-screening step first. |
| 2 | Incumbents with solvers, data and customers (Ansys SimAI, Altair) ship similar AI features and bundle them. | 30% | Synopsys bought Ansys in 2024 partly for its SimAI products, giving rivals distribution the startup lacks. | Rescale (rescale), Pathmind (pathmind) | Pick one vertical such as aerospace thermal or fluids where a startup can be exact and fast. |
| 3 | Funded physics AI rivals out-raise the company and hire the scarce talent. | 30% | The same wedge (AI physics, CFD surrogate) is crowded with startups by 2025, including a Winter 2025 YC physics model company. | Vorticity (vorticity), Carbic (carbic) | Move fast on a named customer and a public benchmark. |

## Pros

- **Large, well documented spend and visible incumbent interest in AI simulation.**: About $10B simulation market and vendor AI products show the demand is real. (https://www.machinedesign.com/cad-cam-software/article/55301259/altair-crunching-the-numerics-computer-aided-engineering)
- **Team of 10 at batch start is larger than the typical two person YC company.**: Stated in the input; more engineering capacity for a hard technical build. (https://www.ansys.com/blog/how-ai-is-quietly-transforming-simulation)

## Roadmap

### Get into YC

A working demo that matches a solver on a real engineering case.

1. Pick one geometry class and publish error against solver output.
2. Get two engineers to run it on their own problems.

You know it worked when: Side by side accuracy table with under 5 percent error.

### Reach Seed

Paying pilots that justify a $3M to $6M seed.

1. Convert design partners to paid pilots at $20K to $50K.
2. Show repeat use by the same engineers weekly.

You know it worked when: Three paid customers and a named lead investor.

### Reach Series A

Revenue and validated accuracy that justify a Series A.

1. Land a certification relevant use case in aerospace.
2. Build an integration into CAD and solver workflows.

You know it worked when: About $1M in ARR with repeat contracts.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 5 | Training physics models that stay accurate on unseen geometries and conditions is research hard; a team of 10 can build a narrow demo in months but cannot guarantee general accuracy, which is both the moat and the risk. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Godela: An invented name with no descriptor, similar to many YC brands that were built up later such as Rippling or Brex; it neither helps nor hurts a B2B engineering tool sold on proof. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Ansys (Synopsys), Altair, NVIDIA, funded physics AI startups within ~12 months. Vendors already ship AI surrogates inside their suites and have the customers, so a copy in 12 months is plausible; the startup differs only if its accuracy and ease of use are clearly better. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Ansys SimAI and AI modules | Incumbent simulation vendor adds AI surrogate models inside its existing solver suite. | Part of the roughly $10B simulation and analysis market (CIMdata 2023 via Machine Design). | https://www.ansys.com/blog/how-ai-is-quietly-transforming-simulation |
| Altair and other CAE vendors | Established CAE suites with AI and optimization add-ons. | Large installed base across aerospace and auto. | https://www.machinedesign.com/cad-cam-software/article/55301259/altair-crunching-the-numerics-computer-aided-engineering |
| Status quo: HPC solver runs and physical prototypes | Engineers queue solver jobs on cloud HPC or build prototypes. | Entrenched in the $10B market; switching cost is trust, not price. | https://www.machinedesign.com/cad-cam-software/article/55301259/altair-crunching-the-numerics-computer-aided-engineering |

### Demand evidence

- Simulation and analysis is about a $10B market, with aerospace, auto, high tech and heavy equipment making up 76 percent. (https://www.machinedesign.com/cad-cam-software/article/55301259/altair-crunching-the-numerics-computer-aided-engineering)
- Incumbents themselves are investing in AI surrogates, which confirms that customers want faster simulation. (https://www.ansys.com/blog/how-ai-is-quietly-transforming-simulation)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Rescale (rescale) | Winter 2012 | Active | Engineering simulation platform sold to aerospace and auto engineers. | Raised a Series B in 2018 and a Series C in 2021, so simulation can support large rounds, but it took years of enterprise sales. |
| Pathmind (pathmind) | Winter 2016 | Inactive | Simulation and reinforcement learning for industrial engineers. | Raised seed in 2016 and 11.5M in 2019, then went inactive as big tech frameworks took over; shows the funding then squeeze risk. |
| Vorticity (vorticity) | Summer 2019 | Active | Fast scientific computing for simulation workloads, deep technical team. | Series A in 2022 about three years after a 2019 batch, showing slow but real progress for hard simulation tech. |
| Carbic (carbic) | Winter 2016 | Active | Ultrasonic plus ML fluid analysis for industrial customers. | Still active with about 8 people and no found raise beyond YC, an example of a niche industrial tool that stays small. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 46% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: seed known-only 61% (lower 50%, upper 68%), cond 61% (n=88). Median months to seed 9 (p25 4, p75 19); time_to_milestones.csv era 2022+ p75 is 14 months.  | Window is 19 months from the as_of date to 2026-11-17. The ever anchor of 61% counts the YC deal as a seed, but this forecast counts only a financing above about $1M from outside investors that closes inside the window, so the anchor is cut to cover only rounds above $1M and only the share that close within 19 months (about 75 to 80 percent of eventual seed raisers close by month 14 to 20). Credit for a 10 person team and a hard tech wedge is capped at 1.25 times and is not applied; the Hard Tech tag cohort (n=13) shows seed 60 percent but with median seed raises of only $500K, which is the YC deal. Odds are not lifted for team or hot sector, per the winners test, and do not rank this company against others. |
| Series A | 33% | 10% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_a cond 33% (n=54), known-only 20%; months to series A median 30 (p25 22, p75 39). | The ever anchor is 33 percent, but only about a quarter of eventual Series A raisers have closed it by month 19 (p25 is 19 to 22 months from batch start), so the windowed value is much lower. Reaching a Series A in later years is common for companies with paying customers, but it falls outside this window. |
| Series B | 17% | 2.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_b cond 17% (n=18); median months to series B 46 overall, 35.5 for 2022 and later (n=40). | Median time to a Series B is about three years from batch start, so inside a 19 month window almost only extreme outliers get there; windowed probability is far below the 17 percent ever anchor. |
| Series C+ | 30% | 5.0% | python3 -I scripts/base_rates.py --calibration-only: series_c cond 36% (n=55) overall; B2B 2022-2024 cohort has 0 of 3 at Series C. Median months to series C about 61. | Series C normally lands about five years after the batch, so a window of 19 months makes it very unlikely; the ever anchor is cut to a token value. |

## Assumptions and limits

- Team of 10 and the description are the only company facts used.
- Blind forecast made as of 2025-04-07 for the window to 2026-11-17 (19 months). Seed means an outside round above about $1M closing in the window, not the standard YC deal of about $500K.
- Coverage limit: 662 of 6,399 companies are researched, and the B2B 2022-2024 cohort has 107 companies, so cohort rates are wide.
- Probabilities do not rank this company against others; the winners test found no separation between raisers and non-raisers.

## Sources

- https://www.ansys.com/blog/how-ai-is-quietly-transforming-simulation
- https://www.machinedesign.com/cad-cam-software/article/55301259/altair-crunching-the-numerics-computer-aided-engineering
