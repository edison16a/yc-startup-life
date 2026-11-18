"use strict";
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, m => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]));
const N = x => +x.toFixed(2);

/* ---------- seeded random ---------- */
function hash(str) { let h = 2166136261; for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
function rng(seed) { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const ri = (r, a, b) => a + Math.floor(r() * (b - a + 1));
const pick = (r, arr) => arr[Math.floor(r() * arr.length)];

/* ---------- palettes ---------- */
const PAIRS = [["#14110F", "#FFFFFF"], ["#FFFFFF", "#14110F"], ["#F26625", "#FFFFFF"], ["#FFFFFF", "#F26625"], ["#2F5BEA", "#FFFFFF"], ["#FFFFFF", "#2F5BEA"], ["#1E9E5A", "#FFFFFF"], ["#14110F", "#F5F0E6"], ["#7C3AED", "#FFFFFF"], ["#E11D48", "#FFFFFF"], ["#0B3D2E", "#E9F5EC"], ["#FACC15", "#14110F"]];
const PRESETS = [
  ["#F26625", "#14110F", "#FBBF24", "#FFFFFF"], ["#2F5BEA", "#7C9CFF", "#14110F", "#FFFFFF"], ["#1E9E5A", "#0B3D2E", "#A7F3D0", "#FFFFFF"], ["#7C3AED", "#C4B5FD", "#14110F", "#FFFFFF"],
  ["#E11D48", "#FB7185", "#FDE68A", "#FFFFFF"], ["#0EA5E9", "#0369A1", "#BAE6FD", "#FFFFFF"], ["#FACC15", "#14110F", "#F26625", "#FFFFFF"], ["#14110F", "#6B655C", "#D6CFC0", "#FFFFFF"],
  ["#FFFFFF", "#F26625", "#FBBF24", "#14110F"], ["#FFFFFF", "#7C9CFF", "#2F5BEA", "#0F172A"], ["#34D399", "#10B981", "#FFFFFF", "#052E2B"], ["#F472B6", "#A78BFA", "#38BDF8", "#FFFFFF"],
  ["#0F766E", "#F59E0B", "#FEF3C7", "#FFFFFF"], ["#9A3412", "#F97316", "#FED7AA", "#FFFBEB"], ["#1E3A8A", "#F43F5E", "#FDE68A", "#F8FAFC"], ["#4D7C0F", "#A3E635", "#14110F", "#FFFFFF"],
  ["#111827", "#F97316", "#FFFFFF", "#F3F4F6"], ["#BE185D", "#F9A8D4", "#FEF3C7", "#FFFFFF"], ["#065F46", "#FBBF24", "#F5F0E6", "#F5F0E6"], ["#4338CA", "#818CF8", "#E0E7FF", "#FFFFFF"]
];

/* ---------- fonts ---------- */
const FONTCSS = FONTS.map(f => `@font-face{font-family:"${f.family}";font-weight:${f.weight};font-style:normal;src:url(data:font/woff2;base64,${f.b64}) format("woff2")}`);
(function () { const st = document.createElement("style"); st.textContent = FONTCSS.join("\n"); document.head.appendChild(st); })();
const fontsReady = Promise.all(FONTS.map(f => document.fonts.load(`${f.weight} 40px "${f.family}"`).catch(() => null)));
const SANS = FONTS.map((f, i) => i).filter(i => FONTS[i].cls === "sans");
const mcv = document.createElement("canvas").getContext("2d");
const mcache = new Map();
function measure(f, text, fs, ls) {
  const k = f.id + "|" + text + "|" + fs + "|" + ls;
  if (mcache.has(k)) return mcache.get(k);
  mcv.font = `${f.weight} ${fs}px "${f.family}"`;
  const w = mcv.measureText(text).width + ls * Math.max(0, text.length - 1);
  mcache.set(k, w); return w;
}
function applyCase(t, mode) { return mode === "upper" ? t.toUpperCase() : mode === "lower" ? t.toLowerCase() : t.replace(/\w\S*/g, w => w[0].toUpperCase() + w.slice(1)); }

/* ---------- geometry helpers ---------- */
function cen(pts) { return [pts.reduce((a, p) => a + p[0], 0) / pts.length, pts.reduce((a, p) => a + p[1], 0) / pts.length]; }
function poly(pts, k, fill) { const [cx, cy] = cen(pts); return `<polygon points="${pts.map(p => N(cx + (p[0] - cx) * k) + "," + N(cy + (p[1] - cy) * k)).join(" ")}" fill="${fill}"/>`; }
function quarter(x, y, s, k, fill) {
  const d = [`M${x} ${y}L${x + s} ${y}A${s} ${s} 0 0 1 ${x} ${y + s}Z`, `M${x + s} ${y}L${x + s} ${y + s}A${s} ${s} 0 0 1 ${x} ${y}Z`, `M${x + s} ${y + s}L${x} ${y + s}A${s} ${s} 0 0 1 ${x + s} ${y}Z`, `M${x} ${y + s}L${x} ${y}A${s} ${s} 0 0 1 ${x + s} ${y + s}Z`][k];
  return `<path d="${d}" fill="${fill}"/>`;
}

/* ---------- mark families (100 x 100 box) ---------- */
const FAM = [
  function petals(r, c) { const n = ri(r, 3, 8), ry = ri(r, 14, 20), rx = ri(r, 6, 12), cyc = r() < .5 ? 2 : 3, k = [c.a, c.b, c.c]; let s = ""; for (let i = 0; i < n; i++) s += `<ellipse cx="50" cy="${50 - ry - 2}" rx="${rx}" ry="${ry}" fill="${k[i % cyc]}" transform="rotate(${N(i * 360 / n)} 50 50)"/>`; return s; },
  function bars(r, c) { const n = ri(r, 3, 5), bw = ri(r, 10, 15), gap = 6, tot = n * bw + (n - 1) * gap, x0 = 50 - tot / 2, rot = pick(r, [0, 0, 45, -45]), rad = r() < .6 ? bw / 2 : 3, base = r() < .5, k = [c.a, c.b, c.c], cyc = r() < .5 ? 1 : 3; let s = ""; for (let i = 0; i < n; i++) { const h = ri(r, 34, 80); const y = base ? 90 - h : 50 - h / 2; s += `<rect x="${N(x0 + i * (bw + gap))}" y="${y}" width="${bw}" height="${h}" rx="${rad}" fill="${k[i % cyc]}"/>`; } return `<g transform="rotate(${rot} 50 50)">${s}</g>`; },
  function dots(r, c) { const keep = [[1, 1], ...[[0, 0], [1, 0], [0, 1], [0, 2], [1, 2]].filter(() => r() < .72)], rr = ri(r, 8, 11), k = [c.a, c.b, c.c], P = [20, 50, 80]; let s = "", m = new Set(); for (const [x, y] of keep) { m.add(x + "," + y); m.add((2 - x) + "," + y); } for (const q of m) { const [x, y] = q.split(",").map(Number); s += `<circle cx="${P[x]}" cy="${P[y]}" r="${rr}" fill="${k[(x + y) % 3]}"/>`; } return s; },
  function orbit(r, c) { const R = ri(r, 28, 34), sw = ri(r, 8, 12), arc = r() < .5; const ring = arc ? `<path d="M${50 - R} 50A${R} ${R} 0 1 1 50 ${50 + R}" fill="none" stroke="${c.a}" stroke-width="${sw}" stroke-linecap="round"/>` : `<circle cx="50" cy="50" r="${R}" fill="none" stroke="${c.a}" stroke-width="${sw}"/>`; return ring + `<circle cx="50" cy="50" r="${ri(r, 10, 15)}" fill="${c.b}"/>` + (r() < .4 ? `<circle cx="${N(50 + R * .71)}" cy="${N(50 - R * .71)}" r="7" fill="${c.c}"/>` : ""); },
  function tiles(r, c) { const k = [c.a, c.b, c.c], s = 41, O = [6, 53]; let out = ""; for (let i = 0; i < 4; i++) { const x = O[i % 2], y = O[i >> 1], t = ri(r, 0, 3), f = k[ri(r, 0, 2)]; if (t === 0) out += quarter(x, y, s, ri(r, 0, 3), f); else if (t === 1) out += `<circle cx="${x + s / 2}" cy="${y + s / 2}" r="${s / 2}" fill="${f}"/>`; else if (t === 2) out += `<rect x="${x}" y="${y}" width="${s}" height="${s}" rx="${r() < .5 ? 0 : 8}" fill="${f}"/>`; else out += quarter(x, y, s, ri(r, 0, 3), f); } return out; },
  function chevrons(r, c) { const n = ri(r, 2, 4), sw = ri(r, 9, 12), g = 20, tot = (n - 1) * g + 24, y0 = 50 - tot / 2, k = [c.a, c.b, c.c], rot = pick(r, [0, 90, 180, 270]); let s = ""; for (let i = 0; i < n; i++) { const y = y0 + i * g; s += `<polyline points="18,${y + 24} 50,${y} 82,${y + 24}" fill="none" stroke="${k[i % 3]}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"/>`; } return `<g transform="rotate(${rot} 50 50)">${s}</g>`; },
  function cube(r, c) { const T = [[50, 8], [86.4, 29], [50, 50], [13.6, 29]], L = [[13.6, 29], [50, 50], [50, 92], [13.6, 71]], R = [[50, 50], [86.4, 29], [86.4, 71], [50, 92]], g = .88 + r() * .04, open = r() < .3 ? ri(r, 0, 2) : -1, F = [[T, c.a], [L, c.b], [R, c.c]]; return F.map(([p, f], i) => i === open ? "" : poly(p, g, f)).join(""); },
  function negative(r, c, u) { const shape = pick(r, ["circle", "round", "squircle"]), cut = pick(r, ["dot", "ring", "slit", "tri"]); const body = shape === "circle" ? `<circle cx="50" cy="50" r="42"` : shape === "round" ? `<rect x="10" y="10" width="80" height="80" rx="14"` : `<rect x="8" y="8" width="84" height="84" rx="30"`; const cf = col => cut === "dot" ? `<circle cx="50" cy="50" r="${ri(r, 14, 22)}" fill="${col}"/>` : cut === "ring" ? `<circle cx="50" cy="50" r="22" fill="none" stroke="${col}" stroke-width="9"/>` : cut === "slit" ? `<rect x="42" y="18" width="16" height="64" rx="8" fill="${col}" transform="rotate(${pick(r, [0, 45, 90])} 50 50)"/>` : `<polygon points="50,28 74,68 26,68" fill="${col}"/>`; if (c.a === c.b) return `<mask id="m${u}"><rect width="100" height="100" fill="#fff"/>${cf("#000")}</mask>${body} fill="${c.a}" mask="url(#m${u})"/>`; return `${body} fill="${c.a}"/>${cf(c.b)}`; },
  function arcs(r, c) { const k = [c.a, c.b, c.c], cap = r() < .6 ? "round" : "butt", rot = pick(r, [0, 90, 180, 270]); let s = ""; [12, 25, 38].forEach((R, i) => s += `<path d="M${50 - R} 62A${R} ${R} 0 0 1 ${50 + R} 62" fill="none" stroke="${k[i]}" stroke-width="9" stroke-linecap="${cap}"/>`); return `<g transform="rotate(${rot} 50 50) translate(0 ${r() < .5 ? 0 : -6})">${s}</g>`; },
  function leaves(r, c) { const n = ri(r, 2, 4), k = [c.a, c.b, c.c], d = "M50 50C50 24 70 12 88 12C88 30 76 50 50 50Z"; let s = ""; for (let i = 0; i < n; i++) s += `<path d="${d}" fill="${k[i % 3]}" transform="rotate(${N(i * 360 / n + (n === 2 ? 0 : 0))} 50 50)"/>`; return `<g transform="rotate(${pick(r, [0, 45, 90])} 50 50)">${s}</g>`; },
  function asterisk(r, c) { const n = ri(r, 3, 6), k = [c.a, c.b]; let s = ""; for (let i = 0; i < n; i++) { const a = i * Math.PI / n; s += `<line x1="${N(50 - Math.cos(a) * 40)}" y1="${N(50 - Math.sin(a) * 40)}" x2="${N(50 + Math.cos(a) * 40)}" y2="${N(50 + Math.sin(a) * 40)}" stroke="${k[i % 2]}" stroke-width="${ri(r, 8, 11)}" stroke-linecap="round"/>`; } return s + `<circle cx="50" cy="50" r="7" fill="${c.c}"/>`; },
  function waves(r, c) { const n = ri(r, 2, 4), k = [c.a, c.b, c.c], g = 100 / (n + 1); let s = ""; for (let i = 1; i <= n; i++) { const y = N(g * i), a = ri(r, 10, 16); s += `<path d="M12 ${y}Q31 ${y - a} 50 ${y}T88 ${y}" fill="none" stroke="${k[(i - 1) % 3]}" stroke-width="${n === 4 ? 7 : 9}" stroke-linecap="round"/>`; } return s; },
  function pills(r, c) { const k = [c.a, c.b, c.c], w = ri(r, 18, 24), n = ri(r, 2, 3), rot = pick(r, [0, 45, 90, 135]); let s = ""; for (let i = 0; i < n; i++) { const h = ri(r, 46, 80), off = (i - (n - 1) / 2) * (w + 6); s += `<rect x="${N(50 + off - w / 2)}" y="${N(50 - h / 2 + (i % 2 ? 8 : -8))}" width="${w}" height="${h}" rx="${w / 2}" fill="${k[i]}"/>`; } return `<g transform="rotate(${rot} 50 50)">${s}</g>`; },
  function split(r, c) { const R = 40, g = 3.5, ang = pick(r, [0, 45, 90, 135]), half = (col, s) => `<path d="M${50 - R} 50A${R} ${R} 0 0 1 ${50 + R} 50Z" fill="${col}" transform="translate(0 ${s * -g})"/>`; return `<g transform="rotate(${ang} 50 50)">${half(c.a, 1)}<g transform="rotate(180 50 50)">${half(c.b, 1)}</g></g>`; },
  function triforce(r, c) { const T = [[50, 12], [70, 46.6], [30, 46.6]], BL = [[30, 46.6], [50, 81.2], [10, 81.2]], BR = [[70, 46.6], [90, 81.2], [50, 81.2]], g = .9, inv = r() < .4, s = [poly(T, g, c.a), poly(BL, g, c.b), poly(BR, g, c.c)].join(""); return inv ? `<g transform="rotate(180 50 50)">${s}</g>` : s; },
  function steps(r, c) { const k = [c.a, c.b, c.c], circ = r() < .35, rad = circ ? 99 : pick(r, [0, 6, 12]), sz = [24, 30, 36]; let s = ""; [[12, 64], [36, 38], [60, 12]].forEach(([x, y], i) => { const z = sz[i]; s += `<rect x="${x}" y="${y + 24 - z + (i === 0 ? 0 : 0)}" width="${z}" height="${z}" rx="${Math.min(rad, z / 2)}" fill="${k[i]}"/>`; }); return s; },
  function dotring(r, c) { const n = ri(r, 6, 10), R = 34; let s = ""; for (let i = 0; i < n; i++) { const a = i / n * Math.PI * 2 - Math.PI / 2, rr = 3.5 + 7 * i / n; s += `<circle cx="${N(50 + Math.cos(a) * R)}" cy="${N(50 + Math.sin(a) * R)}" r="${N(rr)}" fill="${i >= n - 2 ? c.b : c.a}"/>`; } return s; },
  function diamonds(r, c) { const k = [c.a, c.b, c.c, c.b], C = [[50, 26], [74, 50], [50, 74], [26, 50]], R = 24, g = .88; return C.map(([x, y], i) => r() < .12 ? "" : poly([[x, y - R], [x + R, y], [x, y + R], [x - R, y]], g, k[i])).join(""); },
  function slashes(r, c) { const n = ri(r, 3, 4), k = [c.a, c.b, c.c], w = 11, gap = 8, tot = n * w + (n - 1) * gap; let s = ""; for (let i = 0; i < n; i++) { const h = ri(r, 40, 76); s += `<rect x="${N(50 - tot / 2 + i * (w + gap))}" y="${50 - h / 2}" width="${w}" height="${h}" rx="5" fill="${k[i % 3]}"/>`; } return `<g transform="rotate(${pick(r, [30, 35, 40])} 50 50)">${s}</g>`; },
  function layers(r, c) { const k = [c.a, c.b, c.c], n = ri(r, 2, 3), dy = n === 2 ? 22 : 18, y0 = n === 2 ? 24 : 18; let s = ""; for (let i = n - 1; i >= 0; i--) { const y = y0 + i * dy; s += poly([[50, y], [88, y + 20], [50, y + 40], [12, y + 20]], .92, k[i % 3]); } return s; }
];
const NFAM = FAM.length;

const FIELDS = { any: null, tech: [1, 4, 5, 6, 14, 15, 17, 18, 19, 2, 8, 3], organic: [0, 9, 3, 11, 13, 16, 10, 8, 7, 12, 2, 4], consumer: [7, 0, 4, 14, 15, 19, 1, 12, 9, 10, 17, 5] };
function markSpec(idx, salt) { if (CUSTOM.length && idx < CUSTOM.length) return { custom: idx }; const o = FIELDS[st.field], pool = o ? o.concat(Array.from({ length: NFAM }, (_, i) => i).filter(i => !o.includes(i))) : null, n = o ? 14 : NFAM; const fam = pool ? pool[(idx + st.seed) % n] : (idx + st.seed) % NFAM; return { fam, k: Math.floor(idx / n), salt: salt + "|" + st.seed + "|" + st.field + "|" + idx }; }
const CUSTOM = typeof CUSTOM_MARKS !== "undefined" ? CUSTOM_MARKS : [];
function customInner(i, c, u) { return CUSTOM[i].replace(/\{A\}/g, c.a).replace(/\{B\}/g, c.b).replace(/\{C\}/g, c.c).replace(/\{U\}/g, u); }
function markInner(spec, c, u, ctx) {
  if (spec.custom !== undefined) return customInner(spec.custom, c, u); const r = rng(hash(spec.salt) + spec.fam * 977 + spec.k * 131); return FAM[spec.fam](r, c, u, ctx); }

/* ---------- layout builders ---------- */
function monoC(fg) { return { a: fg, b: fg, c: fg }; }
function initial(name) { const m = name.match(/[A-Za-z0-9]/); return (m ? m[0] : "A").toUpperCase(); }

function buildMark(idx, st, u, multi) {
  const used = new Set(), ctx = {}, c = multi ? { a: st.pal[0], b: st.pal[1], c: st.pal[2] } : monoC(st.fg);
  return { inner: markInner(markSpec(idx, (multi ? "m" : "o")), c, u, ctx), w: 100, h: 100, used };
}
function fontFor(idx) { return FONTS[idx % FONTS.length]; }
function caseFor(f, idx) { if (f.cls === "mono") return "lower"; if (f.cls === "serif") return ["title", "lower", "title"][idx % 3]; return ["lower", "title", "lower", "upper", "title"][idx % 5]; }
function lsFor(f, mode) { return mode === "upper" ? Math.round(.06 * 46) : f.cls === "mono" ? 0 : -1; }

function buildLockup(idx, st, u) {
  const used = new Set(), c = monoC(st.fg), spec = markSpec((idx * 7 + 3) % 100, "l"), f = FONTS[(idx * 5 + Math.floor(idx / 3) + st.seed) % FONTS.length], cs = caseFor(f, idx), text = applyCase(st.name, cs), vert = idx % 3 === 2;
  used.add(f.id);
  const mk = markInner(spec, c, u, {});
  const fs = vert ? 40 : 46, ls = lsFor(f, cs) * fs / 46, tw = measure(f, text, fs, ls);
  const tx = (x, y, anchor) => `<text x="${N(x)}" y="${N(y)}" text-anchor="${anchor}" font-family="${f.family}" font-weight="${f.weight}" font-size="${fs}" letter-spacing="${N(ls)}" fill="${c.a}">${esc(text)}</text>`;
  if (!vert) { const gap = 20, w = 100 + gap + tw; return { inner: mk + tx(100 + gap, 50 + .36 * fs, "start"), w, h: 100, used }; }
  const w = Math.max(100, tw), gap = 18; return { inner: `<g transform="translate(${N((w - 100) / 2)} 0)">${mk}</g>` + tx(w / 2, 100 + gap + .74 * fs, "middle"), w, h: 100 + gap + fs, used };
}

function buildWord(idx, st, u) {
  const used = new Set(), c = st.fg, T = (idx + st.seed) % 6, f = FONTS[(Math.floor(idx / 6) + st.seed) % FONTS.length], cs = caseFor(f, idx + (idx > 59 ? 1 : 0)), text = applyCase(st.name, cs), fs = 64, ls = lsFor(f, cs) * fs / 46;
  used.add(f.id);
  const tw = measure(f, text, fs, ls), base = .8 * fs, att = `font-family="${f.family}" font-weight="${f.weight}" font-size="${fs}" letter-spacing="${N(ls)}"`;
  const txt = (x, fill) => `<text x="${N(x)}" y="${N(base)}" ${att} fill="${fill}">${esc(text)}</text>`, H = fs * 1.05;
  const xh = cs === "upper" ? .36 * fs : .27 * fs;
  if (T === 0) return { inner: txt(0, c), w: tw, h: H, used };
  if (T === 1) { const r = fs * .09; return { inner: txt(0, c) + `<circle cx="${N(tw + r * 1.4)}" cy="${N(base - r)}" r="${N(r * 1.15)}" fill="${c}"/>`, w: tw + r * 3.4, h: H, used }; }
  if (T === 2) { const px = fs * .5, py = fs * .26, w = tw + px * 2, h = fs * .8 + py * 2; return { inner: `<mask id="w${u}"><rect width="${N(w)}" height="${N(h)}" fill="#fff"/><text x="${N(px)}" y="${N(py + .8 * fs - fs * .03)}" ${att} fill="#000">${esc(text)}</text></mask><rect width="${N(w)}" height="${N(h)}" rx="${N(h / 2)}" fill="${c}" mask="url(#w${u})"/>`, w, h, used }; }
  if (T === 3) { const th = fs * .09; return { inner: txt(0, c) + `<rect x="0" y="${N(base + fs * .1)}" width="${N(tw * .42)}" height="${N(th)}" rx="${N(th / 2)}" fill="${c}"/>`, w: tw, h: base + fs * .1 + th, used }; }
  if (T === 4) {
    const i = text.search(/[oO]/);
    if (i < 0) { const sq = fs * .3; return { inner: `<rect x="0" y="${N(base - sq)}" width="${N(sq)}" height="${N(sq)}" rx="${N(sq * .3)}" fill="${c}"/>` + `<text x="${N(sq * 1.5)}" y="${N(base)}" ${att} fill="${c}">${esc(text)}</text>`, w: sq * 1.5 + tw, h: H, used }; }
    const a = text.slice(0, i), b = text.slice(i + 1), wa = a ? measure(f, a, fs, ls) + ls : 0, wo = measure(f, text[i], fs, 0), rr = Math.min(wo * .44, xh * 1.0), sw = fs * .12, wb = b ? measure(f, b, fs, ls) : 0, ox = wa + wo / 2;
    return { inner: (a ? `<text x="0" y="${N(base)}" ${att} fill="${c}">${esc(a)}</text>` : "") + `<circle cx="${N(ox)}" cy="${N(base - xh)}" r="${N(rr - sw / 2)}" fill="none" stroke="${c}" stroke-width="${N(sw)}"/>` + (b ? `<text x="${N(wa + wo + ls)}" y="${N(base)}" ${att} fill="${c}">${esc(b)}</text>` : ""), w: wa + wo + ls + wb, h: H, used };
  }
  const sq = fs * .62, g = fs * .26; return { inner: `<rect x="0" y="${N(base - sq)}" width="${N(sq)}" height="${N(sq)}" rx="${N(sq * .5)}" fill="${c}"/>` + `<text x="${N(sq + g)}" y="${N(base)}" ${att} fill="${c}">${esc(text)}</text>`, w: sq + g + tw, h: H, used };
}

const SECTIONS = {
  mark: { title: "Object only", sub: "One flat object in one color. Pick the object color and the background.", build: (i, st, u) => buildMark(i, st, u, false), pad: .16, cls: "" },
  lockup: { title: "Object and name", sub: "A flat object beside or above the company name, set in a clean typeface.", build: buildLockup, pad: .1, cls: "wide" },
  word: { title: "Name only", sub: "The name alone, with a small object built into the type.", build: buildWord, pad: .12, cls: "wide" },
  multi: { title: "Multicolor object", sub: "Objects with up to three preset colors. Change any single color or pick a preset.", build: (i, st, u) => buildMark(i, st, u, true), pad: .16, cls: "" }
};

/* ---------- state ---------- */
const st = { name: DEFAULT_NAME, seed: Math.floor(Math.random() * 1e9), field: "any", sec: "mark", count: 100, fg: DEFAULT_FG, bg: DEFAULT_BG, pal: PRESETS[0].slice(0, 3), mbg: PRESETS[0][3], sel: { mark: 0, lockup: 0, word: 0, multi: 0 } };

function bgOf() { return st.sec === "multi" ? st.mbg : st.bg; }
function cardSVG(logo) { const p = Math.max(logo.w, logo.h) * SECTIONS[st.sec].pad, w = logo.w + 2 * p, h = logo.h + 2 * p; return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${N(-p)} ${N(-p)} ${N(w)} ${N(h)}" aria-hidden="true">${logo.inner}</svg>`; }
function fontStyle(used) { return FONTS.filter(f => used.has(f.id)).map(f => FONTCSS[FONTS.indexOf(f)]).join(""); }
function fullSVG(logo, W, H, bg, sec) {
  const pad = SECTIONS[sec].pad, p = Math.max(logo.w, logo.h) * pad, cw = logo.w + 2 * p, ch = logo.h + 2 * p, ar = W / H;
  let vw = cw, vh = ch; if (vw / vh < ar) vw = vh * ar; else vh = vw / ar;
  const vx = logo.w / 2 - vw / 2, vy = logo.h / 2 - vh / 2;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="${N(vx)} ${N(vy)} ${N(vw)} ${N(vh)}"><defs><style>${fontStyle(logo.used)}</style></defs>${bg ? `<rect x="${N(vx)}" y="${N(vy)}" width="${N(vw)}" height="${N(vh)}" fill="${bg}"/>` : ""}${logo.inner}</svg>`;
}

let logos = [];
function render() {
  const S = SECTIONS[st.sec], grid = $("grid"), n = st.count;
  $("title").textContent = S.title; $("sub").textContent = S.sub;
  grid.className = "grid " + S.cls; logos = []; let html = "";
  for (let i = 0; i < n; i++) { const L = S.build(i, st, "c" + i); logos.push(L); html += `<button type="button" class="card" data-i="${i}" aria-pressed="${st.sel[st.sec] === i}" aria-label="Logo ${i + 1}" style="background:${bgOf()}"><span class="n" style="color:${bgOf()}">${i + 1}</span>${cardSVG(L)}</button>`; }
  grid.innerHTML = html;
  if (st.sel[st.sec] >= n) st.sel[st.sec] = 0;
  renderBig();
}
function renderBig() {
  const i = st.sel[st.sec], L = logos[i]; if (!L) return;
  const big = $("big"), tr = $("transp").checked;
  big.className = "big" + (tr ? "" : " solid"); big.style.background = tr ? "" : bgOf();
  big.innerHTML = cardSVG(L);
  document.querySelectorAll(".card").forEach(b => b.setAttribute("aria-pressed", String(+b.dataset.i === i)));
}

/* ---------- controls ---------- */
function seg(id, cb) { $(id).addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; $(id).querySelectorAll("button").forEach(x => x.setAttribute("aria-pressed", String(x === b))); cb(b.dataset.v); }); }
function setSec(v) {
  st.sec = v; const multi = v === "multi";
  $("monoCols").hidden = multi; $("multiCols").hidden = !multi;
  render();
}
seg("tabs", setSec);
seg("field", v => { st.field = v; render(); });
$("shuffle").addEventListener("click", () => { st.seed = Math.floor(Math.random() * 1e9); render(); say("New set generated from scratch. The name does not change the objects."); });
seg("count", v => { st.count = +v; render(); });
let tm; $("name").addEventListener("input", e => { st.name = e.target.value.trim() || DEFAULT_NAME; clearTimeout(tm); tm = setTimeout(render, 120); });
$("grid").addEventListener("click", e => { const b = e.target.closest(".card"); if (!b) return; st.sel[st.sec] = +b.dataset.i; renderBig(); });
$("transp").addEventListener("change", renderBig);

function syncMono() { $("fg").value = st.fg; $("bgc").value = st.bg; $("fgc").textContent = st.fg.toUpperCase(); $("bgcc").textContent = st.bg.toUpperCase(); $("pal").querySelectorAll("button").forEach((b, i) => b.setAttribute("aria-pressed", String(PAIRS[i][0].toLowerCase() === st.fg.toLowerCase() && PAIRS[i][1].toLowerCase() === st.bg.toLowerCase()))); }
function syncMulti() { ["c1", "c2", "c3"].forEach((id, i) => { $(id).value = st.pal[i]; $(id + "c").textContent = st.pal[i].toUpperCase(); }); $("bgm").value = st.mbg; $("bgmc").textContent = st.mbg.toUpperCase(); $("presets").querySelectorAll("button").forEach((b, i) => b.setAttribute("aria-pressed", String(PRESETS[i].slice(0, 3).join() .toLowerCase() === st.pal.join().toLowerCase() && PRESETS[i][3].toLowerCase() === st.mbg.toLowerCase()))); }
$("pal").innerHTML = PAIRS.map(([a, b], i) => `<button type="button" data-i="${i}" aria-pressed="false" aria-label="Color pair ${i + 1}" style="background:linear-gradient(135deg,${a} 50%,${b} 50%)"></button>`).join("");
$("pal").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; [st.fg, st.bg] = PAIRS[+b.dataset.i]; syncMono(); render(); });
$("presets").innerHTML = PRESETS.map((p, i) => `<button type="button" class="pre" data-i="${i}" aria-pressed="false" aria-label="Preset ${i + 1}">${p.slice(0, 3).map(c => `<i style="background:${c}"></i>`).join("")}</button>`).join("");
$("presets").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; const p = PRESETS[+b.dataset.i]; st.pal = p.slice(0, 3); st.mbg = p[3]; syncMulti(); render(); });
$("fg").addEventListener("input", e => { st.fg = e.target.value; syncMono(); render(); });
$("bgc").addEventListener("input", e => { st.bg = e.target.value; syncMono(); render(); });
["c1", "c2", "c3"].forEach((id, i) => $(id).addEventListener("input", e => { st.pal[i] = e.target.value; syncMulti(); render(); }));
$("bgm").addEventListener("input", e => { st.mbg = e.target.value; syncMulti(); render(); });

/* ---------- export ---------- */
function dims() { const clamp = v => Math.max(16, Math.min(8192, Math.round(+v) || 1024)); return [clamp($("w").value), clamp($("h").value)]; }
function exportBg() { return $("transp").checked ? null : bgOf(); }
function saveBlob(blob, name) { const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 4000); }
function slug() { return (st.name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "logo"); }
function say(t) { $("status").textContent = t; }
function pngBlob(svg, W, H) {
  return new Promise((res, rej) => {
    const img = new Image();
    img.onload = () => { const draw = () => { const cv = document.createElement("canvas"); cv.width = W; cv.height = H; const g = cv.getContext("2d"); g.drawImage(img, 0, 0, W, H); cv.toBlob(b => b ? res(b) : rej(new Error("canvas export failed")), "image/png"); }; (img.decode ? img.decode() : Promise.resolve()).then(() => setTimeout(draw, 60), () => setTimeout(draw, 60)); };
    img.onerror = () => rej(new Error("image load failed"));
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  });
}
$("dlpng").addEventListener("click", async () => {
  const [W, H] = dims(), L = logos[st.sel[st.sec]]; say("Rendering PNG...");
  try { const b = await pngBlob(fullSVG(L, W, H, exportBg(), st.sec), W, H); saveBlob(b, `${slug()}-${st.sec}-${st.sel[st.sec] + 1}-${W}x${H}.png`); say(`Saved ${W} × ${H} PNG${$("transp").checked ? " with transparent background" : ""}.`); } catch (e) { say("PNG export failed: " + e.message); }
});
$("dlsvg").addEventListener("click", () => { const [W, H] = dims(), L = logos[st.sel[st.sec]]; saveBlob(new Blob([fullSVG(L, W, H, exportBg(), st.sec)], { type: "image/svg+xml" }), `${slug()}-${st.sec}-${st.sel[st.sec] + 1}.svg`); say("Saved SVG."); });
const CRC = (() => { const t = []; for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ c >>> 1 : c >>> 1; t[n] = c >>> 0; } return t; })();
function crc32(b) { let c = 0xFFFFFFFF; for (let i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 255] ^ c >>> 8; return (c ^ 0xFFFFFFFF) >>> 0; }
function zip(files) {
  const enc = new TextEncoder(), parts = [], cen = []; let off = 0;
  for (const [name, text] of files) {
    const nb = enc.encode(name), db = enc.encode(text), crc = crc32(db), h = new DataView(new ArrayBuffer(30));
    h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint32(14, crc, true); h.setUint32(18, db.length, true); h.setUint32(22, db.length, true); h.setUint16(26, nb.length, true);
    parts.push(new Uint8Array(h.buffer), nb, db);
    const c = new DataView(new ArrayBuffer(46)); c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint32(16, crc, true); c.setUint32(20, db.length, true); c.setUint32(24, db.length, true); c.setUint16(28, nb.length, true); c.setUint32(42, off, true);
    cen.push(new Uint8Array(c.buffer), nb); off += 30 + nb.length + db.length;
  }
  let cl = 0; cen.forEach(x => cl += x.length); const e = new DataView(new ArrayBuffer(22)); e.setUint32(0, 0x06054b50, true); e.setUint16(8, files.length, true); e.setUint16(10, files.length, true); e.setUint32(12, cl, true); e.setUint32(16, off, true);
  return new Blob([...parts, ...cen, new Uint8Array(e.buffer)], { type: "application/zip" });
}
$("dlall").addEventListener("click", () => {
  const [W, H] = dims(), bg = exportBg();
  saveBlob(zip(logos.map((L, i) => [`${slug()}-${st.sec}-${String(i + 1).padStart(3, "0")}.svg`, fullSVG(L, W, H, bg, st.sec)])), `${slug()}-${st.sec}-svgs.zip`);
  say(`Saved ${logos.length} SVGs in one zip.`);
});

/* ---------- start ---------- */
$("name").value = DEFAULT_NAME; $("fg").value = st.fg; $("bgc").value = st.bg;
syncMono(); syncMulti();
fontsReady.then(() => { mcache.clear(); render(); });
