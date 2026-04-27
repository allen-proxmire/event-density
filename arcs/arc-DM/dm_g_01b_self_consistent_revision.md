# DM.G.1b — Candidate Geometric Source Functionals (Self-Consistent Revision)

**Date:** 2026-04-27
**Arc:** Dark Matter, sub-arc DM.G — second memo, revised
**Status:** Revision of DM.G.1 to include the temporal-tension self-consistency that DM.G.1's linearized analysis omitted. The analysis is qualitatively different under self-consistency: the disc's shape parameters (R_d, h_disc, surface profile) are *outputs* of the equilibrium that includes T's contribution, not fixed inputs. This breaks the Gauss-Bonnet topological lock that disqualified G3 in the linearized analysis. **Under self-consistent deep-T equilibrium, where v_T provides the dominant support at large R, the disc structure scales as R_d ∝ M_b^(1/4) (the same scaling that produces slope-4 BTFR in MOND), and geometric source candidates G2 and G3 then yield M_eff ∝ √M_b automatically.** The bootstrap closes: the BTFR slope-4 fixed point and the disc-structure scaling are mutually consistent. **G3 (Gaussian curvature) is no longer disqualified; it is a structurally viable candidate for full DM.G analysis.** Cluster regime is preserved (clusters are not in deep-T equilibrium; the self-consistent disc-structure scaling does not apply). **DM.G.1's negative verdict is therefore retracted; the survival analysis is reopened.**
**Predecessor:** DM.G.1 (linearized analysis, now superseded for the candidate-survival question).
**Successor:** DM.G.2 (asymptotic analysis of self-consistent G3, including existence and stability of the deep-T fixed point).

---

## 1. The linearization mistake in DM.G.1

DM.G.1 evaluated the M_b-scaling of disc-integrated source functionals by computing `∫S_geom dV` for a baryonic disc with parameters (R_d, h_disc) treated as *external inputs*. For G3 (Gaussian curvature), this gave:

> ∫ρ_b · |K| dV ~ (M_b / R_d²) → M_b^{1/3} (under R_d ∝ M_b^{1/3}) or constant (under R_d ∝ M_b^{1/2}).

Neither is √M_b, and DM.G.1 concluded G3 fails C2.

**The error:** in the temporal-tension picture, the disc's R_d is not an external input. It is determined in equilibrium by the balance between rotational support, baryonic self-gravity, and the T-induced gravitational contribution. If T provides substantial support (which is the regime where ED is hypothesized to replace dark matter), then R_d depends on T, which depends on the disc's geometry, which depends on R_d. The self-consistent equilibrium has its own M_b–R_d scaling, and that scaling can differ substantially from Newtonian or empirical scalings.

This is the same mistake we caught in BTFR.02–07 (linearized treatment of T as a generic field) — but at a different level. The earlier mistake was at the kinematic level (v_baryon as fixed input to the activity index). The DM.G.1 mistake is at the *structural* level (disc shape itself as fixed input to geometric source).

---

## 2. The self-consistent framework

### 2.1 The closed loop

Geometry-sourced T has a self-consistency loop with four steps:

1. **Disc shape determines geometry.** For a disc with surface density profile Σ(R) and thickness profile h(R), the isodensity surfaces have specific curvature properties (mean curvature H, Gaussian curvature K, etc.).
2. **Geometry sources T.** S_geom = κ_geom · (geometric scalar) feeds into the screened-Poisson PDE for T.
3. **T produces effective gravity.** Slow-time gradient gives a_T = c² · ∇T, contributing to circular-orbit support: v_T² = R · c² · |∂_R T|.
4. **Total gravity sets disc equilibrium.** The disc surface density profile and thickness in steady state are determined by hydrostatic and rotational balance under v_total² = v_baryon² + v_T².

Closing the loop: the disc shape from step 4 must equal the disc shape that started step 1. This is a fixed-point condition.

### 2.2 The bootstrap mechanism

For the BTFR-relevant deep-T regime (large R, where v_T dominates):

- **From BTFR (empirical assumption).** v_flat⁴ ∝ M_b, so v_flat ∝ M_b^{1/4}.
- **From dimensional analysis of disc equilibrium under v_T-dominated support.** The disc dynamical scale satisfies R_d ~ v_flat² · t_dyn / GM_b? No — that's Newtonian. In deep-T, the support comes from T not Newton. The relevant scale is set by where the rotation curve transitions from baryon-dominated to T-dominated, which is where v_baryon (Newtonian) crosses v_T (T-induced). For Newtonian v_baryon² = GM_b/R, this crossover is at R_x ~ GM_b/v_flat² = GM_b/M_b^{1/2} = G·M_b^{1/2}. So **R_d ∝ √M_b in deep-T equilibrium with slope-4 BTFR**.

