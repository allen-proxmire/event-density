# ED Atlas — Suggested Text Overlays

Suggested titles, overlay lines, and placement notes for every PNG in
`docs/figures/atlas/`, in the order of `docs/ED_Presentation_Draft.md`.

Overlays are *suggestions only*. PNGs are not modified.

---

## Prologue

### A1_non_negativity.png
**Suggested title:** Axiom 1 — The count is never negative
**Suggested overlay text:**
- (top) The tally of events is always ≥ 0
- (bottom, subtitle) You can't un-happen an event
**Placement:** Title across the top band above the clouds. Subtitle along the bottom, below the pedestal. Leave the rain-gauge silhouette clear.
**Formula placement:** `ED(A) ≥ 0` centered directly under the glowing amber floor line, between the gauge pedestal and the bottom edge.

---

### A2_null_baseline.png
**Suggested title:** Axiom 2 — If there's nothing, the count is exactly zero
**Suggested overlay text:**
- (top) Empty region ⇒ exactly zero
- (bottom, subtitle) Not approximately zero — *exactly* zero
**Placement:** Title across the top to the left of the sun. Subtitle along the bottom under the pedestal. Do not cover the central halo/needle dial.
**Formula placement:** `ED(∅) = 0` centered under the pedestal, aligned with the glowing floor.

---

### A3_monotonicity.png
**Suggested title:** Axiom 3 — A bigger region never has fewer events
**Suggested overlay text:**
- (top) A ⊆ B ⇒ the count on A never exceeds the count on B
- (bottom, subtitle) Expanding the window cannot lose events
**Placement:** Title across the top, spanning both the nested-set panel and the measurement columns. Subtitle at the bottom. Leave the small "circle-in-circle" glyph visible.
**Formula placement:** `A ⊆ B ⇒ ED(A) ≤ ED(B)` in the upper-right corner, just above the amber measurement column.

---

### A4_subadditivity.png
**Suggested title:** Axiom 4 — Don't double-count the overlap
**Suggested overlay text:**
- (top) Counting A and B separately double-counts the shared region
- (bottom, subtitle) Overlap counted *once*, not twice
**Placement:** Title across the top. Subtitle along the bottom. Do not cover the violet lens.
**Formula placement:** `ED(A ∪ B) ≤ ED(A) + ED(B)` centered between the Venn circles and the two comparison columns, roughly at the arrow's height.

---



---

### Compositional_Rule.png
**Suggested title:** At cosmological scale: three geometric corrections
**Suggested overlay text:**
- (top) Relational + gradient + boundary/horizon
- (near the violet lens) Overlap = relational penalty
- (near the cyan ridge fan) Steep gradients = gradient penalty
- (near the outer amber rim) Edges = boundary / horizon
**Placement:** Title across the top. Three tiny inline labels may attach to each correction-badge's arrow tail (violet bottom-center, cyan left, amber right). Keep the field imagery uncluttered.
**Formula placement:**
`p(A ∪ B) = p(A) + p(B) − α∫_{A∩B} p^γ dμ − β∫_{A∪B} |∇p|² dμ − γ∫_{∂(A∪B)} h(|∇p|) dS`
Place as one long line centered under the field, above the violet badge at the bottom.

---

## Interlude — The Seven Constraints

### Locality.png
**Suggested title:** Constraint 1 — Updates depend only on neighbors
**Suggested overlay text:**
- (top) The next state at x depends only on ρ in a small neighborhood around x
- (bottom, subtitle) No action at a distance · no long-range telepathy
**Placement:** Title across the top above the stencil. Subtitle across the bottom. Keep the central anchor cell and the faded "forbidden" long-range links uncovered.
**Formula placement:** `F[ρ](x) = F(ρ(x), ∇ρ(x), ∇²ρ(x), …)` centered under the stencil, just above any red-slash far-cell glyphs.

---

### Isotropy.png
**Suggested title:** Constraint 2 — No preferred direction
**Suggested overlay text:**
- (top) Rotate by any angle — the dynamics are identical
- (bottom, subtitle) No built-in axis · all directions are equal
**Placement:** Title across the top above the wavefronts. Subtitle along the bottom. Keep the cyan orb, the 16 radial arrows, and the three circular wavefronts clear.
**Formula placement:** `F[R·ρ] = R·F[ρ]   for every rotation R` centered just below the outermost dotted wavefront, between the two violet rotation arcs.

---

### GradientFlow.png
**Suggested title:** Constraint 3 — Flux follows slopes
**Suggested overlay text:**
- (upper-left, near the amber hill badge) HIGH
- (lower-right, near the navy valley badge) LOW
- (bottom, subtitle) Current runs downhill along −∇ρ · steeper slope, stronger flux
**Placement:** The two corner glyphs get single-word tags. Subtitle along the very bottom. Keep the cyan downhill-arrow grid and the amber iso-contours unobscured.
**Formula placement:** `J = −M(ρ) ∇ρ` centered along the top, spanning the diagonal from the amber high region to the navy low region.

---

