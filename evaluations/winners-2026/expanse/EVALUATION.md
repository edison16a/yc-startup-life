# Evaluation: Expanse

*As of 2026-04-06. Mode: summary. Twice the work from the GPUs you already own*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Strong founder market fit in a crowded scheduler space, with a seed likely and a Series A a coin flip below even odds.**

**Chance of getting into YC:** 2.0% (range 1.0%–3.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$2M | $10M–$20M | 12% | Unlikely | 0.2% | Very unlikely |
| Seed | $2M–$4M | $15M–$30M | 23% | Reasonable | 0.5% | Very unlikely |
| Seed | $4M–$8M | $30M–$70M | 17% | Unlikely | 0.3% | Very unlikely |
| Seed | $8M–$15M | $70M–$140M | 5.8% | Unlikely | 0.1% | Very unlikely |
| Series A | $4M–$8M | $25M–$45M | 3.5% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$20M | $50M–$100M | 5.6% | Unlikely | 0.1% | Very unlikely |
| Series A | $20M–$40M | $100M–$250M | 2.1% | Very unlikely | <0.1% | Very unlikely |
| Series A | $8M–$18M | $40M–$90M | 2.8% | Very unlikely | <0.1% | Very unlikely |
| Series B | $10M–$25M | $60M–$150M | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$50M | $150M–$350M | 1.0% | Very unlikely | <0.1% | Very unlikely |
| Series B | $50M–$100M | $350M–$900M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$30M | $80M–$200M | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $20M–$40M | $120M–$300M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$800M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$200M | $800M–$3B | 0.2% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Expanse predicts the compute each AI workload needs so organisations can use existing GPU clusters more efficiently. The founders operated such clusters at large quantitative funds, which is a strong signal. GPU scarcity gives the pain real dollar value. The risks are that Nvidia, Run:ai and schedulers bundle the capability, buyers are few, and sales cycles are long. YC analogs in GPU tooling such as Trainy and Luminal raised small seeds or none, and Thunder Compute reached a Series A with a distinct product. A seed within a year is likely, a Series A requires paid enterprise deployments.

## Round by round: where and why it fails

### Getting into YC: 2.0%

**How we got the number.** Placeholder value only, because Expanse is already known to be accepted. Test note: accepted to YC, so the acceptance step is not forecast. The prior is about 1 percent. Four technical founders with direct operating experience of the problem would sit above the prior (founder market fit is the top success tag in the repo data).

**Why it fails here.** YC would most plausibly pass because GPU scheduling is crowded by Run:ai, Slurm tooling and cloud vendors, and prediction accuracy claims are hard to verify. A London team without customers could also appear too early for a sales-led infrastructure product. The interview would test whether the founders can show proof of demand, speed of shipping and a reason the market is open now for Expanse.

### Seed: P(reach this round | in YC) = 58% after the previous step; 58% cumulative if in YC; 1.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$2M | $10M–$20M | 20% | 12% | Unlikely | 0.2% | Very unlikely | Small round if buyers see this as a feature of cluster schedulers. Probability set by judgment from the analogs and current round sizes. |
| $2M–$4M | $15M–$30M | 40% | 23% | Reasonable | 0.5% | Very unlikely | Typical European infrastructure seed, near the $3.2M median for B2B 2022+ in the repo data. |
| $4M–$8M | $30M–$70M | 30% | 17% | Unlikely | 0.3% | Very unlikely | Strong seed, given founders from top hedge funds and the GPU shortage narrative, similar to Luminal's $5.3M seed. |
| $8M–$15M | $70M–$140M | 10% | 5.8% | Unlikely | 0.1% | Very unlikely | Upside with a named hedge fund or lab design partner. Probability set by judgment from the analogs and current round sizes. |

**Why it fails here.** Seed over the YC check is stopped if investors read the product as a scheduler feature that Run:ai, Slurm or cloud vendors will add. Trainy and Thunder Compute show GPU infrastructure companies can raise but also that Trainy has no round found. A London based four person team also faces fewer US seed leads.

### Series A: P(reach this round | in YC) = 24% after the previous step; 14% cumulative if in YC; 0.3% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $25M–$45M | 25% | 3.5% | Very unlikely | <0.1% | Very unlikely | Thin or bridge Series A or a small A extension, below the 2022+ YC median raise of $14M, because growth or revenue is modest. |
| $10M–$20M | $50M–$100M | 40% | 5.6% | Unlikely | 0.1% | Very unlikely | Typical 2022+ YC Series A: median raise $14.15M, p25 to p75 $10M to $20M, against US pre money medians near $60M for a Series A. |
| $20M–$40M | $100M–$250M | 15% | 2.1% | Very unlikely | <0.1% | Very unlikely | Hot AI round with a lead from a top fund after fast revenue growth, in line with 2025 to 2026 AI Series A sizes. |
| $8M–$18M | $40M–$90M | 20% | 2.8% | Very unlikely | <0.1% | Very unlikely | Pivot then raise path: the company changes wedge after the batch and raises an A on the new product, as Eden and Vapi did. |

**Why it fails here.** Series A is missed if prediction accuracy does not turn into measured savings at customers, or if sales cycles into hedge funds and labs are slow. Trainy had self-reported customers but no round, while Thunder Compute raised an A only in 2026 with a distinct product.

### Series B: P(reach this round | in YC) = 18% after the previous step; 2.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $10M–$25M | $60M–$150M | 25% | 0.6% | Very unlikely | <0.1% | Very unlikely | Down or flat B, or a small B led by existing investors after slower growth than the A plan. |
| $25M–$50M | $150M–$350M | 40% | 1.0% | Very unlikely | <0.1% | Very unlikely | Typical 2022+ YC Series B: median $37M, p25 to p75 $25M to $57M. Probability set by judgment from the analogs and current round sizes. |
| $50M–$100M | $350M–$900M | 15% | 0.4% | Very unlikely | <0.1% | Very unlikely | Breakout B with a large lead, as the few 2022+ YC Series B valuations of $550M to $775M suggest. |
| $15M–$30M | $80M–$200M | 20% | 0.5% | Very unlikely | <0.1% | Very unlikely | Strategic round from a customer, partner or incumbent rather than a pure financial lead. |

**Why it fails here.** Series B fails if the market of organisations with large on-prem GPU fleets is too small, or if hyperscalers and Nvidia bundle similar tooling. Few GPU tooling analogs in the repo reached B. For Expanse the milestone to reach this round is paying customers and growth that investors can verify, and the analogs listed in this evaluation show that most companies in the cohort miss that bar.

### Series C+: P(reach this round | in YC) = 30% after the previous step; 0.8% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$40M | $120M–$300M | 30% | 0.2% | Very unlikely | <0.1% | Very unlikely | Small C or growth extension, below the 2022+ YC median C of $45M. Probability set by judgment from the analogs and current round sizes. |
| $40M–$80M | $300M–$800M | 50% | 0.4% | Very unlikely | <0.1% | Very unlikely | Typical C: 2022+ YC median $45M (n=9), US market C deal size near $77M. |
| $80M–$200M | $800M–$3B | 20% | 0.2% | Very unlikely | <0.1% | Very unlikely | Category leader round, as for Deepgram and Vapi style winners, with a valuation above $800M. |

**Why it fails here.** A Series C needs a platform position across enterprise AI infrastructure. Analogs mostly stay seed or are acquired, and Nvidia's Run:ai purchase shows that a leader can absorb the category. For Expanse the milestone to reach this round is paying customers and growth that investors can verify, and the analogs listed in this evaluation show that most companies in the cohort miss that bar.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 52% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 30% | Reasonable | 0.6% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 14% | Unlikely | 0.3% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 4.0% | Very unlikely | <0.1% | Very unlikely |

**Why it fails here.** Likely stall or small acquisition. GPU tooling analogs (Trainy, Thunder Compute, Luminal) are early and most stay small, and the category's leader Run:ai was absorbed by a hardware vendor. A large outcome requires becoming the standard planning layer for enterprise AI compute, which cloud and hardware vendors have strong incentive to own.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Seen as a feature of Slurm, Kubernetes and Run:ai style schedulers | 35% | Run:ai is a Kubernetes native scheduler that optimizes GPU utilization and existing cluster tooling already collects telemetry. | Trainy (trainy), Cerebrium (cerebrium) | Integrate with existing schedulers rather than replacing them. |
| 2 | Prediction accuracy does not hold across diverse workloads | 30% | A 2026 study found Slurm metadata alone is largely non-informative for runtime behavior and needs live telemetry. | Luminal (luminal), Overshoot (overshoot) | Use telemetry and publish measured utilization gains. |
| 3 | Small buyer pool and long sales cycles | 30% | Organisations with large owned GPU fleets are few, and Trainy has not shown a round despite logos. | Trainy (trainy), Ryvn (ryvn) | Land hedge funds and labs where founders have relationships. |
| 4 | Hardware vendors bundle the capability | 25% | Nvidia owns Run:ai and DCGM telemetry and has the distribution. | Thunder Compute (thunder-compute), Cerebrium (cerebrium) | Stay vendor neutral across Nvidia and AMD. |

## Pros

- **Founders ran the clusters they are optimizing**: The team is described as engineers who managed GPU clusters at large quant funds. (https://expanse.sh)
- **Measurable value on scarce, expensive hardware**: GPU idleness and over-allocation are quantified in industry and academic reports. (https://developer.nvidia.com/blog/making-gpu-clusters-more-efficient-with-nvidia-data-center-monitoring/)

## Roadmap

### Get into YC

Show prediction accuracy on real workloads.

1. Benchmark prediction on public cluster traces
2. Run a free pilot on one fund or lab cluster

You know it worked when: Prediction error under 10% on a real workload set

### Reach Seed

Turn pilots into paid contracts.

1. Convert two pilots to annual licenses
2. Integrate with Slurm and Kubernetes

You know it worked when: $250K or more of contracted annual revenue

### Reach Series A

Repeatable sales with measured savings.

1. Publish customer savings case studies
2. Hire first enterprise sales lead

You know it worked when: $1.5M or more annual recurring revenue

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Accurate prediction of GPU memory and runtime before execution needs profiling, modeling and integration with schedulers. The founders' experience helps, but robust coverage across frameworks is hard for four people. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Expanse: A short real word that fits compute but is shared with other products, so search and trademark clarity is weaker. Infrastructure buyers care little about names, so it moves no probability. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Nvidia, Cloud providers, Run:ai, Cluster scheduler vendors within ~12 months. Nvidia and schedulers have telemetry, customers and incentive to add prediction. A rival could ship basic features in about a year. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Run:ai (Nvidia) | Kubernetes native GPU orchestration with fractional sharing | Part of Nvidia enterprise stack | https://www.wwt.com/blog/workload-management-and-orchestration-series-nvidia-runai |
| Slurm with DCGM telemetry | Common HPC scheduler combined with Nvidia monitoring to find idle GPUs | Used in large clusters per Nvidia engineering write-up | https://developer.nvidia.com/blog/making-gpu-clusters-more-efficient-with-nvidia-data-center-monitoring/ |
| Research on workload prediction | Academic GPU demand prediction from Slurm logs | Reported up to 97% accuracy for peak GPU utilization from submission features | https://arxiv.org/html/2604.02158v1 |

### Demand evidence

- Enterprises measure idle GPUs and use telemetry to reduce idleness, showing a paid pain. (https://developer.nvidia.com/blog/making-gpu-clusters-more-efficient-with-nvidia-data-center-monitoring/)
- Research shows GPU over-allocation wastes cluster capacity and prediction can raise utilization. (https://eprints.lancs.ac.uk/144290/1/HotCloud20_GPU_Prediction.pdf)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Trainy (trainy) | Summer 2023 | Active | GPU cluster management software, YC S23. | Small, self-reported customers, no round found. |
| Thunder Compute (thunder-compute) | Summer 2024 | Active | GPU virtualization company, YC S24. | $13M Series A led by Matrix in 2026. |
| Luminal (luminal) | Summer 2025 | Active | GPU efficiency software, YC S25. | $5.3M seed in November 2025. |
| Cerebrium (cerebrium) | Winter 2022 | Active | Serverless AI infrastructure, YC W22. | $8.5M seed in 2025 after years, shows slow B2B infra path. |
| Ryvn (ryvn) | Fall 2024 | Active | Deployment tooling for AI companies. | Active, no public round found. |
| Overshoot (overshoot) | Winter 2026 | Active | Inference optimization, YC W26. | Possible seed, early stage. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 58% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only gave seed cond 59% (lower 49, known 59, upper 65), series_a cond 26% (13/15/29), series_b cond 16% (2/2/18), series_c cond 0% on n=3; the full calibration sample gives series_c cond 36% (n=55) in references/stage_benchmarks.md. Seed within 12 months is lower than ever reaching seed (median 7 months, p75 15). | Seed near the B2B anchor of 0.59: founders have exact operating experience, offset by crowded category and a London base. |
| Series A | 26% | 24% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only gave seed cond 59% (lower 49, known 59, upper 65), series_a cond 26% (13/15/29), series_b cond 16% (2/2/18), series_c cond 0% on n=3; the full calibration sample gives series_c cond 36% (n=55) in references/stage_benchmarks.md. Seed within 12 months is lower than ever reaching seed (median 7 months, p75 15). | Series A near anchor 0.26 and above the infrastructure cohort 0.20 because enterprise on-prem buyers pay for utilization gains. |
| Series B | 16% | 18% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only gave seed cond 59% (lower 49, known 59, upper 65), series_a cond 26% (13/15/29), series_b cond 16% (2/2/18), series_c cond 0% on n=3; the full calibration sample gives series_c cond 36% (n=55) in references/stage_benchmarks.md. Seed within 12 months is lower than ever reaching seed (median 7 months, p75 15). | Series B slightly above the 0.16 anchor because savings are measurable in dollars. |
| Series C+ | 36% | 30% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only gave seed cond 59% (lower 49, known 59, upper 65), series_a cond 26% (13/15/29), series_b cond 16% (2/2/18), series_c cond 0% on n=3; the full calibration sample gives series_c cond 36% (n=55) in references/stage_benchmarks.md. Seed within 12 months is lower than ever reaching seed (median 7 months, p75 15). | Series C+ at 0.30, within 0.75 times the 0.36 anchor. |

## Assumptions and limits

- Blind forecast from batch start 2026-04-06 using only the description.
- Seed step means a round above the $500K YC deal within about 12 months.
- Funding data is partial, so base rates are lower bound to upper bound ranges.

## Sources

- https://www.wwt.com/blog/workload-management-and-orchestration-series-nvidia-runai
- https://developer.nvidia.com/blog/making-gpu-clusters-more-efficient-with-nvidia-data-center-monitoring/
- https://arxiv.org/html/2604.02158v1
- https://eprints.lancs.ac.uk/144290/1/HotCloud20_GPU_Prediction.pdf
- https://expanse.sh
