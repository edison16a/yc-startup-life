# Evaluation: Minicor

*As of 2026-04-06. Mode: summary. Scalable windows desktop automations*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A real but crowded wedge: seed is likely, later rounds depend on beating computer use from big platforms.**

**Chance of getting into YC:** 10% (range 5.0%–15%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $8M–$15M | 12% | Unlikely | 1.2% | Very unlikely |
| Seed | $2M–$5M | $15M–$35M | 34% | Reasonable | 3.4% | Very unlikely |
| Seed | $5M–$12M | $35M–$80M | 16% | Unlikely | 1.6% | Very unlikely |
| Series A | $4M–$8M | $25M–$45M | 3.7% | Very unlikely | 0.4% | Very unlikely |
| Series A | $10M–$20M | $50M–$110M | 10% | Unlikely | 1.0% | Very unlikely |
| Series A | $20M–$35M | $110M–$250M | 4.7% | Very unlikely | 0.5% | Very unlikely |
| Series B | $15M–$30M | $80M–$160M | 0.9% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $160M–$400M | 1.5% | Very unlikely | 0.1% | Very unlikely |
| Series B | $60M–$120M | $400M–$900M | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$70M | $250M–$600M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $70M–$150M | $600M–$1.5B | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $1.5B–$4B | 0.2% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Minicor sells reliable API access to legacy Windows apps for AI startups. Demand is real and the AI infrastructure funding climate is warm, which makes a seed more likely than not. The doubts start at Series A: peers like Cyberdesk and Skyvern show slow funding, and UiPath, Microsoft and model labs can ship the same capability. The story improves if it lands enterprise or healthcare end clients with real volume. The forecast treats the day one description as the best case, anchors on the 2022 to 2024 cohort of researched YC companies, and widens the uncertainty because funding data for recent batches is incomplete and right censored.

## Round by round: where and why it fails

### Getting into YC: 10%

**How we got the number.** Note only: the company is already accepted to YC Spring 2026, so this is not a forecast. Prior of about 1 percent for a random applicant (yc_acceptance.md) is not informative here. The work is in the ladder.

**Why it fails here.** Not applicable because the company was accepted. A reviewer would most plausibly worry that computer use agents from model labs and UiPath make a thin wrapper around Windows VMs easy to copy. Because acceptance is already a fact in this test, the estimate is a placeholder and the forecast value sits in the funding ladder that follows.

### Seed: P(reach this round | in YC) = 62% after the previous step; 62% cumulative if in YC; 6.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $8M–$15M | 20% | 12% | Unlikely | 1.2% | Very unlikely | Small pre seed or angel round after the YC deal, common for infrastructure teams with a few pilots. |
| $2M–$5M | $15M–$35M | 55% | 34% | Reasonable | 3.4% | Very unlikely | Core outcome: 2022+ B2B seed median is about 3.3M (base_rates.py) and AI infrastructure rounds run higher. |
| $5M–$12M | $35M–$80M | 25% | 16% | Unlikely | 1.6% | Very unlikely | Upside if logos in healthcare or insurance back office prove demand, as with Sola. |

**Why it fails here.** The most likely stall is that customers are AI startups that themselves have few paying clients, so revenue stays at pilots. Investors may also doubt that a Windows VM plus a vision model is a company when UiPath, Microsoft and the model labs ship computer use. Cyberdesk, a close peer, shows no confirmed round after its batch.

### Series A: P(reach this round | in YC) = 30% after the previous step; 19% cumulative if in YC; 1.9% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $25M–$45M | 20% | 3.7% | Very unlikely | 0.4% | Very unlikely | Thin round on modest annual recurring revenue. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $10M–$20M | $50M–$110M | 55% | 10% | Unlikely | 1.0% | Very unlikely | Matches the 2022+ B2B Series A median of about 14.9M. |
| $20M–$35M | $110M–$250M | 25% | 4.7% | Very unlikely | 0.5% | Very unlikely | Upside if usage per customer compounds across many enterprise end clients. |

**Why it fails here.** Series A fails if recurring revenue stays below the level investors expect, roughly 1M or more with growth, or if gross margin is hurt by VM and vision model costs. Concentration is a risk when a few AI customers drive usage. Skyvern raised only a seed more than two years after its batch, which is the likely path for a thin wedge.

### Series B: P(reach this round | in YC) = 16% after the previous step; 3.0% cumulative if in YC; 0.3% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$160M | 30% | 0.9% | Very unlikely | <0.1% | Very unlikely | Flat or modest step up. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $30M–$60M | $160M–$400M | 50% | 1.5% | Very unlikely | 0.1% | Very unlikely | 2022+ B2B Series B median about 45M. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $60M–$120M | $400M–$900M | 20% | 0.6% | Very unlikely | <0.1% | Very unlikely | Upside if it becomes the standard bridge to legacy apps. |

**Why it fails here.** Series B fails when the product is replaced by agent platforms that ship their own desktop control, or when enterprises keep building in house. Growth must show net revenue retention above 120 percent and low support cost per automation; self healing flows that still need human fixes keep margins thin.

### Series C+: P(reach this round | in YC) = 30% after the previous step; 0.9% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$70M | $250M–$600M | 40% | 0.4% | Very unlikely | <0.1% | Very unlikely | Growth round at moderate scale. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $70M–$150M | $600M–$1.5B | 40% | 0.4% | Very unlikely | <0.1% | Very unlikely | Typical unicorn path for infrastructure with enterprise contracts. |
| $150M–$400M | $1.5B–$4B | 20% | 0.2% | Very unlikely | <0.1% | Very unlikely | Upside if it becomes core agent infrastructure. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Later rounds fail if growth decays once the early AI customers saturate, or if hyperscalers bundle agent desktops cheaply. Bird style breakout cases are rare and the sample at this stage is small, so the odds are close to the all year base rate with a modest discount.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 96% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 25% | Reasonable | 2.5% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 15% | Unlikely | 1.5% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 5.0% | Unlikely | 0.5% | Very unlikely |

**Why it fails here.** Most likely a stall or a small acquihire by an RPA or agent platform, since the same capability can be built by a well funded rival within months and VM cost and flakiness cap margins. A meaningful exit needs a durable lead in a category where rivals can copy features and raise more money, and most companies in the reference cohort stay small, are acquired cheaply or stop operating before that point.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Computer use from model labs and UiPath, Microsoft and AWS commoditizes Windows desktop control | 40% | UiPath says its computer use covers desktop and Citrix, and Microsoft and AWS market managed agent desktops for apps without APIs. | Cyberdesk (cyberdesk), Warpdrive by Synthetic Minds (synthetic-minds) | Win on reliability, self healing and observability for production, and own customer integrations. |
| 2 | Customers are AI startups with small revenue, so demand is concentrated and fragile | 30% | The buyer is other early AI companies, whose own volume determines usage; Skyvern needed years for a seed. | Skyvern (skyvern), Cyberdesk (cyberdesk) | Move to direct enterprise and healthcare accounts. |
| 3 | Unit economics: VM, vision model and human repair cost leave thin margins | 25% | Each call runs a Windows VM and a model; Citrix and on premises deployments need onsite work. | Automat (automat), Sola (sola) | Cache learned flows, replace vision calls with deterministic steps once stable. |

## Pros

- **Real pain with a long tail of Windows apps that lack APIs.**: Hyperscalers and UiPath target the same gap, validating demand. (https://www.uipath.com/ai/what-is-computer-use)
- **Observability and an agent friendly MCP setup match how buyers work.**: Video replay, logging and Slack alerts are in the description. (https://minicor.com)

## Roadmap

### Get into YC

Show paying production usage.

1. Sign three AI customers on usage pricing
2. Publish reliability numbers per automation

You know it worked when: Paid calls per week and a success rate above 95 percent.

### Reach Seed

Raise above 500K within 12 months of the batch.

1. Add two enterprise end client logos
2. Show falling cost per call

You know it worked when: Recurring revenue of 20K a month or more.

### Reach Series A

Reach scalable repeatable revenue.

1. Build a self serve flow builder through the MCP
2. Land one regulated industry

You know it worked when: About 1M annual recurring revenue with 3x growth.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A small team can build VM orchestration, vision driven control and replay in three months. Reliability across Citrix, latency and self healing at scale are hard but solvable, and depend on third party vision model quality and speed. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Minicor: An invented short name is a common pattern among YC infrastructure companies and neither helps nor hurts, as with Firecrawl where the product mattered more than the name. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by UiPath, Microsoft, AWS, Anthropic and OpenAI computer use within ~9 months. Rivals have the distribution and incentive and could ship a comparable endpoint in under a year; the defense is production grade reliability and customer relationships rather than technology. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| UiPath | Incumbent RPA with computer use covering desktop and Citrix. | FY2026 revenue about 1.6B, up 13 percent. | https://www.uipath.com/ai/what-is-computer-use |
| Cyberdesk | YC startup automating legacy Windows apps via API. | Launched in 2025 with production use in healthcare. | https://www.ycombinator.com/launches/O4a-cyberdesk-the-computer-use-agent-for-developers-to-automate-legacy-windows-apps |
| Microsoft Windows 365 for Agents and AWS WorkSpaces | Managed desktops for agents to drive apps without APIs. | Hyperscaler distribution. | https://www.mindstudio.ai/blog/aws-workspaces-ai-agents-legacy-desktop-software |

### Demand evidence

- UiPath still grows at 13 percent on about 1.6B revenue, showing enterprises pay to automate legacy interfaces. (https://www.zacks.com/stock/news/2716905/automation-boom-fuels-path-s-performance-in-growing-rpa-market)
- Hyperscalers are building desktops for agents because many apps have no API. (https://www.mindstudio.ai/blog/aws-workspaces-ai-agents-legacy-desktop-software)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Cyberdesk (cyberdesk) | Summer 2025 | Active | Direct rival, Windows legacy app agent for developers, Summer 2025. | Active, no confirmed round after the batch; shows slow funding even in a hot space. |
| Automat (automat) | Winter 2023 | Active | Agentic automation against legacy RPA, Winter 2023. | Reached a 15.5M Series A in 2025, about two years after the batch. |
| Sola (sola) | Summer 2023 | Active | Copilot for RPA, Summer 2023. | 3.5M seed then a 17.5M Series A in 2025, led by a top fund. |
| Skyvern (skyvern) | Summer 2023 | Active | API for browser workflows with agents. | Only a 2.7M seed more than two years after the batch. |
| Warpdrive by Synthetic Minds (synthetic-minds) | Summer 2018 | Inactive | Screen recording to desktop automation, Summer 2018. | Shut down; automation without durable demand or distribution. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 62% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | Within 0.75x to 1.1x of the anchor. Up for hot AI infrastructure demand and a nine person team, down because the buyer is other AI startups, a small and young customer base. |
| Series A | 33% | 30% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | 0.9x of the anchor. Automat and Sola reached Series A in the RPA reinvention wave, so no larger discount is justified. |
| Series B | 17% | 16% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | Near the anchor. |
| Series C+ | 36% | 30% | python3 -I scripts/base_rates.py --years 2022-2024 --industry B2B --calibration-only: seed cond 61% (n=88; 50/61/68 lower/known/upper), series_a cond 33% (n=54), series_b cond 17% (n=18); series_c all-year cond 36% (n=55) | Slightly under the anchor because few comparable companies got this far. |

## Assumptions and limits

- Pretend date is 2026-04-06 and only the input file describes the company.
- Seed means a round above about 500K within about 12 months of batch start.
- Base rate cohort B2B 2022 to 2024 has right censoring, so known only rates are biased low.

## Sources

- https://www.uipath.com/ai/what-is-computer-use
- https://www.zacks.com/stock/news/2716905/automation-boom-fuels-path-s-performance-in-growing-rpa-market
- https://www.mindstudio.ai/blog/aws-workspaces-ai-agents-legacy-desktop-software
- https://www.ycombinator.com/launches/O4a-cyberdesk-the-computer-use-agent-for-developers-to-automate-legacy-windows-apps
