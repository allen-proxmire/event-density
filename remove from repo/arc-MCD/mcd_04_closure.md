# MCD.4 — Closure and Structural Verdict for Many-Chain Dynamics

**Date:** 2026-04-27
**Arc:** Many-Chain Dynamics — closure memo
**Status:** **MCD arc officially closed. Many-chain dynamics with the path-of-easiest-updating principle is refuted as a mechanism for deriving slope-4 BTFR.** The single-chain principle (A1.c ≡ A5) is mathematically equivalent to GR's geodesic principle in slow-time vocabulary; it adds no new physics over GR at the single-chain level (MCD.1). The many-chain limit, derived variationally from a canonical Lagrangian construction (quadratic kinetic, quadratic potential, BTFR.08-self-consistent activity coupling), produces a linear field equation for T — recovering the canonical-ED screened-Poisson PDE (MCD.2). The substrate-level analysis confirms that none of the three nonlinearity routes (non-quadratic kinetic term, non-quadratic potential, tensor-gravity structure) is forced by ED's currently-articulated primitives (MCD.3). **MCD is the third independent arc to converge on the same structural wall** (DM.1, DM.G, MCD), strengthening the program-level finding that the linearity wall is robust and not contingent on any specific source-functional or action-principle choice. The arc closes with refutation, the C1 mechanisms identified during MCD.1's eikonal analysis remain valid structural insights, and three foundational research questions are formally elevated to a separate substrate-foundations arc.
**Predecessor:** MCD.3 (substrate-derivation analysis with negative verdict).
**Empirical anchor:** SPARC (BTFR slope-4); cluster merger-lag (preserved).
**Successor:** None within MCD. New arc to be opened: "ED-Substrate Foundations" (working title), addressing the three foundational questions surfaced in §6.

---

## 1. Summary of the MCD arc

The MCD arc was launched following the closure of the canonical DM-arc (DM.0–DM.6) with FAIL on BTFR. The motivating intuition: the DM-arc treated ED as a continuum field theory (linear PDE with smeared kinematic source) and hit a structural wall (linearity-plus-disc-integration trap). MCD reframed the problem at the substrate level: chains are the primitive dynamical objects, and many-chain dynamics is the collective behavior that emerges when multiple chains shape and are shaped by the substrate. The hope was that this reframing would reveal an intrinsic nonlinearity in the many-chain continuum limit, providing the structural ingredient needed for slope-4 BTFR.

### 1.1 MCD.0 — Scoping

Defined the core question: what does "path of easiest updating" mean in ED, and how does the principle extend from single-chain to many-chain regimes? Identified six candidate readings of the principle (A1–A6) and five structural criteria (C1–C5). Established that MCD.3 would be the structural pivot: whether the many-chain coupling produces nonlinearity. Anchored the arc to ED-07's existing principle of least disruption (§5.1), GR-3A's eikonal-limit geodesic result, and the lessons from BTFR.01–09 and DM.G about linearization-artifact testing.

### 1.2 MCD.1 — Candidate action principles

Surveyed A1–A6 against the structural criteria. **Found that A1.c (cost minimization with U = 1−T) and A5 (geodesic on slow-time metric) are mathematically unified**: both reduce to GR's standard free-particle action `S = -mc²·∫dτ_proper` in slow-time vocabulary. **At the single-chain level, the path-of-easiest-updating principle is GR's geodesic principle in different language, with no new content.** The genuine novelty must therefore live entirely in the many-chain extension. A2 (curvature minimization) was structurally restrictive; A3 (entropy maximization) required substrate commitments not in ED-07; A4 (Lagrangian framework) was selected as the embedding for A1+A5; A6 (hybrids) were too open-ended.

### 1.3 MCD.2 — Variational derivation of the field equation

Derived the chain equation of motion (recovers `a = −c²·∇T`, the slow-time Newtonian limit and GR-3A geodesic in eikonal regime) and the field equation for T from the canonical Lagrangian. **Key result: under quadratic kinetic term, quadratic potential, and linear-in-v_T² activity coupling, the field equation is linear in T.** The resulting equation reproduces the canonical-ED PDE up to the BTFR.08 cylindrical-curvature cancellation. Many-chain coupling enters as a linear superposition of chain mass densities (`c²·ρ_chain`) sourcing T; the field equation given a chain configuration is linear, even though the full dynamical system (chains evolving on a field they collectively source) is nonlinear in chain configurations. **The DM-arc linearity wall reappears at the field-equation level.**

