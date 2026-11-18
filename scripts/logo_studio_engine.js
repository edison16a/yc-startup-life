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

/* ---------- marks: ONLY the AI designed marks passed in with --marks ---------- */
const CUSTOM = typeof CUSTOM_MARKS !== "undefined" ? CUSTOM_MARKS : [];
function shuffled(seed) { const o = CUSTOM.map((_, i) => i), r = rng(seed); for (let i = o.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [o[i], o[j]] = [o[j], o[i]]; } return o; }
let ORDER = [];
function markInner(idx, c, u) { const i = ORDER[idx % ORDER.length]; return CUSTOM[i].replace(/\{A\}/g, c.a).replace(/\{B\}/g, c.b).replace(/\{C\}/g, c.c).replace(/\{U\}/g, u); }

/* ---------- layout builders ---------- */
function monoC(fg) { return { a: fg, b: fg, c: fg }; }
function buildMark(idx, st, u, multi) {
  const c = multi ? { a: st.pal[0], b: st.pal[1], c: st.pal[2] } : monoC(st.fg);
  return { inner: markInner(idx, c, u), w: 100, h: 100, used: new Set() };
}
function caseFor(f, idx) { if (f.cls === "mono") return "lower"; if (f.cls === "serif") return ["title", "lower", "title"][idx % 3]; return ["lower", "title", "lower", "upper", "title"][idx % 5]; }
function lsFor(f, mode) { return mode === "upper" ? Math.round(.06 * 46) : f.cls === "mono" ? 0 : -1; }
const fontAt = idx => FONTS[(idx * 5 + Math.floor(idx / 3) + st.seed) % FONTS.length];

function buildLockup(idx, st, u) {
  const used = new Set(), c = monoC(st.fg), f = fontAt(idx), cs = caseFor(f, idx), text = applyCase(st.name, cs), vert = idx % 3 === 2;
  used.add(f.id);
  const mk = markInner(idx, c, u);
  const fs = vert ? 40 : 46, ls = lsFor(f, cs) * fs / 46, tw = measure(f, text, fs, ls);
  const tx = (x, y, anchor) => `<text x="${N(x)}" y="${N(y)}" text-anchor="${anchor}" font-family="${f.family}" font-weight="${f.weight}" font-size="${fs}" letter-spacing="${N(ls)}" fill="${c.a}">${esc(text)}</text>`;
  if (!vert) { const gap = 20, w = 100 + gap + tw; return { inner: mk + tx(100 + gap, 50 + .36 * fs, "start"), w, h: 100, used }; }
  const w = Math.max(100, tw), gap = 18; return { inner: `<g transform="translate(${N((w - 100) / 2)} 0)">${mk}</g>` + tx(w / 2, 100 + gap + .74 * fs, "middle"), w, h: 100 + gap + fs, used };
}

/* Name only: the name in a typeface with a small AI designed object built in (before, after, or in place of the first o). */
function buildWord(idx, st, u) {
  const used = new Set(), c = monoC(st.fg), f = fontAt(idx), cs = caseFor(f, idx), text = applyCase(st.name, cs), fs = 64, ls = lsFor(f, cs) * fs / 46, P = idx % 3;
  used.add(f.id);
  const base = .8 * fs, H = fs * 1.05, att = `font-family="${f.family}" font-weight="${f.weight}" font-size="${fs}" letter-spacing="${N(ls)}" fill="${c.a}"`;
  const T = (x, t) => `<text x="${N(x)}" y="${N(base)}" ${att}>${esc(t)}</text>`, tw = measure(f, text, fs, ls);
  const ob = (x, size, cy) => `<g transform="translate(${N(x)} ${N(cy - size / 2)}) scale(${N(size / 100)})">${markInner(idx, c, u)}</g>`;
  const mid = base - (cs === "upper" ? .36 : .3) * fs, i = text.search(/[oO]/);
  if (P === 2 && i >= 0) {
    const a = text.slice(0, i), b = text.slice(i + 1), wa = a ? measure(f, a, fs, ls) + ls : 0, wo = measure(f, text[i], fs, 0), sz = fs * (cs === "upper" ? .72 : .6), wb = b ? measure(f, b, fs, ls) : 0;
    return { inner: (a ? T(0, a) : "") + ob(wa + (wo - sz) / 2, sz, mid) + (b ? T(wa + wo + ls, b) : ""), w: wa + wo + ls + wb, h: H, used };
  }
  const sz = fs * .74, g = fs * .24;
  if (P === 1) return { inner: T(0, text) + ob(tw + g, sz, mid), w: tw + g + sz, h: H, used };
  return { inner: ob(0, sz, mid) + T(sz + g, text), w: sz + g + tw, h: H, used };
}

const SECTIONS = {
  mark: { title: "Object only", sub: "One flat object in one color. Pick the object color and the background.", build: (i, st, u) => buildMark(i, st, u, false), pad: .16, cls: "" },
  lockup: { title: "Object and name", sub: "A flat object beside or above the company name, set in a clean typeface.", build: buildLockup, pad: .1, cls: "wide" },
  word: { title: "Name only", sub: "The name with a small AI designed object built into the type: before, after, or in place of an o.", build: buildWord, pad: .12, cls: "wide" },
  multi: { title: "Multicolor object", sub: "Objects with up to three preset colors. Change any single color or pick a preset.", build: (i, st, u) => buildMark(i, st, u, true), pad: .16, cls: "" }
};

/* ---------- state ---------- */
const st = { name: DEFAULT_NAME, seed: Math.floor(Math.random() * 1e9), sec: "mark", count: 100, fg: DEFAULT_FG, bg: DEFAULT_BG, pal: PRESETS[0].slice(0, 3), mbg: PRESETS[0][3], sel: { mark: 0, lockup: 0, word: 0, multi: 0 } };

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
  const S = SECTIONS[st.sec], grid = $("grid"), n = (st.sec === "mark" || st.sec === "multi") ? Math.min(st.count, CUSTOM.length) : st.count;
  $("title").textContent = S.title; $("sub").textContent = S.sub;
  grid.className = "grid " + S.cls; logos = []; let html = "";
  if (!CUSTOM.length) { grid.innerHTML = '<p class="empty">No AI designed marks were supplied, so there is nothing to show. Rebuild with --marks.</p>'; $("big").innerHTML = ""; return; }
  ORDER = shuffled(st.seed);
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
$("shuffle").addEventListener("click", () => { st.seed = Math.floor(Math.random() * 1e9); render(); say("Reordered the AI designed marks and paired them with new fonts."); });
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
$("nmarks").textContent = CUSTOM.length;
$("name").value = DEFAULT_NAME; $("fg").value = st.fg; $("bgc").value = st.bg;
syncMono(); syncMulti();
fontsReady.then(() => { mcache.clear(); render(); });
