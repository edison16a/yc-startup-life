---
name: yc-startup-creator
description: Find one genuinely strong startup idea using the researched YC knowledge base, then stress-test it with an Investor, a Doubter, a Judge and the evaluator, looping until the Judge invests. Use when asked to create, find or generate a startup idea.
---

# YC Startup Creator

Produces one startup idea that survives a hostile review, with a full dossier. It stands on the researched YC companies, base rates and distilled knowledge in this repo, and on what people need today. Do not stop at the first decent idea. Keep working until the stopping rule in Stage 4 is met. Do not ask the user questions; record assumptions in the run's `progress.md` and continue.

Settings are in `config.json` under `creator` (`min_conviction`, `max_cycles`, `min_candidates`, `finalists_per_cycle`, `debate_rounds`). Read and use them.

## Ground rules

1. **Evidence over rhetoric.** Every factual claim in a brief, the debate or the dossier needs a source URL or a computed number with the arithmetic shown. Unsourced claims are labelled `assumption`.
2. **Never invent data**: competitors, prices, customer counts, market sizes, YC outcomes. Analog companies must be real slugs from `data/companies.csv`.
3. **"Nobody has tackled this" is almost never literally true.** The working definition: no funded or traction-bearing company serves this exact wedge, shown by recorded searches. Weak or abandoned attempts are fine and informative.
4. **Moat** means something specific for software: proprietary or compounding data, deep workflow or integration lock-in, regulatory or compliance position, network effects or liquidity, a distribution advantage, or switching costs. "Better AI" or "better UX" alone is not one.
5. **Technical complexity cuts both ways.** Too easy means anyone can copy it; too hard means a small team cannot ship. The sweet spot is hard enough to be a moat, buildable by a small team to a useful MVP in about 3 months.
6. **Takeover risk is a first-class filter** (Stage 2), not an afterthought.
7. **No repeats.** Keep `rejected.md` (idea, cycle, reason). New batches need new directions, not reworded rejects.
8. **Roles stay independent.** Run Investor, Doubter and Judge as separate subagents given only the files listed for them. Without subagents, write each in full, in sequence, without softening one because of another.
9. Paraphrase sources; quote under 15 words at most. Commit only if the user asks.

## Stage 0: Load the knowledge

1. `python3 -I scripts/check_complete.py`. If `.claude/skills/yc-startup-creator/references/_finalized.json` does not exist, the extraction is unfinished: read `.claude/skills/yc-knowledge-extractor/SKILL.md` and carry it out until it is, then return. If it exists, continue (the data may have grown since).
2. Read `references/` here (`patterns.md`, `failure_modes.md`, `yc_acceptance.md`, `incumbent_and_complexity.md`, `tables/`), `knowledge/coverage.md` and `knowledge/backtest.md`. Note the coverage limits.
3. `python3 -I scripts/new_run.py` creates `runs/<date>-<n>/`. Make a task list with one task per stage. All later files go in that run folder.

## Stage 1: Criteria

Write `criteria.md` containing: the user's requirements (a specific niche; a large enough market, bottom-up; customers who demonstrably already pay; no funded or traction-bearing company on that exact wedge; software; a defensible moat); the rubric from `patterns.md` (0-5 each: pain severity, willingness to pay, market size, why now, whitespace, wedge/moat, small-team feasibility, distribution path, technical complexity fit, takeover resistance); and the red flags from `failure_modes.md` and the advice notes that disqualify or sharply downgrade an idea.

## Stage 2: Generate and filter ideas (repeat each cycle)

1. **What people need now.** Search the web for what has changed and what people are complaining about and paying for today: new technology capabilities, regulation, cost curves, behavior shifts, broken incumbents, jobs being posted, services firms doing manual work, the current YC Requests for Startups, and communities where buyers describe their pain. Record the evidence with URLs.
2. **Generate** at least `min_candidates` niches into `candidates.md`: customer, painful job, how it is solved today, why now, and the evidence of need. Favor narrow, painful, paid niches over broad categories.
3. **Hard filters.** Drop any candidate that fails one, recording the reason in `rejected.md`:
   - **Money:** evidence the customer already pays for a solution, a workaround or labor.
   - **Size:** a bottom-up estimate (customers x realistic price), inputs sourced, arithmetic shown.
   - **Software:** the core product is software a small team can build and ship to a useful MVP in about 3 months.
   - **Whitespace:** see step 4.
   - **Takeover:** name who could build or absorb it (incumbents, platforms, well-funded startups), how many months they would need, and whether they have the incentive and distribution. Drop it unless a real moat (rule 4) survives their best response. Use the incumbent cases in `incumbent_and_complexity.md`.
