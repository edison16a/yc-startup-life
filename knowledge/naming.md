# Naming and brand: what the data shows

Built on 2026-11-17 from knowledge/tables/name_outcomes.csv (name features for the whole directory, n about 6,398), the branding block of the 614 researched records in data/enrichment that have one (of 662 researched), data/name_features.csv, and the advice notes. The short version: names matter much less than the industry and era a company sits in, and the data cannot separate the two.

## Name features versus outcomes

name_outcomes.csv reports alive percent (not shut down), exit percent (acquired or public) and top company percent by feature and era. The status field is the YC directory status, so this table covers all companies, not only researched ones. Status is a noisy label: Inactive means YC lists it as closed.

Across all eras, kind of name: invented or proper noun n=3,604 alive 82.3 percent exit 14.1; compound words n=1,212 alive 80.9 exit 14.0; name plus descriptor n=896 alive 86.4 exit 8.7; real word n=395 alive 83.8 exit 18.2 top 6.8; suffix coinage n=288 alive 81.9 exit 12.8. Length buckets show no gradient: 5 to 6 characters n=1,724 alive 84.6 exit 13.2, 12 or more n=876 alive 82.3 exit 9.7. Words: one word n=4,022 exit 14.3, two words n=2,123 exit 12.9, three words n=201 exit 6.5. Digits (n=86), hyphens or dots (n=93), camel case (n=918) show no clear effect.

These pooled numbers mislead because the era mix differs by feature. The name plus descriptor kind is concentrated in recent batches (n=557 of 896 in 2022+), where 93 to 95 percent are alive and almost none have had time to exit. Within eras the picture is flatter. In 2005-2012, real words look best: n=42 alive 76.2 percent exit 52.4 top 38.1, against invented n=263 alive 52.1 exit 39.2 top 4.2. That is 16 top companies in 42 and the interval is wide. In 2013-2017 real word n=68 alive 76.5 exit 27.9 top 14.7 versus invented n=468 alive 66.9 exit 31.4 top 3.6. In 2018-2021 real word n=115 alive 74.8 exit 14.8 top 0.9 and invented n=1,047 alive 78.6 exit 17.1. The real word advantage in top company rate is consistent in the oldest two eras and vanishes later, which fits survivorship: a few giants (the known real word names) carry the cell. Short names of 4 characters or fewer had exit 34.1 percent in 2013-2017 (n=85) versus 20.7 for 12 or more (n=145), but in 2018-2021 the gap reverses on alive (72.9 versus 77.9) and exit is 17.5 versus 13.2. Two segments stand out and both are small: hyphen or dot names in 2018-2021 are alive only 56.7 percent (n=30, interval 39 to 73), and the suffix ox is alive 54.5 percent (n=22).

Era rows in 2022+ show alive 91 to 97 percent in every cell and exit near 4 to 5 percent. These are unresolved cohorts, not evidence about names.

## Brand records from the researched sample

Of 614 researched records with branding, name_type counts are real word 182, compound 199, invented 129, suffix coinage 29, descriptive 35, person or place 21, acronym 4, other 15. Researchers marked brand effect on outcome as unclear for 561, neutral 38, helped 14 and hurt 1. So the judgment of a brand effect exists for under 9 percent of the records and mostly says no clear effect.

