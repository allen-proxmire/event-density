# BTFR.03 — ED Viability Against the Two-Condition Theorem

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, third memo
**Status:** Structural verdict: **ED in its current form cannot derive BTFR.** The screened-Poisson PDE with isotropic D_T fails C1 (no logarithmic far-field). The activity-source functional fails C2 (M_eff scales as M_b, not √M_b). Both failures are structural and independent. Two routes to extend ED to a BTFR-compatible form are identified; both require modifications to the PDE or source construction, not to numerical parameters.
**Predecessor:** BTFR.02 (two-condition theorem and viability checklist).
**Successor:** TBD — either an anisotropic-PDE extension (BTFR.04a) or a sublinear-source extension (BTFR.04b).

---

## 1. ED in canonical form

The penalty-channel PDE with activity sourcing (DM.1, Reading B):

> D_T ∇²T − λT = −S(R, z),    S(R, z) = κ_act · A(R, z),

with A(R, z) = α · |∇v_baryon|² + (1 − α) · ω², kinematic activity index built from baryonic shear and vorticity. The kinematic prediction is

> v_T²(R) = −R · γ · ∂_R T(R, z = 0),    γ = D_T / κ_act.

The operator L = D_T ∇² − λ is **3D-isotropic** (single scalar D_T) and **linear**. The Green's function for a localized source is the standard 3D Yukawa form:

> G_3D(r) = (1 / 4π D_T) · e^{−r/L} / r,    L = √(D_T / λ).

L is set by cluster-scale calibration to L ≈ 980 kpc — far larger than any galactic radius. Within the SPARC range (R ≲ 50 kpc, R/L ≲ 0.05), the exponential factor is essentially unity, so

> G_3D(r) ≈ (1 / 4π D_T) · 1/r    (in-galaxy regime).

ED behaves as **un-screened 3D Newtonian Poisson** at galactic scales.

---

## 2. Check C1 — logarithmic far-field?

**Asymptotic kernel form.** g(R) ~ 1/R for R ≪ L.

> R · g′(R) = R · (−1/R²) = −1/R → 0   (R → ∞).

This **fails the flat-curve condition** R · g′(R) → constant ≠ 0. The asymptotic v_T² produced by integrating an activity source against a 1/R kernel goes as R^{−1} (or faster, depending on source extent), not as a constant.

The Yukawa screening at R ~ L would in principle shut off the curve before it could become logarithmic. But within the in-galaxy window the kernel is essentially 1/R, so the question is moot: ED's in-galaxy Green's function is just 3D-Newtonian, and 3D-Newtonian curves fall.

**Effective dimensionality.** The PDE is genuinely 3D-isotropic. The cylindrical-coordinate form

> D_T · [(1/R) ∂_R(R ∂_R T) + ∂_z² T] − λT = −S

uses the same D_T multiplier on the in-plane and perpendicular derivative terms. There is no anisotropy. The disc geometry of the source S(R, z) (a sech² vertical profile localized within h_disc ≈ 0.3 kpc) does not change the *operator's* dimensionality: it only restricts where the source lives. For a thin source emitting into a 3D-isotropic medium, the field at large in-plane R is dominated by the 3D 1/r kernel, not a 2D log kernel.

**Verdict on C1: FAIL.** ED has no logarithmic far-field. Curves produced by activity sources fall as R^{−1/2} or faster. By Corollary 1 of BTFR.02, no choice of source functional within ED's current PDE can produce flat curves at large R. The DM.1 §3.1 derivation that suggested a flat outer regime relied on a mid-radius cancellation, not on a true asymptotic flatness; outside that mid-radius window the curve falls.

This is the structural reason the production run produced χ²_red median ≈ 60 with bad shape on most galaxies: the model's best-effort rotation curves are intrinsically wrong-shaped at large R, and no per-galaxy κ_act fix can repair an operator-level deficit.

---

## 3. Check C2 — amplitude ∝ M_b^{1/2}?

