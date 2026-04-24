# Primitive 01 — Micro-event

**Role in the framework:** Atomic unit of becoming. Everything else in ED is built from micro-events or from relations between them.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

A **micro-event** is a discrete act of becoming. It is the smallest possible event — the atomic unit from which all structure in ED is composed.

### What a micro-event *is*

A micro-event is defined entirely and exclusively by:

- Its **participation relations** — what other micro-events it integrates with, and how
- Its **commitment order** — its position in the irreversible sequence of commitments
- Its **integration into other micro-events** — how it contributes to composite structures (chains, networks, fields)

A micro-event is not a point-particle, not a field excitation, not a spacetime event in the GR sense, not a collapse event in the QM sense. It is prior to all of those.

### What a micro-event is *not*

Explicitly, a micro-event does not have:

- **Position** — micro-events are not located in space, because space does not yet exist at the micro-scale. Space emerges from stable participation adjacency between micro-events (see Primitive 03 §5, and ED-10 §2).
- **Extension** — a micro-event has no size, no volume, no spatial footprint.
- **Duration** — a micro-event does not persist through time, because time itself is the coarse-grained appearance of commitment ordering. A micro-event is a discrete act, not a temporal interval.
- **Trajectory** — a micro-event does not move. What appears as motion in the macro regime is the migration of a pattern of committed micro-events across regions; the individual micro-events do not travel.
- **Persistent identity** — a micro-event does not continue existing. It commits, contributes to the participation structure, and is done.
- **Embedding in a manifold** — micro-events are not "in" spacetime. Spacetime is the thick-participation classical summary of dense committed micro-event patterns (ED-10 §2–§4). There is no background the micro-events live on.

### Why this inversion matters

Every framework with a QM-measurement problem, a quantum-gravity tension, a singularity problem, or a wave-particle puzzle assumes spacetime or field-on-spacetime as fundamental. ED does not. The micro-event as atomic unit is the ontological move that makes the rest of the framework possible:

- No measurement problem: measurement = commitment of a micro-event (Primitive 11)
- No wave-particle duality: wave and particle are two coarse-grainings of micro-event patterns (ED-09 §2.2)
- No singularity problem: singularities are where the manifold approximation breaks down, not where physics fails (ED-10 §9.4)
- No quantum-gravity tension: quantum is thin-participation regime; classical spacetime is thick-participation regime; they are the same substrate in different regimes (ED-10 §7)

All of this hinges on micro-event being prior to space, time, field, and particle.

---

## 2. Mathematical Object

### Candidate structure

A micro-event is most naturally modeled as a **vertex in a directed graph**, where:

- Vertices are micro-events
- Directed edges encode commitment order (source committed before target)
- Undirected (or bidirectional) edges encode participation relations
- Edge weights encode participation bandwidth (Primitive 04)

This is not a spacetime graph (no embedding), not a causal set (causal sets presuppose a manifold-like causal structure), and not a spin network. It is a **participation graph**.

### Why a graph, not a scalar or field

- Scalar/field formulations presuppose a manifold the field lives on. Micro-events have no manifold.
- Graph formulations allow structure (edges, weights, connectivity patterns) without presupposing extension.
- Participation relations *are* edges. Commitment order *is* edge direction. Nothing needs to be added to the graph formalism to express the ontology.

### What is *not yet* settled mathematically

- Whether the graph is best modeled as a **simplicial complex** (so that higher-order participation relations among three or more micro-events have native structure), a **hypergraph** (similar motivation), or a **plain directed graph** (simplest; higher-order relations emerge from the pattern of pairwise edges).
- Whether the graph is **growing** (new micro-events added over "time," which is really over commitment-order) or whether the total graph is **given** and what we call time is a partial order on it.
- The right **measure** on the graph — is the number of micro-events per region (event density; Primitive 05) a count measure on vertices, or something finer?

These are Phase-1 and Phase-2 open questions. The load-bearing claim of this primitive does not depend on which refinement is correct: however it's refined, **micro-events are discrete atomic units, and they carry no intrinsic position, duration, or embedding.**

---

## 3. Relations to Other Primitives

| Composes from this | Primitive # | Relation |
|---|---|---|
| Chain | 02 | A chain is a sequence of micro-events with a consistent update rule |
| Participation | 03 | Participation is the relation that holds between micro-events |
| Event density (ED) | 05 | ED at a region = count/measure of micro-events integrated in that region |
| ED gradient | 06 | ED gradient = variation of ED across participation adjacency |
| Channel | 07 | Channel = stable sequence of participation pathways for a chain to follow |
| Commitment | 11 | Commitment is a discrete event in which a micro-event selects a single participation channel |
| Thickening | 12 | Thickening is the accumulation of many committed micro-events |
| Relational timing | 13 | Relational timing is the phase structure of participation integration between micro-events |

### Upstream dependencies of this primitive

None. Micro-event is the ontological atom.

---

## 4. Measurable Signature

### What is (in principle) observable

Individual micro-events are not directly observable. They are sub-Planck-scale by construction — Planck scale is where the manifold approximation breaks down (ED-10 §9.5), which is where discrete micro-events begin to dominate over the classical-thick regime.

Micro-events manifest observably through their **statistical and architectural signatures**:

- **Discrete outcomes** in quantum measurement (QM calls these quantized energy levels, quantized spin values, discrete photon detection events). Each measurement outcome = one committed micro-event (ED-09 §7.2).
- **Gradient saturation effects** at high ED. ED-Arch-08 demonstrated that as the suppression exponent γ increases, curvature wells stiffen and system behavior transitions from continuous to architectural/discrete. This is the operational signature of micro-event discreteness becoming visible at the simulation level.
- **Planck-scale cutoffs** in quantum field theory. The fact that QFT divergences are regulated at (or above) the Planck scale is, in ED, the signature that the underlying discrete substrate is there; continuum field theory breaks down because it is an approximation to a discrete substrate.
- **Cosmological-scale statistics**. The specific count of micro-events in the observable universe would set fundamental cosmological numbers (baryon-to-photon ratio, horizon entropy, etc.). See Primitive 05 for the counting mechanism.

### What is *not* observable about micro-events

The identity of an individual micro-event is not observable. There is no experiment that isolates "micro-event #73928." Micro-events contribute to statistical and architectural patterns; they do not present as individually trackable entities.

### Operational handle (simulator)

In the ED-Arch simulator, the discretization of the lattice and the single-step update rule effectively models micro-events as the atomic update units. Each lattice site × time step = one candidate update event. The update rule determines whether that event commits. This is the closest operational proxy for a micro-event in existing code.

---

## 5. Example Applications

### 5.1 Quantum measurement as micro-event commitment

A quantum measurement is, in ED vocabulary, the commitment of a single micro-event to a single participation channel in a previously multi-channel (thin, uncommitted) regime (ED-09 §7; ED-I-02 §6). The measurement outcome is which channel was selected. The discreteness of measurement outcomes comes from the discreteness of micro-events — a micro-event cannot partially commit (ED-09 §7.2).

### 5.2 Discrete outcomes in the double-slit experiment

Each photon/electron detection in a double-slit experiment is one committed micro-event (ED-I-07 §5). The interference pattern is the statistical distribution of many micro-event commitments across a participation distribution supported by the two slits. The individual micro-events are not spread across both slits; they commit to single locations. The pattern emerges in aggregate.

### 5.3 Why Planck-scale structure is not geometric

General relativity's prediction of singularities at black hole centers and at t=0 is (in ED) the signature that the manifold approximation fails when ED gradients become too steep for thick participation (ED-10 §9.4). The underlying substrate does not become singular; it becomes discrete-micro-event-dominated, and the manifold model stops describing it. This is a direct consequence of micro-events being the atomic substrate.

---

## 6. Simulator / PDE Instantiation

### Where micro-events live in existing math

- **ED Update Rule / Scenario E**: each discrete lattice update step implements the micro-event commitment logic. The update rule determines which sites commit (increase ED) and which relax (decrease ED) per step.
- **ED-Arch-08**: the γ (suppression exponent) sweep shows that at high γ, curvature wells stiffen and core identity becomes architecturally discrete — this is the macroscopic signature of micro-event atomicity becoming visible in simulation.
- **Q-C Boundary Prediction Path PDE** (ED-Phys-16, ED-Phys-17, P6, 00.3): the PDE treats the effective channel weight D as continuous, but the sharp transition at D = 0.5 and the specific oscillation count N_osc ≈ 9 below D = 0.1 are signatures of underlying discreteness.

### What's missing

A first-principles derivation from the micro-event substrate to the PDE form is not yet written. This is a Phase 2 / Phase 4 task. The intermediate step — how does a discrete participation graph produce a continuum PDE for the effective channel weight D? — is a natural research problem for whoever takes it on.

---

## 7. Open Questions

1. **Discrete graph vs. simplicial complex vs. hypergraph.** Which structure best captures higher-order participation relations? May matter for entanglement mathematics (Primitive 04), may not. Phase 1 open.

2. **Does the participation graph grow?** If new micro-events are added over "time" (really, over commitment-order), then the graph is a growing structure. If the full graph is given and time is a partial order on it, the ontology is different. The ED-10 arrow-of-time section (§6) favors the growing picture — becoming accumulates, which is the definition of irreversible — but the formal model hasn't chosen yet.

3. **Countability of micro-events in a given region.** ED (event density, Primitive 05) is defined as a count/measure of micro-events per region. Is it a discrete count, a continuous measure that coarse-grains a discrete count, or something else? This will connect to the derivation of the baryon-to-photon ratio η ≈ 6 × 10⁻¹⁰ in Phase 4.

4. **Lorentz invariance of the micro-event substrate.** ED-09 §9.3 argues Lorentz invariance emerges because participation is relational and micro-events are not lattice-embedded. The formal demonstration of this (that a Lorentz boost does not pick out a preferred frame in the participation graph) is a natural Phase 2 task.

---

## 8. Citation format for other ED work

When citing this primitive from elsewhere in the ED corpus:

> *Per `quantum/primitives/01_micro_event.md` §1* — for the core definition.
> *Per `quantum/primitives/01_micro_event.md` §3* — for the relation to other primitives.
> *Per `quantum/primitives/01_micro_event.md` §4* — for the measurable signature.

---

## 9. One-line summary

> **A micro-event is a discrete act of becoming. It has no position, no duration, no trajectory, no embedding. It is defined only by its participation relations, its commitment order, and how it integrates with other micro-events. It is the atomic unit from which everything else in ED is composed.**
