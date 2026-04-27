# DM.G.1 — Candidate Geometric Source Functionals

**Date:** 2026-04-27
**Arc:** Dark Matter, sub-arc DM.G — second memo
**Status:** Five candidate geometric source functionals (G1–G5) defined precisely, then evaluated against three structural tests (T1: disc-integrated charge scaling with M_b; T2: coordinate invariance and ED-primitive expressibility; T3: cluster-regime behavior). **No single candidate cleanly passes all three tests with √M_b scaling.** G3 (Gaussian curvature) and G4 (vorticity-shear saddle invariant) survive T2 and T3 but fail T1 with M_b-linear scaling, replicating DM.1's C2 failure mode. G2 (mean curvature) is dimensionally clean and partially passes T3 but also fails T1. G1 (density gradient) and G5 (extrinsic curvature) have structural defects that disqualify them from further analysis. **The honest result of this survey is that simple geometric source functionals, as enumerated, do not produce √M_b scaling automatically.** The Pringle/saddle intuition therefore appears to address C1 (kernel structure) but not C2 (amplitude scaling) — same partition of repair-mechanisms as the BTFR.06/07/08 routes. DM.G.2 must either (a) accept a combined geometric-kinematic candidate (e.g., G3 · √(GM_b)) that is half-derived and half-postulated, or (b) close DM.G with a clean refutation analogous to DM.0/DM.1.
**Predecessor:** DM.G.0 (scoping).
**Successor:** DM.G.2 (asymptotic analysis of the surviving candidate, or pivot decision).

---

## 1. Candidate definitions

Each candidate is a scalar field S_geom(x) constructed from the baryonic distribution and intended to enter the canonical-ED PDE as

> D_T · ∇²T − λ T = − S_geom(x).

For consistency with ED's existing primitives, S_geom should be expressible as

> S_geom = κ_geom · (geometric scalar)

where κ_geom is a coupling constant with units chosen so that S_geom matches the dimensions of `D_T · ∇²T = λ · T` (which has units 1/time when T is dimensionless). κ_geom should be expressible in terms of D_T, λ, c, or κ_act without invoking new fundamental constants.

### 1.1 G1 — Baryon-density gradient norm

> **S_G1(x) = κ_geom · |∇ρ_b(x)|².**

Captures regions where matter changes rapidly. For an exponential disc this is concentrated near the disc edge and at the disc midplane.

**Units.** |∇ρ_b|² has units [mass]²/[length]⁸. To match S in 1/time, κ_geom must have units [length]⁸/([mass]² · [time]). This combination cannot be constructed from D_T, λ, c, κ_act alone — it requires a mass scale and additional length powers that ED's existing primitives do not supply. **G1 is dimensionally not closed under existing ED primitives without invoking Newton's constant G or an explicit mass scale.**

### 1.2 G2 — Mean curvature of baryon-isodensity surfaces

> **S_G2(x) = κ_geom · H²(x),**   H(x) = mean curvature of the isodensity surface ρ_b(y) = ρ_b(x) at x.

Mean curvature is a coordinate-invariant scalar measuring the average bending of a surface. H² is non-negative and vanishes on flat regions of the surface.

**Units.** H has units 1/[length]. H² has units 1/[length]². For S in 1/time, κ_geom must have units [length]²/[time] = D_T. **Dimensionally clean: κ_geom = D_T (or D_T · dimensionless factor).**

### 1.3 G3 — Gaussian curvature of baryon-isodensity surfaces

> **S_G3(x) = κ_geom · |K(x)|,**   K(x) = κ₁(x) · κ₂(x), Gaussian curvature.

Gaussian curvature is the product of principal curvatures. K > 0 on elliptic (sphere-like) regions, K < 0 on saddle regions, K = 0 on parabolic / ruled surfaces. The absolute value ensures non-negativity.

**Units.** K has units 1/[length]². κ_geom must have units [length]²/[time] = D_T. **Dimensionally clean: κ_geom = D_T.**

### 1.4 G4 — Vorticity-shear saddle invariant

> **S_G4(x) = κ_geom · |ω(x) · σ(x)|,**   ω = vorticity vector, σ = symmetric shear tensor of v_baryon(x).

This is the simplest scalar combining vorticity (antisymmetric part of velocity gradient) and shear (symmetric traceless part) that captures "rotation in the presence of shear" — distinctive of disc rotation, vanishing for pure rigid-body or pure shear flows.

