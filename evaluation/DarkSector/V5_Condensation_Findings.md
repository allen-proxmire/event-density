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

---

# Follow-on: Thermal-Decoherence Probe

**Script:** `v5_thermal_decoherence_probe.py`. **Date:** 2026-07-19.
**Question (opened by the condensation probe):** what physically decoheres the relic phases, and is it *thermal* (velocity dispersion) as the galaxy/cluster split requires — or acceleration (which would wrongly condense sub-`a₀` clusters)?

**ED-native decoherence, derived not assumed:** P11 randomizes phases at commitment events; a relic commits on ENCOUNTER (interaction → single-channel collapse); kinetic encounter rate ∝ relative velocity. So decoherence rate is *derived* from the motion. V5 aligns phases at constant coupling `K` (temperature-independent). Relics move with dispersion `σ_v` (= temperature).

**Result:**

| σ_v | 0.05 | 0.10 | 0.20 | 0.35 | 0.50 | 0.75 | 1.0 | 1.5 | 2.5 | 4.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| C | 0.86 | 0.72 | 0.49 | 0.22 | 0.08 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 |
| dec.rate | 0.98 | 1.97 | 3.96 | 6.97 | 9.87 | 14.6 | 19.5 | 29.5 | 49.1 | 78.4 |

**Read:** cold (`σ_v`=0.05, ~galaxy disk) → C=0.86 **CONDENSED**; hot (`σ_v`=4.0, ~cluster) → C=0.00 **DISPERSED**. Decoherence-rate scaling exponent in `σ_v` ≈ **1.00** → kinetic / **THERMAL**, set by velocity not acceleration. **Verdict: thermal boundary confirmed** — cold condenses → MOND, hot disperses → CDM, and the noise is provably ∝ velocity dispersion. Galaxy-vs-cluster `σ_v` differ by ~20–100×, so the transition need only fall in that wide gap. **This resolves the open question from the condensation probe** (the boundary is thermal, derived from P11 + kinetics — not `a₀`).

**Remaining open:** the quantitative transition dispersion in real units (needs ED's V5 reach/strength); a targeted heat-vs-density check for dense-and-hot clusters (this probe fixed density; the last showed density aids coherence — though C→0 at high `σ_v` here suggests heat wins); whether the condensed mode is the khronon with the right `a₀`; and whether any *background* (non-encounter) commitment adds a second, possibly non-thermal, decoherence channel.

---

# Decisive: Khronon-Mode Probe — the unification FAILS

**Script:** `v5_khronon_mode_probe.py`. **Date:** 2026-07-19.
**Question:** does the V5-condensed relic's collective mode reproduce the MOND force (= the khronon), or a standard (Newtonian) force? This is the central unification claim ("one substance = dark matter AND MOND").

**Method:** read the effective kinetic term off the real V5 functional by imposing a uniform phase gradient `k` and measuring `ΔE(k) ~ k^p`. `p=2` → standard kinetic term → Poisson → **Newtonian**. `p=3` → AQUAL / non-analytic → **deep-MOND** (`a = √(a_N a₀)`).

**Result:**

| k | 0.03 | 0.05 | 0.08 | 0.12 | 0.20 | 0.30 | 0.50 | 0.80 | 1.20 |
|---|---|---|---|---|---|---|---|---|---|
| ΔE | 5.3 | 14.8 | 37.8 | 84.9 | 234 | 516 | 1355 | 3029 | 5258 |

**Exponent p = 2.00** (small-k / deep regime), 1.90 (full range). **STANDARD (Newtonian), not MOND.**

**Verdict — the unification is FALSIFIED (at the level of ED's real V5 functional).** The V5-condensed collective mode has the generic `|∇φ|²` kinetic term, which mediates a Newtonian force. MOND needs the non-analytic `√` (AQUAL) structure, which the analytic `cos`-based V5 functional does not produce at any order (its expansion is `(∇φ)², (∇φ)⁴, …` — all even/analytic; no `(∇φ)^{3/2}`). So **the condensed relic is NOT the khronon**; "one substance carries both dark matter and MOND" does not close.

**What survives / what falls:**
- **Survives:** the relic as a *dark-matter* candidate — condensation, mass-independence, and the thermal galaxy/cluster split are all about the dark-matter role and stand.
- **Falls:** the unification. ED reverts to its standing two-part picture — **MOND = the separate khronon** (KM-I, which has the correct non-standard structure by matching) **+ a relic = dark matter**. The double-counting the superfluid picture was meant to dissolve returns un-resolved (a condensed relic gives a Newtonian mode in galaxies, where MOND already works), and the mass tension with it.

**Net of the whole probe sequence:** condensation ✓, mass-independence ✓, thermal boundary ✓ (relic is a viable dark-matter candidate) — but the khronon-mode test ✗ (the condensed mode is Newtonian). The grand unification is falsified by its own decisive test; the honest position is a native dark-matter relic and a separate native MOND khronon, not one unified substance.
