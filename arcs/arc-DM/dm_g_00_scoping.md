# DM.G.0 — Geometry-Sourced Temporal Tension: Scoping

**Date:** 2026-04-27
**Arc:** Dark Matter, sub-arc DM.G — first memo (scoping)
**Status:** New hypothesis launched. Following the closure of the canonical DM-arc (DM.0–DM.6) with FAIL on BTFR, the DM.G sub-arc opens to test an alternative source mechanism for the temporal-tension field T: not the mass density of DM.0 (refuted), nor the kinematic activity of DM.1 (refuted at galactic-disc scales), but **the intrinsic geometry of the baryonic disc itself**. The Pringle/saddle intuition motivates this: a rotating thin disc has a distinctive geometric structure (anisotropic, saddle-like in its embedding) that is absent from the spherical-and-isotropic source assumptions of DM.0/DM.1. This memo scopes the hypothesis, identifies the structural motivations and open questions, defines success/falsifier criteria, and lays out a four-memo work plan.
**Predecessor:** DM.6 (canonical DM-arc closure with FAIL on BTFR).
**Empirical anchor:** SPARC catalog (same as DM-arc); merger-lag prediction must continue to hold (consistency check).
**Successor:** DM.G.1 (candidate geometric source functionals).

---

## 1. The hypothesis

### 1.1 Statement

**T is sourced by the intrinsic geometric structure of the baryonic distribution, not by its mass density nor by its kinematic activity.**

Specifically: a rotating thin baryonic disc has an anisotropic geometric character (it is a roughly 2D surface embedded in 3D space, with non-zero mean and Gaussian curvature where the disc bends, with rotation-induced saddle structure in its velocity field, and with a sharply different in-plane vs perpendicular extent). DM.G hypothesizes that **this geometry itself acts as the source of temporal tension**, with the field T diffusing outward from the disc's geometric features and producing the gravitational-like effects observed as flat rotation curves.

In equation form, the canonical-ED PDE is preserved:

> D_T · ∇²T − λ T = − S_geom(R, z),

but the source `S_geom` is a functional of geometric quantities of the baryonic disc rather than of `ρ_b` (DM.0) or `A_kinematic` (DM.1).

### 1.2 The Pringle/saddle intuition

The user's pushback after the BTFR sub-arc closure pointed at a real structural feature missed by DM.1: **a disc is not a small 3D blob; it is a thin 2D-like sheet with its own intrinsic curvature properties.** Imagine a Pringle: locally saddle-shaped, with negative Gaussian curvature, anisotropic in the principal curvature directions. A rotating self-gravitating disc has analogous structure (warped at large radii, with anisotropic stress-energy distribution).

If T is sourced by *this geometric anisotropy* — by how curved/saddle/anisotropic the disc is at each point — then:

- The source is intrinsically geometric, not kinematic or mass-density-based.
- The source vanishes for a perfectly spherical mass distribution (which has no preferred plane, no saddle structure).
- The source is largest in regions where the disc geometry is most pronounced (rotating discs, especially their warped outer regions; absent in dwarf spheroidals).
- Cluster-scale geometry (roughly spherical) gives small S_geom; cluster predictions are consistent with the canonical merger-lag result.

This is a structurally distinct source class. It hasn't been examined in DM.0, DM.1, or BTFR.01–09.

---

## 2. Structural motivations

### 2.1 Why geometry might naturally repair C1

The BTFR.02 two-condition theorem requires a logarithmic far-field (C1). In BTFR.06 and BTFR.08, two routes were identified for canonical ED to produce a log kernel: (R-1) postulated strong anisotropy with D_z/D_R ≲ 10⁻⁶, or (R-2) the Einstein-like relation D_T = c²·κ_act under self-consistency.

**Geometry-sourced T offers a third, structurally distinct route: if the source itself is intrinsically 2D (concentrated on a 2-surface of vanishing thickness), the field equation reduces to a 2D Helmholtz problem in the disc plane.** In the limit where the source geometry is exactly 2D (a delta function in z with finite extent in R), the in-plane Green's function is the K₀ Bessel function with logarithmic behavior at small radii — without requiring strong perpendicular anisotropy of the diffusion tensor.

This is the 2D analog of the standard result that a charge sheet in 3D Newtonian gravity produces a constant attraction (no falloff) above the sheet, and a logarithmic potential when the sheet is finite. **Geometry-sourced T may naturally produce the log far-field that activity-source ED cannot.**

### 2.2 Why geometry might naturally repair C2

C2 requires the disc-integrated effective charge M_eff to scale as √M_b rather than as M_b. The BTFR.06 analysis showed that activity-source S = κ_act · v²/R² gives M_eff ∝ M_b after disc integration, producing slope-2 BTFR.