Three escape routes were identified: N1 (non-quadratic kinetic term, MOND-style), N2 (non-quadratic potential V(T)), N3 (tensor-gravity beyond weak-field). Each could produce nonlinearity if adopted, but adoption would be postulation rather than derivation.

### 1.4 MCD.3 — Substrate-level analysis

Examined whether ED's substrate physics forces any of N1, N2, N3. **Honest verdict on each:**

- **N1**: allowed but suppressed at galactic scales by EFT power-counting (factor ~10⁻⁶³). Three speculative escape routes exist but none is in the ED canon.
- **N2**: allowed and weakly motivated by GR-convention parallels (logarithmic ρ-T relationship), but produces *perturbative-in-T* nonlinearity, not the *non-perturbative-in-(∇T)* nonlinearity required for MOND-like deep-regime behavior. **Wrong type of nonlinearity.**
- **N3**: allowed (probably required for full ED-GR consistency in strong-field), but irrelevant to weak-field galactic-scale BTFR.

**None of the three is forced by ED's currently-articulated substrate primitives.** Of the three, only N1 has the right *type* of nonlinearity for slope-4 BTFR, but it is suppressed by 63 orders of magnitude at galactic scales.

---

## 2. The core structural finding

> **Single-chain ED = GR geodesic in slow-time language.** No new physics; clean structural reproduction.
>
> **Many-chain ED with canonical Lagrangian = linear screened-Poisson PDE.** Reproduces canonical-ED gravitational-sector equation; same DM-arc result follows.
>
> **Substrate physics does not force any of the three nonlinearity routes (N1, N2, N3).** Either the route is not forced (N1, N2), is wrong type (N2), or is irrelevant to galactic scales (N3).
>
> **Therefore: MCD does not produce nonlinear emergent gravity within ED's currently-articulated framework.** The path-of-easiest-updating principle is structurally clean and consistent, but it does not, by itself, provide the deep-regime nonlinearity required for empirical slope-4 BTFR.

The arc has answered its central question: many-chain dynamics, taken at face value, does not escape the DM-arc linearity wall. The wall is not an artifact of source-functional choice (DM.0 mass-source vs DM.1 activity vs DM.G geometry); it is a structural feature of ED's PDE form combined with disc-integrated source aggregation. **The wall is robust to changes in source choice, action-principle choice, or many-chain coupling structure — under the canonical-ED Lagrangian.**

---

## 3. Three-arc convergence

This is the **third independent arc** to reach the same structural verdict:

| Arc | Hypothesis | Failure mode | Failure level |
|---|---|---|---|
| **DM.1** | T sourced by kinematic activity | C2 fails: M_eff ∝ M_b under self-consistency | Linear PDE + Keplerian inner-disc dominance |
| **DM.G** | T sourced by disc geometry (G1–G5) | C2 fails: same trap; G3 hits Gauss-Bonnet topological lock | Linear PDE + disc-integrated source |
| **MCD** | Path-of-easiest-updating action principle | Canonical Lagrangian produces linear field eq; substrate doesn't force nonlinearity | Linear PDE forced by Lagrangian quadratic structure |

**Three structurally-independent attacks have converged on the same wall.** The convergence is informative:

- **The linearity wall is not contingent** on any specific source-functional choice. Mass, activity, geometry, action-principle — all yield linear field equations under the canonical Lagrangian construction.
- **The linearity wall is not contingent** on linearization-vs-self-consistent treatment. Self-consistent treatment (BTFR.08, DM.G.2) modifies the kernel structure but does not introduce nonlinearity in T.
- **The linearity wall is structural to ED's PDE form**, not to any of the specific arc hypotheses. ED's gravitational-sector equation, derived from the canonical Lagrangian construction, is linear in T.

**The structural reason is now precisely identified:** the canonical Lagrangian's quadratic kinetic term and quadratic potential give a linear field equation. Many-chain coupling is linear in chain mass density. Disc-integrated source has an irreducible M_b-linear inner-disc contribution that dominates any √M_b outer-disc contribution. The result is slope-2 BTFR (or worse, under non-self-consistent linearization), regardless of source-functional choice.

This is the three-arc convergence finding: **ED's currently-articulated gravitational sector is structurally linear, and slope-4 BTFR is structurally inaccessible without an additional foundational commitment beyond what the current canon provides.**

---

## 4. Formal verdict

### 4.1 The verdict

