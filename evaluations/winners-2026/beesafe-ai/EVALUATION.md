# Evaluation: BeeSafe AI

*As of 2026-01-05. Mode: summary. Frontier AI Defenses for Social Engineering Attacks*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A timely fraud intelligence bet whose dataset claim is unproven and whose bank sales cycle is the main danger.**

**Chance of getting into YC:** 4.0% (range 2.0%–8.0%), very unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$1.5M | $8M–$15M | 14% | Unlikely | 0.6% | Very unlikely |
| Seed | $2M–$4M | $15M–$30M | 25% | Reasonable | 1.0% | Very unlikely |
| Seed | $4M–$8M | $30M–$60M | 16% | Unlikely | 0.7% | Very unlikely |
| Series A | $5M–$10M | $25M–$45M | 4.5% | Very unlikely | 0.2% | Very unlikely |
| Series A | $10M–$20M | $50M–$100M | 7.4% | Unlikely | 0.3% | Very unlikely |
| Series A | $20M–$35M | $120M–$250M | 3.0% | Very unlikely | 0.1% | Very unlikely |
| Series B | $15M–$30M | $80M–$150M | 1.0% | Very unlikely | <0.1% | Very unlikely |
| Series B | $30M–$60M | $180M–$400M | 1.3% | Very unlikely | <0.1% | Very unlikely |
| Series B | $60M–$120M | $450M–$1B | 0.6% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $40M–$80M | $300M–$700M | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $80M–$150M | $700M–$1.5B | 0.3% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $150M–$300M | $1.5B–$4B | <0.1% | Very unlikely | <0.1% | Very unlikely |

## General assessment

BeeSafe is a three person Winter 2026 company building undercover AI agents that talk to scammers and turn the conversations into data and models, starting with banks fighting authorised push payment fraud. The need is real and growing, funding for AI security is strong, and a close YC analog was acquired for a reported 150 to 160 million. The risks are slow bank procurement, incumbents that bundle similar features, legal limits on engaging criminals, and a very small team. The most likely path is a seed round in 2026 followed by a hard Series A decision tied to paid bank contracts.

## Round by round: where and why it fails

### Getting into YC: 4.0%

**How we got the number.** Starting from the roughly 1 percent prior for a random applicant (range 0.6 to 2 percent, knowledge note in yc_acceptance.md). The company is already accepted, so this is a note: a sharp wedge in financial crime, an AI security tailwind and a small team with an unusual data approach would move it up, while no stated traction or named customers holds it down.

**Why it fails here.** YC would most plausibly say no because the pitch is a vision of a frontier model built on a dataset that does not yet exist, with no named customers, no revenue and a three person team, and because adversarial engagement with criminals has legal and safety questions that are hard to answer in a ten minute interview.

### Seed: P(reach this round | in YC) = 55% after the previous step; 55% cumulative if in YC; 2.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$1.5M | $8M–$15M | 25% | 14% | Unlikely | 0.6% | Very unlikely | Thin band: a small extension on top of the YC deal from angels or a security scout fund, common when a three person team has pilots but no signed bank contract. |
| $2M–$4M | $15M–$30M | 45% | 25% | Reasonable | 1.0% | Very unlikely | Core band: seed rounds for 2022 and later B2B companies in the benchmark table have a median near 3.4M. Alterya raised 9.8M seed in 2022 with intelligence unit founders, which sets the upper reference. |
| $4M–$8M | $30M–$60M | 30% | 16% | Unlikely | 0.7% | Very unlikely | Upside band: an unusual proprietary data story about scammers could attract a security focused lead, in line with the large 2025 to 2026 AI security seeds. |

**Why it fails here.** BeeSafe has three founders and a product that needs live conversations with criminals, which is hard to demo and slow to turn into a signed bank contract. Investors in early 2026 will ask for proof that banks pay for the data and that the agents scale without legal trouble, because engaging attackers raises entrapment and privacy questions. If pilots stay unpaid by month nine, the round shrinks to a small extension. Alterya raised a large seed because its founders came from intelligence units; a team without that signal needs revenue first.