**Geometric quantities of self-gravitating discs scale sublinearly with mass.** Specifically:

- A self-gravitating exponential disc has scale length R_d that grows roughly as M_b^(1/3) (from virial-like arguments) or as M_b^(1/2) (in some scaling-relation formulations).
- Mean curvature H of the disc surface scales inversely with R_d, so H ~ M_b^(-1/3) or M_b^(-1/2).
- Gaussian curvature K ~ H² ~ M_b^(-2/3) or M_b^(-1).
- Disc-integrated curvature: ∫|H| dA ~ R_d² · H ~ R_d ~ M_b^(1/3) or M_b^(1/2).

If the source is `S_geom ~ |H|`, the disc integral gives M_eff ~ M_b^(1/3) or M_b^(1/2). For the latter case, **C2 is satisfied automatically by the geometric scaling of self-gravitating discs**.

This is a structurally distinct mechanism from MOND's a₀-weighting and from a sublinear source functional postulate. The √M_b emerges *not* because the coupling is engineered to produce it, but because the *geometry of self-gravitating discs* is intrinsically sublinear in mass.

### 2.3 Independence from previous routes

DM.G is structurally independent of BTFR.06 (anisotropic diffusion) and BTFR.07 (MOND-like ν(a/a₀)):

- DM.G keeps the canonical isotropic D_T (no anisotropy postulated).
- DM.G keeps the canonical κ_act as a single coupling constant (no a/a₀-weighting).
- DM.G modifies the source functional only.

This makes DM.G the *least invasive* structural extension among the three known routes. It uses only existing ED primitives (D_T, λ, κ_act) and modifies only the form of S, not the operator.

---

## 3. What "geometry" means in ED terms

The hypothesis statement above is qualitative. Concrete realization requires identifying which geometric quantity of the baryonic disc enters S_geom. Several candidates are structurally available:

### 3.1 Candidate G1 — Baryon-density gradient norm

> S_geom = κ_geom · |∇ρ_b|²

The simplest geometric quantity: where ρ_b changes rapidly. For a disc, this is concentrated at the disc edge and at the disc midplane. The square ensures non-negativity.

**Status:** very simple; conceptually closer to DM.0 than the others. May not capture the "anisotropic saddle" intuition fully. Worth checking but unlikely to be the deepest realization.

### 3.2 Candidate G2 — Mean curvature of the baryon-isodensity surface

> S_geom = κ_geom · H²(x)

where H is the mean curvature of the local isodensity surface of ρ_b at point x. For a thin disc this surface is approximately the disc plane near the midplane, and the mean curvature is largest at the disc edge (where the surface curves over).

