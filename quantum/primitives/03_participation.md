# Primitive 03 — Participation

**Role in the framework:** The relational substrate. Participation is the relation that holds between micro-events — the bare structural fact that micro-events can integrate with one another's becoming. It is what makes chains (Primitive 02) possible, what space and time emerge from (ED-10 §2–3), and what entanglement, interference, and measurement are all consequences of. Together with Primitives 01 and 02, it forms the core triad of ED.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Participation** is the relation that holds between micro-events when they integrate each other's becoming. It is not a force, not a field, not an exchange of information, not a physical medium. It is the relational structure itself — the fact that becoming can be *shared*.

Where Primitive 01 establishes the atoms and Primitive 02 establishes the first composite (sequences of atoms with rules), Primitive 03 establishes the fabric between them. A micro-event is not isolated. It integrates. *How* it integrates — with which other micro-events, in what patterns, with what timing — is participation.

### What participation *is*

Participation has three inseparable aspects:

- **A relation among micro-events.** Given two (or more) micro-events, they either participate or they do not. Participation is the structural fact that one micro-event's becoming is integrated into another's.
- **A substrate for chains.** A chain (Primitive 02) is a sequence of micro-events held together by a consistent update rule. The rule is applied *through* participation — each step of the chain requires that the next micro-event participate with the previous one in the pattern the rule specifies. Without participation, no rule can be instantiated; without rules being instantiated, no chains exist.
- **A geometric potential.** Participation structure has shape. It can be rich or sparse, locally thick or globally non-trivial, adjacent or distant, uniform or curved. All the geometry of the emergent world — distance, curvature, horizons, light cones — is the thick-regime coarse-graining of participation structure.

### What participation is *not*

- **Not a force.** Forces push or pull; participation holds. A force would be a way that one micro-event dynamically affects another across distance; participation is the prior condition that makes "affecting" possible at all. Forces, in the thick regime, are patterns in how participation distributes itself — ED-10 §7.2 makes this explicit for gravity.
- **Not a field.** A field is a value assigned to every point of a pre-existing manifold. Participation is prior to manifolds (ED-10 §2). The field description that classical physics uses is the coarse-grained summary of participation structure once thickening (Primitive 12) has produced a classical manifold.
- **Not an exchange of information.** Information transfer presupposes stable committed states on both ends (ED-10 §5). Participation is more basic — it is what those states are built from. Two entangled particles "share participation," but nothing travels between them (ED-I-02 §4–§5).
- **Not bandwidth.** Participation bandwidth (Primitive 04) is the *measure* of participation — how rich the relation is. Participation is the relation itself. Bandwidth is like "how much" you have; participation is like "that you have any at all."
- **Not a channel.** A channel (Primitive 07) is a *stable pathway* through the participation structure. The channel is a pattern. Participation is the substrate that supports patterns.

The three are distinct: participation (relation), bandwidth (measure of the relation), channel (stable structure in the relation).

### Why participation, not interaction

Standard physics talks about particles "interacting." The word hides an ontological assumption: that there are pre-existing particles, pre-existing space, and then the interaction happens across space. ED inverts this. There are no pre-existing particles (chains are composites; Primitive 02 §1). There is no pre-existing space (space is the thick-regime shadow of participation adjacency; ED-10 §2). What there *is*, at the ontological base, is participation — and everything else (particles, space, interactions) is a coarse-grained summary of what participation is doing.

---

## 2. Mathematical Object

### Candidate structure

In the participation-graph formulation of Primitive 01 §2, participation is the **(weighted) edge structure** of the graph:

- Vertices = micro-events
- **Edges = participation relations** (this is Primitive 03)
- Edge weights = participation bandwidth (Primitive 04)
- Directed edges (a subset) = commitment order

So: if the full structure is a weighted directed graph, then:
- Primitive 01 gives us the vertex set
- Primitive 03 gives us the edge set
- Primitive 04 gives us the edge weights
- Commitment ordering (part of Primitive 11) gives us the direction on the subset of edges that are ordered

### Higher-order structure

A strict pairwise-edge formulation may be insufficient. Several phenomena suggest participation can be irreducibly k-ary:

- **Multi-particle entanglement** where the joint structure is not reducible to pairwise correlations (e.g., GHZ states, W states). These may require participation that is intrinsically 3-ary or higher.
- **Topological effects** (ED-I-14) where the global participation structure of a loop is distinct from any pairwise decomposition along the loop.
- **Gauge-like behavior** where what matters is a closed-loop integral over participation structure.