Brand strength (1 to 5, rated at the brand's peak from sources) tracks status strongly, and this is partly circular. Strength 1: n=119, 56 Inactive (47 percent). Strength 2: n=352, 45 Inactive (13 percent). Strength 3: n=104, 6 Inactive (6 percent). Strength 4: n=11, 1 Inactive. The rating needs press and community evidence, which dead companies leave less of, so the rating partly measures survival. Do not read it as the brand causing survival.

Name problems flagged: confusable 269 (57 Inactive, 21 percent), generic 245 (46 Inactive, 19 percent), hard to spell 75 (15 Inactive, 20 percent), outgrown by pivot 49 (8 Inactive, 16 percent). The base Inactive share among branded records is 114 of 614 (19 percent). So none of these flags moved shutdown rate by more than a few points. Features that are described as qualities (easy to say 431, short 383, distinctive 232, evocative 245) are too common to discriminate.

Domains: I classified the free text domain_note by whether it mentions a .com or only another suffix (a regex on the note, so approximate). Notes mentioning a .com n=346, Inactive 71 (21 percent); only a non .com suffix such as .io, .ai, .so n=93, Inactive 10 (11 percent); no domain note n=206, Inactive 40 (19 percent). Non .com names are mostly recent companies, so this comparison is dominated by era and says nothing against Paul Graham's advice.

## Best and worst brand cases

Helped (researcher verdict plus sources): popl (strength 4, TikTok led launch, https://f2f.substack.com/p/startup-spotlight-18-popl); papa (names Papa and Pals made the offer instantly understandable, https://www.papa.com); lineleap (name states the benefit, campus ambassadors, https://wildcat.arizona.edu/99425/arts/lineleap-the-disney-fast-pass-but-for-bars/); buildspace (founder voice and community, status Inactive, https://buildspace.so/); our-world-in-data (recognised web brand, logo on every reused chart); unsloth-ai (sloth mascot against a speed product); submittable (fixing the name early, https://discover.submittable.com/blog/a-new-name-a-new-chapter); clever (friendly name and the Badge); labdoor (known tester brand despite a retracted 2015 test).

Strong but causal role unproven (rated unclear): doordash (short, deliberate name, renamed from Palo Alto Delivery in 2013-06 when it scaled beyond one city, https://medium.com/@DoorDash/the-new-doordash-logo-76bc2335a02c); zapier (the term Zap built into the name, own rebrand case study, https://zapier.com/blog/zapier-rebrand-case-study/); posthog (hedgehog mascot and tone, https://posthog.com/blog/drawing-hedgehogs); wefunder.

Hurt or weak: spring-in-africa (three name changes in five years, the name now reads like an investment firm, https://techcabal.com/2023/10/19/wallet-africa-introduces-spring-a-multi-currency-wallet/). Collisions and confusion: paradev (original name collided with Apache Superset, rebranded), 222 (a numeric name is hard to search but earned wide press), lunatic (negative connotation, non .com domain, Inactive), memamp (unclear meaning, domain now parked for sale, Inactive), godhands (negative connotation). Hard to pronounce names: zoios, dydema, sentiyen, poth-labs, with mostly Active status, so even these did not clearly fail.

Rebrands: open-listings to Opendoor in 2019-02 (a unified brand and app, after Opendoor bought it in 2018-09), aesthetic from Plato Design in 2020 (hard to own or trademark), rima-ai from Garage in 2024 after pivoting from auto parts to accounting automation. Name outgrown by pivot appears in 49 records, so a pivot is the commonest reason to rename.

## Advice from the corpus

Paul Graham, 2015: a US startup without the .com should probably change the name, he finds a good name about 80 percent of the time in 20 minutes at office hours, and he says almost all top YC companies by valuation own their .com versus about 66 percent of a then current batch (https://paulgraham.com/name.html, no table shown). The repo data cannot test this because domains are free text. The Close founder account warns that branding and polished slides were busy work that did not move the idea, and progress came from prototypes and user feedback (https://close.com/blog/my-seven-attempts-to-get-into-y-combinator, self reported).

## Strong versus forgettable

Strong brands in the cases above share: a name that is easy to say and spell, a distinct identity (mascot, voice or a coined product term), a community or ambassador channel that spreads it, and a name that still fits the product after growth. Forgettable ones are generic or confusable with a larger brand, hard to search, or tied to a first product that was later dropped. The only rigorous element in the repo is the weak association of brand strength rating with survival, which is circular.

## Confounds and limits

Industry and era confound everything. Real word names dominate the oldest era, whose survivors are the famous winners. Consumer companies (35 percent Inactive in the directory, n=892) differ from B2B (15 percent, n=3,250) and may favor playful names. Recent batches are unresolved. The name features table counts the whole directory but names are cleaned by regex, and kind classification is heuristic. Branding records come from sources that exist more for survivors. Treat name choice as a small modifier: avoid obvious collisions and unpronounceable names, and do not expect the name to change the odds by more than a few points.