### Dissipative.png
**Suggested title:** Constraint 4 — Energy decreases over time
**Suggested overlay text:**
- (above panel 1) t₁ — hot-spot
- (above panel 2) t₂ — broadening
- (above panel 3) t₃ — nearly spent
- (bottom, subtitle) No perpetual motion · the arrow of time is built in
**Placement:** Tiny tags above each snapshot with its clock badge. Subtitle along the very bottom, beside the red double-chevron arrow-of-time glyph.
**Formula placement:** `dE/dt ≤ 0` centered above the exponential E(t) curve, just under the three snapshot panels.

---

### ScalarField.png
**Suggested title:** Constraint 5 — One scalar field, nothing more
**Suggested overlay text:**
- (upper-right, near the one-chip swatch) one value per point
- (bottom, subtitle) Not a vector · not a tensor · a single real number ρ(x, t)
**Placement:** A short tag beside the pill-shaped color swatch with a thin leader to the probe dot. Subtitle along the very bottom. Keep the two red-slash "not-this" badges (vector / tensor) clear — they carry the negation visually.
**Formula placement:** `ρ : ℝ^d × ℝ → ℝ` centered along the top, above the violet field.

---

### MinimalCoupling.png
**Suggested title:** Constraint 6 — One clean coupling, nothing extra
**Suggested overlay text:**
- (above ρ globe) ρ — scalar field
- (above ν sphere) ν — participation
- (above cyan top arrow) F[ρ] → ν
- (below amber bottom arrow) H·ν → ρ
- (bottom, subtitle) No extra channels · no hidden variables
**Placement:** Short one-word tags hovering over each globe and over each arrow of the shaft. Subtitle along the very bottom. Keep the four red-slash ghost nodes in the corners uncovered — they make the minimality claim visually.
**Formula placement:** `τ ν̇ = F[ρ] − ζ ν` centered beneath the coupling shaft, between the two nodes.

---

### DimensionalConsistency.png
**Suggested title:** Constraint 7 — Every term carries the same units
**Suggested overlay text:**
- (above the crown) universal invariant
- (above left pan) [LHS] — same units
- (above right pan) [RHS] — same units
- (bottom, subtitle) No arbitrary constants · a scale-honest equation
**Placement:** Crown tag directly above the golden star. Matching pan tags floating above each pan's rim. Subtitle across the very bottom, above the ruler ticks. Keep the beam, the fulcrum triangle, and the six unit cubes with their color-coded tags unobscured.
**Formula placement:** `[ ∂_t ρ ] = [ D · F[ρ] ] = [ H · ν ]` centered just under the "=" badge below the pedestal.

---

## Act I — Seven demands, one equation

### P1_operator_structure.png
**Suggested title:** Demand 1 — The operator has one fixed shape
**Suggested overlay text:**
- (top) Mobility spreads outward · Penalty pulls inward
- (bottom, subtitle) These two tendencies compose the ED operator
**Placement:** Title across the top. Subtitle along the bottom. Leave the central blue globe and the surrounding cyan arrows / amber springs uncovered.
**Formula placement:** `F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)` centered under the bottom edge of the anchor ring.

---

### P2_channel_complementarity.png
**Suggested title:** Demand 2 — Two channels, summing to one
**Suggested overlay text:**
- (above cyan vessel) D channel — direct F[ρ]
- (above amber vessel) H channel — mediated ν
- (bottom, subtitle) Turn one up, the other goes down
**Placement:** Two small vessel tags just above each vessel's rim. Subtitle across the bottom.
**Formula placement:** `∂_t ρ = D·F[ρ] + H·ν,  D + H = 1` centered immediately above the top unit-length split bar, or directly under the bar.

---

### P3_penalty_equilibrium.png
**Suggested title:** Demand 3 — One preferred state
**Suggested overlay text:**
- (near the red ball) ρ* — the equilibrium
- (bottom, subtitle) Penalty vanishes at ρ*, positive everywhere else
**Placement:** A small label with a thin leader line pointing to the red ball at the bowl's bottom. Subtitle across the very bottom below the glowing baseline.
**Formula placement:** `P(ρ*) = 0,  P'(ρ*) > 0` placed above the top of the bowl, centered, not overlapping the curve's apex.

---

### P4_mobility_capacity_bound.png
**Suggested title:** Demand 4 — Mobility shuts off at capacity
**Suggested overlay text:**
- (above top-panel curve) M(ρ) decreases as ρ rises
- (right end, near the wall) Jammed — motion stops
- (left end, over cyan particles) Free-flowing
**Placement:** Small inline labels above each zone of the channel. Do not cover the red ρ_max wall hatching.
**Formula placement:** `M(ρ_max) = 0,  M(ρ) > 0  for ρ < ρ_max` under the bottom ρ-axis, centered between the 0 and the red tick at ρ_max.

---

### P5_participation_feedback.png
**Suggested title:** Demand 5 — Participation responds and remembers
**Suggested overlay text:**
- (above driver tile) Input — F[ρ]
- (above integrator tile) Output — ν
- (bottom trace) ν tracks F with a lag
**Placement:** Tiny labels hanging above the four nodes of the loop diagram (driver, summer, integrator, damping). The two-line caption for the time trace goes under the waveforms.
**Formula placement:** `τ ν̇ = F[ρ] − ζ ν` centered inside the ring, just above or below the summer.

---

