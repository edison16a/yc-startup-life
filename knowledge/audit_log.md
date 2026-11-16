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
