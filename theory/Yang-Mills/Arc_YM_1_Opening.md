# Arc YM — The Yang-Mills Program (Arc Opening)

**Date:** 2026-04-30
**Status:** Arc opening. **Arc YM** — the Yang-Mills program. Substrate-to-continuum derivation of the non-Abelian gauge-field dynamics, mass-gap mechanism from $\ell_P$ substrate cutoff, OS-positivity preservation analysis, and architectural classification of YM content under ED-I-06 ontology. **Now unblocked by closure of Arc D (DCGT) on 2026-04-30.**
**Companions:** [`../Yang_Mills_Roadmap_Scoping.md`](../Yang_Mills_Roadmap_Scoping.md) (queued-arc scoping memo, 2026-04-28), [`../../theorems/T17.md`](../../theorems/T17.md) (Gauge-Fields-as-Rule-Type), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (T18 Kernel Retardation), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md) (DCGT), [`../../papers/Navier Stokes_Synthesis_Paper/NS_Synthesis_Paper.md`](../../papers/Navier%20Stokes_Synthesis_Paper/NS_Synthesis_Paper.md) (NS Synthesis Paper with Appendices C + D), [`../Navier Stokes/MHD/NS_MHD_5_Synthesis.md`](../Navier%20Stokes/MHD/NS_MHD_5_Synthesis.md).

---

## 1. Purpose

This memo opens the Yang-Mills (YM) arc, the next major structural arc of the Event Density program. The arc has six goals:

- **Derive the Yang-Mills continuum equations** from ED substrate primitives — chains, directional fields, T17 gauge-rule-type structure, V1 / V5 kernels — under hydrodynamic-window coarse-graining via DCGT methodology.
- **Establish the substrate → continuum limit for non-Abelian gauge fields.** The Abelian ($U(1)$) case is the closed companion to NS-MHD's Lorentz-force-via-T17 result. The non-Abelian extension is the new structural content of YM.
- **Identify the OS-positivity preservation locus** — the structural stall-risk of the arc. Reflection positivity preservation under continuum limit is where every prior YM-existence approach has hit obstructions; the ED-substrate-discrete-and-finite starting point may dissolve or relocate the obstacle, knowable only by trying.
- **Analyze the mass-gap mechanism** from the substrate cutoff $\ell_P$. Substrate is finite-difference at scale $\ell_P$; discrete-spectrum-class arguments analogous to lattice-gauge-theory should produce a gap; the question is whether the gap survives the continuum limit.
- **Produce a publishable architectural classification of YM content** under ED-I-06 ontology, parallel to NS-MHD-4 / Appendix C for MHD.
- **Provide the ED substrate foundation for the Clay Millennium Problem.** Not solving the Clay problem, but establishing the structural framing under which ED contributes to it: substrate-level existence + coarse-graining bridge + mass-gap-from-cutoff + OS-positivity preservation analysis.

**Arc YM is now unblocked.** As of 2026-04-30, the four structural prerequisites are all closed:

- **T17 (Gauge-Fields-as-Rule-Type, Arc Q closure 2026-04-27)** — provides the substrate-level gauge structure and minimal-coupling vertex for any compact gauge group.
- **T18 (V1 Kernel Retardation, Arc B closure 2026-04-27)** — provides the forward-cone-only causal structure for the substrate kernel and ensures positivity-preserving continuum limit at the analytic-structure level.
- **ED-I-06 (Fields and Forces in Event Density, Feb 2026)** — provides the ontological framework under which gauge fields read as directional-field participation structures and gauge content reads as forces sourced by participation structures.
- **DCGT (Arc D closure 2026-04-30)** — provides the substrate-to-continuum coarse-graining methodology used in YM-2.

Every YM-prerequisite arc is closed. The arc proceeds.

---

## 2. Motivation

Three considerations make Yang-Mills the natural next arc.

**(M1) It is the highest-leverage remaining ED arc.** The NS / MHD program closed on 2026-04-30 with full architectural classification, ED-I-06 ontological grounding, and DCGT substrate-to-continuum bridge. The next major structural targets are: Hall-MHD extension (arc-extension scope, lower leverage), YM (Clay Millennium Problem, highest leverage), and ED-10 spacetime emergence (most ambitious, most speculative). YM dominates the leverage hierarchy: it is a Clay problem, the prerequisites are all closed, the methodology (DCGT) is now available, and the structural posture (substrate-discrete-and-finite + ED-I-06 directional-field reading + T17 substrate gauge content) is novel relative to standard constructive-QFT approaches.

