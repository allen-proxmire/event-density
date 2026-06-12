# B4 Step 4 — Orientation-Relaxation: Results (ONTOLOGY FORK)

**Arc:** B4 — topological-charge hypothesis. **This doc:** a deliberate **fork off canonical ED** — relax the Σ orientation-blindness invariant and ask whether a winding defect then develops a stable, substrate-determined local field. **This is not a measurement of ED-as-built.**
**Code:** `B4_Arc/relaxation_test.py` (numpy; 61×61 lattice, winding-1 defect). **Date:** June 2026.
**Discipline:** no field equation installed; no retrofit to Coulomb. We let the modified rule run and read off what emerges. Winding is imposed only as a boundary condition ("a winding-w defect exists inside"); the interior is filled by the dynamics.

---

## The two nested modifications

To find *which* invariant actually blocks a determined field, we test orientation-relaxation with and without a second change:

- **Mod-A** — *Σ sees coherence, commitment still IRREVERSIBLE (P11 kept).* Each node is committed **once** as the coherence-optimal phase (circular mean) of its already-committed neighbours, then frozen. This is the prompt's minimal relaxation: only orientation-blindness is touched.
- **Mod-B** — *Σ sees coherence AND commitment is REVERSIBLE (P11 also broken).* Nodes re-adjust toward neighbour-coherence iteratively (Jacobi circular-mean). This is standard harmonic/XY relaxation — it abandons P11.

## Results (`relaxation_test.py`, verbatim)

**Mod-A — orientation-blindness relaxed, P11 kept:**

| r | deficit | ang. std | deficit·r² |
|---|---|---|---|
| 3 | 0.00011 | 0.00000 | 0.0010 |
| 6 | 0.00011 | 0.00001 | 0.0041 |
| 12 | 0.00015 | 0.00003 | 0.0211 |
| 24 | 0.00021 | 0.00006 | 0.1199 |

**sweep-dependence (two commit orders): 0.76** → the committed field is **not substrate-determined**. The bulk is locally smoothed (tiny deficit), but the winding's unavoidable 2π mismatch is dumped onto a **commit-order-dependent seam**; two sweeps give nearly-orthogonal fields. Irreversibility forbids annealing the seam away.

**Mod-B — P11 also broken (reversible relaxation):**

| r | deficit | ang. std | deficit·r² |
|---|---|---|---|
| 3 | 0.01961 | 0.01641 | 0.1765 |
| 6 | 0.00391 | 0.00120 | 0.1407 |
| 12 | 0.00089 | 0.00012 | 0.1288 |
| 24 | 0.00022 | 0.00001 | 0.1265 |

**init-dependence: 0.0005** → INIT-INDEPENDENT (determined); **anisotropy 0.13** → isotropic; **deficit·r² ≈ 0.126** constant (the discrete-vortex 1/r² law, coefficient w²/8). A **determined, isotropic, radial 1/r² field** emerges.

*(Honesty note recorded in code: plain Jacobi from a **random** init does **not** reach this — XY metastability freezes vortex–antivortex tangles. The determined field is the *stable fixed point* reached from a winding-consistent init, independent of the noise. "Determined" means the ground-state field is stable and init-independent, not that any init trivially converges.)*

## The decisive finding — two invariants block the field, not one

| Modification | orientation-blind? | P11 irreversible? | Determined local field? |
|---|---|---|---|
| canonical ED (Step 3) | **yes** | **yes** | no — integral Gauss law only |
| **Mod-A** | no | **yes** | **no** — sweep-dependent (0.76) |
| **Mod-B** | no | no | **yes** — isotropic 1/r², init-independent |

Relaxing orientation-blindness **alone is insufficient**: with P11 kept, the coherence-greedy commit cannot do the *iterative re-adjustment* a determined field requires, so the winding stress lands on a commit-order seam — a sweep-dependent artifact, not a field. A determined local field appears **only when P11 is also broken** — at which point the dynamics is harmonic/XY relaxation and **two of ED's defining primitives have been abandoned**.

## Interpretation — what this means for ED's ontology

A determined local (Coulomb-like) field is blocked in ED by **two independent load-bearing invariants**, not one: orientation-blind selection (Σ ignores phase) *and* irreversible commitment (P11). Removing only the first yields a sweep-dependent seam, not a field; removing the second as well recovers a determined 1/r² field — but that is the XY/lattice-field-theory dynamics, no longer ED. The deep point is a **complementarity**: ED's two signature commitments — orientation-blind selection and irreversible commitment — are *precisely* what make it a determinacy-generating substrate (the determinability-boundary results), and are *precisely* what foreclose smooth field dynamics. The **same architecture** that manufactures discrete determinate facts is what prevents a continuous determined field. Charge-as-topology lands exactly on this fault line: ED supplies the discrete/topological half *because* it is a discreteness engine, and withholds the continuous/metrical half *because* it is a discreteness engine. One property does both.

## Classification & recommendation

**Outcome:** Mod-A → **no sourcing** (sweep-dependent, orientation input insufficient). Mod-B → **stable sourced field**, but only by abandoning P11 (no longer ED).

**Recommendation: REJECT the modification (for canonical ED).** Relaxing orientation-blindness does not achieve sourcing (Mod-A fails), and the version that does (Mod-B) destroys irreversible commitment — it is a different theory. So a determined local field is **outside ED's ontology by construction**, blocked by two defining primitives at once. This **closes the B4 arc**: charge-as-topology is realized at the topological level and is **provably not extendable to the metrical level without ceasing to be ED** — a clean, mechanistic boundary, not a gap to be filled.

## Crank-safety payoff

This result is *why ED cannot be quietly retrofitted into electromagnetism.* The topological skeleton (quantization, conservation, protection, Gauss circulation) survives ED's primitives; the metrical flesh (determined local field, Coulomb) requires removing two of them. The line between "what ED gives" and "what needs new physics" is now **mechanistically explained by which invariants block which content** — the strongest possible form of the honest "ED is not a TOE" position for the charge case.

---

*End of B4 Step 4. Forked off canonical ED deliberately; found that a determined local field needs BOTH orientation-blindness and irreversibility removed; concluded the metrical field is outside ED by design. Arc closed.*
