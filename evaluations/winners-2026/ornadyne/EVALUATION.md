# Evaluation: Ornadyne

*As of 2026-04-06. Mode: summary. We're building robot birds for surveillance.*

> These are calibrated judgments anchored on base rates from past YC companies, not statistical predictions. Read the anchors table and the assumptions before relying on any number.

## Verdict at a glance

**A high risk hard tech bet in a hot defense market; seed is plausible if a demo flies, the physics decides everything after.**

**Chance of getting into YC:** 10% (range 5.0%–15%), unlikely.

Labels use these cut-offs: Very likely ≥ 65%, Likely ≥ 45%, Reasonable ≥ 20%, Unlikely ≥ 5%, otherwise Very unlikely. "If in YC" assumes acceptance; "from today" multiplies by the YC odds and ignores funding paths outside YC.

| Stage | Raise | Post-money valuation | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|---|
| Seed | $600K–$2M | $8M–$16M | 20% | Unlikely | 2.0% | Very unlikely |
| Seed | $2M–$5M | $16M–$40M | 32% | Reasonable | 3.2% | Very unlikely |
| Seed | $5M–$12M | $40M–$90M | 13% | Unlikely | 1.3% | Very unlikely |
| Series A | $4M–$8M | $25M–$50M | 4.1% | Very unlikely | 0.4% | Very unlikely |
| Series A | $10M–$25M | $50M–$150M | 8.1% | Unlikely | 0.8% | Very unlikely |
| Series A | $25M–$80M | $150M–$400M | 4.1% | Very unlikely | 0.4% | Very unlikely |
| Series B | $15M–$30M | $70M–$150M | 1.7% | Very unlikely | 0.2% | Very unlikely |
| Series B | $30M–$70M | $150M–$450M | 2.8% | Very unlikely | 0.3% | Very unlikely |
| Series B | $70M–$200M | $450M–$1.5B | 1.1% | Very unlikely | 0.1% | Very unlikely |
| Series C+ | $40M–$100M | $300M–$800M | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $100M–$250M | $800M–$2.5B | 0.8% | Very unlikely | <0.1% | Very unlikely |
| Series C+ | $250M–$600M | $2.5B–$6B | 0.4% | Very unlikely | <0.1% | Very unlikely |

## General assessment

Ornadyne wants flapping wing drones that look like birds for close surveillance. Investors like defense and drones, so a seed is likely if the demo works. The physics is the real risk: flapping flight has missed practical endurance for decades. If it works it is a rare moat. Series A needs field trials and a customer, and defense revenue arrives slowly. The forecast treats the day one description as the best case, anchors on the 2022 to 2024 cohort of researched YC companies, and widens the uncertainty because funding data for recent batches is incomplete and right censored.

## Round by round: where and why it fails

### Getting into YC: 10%

**How we got the number.** Note only: already accepted to YC Spring 2026. Prior of about 1 percent for a random applicant is not informative, so the work is in the ladder.

**Why it fails here.** Not applicable because the company was accepted. A reviewer would most plausibly worry that flapping wing flight has failed to reach practical endurance for decades, and that the defense sales path is slow. Because acceptance is already a fact in this test, the estimate is a placeholder and the forecast value sits in the funding ladder that follows.

### Seed: P(reach this round | in YC) = 65% after the previous step; 65% cumulative if in YC; 6.5% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $600K–$2M | $8M–$16M | 30% | 20% | Unlikely | 2.0% | Very unlikely | Small round for a prototype and a first test campaign. |
| $2M–$5M | $16M–$40M | 50% | 32% | Reasonable | 3.2% | Very unlikely | Core: defense hardware seed, in line with Theseus 4.3M seed in 2025. |
| $5M–$12M | $40M–$90M | 20% | 13% | Unlikely | 1.3% | Very unlikely | Upside with a defense contract or strong demo video. |

**Why it fails here.** Seed stalls if the prototype cannot show stable flight with payload and endurance that beats a small quadcopter. Investors fund defense hardware but demand a demo; Icarus and similar hard tech peers show no confirmed round months after the batch. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series A: P(reach this round | in YC) = 25% after the previous step; 16% cumulative if in YC; 1.6% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $4M–$8M | $25M–$50M | 25% | 4.1% | Very unlikely | 0.4% | Very unlikely | Thin round for further R&D. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $10M–$25M | $50M–$150M | 50% | 8.1% | Unlikely | 0.8% | Very unlikely | Core: a defense hardware Series A. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $25M–$80M | $150M–$400M | 25% | 4.1% | Very unlikely | 0.4% | Very unlikely | Upside with a program of record or a government contract, as with Singularity whose Series A was 80M. |

