# Evaluation: Candor

*As of 2025-01-06. Mode: summary. Protect your data and stop insider risk*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**Candor is a plausible seed candidate in a real but crowded market, and the odds do not rank it against others.**

**Chance of getting into YC:** 97% (range 95%–99%), very likely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $1M–$3M | $10M–$20M | 16% | Unlikely | 15% | Unlikely |
| Seed | $3M–$6M | $20M–$40M | 21% | Reasonable | 20% | Reasonable |
| Seed | $6M–$12M | $35M–$70M | 11% | Unlikely | 11% | Unlikely |
| Seed | $12M–$20M | $60M–$110M | 4.2% | Very unlikely | 4.0% | Very unlikely |
| Series A | $5M–$9M | $25M–$45M | 1.6% | Very unlikely | 1.5% | Very unlikely |
| Series A | $9M–$18M | $45M–$100M | 3.1% | Very unlikely | 3.0% | Very unlikely |
| Series A | $18M–$35M | $100M–$250M | 1.6% | Very unlikely | 1.5% | Very unlikely |
| Series B | $15M–$30M | $80M–$150M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $150M–$350M | 0.1% | Very unlikely | 0.1% | Very unlikely |
| Series B | $60M–$120M | $350M–$900M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$1.5B | <0.1% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$300M | $1.5B–$4B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Candor sells AI agent based data loss prevention to lean security teams, a market with several billion dollars of spend and a well documented complaint about false positives. Near analogs in the YC data (strac, repacket, promptarmor) reached seed rounds in the $3M to $4M range but few reached a Series A, and the incumbents can bundle similar features. Over a 22 month window the seed probability is about half and the A is unlikely. The seed would most likely be $3M to $6M from a security focused fund if pilots convert.

## Round by round: where and why it fails

### Getting into YC: 97%

**How we got the number.** The input file places Candor in the Winter 2025 batch with the batch start as the as_of date, so acceptance is treated as already happened. The prior for a random applicant is about 1 percent (references/yc_acceptance.md), but conditional on being listed in the batch the residual doubt is only data error or a deferral. Seed odds below are conditional on being in YC.

**Why it fails here.** The only way the YC step fails here is a clerical error in the batch listing or a deferral to a later batch. Candor was reported in the batch directory as of the as_of date, so the reason to say no has already been resolved in its favor.

### Seed: P(reach this round | in YC) = 52% after the previous step; 52% cumulative if in YC; 50% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $1M–$3M | $10M–$20M | 30% | 16% | Unlikely | 15% | Unlikely | Small post YC round of $1M to $3M, typically angels and a micro fund. This is the second most common outcome for a 2 to 5 person team with early pilots and no scaled revenue, and it is more likely here than in the winners test sample because press favours big rounds. The plain YC deal of about $500K does not count as seed in this forecast. |
| $3M–$6M | $20M–$40M | 40% | 21% | Reasonable | 20% | Reasonable | Institutional seed of $3M to $6M led by a seed fund. This is the center of the 2022 and later benchmark (median about $4.1M in our table) and of the 2026 confirmed raises (lower quartile $4.3M). |
| $6M–$12M | $35M–$70M | 22% | 11% | Unlikely | 11% | Unlikely | Larger institutional seed of $6M to $12M. Reachable if a design partner or demo produces competitive tension, as in the 2026 winners where the median confirmed raise was $6.0M, a sample that leans high. |
| $12M–$20M | $60M–$110M | 8.0% | 4.2% | Very unlikely | 4.0% | Very unlikely | Upside seed above $12M, reserved for a hot category with a standout team. Rare for a team this small and early. |

**Why it fails here.** Candor most likely misses the seed because three founders with a security product but no named enterprise logos in the batch listing look like a feature of Microsoft Purview or CrowdStrike Falcon Data Protection to a seed investor. Strac, Repacket and PromptArmor reached seed only with named customers and prior security credibility. If Candor cannot show paying design partners and a measured false positive reduction by demo day, the round is a small angel check or the YC deal only.

