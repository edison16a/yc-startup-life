---
name: yc-logo-creator
description: Create logo options for a startup from the user's company name. Builds one self contained HTML logo studio with 100 generated options in four sections (object only, object plus name, name only, multicolor object), color pickers, and PNG download at any size with a transparent or colored background. Use when asked for a logo, logo ideas, or a brand mark.
---

# YC logo creator

Turn a company name into one HTML file full of simple, modern logo options, modeled on what successful YC companies and big brands actually use.

## What good looks like (from `knowledge/logo_patterns.md`)

Researched from 490 YC logos and 108 big brand marks.

1. Simple. Most marks are one flat object, two colors or fewer (68% of YC logos), no gradient (86%).
2. Mostly symbol led. Symbol only 79%, wordmark only 14%, symbol plus word 7% in the YC sample.
3. The object is a letterform, an abstract geometric shape, or a simple picture. Containers (square, circle, rounded square) wrap about half of them.
4. Type is a clean sans serif. Custom display lettering is rare.
5. The object usually has no link to the name. Do not draw the name's meaning or its initial.

## How to run it

1. Take the company name from the user. Optionally ask for the field (tech, health, consumer) and whether they want a particular color. Do not ask more than that.
2. Build the file:

```bash
python3 -I scripts/build_logo_studio.py --name "Acme" --out logo-studio.html
```

Optional flags: `--fg "#14110F"` for the object color and `--bg "#FFFFFF"` for the background.
3. Give the user `logo-studio.html`. It is one file, works offline, and embeds 27 open licensed fonts (SIL OFL, from Fontsource) in `assets/fonts/`.
4. Tell the user how to use it, in plain sentences:
   - Four tabs: Object (one color on one background), Object and name, Name only (with a small object built into the type), Multicolor (three preset colors per object, with 20 presets and a picker for each single color).
   - 50 or 100 options, a Field switch (Any, Tech, Health, Consumer) and Shuffle for a new set.
   - Click a logo, choose Transparent background or a background color, set the size (default 1024 by 1024), then Download PNG. SVG downloads one logo, All SVGs downloads the whole tab as a zip.

## Rules

- The name only sets the text. Objects are generated from scratch on every open and every Shuffle, from design rules and a random seed. Nothing is a stored preset or image, and the name never changes them.
- Do not add gradients, drop shadows or more than three colors.
- Do not claim a generated mark is unique or trademark safe. Say a trademark search is the user's job.
- Never hand edit the generated HTML. Edit `scripts/logo_studio_template.html` or `scripts/logo_studio_engine.js` and rebuild.
- If you change the research (`knowledge/logo_patterns.md`), update the numbers above.

## Files

| File | Purpose |
|---|---|
| `scripts/build_logo_studio.py` | Builds the single HTML file (stdlib only) |
| `scripts/logo_studio_template.html` | Layout and styling, same look as the report |
| `scripts/logo_studio_engine.js` | 20 object families, wordmark treatments, lockups, export |
| `assets/fonts/` | Embedded fonts, SIL Open Font License |
| `knowledge/logo_patterns.md` | The research |
