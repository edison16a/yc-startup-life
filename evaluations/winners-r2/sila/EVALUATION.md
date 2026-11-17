# Evaluation: Sila

*As of 2026-01-05. Mode: summary. Agentic Messenger*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A crowded messenger with a thin pitch; 33 percent for a seed above $1M in 10 months.**

**Chance of getting into YC:** 97% (range 90%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$2.9M | $8M–$20M | 7.3% | Unlikely | 7.0% | Unlikely |
| Seed | $3M–$6M | $15M–$35M | 12% | Unlikely | 12% | Unlikely |
| Seed | $6M–$12M | $30M–$70M | 9.9% | Unlikely | 9.6% | Unlikely |
| Seed | $12M–$25M | $60M–$150M | 4.0% | Very unlikely | 3.8% | Very unlikely |
| Series A | $4M–$8M | $20M–$45M | 0.2% | Very unlikely | 0.2% | Very unlikely |
| Series A | $8M–$18M | $40M–$100M | 0.5% | Very unlikely | 0.5% | Very unlikely |
| Series A | $18M–$40M | $100M–$250M | 0.3% | Very unlikely | 0.3% | Very unlikely |
| Series B | $15M–$30M | $80M–$180M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $180M–$450M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $450M–$1B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Sila is an AI agent messenger from two founders with no stated customers. Incumbents Slack and Teams are adding agents, and past YC messengers such as Openland, Patchwork and Shift Messenger stalled or stayed small. The hot AI sector helps seed odds but I do not lift above the anchor, and the 10 month window is short, so a seed above $1M is about a third. A Series A inside the window is very unlikely. The ladder does not rank this company above others. The main failure path is that teams never switch from Slack and investors see a feature, not a company.

## Round by round: where and why it fails

### Getting into YC: 97%

**How we got the number.** The input file places this company in the Winter 2026 batch, so acceptance is already known and this figure is reported for completeness only. The starting prior for a random applicant is about 1 percent (references/yc_acceptance.md, 0.6 to 2 percent third party range); the near certainty comes from the stated batch, not from a model of the company.

**Why it fails here.** YC is already past, so the only residual risk is a data error in the input about batch membership. Had the company been an ordinary applicant, the most plausible rejection reason would be: A new chat product competing with Slack and Microsoft Teams with a vague pitch and no stated traction or distribution advantage.

### Seed: P(reach this round | in YC) = 33% after the previous step; 33% cumulative if in YC; 32% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$2.9M | $8M–$20M | 22% | 7.3% | Unlikely | 7.0% | Unlikely | Small post YC round of $1M to $3M, usually angels or a small seed fund. A two person AI team with a viral demo can get a $1M to $3M angel round quickly. |
| $3M–$6M | $15M–$35M | 36% | 12% | Unlikely | 12% | Unlikely | Institutional seed of $3M to $6M, the modal outcome in 2022 and later data (median $3.5M to $4.1M in round_benchmarks.csv, which mixes in the YC deal). The central case is a $3M to $6M seed from an AI focused fund. |
| $6M–$12M | $30M–$70M | 30% | 9.9% | Unlikely | 9.6% | Unlikely | Larger seed of $6M to $12M, where 42 percent of confirmed 2026 raises above $1M fell in the winners test. AI native team products have drawn large rounds in 2025, so a $6M to $12M seed is possible with strong usage. |
| $12M–$25M | $60M–$150M | 12% | 4.0% | Very unlikely | 3.8% | Very unlikely | Upside band above $12M, reserved for a standout demo with a named lead. Only with rapid organic growth inside startups. |

**Why it fails here.** Window of 10 months. The most likely miss is that investors see a Slack feature race they cannot judge: Slack and Teams are adding agents themselves, and no traction is stated. Openland raised a $2.25M seed for a messenger and later closed, Patchwork (W24 Slack replacement) stayed at the $500K YC cheque and went inactive, and Shift Messenger raised $1.5M and faded. A 10 month window is short.

### Series A: P(reach this round | in YC) = 3.0% after the previous step; 1.0% cumulative if in YC; 1.0% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $20M–$45M | 20% | 0.2% | Very unlikely | 0.2% | Very unlikely | Thin or bridge style Series A below the 2022 and later median of $14M to $15M, the down or flat band. |
| $8M–$18M | $40M–$100M | 50% | 0.5% | Very unlikely | 0.5% | Very unlikely | Typical Series A near the 2022 and later quartiles ($11M to $21M raise). |
| $18M–$40M | $100M–$250M | 30% | 0.3% | Very unlikely | 0.3% | Very unlikely | Upside Series A led by a top tier fund once revenue is visible; current US medians are about $17M raise on $60M pre money. |

**Why it fails here.** A Series A within 10 months needs paid seats at real companies and retention against Slack, but median time to Series A is about 28 months. Openland and Patchwork show messengers stall at adoption, and nothing in the input shows adoption yet. Investors would also need evidence that agent features, not only chat, drive seat expansion beyond a few friendly startups.

### Series B: P(reach this round | in YC) = 1.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$180M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Flat or small Series B, near the 2018 to 2021 median of $32M but with a lower valuation. |
| $30M–$60M | $180M–$450M | 50% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series B, in line with the 2022 and later median of about $40M. |
| $60M–$120M | $450M–$1B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside Series B for a category leader; 2022 and later posts reach $600M to $1B. |

**Why it fails here.** A Series B inside 10 months would need enterprise revenue and a Series A first, and the median B2B path takes about three years from batch start (B2B median months to series B 47). Rescale, a simulation platform, took years of enterprise selling before its Series B. The likely failure is timing rather than a verdict on the idea.

### Series C+: P(reach this round | in YC) = 3.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series C at the 2022 and later median of $74M. |
| $80M–$150M | $700M–$2B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Growth round for a scaled leader, near the 2022 and later p75 of $103M. |
| $150M–$400M | $2B–$6B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside round for a breakout company; only a few percent of YC companies get here. |

**Why it fails here.** Series C inside 10 months is almost outside the data: the median is about five years after batch start, and only 8 companies in the 2022 and later cohort have reached it. Failing here means the company has not scaled past a niche or the window closed first, not that the idea is bad.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 65% | Very likely | 66% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 18% | Unlikely | 17% | Unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 12% | Unlikely | 12% | Unlikely |
| Acquired or IPO over $1B | $1B–$10B | 5.0% | Unlikely | 4.9% | Very unlikely |

**Why it fails here.** Most messenger startups fail to displace the incumbent, and Slack and Teams are building agent features directly. Openland, Shift Messenger and Patchwork all stalled or went inactive; Mattermost shows a different path of success only through an open source, security focused niche, so a large exit needs a sharp wedge.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Slack and Microsoft Teams ship agents natively, so teams do not change messenger. | 45% | Salesforce repositioned Slack as an agentic operating system and Microsoft integrates agents into Teams. | Openland (openland), Patchwork (patchwork) | Pick a niche such as engineering or agent first teams where switching is cheap. |
| 2 | Network effects: a messenger is useless until a whole team adopts it. | 35% | Messenger startups such as Openland reached only a few hundred communities. | Openland (openland), Shift Messenger (shift-messenger) | Start with small startups and agent workflows that deliver value to one user. |
| 3 | Vague positioning and no stated traction make seed investors pass. | 30% | The description gives a mission but no customers, revenue or usage. | Patchwork (patchwork), Kitemaker (kitemaker) | Show weekly active teams and agent actions per user. |

## Pros

- **Timing: incumbents are validating that agents inside chat is a real category.**: Slack and Teams both launched agent features, per press. (https://www.uctoday.com/collaboration/slack-agentic-os-dreamforce-2025/)
- **Small team can ship fast and hot AI sector for seed investors.**: Two person team stated in the input; Slack agent push confirms demand. (https://www.axios.com/2025/02/25/ai-agents-slack-chat-worplace)

## Roadmap

### Get into YC

A product with a few teams using it daily.

1. Ship to 10 startup teams and watch retention.
2. Show tasks done by agents in chat.

You know it worked when: Ten teams active weekly for a month.

### Reach Seed

Organic growth that justifies a $3M to $6M seed.

1. Convert teams to paid seats.
2. Publish usage per team.

You know it worked when: 100 active teams and paid conversions.

### Reach Series A

Paid seats and retention against Slack.

1. Add admin and security controls.
2. Integrate agent marketplaces.

You know it worked when: About $1M ARR with low churn.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A messenger with agent hooks is buildable by two people in months, but reliability, permissions and enterprise security are the hard parts, and the product must also run agents safely. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Sila: A short invented name like Slack itself is easy to type and remember, but it says nothing about agents and a messenger lives or dies on adoption rather than name. |
| Takeover/copy risk (5 = very likely) | 5 | Could be built or absorbed by Salesforce (Slack), Microsoft (Teams), Google (Chat), OpenAI and Anthropic products within ~6 months. The incumbents already have distribution and are shipping agent features, so a rival can match the core idea in under 6 months. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Slack with Agentforce | Incumbent chat platform repositioned as an agentic operating system. | Part of Salesforce, a $27.7B acquisition per press coverage. | https://www.uctoday.com/collaboration/slack-agentic-os-dreamforce-2025/ |
| Microsoft Teams with Copilot agents | Chat bundled into Microsoft 365 with agents. | Reported significant traction in a roughly $45B collaboration market. | https://www.axios.com/2025/02/25/ai-agents-slack-chat-worplace |
| Status quo: Slack plus separate AI tools | Teams use existing chat and bolt on agents. | Default behaviour. | https://www.axios.com/2025/02/25/ai-agents-slack-chat-worplace |

### Demand evidence

- Salesforce and Microsoft are racing to make chat the surface for AI agents, so the category has real spend. (https://www.uctoday.com/collaboration/slack-agentic-os-dreamforce-2025/)
- Press describes workplace chat shifting to more AI agents and fewer humans. (https://www.axios.com/2025/02/25/ai-agents-slack-chat-worplace)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Openland (openland) | Winter 2018 | Inactive | Team and community messenger from Winter 2018. | Raised a 2.25M seed, pivoted, reached few communities and the founder closed it. |
| Patchwork (patchwork) | Winter 2024 | Inactive | AI powered Slack replacement from two big tech veterans, Winter 2024. | Reportedly only the 500K YC cheque and later listed inactive, so no seed above 1M found. |
| Shift Messenger (shift-messenger) | Winter 2015 | Inactive | Real time messenger for frontline teams. | Raised 1.5M seed in 2015 and later went inactive. |
| Mattermost (mattermost) | Summer 2012 | Active | Open source Slack alternative for technical teams. | Raised a $20M Series A and $50M Series B in 2019 by focusing on secure, self hosted collaboration. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 33% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: seed known-only 61% (lower 50%, upper 68%), cond 61% (n=88). Median months to seed 9 (p25 4, p75 19); time_to_milestones.csv era 2022+ p75 is 14 months.  | Window is 10 months from the as_of date to 2026-11-17. The ever anchor of 61% counts the YC deal as a seed, but this forecast counts only a financing above about $1M from outside investors that closes inside the window, so the anchor is cut to cover only rounds above $1M and only the share that close within 10 months (about 75 to 80 percent of eventual seed raisers close by month 14 to 20). AI native messaging is a hot sector, but I add no credit for it. I cut for a two person team with no stated product or customers, and for the short window: only about half of eventual seed raisers have closed by month 10 (p25 months to seed 4, median 9). Odds are not lifted for team or hot sector, per the winners test, and do not rank this company against others. |
| Series A | 33% | 3.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_a cond 33% (n=54), known-only 20%; months to series A median 30 (p25 22, p75 39). | The ever anchor is 33 percent, but only about a tenth of eventual Series A raisers have closed it by month 10 (p25 is 19 to 22 months from batch start), so the windowed value is much lower. Reaching a Series A in later years is common for companies with paying customers, but it falls outside this window. |
| Series B | 17% | 1.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2024: series_b cond 17% (n=18); median months to series B 46 overall, 35.5 for 2022 and later (n=40). | Median time to a Series B is about three years from batch start, so inside a 10 month window almost only extreme outliers get there; windowed probability is far below the 17 percent ever anchor. |
| Series C+ | 30% | 3.0% | python3 -I scripts/base_rates.py --calibration-only: series_c cond 36% (n=55) overall; B2B 2022-2024 cohort has 0 of 3 at Series C. Median months to series C about 61. | Series C normally lands about five years after the batch, so a window of 10 months makes it very unlikely; the ever anchor is cut to a token value. |

## Assumptions and limits

- Only the description and a team of two are known; no traction is assumed.
- Blind forecast made as of 2026-01-05 for the window to 2026-11-17 (10 months). Seed means an outside round above about $1M closing in the window, not the standard YC deal of about $500K.
- Coverage limit: 662 of 6,399 companies are researched, and the B2B 2022-2024 cohort has 107 companies, so cohort rates are wide.
- Probabilities do not rank this company against others; the winners test found no separation between raisers and non-raisers.

## Sources

- https://www.uctoday.com/collaboration/slack-agentic-os-dreamforce-2025/
- https://www.axios.com/2025/02/25/ai-agents-slack-chat-worplace
