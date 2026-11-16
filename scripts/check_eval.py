#!/usr/bin/env python3
"""Check an evaluation folder: input valid, analog slugs real, EVALUATION.md and report.html present and in sync with the input.

  python3 -I scripts/check_eval.py evaluations/<name>      exit 0 = OK
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))  # work under python3 -I
import evalcore, render_html


def check(d):
    d = _pl.Path(d)
    problems = []
    try:
        inp = evalcore.load_input(d)
    except Exception as e:
        return [f"cannot read evaluation_input.json: {e}"]
    err, _ = evalcore.validate(inp)
    problems += err
    md = d / "EVALUATION.md"
    if not md.exists():
        problems.append("EVALUATION.md missing: run scripts/render_eval.py")
    elif not err and md.read_text() != evalcore.render(inp, evalcore.compute(inp)):
        problems.append("EVALUATION.md is out of sync with evaluation_input.json: re-run scripts/render_eval.py (never edit it by hand)")
    rep = d / "report.html"
    if not rep.exists():
        problems.append("report.html missing: run scripts/render_eval.py")
    elif not err:
        text = rep.read_text(encoding="utf-8")
        m = __import__("re").search(r'<script type="application/json" id="data">(.*?)</script>', text, __import__("re").S)
        try:
            data = __import__("json").loads(m.group(1)) if m else None
        except Exception:
            data = None
        want = render_html.build_data(inp, evalcore.compute(inp), want_logos=False)
        if not data:
            problems.append("report.html has no embedded data block: re-run scripts/render_eval.py")
        elif abs(data["yc"]["p"] - want["yc"]["p"]) > 1e-9 or [s["p_given_yc"] for s in data["stages"]] != [s["p_given_yc"] for s in want["stages"]] or data["startup"]["name"] != want["startup"]["name"]:
            problems.append("report.html is out of sync with evaluation_input.json: re-run scripts/render_eval.py (never edit it by hand)")
    return problems


def main():
    if len(_sys.argv) != 2:
        print(__doc__); return 1
    problems = check(_sys.argv[1])
    for p in problems:
        print("PROBLEM:", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    _sys.exit(main())
