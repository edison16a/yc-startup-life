# Evaluation: herdr

*As of 2026-10-05. Mode: summary. building the open agent runtime*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**An open source agent runtime with unusual traction and a probable seed, but monetization and platform risk limit later rounds.**

**Chance of getting into YC:** 5.0% (range 2.0%–10%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$1.5M | $8M–$15M | 16% | Unlikely | 0.8% | Very unlikely |
| Seed | $1.5M–$5M | $15M–$40M | 40% | Reasonable | 2.0% | Very unlikely |
| Seed | $5M–$12M | $40M–$100M | 24% | Reasonable | 1.2% | Very unlikely |
| Series A | $8M–$12M | $40M–$70M | 7.9% | Unlikely | 0.4% | Very unlikely |
| Series A | $12M–$25M | $70M–$150M | 12% | Unlikely | 0.6% | Very unlikely |
| Series A | $25M–$45M | $150M–$350M | 6.6% | Unlikely | 0.3% | Very unlikely |
| Series B | $25M–$40M | $150M–$300M | 2.6% | Very unlikely | 0.1% | Very unlikely |
| Series B | $40M–$70M | $300M–$700M | 2.6% | Very unlikely | 0.1% | Very unlikely |
| Series B | $70M–$120M | $700M–$1.5B | 1.3% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$70M | $300M–$700M | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $70M–$150M | $700M–$2B | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$300M | $2B–$5B | 0.2% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Herdr is a free Apache licensed runtime that keeps coding agent terminals alive and routes attention across machines. Its reported traction is much higher than typical YC applicants and a seed above the YC deal looks likely. The main risks are solo founder, no revenue, and agent vendors shipping similar features. Open source developer tool cohorts reach Series A at about 39 percent of seed companies, and the comps cmux, continue and fig show adoption without large rounds. The estimates rest on cohort base rates, a handful of real analogs and market searches limited to information available at the batch start, so they carry wide uncertainty and should be read as ranges, not points.

## Round by round: where and why it fails

### Getting into YC: 5.0%

**How we got the number.** Starting rate is about 1 percent with a 0.6 to 2 percent band. The company is already accepted, so this is a note only. A solo founder lowers odds slightly, but 25k GitHub stars, 340k downloads and a large plugin ecosystem are far stronger traction than most applicants show, which lifts the odds several times.

**Why it fails here.** YC would most plausibly say no because the founder is solo and the product is free open source with no revenue. Reviewers would worry that terminal tooling for coding agents is a feature that Anthropic, OpenAI or editors will ship, and that an Apache licensed runtime has no clear way to make money.

### Seed: P(reach this round | in YC) = 80% after the previous step; 80% cumulative if in YC; 4.0% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$1.5M | $8M–$15M | 20% | 16% | Unlikely | 0.8% | Very unlikely | Angel and pre seed rounds for a solo founder. |
| $1.5M–$5M | $15M–$40M | 50% | 40% | Reasonable | 2.0% | Very unlikely | Typical seed for open source developer tools with strong star growth. |
| $5M–$12M | $40M–$100M | 30% | 24% | Reasonable | 1.2% | Very unlikely | Upside seed led by a top dev tools fund, similar to Confident AI style adoption rounds scaled up for star counts. |

**Why it fails here.** Seed fails if the solo founder cannot show a path to revenue and investors treat the project as a free utility. Terminal tools struggle to charge. cmux raised no round beyond YC despite strong adoption and coasts shows a free tool with a modest launch. Investors may also pass on a one person team for a runtime that must be trusted.

### Series A: P(reach this round | in YC) = 33% after the previous step; 26% cumulative if in YC; 1.3% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $8M–$12M | $40M–$70M | 30% | 7.9% | Unlikely | 0.4% | Very unlikely | Flat A funded on adoption alone, judged against the cohort round size tables and current market benchmarks. |
| $12M–$25M | $70M–$150M | 45% | 12% | Unlikely | 0.6% | Very unlikely | Median band for 2022+ YC A rounds of about 14M. |
| $25M–$45M | $150M–$350M | 25% | 6.6% | Unlikely | 0.3% | Very unlikely | Upside if hosted or enterprise product takes off, judged against the cohort round size tables and current market benchmarks. |

**Why it fails here.** Series A fails if usage never turns into a paid hosted product or enterprise plan. Free terminal tools have rarely monetized, and fig, a terminal tool with wide adoption, only reached a seed before an acquisition. Platform vendors may ship agent session management inside their own clients, removing the need.

### Series B: P(reach this round | in YC) = 25% after the previous step; 6.6% cumulative if in YC; 0.3% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $25M–$40M | $150M–$300M | 40% | 2.6% | Very unlikely | 0.1% | Very unlikely | Lower B, judged against the cohort round size tables and current market benchmarks. |
| $40M–$70M | $300M–$700M | 40% | 2.6% | Very unlikely | 0.1% | Very unlikely | Market series B deal near 40M, judged against the cohort round size tables and current market benchmarks. |
| $70M–$120M | $700M–$1.5B | 20% | 1.3% | Very unlikely | <0.1% | Very unlikely | Breakout open source infrastructure, judged against the cohort round size tables and current market benchmarks. |

**Why it fails here.** Series B fails if the project remains a developer convenience and not a revenue engine. Open source companies need a paid tier with strong conversion, and rivals can fork under the Apache license. continue reached only a 3M seed before being acquired by Cursor. Reaching this step also takes time, and the milestone can slip by a year or more before investors accept the evidence, so the odds here already account for timing risk, thin traction data and the small sample behind the cohort anchors.

### Series C+: P(reach this round | in YC) = 20% after the previous step; 1.3% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$70M | $300M–$700M | 40% | 0.5% | Very unlikely | <0.1% | Very unlikely | Low C, judged against the cohort round size tables and current market benchmarks. |
| $70M–$150M | $700M–$2B | 45% | 0.6% | Very unlikely | <0.1% | Very unlikely | Market series C near 77M, judged against the cohort round size tables and current market benchmarks. |
| $150M–$300M | $2B–$5B | 15% | 0.2% | Very unlikely | <0.1% | Very unlikely | Category leader, judged against the cohort round size tables and current market benchmarks. |

**Why it fails here.** Series C fails if agents move into hosted cloud tools where a local runtime is irrelevant, or large vendors give away session management. Few terminal and developer tools in the data reached later rounds, and those that did had enterprise revenue, which an Apache licensed runtime must build from scratch.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 98% | Very likely |
| Acquired or IPO under $100M | $10M–$100M | 33% | Reasonable | 1.7% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 13% | Unlikely | 0.7% | Very unlikely |
| Acquired or IPO over $1B | $1B–$5B | 4.0% | Very unlikely | 0.2% | Very unlikely |

**Why it fails here.** Most paths end in a stall after launch hype fades or a sale of the team to an AI coding company, as continue and fig did. Large exits need a paid business on top of an open runtime, which is rare. Reaching this step also takes time, and the milestone can slip by a year or more before investors accept the evidence, so the odds here already account for timing risk, thin traction data and the small sample behind the cohort anchors.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Platform vendors build session management into their agent clients | 35% | Anthropic, OpenAI and editors already ship cloud and background agents and could add attention queues. | Continue (continue), Fig (fig) | Stay agent neutral and own the cross machine runtime and plugin ecosystem. |
| 2 | No monetization for a free Apache licensed runtime | 35% | cmux has strong adoption but no round beyond YC, and terminal tools rarely charge. | cmux (cmux), Coasts (coasts) | Hosted sync, team features and enterprise control plane. |
| 3 | Solo founder cannot scale support and security trust | 20% | The team is one person with a background project in Turkey, and a runtime that owns sessions must be reliable. | Stably AI (Orca) (stably-ai-orca) | Hire early from the open source community. |
| 4 | Hype fades as agents shift to cloud sandboxes | 20% | Many coding agents are moving to hosted environments, reducing local terminal usage. | Coasts (coasts) | Support remote and sandbox machines as first class. |

## Pros

- **Strong open source adoption claims**: 25k stars and 340k downloads reported four months after launch, with 500 community plugins. (https://alternativeto.net/software/agent-manager/)
- **Fits a real workflow pain**: Fleets of coding agents need persistence and attention routing, which tmux does not provide. (https://agentsroom.dev/alternatives/tmux)

## Roadmap

### Get into YC

Keep the open source lead.

1. Ship remote and mobile clients
2. Grow plugin contributors

You know it worked when: 50k stars and weekly active users

### Reach Seed

Show a paid path.

1. Launch hosted sync and team tier
2. Sign 20 paying teams

You know it worked when: Paid MRR above 20K

### Reach Series A

Turn adoption into revenue.

1. Build enterprise control plane
2. Add audit and policy

You know it worked when: ARR above 1.5M

### Reach Series B

Become the standard runtime.

1. Integrate with all major agents
2. Sell to platform teams

You know it worked when: ARR above 10M

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A persistent background server that owns terminal sessions, detects agent states across many tools and syncs across machines is a manageable engineering task for one strong developer. The hard parts are reliable agent detection as tools change and security of remote access, which grow with scale. |
| Name and brand (5 = iconic, drives growth; effect on success: helps) | 3 | herdr: A short coined word with a clear herding image matches the product of managing fleets, similar to how cmux and tmux use short names developers type. It is a modest growth driver for a developer audience. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Anthropic, OpenAI, Cursor, Terminal vendors within ~6 months. Agent vendors could add attention queues and persistence to their own clients in months. The open license and plugin ecosystem make it a community standard if neutral, but a platform feature could remove demand. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| cmux | Native macOS terminal for agents with notification rings and a socket API. | Open source and active. | https://alternativeto.net/software/agent-manager/ |
| tmux | The status quo for persistent terminal sessions. | Ubiquitous but agent blind. | https://agentsroom.dev/alternatives/tmux |
| AgentsRoom and similar companion apps | Visual status and notifications for agents. | Vendor marketing, unverified. | https://agentsroom.dev/alternatives/tmux |

### Demand evidence

- Several tools already compete to replace tmux for agent fleets, showing developer demand for agent aware session management. (https://alternativeto.net/software/agent-manager/)
- tmux has no concept of agent state, which is the stated gap. (https://agentsroom.dev/alternatives/tmux)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| cmux (cmux) | Summer 2024 | Active | Open source terminal for coding agents with notifications and socket API, the closest comp. | Active, strong developer traction, no funding beyond YC found. |
| Stably AI (Orca) (stably-ai-orca) | Winter 2022 | Active | Open source terminal agent orchestrator. | Active, limited verified funding. |
| Fig (fig) | Summer 2020 | Acquired | Developer terminal tool with free product led growth. | 2.2M seed in 2020, acquired by AWS in 2023 and sunset. |
| Continue (continue) | Summer 2023 | Acquired | Open source coding agent with tens of thousands of stars. | 3M seed in 2025, acquired by Cursor in 2026. |
| Coasts (coasts) | Fall 2025 | Inactive | Free open source tool for agent worktrees. | Listed inactive, modest launch. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 67% | 80% | python3 -I scripts/base_rates.py --years 2018-2025 --tag "Developer Tools" --calibration-only: seed cond 67 percent (n=42), known 67 percent | Within 1.2x. Lift because 25k stars and 340k downloads give investors a visible signal, in a field where open source developer tools raise on adoption. |
| Series A | 39% | 33% | python3 -I scripts/base_rates.py --years 2018-2025 --tag "Developer Tools" --calibration-only: series_a cond 39 percent (n=28) | Within 0.85x. Open source dev tools reach A less than half the time, and the monetization path for terminal tools is unclear. |
| Series B | 18% | 25% | python3 -I scripts/base_rates.py --years 2018-2025 --tag "Developer Tools" --calibration-only: series_b cond 18 percent (n=11) | Within 1.4x, lifted for an exceptional open source following. |
| Series C+ | 36% | 20% | python3 -I scripts/base_rates.py --years 2018-2025 --tag "Developer Tools" --calibration-only: series_c cond 50 percent (n=2); tiny sample, overall table cond 36 percent | Discounted for a tiny sample and a young company. |

## Assumptions and limits

- Blind test: only the batch input file was used for the company.
- A seed here means a round above the YC deal of about 500K within about 12 months of the batch start.
- A market search result named this company directly; it was ignored (LEAK-WEB).
- Traction figures come from the company description and are unverified.

## Sources

- https://alternativeto.net/software/agent-manager/
- https://agentsroom.dev/alternatives/tmux
