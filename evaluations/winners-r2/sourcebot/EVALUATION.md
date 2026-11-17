# Evaluation: Sourcebot

*As of 2025-10-06. Mode: summary. Helping humans and AI agents understand massive codebases*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A real open source product with a plausible seed path, but the odds in 13 months stay at the cohort level.**

**Chance of getting into YC:** 3.0% (range 1.5%–6.6%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $10M–$22M | 15% | Unlikely | 0.4% | Very unlikely |
| Seed | $3M–$6M | $18M–$40M | 17% | Unlikely | 0.5% | Very unlikely |
| Seed | $6M–$12M | $35M–$80M | 7.6% | Unlikely | 0.2% | Very unlikely |
| Seed | $12M–$25M | $70M–$150M | 2.9% | Very unlikely | <0.1% | Very unlikely |
| Series A | $6M–$10M | $35M–$60M | 0.7% | Very unlikely | <0.1% | Very unlikely |
| Series A | $10M–$20M | $60M–$120M | 1.3% | Very unlikely | <0.1% | Very unlikely |
| Series A | $20M–$40M | $120M–$250M | 0.9% | Very unlikely | <0.1% | Very unlikely |
| Series B | $20M–$35M | $120M–$220M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $35M–$70M | $220M–$500M | 0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $70M–$150M | $500M–$1.2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$200M | $700M–$2B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $200M–$500M | $2B–$6B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Sourcebot is an open source tool for searching and understanding large codebases, aimed at both developers and AI agents, with a three person team and claimed use at large companies. The need for better agent context is real, but Sourcegraph, GitHub, Cursor and Augment all address it, and open source products often struggle to turn usage into revenue. For the 13 month window I put the seed probability at 0.42, equal to the window adjusted anchor, because the winners test found that traction claims did not separate funded from unfunded companies. If a seed closes, $3M to $6M is the most likely band, with a large share at $1M to $3M. A Series A inside the window is 0.07. The main killer is free usage that never converts into paying enterprises.

## Round by round: where and why it fails

### Getting into YC: 3.0%

**How we got the number.** Already in the Fall 2025 batch, so this is the prior for a random applicant. YC cites about 1 percent acceptance with a third party range of 0.6 to 2 percent. I set 3 percent because the company shows real usage by named large organizations, two years of full time work and technical founders, which are the factors that move odds, but code tooling is crowded.

**Why it fails here.** YC would most plausibly decline because code search and AI coding context was crowded with Sourcegraph, GitHub, Cursor and Augment, open source usage does not prove paid demand, and a three person team may not show a path to revenue or a reason enterprises pay for it when agents can search code themselves.

### Seed: P(reach this round | in YC) = 42% after the previous step; 42% cumulative if in YC; 1.3% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $10M–$22M | 35% | 15% | Unlikely | 0.4% | Very unlikely | Small post YC round: a $1M to $3M check from angels, a pre-seed fund or a YC partner fund, the usual outcome when the product is early and a team is small. |
| $3M–$6M | $18M–$40M | 40% | 17% | Unlikely | 0.5% | Very unlikely | Institutional seed from a dev or AI focused fund, the cohort median region for 2022 and later seed rounds ($3.1M median, quartiles $2.0M and $4.2M in the Developer Tools cohort). |
| $6M–$12M | $35M–$80M | 18% | 7.6% | Unlikely | 0.2% | Very unlikely | Larger institutional seed on strong early usage or a hot category; among confirmed 2026 raises above $1M the median was $6.0M, so this band is realistic but press skewed. |
| $12M–$25M | $70M–$150M | 7.0% | 2.9% | Very unlikely | <0.1% | Very unlikely | Upside seed or seed plus led by a top tier fund on fast growth; rare and usually tied to revenue or breakout open source or product adoption. |

**Why it fails here.** Seed means a round above $1M within 13 months. It most likely fails if open source usage stays free and paid conversion is low, so investors see a popular tool without revenue, a pattern seen with open source developer tools that raised small rounds or none. Void and Driver show open source code tools get a seed at best, and Sourcegraph and the AI coding vendors compete for the same budget.

### Series A: P(reach this round | in YC) = 7.0% after the previous step; 2.9% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $35M–$60M | 25% | 0.7% | Very unlikely | <0.1% | Very unlikely | Thin or flat Series A under $10M, common when growth is real but revenue is early and the lead wants a smaller bet. |
| $10M–$20M | $60M–$120M | 45% | 1.3% | Very unlikely | <0.1% | Very unlikely | Typical 2022 and later Series A: the Developer Tools cohort median raise is $17.5M and the B2B cohort median $15.0M. |
| $20M–$40M | $120M–$250M | 30% | 0.9% | Very unlikely | <0.1% | Very unlikely | Upside Series A led by a large fund when the product is a visible category leader with fast revenue, as seen for the best AI infrastructure and developer rounds of 2024 and 2025. |

**Why it fails here.** A Series A inside the window needs paid enterprise contracts at scale on top of an open source base. On premises enterprise deals need security reviews and annual sales cycles, so a three person team seldom has enough revenue within a year. Sourcegraph took years to build its enterprise business, and Driver and Sage AI stayed at seed or below.

### Series B: P(reach this round | in YC) = 8.0% after the previous step; 0.2% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $20M–$35M | $120M–$220M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Modest Series B on steady growth, below the Developer Tools median of $50M because few companies in the cohort have reached this round. |
| $35M–$70M | $220M–$500M | 50% | 0.1% | Very unlikely | <0.1% | Very unlikely | Typical 2022 and later Series B: $45M to $50M medians with valuations near $550M to $600M in the few cohort cases with data. |
| $70M–$150M | $500M–$1.2B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Breakout round for a category leader growing several times a year. |

**Why it fails here.** A Series B inside the window would need a Series A and a sales team across large enterprises. Open source infrastructure companies reach later rounds only after sustained revenue growth, which takes longer than the window; no code search or code context peer in the YC data did it inside two years.

### Series C+: P(reach this round | in YC) = 5.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Ordinary growth round for a company that has found a repeatable sales motion. |
| $80M–$200M | $700M–$2B | 45% | <0.1% | Very unlikely | <0.1% | Very unlikely | Large growth round from crossover or late stage funds in a hot AI category. |
| $200M–$500M | $2B–$6B | 15% | <0.1% | Very unlikely | <0.1% | Very unlikely | Category defining round, seen only for the top few AI companies. |

**Why it fails here.** A Series C inside two years of a batch would need breakout status in AI coding context, where Cursor, Sourcegraph, GitHub and model labs compete. For a three person open source team with a self hosted product that must first prove paid conversion, a Series C within two years of the batch is extremely unlikely, and none of the code tooling companies in the YC records reached one that fast.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 99% | Very likely |
| Acquired or IPO under $100M | $10M–$100M | 25% | Reasonable | 0.8% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 15% | Unlikely | 0.4% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 5.0% | Unlikely | 0.1% | Very unlikely |

**Why it fails here.** The usual end is a popular open source tool that never converts: agents get built in search, Sourcegraph and GitHub cover enterprise search, and the founders take an acquisition or a job. Mutable.ai ended in an acquisition after a seed and moonrepo shut down despite an open source base, which is the pattern for this niche.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Open source usage does not convert to paid revenue | 45% | The platform is open source and self hosted, so enterprise users can run it free; moonrepo and Void had open source usage without a clear revenue stream. | moonrepo (moonrepo), Void (void) | Sell the enterprise edition with SSO, audit and support, and measure paid conversion early. |
| 2 | Sourcegraph, GitHub and AI coding tools cover the need | 35% | Sourcegraph has sold enterprise code search for years, and GitHub and Cursor index code for their agents, so a three person team competes with bundled context. | mutable.ai (mutable-ai), Sage AI (sage-ai) | Win on on premises deployment, scale to millions of lines and neutral support for any agent. |
| 3 | Coding agents search code natively | 30% | Agents such as Claude Code use agentic search over repositories directly, which weakens the need for a separate index for context. | Driver (driver), Void (void) | Offer an MCP server and shared team index that agents call, and sell cross repository search that single agents lack. |
| 4 | Enterprise sales cycles outlast the runway | 25% | Large companies such as those named need security review for on premises software, which can take quarters; three founders must do sales and engineering. | Pagedraw (pagedraw), mutable.ai (mutable-ai) | Start with team sized deals under procurement thresholds and add a sales hire after the seed. |

## Pros

- **Real usage at large organizations**: The founders state thousands of engineers at companies such as NVIDIA and Red Hat use the product, which is a rare early signal if true; it is self reported.
- **Founders have worked together for years**: The team met at McGill a decade ago and has built full time for over two years, which lowers co-founder risk.

## Roadmap

### Get into YC

Turn open source usage into paid pilots.

1. Contact the largest open source users and offer an enterprise plan.
2. Track weekly active users per organization.

You know it worked when: Three organizations paying for an enterprise license.

### Reach Seed

Show repeatable enterprise revenue on top of the open source base.

1. Ship SSO, audit logs and an MCP server for agents.
2. Close five annual contracts above $20K.

You know it worked when: $25K or more monthly recurring revenue and a measurable conversion rate from free to paid.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Indexing millions of lines with fast regex search and retrieval for agents is hard engineering but well understood, and a small team has already built a working product. The risk is scaling to the largest repositories and keeping answers accurate across many repos. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Sourcebot: A descriptive compound tells developers what it does, in the way GitLab and Sourcegraph do, and suits open source discovery, but it sounds generic and bot is a crowded suffix in 2025. The name is neutral for success. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Sourcegraph, GitHub, Cursor, Augment Code, Anthropic and OpenAI coding agents within ~6 months. Several vendors already ship repository context and indexing, and agents can search code directly. An open source product reduces switching cost only if an enterprise deployment adds clear value. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Sourcegraph | Enterprise code search and code intelligence, with Cody AI. | Long running enterprise vendor with listed enterprise plans. | https://sourcegraph.com/docs/pricing/enterprise |
| GitHub code search and Copilot | Bundled search and AI inside GitHub. | Default for most teams on GitHub. | https://github.blog/changelog/2024-10-29-github-copilot-code-review-in-github-com-public-preview/ |
| Augment Code and Cursor | AI coding tools with their own codebase context engines. | Vendors claim reduced hallucinations on large repositories; unverified. | https://www.augmentcode.com/tools/the-context-gap-why-some-ai-coding-tools-break |

### Demand evidence

- Vendors report that AI coding tools miss context in large codebases, which supports demand for better code context. (https://www.augmentcode.com/tools/the-context-gap-why-some-ai-coding-tools-break)
- Sourcegraph sells enterprise code search with prices starting in the thousands of dollars per year, showing paid demand. (https://sourcegraph.com/docs/pricing/enterprise)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Driver (driver) | Winter 2024 | Active | Context for codebases, Winter 2024, a close wedge. | Records show a seed as highest round, timing not used; open source and context tools raise modest rounds. |
| Sage AI (sage-ai) | Winter 2023 | Active | Self maintaining code knowledge base, Winter 2023. | Active with no post YC round found at the as_of date. |
| mutable.ai (mutable-ai) | Winter 2022 | Acquired | AI for understanding and writing code, Winter 2022. | Seed, then acquired; a small exit for AI code tooling. |
| moonrepo (moonrepo) | Winter 2023 | Inactive | Open source build tool for large codebases. | Winter 2023, inactive with no round above the YC deal; a cautionary open source case. |
| Void (void) | Summer 2024 | Active | Open source Cursor alternative, Summer 2024. | Active with no round found at the as_of date; open source usage without revenue. |
| Pagedraw (pagedraw) | Winter 2018 | Inactive | Earlier developer tooling that depended on code understanding. | Winter 2018, raised a seed and shut down. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 42% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: seed cond 59% known-only (lower 49%, upper 65%, n=126); python3 -I scripts/base_rates.py --tag "Developer Tools" --years 2022-2025: seed 42% / 49% / 56% (n=254). Timing from knowledge/tables/time_to_milestones.csv era 2022+: months_to_seed p25 3, p50 6, p75 14.2 (n=1146). Open Source tag 2022-2025 calibration only: seed 80% known-only but n=10, too thin to use. | Window is about 13 months (2025-10-06 to 2026-11-17). About 70 to 75 percent of eventual seeds close inside that time, so the window anchor is about 0.42 from the 59 percent B2B figure. I keep 0.42: real open source usage inside large companies is a genuine signal, but the winners test showed traction claims did not separate funded from unfunded companies, and open source revenue is slow. The odds do not rank this company against others. |
| Series A | 26% | 7.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: series_a cond 26% known-only (lower 13%, upper 29%, n=74); Developer Tools 2022-2025: series_a cond 23% (n=124). Timing, era 2022+: months_to_series_a p25 19.4, p50 28, p75 38.4 (n=216). | The anchor is the chance of ever reaching Series A, with a median of 28 months after batch start. A seed in the 13 month window must come first, and open source monetization normally takes longer, so I cut the anchor to about a quarter. |
| Series B | 16% | 8.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: series_b cond 16% (n=19), range 2% to 18% across lower, known and upper. | The anchor is the chance of ever reaching Series B. In a window that ends about 13 to 22 months after the batch starts, the time to milestone table gives a median of about 35 months for Series B in the 2022 and later era, so only a small share of eventual Series B companies get there inside the window; I cut the anchor roughly in half and say the number is a window number. |
| Series C+ | none | 5.0% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2025 --calibration-only: series_c 0% known-only, 16% upper (n=3), so there is no usable rate for the cohort. | The cohort has almost no Series C companies, so I use a small number tied to the window length: reaching Series C within about two years of a YC batch has happened only for a handful of breakout companies in the 2022 and later era, and the time to milestone table shows a median of about 37 months. |

## Assumptions and limits

- Blind forecast as of 2025-10-06 for about 13 months to 2026-11-17; seed means above about $1M from outside investors.
- Only the input file was used for the company; the description's usage claims are the founders' and unverified.
- Market search results naming other companies or dated after the as_of date were ignored.
- Company already in YC; the YC odds are the prior for a random applicant.
- The Open Source tag cohort is too small (n=10) to use as the main anchor.

## Sources

- https://sourcegraph.com/docs/pricing/enterprise
- https://www.augmentcode.com/tools/the-context-gap-why-some-ai-coding-tools-break
- https://github.blog/changelog/2024-10-29-github-copilot-code-review-in-github-com-public-preview/