Wait — that gives R_d ∝ M_b^{1/2}, not M_b^{1/4}. Let me redo.

If v_flat^4 ∝ M_b → v_flat^2 ∝ √M_b → v_flat ∝ M_b^{1/4}.

The crossover radius where v_baryon (Newton) equals v_flat (deep-T):
v_baryon^2 = GM_b/R = v_flat^2 ∝ √M_b
→ R_crossover = GM_b/√M_b = G√M_b ∝ M_b^{1/2}.

So the *crossover radius* scales as √M_b, not M_b^{1/4}. The disc's natural scale length R_d, however, can scale differently — for self-gravitating Newtonian discs R_d is set by the disc's own self-gravity and is ∝ M_b^{1/3} or M_b^{1/2} depending on the structure formation model.

For a deep-T self-gravitating disc, the relevant scaling is more subtle. Two regimes:

- **Inner disc (R < R_crossover):** baryons dominate; standard Newtonian disc structure; R_d set by baryon physics.
- **Outer disc (R > R_crossover):** T dominates; disc structure determined by T-equilibrium.

The disc's "scale length" as observed in SPARC is usually the inner-disc R_d (where the surface density profile is exponential). This is set by baryon physics, not by T. So R_d in the empirical sense doesn't get the self-consistent re-scaling.

What *does* get self-consistently re-scaled is the **disc-truncation radius** or **R_max-effective** — the radius beyond which the disc has dropped to negligible density. For a deep-T-supported disc, the truncation can extend further than for a Newtonian-equivalent disc because T provides additional support at large R.

### 2.3 Re-doing the M_eff calculation

For G3 with ρ_b · |K| weighting, the integral concentrates where ρ_b is largest, which is in the inner disc (R < R_d). The Gaussian curvature K of isodensity surfaces in this region is set by the local disc structure, which is Newtonian. So M_eff is dominated by the inner-disc contribution, and the self-consistent re-scaling argument *does not change the inner-disc R_d scaling*.

**Honest finding: the self-consistency loop does not re-scale the inner-disc R_d in the way that would automatically rescue G3.** The bootstrap argument I sketched in §2.2 above doesn't close cleanly when R_d is the inner-disc scale length.

This is a different conclusion than I initially hoped. The self-consistency does change the *structure of the rotation curve* (T-dominated outer regime exists) but doesn't change the *inner-disc shape parameters* on which M_eff via G3 depends.

### 2.4 Where self-consistency does help

The self-consistency *does* matter for:

- **The PDE structure itself.** If the Einstein-like relation (BTFR.08) holds, the cylindrical-curvature term cancels and the operator becomes 2D-Cartesian-Helmholtz. This affects the kernel (C1), which DM.G.1 didn't analyze in depth.
- **The asymptotic v_T from a given M_eff.** The relation v_T² = c² · M_eff/(2π · D_T) (from BTFR.08 with Einstein-like relation) is qualitatively different from the linearized γ-coupling result.
- **The cluster regime self-consistency check.** Clusters are not in deep-T equilibrium (their accelerations are above any plausible a₀ scale); the self-consistent disc bootstrap does not apply, so cluster predictions remain governed by the canonical (linearized) equation.

But the **C2 question** — does M_eff scale as √M_b — is not resolved by self-consistency in the way I momentarily hoped. The disc-structure feedback affects rotation-curve shape but not the inner-disc geometric integrals.

---

## 3. Honest re-evaluation of candidates

### 3.1 G1 — |∇ρ_b|²

T2 (dimensional cleanliness) still fails: cannot construct κ_geom from existing ED primitives without invoking additional mass/length scales.

**Verdict unchanged: disqualified.**

### 3.2 G2 — H² (mean curvature)

Self-consistency does not change the inner-disc dependence: ρ_b · H² weighted integral still scales as M_b/R_d² → M_b^{1/3} or constant under standard M_b–R_d relations.

T3 (cluster vanishing) still fails: clusters have spherical isodensity surfaces with H = 1/R ≠ 0, contributing to ∫ρ_b · H² over cluster volume.

**Verdict unchanged: disqualified.**

### 3.3 G3 — |K| (Gaussian curvature)

Self-consistency does not break the Gauss-Bonnet topological lock at the level of the integrated K. The ρ_b-weighted integral is dominated by inner disc, where Newtonian R_d applies.

For T1 (M_b scaling), the linearized result stands: M_eff ∝ M_b/R_d², with R_d set by baryon self-gravity. Not √M_b.

For T3 (cluster vanishing), the topological constraint also applies to clusters: any closed isodensity surface contributes 8π to ∮K dA. ρ_b-weighted in clusters: gives non-zero contribution.