The natural generalizations are:

- **Hypergraph**: edges can connect any number of vertices. Hyperedges naturally express k-ary participation.
- **Simplicial complex**: higher-dimensional "cells" (triangles, tetrahedra) express participation relations among groups. Gives native structure for cycles, loops, and topological invariants.

The simplicial-complex option is the richest and is likely the correct formalization for the topological / Aharonov-Bohm phenomena, because simplicial complexes carry native homology and cohomology, which are exactly the mathematical structures that classify non-trivial topological phase effects. But it is not yet established that the simplicial version is required for all phenomena — the hypergraph version may suffice, or plain graph edges with the higher-order structure emerging from edge patterns.

### What is *not yet* settled

- **Pairwise vs. k-ary.** See above. Phase 1 open.
- **Symmetric or asymmetric.** Is participation always symmetric (if A participates with B, then B participates with A)? Likely yes for participation itself (the relation is mutual), but the *timing* of participation (Primitive 13) can be asymmetric — one micro-event can precede another in commitment order.
- **Discrete or continuous.** Participation between two specific micro-events is either present or absent (discrete). But in the aggregate — the participation density between two regions — the description is effectively continuous in the thick regime. Where does the transition happen, formally?
- **Participation topology.** If participation is a simplicial complex, what topological invariants are physically significant? Homology classes, presumably — and the ED-I-14 paper strongly suggests Aharonov-Bohm / Berry phase effects are about participation-graph homology. Needs formal development.

---

## 3. Relations to Other Primitives

### Participation is built on

| Primitive # | Role |
|---|---|
| 01 Micro-event | The atoms that participation relates |

Participation has one upstream dependency: it needs vertices (micro-events) to relate. It does not depend on chains (Primitive 02), because participation is prior — a chain is built *through* participation.

### Participation is the substrate for

| Primitive # | How it uses participation |
|---|---|
| 02 Chain | A chain's update rule is instantiated through participation — each step requires the next micro-event to participate with the previous in the rule-specified pattern |
| 04 Participation bandwidth | The measure of participation richness — how much participation is present, not whether |
| 05 Event density | ED at a region is a count measure on micro-events, but the *region itself* is defined by participation adjacency (ED-10 §2.2) |
| 06 ED gradient | A gradient exists across participation structure; without participation, there is no "across" |
| 07 Channel | A channel is a stable pathway through participation — a locally coherent sub-structure of the full participation relation |
| 08 Multiplicity | The count of distinct channels is a count of distinct participation-pathway types available in a region |
| 09 Tension polarity | A phase relation between a chain's update rule and local participation direction |
| 10 Individuation | The threshold for distinct identity — enough participation internal to a system to support a local rule, distinct from shared participation with another system |
| 11 Commitment | A commitment event selects from available participation channels; without participation structure, there is nothing to select from |
| 12 Thickening | The accumulation of many stable participation patterns produces classical structure |
| 13 Relational timing | Phase relations *within* participation structure; the rhythmic aspect of how participation updates |

### Circular-definition flags — where Participation leans on not-yet-defined primitives

Two flags, smaller than Chain's because Participation is closer to the ontological base:

1. **"Integration" in §1** is the intuitive word for what participation *does* — one micro-event's becoming is integrated into another's. The formal content of "integration" bottoms out in bandwidth (Primitive 04) as the measure of how much integration is happening. Until 04 is drafted, "integration" is understood operationally.

2. **"Participation structure has shape"** in §1 is a deliberate pre-reference to Primitive 06 (ED Gradient) and Primitive 07 (Channel). The shape of participation structure produces gradients and channels. These are downstream but load-bearing — the claim that participation has a geometric potential to produce space, curvature, horizons, etc., presupposes that there is structure in participation to have shape in the first place.

### The core triad

Primitives 01 + 02 + 03 are designed to be a self-contained starting triad. With these three:

- You have the atoms (01)
- You have the composites that persist across atoms (02)
- You have the fabric that holds atoms and composites together (03)

Everything from Primitive 04 onward either measures something in this triad (04, 05, 08) or refines structure within it (06, 07, 09, 10, 11, 12, 13). This is why once 01–03 are drafted, the skeleton is in place for the predictions catalog — because chains operating through participation is the core of every application in the ED-I catalog.

