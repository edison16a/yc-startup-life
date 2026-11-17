# Audit log

Independent auditors re-open the cited sources and check founders, every funding round, the exit, competitor dates and branding claims. Researchers' work is not shown to them. The final line `AUDIT RESULT: PASS` is written only after the Stage 5 final audit.

## Wave 1 (calibration shards 1 to 8), audit 1

Sample: 9 records from shards 2, 3, 4, 5, 7 (reducto, botcity, wit-ai, blockspring, stacker, coval, pardes-bio, zip-phone, tenjin). Three auditors.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| reducto | 22 | 1 | founders[].education was empty; the YC page says MIT, CS. Fixed. |
| botcity | 25 | 0 | The Series A label comes only from the YC page. |
| wit-ai | 22 | 1 | outcome_analysis said founded October 2013; the record's own notes say April 2013. Fixed. |
| blockspring | 16 | 0 | Acquirer, date and seed confirmed. |
| stacker | 24 | 0 | A founder's education could not be confirmed. |
| coval | 20 | 0 | Seed investor list incomplete, not wrong. |
| pardes-bio | 11 | 0 | Exit amount (about $130M) was missing; added. Series A month conflicts between sources (Jan or Feb 2021). |
| zip-phone | 7 | 0 | The acquihire factor is flagged in the record as an inference. |
| tenjin | 10 | 0 | Exit type "acquisition" was unsupported (no acquirer or date, site still active); changed to unknown. Possible missing third founder, unconfirmed. |

Totals: 157 fields checked, 2 wrong (1.3%), limit 10%. Result: wave accepted. Also fixed after audit: pardes-bio exit amount, tenjin exit type.

What the audit says about the data: the numbers that were recorded were right, but records leave things out (investor lists, education, competitors), and many fields could not be verified at all (14 of 157 in batches B and C alone). Treat sparse fields as sparse, not as zero.

## Wave 1 (calibration shards 1 to 20, second queue numbering), audit 2

Sample: 12 records from shards 2, 3, 6, 9, 10, 19, 20 (weav, gigster, airbyte, posthog, zapier, thunkable, mineralsoft, laika, prodigal, craftwork, porter, mocha). Two auditors. Fields checked are approximate counts, because auditors reported by item.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| weav | 7 | 1 | Plaid is an analogy in a 2021-04 article, not a dated competitor at founding. Exit unverified (403). |
| gigster | 8 | 3 | Seed of $2.5M (2015-07, TechCrunch) missing; Series B lead (Redpoint) missing; Upwork competitor weakly supported. |
| airbyte | 7 | 3 | Series A $26M (2021-05) and seed missing; Stitch competitor not supported by its source. |
| posthog | 10 | 3 | Series A amount and date inconsistent ($12M 2020-12 vs $9M 2020-07); Series B has no sourced amount or date. |
| zapier | 8 | 2 | Seed $1.2M vs $1.3M conflict needs a note; co-founders not supported by cited sources. |
| thunkable | 5 | 1 | Series B lead (Owl Ventures) missing; earlier rounds missing. |
| mineralsoft | 6 | 0 | Competitor list empty, nothing to check. |
| laika | 7 | 1 | Seed date should be 2020-07. |
| prodigal | 6 | 2 | Third co-founder Saransh Garg (left 2019) missing; Raje role should be CTO. |
| craftwork | 5 | 1 | Co-founders beyond Tim Griffin possibly missing (unconfirmed). |
| porter | 6 | 1 | Unsourced claim that Heroku was owned by Salesforce. |
| mocha | 5 | 1 | Seed (2023-09, YC and Soma, amount null) missing. |

Totals: about 80 fields checked, 19 wrong (about 24%), limit 10%. Result: wave NOT accepted. Most errors are omissions (missing rounds, founders, investor leads) and weakly sourced competitors, not wrong amounts. Action: shards 2, 3, 6, 9, 10, 19 and 20 are queued for a correction pass with the strict prompt; the 12 audited records are corrected from these findings. Cause: researchers used 4 to 6 calls per company and shared searches across requirements.