**(M2) YM is the non-Abelian analogue of the NS / MHD program.** The Abelian gauge sector ($U(1)$, electromagnetism) was closed in Arc Q (T17) and operationalized in NS-MHD via T17 minimal coupling on charged chains. Non-Abelian YM ($SU(N)$, $SO(N)$, $G_2$, …) generalizes the same substrate-rule-type structure to richer compact simple groups. The same substrate-to-continuum machinery (DCGT) that worked for Abelian gauge content should generalize, with structural modifications at the points where non-Abelian content differs from Abelian (self-coupling vertices, structure-constant terms, parallel-transport non-commutativity). YM is therefore not a structurally new arc but a structurally extended one — running the same methodology in a richer setting.

**(M3) DCGT provides the substrate-to-continuum machinery YM-2 requires.** Before Arc D, the substrate-to-continuum bridge was INHERITED at the level of NS / MHD viscous content and Lorentz coarse-graining. Without DCGT, attempting YM-2 (substrate → continuum limit for non-Abelian gauge fields) would mean reinventing the coarse-graining machinery from scratch, simultaneously with the harder OS-positivity question. With DCGT, the coarse-graining is a closed methodology that generalizes naturally to gauge-field correlators. This is the structural reason Yang-Mills is timed *after* Arc D closure: the prerequisite methodology is now operational.

**(M4) YM mass-gap analysis requires the substrate cutoff $\ell_P$.** ED's substrate is finite-difference at scale $\ell_P$ (forced by Theorem 19 + Theorem 18 + Primitive 13). The gap-from-cutoff argument is structurally analogous to lattice-gauge-theory's gap arguments, with $\ell_P$ playing the role of the lattice spacing. The continuum-limit-survival of the gap is the load-bearing question of YM-3.

**(M5) YM is the next Clay-relevant structural target after NS.** The NS Synthesis Paper closed the NS / MHD architectural-and-substrate program, including the Intermediate Path C verdict on Clay-NS smoothness (advection as the unique transport-kinematic obstruction outside ED's canonical regularizing architecture). The natural next Clay-relevant arc in the program is YM-existence-and-mass-gap. The structural posture is similar (architectural decomposition + substrate grounding + Clay-relevance verdict), but the technical content is different (gauge-field correlators rather than fluid velocity; reflection positivity rather than smoothness; mass gap rather than blow-up).

---

## 3. Scope

Arc YM is scoped as a six-memo arc with the following structural targets:

- **YM-1 (this memo).** Arc opening; framing, scope, non-goals, inputs, plan.
- **YM-2.** Substrate → continuum limit for non-Abelian gauge fields. Apply DCGT methodology to gauge-field correlators; derive the continuum YM equations $D_\mu F^{\mu\nu} = J^\nu$ from substrate-level non-Abelian gauge dynamics; identify the structural points where non-Abelian content differs from Abelian.
- **YM-3.** Mass-gap mechanism from substrate cutoff $\ell_P$. Lattice-analogous gap argument adapted to ED substrate; analyze whether the gap survives the continuum limit; identify the load-bearing technical conditions.
- **YM-4.** Architectural classification of YM content. Apply NS-MHD-4-style classification table to YM content channels (gauge-field kinetic term, self-coupling vertices, gauge-fixing terms, ghost terms, matter-coupling terms); classify each under ED-I-06 ontology.
- **YM-5.** OS-positivity preservation analysis. Audit reflection positivity through DCGT coarse-graining; identify the structural stall-risk locus; verify whether T18 forward-cone-causality + V1 positive-Fourier-transform jointly preserve OS positivity, or whether additional structural commitments are required.
- **YM-6.** Synthesis + Clay-relevance memo. Aggregate the five sub-arc results; state ED's structural contribution to the Clay YM-existence-and-mass-gap problem; honest disclaimers on what ED resolves and what remains open.

Arc YM will use:

- **T17 minimal coupling generalized to non-Abelian gauge groups.** The substrate-level minimal-coupling vertex $\partial_\mu \to \partial_\mu - igA_\mu$ (with $A_\mu = A_\mu^a T^a$, $T^a$ generators of the gauge Lie algebra) extends T17 from $U(1)$ to compact simple groups. The substrate-rule-type structure of $\tau_g$ supplies the group-theoretic content (T17 clauses C2 + C3); non-Abelian extension adds non-commutativity at the vertex.
- **DCGT-style coarse-graining for gauge-field fluxes.** The hydrodynamic-window machinery of Arc_D_2 / Arc_D_3 / Arc_D_4 / Arc_D_5 generalizes to gauge-field-correlator coarse-graining. Multi-scale expansion of the gauge-field flux statistics under V1 weighting produces the continuum gauge-kinetic operator structure; multi-scale expansion of charged-chain populations under T17 minimal coupling produces the gauge-current source. The same methodology, applied to non-Abelian content.
- **ED-I-06 directional-field ontology for gauge potentials.** $A_\mu$ is the participation measure of the substrate gauge rule-type $\tau_g$ (T17 clause C1); under ED-I-06 §3 it is a directional-field-class participation structure. The YM field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu]$ inherits directional-field status with non-Abelian extension at the commutator term.
- **V1 / V5 kernels for smoothing and memory structure.** V1 supplies the substrate spatial smoothing kernel (Theorem N1, Theorem 18 forward-cone support); V5 supplies the substrate cross-chain memory. Both extend to the gauge sector via T17's vacuum-coupling clauses (C5–C7, the $B[v;\tau_g]$ additive background functional).