### P6_damping_discriminant.png
**Suggested title:** Demand 6 — A sharp threshold divides oscillation from decay
**Suggested overlay text:**
- (left panel) Underdamped — rings and decays
- (right panel) Overdamped — glides home
- (center, below the ridge) D_crit = 0.5
**Placement:** One short label per panel at the top, leaving both waveforms and rigs visible. The threshold label sits directly on the golden ridge, either at the peak or on the amber axis-tick below.
**Formula placement:** `Δ = D + 2ζ,  D_crit = 0.5  (sharp)` along the very bottom, centered on the critical tick.

---

### P7_nonlinear_triad.png
**Suggested title:** Demand 7 — Three modes make a fourth
**Suggested overlay text:**
- (upper-left badge) k₁
- (lower-left badge) k₂
- (right badge) k₃ = k₁ + k₂
**Placement:** Letters directly inside or beside each wave-icon badge. Keep them short; the k-space vector triangle in the inset is self-explanatory.
**Formula placement:** `M'(ρ)|∇ρ|²  generates  k₃ = k₁ ± k₂` centered below the main mixer/wave composition, above the k-space inset.

---

### D19_uniqueness.png
**Suggested title:** Uniqueness — eleven demands, one equation
**Suggested overlay text:**
- (upper-left, above the axiom-orbs) 4 axioms
- (lower-left, below the principle-orbs) 7 principles
- (right, near the ghosts) Alternatives ruled out
- (below the output orb) The unique ED PDE
**Placement:** Short group-labels on the left column next to the two stacks of orbs; a small badge callout on the right over the ghost orbs; the PDE tag below the luminous right orb.
**Formula placement:** Optional single line `4 axioms + 7 principles ⇒ 1 PDE` centered below the whole composition, under the amber tally mark.

---

### UnifiedPDE.png
**Suggested title:** The Unified PDE
**Suggested overlay text:**
- (over the blue globe) ρ — scalar density field
- (over the amber sphere) ν — participation
- (above the coupling shaft arrows) F[ρ] → ν  and  H·ν → ρ
**Placement:** Short labels hovering over each machine. Keep the satellite operator badges uncovered so each channel reads visually.
**Formula placement:** Place the full system as a stacked block, centered just above or below the golden frame:
- Line 1: `∂_t ρ = D·[ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ] + H·ν`
- Line 2: `τ ν̇ = F̃(ρ) − ζ ν`
- Line 3 (smaller, side-by-side): `M(ρ) = M₀ (ρ_max − ρ)^β` and `P_SY2(ρ) = αγ · (ρ − ρ*) / √((ρ − ρ*)² + ρ₀²)`

---

## Act II — Three channels, three familiar physics

### Mobility_alone.png
**Suggested title:** Channel 1 — Pure spatial spreading
**Suggested overlay text:**
- (top) Mobility only — no penalty, no participation
- (bottom inset) Three time snapshots: solid → dashed → dotted
**Placement:** Title across the top above the clouds. The inset-caption sits above the bottom inset panel.
**Formula placement:** `∂_t ρ = D ∇·[ M(ρ) ∇ρ ]` centered below the main 2D cloud, above the inset panel.

---

### Penalty_alone.png
**Suggested title:** Channel 2 — Pure relaxation to equilibrium
**Suggested overlay text:**
- (above the three slabs) Uniform field — no spatial structure
- (near the glowing ρ* line, bottom) ρ* — equilibrium
**Placement:** One short caption just above the three snapshot tiles. A small tick label on the left end of the glowing baseline for ρ*.
**Formula placement:** `∂_t ρ = −D P₀ (ρ − ρ*)` centered under the decay curve, just above the time-axis arrow.

---

### Participation_alone.png
**Suggested title:** Channel 3 — Pure temporal response
**Suggested overlay text:**
- (over pulsing node, left) Driver — F[ρ]
- (right-end, on the settled node) ν settles
- (top, above peak dot) Overshoot · ring · settle
**Placement:** Short label adjacent to the input node; second label near the right-end steady orange node; a thin tag above the first peak.
**Formula placement:** `τ ν̇ + ζ ν = F̃(ρ)` centered under the curve's mid-section, above the horizontal time axis.

---

### PME_porous_medium.png
**Suggested title:** Mobility's textbook fingerprint — porous medium equation
**Suggested overlay text:**
- (over puddle) Barenblatt profile — flat plateau + sharp edge
- (below inset) Front decelerates as time increases
**Placement:** Caption over the main puddle/porous panel. A second short line just above the bottom 1D-profile inset.
**Formula placement:**
- `∂_t δ = D_pme ∇² (δ^m),  m = β + 1` below the main porous panel, above the inset.
- `Barenblatt:  R(t) ∝ t^{1 / [d(m−1) + 2]}` as a smaller second line directly beneath the first.

---

### RC_debye.png
**Suggested title:** Penalty's textbook fingerprint — Debye / RC exponential
**Suggested overlay text:**
- (near the schematic) Discharging RC circuit
- (over curve) Monotone exponential decay to ρ*
- (right end, on baseline) ρ*
**Placement:** Short label floating above the schematic panel (top-left). A second label in the empty upper half of the curve panel, above the third snapshot.
**Formula placement:**
- `ρ(t) = ρ* + (ρ₀ − ρ*) e^{−t / τ_RC}` centered along the top of the curve panel.
- `τ_RC = 1 / (D P₀)` as a smaller second line directly under the main formula.

