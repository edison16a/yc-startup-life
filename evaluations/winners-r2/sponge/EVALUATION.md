# Evaluation: Sponge

*As of 2026-01-05. Mode: summary. Financial infrastructure for the agent economy*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Sponge is early to a market that is real but tiny today, so a seed in 10 months is under even odds and the odds do not rank it.**

**Chance of getting into YC:** 97% (range 95%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $10M–$20M | 11% | Unlikely | 11% | Unlikely |
| Seed | $3M–$6M | $20M–$40M | 15% | Unlikely | 15% | Unlikely |
| Seed | $6M–$12M | $35M–$70M | 8.4% | Unlikely | 8.1% | Unlikely |
| Seed | $12M–$20M | $60M–$110M | 3.0% | Very unlikely | 2.9% | Very unlikely |
| Series A | $5M–$9M | $25M–$45M | 0.4% | Very unlikely | 0.4% | Very unlikely |
| Series A | $9M–$18M | $45M–$100M | 0.8% | Very unlikely | 0.7% | Very unlikely |
| Series A | $18M–$35M | $100M–$250M | 0.4% | Very unlikely | 0.4% | Very unlikely |
| Series B | $15M–$30M | $80M–$150M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $150M–$350M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $350M–$900M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$1.5B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$300M | $1.5B–$4B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Sponge sells wallets, cards and acceptance rails to the agent economy, a theme that Coinbase, Stripe, Visa and Google are all building toward. YC peers in agent and stablecoin infrastructure such as naive and primevault show no post YC rounds, while wallet infrastructure like zerodev reached a Series A over several years. In a 10 month window the seed is about 38 percent and mostly $3M to $6M if reached. The big risk is that platforms and open standards own the rails and agent spend stays small.

## Round by round: where and why it fails

### Getting into YC: 97%

**How we got the number.** The input file places Sponge in the Winter 2026 batch with the batch start as the as_of date, so acceptance is treated as already happened. The prior for a random applicant is about 1 percent (references/yc_acceptance.md), but conditional on being listed in the batch the residual doubt is only data error or a deferral. Seed odds below are conditional on being in YC.

**Why it fails here.** The only way the YC step fails here is a clerical error in the batch listing or a deferral to a later batch. Sponge was reported in the batch directory as of the as_of date, so the reason to say no has already been resolved in its favor.

### Seed: P(reach this round | in YC) = 38% after the previous step; 38% cumulative if in YC; 37% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $10M–$20M | 30% | 11% | Unlikely | 11% | Unlikely | Small post YC round of $1M to $3M, typically angels and a micro fund. This is the second most common outcome for a 2 to 5 person team with early pilots and no scaled revenue, and it is more likely here than in the winners test sample because press favours big rounds. The plain YC deal of about $500K does not count as seed in this forecast. |
| $3M–$6M | $20M–$40M | 40% | 15% | Unlikely | 15% | Unlikely | Institutional seed of $3M to $6M led by a seed fund. This is the center of the 2022 and later benchmark (median about $4.1M in our table) and of the 2026 confirmed raises (lower quartile $4.3M). |
| $6M–$12M | $35M–$70M | 22% | 8.4% | Unlikely | 8.1% | Unlikely | Larger institutional seed of $6M to $12M. Reachable if a design partner or demo produces competitive tension, as in the 2026 winners where the median confirmed raise was $6.0M, a sample that leans high. |
| $12M–$20M | $60M–$110M | 8.0% | 3.0% | Very unlikely | 2.9% | Very unlikely | Upside seed above $12M, reserved for a hot category with a standout team. Rare for a team this small and early. |

**Why it fails here.** Sponge most likely misses the seed because the agent commerce market has little transaction volume yet and open standards such as x402 let any API accept stablecoin payments without an intermediary, so an investor sees thin revenue and a protocol risk. Naive and Primevault from the YC data show agent and stablecoin infrastructure companies reaching seed only with a clear regulated product. If agent spend stays tiny, Sponge gets only the YC deal.

### Series A: P(reach this round | in YC) = 4.0% after the previous step; 1.5% cumulative if in YC; 1.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$9M | $25M–$45M | 25% | 0.4% | Very unlikely | 0.4% | Very unlikely | Thin or small Series A, close to a large seed, for a company with some revenue but unproven repeatability. Current 2022 and later YC Series A lower quartile is $10.0M, so this is the thin end. |
| $9M–$18M | $45M–$100M | 50% | 0.8% | Very unlikely | 0.7% | Very unlikely | Typical Series A of $9M to $18M, matching the 2022 and later YC median of $14.15M (n=52) and public market medians near $17M. |
| $18M–$35M | $100M–$250M | 25% | 0.4% | Very unlikely | 0.4% | Very unlikely | Upside Series A with a clear ARR ramp; AI native companies have printed larger A rounds in 2025 and 2026 but these remain the minority. |

**Why it fails here.** A Series A needs real volume from agents, but 2026 volumes are still small and Stripe, Coinbase and Visa are building agent payment protocols with distribution Sponge lacks. Compliance, bank partners and card issuing add months and licensing costs. The likely stall is a seed funded pilot with a few hundred agent developers and no sustaining revenue.

### Series B: P(reach this round | in YC) = 2.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$150M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Thin Series B or extension, near the 2022 and later lower quartile of $25M. |
| $30M–$60M | $150M–$350M | 50% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series B, around the YC 2022 and later median of $37M (n=22). |
| $60M–$120M | $350M–$900M | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside Series B on breakout growth, in line with the few 2022 and later B valuations near $775M. |

**Why it fails here.** A Series B within 10 months of the batch is a tail event that needs the agent payments market to explode and Sponge to be the default rail. The floor reflects only that scenario. Even beyond the window, a B requires agent spending to become large and Sponge to be a default rail against Stripe, Coinbase and Visa, while compliance and bank partners slow growth. Stablecoin infrastructure peers like primevault show no round beyond seed in the data.

### Series C+: P(reach this round | in YC) = 2.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Series C or growth round near the 2022 and later YC median of $45M (n=9), with a flat or modest step up. |
| $80M–$150M | $700M–$1.5B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical growth round of $80M to $150M for a category leader with strong net retention, as seen in the larger 2022 and later rounds in the YC data. |
| $150M–$300M | $1.5B–$4B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside round for a category winner; the sample of 2022 and later C rounds is tiny (n=9) so this band is judgment. |

**Why it fails here.** A Series C inside the window is essentially impossible by timing and the probability is a floor. Beyond the window a late stage round would need real network scale in agent payments and licenses held directly. No close YC peer has gotten there, so the number is a floor and the realistic tail is acquisition by a payments company wanting agent distribution.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 62% | Likely | 63% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 22% | Reasonable | 21% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 12% | Unlikely | 12% | Unlikely |
| Acquired or IPO over $1B | $1B–$5B | 4.0% | Very unlikely | 3.9% | Very unlikely |

**Why it fails here.** Most paths end with stall or pivot: the product depends on an agent economy that is not yet paying, standards bodies and giants (Stripe, Coinbase, Visa, Google) set the rails, and a small team carries bank, card and compliance dependencies. The upside is an acquisition by a payments company wanting agent distribution.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Agent spending volume stays too small to build revenue | 40% | Agent payments protocols launched only in 2025 and adoption claims are vendor sourced and unverified in the search results. | Naïve (naive), PrimeVault (primevault) | Sell to a few agent platforms with real spend and charge a SaaS fee, not only take rate. |
| 2 | Giants and open protocols own the rails: Coinbase x402, Stripe, Visa and Google | 35% | Coinbase announced x402 with AWS, Circle and Anthropic in May 2025 and Visa and Stripe have their own agent protocols. | ZeroDev (zerodev), Mono (mono-2) | Be the neutral multi rail layer and onboard sellers fast. |
| 3 | Regulation and compliance: holding funds and issuing cards needs licenses and bank partners | 30% | Embedded finance startups in the YC data (mono-2, paycaddy) spent years on licensing and bank partners. | Mono (mono-2), PayCaddy (paycaddy) | Use licensed partners and limit to stablecoins first. |
| 4 | Three person team spread across bank accounts, cards and crypto | 25% | Team size 3 and a scope covering three money rails for agents and sellers. | PrimeVault (primevault) | Choose one rail first. |

## Pros

- **Timely theme backed by large platforms**: Coinbase, Stripe, Visa and Google all publish agent payment work, validating the problem. (https://www.coinbase.com/developer-platform/discover/launches/x402)
- **Two sided model: wallets for agents and acceptance for sellers**: The description offers both sides of the market, which could build a network.

## Roadmap

### Get into YC

Show agents actually spend money through Sponge.

1. Onboard 20 agent builders
2. Ship a wallet and card API

You know it worked when: $50K monthly agent volume

### Reach Seed

Show growing volume and sellers.

1. Add 10 sellers who accept agent payments
2. Add stablecoin and card rails

You know it worked when: $1M monthly volume

### Reach Series A

Show revenue and compliance.

1. Obtain licensing through partners
2. Reach take rate revenue

You know it worked when: $500K annualized net revenue

### Reach Series B

Become a default rail.

1. Add enterprise controls
2. Add regions

You know it worked when: $10M annualized net revenue

### Reach Series C and beyond

Scale as payments network.

1. Direct network integrations
2. Acquire licenses

You know it worked when: $40M annualized net revenue

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Holding funds for agents across bank accounts, cards and crypto needs compliance, fraud controls, ledger accuracy and licensed partners. A small team can wrap partners and ship a crypto wallet API in three months, but real bank and card programs take much longer. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Sponge: Sponge is a short, friendly common word like Brex or Ramp style names, but the cartoon association may undercut trust for a money product. It is neutral for the ladder. |
| Takeover/copy risk (5 = very likely) | 5 | Could be built or absorbed by Coinbase, Stripe, Visa, Google within ~6 months. Coinbase, Stripe, Visa and Google already publish agent payment standards and own distribution and licenses, so they can add the features in months. The startup survives only as a neutral layer or a fast partner. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Coinbase x402 | HTTP native stablecoin payment protocol for agents and APIs. | Announced May 2025 with AWS, Circle, Anthropic and Near as partners. | https://www.coinbase.com/developer-platform/discover/launches/x402 |
| Stripe and Visa agent commerce protocols | Agentic Commerce Protocol and Trusted Agent Protocol for card payments by agents. | Named alongside x402 as coordinating standards. | https://www.allium.so/blog/x402-explained-the-internet-native-payments-standard-for-apis-data-and-agent-commerce/ |
| Google AP2 | Agent Payments Protocol with an x402 extension. | Coverage describes interoperability work among major protocols. | https://www.spark.money/research/x402-protocol-ai-agent-payments |

### Demand evidence

- Coinbase launched the x402 stablecoin payment protocol for agents in May 2025 with major partners, signaling that platforms see demand. (https://www.coinbase.com/developer-platform/discover/launches/x402)
- Several protocols for agent payments are coordinating on interoperability, per trade coverage, though adoption figures are unverified. (https://www.spark.money/research/x402-protocol-ai-agent-payments)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Naïve (naive) | Spring 2025 | Active | Autonomous company infrastructure for agents, Spring 2025, the same theme of agents that transact. | Alive with no post YC round recorded in the data, so the agent finance theme has not yet proven fundable in this cohort. |
| PrimeVault (primevault) | Summer 2022 | Active | Stablecoin and digital finance infrastructure, Summer 2022, the same crypto rail layer. | Alive with no post YC round recorded. |
| ZeroDev (zerodev) | Winter 2023 | Active | Account abstraction wallets as a service, Winter 2023, the same wallet infra for apps. | Alive and reached a Series A according to the record, a successful wallet infrastructure path. |
| Mono (mono-2) | Winter 2022 | Active | Embedded finance infrastructure, Winter 2022, shows the compliance heavy API business. | Alive and reached a seed as its highest round, a standard fintech infrastructure trajectory. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 66% | 38% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025 (150 researched: seed 49% / 59% / 65%, series_a cond 26% n=74, series_b cond 16% n=19); seed cond known-only 66% (Fintech 2022-2025 n=29; B2B 59%); months_to_seed median 7 (p25 3, p75 15) from knowledge/tables/time_to_milestones.csv calibration sample | The anchor is 66 percent known-only for Fintech 2022 to 2025 (n=29) and 59 percent for B2B. The window is 10 months, which realizes about 55 to 60 percent of eventual seed raising (median 7 months), giving about 0.38 on the Fintech anchor. The agent payments theme is hot and crypto adjacent, but fintech compliance is slow, so I give no lift and stay under the 1.25 times cap. The number does not rank Sponge against others. |
| Series A | 26% | 4.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025 (150 researched: seed 49% / 59% / 65%, series_a cond 26% n=74, series_b cond 16% n=19); series_a cond 26% (n=74) (ever); months_to_series_a median 29 from batch start (B2B 2022 to 2025, n=19) | A Series A within 10 months is rare; the Fintech cohort shows A at 10 percent known-only and cond 16 percent, and median time to A is about 29 months from batch start. Inside this window about 0.04 given a seed. |
| Series B | 16% | 2.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025: series_b cond 16% (n=19) ever, lower 2% known-only | The window is 10 months, and Series B needs a median of 46 months from batch start (all eras, n=510 in time_to_milestones.csv; B2B 2022 to 2025 median 26 months on n=3, right censored). The probability is a floor for a fast outlier, far below the 16 percent ever rate, because only a company that raised both a seed and an A inside the window can get here. |
| Series C+ | 12% | 2.0% | Series C cond is 0% of n=3 in the B2B 2022 to 2025 cohort; the older all-era calibration sample gives about 30 to 35 percent of series_b reaching C, discounted here for the window | The window ends 10 months after the as_of date and a Series C needs a median of 61 months from batch start (all eras, n=221 in time_to_milestones.csv). The probability is a small floor rather than an anchor ratio, because 3 companies in the recent cohort cannot support a rate. |

## Assumptions and limits

- Window is 10 months from 2026-01-05 to 2026-11-17; seed means above about $1M from outside investors, excluding the YC deal.
- Team of 3 and empty tags from the input file.
- Several crypto sources are promotional and adoption figures were not used.
- No search result named Sponge.

## Sources

- https://www.coinbase.com/developer-platform/discover/launches/x402
- https://www.allium.so/blog/x402-explained-the-internet-native-payments-standard-for-apis-data-and-agent-commerce/
- https://www.spark.money/research/x402-protocol-ai-agent-payments
