<p align="center">
  <img src="assets/brand/logo.svg" alt="Will I Raise logo" width="72">
</p>

<h1 align="center">Will I Raise</h1>

<p align="center">
  A Claude Code skill that tells you your odds of getting into Y Combinator and raising each round, using every past YC company as the evidence.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-F26625" alt="License: MIT">
  <img src="https://img.shields.io/badge/python-3.9%2B-F26625" alt="Python 3.9 or newer">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-F26625" alt="Platforms: macOS, Linux, Windows">
</p>

## What it does

Describe your startup to Claude and ask whether you will raise. The skill returns the chance of getting into YC, then the odds of reaching Seed, Series A, Series B and Series C or later, with a likely raise and valuation for each and a paragraph on why it fails at each step. It also finds startup ideas, names a startup, and makes logos.

It does this by comparing you with the 6,399 companies in the public YC directory. Each one was researched for its timeline, funding rounds, founders, competitors at the time it started, how hard it was to build, why it won or failed, and how strong its name was. Where the data is missing, the answer says so.

Five skills ship in `.claude/skills/`:

- **Evaluator.** Give it a startup. You get a short text answer and one standalone `report.html`.
- **Creator.** Finds one startup idea and attacks it with an Investor, a Doubter and a Judge until the Judge would invest.
- **Name creator.** Makes and scores startup names and rates the brand. The other two call it.
- **Logo creator.** Give it a company name and the AI designs original logos from the researched examples. You get one HTML file with PNG export. It contains no templates.
- **Extractor.** Built the dataset. You only need it to refresh the data.

## For AI agents: what each skill does and what it returns

If you are an agent working in this repo, read `CLAUDE.md` first. Pick the skill by the user's request, run it as written in its `SKILL.md`, and hand back the files listed below. Run Python as `python3 -I scripts/<name>.py` (standard library only).

| Skill | Use it when the user asks to | You return |
|---|---|---|
| `yc-startup-evaluator` | Evaluate a startup, forecast its YC chance, raises and valuations, or stress test it ("Will I raise?") | A short text summary and one standalone `evaluations/<name>/report.html` (also `EVALUATION.md`). Never hand edit these. Edit `evaluation_input.json` and re-render with `scripts/render_eval.py`. |
| `yc-startup-creator` | Find or generate a startup idea | One idea that survived an Investor, a Doubter, a Judge and the evaluator, plus its evaluation report. |
| `yc-name-creator` | Name a startup or judge a name | Ranked name options with a brand assessment. The evaluator and creator also call it. |
| `yc-logo-creator` | Make a logo, logo ideas or a brand mark | One self contained `logo-studio.html` (see below). |
| `yc-knowledge-extractor` | Refresh or finish the dataset | Nothing to the user until `python3 -I scripts/check_complete.py` exits 0. It resumes from files on disk. |

On the first message in a fresh clone, run `python3 -I scripts/check_complete.py`. It currently reports the extraction as complete, so go straight to the user's request.

### The logo creator in detail (AI designed marks only, no templates)

**Every logo in the final HTML is designed by the AI for that request. The file contains no templates, no preset shapes and no logo generator.** The builder refuses to run unless the agent supplies its own marks, and the studio only places those marks with fonts and colors and exports them.

The agent studies the researched examples first. Read `knowledge/logo_patterns.md` and sample `knowledge/logo_examples.json` (598 labeled YC and big brand logos). Then write 50 to 100 original marks as SVG into a `marks.json` list (100 by 100 box, color tokens `{A}` `{B}` `{C}`, no gradients, no text, each mark must still read when all three tokens are one color). Do not copy any one logo, do not reuse marks from an earlier run, and do not draw the company name. Build with:

```bash
python3 -I scripts/build_logo_studio.py --name "Acme" --marks marks.json --out logo-studio.html
```

Without `--marks` the build fails on purpose. Look at a screenshot of each tab and drop weak marks before handing the file over. Optional flags are `--fg "#14110F"` for the object color and `--bg "#FFFFFF"` for the background. The output is one HTML file of about 640 KB. It works offline, with 27 open licensed fonts embedded, and needs no server. Give that file to the user and tell them how to use it:

