#!/usr/bin/env python3
"""Make the evaluator and creator skills self-contained: refresh tables, copy the distilled knowledge into each
skill's references/ folder, and stamp them. Run after the knowledge files exist (extractor Stage 4).

  python3 -I scripts/finalize_skills.py
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import datetime, json, shutil, subprocess
from common import ROOT, KNOW, DATA, load_companies, load_enrichment, load_unresearchable

REQUIRED_KNOWLEDGE = ["patterns.md", "failure_modes.md", "yc_acceptance.md", "stage_benchmarks.md", "incumbent_and_complexity.md"]
SKILLS = ROOT / ".claude" / "skills"
TARGETS = {
    "yc-startup-evaluator": {"knowledge": REQUIRED_KNOWLEDGE + ["coverage.md"],
                             "tables": "all", "extra": [("docs/taxonomy.md", "taxonomy.md"), ("knowledge/advice/sources.md", "advice_sources.md")]},
    "yc-startup-creator": {"knowledge": ["patterns.md", "failure_modes.md", "yc_acceptance.md", "incumbent_and_complexity.md", "coverage.md"],
                           "tables": ["stage_progression.csv", "factor_outcomes.csv", "failure_factor_counts.csv", "success_factor_counts.csv", "status_mix.csv"],
                           "extra": [("docs/taxonomy.md", "taxonomy.md"), ("knowledge/advice/sources.md", "advice_sources.md")]},
}


def main():
    missing = [f for f in REQUIRED_KNOWLEDGE if not (KNOW / f).exists() or not (KNOW / f).read_text().strip()]
    if missing:
        print("Cannot finalize. Missing knowledge files:", ", ".join(f"knowledge/{m}" for m in missing)); return 1
    for cmd in (["merge_enrichment.py"], ["base_rates.py", "--write-tables"]):
        r = subprocess.run([_sys.executable, "-I", str(ROOT / "scripts" / cmd[0])] + cmd[1:], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"{cmd[0]} failed:\n{r.stdout[-1500:]}\n{r.stderr[-1500:]}"); return 1
    companies, enr = load_companies(), load_enrichment(min_depth=2)
    cal = {l.split(",")[0] for l in (DATA / "calibration_sample.csv").read_text().splitlines()[1:]} if (DATA / "calibration_sample.csv").exists() else set()
    stamp = {"finalized": datetime.date.today().isoformat(), "companies_total": len(companies), "depth2": len(enr),
             "unresearchable": len(load_unresearchable()), "calibration_done": sum(1 for s in cal if s in enr), "calibration_total": len(cal)}
    for skill, spec in TARGETS.items():
        ref = SKILLS / skill / "references"
        shutil.rmtree(ref, ignore_errors=True)
        (ref / "tables").mkdir(parents=True)
        copied = []
        for k in spec["knowledge"]:
            shutil.copy(KNOW / k, ref / k); copied.append(k)
        tdir = KNOW / "tables"
        names = [p.name for p in tdir.glob("*.csv")] if spec["tables"] == "all" else spec["tables"]
        for t in names:
            if (tdir / t).exists():
                shutil.copy(tdir / t, ref / "tables" / t); copied.append(f"tables/{t}")
        for src, dst in spec["extra"]:
            if (ROOT / src).exists():
                shutil.copy(ROOT / src, ref / dst); copied.append(dst)
        (ref / "_finalized.json").write_text(json.dumps({**stamp, "files": copied}, indent=1))
        print(f"finalized {skill}: {len(copied)} reference files")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
