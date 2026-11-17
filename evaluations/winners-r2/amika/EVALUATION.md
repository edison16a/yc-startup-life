# Evaluation: Amika

*As of 2025-10-06. Mode: summary. Turn any spare computer into agent devboxes or CI runners*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Crowded dev infrastructure wedge with a clear cost angle; plausible small round, but a feature risk.**

**Chance of getting into YC:** 1.5% (range 0.6%–4.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$20M | 12% | Unlikely | 0.2% | Very unlikely |
| Seed | $3M–$6M | $15M–$30M | 18% | Unlikely | 0.3% | Very unlikely |
| Seed | $6M–$12M | $30M–$60M | 14% | Unlikely | 0.2% | Very unlikely |
| Seed | $12M–$25M | $60M–$150M | 6.0% | Unlikely | <0.1% | Very unlikely |
| Series A | $4M–$8M | $20M–$40M | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series A | $8M–$16M | $40M–$90M | 1.6% | Very unlikely | <0.1% | Very unlikely |
| Series A | $16M–$30M | $90M–$250M | 1.2% | Very unlikely | <0.1% | Very unlikely |
| Series A | $30M–$50M | $250M–$500M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series B | $10M–$25M | $50M–$120M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$50M | $120M–$400M | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series B | $50M–$100M | $400M–$1B | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $25M–$60M | $250M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $60M–$120M | $700M–$1.5B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $120M–$400M | $1.5B–$5B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Amika sells a way to turn spare computers into agent devboxes and CI runners on one private network. The need is real because coding agents want always on machines and CI bills are large. But the category already has funded runner vendors and agent sandbox vendors, and the team is two founders with no stated traction at the start of the batch. A seed above $1M is plausible inside 13 months given the AI infra heat, but it is not more likely than the cohort base rate, and the odds here do not rank Amika against other companies. Later rounds depend on proving a buyer who pays more than hobbyists.

## Round by round: where and why it fails

### Getting into YC: 1.5%

**How we got the number.** Start from the third party prior of about 1 percent (range 0.6 to 2 percent, references/yc_acceptance.md). Technical two founder team and a topical agents infrastructure idea lift it slightly; no traction stated and a crowded CI runner and sandbox space hold it back, so about 1.5 percent. This is the view as if applying; the company is already in the Fall 2025 batch.

**Why it fails here.** YC would most plausibly say no because the pitch sounds like a cheaper CI runner, a category with several funded YC alumni such as depot and warpbuild, and the founders show no usage yet. Interviewers also ask why customers would not use GitHub hosted runners or a hosted agent sandbox, and a bring your own hardware angle can read as a feature.

### Seed: P(reach this round | in YC) = 50% after the previous step; 50% cumulative if in YC; 0.8% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$20M | 25% | 12% | Unlikely | 0.2% | Very unlikely | Small post YC round under $3M from angels and a small fund, the most common path for a 2 or 3 person team without revenue. Window is 13 months from 2025-10-06 to 2026-11-17; rounds under $1M and the YC deal itself do not count. |
| $3M–$6M | $15M–$30M | 35% | 18% | Unlikely | 0.3% | Very unlikely | Institutional seed of $3M to $6M, the middle of the 2022 and later table (median about $3.5M to $4M). |
| $6M–$12M | $30M–$60M | 28% | 14% | Unlikely | 0.2% | Very unlikely | Larger institutional seed of $6M to $12M, which the 2026 winners test showed is more common than forecasts assumed. |
| $12M–$25M | $60M–$150M | 12% | 6.0% | Unlikely | <0.1% | Very unlikely | Hot round above $12M, possible only if the product shows fast usage; upside band. |

**Why it fails here.** In the 13 month window the most likely miss is that the product reads as a CI runner discount, the same pitch as warpbuild and buildjet, which stayed near YC deal money. Investors will ask why a customer would not use GitHub hosted runners or a funded sandbox vendor, and two founders without paid usage may not have an answer by demo day. A seed then needs paid fleets, not installs.

### Series A: P(reach this round | in YC) = 8.0% after the previous step; 4.0% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $20M–$40M | 20% | 0.8% | Very unlikely | <0.1% | Very unlikely | Thin Series A or extended seed below the 2022 and later p25 of $11M, typical when growth is slower than hoped. |
| $8M–$16M | $40M–$90M | 40% | 1.6% | Very unlikely | <0.1% | Very unlikely | Typical Series A near the 2022 and later median of about $14M to $15M. |
| $16M–$30M | $90M–$250M | 30% | 1.2% | Very unlikely | <0.1% | Very unlikely | Strong Series A of $16M to $30M when revenue growth is clear and a lead investor competes, above the 2022 and later p75 of about $20M. |
| $30M–$50M | $250M–$500M | 10% | 0.4% | Very unlikely | <0.1% | Very unlikely | Breakout Series A above $30M, possible only for a category leader with fast revenue growth; upside band. |

**Why it fails here.** A Series A needs recurring revenue in the high six figures and a repeatable buyer. Amika would need to show that teams pay for fleets, not just install, and that churn is low. Depot reached a seed after bootstrapping on usage revenue and a Series A only years later, so most companies like this miss the Series A bar for a long time.

### Series B: P(reach this round | in YC) = 25% after the previous step; 1.0% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $10M–$25M | $50M–$120M | 30% | 0.3% | Very unlikely | <0.1% | Very unlikely | Down or flat round, below the 2022 and later p25 of $27M. |
| $25M–$50M | $120M–$400M | 45% | 0.5% | Very unlikely | <0.1% | Very unlikely | Typical Series B near the $32M to $40M median. |
| $50M–$100M | $400M–$1B | 25% | 0.2% | Very unlikely | <0.1% | Very unlikely | Upside band at the p75 of $55M and above. |

**Why it fails here.** A Series B requires scale of tens of millions in revenue and a defensible platform. If GitHub, a sandbox vendor or a mesh network vendor ships bring your own hardware runners, growth flattens at a niche and investors pass, as happened to thin margin runner products.

### Series C+: P(reach this round | in YC) = 30% after the previous step; 0.3% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $25M–$60M | $250M–$700M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Smaller growth round or bridge financing below the 2022 and later series C p25 of about $50M. |
| $60M–$120M | $700M–$1.5B | 45% | 0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series C near the $60M to $74M median. |
| $120M–$400M | $1.5B–$5B | 25% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside band for a category leader, above the 2022 and later series C p75 of about $100M. |

**Why it fails here.** Growth rounds need category leadership. A bring your own compute tool would have to become the control plane for agent fleets, which rivals with larger distribution are better placed to own. If it stays a niche utility, investors will not lead a $60M round and the company stops at Series B or earlier.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 62% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 20% | Reasonable | 0.3% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 14% | Unlikely | 0.2% | Very unlikely |
| Acquired or IPO over $1B | $1B–$5B | 4.0% | Very unlikely | <0.1% | Very unlikely |

**Why it fails here.** Most likely end is a stall as an open source or cloud sandbox product absorbs the use case. Dev infrastructure startups with two founders often sell to individual developers who will not pay, while large teams buy from funded vendors. Analogs such as warpbuild and buildjet show that thin margin runner products stay small unless the team finds a wedge beyond cheap compute.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Cloud sandbox vendors and GitHub itself cover agent devboxes, so a bring your own hardware pitch is a feature, not a company | 40% | Competition then includes hosted CI runner vendors and GitHub hosted runners; buildjet was rated takeover risk 5 for this reason. | BuildJet (buildjet), WarpBuild (warpbuild) | Own the private network and fleet management layer so the hardware story is the product and not a discount. |
| 2 | Buyers are hobbyists with spare Mac Minis who will not pay enough to support a venture sized company | 35% | The spare computer framing points to individual developers and small teams; warpbuild shows modest funding for runner products. | WarpBuild (warpbuild) | Target mid size teams with large CI bills and an EC2 in VPC story, and price per fleet. |
| 3 | Security review: running agents and CI on customer hardware needs isolation guarantees a 2 person team must prove | 25% | Isolated devboxes and a private mesh network touch secrets and source code, which enterprises audit heavily. | Depot (depot) | Ship open isolation design and get an early SOC 2 and an independent audit. |

## Pros

- **Real and growing need for agent computers and cheaper CI**: Managed runner vendors exist and funded sandbox vendors sell agent compute. (https://www.qovery.com/blog/github-actions-alternatives)
- **Bring your own hardware is a cost angle large teams care about**: Teams with idle machines and EC2 in VPC can avoid per minute fees. (https://docs.github.com/en/actions/hosting-your-own-runners)

## Roadmap

### Get into YC

A working product with a few teams running agents or CI on their own hardware

1. Ship a demo that joins three machines to one network in minutes
2. Get 10 teams from developer communities to install it

You know it worked when: Ten teams with weekly active fleets

### Reach Seed

Paid usage and a clear buyer beyond hobbyists

1. Charge per fleet from day one
2. Land two companies with CI bills over $2,000 a month

You know it worked when: $10,000 monthly recurring revenue and a design partner reference

### Reach Series A

Repeatable sales into mid size engineering teams

1. Add audit logs and SSO
2. Hire a first sales engineer

You know it worked when: Net revenue retention above 110 percent

### Reach Series B

A platform position beyond CI

1. Expand to agent fleet management
2. Add enterprise on premise deployment

You know it worked when: Multiple Fortune 1000 deployments

### Reach Series C and beyond

Category leadership in bring your own compute

1. Add partnerships with chip and cloud vendors
2. Open a second product line

You know it worked when: Revenue above $50M

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A tunnel based private network, isolation of devboxes on mixed hardware (Mac, Linux, EC2) and a job scheduler are doable by two strong infra engineers in three months, but a secure multi tenant control plane and macOS virtualization limits are real work. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Amika: A short invented style name like many 2022 and later YC companies, easy to say and register but carrying no meaning for the product. Past YC brands such as Depot and Replicate show that the name matters little against product pull. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by GitHub, Tailscale, E2B, Cloudflare within ~6 months. Several funded companies could add bring your own hardware agent runners within a few months. GitHub already supports self hosted runners, and mesh network and sandbox vendors have distribution Amika lacks. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Blacksmith and Depot | Managed faster GitHub Actions runners | Depot is a YC Winter 2023 company that raised a seed in 2024 | https://depot.dev |
| GitHub hosted and self hosted runners with Actions Runner Controller | The status quo for CI, free self hosting on Kubernetes | Default for most GitHub users | https://docs.github.com/en/actions/hosting-your-own-runners |
| E2B and Daytona sandboxes | Hosted sandboxes for AI agents | Funded vendors selling agent compute by usage | https://e2b.dev |

### Demand evidence

- GitHub self hosted runners and managed runner vendors show teams pay to cut CI cost and time (https://www.qovery.com/blog/github-actions-alternatives)
- Agent sandbox vendors show demand for isolated compute for coding agents (https://e2b.dev)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| WarpBuild (warpbuild) | Summer 2021 | Active | Sells faster cheaper CI runners to GitHub Actions users, the same CI offload use case. | Active at small scale with only aggregator reported funding of about $0.5M to $2M, no institutional round found by 2025. |
| BuildJet (buildjet) | Winter 2023 | Active | Faster cheaper GitHub Actions runners, two founders, Winter 2023. | Raised roughly $0.5M, the YC deal, and no institutional seed in its first two years; takeover risk from GitHub rated 5. |
| Depot (depot) | Winter 2023 | Active | Managed CI and build acceleration, the best funded neighbor in the runner category. | Raised a seed of about $4M in 2024 after bootstrapping on usage revenue, showing a seed is reachable with paying customers. |
| Replicate (replicate) | Winter 2020 | Acquired | Developer infrastructure that rented compute for a workload, Winter 2020. | Reached large rounds after becoming the default for running models; shows infra can win with a clear developer product. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 64% | 50% | python3 -I scripts/base_rates.py --calibration-only --tag AI gave seed lower/known/upper 51%/64%/71%, cond 64% (n=183), ever and not windowed. Time table: calibration median 7 months to seed, p75 19.5 months (knowledge/tables/time_to_milestones.csv), so a 13 month window captures most but not all. | Set below the ever anchor of 0.64 for the 13 month window and a crowded dev infra category with a 2 person team and no stated traction; no lift for AI heat per the winners test rules. These odds do not rank Amika against other companies. |
| Series A | 30% | 8.0% | python3 -I scripts/base_rates.py --calibration-only --tag AI gave series_a 15%/19%/36%, cond 30% (n=117). Time to series A median 28 months, p25 19 months, so within 13 months few companies reach it. | Given seed within the window, a Series A inside 13 months is early: the calibration p25 is 19 months from batch start, so I use about a quarter of the ever anchor. |
| Series B | 31% | 25% | python3 -I scripts/base_rates.py --calibration-only --tag AI gave series_b 5%/6%/26%, cond 31% (n=35). Ever, not windowed. | Slightly below the 0.31 anchor because the product competes with platform features and revenue is unproven. |
| Series C+ | 45% | 30% | python3 -I scripts/base_rates.py --calibration-only --tag AI gave series_c 2%/3%/23%, cond 45% (n=11). Ever, not windowed. | Below the 0.45 anchor since few infra startups of this kind reach growth rounds. |

## Assumptions and limits

- Information limited to the input file and market searches dated before 2025-10-06.
- Window of 13 months from 2025-10-06 to 2026-11-17.
- Seed means a round above about $1M from outside investors, excluding the standard YC deal.
- Team described as 2 people with no traction data.

## Sources

- https://www.qovery.com/blog/github-actions-alternatives
- https://depot.dev
- https://e2b.dev
- https://docs.github.com/en/actions/hosting-your-own-runners
