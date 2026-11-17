# Evaluation: Tasklet

*As of 2026-04-06. Mode: summary. Agents that own the work*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A capable general agent in the most crowded category in software; seed is very likely, later rounds depend on retention against labs.**

**Chance of getting into YC:** 4.0% (range 2.0%–7.2%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$1.5M | $8M–$15M | 8.0% | Unlikely | 0.3% | Very unlikely |
| Seed | $2M–$4M | $15M–$30M | 28% | Reasonable | 1.1% | Very unlikely |
| Seed | $4M–$8M | $30M–$60M | 28% | Reasonable | 1.1% | Very unlikely |
| Seed | $8M–$20M | $60M–$150M | 16% | Unlikely | 0.6% | Very unlikely |
| Series A | $4M–$8M | $20M–$40M | 6.8% | Unlikely | 0.3% | Very unlikely |
| Series A | $10M–$18M | $45M–$90M | 12% | Unlikely | 0.5% | Very unlikely |
| Series A | $18M–$35M | $90M–$220M | 8.2% | Unlikely | 0.3% | Very unlikely |
| Series B | $15M–$30M | $80M–$180M | 1.8% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$55M | $180M–$450M | 2.7% | Very unlikely | 0.1% | Very unlikely |
| Series B | $55M–$120M | $450M–$1B | 1.5% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $30M–$60M | $300M–$700M | 0.4% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $60M–$150M | $700M–$1.8B | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $1.8B–$5B | 0.3% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Tasklet is a chat based agent that connects to many tools and runs in the cloud. Demand is real, investors fund agents in 2026, and the eight person team suggests a shipped product, so a seed above the YC deal is very likely. The danger is that OpenAI, Anthropic, Microsoft and Zapier already ship similar agents with huge distribution. Analogs such as Sim and Pylon show a path with a clear wedge, while Workflow86 and Peakflo show stalls. The ladder sits above B2B anchors at seed and A, within 2x, with wide uncertainty later.

## Round by round: where and why it fails

### Getting into YC: 4.0%

**How we got the number.** Test note: this company was accepted to YC, so this is only the forward estimate. Starting prior is about 1 percent for a random applicant (0.6 to 2 percent third party range, per references/yc_acceptance.md). Eight person team with a detailed product description suggests an existing shipped product (up), a technical agent runtime (up), general AI agent market is very crowded and dominated by labs (down), unbundling SaaS is a favored YC theme (up). Net about 4 percent.

**Why it fails here.** YC would most likely say a general purpose agent that connects to everything competes head on with ChatGPT, Claude, Zapier and Lindy, so differentiation and retention are unclear. Without strong usage, paying customers or growth numbers, partners may see a product that model labs will ship as a feature.

### Seed: P(reach this round | in YC) = 80% after the previous step; 80% cumulative if in YC; 3.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$1.5M | $8M–$15M | 10% | 8.0% | Unlikely | 0.3% | Very unlikely | Small pre-seed of about 600K to 1.5M on a SAFE, barely above the YC deal. If usage is weak, a small round follows. |
| $2M–$4M | $15M–$30M | 35% | 28% | Reasonable | 1.1% | Very unlikely | Typical 2026 seed near the 3.0M US median deal size and 18M pre money from PitchBook NVCA via Equidam (see stage_benchmarks.md). Typical seed given the team size and shipped product. |
| $4M–$8M | $30M–$60M | 35% | 28% | Reasonable | 1.1% | Very unlikely | Strong seed led by a known fund, near the YC 2022+ announced median of 4.1M or above. Strong agent growth draws a top fund. |
| $8M–$20M | $60M–$150M | 20% | 16% | Unlikely | 0.6% | Very unlikely | Upside seed or large first round if usage or revenue spikes, common for hot AI categories in 2026. Hot agent category in 2026 can give a large seed. |

**Why it fails here.** The seed step above 500K fails if the product shows weak retention, or if investors decide ChatGPT, Claude and Zapier agents will absorb the category. With eight people the team has a burn that needs real funding, so this miss is less likely, but Workflow86 and Peakflo show agent workflow companies that stayed at small rounds.

### Series A: P(reach this round | in YC) = 34% after the previous step; 27% cumulative if in YC; 1.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $20M–$40M | 25% | 6.8% | Unlikely | 0.3% | Very unlikely | Small or bridge style A, or a down-ish A after a slow year. Churn after trials. |
| $10M–$18M | $45M–$90M | 45% | 12% | Unlikely | 0.5% | Very unlikely | Median 2022+ YC Series A raise is 14.15M, market 17.4M. Needs strong paid usage. |
| $18M–$35M | $90M–$220M | 30% | 8.2% | Unlikely | 0.3% | Very unlikely | Hot-category A led by a top fund, 62M pre money median market. Needs breakout growth. |

**Why it fails here.** Series A needs strong paid growth and retention. It fails if usage is trials and one off tasks, if token and sandbox costs squeeze margin, or if labs ship the same connected agent. Sim reached a 7M Series A from open source adoption, while Workflow86 has no public growth round, showing the split between winners and the rest.

### Series B: P(reach this round | in YC) = 22% after the previous step; 6.0% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$180M | 30% | 1.8% | Very unlikely | <0.1% | Very unlikely | Thin B or flat step. Pressure from labs. |
| $30M–$55M | $180M–$450M | 45% | 2.7% | Very unlikely | 0.1% | Very unlikely | Median 2022+ YC Series B is 37M, market 39.5M. Needs strong retention. |
| $55M–$120M | $450M–$1B | 25% | 1.5% | Very unlikely | <0.1% | Very unlikely | Breakout B at unicorn range if growth is exceptional. Needs category leadership. |

**Why it fails here.** Series B needs durable revenue and a defensible runtime. It fails if model vendors bundle agents into their apps and general agents become commodity. Pylon reached B only through a narrow B2B support wedge, which shows that horizontal agents struggle to hold a position, so a Series B would likely need a vertical focus.

### Series C+: P(reach this round | in YC) = 22% after the previous step; 1.3% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$60M | $300M–$700M | 30% | 0.4% | Very unlikely | <0.1% | Very unlikely | Modest C or growth round, or venture debt plus equity. Few reach this. |
| $60M–$150M | $700M–$1.8B | 45% | 0.6% | Very unlikely | <0.1% | Very unlikely | Typical C or later; 2022+ YC median C is 45M, D plus 97.5M. Needs a platform. |
| $150M–$400M | $1.8B–$5B | 25% | 0.3% | Very unlikely | <0.1% | Very unlikely | Breakout later round at multi billion value. Needs agent OS leadership. |

**Why it fails here.** Series C or later requires becoming the operating layer for work across companies. It fails against Microsoft, Google, OpenAI and Anthropic with distribution and models. Few horizontal tools reach this scale, and most that do are acquired earlier, so the odds of a Series C or later round are low even if the product works.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 42% | Reasonable | 98% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 34% | Reasonable | 1.4% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 16% | Unlikely | 0.6% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 8.0% | Unlikely | 0.3% | Very unlikely |

**Why it fails here.** Failure is most likely that general agents become a feature of ChatGPT, Claude and Microsoft products, so a startup with no vertical wedge loses retention and stalls or is acquired for its runtime. OpenInt and Nango show integration startups acquired or staying mid sized. Upside needs a pivot to a vertical product or breakout usage.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Labs and incumbents ship connected agents | 55% | OpenAI, Anthropic and Microsoft ship agents with connectors, and Zapier added agent features. | OpenInt (openint), Workflow86 (workflow86) | Win a vertical or a reliability niche and own the runtime. |
| 2 | Weak retention and cost of tokens | 40% | General agents see one off trials and high inference costs that squeeze margins. | Peakflo (peakflo), Sim (sim) | Focus on recurring triggered workflows with usage pricing. |
| 3 | Crowded agent builder category | 40% | Lindy, Relevance AI, n8n and others sell similar no-code agents to the same users. | Workflow86 (workflow86), Sim (sim) | Differentiate through the cloud runtime and integration breadth. |

## Pros

- **Eight person team with a described shipped product**: The description details a runtime, integrations and browser use, which suggests working software. (https://www.ycombinator.com/deal)
- **Demand for agents that run continuously is clear**: Zapier and Lindy show paid demand for automation. (https://zapier.com)

## Roadmap

### Reach Seed

Show paid usage with retention among recurring workflows.

1. Track weekly active agents
2. Launch usage pricing
3. Find 2 segments with high retention

You know it worked when: 1,000 paying users and 70 percent monthly retention

### Reach Series A

Show recurring revenue growing fast with healthy margins.

1. Cut inference cost
2. Build templates by role
3. Add team plans

You know it worked when: 1M to 2M ARR

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | A cloud agent runtime with integrations, code sandbox and browser control uses existing components and model APIs. An eight person team can ship this, and reliability and context engineering are the hard parts, with all value depending on rented models. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Tasklet: Tasklet suggests small tasks done by an agent, which fits. It is short and easy to spell, similar in style to names like Pylon or Nango. The name has little effect on outcomes. |
| Takeover/copy risk (5 = very likely) | 5 | Could be built or absorbed by OpenAI, Anthropic, Microsoft, Zapier within ~6 months. Labs and platforms already ship connected agents with distribution to millions, so a competing product exists or will within months. Only reliability and ease of use remain as edges. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Zapier | Automation with thousands of integrations and agents | Large user base | https://zapier.com |
| Lindy | No-code AI agent builder | Funded agent startup | https://www.lindy.ai |
| OpenAI and Anthropic | Chat assistants with connectors and agents | Hundreds of millions of users | https://openai.com |
| n8n | Workflow automation with AI | Large developer base | https://n8n.io |

### Demand evidence

- Knowledge workers pay for automation tools and agent products today. (https://zapier.com)
- No-code agent builders have raised funding and have paying users. (https://www.lindy.ai)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Sim (sim) | Spring 2025 | Active | Agent builder for enterprise systems, S25 | Open source launch, 7M Series A in November 2025. |
| Pylon (pylon-2) | Winter 2023 | Active | Agent support platform, W23 | Seed 3.2M, Series A 17M, Series B 31M after a pivot. |
| Nango (nango) | Winter 2023 | Active | Integrations for products, W23 | Bootstrapped, 7.5M seed in April 2026. |
| OpenInt (openint) | Winter 2023 | Acquired | Open source integrations, W23 | Four person team, acquired by Replit in 2025. |
| Workflow86 (workflow86) | Winter 2022 | Active | Agentic workflows for operations, W22 | Active small team, no growth round. |
| Peakflo (peakflo) | Winter 2022 | Active | Agentic back office workflows, W22 | 4.1M seed in 2022, no later round found. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 80% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed cond 59% (n=126, lower/known/upper 49/59/65), series_a cond 26% (n=74; 13/15/29), series_b cond 16% (n=19; 2/2/18), series_c cond 0% (n=3; upper 16%). Second cohort --industry B2B --years 2020-2022: seed 77%, A 30%, B 35%, C 33%. Calibration rule: stay at or above 0.75 times anchor unless a named analog shows a fatal problem. Coverage is partial, known-only rates are biased low. | 0.80/0.59 anchor is 1.36x: team size 8 and shipped product, hot category, within 2x. |
| Series A | 26% | 34% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed cond 59% (n=126, lower/known/upper 49/59/65), series_a cond 26% (n=74; 13/15/29), series_b cond 16% (n=19; 2/2/18), series_c cond 0% (n=3; upper 16%). Second cohort --industry B2B --years 2020-2022: seed 77%, A 30%, B 35%, C 33%. Calibration rule: stay at or above 0.75 times anchor unless a named analog shows a fatal problem. Coverage is partial, known-only rates are biased low. | 0.34 vs 26 percent anchor, 1.3x; shipped product and large team lift it. |
| Series B | 16% | 22% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed cond 59% (n=126, lower/known/upper 49/59/65), series_a cond 26% (n=74; 13/15/29), series_b cond 16% (n=19; 2/2/18), series_c cond 0% (n=3; upper 16%). Second cohort --industry B2B --years 2020-2022: seed 77%, A 30%, B 35%, C 33%. Calibration rule: stay at or above 0.75 times anchor unless a named analog shows a fatal problem. Coverage is partial, known-only rates are biased low. | Anchor 16 percent; 0.22 is 1.4x with the same lift, within 2x. |
| Series C+ | 20% | 22% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed cond 59% (n=126, lower/known/upper 49/59/65), series_a cond 26% (n=74; 13/15/29), series_b cond 16% (n=19; 2/2/18), series_c cond 0% (n=3; upper 16%). Second cohort --industry B2B --years 2020-2022: seed 77%, A 30%, B 35%, C 33%. Calibration rule: stay at or above 0.75 times anchor unless a named analog shows a fatal problem. Coverage is partial, known-only rates are biased low. | Wide prior; anchor n=3, upper 16 percent. |

## Assumptions and limits

- Blind forecast: only the YC listing text was used.
- Seed means a round above 500K within about 12 months.
- Team size of eight is treated as a sign of an existing product.
- Recorded 2026 batch funding was not used as evidence.

## Sources

- https://zapier.com
- https://www.lindy.ai
- https://openai.com
- https://n8n.io
