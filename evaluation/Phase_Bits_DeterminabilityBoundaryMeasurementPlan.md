# Phase Bits — Determinability-Boundary Measurement Plan

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** Bits (empirical program — planning)
**Status:** Launches the empirical arc; opens the one remaining open item from Phase G (§8.3)
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_E_ConstraintSurface.md` §6 (determinability boundary = decoupling surface); `Phase_G_Generalization.md` §8.3 (the standing empirical deliverable); `AD_Note_SubstrateBeneathTheShadow.md` (the FS↔ED parallel)

---

## 1. Purpose

This document launches the **empirical side of the ED ↔ FS parallel**. The architectural evaluation (Phases A–G, plus the tie-break and orientation-primitivity closures — twelve documents, AD score 6/6) located the ED substrate's **determinability boundary** at the decoupling surface, *structurally*. It did not quantify it. This program does.

The goal is to define how to **measure, in bits, the information lost across the determinability boundary** — how much determination is forfeited when one tries to predict the state on the far side of a decoupling surface from information on the near side. This is the direct counterpart to FS's quantified parity barrier (where the loss is a number — an escape density, a bit count), played for ED's structural horizon instead of FS's multiplicative one.

**The architecture is fixed.** This phase introduces no new axiom, no new channel, no new invariant, and no revision to any verdict. The substrate specification is closed and minimal. This phase is **purely quantitative**: it takes the fixed architecture as given and measures a number that the architecture already implies but never computed. Nothing here can change the 6/6 result; it can only attach a magnitude to a boundary the evaluation already proved exists.

This is a *planning* document. It designs the measurement; it does not perform it or report results.

---

## 2. Structural Inputs

The program relies on the following established structural facts. Each is a *result* of the completed evaluation, cited, not a new assumption:

- **The decoupling surface is the determinability boundary** (Phase E §6). Inside a reach stratum the substrate is determinable from local channels; across a decoupling surface no channel carries the determining information. Reach horizon and determinability horizon coincide. *This is the boundary whose loss we quantify.*
- **Reach-strata are causally independent** (causal-cone factorization, Phase C §6 / Phase E §6). The reachable set factorizes across decoupling boundaries; one-sided influence may flow outward across a surface, but reciprocal participation does not. *This factorization is the structural source of the information loss — the thing the bits measure should detect.*
- **Invariants are stratified** (Phase E §7). Orientation — and, by the same stratification logic, the determinable structure generally — is a local invariant within a stratum and undefined across. *The bits measure should register that across-boundary quantities are not merely hard to predict but structurally undefined relative to within-stratum information.*
- **Evolution is sharpening, acyclic, and Σ-maximizing** (Phase D §3/§6, with tie-break closure). Fronts select extremes (not diffusive averages); dynamics run one-way to local-maximization fixed points; the forward step is unique given the tie-break rule. *This makes individual trajectories deterministic within a stratum, which is what lets us attribute across-boundary uncertainty to the boundary rather than to dynamical chaos.*

**No new architectural assumptions will be introduced.** Every structural fact the measurement uses is already proven. The program's only freedom is in *how it measures*, never in *what the substrate is*.

---

## 3. Measurement Objective

**Core quantity.** The bits of determination lost when predicting across a decoupling surface — informally, *how much less you can say about the far side of the boundary given everything on the near side, compared to a within-stratum baseline where determination is complete.*

**Information-theoretic statement.** Let **A** denote the configuration of a region on the near side of a decoupling surface (within a reach stratum, where the substrate is determinable) and **B** the configuration of a region on the far side (across the boundary, in a causally independent stratum). The central candidate quantities:

- **Mutual information I(A; B)** — how many bits A and B share. The factorization result predicts this should be *low* (ideally → 0 for the across-boundary, reciprocally-decoupled component), and the measured value quantifies *how* low.
- **Conditional entropy H(B | A)** — the residual uncertainty about B after A is fully known. The determinability loss is the gap between H(B | A) and the within-stratum baseline H(B′ | A) where B′ is a same-stratum region at comparable separation.
- **Determination deficit Δ** — the program's headline quantity, defined as the difference between within-stratum predictability and across-boundary predictability at matched separation: **Δ = [predictability within stratum] − [predictability across boundary]**, expressed in bits. Δ isolates the *boundary's* contribution by differencing against a baseline that shares everything *except* the boundary crossing.

**Aim.** Produce a **numerical estimate (or a range/function)** for Δ — the bits-of-determination forfeited at the decoupling surface. A single robust number is the ideal; a function of reach profile or boundary sharpness is the acceptable and likely realistic outcome.

---

## 4. Experimental Setup (Conceptual)

**Simulation kind.** Discrete ED-substrate simulations on a participation graph:

1. **Initialize** configurations within a reach stratum — a connected participation region bounded by (or containing) at least one decoupling surface.
2. **Evolve** under the fixed ED update rule: Σ = Coh − Str − Grad maximized, with the specified tie-break (channel-bandwidth-ordering, B1-distinctness final key). The dynamics are deterministic per trajectory given initial data, which is essential for clean attribution.
3. **Identify decoupling surfaces** — locate where reciprocal participation goes one-sided (B6) — and **track what crosses and what doesn't**: record the one-sided outward influence and confirm the absence of reciprocal return (the factorization, as a simulation-level check, not an assumption).

**Observables.** State variables recorded per micro-event / per region / per time step:

- **commitment density ρ** (the primary state variable; monotone by I4 — a useful internal consistency check);
- **channel states** — Coh/Str/Grad values and the selected candidate (the Σ-maximizer);
- **orientation** — both the longitudinal (commitment-flow) and, where representable, the transverse component (the primitive B5 content);
- **decoupling-surface location and one-sidedness** over time.

**Regions and windows.** Define paired regions for the Δ difference:
- **near-boundary vs. far-from-boundary** within the *same* stratum (the within-stratum baseline);
- **near-boundary on side 1 vs. near-boundary on side 2** of a decoupling surface (the across-boundary case).
Match separations (graph distance) between the baseline and across-boundary pairs so Δ differences out everything but the boundary. Time windows: a transient window (active propagation) and a late window (near the fixed point), measured separately — the loss may differ between them.

---

## 5. Information-Theoretic Framework

Three candidate measures, with trade-offs:

**M1 — Mutual information I(A; B).**
*Pros:* symmetric, standard, directly interprets as "shared bits"; a clean → 0 result would be a strong, legible statement of the factorization. *Cons:* estimating MI from finite samples is bias-prone (especially for high-dimensional A, B); requires many ensemble runs; sensitive to binning/representation of configurations.

**M2 — Conditional entropy H(B | A).**
*Pros:* directly "residual uncertainty about the far side given the near side"; pairs naturally with the within-stratum baseline to form Δ. *Cons:* same finite-sample/dimensionality estimation difficulty as MI (they are algebraically related); needs a fixed, justified configuration representation.

**M3 — Predictive success rate of a within-stratum-restricted model.**
*Pros:* operational and robust — train/fit a predictor using *only* within-stratum information and measure its accuracy on across-boundary targets vs. a within-stratum baseline; converts "bits of determination" into a measurable predictive gap that is comparatively cheap to estimate and hard to fake. *Cons:* the bit-interpretation is indirect (accuracy → bits requires a calibration assumption); model-class dependence (a weak predictor understates determinability).

**Relation to "bits of determination."** M1/M2 give bits *directly* but are estimation-fragile; M3 gives a predictive gap that *maps to* bits under a stated calibration and is estimation-robust. **Recommended posture:** use **M3 as the operational workhorse** (robust, interpretable as a gap) and **M2/Δ as the bit-denominated headline**, cross-checking the two. The program fixes *one* measure as primary before running (Practical Plan §7) to avoid measure-shopping; the others serve as consistency checks.

---

## 6. FS Parallel (Target Shape)

**FS, briefly.** The Factor Skyline work quantifies its determinability limit — the **parity barrier** (Sarnak disjointness) — as a number: an escape density (≈ 0.265 in the bit-decomposition: H(dx) ≈ 2.483, template ≈ 1.700, escape ≈ 0.265, activation ≈ 0.517). The barrier is not merely named; it is *measured*, in bits, as a specific fraction of the structure that the multiplicative architecture cannot determine.

**Desired ED result shape.** A number (or function) that plays the **same role** for ED's determinability boundary as FS's escape density plays for the parity barrier: *the quantity of structure the ED substrate's reach-bounded architecture cannot determine across a decoupling surface*, in bits. Concretely, a value of Δ (or a small family of Δ values parameterized by reach profile) that can sit beside FS's escape density as the ED entry in a two-row "determinability-boundary, quantified" comparison.

**Discipline — structural analogy only.** FS measures a multiplicative-number-theoretic barrier; ED measures a physical-substrate reach horizon. They share **architectural form** (a finite-reach architecture with a quantifiable horizon past which determination fails), detected by a shared methodology. **No claim** is made that the two numbers are equal, that ED's boundary *is* a parity barrier, or that the domains share content. The parallel is: *both architectures admit a bits-denominated determinability measure, and we compute ED's so it can be compared in form to FS's.* The comparison is of *roles*, not of *values*.

---

## 7. Practical Plan

Concrete steps, in order:

1. **Implement the ED substrate simulator.** Participation graph with bandwidth-weighted channels; the Σ update with the specified tie-break; explicit decoupling-surface construction (regions whose reciprocal participation is severed beyond a reach threshold). Validate against known structural results first — confirm monotone ρ (I4), acyclicity (no state recurrence), and one-sided cross-boundary influence (factorization) — as correctness gates before any measurement.
2. **Fix one primary measure.** Commit to **M3 (within-stratum-restricted predictive gap)** as primary and **Δ via M2** as the bit-denominated headline, *before* running ensembles. Record the choice and the calibration assumption mapping M3's gap to bits. No changing the primary measure after seeing results.
3. **Run ensembles.** Many initial conditions per configuration class; paired baseline (within-stratum) and across-boundary measurements at matched graph separations; transient and late-time windows measured separately.
4. **Analyze robustness.** Vary initial conditions, reach profiles (sharp vs. graded decoupling), graph topologies, and boundary geometries. Report Δ as a central estimate with a spread, and as a function of reach profile if it varies systematically. Flag any dependence on the configuration representation (a representation-sensitive result is a warning, not a finding).

**Required tools.** A discrete-graph simulation environment (Python with a graph library — NetworkX or equivalent — for the participation graph; NumPy for state arrays); an information-theoretic estimation stack (a vetted MI/entropy estimator with finite-sample bias correction; scikit-learn or similar for the M3 predictor); a reproducible experiment harness (fixed seeds recorded, ensembles scripted, results logged). No specialized hardware anticipated at planning stage; scale of graphs determines compute, to be sized in step 1.

### Reusable simulation assets (existing ED codebases)

Two existing repositories were surveyed for reuse. Neither performs this measurement, and — importantly — **neither implements the Σ-maximization selection rule**: both evolve by diffusion / gradient-flow / ballistic dynamics, which is precisely the *averaging* behavior that produces the diffusive **shadow** (Phase D §3), not the sharpening **substrate**. They are therefore **infrastructure and a starting scaffold, not a drop-in substrate simulator.** They map cleanly onto the substrate/shadow distinction the evaluation established:

| Repo | Side | What it is | Reuse role |
|---|---|---|---|
| `ed-lab` (`edsim`) | **Shadow** | Mature d=1–4 solver for the degenerate-parabolic ED PDE `M(ρ)∇²ρ + M'(ρ)\|∇ρ\|² − P(ρ)` — i.e. the coarse-grained shadow (catalog entry #15). 112 tests, NumPy/SciPy. | **Analysis stack + shadow reference** |
| `Emergence Universe` | **Both** | Engine A: a second diffusion lattice (shadow). **Engine B: discrete micro-event "ring" dynamics** — coupled particles, collapse *events*, PBC boundaries as horizon analogues, a finite collapse-mechanism taxonomy. | **Substrate scaffold (Engine B)** |