### Series A: P(reach this round | in YC) = 12% after the previous step; 6.2% cumulative if in YC; 6.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$9M | $25M–$45M | 25% | 1.6% | Very unlikely | 1.5% | Very unlikely | Thin or small Series A, close to a large seed, for a company with some revenue but unproven repeatability. Current 2022 and later YC Series A lower quartile is $10.0M, so this is the thin end. |
| $9M–$18M | $45M–$100M | 50% | 3.1% | Very unlikely | 3.0% | Very unlikely | Typical Series A of $9M to $18M, matching the 2022 and later YC median of $14.15M (n=52) and public market medians near $17M. |
| $18M–$35M | $100M–$250M | 25% | 1.6% | Very unlikely | 1.5% | Very unlikely | Upside Series A with a clear ARR ramp; AI native companies have printed larger A rounds in 2025 and 2026 but these remain the minority. |

**Why it fails here.** An A in under two years after the batch requires roughly $1M or more in annual recurring revenue from security buyers, who have long evaluation cycles and SOC 2 style procurement hurdles. Candor is likely to hold a seed and about 6 to 10 pilots with little paid conversion, and investors will ask why customers would swap a bundled Microsoft or Google DLP for a three person startup. Thinair reached A in a prior cycle and still died, which shows an A is not safety.

### Series B: P(reach this round | in YC) = 4.0% after the previous step; 0.2% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$150M | 30% | <0.1% | Very unlikely | <0.1% | Very unlikely | Thin Series B or extension, near the 2022 and later lower quartile of $25M. |
| $30M–$60M | $150M–$350M | 50% | 0.1% | Very unlikely | 0.1% | Very unlikely | Typical Series B, around the YC 2022 and later median of $37M (n=22). |
| $60M–$120M | $350M–$900M | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside Series B on breakout growth, in line with the few 2022 and later B valuations near $775M. |

**Why it fails here.** Reaching a Series B inside this window would need an A in the first half of the window and growth that doubles repeatedly. Security data products are slow to compound because each deployment needs endpoint agents and policy tuning, and large DLP rivals bundle price. The likely stop is at the A or earlier, so the B is a floor probability for an outlier ramp.

### Series C+: P(reach this round | in YC) = 2.0% after the previous step; <0.1% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Series C or growth round near the 2022 and later YC median of $45M (n=9), with a flat or modest step up. |
| $80M–$150M | $700M–$1.5B | 40% | <0.1% | Very unlikely | <0.1% | Very unlikely | Typical growth round of $80M to $150M for a category leader with strong net retention, as seen in the larger 2022 and later rounds in the YC data. |
| $150M–$300M | $1.5B–$4B | 20% | <0.1% | Very unlikely | <0.1% | Very unlikely | Upside round for a category winner; the sample of 2022 and later C rounds is tiny (n=9) so this band is judgment. |

**Why it fails here.** A Series C in the window is nearly impossible: it requires two prior rounds inside 22 months and a scale that no recent YC security company reached that fast. Past YC security companies that reached C needed 7 or more years. The floor reflects only an extreme outlier.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 62% | Likely | 63% | Likely |
| Acquired or IPO under $100M | $5M–$100M | 22% | Reasonable | 21% | Reasonable |
| Acquired or IPO $100M-$1B | $100M–$1B | 12% | Unlikely | 12% | Unlikely |
| Acquired or IPO over $1B | $1B–$5B | 4.0% | Very unlikely | 3.9% | Very unlikely |

**Why it fails here.** Most paths end in a shutdown, a quiet stall, or a small acqui-hire because DLP is a mature category dominated by Microsoft, Forcepoint, Proofpoint and CrowdStrike, which can bundle a similar agent feature in under 18 months. A three person team must win a trust sale to security buyers who prefer incumbents, and the winner outcome needs a platform expansion to broader data security that the analogs (strac, unbound) have only partly achieved.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Incumbent bundling: Microsoft Purview and CrowdStrike ship agentic DLP inside suites | 35% | Gartner says the DLP market is mature and converging with insider risk, and large vendors already add AI classification to reduce false positives. | ThinAir (thinair), Strac (strac) | Pick a wedge incumbents ignore, such as source code exfiltration at startups, and win on setup in minutes. |
| 2 | Long security sales cycles and trust: buyers will not install an endpoint agent from three people | 30% | Past YC security companies needed named logos and certifications before seeds; Repacket and PromptArmor sold with proof of customers. | Repacket (repacket), PromptArmor (promptarmor) | Land design partners through founder networks and obtain SOC 2 early. |
| 3 | Team of 3 with no stated security leadership logos stalls before a seed | 25% | The listing shows a 3 person team and no customers; seeds in the cohort went to teams with product experience at Palo Alto Networks or Imperva. | Repacket (repacket), PromptArmor (promptarmor) | Add a security advisor and show pilot data in the first 8 weeks. |
| 4 | AI agent accuracy: if the agents hallucinate or miss exfiltration the product loses its one claim of fewer false positives | 20% | The company positioning rests entirely on lower noise than legacy tools, with no public benchmark in the input description. | Strac (strac) | Publish a head to head false positive benchmark with a design partner. |

