# Evaluation: Deeptrace

*As of 2025-10-06. Mode: summary. AI agents for on-call*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A real pain with active money in the category, but a crowded AI SRE field makes a seed in 13 months about a coin flip and Series A in the window unlikely.**

**Chance of getting into YC:** 3.0% (range 1.0%–7.8%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$16M | 12% | Unlikely | 0.4% | Very unlikely |
| Seed | $3M–$6M | $16M–$32M | 19% | Unlikely | 0.6% | Very unlikely |
| Seed | $6M–$12M | $30M–$60M | 14% | Unlikely | 0.4% | Very unlikely |
| Seed | $12M–$20M | $60M–$110M | 5.0% | Unlikely | 0.1% | Very unlikely |
| Series A | $6M–$10M | $30M–$50M | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$18M | $50M–$90M | 1.8% | Very unlikely | <0.1% | Very unlikely |
| Series A | $18M–$30M | $90M–$160M | 1.1% | Very unlikely | <0.1% | Very unlikely |
| Series A | $30M–$60M | $200M–$450M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$25M | $70M–$130M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$45M | $130M–$300M | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series B | $45M–$90M | $300M–$700M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $90M–$150M | $700M–$1.5B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$60M | $200M–$500M | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $60M–$120M | $500M–$1.2B | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $120M–$300M | $1.2B–$3B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $300M–$600M | $3B–$8B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Deeptrace sells AI agents that handle production alerts for engineering teams, a category where buyers already pay for on-call software and investors were funding rivals by mid 2025. The team is four people, small and technical, and claims live use at fast growing companies. The cohort anchor for AI companies reaching a seed is about 64 percent ever, trimmed to about 50 percent for a 13 month window; Series A inside the window is only about 8 percent because the median time to A is 28 months. The odds do not rank this company against others. The main risks are crowding by better funded rivals, buyers not trusting autonomous production changes, and incumbent on-call vendors bundling similar agents. The upside is a pivot toward a narrow stack where resolution quality is provable.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Start from the roughly 1 percent applicant prior (band 0.6 to 2 percent, references/yc_acceptance.md). Adjust up about 2x because AI developer tools fit YC's current priorities and the description claims live production use at fast growing customers, and a small technical team is typical of accepted AI infrastructure companies. Adjust down because AI SRE is already crowded with funded rivals and traction is unverified. Net about 3 percent, inside the 0.3 to 15 percent guardrail.

**Why it fails here.** YC would most plausibly say the space is already occupied: several funded AI SRE and incident response startups exist, and a four person team has to show why its agent resolves alerts better than them. Unnamed customers and no revenue figures leave the traction claim unprovable, so an interviewer may not see founders with a unique insight or unfair access.

### Seed: P(reach this round | in YC) = 50% after the previous step; 50% cumulative if in YC; 1.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$16M | 25% | 12% | Unlikely | 0.4% | Very unlikely | Small post YC round under $3M from angels and a micro fund. Common for a team of two to four before a customer logo is public; the 2022 and later seed row has p25 of $2.8M, so this is the lower quartile. |
| $3M–$6M | $16M–$32M | 38% | 19% | Unlikely | 0.6% | Very unlikely | Institutional seed at the center of the 2022 and later table (median $3.5M to $4.1M) shifted up a little for AI native B2B. Most likely if two or three paying design partners are visible. |
| $6M–$12M | $30M–$60M | 27% | 14% | Unlikely | 0.4% | Very unlikely | Large AI seed. Among confirmed 2026 raises above $1M the median was $6.0M, but press covers big rounds more, so this band is kept below the central one. |
| $12M–$20M | $60M–$110M | 10% | 5.0% | Unlikely | 0.1% | Very unlikely | Upside: a hot category plus fast revenue and a lead from a multi stage fund. Rare in the YC data. |

**Why it fails here.** The most likely miss is that investors treat AI SRE as a category already claimed by better known rivals, and want revenue or named logos that four founders cannot yet show within 13 months. Relvy, a Fall 2024 YC company in the same area, shows only the YC money publicly, while DrDroid did land an Accel led seed in June 2024, so the category does fund but unevenly.

### Series A: P(reach this round | in YC) = 8.0% after the previous step; 4.0% cumulative if in YC; 0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $30M–$50M | 20% | 0.8% | Very unlikely | <0.1% | Very unlikely | Thin or bridge style A under $10M, a down or flat round relative to the seed. |
| $10M–$18M | $50M–$90M | 45% | 1.8% | Very unlikely | <0.1% | Very unlikely | Central band: 2022 and later series A median $14.15M, with market medians near $17M. |
| $18M–$30M | $90M–$160M | 27% | 1.1% | Very unlikely | <0.1% | Very unlikely | Strong A led by a top fund after clear revenue growth. |
| $30M–$60M | $200M–$450M | 8.0% | 0.3% | Very unlikely | <0.1% | Very unlikely | Upside: breakout category leader, AI infrastructure style round. |

**Why it fails here.** A Series A needs recurring revenue that survives a pilot, and AI SRE agents must prove they cut incidents without making wrong changes in production. Within the window the team would have to go from pilots to six figure recurring revenue; Rootly took about 25 months between its seed and A, and DrDroid shows no A after a mid 2024 seed.

### Series B: P(reach this round | in YC) = 35% after the previous step; 1.4% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$25M | $70M–$130M | 25% | 0.3% | Very unlikely | <0.1% | Very unlikely | Small or extension B: growth slowed after the A, so the round is modest or flat to the prior valuation. |
| $25M–$45M | $130M–$300M | 45% | 0.6% | Very unlikely | <0.1% | Very unlikely | Typical B, 2022 and later median about $37M to $40M. |
| $45M–$90M | $300M–$700M | 22% | 0.3% | Very unlikely | <0.1% | Very unlikely | Large B for a category leader with strong revenue growth and a top tier lead investor. |
| $90M–$150M | $700M–$1.5B | 8.0% | 0.1% | Very unlikely | <0.1% | Very unlikely | Upside round if the company becomes the clear category winner with outsized growth. |

**Why it fails here.** By the B the company must show enterprise scale revenue and gross margins despite large model inference costs per investigation. The likely failure is a platform vendor such as an observability incumbent offering a bundled agent, so growth stalls at mid market and investors pass. Rootly's path to A took about two years and it has not shown a B in the record.

### Series C+: P(reach this round | in YC) = 34% after the previous step; 0.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$60M | $200M–$500M | 30% | 0.1% | Very unlikely | <0.1% | Very unlikely | Modest C with a flat valuation to the B, reflecting slower growth and tougher market multiples. |
| $60M–$120M | $500M–$1.2B | 45% | 0.2% | Very unlikely | <0.1% | Very unlikely | Typical C or D, 2022 and later median $74M to $150M. |
| $120M–$300M | $1.2B–$3B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Large growth round for a company with strong enterprise revenue and expanding margins. |
| $300M–$600M | $3B–$8B | 5.0% | <0.1% | Very unlikely | <0.1% | Very unlikely | Category winner raising a very large round on a premium valuation. |

**Why it fails here.** Reaching a C needs a category leader position in AI incident response against rivals that raised large rounds earlier and bundle with incumbents. The usual failure is a strategic acquisition at B stage valuation, or growth that plateaus once the best early adopters are saturated and enterprise sales cycles lengthen.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 22% | Reasonable | 0.7% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 18% | Unlikely | 0.5% | Very unlikely |
| Acquired or IPO over $1B | $1B–$6B | 5.0% | Unlikely | 0.1% | Very unlikely |

**Why it fails here.** Most AI infrastructure agent startups in a crowded category end by acquihire or fade after the seed, as Neptune.io did after a seed of about $1M in a similar alert fix idea. Incumbents in on-call such as PagerDuty ship agents of their own, which compresses independent value.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Crowded AI SRE category with better funded rivals and a thin differentiation story | 45% | By late 2025 several AI incident response startups and the incumbents on-call vendors already sell similar agents, and records show Relvy stuck at YC level funding in the same wedge. | Relvy AI (relvy-ai), Neptune.io (neptune-io) | Pick a narrow stack or customer type where resolution accuracy is provable and publish before and after numbers from a few named customers. |
| 2 | Trust and safety: agents that act on production make costly mistakes, so buyers keep humans in the loop and pay less | 30% | Autonomous remediation touches live systems, and engineering teams adopt read only investigation first; this caps early contract value. | DrDroid (drdroid), Rootly (rootly) | Start with read only root cause with citations, earn write access through approvals and audit logs. |
| 3 | Incumbent bundling by on-call and observability vendors | 30% | PagerDuty and similar vendors own the alert stream and can add an agent at near zero marginal price, which is how Neptune.io's niche was squeezed. | PagerDuty (pagerduty), Neptune.io (neptune-io) | Be vendor neutral across observability stacks and win on resolution quality. |

## Pros

- **Real, paid on-call pain with proven budgets**: PagerDuty is public and Rootly raised a Series A, so teams already pay to manage alerts. (https://rootly.com)
- **Fast ship cycle on frontier models**: A four person technical team can build a working agent quickly and iterate with customers, as DrDroid did before its Accel led seed. (https://www.ycombinator.com/companies/drdroid)

## Roadmap

### Get into YC

Show production use at two or three named fast growing companies with measured time saved.

1. Instrument each deployment to report triage minutes saved per alert and resolution accuracy.
2. Get one customer to be quotable in the application and demo.

You know it worked when: Three paying or committed customers with a written before and after metric.

### Reach Seed

Convert pilots into recurring contracts that distinguish Deeptrace from Traversal and Resolve AI.

1. Narrow to one stack and one incident type where the agent is clearly better.
2. Publish accuracy benchmarks on real alert datasets.

You know it worked when: $20K to $50K monthly recurring revenue and a lead investor term sheet.

### Reach Series A

Prove repeatable enterprise sales with write access to production.

1. Hire a first sales engineer and land three accounts above $50K a year.
2. Ship approval workflows and audit logs for autonomous fixes.

You know it worked when: $1M or more annual recurring revenue with net retention above 110 percent.

### Reach Series B

Show the product scales across customers without per customer tuning.

1. Cut inference cost per investigation to keep gross margin above 70 percent.
2. Add integrations so deployment takes days.

You know it worked when: $8M to $10M annual recurring revenue and low churn.

### Reach Series C and beyond

Be a category leader in autonomous production engineering.

1. Expand from alerts to deploys, capacity and reliability work.
2. Open a second buying center beyond SRE.

You know it worked when: $30M or more annual recurring revenue and strategic partnerships.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | The hard part is accurate root cause reasoning across noisy logs, metrics, traces and code with low false positives, plus safe integrations into many observability stacks. A four person team can ship a working triage agent in three months using frontier models, but reliability across diverse customer environments is the real work and it is not a hard moat. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Deeptrace: A short invented compound like Rootly or Vapi style names is typical of YC infrastructure companies and works, but Deeptrace sits near existing trace and observability brands, so it is neutral and does not move the ladder. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by PagerDuty, Datadog, incident.io, Rootly within ~9 months. Observability and on-call vendors already hold the alert data and customer relationships, and frontier model labs ship coding agents that can read logs. A resourced rival could ship a comparable investigator in six to nine months, though depth on resolution is harder to copy. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Traversal | Enterprise AI SRE agent for triage, root cause and remediation. | Announced $48M across seed and Series A in June 2025 led by Sequoia and Kleiner Perkins. | https://builtin.com/articles/traversal-raises-48m-to-launch-ai-sre-20250620 |
| Resolve AI | Agentic AI for production engineering, from two ex Splunk founders. | Well funded early stage rival in autonomous incident response (details not verified before the as of date). | https://resolve.ai |
| Rootly and PagerDuty | On-call and incident management platforms adding AI features. | Rootly raised a $12M Series A in 2023 and PagerDuty is public; both own the alert workflow. | https://rootly.com |
| Status quo: on-call engineers and runbooks | Humans triage alerts with dashboards and runbooks. | Default for nearly every team; the switching cost is trust, not price. | https://www.pagerduty.com |

### Demand evidence

- Investors put tens of millions into AI SRE agents by mid 2025, signalling buyer demand for automating alert triage. (https://builtin.com/articles/traversal-raises-48m-to-launch-ai-sre-20250620)
- On-call tooling is a proven paid category: Rootly raised a Series A and PagerDuty is a public company. (https://rootly.com)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Relvy AI (relvy-ai) | Fall 2024 | Active | Fall 2024 YC company building AI debugging for incident response, same wedge a year earlier. | Active three person team; only about $500K YC level funding is reported by aggregators, no public customers or later round as of the record, so the category does not guarantee a seed. |
| DrDroid (drdroid) | Winter 2023 | Active | AI SRE assistant for production issues, Winter 2023 batch. | Seed round led by Accel with YC announced June 2024, after founders with relevant engineering background; evidence that investors fund this wedge. |
| Rootly (rootly) | Summer 2021 | Active | Incident response and on-call tooling sold to engineering teams, Summer 2021. | Seed of $3.2M in July 2021 and $12M Series A in August 2023, about 25 months later: the realistic pace to an A even for a well regarded team in this niche. |
| Neptune.io (neptune-io) | Summer 2014 | Inactive | Self healing platform that fixed server alerts automatically, Summer 2014, an earlier try at the same idea. | Raised about $1M and is now listed inactive; competing against New Relic and PagerDuty without a way to win distribution. |
| PagerDuty (pagerduty) | Summer 2010 | Public | The on-call incumbent that grew out of YC. | Became a public company; shows the on-call budget is real and also that a strong incumbent owns the pager workflow Deeptrace must plug into. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 64% | 50% | python3 -I scripts/base_rates.py --calibration-only --tag AI: seed cond 64 percent (n=183), known only 64, lower 51, upper 71. python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2026: seed 52 percent (n=163). Window is 13 months from 2025-10-06 to 2026-11-17; time_to_milestones.csv 2022+ months_to_seed p25 3, median 6, p75 14.2. | The anchors are for ever reaching a seed. The 13 month window covers about 75 percent of the reachers' timing (p75 is 14 months), so about 0.64 times 0.78 near 0.50, and I did not lift for the hot category or for the production claim because the winners test showed such lifts do not rank companies. The seed here means an outside round above about $1M, not the standard $500K YC deal. These odds do not rank this company against others. |
| Series A | 30% | 8.0% | python3 -I scripts/base_rates.py --calibration-only --tag AI: series_a cond 30 percent (n=117), lower 15, known 19, upper 36. time_to_milestones.csv 2022+ months_to_series_a p25 19.4, median 28.0. | Window anchored: the same 13 month window ends well before the median 28 months to Series A, so only the fastest quarter of seed companies reach A inside it. 0.30 times about 0.27 gives 0.08, more than 2x below the ever anchor, because of the window and not because of company quality. Rootly took 25 months from seed to A. |
| Series B | 31% | 35% | python3 -I scripts/base_rates.py --calibration-only --tag AI: series_b cond 31 percent (n=35), lower 5, known 6, upper 26. | Slightly above the anchor (1.13x, inside the 1.25x cap) since a company that has raised an A in a category with public nine figure rounds can often raise a B, but this is ever and not windowed. |
| Series C+ | 45% | 34% | python3 -I scripts/base_rates.py --calibration-only --tag AI: series_c cond 45 percent (n=11), small sample; B2B all eras 50 percent (n=28). | Below the anchor (0.76x) because the AI cohort n is 11 and the category will be consolidating by then. Ever, not windowed. |

## Assumptions and limits

- Only the as of date input was used: description, batch, team of 4, San Francisco.
- Window is 13 months from 2025-10-06 to 2026-11-17; seed means an outside round above about $1M, not the YC deal.
- Customer traction claims in the description are unverified.
- Comparable records after 2025-10-06 were ignored. The comps tool also returned later batches and I did not use them.
- Funding data for 2022+ analogs is partial and right censored.

## Sources

- https://builtin.com/articles/traversal-raises-48m-to-launch-ai-sre-20250620
- https://rootly.com
- https://resolve.ai
- https://www.pagerduty.com
- https://www.ycombinator.com/companies/drdroid