---

### RLC_oscillator.png
**Suggested title:** Participation's textbook fingerprint — RLC oscillator
**Suggested overlay text:**
- (near the schematic) RLC loop — inductor · resistor · capacitor
- (above the envelope) Exponential envelope
- (below the curve) Damped sinusoid
**Placement:** One short label beside the RLC schematic. Curve captions sit just above (envelope) and just below (sinusoid) the central waveform, near the first peak for maximum read.
**Formula placement:**
- `τ v̈ + ζ v̇ + v = 0` centered above the main waveform.
- `ω = √( 1/τ − (ζ / 2τ)² )` as a smaller second line below the first.

---

## Act III — Does nature actually do this?

### UDM_universal.png
**Suggested title:** Mobility confirmed — 11 materials, one law
**Suggested overlay text:**
- (top) Universal diffusion mobility law
- (bottom, above legend strip) 11 materials · R² > 0.986 · no per-material tuning
- (corner badge) CONFIRMED ✓
**Placement:** Title across the top of the plot. The performance line sits above the bottom legend strip. Put a small green "CONFIRMED" tag in the upper-right corner of the plot card.
**Formula placement:** `D(c) = D₀ (1 − c/c_max)^β` centered just below the title, inside the upper portion of the plot frame.

---

### CMLag_merger.png
**Suggested title:** Penalty confirmed — cluster mergers leave a lag
**Suggested overlay text:**
- (near left cluster) Moving cluster
- (near each wake tip) Trailing density peak
- (under each lag bracket) ℓ = lag length
- (bottom) 7 clusters + Finner+25 aggregate of 58 subclusters · CONFIRMED ✓
**Placement:** Tiny labels at cluster cores and wake tips. Bracket labels sit between the dashed guide lines under each bracket. Summary line across the very bottom.
**Formula placement:**
- `ℓ = D_T / v_current` centered at the top, spanning between the two clusters.
- `D_T = 2.1 × 10²⁷ m²/s  (from Mistele WL)` as a smaller second line directly beneath.

---

### FRAP_BSA.png
**Suggested title:** Participation — the pending bet on BSA
**Suggested overlay text:**
- (over microscope field) Bleached spot recovers with *ringing*, not smooth diffusion
- (above the curve) RLC-like recovery signature predicted
- (corner) PENDING ⏳ — Creative Proteomics technician review
**Placement:** Short caption above the circular microscope field. A second caption above the curve. Put a small amber "PENDING" tag in the upper-right corner of the curve panel.
**Formula placement:** `τ ρ̈ + ζ ρ̇ + ρ = 0` centered above the recovery curve.

---

## Act IV — What falls out for free

### DimInv.png
**Suggested title:** Dimensional invariant — one ratio across 61 orders of magnitude
**Suggested overlay text:**
- (top) Across 5 regimes: Planck · quantum · condensed matter · galactic · cosmological
- (center, under the gold orb) Same dimensionless ratio in every badge
**Placement:** Top line across the dark sky. Secondary line hugging the bottom edge, below the pentagon of regime badges.
**Formula placement:** `D · T₀ / L₀² = 0.3` centered directly beneath the central gold core, between the core and the two lower regime badges.

---

### SharpBif.png
**Suggested title:** Sharp bifurcation — Δ_crit = 0.5
**Suggested overlay text:**
- (left panel) Oscillatory regime — D < 0.5
- (right panel) Overdamped regime — D > 0.5
- (on the central ridge) Knife-edge transition
**Placement:** Two short tags at the top of each panel. A thin label near the top of the golden ridge (or just to the right of the balance ball).
**Formula placement:** `Δ = D + 2ζ = 1  →  D_crit = 0.5` along the bottom, centered over the amber critical tick.

---

### UniversalInv.png
**Suggested title:** Universal invariants — different beginnings, same ending
**Suggested overlay text:**
- (around the central gold orb, inside the panel) Universal attractor
- (below the inset) E_ground baseline · same τ_rel for every trajectory
**Placement:** A compact tag just above or beside the central attractor orb. Inset caption along the bottom of the decay panel.
**Formula placement:**
- `E_ground = α γ ρ₀` at the right end of the glowing ρ* baseline in the inset.
- `τ_rel ≈ ρ₀ / (α γ)` over the dashed vertical τ line, near the small clock badge.

---

### TriadCoupling.png
**Suggested title:** Triad coupling — spectral fingerprint of P7
**Suggested overlay text:**
- (over tall cyan peak) k₁
- (over tall green peak) k₂
- (over small amber peak) k₃ = k₁ + k₂
- (next to right-side ratio bar) ~3–6% of primaries
**Placement:** Tiny k-labels next to each peak badge. The amplitude-ratio caption hangs to the right of the vertical bar.
**Formula placement:** `C ≈ 0.03,  k₃ / k₁ = 3–6%` centered under the axis arrow, bottom of the plot frame.

---

