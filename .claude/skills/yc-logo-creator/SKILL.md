---
name: yc-logo-creator
description: Create logo options for a startup from the user's company name. The AI designs every mark from scratch, then builds one self contained HTML logo studio in four sections (object only, object plus name, name only, multicolor object), color pickers, and PNG download at any size with a transparent or colored background. Use when asked for a logo, logo ideas, or a brand mark.
---

# YC logo creator

**The final HTML contains no templates and no preset shapes. Every object in it was designed by the AI for this request.** The builder refuses to run without the AI's marks (`--marks`), and the file has no logo generator code in it. The studio only arranges the AI's marks with fonts and colors and exports them.

Turn a company name into one HTML file full of simple, modern logo options, modeled on what successful YC companies and big brands actually use.

## What good looks like (from `knowledge/logo_patterns.md`)

Researched from 490 YC logos and 108 big brand marks.

1. Simple. Most marks are one flat object, two colors or fewer (68% of YC logos), no gradient (86%).
2. Mostly symbol led. Symbol only 79%, wordmark only 14%, symbol plus word 7% in the YC sample.
3. The object is a letterform, an abstract geometric shape, or a simple picture. Containers (square, circle, rounded square) wrap about half of them.
4. Type is a clean sans serif. Custom display lettering is rare.
5. The object usually has no link to the name. Do not draw the name's meaning or its initial.

## How to run it

The agent designs every logo. There is no generator and no fallback: the build fails without the agent's marks.

1. Take the company name from the user. Optionally ask for the field and a preferred color. Ask nothing else.
2. Study the examples. Read `knowledge/logo_patterns.md`. Open `knowledge/logo_examples.json` (598 labeled logos: composition, symbol kind, container, colors, complexity, a one line trait). Filter it to the user's field or to the strongest patterns, and read 30 or more rows. To look at an actual YC logo, fetch its `small_logo_thumb_url` from `data/raw/yc_all.json`. Learn the pattern, do not copy any one logo.
3. Design 50 to 100 original marks as SVG, using what you learned: one flat object, simple geometry, two or three colors, optional container, clean negative space. Vary the idea (abstract geometry, simplified pictorial, negative space cuts, lines or bars, tiles, letterforms that are not the company's initial). The object must not spell or depict the company name. Write them as a JSON list of strings in `marks.json`:
   - Draw in a 100 by 100 box.
   - Use color tokens `{A}` (main), `{B}` and `{C}` (extra colors). The Object and Object and name tabs paint all three tokens in one color, so a mark must still read when `{A}`, `{B}` and `{C}` are identical: leave gaps between shapes, or use a mask cut out, instead of drawing `{B}` on top of `{A}`. About half the marks should use `{B}` or `{C}` so the Multicolor tab has real color.
   - For a cut out, use a mask with the id `m{U}` (`{U}` becomes a unique id).
   - No gradients, text, images, scripts or external links. The builder rejects them.
   - At least 12 marks are required, and 50 or more fill the Object and Multicolor tabs. The Object and name and the Name only tabs reuse your marks with different fonts, so they always show the full count.
4. Build the file:

```bash
python3 -I scripts/build_logo_studio.py --name "Acme" --marks marks.json --out logo-studio.html
```

Optional flags: `--fg`, `--bg`. Never copy marks from an earlier run or from a file in the repo: design new ones every time.
5. Check the result. Open the file in a browser (Playwright is available), look at a screenshot of each tab, and delete or redraw marks that look cluttered, lopsided, collapse in one color, or look like a famous logo. Rebuild.
6. Give the user `logo-studio.html`. It is one offline file with 27 open licensed fonts (SIL OFL, Fontsource) embedded. Explain, in plain sentences:
   - Four tabs: Object (one color on one background), Object and name, Name only (with a small object built into the type), Multicolor (three preset colors per object, 20 presets, a picker for each color).
   - 50 or 100 options, and Shuffle, which reorders the AI's marks and pairs them with new fonts.
   - Every logo in the file is original AI work for this request. There are no built in templates.
   - Click a logo, pick Transparent background or a color, set the size (default 1024 by 1024), then Download PNG. SVG saves one logo and All SVGs saves the tab as a zip.

## Rules

- The name only sets the text. Agent designed marks are made from the examples and the rules, never from the name. Objects are generated from scratch on every open and every Shuffle, from design rules and a random seed. Nothing is a stored preset or image, and the name never changes them.
- Do not add gradients, drop shadows or more than three colors.
- Do not claim a generated mark is unique or trademark safe. Say a trademark search is the user's job.
- Never hand edit the generated HTML. Edit `scripts/logo_studio_template.html` or `scripts/logo_studio_engine.js` and rebuild.
- If you change the research (`knowledge/logo_patterns.md`), update the numbers above.

## Files

| File | Purpose |
|---|---|
| `scripts/build_logo_studio.py` | Builds the single HTML file (stdlib only) |
| `scripts/logo_studio_template.html` | Layout and styling, same look as the report |
| `scripts/logo_studio_engine.js` | Layout only: places the AI's marks with fonts and colors, and exports. Contains no logo shapes |
| `assets/fonts/` | Embedded fonts, SIL Open Font License |
| `knowledge/logo_patterns.md` | The research summary |
| `knowledge/logo_examples.json` | The 598 labeled example logos the agent studies |
