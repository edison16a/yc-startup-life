---
name: yc-knowledge-extractor
description: Research every past YC company in depth (timeline, funding rounds, founders, competition at the time, why it won or failed), distill YC advice, derive base rates, and finalize the evaluator and creator skills. Use to run, resume or verify the extraction.
---

# YC Knowledge Extractor

This skill turns the YC company directory (6,399 companies in `data/companies.csv`) into a researched dataset, a distilled advice corpus and calibrated reference knowledge, then finalizes the `yc-startup-evaluator` and `yc-startup-creator` skills with it. The job is **finished only when `python3 -I scripts/check_complete.py` exits 0.** It is very large and resumable: keep going, wave after wave, until it passes or the user's budget ends. Do not ask the user questions; record assumptions in `knowledge/progress.md` and continue.

## Ground rules

1. **Never invent data.** Use `null` / `[]` for what you cannot find. Every non-obvious fact needs a URL in `sources`; every funding round and competitor carries its own `source_url`.
2. **Time accounting.** Every historical fact carries a date. We want what was true *when*, not what is true now. Rounds have dates; the exit or shutdown has a date; competitors are dated (below).
3. **Competition is as of founding.** `competition_at_founding` lists only competitors that existed around the company's YC batch, evidenced by sources dated then (launch coverage, early product pages, Web Archive snapshots, contemporaneous reviews and comparison posts). Competitors that appeared later go in `outcome_analysis`. Competition today is irrelevant here.
4. **Unknown is not zero.** If a funding history cannot be found, set `funding_data_coverage` to `none_found`. Never record "raised nothing" without sources. This matters: the base rates are only honest if missing data is not mistaken for failure.
5. **Ages** only when a source states age or birth year; never estimate.
6. **Public sources only.** Use WebSearch and WebFetch. If a site is declined or blocked, do not work around it (no mirrors, caches or scrapers); use another source or record the gap. Do not use logged-in or paywalled content.
7. **Paraphrase** advice and articles. Never paste article text; quote under 15 words at most, once per source.
8. **Judgment fields are rated for the time of founding** (technical complexity, defensibility, takeover risk), using the scales in `docs/schema.md`, with a rationale that cites concrete facts.
9. **Resumable.** One JSON per company at `data/enrichment/<slug>.json`. Finished companies are skipped. Never delete or overwrite a valid depth-2 record except to correct it.
10. **Search budget.** WebSearch is limited per turn (about 200 calls, shared by every agent in the turn). One shard needs roughly 30 to 50 searches, so launch at most 4 shards per wave unless the environment raises the limit. A subagent whose searches are refused must not write depth-2 records from page fetches alone: it writes depth-1 records (set `depth: 1` and say why in `notes`) or nothing, and reports it. The orchestrator downgrades any depth-2 record written without the required searches to `depth: 1` so it is re-queued and kept out of the base rates.
11. Commit only if the user asks.

## Progress and restarts

Start every session with `python3 -I scripts/check_complete.py` and read `knowledge/progress.md`. Create a task list with one task per stage below. After every wave of shards, update `knowledge/progress.md` (stage, shards done and left, audit results, problems, assumptions). If your context fills up, the files are the memory: re-run the queue builder and carry on.

## Stage 0: Setup

1. If `data/companies.csv` is missing: `python3 -I scripts/fetch_yc_companies.py && python3 -I scripts/build_csv.py`. If fetching fails, say so and ask for `data/raw/yc_all.json`; this is the only valid early stop.
2. Read `docs/schema.md`, `docs/taxonomy.md` and `config.json` (the `extraction` block sets shard size, parallelism, per-company tool budget, audit rates).

## Stage 1: Research every company (depth 2)

**Order:** the random calibration sample first (about 10% of every batch), then everything else by priority tier (public/top, acquired, recent active, other active, inactive). The calibration sample comes first because base rates from a hand-picked set of winners would be biased; a random sample gives honest numbers early, so the evaluator is usable long before the last shard.

