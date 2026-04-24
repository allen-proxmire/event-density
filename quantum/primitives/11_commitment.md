# Primitive 11 — Commitment

**Role in the framework:** The discrete event in which a chain selects one of its available channels and adds a new micro-event along that channel. Commitment is the ED structural content of "a quantum measurement outcome," "wavefunction collapse," "decoherence settling," and generally *any discrete step of becoming* that reduces multiplicity and adds new structure. Every micro-event (Primitive 01) enters the universe through a commitment event. The Born rule, the quantum-to-classical transition, and the irreversibility of measurement all have their structural account at Primitive 11.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**A commitment event** is the discrete selection of a single channel from those available to a chain, together with the addition of a new micro-event at the selected channel's next-vertex position. Before a commitment: the chain has multiplicity `M > 1`, bandwidth distributed across channels, phase coherence among them. After a commitment: the chain has `M = 1` locally, bandwidth concentrated in the selected channel, and a new micro-event vertex exists.

Commitment is how *anything new* happens in ED. It is the atomic step of dynamics. Chain propagation is a sequence of commitment events. Measurement outcome is a single forced commitment. Decoherence is a rapid sequence of environmental-forced commitments.

### What commitment *is*

- **Discrete.** A single event, not a process. Time may be continuous at thick scales, but at the base, becoming advances through discrete commitment events.
- **Channel-selective.** The event selects one channel from the available set. Selection probabilities are the Born-rule weights (bandwidth ratios across channels — Primitive 04 §5.2).
- **Irreversible at the event scale.** Once committed, the pre-commitment multiplicity is gone for that chain at that vertex. Reversibility re-appears only at ensemble / statistical scales.
- **Multiplicity-reducing.** M drops at commitment. This is the structural content of "collapse."
- **Producer of new structure.** A commitment adds a vertex to the participation graph. It is how the graph *grows*.

### What commitment is *not*

- **Not measurement specifically.** Every chain step is a commitment; measurement is a special case where environmental bandwidth is large enough to force commitment immediately. Chains commit constantly in isolation too — just at rates governed by their internal dynamics rather than external pressure.
- **Not wavefunction collapse in the von Neumann sense.** Collapse in standard QM is an instantaneous projection on a Hilbert space. Commitment is a discrete structural event at the graph level; projection is its thick-regime shadow.
- **Not continuous.** Even when commitment rates are high and the thick-regime description smooths them into continuous flow, the underlying events are discrete.
- **Not unique to conscious observation.** No observer required. Commitment is triggered by bandwidth conditions, not by knowledge states.

---

## 2. Mathematical Object

### Discrete event structure

A commitment event `ε` at vertex `u ∈ V` for chain C has:

- **Pre-state:** `(M_pre, {b_K}_pre)` — multiplicity M_pre and bandwidth distribution across available channels
- **Selection:** channel `K*` is chosen with probability `P(K*) = b_{K*}² / Σ b_K²` (Born-like weight; precise functional may deviate at the discrete scale)
- **Post-state:** new vertex `v` added adjacent to u along `K*`; chain C now has its next micro-event at v; M_post = 1 locally at v along this chain

### Commitment rate

For a chain with internal rule-bandwidth `b_int` and environmental pressure, the commitment rate is roughly `Γ_commit ~ b_int / (commitment-reserve budget)` in isolation, modified upward by environmental bandwidth. This is why measurement "forces" commitment: large environmental bandwidth pushes the rate up, so the chain commits sooner.

### Born rule as bandwidth squared

The standard QM selection probability `|ψ_K|²` is, in ED, the bandwidth ratio `b_K² / Σ b²`. The squared-amplitude structure emerges because bandwidth composes sublinearly under channel merging (Primitive 04 §7 item 2) in a way that, after normalization, gives `|ψ|²` weighting. The Born rule is therefore a thick-regime emergent statement about discrete commitment selection.

### Commitment and thickening

Each commitment adds one vertex, one selected channel, one incremented ρ. Thickening (Primitive 12) is the accumulation of many commitments into stable structure.

### What is *not yet* settled

- **Precise commitment trigger condition.** What exactly determines when a chain commits? Likely: when the bandwidth-integrity of its current multi-channel state falls below a structural threshold due to internal drift or external pressure. Explicit form is open.
- **Born rule derivation.** The `|ψ|²` structure is motivated but not derived from a specific graph-level commitment rule. This is a known-hard derivation (the "Born rule problem" in QM foundations is a real open question); ED has a candidate answer but the derivation is Phase 2 work.
- **Discreteness vs. continuity at high rate.** When commitment rate is very high, the discrete events can be approximated as a continuous stochastic process. The formal limit needs treatment.
- **Reversibility at the ensemble level.** Statistical mechanics is reversible at the ensemble level while individual events are not. The ensemble-vs-individual reconciliation needs explicit formulation.

---

## 3. Relations to Earlier Primitives

### Upstream

