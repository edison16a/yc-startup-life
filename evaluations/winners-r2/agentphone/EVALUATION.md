# Evaluation: AgentPhone

*As of 2026-04-06. Mode: summary. Phone Numbers for AI Agents*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A clear, timely agent infrastructure wedge, but a thin reseller layer over carriers with strong incumbents.**

**Chance of getting into YC:** 2.0% (range 1.0%–5.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$18M | 16% | Unlikely | 0.3% | Very unlikely |
| Seed | $3M–$6M | $15M–$30M | 16% | Unlikely | 0.3% | Very unlikely |
| Seed | $6M–$12M | $28M–$60M | 9.9% | Unlikely | 0.2% | Very unlikely |
| Seed | $12M–$25M | $55M–$120M | 3.6% | Very unlikely | <0.1% | Very unlikely |
| Series A | $6M–$10M | $30M–$60M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$20M | $50M–$120M | 1.4% | Very unlikely | <0.1% | Very unlikely |
| Series A | $20M–$40M | $120M–$300M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series B | $20M–$35M | $120M–$250M | 0.2% | Very unlikely | <0.1% | Very unlikely |
| Series B | $35M–$60M | $250M–$700M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $700M–$1.5B | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$900M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $900M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

AgentPhone sells phone numbers to AI agents. Demand from agent builders is plausible and voice-AI neighbors Vapi and Bland AI raised sizeable rounds in the previous wave, but the layer sits on top of carriers and CPaaS vendors that can add the same feature, and Struct and Surge show that voice infrastructure can stall. Over a 7.4 month window the cohort anchor for a seed above $1M is about 0.44 ever and most of it falls in the first 6 months; I use 0.45. The odds do not rank this company against others.

## Round by round: where and why it fails

### Getting into YC: 2.0%

**How we got the number.** Start from about 1 percent. Adjust up for a clear developer-facing wedge in agent infrastructure and fast-growing demand for voice and messaging agents; adjust down because it is a thin layer on top of carriers such as Twilio and Telnyx, there is no stated team background or traction, and voice infrastructure is crowded (Vapi, Bland, Retell, Surge). Net about 2 percent; already in the Spring 2026 batch.

**Why it fails here.** YC would most plausibly say this is a wrapper over existing telephony APIs: Twilio, Telnyx and the voice-agent platforms already provide numbers, and the one-liner does not say what is hard that they cannot add in a quarter. The team size and background are not stated, and carrier registration and spam rules could swallow a small team.

### Seed: P(reach this round | in YC) = 45% after the previous step; 45% cumulative if in YC; 0.9% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$18M | 35% | 16% | Unlikely | 0.3% | Very unlikely | Small post YC round under $3M from angels and a seed fund, the thin band. Cohort B2B 2022+ seed raise p25 is $2.0M, so about a third of rounds land here; the YC deal alone (about $500K) does not count as seed in this window. |
| $3M–$6M | $15M–$30M | 35% | 16% | Unlikely | 0.3% | Very unlikely | Typical institutional seed. Cohort median is $3.3M to $4.0M (B2B 2022+, n=530) and the winners test confirmed raises had quartiles of $4.3M and $10M, so this band holds the middle. |
| $6M–$12M | $28M–$60M | 22% | 9.9% | Unlikely | 0.2% | Very unlikely | Hot-category seed led by a known fund. In the winners test 42 percent of confirmed raises fell in $6M to $12M, though press coverage biases that sample upward, so it is weighted below that. |
| $12M–$25M | $55M–$120M | 8.0% | 3.6% | Very unlikely | <0.1% | Very unlikely | Upside band: a large AI-category seed or pivot-then-raise path with top-tier lead. Rare in the cohort (above the p75 of $5.0M to $6.0M by 2x). |

**Why it fails here.** Seed fails if usage does not show quickly: investors need agent developers actually paying for numbers, and carriers and CPaaS firms can undercut price. Surge (F24, Stripe for telephony) and Struct (W23, shut down) show voice infrastructure can stall without a round, and unit margins on resold minutes are thin, so a small founding team may not reach the traction investors want in 7 months.

### Series A: P(reach this round | in YC) = 6.0% after the previous step; 2.7% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $30M–$60M | 25% | 0.7% | Very unlikely | <0.1% | Very unlikely | Thin or flat-ish Series A on modest ARR; the 2018-2021 B2B series_a p25 was $10M, so this is below the typical cohort round and covers extension-like A rounds. |
| $10M–$20M | $50M–$120M | 50% | 1.4% | Very unlikely | <0.1% | Very unlikely | Central case. B2B 2022+ series_a raise p25 $13M, median $17M, p75 $22M (n=130); post-money reported for only n=3 so valuation is thin data. |
| $20M–$40M | $120M–$300M | 25% | 0.7% | Very unlikely | <0.1% | Very unlikely | Upside band with fast ARR growth in a hot AI category; 2022+ all-industry series_a post-money p75 was $345M on n=18 reported rounds. |

**Why it fails here.** Series A needs usage-based revenue of about $1M to $2M ARR with healthy gross margins. A reseller of carrier capacity has thin margins and customers can switch to Twilio or Telnyx, so growth must come from agent-specific features like identity, compliance and memory, which need time to prove.

### Series B: P(reach this round | in YC) = 20% after the previous step; 0.5% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$35M | $120M–$250M | 30% | 0.2% | Very unlikely | <0.1% | Very unlikely | Thin Series B below the cohort p25 of $39M, flat or modest step up. |
| $35M–$60M | $250M–$700M | 50% | 0.3% | Very unlikely | <0.1% | Very unlikely | Central: B2B 2022+ series_b median $42.5M raise and $600M post (n=9 valuations). |
| $60M–$120M | $700M–$1.5B | 20% | 0.1% | Very unlikely | <0.1% | Very unlikely | Upside band for a category leader; era is inflated by AI rounds so use with care. |

**Why it fails here.** A Series B requires the company to become the default identity and messaging layer for agents, with large enterprise accounts. Twilio, Telnyx and agent platforms can bundle numbers, and carriers control pricing, so growth may stall at a niche developer audience, as Surge (F24) and Vogent (S21) show for telephony infrastructure that never became the default.

### Series C+: P(reach this round | in YC) = 15% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$900M | 35% | <0.1% | Very unlikely | <0.1% | Very unlikely | Modest growth round; series_c 2022+ p25 raise $50M. |
| $80M–$150M | $900M–$2B | 45% | <0.1% | Very unlikely | <0.1% | Very unlikely | Central: 2022+ series_c median raise $74M to $101M, post-money median about $1.2B (n=3 to 34). |
| $150M–$400M | $2B–$6B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside: breakout category winner, cf. Bland-style rounds; very few companies. |

**Why it fails here.** Series C needs hundreds of millions in volume. Voice infrastructure has capital-heavy competitors and carrier relationships that are hard to replicate, and acquirers such as Twilio or the model labs may buy the category instead of letting an independent scale; Vocode and Vogent ended as acquisitions rather than as independent growth stories.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 52% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 30% | Reasonable | 0.6% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 15% | Unlikely | 0.3% | Very unlikely |
| Acquired or IPO over $1B | $1B–$20B | 3.0% | Very unlikely | <0.1% | Very unlikely |

**Why it fails here.** The likeliest outcome is a small acquisition by a CPaaS or voice platform, as happened to Vocode and Vogent, or a stall as agent builders consolidate on the voice platforms. A $1B outcome requires agent identity to become a standard layer, and carriers or labs may build it.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Carrier and CPaaS incumbents (Twilio, Telnyx) add agent features and undercut price. | 40% | Telnyx and Twilio already expose numbers, SMS and voice APIs that agents can call. | Vapi (vapi), Surge (surge) | Offer agent-native identity, compliance and memory, not raw numbers. |
| 2 | Regulation and spam: carrier registration, 10DLC rules and anti-robocall enforcement can block agent-initiated calls. | 30% | Production SMS and outbound calls need registration and consent, and agents risk number blacklisting. | Bland AI (bland-ai), Struct (struct) | Build compliance into the product and screen customers. |
| 3 | Thin gross margins from reselling carrier minutes. | 30% | Resold voice minutes and SMS carry carrier costs that leave small margins at low volume. | Vocode (vocode), Vogent (vogent) | Add software value and sell platform fees on top of usage. |
| 4 | Voice-agent platforms bundle numbers so customers never buy separately. | 30% | Vapi, Bland and Retell AI already attach numbers to their agent products. | Vapi (vapi), Retell AI (retell-ai), Bland AI (bland-ai) | Be the neutral layer that works across all agent platforms. |

## Pros

- **Clear, simple developer wedge and timely agent theme.**: One-liner states a single product, numbers for agents. (https://agentphone.ai/)
- **Voice-AI neighbors raised large rounds in the previous wave.**: Vapi and Bland AI reached series B and C in the researched records. (https://blog.vapi.ai/vapi-secures-20m-to-start-the-voice-revolution-2)

## Roadmap

### Get into YC

Show developers pay for agent numbers.

1. Get 20 agent builders onto paid numbers
2. Show message and call volume growth

You know it worked when: Weekly active numbers and paid minutes

### Reach Seed

Real usage revenue within 7 months.

1. Add compliance and registration so customers can go to production
2. Land two agent platforms as channel partners
3. Pitch agent-infra seed funds with the volume curve

You know it worked when: $20K to $50K MRR and a seed term sheet above $1M

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Provisioning numbers and routing calls and messages through carrier partners is not hard in 3 months; the hard parts are carrier registration, compliance, call quality and reliability, and fraud prevention, which a small team can reach with partners but cannot own. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | AgentPhone: A descriptive compound is clear like Surge-style category names but is easy to copy and weak as a brand; several competitors use nearby names, so it neither helps nor hurts the odds much. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Twilio, Telnyx, Vapi, Bland, Retell, model labs within ~6 months. A CPaaS can ship an agent-numbers product in a few months and already has the carrier relationships and customers; platform dependency on carriers also limits pricing power. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Telnyx | Carrier-grade voice, SMS and numbers API with AI features | Established carrier API used by AI companies | https://telnyx.com/customer-stories/photon |
| Firsty | Numbers in 18 countries with voice and SMS through one API for agents | Early | https://www.firsty.app/use-cases/telephone-for-ai-agents |
| Tryvox | SIP trunks, virtual numbers and SMS for agents | Early stage fund-backed | https://f4.fund/startups/tryvox |
| Status quo: Twilio account plus glue code | Developers buy numbers from a CPaaS and wire them themselves | Dominant | https://jentic.com/apis/telnyx.com/telnyx-api |

### Demand evidence

- Several startups already offer phone numbers and SMS for AI agents, which shows developer demand. (https://www.firsty.app/use-cases/telephone-for-ai-agents)
- Carrier APIs are marketing agent use cases, a sign of spend. (https://telnyx.com/customer-stories/photon)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Vapi (vapi) | Winter 2021 | Active | Voice AI for developers, W21; developer API in the same wave. | Alive, reached series_b; shows demand for agent voice infrastructure. |
| Bland AI (bland-ai) | Summer 2023 | Active | Enterprise AI phone calls, S23. | Alive, reached series_c; the strongest outcome in the lane. |
| Vocode (vocode) | Winter 2023 | Acquired | Open source voice AI, W23. | Acquired after a seed; shows a small exit. |
| Surge (surge) | Fall 2024 | Active | Stripe for telephony, F24; nearest infrastructure wedge. | Alive, no recorded round; telephony infra can stall. |
| Struct (struct) | Winter 2023 | Inactive | Multi-lingual voice agents, W23. | Shut down with no post-YC round. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 44% | 45% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2026 gave seed 36% lower / 44% known / 54% upper, cond 44% (n=1541); series_a cond 20% (n=679); series_b cond 19% (n=136); series_c cond 19% (n=26). Calibration-only B2B: seed 52/65/72, series_a cond 32%, series_b cond 46%. | Window is 7.4 months (2026-04-06 to 2026-11-17); seed means an outside round above about $1M closing in it. Anchor 0.44 ever for B2B 2022+ with median 6 months to seed and p25 3, so about 70 to 80 percent of ever-seeds close in 7 months; I lift to 0.45, within the 1.25x cap, for the strength of the agent-infrastructure theme and the voice-AI analogs Vapi, Bland AI and Retell AI that raised early, offset by an unknown team. The odds do not rank the company against others. |
| Series A | 20% | 6.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2026: series_a cond 20% (n=679); time table months_to_series_a p50 28, p25 19 (era 2022+). | Window is 7.4 months, and Series A p25 is 19 months after batch start in the 2022+ time table, so only a small share of the 0.20 ever anchor falls in the window. Used 0.06, the discount being for time and not for company quality. Vapi and Bland did reach later rounds quickly, which keeps it above 0.04. |
| Series B | 19% | 20% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2026: series_b cond 19% (n=136); calibration-only B2B cond 46% (n=61); lower/known/upper ranges 1/2/19 percent ever. | Anchor cond 19 percent; 0.20 because voice AI analogs Vapi (series B) and Bland AI (later rounds) show faster progress than the typical B2B cohort in this wave. |
| Series C+ | 19% | 15% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2026: series_c cond 19% (n=26); calibration-only B2B cond 50% (n=28). | Anchor cond 19 percent; 0.15 because a telephony reseller faces margin pressure and few YC analogs reached a Series C (Bland is the exception). |

## Assumptions and limits

- Window is 7.4 months from 2026-04-06; seed means an outside round above about $1M.
- Team size is not stated in the input, so no team-based adjustment was made.
- LEAK-WEB: one market search returned pages naming agentphone, including a page on ycombinator.com; I did not read or use them and drew no facts from them, and the result is flagged so the run can be dropped from scoring.
- Competitors in the list come from non-AgentPhone search results (Telnyx, Firsty, Tryvox).

## Sources

- https://www.firsty.app/use-cases/telephone-for-ai-agents
- https://telnyx.com/customer-stories/photon
- https://f4.fund/startups/tryvox
- https://jentic.com/apis/telnyx.com/telnyx-api
- https://blog.vapi.ai/vapi-secures-20m-to-start-the-voice-revolution-2