---

## 4. Measurable Signature

Participation itself is not directly observable. What's observable are its **consequences** — all of them, across all physics.

### Direct observable consequences

- **Coherence times.** How long a quantum system maintains a coherent state is how long its participation bandwidth with the environment is low enough that its internal participation structure is not disrupted. Coherence time = participation-maintenance time (ED-09 §6; ED-I-04 §5).
- **Correlation strength in entangled systems.** Entanglement correlations (Bell inequality violations, CHSH ≈ 2.828) are the statistical signature of shared participation structure (ED-09 §5.4; ED-I-02 §4). The strength of the correlation measures the degree of shared participation.
- **Distance itself.** The fact that any two regions have a "distance" between them is participation's observable signature in the thick regime (ED-10 §3.2). High participation adjacency → short distance; low participation adjacency → long distance; zero participation → causal disconnection.
- **Light cones.** The maximum rate at which participation can propagate defines causal cones (ED-10 §8.1, §8.6). The existence of an invariant speed c is the observable manifestation of participation's propagation limit.
- **Superconducting and superfluid phenomena.** Dissipationless flow in superconductors is the observable signature of a shared participation structure spanning the material (ED-I-23 §3). Cooper pair coherence is participation coherence at the pair level.
- **Interference patterns.** Double-slit interference, Mach-Zehnder interference, and all interference phenomena are the participation field's geometric structure expressed in detection statistics (ED-I-07 §2, §7).
- **Topological phase effects.** Aharonov-Bohm, Berry, Aharonov-Casher phases are observable signatures of participation geometry with non-trivial global topology (ED-I-14).

### Indirect observable consequences

Essentially all of physics. Because participation is what makes chains, gradients, channels, and eventually space and time possible, every physical phenomenon is in some sense "what participation is doing" at some scale. The question isn't whether a phenomenon relates to participation; it's what aspect of participation a given phenomenon reveals.

### Operational handle (simulator / PDE)

- **ED-Arch simulator.** In Scenario E, the participation structure is implemented as the local interaction between lattice sites — each site's update depends on a local neighborhood. This implements participation at the simulation scale: sites that are in each other's interaction neighborhood are the simulated participation adjacency. The fact that cores persist, interact, and show regime boundaries (ED-Arch-07, ED-Arch-08) is the simulated signature of participation structure at work.
- **Q-C Boundary PDE.** The effective channel weight `D(x)` implicitly carries the participation structure through its coupling to the underlying ED field. A chain with D < 0.1 is in a participation regime where many channels are supported (high-multiplicity, thin participation). A chain with D > 0.5 is in a regime where participation has thickened into single-channel commitment. The PDE is the continuum description of participation-regime dynamics for a propagating chain.

---

## 5. Example Applications

### 5.1 Entanglement as shared participation structure

Two entangled particles are not two separate systems with coordinated outcomes. They are a single participation structure expressed at two endpoints (ED-I-02 §3, §5). The participation bandwidth that would normally individuate one system from the other has not accumulated internally to either; the systems share the participation bandwidth of the parent.

Perfect correlations follow because there is one participation structure completing itself in two locations — not two structures mysteriously coordinating. No information travels because there is no transmission of a substance; the structure was already shared. Bell inequality violations quantify the degree of sharing.

This is the cleanest application of Participation as the primary primitive: entanglement is participation itself, at its clearest.

### 5.2 Distance and locality from participation adjacency

Two regions are "near" each other when their participation adjacency is strong — when micro-events in one region reliably integrate with micro-events in the other (ED-10 §3.2). Distance is inverse participation resistance. Regions with low participation adjacency "feel distant"; regions with zero participation bandwidth are causally disconnected.

Locality — the classical intuition that only nearby things affect each other — is a large-scale statistical regularity of thick participation networks (ED-10 §4.3). It's not fundamental. It's a property of the regime in which participation is thick enough that aggregate behavior looks smooth and local.

This is why quantum nonlocality (entanglement across arbitrary distance) is not mysterious in ED: the correlations are shared participation structure, and distance is inverse participation. A shared structure isn't less shared because it spans two endpoints that have high inverse-participation to each other in the surrounding participation manifold. Locality is a thick-regime regularity that shared-participation phenomena don't respect because they aren't part of the thick regime.

