# Phase A1 — Substrate-Level AD Criteria

**Evaluation:** Architectural Distillation of the Event Density substrate
**Phase:** A1 (criterion reformulation)
**Status:** Methodological extension — to be fixed before any evaluation
**Date filed:** June 2026
**Author:** Allen Proxmire
**Follows:** `Phase_A_CriterionMapping.md` (which determined that three criteria require reformulation)

---

## 1. Purpose

Phase A determined that three of AD's six criteria — **locality, determinism, envelope tightness** — do not transfer to a discrete relational substrate in their continuum wording, and that they require reformulation before the substrate can be evaluated without distortion. This document produces those reformulations.

Two constraints govern this document, and they are not negotiable:

- **The criteria are general, not ED-specific.** Each substrate-level criterion below is stated for *any discrete relational architecture* — any system of nodes, edges, and a local update rule. The Event Density substrate is the eventual object of evaluation, but it appears nowhere in the definitions. A criterion written so that ED satisfies it is worthless; a criterion written for the general class, against which ED is later scored, is the only kind that carries information.

- **The criteria are fixed before evaluation.** This document precedes Phase B. Per the circularity guard (Memo-00 §5), the criteria must be stated in full and independently before the substrate is measured against them. Once filed, these definitions are the standard; the substrate's verdict in Phase F falls where the evidence puts it, against criteria that were not written to accommodate it.

This is methodological work: extending AD's criterion set downward to the discrete substrate level, stated generally. It is not an evaluation and reaches no verdict about any system.

---

## 2. Criteria Requiring Reformulation

Phase A identified three criteria whose continuum wording lacks a direct substrate referent.

**Locality.** *Continuum AD:* evolution at a point depends only on the state and its derivatives at that point or an infinitesimal neighborhood. *Why it does not transfer:* a discrete substrate has no derivatives and no points-with-neighborhoods in the continuum sense; it has nodes, edges, and graph-distance. "Local" must be redefined graph-theoretically, and the continuum assumption of unbounded propagation speed conflicts with a substrate whose reach is finite.

**Determinism.** *Continuum AD:* well-posedness — existence, uniqueness, and continuous dependence on initial data, with initial data determining evolution for all time. *Why it does not transfer:* "continuous dependence" has no referent without a continuum metric; "for all time / everywhere" assumes unbounded determination, which a finite-reach substrate does not provide; and a substrate whose update is a local selection (e.g., a maximization) raises a uniqueness question the continuum criterion never poses. The irreversibility of the substrate, by contrast, is *not* a mismatch — it is shared with the irreversible (parabolic) continuum shadow — and so the reformulation drops the backward-determination assumption rather than treating irreversibility as a defect.

**Envelope tightness.** *Continuum AD:* the system's bounds are sharp — saturated by actual solutions — and the envelope is closed. *Why it does not transfer:* "saturated by a solution" presumes a function-space solution; the discrete analogue is saturation by an explicit configuration, and the envelope itself — the set of admissible, reachable states — must be defined over graph configurations before its tightness is meaningful.

The remaining three criteria — minimality, generative sufficiency, structural optimality — are domain-agnostic and transfer without reformulation (Phase A §2). They are not restated here.

---

## 3. Substrate-Level Criterion: Locality

### 3.1 The setting

A discrete relational substrate is a graph of nodes (the substrate's discrete constituents) connected by edges (adjacency relations), evolving under an update rule that assigns each node its next state. There is a graph metric: the distance between two nodes is the number of edges on the shortest path between them.

### 3.2 What counts as a local update

An update rule is **graph-local** if the next state of any node depends only on the states of nodes within a bounded graph-distance of it. Formally: there exists a finite **locality radius** *r* such that, for every node, the rule's output at that node is a function only of the configuration on the ball of radius *r* around it. No term in the update rule may depend on the global configuration, on nodes at unbounded distance, or on aggregate quantities computed over the whole graph (a single quarantined zero-dimensional aggregate, if structurally necessary and confined, is the discrete analogue of AD's permitted quarantined nonlocal sector and must be identified and bounded as such).

### 3.3 Finite reach and decoupling surfaces

Continuum locality permits unbounded propagation speed — a parabolic law spreads influence everywhere instantly. A discrete substrate need not, and a substrate with **finite reach** propagates influence at most *r* edges per update step. Over *t* steps, influence reaches at most distance *r·t* — a discrete causal cone.

Finite reach is therefore **a strengthening of locality, not a violation of it.** Where the substrate carries **decoupling surfaces** — boundaries beyond which reciprocal influence ceases — those surfaces bound effective reach more tightly still: influence may be one-sided across them or absent entirely. The locality criterion must *recognize* decoupling surfaces as legitimate reach boundaries, not flag them as anomalies. A decoupling surface is a place where locality is, if anything, maximally enforced.

### 3.4 The general criterion

