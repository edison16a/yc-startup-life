---
name: yc-name-creator
description: Create and evaluate startup names and brand direction using the branding research on past YC companies (name features, outcome rates, brand cases like mascots and voice). Use when asked to name a startup, judge a name, or when the evaluator or creator needs a brand assessment.
---

# YC Name Creator

Two jobs: **create** names for a startup and **evaluate** a name (new or existing), grounded in how past YC companies' names and brands did. The evaluator and creator skills call this one; it also runs on its own. Do not ask questions: record assumptions and continue.

Brand is a real factor in success but a secondary one. A great name rarely rescues a weak company and a mediocre name rarely sinks a strong one. Say so, and rate the name on its own evidence.

## Ground rules

1. **Never invent evidence.** Brand cases come from `data/enrichment/<slug>.json` `branding` blocks (check the slug exists) or sourced web pages. Say when a case is an anecdote.
2. **Name statistics are context, not causes.** `scripts/name_features.py` cohorts are confounded with industry and era and shaped by survivorship. Use them to catch outliers; never pick a name because a cohort did well.
3. **Check conflicts for real.** A name is not "available" because you did not find a conflict. Record what you searched.
4. **Say the name aloud.** Pronunciation, spelling-by-ear and voice-search failures kill names. Test each finalist on: heard once, can someone type it? Said in a sentence, is it clear?
5. Paraphrase sources; quote under 15 words at most.

## Stage 0: Load

Read `references/` here: `naming.md` (distilled branding findings; if missing, the extraction is unfinished, so proceed with `python3 -I scripts/name_features.py --score` output and whatever `branding` records exist under `data/enrichment/`, and say the evidence is thin) and `tables/name_outcomes.csv`. To find strong and weak brand cases, search the records: `grep -l '"brand_effect_on_outcome": "helped"' data/enrichment/*.json` (and `hurt`), and read a handful, especially in the same industry and era.

## Mode A: Evaluate a name

1. `python3 -I scripts/name_features.py --score "<Name>" --era <era of the intended batch>`. Record the command and headline.
2. Score 1-5 each, with one sentence of evidence per score:
   - **Distinctiveness**: could it be confused with, or lost among, other companies and common words?
   - **Say and spell**: pronounceable on first read; spelling guessable after hearing it once.
   - **Memorability and warmth**: short, concrete, evocative; does it carry an image or feeling people can hold (a character, an animal, a sound)?
   - **Fit**: tone matches the buyer (a bank is not a mascot, a dev tool can be playful) and does not describe a wedge the company will outgrow after a pivot.
   - **Searchability and domain**: findable on search; exact `.com` or a credible alternative; handles. Check with web search and DNS (`getent hosts <name>.com`, a weak signal only, never proof of availability).
   - **Conflict and trademark**: existing companies, products, marks in the same class; search USPTO and the web; this is a screen, not legal advice.
   - **Connotation**: meaning in major languages and common slang; negative or awkward readings.
   - **Brand extensibility**: room for a mascot, voice, visual identity and a community ritual. Name the one brand asset the company could own.
3. `brand.rating` for the evaluator: the rounded average, pulled down by any score of 1 on conflict, connotation or say-and-spell (these are near-vetoes). Give strengths, weaknesses and `effect_on_success` (`helps | neutral | hurts | unclear`) with the comparison cases that justify it.
4. For an existing company, add what exists today: logo, voice, mascot, community, rebrands, with sources.

## Mode B: Create names

1. Understand the company: customer, tone, what it will grow into, markets, whether the name must work verbally.
2. Generate at least 40 candidates across styles, not variations of one: real words with new meaning, short coinages, compounds, evocative animals or objects, person or place references, suffix coinages. Avoid category jargon unless the user wants descriptive names.
3. Screen all 40 with `name_features.py --score` flags and aloud-testing, cut to 12, run the conflict and domain checks on the 12, cut to the best 5.
4. For each finalist run Mode A in full. For the top 2, also write a brand sketch: the one memorable asset (mascot, phrase, colour, ritual), voice and tone, visual direction, and one launch-day idea that uses the name.
5. **Independent challenge.** Launch a Doubter subagent given only the five names, the company description and the rubric. It must find the strongest reason each name fails (confusion, connotation, pivot risk, buyer fit, trademark). Revise or drop names it breaks; note what it caught.
6. Deliver a ranked shortlist: name, score, why it works, the main risk, domain and handle status with what was checked, and the brand sketch for the top two. Write it to the file path the calling skill gives, otherwise `names/<startup-slug>.md`.

## Used by other skills

- **Evaluator**: run Mode A in `summary` form on the startup's name and fill the `brand` block of `evaluation_input.json` (see `docs/eval-input-schema.md`). If the startup has no name yet, say so, run Mode B briefly, and evaluate the best candidate.
- **Creator**: for each finalist, a working name from Mode B goes in the brief; the winner gets a full Mode B in the dossier's "Name and brand" section.