---

## 4. Non-Goals

Arc YM explicitly does **not**:

- **Solve the Clay problem directly.** The Clay YM-existence-and-mass-gap problem requires a constructive proof of YM existence with mass gap on $\mathbb{R}^4$ at the level of Streater-Wightman / Osterwalder-Schrader axioms. Arc YM's deliverable is structural — the ED account of YM existence and mass gap under substrate-discrete-and-finite assumptions, with OS-positivity preservation analyzed but not necessarily proven in full constructive rigor. ED's contribution to the Clay problem is the substrate framing, not the solution.
- **Compute numerical mass-gap values.** All numerical content is INHERITED at value layer per the program's standard form-FORCED / value-INHERITED methodology. The mass gap's *existence* and its *substrate origin* are within scope; the *numerical value* is INHERITED.
- **Derive the Standard Model.** The specific gauge group of the Standard Model ($SU(3)\times SU(2)\times U(1)$), specific representation content (matter sectors, Higgs sector), Yukawa couplings, and CKM/PMNS mixing matrices are out of scope. Arc YM addresses YM-existence-and-mass-gap for general compact simple gauge groups; specific group choice and matter content are EMPIRICAL per Arc Q.6.
- **Unify YM with ED-10 curvature emergence.** The ED-10 spacetime-emergence arc (substrate-to-continuum metric coarse-graining) is queued separately. Arc YM operates in flat Minkowski spacetime per ED-Phys-10 acoustic-metric guardrails; coupling to spacetime curvature is deferred.
- **Derive confinement phenomenology.** Confinement, asymptotic freedom, $\beta$-function coefficients, glueball spectra, and other phenomenological YM features are out of scope. The mass gap exists / does-not-exist verdict is within scope; phenomenological details are INHERITED.

Arc YM focuses strictly on:

- substrate → continuum mapping for non-Abelian gauge fields (YM-2);
- architectural classification of YM content under ED-I-06 (YM-4);
- mass-gap mechanism from $\ell_P$ substrate cutoff (YM-3);
- OS-positivity preservation through DCGT coarse-graining (YM-5).

---

## 5. Inputs (Upstream Arcs)

The arc depends structurally on the following upstream content:

- **T17 (Gauge-Fields-as-Rule-Type, Arc Q closure).** Provides the substrate-level gauge structure: $A_\mu$ as participation measure of $\tau_g$, gauge-group content (non-Abelian-capable, Killing form, Jacobi closure), minimal-coupling vertex, gauge-quotient identification, vacuum-kernel structure ($B[v;\tau_g]$). All four T17 channels (group / vertex / worldline / vacuum) extend to non-Abelian gauge groups via T17's existing structural content.
- **T18 (V1 Kernel Retardation, Arc B closure).** Provides forward-cone-only causal structure for the substrate kernel. Required for OS-positivity-preservation analysis (YM-5): forward-cone support is the substrate-level analytic-structure ancestor of the upper-half-plane analyticity standard QFT postulates as Wightman-axiom / OS-axiom ingredient.
- **ED-I-06 (Fields and Forces in Event Density, Feb 2026).** Directional/scalar/curvature-like field ontology. Gauge potentials are directional-field-class participation structures; forces are biases sourced by stable participation structures; transport-kinematic frame artifacts and continuum-imposed constraints are non-ED. The ontological reading of YM content under ED-I-06 is YM-4's deliverable.
- **DCGT (Arc D closure 2026-04-30).** Substrate-to-continuum coarse-graining theorem. The methodology used in YM-2 to derive continuum YM equations from substrate gauge-field-correlator dynamics. DCGT establishes (a) hydrodynamic-window scale separation conditions, (b) multi-scale expansion methodology, (c) form-FORCED / value-INHERITED structural split, (d) sign-FORCED kernel-positivity arguments, (e) error-bound scaling. All five generalize to the non-Abelian gauge-field case.
- **NS-MHD-5 (Synthesis).** Canonical / non-canonical boundary for gauge-field couplings. NS-MHD-5 established that the Lorentz force is canonical ED via T17 minimal coupling; the kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) is the structural pattern that YM-4 will generalize.
- **NS Synthesis Paper (Appendices C & D).** Architectural + substrate foundation for fluid-mechanical content. Appendix C supplies the ED-I-06 ontological reading template; Appendix D supplies the DCGT substrate-derivation template. Both will be reused in the YM synthesis (YM-6) memo.
- **Yang-Mills Roadmap Scoping (2026-04-28).** Prior queued-arc scoping memo at `theory/Yang_Mills_Roadmap_Scoping.md`. Identifies the four-arc structure (later refined to six in the present scoping), the OS-positivity preservation as the stall-risk locus, the mass-gap-from-cutoff mechanism, and the connection-watch list for relevant structural surfaces. The present arc supersedes the queued scoping with the executed plan.

---

## 6. Planned Structure of Arc YM (6 memos)

The arc is planned as six memos parallel in scope to NS-MHD and Arc D:

1. **Arc_YM_1_Opening.md** *(this memo)* — Framing, scope, non-goals, inputs, plan.

2. **Arc_YM_2_Substrate_to_Continuum_Limit.md** — Derive the continuum Yang-Mills equations from substrate primitives. Define non-Abelian gauge-field correlators at substrate level under T17 generalized minimal coupling. Apply DCGT-style multi-scale expansion to gauge-field flux statistics. Derive the continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ with non-Abelian commutator structure. Identify the points where non-Abelian content differs from the Abelian (NS-MHD-2) case: self-coupling vertices, structure-constant terms, parallel-transport non-commutativity at the multi-scale-expansion level.

3. **Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md** — Analyze the mass-gap mechanism from $\ell_P$ substrate cutoff and V1 / V5 kernel retardation. Adapt the lattice-gauge-theory gap argument to ED substrate; identify the substrate-level mechanism for the mass gap; analyze whether the gap survives the continuum limit. Working a-priori: substrate-discrete-and-finite gives gap automatically; the continuum-limit-survival question hinges on T18 forward-cone causality + V1 positive-Fourier-transform jointly bounding the spectrum away from zero.

4. **Arc_YM_4_Architectural_Classification.md** — Classify YM content channels under ED-I-06 ontology. Content: gauge-field kinetic term $-\tfrac{1}{4}F^a_{\mu\nu}F^{a\,\mu\nu}$, non-Abelian self-coupling vertices ($AAA$ and $AAAA$), gauge-fixing terms (Lorenz / Coulomb / axial), ghost terms (Faddeev-Popov), matter-coupling terms ($\bar\psi i\gamma^\mu D_\mu \psi$ at fluid scale via T17 minimal coupling), substrate-cutoff / R1-class terms inherited from gauge-field V1 coarse-graining. Each classified under canonical-ED / continuum-constraint / transport-kinematic categories.

5. **Arc_YM_5_OS_Positivity_And_Continuum_Stability.md** — Identify the OS-positivity preservation locus; analyze stall-risk. Audit reflection positivity through DCGT coarse-graining; verify whether T18 forward-cone causality + V1 positive-Fourier-transform jointly preserve OS positivity, or whether additional structural commitments are required. Identify the load-bearing technical condition for continuum-limit reflection positivity. Working a-priori: T18 forward-cone support is the substrate ancestor of upper-half-plane analyticity → OS positivity at substrate level is automatic; preservation under DCGT coarse-graining is the load-bearing question.