**Directly reusable for this program:**

- **`ed-lab/simulations/edsim/invariants/` — the analysis stack, largely pre-built.** `spectral.py` provides Shannon entropy `H = −Σ pₖ ln pₖ`; `correlation.py` provides correlation length ξ and structure functions over matched separations (the **Δ difference design** in §3 needs exactly such matched-separation measurements); the sweep/reproducibility/test harness (`experiments/`, `reproducibility/`) is a ready template for §7 step 3's ensembles with recorded seeds. Much of the §7 "information-theoretic estimation stack" requirement is already written here — though note it currently computes entropy *globally*, not *across a boundary*; the cross-boundary MI/conditional-entropy (M1/M2) and the M3 predictor are **new** and must be added.
- **`Emergence Universe` Engine B (`event_lattice.py`, `RingState`, the collapse-event detector, `run_until_collapse()`) — the closest existing substrate scaffold.** Its discrete-event loop, boundary-crossing instrumentation, and history-recording pattern are reusable; its `taxonomy_entropy()` shows the entropy-as-summary idiom. The build is to **swap ballistic motion for Σ-maximization (+ tie-break)** and **generalize the ring to a bandwidth-weighted participation graph** with explicitly-severed decoupling surfaces (NetworkX over the existing NumPy state arrays is the natural bridge).
- **Shared stack alignment.** Both repos are NumPy/SciPy + Matplotlib + JSON-sweep — the same stack named above, so no new tooling decisions.

