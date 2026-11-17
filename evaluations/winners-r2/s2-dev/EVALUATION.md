# Evaluation: s2.dev

*As of 2025-10-06. Mode: summary. API for unlimited, durable, real-time streams*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A technically deep streaming primitive with a normal seed chance in 13 months and heavy incumbent pull.**

**Chance of getting into YC:** 1.5% (range 0.8%–3.5%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$15M | 8.0% | Unlikely | 0.1% | Very unlikely |
| Seed | $3M–$6M | $15M–$30M | 13% | Unlikely | 0.2% | Very unlikely |
| Seed | $6M–$12M | $30M–$60M | 8.0% | Unlikely | 0.1% | Very unlikely |
| Seed | $12M–$20M | $60M–$120M | 3.2% | Very unlikely | <0.1% | Very unlikely |
| Series A | $4M–$9M | $20M–$40M | 1.3% | Very unlikely | <0.1% | Very unlikely |
| Series A | $9M–$16M | $40M–$80M | 1.7% | Very unlikely | <0.1% | Very unlikely |
| Series A | $16M–$30M | $80M–$200M | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$30M | $80M–$150M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$55M | $150M–$400M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $55M–$100M | $400M–$900M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$50M | $200M–$500M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $50M–$100M | $500M–$1.2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $100M–$200M | $1.2B–$3B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

s2.dev builds serverless durable streams, positioned as S3 for streams. With a five person technical team and a 13.4 month window, the developer tools cohort gives about 51 percent ever and about 32 percent for the window. Infrastructure investors may back technical credibility early, but analogs show mixed results and no verified rounds for some, so there is no lift above the anchor. The odds do not rank it against others in the batch. A technically deep primitive, with a five person team. The scored numbers are window specific and anchored on older cohorts, and the remaining risk is mostly execution and timing rather than the idea alone.

## Round by round: where and why it fails

### Getting into YC: 1.5%

**How we got the number.** YC publishes no acceptance rate; the working prior is about 1 percent with a band of 0.6 to 2 percent (references/yc_acceptance.md). This company is already in the batch named in the input, so the number is for completeness only. Five person technical team on a hard infrastructure primitive with a clear thesis; infrastructure and developer tools are well liked by YC but the market for streams is crowded by Kafka vendors; about 1.5 percent. Already in the batch.

**Why it fails here.** A new database primitive is a slow sell with open source competitors and Kafka compatible vendors, and YC could ask why developers would leave Kafka or managed streaming services and who pays first beyond hobby projects. YC may also ask whether the first paying customers are AI agent builders or traditional data teams, and whether an open source Kafka compatible alternative would be easier to adopt than a new API.

### Seed: P(reach this round | in YC) = 32% after the previous step; 32% cumulative if in YC; 0.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$15M | 25% | 8.0% | Unlikely | 0.1% | Very unlikely | small post YC round under $3M from angels or a micro fund, the most common outcome for companies with thin traction at 2022 and later seed data |
| $3M–$6M | $15M–$30M | 40% | 13% | Unlikely | 0.2% | Very unlikely | typical institutional seed; the 2022 and later table has a $3.5M median that mixes in the YC deal, so institutional seeds sit a bit higher |
| $6M–$12M | $30M–$60M | 25% | 8.0% | Unlikely | 0.1% | Very unlikely | larger institutional seed for fast growth or a hot category; confirmed 2026 raises above $1M had a $6M median but press favours big rounds |
| $12M–$20M | $60M–$120M | 10% | 3.2% | Very unlikely | <0.1% | Very unlikely | upside seed or seed plus, needs unusual traction or a repeat founder; rare |

**Why it fails here.** Seed here means a round above about $1M from outside investors closing inside the 13.4 month window from the as of date. Developer tools cohort has 51 percent ever; the window cuts to about 32 percent. Infrastructure with a technical team raises on credibility, yet analogs such as Arroyo and Rivet had no verified round and Streamdal shut down after a seed, so investors may wait for paying usage.

### Series A: P(reach this round | in YC) = 12% after the previous step; 3.8% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$9M | $20M–$40M | 35% | 1.3% | Very unlikely | <0.1% | Very unlikely | thin or flat A, below the 2022 and later $10M p25, after a slow year; includes a bridge style A |
| $9M–$16M | $40M–$80M | 45% | 1.7% | Very unlikely | <0.1% | Very unlikely | median A, 2022 and later raise median about $13.5M with few disclosed valuations |
| $16M–$30M | $80M–$200M | 20% | 0.8% | Very unlikely | <0.1% | Very unlikely | upside A after real revenue growth, p75 of the 2022 and later table is $20M |

**Why it fails here.** Series A given a seed in the window is about 12 percent. Developer tools cohort conditional is 26 percent ever and infrastructure needs revenue; LanceDB took years to reach A and Replicate reached B only after wide adoption. Series A given a seed in the window is about 12 percent. The developer tools cohort has a 26 percent conditional rate ever, and infrastructure needs revenue evidence; LanceDB took years to reach A and Replicate reached B only after wide adoption, so a quick A is uncommon.

### Series B: P(reach this round | in YC) = 5.0% after the previous step; 0.2% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$150M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | small B near the 2018 to 2021 median of $30M, flat valuation |
| $30M–$55M | $150M–$400M | 50% | <0.1% | Very unlikely | <0.1% | Very unlikely | median B, 2022 and later median $37M, p75 $57M |
| $55M–$100M | $400M–$900M | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | upside B in a category leader; disclosed 2022 and later valuations around $775M |

**Why it fails here.** A Series B inside this window requires explosive adoption; Replicate reached B after years, and open source analogs mostly sell before B. A Series B inside this window requires explosive adoption and revenue; Replicate reached B after years, and several open source infrastructure analogs sold before ever raising one, so the number is small.

### Series C+: P(reach this round | in YC) = 3.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$50M | $200M–$500M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | small C or extension, 2022 and later median $42.5M |
| $50M–$100M | $500M–$1.2B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | typical C for a company with scaled revenue |
| $100M–$200M | $1.2B–$3B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | upside growth round for a category leader with strong revenue, rare among YC companies in any cohort |

**Why it fails here.** A Series C inside the window is unobserved for infrastructure companies this young; the figure is a floor. A Series C inside the window is unobserved for infrastructure companies this young, so the figure is a floor. It would need a default building block status across many large customers.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 32% | Reasonable | 0.5% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 15% | Unlikely | 0.2% | Very unlikely |
| Acquired or IPO over $1B | $1B–$5B | 3.0% | Very unlikely | <0.1% | Very unlikely |

**Why it fails here.** Data infrastructure startups often end by acquisition for the team, as Arroyo, Jitsu and Triplit did, or shut down if adoption stays hobbyist. A large exit needs becoming a default building block, as the object storage analogy suggests. Data infrastructure startups often end by acquisition for the team, as Arroyo, Jitsu and Triplit did, or shut down if adoption stays hobbyist. A large exit needs becoming a default building block, as the object storage analogy suggests, against cloud vendors.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Developers stay on Kafka, managed streaming or Redis streams | 45% | Kafka vendors are building diskless object storage versions and cloud providers sell serverless streams | Streamdal (streamdal), Arroyo (arroyo) | Win a use case Kafka serves poorly, such as agent state and per user streams |
| 2 | Hyperscalers or Cloudflare ship an equivalent | 35% | Object storage backed streams are a visible direction for large vendors | Replicate (replicate), Rivet (rivet) | Open source the core and move faster |
| 3 | Slow usage revenue delays a seed | 35% | Infrastructure revenue follows adoption over many months Large vendors are rebuilding Kafka on object storage and hyperscalers sell serverless streams, so a new API must beat them on price | Triplit (triplit), Arroyo (arroyo) | Charge early and show usage growth |

## Pros

- **Technically credible team on a real infrastructure gap**: Founders describe years of data systems work and a clear architectural thesis (https://www.kai-waehner.de/blog/2025/08/11/the-rise-of-diskless-kafka-rethinking-brokers-storage-and-the-kafka-protocol/)
- **Tailwind from AI agents needing durable state**: Agents and sandboxes need cheap per instance logs (https://www.automq.com/blog/top-warpstream-alternatives-diskless-kafka-byoc)

## Roadmap

### Get into YC

Show developer adoption and a few paying users

1. Open source or free tier with docs
2. Reach production use at 5 companies

You know it worked when: Hundreds of active developers and first paid usage

### Reach Seed

Show usage revenue growth and reliability

1. Publish uptime and benchmark data
2. Land agent platform customers

You know it worked when: Usage revenue above $30K a month

### Reach Series A

Become a default stream layer

1. Add enterprise features such as access control and compliance
2. Hire sales engineers

You know it worked when: ARR above $3M

### Reach Series B

Repeatable expansion with a second product or segment and efficient growth

1. Add a second wedge sold to the same buyer
2. Hire a sales leader and a customer success team
3. Show net revenue retention above 110 percent

You know it worked when: Revenue growth above 2x for a full year with stable gross margin

### Reach Series C and beyond

Category leadership with durable margins

1. Expand to adjacent markets or geographies
2. Build channel or platform partnerships
3. Show a path to profitability or a clear exit buyer

You know it worked when: Large enterprise customers and net retention above 120 percent

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 5 | Durable distributed logs with strong ordering, unlimited streams and low latency on object storage are hard; a small expert team can build a core in months but operating it reliably at scale is a long, risky effort. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 2 | s2.dev: s2.dev is a short letter plus digit name like S3 that signals the object storage analogy to engineers, but is hard to search and say aloud, so effect is neutral for a developer product. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Cloud providers and Cloudflare, Confluent and diskless Kafka vendors, Redpanda and StreamNative within ~18 months. Large vendors have distribution and could add a serverless stream primitive; the Kafka diskless proposals show the industry moving in this direction, though a new API gives a differentiated model. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Confluent and WarpStream | Kafka and diskless Kafka on object storage | Market leader | https://www.kai-waehner.de/blog/2025/08/11/the-rise-of-diskless-kafka-rethinking-brokers-storage-and-the-kafka-protocol/ |
| AutoMQ and Redpanda | Kafka compatible object storage streaming | Funded vendors | https://www.automq.com/blog/warpstream-vs-automq-object-storage-backed-kafka |
| Amazon MSK Serverless | Managed serverless Kafka | Large cloud customer base | https://jack-vanlightly.com/blog/2025/10/22/a-fork-in-the-road-deciding-kafkas-diskless-future |

### Demand evidence

- Vendors are rebuilding streaming on object storage, showing demand for cheaper durable streams (https://www.kai-waehner.de/blog/2025/08/11/the-rise-of-diskless-kafka-rethinking-brokers-storage-and-the-kafka-protocol/)
- Kafka alternatives are a recognised buying category with paid products (https://www.automq.com/blog/top-warpstream-alternatives-diskless-kafka-byoc)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Streamdal (streamdal) | Summer 2020 | Inactive | Streaming data tooling | Shut down after a seed |
| Arroyo (arroyo) | Winter 2023 | Acquired | Cloud native stream processing | Acquired, no verified round |
| Rivet (rivet) | Winter 2023 | Active | Infrastructure for agentic workloads | Alive, no verified round |
| LanceDB (lancedb) | Winter 2022 | Active | Open source database primitive | Series A after a few years |
| Replicate (replicate) | Winter 2020 | Acquired | Developer API for a new compute primitive | Series B then acquired |
| Triplit (triplit) | Winter 2021 | Inactive | Database for app developers | Wound down and acquired, no round |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 51% | 32% | python3 -I scripts/base_rates.py --tag "Developer Tools" --years 2022-2024: seed known-only ever, cond figure 0.51; the forecast window is 13.4 months so only the share reaching seed that early counts (time_to_milestones.csv p50 7 months, p75 20 months) | Window of 13.4 months from the as of date: the ever anchor is cut by the share of seeds that happen that early, with no lift for team or hype per the winners test rules. The odds do not rank this company against others. |
| Series A | 26% | 12% | python3 -I scripts/base_rates.py --tag "Developer Tools" --years 2022-2024: series_a cond 0.26 ever, given seed | The anchor is for reaching Series A ever; inside 13.4 months only fast seed companies get there (Series A median is 28 months from batch start), so the figure is far below the anchor by construction. |
| Series B | 19% | 5.0% | python3 -I scripts/base_rates.py --tag "Developer Tools" --years 2022-2024: series_b cond 0.19 ever | The anchor is ever; reaching a Series B inside the window needs a Series A and then a B within about two years of the batch, which the 2022 and later data shows only for a handful of companies. |
| Series C+ | 0.0% | 3.0% | python3 -I scripts/base_rates.py --tag "Developer Tools" --years 2022-2024: series_c cond 0.0 ever | The anchor is ever; a Series C or later inside the window is close to unobserved for batches this recent, so the number is a floor, not a forecast of a ceiling. |

## Assumptions and limits

- Window is 13.4 months from 2025-10-06 to 2026-11-17.
- LEAK-WEB: s2-dev; a market search returned pages naming the company and 2026 dated pages; those were ignored.
- Series C anchor n/a in cohort (0 percent), used as 0.0 for the record.

## Sources

- https://www.kai-waehner.de/blog/2025/08/11/the-rise-of-diskless-kafka-rethinking-brokers-storage-and-the-kafka-protocol/
- https://www.automq.com/blog/top-warpstream-alternatives-diskless-kafka-byoc
- https://www.automq.com/blog/warpstream-vs-automq-object-storage-backed-kafka
- https://jack-vanlightly.com/blog/2025/10/22/a-fork-in-the-road-deciding-kafkas-diskless-future