### dConsistency.png
**Suggested title:** d-consistency — same rule in 1D, 2D, 3D
**Suggested overlay text:**
- (under panel 1) d = 1 — line
- (under panel 2) d = 2 — surface
- (under panel 3) d = 3 — volume
- (near the central gold orb) Same formula, all dimensions
**Placement:** Short dimension tags just under each panel's dim-badge. A compact line hanging below the central invariant orb or beside it.
**Formula placement:** `α_R = 1 / [ d (m − 1) + 2 ]` centered at the top, just below the gold core's starburst.

---

### EDSC2.png
**Suggested title:** ED-SC 2.0 — r* ≈ −1.304 across 20 orders of magnitude
**Suggested overlay text:**
- (over left badge) Scenario D — ED simulation
- (over center badge) Local Group mass sheet — cosmological
- (over right badge) Casimir cavity — nanoscale
- (above the violet star-badge) Universal curvature median
**Placement:** Short system tags directly above each of the three top-row badges. A one-line label hovers just above the violet star on the r* line.
**Formula placement:** `r* = med ℛ_motif (∇²E) ≈ −1.304` centered along the bottom axis, just above or below the violet r* tick.


### SaddleGeometry.png. Script: analysis/scripts/atlas/SaddleGeometry_visual_only.py.

Composition matching the existing atlas style:

Backdrop — the shared pale blue gradient + warm amber floor band used across the other atlas PNGs.
Main centerpiece — a 3D saddle surface z = x² − y² viewed at elev=26°, azim=−58° (classic Pringle pose). Shaded with a custom cyan → pale → amber diverging cmap so the two "up" corners glow amber and the two "down" corners sit in cyan. Faint navy wireframe over the surface reinforces the chip-like ridged texture.
Principal-axis curves traced directly on the surface — amber ridge along the expansion axis (y=0, z=x² with an amber glow underlay), cyan valley along the compression axis (x=0, z=−y² with a cyan glow underlay). Small colored end-markers at each axis tip suggest the arrows without cluttering the 3D scene.
Saddle point — golden dot at the origin with two halo rings and an inner pale core (same gold palette as the DimInv / UniversalInv invariant orbs).
Four structural tags in the corners, as rounded color-coded pills:
Upper left (rose) — det(H) < 0 saddle
Upper right (amber) — κ⊥ > 0 expansion
Lower left (cyan) — κ∥ < 0 compression
Lower right (lavender, matching the Seven Constraints palette) — r* = λ∥/λ⊥ ≈ −1.304
Title bar at top — "Saddle Geometry" with the one-line subtitle "one axis compresses | one axis expands | det(H) < 0".
Legend swatches along the amber floor — three small circles keyed to expansion axis / compression axis / saddle point.
Drops naturally into the slide deck near the ED-SC 2.0 / scale correspondence beat if you want to precede that slide with the geometric primitive, or tuck it into the ED-Arch-02 explanation layer anywhere the saddle motif needs to be shown before the invariant claim.


---

## Coda

### ScenarioD.png
**Suggested title:** Scenario D — a noisy universe finds its architecture
**Suggested overlay text:**
- (top) Random seeds at t = 0
- (bottom) Emergent saddles · filaments · curvature — ED dynamics, running
- (near any saddle glyph) Saddle points = ED-SC 2.0 signature
**Placement:** Two short phrases at the top and bottom of the framed cosmological patch. One optional leader line from a saddle glyph to a tiny tag.
**Formula placement:** None required — Scenario D is a simulation frame, not a formula slide. If a tag is wanted, a small corner label "ED-SIM · Scenario D" sits inside one of the amber L-brackets.

---

## Closer

### Grid_3x3_story.png
**Suggested title:** The Event Density framework in one image
**Suggested overlay text:**
- (left of row 1, cyan strip) Mobility
- (left of row 2, amber strip) Penalty
- (left of row 3, coral strip) Participation
- (above column 1) Channel
- (above column 2) Textbook analogue
- (above column 3, amber header) Data
**Placement:** Row labels on the left accent strips; column labels in the top header bars. Keep them short — single words.
**Formula placement:** Optionally a single bottom-band caption, centered along the amber strip at the very bottom:
`Three channels → three classical physics → three empirical confirmations.`

---

*End of overlay suggestions.*

*Copilot overlay suggestions Begin*

---

# ED Atlas — Suggested Text Overlays (Full Set)

---

# PROLOGUE — THE FOUR AXIOMS + COMPOSITIONAL RULE

## A1_non_negativity.png
**Suggested Title (top‑center):**  
Axiom 1 — The count is never negative

**Suggested Overlay Text (lower‑left):**  
“Event density ≥ 0.  
You can’t un‑happen an event.”

**Optional Formula (bottom‑right):**  
ρ(x) ≥ 0

**Placement Notes:**  
• Keep text away from the water column.  
• Formula near the gauge base reinforces the “hard floor.”

---

## A2_null_baseline.png
**Suggested Title (top‑center):**  
Axiom 2 — If there’s nothing, the count is exactly zero

**Suggested Overlay Text (lower‑left):**  
“Empty region → event density = 0.  
Zero means zero.”

**Optional Formula (bottom‑right):**  
ρ(x) = 0

**Placement Notes:**  
• Place text near the empty gauge body.  
• Formula near the bottom boundary line.

---

## A3_monotonicity.png
**Suggested Title (top‑center):**  
Axiom 3 — A bigger region never has fewer events