### Series A: P(reach this round | in YC) = 27% after the previous step; 15% cumulative if in YC; 0.6% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $5M–$10M | $25M–$45M | 30% | 4.5% | Very unlikely | 0.2% | Very unlikely | Thin A: a few bank pilots, data licensing revenue not yet recurring. |
| $10M–$20M | $50M–$100M | 50% | 7.4% | Unlikely | 0.3% | Very unlikely | Core A: 2022+ B2B Series A median raise 13M (n=25) per base_rates.py. |
| $20M–$35M | $120M–$250M | 20% | 3.0% | Very unlikely | 0.1% | Very unlikely | Upside A: signed banks and a visible data asset, as with the hot AI security Series As. |

**Why it fails here.** Series A needs recurring revenue from banks or telecoms. Bank procurement for fraud tools runs six to twelve months and security reviews are long, so a three person team can miss the milestone before the seed money ends. Established fraud vendors such as Sardine and Unit21 can add scam intelligence features and bundle them. Inscribe reached Series A only after years of document fraud sales, and Smyte needed two years from seed to a four million dollar A, so slow conversion from pilots is the normal failure here.

### Series B: P(reach this round | in YC) = 20% after the previous step; 3.0% cumulative if in YC; 0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $80M–$150M | 35% | 1.0% | Very unlikely | <0.1% | Very unlikely | Modest Series B resting on bank contract revenue and a smaller dataset advantage than hoped. |
| $30M–$60M | $180M–$400M | 45% | 1.3% | Very unlikely | <0.1% | Very unlikely | Core B, 2022+ B2B median raise 45M but n=5. |
| $60M–$120M | $450M–$1B | 20% | 0.6% | Very unlikely | <0.1% | Very unlikely | Upside B if the dataset becomes a platform for telecoms and platforms. |

**Why it fails here.** Series B requires that the proprietary attacker dataset is both defensible and sold across more than one buyer type. The risk is that the data stays a niche input for a few banks and the foundation model claim does not produce measurably better detection than incumbents. Inscribe raised a B and then cut staff after missing revenue targets, which shows that fraud tooling Series Bs are tied to bank budgets. Without a second buyer such as telecoms or platforms, growth flattens.

### Series C+: P(reach this round | in YC) = 22% after the previous step; 0.7% cumulative if in YC; <0.1% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$80M | $300M–$700M | 45% | 0.3% | Very unlikely | <0.1% | Very unlikely | Typical later round for a security data company. |
| $80M–$150M | $700M–$1.5B | 40% | 0.3% | Very unlikely | <0.1% | Very unlikely | Scaled platform with enterprise and government sales across several buyer types. |
| $150M–$300M | $1.5B–$4B | 15% | <0.1% | Very unlikely | <0.1% | Very unlikely | Category leader outcome where the dataset becomes the standard feed for scam defense. |

**Why it fails here.** Reaching Series C needs a platform business across consumers, enterprises and governments, as the pitch says. Few YC fraud companies got there; Veriff did on identity verification demand, but most such companies end in acquisition, like Alterya to Chainalysis, Berbix to Socure and Smyte to Twitter. Acquirers will likely arrive before a C is needed, and regulation of adversarial engagement could cap the model.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 52% | Likely | 98% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 25% | Reasonable | 1.0% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 18% | Unlikely | 0.7% | Very unlikely |
| Acquired or IPO over $1B | $1B–$4B | 5.0% | Unlikely | 0.2% | Very unlikely |

