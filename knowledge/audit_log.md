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

## Wave 10 (rest shards, strict prompt with audit lessons), audit 5

Sample: 8 records (armory, metaplane, humi, embrace, gaiia, mono, kovi, pachama). One auditor. A field is one founder entry, one round, the exit or the competitor list; counts are approximate.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| armory | 9 | 3 | CEO and co-founder Daniel Odio omitted; exit amount (about $7M cash, TechCrunch 2024-01-11) left null; seed investor list unsupported. |
| metaplane | 8 | 2 | Founder employers and education omitted though TechCrunch states them; founding year conflict (2019 vs 2020) not noted. |
| humi | 7 | 2 | Co-CEO Simon Bourgeois omitted; exit price conflict (CAD 100M vs 155M) not noted. |
| embrace | 8 | 1 | Co-founder from a single article only (flagged in record). |
| gaiia | 8 | 2 | Prior employer for one founder inferred, not sourced; Series A dated 2024-06 where the source says May 2024. |
| mono | 8 | 2 | Pre-seed omitted; competitor list incomplete. |
| kovi | 8 | 1 | Competitor name misquoted (Movida vs Movia in the source). |
| pachama | 7 | 1 | About $9M of earlier funding not itemised as rounds. |

Totals: about 63 fields checked, 14 wrong or incomplete (22 percent), limit 10 percent. Result: wave NOT accepted. Down from 42 percent in audit 4 after the prompt change, but still over the limit. Remaining error types: co-founders and CEOs named in press but not on the YC page, early rounds not itemised, exit amounts left null when a source states them, and small date errors. AUDIT RESULT is not PASS.

## Waves 19 and 20 (strict prompt with audit lessons), audit 6

Sample: 16 records (nomi, brainbase-labs, norra, aminoanalytica, theora, bilanc, abel-police, conductor, cloudglue, splash-inc, wafer, paraquery, verbiflow, quotain, parrot, waffle), drawn at random from the 320 records written in these two waves. Two auditors, eight records each. A field is one founder entry, one round, the exit or the competitor list.

| Slug | Fields checked | Wrong | Notes |
|---|---|---|---|
| nomi | 4 | 1 | Co-founder Ethan Safar recorded as unconfirmed, but the launch post and Round Funded name him co-founder. |
| brainbase-labs | 3 | 0 | Matches the YC page. |
| norra | 4 | 0 | Matches. |
| aminoanalytica | 4 | 0 | Matches; aggregator-only funding correctly left unrecorded. |
| theora | 3 | 0 | Matches; the YC page lists one founder. |
| bilanc | 4 | 0 | Seed matches Nordic9. |
| abel-police | 4 | 2 | Competitor Policereports.ai omitted; AI Grant investor unsourced. |
| conductor | 5 | 1 | Matrix-led seed round omitted. |
| cloudglue | 3 | 1 | Competitor entry cites a figure the source page does not support. |
| splash-inc | 4 | 0 | Matches. |
| wafer | 6 | 2 | Seed of about 4M omitted; competitor list empty. |
| paraquery | 3 | 0 | Matches. |
| verbiflow | 4 | 1 | Competitor list empty in a crowded category. |
| quotain | 4 | 1 | Competitor list empty; former name Eden not mentioned. |
| parrot | 5 | 1 | Competitor list empty. |
| waffle | 4 | 1 | Competitor list empty although risk notes name CapCut and Opus Clip. |

Totals: 64 fields checked. Counting every empty or incomplete competitor list as wrong, 15 are wrong (23 percent). Counting only fields contradicted or shown missing by a named source, 6 are wrong (9.4 percent). The limit is 10 percent. Result: wave NOT accepted under the strict count, which is the standard used in audits 1 to 5. The lenient figure is recorded for transparency only and does not count toward a pass. Dominant error: competitor lists left empty because no source dated near the batch was found, plus a few omitted early rounds and co-founders. Action: the 8 records with wrong fields are being corrected, and the final audit must use the strict standard. AUDIT RESULT is not PASS.

## Waves 21 and 22 (strict prompt with audit lessons), audit 7

Sample: 16 records drawn at random from the 330 most recently written (domu-technology-inc, event-horizon-labs, ai-2, synsorybio, tandem-2, onegrep, kenley, deepsim-inc, diffusion-studio, humanlayer, integuru, general-learning, the-forecasting-company, healthspark, revyl, offstream). Two auditors, eight records each. Both auditors worked mostly from search results and could not open every page (several sources returned 403 or 404), so their counts are indicative.

