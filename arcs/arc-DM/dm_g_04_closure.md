# DM.G.4 — Closure and Structural Verdict for Geometry-Sourced T

**Date:** 2026-04-27
**Arc:** Dark Matter, sub-arc DM.G — closure memo
**Status:** **DM.G arc officially closed. Geometry-sourced T is refuted as a dark-matter-source hypothesis under ED's linear-PDE framework.** The full self-consistent asymptotic analysis (DM.G.2) showed that no canonical-ED source functional — geometric, kinematic, or hybrid — escapes the inner-disc M_b-linear dominance that produces slope-2 BTFR. The structural reason is precisely identified: in any linear PDE, the disc-integrated source is an additive sum over disc regions, and the Keplerian inner-disc contribution dominates the deep-T outer-disc contribution for any galaxy with a non-trivial baryonic core. **Only a nonlinear field equation can bypass this trap.** DM.G joins DM.0 (mass-source refuted) and DM.1 (linearized activity-source refuted) as a clean structural refutation. The C1 mechanisms identified during the arc (anisotropy, Einstein-like relation, geometric 2-surface localization) are *real structural insights* and remain valid even though C2 cannot be repaired within the linear-PDE class. The arc closes with the C2 problem precisely formulated as the central unresolved obstacle for ED's gravitational sector.
**Predecessor:** DM.G.2 (self-consistent asymptotic derivation, slope-2 verdict).
**Empirical anchor:** SPARC; canonical-ED merger-lag prediction at cluster scales (preserved).
**Successor:** None within DM.G. Forwarded items: clarifying addenda to DM.5/DM.6 (three C1 mechanisms; slope-2 as canonical structural prediction); the C2 problem as an open foundational question.

---

## 1. Summary of the DM.G arc

DM.G was launched (DM.G.0) following the closure of the canonical DM-arc (DM.5/DM.6) with FAIL on BTFR. The hypothesis: T is sourced not by mass density (DM.0, refuted) nor by kinematic activity (DM.1, refuted), but by **the intrinsic geometric structure of the baryonic disc itself**. Motivation: the user's Pringle/saddle intuition that disc geometry is structurally distinct from the spherical-and-isotropic source assumptions that failed in DM.0/DM.1.

### 1.1 DM.G.0 — Scoping

- Defined the hypothesis class precisely: T is sourced by S_geom(R, z) constructed from geometric scalars of the baryon distribution.
- Identified five candidate source functionals (G1–G5): density-gradient norm, mean curvature, Gaussian curvature, vorticity-shear saddle invariant, and disc extrinsic curvature.
- Established three structural tests (T1: M_b scaling; T2: dimensional/coordinate invariance; T3: cluster-regime behavior).
- Established success/falsifier criteria including slope-4 BTFR, no per-galaxy tuning, cluster preservation, no new fundamental constants, and foundational compatibility.

### 1.2 DM.G.1 — Candidate evaluation (linearized)

- Evaluated G1–G5 against T1, T2, T3 in the linearized framework.
- Results: G1 disqualified on T2 (dimensional); G2 and G3 disqualified on T3 (cluster non-vanishing) and T1 (wrong M_b scaling); G4 and G5 noted as partially surviving.
- Closed with a "no candidate cleanly survives" verdict and recommendation to consider closure.

### 1.3 DM.G.1b — Self-consistent re-evaluation (partial)

