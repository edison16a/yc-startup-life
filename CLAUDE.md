# YC Startup Engine: standing orders

This repo researches every past YC company in depth and uses that to evaluate startups and create new startup ideas. It holds four skills in `.claude/skills/`:

- `yc-knowledge-extractor`: researches all 6,399 companies, distills YC advice, derives base rates, and finalizes the other two skills.
- `yc-startup-evaluator`: forecasts a startup's chance of getting into YC, then per-round odds, raises and valuations, and why it fails. Delivers a text summary plus one standalone animated `report.html`.
- `yc-name-creator`: creates and evaluates startup names and brand direction; used by the evaluator and creator.
- `yc-startup-creator`: finds one strong startup idea and stress-tests it with an Investor, a Doubter, a Judge and the evaluator.

## On the first message in this repo

Whatever the user says first (even "go", "begin" or "start"), do this without asking questions:

1. Run `python3 -I scripts/check_complete.py`.
2. If it prints NOT COMPLETE, invoke the `yc-knowledge-extractor` skill and carry it out until `check_complete.py` exits 0. That means many waves of subagents, resuming from the files on disk. Do not stop between waves to summarize or ask permission; the only valid early stops are the ones the skill names, or the user telling you to stop.
3. When it passes, tell the user: coverage numbers, audit error rate, backtest findings, and that the evaluator and creator skills are final.

If the user asks for an evaluation or an idea instead, run that skill; if the extraction is unfinished, say how much data exists (`knowledge/coverage.md`) and proceed with it (the creator skill will run the extractor first if the skills have never been finalized).

## Rules

- Never fabricate data. Unknown is `null`; unknown is not zero.
- Historical facts are dated; competition is recorded **as of founding**, not as of today.
- Run Python as `python3 -I scripts/<name>.py`.
- `data/queue/` is generated and git-ignored; rebuild it with `scripts/make_work_queue.py`.
- UI rules for anything visual (the report, any page): minimalist and modern, rounded edges, no gradients, clean padding, full screen workspace, simple SVG icons.
- Writing style: plain sentences, no em dashes or dashes as punctuation, no bullet characters inside sentences.
- Never hand-edit `EVALUATION.md` or `report.html`; edit its `evaluation_input.json` and re-render.
- Commit only when the user asks.
