# Failure modes

Sources: failure_factor_counts.csv (factors among the 115 researched shutdowns in the calibration sample, n=115), time_to_milestones.csv, factor_outcomes.csv, data/enrichment records, and the cited advice notes. A shutdown can carry several factors, so shares do not sum to 100 percent. Factors were assigned by the research agent from public sources, so they are interpretations. Only 25 of the 115 shutdowns have a dated shutdown, so timing is thin.

## Biases
Survivorship and visibility: small failures vanish quietly and may be marked Active or recorded with unknown dates. Some shutdown dates are inferred from a website going dark. Recent batches have unresolved outcomes, so recent failures are undercounted and the typical time to shutdown is biased by who has had time to fail. Missing funding is not zero: "could not raise next round" is inferred from absent funding data, and 299 of 662 records found no funding data at all, so this factor may be over or under stated. Failory counts about 20 percent inactive over 2,200 companies and 40 percent in the first 17 batches (note failory-yc-failures); this repo's directory shows 17 percent inactive overall (n=6399) and 45 percent in 2005-2012 (n=460), so the repo figures override.

## Timing
Months from batch start to shutdown across the calibration sample: p25 24.5, median 42, p75 52 (n=25). By era: 2005-2012 median 22 (n=8), 2013-2017 median 43 (n=5), 2018-2021 median 49 (n=9). The early eras include faster dot-com style burns, and the later era is right censored. Typical companies die about three and a half years after batch start, which is usually after the seed money is spent and one round fails to come.

## Failure factors
Counts are from the table, shares are of 115 shutdowns. Median months are my own tally from batch start to exit date within the researched shutdowns and use small n, so treat them as rough.

1. Could not raise the next round, n=13 (11 percent). Median about 48 months (n=10). Warning signs: seed raised more than 18 months ago with no growth story, revenue flat for two quarters, investors asking for traction you do not have. Examples: alphaflow, cakework, call9, carwoo, codestory.
2. Competition won, n=10 (9 percent). Median about 38 months (n=5). Warning signs: a rival with a better channel, price cuts, losing deals in every recurring segment. Examples: cakework, carwoo, controlhub, dittofeed, bud.
3. Unit economics, n=7 (6 percent). Median about 49 months (n=7). Warning signs: gross margin below what support or delivery costs, acquisition cost that exceeds lifetime value, subsidized growth. Examples: call9, envkey, grouper, mocha, multiverse.
4. Pivot failed, n=5 (4 percent). Warning signs: second or third pivot with no earlier signal, team shrinking. Examples: mango-health, pre, patterns, justspotted.
5. Distribution failed, n=4 (3 percent). Median about 29 months (n=4). Warning signs: all growth from one paid channel or one launch spike, no repeat usage. Examples: mocha, newslabs, notifo, queenly.
6. Incumbent copied, n=4 (3 percent). The single case with a date went at about 20 months. Warning signs: a large incumbent ships the feature free or announces a rival. Examples: awesometalk, codestory, hoverchat, appcanary.
7. Weak willingness to pay, n=3. Examples: dittofeed, lotus, tipjoy, mattermark.
8. Market too small, n=3. Examples: multiverse, tipjoy, voodoo-manufacturing.
9. Ran out of money, n=3. Examples: lotus, moxion-power-co, queenly.
10. Acquihire soft landing, n=2, scaling failed, n=2, macro downturn, n=2, other, n=3. Examples: cribspot, ivella, grouper, alphaflow.
11. Single cases, n=1 each: fraud or legal (mixwit, about 11 months), platform dependency (mixwit), tech unsolved, market timing late (taste).

The tagged factor counts sum to 67 across 115 shutdowns, and some shutdowns carry several factors, so some shutdowns have few or no tags, usually because public information was thin. Do not read the factor shares as a full causal split.

## Structural predictors from factor_outcomes.csv
Defensibility 1 (n=98): 50 percent shut down, versus 14 percent at rating 2 (n=395) and 5 percent at rating 3 (n=149). Consumer companies are 35 percent Inactive (n=892) versus 15 percent for B2B (n=3250). Marketplaces (n=14) shut down 43 percent, free models (n=14) 43 percent, hardware (n=18) 28 percent. Non-technical founding teams (n=174) shut down 28 percent versus 14 percent with a technical founder (n=488). Counts by business model have many label variants, so only groups with n of 14 or more are quoted.

## Warning signs summary
Seed money gone with no growth rate to show. A consumer or marketplace model with no repeat behavior. Growth that disappears when ad spend stops. A rival or platform that copies the feature. Costs per customer that do not fall with scale. Founders talking about the third pivot. Graham's list of mistakes (note p1-pg-18-mistakes) overlaps: co-founder conflict, slow launch, and losing focus.
