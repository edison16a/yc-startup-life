# Evaluation: Scott AI

*As of 2025-10-06. Mode: summary. The planning layer for teams that build with coding agents*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A crowded, platform exposed planning layer for coding agents; seed in 13 months is plausible but below even.**

**Chance of getting into YC:** 3.0% (range 1.0%–9.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$20M | 11% | Unlikely | 0.3% | Very unlikely |
| Seed | $3M–$6M | $15M–$35M | 16% | Unlikely | 0.5% | Very unlikely |
| Seed | $6M–$12M | $30M–$70M | 9.8% | Unlikely | 0.3% | Very unlikely |
| Seed | $12M–$25M | $60M–$150M | 4.1% | Very unlikely | 0.1% | Very unlikely |
| Series A | $5M–$8M | $25M–$45M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series A | $8M–$15M | $45M–$90M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series A | $15M–$25M | $90M–$180M | 0.5% | Very unlikely | <0.1% | Very unlikely |
| Series A | $25M–$50M | $180M–$400M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series B | $15M–$25M | $80M–$150M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $25M–$45M | $150M–$300M | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $45M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $80M–$150M | $700M–$1.5B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$50M | $250M–$500M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $50M–$100M | $500M–$1B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $100M–$200M | $1B–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $200M–$500M | $2B–$5B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Scott AI targets coordination among engineers using coding agents. The 13.4 month window gives about two fifths seed odds from the B2B base rate, and a Series A is unlikely in that time. Spec-driven development was a hot but fast copied category, so the strongest risk is that the agents absorb the feature. The odds do not rank this company against others. The company has three people and a thesis that planning becomes the bottleneck once code is cheap. That thesis is credible and also widely shared, with Spec Kit, Tessl and plan modes appearing in the same months. The cohort anchors do not separate winners from losers in the earlier winners test, so treat the number as a base rate.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Scott AI is already in Fall 2025, so shown for completeness. Starting rate about 1 percent. The idea fits a YC area (AI developer tools) and the team is small and technical, but the space is crowded, so about 3 percent.

**Why it fails here.** YC would most plausibly say no because planning tools for coding agents are an obvious wedge for many teams and no usage or revenue is stated. Fable, a planning tool for product teams, was copied by incumbents and shut in 2022, which is the pattern a reviewer would worry about.

### Seed: P(reach this round | in YC) = 41% after the previous step; 41% cumulative if in YC; 1.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$20M | 28% | 11% | Unlikely | 0.3% | Very unlikely | Small post YC round between $1M and $3M, above the YC deal of about $500K. Developer tools seeds for agent workflows were common in 2025. Our 2022+ seed table has p25 $2.8M (round_benchmarks.csv), and the winners test put about 11 percent of confirmed 2026 raises under $3M. |
| $3M–$6M | $15M–$35M | 38% | 16% | Unlikely | 0.5% | Very unlikely | Institutional seed of $3M to $6M. The 2022+ B2B median raise is $3.3M (p75 $5.6M, n=39 in base_rates.py), and market seed deal size is about $3M. Developer tools seeds for agent workflows were common in 2025. |
| $6M–$12M | $30M–$70M | 24% | 9.8% | Unlikely | 0.3% | Very unlikely | Larger institutional seed. Confirmed 2026 raises above $1M had median $6.0M, quartiles $4.3M and $10M (winners test, press leaning). |
| $12M–$25M | $60M–$150M | 10% | 4.1% | Very unlikely | 0.1% | Very unlikely | Hot AI round led by a top fund; rare, but 2025 and 2026 press shows AI-native seeds above $10M exist. |

**Why it fails here.** The category is moving faster than a three person team can lock in: GitHub Spec Kit, Tessl and coding agents' own plan modes already offer planning for free or bundled, and Fable (command center for product teams) shut down in 2022 after incumbents copied it. If no team pays and adoption stays at individual developers, investors treat it as a feature of the agents and pass.

### Series A: P(reach this round | in YC) = 4.0% after the previous step; 1.6% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$8M | $25M–$45M | 15% | 0.2% | Very unlikely | <0.1% | Very unlikely | Thin or flat Series A of $5M to $8M for a company with revenue but no clear breakout; this is the 'reached A, barely' case. Below the 2022+ A median of $14.9M (B2B 2022-24, n=18). |
| $8M–$15M | $45M–$90M | 40% | 0.7% | Very unlikely | <0.1% | Very unlikely | Core band around the 2022+ B2B median raise of about $15M (p25 $11M, p50 $15M); post money from public seed-to-A step ups, valuations are sparse in our data. |
| $15M–$25M | $90M–$180M | 30% | 0.5% | Very unlikely | <0.1% | Very unlikely | Strong band: AI-native companies with fast revenue growth drew A rounds near the p75 of $23M (B2B 2022-24). |
| $25M–$50M | $180M–$400M | 15% | 0.2% | Very unlikely | <0.1% | Very unlikely | Upside band for a breakout; rare in our cohorts and press-driven. |

**Why it fails here.** A Series A by late 2026 needs fast team adoption and real revenue from paying engineering orgs. Planning tools struggle to show retention because the workflow can move into the coding agent itself, and Vibe Kanban style tools and Nuanced show how thin the layer is.

### Series B: P(reach this round | in YC) = 18% after the previous step; 0.3% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$25M | $80M–$150M | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Thin or bridge-like Series B near $15M to $25M, a flat or slightly down step from the A valuation; this happens when growth slows after the A and investors reprice, as in many 2022 to 2024 B2B rounds. |
| $25M–$45M | $150M–$300M | 45% | 0.1% | Very unlikely | <0.1% | Very unlikely | Core: B2B 2022+ Series B raise $35M to $60M (n=3), market median about $40M. |
| $45M–$80M | $300M–$700M | 25% | <0.1% | Very unlikely | <0.1% | Very unlikely | Strong growth round of $45M to $80M for a company growing well over 2x a year; the 2022+ Series B table has p75 $55M (round_benchmarks.csv, n=192 all companies). |
| $80M–$150M | $700M–$1.5B | 10% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside breakout case of $80M to $150M led by a growth fund; rare and mostly seen for AI leaders with very fast revenue, so it carries only a tenth of the mass. |

**Why it fails here.** Series B needs enterprise seats and net revenue retention in the face of GitHub, Atlassian and Linear shipping planning features inside their suites. Reaching Series B would require enterprise engineering organisations to pay per seat for a planning layer that sits next to Jira, Linear and the coding agents themselves. The analog Fable lost its position when larger tools added the same collaborative surface, and net revenue retention is hard to prove for a tool teams can switch off.

### Series C+: P(reach this round | in YC) = 28% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$50M | $250M–$500M | 25% | <0.1% | Very unlikely | <0.1% | Very unlikely | Thin Series C of $30M to $50M at a flat valuation, typical when growth normalises after a B and the company raises mainly to extend runway or fund acquisitions. |
| $50M–$100M | $500M–$1B | 45% | <0.1% | Very unlikely | <0.1% | Very unlikely | Core C (2022+ median about $45M to $74M). |
| $100M–$200M | $1B–$2B | 25% | <0.1% | Very unlikely | <0.1% | Very unlikely | Strong Series C of $100M to $200M, around the 2022+ p75 of $103M for all companies (round_benchmarks.csv), for a clear category leader with durable revenue. |
| $200M–$500M | $2B–$5B | 5.0% | <0.1% | Very unlikely | <0.1% | Very unlikely | Breakout round above $200M for a market leader; the 2022+ Series C p75 is about $103M, so this is a tail band with 5 percent of the mass. |

**Why it fails here.** Series C requires becoming a system of record for software planning. Incumbents (Atlassian, GitHub, Linear) own that spot, so most dev tool wedges stop at B or are acquired. A Series C planning platform would need to be the shared source of truth for agent driven software work. Atlassian, GitHub and the model vendors have much larger installed bases, so the likely outcome is acquisition by one of them before a Series C.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 66% | Very likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 19% | Unlikely | 0.6% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 11% | Unlikely | 0.3% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 4.0% | Very unlikely | 0.1% | Very unlikely |

**Why it fails here.** Most agent-era dev tools are absorbed by the coding agent vendors or by workflow suites, and shut or sell for under $100M. A breakout needs the planning layer to become the standard shared context for agent teams. Dev tool wedges in the agent era are consolidating quickly, and a three person team with no stated revenue is more likely to be acquihired or to fade than to build a large company. A large outcome needs planning to become a distinct paid layer instead of a built in mode of coding agents.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Planning becomes a built-in feature of coding agents | 50% | Plan modes in Claude Code and Cursor, and GitHub Spec Kit, already cover planning; GitHub open-sourced Spec Kit in September 2025. | Fable (fable), Nuanced (nuanced) | Focus on multi person alignment, which a single agent session does not solve. |
| 2 | Individuals adopt, teams do not pay | 40% | Dev tools often get bottom-up free use; seat conversion needs a shared artifact tied to review and approvals. | Fable (fable), sudocode (sudocode) | Sell to engineering managers with approvals and audit trails. |
| 3 | Three person team cannot out ship funded spec-driven players | 35% | Tessl is reported as funded around $125M and Codeplain raised $3M. | Codevisor (codevisor), Nuanced (nuanced) | Stay narrow on team alignment and integrate with every agent. |

## Pros

- **Real coordination pain when agents speed up code**: The pitch matches the emergence of spec-driven development as a category in 2025. (https://thenewstack.io/spec-driven-development-the-key-to-scalable-ai-agents/)
- **Hot investor interest in AI developer tools**: Spec-driven startups such as Tessl and Codeplain raised funding. (https://www.tamradar.com/funding-rounds/codeplain-seed-3m)

## Roadmap

### Get into YC

Prove teams, not individuals, use the plan layer.

1. Onboard 10 engineering teams of 5 or more
2. Measure plans approved before agent runs

You know it worked when: 10 teams using it weekly for a month.

### Reach Seed

Show willingness to pay.

1. Charge per seat
2. Show retention across 3 months

You know it worked when: $10K MRR with 80 percent team retention.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 2 | A collaborative planning workspace with agent hand-off is within reach of a small team in three months; the hard part is integrating with many agents and keeping plans in sync with code, which depends on third party APIs. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 2 | Scott AI: A first name plus AI is a pattern many 2023 to 2025 companies used, so it is hard to own in search; past YC names with human first names worked only when the product was strongly tied to the persona. |
| Takeover/copy risk (5 = very likely) | 5 | Could be built or absorbed by GitHub, Anthropic, Cursor, Atlassian, Linear within ~6 months. Coding agent vendors and issue trackers can ship planning features in months and already own the developer workflow; platform dependence is high. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| GitHub Spec Kit | Open source spec-driven development toolkit released September 2025. | Widely referenced in coverage of spec-driven development. | https://thenewstack.io/spec-driven-development-the-key-to-scalable-ai-agents/ |
| Tessl | Spec-as-source platform and spec registry. | Reported to have raised about $125M. | https://tessl.io/blog/why-codeplain-is-betting-on-spec-driven-software-development |
| Linear and Notion | Existing planning and docs tools where teams already write specs. | Large installed bases. | https://linear.app |

### Demand evidence

- Spec-driven development became a named practice in 2025 with several frameworks. (https://thenewstack.io/spec-driven-development-the-key-to-scalable-ai-agents/)
- Spec-first startups raised funding (Codeplain seed, Tessl). (https://www.tamradar.com/funding-rounds/codeplain-seed-3m)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Fable (fable) | Winter 2021 | Inactive | Command center for product teams (2021). | Shut down in 2022; incumbents copied it and willingness to pay was weak. |
| Nuanced (nuanced) | Winter 2024 | Active | AI coding app for thinking, 2024 batch. | Active; early dev tool in the same area. |
| Codevisor (codevisor) | Winter 2025 | Active | Native app for agentic engineering, 2025. | Active; shows crowded agent workspace field. |
| sudocode (sudocode) | Summer 2023 | Active | Orchestration of coding agents (2023). | Active; thin layer on top of agents. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 41% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only : seed 50% lower / 61% known-only / 68% upper, cond 61% (n=88). Time to seed (B2B 2022-24) p25 4, median 9, p75 19 months (n=54); time_to_milestones.csv calibration_sample p25 3, median 7, p75 19.5 (n=363). | Window forecast, 13.4 months. Anchor 0.61 to 0.68 ever; about 62 to 65 percent of eventual seed raisers close within 13 months (median 7 to 9, p75 19 to 20), so 0.65 times 0.63 is about 0.41. Developer tools aimed at AI coding were a hot area in late 2025, but I did not lift above the anchor, per the winners test. The odds do not rank Scott AI against other companies. |
| Series A | 33% | 4.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only : series_a cond 33% (n=54), lower 17%, known-only 20%, upper 35%. Time: months_to_series_a p25 22, median 30 (n=18); calibration_sample p25 19.3, median 28. | Window forecast, 13.4 months. Series A median 28 to 30 months after batch start, p25 about 19 to 22; so about 10 percent of Series A companies appear by 13 months. 0.33 times about 0.12 is 0.04. The gap to the anchor is due to the window. |
| Series B | 17% | 18% | base_rates.py --industry B2B --years 2022-2024 --calibration-only : series_b cond 17% (n=18); overall calibration conditional 44% (n=126). This step is an ever-reached figure beyond the forecast window. | Ever-reached beyond the window; anchor 0.17 (B2B 2022-24 n=18), a small discount for platform risk. |
| Series C+ | 36% | 28% | base_rates.py calibration sample: series_c cond 36% (n=55); B2B 2022-24 has n=3 so the broad figure is used. Ever-reached figure beyond the window. | Ever-reached beyond the window; just under the 36% calibration conditional due to the platform ceiling. |

## Assumptions and limits

- Only the input file used.
- Window 13.4 months from 2025-10-06 to 2026-11-17.
- Pages dated after 2025-10-06 ignored.
- B and C steps are ever-reached odds.

## Sources

- https://thenewstack.io/spec-driven-development-the-key-to-scalable-ai-agents/
- https://www.tamradar.com/funding-rounds/codeplain-seed-3m
- https://tessl.io/blog/why-codeplain-is-betting-on-spec-driven-software-development
- https://linear.app
