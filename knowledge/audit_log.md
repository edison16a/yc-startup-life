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

## Wave 2 (calibration shards, strict prompt), audit 3

Sample: 10 records from 10 different shards (papa, flexport, wanderlog, candid-health, trella, imgix, jenfi, coub, daily, wibond). Two auditors. Fields checked are approximate counts.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| papa | 12 | 0 | Series D unverified (403). Competitor sourcing weak. |
| flexport | 6 | 2 | 2022 round is dated 2022-02-07 and labelled Series E; investors Shopify, DST, Founders Fund missing; pre-2019 rounds omitted. |
| wanderlog | 5 | 0 | Founder surname ambiguous in the source. |
| candid-health | 8 | 1 | Co-founder Adam Reis and Series B investors rest on aggregators; seed and Series A omitted. |
| trella | 8 | 1 | 2022 DFC debt facility and bridge round omitted. |
| imgix | 6 | 1 | Series A extension (2016) omitted. |
| jenfi | 8 | 1 | 2023 round is labelled pre-Series B by a source; $25M debt round omitted. |
| coub | 7 | 1 | Possible third co-founder omitted; competitor source dead link. |
| daily | 8 | 2 | Seed month 2016-08 unsupported (year only); Series B lead Renegade omitted. |
| wibond | 6 | 1 | Co-founder conflict (Porta vs Silvestre) between low-quality sources. |

Totals: about 74 fields checked, 11 wrong (about 15%), limit 10%. Result: wave NOT accepted. Improved from audit 2 (24%) after the strict prompt, but errors are still mostly omitted rounds and investor leads. The 10 audited records are corrected from these findings. Records from before the strict prompt (wave 1) and this wave need a further correction pass focused on completeness of funding rounds before the final audit.

## Wave 5 (rest shards, priority tier public or top), audit 4

Sample: 12 records (stripe, dropbox, brex, faire, groww, algolia, retool, langfuse, helicone, flowiseai, honeylove, twitch). Two auditors. Fields checked are approximate counts of items the auditors examined.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| stripe | 8 | 3 | Founder education uncited (general knowledge); competitor source dates 2013 vs 2009 founding; seed date conflict. Series B and C omitted. |
| dropbox | 7 | 3 | Founder education uncited; Accel unconfirmed in Series A; Series B investor list unclear. |
| brex | 8 | 4 | Founders both listed CEO; education and prior exit uncited; exit close confirmed 2026-04-07 but recorded unconfirmed; early rounds omitted. |
| faire | 9 | 5 | Fourth founder missing; no education; wrong round date and valuation for 2022; Series A, G and earlier rounds omitted. |
| groww | 9 | 4 | Education empty; Series A ($6.2M, Sequoia India, 2019-01) and earlier rounds omitted; competitor dates late. |
| algolia | 7 | 4 | Prior employer Exalead omitted; seed omitted; pivot unsourced; round dates year only. |
| retool | 7 | 2 | Series A and B omitted though the company blog confirms the Sequoia led Series B; Oxford education uncited. |
| langfuse | 5 | 1 | Exit date conflict (2026-01 vs 2026-07 on source). |
| helicone | 5 | 2 | Education incomplete; Gottdank co-founder status unverified from YC page. |
| flowiseai | 4 | 1 | Workday director note unsourced. |
| honeylove | 5 | 1 | Seed omitted although Seedtable and Caplight support it. |
| twitch | 7 | 4 | Seibel listed as co-founder without YC support; Kan education uncited; Series C omitted; exit source weak. |

Totals: about 81 fields checked, about 34 wrong (about 42 percent), limit 10 percent. Result: wave NOT accepted. The error pattern is systematic: (1) founder education and prior employers filled from general knowledge without a source, (2) real, documented funding rounds left in notes as unverified when a primary source exists, (3) competitor entries whose source is dated years after founding. Action: the research prompt now forbids uncited education, requires recording rounds that a company blog or press release confirms, and forbids unstated stage labels. The 12 audited records are corrected. All depth 2 records written before this prompt change (every record in data/enrichment so far) still carry these defects at an unmeasured rate and need a completeness correction pass before the final audit can pass. AUDIT RESULT is therefore not PASS.
