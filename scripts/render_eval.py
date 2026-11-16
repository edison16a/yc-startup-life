#!/usr/bin/env python3
"""Validate <dir>/evaluation_input.json, compute odds and labels, write <dir>/EVALUATION.md and evaluation_computed.json.

  python3 -I scripts/render_eval.py evaluations/<name>
Exit 1 and print every problem if the input is invalid. Never edit EVALUATION.md by hand: edit the JSON and re-run.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import json
import evalcore


def main():
    if len(_sys.argv) != 2:
        print(__doc__); return 1
    d = _pl.Path(_sys.argv[1])
    try:
        inp = evalcore.load_input(d)
    except Exception as e:
        print(f"cannot read {d}/evaluation_input.json: {e}"); return 1
    err, warn = evalcore.validate(inp)
    for w in warn:
        print("warn:", w)
    if err:
        for e in err:
            print("ERROR:", e)
        print(f"{len(err)} problem(s); EVALUATION.md not written")
        return 1
    comp = evalcore.compute(inp)
    (d / "evaluation_computed.json").write_text(json.dumps(comp, indent=1))
    (d / "EVALUATION.md").write_text(evalcore.render(inp, comp))
    print(f"wrote {d}/EVALUATION.md")
    print(f"YC acceptance {evalcore.pf(comp['p_yc'])} ({comp['label_yc']})")
    for st in comp["stages"]:
        print(f"  {st['stage']:<14} reach|in YC {evalcore.pf(st['p_stage_given_yc']):>6}  from today {evalcore.pf(st['p_stage_from_today']):>6}")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