**Suggested Overlay Text (lower‑left):**  
“If A ⊂ B, then ED(A) ≤ ED(B).  
Expanding your window cannot lose events.”

**Optional Formula (bottom‑right):**  
ρ(A) ≤ ρ(B)

**Placement Notes:**  
• Place text near the bar‑chart metaphor.  
• Formula near the smaller bar.

---

## A4_subadditivity.png
**Suggested Title (top‑center):**  
Axiom 4 — Don’t double‑count the overlap

**Suggested Overlay Text (lower‑left):**  
“ED(A ∪ B) ≤ ED(A) + ED(B).  
The violet region counts only once.”

**Optional Formula (bottom‑right):**  
ρ(A ∪ B) ≤ ρ(A) + ρ(B)

**Placement Notes:**  
• Place text near the violet overlap zone.  
• Formula near the bars showing the phantom band.

---

# ED Atlas — Suggested Text Overlays for the Seven Constraints

---

## Locality.png
**Suggested Title (top‑center):**  
Locality — updates depend only on neighbors

**Suggested Overlay Text (lower‑left):**  
“Only nearby values influence the update.  
No long‑range telepathy.”

**Optional Formula (bottom‑right):**  
F[ρ](x) depends only on ρ(x + ε)

**Placement Notes:**  
• Place text near the local stencil or neighborhood kernel.  
• Keep arrows short to emphasize locality.

---

## Isotropy.png
**Suggested Title (top‑center):**  
Isotropy — no preferred direction

**Suggested Overlay Text (lower‑left):**  
“Same behavior in every direction.  
No built‑in orientation.”

**Optional Formula (bottom‑right):**  
F[Rρ] = R F[ρ]

**Placement Notes:**  
• Place text near the radial symmetry pattern.  
• Keep the center unobscured.

---

## GradientDrivenFlow.png
**Suggested Title (top‑center):**  
Gradient‑driven flow — flux follows slopes

**Suggested Overlay Text (lower‑left):**  
“Flow moves from high to low.  
Gradients drive dynamics.”

**Optional Formula (bottom‑right):**  
J = −M ∇ρ

**Placement Notes:**  
• Place text near the downhill arrows.  
• Formula near the steepest‑descent region.

---

## DissipativeStructure.png
**Suggested Title (top‑center):**  
Dissipative structure — energy decreases

**Suggested Overlay Text (lower‑left):**  
“No perpetual motion.  
Dynamics relax over time.”

**Optional Formula (bottom‑right):**  
dE/dt ≤ 0

**Placement Notes:**  
• Place text near the fading high‑energy region.  
• Formula near the cooling gradient.

---

## SingleScalarField.png
**Suggested Title (top‑center):**  
Single scalar field — ρ is the only degree of freedom

**Suggested Overlay Text (lower‑left):**  
“One field.  
No vectors, no tensors.”

**Optional Formula (bottom‑right):**  
ρ = ρ(x, t)

**Placement Notes:**  
• Place text near the smooth scalar surface.  
• Keep the field uncluttered.

---

## MinimalCoupling.png
**Suggested Title (top‑center):**  
Minimal coupling — ν interacts only through F[ρ]

**Suggested Overlay Text (lower‑left):**  
“No extra channels.  
One clean feedback loop.”

**Optional Formula (bottom‑right):**  
ν̇ ∝ F[ρ] − ζν

**Placement Notes:**  
• Place text near the simple two‑node coupling.  
• Formula near the feedback arrow.

---

## DimensionalConsistency.png
**Suggested Title (top‑center):**  
Dimensional consistency — units match everywhere

**Suggested Overlay Text (lower‑left):**  
“No arbitrary constants.  
Scale‑honest equation.”

**Optional Formula (bottom‑right):**  
[LHS units] = [RHS units]

**Placement Notes:**  
• Place text near the balanced scale or geometric unit cube.  
• Keep the balance beam unobscured.



---

## Compositional_Rule.png
**Suggested Title (top‑center):**  
Subadditivity becomes geometry

**Suggested Overlay Text (lower‑left):**  
“Three corrections appear:  
• relational penalty  
• gradient penalty  
• boundary / horizon term”

**Optional Formula:**  
None

**Placement Notes:**  
• Align bullets near their colored regions.  
• Keep spacing generous.

---

# ACT I — THE SEVEN PRINCIPLES + UNIQUENESS + UNIFIED PDE

## P1_operator_structure.png
**Suggested Title (top‑center):**  
Demand 1 — One fixed operator shape

**Suggested Overlay Text (lower‑left):**  
“Mobility pushes outward.  
Penalty pulls inward.  
F = mobility − penalty.”

**Optional Formula (bottom‑right):**  
F[ρ] = ∇·(M∇ρ) − P(ρ)

**Placement Notes:**  
• Place text near the arrows and springs.  
• Formula near the density cloud.

---

## P2_channel_complementarity.png
**Suggested Title (top‑center):**  
Demand 2 — Two channels summing to one

**Suggested Overlay Text (lower‑left):**  
“Direct channel + participation channel = 1.  
Turning one up turns the other down.”

**Optional Formula (bottom‑right):**  
D + H = 1

**Placement Notes:**  
• Place text near the two vessels.  
• Formula near the unit bar.