**The irreducible new build** (present in neither repo) remains exactly §7 step 1's core: a **participation graph evolving under Σ = Coh − Str − Grad maximization with the specified tie-break and explicit decoupling surfaces, instrumented to record per-region (ρ, channel states, orientation) for the Δ measurement.** The recommended path is therefore *not* greenfield: extend Engine B's discrete-event loop with the Σ-maximization rule, borrow `ed-lab`'s invariant atlas for the analysis layer, and add the cross-boundary information measures (M1/M2/M3) that neither repo has.

*Incidental bonus.* Because `ed-lab` simulates the shadow directly, it provides a free comparison target should the program ever wish to *empirically* exhibit the "substrate sharpens / shadow diffuses" result (Phase D §3): the shadow side already runs; only the substrate side would be built.

---

## 8. Risks and Ambiguities

**R1 — Defining the boundary cleanly in discrete simulations.** A decoupling surface is sharp in the axioms but may be fuzzy in a finite simulated graph (a region of *weakening* reciprocity rather than a crisp cut). *Mitigation:* construct decoupling surfaces by explicit severing (hard threshold) in the controlled experiments, so the boundary is unambiguous by construction; treat graded-decoupling cases as a separate, later robustness study, not the primary measurement.

**R2 — Separating architectural determinability loss from numerical artifacts.** Finite-sample MI bias, predictor weakness, and binning choices can all masquerade as (or mask) genuine loss. *Mitigation:* the **Δ difference design** is the primary defense — baseline and across-boundary cases share the same estimator, representation, sample size, and separation, so shared artifacts cancel in the difference. Additionally: bias-corrected estimators, convergence checks vs. sample size, and the M3/M2 cross-check (two measures disagreeing flags an artifact).