> **Direct, graph-local, finite-reach locality.** A discrete relational substrate satisfies locality if:
>
> 1. **Direct** — no term of the update rule depends on the global configuration or on nodes at unbounded graph-distance; any aggregate dependence is a single confined, structurally necessary, explicitly identified sector.
> 2. **Graph-local** — there exists a finite locality radius *r* such that each node's update depends only on the configuration within graph-distance *r* of it.
> 3. **Finite-reach** — influence propagates at most *r* edges per update step (a discrete causal cone *r·t*), and any decoupling surfaces are honored as consistent reach boundaries.
>
> Finite reach and decoupling surfaces count *toward* locality, not against it.

A substrate fails this criterion if its update rule requires unbounded-distance dependence that cannot be confined to a single justified sector, or if its propagation violates a stated reach bound.

---

## 4. Substrate-Level Criterion: Determinism

### 4.1 The continuum starting point

AD's determinism is well-posedness: existence, uniqueness, and continuous dependence on initial data, with initial data determining the evolution for all time. Three features of a discrete relational substrate require this to be reformulated, and one apparent feature does not.

**Requires reformulation:**

- **Forward-only evolution.** If the substrate's update is irreversible — each step commits and cannot be undone — the criterion cannot demand backward determination. (This is *not* a weakening: the irreversible continuum shadow, a parabolic law, is itself forward-well-posed and backward-ill-posed. Forward-only is the discrete root of an irreversibility the continuum already has. The reformulation states determinism forward, and that is the honest form, not a relaxed one.)
- **Finite reach.** Determination cannot be "for all time everywhere" when influence has a bounded reach. A region's evolution is determined by data within its reach horizon and is structurally independent of data beyond it.
- **Unique local selection.** If the update rule selects each next state by a local optimization (a maximization of a score, or any local selection principle), determinism requires the selection to be unambiguous — the optimum must be unique, or the ambiguous configurations must be non-generic and accompanied by a stated tie-breaking rule. The continuum criterion does not pose this, because a differential equation's uniqueness is a property of the equation, not of a per-step selection.

**Does not require reformulation:** the *existence and forward-uniqueness* of evolution carries over directly, and "continuous dependence" maps to a discrete *stable dependence* (bounded sensitivity), which is a restatement rather than a new demand.

### 4.2 The general criterion

> **Substrate-level determinism.** A discrete relational substrate is deterministic if all four hold:
>
> 1. **Forward determinism.** From any admissible configuration, the update rule produces a unique next configuration. Iterated, initial data generates a unique forward trajectory. Backward determination is *not* required.
> 2. **Stable dependence.** A bounded perturbation of the initial configuration, measured in a discrete configuration metric (e.g., edit distance on node states and edges), produces a bounded change in the trajectory over bounded time. Small differences in input do not amplify without bound over finite horizons.
> 3. **Reach-bounded determination.** The forward evolution of any region is uniquely determined by the initial data within that region's reach horizon, and is independent of data beyond it. Determination is bounded by reach; what lies beyond the horizon is structurally undetermined from inside it.
> 4. **Unique local maximizer.** If the update rule is a local selection (optimization), the selected next state is generically unique. Configurations admitting ties are non-generic and, where they occur, are resolved by a stated, deterministic tie-breaking rule.

A substrate satisfies determinism only if all four hold. Failure of (1) means the dynamics are non-deterministic; failure of (2) means sensitive dependence without bound (a discrete chaos that defeats prediction at finite resolution); failure of (3) means determination leaks across reach boundaries (inconsistent with finite reach); failure of (4) means the update rule is ambiguous and the "trajectory" is not single-valued.

### 4.3 Note on component (3)

Component (3), reach-bounded determination, is the component with **no continuum analogue.** It is where finite reach enters the determinism criterion, and it is the formal seat of a substrate's *determinability boundary* — the structural distinction between what the substrate determines (in-horizon) and what it cannot (beyond-horizon). This component is what makes substrate-level determinism a genuinely new criterion rather than a translated one, and it is the component most worth examining when any specific substrate is later evaluated.

---

## 5. Substrate-Level Criterion: Envelope Tightness

### 5.1 The continuum starting point

AD's envelope tightness asks whether the system's bounds are sharp — saturated by actual solutions — and whether the envelope is closed (all faces sealed, the dynamics cannot escape). The discrete analogue requires defining the envelope over graph configurations and replacing "solution" with "configuration."

### 5.2 The discrete envelope

For a discrete relational substrate, define:

- **Forbidden configurations** — graph patterns (subgraph motifs, state assignments) that the substrate's axioms/primitives **disallow**. These are the patterns excluded a priori, traceable to a specific primitive.
- **Necessary configurations** — graph patterns that the update rule **forces** into existence under admissible evolution. These are the patterns guaranteed to appear.
- **The envelope** — the set of participation-graph states that are **reachable** under the update rule from admissible initial configurations. The envelope is the realized state space: everything the dynamics actually produces.

### 5.3 Ghost states and tightness

The key discrete notion is the **ghost state**: a configuration that the axioms *permit* but the update rule *never reaches.* A ghost state is exactly architectural slack — the axioms are looser than the dynamics, admitting structure the system's own evolution never realizes. A tight envelope is one in which the admissible set (what the axioms allow) and the reachable set (what the dynamics produce) coincide: no slack, no ghosts.