**Status:** intrinsically geometric; coordinate-invariant; natural in differential-geometry language. Captures the "Pringle" intuition partially (mean curvature of a saddle is small or zero; Gaussian curvature is what's negative).

### 3.3 Candidate G3 — Gaussian curvature of the baryon-isodensity surface

> S_geom = κ_geom · |K(x)|

where K is the Gaussian curvature. This is the direct Pringle quantity: K < 0 for saddle-shaped surfaces, K > 0 for elliptic (sphere-like) surfaces, K = 0 for ruled surfaces (cylinder, cone).

**Status:** most direct realization of the user's saddle intuition. Topological-flavored (∫K dA = 4π·χ where χ is the Euler characteristic). For a disc, χ = 1, so the integrated Gaussian curvature is fixed by topology, not by mass — a structurally sharp feature.

### 3.4 Candidate G4 — Vorticity-shear saddle invariant

> S_geom = κ_geom · |ω · σ|

where ω is the vorticity vector and σ is a symmetric shear tensor of the velocity field. This is an antisymmetric-symmetric coupling that captures "rotation in the presence of shear" — distinctive of disc rotation, absent in pure rigid-body or pure vorticity-free flows.

**Status:** kinematic-geometric hybrid; closer in spirit to DM.1 but with a different invariant structure. May be related to chiral structure or helicity of the velocity field.

### 3.5 Candidate G5 — Disc-extrinsic-curvature of the embedded 2-surface

> S_geom = κ_geom · |II(x)|²

where II is the second fundamental form of the disc embedded in 3D (or 4D for a relativistic version). This measures how the disc "bends" relative to its tangent plane.

**Status:** most rigorous differential-geometric formulation. Requires identifying the disc as a 2-surface (which is approximate for a real galactic disc with finite thickness). Likely the most mathematically clean if a precise definition can be given.

### 3.6 Selection criterion

DM.G.1 will evaluate these candidates against three structural tests:

- **Disc-integrated charge scaling.** Does ∫S_geom dV produce M_eff ∝ √M_b for self-gravitating discs?
- **Coordinate / gauge invariance.** Is S_geom a well-defined geometric scalar that doesn't depend on artificial coordinate choices?
- **Cluster-regime behavior.** Does S_geom vanish (or become small) for roughly-spherical cluster mass distributions, preserving the cluster anchor?

Whichever candidate(s) pass these tests will proceed to DM.G.2 for asymptotic analysis.

---

## 4. Minimal mathematical questions

The arc must answer these structural questions, in order:

### 4.1 The source functional

- **Q1.** What is the structurally most natural choice of S_geom? G1, G2, G3, G4, G5, or some combination?
- **Q2.** Does the chosen S_geom respect rotational symmetry, parity, and time-reversal in the appropriate way?
- **Q3.** Does S_geom contain only existing ED primitives (D_T, λ, κ_act, ρ_b), or does it require new fundamental constants?

### 4.2 The disc integral

- **Q4.** For a self-gravitating exponential disc with mass M_b and scale length R_d, what is `M_eff = ∫S_geom dV`?
- **Q5.** Does M_eff(M_b, R_d) reduce to a function of M_b alone for the empirical M_b–R_d relation? Or does it retain explicit R_d dependence?
- **Q6.** Does M_eff scale as √M_b (passing C2) or as M_b (failing C2)?

### 4.3 The asymptotic field

- **Q7.** Given S_geom localized to a thin disc, what is the asymptotic far-field of T(R) outside the disc?
- **Q8.** Does the resulting Green's-function structure produce a logarithmic in-plane far-field (passing C1)?
- **Q9.** Does the asymptotic v_T satisfy v_T⁴ ∝ M_b with the empirical proportionality constant ≈ 47 M_⊙⁻¹ (km/s)⁴?

### 4.4 Consistency

- **Q10.** Does DM.G's source vanish in the cluster regime (roughly-spherical geometry), preserving the merger-lag prediction?
- **Q11.** Does DM.G predict universality of the coupling κ_geom (analogous to the universality result that survived DM.5)?
- **Q12.** Does DM.G affect any of the foundational arcs (R, M, N, Q, B, GR)? (Expected: no, since the modification is to S only, not to the operator.)

---

## 5. Success and falsifier criteria

### 5.1 Success criteria

DM.G is judged successful if and only if all of the following hold:

- **(S-1) Slope-4 BTFR.** Asymptotic v_T⁴ ∝ M_b with the empirically-correct coefficient (within order-of-magnitude before fitting; within the empirical scatter after).
- **(S-2) No per-galaxy tuning.** The coupling κ_geom takes a single universal value across the SPARC sample (analog of the DM.1 universality test, σ(κ_geom)/mean < 0.13 with all Spearman correlations |ρ| < 0.3).
- **(S-3) Cluster preservation.** The merger-lag prediction continues to hold; geometry-sourced T at cluster scales is consistent with the canonical D_T calibration.
- **(S-4) No new fundamental constants.** S_geom uses only D_T, λ, κ_geom (one coupling, analogous to κ_act), and possibly basic geometric primitives. No imported acceleration scale, no postulated anisotropy ratio.
- **(S-5) Foundational compatibility.** No conflict with closed Theorems N1, GR.1, or the forced theorems of arcs R, M, Q, B.

### 5.2 Falsifier criteria

DM.G is refuted (and the arc closes) if any one of the following holds:

- **(F-1) Slope-2 or slope-other-than-4.** If the structural derivation gives any BTFR slope ≠ 4, DM.G has the same failure mode as DM.1 and offers no theoretical advance.
- **(F-2) Explicit R_d retention.** If the asymptotic v_T depends on R_d (or surface brightness, or other galaxy parameters) in a way that survives the empirical M_b–R_d scaling, DM.G cannot reproduce the empirical 0.1-dex BTFR scatter.
- **(F-3) Required new constants.** If DM.G needs a new fundamental constant (a₀-equivalent, anisotropy ratio, etc.) to produce slope-4, then it is no more parsimonious than the BTFR.07 options and offers no theoretical advance.
- **(F-4) Cluster anchor violation.** If S_geom does not vanish (or become small) for cluster geometry, the cluster merger-lag prediction is broken and DM.G is inconsistent with the canonical anchor.
- **(F-5) Foundational conflict.** If any arc's forced theorem requires modification to accommodate DM.G, the arc is structurally too expensive to pursue.

### 5.3 Possible mixed outcomes

If DM.G produces slope-4 BTFR but only with explicit R_d dependence (failing F-2), or only with one new constant (failing F-3), it remains a *partial* result — a clean alternative to BTFR.07's three options, but not a full structural derivation of BTFR. The DM.G.4 decision memo will distinguish full success, partial success, and falsification.

---

## 6. Roadmap for DM.G.1–DM.G.4

### 6.1 DM.G.1 — Candidate source functionals

Evaluate G1–G5 (and any other candidates surfaced during analysis) against the three selection criteria (§3.6). Produce a structural shortlist of one or two candidates that warrant asymptotic analysis. Output: ranked list of S_geom candidates with structural justification.

### 6.2 DM.G.2 — Asymptotic analysis of the resulting PDE

For the selected candidate(s), derive:
- The disc-integrated effective charge M_eff(M_b, R_d).
- The far-field Green's-function structure.
- The asymptotic v_T(R) including its R-dependence.
- The proportionality constant in v_T⁴ ∝ f(M_b).

This is the analytic core of the arc. No numerical work required; structural derivation only.

### 6.3 DM.G.3 — BTFR viability check (C1 + C2)

Apply the BTFR.02 two-condition theorem to the analytic results from DM.G.2. Determine:
- Whether C1 (log far-field) is satisfied.
- Whether C2 (M_eff ∝ √M_b) is satisfied.
- Whether the resulting BTFR slope is exactly 4, exactly 2, or something else.
- Whether R_d dependence persists in the asymptotic v_T.

Output: pass/fail for each of S-1 through S-5; identification of which (if any) F-1 through F-5 trigger.

### 6.4 DM.G.4 — Decision memo

Based on DM.G.3, decide:
- **Adopt:** all S-criteria pass, no F-criteria trigger. DM.G is the canonical activity-source-replacement and should be implemented numerically (parallel to DM.7–DM.14 in scale).
- **Revise:** one F-criterion triggers but the structural posture is otherwise promising. Identify the minimal modification (e.g., a different geometric invariant) and either continue the arc or fork to DM.G'.
- **Reject:** multiple F-criteria trigger or the structural derivation is incompatible with foundational arcs. Close DM.G with a clean rejection memo (analog of DM.0's rejection of mass-source).

---

## 7. Scope discipline

### 7.1 What this arc is

A structural-derivation arc, parallel in flavor to BTFR.01–09 but focused on a different hypothesis (geometry-sourced T) rather than on canonical-ED extensions. The arc is bounded: four memos (DM.G.1–DM.G.4), each focused on one structural question. No numerical implementation work until DM.G.4 if-and-only-if the decision is "adopt."

### 7.2 What this arc is not

- Not a revival of the DM.0–DM.6 numerical pipeline. The DM-arc is closed; DM.G is independent.
- Not a substrate-foundational derivation. DM.G assumes ED's existing PDE form and modifies only S; substrate-level questions (e.g., BTFR.10's foundational derivation of D_T) remain out-of-scope.
- Not a re-litigation of BTFR.06 anisotropy or BTFR.07 MOND-like coupling. DM.G is a structurally distinct hypothesis; the BTFR sub-arc routes are not its competitors but its predecessors.

### 7.3 Termination conditions

The arc terminates at DM.G.4 with either adoption, revision (which extends it), or rejection. Adoption triggers a parallel implementation arc (DM.G.5+) only if the decision memo deems numerical confrontation warranted. Rejection closes the arc with a clean refutation record analogous to DM.0's mass-source rejection.

---

## 8. Recommended Next Steps

Three concrete next steps, in order:

1. **DM.G.1: Candidate source functionals.** Survey G1–G5 (and any structurally-motivated alternatives) against the three selection criteria (§3.6). Identify the top one or two candidates for asymptotic analysis. This is a single-memo structural-survey task; should take roughly the same effort as a single BTFR.0x memo. **This is the immediate next step.**

2. **Establish a clean dimensional accounting before DM.G.2.** When the candidate source is selected, verify that S_geom uses only existing ED primitives (D_T, λ, κ_geom) plus geometric quantities (curvatures, gradients of ρ_b) that are coordinate-invariant. Flag any hidden new constants explicitly before they propagate into the asymptotic analysis. This is a half-memo housekeeping task to be folded into DM.G.1.

3. **Hold the merger-lag retrodiction recommendation from DM.6 §6.1 in parallel.** DM.G is a structural-theory arc; the merger-lag work is empirical-arc work. The two are independent and can proceed in parallel. The merger-lag retrodiction does not depend on whether DM.G succeeds or fails, and a positive merger-lag result would strengthen ED's empirical position regardless of the DM.G outcome. Recommend keeping it on the active-empirical-arcs list.

DM.G is opened with cautious optimism. The Pringle/saddle intuition has not been examined in any prior ED memo, and it represents a structurally distinct hypothesis class. Whether it produces slope-4 BTFR cleanly or fails for the same C2 reasons as DM.1 is the question DM.G.1–DM.G.4 will answer. Expected duration: four memos over a contained work session, paralleling the BTFR sub-arc's structural-only character (no numerical implementation until adoption).

Status: complete.