**R3 — Choosing a measure interpretable and comparable to FS.** A measure that gives bits but isn't comparable in *role* to FS's escape density would miss the point. *Mitigation:* fix the headline as a *fraction/quantity of undeterminable structure* (Δ in bits, optionally normalized to a within-stratum total), which is the same *role* FS's escape density plays — a fraction of structure the architecture cannot reach. Comparability is of role, asserted explicitly, never of numerical value.

**R4 — Over-reading the FS parallel.** The program's own framing could drift into content claims. *Mitigation:* the structural-analogy-only discipline (§6) is restated in every deliverable; any comparison is role-to-role, with the disclaimer attached.

---

## 9. Deliverables

Success for this program is defined as producing:

1. **A clear definition of the determinability-boundary bits measure** — the fixed primary measure (M3 operational + Δ/M2 bit-denominated), its calibration, and its computation procedure, stated precisely enough to be reproduced.
2. **A numerical estimate (or family of estimates) for ED** — Δ as a central value with spread, and as a function of reach profile if it varies; with the robustness analysis (R-series mitigations) reported alongside, so the number carries its uncertainty honestly.
3. **A comparison narrative to FS's parity barrier, strictly at the structural level** — a short account placing ED's Δ beside FS's escape density as two instances of *a bits-denominated determinability boundary*, role-to-role, with the no-content-claim discipline explicit. This is the quantitative completion of the AD note's proposed parallel: the note proposed the structural analogy; this delivers the measured ED side.

**Location.** These deliverables live in a **new empirical arc**, separate from the architectural evaluation. The twelve architectural documents (Phases A–G + tie-break + orientation) are closed and fixed; this measurement program is a distinct body of work that *uses* their results without modifying them. Recommended home: an `ED_Substrate/Bits/` subfolder (this plan, then the simulator, then the results and comparison), or a sibling `evaluations/ED_Substrate_Bits/` arc — to be fixed when implementation begins.

A closing discipline note. This program quantifies a boundary the architecture already proved exists; it cannot validate or invalidate Event Density as physics (outside AD's remit), and it cannot change the 6/6 architectural verdict. Its sole product is a *number* — the bits ED forfeits at its determinability horizon — reported with its uncertainty and compared, in form only, to the number FS reports at its own. That number is the empirical counterpart to a structural fact, and nothing more is claimed for it.

---

*End of Phase Bits measurement plan. This document designs the determinability-boundary bits measurement; it does not perform it. The architecture is fixed; this is the quantitative arc. Implementation begins when the simulator is built and the primary measure is fixed per §7.*
