# Phase A2 — Discrete Extraction Modes

**Evaluation:** Architectural Distillation of the Event Density substrate
**Phase:** A2 (extraction-mode reformulation)
**Status:** Methodological extension — to be fixed before any evaluation
**Date filed:** June 2026
**Author:** Allen Proxmire
**Follows:** `Phase_A1_SubstrateLevel_AD_Criteria.md` (the reformulated criteria); completes the Phase-A methodological extension

---

## 1. Purpose

Phase A determined that AD's three-mode extraction engine — Mode 1 (envelope), Mode 2 (extremal dynamics), Mode 3 (constraint surface) — requires adaptation before it can extract constraints from a discrete relational substrate rather than a continuum governing equation. Phase A1 reformulated the three criteria that needed it; this document, Phase A2, reformulates the three extraction modes.

The same two constraints from A1 govern here, and they are not negotiable:

- **The modes are general, not ED-specific.** Each discrete mode below is defined for *any discrete relational architecture* — any system of nodes, edges, and a local update rule. The Event Density substrate is the eventual object of evaluation, but it does not appear in any mode definition. A procedure written so that ED's extraction comes out clean is worthless; a procedure written for the general class, then applied to ED in later phases, is the only kind that carries information.

- **The modes are fixed before evaluation.** This document precedes Phase B. The extraction procedures must be settled before they are run on any specific substrate, so that what they produce is a finding rather than an artifact of a procedure tuned to its target.

With Phase A1 (criteria) and Phase A2 (modes) filed, AD's substrate-level extension is complete, and the evaluation can begin at Phase B against a methodology that was settled in advance.

---

## 2. Why the Continuum Modes Do Not Transfer Directly

AD's three modes extract three layers of constraint from a continuum system. Each has a clear purpose and a clear point of failure on a discrete substrate.

- **Mode 1 (Axiom → Envelope).** *Purpose:* derive forbidden/necessary configurations and bounding inequalities from the axioms alone, without solving anything. *Mismatch:* the continuum envelope is a system of inequalities on state variables and their derivatives. A discrete substrate has no derivatives and no differential inequalities; its envelope is over graph configurations, and its bounds are combinatorial, not analytic.

- **Mode 2 (Equation → Extremal Dynamics).** *Purpose:* derive front speeds, decay rates, stability, and blow-up behavior from the governing equation. *Mismatch:* a discrete substrate has no governing differential equation; it has a local update rule. "Front speed" presumes continuous propagation; the substrate propagates a bounded number of edges per step and has decoupling surfaces that bound reach. "Decay rate" presumes a continuous relaxation; the substrate relaxes strain through discrete update steps.

- **Mode 3 (Channels → Constraint Surface).** *Purpose:* derive the geometry of channel interactions — impossible and forced combinations, universality classes. *Mismatch:* the continuum constraint surface is a geometric object in continuous channel-activity space. A discrete substrate's interaction structure is the participation graph itself; its "constraint surface" is combinatorial geometry over graph configurations, not a smooth manifold of channel activities.

The common thread: the continuum modes assume derivatives, a continuum metric, unbounded propagation, and a differential governing law. A discrete substrate has none of these — it has graph-locality, finite reach, a discrete metric, and an update rule that is a *selection* (a local optimization), not a differential equation.

**The goal is not to mimic the continuum modes but to preserve the *spirit* of each.** Mode 1 extracts what the axioms forbid and force; Mode 2 extracts what the dynamics drive things toward at the extremes; Mode 3 extracts how the interaction structure constrains itself. Those three jobs are domain-agnostic. What changes is the machinery: combinatorial in place of analytic, reach-bounded in place of unbounded, selection-driven in place of differential.

---

## 3. Discrete Mode 1 — Envelope Extraction

### 3.1 The discrete envelope

For a discrete relational substrate, the **envelope** is the set of participation-graph states that are both **admissible** (permitted by the primitives) and **reachable** (produced by the update rule from admissible initial states). Mode 1 derives the envelope's structure from the primitives alone, before the update rule is iterated — the analogue of AD's "from the axioms, without solving."

### 3.2 What Mode 1 extracts