Even if C1 held (it doesn't), C2 would have to be checked independently.

**Source functional integration.** The activity index for a baryonic disc with v_baryon(R):

> A(R) ≈ α · (dv_baryon/dR)² + (1 − α) · (v_baryon/R)².

For a Keplerian outer disc, v_baryon² ≈ G M_b / R, so

> (dv_baryon/dR)² ∝ G M_b / R³,    (v_baryon/R)² ∝ G M_b / R³.

Both shear² and vorticity² scale **linearly in M_b** at fixed R. The disc-integrated effective charge is

> M_eff = ∫ S dV = κ_act · ∫ A(R, z) · 2π R dR dz ∝ κ_act · M_b · ∫(R-dependent factors)

with no √M_b structure. **M_eff is linear in M_b.**

Plug into the (counterfactual) flat-curve formula from BTFR.02 §4:

> v_flat² ∝ M_eff ∝ M_b   ⟹   v_flat⁴ ∝ M_b².

ED's source functional, even paired with a hypothetical log kernel, would predict **slope 2** for the BTFR (v_flat⁴ ∝ M_b²), not slope 4 (v_flat⁴ ∝ M_b). The numerical run reported slope 0.24, dominated by the kernel failure (C1) rather than the source-scaling failure (C2); but the source-scaling failure is independently structural.

**Embedded acceleration scale.** ED's fundamental constants in the PDE are D_T (kpc²/Gyr), λ (1/Gyr), κ_act (dimensionally a per-time-squared coefficient on activity). Combinations:

- D_T · λ has dimensions (kpc/Gyr)² — a velocity squared, ≈ (200 km/s)². Not an acceleration.
- D_T / λ has dimensions kpc² — a length squared (the screening length squared). Not an acceleration.
- κ_act has units that depend on what units A is expressed in; in galactic-natural units it is dimensionless.
- λ² · D_T has dimensions kpc² / Gyr³ — a velocity per time, i.e. acceleration. Numerically ≈ 6.97e4 / (13.8)³ ≈ 27 (kpc / Gyr²) ≈ 1e−10 m/s². This is suggestively close to MOND's a₀ ≈ 1.2e−10 m/s², but the appearance of an acceleration combination is incidental to ED's structure: ED does **not** use this combination as a scale anywhere in its source construction or PDE coupling.

The presence of a dimensional combination with units of acceleration is necessary but not sufficient for Route A. Route A requires the theory to *use* such a scale to weight the source coupling sublinearly. ED's coupling κ_act is a single multiplicative constant on a kinematic activity functional; it carries no a₀-weighting.

**Verdict on C2: FAIL.** ED's source functional is linear in M_b (after disc integration), and ED does not invoke an embedded acceleration scale to weight the coupling sublinearly. Neither Route A nor Route B is in place. Even with a hypothetical log kernel, ED would predict slope 2, not 4.

---

## 4. Check C3 — R-independence?

In ED's current form the asymptotic v_T at any given R depends on:

- Disc scale length R_d (sets where the activity index peaks).
- Surface brightness (enters κ_act-weighted activity through v_disk(R)).
- Inclination-corrected v_baryon(R) (enters shear and vorticity directly).
- Distance-dependent M_baryon (enters as overall normalization of the source).

The activity index A(R) for two galaxies of identical M_b but different R_d gives different shear and vorticity profiles, and hence different T(R) and v_T(R). The asymptotic v_T (such as it is, before falling off due to the kernel failure) is **size-dependent**.

**Verdict on C3: FAIL.** ED's prediction depends explicitly on R_d and surface brightness. Even the universality result from the production run (σ(κ_act)/mean ≈ 2.1%) does not save this: that universality is a statement about the optimally-fit κ_act, not about the predicted v_flat for fixed M_b. Two galaxies with the same M_b and different R_d will give different fitted v_flat in ED's framework.

The empirical 0.1 dex BTFR scatter cannot be reproduced by a theory whose asymptotic prediction varies with R_d at the level the SPARC sample does (R_d ranging from ~0.5 to ~10 kpc within fixed M_b bins).

---

## 5. Check C4 — proportionality constant from theory parameters?

Moot, given C1, C2, C3 all fail. The theory does not produce v_flat⁴ ∝ M_b in any limit; asking whether the proportionality constant matches 47 M_⊙^{−1} (km/s)⁴ has no answer to evaluate.

The numerical fit's BTFR slope of 0.24 with scatter 3.7 dex is consistent with this: ED is producing some power-law-like residual structure between v_T and M_b across galaxies, but it is not BTFR.

**Verdict on C4: not evaluable; structurally pre-empted by failures of C1–C3.**

---

## 6. Aggregate verdict

| Condition | Pass / Fail | Structural cause |
|---|---|---|
| C1 (log far-field) | **Fail** | Isotropic 3D screened-Poisson; in-galaxy regime is 3D Newtonian; no log tail. |
| C2 (amplitude ∝ M_b^{1/2}) | **Fail** | Activity source functional integrates to M_eff ∝ M_b; no embedded a₀ weighting; would predict slope 2 with a log kernel. |
| C3 (R-independence) | **Fail** | v_T(R) depends explicitly on R_d, surface brightness, v_baryon profile shape. |
| C4 (constant from theory) | not evaluable | Pre-empted. |

**ED in its current canonical form cannot derive BTFR.** The failure is not numerical, not parameter-dependent, and not curable by re-running with different κ_act or α. It is structural at two independent levels (kernel and source) and a third level (disc-parameter dependence).

This is a refutation of the *current canonical ED* against BTFR. It is **not** a refutation of ED as a research framework. It identifies which structural elements would have to change to bring ED into the BTFR-derivable class.

---

## 7. Routes to a BTFR-compatible ED extension

Two routes are structurally available, corresponding to repairs of C1 and C2 respectively. Both require modification of the PDE or source construction; neither is a numerical recalibration.

### 7.1 Route I — Anisotropic diffusion (repair of C1)

Replace the scalar D_T with an anisotropic tensor:

> D_R · (1/R) ∂_R(R ∂_R T) + D_z · ∂_z² T − λT = −S,

with D_z ≪ D_R. The in-plane screening length L_R = √(D_R / λ) and perpendicular L_z = √(D_z / λ) are now distinct. In the regime L_z ≪ R ≪ L_R, the operator behaves locally as a 2D Laplacian with a logarithmic in-plane Green's function. C1 is satisfied **over a finite radial window** set by L_z and L_R.

This is what the user's intuition (galaxies are 2D discs; diffusion isn't equal in all directions) is pointing at. Structurally it is the cleanest single-modification route to repair C1.