**Why it fails here.** Series A fails if endurance, payload and noise do not clear field trials, or if no customer commits to a paid pilot. Hardware iteration is slow and capital hungry, and counter drone buyers prefer proven fixed wing platforms. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series B: P(reach this round | in YC) = 35% after the previous step; 5.7% cumulative if in YC; 0.6% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $15M–$30M | $70M–$150M | 30% | 1.7% | Very unlikely | 0.2% | Very unlikely | Modest round. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $30M–$70M | $150M–$450M | 50% | 2.8% | Very unlikely | 0.3% | Very unlikely | Core. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $70M–$200M | $450M–$1.5B | 20% | 1.1% | Very unlikely | 0.1% | Very unlikely | Upside with defense production orders. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Series B fails if production yield, supply chain and certification delay deliveries, or if defense contract timing slips for years. Government revenue arrives late and unevenly, which strains runway. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Series C+: P(reach this round | in YC) = 33% after the previous step; 1.9% cumulative if in YC; 0.2% from today

| Raise | Post-money | P of this band (given round reached) | P if in YC | Label | P from today | Label | Why this band |
|---|---|---|---|---|---|---|---|
| $40M–$100M | $300M–$800M | 40% | 0.8% | Very unlikely | <0.1% | Very unlikely | Growth round for production scale. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $100M–$250M | $800M–$2.5B | 40% | 0.8% | Very unlikely | <0.1% | Very unlikely | Core. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |
| $250M–$600M | $2.5B–$6B | 20% | 0.4% | Very unlikely | <0.1% | Very unlikely | Upside as a major defense supplier. Sized from 2022+ round medians in base_rates.py and current market benchmarks in stage_benchmarks.md. |

**Why it fails here.** Fails if larger defense primes or well funded drone makers capture the budget, or if the stealth advantage fades as counter systems improve, leaving a niche product. Investors at this step want proof that growth, retention and margins hold up against better funded rivals, and a weak showing on any of them ends the path here, as the analogs listed in this evaluation show.

### Final outcomes

| Outcome | Value | P if in YC | Label | P from today | Label |
|---|---|---|---|---|---|
| Shuts down or stalls | n/a | 55% | Likely | 96% | Very likely |
| Acquired or IPO under $100M | $5M–$100M | 20% | Reasonable | 2.0% | Very unlikely |
| Acquired or IPO $100M-$1B | $100M–$1B | 18% | Unlikely | 1.8% | Very unlikely |
| Acquired or IPO over $1B | $1B–$10B | 7.0% | Unlikely | 0.7% | Very unlikely |

**Why it fails here.** Most likely a stall because endurance and control for flapping flight are unsolved, or a modest acquisition of the technology by a defense firm. Success would be a large defense outcome if the physics works. A meaningful exit needs a durable lead in a category where rivals can copy features and raise more money, and most companies in the reference cohort stay small, are acquired cheaply or stop operating before that point.

## Why this company may not work: the killers

| # | Risk | P it happens | Evidence | Analog YC companies | Mitigation |
|---|---|---|---|---|---|
| 1 | Flapping wing flight does not reach useful endurance or payload | 45% | Prior programs such as AeroVironment Nano Hummingbird and Animal Dynamics Skeeter did not become fielded products. | Icarus (icarus), Unima (unima) | Show a measurable endurance and noise advantage early, with open test data. |
| 2 | Defense buyers move slowly and prefer incumbents | 30% | Defense procurement takes years and well funded drone makers dominate counter drone and ISR budgets. | Singularity (singularity), Rownd (rownd) | Pursue small SBIR style contracts and demo days with units. |
| 3 | Capital intensity outruns the funding | 25% | Hardware R&D with test flights and custom parts costs far more than software. | Theseus (theseus) | Stage the roadmap around cheap prototypes and non dilutive grants. |

## Pros

