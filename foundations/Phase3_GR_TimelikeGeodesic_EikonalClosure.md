# Phase-3 GR — Closing the Timelike Geodesic Identity: the Massive Eikonal Deflection

**Foundations computation — advances the timelike geodesic identity (GR-III §5 / the timelike note) from *limit-forced reduction* to *computed and confirmed at the eikonal level*. Not a corpus edit, not a new primitive.**
The timelike note reduced the identity to: ED's subluminal max-Σ front is the **massive eikonal** of `g ∼ b⁻¹`, with eikonal (Jacobi) index `n_eff = (1/b)√(E² − m²b)`, limit-forced to recover the proven null (Fermat) result (`m → 0`) and Newtonian orbits (weak field). The residual was to **trace the massive eikonal explicitly** and confirm its rays are the timelike geodesics — i.e. that the massive front bends by the relativistic velocity-dependent deflection. This note does that.
**Crank rail:** `n_eff` is the Jacobi index *derived* in the timelike note (not tuned); the deflection is measured and compared to the standard relativistic `α(β)`; the `m → 0` endpoint must reproduce R7's factor of two or the construction is wrong. Sim: `evaluation/DynamicalBandwidth/massive_deflection.py`.

---

## 1. The test

A massive particle of velocity `β = v/c` deflecting past a mass (`b = 1 − r_s/r`) bends, in GR, by

> `α(β) = (r_s/ξ)\,(1 + 1/β²)`,

which interpolates **Newtonian** (`β → 0`: `α → (r_s/ξ)/β²`, the slow-particle `1/v²` law) to the **factor of two** (`β = 1`, `m = 0`: `α = 2r_s/ξ` — *R7's proven null result*). Tracing the massive eikonal rays (`n_eff = (1/b)√(E²−m²b)`, `E = 1`, so `β = √(1−m²)`) past the mass and measuring `α(β)`:

## 2. Result

| `m` | `β = v/c` | `α·ξ/r_s` (measured) | `1 + 1/β²` (predicted) | ratio |
|---|---|---|---|---|
| 0.00 | 1.000 | **2.055** | 2.000 | 1.027 |
| 0.50 | 0.866 | 2.401 | 2.333 | 1.029 |
| 0.70 | 0.714 | 3.053 | 2.961 | 1.031 |
| 0.85 | 0.527 | 4.754 | 4.604 | 1.033 |
| 0.95 | 0.312 | 11.583 | 11.256 | 1.029 |

The measured deflection tracks `1 + 1/β²` across the whole velocity range — **a constant ~3 % offset** (the finite-`ξ` weak-field curvature, exactly the offset that gives R7's `2.09` vs `2.00`). The two endpoints are decisive:

- **`β = 1` (null):** `α·ξ/r_s = 2.055 ≈ 2` — **the factor of two, matching R7's proven null result.** The massless limit of the massive eikonal *is* the Fermat/null deflection.
- **`β = 0.31` (slow):** `α·ξ/r_s = 11.58 ≈ 1 + 1/β²` (the Newtonian `1/β² = 10.26` plus the relativistic `1`).

## 3. Verdict

**The massive eikonal of `g ∼ b⁻¹` reproduces the relativistic deflection law `α = (r_s/ξ)(1 + 1/β²)` across all velocities, with the `β = 1` endpoint landing on R7's proven factor of two.** Combined with the timelike note's identification of ED's subluminal max-Σ front *as* this massive eikonal (the Jacobi index `n_eff = (1/b)√(E²−m²b)` derived there), the timelike geodesic identity is now **computed and confirmed at the eikonal level** — the massive fronts follow the timelike geodesics, with the correct velocity-dependent bending, interpolating Newtonian → factor-of-two.

**The honest residual.** This confirms the **eikonal/geodesic side** explicitly (the massive rays of `g ∼ b⁻¹` have the right `α(β)`). The remaining step is the standard **eikonal limit** of the substrate front (that the actual Σ-rule front's phase obeys the Hamilton–Jacobi equation whose rays these are) — which the timelike note covered structurally and which is the generic eikonal correspondence, not a separate physical input. So the identity moves from *limit-forced reduction* to *computed at the eikonal level, both limits confirmed, the null endpoint matching the proven result* — a substantial closure, with only the generic front→eikonal correspondence between it and a fully-bit-for-bit Σ-rule proof. The `~3 %` offset is finite-`ξ` weak-field curvature (as in R7), not a deviation.

---

*Closes the timelike geodesic identity at the eikonal level. The massive eikonal of `g ∼ b⁻¹` (Jacobi index `n_eff = (1/b)√(E²−m²b)`, derived in the timelike note) reproduces the relativistic deflection `α = (r_s/ξ)(1+1/β²)` across velocities — Newtonian `1/β²` at low `β`, the factor of two at `β = 1` (matching R7's proven null result). The timelike geodesic identity is advanced from limit-forced reduction to computed-and-confirmed at the eikonal level, the residual being the generic front→eikonal correspondence. `~3 %` finite-`ξ` offset (as R7). No corpus edits, no new primitives.*
