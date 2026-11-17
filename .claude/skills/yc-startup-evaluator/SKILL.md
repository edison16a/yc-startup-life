---
name: yc-startup-evaluator
description: Evaluate a startup if it applied to YC: chance of getting in, then per-round probabilities, raise sizes and valuations with labels, why it fails at each round, and a deep pre-mortem, anchored on researched past YC companies. Use when asked to evaluate, forecast or stress-test a startup.
---

# YC Startup Evaluator

Produces an evaluation of one startup: the chance it gets into YC, and, if it does, the probability of reaching each funding round with the likely raise and valuation (each labelled Very likely / Likely / Reasonable / Unlikely / Very unlikely), a one-paragraph explanation of why it fails at each round, and then a deep dive into why the company may not work. Everything is anchored on the researched YC companies in this repo, not on gut feel.

Two modes: `full` (default) and `summary` (used by the creator skill for finalists and by backtests: same numbers and per-round paragraphs, fewer killers, no deep dive).

The user will describe the startup (or point to a repo, site or pitch). If the description is thin, work with what you have, list the gaps under assumptions, and continue. Do not ask questions.

## Ground rules

1. **Reference-class forecasting.** Start from base rates for similar past YC companies; adjust for this startup with stated reasons. A number with no anchor and no reason is a guess; the scripts reject it.
2. **Never invent evidence.** Competitors, demand evidence, benchmarks and YC statistics need source URLs. Analog companies must be real (their slugs are checked against `data/companies.csv`).
3. **Be skeptical by default.** A founder's description is the best case. Look for the reasons it fails, then weigh them honestly.
4. **Probabilities are never 0 or 1**, and cumulative odds must be consistent with the base rates unless you can show why this company is different.
5. **Era matters.** Round sizes and valuations from 2018-2021 are inflated relative to today; use current benchmarks and say so.
6. **Missing funding data is not failure.** Use the lower/known/upper range from `base_rates.py`, not a single number, and say which you used.
7. Never edit `EVALUATION.md` by hand: fix `evaluation_input.json` and re-render.
8. Paraphrase sources; quote under 15 words at most.

## Stage 0: Load the knowledge

Read `references/` in this skill folder: `yc_acceptance.md`, `stage_benchmarks.md`, `patterns.md`, `failure_modes.md`, `incumbent_and_complexity.md`, `naming.md`, the tables in `references/tables/`, and `knowledge/backtest.md` in the repo if it exists (lessons on over- and under-confidence). Check `references/_finalized.json`: if it is missing, the extraction is unfinished. Do not refuse: proceed with whatever data exists (run `python3 -I scripts/base_rates.py` and read `knowledge/coverage.md`), and state the coverage limits prominently in the assumptions. If the data is thin, widen your uncertainty.

## Stage 1: Set up

`python3 -I scripts/new_eval.py <startup-slug> --mode full` (or `summary`; add `--out <dir>` when another skill tells you where) creates the folder and a blank `evaluation_input.json` (see `docs/eval-input-schema.md`). Create a task list: research, analogs and base rates, YC odds, ladder, killers and deep dive, render and check.

## Stage 2: The world today

Search the web and record sources for each:

