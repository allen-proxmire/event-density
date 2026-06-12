# Phase E — Constraint Surface (Discrete Mode 3)

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** E (Constraint Surface)
**AD step:** Step 4 — Mode 3 (Constraint Surface)
**Status:** Third extraction phase; resolves the orientation-gap deferral from Phases C and D
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_B_ArchitecturalSpecification.md`; `Phase_C_EnvelopeExtraction.md`; `Phase_D_ExtremalDynamics.md`; `Phase_A2_DiscreteExtraction_Modes.md` (discrete Mode 3 machinery, surface-type taxonomy)

---

## 1. Purpose

Phase E constructs the **constraint surface** of the ED substrate using the discrete Mode 3 from Phase A2. This is the integrating phase: where Mode 1 (Phase C) extracted the static envelope and Mode 2 (Phase D) extracted the dynamical behavior, Mode 3 assembles both — plus the axioms and the update rule — into a single geometric object whose faces are the substrate's structural and dynamical constraints, and whose closure properties characterize the whole architecture.

Phase E is the phase that:

- **integrates** the axioms (B1–B7), the update rule (Σ), the envelope (Phase C), and the extremal dynamics (Phase D) into one constraint surface;
- **identifies the structural faces** (imposed by axioms) and the **dynamical faces** (imposed by the rule and the extremal dynamics);
- **determines whether orientation conservation is forced, optional, or stratified** — the decisive resolution of the deferral carried from Phase C (F4/I1) through Phase D (located, by §5 orientation-blindness, as a channel-structure question);
- **locates the determinability boundary geometrically** — the structural feature the whole ED-substrate review was motivated to find.

Output: a full constraint-surface description, a closure assessment, and a surface-type classification. As in all extraction phases, Phase E produces *evidence*. The criteria verdicts (PASS/CONDITIONAL/FAIL) are Phase F's work, not Phase E's.

---

## 2. Inputs

Phase E uses **only** the Phase B–D results and the general discrete Mode 3 machinery from Phase A2. Inputs:

- **Axioms B1–B7** and the **evolution rule** Σ = Coh − Str − Grad (maximized, graph-local, finite reach, tie-breaking open).
- **Channel table** — coherence (stabilizing), strain (destabilizing), gradient strain (destabilizing/steering), orientation (structuring/neutral), decoupling (bounding).
- **Candidate invariants I1–I5** — with **I4 established** (Phase C N2: ρ-monotonicity forced), **I5 present and partially recoverable** (Phase D §7), **I2/I3 forced**, and **I1 (orientation) open and located** as a channel-structure question.
- **Envelope results (Phase C)** — F1–F5 (F4 open), N1–N4, inequalities E-I4/E-I5/E-I2, causal-cone factorization, two characterized ghost-state classes (trans-decoupling; non-maximal-path), closure "partially open with characterized openness."
- **Extremal dynamics (Phase D)** — sharpening (non-diffusing) fronts; self-limiting concentration; **acyclic** dynamics with **local-maximization fixed points** as sole terminal attractor; **partially recoverable** footprint; Σ-transitions distinct from but correlated with decoupling surfaces; orientation gap **located** in the channel structure (Σ is orientation-blind).

The decisive Phase D hand-off: orientation conservation, *if* it holds, must be a property of the **channel/participation structure (B2, B5)** — it cannot come from the rule. Phase E is where the channel structure is examined directly, so this is where the question is answered.

---

## 3. Channel Space Definition

The constraint surface lives in the substrate's **channel space**: the space whose coordinates are the five channels of the Phase B decomposition, evaluated over the participation graph. A substrate configuration is a point in this space; the constraint surface is the locus of admissible-and-reachable points.

**The five channel coordinates:**

1. **Coherence channel** (Coh) — stabilizing, score-bearing, local.
2. **Strain channel** (Str) — destabilizing, score-bearing, local.
3. **Gradient-strain channel** (Grad) — destabilizing/steering, score-bearing, meso (couples local step to the ρ-field).
4. **Orientation channel** — structuring, *non-score-bearing* (neutral in Σ), meso–global.
5. **Decoupling channel** — bounding, *non-score-bearing*, local-boundary → global-partition.

**Dimensionality and degrees of freedom.** The channel space is not uniform-dimensional: it splits into a **score-bearing subspace** (coherence, strain, gradient-strain — the three Σ inputs) and a **structural subspace** (orientation, decoupling — carried by the architecture, invisible to Σ). The score-bearing subspace is where the update rule acts; its effective degrees of freedom are reduced by the maximization constraint (every reachable point is a Σ-maximizer, collapsing the three score coordinates onto the maximization footprint, §5 of Phase C). The structural subspace is *orthogonal to the rule's objective* — its degrees of freedom are set by the participation-graph geometry, not by the dynamics.

**Interaction vs. independence.**

- The three score-bearing channels **interact**: Σ = Coh − Str − Grad couples them into one scalar at every step. They are not independent; they trade off.
- The **decoupling channel interacts with all of them** as a *boundary*: it sets the finite reach inside which the other channels are even defined (no channel reaches past a decoupling surface).
- The **orientation channel is independent of the score-bearing subspace** — this is the structural restatement of Phase D's "Σ is orientation-blind." Orientation neither enters Σ nor is altered by Σ-maximization. Whether orientation interacts with the *decoupling* channel is precisely the orientation-face question (§7): does the reach structure constrain orientation, even though the score structure does not?

This split — score-bearing subspace coupled by the rule, structural subspace independent of it, with decoupling as the boundary of both — is the architecture of the channel space and the frame for every face below.

---

## 4. Structural Faces

Structural faces are constraints the **axioms** impose directly on the channel space, independent of the dynamics. Each bounds the admissible region.

**SF1 — Finite-reach face (decoupling).**
*Constraint:* no point of the channel space has support across a decoupling surface; every channel is defined only within a reach horizon R_decouple (B6). The surface is partitioned into causally independent reach cells.
*Sharp/loose:* **sharp.** The decoupling surface is a hard boundary (F2 forbids trans-decoupling reciprocity); there is no slack at the reach horizon.
*Orientation interaction:* **yes — this is the load-bearing interaction.** The finite-reach face partitions the channel space, and whether orientation is constrained *across* that partition is the §7 question. Flagged.

**SF2 — Forward-only face (P11).**
*Constraint:* the surface admits no point reachable only by uncommitting a prior commitment; the admissible region is closed under forward evolution and excludes all backward transitions (B7, F1).
*Sharp/loose:* **sharp.** Irreversibility is absolute; no slack.
*Orientation interaction:* **no.** P11 acts on commitment density, not orientation. (Orientation is a channel-layer field; commitment is an event-layer accumulation.)

**SF3 — Chain-continuity face.**
*Constraint:* the surface admits only configurations built from adjacency-connected chains (B3); no point requires a non-adjacent jump (F3). The admissible region is the adjacency-connected closure of the participation graph.
*Sharp/loose:* **sharp.** Adjacency is bandwidth-gated and definite; a step is adjacent or it is not.
*Orientation interaction:* **partial.** Chains *carry* orientation (B5), so chain-continuity transports orientation along a chain — but continuity alone does not constrain whether orientation is *consistent* between distinct chains. Continuity is necessary for orientation transport, insufficient for orientation conservation. Flagged as contributing to §7.

**SF4 — Monotonicity face (now established).**
*Constraint:* the surface admits only ρ-monotone histories; ρ(x, t₂) ≥ ρ(x, t₁) at every position (E-I4, forced by Phase C N2). This is no longer a candidate — it is an established structural face.
*Sharp/loose:* **sharp at the lower bound** (attained at quiescent positions and at strict-increase positions alike).
*Orientation interaction:* **no.** Monotonicity is a ρ-property; orthogonal to the orientation channel.

**Reading of §4.** Three of four structural faces (SF2, SF4, and SF3 for ρ/commitment) are sharp and orientation-orthogonal — the architecture's *commitment* structure is cleanly bounded. The orientation interactions concentrate entirely in **SF1 (finite-reach)** and **SF3 (chain-continuity transport)**. This confirms Phase D's routing: orientation's fate is bound to the *reach partition*, not to the commitment dynamics. §6 and §7 follow this thread.

---

## 5. Dynamical Faces

Dynamical faces are constraints the **update rule and extremal dynamics** impose. They sit inside the structural faces and further restrict the reachable region.

**DF1 — Maximization-footprint face.**
*Constraint:* every reachable point is a Σ-maximizer in its neighborhood (Phase C N1, E-I5); the score-bearing subspace collapses onto the footprint locus. Non-maximal points are admissible-as-static but unreachable (the non-maximal-path ghost class).
*Sharp/loose:* **sharp by construction** (the face *is* the maximization rule).
*Orientation interaction:* **no.** The footprint is a score-subspace face; Σ is orientation-blind (Phase D §5).

**DF2 — Sharpening-front face.**
*Constraint:* reachable configurations are produced by sharpening (extreme-selecting) fronts, not diffusive averaging (Phase D §3). The surface excludes diffusively-blended intermediate states that a parabolic rule would admit — those are *not reachable* under maximization.
*Sharp/loose:* **sharp** at the front (discrete selection), with the caveat that the *coarse-grained* shadow re-introduces apparent looseness (diffusion) by averaging — but that looseness is a property of the shadow, not the substrate surface.
*Orientation interaction:* **transport only.** The front carries orientation (Phase D §3) but, being Σ-driven, does not constrain its consistency. Contributes to §7 as transport, not constraint.

**DF3 — Acyclic-attractor face.**
*Constraint:* the surface has no closed orbits; every trajectory terminates at a local-maximization fixed point (Phase D §6, cycles excluded by E-I4 + F1). The reachable region is a *forest of monotone trajectories converging on fixed points*, not a space with recurrent loops.
*Sharp/loose:* **sharp.** Acyclicity is absolute (a cycle would violate monotonicity).
*Orientation interaction:* **yes — at the fixed point.** Phase D found fixed points are ρ-stabilized and footprint-stabilized but **orientation-ambiguous**: nothing in the attractor forces a unique orientation at the terminal state. This is the orientation gap reappearing as a property of the dynamical face. Flagged for §7.

**DF4 — Footprint-recoverability face.**
*Constraint:* late-time states preserve the *extensive* footprint (commitment set + ρ-profile + maximality certification) but not the *intensive* footprint (margins, order, tie resolutions) (Phase D §7). The surface is *legible to outcomes but not to margins*.
*Sharp/loose:* **partially sharp** — sharp on what is preserved (forced by F1 + E-I4), loose/lossy on what is not (margins are genuinely absent, not merely hard to read).
*Orientation interaction:* **indirect.** Whether orientation is recoverable at late time depends on whether it is conserved (if conserved within a stratum, the fixed-point orientation records the stratum's orientation; if ambiguous, it records nothing). Routed through §7.

**Reading of §5.** As in §4, the orientation interactions cluster: **DF3 (acyclic attractor, at the fixed point)** is the dynamical sibling of **SF1 (finite-reach)**. The commitment-and-score faces are sharp and orientation-orthogonal; orientation's openness lives specifically at *reach boundaries* (SF1) and *terminal fixed points* (DF3) — and those are the same sites, because a fixed point is where a causal cone has run to completion. The constraint surface is telling us, consistently across four independent faces, that orientation is undetermined exactly at the reach/termination boundary and nowhere else.

---

## 6. Reach-Bounded Faces (Reach-Stratified Structure)

This section constructs the **reach-stratified surface type** from Phase A2 and uses it to **locate the determinability boundary geometrically** — the central structural deliverable of the whole ED-substrate review.

**Construction.** By SF1 and causal-cone factorization (Phase C §6), the channel space partitions into **reach strata**: maximal regions within which all channels are mutually defined (reciprocal participation holds throughout), separated by decoupling surfaces across which reciprocal participation is one-sided. Each stratum is a causal cone. The reachable set **factorizes** across strata: the configuration of one stratum is causally independent of another's, because no channel — score-bearing or structural — reaches across the boundary.

**The reach-stratified surface** is therefore a *product* surface: globally, the constraint surface is the product of per-stratum constraint surfaces, glued *only* by the one-sided influence permitted across decoupling boundaries (forward influence out of a cone, never reciprocal influence back in).

**Locating the determinability boundary.** Within a single stratum, the substrate is *fully determinable*: every channel is defined, the maximization rule has access to all the local information it needs, the footprint is well-defined, and (anticipating §7) orientation is coherent. The dynamics inside a stratum are forward-deterministic up to the open tie-breaking point.

**Across a decoupling surface, determinability ends.** This is the geometric determinability boundary, and it is *exactly the decoupling surface*:

> **The determinability boundary of the ED substrate is the decoupling surface (B6). Inside a reach stratum, the substrate's evolution is determined by its local channels; across a decoupling surface, no channel carries the information that would determine the relationship between strata. The reach horizon and the determinability horizon coincide.**

This is the structural counterpart the scoping memo and the AD note sought: where FS has the parity barrier (Sarnak disjointness) as its determinability boundary, ED has the decoupling surface. In both cases the boundary is *finite reach made into a horizon*: the architecture can determine what lies within reach and is structurally blind to relationships across the reach boundary. The boundary is not a failure of the dynamics — it is a positive structural feature (B6 is an axiom, not an absence).

**Orientation across strata — the §7 question, now sharply posed.** Within a stratum, the question is whether orientation is conserved (forced consistent). Across a stratum boundary, the prior question is whether orientation is even *comparable*: if no channel reaches across the decoupling surface, then there is no structural means to compare the orientation of one stratum with another. This distinction — *conserved within, comparable across* — is what §7 must resolve.

---

## 7. Orientation-Face Analysis (Decisive Section)

This section resolves the deferral carried from Phase C (F4/I1) through Phase D (located here). The three possibilities, each evaluated for structural cause:

**Possibility A — orientation forced consistent (gap closes).**
*Would require:* a structural mechanism that compels orientation consistency across *all* of the channel space, including across decoupling surfaces. *Structural cause available?* **No.** Causal-cone factorization (§6) establishes that no channel reaches across a decoupling surface. There is therefore no structural means to *compel* orientation agreement between distinct strata — the mechanism that would force global consistency does not exist in the architecture. Possibility A fails at the reach boundary.

**Possibility B — orientation fully optional (gap stays open everywhere).**
*Would require:* the channel structure imposing *no* orientation constraint even within a stratum. *Structural cause against?* **The chain-continuity face (SF3) and the within-stratum coherence of the front (Phase D §3).** Within a single reach stratum, orientation is transported coherently along adjacency-connected chains (SF3), and the front advances into a consistent neighborhood carrying its orientation without a score incentive to reverse (there is no Σ term that rewards reversal — Σ is orientation-blind, so reversal is never selected *for*, and continuity transports the existing orientation). Within a stratum, spontaneous reversal (F4) has no structural pathway: it is neither forced by the rule (orientation-blind) nor admitted by continuity (which transports the existing value). So orientation is **not** freely optional within a stratum. Possibility B fails inside the stratum.

**Possibility C — orientation stratified (partial closure).**
*Structure:* orientation is **forced consistent within each reach stratum** (by SF3 transport + Σ orientation-neutrality, which together leave the carried orientation unperturbed) and **independent across strata** (by causal-cone factorization, which removes any channel that could relate them). Orientation conservation is a **local (within-cone) invariant, not a global one.** Across a decoupling surface, orientation is not "reversed" or "conserved" — those predicates are *undefined*, because no channel makes the two strata's orientations comparable.
*Structural cause:* present and identified — SF1 (reach partition) + SF3 (within-stratum transport) + DF3 (orientation-ambiguous fixed points are ambiguous only *relative to other strata*, definite within their own).
*Structural or dynamical:* **structural.** The stratification is imposed by the axioms (B6 reach + B3 continuity), not by the rule. The rule's only contribution is its orientation-neutrality, which *permits* the structural outcome rather than causing it.

**VERDICT: orientation is STRATIFIED.**

> Orientation conservation holds as a **local invariant within each reach stratum** and is **undefined (not violated) across decoupling surfaces.** I1 is established in the stratified sense: orientation is conserved everywhere it is *comparable*, and comparability is exactly co-extensive with reach.

**Consequences, recorded for Phase F:**

- **F4 (spontaneous orientation reversal) is forbidden within a stratum** — closing the Phase C soft edge *locally*. Within reach, F4 is now a genuine forbidden pattern (no structural pathway).
- **F4 is undefined across strata** — not forbidden, not admitted; the predicate does not apply, because the comparison requires a channel that finite reach removes.
- **I1 is a stratified invariant**, parallel in form to I4 (ρ-monotonicity) but *scoped to the stratum*. This is **not** the additional-axiom outcome Phase D flagged as the CONDITIONAL branch: orientation conservation is *derived* (from B3 + B6 + Σ-neutrality), not *added*. The gap closes — but it closes to a **local** invariant, honestly scoped, not to a global one the architecture cannot support.
- **The orientation result and the determinability boundary are the same fact.** Orientation is determinate exactly within reach and indeterminate exactly beyond it — orientation conservation is *the determinability boundary expressed in the orientation channel*. This is the cleanest confirmation that the determinability boundary (§6) is a real, multiply-witnessed structural feature, not an artifact of one channel.

---

## 8. Closure Assessment

Does the constraint surface's **reachable** region coincide with its **admissible** region?

**By subspace:**

- **Commitment/score subspace — closed.** The monotonicity face (SF4), forward-only face (SF2), chain-continuity face (SF3), and maximization-footprint face (DF1) are all sharp; the two ghost-state classes from Phase C (trans-decoupling, non-maximal-path) are both *structurally characterized*, not residual slack. No uncharacterized ghost faces here.
- **Reach-stratified structure — closed by construction.** The product-of-strata structure (§6) is exactly the reachable set; there are no admissible cross-stratum configurations that the factorization fails to account for, because trans-decoupling configurations are precisely the (characterized) trans-decoupling ghost class.
- **Orientation subspace — closed, in the stratified sense.** With the §7 verdict, orientation is no longer an open admissibility question: within a stratum it is forced consistent (closed), across strata it is undefined (not an open region but a non-region — the predicate does not apply). The Phase C "open admissibility question" is **resolved**, not merely deferred.

**Ghost faces.** The only ghost states are the two Phase C classes — trans-decoupling and non-maximal-path — both **structurally characterized and bounded.** Phase E adds **no new uncharacterized ghost faces.** The orientation gap, which in Phase C looked like a potential uncharacterized opening, is resolved by §7 into a *characterized stratification*, not a ghost region.

**Closure verdict (neutral): the constraint surface is CLOSED in the characterized sense.** The reachable region equals the admissible region up to two structurally-characterized, bounded ghost-state classes, with **no uncharacterized slack and no unresolved admissibility boundary.** This is a stronger closure statement than Phase C's "partially open" — because Phase E *resolved* the orientation gap that kept Phase C's verdict qualified. Recorded as evidence for Phase F's envelope-tightness and determinism criteria; not itself a criterion verdict.

---

## 9. Surface-Type Classification

Classifying the ED-substrate constraint surface against the discrete Mode 3 taxonomy (graph-contractive / stability-resolved / reach-stratified / commitment-dissipative). More than one type can apply; the substrate is characterized by *which combination*.

**Graph-contractive? — Partially.** The front sharpens and concentration self-limits (Phase D §3–4), and trajectories contract onto fixed points (DF3). The dynamics *do* contract the reachable region toward attractors. But the surface is not *globally* contractive — the reach partition (§6) means contraction happens *within* strata, independently. **Verdict: locally graph-contractive, within strata.**

**Stability-resolved? — Yes.** The defining feature: every reachable point is a Σ-maximizer (DF1), so the surface is the locus where the coherence–strain stability balance is *resolved* at every step. The score-bearing subspace collapses onto the stability-resolved footprint. **This is the substrate's primary surface type** — the surface is, first and foremost, the set of stability-resolved configurations.

**Reach-stratified? — Yes, definitively.** §6 constructs exactly this: the surface is a product of per-stratum surfaces glued by one-sided cross-decoupling influence, with the determinability boundary at the stratum boundaries. **This is the substrate's defining structural type** — and the one with no continuum analogue (Phase A2's reach-stratified surface, here instantiated).

**Commitment-dissipative? — Yes, in the irreversible-accumulation sense.** P11 + monotonicity (SF2 + SF4) make the surface *dissipative* in the thermodynamic-analogue sense: commitment accumulates irreversibly, trajectories run one-way to fixed points, and nothing returns (acyclicity, DF3). The "dissipation" is of *reversibility*, not of commitment density (which only grows). **Verdict: commitment-dissipative (irreversible-forward type).**

**Combined classification:** the ED-substrate constraint surface is a **stability-resolved, reach-stratified, commitment-dissipative surface that is locally graph-contractive within strata.** The two defining types are **stability-resolved** (the dynamical character — every point is a maximizer) and **reach-stratified** (the structural character — the surface factorizes at decoupling boundaries, where the determinability boundary sits). The other two types are present but subordinate: graph-contractive is *local* (scoped to strata), commitment-dissipative is the *irreversibility signature* of the forward-only axiom.

---

## 10. Summary Table

| Face | Type | Sharp/Loose | Orientation Status | Notes |
|---|---|---|---|---|
| **SF1** Finite-reach (decoupling) | Structural | Sharp | **Load-bearing** | Partitions channel space; seat of determinability boundary |
| **SF2** Forward-only (P11) | Structural | Sharp | Orthogonal | Irreversibility; no orientation interaction |
| **SF3** Chain-continuity | Structural | Sharp | Transport | Carries orientation along chains; necessary for within-stratum consistency |
| **SF4** Monotonicity (established) | Structural | Sharp (lower bound) | Orthogonal | I4 as a fixed face; ρ-property |
| **DF1** Maximization footprint | Dynamical | Sharp (by construction) | Orthogonal (Σ orientation-blind) | Score subspace collapses to maximizer locus |
| **DF2** Sharpening front | Dynamical | Sharp (substrate); loose in shadow | Transport only | Substrate sharpens; PDE diffusion is a coarse-graining artifact |
| **DF3** Acyclic attractor | Dynamical | Sharp | **Ambiguous at fixed point (cross-stratum)** | Fixed points orientation-definite within stratum, ambiguous across |
| **DF4** Footprint recoverability | Dynamical | Partially sharp (lossy on margins) | Indirect (via §7) | Extensive footprint preserved; intensive lost |
| **Reach-stratified structure** | Reach | Sharp boundaries | **Conserved within / undefined across** | Product surface; **determinability boundary = decoupling surface** |
| **Orientation face (verdict)** | Structural | Sharp within stratum | **STRATIFIED** | I1 = local invariant, derived not added; F4 forbidden within, undefined across |
| **Closure** | — | — | Resolved | Closed in characterized sense; 2 bounded ghost classes; no uncharacterized slack |

---

## 11. Next Actions

Phase E completes **Step 4 of AD** (Mode 3 — Constraint Surface). Results integrated across all extraction phases:

- The channel space splits into a **score-bearing subspace** (coupled by the maximization rule) and a **structural subspace** (orientation + decoupling, independent of the rule), with decoupling as the boundary of both.
- **Four structural faces** (SF1–SF4) and **four dynamical faces** (DF1–DF4) are identified; the commitment/score faces are sharp and orientation-orthogonal, while orientation's openness localizes precisely to the **reach boundary** (SF1) and **terminal fixed points** (DF3) — the same site.
- The **determinability boundary is located geometrically: it is the decoupling surface.** Inside a reach stratum the substrate is determinable; across a decoupling surface no channel carries the determining information. Reach horizon and determinability horizon coincide — the ED structural counterpart to FS's parity barrier.
- **The orientation gap is resolved: orientation is STRATIFIED** — a local invariant conserved within each reach stratum and undefined (not violated) across strata. I1 is *derived*, not added as an axiom; F4 is forbidden within a stratum and undefined across. The orientation result and the determinability boundary are the same structural fact witnessed in the orientation channel.
- **Closure is CLOSED in the characterized sense** — two bounded ghost-state classes, no uncharacterized slack, no unresolved admissibility boundary.
- **Surface-type classification: stability-resolved, reach-stratified, commitment-dissipative, locally graph-contractive within strata** — with stability-resolved and reach-stratified as the two defining types.

**Phase F begins Step 5 of AD.** It evaluates the ED substrate against the **substrate-level AD criteria** reformulated in Phase A1 (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality), rendering **PASS / CONDITIONAL / FAIL** with evidence drawn from Phases B–E, plus a constraint census. Phase F is the first phase that judges; all prior phases supplied the evidence it will weigh. Of particular note for Phase F: the stratified orientation result and the geometric determinability boundary bear directly on the **determinism** criterion (specifically its reach-bounded-determination component from Phase A1), and the characterized closure bears directly on **envelope tightness**.

The constraint surface is constructed. The criteria evaluation begins.

---

*End of Phase E. This phase constructs the ED substrate's Mode 3 constraint surface and locates the determinability boundary as evidence; it does not render criteria verdicts, which are Phase F. The criteria evaluation begins at Phase F.*
