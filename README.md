# YC Startup Engine

One repo that (1) researches every past Y Combinator company in depth, (2) evaluates a startup's odds if it applied to YC, round by round, and (3) creates a new startup idea and stress-tests it. The extraction builds the data and the calibrated knowledge; the evaluator and creator skills run on top of it.

## Use it

```bash
unzip yc-startup-engine.zip && cd yc-startup-engine
claude
```
Then say **"Begin."** The agent reads `CLAUDE.md`, runs `python3 -I scripts/check_complete.py`, and carries out the extractor skill until it passes. Afterwards:

- "Evaluate this startup: ..." runs the **evaluator**.
- "Find me a startup idea." runs the **creator**.

## The three skills (`.claude/skills/`)

| Skill | What it does |
|---|---|
| `yc-knowledge-extractor` | Researches all 6,399 companies (timeline, every funding round with date and amount, founders, **competitors at the time of founding**, technical complexity, defensibility, takeover risk then, why it won or failed), builds the advice corpus (including applicant accounts and YC acceptance figures), derives base rates and benchmark tables, writes the knowledge files, finalizes the other two skills, audits and backtests. |
| `yc-startup-evaluator` | For one startup: chance of getting into YC, then Seed / Series A / Series B / Series C+ probabilities with raise and post-money bands, labelled Very likely to Very unlikely, **a paragraph on why it fails at each round**, and a deep pre-mortem (need today, competition now vs. then, technical complexity, who could take it over, economics, team, why YC may say no). Numbers are anchored on cohort base rates and checked by script. |
| `yc-startup-creator` | Scans what people need now, generates 25+ niches, filters on payment evidence, bottom-up size, whitespace (checked against all past YC companies and the web), technical feasibility and takeover risk, then runs an Investor, a Doubter and a Judge (with an evaluator summary for each finalist) and loops until the Judge invests at conviction 8+. Delivers a full dossier with a full evaluation and a draft YC application. |

## How the numbers stay honest

- **Calibration sample first.** About 10% of every batch (663 companies, chosen by a fixed hash) is researched before anything else, so base rates are unbiased early. The evaluator is usable once it is done.
- **Missing is not zero.** Funding history is often not public. Each record states how complete it is, and base rates report a lower / known-only / upper range.
- **Dated facts.** Every round, exit and competitor has a date. Competitors must be evidenced as of founding, not today.
- **Scripts do the arithmetic.** `scripts/render_eval.py` computes cumulative odds and labels from the agent's conditional probabilities; `check_eval.py` fails if the report drifts from its inputs, if band probabilities don't sum to 1, if an estimate is far from its base-rate anchor without a reason, or if an analog company isn't real.
- **Audits and a backtest.** Independent agents re-verify a sample of records every wave; the finished evaluator is backtested on past companies; `check_complete.py` gates the whole thing.

## Scale, honestly

Deep research on 6,399 companies is a very large job: up to about 14 tool calls each (set in `config.json`) is on the order of 90,000 tool calls and substantial agent time and cost, likely days of wall-clock with several agents in parallel. It is resumable and ordered so intermediate results are usable. Tune `extraction.parallel_agents` and `max_tool_calls_per_company` to your budget; lowering the per-company budget lowers the share of fields found, which the confidence and coverage fields record.

## Limits

- Everything is built from public sources. Private funding terms are often unknown, so valuation data in particular is sparse, and founder ages will be rare.
- The evaluator's probabilities are calibrated judgments anchored on past YC companies, not statistical predictions. Past YC companies are survivors of a selection process, the researched set is a sample, and the market changes.
- The Investor, Doubter, Judge, Auditor and Doubter-in-the-evaluator are the same underlying model in roles. Independent agents and required sources reduce echoing but do not remove it.
- The creator's output is a well-tested hypothesis; the dossier's 30-day experiments are how you find out.

## Layout

```
.claude/skills/        the three skills (references/ filled at finalize)
config.json            extraction, creator and evaluator settings, label cut-offs
data/                  directory snapshot, enrichment/<slug>.json, generated CSV tables
knowledge/             advice notes, derived knowledge files, tables, audit log, backtest
docs/                  schema, taxonomy, templates
scripts/               queue, merge, base rates, comps, evaluation render/check, completeness gate
runs/  evaluations/    creator runs and evaluator outputs
```