**Why it fails here.** Most likely the company stalls because the data advantage does not translate into a better fraud signal than what banks already buy, and sales cycles outlast the cash. Analogs show that even good fraud companies mostly end as acquisitions. Alterya sold for about 150 to 160 million after two and a half years, Berbix sold for about 70 million, and Smyte was a talent acquisition, so a large independent outcome is rare.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Banks pilot but do not pay, so no recurring revenue appears before the seed runs out | 35% | Fraud buyers run long security reviews, and Inscribe and Next Caller both needed years between seed and A. | Inscribe (inscribe), Next Caller (next-caller) | Sell the data and mule network intelligence as a paid annual feed to two banks before building the model. |
| 2 | Incumbent fraud vendors ship scam intelligence and bundle it | 30% | Sardine, Unit21 and others already sell to the same banks and have distribution; competitors recorded for similar YC companies list them. | Variance (variance), Finic (finic) | Own a unique dataset that incumbents cannot buy, and partner rather than compete. |
| 3 | Team of three cannot build both the agents and the foundation model | 25% | The pitch needs voice, SMS and email agents plus model training; no founder background is stated in the input. | Finic (finic), Variance (variance) | Narrow to one channel and one fraud type first, such as mule account networks. |
| 4 | Legal and platform limits on engaging criminals and handling conversation data | 20% | Undercover engagement with live attackers across SMS and voice touches wiretap, privacy and terms of service rules that vary by country. | Smyte (smyte), Alterya (alterya) | Start with banks that own the channel and get legal sign off in a single jurisdiction. |

## Pros