| Primitive | Role |
|---|---|
| 01 Micro-event | Commitment adds one |
| 02 Chain | Commitment advances a chain by one step |
| 04 Bandwidth | Selection probability is bandwidth-ratio |
| 07 Channel | Commitment selects from available channels |
| 08 Multiplicity | Commitment reduces M |
| 09 Tension polarity | Saturation-era commitment is polarity-filtered |
| 10 Individuation | Commitment events typically increase individuation |

### Downstream

| Primitive | Role |
|---|---|
| 12 Thickening | Accumulation of commitments = thickening |
| 13 Relational timing | Commitment rate is the basic temporal rhythm of a chain |

### Circular-definition flags

1. **"Commitment-reserve bandwidth"** from Primitive 04 was defined by forward-reference to this primitive. Now formalized: commitment-reserve is the bandwidth budget available for commitment events. Mutual dependency resolved.
2. **"Irreversibility at event scale"** is operational; full irreversibility structure connects to thermodynamic arrow-of-time questions (open).

---

## 4. Measurable Signature

- **Measurement outcomes.** A measurement produces a commitment event; the outcome is the selected channel's label.
- **Click rates in single-photon detectors.** Each click = one commitment. Rate = Γ_commit.
- **Decoherence rates.** Environmental-forced commitment rate.
- **Spontaneous emission rates.** A chain's internal commitment rate in the absence of external pressure; determined by internal-bandwidth and channel-availability.
- **Fermi's golden rule.** Transition rate as a function of channel density — a thick-regime form of commitment rate formula with channel-density input.
- **Zeno effect.** Very frequent measurement suppresses non-trivial commitment outcomes; chain commits repeatedly to its current channel, never drifting.

### Operational handle

- **ED-Arch:** every step of simulator update is a commitment event at every site simultaneously.
- **Q-C PDE:** D(x) crossing 0.5 represents the regime where commitment becomes effectively single-channel.

---

## 5. Example Applications

### 5.1 Measurement as environment-forced commitment

A measurement device has high bandwidth with the measured chain. This pushes commitment-rate up dramatically; the chain commits to one channel almost immediately upon contact. The outcome: the channel that won the Born-weighted selection.

### 5.2 Decoherence as rapid environmental commitment sequence

A qubit weakly coupled to an environment doesn't commit once; it commits in a stream of small environmental-forced events, each selecting one environmental-channel endpoint. The qubit's coherent phase information redistributes across environmental channels at each such event. Over many events, coherence is lost.

### 5.3 Zeno effect as commitment-starved drift

Frequent measurement causes repeated commitment to the current channel. The chain's internal rule, which would have drifted it to a different channel over free evolution time, never gets the chance — every commitment lands it on the same channel it started from.

### 5.4 Spontaneous emission rate

An excited atom has an internal rule that slowly drifts toward the ground-state channel. At some point the drift produces a photon-channel availability that, combined with the internal rule-bandwidth, triggers a commitment — a photon is emitted. The rate is determined by the internal-bandwidth structure and the photon-channel density.

### 5.5 Born rule

When a chain at multi-channel state commits, which channel? Bandwidth ratios give selection probabilities: P(K) ∝ b_K². This is the Born rule as a statement about commitment selection.

### 5.6 Growing-graph cosmology

New micro-events are added at each commitment. The universe's participation-graph grows event-by-event. Inflation is a regime of very high commitment rate; baryogenesis is polarity-selective commitment in saturated conditions; structure formation is aggregated commitment in ∇ρ-steered channels.

---

## 6. Simulator / PDE Instantiation

- **ED-Arch:** each time-step update at each site is an ensemble of commitment events. Rate set by rule parameters (γ, etc.).
- **Q-C PDE:** D(x) dynamics trace the effective commitment regime; threshold D = 0.5 marks effective single-channel commitment.
- **GR-SC / ED-SC 3.x:** motif-count-based diagnostics implicitly measure commitment structure.

### What's missing

- Explicit formal commitment-trigger rule.
- Born rule derivation at the discrete-graph level — the hard one, Phase 2.
- Cosmological-scale commitment dynamics for η derivation.

---

## 7. Open Questions

1. **Commitment trigger condition** — explicit form.
2. **Born rule derivation** — hard, Phase 2. Candidate: bandwidth-squared selection from sublinear composition.
3. **Commitment reversibility at ensemble scale** — connection to statistical-mechanical arrow of time.
4. **Continuous-limit commitment** — when is the stochastic-process approximation valid?
5. **Commitment selection under polarity constraint** — the saturation-era case; central to η derivation. **Phase 4.**
6. **Discrete-vs-continuous at very low rate** — in deep-vacuum regimes, commitment is very rare; the discrete structure matters. Phenomenology?

---

## 8. One-line summary

> **A commitment event is the discrete selection of one channel by a chain, adding a new micro-event along that channel and collapsing local multiplicity. It is the atomic step of becoming, the ED account of measurement outcomes and the Born rule, and the rate-variable whose regime sets the thin-versus-thick phenomenology.**