6. **Arc_YM_6_Synthesis_And_Clay_Relevance.md** — Synthesize the arc; state ED's structural contribution to the Clay problem. Aggregate the five sub-arc results; produce a Clay-relevance verdict parallel to NS-Smoothness's Intermediate Path C. Honest disclaimers on what ED resolves and what remains open. Recommend integration into the NS Synthesis Paper as Appendix E (or into a new YM Synthesis Paper, depending on scope after sub-arc closure).

Estimated effort: 6 memos at the demonstrated pace, comparable to Arc D (6 memos) and NS-MHD (5 memos). Total estimated 6–10 effective sessions, with YM-2 (substrate-to-continuum) and YM-5 (OS-positivity) likely the longest individual memos given their technical load.

---

## 7. Deliverables

Final outputs of Arc YM:

- **A substrate-derived continuum Yang-Mills equation.** $D_\mu F^{\mu\nu} = J^\nu$ with non-Abelian commutator structure, derived from substrate gauge-field correlator dynamics via DCGT-style multi-scale expansion. Form FORCED at substrate level; coupling and group-specific content INHERITED at value layer.
- **A mass-gap mechanism grounded in $\ell_P$.** Substrate cutoff produces a gap automatically (lattice-analogous); continuum-limit survival analysis identifies the load-bearing conditions and verdict (gap survives / gap closes / gap survives conditionally).
- **An architectural classification of YM content.** Eleven-or-so-item classification table parallel to NS-MHD-4 / Appendix C, with each YM content channel classified canonical-ED / continuum-constraint / transport-kinematic under ED-I-06 ontology.
- **An OS-positivity preservation analysis.** Identification of the structural stall-risk locus; verdict on whether T18 + V1 + DCGT jointly preserve OS positivity, or what additional structural commitments are needed.
- **A publishable YM synthesis memo.** Aggregating the above into a single memo parallel to NS-MHD-5 / NS Synthesis Paper.
- **A Clay-relevance statement.** ED's contribution to the Clay YM-existence-and-mass-gap problem: substrate framing, coarse-graining bridge, mass-gap mechanism, OS-positivity preservation analysis. Honest scope: not a Clay-problem solution, but a structural account of the problem under ED.

Once Arc YM closes, the NS / MHD architectural-and-substrate program will be joined by an analogous YM architectural-and-substrate program, both anchored on T17 + T18 + ED-I-06 + DCGT.

---

## 8. Recommended Next Steps

After this opening memo, proceed to **Arc_YM_2 (Substrate → Continuum Limit for non-Abelian gauge fields)**. File: `theory/Yang-Mills/Arc_YM_2_Substrate_to_Continuum_Limit.md`. Scope: derive the continuum Yang-Mills equation $D_\mu F^{\mu\nu} = J^\nu$ from substrate primitives. Define non-Abelian gauge-field correlators at substrate level via T17 generalized minimal coupling on $\tau_g$ with compact-simple-group structure. Apply DCGT multi-scale expansion to the gauge-field flux statistics. Identify the points where non-Abelian content differs from the Abelian NS-MHD-2 case and verify that DCGT machinery generalizes.

Estimated 2–3 sessions for Arc_YM_2 given the technical load.

### Decisions for you

- **Confirm arc framing.** Yang-Mills program as the non-Abelian analogue of NS / MHD, unblocked by T17 + T18 + ED-I-06 + DCGT closure.
- **Confirm six-memo plan.** Estimated 6–10 effective sessions; comparable scope to Arc D.
- **Confirm proceeding to Arc_YM_2 (substrate → continuum limit) as the next deliverable.**

---

*Arc YM opened. The Yang-Mills program in Event Density: substrate-to-continuum derivation of non-Abelian gauge-field dynamics, mass-gap mechanism from $\ell_P$ substrate cutoff, OS-positivity preservation analysis, architectural classification under ED-I-06, Clay-relevance statement. Six-memo plan parallel to Arc D / NS-MHD scope. All four prerequisites closed: T17 (gauge-as-rule-type, 2026-04-27), T18 (kernel retardation, 2026-04-27), ED-I-06 (fields ontology, Feb 2026), DCGT (Arc D, 2026-04-30). Non-goals: no Clay-problem solution, no numerical mass-gap values, no Standard Model derivation, no ED-10 curvature unification, no confinement phenomenology. Arc_YM_2 (substrate → continuum limit) is the next deliverable; estimated 2–3 sessions given technical load.*
