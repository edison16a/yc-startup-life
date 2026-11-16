#!/usr/bin/env python3
"""Create an evaluation folder with a blank evaluation_input.json.

  python3 -I scripts/new_eval.py <startup-slug> [--mode full|summary] [--out DIR]
Default folder: evaluations/<startup-slug>-<date>. Prints the path.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import argparse, datetime, json
from common import ROOT


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--mode", default="full", choices=["full", "summary"])
    ap.add_argument("--out")
    a = ap.parse_args()
    d = _pl.Path(a.out) if a.out else ROOT / "evaluations" / f"{a.slug}-{datetime.date.today().isoformat()}"
    d.mkdir(parents=True, exist_ok=True)
    t = json.loads((ROOT / "docs" / "eval-input-template.json").read_text())
    t["mode"] = a.mode
    t["startup"]["as_of"] = datetime.date.today().isoformat()
    (d / "evaluation_input.json").write_text(json.dumps(t, indent=2))
    print(d)


if __name__ == "__main__":
    main()
