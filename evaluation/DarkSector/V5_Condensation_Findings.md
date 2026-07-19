# V5-Coherence Condensation Probe — Findings

**Script:** `v5_condensation_probe.py`. **Date:** 2026-07-19.
**Question:** does a gas of committed relics coupled by the **real** V5 coherence functional phase-lock (condense) in calm environments and decohere in hot ones — and is it mass-independent? (The decisive test of the dark-sector superfluid-relic program; see `ED Generative/physics-papers/dark-sector/DarkSector_SuperfluidRelic_Program.md`.)

## Setup (faithful to the real V5 coupling)

Real V5 functional (from `ChiralGauge/homochirality_v5_verify.py`, Paper_090):
`E = Σ_{i<j} exp(−r_ij/ℓ)·cos(φ_i − φ_j)` — reach-weighted phase alignment. **No mass term.**
Overdamped Langevin (Kuramoto with the V5 reach kernel): `dφ_i = K Σ_j w(r_ij) sin(φ_j−φ_i) dt + √(2D dt)·η`, with `D` = decoherence (environment: low = calm/galaxy, high = hot/cluster). Order parameter `C = Σ w cos(Δφ) / Σ w` (1 = condensed, 0 = dispersed).

## Results

Coherence `C` vs decoherence `D`, for relic counts `N` (fixed box → `N` = density proxy):

| D → | 0.02 | 0.05 | 0.10 | 0.20 | 0.35 | 0.50 | 0.75 | 1.00 | 1.50 | 2.50 |
|---|---|---|---|---|---|---|---|---|---|---|
| N=20 | 1.00 | 0.99 | 0.98 | 0.96 | 0.92 | 0.88 | 0.82 | 0.74 | 0.56 | 0.18 |
| N=40 | 1.00 | 0.99 | 0.99 | 0.97 | 0.95 | 0.93 | 0.90 | 0.86 | 0.78 | 0.56 |
| N=80 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 | 0.97 | 0.95 | 0.93 | 0.89 | 0.82 |

## Read

1. **Condensation happens.** Calm (D=0.02): C=1.00, fully condensed. The relic gas phase-locks under the real V5 functional. The core mechanism works.
2. **Mass-independent — the make-or-break, PASSED.** The V5 functional contains only positions and phases; there is **no mass term**, so condensation cannot depend on the relic mass (contrast: BEC needs a light boson). A heavy, abundance-friendly relic can still condense. **This dissolves the mass tension** that squeezed the whole program — structural, confirmed by the functional's form.
3. **The boundary is NOT `a₀` — it's the decoherence source (correction).** Low noise → condense, high noise → disperse. If the decohering agent were *acceleration* (→ `a₀`), clusters (also sub-`a₀`) would wrongly condense too. The version that gives the needed galaxy=MOND / cluster=CDM split needs the decoherence to be **thermal (velocity dispersion)** — galaxies cold → condense, clusters hot → disperse. So the earlier "`a₀` = the coherence boundary" claim is retracted; the boundary is set by *what physically decoheres the relic phases*, and identifying that (acceleration vs. temperature) is the new sharp open question.
4. **Density-dependence (new caveat).** The condensation threshold rises with density (N=20 breaks by D≈1.7; N=80 holds coherence even at D=2.5). Denser clumps resist decoherence. Clusters are dense, so "clusters must disperse to CDM" is a live quantitative competition (heat vs. density), not automatic — needs the real ED numbers (V5 reach & strength, cluster density & dispersion).

## Tier and scope

**Measured (structural, faithful functional):** condensation transition on the real V5 coupling; the mass-independence (analytic from the functional's form, confirmed). **Not established:** the quantitative boundary (the `D`↔physics map — acceleration vs. temperature); that clusters actually land on the dispersed side; that the condensed collective mode reproduces the khronon/MOND with the correct `a₀`. This is a Kuramoto-with-the-real-V5-kernel realization — faithful to V5's *structure*, not the full certified Σ-rule substrate with real accelerations.

## Net

The decisive test **passed on the one question that mattered** — condensation is real and mass-independent, so the mass tension that threatened the whole superfluid-relic program is dissolved. It **corrected two overclaims** — the boundary is not `a₀` but the (thermal) decoherence source, and the galaxy/cluster split is a quantitative competition, not automatic. The program survives, sharper: the next open questions are *what decoheres the relic phases* (must be thermal for the split to work) and *whether clusters disperse* against their own density.