| Slug | Fields checked | Wrong (strict) | Wrong (lenient) | Notes |
|---|---|---|---|---|
| domu-technology-inc | 5 | 1 | 0 | Rounds empty; company site claims a Series A and aggregators show a YC seed, neither confirmed by press. |
| event-horizon-labs | 4 | 1 | 0 | YC page lists no founder; search names Owen Colegrove. |
| ai-2 | 5 | 0 | 0 | Seed confirmed. |
| synsorybio | 5 | 1 | 0 | Pre-seed omitted. |
| tandem-2 | 6 | 1 | 0 | Pre-seed double counted inside the 6.1M seed. |
| onegrep | 5 | 1 | 0 | Rounds empty, sources conflict. |
| kenley | 5 | 0 | 0 | Matches. |
| deepsim-inc | 7 | 1 | 0 | Seed omitted although trade coverage reports it. |
| diffusion-studio | 4 | 1 | 0 | Competitor Remotion omitted. |
| humanlayer | 4 | 1 | 1 | Co-founder Kyle Mistele omitted; Factory announcement names him. |
| integuru | 3 | 1 | 0 | Investor roles omit ZhenFund. |
| general-learning | 5 | 1 | 0 | 3.4M seed omitted. |
| the-forecasting-company | 4 | 1 | 0 | 500K convertible note omitted. |
| healthspark | 3 | 1 | 0 | Co-founder Jonah Tuchow omitted. |
| revyl | 5 | 1 | 0 | Competitors QA Wolf and Waldo omitted. |
| offstream | 4 | 0 | 0 | Matches. |

Totals: 74 fields checked. Strict count (omitted rounds, co-founders and competitors that secondary sources support): 13 wrong (17.6 percent). Lenient count (only fields contradicted by a source): 1 wrong (1.4 percent). The limit is 10 percent. Result: wave NOT accepted under the strict count, which is the standard used in audits 1 to 6. Down from 23 percent in audit 6. The dominant pattern is caution: researchers leave out rounds and co-founders that only aggregators or one outlet support, and leave competitor lists empty. A decision is needed for the final audit: recording well supported aggregator rounds with a clear unverified label would cut the strict error rate without fabricating data. The 12 records with wrong fields are being corrected. AUDIT RESULT is not PASS.

## Waves 23 and 24 (strict prompt with audit lessons), audit 8

Sample: 16 records drawn at random from the 340 most recently written (diligent, letterbook, thunder-compute, vista-power, upsolve-ai, ncompass-technologies, velorum-therapeutics, unusual, aglide, alaan, moonset-health, fluid-markets, persist-ai, outset, adventris-pharmaceuticals, synnax). Two auditors, eight records each. Both auditors mostly opened YC pages and a few company posts and relied on search result summaries for the rest, so the counts are indicative.

| Slug | Fields checked | Wrong (strict) | Wrong (lenient) | Notes |
|---|---|---|---|---|
| diligent | 5 | 1 | 0 | Competitor ComplyAdvantage omitted. |
| letterbook | 5 | 2 | 0 | 2M seed omitted; competitor Intercom Fin omitted. |
| thunder-compute | 6 | 2 | 1 | Matrix-led 4.5M seed dismissed although the company blog states it; competitors omitted. |
| vista-power | 6 | 2 | 0 | Aggregator pre-seed and competitors omitted. |
| upsolve-ai | 4 | 1 | 0 | Competitors Cube and Explo omitted. |
| ncompass-technologies | 4 | 0 | 0 | Matches. |
| velorum-therapeutics | 4 | 0 | 0 | Matches; competitor date a few months after the batch. |
| unusual | 5 | 3 | 0 | Founder prior employers omitted, one title wrong, competitor Profound omitted. |
| aglide | 4 | 0 | 0 | Matches. |
| alaan | 7 | 0 | 0 | Matches. |
| moonset-health | 5 | 0 | 0 | Matches. |
| fluid-markets | 4 | 0 | 0 | Matches. |
| persist-ai | 6 | 1 | 0 | Seed investors incomplete. |
| outset | 7 | 0 | 0 | Matches. |
| adventris-pharmaceuticals | 5 | 1 | 0 | Scientific co-founder omitted. |
| synnax | 5 | 1 | 0 | Competitor LabVIEW omitted. |

