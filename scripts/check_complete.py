#!/usr/bin/env python3
"""The master gate: is the extraction finished and are the evaluator and creator skills final?

  python3 -I scripts/check_complete.py            exit 0 only when everything below passes
  python3 -I scripts/check_complete.py --json

Gates: every company researched at depth 2 (or listed in data/unresearchable.csv with a reason); calibration sample
complete; all records valid; audit passed; advice corpus size; derived knowledge files and tables exist;
skill references finalized against the current data.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import csv, json, re, subprocess
from common import ROOT, DATA, KNOW, CONFIG, load_companies, load_enrichment, load_unresearchable

KNOWLEDGE_FILES = ["patterns.md", "failure_modes.md", "yc_acceptance.md", "stage_benchmarks.md", "incumbent_and_complexity.md", "naming.md"]
TABLES = ["stage_progression.csv", "round_benchmarks.csv", "time_to_milestones.csv", "status_mix.csv",
          "factor_outcomes.csv", "failure_factor_counts.csv", "success_factor_counts.csv", "name_outcomes.csv"]


def main():
    ex = CONFIG["extraction"]
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    companies = load_companies()
    enr = load_enrichment(min_depth=2)
    unres = load_unresearchable()
    total = len(companies)
    bad_unres = [s for s in unres if s not in companies]
    done = len(set(enr) | (set(unres) & set(companies)))
    add("every company researched (depth 2) or marked unresearchable", done == total and not bad_unres,
        f"{len(enr)} researched + {len(unres)} unresearchable of {total}; {total - done} remaining")
    cal = [r["slug"] for r in csv.DictReader((DATA / "calibration_sample.csv").open())] if (DATA / "calibration_sample.csv").exists() else []
    cal_missing = [s for s in cal if s not in enr and s not in unres]
    add("calibration sample complete", bool(cal) and not cal_missing, f"{len(cal) - len(cal_missing)}/{len(cal)}")
    if unres and len(unres) / total > 0.05:
        add("unresearchable share <= 5%", False, f"{len(unres)} of {total}")
    r = subprocess.run([_sys.executable, "-I", str(ROOT / "scripts" / "merge_enrichment.py")], capture_output=True, text=True)
    add("all enrichment records valid", r.returncode == 0, "" if r.returncode == 0 else r.stderr.strip().splitlines()[0][:200] if r.stderr.strip() else "merge failed")
    audit = KNOW / "audit_log.md"
    add("audit passed", audit.exists() and "AUDIT RESULT: PASS" in audit.read_text(), "knowledge/audit_log.md must end with 'AUDIT RESULT: PASS'")
    advice = [p for p in (KNOW / "advice").glob("*.md") if p.name != "sources.md"]
    types = [re.search(r"(?mi)^type:\s*(\w+)", p.read_text()) for p in advice]
    n_app = sum(1 for m in types if m and m.group(1).lower() == "applicant_account")
    add(f"advice notes >= {ex['advice_sources_min']}", len(advice) >= ex["advice_sources_min"], f"{len(advice)} notes")
    add(f"applicant accounts >= {ex['applicant_accounts_min']}", n_app >= ex["applicant_accounts_min"], f"{n_app} (notes need a 'type: applicant_account' line)")
    bt = KNOW / "backtest.md"
    add("backtest written (knowledge/backtest.md, >= 150 words)", bt.exists() and len(re.findall(r"\w+", bt.read_text())) >= 150)
    for f in KNOWLEDGE_FILES:
        p = KNOW / f
        n = len(re.findall(r"\w+", p.read_text())) if p.exists() else 0
        add(f"knowledge/{f} written (>= 250 words)", n >= 250, f"{n} words")
    for t in TABLES:
        p = KNOW / "tables" / t
        add(f"tables/{t} present", p.exists() and p.stat().st_size > 0)
    for skill in ("yc-startup-evaluator", "yc-startup-creator", "yc-name-creator"):
        p = ROOT / ".claude" / "skills" / skill / "references" / "_finalized.json"
        if not p.exists():
            add(f"{skill} finalized", False, "run scripts/finalize_skills.py")
        else:
            st = json.loads(p.read_text())
            add(f"{skill} finalized against current data", st.get("depth2") == len(enr), f"stamp {st.get('depth2')} vs current {len(enr)}")
    ok = all(c["ok"] for c in checks)
    if "--json" in _sys.argv:
        print(json.dumps({"complete": ok, "checks": checks}, indent=1))
    else:
        for c in checks:
            print(f"[{'x' if c['ok'] else ' '}] {c['check']}" + (f"  ({c['detail']})" if c["detail"] else ""))
        print("\nCOMPLETE: extraction finished and skills are final." if ok else "\nNOT COMPLETE: continue the extractor skill from the first unchecked item.")
    return 0 if ok else 1


if __name__ == "__main__":
    _sys.exit(main())