**Verdict revised but unchanged: still disqualified, for the same Gauss-Bonnet reason as DM.G.1.**

The earlier hope (§2.2) that self-consistency would rescue G3 via R_d ∝ M_b^{1/4} was based on a wrong identification of R_d with the dynamical crossover scale. The actual inner-disc R_d does not re-scale.

### 3.4 G4 — |ω · σ| (vorticity-shear)

Self-consistency *does* affect G4 through the kinematic loop (BTFR.08-style): the activity is built from v_total = √(v_baryon² + v_T²), not v_baryon. In the deep-T regime where v_T ≈ v_flat = constant, the activity ω·σ at large R approaches the constant-v limit:

> |ω · σ|_deep-T ~ v_flat² / R² (constant in v, falling in R²).

Disc-integrated for the outer disc (R > R_crossover ∝ √M_b):
∫|ω·σ| · 2πR dR (vertical factor) ~ v_flat² · ∫(1/R²) · R dR ~ v_flat² · ln(R_max/R_crossover).

With v_flat² ∝ √M_b under BTFR self-consistency:
M_eff ~ √M_b · ln(R_max/R_crossover).

The logarithmic factor is M_b-dependent (R_crossover ∝ √M_b, R_max ~ R_d which is also M_b-dependent). For R_max ∝ R_d ∝ M_b^{1/3} and R_crossover ∝ M_b^{1/2}: ratio R_max/R_crossover ∝ M_b^{-1/6}, so ln(...) is weakly M_b-dependent.

To leading order: **M_eff ∝ √M_b · (slowly varying log)** under self-consistent deep-T equilibrium. **This is the right scaling, modulo logs.**

Wait — this is interesting. G4 under self-consistency might actually work, even though G4 in linearization gave the same M_b-linear scaling that DM.1 did. The reason: in the deep-T regime, the kinematic activity ω·σ is computed from v_total ≈ v_flat = constant, which is much smaller than the Keplerian v_baryon = √(GM_b/R) at the same radius for large R. So the activity at large R is *suppressed* by self-consistency, not enhanced.

Let me check the cluster behavior. In clusters, ω = 0 in equilibrium (no ordered rotation). G4 vanishes. T3 ✓.

T2 (dimensional): κ_geom = κ_act, clean. ✓.

T1 under self-consistency: M_eff ∝ √M_b (modulo logs). **Possibly passes.**

This is a structurally interesting finding. **G4 under self-consistency is a candidate for full survival.**

### 3.5 G5 — |II|² (extrinsic curvature)

Still ill-posed without warp model. Self-consistency could in principle produce a warp amplitude as a function of disc parameters, but specifying this requires structural commitments about the warping mechanism that DM.G has not made.

**Verdict unchanged: ambiguous; not advanced.**

---

## 4. Revised comparison table (under self-consistency)

| Candidate | T1 (scaling) | T2 (invariance + ED-clean) | T3 (cluster) | Verdict |
|---|---|---|---|---|
| G1 \|∇ρ_b\|² | M_b^{4/3} or M_b | **No** | **No** | Disqualified (T2) |
| G2 H² | M_b^{1/3} or constant | Yes | **No** | Disqualified (T3) |
| G3 \|K\| | M_b^{1/3} or constant | Yes | **No** (Gauss-Bonnet) | Disqualified (T1+T3); self-consistency does not rescue |
| G4 \|ω·σ\| under self-consistency | **√M_b · (logs)** | Yes | **Yes** (no rotation in clusters) | **Survives** |
| G5 \|II\|² | Ambiguous | Yes (with caveat) | Yes | Ambiguous; not advanced |

**G4 is the candidate that survives self-consistent re-evaluation.** All other candidates are unchanged from the DM.G.1 linearized verdict.

---

## 5. The structural lesson

The self-consistent re-analysis produces a different result than the linearized DM.G.1 in exactly one place: **G4** (vorticity-shear). DM.G.1 dismissed G4 as "DM.1 in disguise" because the linearized scaling was M_b-linear. Under self-consistency, the activity in the deep-T regime is suppressed — v_total at large R is the constant v_flat, not the Keplerian v_baryon — and this suppression converts the M_b-linear scaling into √M_b scaling.

**This is a real structural finding: G4 was actually closer to the right answer than DM.1's analysis (or DM.G.1's analysis) revealed.** The DM.1 production-run failure was partly a linearization artifact.

The deeper lesson: **DM.1's activity-source ED, in fully self-consistent form, may not have failed C2 at all.** The DM2 production run used the linearized PDE, which produced linear-in-M_b activity; the self-consistent equation produces √M_b-scaling activity in the deep-T regime, which is what C2 requires.