Totals: 82 fields checked. Strict count: 14 wrong (17.1 percent). Lenient count: 1 wrong (1.2 percent). The limit is 10 percent. Result: wave NOT accepted under the strict count, which is the standard used in audits 1 to 7. The strict rate is stable at about 17 percent across audits 7 and 8. Almost all of it is empty competitor lists plus a few omitted rounds and co-founders. Competitor lists are the main lever: researchers leave them empty whenever no source dated near the batch is found, but auditors name dated competitors easily from launch posts and incumbent comparisons. Action: the records with wrong fields are being corrected and the research prompt will push researchers to name incumbents mentioned on the YC launch post. AUDIT RESULT is not PASS.

## Waves 25 and 26 (strict prompt with audit lessons and the new competitor lesson), audit 9

Sample: 16 records drawn at random from the 330 most recently written (scanbase, refine, express-building, avocademy, boya, agave, syncly, compup, inventive-ai, eazipay-inc, dr-treat, warp, flair-labs, credibook, rimward, roame). Two auditors, eight records each. Auditor A opened all 8 YC pages and several press and company posts; auditor B opened only 4 YC pages and worked from search results, so B's counts are soft.

| Slug | Fields checked | Wrong (strict) | Wrong (lenient) | Notes |
|---|---|---|---|---|
| scanbase | 5 | 1 | 0 | Seed exists, size disputed between aggregators. |
| refine | 7 | 2 | 0 | The company blog confirms a 1M seed (2022-06) and a 2.8M seed (2024-05); record has no rounds. |
| express-building | 4 | 0 | 0 | Matches. |
| avocademy | 5 | 2 | 0 | Seed reported by aggregators only; competitors undated. |
| boya | 5 | 1 | 0 | Convertible note on aggregators only. |
| agave | 8 | 3 | 0 | TechCrunch names a fourth founder and competitors Workato and Boomi; Series A investors unconfirmed. |
| syncly | 6 | 0 | 0 | Matches. |
| compup | 6 | 0 | 0 | Matches. |
| inventive-ai | 6 | 1 | 0 | Competitors empty. |
| eazipay-inc | 4 | 2 | 0 | Co-founders and a YC round on aggregators only. |
| dr-treat | 5 | 1 | 0 | Exit typed unknown although the YC page says acquired in 2025. |
| warp | 7 | 3 | 0 | Co-founder, 2023 seed and competitors omitted. |
| flair-labs | 7 | 2 | 0 | Third co-founder and an aggregator pre-seed omitted. |
| credibook | 7 | 1 | 1 | Series A dated 2022-03, sources say 2022-04-05. |
| rimward | 3 | 0 | 0 | Matches. |
| roame | 5 | 2 | 0 | Aggregator round omitted; competitor funding_then leaks a later round. |

Totals: 90 fields checked. Strict count (anything an auditor could find that is missing, including aggregator-only rounds and unsourced competitors): 21 wrong (23.3 percent). Lenient count (only fields contradicted by a source the auditor opened): 1 wrong (1.1 percent). A middle count, adding omissions confirmed by a non-aggregator source (Refine's blog rounds, Agave's TechCrunch founder and competitors, Dr Treat's acquisition, Roame's look-ahead leak), is roughly 8 fields, about 9 percent; this middle count is approximate because it was assembled by hand. The limit is 10 percent.

Note on the standard: the strict count penalizes the repo's own no-fabrication rule, because aggregator-only rounds are deliberately kept in notes as unverified. The extractor skill asks auditors to check recorded founders, rounds, exits and competitor dates, which is closest to the middle count. For the final audit (Stage 5) I will report all three counts side by side and will only write the PASS line if the middle count is at or below 10 percent on a fresh sample, with the lenient and strict figures shown next to it. Result of this audit: not accepted as PASS-eligible because the sample was not a final audit. AUDIT RESULT is not PASS.

## Waves 27 and 28 (strict prompt with the competitor and co-founder lessons), audit 10

Sample: 16 records drawn at random from the 330 most recently written (kamion, alokai, savein, seaflight-technologies, palitronica-inc, numida, inferedge, vendoo, digi, ahazou, hype, hypestream, kapital-bank, sota2, julius, haddock). Two auditors. Both opened only a handful of pages and worked from search results for the rest, so the middle and lenient counts are lower bounds. This time each auditor reported three counts: strict (anything findable and missing, including aggregator-only rounds and empty competitor lists), middle (recorded items that are wrong or unsourced, plus omissions confirmed by a non-aggregator source the auditor opened) and lenient (only fields contradicted by an opened source).

