# Evaluation: Ardent

*As of 2026-04-06. Mode: summary. Database sandboxes for Agents*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A sharp technical wedge in a crowded, fast moving niche where acquisition is more likely than independence.**

**Chance of getting into YC:** 3.0% (range 1.0%–6.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $700K–$1.5M | $8M–$14M | 15% | Unlikely | 0.4% | Very unlikely |
| Seed | $1.5M–$4M | $14M–$30M | 30% | Reasonable | 0.9% | Very unlikely |
| Seed | $4M–$8M | $30M–$60M | 15% | Unlikely | 0.4% | Very unlikely |
| Series A | $5M–$9M | $30M–$55M | 3.3% | Very unlikely | <0.1% | Very unlikely |
| Series A | $9M–$18M | $55M–$110M | 7.3% | Unlikely | 0.2% | Very unlikely |
| Series A | $18M–$30M | $110M–$250M | 2.6% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$28M | $70M–$140M | 0.9% | Very unlikely | <0.1% | Very unlikely |
| Series B | $28M–$50M | $140M–$350M | 1.2% | Very unlikely | <0.1% | Very unlikely |
| Series B | $50M–$90M | $350M–$800M | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$50M | $250M–$500M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $50M–$100M | $500M–$1B | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $100M–$200M | $1B–$2.5B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Ardent offers instant Postgres clones for agents. Timing is good because agents need safe test databases, but branching products from funded rivals already exist and database hosts can bundle the feature. B2B cohorts reach seed about 53 percent of the time and Series A about 26 percent given a seed. Expect a seed if developer pull shows and a small acquisition as the common end. Reaching later rounds is common for companies with paying customers even years after the batch, so the odds below describe whether a round happens, not when. The main drivers are whether early customers pay, whether the product beats bundled features from larger vendors, and whether the team can keep a small burn long enough to show repeat revenue.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Company is assumed accepted, so this is a note only. Prior is about 1 percent per applicant with a 0.6 to 2 percent band. A concrete technical claim and a hot agent infrastructure theme help, while the idea is thin on stated traction and close to existing branching products.

**Why it fails here.** YC would most plausibly say no because instant Postgres branching already exists from several funded vendors, and the pitch gives no customers, so it can look like a feature of a database host. The decision would also weigh whether the three person team can show real users within one batch, and whether the founders can explain a wedge that incumbents are unlikely to copy quickly.

### Seed: P(reach this round | in YC) = 60% after the previous step; 60% cumulative if in YC; 1.8% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $700K–$1.5M | $8M–$14M | 25% | 15% | Unlikely | 0.4% | Very unlikely | Small round above the YC deal. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $1.5M–$4M | $14M–$30M | 50% | 30% | Reasonable | 0.9% | Very unlikely | Infrastructure seed 2022+ median is about $4.2M raise. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $4M–$8M | $30M–$60M | 25% | 15% | Unlikely | 0.4% | Very unlikely | Upside if developer pull appears from agent builders. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |

**Why it fails here.** The seed fails if the team cannot show real agent builders using it daily. Investors will ask why a customer would not use Neon branches or the agent features of a Postgres host. Lantern and Midplane show Postgres and agent database teams that stayed small or stopped without a priced round.

### Series A: P(reach this round | in YC) = 22% after the previous step; 13% cumulative if in YC; 0.4% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$9M | $30M–$55M | 25% | 3.3% | Very unlikely | <0.1% | Very unlikely | Thin A from a niche tool. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $9M–$18M | $55M–$110M | 55% | 7.3% | Unlikely | 0.2% | Very unlikely | Infrastructure Series A 2022+ median is about $12.5M raise. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $18M–$30M | $110M–$250M | 20% | 2.6% | Very unlikely | <0.1% | Very unlikely | Upside if it becomes the default test environment for coding agents. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |

**Why it fails here.** A Series A fails if usage stays free tier and revenue is under a few hundred thousand dollars. Neon was bought by Databricks and others like Xata and Simplyblock offer branching, so investors will doubt a stand alone product. ParadeDB reached an A with open source pull, which Ardent would need to match.

### Series B: P(reach this round | in YC) = 20% after the previous step; 2.6% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$28M | $70M–$140M | 35% | 0.9% | Very unlikely | <0.1% | Very unlikely | Modest B. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $28M–$50M | $140M–$350M | 45% | 1.2% | Very unlikely | <0.1% | Very unlikely | Series B 2022+ median about $37M. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $50M–$90M | $350M–$800M | 20% | 0.5% | Very unlikely | <0.1% | Very unlikely | Upside if usage scales with agent adoption. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |

**Why it fails here.** A Series B fails if the product broadens into general sandboxes and loses its edge against better funded agent sandbox vendors. Investors want revenue growth and retention, and per usage pricing on database clones may stay small. Supabase shows the ceiling for Postgres companies but depends on a far larger developer platform.

### Series C+: P(reach this round | in YC) = 20% after the previous step; 0.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$50M | $250M–$500M | 45% | 0.2% | Very unlikely | <0.1% | Very unlikely | Median Series C 2022+ is about $45M. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $50M–$100M | $500M–$1B | 40% | 0.2% | Very unlikely | <0.1% | Very unlikely | Growth round on strong agent infrastructure demand. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |
| $100M–$200M | $1B–$2.5B | 15% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside if it is a core data layer for agents. This scenario is sized from the researched round benchmarks for recent cohorts and weighted by how often similar companies landed there. |

**Why it fails here.** A later round fails if cloud and database hosts bundle cloning for free and the stand alone vendor cannot move beyond testing. Late stage investors want a large platform with expansion, and a sandbox feature has a ceiling in spend. Acquisition by a database company is the more common end, as with Hydra and Citus Data.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 45% | Likely | 98% | Very likely |
| Acquired or IPO under $100M | $10M–$100M | 33% | Reasonable | 1.0% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 18% | Unlikely | 0.5% | Very unlikely |
| Acquired or IPO over $1B | $1B–$3B | 4.0% | Very unlikely | 0.1% | Very unlikely |

**Why it fails here.** The company most likely stalls or sells small because the core feature, fast copy on write cloning, is available from funded rivals and from database hosts that can bundle it. Database infrastructure startups in the YC set often end in acquisition by a larger database company at modest value, as with Hydra, PeerDB and Citus Data.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Branching is a feature of database hosts | 45% | Neon was bought by Databricks in 2025 and Xata and Simplyblock sell copy on write Postgres branches, so cloning can be bundled for free. | Lantern (lantern-2), Hydra (hydra) | Work across existing databases without migration and win on speed for large databases. |
| 2 | Small spend per customer | 30% | Agent testing sandboxes are an early use and teams may use cheap ad hoc clones or snapshots. | Midplane (midplane), Freestyle (freestyle) | Tie pricing to agent runs and sell to teams already running many agents. |
| 3 | Larger sandbox vendors absorb the use case | 25% | Agent sandbox companies are adding database support to their environments and have the distribution. | Freestyle (freestyle), Beam (beam) | Integrate into those sandboxes as a partner. |

## Pros

- **Clear technical claim that can be benchmarked.**: Cloning any size Postgres in six seconds is specific and testable.
- **Strong timing as agents need safe test environments.**: Market activity around Postgres branching and agent databases in 2025 and 2026. (https://xata.io/blog/every-ai-agent-needs-a-database-it-can-break)

## Roadmap

### Get into YC

Prove the six second clone claim on large databases.

1. Publish a benchmark on 1TB databases
2. Get five agent builders to try it

You know it worked when: Public benchmark and five active users.

### Reach Seed

Show paid usage from teams running agents.

1. Offer a usage based plan
2. Integrate with two agent sandbox vendors

You know it worked when: Recurring revenue from several teams and growing clone counts.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Fast cloning of large Postgres databases needs storage level copy on write and careful consistency, which is hard but doable for a small expert team. Safety, masking and running against customers' existing databases add work. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Ardent: A short real word is common among strong recent YC names, but there is no link to databases or agents. Developer buyers choose on speed and price, so the name has little effect. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Databricks and Neon, Supabase, Cloud database hosts, Agent sandbox vendors within ~9 months. Database hosts already have branching and could expose it to agents with little work. Cloning for external databases is harder, which gives some room, but acquisition is the likelier path than independence. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Xata | Postgres with copy on write branches. | Vendor claims branch ready in seconds regardless of size. | https://xata.io/blog/every-ai-agent-needs-a-database-it-can-break |
| Neon (Databricks) | Serverless Postgres with branching, acquired by Databricks in May 2025. | Large installed base. | https://dzone.com/articles/lakebase-ai-agents |
| Simplyblock Vela | Git style Postgres branches on its block storage. | Hosted sandbox in beta. | https://www.blocksandfiles.com/block/2026/02/10/simplyblock-provides-postgres-git-style-branching/4090455 |

### Demand evidence

- Vendors argue every agent needs a disposable database copy, and big companies paid for branching technology. (https://xata.io/blog/every-ai-agent-needs-a-database-it-can-break)
- Databricks bought Neon for about $1B in 2025 largely for agent use of Postgres. (https://dzone.com/articles/lakebase-ai-agents)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Supabase (supabase) | Summer 2020 | Active | Postgres developer platform for builders. | Raised a seed and many later rounds, reaching a very large valuation. |
| Lantern (lantern-2) | Winter 2024 | Inactive | Postgres extension and cloud product for AI apps. | Pre seed, then listed inactive. |
| Hydra (hydra) | Winter 2022 | Acquired | Postgres analytics start up. | Seed of about $3.1M, later joined a larger Postgres platform. |
| ParadeDB (paradedb) | Summer 2023 | Active | Postgres search and analytics with open source pull. | Series A of $12M in 2025. |
| Midplane (midplane) | Summer 2022 | Active | Safety layer between AI agents and Postgres. | Two person team, no funding beyond YC found. |
| PeerDB (peerdb) | Summer 2023 | Acquired | Narrow Postgres tool bought by a larger database vendor. | Seed then acquisition within months. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 53% | 60% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 gave seed 47% lower, 53% known only, 59% upper, cond 53% (n=878). Infrastructure tag cond 52% (n=48). | Slightly above anchor because agent infrastructure is a hot theme with active seed investors, but still within 1.2 times. |
| Series A | 26% | 22% | B2B cohort cond 26% (n=468), known only 14%, upper 25%. Infrastructure tag cond 20% (n=25). | Within the anchor range. Slightly lower because takeover risk is high. |
| Series B | 21% | 20% | B2B cohort cond 21% (n=123). | Anchored on cohort. |
| Series C+ | 19% | 20% | B2B cohort series_c cond 19% (n=26). | Anchored on cohort; very thin data. |

## Assumptions and limits

- Only the supplied input file was used for company facts.
- Accepted to YC as stated; acceptance note is for completeness.
- Seed in this test means a round above about $500K within 12 months of the batch start.
- Web results dated after the as_of date were ignored.

## Sources

- https://xata.io/blog/every-ai-agent-needs-a-database-it-can-break
- https://dzone.com/articles/lakebase-ai-agents
- https://www.blocksandfiles.com/block/2026/02/10/simplyblock-provides-postgres-git-style-branching/4090455
