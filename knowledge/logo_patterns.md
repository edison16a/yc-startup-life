# Logo patterns

Research behind the `yc-logo-creator` skill. Source: 490 YC company logos (the 222 companies with the strongest valuation evidence in this knowledge base plus well known YC companies up to 503 targets, 490 logos downloaded) and 108 big brand marks (including NASA and NVIDIA), downloaded as monochrome glyphs from simple-icons.

## Method and limits

Each logo was placed on a contact sheet and classified by a vision model, one sheet of 30 per subagent. Labels are judgments, so treat shares as roughly plus or minus 5 points. Big brand glyphs are single color by construction, so color and gradient shares for them say nothing. Valuation data is sparse, so the YC set mixes confirmed 100 million plus companies with well known proxies. Nothing here is a claim about what makes a company succeed, only what successful brands look like.

## YC logos (n=490)

### Composition
| value | n | share |
|---|---|---|
| symbol_only | 387 | 79% |
| wordmark_only | 67 | 14% |
| symbol_plus_word | 36 | 7% |

### Symbol kind
| value | n | share |
|---|---|---|
| letterform | 139 | 28% |
| abstract_geometric | 119 | 24% |
| pictorial | 97 | 20% |
| none | 69 | 14% |
| lines_or_bars | 27 | 6% |
| negative_space | 25 | 5% |
| ring_or_circle | 14 | 3% |

### Container
| value | n | share |
|---|---|---|
| none | 205 | 42% |
| square | 193 | 39% |
| circle | 50 | 10% |
| rounded_square | 37 | 8% |
| other | 4 | 1% |
| ring_or_circle | 1 | 0% |

### Colors used
| value | n | share |
|---|---|---|
| 2 | 259 | 53% |
| 3 | 109 | 22% |
| 1 | 76 | 16% |
| 4 | 34 | 7% |
| 5 | 10 | 2% |
| 6 | 1 | 0% |
| 7 | 1 | 0% |

Gradient used: 14%. Two colors or fewer: 68%. Three or fewer: 91%.

### Complexity (1 simplest, 5 most detailed)
| value | n | share |
|---|---|---|
| 3 | 209 | 43% |
| 2 | 165 | 34% |
| 4 | 67 | 14% |
| 1 | 29 | 6% |
| 5 | 20 | 4% |

### Wordmark font class (logos with lettering)
| value | n | share |
|---|---|---|
| none | 361 | 74% |
| geometric_sans | 48 | 10% |
| custom_display | 38 | 8% |
| grotesque_sans | 15 | 3% |
| serif | 10 | 2% |
| script | 8 | 2% |
| humanist_sans | 6 | 1% |
| slab | 3 | 1% |
| mono | 1 | 0% |

### Letter case
| value | n | share |
|---|---|---|
| none | 348 | 71% |
| lowercase | 58 | 12% |
| uppercase | 58 | 12% |
| titlecase | 26 | 5% |

## Big brands (n=108)

### Composition
| value | n | share |
|---|---|---|
| symbol_only | 77 | 71% |
| wordmark_only | 19 | 18% |
| symbol_plus_word | 12 | 11% |

### Symbol kind
| value | n | share |
|---|---|---|
| pictorial | 30 | 28% |
| letterform | 26 | 24% |
| none | 19 | 18% |
| abstract_geometric | 18 | 17% |
| negative_space | 8 | 7% |
| lines_or_bars | 4 | 4% |
| ring_or_circle | 3 | 3% |

### Container
| value | n | share |
|---|---|---|
| none | 82 | 76% |
| circle | 13 | 12% |
| other | 8 | 7% |
| rounded_square | 4 | 4% |
| square | 1 | 1% |

## What a good logo looks like here

Simple. Most logos have complexity 2 or 3, use two colors or fewer, and carry no gradient. The common recipe is one flat mark, often a letterform or an abstract geometric shape, sometimes inside a square or circle container, set beside or without a clean sans serif name. Custom display lettering is rare and mostly belongs to consumer brands. Symmetric and asymmetric marks both appear, with asymmetry more common.

These shares drive the generator in `scripts/logo_studio_template.html` and the rules in `.claude/skills/yc-logo-creator/SKILL.md`.