| Slug | Fields checked | Strict | Middle | Lenient | Notes |
|---|---|---|---|---|---|
| kamion | 5 | 1 | 1 | 0 | Parade Dergi (opened) reports a YC investment of 8.5M TL in July 2022 that the record omits. |
| alokai | 8 | 2 | 1 | 0 | 20M round labelled series_a but the company post gives no stage; lead investors omitted; competitors empty. |
| savein | 9 | 2 | 1 | 0 | Inc42 (opened) reports a 3M tranche in July 2022. |
| seaflight-technologies | 7 | 2 | 0 | 0 | Competitors empty; aggregator rounds. |
| palitronica-inc | 6 | 2 | 0 | 0 | Competitors empty; aggregator seed. |
| numida | 9 | 3 | 0 | 0 | Competitor as_of does not match the batch; aggregator raise. |
| inferedge | 5 | 1 | 0 | 0 | Aggregator seed. |
| vendoo | 7 | 2 | 0 | 0 | Undated round; aggregator rounds. |
| digi | 4 | 2 | 0 | 0 | Aggregator seed; competitors empty. |
| ahazou | 3 | 1 | 0 | 0 | Aggregator seed. |
| hype | 3 | 2 | 0 | 0 | Aggregator seed; competitors empty. |
| hypestream | 3 | 1 | 0 | 0 | Competitors empty. |
| kapital-bank | 9 | 6 | 3 | 1 | Foley notice (opened) labels the July 2022 30M round Series A with more investors; May 2023 Series A amount missing (LatamList, opened, says 20M); competitors undated. |
| sota2 | 4 | 1 | 0 | 0 | Aggregator seed; founders unconfirmed. |
| julius | 4 | 3 | 2 | 0 | AI Grant omitted from the seed (TechCrunch, opened); competitor dated after the as_of. |
| haddock | 5 | 4 | 1 | 0 | Seed investors incomplete; undated competitors. |

Totals: 91 fields checked. Strict: 35 wrong (38.5 percent). Middle: 9 wrong (9.9 percent). Lenient: 1 wrong (1.1 percent). The limit is 10 percent. The middle count is just under the limit and is a lower bound, so this is not evidence of a pass. Errors cluster in older companies with real funding history (Kapital Bank, Julius, Haddock, SaveIN, Kamion): the researcher found a seed but missed later rounds, stages and extra investors. Action: the records with middle errors are being corrected. AUDIT RESULT is not PASS.

## Waves 29 and 30, audit 11

Sample: 16 records drawn at random from the 330 most recently written (palla, fintoc, kaya, velt, parallel-bio, coderhouse, echoes-hq, hubuc, medium-biosciences, meru-com, infracost, coloop, dailybot, jabu, upbanx, kaipod-learning). Two auditors who opened more cited pages than in earlier audits (about 10 each). Three counts as in audit 10.

| Slug | Fields checked | Strict | Middle | Lenient | Notes |
|---|---|---|---|---|---|
| palla | 5 | 2 | 1 | 0 | Third co-founder (CTO) listed on the Cowboy Ventures page is missing. |
| fintoc | 5 | 2 | 2 | 0 | 3M seed (LatamList, opened) missing; only competitor sourced to 2024 against an as_of of 2021-03. |
| kaya | 4 | 1 | 0 | 0 | Aggregator note only. |
| velt | 4 | 2 | 0 | 0 | Aggregator co-founder and possible earlier round. |
| parallel-bio | 6 | 2 | 0 | 0 | Aggregator round; competitor sourced to a blog title. |
| coderhouse | 5 | 4 | 2 | 0 | Co-founder named on the company story page missing; competitors undated. |
| echoes-hq | 3 | 1 | 0 | 0 | Aggregator round. |
| hubuc | 6 | 3 | 2 | 0 | Pre-seed amount of 350K euros stated by the cited source left null; undated competitors. |
| medium-biosciences | 4 | 2 | 0 | 0 | Aggregator seed; competitors empty. |
| meru-com | 8 | 2 | 2 | 0 | TechCrunch's total raised implies an earlier round; competitors undated. |
| infracost | 7 | 1 | 0 | 0 | Competitor list possibly incomplete. |
| coloop | 5 | 3 | 2 | 0 | Research-Live calls it Pre-Series A and gives totals implying an earlier round; competitors empty. |
| dailybot | 4 | 2 | 0 | 0 | Aggregator note; competitors empty. |
| jabu | 5 | 2 | 1 | 0 | Series A investors incomplete; date; competitor dated after as_of. |
| upbanx | 6 | 1 | 1 | 0 | Competitor dated after as_of. |
| kaipod-learning | 4 | 2 | 1 | 0 | Aggregator pre-seed; undated competitor. |