- **Defense and counter drone spending is high and rising.**: Counter UAS investment headlines and procurement marketplaces noted in market search. (https://dronelife.com/2020/09/13/researchers-develop-a-drone-that-flaps-its-wings-like-a-swift/)
- **A real thesis: quadcopters are detectable, birds are not.**: Governments have repeatedly funded bio inspired surveillance research. (https://www.theengineer.co.uk/articles/insect-inspiration-uk-defence-drone-mimics-dragonfly-flight)

## Roadmap

### Get into YC

Prove stable flight.

1. Publish a flight video with payload
2. Measure noise and detectability against quadcopters

You know it worked when: Ten minute endurance flight.

### Reach Seed

Raise above 500K in 12 months.

1. Win a small defense or university grant
2. Secure a letter of intent from a unit

You know it worked when: One paid pilot or grant.

### Reach Series A

Field ready system.

1. Complete field trials
2. Hire a defense business lead

You know it worked when: Repeatable mission performance and a funded contract.

## Scorecard

| Factor | Rating (1-5) | Notes |
|---|---|---|
| Market need today (5 = urgent, paid) | 3 | 1 sourced evidence items |
| Technical complexity (5 = very hard) | 5 | Flapping wing aerodynamics, lightweight actuation, control and endurance are open research problems. A four person team can build prototypes in three months but not a field ready system, so the hard part is a real moat only if it works. |
| Name and brand (5 = iconic, drives growth; effect on success: neutral) | 3 | Ornadyne: Defense hardware names are often invented or technical like Anduril or Singularity; the name will not decide outcomes and the aerodynamics will. |
| Takeover/copy risk (5 = very likely) | 2 | Could be built or absorbed by Defense primes, Well funded drone startups within ~36 months. If flapping flight works it is hard to copy quickly, and rivals have little reason to pursue it first; the larger risk is technical failure, not takeover. |

### Competition today

| Competitor | What they do | Traction | Source |
|---|---|---|---|
| AeroVironment and Animal Dynamics | Earlier funded flapping wing programs. | Government funded demos, no mass fielding. | https://www.theengineer.co.uk/articles/insect-inspiration-uk-defence-drone-mimics-dragonfly-flight |
| Small quadcopter makers and defense startups | Conventional drones used for ISR. | Large funded players. | https://dronelife.com/2020/09/13/researchers-develop-a-drone-that-flaps-its-wings-like-a-swift/ |
| UMD Morpheus Lab | University flapping wing research. | Academic flight tests. | https://aero.umd.edu/news/news_story.php?id=6806 |

### Demand evidence

- Governments fund flapping wing surveillance research, showing interest but not mass purchases. (https://www.theengineer.co.uk/articles/insect-inspiration-uk-defence-drone-mimics-dragonfly-flight)

## Evidence from past YC companies

| Company | Batch | Directory status | Why it is relevant | What happened |
|---|---|---|---|---|
| Theseus (theseus) | Summer 2024 | Active | Defense drone navigation, Summer 2024. | Raised a 4.3M seed in 2025 after hackathon traction. |
| Icarus (icarus) | Fall 2025 | Active | Stratospheric bird like aircraft for defense, Fall 2025. | Active with a factory hiring but no confirmed funding. |
| Singularity (singularity) | Summer 2023 | Active | Defense hardware from a propulsion engineer. | Stealth, then an 80M Series A in 2026. |
| Rownd (rownd) | Winter 2022 | Active | Pivoted to defense drones. | Seed of 2.2M, later a reported defense contract. |
| Unima (unima) | Winter 2016 | Inactive | Hard tech with long development, Winter 2016. | Shut down after about 2.6M raised. |

### Base-rate anchors

| Stage | Base-rate anchor | Our P(reach | previous) | Source | Adjustment |
|---|---|---|---|---|
| Seed | 68% | 65% | python3 -I scripts/base_rates.py --years 2018-2024 --industry Industrials --calibration-only (only 19 companies, anecdotal): seed cond 68% (n=19), series_a cond 31% (n=13), series_b cond 50% (n=4); broad 2022-2024 all: seed 59%, A 28%, B 12%; series_c all-year cond 36% (n=55) | 0.95x of the Industrials anchor. Defense and drone investor interest is high, but flapping flight is unproven and the team is four. |
| Series A | 31% | 25% | python3 -I scripts/base_rates.py --years 2018-2024 --industry Industrials --calibration-only (only 19 companies, anecdotal): seed cond 68% (n=19), series_a cond 31% (n=13), series_b cond 50% (n=4); broad 2022-2024 all: seed 59%, A 28%, B 12%; series_c all-year cond 36% (n=55) | 0.8x of the Industrials anchor, since few hardware teams hit a field ready product and flapping flight has a long history of failing. |
| Series B | 38% | 35% | python3 -I scripts/base_rates.py --years 2018-2024 --industry Industrials --calibration-only (only 19 companies, anecdotal): seed cond 68% (n=19), series_a cond 31% (n=13), series_b cond 50% (n=4); broad 2022-2024 all: seed 59%, A 28%, B 12%; series_c all-year cond 36% (n=55) | 0.9x of a blend between the Industrials anchor (50 percent, n=4) and the all cohort rate. |
| Series C+ | 36% | 33% | python3 -I scripts/base_rates.py --years 2018-2024 --industry Industrials --calibration-only (only 19 companies, anecdotal): seed cond 68% (n=19), series_a cond 31% (n=13), series_b cond 50% (n=4); broad 2022-2024 all: seed 59%, A 28%, B 12%; series_c all-year cond 36% (n=55) | Near the all stage anchor. |

## Assumptions and limits

- Pretend date is 2026-04-06 and only the input file describes the company.
- Seed means a round above about 500K within about 12 months of batch start.
- Industrials cohort has only 19 companies so the anchor is anecdotal.

## Sources

- https://www.theengineer.co.uk/articles/insect-inspiration-uk-defence-drone-mimics-dragonfly-flight
- https://dronelife.com/2020/09/13/researchers-develop-a-drone-that-flaps-its-wings-like-a-swift/
- https://aero.umd.edu/news/news_story.php?id=6806