---

## P3_penalty_equilibrium.png
**Suggested Title (top‑center):**  
Demand 3 — One preferred state

**Suggested Overlay Text (lower‑left):**  
“Penalty vanishes only at ρ*.  
Everywhere else it restores the field.”

**Optional Formula (bottom‑right):**  
P(ρ*) = 0

**Placement Notes:**  
• Place text near the red ball at the minimum.  
• Formula near the bottom of the well.

---

## P4_mobility_capacity_bound.png
**Suggested Title (top‑center):**  
Demand 4 — Mobility shuts off at capacity

**Suggested Overlay Text (lower‑left):**  
“M(ρ) → 0 as ρ → ρ_max.  
Crowding kills motion.”

**Optional Formula (bottom‑right):**  
M(ρ_max) = 0

**Placement Notes:**  
• Place text near the jammed red region.  
• Formula near the mobility curve.

---

## P5_participation_feedback.png
**Suggested Title (top‑center):**  
Demand 5 — Participation responds and remembers

**Suggested Overlay Text (lower‑left):**  
“ν integrates the driver and damps over time.  
A system with memory.”

**Optional Formula (bottom‑right):**  
τν̇ + ζν = F̂(ρ)

**Placement Notes:**  
• Place text near the feedback loop.  
• Formula near the time‑trace.

---

## P6_damping_discriminant.png
**Suggested Title (top‑center):**  
Demand 6 — A sharp threshold divides regimes

**Suggested Overlay Text (lower‑left):**  
“Δ < 0.5 → oscillation.  
Δ > 0.5 → monotone decay.”

**Optional Formula (bottom‑right):**  
Δ_crit = 0.5

**Placement Notes:**  
• Place text between the two rigs.  
• Formula near the golden ridge.

---

## P7_nonlinear_triad.png
**Suggested Title (top‑center):**  
Demand 7 — Three modes make a fourth

**Suggested Overlay Text (lower‑left):**  
“Nonlinear mixing: k₃ = k₁ + k₂.  
A spectral fingerprint.”

**Optional Formula (bottom‑right):**  
k₃ = k₁ + k₂

**Placement Notes:**  
• Place text near the mixer node.  
• Formula near the vector triangle.

---

## D19_uniqueness.png
**Suggested Title (top‑center):**  
The uniqueness theorem — eleven demands, one equation

**Suggested Overlay Text (lower‑left):**  
“All alternatives fail one of the constraints.  
Only one PDE survives.”

**Optional Formula:**  
None (conceptual)

**Placement Notes:**  
• Place text near the converging beams.  
• Keep the “forbidden” orbs unobscured.

---

## UnifiedPDE.png
**Suggested Title (top‑center):**  
One scalar field + one participation ODE

**Suggested Overlay Text (lower‑left):**  
“ρ‑engine + ν‑oscillator.  
Coupled bidirectionally.”

**Optional Formula (bottom‑right):**  
∂ₜρ = D·F[ρ] + Hν  
τν̇ = F̂(ρ) − ζν

**Placement Notes:**  
• Place text between the two machines.  
• Formula near the coupling shaft.

---

# ACT II — THREE CHANNELS + THREE TEXTBOOK ANALOGUES

## Mobility_alone.png
**Suggested Title (top‑center):**  
Channel 1 — pure spatial spreading

**Suggested Overlay Text (lower‑left):**  
“Mass conserved.  
Extent grows.  
Diffusion‑like.”

**Optional Formula (bottom‑right):**  
∂ₜρ = D∇·(M∇ρ)

**Placement Notes:**  
• Place text near the expanding rings.  
• Formula near the 1D profiles.

---

## PME_porous_medium.png
**Suggested Title (top‑center):**  
Mobility’s fingerprint — the porous medium equation

**Suggested Overlay Text (lower‑left):**  
“Nonlinear diffusion.  
Flat top, sharp edge, slowing front.”

**Optional Formula (bottom‑right):**  
∂ₜδ = Dₚₘₑ ∇²(δᵐ)

**Placement Notes:**  
• Place text near the plateau region.  
• Formula near the time‑stacked profiles.

---

## Penalty_alone.png
**Suggested Title (top‑center):**  
Channel 2 — pure relaxation

**Suggested Overlay Text (lower‑left):**  
“Uniform field.  
Single timescale.  
Monotone decay.”

**Optional Formula (bottom‑right):**  
∂ₜρ = −D P(ρ − ρ*)

**Placement Notes:**  
• Place text near the uniform tiles.  
• Formula near the exponential curve.

---

## RC_debye.png
**Suggested Title (top‑center):**  
Penalty’s fingerprint — Debye / RC relaxation

**Suggested Overlay Text (lower‑left):**  
“Classic exponential decay.  
One time constant.”

**Optional Formula (bottom‑right):**  
ρ(t) = ρ* + (ρ₀ − ρ*) e^(−t/τ_RC)

**Placement Notes:**  
• Place text near the RC schematic.  
• Formula near the decay curve.

---

## Participation_alone.png
**Suggested Title (top‑center):**  
Channel 3 — pure temporal response

**Suggested Overlay Text (lower‑left):**  
“Driven, damped oscillator.  
Overshoot and ring.”