## Pros

- **Real, funded pain with an AI tailwind**: DLP spend runs in the billions and analysts cite false positives as the main complaint that agents can address. (https://www.marketsandmarkets.com/ResearchInsight/size-and-share-of-data-loss-prevention-advanced-technologies-market.asp)
- **Nearby YC wedges (strac, repacket) reached seed**: Both are recorded in the YC data with seed rounds and no shutdown, so seed odds for this wedge are real.

## Roadmap

### Get into YC

Show real security buyers will test it.

1. Sign 3 design partners from the founders' network
2. Ship an email and cloud drive exfiltration detector

You know it worked when: 3 signed pilots and a measured false positive rate

### Reach Seed

Prove paid conversion beyond pilots.

1. Convert pilots to paid annual contracts
2. Publish a false positive benchmark against legacy DLP

You know it worked when: $150K in annual contract value from at least 5 customers

### Reach Series A

Show a repeatable security sale.

1. Hire a first sales leader
2. Add SOC 2 and endpoint coverage

You know it worked when: $1M in recurring revenue with under 5 percent logo churn

### Reach Series B

Expand from DLP to broader data security.

1. Add DSPM and AI usage control modules
2. Build channel partners

You know it worked when: $8M in recurring revenue growing 2.5x

### Reach Series C and beyond

Become a category platform.

1. Move upmarket to enterprise
2. Add international coverage

You know it worked when: $30M in recurring revenue and a net retention above 120 percent

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 3 | Detecting data movement across email, cloud and endpoints needs integrations and an agent, and judging intent with LLMs needs careful evaluation, but a 3 person team can ship a narrow email and cloud storage version in three months. The hard part is trust and accuracy, not core research. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Candor: Candor is short and pronounceable like other recent YC security names such as Strac, but it does not signal the category or give a distinct brand voice. A weak or neutral name rarely sinks a company, so it does not move the ladder. |
| Takeover/copy risk (5 = very likely) | 4 | Could be built or absorbed by Microsoft, CrowdStrike, Palo Alto Networks, Forcepoint within ~12 months. Large vendors already own the endpoint and email data and have both the incentive and distribution to add an AI triage layer. A well resourced rival could ship a similar agent feature in about 12 months, so the startup must be a faster, cheaper wedge at smaller companies. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Microsoft Purview | Bundled DLP and insider risk management for Microsoft 365 customers. | Default for Microsoft shops; free or cheap inside E5 licenses. | https://www.marketsandmarkets.com/ResearchInsight/size-and-share-of-data-loss-prevention-advanced-technologies-market.asp |
| Forcepoint and Proofpoint DLP | Legacy enterprise DLP with classification engines and insider risk modules. | Long tenured vendors named in Gartner DLP market overview; the incumbents the pitch positions against. | https://www.forcepoint.com/resources/industry-analyst-reports/gartner-market-overview-data-loss-prevention |
| Strac and Unbound style SaaS and AI DLP startups | Newer startups selling data discovery, DLP and AI usage control. | Seed stage companies with public customers per YC directory records. | https://www.crowdstrike.com/content/dam/crowdstrike/marketing/en-us/documents/pdfs/reports/DLP-Report.pdf |

### Demand evidence

- DLP is a multi billion dollar market with estimates from $2B to $4.7B in 2024, and analysts tie false positives to buyer pain. (https://www.marketsandmarkets.com/ResearchInsight/size-and-share-of-data-loss-prevention-advanced-technologies-market.asp)
- Gartner says the line between data loss and insider risk is disappearing and cites false positives as friction between security and business teams. (https://www.forcepoint.com/blog/insights/2025-gartner-market-guide-dlp)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Strac (strac) | Winter 2022 | Active | Closest wedge: DLP and data security for SaaS, same buyer and same incumbents, batch Winter 2022. | Raised a $3.5M seed in July 2022, stayed independent and expanded into DSPM and AI data governance; an alive survivor but not a runaway, which is the median good outcome for this wedge. |
| Repacket (repacket) | Winter 2023 | Active | Small team employee security product from Winter 2023 selling to lean security teams. | Raised a seed in 2023 and is still active with a small team; no A reported, showing the plateau after seed. |
| PromptArmor (promptarmor) | Winter 2024 | Active | AI security startup from Winter 2024 with named enterprise customers and a crowded field. | Alive with a seed as its highest round; the category consolidates through acquisitions, which raises both pressure and exit odds. |
| ThinAir (thinair) | Winter 2015 | Inactive | Data security for teams from Winter 2015, an older DLP style failure case. | Reached a Series A in 2016 per directory data but is now marked inactive; shows that an A does not rescue a crowded security category. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 52% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025 (150 researched: seed 49% / 59% / 65%, series_a cond 26% n=74, series_b cond 16% n=19); seed cond known-only 59% (n=126); months_to_seed median 7 (p25 3, p75 15) from knowledge/tables/time_to_milestones.csv calibration sample | The anchor is the ever rate for B2B companies from 2022 to 2025 (59 percent known-only, 65 percent upper). The window is 22 months from the Winter 2025 batch start to 2026-11-17, and by about 22 months most companies that eventually raise a seed have done so (median 7 months, p75 about 15 to 20), so about 85 percent of the ever rate is realized, giving about 0.50. The security cohort anchor is 72 percent (n=18) and a named analog (strac) raised an institutional seed, so I nudge to 0.52, under the 1.25 times cap. This number does not rank Candor against other companies. |
| Series A | 26% | 12% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025 (150 researched: seed 49% / 59% / 65%, series_a cond 26% n=74, series_b cond 16% n=19); series_a cond 26% (n=74) (ever); months_to_series_a median 29 from batch start (B2B 2022 to 2025, n=19) | The window is 22 months but only a minority of seed companies go on to a Series A within about 20 months of the seed (median 29 months from batch start to A in this cohort, n=19, right censored). The ever conditional rate is 26 percent for B2B and 38 percent for security (n=13). Within the window I put about 0.12, under half of the ever rate, because the seed itself has to land early for an A to also land. |
| Series B | 16% | 4.0% | python3 -I scripts/base_rates.py --calibration-only --industry B2B --years 2022-2025: series_b cond 16% (n=19) ever, lower 2% known-only | The window is 22 months, and Series B needs a median of 46 months from batch start (all eras, n=510 in time_to_milestones.csv; B2B 2022 to 2025 median 26 months on n=3, right censored). The probability is a floor for a fast outlier, far below the 16 percent ever rate, because only a company that raised both a seed and an A inside the window can get here. |
| Series C+ | 12% | 2.0% | Series C cond is 0% of n=3 in the B2B 2022 to 2025 cohort; the older all-era calibration sample gives about 30 to 35 percent of series_b reaching C, discounted here for the window | The window ends 22 months after the as_of date and a Series C needs a median of 61 months from batch start (all eras, n=221 in time_to_milestones.csv). The probability is a small floor rather than an anchor ratio, because 3 companies in the recent cohort cannot support a rate. |

## Assumptions and limits

- Window is 22 months from the 2025-01-06 as_of to 2026-11-17; seed means a round above about $1M from outside investors, excluding the YC deal.
- Team of 3 and no customer data are known only from the input description.
- Analog records were read as of their stored fields; their outcomes after the as_of date were not used for Candor.
- Market web search found no result naming Candor.

## Sources

- https://www.marketsandmarkets.com/ResearchInsight/size-and-share-of-data-loss-prevention-advanced-technologies-market.asp
- https://www.forcepoint.com/blog/insights/2025-gartner-market-guide-dlp
- https://www.crowdstrike.com/content/dam/crowdstrike/marketing/en-us/documents/pdfs/reports/DLP-Report.pdf
- https://www.forcepoint.com/resources/industry-analyst-reports/gartner-market-overview-data-loss-prevention