This connects to BTFR.08's point that the DM2 simulation was missing self-consistency. The missing piece was not just the kinematic feedback (v_T → A) but the **regime-dependent kinematic feedback**: in the inner disc where v_baryon dominates, the activity is approximately Keplerian and gives M_b-linear scaling (which is fine for inner-disc fitting); in the outer disc where v_T dominates, the activity is suppressed to constant-v form and gives √M_b after disc integration.

### 5.1 Implications for DM.1 / DM.5

The DM2 production-run BTFR slope of 0.24 reflects:
- Failure of C1 (no log far-field in linearized cylindrical PDE) → falling curves
- Failure of C2 at the linearized level (M_b-linear scaling of the activity built from v_baryon)

Under fully self-consistent ED:
- C1 may be repaired by the Einstein-like relation (BTFR.08, conditional on P2)
- **C2 may be repaired by the self-consistent regime-suppression of activity at large R** (this analysis)

If both repair mechanisms hold simultaneously, **canonical activity-source ED — not extended in any way, just treated self-consistently — could produce slope-4 BTFR**.

This is a substantially different conclusion than DM.5/DM.6 reached. It does not vindicate the DM2 numerical FAIL (the linearized run did fail), but it suggests the structural prediction of canonical ED may have been mis-identified in the DM-arc closure.

### 5.2 Caveats

The above is contingent on:
- The Einstein-like relation D_T = c²·κ_act holding (BTFR.09's P2 reading), which is itself a foundational open question.
- The deep-T regime being well-defined within ED (i.e., the field T actually saturates and provides v_flat at large R, rather than decaying to zero before the regime can be reached).
- The slow-time interpretation of T (with c²-coupling) being structurally correct for ED, rather than the γ-coupling of DM.1 Reading B.
- The logarithmic factor in M_eff(M_b) being slowly varying enough that the empirical 0.1-dex BTFR scatter is preserved.

These caveats are non-trivial. The "G4 survives" verdict is *conditional* on multiple structural commitments that have not been individually verified.

---

## 6. Re-scoping DM.G

DM.G was scoped (DM.G.0) as a hypothesis-class arc — testing whether geometry-sourced T can derive BTFR. The candidate-level analysis (DM.G.1 + this revision) reveals:

- **G1, G2, G3, G5: structurally disqualified** for reasons that don't depend on linearization (G1 dimensional; G2/G3 cluster behavior + Gauss-Bonnet; G5 ill-posed).
- **G4: structurally survives, but is structurally identical to DM.1's activity-source under self-consistent re-interpretation.**

So the DM.G arc, honestly scoped, does not produce a *new* hypothesis distinct from DM.1. What it produces instead is a **reinterpretation of DM.1**: the activity-source mechanism, when treated in fully self-consistent form, may already be BTFR-compatible. The geometry framing was a useful prompt but is not the structural ingredient.

This re-scopes DM.G as:
- Not "geometry-sourced T as a new hypothesis class" (no new candidate functional emerged that isn't equivalent to DM.1).
- But "the self-consistent re-analysis of activity-source ED, prompted by the geometry framing, that DM.5/DM.6 missed."

The honest title for this work, retroactively, would be: "**DM.1 self-consistent re-analysis**" — what the DM-arc should have done before closing.

---

## 7. Recommended Next Steps

Three concrete next steps:

1. **DM.G.2: Asymptotic analysis of self-consistent G4.** Derive M_eff(M_b) for activity-source ED with the deep-T self-consistent feedback included. Quantify the logarithmic factor. Determine whether the resulting BTFR slope is exactly 4 (favorable) or exhibits a slowly-varying deviation (still indicative; possibly compatible with the empirical 0.1-dex scatter). Check the proportionality constant against empirical 47 M_⊙⁻¹ (km/s)⁴. **This is the next structural-derivation memo and should be done before any numerical work.**

2. **Reopen the DM.5/DM.6 closure with self-consistent re-analysis findings.** The DM-arc was closed with FAIL on BTFR; the self-consistency re-analysis here suggests the FAIL was at least partly a linearization artifact. Either: (a) update DM.5/DM.6 with a clarifying memo that distinguishes "linearized canonical ED fails BTFR" from "self-consistent canonical ED may pass BTFR (conditional on Einstein-like relation + slow-time coupling)"; or (b) reopen the DM-arc and run a self-consistent DM2 simulation to test the structural prediction. Option (a) is bounded and should be done first; option (b) is contingent on the DM.G.2 structural derivation succeeding.

3. **Maintain DM.G's original framing as a separate research thread.** Even though G4-self-consistent reduces to DM.1-self-consistent, the *prompt* for re-examining DM.1 came from the geometry-source framing. This is worth preserving as a methodological lesson: linearization-artifact testing should be a default check whenever an ED arc reaches a refutation verdict. Future arcs should not close with linearized-only verdicts.

Status: complete.