4. **Whitespace and category history**, recorded in `evidence/<idea-slug>.md`:
   - `python3 -I scripts/comps.py "<idea>" --all --k 20` and `python3 -I scripts/yc_overlap.py "<keyword>" ...` with at least three different keyword sets. A past YC company with traction on the same wedge is a fail; a dead one is a lesson, so find out why it died (read its record in `data/enrichment/`).
   - `python3 -I scripts/base_rates.py --tag "<tag>"` (and `--industry`) for the category's history: if its shutdown rate or progression is much worse than the overall base rate, the idea needs a clear reason it differs.
   - Search the web, app stores, GitHub, Product Hunt and funding news for competitors. Record each closest competitor, its traction and funding, and the specific gap.
   - Pass only if no funded or traction-bearing company serves this exact wedge.
5. **Score** survivors on the rubric. Keep the top `finalists_per_cycle`. Write a one-page brief per finalist in `briefs/<idea-slug>.md`: customer, pain, product, MVP scope, pricing, bottom-up market size, wedge, named moat, technical complexity and what is hard, takeover analysis, go-to-market, why now, founder-market-fit assumptions, key risks. Every claim sourced.

## Stage 3: Review

For each finalist create `debate/<idea-slug>/` and run:

- **Evaluator (summary mode).** Run the `yc-startup-evaluator` skill in `summary` mode on the brief, output to `debate/<idea-slug>/evaluation/` (`python3 -I scripts/new_eval.py <idea-slug> --mode summary --out debate/<idea-slug>/evaluation`). Its YC odds, round table and killers go to all three roles below.
- **Investor** (`investor.md`): wants to invest; builds the strongest honest case: market pull, timing, wedge, moat, expansion path, comparable YC outcomes. Inputs: brief, evidence, evaluation, `patterns.md`. Every claim sourced.
- **Doubter** (`doubter.md`): assumes failure; finds every credible reason: willingness to pay, real market size, distribution, incumbents copying it, platform risk, regulation, technical risk, long sales cycles, why nobody has built it, and the lessons of dead YC companies in the space. Same inputs. Every claim sourced.
- **Rebuttals** (`investor_rebuttal.md`, `doubter_rebuttal.md`): `debate_rounds` rounds in total; each side answers the other's strongest points and may concede.
- **Judge** (`judge.md`, `judge.json`): reads everything, **re-opens at least three of the sources the two sides lean on most**, looks for what both missed, scores the idea on the rubric, and rules `INVEST` (conviction 1-10, 3 reasons, 3 risks), `PASS` (reasons, what would have to change) or `REVISE` (named changes). The Judge may not issue `INVEST` at or above `min_conviction` unless the money evidence, the size arithmetic, the whitespace evidence and the takeover assessment are each present and checked (`hard_filters_checked` in `judge.json`; format in `docs/judge-schema.md`). The `idea` value equals the folder name.

## Stage 4: Loop

Update `state.json` and `progress.md` after every cycle.

- `REVISE`: apply the changes, update brief, evidence and evaluation, and re-run Stage 3 for that idea (not a new cycle).
- All finalists `PASS`: start a new cycle at Stage 2, using the Doubters' findings to choose new directions; increment `cycle`.
- **Stop** when a Judge returns `INVEST` at or above `min_conviction`.
- **Cap:** after `max_cycles` cycles without that, set `state.json` status to `cap_reached` and deliver the highest-conviction idea, labelled "best found, not confirmed", with what is unresolved. Never present a weak idea as strong.

## Stage 5: Dossier and verification

1. Run the `yc-startup-evaluator` skill in **full** mode on the winner, output to `runs/<run-id>/evaluation/` (`new_eval.py ... --mode full --out runs/<run-id>/evaluation`). It must pass `check_eval.py`.
2. Write `FINAL.md` with exactly the headings in `docs/dossier-template.md` (the checker looks for them), including full detail: the idea, who pays and why, product and MVP scope, pricing, market size with arithmetic, competition and whitespace evidence, technical complexity and takeover risk, fit with YC patterns and analog outcomes, the funding outlook from the evaluation (the round table), go-to-market, founder profile, 30-day experiments, the debate summary, runners-up, a draft YC application, research limits, sources.
3. Verify: re-run the market-size arithmetic; re-open five sources behind key claims; then `python3 -I scripts/check_run.py runs/<run-id>` must print OK.
4. Deliver `FINAL.md` (as a doc if the session offers one, otherwise as a file) and give the user a short message: the idea, the Judge's verdict and conviction, the YC odds, and the biggest open risk.