**Optional Formula (bottom‑right):**  
τν̇ + ζν = F̂(ρ)

**Placement Notes:**  
• Place text near the ν‑trace.  
• Formula near the driver pulse.

---

## RLC_oscillator.png
**Suggested Title (top‑center):**  
Participation’s fingerprint — the RLC oscillator

**Suggested Overlay Text (lower‑left):**  
“Damped sinusoid.  
Envelope decay.”

**Optional Formula (bottom‑right):**  
τv̈ + ζv̇ + v = 0

**Placement Notes:**  
• Place text near the oscilloscope trace.  
• Formula near the circuit loop.

---

# ACT III — THREE EMPIRICAL MODULES

## UDM_universal.png
**Suggested Title (top‑center):**  
Mobility confirmed — one universal curve

**Suggested Overlay Text (lower‑left):**  
“D = D₀(1 − c/c_max)^β.  
11 materials, one law.”

**Optional Formula (bottom‑right):**  
D(c) = D₀(1 − c/c_max)^β

**Placement Notes:**  
• Place text near the master curve.  
• Formula near the scatter.

---

## CMLag_merger.png
**Suggested Title (top‑center):**  
Penalty confirmed — cluster merger lag

**Suggested Overlay Text (lower‑left):**  
“Lag length ℓ = D_T / v_current.  
Observed in 7 clusters.”

**Optional Formula (bottom‑right):**  
ℓ = D_T / v_current

**Placement Notes:**  
• Place text near the wake offset.  
• Formula near the cluster cores.

---

## FRAP_BSA.png
**Suggested Title (top‑center):**  
Participation channel — the pending test

**Suggested Overlay Text (lower‑left):**  
“ED predicts damped oscillatory recovery.  
Standard diffusion predicts monotone.”

**Optional Formula (bottom‑right):**  
τρ̈ + ζρ̇ + ρ = 0

**Placement Notes:**  
• Place text near the bleached spot.  
• Formula near the predicted curve.

---

# ACT IV — SIX INVARIANTS

## DimInv.png
**Suggested Title (top‑center):**  
A dimensionless ratio equal to 0.3

**Suggested Overlay Text (lower‑left):**  
“Same value across 61 orders of magnitude.”

**Optional Formula (bottom‑right):**  
D·T₀ / L₀² = 0.3

**Placement Notes:**  
• Place text near the golden core.  
• Formula near the surrounding scenes.

---

## SharpBif.png
**Suggested Title (top‑center):**  
A universal threshold at Δ = 0.5

**Suggested Overlay Text (lower‑left):**  
“Left: oscillatory.  
Right: monotone.  
Critical ridge at 0.5.”

**Optional Formula (bottom‑right):**  
Δ_crit = 0.5

**Placement Notes:**  
• Place text between the two phase portraits.  
• Formula near the ridge.

---

## UniversalInv.png
**Suggested Title (top‑center):**  
Different beginnings, same ending

**Suggested Overlay Text (lower‑left):**  
“All trajectories converge to E_ground.  
Same τ_rel for all.”

**Optional Formula (bottom‑right):**  
E_ground = qYρ₀  
τ_rel = ρ₀/(qY)

**Placement Notes:**  
• Place text near the attractor.  
• Formula near the decay curves.

---

## TriadCoupling.png
**Suggested Title (top‑center):**  
A spectral fingerprint of P7

**Suggested Overlay Text (lower‑left):**  
“Small peak at k₁ + k₂.  
Coupling ≈ 3–6%.”

**Optional Formula (bottom‑right):**  
k₃ = k₁ + k₂

**Placement Notes:**  
• Place text near the amber peak.  
• Formula near the vector arrows.

---

## dConsistency.png
**Suggested Title (top‑center):**  
Same scaling rule in 1D, 2D, 3D

**Suggested Overlay Text (lower‑left):**  
“α_R = 1 / [d(m−1) + 2].  
Verified in all dimensions.”

**Optional Formula (bottom‑right):**  
α_R = 1 / [d(m−1) + 2]

**Placement Notes:**  
• Place text near the three panels.  
• Formula near the golden tag.

---

## EDSC2.png
**Suggested Title (top‑center):**  
The deepest invariant — r* ≈ −1.304

**Suggested Overlay Text (lower‑left):**  
“Same curvature signature  
from nanoscale to megaparsec.”

**Optional Formula (bottom‑right):**  
r* = median R_mott(∇²E)

**Placement Notes:**  
• Place text near the violet median line.  
• Formula near the violins.

---

# CODA

## ScenarioD.png
**Suggested Title (top‑center):**  
Random seeds → emergent architecture

**Suggested Overlay Text (lower‑left):**  
“Noise evolves into structure.  
Saddles appear with correct curvature.”

**Optional Formula:**  
None

**Placement Notes:**  
• Place text near the forming clusters.  
• Keep saddle markers unobscured.

---

# CLOSER

## Grid_3x3_story.png
**Suggested Title (top‑center):**  
The whole story in one grid

**Suggested Overlay Text (lower‑left):**  
“Three channels × three levels.  
Abstract → textbook → empirical.”

**Optional Formula:**  
None

**Placement Notes:**  
• Place text unobtrusively in a corner.  
• Let the grid speak for itself.



---