> **MCD is refuted as a mechanism for deriving slope-4 BTFR.** The path-of-easiest-updating principle, formalized through the unified A1.c+A5 single-chain action embedded in the A4 Lagrangian framework, produces a linear field equation for T at the many-chain level. The substrate-derivation check confirms that no nonlinearity route is forced by ED's currently-articulated primitives.
>
> **The gravitational sector of ED, as currently articulated, is structurally linear.** This is now established at three independent levels: source-functional (DM.0/1/G), action-principle (MCD.1–2), substrate-physics (MCD.3). The convergence across three arcs makes the verdict robust.
>
> **Any future nonlinear emergent gravity in ED must come from new substrate principles, not from many-chain dynamics alone.** MCD has exhausted what can be derived from ED's existing canon. Further progress requires foundational extension.

### 4.2 What MCD accomplished

The arc was not a wasted exercise:

- **Confirmed that the path-of-easiest-updating principle is GR-equivalent at the single-chain level.** This is a positive structural finding: it means ED's principle of least disruption is consistent with GR's geodesic principle, with no contradiction. The structural marriage between ED's substrate ontology and GR's geodesic dynamics is clean.
- **Derived the chain equation of motion explicitly** from the slow-time action `S = -mc²∫(1−T)dt`. The Euler-Lagrange result `a = −c²·∇T` is now established as the canonical ED-substrate-derived equation of motion, recovering Newtonian gravity in the limit of small T.
- **Established the canonical Lagrangian construction** for ED's gravitational sector: `L = (1/2)(∇T)² − V(T) − κ_act·A(x,T) + c²·ρ_chain·T`. This Lagrangian is the canonical-ED equivalent in field-theoretic form.
- **Identified the three nonlinearity routes precisely** and analyzed each against substrate physics. Future work on ED's gravitational sector now has a clean structural map: any nonlinear extension must come through one of N1, N2, N3 (or a new N4 from ED-07 §5.1 criteria b/c), and the structural status of each route is now documented.
- **Strengthened the three-arc convergence finding.** The DM.1 + DM.G + MCD pattern establishes the linearity wall as a robust structural feature, not an artifact of any specific arc's hypothesis.
- **Maintained methodological discipline.** The lessons from BTFR.01–09 (linearization-artifact testing, full-integration verification, conditional-results labeling) were carried forward consistently. No mid-arc verdict reversals were needed. The arc closed cleanly with the verdict it derived.

---

## 5. What remains intact

> **The MCD verdict refutes only the gravitational-sector slope-4 BTFR derivation. It does not affect ED's foundational structure.**

### 5.1 Foundational arcs preserved