- **Scam losses are large and rising and banks face reimbursement liability.**: UK APP fraud losses rose 12 percent in H1 2025 and banks now reimburse victims. (https://www.pymnts.com/fraud-prevention/2025/authorized-push-payment-fraud-losses-in-uk-rise-12/)
- **A closest YC analog exited at a strong price.**: Alterya sold to Chainalysis for a reported 150 to 160M two and a half years after its batch. (https://www.ycombinator.com/companies/alterya)

## Roadmap

### Reach Seed

Show two banks or payment firms paying for scam intelligence before the seed raise.

1. Run paid pilots on mule network detection with two design partner banks
2. Publish one case showing money recovered or accounts frozen from agent engagements

You know it worked when: Two signed paid pilots and a documented fraud loss prevented.

### Reach Series A

Recurring revenue from several banks plus a second buyer type.

1. Package the dataset as an annual feed and API
2. Add telecoms or a payments platform as a second customer segment
3. Complete SOC 2 and a legal review of engagement methods

You know it worked when: Annual recurring revenue of 1M or more across five or more paying customers.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 4 | 2 sourced evidence items |
| Technical complexity (5 = very hard) | 4 | Convincing multi turn conversational agents across voice, SMS and email, and then training models on the collected attacker dialogue, is hard and needs safety work. A three person team can ship a narrow single channel agent in three months, but a frontier model claim needs data volume that takes a year or more to gather. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | BeeSafe AI: A friendly name for a product that engages criminals is slightly off tone for bank buyers, but names rarely sink B2B security companies; Alterya and Smyte were also plain names. Brand is a minor factor here. |
| Takeover/copy risk (5 = very likely) | 3 | Could be built or absorbed by Sardine, Unit21, Chainalysis, large bank vendors such as BioCatch within ~18 months. Incumbents have distribution into banks and could build agent based scam engagement within a year or two, but the dataset of live attacker conversations is slow to copy, so risk is medium. Past cases such as Alterya show acquirers prefer buying this capability. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| Sardine and Unit21 (established fraud platforms) | Fraud and AML platforms sold to banks that could add scam intelligence. | Recorded as competitors of YC fraud companies in the repo data, no figures used. | https://www.takefive-stopfraud.org.uk/news/over-600-million-stolen-by-fraudsters-in-first-half-of-2025/ |
| Bank internal fraud teams and the status quo | Rules engines, transaction monitoring and manual investigation. | UK banks reimbursed most authorised push payment fraud under the 2024 regime, so they have a strong reason to spend. | https://www.pymnts.com/fraud-prevention/2025/authorized-push-payment-fraud-losses-in-uk-rise-12/ |
| Alterya (acquired by Chainalysis) | AI agents that find scam sites for banks and crypto firms. | Acquired in January 2025 for a reported 150 to 160M. | https://www.ycombinator.com/companies/alterya |

### Demand evidence

- UK authorised push payment fraud losses rose 12 percent in the first half of 2025 to about 257M pounds, and banks are now liable for reimbursing victims. (https://www.pymnts.com/fraud-prevention/2025/authorized-push-payment-fraud-losses-in-uk-rise-12/)
- Two thirds of UK authorised push payment fraud now originates online, outside the bank, which is where conversational intelligence would operate. (https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Alterya (alterya) | Summer 2022 | Acquired | Scam detection agents for banks and crypto firms, intelligence unit founders. | Seed 9.8M in 2022, acquired by Chainalysis in January 2025 for a reported 150 to 160M. |
| Smyte (smyte) | Winter 2015 | Acquired | Anti abuse and fraud tooling for platforms. | Seed 2.25M, Series A 4M, sold to Twitter in 2018 as a talent deal. |
| Inscribe (inscribe) | Summer 2018 | Active | AI fraud detection sold to banks and lenders. | Series A 10.5M in 2021, Series B 25M in 2023, then cut about 40 percent of staff in 2024. |
| Berbix (berbix) | Summer 2018 | Acquired | Fraud and identity verification, domain expert founders. | Series A 9M in 2020, sold to Socure in 2023 for about 70M. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 59% | 55% | python3 -I scripts/base_rates.py --calibration-only --years 2022-2025 --industry B2B: seed cond 59% known only (65% upper, n=126), series_a cond 26% (n=74), series_b cond 16% (n=19). Series C and later from --years 2019-2025 --tag AI: cond 25% (n=4, anecdote). | Our 0.55 is below the 0.59 anchor by about 7 percent; three person team with no disclosed revenue and a legally awkward product, offset by a strong category tailwind. |
| Series A | 26% | 27% | python3 -I scripts/base_rates.py --calibration-only --years 2022-2025 --industry B2B: seed cond 59% known only (65% upper, n=126), series_a cond 26% (n=74), series_b cond 16% (n=19). Series C and later from --years 2019-2025 --tag AI: cond 25% (n=4, anecdote). | 0.27 is near the 0.26 anchor; strong AI tailwind offset by long bank procurement. |
| Series B | 16% | 20% | python3 -I scripts/base_rates.py --calibration-only --years 2022-2025 --industry B2B: seed cond 59% known only (65% upper, n=126), series_a cond 26% (n=74), series_b cond 16% (n=19). Series C and later from --years 2019-2025 --tag AI: cond 25% (n=4, anecdote). | 0.20 against anchor 0.16; the dataset could be a real moat but this is untested. |
| Series C+ | 25% | 22% | python3 -I scripts/base_rates.py --calibration-only --years 2022-2025 --industry B2B: seed cond 59% known only (65% upper, n=126), series_a cond 26% (n=74), series_b cond 16% (n=19). Series C and later from --years 2019-2025 --tag AI: cond 25% (n=4, anecdote). | 0.22 against anchor 0.25 from a tiny sample; most comparable companies exit by acquisition first. |

## Assumptions and limits

- Blind forecast as of the batch start 2026-01-05, using only the input file and market searches.
- Seed here means a round above about 500K within about 12 months of the batch start.
- Base rate cohorts include few 2025 and 2026 batches, which are not yet resolved, so later stages are anchored on small samples.

## Sources

- https://www.pymnts.com/fraud-prevention/2025/authorized-push-payment-fraud-losses-in-uk-rise-12/
- https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds
- https://www.takefive-stopfraud.org.uk/news/over-600-million-stolen-by-fraudsters-in-first-half-of-2025/
- https://www.ycombinator.com/companies/alterya
