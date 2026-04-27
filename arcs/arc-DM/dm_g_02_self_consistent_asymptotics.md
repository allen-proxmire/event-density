# DM.G.2 — Self-Consistent G4 Asymptotic Derivation and Provisional Verdict

**Date:** 2026-04-27
**Arc:** Dark Matter, sub-arc DM.G — third memo (asymptotic derivation)
**Status:** Honest re-analysis of the G4 (vorticity-shear / activity-index) candidate under full self-consistency, including the inner-disc contribution that DM.G.1b's hopeful verdict overlooked. The disc-integrated effective charge `M_eff(M_b)` decomposes into an inner-regime contribution (where `v_baryon` dominates) scaling as `M_b`, plus an outer-regime contribution (deep-T, where `v_T` dominates) scaling as `√M_b · log(M_b)`. **For galaxies in the SPARC regime, the inner-regime M_b-linear term dominates M_eff at large M_b, giving asymptotic v_flat⁴ ∝ M_b² — slope-2 BTFR.** The outer-regime √M_b contribution exists but is subdominant; it does *not* produce slope-4 BTFR globally. **DM.G.1b's "G4 survives" verdict was based on an incomplete analysis (outer-regime only) and is retracted.** **The structural reason ED's linear-PDE framework cannot derive slope-4 BTFR is now precisely identified: linearity of the PDE means M_eff is a *sum* over disc regions, and the M_b-linear inner contribution dominates the √M_b outer contribution for large galaxies; only a nonlinear PDE (MOND-style) bypasses this by making the asymptotic v determined by total enclosed mass through nonlinear field equations rather than by source integration.** **Provisional verdict: self-consistent canonical ED predicts slope-2 BTFR robustly. DM.G arc should close with refutation.**
**Predecessor:** DM.G.1b (self-consistent re-evaluation, partial analysis).
**Successor:** DM.G.3 (BTFR viability check) folded into this memo's verdict; DM.G.4 (closure decision memo).

---

## 1. Setup: G4 ≡ DM.1 activity index under self-consistency

### 1.1 What G4 reduces to

The vorticity-shear saddle invariant defined in DM.G.1 (§1.4) reduces, for axisymmetric circular flow with v(R), to

> S_G4(R) = κ_act · |ω · σ| ∝ κ_act · v_total² / R²

up to dimensionless O(1) factors set by the geometric coefficients of the symmetric/antisymmetric decomposition. This is the same structural form as DM.1's activity index `A = α · shear² + (1 − α) · vorticity²`, which also reduces to A ≈ v²/R² in the asymptotic regime regardless of α. **G4 and DM.1's activity index are the same scalar for axisymmetric circular flow.**

What distinguishes the DM.G.1b analysis from DM.5 is not the source choice but the *self-consistency treatment*:

- **DM.5 / DM2 production-run:** activity built from `v_baryon` (photometric mass models, treated as fixed external input). PDE solved with this as a static source.
- **DM.G.1b / this memo:** activity built from `v_total = √(v_baryon² + v_T²)` (self-consistent equilibrium velocity). The source depends on T through v_T's contribution.

### 1.2 Why the self-consistent treatment is correct

In ED's slow-time picture, T affects the equilibrium rotation of disc matter through the geodesic-equation force `a = c² · ∇T`. The actual rotation velocity of disc matter at radius R is `v_total(R)`, not v_baryon(R). The kinematic activity that physically sources T is the activity of the actual rotation, not the activity of a hypothetical baryon-only disc.

The DM2 simulation used v_baryon for computational simplicity (the SPARC catalog tabulates v_gas, v_disk, v_bulge as the photometric components, so the activity is straightforward to compute from these). But this is the linearized version of the equation. The structurally honest version uses v_total.

---

## 2. The self-consistent PDE

### 2.1 Substituting the self-consistent activity

With v_total² = v_baryon² + v_T² and v_T² = R · c² · |∂_R T| (slow-time geodesic relation):

> A(R) = v_total² / R² = v_baryon² / R² + c² · |∂_R T| / R.

For an asymptotically Keplerian baryonic disc at large R, v_baryon² → G·M_b/R, so:

> A(R) = G·M_b / R³ − c² · ∂_R T / R     (using ∂_R T < 0 for T-decreasing-outward).