- **Forbidden graph patterns.** Subgraph motifs or state assignments that the primitives **structurally exclude** — patterns no admissible configuration can contain, each traceable to a specific primitive. These define the exterior of the envelope.
- **Necessary graph patterns.** Motifs that the primitives **force** into any admissible configuration — structures that must be present. These define the interior skeleton of the envelope.
- **Reachability constraints.** Bounds imposed by **finite propagation**: from a given configuration, only states within the discrete causal cone (reach *r* per step) are reachable in bounded time. Decoupling surfaces further restrict reachability by bounding which regions can influence which. These define the envelope's *dynamical* boundary, distinct from the *admissibility* boundary set by the forbidden/necessary patterns.

### 3.3 The discrete envelope inequalities

The continuum envelope's inequalities (conservation identities, dissipation bounds, regularity estimates) have combinatorial analogues:

- **Monotonicity constraints.** Quantities that can only increase or only decrease under the update rule — the discrete analogue of a dissipation identity. Commitment, under an irreversible update, is the archetype: it does not decrease. Any monotone quantity is an envelope constraint, because it bounds the reachable set to one side.
- **Stability constraints.** Bounds that confine the configuration to a region under iteration — the discrete analogue of an invariant box. If the update rule keeps a quantity within a fixed range for all admissible initial data, that range is an envelope constraint.
- **Local maximization constraints.** Constraints imposed by the update rule's *selection* structure: if each step selects the local optimum of a score, then every reached configuration satisfies a local-optimality condition (no admissible single-node change would have scored higher at the selecting step). This is an envelope constraint with no continuum analogue — it is a footprint left by the selection rule on every reachable state.

### 3.4 General procedure (Mode 1)

For any discrete relational substrate:

1. **Enumerate forbidden patterns.** From each primitive, derive the graph patterns it excludes. Collect them; each is traceable to its source primitive.
2. **Enumerate necessary patterns.** From the primitives, derive the patterns that must be present in any admissible configuration.
3. **Derive reachability bounds.** From the update rule's reach (propagation per step) and any decoupling surfaces, bound the reachable set in the discrete causal cone.
4. **Identify monotone, stable, and selection-footprint quantities.** Find the quantities the update rule only increases/decreases (monotonicity), confines (stability), or stamps with local-optimality (maximization footprint).
5. **Assemble the envelope.** The envelope is the intersection of the admissible set (forbidden/necessary patterns) and the reachable set (reachability bounds), characterized by the monotone/stable/selection constraints. The output is a minimal set of combinatorial envelope constraints, each labeled by source.

---

## 4. Discrete Mode 2 — Extremal Dynamics

### 4.1 Extremal behaviors in discrete systems

Mode 2's spirit is to characterize what the dynamics drive things toward at the extremes. For a discrete substrate, the extremal behaviors are:

- **Propagation fronts.** The boundary of the reach horizon as it grows under iteration — the discrete causal cone's leading edge. Where continuum fronts have a *speed*, discrete fronts advance a bounded number of edges per step, capped by reach and halted at decoupling surfaces.
- **Concentration points.** Nodes or regions where a quantity (commitment density, participation, strain) accumulates under iteration — the discrete analogue of blow-up or aggregation, but bounded if the substrate's primitives cap the quantity.
- **Extinction patterns.** Configurations or substructures that the update rule drives to disappear — chains that fail to maintain coherent participation and terminate; the discrete analogue of decay to zero.
- **Shock-like transitions in the selection score.** Sharp changes in the update rule's score (the discrete analogue of a shock): adjacent steps where the selected configuration changes qualitatively because the score's optimum jumps. These are the discrete loci where the dynamics "select differently," analogous to where a continuum solution forms a discontinuity.

### 4.2 Universal inequalities in discrete form

The continuum mode's universal inequalities become:

- **Bounds on score-change per update.** A bound on how much the selection score can change in a single step. If the update is local and the graph is bounded-degree, the per-step score change is bounded — a discrete analogue of a bounded dissipation rate.
- **Bounds on propagation speed.** The finite-reach bound: influence advances at most *r* edges per step, the discrete causal cone *r·t*, with decoupling surfaces as hard caps. This is the discrete analogue of a finite signal speed, and it holds for all admissible evolutions.
- **Bounds on local curvature / commitment change.** Bounds on how fast the substrate's discrete-geometric quantities (relational curvature, commitment density) can change per update at a node — the discrete analogue of a regularity estimate.

### 4.3 Attractor types for discrete substrates

The continuum surface types (contracting, isoenergetic, etc.) have discrete attractor analogues:

- **Fixed points.** Configurations the update rule maps to themselves — the discrete analogue of a stable equilibrium. The substrate, once there, stays.
- **Cycles.** Finite sequences of configurations the update rule traverses and repeats. On a bounded substrate, a deterministic forward update *must* eventually reach a fixed point or a cycle (pigeonhole on a finite configuration set), so the attractor structure is fixed-point-or-cycle by necessity at bounded scale.
- **Quasi-stable patterns.** Configurations that persist for many update steps before changing — long transients that are not strictly fixed or cyclic but are effectively stable on the timescale of interest. These are the discrete analogue of a slowly-relaxing metastable state.

### 4.4 General procedure (Mode 2)

For any discrete relational substrate:

1. **Characterize the front.** Determine how the reach horizon grows per step (the discrete causal cone) and where decoupling surfaces halt it.
2. **Locate concentration and extinction.** Identify where the update rule accumulates quantities (concentration) and where it drives substructures to disappear (extinction), with the primitives' caps noted.
3. **Find the score-transition loci.** Identify configurations where the selection score's optimum jumps (shock-like transitions).
4. **Bound the universal inequalities.** Derive the per-step score-change bound, the propagation-speed bound (reach), and the local-change bounds.
5. **Classify the attractors.** Determine the fixed points, cycles, and quasi-stable patterns the update rule produces from admissible initial data. The output is the extremal-dynamics profile: fronts, extremes, bounds, and attractor structure.

---

## 5. Discrete Mode 3 — Constraint Surface

### 5.1 The channel space of a participation graph

Mode 3's spirit is to characterize how the interaction structure constrains itself. For a discrete substrate, the interaction structure is the participation graph: nodes, adjacency, and the channels carrying participation between them. The **channel space** is the space of channel-activity configurations — which channels are active, at what bandwidth, in what adjacency pattern — subject to the substrate's structural constraints. The **constraint surface** is the geometry of admissible, reachable channel configurations within this space.

### 5.2 Faces of the constraint surface

A face is a structural limit — a direction in which the configuration is pushed to an extreme. For a discrete substrate:

- **Structural faces (from the primitives).** Limits imposed by the axioms: channel configurations that the primitives forbid or force. These are the faces present before any dynamics — the boundary of the admissible set in channel space.
- **Dynamical faces (from the update rule's selection).** Limits imposed by the selection structure: channel configurations the maximization can or cannot select. These are the faces the update rule adds — the boundary of the reachable set.
- **Reach-bounded faces (from decoupling surfaces).** Limits imposed by finite reach: channel interactions that cannot occur because the participating regions are decoupled. These are the faces finite reach contributes — interactions structurally excluded by the reach horizon.

### 5.3 Closure conditions

The constraint surface is **closed** if the configuration cannot escape it under iteration — the discrete analogue of AD's sealed-face closure. Two conditions:

- **No ghost faces.** Every face of the surface corresponds to a genuine structural or dynamical limit; there is no face the axioms describe but the dynamics never approach. (The face-level analogue of the ghost state from Phase A1 §5.)
- **No unreachable admissible regions.** Every admissible region of channel space is reachable under the update rule. There is no region the primitives permit that the dynamics never enter — the channel-space statement of "admissible equals reachable."

A surface failing either condition is open: the architecture's channel-space description is looser than its channel-space dynamics.

### 5.4 Surface types for discrete substrates

The continuum surface types have discrete analogues, classified by what dominates the channel-space dynamics:

- **Graph-contractive.** The surface contracts under iteration toward an attractor — channel configurations converge. The discrete analogue of the contracting (Lyapunov) surface; the hallmark of a substrate whose update rule descends a monotone quantity.
- **Stability-resolved.** The surface develops branch points resolved by the selection rule — where the maximization picks one channel configuration over a competing one. The discrete analogue of the entropy-resolved (hyperbolic) surface; selection plays the role the entropy condition plays in the continuum.
- **Reach-stratified.** The surface's structure depends on the reach horizon — different channel configurations are admissible at different reach scales, and decoupling surfaces partition the surface. The discrete analogue of the mass-stratified surface, with reach in place of a conserved scalar. This type has no clean continuum counterpart and is distinctive to finite-reach substrates.
- **Commitment-dissipative.** The surface contracts through an irreversible quantity (commitment) that only accumulates — the discrete analogue of a dissipative surface, where irreversibility, not a scalar Lyapunov functional, drives the contraction.

### 5.5 General procedure (Mode 3)

For any discrete relational substrate:

1. **Define the channel space.** Identify the channels, their activity/bandwidth variables, and the structural constraints on their configurations.
2. **Enumerate the faces.** Derive the structural faces (from primitives), dynamical faces (from selection), and reach-bounded faces (from decoupling surfaces).
3. **Test closure.** Check for ghost faces (faces described but never approached) and unreachable admissible regions (admissible channel configurations the dynamics never enter).
4. **Identify impossible and forced channel combinations.** From the faces, derive which channel combinations cannot coexist and which force one another.
5. **Classify the surface.** Determine which surface type (graph-contractive, stability-resolved, reach-stratified, commitment-dissipative, or a combination) dominates. The output is the constraint-surface profile: faces, closure status, channel combination rules, and surface type.

---

## 6. Summary Table

| Mode | Continuum Definition (AD) | Discrete Definition | Notes |
|---|---|---|---|
| **Mode 1 — Envelope** | Forbidden/necessary configurations and bounding inequalities from the axioms; bounds on state variables and derivatives | Forbidden/necessary **graph patterns** + **reachability bounds** (finite causal cone); envelope = admissible ∩ reachable, characterized by **monotonicity, stability, and local-maximization** constraints | The maximization-footprint constraint has no continuum analogue; bounds are combinatorial, not analytic |
| **Mode 2 — Extremal Dynamics** | Front speeds, decay rates, stability, blow-up, universal inequalities from the governing equation | **Propagation fronts** (reach horizon), **concentration/extinction**, **score-transition loci**; bounds on **per-step score change, propagation (reach), local change**; attractors = **fixed points / cycles / quasi-stable** | "Front speed" → bounded reach per step; bounded substrates necessarily reach a fixed point or cycle |
| **Mode 3 — Constraint Surface** | Geometry of channel interactions in continuous channel space; faces, closure, surface types | Channel space of the **participation graph**; **structural / dynamical / reach-bounded faces**; closure = **no ghost faces, no unreachable admissible regions**; types = **graph-contractive / stability-resolved / reach-stratified / commitment-dissipative** | The reach-stratified type is distinctive to finite-reach substrates and has no clean continuum counterpart |

The three discrete modes, together with the three reformulated criteria of Phase A1 and the three criteria that transfer directly, constitute the complete substrate-level extension of AD. All are stated for the general class of discrete relational architectures; no system-specific content appears in any mode definition.

---

## 7. Next Actions

With Phase A1 (criteria) and Phase A2 (extraction modes) filed, **the substrate-level extension of AD is complete.** AD now has, for the general class of discrete relational architectures: three transferred criteria (minimality, generative sufficiency, structural optimality), three reformulated criteria (locality, determinism, envelope tightness), and three discrete extraction modes (envelope, extremal dynamics, constraint surface). The methodology was settled before any specific substrate was scored against it, as the circularity guard requires.

The evaluation now proceeds:

- **Phase B — Architectural Specification (Step 1).** Enumerate the Event Density substrate's primitives (axioms), its update rule (the stability-score maximization, as governing rule), its channels and participation structure (interaction structure), and its candidate invariants — using the extended methodology fixed in A1 and A2.
- **Phase C — Envelope (Discrete Mode 1).** Extract the substrate's forbidden/necessary patterns, reachability bounds, and envelope constraints.
- **Phase D — Extremal Dynamics (Discrete Mode 2).** Extract the substrate's fronts, extremes, universal bounds, and attractor structure.
- **Phase E — Constraint Surface (Discrete Mode 3).** Construct the substrate's channel space, faces, closure status, and surface type.
- **Phase F — Criteria Evaluation (Step 5).** Apply the six substrate-level criteria to the substrate; render PASS/CONDITIONAL/FAIL with evidence; compile the constraint census.
- **Phase G — Generalization (Step 6).** Determine whether the substrate constitutes a new pole or a cross-domain invariant; integrate with the determinability-boundary note and the FS parallel.

**Immediate next action:** begin **Phase B — Architectural Specification of the ED substrate**, using the extended AD framework. The methodology is fixed; the evaluation begins.

---

*End of Phase A2. Three discrete extraction modes — envelope, extremal dynamics, constraint surface — defined for the general class of discrete relational architectures, fixed before any evaluation. With A1 and A2 filed, AD's substrate-level extension is complete and Phase B begins the evaluation proper.*