- **Four tabs.** Object (one flat object, one color, one background). Object and name (the object beside or above the name). Name only (the name with a small AI designed object built into the type). Multicolor (the AI's objects with three preset colors; 20 presets, plus a picker for each single color).
- **Controls.** Show 50 or 100 options. Shuffle reorders the AI's marks and pairs them with new fonts.
- **Original work only.** All objects come from the AI's own designs, informed by the examples. The company name only sets the text and never changes the objects.
- **Export.** Click a logo, choose a transparent or colored background, set the size (default 1024 by 1024), then Download PNG. SVG saves one logo. All SVGs saves every option in the tab as a zip.

The design rules come from `knowledge/logo_patterns.md`, a study of 490 YC logos and 108 big brand marks: most are one flat object, two colors or fewer, no gradient, with clean sans serif type. The labels come from a vision model, so treat the shares as rough. The skill does not check trademarks. To change the look, edit `scripts/logo_studio_template.html` or `scripts/logo_studio_engine.js` and rebuild. Do not hand edit the generated file.

## Screenshots

<p align="center">
  <img src="assets/screenshots/overview.png" alt="Report overview: YC chance, most likely stopping stage, similar companies and step by step odds" width="100%">
</p>

<table>
  <tr>
    <td width="50%"><img src="assets/screenshots/compare.png" alt="Comparison chart of similar YC companies with logos, smooth curves and a draggable timeline"><br><sub>Compare: similar YC companies on one timeline. Click one to highlight it, drag to see who had died by then.</sub></td>
    <td width="50%"><img src="assets/screenshots/walkthrough.png" alt="Walkthrough: a simulated run that rises through each round and then crashes"><br><sub>Walkthrough: press the arrow and the startup rises or crashes at each step, using the evaluation's odds.</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/screenshots/possibilities.png" alt="Possibilities tree showing every path from YC acceptance to each funding round"><br><sub>Possibilities: a tree of every way it can go, with the odds on each branch.</sub></td>
    <td width="50%"><img src="assets/screenshots/roadmap.png" alt="Roadmap in dark mode with goals, actions and proof for each step"><br><sub>Roadmap, in dark mode: what to do to reach each step, and how you know it worked.</sub></td>
  </tr>
</table>

The screenshots show an illustrative example (a made up startup called Pagewise) in `evaluations/example-pagewise/`. Its probabilities are set by hand to show the format and are not calibrated. The ten comparison companies on its chart are real researched YC records.

The Funding tab also has a raise calculator. Type how much you want to raise and the valuation cap, for example 50K on a 1M cap, and it shows the share of the company you sell (5% in that case) and where your cap sits against the seed range in the report.

## Technical details

| Part | Where |
|---|---|
| Skills | `.claude/skills/` (`yc-startup-evaluator`, `yc-startup-creator`, `yc-name-creator`, `yc-logo-creator`, `yc-knowledge-extractor`) |
| Company records | `data/enrichment/<slug>.json`, schema in `docs/schema.md` |
| Directory snapshot | `data/raw/yc_all.json`, `data/companies.csv` |
| Knowledge files and tables | `knowledge/` and `knowledge/tables/` |
| Backtest | `knowledge/backtest.md`, `evaluations/backtest-*` |
| Name features | `scripts/name_features.py`, `data/name_features.csv`, `knowledge/tables/name_outcomes.csv` |
| Evaluation input and render | `scripts/evalcore.py`, `scripts/render_eval.py`, `scripts/check_eval.py` |
| HTML report | `scripts/render_html.py`, `scripts/report_template.html` |
| Logo studio | `python3 -I scripts/build_logo_studio.py --name "Acme"` builds one HTML file from the AI's own marks (`--marks`) with PNG export (research in `knowledge/logo_patterns.md`) |
| Landing page | `site/index.html` (one file, open it in a browser; images in `site/img/`) |
| Settings | `config.json` |

Rules the data follows:

- Unknown is `null`, never zero. Each record states how complete its funding data is, and base rates report a lower, known-only and upper range.
- Every fact is dated. Competitors are recorded as of the YC batch, not as of today.
- A round reported by a single database or outlet is recorded with its source and flagged in `notes` as resting on one source.
- Python only, standard library only. Run scripts as `python3 -I scripts/<name>.py`.

The HTML report has eight tabs: Overview, Compare, Walkthrough, Possibilities, Funding, Roadmap, Insights, and Pros and cons. It is one file with no dependencies. Data, styles, scripts and company logos are embedded. Logos are downloaded once from the public YC directory and cached in `data/logo_cache/`. If a logo cannot be fetched, the page shows a letter badge.

## How the data was built

1. **Research.** The extractor skill worked through the directory in waves of subagents, 8 companies per shard, calibration sample first (about 10% of every batch, picked by a fixed hash, so base rates are not built from hand picked winners). Each company is one JSON file in `data/enrichment/`.
2. **Audit.** Independent agents re-opened the cited sources for samples from every wave and the findings were corrected. Results are in `knowledge/audit_log.md`.
3. **Derive.** Scripts turn the records into base rates and benchmark tables, and six knowledge files are written from them.
4. **Finalize and backtest.** The knowledge is copied into each skill's `references/` folder, and the evaluator was tested on six calibration companies as if it were their batch date. Findings are in `knowledge/backtest.md`.

## Status and limits

Coverage is in `knowledge/coverage.md`. Every company in the directory was researched except one, marked unresearchable with a reason. Many records have thin funding data, because small and old companies leave little public trace. The last audit of 36 fresh records found a clear error or a missing sourced fact in 9.4 percent of 245 fields checked (the bar was 10 percent); the sample is small, so treat that as a rough measure. `scripts/check_complete.py` is the gate for whether the dataset counts as finished, and `knowledge/audit_log.md` records how accurate the audits found it.

- The evaluator's odds are calibrated judgments anchored on past companies, not statistical predictions. Past YC companies are survivors of a selection process.
- The backtest covers six companies, so it shows direction and not measured error. It found the evaluator too pessimistic about niche sounding B2B companies.
- Funding amounts and valuations are often not public. On the comparison chart, valuation data is sparse, so it defaults to total raised when fewer than three companies have a reported valuation.
- Branding evidence is thin for small companies. Most have no press about their own brand, so name origins are mostly `null`.
- Name statistics are confounded with industry and era. They help catch outliers and do not pick winners.

## How to start

You need Python 3.9 or newer and [Claude Code](https://claude.com/claude-code). The logo studio also works in any browser.

```bash
git clone https://github.com/edison16a/yc-startup-life
cd yc-startup-life
claude
```

Then ask in plain words:

- "Will I raise? My startup is ..." runs the evaluator and gives you the text answer plus `report.html`.
- "Find me a startup idea." runs the creator.
- "Name my startup" or "Is this a good name: ..." runs the name creator.
- "Make me logos for Acme" runs the logo creator and gives you `logo-studio.html`.

To open a report, double click `evaluations/<name>/report.html`. To refresh the dataset, ask Claude to run the extractor skill; it resumes from the files on disk.

## License

MIT. See `LICENSE`.