### 5.4 The general criterion

> **Discrete envelope tightness.** A discrete relational substrate has a tight envelope if:
>
> 1. **Forbidden patterns are structurally forbidden** — every disallowed pattern is excluded by a primitive or axiom, not merely absent in observation. The exclusion is structural, traceable, and exact.
> 2. **Necessary patterns are forced** — every necessary pattern is guaranteed by the update rule under admissible evolution, not merely typical or frequent. The forcing is structural, not statistical.
> 3. **No ghost states** — there is no configuration admitted by the axioms but unreachable under the update rule. The admissible set and the reachable set coincide; the architecture carries no slack between what it permits and what it produces.
> 4. **Envelope closure is decidable in principle** — there exists a well-defined procedure (however expensive) to determine whether a given configuration is inside the envelope (admissible and reachable) or outside it. The envelope's boundary is sharp enough to be a decision problem, not a vague region.

A substrate fails this criterion if forbidden patterns are merely unobserved rather than excluded, if necessary patterns are typical rather than forced, if ghost states exist (axiom-admissible but dynamically unreachable configurations — the discrete signature of a loose architecture), or if envelope membership is not decidable even in principle.

### 5.5 Note on the ghost-state condition

Condition (3), no ghost states, is the discrete counterpart of AD's "tight, not loose" — the place where envelope tightness most directly tests whether an architecture's axioms are doing the same work as its dynamics. A system with ghost states has axioms that permit more than the dynamics deliver, which is precisely the architectural looseness AD's continuum envelope-tightness criterion was built to detect. The condition transfers the diagnostic intact into discrete terms.

---

## 6. Summary Table

| Criterion | Continuum Definition (AD) | Substrate-Level Definition | Notes |
|---|---|---|---|
| **Locality** | Evolution at a point depends only on local state and its derivatives; no nonlocal operators | **Direct, graph-local, finite-reach:** update depends only on a bounded-radius graph neighborhood; influence propagates at a bounded rate; decoupling surfaces are honored as reach boundaries | Finite reach counts *toward* locality; a quarantined zero-dimensional aggregate is the only permitted nonlocal sector |
| **Determinism** | Well-posedness: existence, uniqueness, continuous dependence; determination for all time | **Four components:** (1) forward determinism (unique next state, no backward requirement); (2) stable dependence (bounded sensitivity in a discrete metric); (3) reach-bounded determination (in-horizon data only); (4) unique local maximizer (no update degeneracy) | Component (3) has no continuum analogue; it is the formal seat of the determinability boundary |
| **Envelope Tightness** | Bounds sharp, saturated by solutions; envelope closed | **Four conditions:** forbidden patterns structurally excluded; necessary patterns dynamically forced; **no ghost states** (admissible = reachable); envelope membership decidable in principle | Ghost states are the discrete signature of architectural slack; their absence is the discrete "tight, not loose" |

The three reformulated criteria, together with the three that transfer directly (minimality, generative sufficiency, structural optimality), constitute the full substrate-level AD criterion set. They are stated for the general class of discrete relational architectures; no system-specific content appears in any definition.

---

## 7. Next Actions

Phase A1 has fixed the reformulated criteria. The remaining methodological prerequisite is the discrete restatement of AD's three-mode extraction engine — the process by which the envelope, extremal dynamics, and constraint surface are derived for a discrete substrate rather than a continuum law.

**Next document: `Phase_A2_DiscreteExtraction_Modes.md`** — defining:
- **Mode 1 (discrete):** how to derive the envelope (forbidden/necessary configurations, structural invariants) from the substrate's primitives alone.
- **Mode 2 (discrete):** how to derive extremal dynamics (reach-horizon behavior, strain relaxation, stability of the update rule, irreversibility consequences) from the update rule.
- **Mode 3 (discrete):** how to derive the constraint surface (channel/participation interaction geometry, impossible and forced combinations) from the interaction structure of the participation graph.

After Phase A1 (criteria) and Phase A2 (extraction modes) are both filed, the methodological extension is complete and the evaluation proceeds:

- **Phase B** — Architectural Specification (Step 1), against the extended methodology.
- **Phases C–E** — Envelope, extremal dynamics, constraint surface (Steps 2–4), using the discrete extraction modes.
- **Phase F** — Criteria evaluation (Step 5): the six criteria — three transferred, three reformulated here — applied to the substrate.
- **Phase G** — Generalization (Step 6).

**Immediate next action:** draft `Phase_A2_DiscreteExtraction_Modes.md`. With the criteria fixed (A1) and the extraction modes defined (A2), the substrate evaluation can begin at Phase B against a methodology that was settled before the substrate was scored against it.

---

*End of Phase A1. Three substrate-level criteria — locality, determinism, envelope tightness — stated as general criteria for discrete relational architectures, fixed before any evaluation. No system-specific content appears in the definitions. Phase A2 defines the discrete extraction modes next.*
