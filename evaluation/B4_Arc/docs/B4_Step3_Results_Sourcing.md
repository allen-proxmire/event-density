# B4 Step 3 — Sourcing Test: Does the Winding Induce a Spatial Pattern?

**Arc:** B4 — topological-charge hypothesis. **This doc:** the sourcing question — embedded in a 2-D spatial substrate (P06), does the integer winding generate a stable, distance-dependent pattern, with Σ orientation-blind?
**Code:** `B4_Arc/sourcing_test.py` (numpy; 81×81 lattice, central winding-w defect). **Date:** June 2026.
**Discipline:** no hand-installed field equation. We embed *only* the winding (a connection with loop-holonomy 2πw) and read off what single-valued commitment (P11) forces — separating the integral content from the local content.

---

## Setup

An L×L lattice with P06 4-neighbour adjacency; the substrate phase is U(1)-valued everywhere (P09); a winding-w defect sits at the centre. The only phase→dynamics channel is bandwidth (P04 coherence `b_e = cos²(A_e/2)`); Σ never reads it. We ask two deliberately separated questions:

- **(1) Integral:** the circulation `(1/2π) Σ_loop wrap(A_e)` around an enclosing loop.
- **(2) Local:** the per-edge bandwidth-deficit pattern `1 − cos²(A_e/2)`.

## Results (`sourcing_test.py`, verbatim)

**(1) Integral — a topological Gauss law.** Circulation is **independent of loop size/shape** and equals the enclosed winding:

| loop half-size s | w=0 | w=1 | w=2 |
|---|---|---|---|
| 2 | 0.000 | 1.000 | 2.000 |
| 5 | 0.000 | 1.000 | 2.000 |
| 10 | 0.000 | 1.000 | 2.000 |
| 20 | 0.000 | 1.000 | 2.000 |
| 35 | 0.000 | 1.000 | 2.000 |

The winding is **unscreenable**: every enclosing loop, at any radius, sees exactly 2πw. This is the discrete/topological content of Gauss's law — enclosed "charge" = quantized circulation, loop-independent.

**(2a) Local — a 1/r² profile is *available*.** In the smooth (vortex) representative, the bandwidth deficit is radial:

| r | mean deficit | deficit·r² |
|---|---|---|
| 4 | 0.00781 | 0.1250 |
| 8 | 0.00196 | 0.1256 |
| 16 | 0.00049 | 0.1251 |
| 32 | 0.00012 | 0.1249 |

`deficit·r² ≈ 0.125` constant → a clean **1/r² radial field-like profile**.

**(2b) Local — but it is *not determined*.** The *same* winding in a different committed representative (a smooth sweep/gauge shift) keeps the circulation fixed (1.000 at s=20) while **relocating** the local deficit (near-core 0.139 → 0.148, pattern moved). The local field is a **choice of committed field**, not a substrate-fixed quantity.

## The decisive reading — integral content present, local content withheld

The winding **does** source something distance-spanning and unscreenable: the integral Gauss law (circulation = 2πw around any loop). But the **local field is undetermined**. The 1/r² vortex is the *minimum-stress* configuration and ED can **host** it — but ED does not **source** it, because selecting it requires a **coherence-relaxation dynamic** (drive Δφ toward smoothness, a discrete Poisson/Laplace relaxation), and **Σ is orientation-blind**: nothing in the ρ-dynamics ever pushes the phase toward coherence. The committed pattern is fixed by the (phase-blind) sweep, with no preference for the field-like configuration over a concentrated one. So: **integral Gauss law present; determined local field absent.**

## Outcome classification

**WEAK / TOPOLOGICAL sourcing.** Not inert (the enclosed circulation is real, quantized, unscreenable, distance-spanning), but not structured-determined either (the local profile is sweep/representative-dependent). ED supplies the **integral** half of Gauss's law and withholds the **local** half. Σ-invariant intact throughout.

## Interpretation — for B4 viability

Embedded in space, the winding produces a genuine, quantized, unscreenable circulation around every enclosing loop — the topological/integral content of a sourcing law — but **no determined local field**, because the metric content of a field (a determined 1/r profile) requires a coherence-relaxation dynamic that ED's orientation-blind Σ does not provide. ED can *host* a field-like (vortex) configuration but does not *source* one. This is the same boundary that capped Steps 1 and 2, now in spatial form: the substrate realizes the **topological skeleton** of a charge and withholds its **metrical flesh**.

## The unifying result across the whole arc

Orientation-blindness is the **single consistent boundary** across all three steps — ED gives the topological content of charge and withholds the metrical/dynamical content, for one reason throughout (Σ never lets phase-coherence drive the ρ-dynamics):

| Step | Question | ED supplies | ED withholds | Reason |
|---|---|---|---|---|
| 1 | quantize? | winding ∈ ℤ, conserved, protected | any dynamical effect (inert) | Σ phase-blind |
| 2 | couple? | discrete w-indexed bandwidth ladder | strong / Σ-level coupling | Σ phase-blind |
| 3 | source? | integral Gauss law (unscreenable 2πw) | a determined local field | no relaxation (Σ phase-blind) |

> **B4 verdict:** ED realizes the **entire topological skeleton** of electric charge — quantization, conservation, irreversibility-protection, and an integral (Gauss-law) circulation — and withholds the **metrical flesh** — determined coupling strength, a local field, Coulomb's law — and it does so by a *single* load-bearing invariant, orientation-blindness, consistently across all three tests. Charge-as-topology is **structurally real in ED at the topological level and absent at the metrical level**, by one clean reason.

## Recommendation: ARC COMPLETE — bank the three-step characterization

B4 has reached a complete, honest, crank-safe structural verdict in three bounded steps, each reached graph-first. The remaining frontier is **not a measurement step**: to obtain a determined local field (Coulomb), one must **relax orientation-blindness** — let phase-coherence feed back into the ρ-dynamics. That is a **load-bearing ontological modification** with corpus-wide consequences (the stratified-orientation result and the determinability-boundary measurement all rest on Σ being phase-blind), not a casual next experiment. So:

- **Defensible result (now):** charge-as-topology is realized in ED at the topological level (quantization + protection + integral Gauss law) and blocked at the metrical level (no local field) by orientation-blindness — a single, clean, falsifiable characterization.
- **The only way forward** is a deliberate ontology decision (modify orientation-blindness and trace the consequences), scoped as its own project — not pursued here.

---

*End of B4 active investigation. The arc delivered a real partial cash-out of the Facts-paper's boldest claim: ED carries the topological skeleton of charge, withholds its metrical flesh, and does so by one consistent invariant. Honest, bounded, crank-safe throughout.*