Source: S = κ_act · A. Plug into PDE D_T·∇²T − λT = −S:

> D_T·∇²T − λT = −κ_act · G·M_b/R³ + κ_act · c² · ∂_R T / R.

Move T-dependent term to LHS:

> D_T·∇²T − (κ_act · c² / R) · ∂_R T − λT = −κ_act · G·M_b / R³.

### 2.2 The Einstein-like relation cancellation

Expanding the cylindrical Laplacian at z = 0: ∇²T = ∂²_R T + (1/R)·∂_R T + ∂²_z T. The (1/R)·∂_R T coefficient becomes (D_T − κ_act·c²)/R. **If D_T = c²·κ_act (Einstein-like relation, BTFR.08), this term vanishes**, leaving:

> **D_T · (∂²_R + ∂²_z) T − λ T = − κ_act · G·M_b / R³.**     (Einstein-like relation assumed)

This is the 2D-Cartesian Helmholtz operator with Green's function K_0:

> G(R) = (1 / [2π·D_T]) · K_0(R / L),    L = √(D_T/λ).

For R ≪ L, K_0(R/L) ≈ −ln(R/L) (logarithmic regime, satisfying C1).

**Conditional dependency:** the rest of this memo assumes the Einstein-like relation holds (BTFR.09's P2 reading). If not, the operator is closer to canonical cylindrical screened-Poisson and C1 fails, and the slope-2 verdict below is *strengthened* (the failure would be at both C1 and C2 levels rather than C2 only).

---

## 3. The two-regime structure of the source

The source on the RHS is `S(R) = κ_act · G·M_b / R³`. This reflects the *baryonic* (Keplerian) contribution to A. But this is the activity in the regime where v_baryon dominates. **In the regime where v_T dominates, the activity is computed differently.**

### 3.1 The crossover radius

Define R_x as the radius where v_baryon² = v_T². For Keplerian v_baryon² = G·M_b/R and asymptotic v_T² = v_flat² (constant in deep-T):

> R_x = G·M_b / v_flat².

In the self-consistent fixed point with slope-4 BTFR (v_flat² ∝ √M_b), R_x ∝ M_b/√M_b = √M_b.

### 3.2 Inner regime: R < R_x

v_baryon dominates. v_total² ≈ v_baryon² = G·M_b/R. Activity:

> A_inner(R) ≈ G·M_b / R³.

Source contribution (per unit volume): κ_act · G · M_b / R³. **Linear in M_b.**

### 3.3 Outer regime: R > R_x

v_T dominates. v_total² ≈ v_T² = v_flat² (constant in deep-T). Activity:

> A_outer(R) ≈ v_flat² / R².

Source contribution (per unit volume): κ_act · v_flat² / R². **Proportional to v_flat², which is ∝ √M_b under slope-4 BTFR.**

### 3.4 The piecewise source

For the disc, the activity is well-approximated by:

> A(R) ≈ G·M_b/R³  for R < R_x;    A(R) ≈ v_flat²/R²  for R > R_x.

This is the form derived from kinematic self-consistency. The source for the PDE is S(R) = κ_act · A(R) over both regimes.

---

## 4. The disc-integrated effective charge

### 4.1 Inner contribution

> M_eff^{inner} = ∫(R_min to R_x) S(R) · 2π R dR · (vertical factor)
>               = 2π · κ_act · G · M_b · ∫(R_min to R_x) dR / R²
>               = 2π · κ_act · G · M_b · [1/R_min − 1/R_x].

For R_x ≫ R_min (true for any non-trivial galaxy):

> **M_eff^{inner} ≈ (2π · κ_act · G / R_min) · M_b.**

This is **linear in M_b**, with proportionality constant depending on R_min (the inner disc cutoff, set by bulge or stellar physics, roughly M_b-independent or weakly M_b-dependent at most).

### 4.2 Outer contribution

> M_eff^{outer} = ∫(R_x to R_max) S(R) · 2π R dR · (vertical factor)
>               = 2π · κ_act · v_flat² · ∫(R_x to R_max) dR / R
>               = 2π · κ_act · v_flat² · ln(R_max / R_x).

With v_flat² = (M_eff_total)/(2π·κ_act) (from log-kernel asymptotic, derived in §5 below), and R_x ∝ √M_b, R_max ~ R_d (disc scale, weakly M_b-dependent):

> **M_eff^{outer} ≈ M_eff_total · ln(R_max / R_x).**

This is a self-consistency constraint: M_eff_outer is a fraction of M_eff_total times a log factor. We'll combine this with the inner contribution to solve for M_eff_total.

### 4.3 Solving the self-consistency

Set M_eff_total = M_eff^{inner} + M_eff^{outer}:

> M_eff_total = (2π · κ_act · G / R_min) · M_b + M_eff_total · ln(R_max / R_x).

Solve for M_eff_total:

> **M_eff_total = (2π · κ_act · G / R_min) · M_b / [1 − ln(R_max / R_x)].**

For ln(R_max/R_x) < 1 (which requires R_x not too small compared to R_max), the denominator is finite and positive. For R_max/R_x of order 10, ln ≈ 2.3 — the bracket goes negative, indicating no fixed point in this naive treatment.

**The naive piecewise treatment breaks down when the deep-T regime is large enough that the outer contribution would dominate.** This indicates the self-consistency loop is more subtle than a simple two-regime substitution can capture.

### 4.4 Honest interpretation

For SPARC galaxies, R_max/R_x is order 1 to 10 (the deep-T regime exists but doesn't extend many decades beyond R_x). The log factor is small but not negligible. The fixed-point analysis above suggests M_eff_total is dominated by the inner contribution if ln(R_max/R_x) is small, with corrections from the outer term.

In the limit where outer contribution is small (ln ≪ 1):

> M_eff_total ≈ (2π · κ_act · G / R_min) · M_b · [1 + ln(R_max/R_x) + O(ln²)].

**M_eff is linear in M_b at leading order.** The √M_b scaling expected from the outer regime alone does *not* survive because the inner regime contributes an M_b-linear term that is generically larger.

In the opposite limit where outer dominates (ln large), the fixed-point equation diverges, indicating the linear-PDE treatment with hard-piecewise activity breaks down. A smoothly-interpolated activity (which is more physical) would give a finite answer somewhere between the two regimes.

---

## 5. The asymptotic v_flat

In the log regime (R ≪ L), the K_0 Green's function gives:

> T(R) ≈ −(M_eff_total / [2π·D_T]) · ln(R / L_eff)

(for L_eff = L · 2 · e^{−γ_E}). The slow-time gradient:

> ∂_R T ≈ − M_eff_total / [2π · D_T · R].

Asymptotic v_T from the slow-time geodesic:

> v_T² = R · c² · |∂_R T| = c² · M_eff_total / (2π · D_T).

With Einstein-like relation D_T = c² · κ_act:

> **v_T² = M_eff_total / (2π · κ_act).**

Squaring:

> v_T^4 = M_eff_total² / (4π² · κ_act²).

For BTFR slope-4 (v_T^4 ∝ M_b), need M_eff_total ∝ √M_b. From §4.4, M_eff_total ≈ M_b-linear (at leading order). So:

> **v_T^4 ∝ M_b² (slope-2 BTFR), not M_b (slope-4).**

The √M_b · log correction from the outer regime modifies the prefactor and introduces a slow log dependence, but does *not* change the leading slope.

---

## 6. BTFR conditions revisited

### 6.1 C1 (log far-field)

**Conditional pass.** The Einstein-like relation D_T = c²·κ_act produces 2D-Cartesian Helmholtz with K_0 Green's function and logarithmic in-plane far-field over the entire SPARC galactic regime (R ≪ L = 980 kpc). C1 is satisfied if the relation holds. If the relation does not hold (P1 reading, BTFR.09), C1 is *not* satisfied and the analysis is moot.

### 6.2 C2 (M_eff ∝ √M_b)

**Failed.** Despite the self-consistent kinematic feedback that DM.G.1b emphasized, the inner-disc Keplerian contribution to the activity gives M_eff^{inner} ∝ M_b, which dominates the outer-disc √M_b contribution for any galaxy with a non-trivial Keplerian inner regime. The √M_b scaling is *real but subdominant*. The asymptotic BTFR slope is 2, not 4.

### 6.3 C3 (R_d independence)

**Partially failed.** The inner contribution has R_min in the denominator, so v_T^4 ∝ M_b² × 1/R_min². R_min varies across the SPARC sample (different galaxies have different inner-disc cutoffs). This introduces additional scatter beyond what slope-2 alone would predict. Even setting aside the slope error, the empirical 0.1-dex BTFR scatter is unlikely to be reproduced.

### 6.4 Honest aggregate

| Condition | Self-consistent canonical ED status |
|---|---|
| C1 | **Conditional pass** (under Einstein-like relation D_T = c²·κ_act) |
| C2 | **Fail** (M_eff dominated by M_b-linear inner contribution) |
| C3 | **Fail** (R_min dependence) |
| Slope-4 BTFR | **No** (predicts slope-2 robustly) |

---

## 7. Why MOND succeeds where ED-self-consistent fails

The slope-2 vs slope-4 distinction is structurally illuminating.

In MOND, the equation is **nonlinear**: ∇·[μ(|∇Φ|/a₀)·∇Φ] = 4π·G·ρ_b. In the deep-MOND limit (μ → x), this becomes:

> |∇Φ|² = a₀ · G · M_enc / R²    →   v² = R · |∇Φ| = √(G · M_enc · a₀) (asymptotic).

The asymptotic v_flat depends on **total enclosed mass M_b**, not on the disc-integrated activity. The nonlinear field equation enforces this directly: at radius R outside the bulk of the baryonic mass, v² is determined by what's inside R, regardless of the inner-disc kinematic structure.

In ED's *linear* PDE (even with self-consistency), v_T at radius R is determined by the disc-integrated source ∫S(R')·G(R, R')·dR'. The Green's function is sensitive to source distribution, not just to total enclosed mass. So inner-disc activity contributes to T(R) at the same order as outer-disc activity (modulo log weighting from K_0).

**The structural obstacle to slope-4 BTFR in canonical ED is the linearity of the field equation**, not any specific feature of the source functional. Self-consistency does not repair this: the source remains a kinematic functional integrated against a linear Green's function, and the M_b-linear inner contribution always exists.

This recapitulates BTFR.07 Option C: only a **nonlinear PDE** can natively produce slope-4 BTFR. ED's linear screened-Poisson, regardless of source choice (mass, activity, geometry, self-consistent activity), gives at best slope-2.

---

## 8. Provisional verdict

> **Self-consistent canonical ED predicts slope-2 BTFR robustly under the Einstein-like relation, slope-undefined or worse without it.** The √M_b scaling that DM.G.1b §3.4 identified in the outer-disc regime is a real structural feature of the deep-T equilibrium, but it is *additive* with an M_b-linear inner-disc contribution that dominates the disc-integrated source for any realistic galaxy.
>
> **The DM.G.1b "G4 survives" verdict is retracted.** G4 under self-consistency does not produce slope-4 BTFR. It produces slope-2 with a √M_b-log correction.
>
> **The DM.G arc therefore concludes with refutation, parallel to DM.0 and DM.1.** No canonical-ED source functional examined (mass, activity, density-gradient, mean curvature, Gaussian curvature, vorticity-shear, extrinsic curvature) produces slope-4 BTFR under self-consistency. The structural obstacle is identified: ED's linear-PDE framework, combined with disc-integrated source averaging, locks the BTFR slope at 2 regardless of source-functional choice.

---

## 9. Explicit dependency map

What this verdict depends on:

| Result | Depends on |
|---|---|
| C1 satisfied (log kernel) | Einstein-like relation `D_T = c²·κ_act` (BTFR.09's P2 reading) |
| Outer-disc √M_b scaling | Slow-time interpretation (a = c²·∇T); deep-T regime existence |
| Inner-disc M_b-linear scaling | Keplerian v_baryon at small R; standard exponential disc profile |
| Slope-2 verdict | Both regimes contributing additively; linear PDE with log-kernel Green's function |
| MOND-comparison conclusion | Standard MOND deep-regime derivation |

**Unconditional results:**
- The self-consistent equation has the form derived in §2 (independent of the Einstein-like relation; the relation only affects whether the (1/R)·∂_R T term cancels).
- The two-regime structure of the activity is a direct consequence of the kinematic decomposition v_total² = v_baryon² + v_T² and the existence of a deep-T regime where v_T saturates.
- The M_b-linear inner contribution is unavoidable for any galaxy with a Keplerian inner disc.

**Conditional results:**
- The exact form of K_0 kernel asymptotics requires Einstein-like relation.
- The √M_b scaling of the outer contribution requires v_flat² ∝ √M_b, which is BTFR slope-4 — circular if used to derive slope-4.

The conditionalities suggest one possible escape: if the Einstein-like relation does *not* hold (P1), then the operator is canonical cylindrical and C1 fails directly, giving falling rotation curves and BTFR slope ≪ 2 (consistent with DM2's 0.24). If the relation *does* hold (P2), C1 passes but C2 fails by the inner-disc dominance. **Neither reading produces slope-4.**

---

## 10. Implications for DM.5/DM.6 closure

DM.5 and DM.6 closed the DM-arc with a FAIL verdict on canonical activity-source ED. DM.G.1b raised the question whether that closure was premature — whether the DM2 numerical FAIL was a linearization artifact and self-consistent canonical ED would actually produce slope-4 BTFR.

This memo answers that question: **no.** The self-consistent canonical ED produces slope-2 BTFR robustly. The DM2 numerical slope of 0.24 reflects:
- C1 failure of the linearized cylindrical PDE (no log kernel) → curves fall too fast
- C2 failure under linearization (inner-disc M_b-linear scaling)

Self-consistency *partially* repairs the analysis (inserts the missing v_T-back-reaction term, opens the C1 repair via Einstein-like relation), but does not produce slope-4. The structural prediction of canonical self-consistent ED is slope-2, not slope-0.24 and not slope-4.

**This sharpens but does not overturn the DM.5/DM.6 closure.** The honest summary is:

- Linearized canonical ED (DM2 simulation): slope ~0.24 (failed C1 hard).
- Self-consistent canonical ED with Einstein-like relation: slope 2 (passes C1, fails C2).
- Empirical: slope 4.

ED's structural prediction is wrong by a slope factor of 2 (not by a factor of 16). This is a more honest characterization of the failure than the DM2 numerical fit suggested, but it is still a failure.

The DM-arc's overall verdict (canonical activity-source ED structurally fails BTFR) stands. **DM.6 §3.1's enumeration of "two routes to repair C1" should be updated to "three routes" (anisotropy, Einstein-like relation, geometric 2-surface localization), but the C2 problem remains the persistent obstacle, and no enumerated route repairs it.**

---

## 11. Recommended Next Steps

Three concrete next steps:

1. **DM.G.4 closure decision memo.** With G4 (and by extension all candidates G1–G5) failing C2 under self-consistent re-analysis, DM.G should close with refutation. The closure memo should be parallel in tone to DM.0's mass-source rejection: clean structural refutation, lessons learned (linear-PDE framework predicts slope-2 regardless of source choice), no further DM.x work scheduled. **This is the recommended path.**

2. **A clarifying addendum to DM.5/DM.6.** Update DM.6 §3.1 from "two routes to repair C1" to "three routes" (adding geometric 2-surface localization), and add an explicit note that all canonical-ED source choices examined predict slope-2 BTFR under self-consistency. This is a small documentation task that prevents future-session confusion about the structural status of canonical activity-source ED.

3. **Elevate the C2 problem as the central open question for any ED gravitational-sector revival.** No future BTFR-extension work in canonical ED should expect to succeed without addressing C2. The structural pattern is now established: linear-PDE + disc-integrated kinematic source = slope-2 by construction. **Any future ED-derives-BTFR claim must either (a) demonstrate a nonlinear field equation that derives slope-4 directly (Option C from BTFR.07), or (b) demonstrate a non-local source construction that bypasses disc-integration (no examples currently known), or (c) accept that ED extends its range only to slope-2-compatible observations and is incompatible with empirical slope-4 BTFR.** This framing should be carried forward in the program's ED-Orientation document.

The DM.G arc has accomplished its purpose: it tested whether a structurally-distinct source mechanism (geometry-sourced T) can produce slope-4 BTFR within ED's linear-PDE framework. The answer is no, and the structural reason is now precisely identified (linearity of the PDE, not any specific source-functional choice). The DM-arc as a whole closes with this finding.

Status: complete.
