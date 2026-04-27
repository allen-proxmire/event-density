# BTFR.06 — Implementation of the BTFR-Compatible ED Extension

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, sixth memo (implementation)
**Status:** Anisotropic-screened-Poisson Green's function derived. Windowed-log regime identified. **Honest finding: the log window only spans galactic scales under stronger anisotropy than BTFR.05 anticipated** (D_z/D_R ≲ 10⁻⁶, not 10⁻²). The embedded a₀-weighting required for Route II-A is identified but is shown to be a genuine *additional* structural modification, not a consequence of dimensional analysis alone. Slope-4 BTFR derivation requires either an explicit a₀-weighted source coupling or a sublinear source functional; neither emerges automatically from anisotropy + the existing constants. The extension is structurally viable but more substantive than the BTFR.05 synthesis suggested.
**Predecessors:** BTFR.02 (two-condition theorem), BTFR.03 (canonical-ED viability test), BTFR.05 (synthesis pointing to Route I + II-A).
**Successor:** BTFR.07 (revisit BTFR.05 verdict in light of corrected parameter accounting; alternatively, explore a nonlinear-source ED variant).

---

## 1. The extended PDE

The proposed extension to ED's penalty-channel equation, in cylindrical coordinates:

> D_R · (1/R) ∂_R(R ∂_R T) + D_z · ∂_z² T − λ T = − S_eff(R, z),
>
> S_eff(R, z) = σ_eff(a_baryon / a₀) · κ_act · A(R, z),

with:

- **D_R, D_z**: anisotropic diffusion coefficients. D_R inherits the cluster-calibrated D_T. D_z is set by some structural feature of disc geometry. Their ratio is the central tunable.
- **λ**: cluster-calibrated rate, unchanged.
- **a₀ ≡ λ² · D_T**: the candidate ED-derived acceleration scale. Numerically ≈ 1.0 × 10⁻¹⁰ m/s² (≈ 27 kpc/Gyr²) from cluster constants.
- **σ_eff(a/a₀)**: a coupling weighting function, to be derived. In the deep regime (a ≪ a₀) it must yield a sublinear M_b dependence to satisfy C2.
- **a_baryon(R)**: the local Newtonian gravitational acceleration of the baryonic distribution, `a_baryon = ∂_R Φ_baryon`.
- **κ_act, A(R, z)**: unchanged from canonical ED.

The two structural modifications compared to canonical ED are:
1. **Anisotropy** — replacement of scalar D_T with diagonal tensor (D_R, D_z).
2. **Coupling weighting** — replacement of constant κ_act with σ_eff(a/a₀) · κ_act.

Both modifications are required (BTFR.02 two-condition theorem; BTFR.03 §7).

---

## 2. Anisotropic Green's function

### 2.1 Hankel-transform solution

For a unit point source at the origin, σ(R) δ(z), the equation

> D_R · (1/R) ∂_R(R ∂_R T) + D_z · ∂_z² T − λ T = − δ²(R) δ(z)

is solved by Hankel transform in R and Fourier transform in z. Define the 2D Hankel transform

> T̂(k, z) = ∫₀^∞ T(R, z) J₀(kR) R dR.

The transformed equation becomes

> − D_R · k² · T̂ + D_z · ∂_z² T̂ − λ · T̂ = − (1 / 2π) · δ(z)

with solution (decaying at |z| → ∞)

> T̂(k, z) = (1 / [4π · √(D_z (D_R k² + λ))]) · exp(− |z| · √((D_R k² + λ) / D_z)).

Inverse Hankel transform at z = 0:

> T(R, 0) = (1 / 4π) ∫₀^∞ [k · J₀(kR) / √(D_z · (D_R k² + λ))] dk.

Using the standard integral ∫₀^∞ [k · J₀(kR) / √(k² + a²)] dk = e^{-aR} / R:

> **T(R, 0) = (1 / [4π · √(D_R · D_z)]) · e^{−R / L_R} / R,    L_R = √(D_R / λ).**

This is the **3D-anisotropic Yukawa Green's function evaluated on the disc plane**: it has 1/R structure, not log, even with strong anisotropy. The anisotropy enters only through the prefactor √(D_R · D_z).