For axisymmetric circular flow with v(R), the relevant component is

> ω · σ ~ ω_z · σ_{Rφ} ~ (v/R + ∂_R v) · (R · ∂_R(v/R))

which for Keplerian v² = GM_b/R gives

> |ω · σ| ~ (1/2)(3/2) · GM_b/R³ = (3/4) · GM_b/R³.

**Units.** |ω · σ| has units 1/[time]². κ_geom must have units [time]. This is the same dimensional class as DM.1's κ_act. **Dimensionally clean: κ_geom = κ_act (or κ_act · dimensionless factor).**

### 1.5 G5 — Disc extrinsic curvature (second fundamental form)

> **S_G5(x) = κ_geom · |II(x)|²,**   II = second fundamental form of the baryonic disc as a 2-surface embedded in 3D space.

Extrinsic curvature measures how a 2-surface bends in its embedding space. For a perfectly flat disc, II = 0. For a warped (Pringle-shaped) disc, II ≠ 0 with magnitude proportional to the warp.

**Units.** |II|² has units 1/[length]². κ_geom = D_T as in G2/G3. Dimensionally clean.

**Structural caveat:** G5 requires identifying the baryonic disc as a well-defined 2-surface, which is approximate for real galactic discs (which have finite thickness and density profiles, not sharp boundaries). Unlike G2 and G3 (which are well-defined for any density distribution via isodensity surfaces), G5 requires an additional step — choosing a "disc surface" — that introduces ambiguity unless a structural prescription is given.

---

## 2. Structural tests

### 2.1 T1 — Disc-integrated charge scaling

For a self-gravitating exponential disc with mass M_b, scale length R_d, and thickness h_disc, compute

> M_eff = ∫ S_geom(x) dV.

For BTFR via the BTFR.02 two-condition theorem under the log-kernel assumption (C1 satisfied), C2 requires M_eff ∝ M_b^{1/2}.

The empirical SPARC M_b–R_d relation is approximately R_d ∝ M_b^{1/3} (with substantial scatter); for self-gravitating-disc theory R_d ∝ M_b^{1/2} is also defensible. We evaluate scaling under both.

#### G1 — |∇ρ_b|²

For ρ_b(R, z) = ρ₀ · exp(−R/R_d) · sech²(z/h_disc) with ρ₀ = M_b / (4π R_d² h_disc):

|∇ρ_b|² ≈ (∂ρ_b/∂z)² (vertical dominates for thin disc) ≈ 4 · ρ_b² · tanh²(z/h_disc) / h_disc².

∫|∇ρ_b|² dV ~ ρ₀² · R_d² · h_disc · (1 / h_disc²) ~ M_b² / (R_d² · h_disc³).

For R_d ∝ M_b^{1/3}: M_eff ~ M_b² / M_b^{2/3} = M_b^{4/3}.
For R_d ∝ M_b^{1/2}: M_eff ~ M_b² / M_b = M_b.

Neither gives M_b^{1/2}. **G1 fails T1.**

#### G2 — H²

Mean curvature of an isodensity surface: H ~ 1/R_curv, where R_curv is the local radius of surface curvature.

For an exponential disc, isodensity surfaces near the midplane are roughly flat (H ≈ 0); near the disc "edge" (where ρ_b drops by a factor ~e), they curve over with R_curv ~ R_d. In the halo (low ρ_b), surfaces are nearly spherical with R_curv ~ R, and H² ~ 1/R² → ∫H² dV ~ ∫dR diverges without regularization.

Weighted by ρ_b (to regularize the halo divergence): ∫ρ_b · H² dV. For the disc-edge contribution:
∫(disc edge) ρ_b · H² dV ~ ρ₀ · (1/R_d²) · (R_d² · h_disc) ~ ρ₀ · h_disc ~ M_b / R_d².

For R_d ∝ M_b^{1/3}: M_eff ~ M_b · M_b^{−2/3} = M_b^{1/3}.
For R_d ∝ M_b^{1/2}: M_eff ~ M_b · M_b^{−1} = constant.

Closer to the right neighborhood than G1, but neither M_b^{1/2}. **G2 fails T1** (under either M_b–R_d relation).

Without ρ_b-weighting (i.e., just ∫H² dV), the integral diverges in the halo. **G2 is structurally ill-defined without a regularization choice that itself introduces M_b-dependence.**