Totals: 81 fields checked. Strict: 32 wrong (39.5 percent). Middle: 14 wrong (17.3 percent). Lenient: 0 wrong (0 percent). The limit is 10 percent. Result: not accepted. The middle rate rose from about 10 percent in audit 10 to 17 percent, partly because these auditors opened more pages. The dominant defects are the same: a round or co-founder that a cited article states directly but the researcher left out or left blank (amount, investors, stage), and competitors whose sources are dated after the as_of. Action: the research prompt gets two more lessons (use the cited article's own total raised and investor list to find missing rounds; read the company story page for co-founders), the flagged records are corrected, and a completeness correction pass over earlier records is required before the final audit. AUDIT RESULT is not PASS.

## Waves 31 and 32, audit 12

Sample: 16 records drawn at random from the 330 most recently written (stipop, awtomic, treinta, studystream, siglo, text-blaze, kodex, rootly, zensors-inc, titipku, daedalus, synder, kodo, medpiper-technologies-inc, recall-ai, modernbanc). This is the first audit of records written after the researcher prompt gained lessons 7 to 9 (use cited articles' totals to find missing rounds, read company story pages for co-founders, date competitor sources near the batch). Two auditors opened about 10 pages each. Three counts as before.

| Slug | Fields checked | Strict | Middle | Lenient | Notes |
|---|---|---|---|---|---|
| stipop | 4 | 3 | 1 | 0 | Rounds empty; competitor sourced to an undated page. |
| awtomic | 3 | 4 | 3 | 0 | Two co-founders named on the company about page (opened) missing; competitor source dated after as_of. |
| treinta | 7 | 5 | 2 | 0 | Forbes Colombia (opened) calls the 14.3M round seed with named investors; Series A investors incomplete. |
| studystream | 6 | 2 | 0 | 0 | Aggregator rounds and competitors. |
| siglo | 4 | 2 | 0 | 0 | Aggregator seed; competitors empty. |
| text-blaze | 5 | 2 | 0 | 0 | Aggregator pre-seed; competitors empty. |
| kodex | 5 | 2 | 1 | 0 | Company blog says total raised 12M, implying about 2M earlier unrecorded. |
| rootly | 6 | 2 | 1 | 0 | Competitor citation does not support PagerDuty. |
| zensors-inc | 3 | 3 | 0 | 0 | Aggregator co-founder and seed. |
| titipku | 5 | 2 | 0 | 0 | Aggregator deal. |
| daedalus | 5 | 3 | 0 | 0 | Founder via unopened page; aggregator pre-seed. |
| synder | 6 | 2 | 0 | 0 | Aggregator seed. |
| kodo | 4 | 2 | 0 | 0 | Co-founder via search summaries. |
| medpiper-technologies-inc | 5 | 2 | 0 | 0 | Aggregator seeds. |
| recall-ai | 7 | 1 | 1 | 0 | Seed investors named in the company post missing; seed source_url wrong. |
| modernbanc | 4 | 2 | 0 | 0 | Aggregator seed. |

Totals: 79 fields checked. Strict: 39 wrong (49.4 percent). Middle: 9 wrong (11.4 percent). Lenient: 0 wrong (0 percent). The limit is 10 percent. Middle fell from 17.3 percent (audit 11) to 11.4 percent, still above the limit. The two auditors differed sharply (middle 8 of 40 versus 1 of 39), which shows the count depends on which pages an auditor opens. Remaining middle defects are real: co-founders on the company's own page, seed investors and stage taken from a cited article, totals that imply a missed round. Action: correct the flagged records. The final audit will use at least 25 records and a middle-style count with the auditors told to open the company's own pages and cited articles. AUDIT RESULT is not PASS.

## Audit 13 (records from waves 33 to 35)

Two independent auditors, 8 records each: pronto, valo, gen1e-lifesciences, pulse-active-stations-network, medpiper-technologies-inc, upflow, rct-studio, supertokens, keynua, treinta, corvus-robotics, excepgen, embeddables, taali-inc, signadot, circumvent.

Batch A: 55 fields, strict 13, middle 6, lenient 1. Batch B: 46 fields, strict 19, middle 7, lenient 2.

Totals: 101 fields checked. Strict: 32 wrong (31.7 percent). Middle: 13 wrong (12.9 percent). Lenient: 3 wrong (3.0 percent). The limit is 10 percent. Middle rose slightly from 11.4 percent (audit 12). Defects are mostly incomplete round lists (YC investment and seed rounds known only from aggregators or cited totals), one cumulative amount counted twice (corvus-robotics), one missed co-founder (upflow), inferred investors (rct-studio) and competitors not dated to the founding (embeddables, medpiper). Action: correct the flagged records. AUDIT RESULT is not PASS.
