# DM.0 — Equilibrium Rotation-Curve Derivation for the Penalty-Channel PDE

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — first memo
**Status:** Derivation complete. Verdict: **NEGATIVE under the natural T-to-gravity mapping.** The equilibrium solution of the penalty-channel PDE, with parameters fixed from cluster scales (D_T = 2.1 × 10²⁷ m²/s, λ ≈ 1/t_H), does not reproduce flat galactic rotation curves. Three independent failure modes are identified. Multiple structural rescues are catalogued.
**Source PDE:** Galaxy-15 merger-lag paper, Eq. (2).
**Predecessor:** ED-04 (qualitative; does not contain this derivation).
**Successor:** see *Recommended Next Step* (DM.1).

---

## 1. Equilibrium reduction

The penalty-channel PDE in its merger-lag form is

> ∂T/∂t = D_T ∇²T + S(x, t) − λT.

Setting ∂T/∂t = 0 for a stationary baryonic source gives the **equilibrium equation**

> D_T ∇²T − λT = −S(x).

Dividing by D_T and defining the **screening length**

> L ≡ √(D_T / λ),

we obtain the canonical screened-Poisson form

> ∇²T − T / L² = −S(x) / D_T.

This is a Yukawa equation. Its Green's function in 3D is

> G(r) = exp(−r/L) / (4π r),

and the equilibrium solution is the convolution