#### G3 — |K|

Gaussian curvature is bounded by the Gauss-Bonnet theorem: for any closed isodensity surface (Euler characteristic χ = 2 for sphere-topology),

> ∮ K dA = 4π χ = 8π,    independent of size or shape.

The integrated **signed** Gaussian curvature is a topological invariant. The integrated **absolute** value |K| is bounded below by 8π but can be larger if there are saddle regions.

For a thin disc shape: outer edges have K < 0 (saddle), top and bottom faces have K > 0 (elliptic). The total |K| integrates to roughly twice the topological 8π = 16π.

Volume integration weighted by ρ_b: ∫ρ_b · |K| dV. The disc has K ~ 1/R_d² over a region of volume ~ R_d² · h_disc:

> M_eff ~ ρ_b · (1/R_d²) · (R_d² · h_disc) ~ M_b / R_d².

Same scaling as G2: M_eff ∝ M_b/R_d² → either M_b^{1/3} or constant depending on M_b–R_d relation. **G3 fails T1.**

#### G4 — |ω · σ|

For Keplerian outer disc:

> S_G4 ~ κ_act · GM_b / R³.

Disc-integrated: M_eff ~ κ_act · GM_b · ∫(1/R³) · 2πR dR · (vertical factor) ~ κ_act · GM_b / R_min²

where R_min is the inner cutoff. **Linear in M_b, with R_min residual.**

This is exactly DM.1's scaling (the activity index is itself a vorticity-shear-like invariant). **G4 fails T1 in the same way DM.1 did.**

#### G5 — |II|²

For a flat disc, II = 0. For a self-gravitating disc, the warp amplitude ε is set by the balance between disc self-gravity, halo gravity, and rotational support. The dependence of ε on M_b is model-dependent — for typical disc-warping mechanisms (tidal, halo-misalignment, secular bending instabilities), ε ~ degrees-of-warp, weakly dependent on M_b.

Without a definite ε(M_b) scaling law, the M_b dependence of M_eff is not derivable from first principles. **G5 fails T1 by ambiguity** (unlike G1–G4 which fail with a clean wrong answer, G5 fails to even produce a definite answer without postulating the warp mechanism).

### 2.2 T2 — Coordinate invariance and ED-primitive expressibility

| Candidate | Coord. invariant | κ_geom from existing ED primitives |
|---|---|---|
| G1 | Yes | **No** (requires mass-scale and length-power combination unavailable from D_T, λ, c, κ_act) |
| G2 | Yes | Yes (κ_geom = D_T) |
| G3 | Yes | Yes (κ_geom = D_T) |
| G4 | Yes | Yes (κ_geom = κ_act) |
| G5 | Yes (with disc-surface specification) | Yes (κ_geom = D_T) |

**G1 fails T2.** All others pass.

### 2.3 T3 — Cluster-regime behavior

Clusters have roughly spherical mass distributions; isodensity surfaces are nearly spherical. Cluster gas has minimal ordered rotation in equilibrium.

| Candidate | Cluster behavior | T3 |
|---|---|---|
| G1 | ∇ρ ≠ 0 for any non-uniform distribution; sphere has radial gradient ~ ρ/R | **Non-zero in clusters; fails T3** |
| G2 | H ≠ 0 for spherical surfaces (H = 1/R for sphere); contributes ρ_b · H² over cluster volume | **Non-zero in clusters; fails T3** |
| G3 | K = 1/R² > 0 for spheres; |K| · area = topological 8π | **Topologically-fixed non-zero in clusters; fails T3** |
| G4 | ω = 0 in equilibrium clusters → S_G4 → 0 | **Vanishes in clusters; passes T3** |
| G5 | Cluster has no preferred 2-surface; II not naturally defined | **Vanishes by non-applicability; passes T3 trivially** |

**G1, G2, G3 fail T3.** G4 passes structurally; G5 passes by inapplicability.

---

## 3. Comparison table