### 5.3 Measurement as forced participation

A measurement device is a high-multiplicity, high-bandwidth participation structure (ED-I-02 §6; ED-09 §7.5). When a low-ED (thin-participation) system interacts with it, the device's participation structure overwhelms the system's internal participation structure. The system cannot maintain its multi-channel uncommitted state because the device's dense participation forces individuation.

The measurement outcome is which channel the system commits to. The Born rule probability (|ψ|²) is, in ED, the participation weight of each channel — how much participation bandwidth each channel had before commitment (ED-09 §4.2, §7.4).

Measurement does not require an observer, consciousness, or knowledge. It requires only a thick participation structure forcing individuation of a thin one. This is the ED dissolution of the measurement problem.

### 5.4 Light cones as participation limits

The maximum rate at which participation can propagate is finite (ED-10 §8.1). This rate is what classical and quantum frameworks call c. Light cones are participation cones — the regions within which one micro-event's becoming can integrate with another's.

Inside the cone: participation bandwidth is nonzero, integration is possible, causal influence can propagate. Outside the cone: participation bandwidth is zero, no integration, causal disconnection.

Entanglement correlations can span outside of cones because entanglement is *not* participation propagation — it is *shared* participation structure that existed before the endpoints separated. No new participation crosses the cone; the existing shared structure resolves jointly.

### 5.5 Topological effects as participation geometry

Aharonov-Bohm, Berry phase, Aharonov-Casher: a chain traversing a closed loop picks up a phase that depends on the global participation geometry enclosed by the loop, not on any local force or local field along its path (ED-I-14 §4–§7).

In ED, this is immediate: participation has geometric structure, and when the structure is topologically non-trivial (a hole in the participation manifold, or a singularity in participation adjacency), a chain transported around the hole acquires an identity-alignment shift that reflects the enclosed topology. No gauge potential is needed because participation geometry *is* what gauge potential was a bookkeeping device for.

This is where the channel-exists-before-the-pattern principle lands most cleanly. The participation structure exists before the chain traverses it. The chain's phase shift is the chain registering the participation topology. Shielding local fields doesn't help because shielding is a local operation and participation topology is global.

### 5.6 Superposition persistence in isolation

A system with low participation bandwidth with its environment (well-isolated, thin participation to outside) maintains its internal multi-channel participation structure — which classical QM calls superposition (ED-09 §4.4). The superposition doesn't persist because of some special quantum rule; it persists because nothing outside the system has enough participation with it to force individuation.

Break isolation (increase environmental participation bandwidth) → individuation forced → single-channel commitment → "collapse."

This is the ED account of why superposition is fragile outside of careful laboratory conditions and why it is nearly impossible to maintain at macroscopic scales. Macroscopic systems are highly individuated with their environments (lots of thick participation); microscopic systems can be isolated to low-bandwidth participation regimes where thin uncommitted structure survives.

---

## 6. Simulator / PDE Instantiation

### Participation in the ED-Arch simulator

Participation is implemented at two levels in the simulator:

1. **Local neighborhood coupling.** Each lattice site updates based on its immediate neighbors. This implements pairwise participation adjacency — the site "participates" with its neighborhood, and its update is determined by integrating that neighborhood's state.

2. **Emergent core interactions.** When stable cores form (ED-Arch-07, ED-Arch-08), the interaction between two cores — whether they annihilate, merge, or hover/orbit — is an emergent participation relationship at the core-chain scale. The two cores "participate" as macroscopic chains, and their interaction is participation composition at the chain level.

The γ-sweep in ED-Arch-08 shows that as γ (the suppression exponent) increases, cores become more rigid and their interaction manifold sharpens. In participation terms, higher γ means participation structure is more stiffly maintained — the ED field resists rearrangement that would destroy participation adjacency patterns. Stiffer participation = more architectural quantization = the emergence of discrete behavior.

### Participation in the Q-C Boundary PDE

The PDE (ED-Phys-16/17, P6, 00.3) is a continuum equation for the effective channel weight `D(x)` along a propagating chain. Implicitly, it assumes:

- Participation structure is dense enough to have a continuum description at the level of D
- `D < 0.1`: thin participation, multi-channel uncommitted regime
- `D > 0.5`: thick participation, single-channel committed regime
- `D = 0.5` exactly: the sharp transition