1. `python3 -I scripts/make_work_queue.py` writes `data/queue/cal_NNNN.json` (calibration) then `shard_NNNN.json`. Re-run it after each wave: it only queues what is still undone.
2. Work in **waves**: launch `parallel_agents` subagents at once, one shard each, using the **research prompt** below; wait for the wave to finish; run `python3 -I scripts/merge_enrichment.py`; fix anything it reports INVALID (re-run those companies); then audit (next step); then launch the next wave. Finish all `cal_*` shards before any `shard_*`.
3. **Audit every wave.** Pick `audit_sample_per_100` records per 100 written (at least 3 per wave), spread across shards. Give each to an independent auditor subagent that has not seen the researcher's work: re-open the cited sources and check founders, every funding round (stage, date, amount), the exit or shutdown, and that each listed competitor has a source dated near the founding. Append findings to `knowledge/audit_log.md` (slug, fields checked, errors found). If more than `audit_max_error_rate` of audited fields are wrong, redo the whole shard with the corrected prompt and note it.
4. Companies with essentially no public information (stealth, long dead with no trace) still get a depth-2 record with `confidence: low`, `funding_data_coverage: none_found` and an honest `outcome_analysis`. Only if no meaningful record can be written at all, add the slug to `data/unresearchable.csv` (`slug,reason`); this may not exceed 5% of companies. (`data/unresearchable.csv` already lists `y-combinator`, which is YC itself and has no batch.)

Exit: the queue builder reports 0 left (every company is depth 2 or unresearchable), the calibration sample is complete, and the merge exits 0.

### Research prompt (give each subagent its shard path)

> You are researching YC companies for a dataset used to forecast startup outcomes. Read `<shard path>`, `docs/schema.md`, `docs/taxonomy.md` and `config.json`. For each company write `data/enrichment/<slug>.json` with `depth: 2` following the schema exactly, including the `branding` block. Spend at most `max_tool_calls_per_company` tool calls per company, then write what you have.
>
> **Required minimum per company** (the first pilot skipped these and produced thin records; do not skip them):
> 1. The YC page (`yc_url`) and the company website, or a note that the site is dead.
> 2. One **outcome search** (acquisition, shutdown, post-mortem, layoffs, "<name> shuts down"). For every Inactive company, search for the cause; if none is found write `outcome_analysis` stating that the cause is not public, and leave `failure_factors` empty only then.
> 3. One **funding search plus one cross-check** (press release, SEC EDGAR Form D, Wikipedia, or a second outlet). A figure seen only in a search snippet or one aggregator goes in `notes` as unverified; do not record it as a round.
> 4. One **competitor search with date terms** (batch year, "launches", "alternative to"). If nothing dated near the batch exists, leave the list empty and say so in `notes`; never fill it from today's market.
> 5. One **branding search**: name origin and meaning (founder interviews, "why we named"), mascot or character, logo and visual style, voice, rebrands, community and merch, press about the brand itself, domain history. Use the company's own site and social pages too. Rate only what sources show; use `unclear` and `null` freely.
>
> Method for the rest: (1) founders from the YC page and bios: prior employers, education, technical or not, previous startups; age only if a source states it. (2) Record every round with date, amount, post-money only if a source states or estimates it (`valuation_basis`), investors, and `source_url`. (3) Rate technical complexity, defensibility and takeover risk **as of the time of founding**, with a rationale citing facts; for takeover risk, record what incumbents actually did. (4) `market_need_then`: evidence of demand when they started. (5) Pivots with dates. (6) `success_factors` / `failure_factors` from the taxonomy (including `brand_pull` and `brand_confusion` when a source supports them). (7) `outcome_analysis`: one paragraph on why this company succeeded, stalled or failed.
>
> Never guess. Unknown means `null`, `[]` or `none_found`. If the directory status disagrees with what you find, say so in `notes`. A site that returns 403 or is blocked is not worked around. Then run `python3 -I scripts/merge_enrichment.py --check data/enrichment/<slug>.json` for each file and fix every ERROR and every avoidable warning. Reply with one line per company: slug, confidence, funding_data_coverage, brand_strength rating, and one line on tool problems.

## Stage 2: Advice corpus and YC facts

1. Start from `knowledge/advice/sources.md`, then find more. Cover (including naming and branding advice): Paul Graham essays on ideas and startups; the YC Library and Startup School; YC's application and interview guidance; the current Requests for Startups; partner talks and posts; **first-person accounts from accepted and rejected applicants** (Reddit, Hacker News, Indie Hackers, personal blogs, X threads); founder post-mortems; published YC acceptance-rate and applicant-count statements; the current YC standard deal terms.
2. For each source write `knowledge/advice/<short-slug>.md`, starting with these lines: `type: official | insider | applicant_account | post_mortem | anecdote`, `url:`, `author:`, `date:`. Then, in your own words: the claims, the evidence the author gives, and how widely other sources corroborate it. Update `knowledge/advice/sources.md` with each source's status.
3. Treat anecdotes as anecdotes. Weight official statements and corroborated patterns higher, and say so.