It does **not** repair C2. With anisotropic diffusion + activity source, the predicted scaling is v_flat⁴ ∝ M_b², not BTFR.

### 7.2 Route II — Sublinear source functional or embedded a₀ (repair of C2)

Two sub-options:

- **Route II-A.** Introduce a fundamental acceleration scale a₀ into ED's constants (or derive one from D_T, λ, κ_act in a way that the source coupling is required to use). Modify the source coupling to σ_eff = σ / √(1 + a/a₀) or similar form, so that in the deep regime the effective coupling carries a √M_b^{−1} weight. Equivalent in deep-regime structure to MOND.

- **Route II-B.** Replace the activity index A(R, z) with a functional whose disc integral scales as √M_b. Candidate forms involve square roots of kinematic quantities or Mach-number-like ratios. Less canonical than II-A; more degrees of freedom; structurally less constrained.

Either sub-option of Route II repairs C2. Neither repairs C1 unless combined with Route I.

### 7.3 Combined Route I + II — minimal BTFR-compatible ED

To pass C1 and C2 simultaneously, ED must adopt **both** anisotropic diffusion **and** either an embedded a₀ or a sublinear source. This is the minimal modification set that brings ED into the linear-PDE BTFR-derivable class identified by BTFR.02.

A combined Route I + II-A is structurally closest to MOND (it adopts MOND's embedded a₀ and would inherit MOND's BTFR derivation in the deep regime) while preserving ED's PDE form (just with anisotropic D and an a₀-weighted κ_act).

A combined Route I + II-B preserves more of ED's distinctive source-construction philosophy but is harder to constrain.

### 7.4 What is *not* a route

- **Re-running with different κ_act, α, or D_T.** None of these change the operator's dimensionality or the source-functional's M_b scaling. The BTFR failure is structural; no choice of parameter values cures it.
- **Increasing optimizer evaluations.** The fitting limitations identified in the production run (max_evals = 50) explain a portion of the χ² behavior but not the structural BTFR-incompatibility identified here.
- **Switching from activity-source back to mass-source (V1 reversion) without anisotropic diffusion.** V1 was rejected in DM.0 partly on BTFR grounds; reverting without addressing C1 reproduces DM.0's failure modes.

The user's instinct in DM2-followup §C ("anisotropic diffusion + V1 mass source") is structurally a Route-I + (different-source-functional) combination. If V1 with anisotropic diffusion happens to produce a √M_b-yielding M_eff after disc integration, it is a candidate for the BTFR-compatible class. This is worth checking analytically before any numerical work, but the prior expectation should be that V1 mass-source still gives M_eff ∝ M_b (linear), so V1 + Route I would predict slope 2, not 4.

---

## 8. Final structural verdict

**ED in its canonical screened-Poisson + activity-source form cannot derive BTFR.** Both C1 and C2 fail independently, and C3 fails as a corollary of the disc-parameter dependence of the source. The numerical FAIL verdict from the DM2 production run is the empirical signature of these structural deficits.

The arc is not closed. **ED requires extension to derive BTFR.** The minimal extension set is:

> **(I) anisotropic diffusion (D_z ≪ D_R) to obtain a logarithmic in-plane far-field, plus**
> **(II) either an embedded acceleration scale weighting the source coupling, or a sublinear source functional, to obtain M_eff ∝ √M_b.**

Either anisotropy alone or sublinear coupling alone is insufficient; both are required.

A future BTFR.04 memo should pursue one of:

- **BTFR.04a** — derive the anisotropic-diffusion Green's function explicitly and confirm the windowed-log regime; check whether any natural ED source functional yields √M_b under disc integration; if not, introduce II-A or II-B as the minimal coupling modification.
- **BTFR.04b** — investigate whether ED's existing constants (D_T, λ, κ_act) admit a derived acceleration scale that the theory could be required to use, without adding new parameters; this would be the most parsimonious Route II realization.

Status: complete.
