# ED Architecture Certificate — Design Specification

## Publication-Ready Figure for the ED-SIM-01 Release

---

# 1. Overview

The ED Architecture Certificate is the single visual artifact that encodes the global structural verdict of the Event Density architecture. It is the front page of the invariant atlas: the condensed, human-readable summary of sixteen invariant families, three meta-analyses, and sixty-four parameter-regime simulations.

The certificate serves three audiences simultaneously:

- **For the paper.** It is Figure 7 of the ED-SIM-01 manuscript — the figure that a reviewer looks at to understand the global result before reading the methods.
- **For the website.** It is the hero image of the ED-SIM release page — the visual anchor that communicates "this architecture is self-consistent" at a glance.
- **For reproducibility.** It is the output of `generate_master_index_and_certificate.py` — the machine-generated document that any researcher can regenerate and compare.

The certificate must therefore be simultaneously precise (every number is meaningful), legible (the verdict is visible in under two seconds), and beautiful (it represents the architecture's aesthetic: clean, structural, inevitable).

---

# 2. Layout Specification

## 2.1 Canvas

| Property | Value |
|----------|-------|
| Aspect ratio | 3:4 (portrait) |
| Canonical size | 600 × 800 pt (8.33 × 11.11 in) |
| Print size | 6 × 8 in at 300 DPI |
| Web size | 1200 × 1600 px at 2× |

## 2.2 Grid System

The layout uses a **4-column, 24-row grid** with the following structure:

```
┌─────────────────────────────────────────────────────┐
│                   TOP MARGIN (3%)                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│              A. HEADER BOX (18%)                    │
│              Title, subtitle, version               │
│                                                     │
├─────────────────────────────────────────────────────┤
│                   GAP (2%)                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│            B. VERDICT BANNER (12%)                  │
│            PASS / PARTIAL / FAIL                    │
│                                                     │
├─────────────────────────────────────────────────────┤
│                   GAP (2%)                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│                                                     │
│           C. METRICS TABLE (42%)                    │
│           5 diagnostics × 3 columns                 │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│                   GAP (2%)                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│           D. FOOTER (12%)                           │
│           Statement, timestamp, signature           │
│                                                     │
├─────────────────────────────────────────────────────┤
│                  BOTTOM MARGIN (3%)                 │
└─────────────────────────────────────────────────────┘
```

Vertical proportions (of canvas height):

| Zone | Allocation | Rows (of 24) |
|------|-----------|--------------|
| Top margin | 3% | — |
| A. Header | 18% | 4.3 |
| Gap | 2% | 0.5 |
| B. Verdict | 12% | 2.9 |
| Gap | 2% | 0.5 |
| C. Metrics | 42% | 10.1 |
| Gap | 2% | 0.5 |
| D. Footer | 12% | 2.9 |
| Bottom margin | 3% | — |
| **Gaps + margins** | **14%** | — |
| **Content** | **86%** | — |

## 2.3 Horizontal Layout

| Property | Value |
|----------|-------|
| Left margin | 8% of width |
| Right margin | 8% of width |
| Content width | 84% of width |
| Column gutters | 2% of width |

The four columns span the content width equally (each 20% of canvas width, with 1.33% gutters). The metrics table uses a 3-column sub-grid within the content area:

| Column | Width | Content |
|--------|-------|---------|
| Icon | 8% | Geometric mark |
| Label | 42% | Diagnostic name + sub-metrics |
| Value | 34% | Verdict + key number |

## 2.4 Alignment Rules

- All text is **left-aligned** except the verdict banner (centred) and the footer timestamp (right-aligned).
- Vertical rhythm is maintained by a **baseline grid** of 16 pt increments.
- All box edges align to the 4-column grid.
- Numbers in the value column are **right-aligned** within their cells.
- Verdict text in the value column is **left-aligned**.

---

# 3. Typography Specification

## 3.1 Font Stack

| Role | Primary | Fallback | Weight |
|------|---------|----------|--------|
| Title | Inter | Helvetica Neue, Arial | 700 (Bold) |
| Subtitle | Inter | Helvetica Neue, Arial | 400 (Regular) |
| Verdict banner | Inter | Helvetica Neue, Arial | 800 (ExtraBold) |
| Diagnostic label | Inter | Helvetica Neue, Arial | 600 (SemiBold) |
| Sub-metric label | Inter | Helvetica Neue, Arial | 400 (Regular) |
| Metric value | JetBrains Mono | Consolas, Courier New | 500 (Medium) |
| Footer text | Inter | Helvetica Neue, Arial | 400 (Regular) |
| Footer timestamp | JetBrains Mono | Consolas, Courier New | 400 (Regular) |

## 3.2 Size Hierarchy

All sizes are in points (pt) at the canonical 600 × 800 canvas. Scale proportionally for other sizes.

| Element | Size | Line height | Letter spacing |
|---------|------|-------------|----------------|
| Title ("ED ARCHITECTURE") | 22 pt | 28 pt | +0.08 em |
| Subtitle ("CONSISTENCY CERTIFICATE") | 14 pt | 20 pt | +0.12 em |
| Version | 9 pt | 14 pt | +0.05 em |
| Verdict text | 28 pt | 34 pt | +0.06 em |
| Diagnostic label | 11 pt | 16 pt | 0 |
| Sub-metric label | 9 pt | 14 pt | 0 |
| Metric value | 12 pt | 16 pt | 0 |
| Sub-metric value | 9 pt | 14 pt | 0 |
| Footer statement | 8 pt | 12 pt | 0 |
| Footer timestamp | 8 pt | 12 pt | 0 |

## 3.3 Hierarchy Rules

1. **Title** is uppercase, tracked wide (+0.08 em), bold. It commands the top of the page.
2. **Subtitle** is uppercase, tracked wider (+0.12 em), regular weight. It is subordinate to the title.
3. **Verdict** is uppercase, tracked moderately, extra-bold. It is the single most prominent text element.
4. **Diagnostic labels** are sentence case, semi-bold. They anchor each row of the metrics table.
5. **Metric values** are monospaced, medium weight. They carry the quantitative content.
6. **Footer** is small, light, and unobtrusive. It provides provenance without competing for attention.

## 3.4 Accessibility

- All text meets WCAG 2.1 AA contrast ratio (≥ 4.5:1 for body text, ≥ 3:1 for large text).
- The verdict banner meets AAA (≥ 7:1) against its background.
- Monospaced text uses a font with clear distinction between O/0, I/l/1, and similar ambiguous glyphs (JetBrains Mono satisfies this).

---

# 4. Colour Palette Specification

## 4.1 PASS Palette (Primary)

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| Verdict background | #E8F5E9 | 232, 245, 233 | Verdict banner fill |
| Verdict border | #2E7D32 | 46, 125, 50 | Verdict banner stroke |
| Verdict text | #1B5E20 | 27, 94, 32 | "PASS" text |
| Accent | #43A047 | 67, 160, 71 | Icon fills, metric highlights |
| Accent light | #A5D6A7 | 165, 214, 167 | Sub-metric backgrounds |

## 4.2 PARTIAL Palette (Secondary)

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| Verdict background | #FFF8E1 | 255, 248, 225 | Verdict banner fill |
| Verdict border | #F9A825 | 249, 168, 37 | Verdict banner stroke |
| Verdict text | #E65100 | 230, 81, 0 | "PARTIAL" text |
| Accent | #FFB300 | 255, 179, 0 | Icon fills |
| Accent light | #FFE082 | 255, 224, 130 | Sub-metric backgrounds |

## 4.3 FAIL Palette (Tertiary)

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| Verdict background | #FFEBEE | 255, 235, 238 | Verdict banner fill |
| Verdict border | #C62828 | 198, 40, 40 | Verdict banner stroke (dashed) |
| Verdict text | #B71C1C | 183, 28, 28 | "FAIL" text |
| Accent | #E53935 | 229, 57, 53 | Icon fills |
| Accent light | #EF9A9A | 239, 154, 154 | Sub-metric backgrounds |

## 4.4 Neutral Palette

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| Title text | #1A1A2E | 26, 26, 46 | Header text |
| Body text | #2B2D42 | 43, 45, 66 | Labels, descriptions |
| Muted text | #8D99AE | 141, 153, 174 | Footer, timestamps |
| Table border | #D6D9E0 | 214, 217, 224 | Row separators |
| Table header bg | #F0F1F5 | 240, 241, 245 | Column header fill |
| Card background | #FFFFFF | 255, 255, 255 | Main background (light) |
| Page background | #FAFBFC | 250, 251, 252 | Outer background (light) |

## 4.5 Dark Mode

| Role | Hex | Usage |
|------|-----|-------|
| Card background | #1E1E2E | Main background |
| Page background | #11111B | Outer background |
| Title text | #CDD6F4 | Header text |
| Body text | #BAC2DE | Labels |
| Muted text | #6C7086 | Footer |
| Table border | #313244 | Row separators |
| PASS verdict bg | #1E3A2F | Banner fill |
| PASS verdict text | #A6E3A1 | "PASS" text |

---

# 5. Border and Box System

## 5.1 Box Styles

| Box | Border weight | Corner radius | Border style | Fill |
|-----|--------------|---------------|-------------|------|
| Header | 1.5 pt | 0 (square) | Solid | Card background |
| Verdict (PASS) | 2.5 pt | 4 pt | Solid | Verdict background |
| Verdict (PARTIAL) | 2.0 pt | 4 pt | Solid | Verdict background |
| Verdict (FAIL) | 2.0 pt | 4 pt | Dashed (8 pt on, 4 pt off) | Verdict background |
| Metrics table | 1.0 pt | 0 | Solid (outer only) | Card background |
| Metric row | 0.5 pt | 0 | Solid (bottom only) | Transparent |
| Footer | 0 pt | 0 | None (rule line above) | Transparent |

## 5.2 Spacing

| Element | Value |
|---------|-------|
| Header internal padding | 20 pt top/bottom, 24 pt left/right |
| Verdict internal padding | 16 pt top/bottom, 24 pt left/right |
| Metrics table internal padding | 16 pt top, 12 pt bottom, 24 pt left/right |
| Metric row height | 56 pt (main diagnostics), 32 pt (sub-metrics) |
| Metric row internal padding | 8 pt top/bottom |
| Footer internal padding | 12 pt top/bottom |
| Gap between zones | 12 pt |

## 5.3 Visual Hierarchy

The border system creates three levels of containment:

1. **Outer frame** — the certificate's overall boundary. Defined by the card background against the page background. No visible stroke; the shadow-free contrast is sufficient.
2. **Zone boxes** — the header, verdict, metrics, and footer. The header and verdict have visible borders; the metrics table has a thin outer border; the footer has only a top rule.
3. **Row separators** — within the metrics table, thin horizontal rules separate the five diagnostics. No vertical rules.

---

# 6. Verdict Banner

## 6.1 Structure

The verdict banner occupies Zone B (12% of canvas height). It is horizontally centred within the content width. Its internal structure is:

```
┌─────────────────────────────────────────────────┐
│                                                 │
│              [VERDICT TEXT]                      │
│              [Subtext: pass fraction]            │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 6.2 Three Variants

### PASS

| Property | Value |
|----------|-------|
| Border | 2.5 pt solid #2E7D32 |
| Fill | #E8F5E9 |
| Corner radius | 4 pt |
| Text | "PASS" in 28 pt Inter ExtraBold, #1B5E20 |
| Subtext | "All diagnostics satisfactory" in 10 pt Inter Regular, #43A047 |
| Symbolic mark | Solid circle (⬤) 8 pt, #2E7D32, left of text, vertically centred |

### PARTIAL

| Property | Value |
|----------|-------|
| Border | 2.0 pt solid #F9A825 |
| Fill | #FFF8E1 |
| Corner radius | 4 pt |
| Text | "PARTIAL" in 28 pt Inter ExtraBold, #E65100 |
| Subtext | "n/5 diagnostics satisfactory" in 10 pt Inter Regular, #F9A825 |
| Symbolic mark | Half-filled circle (◐) 8 pt, #F9A825, left of text |

### FAIL

| Property | Value |
|----------|-------|
| Border | 2.0 pt dashed #C62828 (8 on, 4 off) |
| Fill | #FFEBEE |
| Corner radius | 4 pt |
| Text | "FAIL" in 28 pt Inter ExtraBold, #B71C1C |
| Subtext | "Architecture inconsistency detected" in 10 pt Inter Regular, #E53935 |
| Symbolic mark | Open circle (○) 8 pt, stroke #C62828, left of text |

---

# 7. Metrics Table

## 7.1 Structure

The metrics table contains five rows, one per diagnostic. Each row has three columns:

| Column | Width | Alignment | Content |
|--------|-------|-----------|---------|
| Icon | 36 pt fixed | Centre | Geometric mark |
| Label | Flexible | Left | Diagnostic name (bold) + sub-metrics (regular) |
| Value | 120 pt fixed | Right (numbers), Left (verdicts) | Key metric + per-diagnostic verdict |

## 7.2 Row Definitions

### Row 1: Universality

| Field | Content |
|-------|---------|
| Icon | Concentric circles (see §8.1) |
| Label | **Universality** |
| Sub-label | Parameter-independence of invariant vectors |
| Value | U = {value} |
| Verdict chip | UNIVERSAL / WEAKLY / NOT |
| Accent colour | Verdict-dependent |

### Row 2: Cross-Consistency

| Field | Content |
|-------|---------|
| Icon | Interlocking rings (see §8.2) |
| Label | **Cross-Consistency** |
| Sub-label | Agreement between invariant families |
| Value | C = {value} |
| Verdict chip | CONSISTENT / PARTIAL / INCONSISTENT |

### Row 3: Stability

| Field | Content |
|-------|---------|
| Icon | Downward arrow (see §8.3) |
| Label | **Stability** |
| Sub-metrics (indented, smaller): | |
| — Positive Lyapunov exponents | n₊ = {value} |
| — Kaplan–Yorke dimension | D_KY = {value} |
| — Effective dimension (PCA) | D_eff = {value} |
| Verdict chip | STABLE / MARGINAL / UNSTABLE |

### Row 4: Embedding Collapse

| Field | Content |
|-------|---------|
| Icon | Cluster dot (see §8.4) |
| Label | **Embedding Collapse** |
| Sub-label | Invariant-space cluster tightness |
| Value | r = {value} |
| Verdict chip | COLLAPSED / DIFFUSE / SCATTERED |

### Row 5: Perturbation Recovery

| Field | Content |
|-------|---------|
| Icon | Return arrow (see §8.5) |
| Label | **Perturbation Recovery** |
| Sub-label | ε-independence of recovery rates |
| Value | CV = {value} |
| Verdict chip | ROBUST / SENSITIVE / FRAGILE |

## 7.3 Verdict Chips

Each row includes a small verdict chip: a rounded rectangle (corner radius 3 pt, height 18 pt) with the per-diagnostic verdict. Chip colours:

| Verdict class | Background | Text | Border |
|--------------|-----------|------|--------|
| Positive (UNIVERSAL, CONSISTENT, STABLE, COLLAPSED, ROBUST) | Accent light | Accent | Accent |
| Marginal (WEAKLY, PARTIAL, MARGINAL, DIFFUSE, SENSITIVE) | #FFF3E0 | #E65100 | #FFB300 |
| Negative (NOT, INCONSISTENT, UNSTABLE, SCATTERED, FRAGILE) | #FFEBEE | #C62828 | #E53935 |

## 7.4 Missing Data

If a diagnostic was not computed (script failed or was skipped):

- Icon: greyed out (opacity 0.3).
- Label: normal styling, with "(not computed)" appended in muted text.
- Value: em-dash "—" in muted monospace.
- Verdict chip: grey background, "N/A" text.

---

# 8. Iconography

All icons are geometric, monochrome (using the row's accent colour), constructed from basic shapes, and rendered at 24 × 24 pt within the 36-pt icon column.

## 8.1 Universality — Concentric Circles

Three concentric circles (radii 4, 8, 12 pt), all sharing a common centre. Stroke only, no fill. Stroke weight: 1.5 pt. Colour: diagnostic accent.

*Meaning:* Multiple parameter regimes (the circles) converge to the same centre (the attractor).

## 8.2 Cross-Consistency — Interlocking Rings

Two circles (radius 8 pt each), offset horizontally by 8 pt so they overlap in the centre. Stroke only, 1.5 pt. The overlap region is implied, not filled.

*Meaning:* Two independent measures (the rings) agree in their overlap.

## 8.3 Stability — Downward Converging Arrow

A chevron pointing downward: two lines meeting at a point at the bottom, forming a 60° angle. Stroke only, 1.5 pt. Total height: 16 pt, width: 16 pt.

*Meaning:* All trajectories converge downward (to the attractor).

## 8.4 Embedding Collapse — Cluster Dot

A central filled circle (radius 3 pt) surrounded by six smaller dots (radius 1.5 pt) arranged in a hexagonal pattern at radius 8 pt. The outer dots are at 50% opacity.

*Meaning:* Scattered points (the outer dots) collapsing toward a centre (the filled dot).

## 8.5 Perturbation Recovery — Return Arrow

A circular arc (270° of a circle, radius 8 pt, starting at 12 o'clock, sweeping clockwise) with an arrowhead at the terminal end (pointing back to 12 o'clock). Stroke only, 1.5 pt.

*Meaning:* The system returns to its starting state after perturbation.

## 8.6 Style Rules

| Property | Value |
|----------|-------|
| Stroke weight | 1.5 pt |
| Stroke cap | Round |
| Stroke join | Round |
| Colour | Row accent colour (from §4) |
| Canvas | 24 × 24 pt, centred in 36-pt column |
| Anti-aliasing | On |

---

# 9. Watermark / Background Motif

## 9.1 The Attractor Spiral

A logarithmic spiral (3 full turns, expanding from centre) is drawn as a single continuous curve. The spiral begins at the exact centre of the certificate canvas and expands outward. The curve uses a stroke weight of 0.5 pt and is rendered in the neutral body-text colour at **3% opacity** (light mode) or **5% opacity** (dark mode).

## 9.2 Placement

The spiral is centred on the certificate canvas, with its outermost turn reaching approximately 80% of the canvas width. It underlies all content but is behind every box, text element, and border. It is a background layer only.

## 9.3 Alternative Motif: Seven Converging Lines

Seven straight lines originate from the left edge of the canvas at evenly spaced vertical positions (spanning 60% of the canvas height, centred vertically). Each line converges toward a single point on the right edge at the vertical centre. The lines use 0.3 pt stroke weight at 4% opacity.

*Use:* the spiral is the default. The seven-line motif is an alternative for contexts where the spiral reads as decorative rather than structural.

## 9.4 Rules

- The watermark must never interfere with text readability.
- It must be invisible in greyscale print at low contrast.
- It must be perceptible on screen at full resolution as a subtle texture.
- It is omitted entirely if the rendering environment cannot guarantee sub-5% opacity fidelity.

---

# 10. Export Guidelines

## 10.1 Formats

| Format | Resolution | Use Case | Colour Profile |
|--------|-----------|----------|---------------|
| PDF | Vector | Print, archival, paper submission | CMYK (Fogra39) or sRGB |
| SVG | Vector | Web, interactive, Figma | sRGB |
| PNG | 300 DPI | Paper figures, press kit | sRGB |
| PNG | 150 DPI | Web thumbnails, social media | sRGB |
| PNG (2×) | 600 DPI | Retina displays, zoomed views | sRGB |

## 10.2 Safe Margins

Add 12 pt (1/6 inch) of transparent margin around the certificate boundary in all raster exports. This prevents clipping when the figure is embedded in documents with tight margins.

## 10.3 Colour-Profile Notes

- The PASS green (#2E7D32) maps to CMYK (82, 18, 100, 6). Verify on proof.
- The PARTIAL amber (#F9A825) maps to CMYK (0, 37, 90, 0). Vibrant; may need desaturation for CMYK print.
- The FAIL red (#C62828) maps to CMYK (8, 92, 85, 1). Stable in CMYK.
- All neutrals (#1A1A2E, #2B2D42) are near-black and map cleanly.

## 10.4 Background Transparency

- PDF: opaque white background.
- SVG: transparent background (card background is an explicit white rectangle).
- PNG: opaque white background for print; transparent option for web compositing.

---

# 11. Implementation Notes

## 11.1 matplotlib Implementation

The certificate can be generated entirely within matplotlib using `fig.add_axes()` for precise box placement and `fig.text()` for all typography. Key implementation details:

**Canvas setup:**
```
fig = plt.figure(figsize=(6, 8), dpi=300)
fig.patch.set_facecolor('#FAFBFC')
```

**Zone placement:** Use `fig.add_axes([left, bottom, width, height])` in figure-fraction coordinates. The header box is `[0.08, 0.77, 0.84, 0.18]`. The verdict banner is `[0.08, 0.63, 0.84, 0.12]`. The metrics table is `[0.08, 0.19, 0.84, 0.42]`. The footer is `[0.08, 0.05, 0.84, 0.12]`.

**Box drawing:** Use `FancyBboxPatch` from `matplotlib.patches` for rounded-corner boxes. Set `boxstyle='round,pad=0.01,rounding_size=0.005'` for the verdict banner. Use `Rectangle` for square-cornered boxes.

**Typography:** Use `fig.text()` with `fontfamily='Inter'` (or fallback). Set `fontweight` and `fontsize` per the hierarchy. For monospaced values, use `fontfamily='JetBrains Mono'`. Ensure fonts are installed or embedded.

**Icons:** Render using `matplotlib.patches` primitives: `Circle`, `Arc`, `FancyArrowPatch`. Place in small axes with `set_xlim`, `set_ylim`, and `set_aspect('equal')`.

**Watermark:** Draw the spiral using `plt.plot()` in polar coordinates converted to Cartesian, on a background axes with `zorder=-1` and `alpha=0.03`.

**Verdict chips:** Use `FancyBboxPatch` with `boxstyle='round,pad=0.003,rounding_size=0.008'`, filled with the chip colour, and overlay `text()` centred within.

**Export:** `fig.savefig('certificate.pdf', bbox_inches='tight', pad_inches=0.17)` for PDF. Replace extension for PNG/SVG.

## 11.2 Illustrator / Figma Implementation

**Layer structure (bottom to top):**

1. `Background` — page background fill (#FAFBFC)
2. `Watermark` — spiral motif at 3% opacity
3. `Boxes` — header, verdict, metrics, footer rectangles
4. `Borders` — box strokes (separate layer for easy colour swapping)
5. `Icons` — five geometric marks
6. `Typography` — all text elements
7. `Chips` — verdict chip rectangles + text

**Font embedding:** Ensure Inter and JetBrains Mono are embedded (not outlined) in PDF exports for accessibility and searchability. Outline only for final print if required by the printer.

**Colour swapping:** The three verdict variants (PASS / PARTIAL / FAIL) should be implemented as three **symbol overrides** or **component variants** in Figma, or as three **graphic styles** in Illustrator. The neutral palette is constant across all variants; only the verdict-dependent colours change.

**Artboard:** 600 × 800 pt. Use point units throughout (not pixels) for print fidelity.

---

# 12. Full Figure Description

## 12.1 Paper Caption (for ED-SIM-01 manuscript)

**Figure 7.** *ED Architecture Certificate (PASS variant).* The certificate summarises the global structural verdict of the ED-SIM-01 invariant atlas. The header (top) identifies the document as the ED Architecture Consistency Certificate, version 1.0.0. The verdict banner (centre-top) displays the final verdict — PASS, indicating that all five global diagnostics are satisfactory. The metrics table (centre) reports the five diagnostics: universality score $U$, cross-consistency score $C$, stability indicators (number of positive Lyapunov exponents $n_+$, Kaplan–Yorke dimension $D_{\mathrm{KY}}$, effective PCA dimension $D_{\mathrm{eff}}$), embedding cluster radius $r$, and perturbation-recovery coefficient of variation. Each diagnostic carries a per-row verdict chip (UNIVERSAL, CONSISTENT, STABLE, COLLAPSED, ROBUST). Geometric icons in the left column encode the diagnostic type. The footer provides the reproducibility statement, generation timestamp, and pipeline version. A logarithmic-spiral watermark at 3% opacity underlies the entire figure, representing the attractor convergence motif. The certificate is machine-generated by `generate_master_index_and_certificate.py` and is fully reproducible.

## 12.2 Website Description

The ED Architecture Certificate is the single-page summary of the Event Density invariant atlas. It encodes five structural diagnostics — universality, consistency, stability, embedding, and recovery — into a clear visual verdict: PASS (green), PARTIAL (amber), or FAIL (red). Every number on the certificate is computed from sixty-four simulations and sixteen invariant families. The certificate can be regenerated from scratch with a single command.

## 12.3 Press-Kit One-Sentence Version

The ED Architecture Certificate is a machine-generated, fully reproducible one-page document that summarises whether the Event Density mathematical framework is structurally self-consistent across all tested parameter regimes.

---

*Design specification for the Event Density Research Program. ED-SIM v1.0.0.*
