# Evaluation: Promptless

*As of 2025-01-06. Mode: summary. An AI teammate that automatically updates your customer-facing docs*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A narrow docs agent with a thin budget category; seed odds track the anchor over a long 22 month window.**

**Chance of getting into YC:** 99% (range 97%–100%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $8M–$20M | 16% | Unlikely | 15% | Unlikely |
| Seed | $3M–$6M | $15M–$35M | 21% | Reasonable | 21% | Reasonable |
| Seed | $6M–$12M | $30M–$70M | 11% | Unlikely | 11% | Unlikely |
| Seed | $12M–$25M | $70M–$150M | 4.2% | Very unlikely | 4.1% | Very unlikely |
| Series A | $6M–$10M | $30M–$55M | 1.6% | Very unlikely | 1.5% | Very unlikely |
| Series A | $10M–$20M | $55M–$110M | 2.3% | Very unlikely | 2.3% | Very unlikely |
| Series A | $20M–$40M | $110M–$250M | 1.3% | Very unlikely | 1.3% | Very unlikely |
| Series B | $15M–$30M | $90M–$200M | 0.3% | Very unlikely | 0.3% | Very unlikely |
| Series B | $30M–$60M | $200M–$500M | 0.4% | Very unlikely | 0.3% | Very unlikely |
| Series B | $60M–$120M | $500M–$1B | 0.2% | Very unlikely | 0.2% | Very unlikely |
| Series C+ | $30M–$70M | $250M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $70M–$150M | $700M–$1.8B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$400M | $1.8B–$5B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Promptless is an AI agent that updates customer facing docs from releases, tickets and Slack. Over a 22.3 month window the B2B cohort anchor gives a seed probability near 0.54, and I report 0.52. Series A inside the same window is about 0.10. Documentation tooling has many entrants and a small budget, and the same wedge produced FifthTry, which died after a seed. The company has a team of five and claims enterprise users, which helps but does not rank it.

## Round by round: where and why it fails

### Getting into YC: 99%

**How we got the number.** The company is already in the batch that starts at the as_of date, so the acceptance step is reported only for completeness: the prior for a random applicant is about 1 percent (0.6 to 2 percent), and conditional on being accepted the forecast below is what matters. Team of 5 with enterprise customers claimed suggests real usage; ideas in developer tools get interest but the wedge is narrow.

**Why it fails here.** YC would most plausibly pass because documentation maintenance looks like a feature rather than a company: docs platforms such as Mintlify and GitBook already offer update agents, coding assistants can draft doc changes inside the repository, and the budget owner is unclear between support, developer relations and engineering. A team of five with claimed enterprise users is a good sign, but the market size question would likely dominate the interview.

### Seed: P(reach this round | in YC) = 52% after the previous step; 52% cumulative if in YC; 51% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $8M–$20M | 30% | 16% | Unlikely | 15% | Unlikely | Small post YC round of about $1M to $3M, often angels and a micro fund. Window based: only a round above about $1M from outside investors that closes inside the window counts, the standard YC deal of about $500K does not. Bands follow the 2022+ seed table (p25 $2.8M, median $4.1M, p75 $6.5M) split into small post YC, institutional and hot seeds. |
| $3M–$6M | $15M–$35M | 40% | 21% | Reasonable | 21% | Reasonable | Institutional seed of $3M to $6M, the common case. Window based: only a round above about $1M from outside investors that closes inside the window counts, the standard YC deal of about $500K does not. Bands follow the 2022+ seed table (p25 $2.8M, median $4.1M, p75 $6.5M) split into small post YC, institutional and hot seeds. |
| $6M–$12M | $30M–$70M | 22% | 11% | Unlikely | 11% | Unlikely | Larger institutional seed of $6M to $12M after fast early traction. Window based: only a round above about $1M from outside investors that closes inside the window counts, the standard YC deal of about $500K does not. Bands follow the 2022+ seed table (p25 $2.8M, median $4.1M, p75 $6.5M) split into small post YC, institutional and hot seeds. |
| $12M–$25M | $70M–$150M | 8.0% | 4.2% | Very unlikely | 4.1% | Very unlikely | Hot seed above $12M, up to about $25M, for an unusually strong story. Window based: only a round above about $1M from outside investors that closes inside the window counts, the standard YC deal of about $500K does not. Bands follow the 2022+ seed table (p25 $2.8M, median $4.1M, p75 $6.5M) split into small post YC, institutional and hot seeds. |

**Why it fails here.** Window of 22.3 months (2025-01-06 to 2026-11-17). The likeliest miss is that docs automation looks like a feature: Mintlify, Swimm, GitBook and ReadMe already sell to the same docs owners and coding assistants can draft doc changes, so investors question the size of the budget. FifthTry (continuous documentation) raised a seed and still shut down, and Nimbic AI is a Spring 2025 neighbor, so a round above $1M needs proof of paid seats at larger firms.

### Series A: P(reach this round | in YC) = 10% after the previous step; 5.2% cumulative if in YC; 5.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $6M–$10M | $30M–$55M | 30% | 1.6% | Very unlikely | 1.5% | Very unlikely | Thin Series A of $6M to $10M at a modest valuation, below the 2022+ median. Series A bands use the 2022+ YC table (p25 $11M, median $15M, p75 $21M) and public medians of about $17M. |
| $10M–$20M | $55M–$110M | 45% | 2.3% | Very unlikely | 2.3% | Very unlikely | Typical Series A of $10M to $20M, near the 2022+ YC median of about $14M. Series A bands use the 2022+ YC table (p25 $11M, median $15M, p75 $21M) and public medians of about $17M. |
| $20M–$40M | $110M–$250M | 25% | 1.3% | Very unlikely | 1.3% | Very unlikely | Strong Series A of $20M to $40M for a fast growing product with revenue. Series A bands use the 2022+ YC table (p25 $11M, median $15M, p75 $21M) and public medians of about $17M. |

**Why it fails here.** A Series A inside 22 months needs about $1M or more of ARR from companies that treat docs as a growth lever. Documentation budgets are small and sit under support or developer relations, sales cycles are slow, and coding assistants that update docs in the repo can substitute. Close analogs (Nimbic AI, FifthTry) stalled at seed, and Series A medians are near 30 months after batch start.

### Series B: P(reach this round | in YC) = 15% after the previous step; 0.8% cumulative if in YC; 0.8% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $90M–$200M | 35% | 0.3% | Very unlikely | 0.3% | Very unlikely | Flat or down style Series B of $15M to $30M. Series B bands use the 2022+ YC table (p25 $27M, median $40M, p75 $55M); few YC companies reach it. |
| $30M–$60M | $200M–$500M | 45% | 0.4% | Very unlikely | 0.3% | Very unlikely | Typical Series B of $30M to $60M, near the 2022+ median of about $40M. Series B bands use the 2022+ YC table (p25 $27M, median $40M, p75 $55M); few YC companies reach it. |
| $60M–$120M | $500M–$1B | 20% | 0.2% | Very unlikely | 0.2% | Very unlikely | Upside Series B of $60M to $120M. Series B bands use the 2022+ YC table (p25 $27M, median $40M, p75 $55M); few YC companies reach it. |

**Why it fails here.** Series B would need a broad product beyond docs updates, for example a support knowledge layer, as a narrow docs agent has a limited ceiling. Only about one in six B2B seed companies reaches B, and the team of five has little time inside the window.

### Series C+: P(reach this round | in YC) = 20% after the previous step; 0.2% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $30M–$70M | $250M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Smaller growth round of $30M to $70M. Series C and later bands use the 2022+ YC table (Series C median $74M, Series D plus $150M); small samples. |
| $70M–$150M | $700M–$1.8B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical Series C of $70M to $150M. Series C and later bands use the 2022+ YC table (Series C median $74M, Series D plus $150M); small samples. |
| $150M–$400M | $1.8B–$5B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Large late round above $150M. Series C and later bands use the 2022+ YC table (Series C median $74M, Series D plus $150M); small samples. |

**Why it fails here.** Series C needs a platform sized category position, and documentation maintenance is a small slice of software spend that docs vendors and coding assistants can absorb by adding an agent. The 2022 to 2024 B2B cohort has no Series C yet, and almost no companies of this size reach it inside two years of batch start, so the probability here is only a small floor value.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 50% | Likely | 50% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 33% | Reasonable | 33% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 14% | Unlikely | 14% | Unlikely |
| Acquired or IPO over $1B | $1B–$10B | 3.0% | Very unlikely | 3.0% | Very unlikely |

**Why it fails here.** The most likely end is a stall or a small acquisition by a docs platform or support vendor: Inari and Unthread are acquired YC analogs at small scale and FifthTry, which sold continuous documentation, shut down after a seed. A larger outcome would require expanding from docs updates into the knowledge layer that support agents and coding assistants read, which is a different and more contested product.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Docs automation is absorbed as a feature by docs platforms and coding assistants | 45% | Mintlify, Swimm and GitBook already sell to docs owners and describe agents that open doc update pull requests. | FifthTry (fifthtry), Nimbic AI (nimbic-ai) | Stay platform agnostic and pull in support and Slack context which code tools lack. |
| 2 | Small budget and long sales cycles keep revenue too low for a round above $1M | 35% | Mid market documentation platforms are priced at about $200 to $1,000 per month per a vendor guide. | FifthTry (fifthtry), Inari (inari) | Anchor on enterprise accounts where docs quality hits churn. |
| 3 | Agent quality errors in customer facing docs erode trust | 25% | Vendor guides note that major changes still need human review, and wrong edits in customer facing docs can cause support load and lost trust. | Nimbic AI (nimbic-ai), FifthTry (fifthtry) | Human approval flow and reliable source citations. |

## Pros

- **Real triggers and context sources**: Product ties updates to releases, tickets and Slack, which docs only tools lack
- **Reported use by Fortune 500 enterprises**: Company description claims enterprise users, unverified

## Roadmap

### Reach Seed

Prove paid seats at larger companies and measurable support deflection

1. Convert pilots at five Fortune 500 or fast growing accounts to annual contracts
2. Show reduced support tickets from updated docs

You know it worked when: $30K plus monthly recurring revenue and a quantified deflection case study

### Reach Series A

Expand beyond docs updates to the knowledge layer

1. Add support and agent facing knowledge base outputs
2. Integrate with the top five docs and help center platforms

You know it worked when: $1M ARR with logo retention above 90 percent

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 1 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Reading code, tickets and Slack and producing accurate edits across arbitrary docs platforms is feasible with current models; the hard part is trustworthy context retrieval, avoiding wrong edits and many integrations. A team of five can ship an MVP in three months but breadth of integrations takes longer. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Promptless: Prompt-based names tie a company to a passing term, much like other AI era coined names; the cohort data show no survival difference, so the name is neutral. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Mintlify, GitBook, Intercom, GitHub Copilot within ~9 months. Docs platforms and coding assistants have distribution and the incentive to ship update agents quickly; a standalone vendor survives only through cross source context and enterprise workflow depth. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Mintlify | Docs platform with agents that propose updates from code changes | Widely used among developer tool startups | https://www.mintlify.com/library/best-code-documentation-tools |
| Swimm and GitBook | Track code to doc relationships and flag stale docs | Established vendors | https://toolradar.com/guides/best-ai-documentation-generators |
| Status quo | Technical writers and engineers editing docs by hand | Default for nearly all companies | https://www.docuwriter.ai/posts/ai-documentation-tools |

### Demand evidence

- Several vendors sell tools that keep docs in sync with code, showing paid demand but a crowded field (https://toolradar.com/guides/best-ai-documentation-generators)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| FifthTry (fifthtry) | Winter 2021 | Inactive | Winter 2021 continuous documentation to end documentation rot, nearly the same pitch. | Raised a seed and later inactive; shows documentation as a thin budget. |
| Nimbic AI (nimbic-ai) | Spring 2025 | Active | Spring 2025 automatically writes and updates internal docs with every code commit. | Active with a seed round, a contemporaneous rival in the same wedge. |
| Inari (inari) | Summer 2023 | Acquired | Summer 2023 junior AI product manager, adjacent knowledge work agent. | Acquired with no post YC round, an acqui-hire style exit. |
| Unthread (unthread) | Summer 2022 | Acquired | Summer 2022 AI helpdesk for Slack, same triggering from support conversations. | Seed then acquired, showing support adjacent tools exit small. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 61% | 52% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed cond 61 percent (n=88), series_a cond 33 percent (n=54), series_b cond 17 percent (n=18); months_to_seed p25 4, median 9, p75 19. Ever 0.61 times about 0.88 arriving inside 22 months gives 0.54. | Anchor times window fraction is 0.54; I trim to 0.52 because documentation tooling is a small paid category where the analog FifthTry died after a seed, but this stays within 1.25 times the anchor and does not rank the company. |
| Series A | 33% | 10% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed cond 61 percent (n=88), series_a cond 33 percent (n=54), series_b cond 17 percent (n=18); months_to_seed p25 4, median 9, p75 19. Ever 0.33 times about 0.3 arriving by month 22 gives 0.10. | More than 2x below the ever rate because only 22 months pass and median months to Series A is 30 from batch start; a five person company with enterprise logos could be early but most are not. |
| Series B | 17% | 15% | python3 -I scripts/base_rates.py --industry B2B --years 2022-2024 --calibration-only: seed cond 61 percent (n=88), series_a cond 33 percent (n=54), series_b cond 17 percent (n=18); months_to_seed p25 4, median 9, p75 19 | Conditional on an A inside 22 months the company would be fast; I keep 0.15 near the 0.17 anchor and the window leaves little room for a B. |
| Series C+ | 36% | 20% | python3 -I scripts/base_rates.py --calibration-only: series_c cond 36 percent (n=55) | Kept at 0.20 because a Series C conditional on a fast B is rare inside this window and the 2022 to 2024 B2B sample has none yet. |

## Assumptions and limits

- Blind forecast made as of 2025-01-06 using only the YC batch description in the input file, with market-only web searches.
- Forecast window is 22.3 months, from 2025-01-06 to 2026-11-17.
- Seed means an outside financing round above about $1M that closes inside the window, not the standard YC deal of about $500K; the seed and Series A probabilities are window probabilities, not ever probabilities.
- The odds do not rank this company against other companies in the batch: in the 2026 winners test, team size, claimed traction and a hot sector did not separate raisers from non raisers, so the seed number stays near the cohort anchor.
- Cohort anchors come from older and 2022 to 2024 batches and are partly right censored; funding coverage in the data is incomplete (lower, known and upper ranges quoted).

## Sources

- https://www.mintlify.com/library/best-code-documentation-tools
- https://toolradar.com/guides/best-ai-documentation-generators
- https://www.docuwriter.ai/posts/ai-documentation-tools