- **Need now.** Evidence that customers want this today and pay for something like it: spend, pricing pages, job postings, services firms, public complaints, regulation, community demand, analyst data, recent funding in the category. Rate 1-5 (5 = urgent and paid). At least 2 sourced items in full mode.
- **Competition now.** Direct competitors, adjacent products, incumbents, and the status quo (spreadsheets, services, doing nothing): what they do, traction, funding, source. At least 3 in full mode. What is this startup actually competing against, and why would a customer switch?
- **Technical complexity.** What is genuinely hard, what a small team can and cannot build in 3 months, dependencies on models, data, hardware or licences. Rate 1-5 using the scale in `docs/schema.md`. Hard parts that a small team can solve are a moat; hard parts it cannot are a risk.
- **Takeover and copy risk.** Which companies or platforms could build or absorb this, how many months a well-resourced rival would need, whether they have the incentive and distribution, and any platform dependency. Rate 1-5 (5 = very likely). Use the incumbent cases in `incumbent_and_complexity.md` for how this has played out for past YC companies.
- **Name and brand.** Run the `yc-name-creator` skill in Mode A on the startup's name (summary form in `summary` mode). Fill the `brand` block: rating, `effect_on_success`, the `name_check` command and result, strengths and weaknesses, and a rationale that cites real past YC brand cases. Brand is a secondary success factor: let it move a probability only with a stated reason, and never let it outweigh need, competition or team.
- **Funding climate.** Current typical seed / Series A / Series B / C raise sizes and valuations for this category, the latest YC acceptance rate and applicant figures, and the current YC deal. Cite them.

## Stage 3: Analogs and base rates

1. `python3 -I scripts/comps.py "<description>" --k 15`. Read the records (`data/enrichment/<slug>.json`) of the most similar companies. Choose at least 5 (full) or 3 (summary) that are really comparable, including failures. Aim for 10 in full mode when the data has that many: the report plots up to 10 on its comparison chart, and the chart is only informative if the set includes companies that died, not just survivors. For each: what happened and why, how crowded it was then versus now, its complexity, takeover outcome.
2. `python3 -I scripts/yc_overlap.py "<keyword>" ...` for direct YC overlap in the same wedge; find out what became of them.
3. `python3 -I scripts/base_rates.py` for at least two cohorts: a broad one (industry or tag, recent batches) and a narrow one (business model or tight tag). Use `--calibration-only` for unbiased rates. If a cohort has fewer than 30 researched companies, widen it. Record the command and the numbers: they become the anchors. Mapping: the ladder stages `seed`, `series_a`, `series_b` match the base-rate rows of the same name, and `series_c_plus` matches the `series_c` row (which counts companies that reached Series C or later). Each row's `cond` figure is P(stage | previous stage) and is the usual anchor for `p_reach_given_prev`; quote the lower / known-only / upper range in `anchors.source`.

## Stage 4: Chance of getting into YC

Start from the published acceptance rate (see `references/yc_acceptance.md`, and verify the latest figure by search). Adjust using the factor table there: team and founder-market fit, idea and market, traction, how crowded the space is, technical credibility, how the idea fits YC's current priorities. Give `p`, `p_low`, `p_high` and a `basis` that shows the starting rate and each adjustment. Then write `why_it_fails`: one specific paragraph on why YC would most plausibly say no. If the company is already in YC or the user wants the "if accepted" view only, still report the acceptance estimate for completeness and say so.

## Stage 5: The funding ladder

For each of `seed`, `series_a`, `series_b`, `series_c_plus`:

1. **`p_reach_given_prev`**: the probability of reaching this round given the previous step (seed is given acceptance to YC). Start from the base-rate anchor (the conditional rate for the cohort), then adjust for need, competition, complexity, takeover risk, team and traction. If you differ from the anchor by more than 2x, the `adjustment_reason` must justify it with evidence. Record the anchor and its source.
2. **`bands`**: 2-4 scenarios for the round **if reached**, each with `raise_usd [low, high]`, `post_money_usd [low, high]` and `p_band`. Use `stage_benchmarks.md`, the round-size tables and the current climate. Include a thin or down-round band and an upside band. The `p_band` values partition the round (sum to 1.00). Explain each band in `rationale`.
3. **`why_it_fails`**: one paragraph (45+ words), specific to this company and this round: what milestone it will miss, why investors pass, what the analogs show. No generic advice.

Then `outcomes`: a partition of final results (shuts down or stalls; acquired or IPO under $100M; $100M-$1B; over $1B) with value ranges and a `why_it_fails` paragraph for failing to reach a meaningful exit.

## Stage 6: Killers and deep dive

**Summary mode:** list at least 3 killers yourself, each with evidence and real analog slugs, then go to Stage 7.

