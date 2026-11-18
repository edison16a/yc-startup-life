#!/usr/bin/env python3
"""Build one self contained logo studio HTML file.

Usage: python3 -I scripts/build_logo_studio.py --name "Acme" --marks marks.json --out logo-studio.html
Stdlib only. Fonts (OFL licensed) are embedded as base64 so the file works offline.
"""
import argparse, base64, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / ".claude/skills/yc-logo-creator/assets/fonts"
CLS = {"mono": "mono", "serif": "serif", "fraunces": "serif", "playfair": "serif", "instrument": "serif"}
SPECIAL = {"dm": "DM", "ibm": "IBM"}


def family(slug):
    return " ".join(SPECIAL.get(p, p.capitalize()) for p in slug.split("-"))


def fonts():
    out = []
    for p in sorted(FONT_DIR.glob("*.woff2")):
        m = re.match(r"(.+)-(\d+)$", p.stem)
        slug, w = m.group(1), int(m.group(2))
        cls = "mono" if "mono" in slug else "serif" if any(k in slug for k in ("serif", "fraunces", "playfair", "instrument")) else "sans"
        out.append({"id": p.stem, "family": family(slug), "weight": w, "cls": cls, "b64": base64.b64encode(p.read_bytes()).decode()})
    return out


BAD = re.compile(r"<script|<foreignObject|<image|<use|\bon\w+\s*=|href\s*=|javascript:|url\((?!#|\\\"#|'#)|@import", re.I)


def load_marks(path):
    if not path:
        raise SystemExit("--marks is required. The studio contains no built in logo templates: the AI must design the marks (see .claude/skills/yc-logo-creator/SKILL.md).")
    marks = json.loads(Path(path).read_text())
    if not isinstance(marks, list) or not all(isinstance(m, str) for m in marks):
        raise SystemExit("marks file must be a JSON list of SVG strings")
    for i, m in enumerate(marks):
        if BAD.search(m):
            raise SystemExit(f"mark {i} uses a disallowed element or attribute")
        if "{A}" not in m:
            raise SystemExit(f"mark {i} must use the {{A}} color token")
    if len(marks) < 12:
        raise SystemExit(f"only {len(marks)} marks. Design at least 12, ideally 50 to 100.")
    if len(marks) < 50:
        print(f"warning: only {len(marks)} marks. The Object and Multicolor tabs will show {len(marks)} options.")
    return marks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="Acme")
    ap.add_argument("--fg", default="#14110F")
    ap.add_argument("--bg", default="#FFFFFF")
    ap.add_argument("--marks", help="JSON list of agent designed SVG marks (100 x 100 box, colors {A} {B} {C}, ids {U})")
    ap.add_argument("--out", default="logo-studio.html")
    a = ap.parse_args()
    here = Path(__file__).resolve().parent
    html = (here / "logo_studio_template.html").read_text()
    engine = (here / "logo_studio_engine.js").read_text()
    fs = fonts()
    if not fs:
        raise SystemExit("no fonts found in " + str(FONT_DIR))
    marks = load_marks(a.marks)
    html = (html.replace("__CUSTOM__", json.dumps(marks)).replace("__FONTS__", json.dumps(fs)).replace("__DEFAULT_NAME__", json.dumps(a.name))
            .replace("__DEFAULT_FG__", json.dumps(a.fg)).replace("__DEFAULT_BG__", json.dumps(a.bg)))
    html = html.replace("__ENGINE__", engine.replace("</script", "<\\/script"))
    Path(a.out).write_text(html)
    print(f"wrote {a.out} ({len(html)//1024} KB, {len(fs)} fonts)")


if __name__ == "__main__":
    main()
