# Evaluation: Chamber

*As of 2026-01-05. Mode: summary. The AIOps Agent for ML Teams*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A real, costly GPU problem and a strong team size, but a crowded AIOps field where trust and bundling decide the outcome.**

**Chance of getting into YC:** 4.0% (range 1.5%–8.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$1.5M | $8M–$15M | 14% | Unlikely | 0.5% | Very unlikely |
| Seed | $2M–$5M | $15M–$35M | 37% | Reasonable | 1.5% | Very unlikely |
| Seed | $6M–$12M | $40M–$80M | 17% | Unlikely | 0.7% | Very unlikely |
| Series A | $6M–$10M | $30M–$55M | 5.6% | Unlikely | 0.2% | Very unlikely |
| Series A | $10M–$20M | $60M–$120M | 12% | Unlikely | 0.5% | Very unlikely |
| Series A | $25M–$45M | $150M–$300M | 4.5% | Very unlikely | 0.2% | Very unlikely |
| Series B | $15M–$25M | $70M–$130M | 1.5% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$50M | $150M–$320M | 2.5% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$100M | $400M–$800M | 1.0% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$55M | $200M–$400M | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $60M–$100M | $500M–$1B | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $120M–$250M | $1.2B–$3B | 0.3% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Chamber sells autonomous agents that keep AI infrastructure running and cut GPU waste. The pain is real and measurable, and AI infrastructure companies have raised quickly, so a seed above $500K within a year is more likely than the cohort average. The risks are customer trust in autonomous fixes, a limited buyer set and bundling by Datadog and the clouds. Analogs split between Thunder Compute, which raised an A, and Serial, Relvy and Cedana, which stayed small or closed. Estimates are near the B2B cohort anchors.

## Round by round: where and why it fails

### Getting into YC: 4.0%

**How we got the number.** Test assumes the company was accepted, so this is only a note. Prior about 1 percent (0.6 to 2 percent third party range). Up for a four person technical team, a painful and expensive problem (idle GPUs) and strong AI infrastructure timing, down for a crowded infra agent space and no stated customers.

**Why it fails here.** YC would most plausibly pass because AI SRE and GPU optimisation pitches are common, the description lists capabilities without a named customer or number, and large clouds and observability vendors could offer the same agents, so reviewers question defensibility. Four founders make the team credible, but the application alone does not show why it would win customers.

### Seed: P(reach this round | in YC) = 68% after the previous step; 68% cumulative if in YC; 2.7% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$1.5M | $8M–$15M | 20% | 14% | Unlikely | 0.5% | Very unlikely | Thin round just above the standard deal if pilots are slow. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $2M–$5M | $15M–$35M | 55% | 37% | Reasonable | 1.5% | Very unlikely | Typical 2026 AI infrastructure seed, a little above the 2022+ median of about $4M because of GPU heavy demand. |
| $6M–$12M | $40M–$80M | 25% | 17% | Unlikely | 0.7% | Very unlikely | Upside if teams with large GPU fleets pay early and infrastructure funds compete, as for Thunder Compute style companies. |

**Why it fails here.** The seed fails if no team will give an autonomous agent write access to production training clusters, so pilots stay read only and revenue never shows. Investors also ask why a four person team beats observability vendors and the clouds. Serial, a root cause startup, raised only the YC deal and shut down.

### Series A: P(reach this round | in YC) = 33% after the previous step; 22% cumulative if in YC; 0.9% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $30M–$55M | 25% | 5.6% | Unlikely | 0.2% | Very unlikely | Small A if revenue stays pilot sized. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $10M–$20M | $60M–$120M | 55% | 12% | Unlikely | 0.5% | Very unlikely | Typical 2022+ Series A, around the $14M median. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $25M–$45M | $150M–$300M | 20% | 4.5% | Very unlikely | 0.2% | Very unlikely | Upside if the product becomes the standard for managing GPU workloads. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |

**Why it fails here.** A Series A needs proof that the agents cut GPU waste and failures by a clear dollar amount at several customers. Customers with large fleets are few, trust in autonomous changes is low, and observability vendors like Datadog extend into the same area. Wild Moose took three years from its batch to a seed that emerged, and Relvy and Cedana show small teams stuck without a round.

### Series B: P(reach this round | in YC) = 22% after the previous step; 4.9% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$25M | $70M–$130M | 30% | 1.5% | Very unlikely | <0.1% | Very unlikely | Flat B near the 2022+ p25. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $25M–$50M | $150M–$320M | 50% | 2.5% | Very unlikely | <0.1% | Very unlikely | Typical 2022+ B. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $60M–$100M | $400M–$800M | 20% | 1.0% | Very unlikely | <0.1% | Very unlikely | Upside if it scales with GPU spend. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |

**Why it fails here.** A Series B needs scaled revenue from many ML teams as GPU spend grows. The buyer set is limited, many large labs build tooling in house, and the cloud providers bundle management features. Few B2B infra companies in the cohort reach B, and the ones that do usually show revenue growth that tracks customer GPU spend.

### Series C+: P(reach this round | in YC) = 28% after the previous step; 1.4% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$55M | $200M–$400M | 40% | 0.6% | Very unlikely | <0.1% | Very unlikely | Modest later round. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $60M–$100M | $500M–$1B | 40% | 0.6% | Very unlikely | <0.1% | Very unlikely | Typical growth round. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |
| $120M–$250M | $1.2B–$3B | 20% | 0.3% | Very unlikely | <0.1% | Very unlikely | Upside if it is a core AI infrastructure layer. Sized from the 2022+ round benchmark tables for this stage, with the post money range an estimate because valuations are rarely disclosed. |

**Why it fails here.** A Series C requires a defensible platform position and margins that survive cloud competition. AI infrastructure is volatile with GPU supply changes and consolidation, and acquirers such as large observability or cloud firms often buy before a late round, which caps the number of independent companies that reach this stage in the cohort.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 48% | Likely | 98% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 30% | Reasonable | 1.2% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 16% | Unlikely | 0.6% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 6.0% | Unlikely | 0.2% | Very unlikely |

**Why it fails here.** Most likely the company stalls when large clouds and observability vendors bundle agentic operations, or it is acquired for a small price. Serial shut down, Relvy and Cedana stay small and Thunder Compute shows that GPU infrastructure can raise. Reaching a billion dollar value needs the company to be the default operations layer for AI workloads.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Customers will not give autonomous agents write access to production ML clusters | 40% | Production training jobs cost thousands per hour, and an agent fix that fails could waste large budgets, so teams keep humans in the loop. | Serial (serial), Relvy AI (relvy-ai) | Start read only with recommendations and earn write access with audit logs and rollback. |
| 2 | Cloud providers and observability vendors bundle the same agents | 40% | Datadog, major clouds and GPU platforms add AI operations features to their products and already hold the data. | Wild Moose (wild-moose), Cedana (cedana) | Be multi cloud and specialise in GPU failure and efficiency where general tools are weak. |
| 3 | The set of buyers with enough GPU spend is small | 30% | Only labs and larger ML teams run fleets where the savings justify a vendor, and many build tools in house. | Thunder Compute (thunder-compute), Cedana (cedana) | Price on savings share and target neoclouds and mid size ML teams. |

## Pros

- **Expensive and growing pain point**: GPU spend and failed jobs create direct dollar savings that justify a fee. (https://wandb.ai)
- **Technical team of four with infra timing**: A four person team can build and sell to ML teams while AI infrastructure investing is strong, and Thunder Compute reached an A. (https://www.datadoghq.com)

## Roadmap

### Get into YC

Show measured GPU savings on a real cluster

1. Interview 20 ML platform leads
2. Run the agent read only on two clusters

You know it worked when: Two teams agreeing to a pilot

### Reach Seed

Raise above $500K within 12 months of the batch

1. Convert pilots to paid contracts
2. Publish failure rate and cost savings

You know it worked when: Paying customers and a lead investor

### Reach Series A

Prove repeatable revenue

1. Add multi cloud support
2. Gain write access at several customers

You know it worked when: $1M recurring revenue and savings above the fee

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | The agents must integrate with Kubernetes, schedulers, multiple clouds and training frameworks, and diagnose distributed failures reliably. A small team can build monitoring and root cause suggestions in months, but safe autonomous remediation across clouds is much harder. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Chamber: Real word names did well in the oldest YC eras but show no gap in 2018+. The name is easy to say and sets a calm tone for infrastructure, but it will not differentiate, and sales depend on measured savings as with Thunder Compute. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Datadog, AWS, Google Cloud and Azure, Weights & Biases within ~12 months. Observability vendors and clouds have the data and customers and are shipping AI operations agents. They could match basic monitoring in under a year, so the startup needs GPU specific depth. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Datadog | Observability platform expanding into AI and LLM monitoring | Public company with a very large customer base | https://www.datadoghq.com |
| Weights & Biases | ML experiment tracking and monitoring | Widely used by ML teams | https://wandb.ai |
| Run:ai and cloud scheduler tools | GPU orchestration and scheduling | Used in large GPU fleets | https://www.run.ai |
| Status quo of in house platform engineers and scripts | Manual monitoring and debugging | Default at most ML teams | https://kubernetes.io |

### Demand evidence

- GPU costs are a top expense for AI teams and idle or failed jobs waste large budgets, which motivates tooling spend. (https://wandb.ai)
- Observability vendors and funded startups already sell AI operations and root cause tools, showing paid demand. (https://www.datadoghq.com)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Wild Moose (wild-moose) | Winter 2023 | Active | AI root cause analysis for engineering incidents | Active; emerged from stealth with a $7M seed in 2025, about two and a half years after the batch. |
| Thunder Compute (thunder-compute) | Summer 2024 | Active | GPU infrastructure for AI developers | Raised a $13M Series A led by a top fund in 2026. |
| Serial (serial) | Winter 2023 | Inactive | Root cause analysis software for engineers | Inactive with only the YC investment found. |
| Cedana (cedana) | Summer 2023 | Active | GPU workload tooling with deep technical team | Active, no round beyond YC found. |
| Relvy AI (relvy-ai) | Fall 2024 | Active | AI debugging for incident response | Active three person team with a small reported round. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 68% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed 50/61/68 (cond 61, n=88), A 17/20/35 (cond 33, n=54), B 3/3/21 (cond 17, n=18), C 0/0/18 (n=3); --industry B2B --years 2019-2023: seed cond 73 (n=113), A cond 32 (n=82), B cond 23 (n=26), C cond 33 (n=6). | 1.1 times the B2B 2022-24 anchor and 0.93 times the 2019-23 anchor. Four technical founders, GPU cost pain and hot AI infrastructure investing push it up, while the 12 month window and no stated customers hold it back. |
| Series A | 33% | 33% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed 50/61/68 (cond 61, n=88), A 17/20/35 (cond 33, n=54), B 3/3/21 (cond 17, n=18), C 0/0/18 (n=3); --industry B2B --years 2019-2023: seed cond 73 (n=113), A cond 32 (n=82), B cond 23 (n=26), C cond 33 (n=6). | At the 33 percent B2B 2022-24 anchor. Infrastructure with usage tied pricing has done well in the cohort (Thunder Compute, Wild Moose), offset by competition. |
| Series B | 23% | 22% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed 50/61/68 (cond 61, n=88), A 17/20/35 (cond 33, n=54), B 3/3/21 (cond 17, n=18), C 0/0/18 (n=3); --industry B2B --years 2019-2023: seed cond 73 (n=113), A cond 32 (n=82), B cond 23 (n=26), C cond 33 (n=6). | 0.96 times the 23 percent anchor (B2B 2019-23, n=26) and above the 17 percent 2022-24 anchor. |
| Series C+ | 33% | 28% | python3 -I scripts/base_rates.py --industry B2B --years 2019-2023 --calibration-only: series_c cond 33 (n=6). | 0.85 times the anchor from only 6 companies, so it is a weak anchor. |

## Assumptions and limits

- Only the input file was used for the company; market sections use general knowledge and homepage URLs.
- Seed in this test means a round above about $500K within 12 months of the batch start.
- The B2B cohort includes many unlike companies, so rates are approximate.
- Competition recorded as of January 2026.

## Sources

- https://www.roundfunded.com/en/blogs/yc-acceptance-rate-2026
- https://www.datadoghq.com
- https://wandb.ai
- https://www.run.ai
- https://kubernetes.io