| Candidate | T1: scaling | T2: invariance + ED-clean | T3: cluster | Notes |
|---|---|---|---|---|
| **G1** \|∇ρ_b\|² | M_b^{4/3} or M_b | **No** (needs new units) | **No** (∇ρ ≠ 0 in clusters) | Disqualified on T2 |
| **G2** H² | M_b^{1/3} or constant | Yes (D_T) | **No** (spherical H ≠ 0) | Halo-divergent without ρ_b-weighting |
| **G3** \|K\| | M_b^{1/3} or constant (with ρ_b weighting) | Yes (D_T) | **No** (Gauss-Bonnet topological) | Most directly captures Pringle intuition; fails T3 |
| **G4** \|ω·σ\| | M_b (linear) | Yes (κ_act) | **Yes** (no rotation in clusters) | Same scaling as DM.1; passes T3 only |
| **G5** \|II\|² | Ambiguous; depends on warp ε(M_b) | Yes (D_T), with disc-surface caveat | Yes (cluster has no embedded 2-surface) | Structurally ill-posed without warp model |

**No candidate passes all three tests with M_b^{1/2} scaling.**

---

## 4. Survivors

Strict reading of the three tests:

- G1 fails T2 (unable to construct κ_geom from existing ED primitives). **Disqualified.**
- G2 fails T1 (wrong scaling) and T3 (non-zero in clusters). **Disqualified.**
- G3 fails T1 (wrong scaling) and T3 (Gauss-Bonnet locks ∮K dA at 8π for spherical surfaces). **Disqualified.**
- G4 fails T1 (M_b-linear scaling, replicating DM.1). Passes T2 and T3. **Survives by partial pass.**
- G5 passes T2 and T3 by the looser readings, but T1 is undecided. **Survives only by ambiguity.**

**Strictly, no candidate cleanly survives.** The candidate-level survey produces a clean negative result: simple geometric scalars do not naturally yield √M_b scaling for self-gravitating discs.

---

## 5. Structural discussion

### 5.1 Which candidates are most promising for C1 (log far-field)?

The kernel-level argument for C1 — that geometry-sourced T might naturally produce a log far-field — comes from the observation that a 2D-surface-localized source in a 3D-isotropic medium produces a different far-field from a 3D-volume-localized source.

**G3 (|K|) is the most direct realization.** Gaussian curvature is concentrated on the 2-surface itself; the source is intrinsically 2-dimensional in support. In the limit of vanishing disc thickness, S_G3 becomes a genuine 2-surface delta-function, and the in-plane field equation reduces to a 2D problem with K₀-Bessel Green's function (log-windowed regime).

This is the structurally cleanest path to C1 among the candidates. **G3 would repair C1 if it survived T1.**

G2 (H²) shares the 2-surface concentration but has the halo-divergence problem.

G4 (|ω·σ|) is volume-distributed in the rotating disc, not 2-surface-concentrated; less promising for C1.

G5 (|II|²) is 2-surface-concentrated but ambiguous.

### 5.2 Which candidates are most promising for C2 (√M_b scaling)?

**None.** All candidates evaluated give either M_b-linear scaling (G4), constant or M_b^{1/3} scaling (G2, G3), or ambiguous scaling (G5). The structural reason: geometric quantities of self-gravitating discs scale either as topological invariants (M_b-independent), as inverse-length-squared (giving M_b/R_d² → constant for R_d ∝ M_b^{1/2}), or as linear-in-M_b kinematic combinations.

**Producing M_b^{1/2} from a geometric source requires a sublinear functional that doesn't appear in the natural enumeration.** The DM.G.0 §2.2 expectation — that "geometric quantities of self-gravitating discs scale sublinearly with mass" — was overly optimistic; the actual scalings are either sub-sublinear (constant or M_b^{1/3}) or supra-linear (M_b for activity-like terms).

### 5.3 Which are likely dead ends?

**G1** is a dead end on dimensional grounds (T2 fail).

**G2** is a dead end without a regularization mechanism that doesn't introduce arbitrary M_b dependence.

**G3** is the most theoretically interesting candidate but is locked by the Gauss-Bonnet theorem to topological-invariant scaling. The integrated Gaussian curvature is fixed by topology, not by M_b. Localized weighting (ρ_b · |K|) produces wrong scaling. **G3 hits a topological obstruction, not a gap in the analysis** — strengthening this candidate would require either dropping the topological constraint (e.g., by integrating only over a sub-region) or finding a different geometric quantity that captures saddleness without being a Gauss-Bonnet integrand.

**G4** is an honest re-statement of DM.1 with different motivation. It does not advance beyond what BTFR.01–09 already analyzed.

**G5** is structurally ill-posed without a warp-model commitment.

### 5.4 The honest finding