> T(x) = (1 / D_T) ∫ G(|x − x'|) S(x') d³x'
>      = (1 / 4π D_T) ∫ exp(−|x − x'| / L) / |x − x'| · S(x') d³x'.

This is the foundation. Everything downstream is interpretation of this convolution.

---

## 2. Numerical scale of L

With D_T = 2.1 × 10²⁷ m² s⁻¹ (Mistele-derived) and λ = 1/t_H, where t_H ≈ 4.35 × 10¹⁷ s (Hubble time), so λ ≈ 2.3 × 10⁻¹⁸ s⁻¹:

> L² = D_T / λ ≈ 9.1 × 10⁴⁴ m²
> L ≈ 3.0 × 10²² m ≈ **1 Mpc**.

This recovers the Mistele scale ℓ_T ~ 1 Mpc that the merger-lag paper used to *set* D_T. Internally consistent — the screening length in equilibrium is the same scale that fixes D_T from weak-lensing data. No new free parameter.

**Implication for galactic dynamics:** all galaxies (R ≲ 30 kpc) sit deep in the unscreened regime r ≪ L. The Yukawa kernel is essentially Newtonian (1/r) for galactic separations; the exponential cutoff matters only at cluster and inter-cluster scales.

---

## 3. Solution for a point source

For a delta-function source S(x) = S₀ δ³(x):

> T(r) = S₀ / (4π D_T r) · exp(−r/L).

For r ≪ L, this reduces to

> T(r) ≈ S₀ / (4π D_T r).

So **T(r) ∝ 1/r at galactic scales.** This is the central structural fact. Everything that follows depends on how T is mapped to gravity.

The total spatial integral of T (over all space, point source) is finite:

> ∫ T d³x = S₀ ∫ exp(−r/L) / (D_T r) · r² dr · 4π / (4π)
>         = S₀ L² / D_T = S₀ / λ.

So the temporal-tension halo around a point source has integrated content S₀/λ, which is the source strength divided by the relaxation rate. With λ = 1/t_H, the integrated halo equals S₀ × t_H.

---

## 4. Solution for an exponential disk

Real galaxies are not point sources. The standard test case is an exponential thin disk:

> Σ_b(R) = (M_b / 2π R_d²) exp(−R/R_d),

where R_d is the disk scale length (typical R_d ≈ 3 kpc for a Milky-Way-class galaxy) and M_b is the total baryonic mass.

Treating S(x) as proportional to the baryonic mass density, S = β ρ_b(x) for some coupling β with units [s⁻¹] (since [S] / [D_T ∇²T] dimensional consistency forces this, given [T] = [ρ_b] · t):

> S(R, z) = β ρ_b(R, z) ≈ β · Σ_b(R) · δ(z) · (thickness factor).

For the thin-disk limit, this is a 2D source distribution. The Yukawa convolution gives, at r ≪ L (which covers the entire galactic disk),

> T(r) ≈ (β / 4π D_T) ∫ Σ_b(R') / |r − r'| d²R' · (line-of-sight factor).

The functional form is the **standard 2D Newtonian potential of an exponential disk**, scaled by β/D_T instead of G. This is the central observation: at r ≪ L, the screened-Poisson solution is *the Newtonian potential* of the source, with a different coupling.

For the exponential disk, this potential has a well-known form (Toomre 1962; Binney & Tremaine §2.6) involving Bessel functions. Asymptotically at large R:

> Φ_disk(R) ∝ M_b / R   (Keplerian falloff).

This produces v(R) ∝ R^(−1/2) — a **Keplerian rotation curve, not a flat one.**

---

## 5. Mapping T to gravitational response — three readings

The merger-lag paper writes κ_total = κ_baryon + κ_T but does not specify the exact functional relationship between T and gravitational potential. Three natural readings exist, each with a different rotation-curve consequence.

### 5.1 Reading A: T as effective mass density

The merger-lag paper's lensing-convergence decomposition is most cleanly read as:

> ρ_T_eff(x) = α · T(x),

where α has units [kg m⁻³ / [T units]] to make ρ_T a proper mass density. This ρ_T_eff then sources Newtonian gravity:

> ∇² Φ_T = 4π G ρ_T_eff = 4π G α T.

For the point source at r ≪ L: T ∝ 1/r, so ρ_T ∝ 1/r, and the enclosed mass within radius r is

> M_T(<r) = ∫₀ʳ 4π r'² · α T(r') dr' = (α S₀ / D_T) · r²/2.

That is, **M_T(<r) ∝ r²,** giving rotation contribution

> v_T²(r) = G M_T(<r) / r = G α S₀ r / (2 D_T) ∝ r.

So v_T ∝ √r — a **rising** rotation curve, not flat. Beyond r ~ L the exponential cutoff drops it back down.

### 5.2 Reading B: T as gravitational potential directly

If instead T *is* the gravitational potential contribution (Φ_T = γ T for some coupling γ), then for point source at r ≪ L:

> Φ_T ∝ 1/r → v² = R dΦ/dR ∝ 1/r.

This gives **v ∝ r^(−1/2)** — Keplerian falloff. Even worse than Reading A.

### 5.3 Reading C: T as a contribution to the metric coefficient (acoustic-metric reading)

In Phase-3 / ED-Phys-10, ED commits to an acoustic metric only. T could enter as a perturbation to the metric coefficient g_tt. In the weak-field limit, this maps onto a potential:

> Φ_eff = Φ_N + (c²/2) δg_tt,

with δg_tt ∝ T. This is structurally equivalent to Reading B with γ = c²/2. Same Keplerian outcome.

### 5.4 None of these gives flat curves

**Under all three natural readings, the equilibrium solution of the screened-Poisson PDE fails to produce flat rotation curves at galactic scales.** The cleanest reading (A, mass-density-equivalent) gives rising curves. The other two give falling curves. The shape of T(r) ∝ 1/r at r ≪ L is wrong for the observed phenomenology under any of them.

---

## 6. Tully-Fisher check

The baryonic Tully-Fisher relation requires v_∞⁴ ∝ M_b at the asymptotic flat-rotation velocity. In our equilibrium solution, **there is no asymptotic flat regime** under Reading A or B/C:

- Reading A: v_T peaks near r ~ L and drops exponentially beyond. No v_∞ exists.
- Reading B/C: v_T → 0 as r^(−1/2) (Keplerian). v_∞ = 0.

Under no reading does v_∞⁴ ∝ M_b emerge structurally. The BTFR is not reproduced.

---

## 7. a₀ check

A MOND-like acceleration scale a₀ sets the transition between Newtonian and modified-gravity regimes. The natural scale candidate from the PDE is

> a_PDE ≡ D_T / (L · t_H) = D_T · λ / L = √(D_T λ³) ≈ ?

Computing: D_T · λ = 2.1 × 10²⁷ × 2.3 × 10⁻¹⁸ ≈ 4.8 × 10⁹ m s⁻¹? Units check: [D_T λ] = m²/s · 1/s = m²/s². Divided by L (m) gives m/s². So:

> a_PDE = D_T · λ / L = D_T · λ / √(D_T/λ) = √(D_T · λ³)
>       = √(2.1 × 10²⁷ × (2.3 × 10⁻¹⁸)³)
>       ≈ √(2.1 × 10²⁷ × 1.2 × 10⁻⁵³)
>       ≈ √(2.5 × 10⁻²⁶)
>       ≈ **1.6 × 10⁻¹³ m s⁻²**.

Milgrom's a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻². The PDE-derived candidate scale is **three orders of magnitude too small.**

Even if the structural form were right (which §5 shows it is not), the parameters fixed from cluster scales produce an acceleration scale far below a₀.

---

## 8. Order-of-magnitude check for a real galaxy

Milky-Way-class galaxy: M_b ≈ 10¹¹ M☉ ≈ 2 × 10⁴¹ kg. Observed v_flat ≈ 220 km s⁻¹ ≈ 2.2 × 10⁵ m s⁻¹ at R ≈ 20–30 kpc.

For Reading A, with the unscreened-Poisson approximation valid (r ≪ L), the temporal-tension halo at radius r encloses

> M_T(<r) ≈ (α β / D_T) · M_b · r² · (geometric factor).

For this to deliver M_T ~ M_b at r ≈ 30 kpc = 10²¹ m (i.e., to give a "dark-matter-equivalent" amount), the dimensional combination α β / D_T must satisfy

> α β / D_T ~ 1 / r² = 10⁻⁴² m⁻².

Equivalently, α β ~ D_T / r² ~ 2 × 10⁻¹⁵ m s⁻² (after units cancel through, treating α as dimensionless and β as [s⁻¹]). With β ~ λ as the natural scale, β ~ 2.3 × 10⁻¹⁸ s⁻¹, so α would need to be of order 10³.

The natural prediction from "form forced, value inherited" with λ as the only relaxation scale gives **α β ≈ λ ≈ 2.3 × 10⁻¹⁸ s⁻¹**, which is **three orders of magnitude too small** to match observed rotation amplitudes. 

This matches the a₀ shortfall in §7 and confirms the diagnosis: the equilibrium temporal-tension contribution at galactic scales, with parameters set from cluster physics, is too weak by ~10³ to do dark-matter's work.

---

## 9. Three independent failure modes — summary

The derivation reveals three structurally independent ways the equilibrium PDE fails to reproduce galactic rotation curves:

1. **Wrong shape.** T(r) ∝ 1/r at r ≪ L produces rising (Reading A) or Keplerian-falling (Readings B/C) curves, not flat ones.
2. **No BTFR.** No asymptotic flat regime exists under any T-to-gravity mapping.
3. **Wrong magnitude.** The natural acceleration scale derived from cluster-scale parameters is ~10³ smaller than Milgrom's a₀.

These are not three aspects of one problem. They are three independent symptoms, and any structural fix has to address all three.

---

## 10. What is forced, what is inherited, what is open

### Forced (by the PDE form alone)
- The equilibrium solution is a Yukawa convolution of the source.
- The screening length L = √(D_T / λ) ≈ 1 Mpc.
- For r ≪ L (all galactic radii), T(x) is the Newtonian potential of the source with coupling β/D_T.

### Inherited (set externally)
- D_T (from Mistele weak-lensing extent).
- λ (set to 1/t_H phenomenologically).
- α and β (T-to-gravity coupling, source coupling — not specified anywhere in the framework).
- The mapping from T to effective gravity (Reading A vs. B vs. C — not committed in any paper).

### Open (cannot be settled by the PDE alone)
- Whether the equilibrium framing is the right one for galactic dynamics.
- Whether activity-dependent sourcing (S = S(ρ_b, |∇v|, σ_τ, ...)) changes the conclusion.
- Whether the PDE itself is incomplete (missing nonlinear terms, missing channels).
- Whether a separate ED mechanism (not the penalty channel) produces galactic flat curves.

### Requires simulation
- Full 3D Yukawa convolution against realistic SPARC baryonic distributions (extension of this analytic work into per-galaxy fits) — but only after the structural failure modes in §9 are addressed, since simulation can't fix wrong shape or wrong magnitude.

### Requires additional structure
- A different T-to-gravity mapping (e.g., nonlinear: ρ_eff ∝ |∇T|² instead of T).
- A different sourcing law (e.g., S ∝ activity rather than S ∝ ρ_b).
- A galactic-scale parameter that differs from the cluster-scale parameter (breaking the "one D_T everywhere" claim).
- A separate ED channel doing the galactic-rotation-curve work, with the penalty channel responsible only for cluster mergers.

---

## 11. Refutation conditions

This memo's verdict can be refuted in three ways:

1. **Identify a fourth T-to-gravity mapping** consistent with the merger-lag paper's κ-decomposition that produces flat curves naturally.
2. **Show that the equilibrium reduction is invalid** for galactic dynamics (e.g., that t_eq ~ t_dyn so the equilibrium assumption fails). Order-of-magnitude check rules this out: t_eq ~ 10⁷ years, t_dyn ~ 10⁸ years, so equilibrium is justified.
3. **Show that activity-dependent sourcing**, with S = S(activity) rather than S = β ρ_b, produces flat curves at galactic scales while still reproducing the cluster-merger-lag result.

Any of these would overturn the negative verdict. None has been demonstrated.

---

## 12. What ED-04's SPARC dwarf result actually showed

ED-04's §5 reports that Active dwarfs have ⟨D_outer⟩ ≈ 6.01 vs. Quiet dwarfs at 3.94 (53% higher). This is a *signature* test of the activity-dependence prediction — confirming that activity-dependent variation exists in the data — but it is **not** a derivation or fit of a rotation-curve law. The result does not address shape, BTFR, or magnitude.

The result is consistent with the temporal-tension framework's *qualitative* prediction (active > quiet) but does not test the *quantitative* claim that ED reproduces the rotation-curve law. Under the equilibrium PDE derivation above, the quantitative claim fails. The activity-dependence may still be real and may still be a temporal-tension signature — but if so, the *mechanism* producing it is not the equilibrium PDE solution. It is whatever additional structure (activity-dependent S, nonlinear T-to-gravity mapping, or separate channel) is responsible for the bulk of the rotation-curve effect.

This is consistent with the SPARC result being a Tier-1 *signature* confirmation rather than a Tier-1 *mechanism* confirmation.

---

## 13. Verdict

**The equilibrium solution of the penalty-channel PDE, with parameters fixed from cluster-merger physics, does not reproduce flat galactic rotation curves.** Three independent failure modes (wrong shape, no BTFR, wrong magnitude by ~10³) have been identified. Each is a structural finding, not a numerical artifact.

The merger-lag paper's citation of ED-04 for galactic-scale flat curves is, on this analysis, not supported by the PDE itself. ED-04 asserts the consequence; the derivation does not deliver it.

This does **not** refute Event Density. It refutes the specific claim that the penalty channel, in its current form with current parameters, accounts for galactic rotation curves. The framework retains:
- The cluster-merger lag (confirmed).
- The activity-dependence signature (confirmed in dwarf SPARC means).
- All forced theorems in the quantum and gravitational sectors.

What it loses, until rescued, is the implicit claim that *a single ED mechanism with a single parameter handles both clusters and galaxies in equilibrium.*

---

## Recommended Next Step

**DM.1 — Activity-dependent sourcing memo.**

The most plausible structural rescue, and the one ED-04's text most directly supports, is that S(x) is not simply proportional to baryonic mass density but proportional to **activity density** — rotation, shear, turbulence, star formation. ED-04 §2.2 explicitly says: *"Temporal tension arises from ED gradients driven not by mass density but by activity density."*

If S = S(activity) rather than S = β ρ_b, then:

1. The screened-Poisson equation is the same; only the source changes.
2. Activity is concentrated where the disk is dynamically active (rotation, shear, star-forming regions), which is itself a function of radius.
3. The resulting T(r) would have a different shape than 1/r, possibly one that produces flat-curve phenomenology.
4. The amplitude could be naturally different from the mass-density coupling, potentially fixing the magnitude problem.

DM.1 should:
- Specify a quantitative model for activity density (e.g., S ∝ |∇v|² · Σ_b, or S ∝ Σ_SFR, or S ∝ ω · Σ_b for angular velocity ω).
- Solve the screened-Poisson equation with this activity-dependent source.
- Check whether the resulting T(r) gives flat curves under any of the three T-to-gravity readings.
- Check the BTFR scaling.
- Check the magnitude with cluster-fixed D_T and λ.
- Report verdict.

The expected outcome is one of:
- **PASS:** activity-dependent sourcing produces flat curves at the right magnitude with the right BTFR. The framework is rescued.
- **PARTIAL:** activity-dependent sourcing produces flat curves but with wrong magnitude or wrong BTFR. Identifies which structural piece is still missing.
- **FAIL:** activity-dependent sourcing does not help. The equilibrium-PDE-based DM mechanism is structurally incomplete and a deeper revision is required.

This is the smallest executable next step, and it isolates the single most plausible structural escape. DM.2 onward would depend on its outcome.

---

## End-of-turn summary

What got done: the explicit equilibrium derivation that ED-04 asserted but did not perform. The screened-Poisson Yukawa solution is now in hand. Three independent failure modes are documented under the natural T-to-gravity mappings.

What did not get done: a rescue of the framework. The negative verdict stands until DM.1 (activity-dependent sourcing) is run, or until a structural alternative is identified.

What this means for the program: the cluster-merger result is unaffected — that's a *non-equilibrium* test of the same PDE, and it stands. What this memo touches is only the *equilibrium* extension to galactic scales, and on that question the implicit claim in ED-04 and in the merger-lag paper's §2.1 citation is not supported by the math as written. The arc continues with DM.1.