The specific quantitative predictions (N_osc ≈ 9, Q ≈ 3.5, triad ≈ 0.03, 3–6% third-harmonic) are all features of chain dynamics in a specific participation regime. The PDE is the coarse-grained description of participation-regime transitions during chain propagation.

### What's missing

- **Formal derivation from discrete participation structure to the continuum PDE.** What coarse-graining exactly produces `D(x)` from the underlying discrete participation graph? Phase 2 / Phase 4 task, flagged in Primitive 01 §6 and Primitive 02 §6.
- **Gauge / topological participation formalism.** The Aharonov-Bohm interpretation requires that participation structure carries topology (homology classes). Formalizing this — so ED has an explicit participation-cohomology theory — is a major theoretical target.
- **Participation algebra for entanglement.** What formal operation composes two chains into a shared participation structure (entangled state)? What operation factors an entangled structure into two individuated chains (decoherence)? These need precise definitions in terms of participation-graph operations.

---

## 7. Open Questions

1. **Pairwise vs. higher-order participation.** Already flagged in §2. Does the formal structure require hypergraph/simplicial-complex generalizations, or is pairwise enough? Matters for many-body entanglement, for gauge structure, for topological phenomena. Phase 1 / 2 open.

2. **Participation and the emergence of gauge theory.** The ED-I-14 paper strongly suggests that what classical physics calls "gauge potentials" are bookkeeping devices for participation-geometry topology. Making this formal — showing that U(1), SU(2), SU(3) gauge structures arise as specific participation-topology classes — would be one of the most consequential derivations in the program. Phase 2 / 3 target.

3. **Participation across horizons.** Horizons are participation bottlenecks (ED-10 §4.4, §8.2). Entanglement spans horizons because it's shared participation structure, not participation flow. The formal mechanism — how participation structure remains shared across a participation bottleneck — needs explicit treatment. This is the ED account of black hole complementarity / firewall paradoxes / holographic information (ED-10 §8.5).

4. **The η thread — participation selection in saturated regimes.** The baryon-to-photon ratio η ≈ 6 × 10⁻¹⁰ emerges (ED-I-11) from the fact that in the early universe's saturated ED-flow, only aligned-tension chains could have their update rules instantiated. The deep reason is a **participation selection rule**: saturated participation structure can only support rules that are phase-aligned with the local relaxation direction. Anti-aligned rules require participation rearrangement that saturation forbids. Formalizing this selection rule — precisely what structural property of participation makes it select aligned-tension and decohere anti-aligned-tension — is the path to deriving η from first principles. **Phase 4 target; the highest-leverage open problem in the program.**

5. **Relationship between participation and event density.** Primitive 05 (ED) is a scalar count of micro-events per region. Primitive 03 (Participation) is the relational structure. They are tightly coupled (dense ED generally means dense participation) but distinct (two regions could have high ED but low mutual participation, if the micro-events don't integrate across the region boundary). The formal relationship — whether ED is derivable from participation or vice versa, or whether both are independent primitives — needs clarification in drafting Primitive 05.

6. **Participation dynamics.** Participation structure is not static. New participation relations form (commitment events), existing ones strengthen (thickening), and some are disrupted (decoherence, horizon formation). What is the dynamical equation governing participation-structure evolution? This is the most general form of the question the Q-C Boundary PDE partially answers — and a complete answer would be the fundamental equation of ED. Phase 4 target.

---

## 8. Citation format for other ED work

When citing this primitive from elsewhere:

> *Per `quantum/primitives/03_participation.md` §1* — for the definition of participation as relational substrate.
> *Per `quantum/primitives/03_participation.md` §2* — for the mathematical object (edge structure of the participation graph).
> *Per `quantum/primitives/03_participation.md` §3* — for the relations to other primitives.
> *Per `quantum/primitives/03_participation.md` §5.5* — for the topological-phase / Aharonov-Bohm application.
> *Per `quantum/primitives/03_participation.md` §7 (4)* — for the η derivation thread.

---

## 9. One-line summary

> **Participation is the relation that holds between micro-events when they integrate each other's becoming. It is the relational substrate — not a force, not a field, not a medium, not a channel — and it is what chains ride on, what space and time emerge from, what entanglement is shared across, what measurement forces, and what topological phases register. Together with micro-events (01) and chains (02), it is the core triad of ED.**