### 2.2 The vertically-integrated potential

A different quantity — the z-integrated field T_⊥(R) ≡ ∫ T(R, z) dz — *does* satisfy a 2D screened-Poisson equation. Integrating the PDE over z (boundary terms vanish at |z| → ∞):

> D_R · (1/R) ∂_R(R ∂_R T_⊥) − λ T_⊥ = − σ(R)

where σ(R) = ∫ S(R, z) dz is the in-plane integrated source. The Green's function is the 2D modified Bessel:

> **T_⊥(R) = (1 / [2π D_R]) · K₀(R / L_R),    L_R = √(D_R / λ).**

K₀(x) has the asymptotics:

- Small x: K₀(x) ≈ −ln(x/2) − γ. **Logarithmic.**
- Large x: K₀(x) ≈ √(π / 2x) · e^{−x}. Exponential decay.

So **T_⊥ has a logarithmic regime for R ≪ L_R**, as required by C1.

### 2.3 The log window for T(R, 0)

The kinematic prediction `v_T² = −R · γ · ∂_R T(R, 0)` uses the *in-plane* field T(R, 0), not the integrated T_⊥. The relation between them depends on the perpendicular profile of T, which is governed by L_z = √(D_z / λ).

In the limit D_z → 0 strictly (no perpendicular diffusion), the equation at each z decouples: T(R, z) satisfies a 2D screened-Poisson equation independently at each z, sourced by S(R, z). For a thin disc source S(R, z) ≈ σ(R) · δ(z), this gives T(R, z) = 0 except at z = 0, where

