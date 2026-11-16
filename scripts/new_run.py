#!/usr/bin/env python3
"""Create runs/<date>-<n>/ with the folder layout the creator skill expects, and print its path."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import datetime, json
from common import ROOT


def main():
    base = ROOT / "runs"
    base.mkdir(exist_ok=True)
    today = datetime.date.today().isoformat()
    n = 1
    while (base / f"{today}-{n}").exists():
        n += 1
    run = base / f"{today}-{n}"
    for d in ("evidence", "briefs", "debate", "evaluation"):
        (run / d).mkdir(parents=True)
    (run / "candidates.md").write_text("# Candidates\n\n(25+ niches: customer, painful job, how solved today, why now.)\n")
    (run / "rejected.md").write_text("# Rejected ideas\n\n| Idea | Cycle | Reason |\n|---|---|---|\n")
    (run / "progress.md").write_text("# Run progress\n\n| Cycle | Stage | Notes |\n|---|---|---|\n")
    (run / "state.json").write_text(json.dumps({"cycle": 1, "status": "in_progress"}, indent=1))
    print(run)


if __name__ == "__main__":
    main()