Exit: at least `advice_sources_min` notes, at least `applicant_accounts_min` of them `type: applicant_account`, including the current RFS list and published acceptance-rate statements. Record sources that could not be fetched.

## Stage 3: Derive the knowledge

1. `python3 -I scripts/merge_enrichment.py && python3 -I scripts/base_rates.py --write-tables`, then read `knowledge/tables/*.csv` and run `scripts/base_rates.py` for the cohorts you want to discuss. Use calibration-sample numbers for unbiased rates and the full set for detail; always quote sample sizes and the lower/known/upper range for funding stages.
2. Write these files in `knowledge/` (each at least 250 words, every number traceable to a table, a base_rates run, or a cited source, with the biases stated):
   - `patterns.md`: what the winners had in common versus the failures: industries, models, founder profiles, timing, competition at founding, pivots, moat; plus a 0-5 scoring rubric (pain severity, willingness to pay, market size, why now, whitespace, wedge/moat, small-team feasibility, distribution path, technical complexity fit, takeover resistance) with what each score means.
   - `failure_modes.md`: each failure factor with counts, typical months to shutdown, early warning signs, and example slugs.
   - `yc_acceptance.md`: published acceptance rates and applicant counts with sources; the selection criteria from YC's own material and insider accounts; a factor table for adjusting odds up or down; what the accepted founders looked like in the data; explicit uncertainty (nobody outside YC knows the real model).
   - `stage_benchmarks.md`: round sizes and valuations by stage and era from `round_benchmarks.csv`, time between milestones from `time_to_milestones.csv`, how to translate older eras to today (research current seed/A/B/C benchmarks from public reports and cite them), current YC deal terms, and data-coverage caveats.
   - `naming.md`: what the `branding` records and `name_outcomes.csv` show: name types, lengths and styles versus outcomes by era (quote n and the confounds), the best and worst brand cases with slugs and sources (mascots, voice, community, rebrands, confusing or generic names), name-and-domain patterns, advice from the corpus on naming, and a short guide to what separates a strong brand from a forgettable one. State plainly how much of the effect is confounded with industry and era.
   - `incumbent_and_complexity.md`: outcomes by technical complexity, defensibility, takeover risk and competitor count from `factor_outcomes.csv`; concrete cases where incumbents copied, bought or ignored a wedge and how fast; what defended.

Exit: the six files exist and the tables are current.

## Stage 4: Finalize the skills and backtest

1. `python3 -I scripts/finalize_skills.py` copies the distilled knowledge and tables into the `references/` folders of `yc-startup-evaluator`, `yc-startup-creator` and `yc-name-creator` and stamps them with the data they were built from.
2. **Backtest.** Pick at least 5 companies from `data/calibration_sample.csv` with different outcomes (shutdown, stalled, Series A, later rounds, exit). For each, run the evaluator skill in `summary` mode as if it were their batch date, describing the company only from facts available then, with `comps.py --exclude <slug>` so it is not its own analog. Compare each forecast with what actually happened. Write `knowledge/backtest.md`: per company the forecast, the outcome, and what the miss teaches; then concrete calibration notes (are probabilities too high or low, which factors were overweighted) and append the lessons to the evaluator's `references/` by re-running finalize. Backtest evaluation folders go under `evaluations/backtest-*`.
3. Fix the evaluator and creator SKILL.md files if the backtest shows a recurring mistake, and say what you changed in `knowledge/progress.md`.

## Stage 5: Verify and finish

1. Final audit: sample another round of records (at least 25 spread across eras and outcomes) and verify as in Stage 1. Append the results and end `knowledge/audit_log.md` with the exact line `AUDIT RESULT: PASS` only if the error rate is at or below `audit_max_error_rate`; otherwise fix and re-audit.
2. `python3 -I scripts/finalize_skills.py` once more (it re-stamps), then `python3 -I scripts/check_complete.py` must exit 0.
3. Report to the user: coverage numbers, sample sizes behind the headline base rates, audit error rate, backtest findings, and anything not done. Do not call anything "complete" while `check_complete.py` fails.