**Full mode:** go deep on why this company will not work.
1. Launch a **Doubter** subagent that has not seen your probabilities. Give it the description, the research notes, the analogs and the failure-mode data. It assumes the company has failed five years from now and writes: at least 5 ranked killers (risk, probability the risk materializes, evidence, analog slugs, mitigation) and the seven deep-dive sections (`market_need`, `competition`, `technical_complexity`, `takeover`, `economics_and_distribution`, `team`, `yc_specific`), each 60+ words and specific. In the competition section it must contrast competition now with what competition looked like for the analogs at their founding.
2. Merge its output into the JSON. If its killers contradict your probabilities (a killer with a 40% chance of happening, but a ladder that ignores it), reconcile them.
3. Write `narrative.general_summary` (the general picture first, 80+ words) and `narrative.headline`.

## Stage 7: Audit, render, check

1. Launch an **Auditor** subagent (full mode) with only the finished JSON and the repo. It must: re-open at least 5 of the cited sources and confirm them; open at least 3 analog records and confirm the summaries match; re-run the cited `base_rates.py` commands and compare the anchors; check that the cumulative odds are plausible against the base rates (flag any stage where the final odds are much better than the cohort without a documented reason); and return a list of issues. Fix them.
2. Fill `roadmap` (see `docs/eval-input-schema.md`), `pros` (the honest strengths) and `brand` (from `yc-name-creator`) in the input. `python3 -I scripts/render_eval.py <dir>` validates the input, computes the cumulative odds and labels, and writes `EVALUATION.md`, `evaluation_computed.json` and **`report.html`**. Fix every ERROR and re-run. Then `python3 -I scripts/check_eval.py <dir>` must print OK (it also checks that `report.html` matches the input).
3. **Deliver both.** Every evaluation ends with a text response in the chat and the standalone `report.html`. Give the user the file (send it so they can download and open it; it is one self-contained file, no server needed) and keep `EVALUATION.md` as the plain-text record. Open the report in a browser once (Playwright is available) and check it renders with no console errors before you hand it over. Never edit `report.html` by hand.
4. The text response is short: the headline, the YC odds with its label, where it most likely stops if accepted and the typical valuation there, how many of the comparable companies shut down, the single biggest killer, and what would most change the numbers. Say plainly when the data behind a number is thin.

## Calibration rules from the backtest

From `knowledge/backtest.md` (six companies, direction only): keep each step within 0.75 times its cohort anchor unless a named analog shows the same fatal problem, because niche-sounding stories were over-discounted. State that reaching a round years later is common for companies with paying customers. Include a pivot-then-raise path in the upside band. In a backtest, run `yc_overlap.py` with `--exclude <slug>` so the company does not see its own outcome.

## The report (`report.html`)

One animated file with eight tabs: **Overview** (YC chance, most likely stopping stage, furthest credible stage, how the similar companies ended, step by step odds, four scorecards), **Compare** (up to 10 similar past YC companies as app icons on smooth curves, dimmed until you click one in the list; this startup is the bright orange line and ends with a mark where it most likely stops; drag along the timeline to see who had died by then), **Walkthrough** (a simulated run: each press of the arrow draws the next step from the evaluation's odds, so the line rises or crashes, ending in the reason and a link to the roadmap for that step), **Possibilities** (a clickable tree of every path with the odds on each branch), **Funding** (each round's odds, valuation bands and why it fails there), **Roadmap** (what to do to reach each step, from the input's `roadmap`), **Insights** (need, competition, technical, takeover, brand, deep dive, sources), **Pros and cons**. Design rules: minimal and modern, rounded, orange and black with blue accents on beige or dark, simple SVG icons, no gradients, no background fills on icon buttons or tabs (color change only), company logos as rounded square app icons with no border or circle, no filler subtitles or chips. Valuation data for past companies is sparse, so the chart defaults to total raised when fewer than three comparable companies have a reported valuation, and says so on the page.