The Pringle/saddle intuition motivates DM.G but does not, by itself, supply a √M_b mechanism. The intuition is structurally sound for C1 (kernel-shape concentration on a 2-surface produces a log far-field naturally), but does not address C2 (amplitude scaling with M_b is governed by separate considerations — disc-integrated geometric quantities, not by saddle structure per se).

This puts DM.G in the same epistemic position as BTFR.06 (anisotropy) and BTFR.08 (self-consistency): it offers a structural mechanism for C1 but leaves C2 unsolved. **DM.G's structural value, as currently scoped, is in repairing C1, not in repairing C2.**

If DM.G is to derive slope-4 BTFR, one of the following must hold:
- A combined functional (geometric × kinematic) is admissible. For example, S_combined = κ_geom · |K| · √(GM_b/R²) — Gaussian curvature weighted by a √M_b factor. This is "half-derived" (the geometric part) and "half-postulated" (the √M_b weighting), structurally similar to BTFR.07 Routes II-A/B.
- A higher-order geometric invariant exists that scales sublinearly with M_b for self-gravitating discs and was not enumerated in G1–G5.
- The arc accepts a slope-2 outcome and reports geometry-sourced T as a structural alternative to anisotropy/self-consistency for C1, with C2 still open.

---

## 6. Implications for DM.G.2

DM.G.2 was scoped as "asymptotic analysis of the surviving candidate." With no candidate cleanly surviving all three tests, DM.G.2 must instead be a **decision memo** with three options:

- **(A) Accept partial survival.** Carry G3 (cleanest geometric realization) into asymptotic analysis with the explicit acknowledgment that it will fail C2 with topological-invariant M_eff. The analysis would confirm C1 satisfied, C2 failed, predict slope-2 or slope-other-than-4 BTFR. Outcome: clean refutation memo for DM.G.4, parallel to DM.0 and DM.1 closures.

- **(B) Expand the candidate space.** Consider combined geometric-kinematic functionals (G3 × √M_b weighting, or geometric-invariant combinations not in G1–G5) and higher-derivative invariants (Laplacian of curvature, divergence of shear-vorticity coupling). Single additional memo before DM.G.2.

- **(C) Close DM.G early.** Recognize that the candidate-level survey produces a clean negative result and that the DM.G hypothesis class — *simple* geometric source functionals — does not derive BTFR. Proceed directly to DM.G.4 closure memo. The structural lesson is preserved: geometry-sourced T can plausibly repair C1 (G3 is the cleanest realization) but cannot repair C2 in any single-functional form.

The most honest path is (A) or (C). Path (B) risks being a fishing expedition unless a specific structural motivation supplies a new candidate.

---

## 7. Recommended Next Steps

Three concrete next steps, in decreasing priority:

1. **DM.G.2 as decision memo (path A or C).** Frame DM.G.2 not as "asymptotic analysis of the survivor" but as "asymptotic confirmation that G3 fails C2 + structural lesson about geometry-sourced T." This produces a clean closure trajectory: G3's topological-invariant scaling can be analytically derived for an exponential disc, the predicted BTFR slope can be computed (likely slope 2 with no R_d residual, since topology is independent of size), and DM.G.4 can close the arc with a refutation analogous to DM.0/DM.1. **This is the recommended path.**

2. **Reserve path B for a single-memo expansion if a specific structural motivation surfaces.** If during the next session a particular combined-functional candidate emerges from independent reasoning (e.g., a Lagrangian derivation of the source from ED's substrate, or a constraint imposed by a foundational arc result), then a DM.G.1.5 expansion memo could test it before committing to closure. Otherwise, DM.G should not become an open-ended geometric-functional search.

3. **Carry the C1-only finding forward as a structural insight, regardless of DM.G's adoption decision.** Even if DM.G closes with refutation, the result that "intrinsic 2-surface localization of the source produces a log far-field naturally" is a structurally interesting alternative to BTFR.06 anisotropy and BTFR.08 self-consistency. It belongs in the closure memo (DM.6 §3.1's "two routes to repair C1" should be updated to "three routes to repair C1: anisotropy, Einstein-like relation, geometric-2-surface localization") and in any future revival of the BTFR question.

The DM.G arc has produced its first clean structural result — that simple geometric source functionals do not naturally satisfy C2, replicating DM.1's failure mode. The arc should now move quickly toward closure rather than expanding into open-ended candidate search.

Status: complete.