| Arc | Status after MCD |
|---|---|
| **R** (relativistic emergence: KG, Dirac, spin-statistics, g=2) | Unaffected |
| **M** (matter-wave structure, σ_τ form) | Unaffected |
| **N** (vacuum kernel, Theorem N1: V1 finite-width) | Unaffected |
| **Q** (quantum sector: GRH, UV-FIN, canonical commutation) | Unaffected |
| **B** (Born-Gleason / measurement foundations) | Unaffected |
| **GR / Phase-3** (Theorem GR.1: V1 with Synge world function) | Unaffected; in fact strengthened (MCD.1's confirmation that single-chain ED is GR-equivalent in slow-time gives GR.1 a cleaner derivational foundation) |
| **GR-SC** (curvature-invariant taxonomy) | Unaffected |
| **RG** (Wilsonian three-regime structure) | Unaffected |
| **ED-SC 3.x** (cross-scale invariance) | Unaffected |

### 5.2 Cluster-scale calibration preserved

The cluster merger-lag prediction that anchors D_T and λ is unaffected by MCD's verdict. Cluster-scale geometry is roughly 3D-isotropic and the deep-acceleration regime (where the BTFR.07 distinction between Newton and MOND lives) does not apply at cluster scales. MCD's linear field equation is the canonical-ED equation, which reproduces the cluster anchor by construction.

### 5.3 Universality of κ_act preserved (provisional)

The DM2 production-run finding `σ(κ_act)/mean ≈ 2.1%` (DM.5 §3.2) survives MCD. The optimizer-convergence caveat (max_evals = 50 was reached in the DM2 run) remains, but no MCD analysis has invalidated the universality finding. ED's qualitative prediction of "no per-galaxy tuning" remains a positive feature distinct from per-halo-tuned dark-matter fits and from environment-dependent MOND variants.

### 5.4 The c·H₀ ≈ a₀ coincidence as an open structural clue

BTFR.09 §3.1 noted that the dimensional combination `c·λ ≈ c·H₀ ≈ 7 × 10⁻¹⁰ m/s²` is within a factor of ~6 of MOND's `a₀ ≈ 1.2 × 10⁻¹⁰ m/s²`. This combination uses ED's existing primitives (c implicit in slow-time, λ from cluster-scale screening) without new constants.

**Whether this proximity is coincidence or a genuine structural prediction of ED is an open foundational question.** If it can be promoted from "numerical coincidence" to "structural derivation" — i.e., if ED's substrate physics produces a₀-scale nonlinearity through some mechanism that uses c·λ as the natural scale — then ED gains a structurally-clean MOND-equivalent without requiring postulated machinery. This is not within MCD's scope but is one of the foundational questions elevated in §6.

---

## 6. Elevated foundational research questions

Three open questions surface across the BTFR sub-arc, DM.G arc, and MCD arc that exceed the scope of any single source-functional or action-principle arc. They belong at the substrate-foundations level. **MCD.4 formally elevates them to a new arc.**

### 6.1 Q1 — Substrate-level ρ-T relationship

ED-07 articulates ρ (event density / becoming rate) and T (slow-time field) as related but does not give an explicit functional form `T = T(ρ)` or `ρ = ρ(T)`. MCD.3 §4 noted that the choice between linear (R1), logarithmic (R2), or power-law (R3) relationships has structural consequences for whether N2 (non-quadratic V(T)) is allowed, weakly motivated, or strongly motivated.

**Research question Q1:** What does ED's substrate physics imply for the ρ-T relationship? Is there a structural derivation from ED's micro-event substrate that selects (R1), (R2), (R3), or some other form?

This is foundational substrate-physics work, parallel in flavor to BTFR.10's question about D_T's substrate origin. A positive result might unlock N2 (or a related non-trivial-V mechanism) as a structurally-derived rather than postulated feature.

### 6.2 Q2 — Structural status of c·H₀ ≈ a₀

The numerical coincidence between `c·λ ≈ c·H₀` (an ED-internal combination) and MOND's a₀ (an empirical galactic-scale acceleration constant) is suggestive but not currently structural.

**Research question Q2:** Can ED's substrate physics promote c·H₀ from a numerical coincidence to a structural prediction? Specifically: is there a mechanism by which ED's substrate gives this combination the role MOND assigns to a₀ (the boundary between Newtonian and deep-MOND regimes)?

A positive result would give ED a derived MOND-equivalent without postulating an a₀-weighting interpolation function. This connects to BTFR.07's Route II-A and to the BTFR.09 P2 reading of the Einstein-like relation.

### 6.3 Q3 — Mathematical content of ED-07 §5.1 (b) and (c)

ED-07 §5.1 articulates three criteria for an inertial path: (a) ED gradient along the path is minimal; (b) internal micro-event structure remains maximally coherent; (c) participation with the surrounding field is least strained. **MCD.1 mapped (a) onto A1.d ≡ A1.c, but did not give (b) or (c) precise mathematical content.**

If (b) and (c) encode genuinely additional principles beyond geodesic motion — e.g., an entropic component to "maximal coherence" or a non-local "participation" measure — they could provide a structural input to nonlinearity that the MCD analysis did not consider. **This would constitute a fourth nonlinearity route N4 beyond the N1/N2/N3 enumerated in MCD.2.**

**Research question Q3:** Do ED-07 §5.1 criteria (b) and (c) admit precise mathematical formulation, and if so, do they introduce a structurally-distinct nonlinearity route that the MCD analysis missed?

This is foundational substrate-physics work. A positive result might revive ED's gravitational-sector prospects through a path that the linear-Lagrangian framework did not capture.

### 6.4 Scoping the new arc

The three questions Q1, Q2, Q3 should be addressed in a single foundational arc, working title **"ED-Substrate Foundations" (ESF arc)** or similar. The arc would:

- Open with ESF.0 (scoping) covering all three questions.
- Address each in 2–3 memos (ESF.1–ESF.7 approximately).
- Close at ESF.X with one of three program-level outcomes:
  - **Foundational extension found.** One or more of Q1/Q2/Q3 yields a positive substrate derivation that revives the gravitational-sector question. A new gravitational-sector arc can then be opened with the new foundational input.
  - **No extension found, but program preserved.** All three questions produce negative or inconclusive results. ED's gravitational sector is confirmed as linear at galactic scales, and the program continues with empirical work (merger-lag, weak-lensing) and acceptance of the BTFR-incompatibility finding.
  - **Substrate revision required.** The investigation reveals that ED's substrate physics needs structural revision to be self-consistent (e.g., the ρ-T relationship analysis surfaces a contradiction with existing theorems). This would be a major program event requiring careful integration with the closed arcs.

The ESF arc is **structural-foundational work, not empirical-fitting work.** It does not replace the empirical arcs (merger-lag retrodiction, weak-lensing) but proceeds in parallel. Estimated duration: comparable to BTFR.01–09 in scope and depth.

---

## 7. Place in the ED program

### 7.1 The DM/MCD lineage

| Sub-arc | Hypothesis | Verdict | Year |
|---|---|---|---|
| DM.0 | T sourced by ρ_b | Refuted (DM.1 §1) | 2026 |
| DM.1 | T sourced by activity (linearized DM2 run) | Refuted (DM.5 + BTFR.01–09) | 2026 |
| DM.G | T sourced by disc geometry | Refuted (DM.G.4) | 2026 |
| MCD | Path-of-easiest-updating action principle | **Refuted (this memo)** | 2026 |

Four independent attempts have failed to derive slope-4 BTFR within ED's currently-articulated structure. The pattern is robust and informative: the linearity wall is structural, not contingent on hypothesis choice.

### 7.2 The honest program-level status

> **ED is structurally consistent at the foundational level and produces a precise galactic-scale prediction (slope-2 BTFR with flat rotation curves under the Einstein-like relation) that is empirically wrong by a factor of 2 in slope.** This is established at three independent structural levels (DM.G + MCD) and confirmed by the DM2 numerical FAIL.
>
> **Three foundational research questions (Q1, Q2, Q3) remain open and could in principle revive the gravitational-sector question.** None has been addressed at the substrate-foundations level; none should be expected to succeed; but each is a genuine open path.
>
> **ED's foundational arcs (R, M, N, Q, B, GR, GR-SC, RG, ED-SC 3.x) and cluster-scale calibration are unaffected.** The damage is structurally local to the galactic-disc-dynamics gravitational sector.
>
> **The universality result (DM.5 §3.2) remains as ED's genuine positive finding** at galactic scales, modulo the optimizer-convergence caveat. ED's qualitative no-per-galaxy-tuning prediction holds.

### 7.3 What this means for further research

The ED program continues, with two clear directions:

**Empirical:** Pursue ED's other galactic and cluster-scale predictions (merger-lag, weak-lensing, environmental effects) where its activity-source mechanism may have positive predictions independent of BTFR.

**Foundational:** Pursue the three Q1/Q2/Q3 questions at the substrate-foundations level. A positive result on any of them would revive the gravitational-sector question; negative results would lock in the slope-2 verdict as ED's structural prediction at galactic scales.

The two directions proceed independently. **Neither is contingent on the other.**

---

## 8. Recommended Next Steps

Three concrete next steps for the ED program after MCD closure:

1. **Open the ESF arc (ED-Substrate Foundations) with a single scoping memo.** Address Q1, Q2, Q3 as the three sub-questions. Do not attempt to resolve them in the scoping memo; the goal is a clean roadmap for the foundational arc, parallel in scope to MCD.0 or DM.G.0. **This is the recommended next step if the program continues structural work** in the gravitational sector.

2. **Pursue empirical work in parallel — merger-lag retrodiction is the highest-priority test.** The DM-arc closed with FAIL on BTFR but with cluster-scale predictions intact. The merger-lag retrodiction recommendation (DM.6 §6.1, project_next_predictions memory) is the natural next empirical confrontation. Independent of the ESF foundational work; either confirms or refutes ED's cluster-scale predictions, which are presently the strongest part of the program.

3. **Update program-orientation documents (ED-Orientation, MEMORY) with the four-arc convergence finding and the ESF roadmap.** The DM.0/1, DM.G, and MCD closures collectively establish the gravitational-sector structural status. Future-session orientation should reflect: (a) ED's gravitational sector is currently linear at galactic scales; (b) slope-2 is the canonical structural prediction; (c) three foundational questions (ESF arc) could change this; (d) empirical work proceeds on independent predictions. This is a small documentation task that prevents future confusion and gives the program a clean status at this point.

The MCD arc has delivered its honest result. **Many-chain dynamics, taken at face value, does not escape the DM-arc linearity wall.** The path-of-easiest-updating principle is GR-equivalent at single-chain level and canonical-ED-equivalent at many-chain level. The substrate-physics analysis confirms that the wall is robust. **The arc closes here, the structural foundations remain intact, and the empirical and foundational programs continue on independent paths.**

Status: complete.