> T(R, 0) = (1 / [2π D_R]) · K₀(R / L_R) · ∫ σ(R') (some kernel) dR'

— the 2D screened-Poisson Green's function applies *directly* to T(R, 0). In this strict limit, the log window for T(R, 0) is the same as for T_⊥, namely R ≪ L_R.

For finite D_z > 0, the field at z = 0 has the 3D-anisotropic 1/R structure (§2.1), not log. The transition between log-like (effective 2D) and 1/R-like (effective 3D) behavior happens at the perpendicular scale L_z = √(D_z / λ):

- **R ≪ L_z:** field hasn't propagated significantly in z; behaves as 3D-Yukawa-localized.
- **L_z ≪ R ≪ L_R:** the 2D-effective Green's function dominates; log behavior.
- **R ≫ L_R:** full screening, exponential cutoff.

**The log window is L_z ≪ R ≪ L_R.**

### 2.4 Anisotropy required for galactic-scale log

For the log window to span galactic radii (R ≈ 1 to 50 kpc) with L_R fixed at the cluster-calibrated 980 kpc:

- Upper bound (50 kpc) ≪ L_R = 980 kpc: ✓ automatic.
- Lower bound (1 kpc) ≫ L_z: requires L_z ≪ 1 kpc.

L_z = √(D_z / λ) and λ = 1/13.8 Gyr⁻¹, so L_z ≪ 1 kpc requires D_z ≪ λ · (1 kpc)² = 0.072 kpc²/Gyr.

With D_R = D_T = 6.97 × 10⁴ kpc²/Gyr (cluster-calibrated):

> **D_z / D_R ≲ 10⁻⁶.**

This is **four orders of magnitude smaller** than the BTFR.05 estimate of D_z/D_R ~ (h_disc / R_d)² ~ 10⁻². The disc-thickness-ratio intuition is insufficient to deliver the required anisotropy.

---

## 3. Implications for the parameter count claim

BTFR.05 claimed the combined extension introduces **zero new free parameters** by identifying D_z = D_R · (h_disc / R_d)². §2.4 above shows that estimate is wrong: D_z must be ~10⁴× smaller than (h_disc / R_d)² · D_R to put the log window at galactic scales.

**The honest accounting is:**

- D_R = D_T (cluster-calibrated): 0 new parameters.
- λ unchanged: 0 new parameters.
- κ_act unchanged: 0 new parameters.
- a₀ = λ² · D_T (derived): 0 new parameters.
- **D_z: 1 new parameter** (or 1 new structural relation that fixes it). The disc-thickness ratio does *not* fix it; some other structural argument is needed.

Possible structural arguments for D_z:

- **Matter-confined diffusion.** If D_T couples to local matter density (D_T ∝ ρ_local + const), then D_z is suppressed where the perpendicular matter column is thin. This is a non-trivial structural change to the theory; not "derived for free".
- **Disc-induced effective anisotropy.** Some symmetry-breaking mechanism by which the disc geometry imprints itself on the diffusion tensor. Requires a coupling between source geometry and operator, which is not in the canonical PDE.
- **Direct postulate.** Treat D_z / D_R as an empirical anisotropy ratio fixed by fitting BTFR. This adds 1 free parameter to ED's galactic-scale constants but is the simplest path.

**None of these is derived from existing ED structure.** BTFR.05's claim of zero new parameters was over-optimistic. A more honest claim: the combined extension introduces **one structural relation or one new parameter** (D_z, or whatever structural mechanism fixes it), in addition to D_R, λ, κ_act, and a₀.

---

## 4. The σ_eff coupling and amplitude scaling

### 4.1 What Route II-A requires

For C2 (M_eff ∝ √M_b), the source coupling must carry a √M_b weight after disc integration. The dimensional combination a₀ = λ² · D_T provides a *scale*; it does not by itself provide a *weighting function*. Route II-A demands an explicit functional form σ_eff(a / a₀) such that, when convolved with the activity index over a baryonic disc, the result scales as √M_b.

In MOND, the analogous role is played by the interpolation function μ(a/a₀) inside the *operator* — the equation itself is nonlinear. ED's PDE is linear by construction; we have to put the nonlinearity in the source coupling instead.

### 4.2 A candidate σ_eff

A natural candidate that mimics the deep-MOND scaling:

> σ_eff(a / a₀) = κ_act · √(a_baryon / a₀)    in the deep-acceleration regime (a_baryon ≪ a₀).

For an asymptotically Keplerian disc with total baryon mass M_b, a_baryon(R) = G M_b / R² in the outer regime, so

> √(a_baryon / a₀) = √(G M_b) / (R · √a₀).

Now compute M_eff = ∫ S_eff(R, z) dV:

> M_eff = ∫ κ_act · √(a_baryon / a₀) · A(R, z) · 2π R dR dz
>       = (κ_act · √(G M_b) / √a₀) · ∫ [A(R, z) / R] · 2π R dR dz

For activity index A ∝ G M_b / R³ (BTFR.03 §3):

> M_eff ∝ (κ_act / √a₀) · √(G M_b) · G M_b · ∫ dR / R³ · 2π R dz
>       ∝ (κ_act / √a₀) · (G M_b)^{3/2} · (geometric factor)

This is M_eff ∝ M_b^{3/2}, **not** √M_b. Plugging into v_flat² ∝ M_eff:

> v_flat² ∝ M_b^{3/2}    ⟹    v_flat⁴ ∝ M_b³,

which is slope 6, not 4. **The naive √(a/a₀) weighting on the activity source over-corrects.**

### 4.3 What the correct σ_eff would have to be

For BTFR (M_eff ∝ √M_b) with activity source A ∝ G M_b / R³, the σ_eff function must contribute an M_b^{−1} factor. With a_baryon ∝ M_b/R²:

> σ_eff(a / a₀) ∝ (a / a₀)^p    requires    M_b^p · M_b = M_b^{1/2}    ⟹    p = −1/2,

so σ_eff ∝ √(a₀ / a_baryon) = √(a₀ R² / (G M_b)) = R · √(a₀ / (G M_b)).

This puts an R · M_b^{−1/2} factor in the coupling. After disc integration:

> M_eff ∝ (κ_act / √(G M_b)) · (G M_b) · R · ∫ dR / R³ · 2π R dz
>       ∝ √(M_b) · (geometric factor)

OK so M_eff ∝ √M_b if σ_eff ∝ √(a₀ / a_baryon). **The inverse square root** of the local Newtonian acceleration.

But this functional form has no obvious physical motivation: it diverges in the high-acceleration (small-R) limit, which is unphysical and suggests the coupling cannot be a simple power of (a/a₀) but must saturate or otherwise regulate. In MOND, the interpolation function μ(x) interpolates smoothly between μ(x→0) = x and μ(x→∞) = 1, with the deep-MOND limit producing the right scaling automatically. A simple power σ_eff ∝ (a/a₀)^p does not interpolate; it diverges.

A better-behaved candidate that recovers the deep-regime BTFR is:

> σ_eff = κ_act · ν(a_baryon / a₀),    with    ν(x) → 1/√x    as    x → 0.

Such a function diverges at low acceleration (analogous to the MOND interpolation near deep regime). The behavior at high acceleration must be regulated to recover Newtonian-limit physics (galaxies dominated by their inner regions).

**This is essentially MOND, ported into a screened-Poisson source coupling.** The structural lesson: getting BTFR slope 4 in a linear-PDE framework requires importing the MOND interpolation function — there is no parsimony gain over just postulating MOND directly.

### 4.4 Alternative: a sublinear source functional (Route II-B)

Replace the activity index A with a √-yielding functional. Candidate:

> A_sub(R, z) = √(ρ_b(R, z) · a_baryon(R)).

For the asymptotic disc, ρ_b ∝ M_b · (disc shape), a_baryon ∝ M_b / R²:

> A_sub ∝ √(M_b · M_b / R²) · (disc shape) = (M_b / R) · (disc shape)

Disc-integrated:

> M_eff ∝ ∫ (M_b / R) · (shape) · 2π R dR ∝ M_b · (∫ shape · dR) = M_b · (R-dependent geometric factor).

So this gives M_b, not √M_b. Wrong scaling.

A different sublinear candidate:

> A_sub(R, z) = √(ρ_b(R, z) · a_baryon(R) · a₀).

Then A_sub ∝ √(M_b · M_b/R² · a₀) = √(M_b² · a₀ / R²) = M_b · √(a₀)/R. Still linear in M_b.

Constructing a √M_b-yielding *local* functional is hard because local densities and accelerations all carry M_b linearly for a Keplerian disc. The √M_b can only emerge from a *non-local* functional (averaging over the global baryonic structure), which is precisely what MOND's nonlinear PDE accomplishes implicitly.

**Conclusion: in any linear-PDE framework with strictly local source functionals, the natural M_b scaling is linear (slope 2 BTFR), not slope 4.** Recovering slope 4 requires either (a) an MOND-like nonlinear coupling function in σ_eff, or (b) a non-local source construction. Both are substantive structural commitments beyond "minimal extension".

---

## 5. Honest summary of the slope outcomes

| Configuration | C1 (log) | C2 (√M_b) | BTFR slope predicted |
|---|---|---|---|
| Canonical ED | Fail (1/R) | Fail (linear M_b) | falling curves; no flat regime; effective slope ill-defined |
| Anisotropic ED, no σ_eff | Pass (windowed log if D_z/D_R ≲ 10⁻⁶) | Fail (linear M_b) | 2 |
| Anisotropic ED + naive σ_eff = κ_act · √(a/a₀) | Pass | Over-corrects (M_b^{3/2}) | 6 |
| Anisotropic ED + correct σ_eff ∝ √(a₀/a) | Pass | Pass | 4, by construction |
| Anisotropic ED + ν(a/a₀) interpolation | Pass | Pass in deep regime | 4 (deep regime); recovers Newtonian elsewhere |

The bottom row is the structurally complete BTFR-derivation, but it requires both the strong anisotropy condition (§2.4) and an MOND-like interpolation function in the source coupling (§4.3). It is *not* parameter-free in the way BTFR.05 implied.

---

## 6. Cluster-regime consistency

At cluster scales (R ≳ Mpc, source distribution roughly 3D-isotropic with extent comparable to L_R):

- The anisotropy assumption breaks down: there is no preferred plane in a roughly-spherical cluster source. D_R = D_z = D_T isotropic is the correct limit. The log window collapses; the in-plane Green's function reverts to 3D Yukawa.
- The σ_eff(a/a₀) function: cluster-scale baryonic accelerations are *higher* than a₀ (clusters have bulk gas and merger shocks producing accelerations ≳ 10⁻⁹ m/s², well above a₀ ≈ 10⁻¹⁰ m/s²). The interpolation function ν(a/a₀) → 1 at high acceleration, recovering the canonical κ_act coupling.
- The merger-lag prediction (D_T ∇²T − λT = −S_activity at cluster scales) is unchanged because both modifications (anisotropy, σ_eff) deactivate in the cluster regime.

**Cluster-scale calibration is preserved.** The extension affects only galactic-disc physics, where the anisotropy (disc geometry) and deep-acceleration regime (a < a₀) both apply.

A remaining check, deferred to BTFR.07 or later: confirm that the cluster-scale regime transition is smooth (no discontinuity in predictions as one moves from disc to cluster scale). The interpolation ν(a/a₀) provides natural continuity in the source coupling. The anisotropy transition is sharper — it depends on the geometry of the source distribution — but should not produce observable inconsistencies because the relevant cluster predictions integrate over the source and are not sensitive to the anisotropy structure of the medium between sources.

---

## 7. The extended PDE in final form

Putting it all together:

> **D_R · (1/R) ∂_R(R ∂_R T) + D_z · ∂_z² T − λ T = − ν(a_baryon / a₀) · κ_act · A(R, z)**

with:

| Constant / function | Role | Origin |
|---|---|---|
| D_R | in-plane diffusion | = D_T cluster-calibrated |
| D_z | perpendicular diffusion | new structural relation or empirical (D_z / D_R ≲ 10⁻⁶ for galactic-scale log window) |
| λ | screening rate | cluster-calibrated |
| a₀ ≡ λ² · D_T | embedded acceleration scale | derived |
| ν(a/a₀) | coupling interpolation function | new structural choice; ν → 1 at high a, ν → √(a₀/a) at low a |
| κ_act | activity coupling | unchanged |
| A(R, z) | activity index | unchanged |

**Physical interpretation.** The penalty-channel field T is sourced by kinematic activity, but the source coupling depends on the local baryonic acceleration: in regions where Newtonian gravity is weak (a < a₀), the coupling is enhanced by √(a₀/a), producing additional T to compensate; in regions where Newtonian gravity is strong (a > a₀), the coupling is just κ_act and ED reduces to its canonical form. The diffusion of T through galactic discs is anisotropic (suppressed perpendicular to the disc) because the medium carrying T is itself disc-confined; in roughly-spherical environments (clusters, the cosmic web), the diffusion is isotropic.

This picture is structurally close to MOND in the deep-acceleration regime, but distinguishes itself at the level of:
- Source: kinematic activity rather than mass density.
- Operator: linear anisotropic-screened-Poisson rather than nonlinear-Poisson.
- Cluster regime: ED's screening provides the Mpc-scale cutoff where MOND requires an external-field-effect.

Whether this extension is the correct ED of nature is empirical. Whether it derives BTFR is structural — and the structural derivation, **once the strong anisotropy and the ν-interpolation are accepted as new structural inputs, succeeds**.

---

## 8. Recommended Next Steps

Three concrete options, ranked by parsimony:

1. **BTFR.07 — Re-evaluate the parameter accounting honestly.** Revisit BTFR.05's "zero new parameters" claim in light of §3 and §4. Decide whether ED-with-extension still counts as a *structural* derivation of BTFR or whether it has effectively imported MOND wholesale. Output: a corrected synthesis verdict and a clear statement of how many new structural commitments the extension requires.

2. **Anisotropy-mechanism derivation.** Investigate whether the strong-anisotropy condition D_z / D_R ≲ 10⁻⁶ can be derived from a structural mechanism (matter-coupled D_T; geometry-induced operator anisotropy) rather than postulated. If yes, the parameter count reduces and the BTFR derivation becomes more compelling. If no, the extension is parametrically equivalent to MOND-with-extra-screening.

3. **Pivot to nonlinear ED variant.** Drop the linear-PDE constraint and explore an ED formulation in which the source coupling is intrinsically nonlinear (analogous to MOND's μ(|∇φ|/a₀) inside the operator). Such a formulation might produce slope-4 BTFR more naturally and might reduce the number of structural inputs. Output: a new memo (BTFR.08) sketching the nonlinear-ED structural equations and checking whether they pass the BTFR.02 conditions intrinsically.

Status: complete.