- Triggered by user observation that DM.G.1's analysis omitted the temporal-tension self-consistency identified in BTFR.08.
- Re-analyzed candidates with v_total² = v_baryon² + v_T² feedback.
- **Hopefully concluded** that G4 (vorticity-shear, equivalent to DM.1's activity index) survives self-consistent re-analysis with M_eff ∝ √M_b · log(M_b).
- Implied that DM.5/DM.6's FAIL verdict might be a linearization artifact and self-consistent canonical ED could produce slope-4 BTFR.

### 1.4 DM.G.2 — Full asymptotic derivation

- Worked through the self-consistent disc integral honestly, including both the inner regime (R < R_x, where v_baryon dominates) and the outer regime (R > R_x, deep-T).
- Found that DM.G.1b had analyzed only the outer-regime contribution; the inner-regime Keplerian contribution gives M_eff^{inner} ∝ M_b that *dominates* the outer M_eff^{outer} ∝ √M_b · log for any realistic galaxy.
- **Retracted DM.G.1b's "G4 survives" verdict.** Self-consistent canonical ED predicts slope-2 BTFR, not slope-4.
- Identified the structural obstacle as **linearity of the PDE combined with additive disc integration**, independent of the specific source functional.

---

## 2. The key structural finding

For canonical activity-source ED with self-consistent kinematic feedback and (provisionally) the Einstein-like relation D_T = c²·κ_act repairing C1, the disc-integrated effective charge takes the form:

> **M_eff = M_eff^{inner} + M_eff^{outer}**
>
> M_eff^{inner} ≈ (2π · κ_act · G / R_min) · M_b      (Keplerian inner disc)
>
> M_eff^{outer} ≈ 2π · κ_act · v_flat² · ln(R_max / R_x)      (deep-T outer disc)

The outer term is a self-consistency condition: v_flat² is itself proportional to M_eff_total, so M_eff^{outer} is a fraction of M_eff_total. Solving:

> **M_eff ≈ (linear in M_b) + O(√M_b · log)**

The leading scaling is M_b-linear. Plugging into v_T² = M_eff/(2π·κ_act) (log-kernel asymptotic under Einstein-like relation):

> v_T² ∝ M_b      ⟹      **v_T⁴ ∝ M_b² ⟹ slope-2 BTFR.**

The outer √M_b · log contribution is real but subdominant. It modifies the prefactor and introduces a slow logarithmic correction, but does not change the leading slope.

**No choice of source functional within the canonical-ED class produces slope-4 BTFR under self-consistent treatment.** The slope-2 verdict is robust to source-functional variation (G1–G5 plus their kinematic equivalents) and to whether the Einstein-like relation holds (without it, the failure is at C1, giving slope < 2; with it, the failure is at C2, giving exactly slope-2).

---

## 3. Why the failure is structural

### 3.1 The linearity-plus-disc-integration trap

ED's PDE is *linear* in T. Linearity means the field at any observation point is a sum of contributions from each source element:

> T(R_obs) = ∫ G(R_obs, R') · S(R') · dV'

The disc-integrated effective charge M_eff = ∫S · dV is the total source strength. Whatever S(R) looks like — built from ρ_b, |∇ρ_b|², H², |K|, |ω · σ|, |II|², or any other local functional — the disc integral is *additive over disc regions*.

For any galaxy with both a Keplerian inner disc and a deep-T outer disc, **the inner-disc activity contributes M_b-linear scaling and the outer-disc activity contributes √M_b · log scaling**. The inner contribution is finite (set by inner disc structure, R_min, baryon density, etc.) and proportional to M_b. The outer contribution is finite and proportional to √M_b. **For large galaxies the inner term dominates; for small galaxies the outer term may compete but cannot reverse the slope across 5 decades of M_b uniformly.**

This is the **linearity-plus-disc-integration trap**: linear PDEs cannot natively produce sublinear M_b scaling because the source itself, as an integrated quantity over a disc whose structure includes a Keplerian regime, has an irreducible linear-in-M_b component.

### 3.2 Independence from source functional choice

The trap operates independently of which specific source functional is chosen:

| Functional | Inner-disc scaling | Outer-disc scaling | Dominant slope |
|---|---|---|---|
| Mass density (DM.0) | M_b (trivially) | n/a (no kinematic suppression) | 2 |
| Activity / vorticity-shear (DM.1, G4) | M_b | √M_b · log | 2 (inner dominates) |
| Density gradient (G1) | M_b^{4/3} or M_b | n/a | wrong scaling regardless |
| Mean curvature (G2) | M_b^{1/3} or constant | n/a | wrong scaling regardless |
| Gaussian curvature (G3) | M_b/R_d² | n/a (Gauss-Bonnet topological lock) | wrong scaling regardless |
| Extrinsic curvature (G5) | ambiguous | ambiguous | undefined |

**No enumerated source functional produces leading-order √M_b scaling within the linear-PDE framework.** This is what "structural" means here: the failure is not about the source being too simple or wrongly chosen; it's about the linearity of the equation forbidding the required scaling behavior.

### 3.3 Independence from the C1 repair mechanism

Three mechanisms have been identified that repair C1 (logarithmic far-field of the kernel):

- **Anisotropy** (BTFR.06): postulated D_z/D_R ≲ 10⁻⁶, gives windowed-log behavior over galactic scales.
- **Einstein-like relation** (BTFR.08): D_T = c²·κ_act under self-consistency, cancels the cylindrical-curvature term, gives 2D-Cartesian Helmholtz with K_0 Green's function.
- **Geometric 2-surface localization** (DM.G.1, G3): source intrinsically concentrated on a 2-surface gives K_0 directly.

**All three mechanisms repair C1, but none repairs C2.** The slope-2 verdict applies under any of the three, because C2 is governed by the disc-integrated source, not by the kernel structure.

### 3.4 Independence from self-consistency vs linearization

The slope-2 verdict applies in both:

- **Linearized treatment** (DM2 simulation): activity built from v_baryon alone. Slope-0.24 in numerics due to additional C1 failure (no log kernel in cylindrical screened-Poisson). Asymptotic slope-2 if the kernel is repaired.
- **Self-consistent treatment** (DM.G.2): activity built from v_total = √(v_baryon² + v_T²). Inner-disc M_b-linear contribution still dominates. Asymptotic slope-2 even with all kernel repairs.

Self-consistency repairs the *shape* of rotation curves (gives flat outer regime) but not the *amplitude scaling* with M_b. The DM2 numerical slope is closer to the true structural prediction once self-consistency is folded in (slope-2 instead of slope-0.24), but the fundamental conclusion — ED structurally fails empirical slope-4 BTFR — does not change.

### 3.5 What would be required to bypass the trap

A nonlinear PDE. In MOND, the deep-MOND limit makes v_flat at radius R determined by **total enclosed M_b** through the nonlinear field equation:

> ∇·[μ(|∇Φ|/a₀)·∇Φ] = 4π·G·ρ_b    →    v² = √(G · M_enc · a₀)    in deep regime.

The nonlinear operator forces the asymptotic v_flat to depend on enclosed mass directly, not on source-distribution-integrated quantity. This is the structural feature ED's linear PDE lacks.

**Any future ED-derives-BTFR claim must therefore address the linearity obstacle directly.** Options that have been explored and remain available:

- (BTFR.07 Option C) Replace ED's linear screened-Poisson with a nonlinear operator analogous to MOND but sourced by activity. Major structural commitment; potentially affects Theorem N1 and GR.1.
- (Hypothetical) Find a non-local source construction that bypasses disc-integration. No examples currently known; structurally speculative.
- (Honest closure) Accept that ED's linear-PDE framework is incompatible with empirical slope-4 BTFR and accept the slope-2 prediction as a real but partial result.

---

## 4. Formal verdict

### 4.1 The verdict

> **DM.G is refuted.** Geometry-sourced T, in any of the candidate forms enumerated (G1 through G5) and under self-consistent treatment with all available C1-repair mechanisms, produces at best slope-2 BTFR. The empirical slope is 4. The structural obstacle is the linearity of ED's PDE combined with additive disc integration, not any specific feature of geometry-sourced T.
>
> **The C1 mechanisms identified during DM.G remain valid structural insights**, even though they do not yield BTFR by themselves:
>
> - Anisotropy (BTFR.06).
> - Einstein-like relation D_T = c²·κ_act (BTFR.08, conditional on foundational P2 reading from BTFR.09).
> - Geometric 2-surface localization (DM.G.1, conceptually clean for thin-disc sources).
>
> These three mechanisms are independent and any of them repairs the kernel structure that the canonical cylindrical screened-Poisson lacks.
>
> **The C2 obstacle is the central unresolved issue for ED's gravitational sector.** No source-functional choice within the linear-PDE framework produces M_eff ∝ √M_b. Resolving C2 requires either (a) demonstrating an ED-internal nonlinear field equation, (b) finding a non-local source construction, or (c) accepting slope-2 as ED's structural prediction and revising empirical expectations accordingly.

### 4.2 What DM.G accomplished

The arc was not a wasted exercise:

- **Identified a third C1 repair mechanism** (geometric 2-surface localization), expanding DM.6's "two routes" to "three routes."
- **Sharpened the structural diagnosis of the BTFR failure** from "canonical ED predicts slope-0.24" (linearized DM2 result) to "canonical ED predicts slope-2 robustly" (self-consistent DM.G.2 result). This is a more honest characterization.
- **Precisely localized the structural obstacle** to linearity-plus-additive-disc-integration. This is a sharper diagnosis than DM.5 had: it tells us which structural feature must change (linearity) and what the alternatives are (nonlinear field equation, non-local source).
- **Caught and corrected two methodological errors** (the linearization blind spot in DM.G.1, the partial-integration blind spot in DM.G.1b). This raises the standard for future ED structural-derivation work: linearization-artifact testing and full-integration verification should be default checks before any verdict.
- **Demonstrated that the user's Pringle/saddle intuition was structurally sound about C1** (geometry-sourced T does naturally repair the kernel structure) while showing that the same intuition does not extend to C2.

The arc closes with a clean refutation that is more informative than the DM.5/DM.6 closure was. The structural picture of ED's gravitational sector is now more precisely articulated.

---

## 5. Place in the ED program

### 5.1 DM.G in the DM-arc lineage

| Sub-arc | Hypothesis | Verdict | Structural reason |
|---|---|---|---|
| DM.0 | T sourced by ρ_b | Refuted | Wrong shape, no BTFR, magnitude shortfall ~10³ |
| DM.1 | T sourced by kinematic activity | Refuted (DM.5) | Slope-0.24 in numerics; structurally slope-2 (this memo) |
| DM.G | T sourced by disc geometry | Refuted (this memo) | Linearity-plus-disc-integration trap |

DM.0 was refuted at the source level (mass density doesn't give the right shape). DM.1 was refuted at the C1 + C2 levels under linearization, and at C2 only under self-consistency. DM.G is refuted at the C2 level under all C1-repair mechanisms. **All three sub-arcs converge on the same structural finding: linear-PDE ED with disc-integrated source does not produce slope-4 BTFR.**

### 5.2 Updates needed to DM.5/DM.6

The DM-arc closure memos should be updated to reflect:

- **Three C1 mechanisms**, not two (add geometric 2-surface localization).
- **Slope-2 as the canonical structural prediction**, with slope-0.24 identified as a linearization artifact of the DM2 simulation. The empirical FAIL is a slope-2 vs slope-4 mismatch, not a slope-0 vs slope-4 mismatch.
- **The C2 problem identified as the central unresolved obstacle**, with the linearity-plus-disc-integration diagnosis as its precise structural formulation.
- **Linearization-artifact testing and full-integration verification** as default methodological checks for future structural-derivation arcs.

These are clarifications, not retractions. The DM.5/DM.6 closure verdict (canonical ED fails BTFR; FAIL is structural; damage contained) stands. What changes is the precision of the structural diagnosis and the lessons-learned record.

### 5.3 Impact on other arcs

Unchanged after DM.G:

- **Arc R** (relativistic emergence): no impact.
- **Arc M** (matter-wave structure): no impact.
- **Arc N** (vacuum kernel, Theorem N1): no impact under linear-PDE class. *Conditionally affected* if a future ED revival pursues a nonlinear operator (Option C from BTFR.07).
- **Arc Q** (quantum sector): no impact.
- **Arc B** (Born-Gleason / foundations): no impact.
- **Phase 3 / GR (Theorem GR.1)**: no impact under linear-PDE class. *Conditionally affected* by Option C in the same way as N.
- **GR-SC** (curvature-invariant taxonomy): no impact.
- **Cluster-scale calibration** (D_T from merger-lag): unchanged; the BTFR failure is galactic-disc-specific.

The DM.G arc, like DM.0–DM.6 before it, leaves the foundational arcs and cluster calibration intact. The damage from canonical-ED-fails-BTFR is contained to the galactic-disc-dynamics prediction.

---

## 6. The honest status of ED after DM.G

> **ED is structurally consistent at the foundational level and produces a precise galactic-scale prediction (slope-2 BTFR with flat rotation curves under the Einstein-like relation) that is empirically wrong by a factor of 2 in slope.** This is a refutation of canonical ED's gravitational-sector prediction at galactic-disc scales, with the structural cause (linearity of the PDE) precisely identified.
>
> **Three independent paths are available for any future revival**: (a) extend ED with a nonlinear field equation that bypasses the linearity-plus-disc-integration trap (potentially affecting Arcs N and GR; major structural commitment); (b) discover a non-local source construction within ED's existing primitives (no examples currently known); (c) accept slope-2 as ED's structural prediction and find an alternative interpretation of the empirical slope-4 BTFR.
>
> **The universality result (DM.5 §3.2) survives** as the genuine ED-distinctive positive finding, modulo the optimizer-convergence caveat. ED's qualitative prediction of "no per-galaxy tuning" is preserved.
>
> **The ED program continues** on independent empirical and foundational tasks. The DM-arc and DM.G sub-arc are both formally closed.

---

## 7. Recommended Next Steps

Three concrete next steps for the ED program after DM.G closure:

1. **Update DM.6 and the program orientation document.** Add a single clarifying memo (DM.6.1 or an appendix to DM.6) that records: (i) three C1 mechanisms instead of two; (ii) slope-2 as canonical ED's structural prediction (replacing the slope-0.24 framing in DM.5); (iii) the linearity-plus-disc-integration diagnosis as the precise C2 obstacle; (iv) the methodological lesson about linearization-artifact testing. This is a small documentation task that prevents future-session confusion. **Recommended as immediate next step.**

2. **Pivot to non-DM-arc empirical work, with the merger-lag retrodiction as the first priority.** The DM-arc has fully exhausted its current structural questions. Empirical tests of ED's other predictions are independently motivated and can proceed without further DM-arc work. The merger-lag retrodiction (DM.6 §6.1, project_next_predictions) is the highest-priority next test: it probes ED's cluster-scale anchor independently of any galactic-scale extension and would either strengthen the cluster-scale prediction or expose a second empirical mismatch.

3. **Reserve the C2 problem as a foundational research question for a future Phase-2-style arc.** The "linearity-plus-disc-integration trap" is a precisely-formulated structural obstacle that deserves explicit foundational attention if-and-when ED's gravitational-sector revival is contemplated. Possible directions: examine whether ED's substrate physics admits a natively-nonlinear coarse-graining (Option C from BTFR.07); examine whether non-local source constructions (e.g., via path-integral or holographic-style derivations) can produce √M_b scaling in a linear PDE; or accept the slope-2 prediction and examine whether any subset of empirical galactic-scale phenomena is consistent with it (some early-universe galaxies, ultra-faint dwarfs, etc., where slope-4 BTFR is less well-tested). **Not scheduled; held as a forwarded structural-research item.**

The DM.G arc has delivered its honest result. The DM sub-arcs (DM.0, DM.1, DM.G) collectively close with three independent refutations, all converging on a single structural diagnosis: ED's linear PDE cannot derive empirical slope-4 BTFR regardless of source choice. The path forward for ED's gravitational sector — if there is one — requires structural commitments beyond the linear-PDE class.

Status: complete.
