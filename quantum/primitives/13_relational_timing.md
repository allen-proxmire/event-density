# Primitive 13 — Relational Timing

**Role in the framework:** The phase-like coupling structure between participation channels, chains, and regions. Relational timing is what orchestrates the rhythm of commitments across coupled systems — the reason interference phenomena are stable, the reason oscillations have definite frequencies, the reason phase-coherence is meaningful, the reason "time" in the thick regime emerges as a coordinate at all. Primitives 01–12 supply the substance and structure of ED; Primitive 13 supplies the rhythm.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Relational timing** is the phase-coupling structure between participation channels and chains. It is the relational rhythm at which commitments on one channel synchronize with (or precess against) commitments on another. It is defined only *between* structures — no absolute clock, no external time — so "time" in ED is always a relational quantity, a phase relationship between two or more participating channels.

Relational timing is what classical physics packages as phase, frequency, oscillation, coherence, and (in the thick-regime coarse-graining) time itself.

### What relational timing *is*

- **A phase relation between two (or more) coupled channels.** Not an intrinsic property of either.
- **The rhythm of commitment events across a coupled system.** In coupled chains, commitments on one channel correlate with commitments on another; the phase relationship between commitment events is the relational timing.
- **The structural origin of "time."** Time as a coordinate emerges from relational timing in the thick regime. Before thick-regime coarse-graining, there is no absolute t; there are only phase relationships between participating channels.
- **Relational in the strong sense.** Remove one of the two channels, and there is no timing — only the participation dynamics of the remaining one against some other reference. Time, in ED, does not exist except between participating structures.

### What relational timing is *not*

- **Not an absolute time coordinate.** The ED account of time is thoroughgoingly relational. Absolute time is a thick-regime statistical regularity, not a base feature.
- **Not a clock rate.** A clock is a specific participating structure with a stable internal timing that other structures can reference against. Relational timing is the relation a clock measures.
- **Not dynamical evolution.** Evolution is the sequence of commitments. Timing is the phase structure on that sequence, measured against another sequence.
- **Not the same as participation bandwidth.** Bandwidth is the *richness* of participation; timing is the *phase* structure on that participation. They are distinct.

---

## 2. Mathematical Object

### Discrete version

For two channels `K_A` and `K_B` with commitment-event sequences `{ε_A^n}` and `{ε_B^m}`:

- Commitment phase of `K_A` at event n: `φ_A(n) ∈ S¹`
- Relational timing between A and B: `Δφ(n, m) = φ_A(n) - φ_B(m)` for corresponding (coupled) events

Stable relational timing = `Δφ` varies smoothly or stays within a narrow range as events accumulate. Unstable / incoherent timing = `Δφ` randomizes.

### Continuum / frequency

At high commitment rates, phase becomes continuous and we recover oscillation frequencies:

`ω_A = dφ_A/dt` (in an emergent time coordinate)
`ω_AB = ω_A - ω_B` = relational frequency between A and B

Oscillation frequencies in QM (Rabi, Josephson, Larmor, etc.) are all relational timing rates against some reference oscillation.

### Phase coherence

`coherence(A, B) = |⟨e^{i Δφ}⟩|` — the stability of the relational phase. Coherence = 1 means perfectly locked relational timing; coherence = 0 means randomized.

### Emergent time

In the thick regime, many-channel systems acquire a statistically-regular reference rhythm (thermodynamic time, cosmological time) against which other phases can be measured. This is the origin of the global time coordinate. Relativity emerges because different thick regions have different reference rhythms — time dilation is the statement that two thickly-thickening regions keep pace at different rates depending on their bandwidth / ρ configurations.

### What is *not yet* settled

- **Emergent-time formalization.** How exactly does the thick-regime global time coordinate emerge? Partially addressed in ED-10 §§ on time-emergence, but the formal derivation remains open.
- **Relational timing under individuation.** When chains are individuated, they have internal rhythms. How these internal rhythms compose to produce macroscopic time is a coarse-graining question.
- **Connection to tension polarity (Primitive 09).** Polarity is a phase relation between rule and flow. Timing is a phase relation between channels. The two live in the same phase-structure family; the formal relationship is open.

---

## 3. Relations to Earlier Primitives

### Upstream

| Primitive | Role |
|---|---|
| 02 Chain | Chains have internal rule-phase; timing is phase among chains |
| 07 Channel | Channels are the carriers of timing |
| 09 Tension polarity | Polarity is a specific kind of phase relation |
| 11 Commitment | Commitment events are the beats whose phase-structure is timing |

### Downstream

None — 13 is the last primitive. Its downstream "users" are the effective-theory programs of Phase 2 (QM as thin-regime effective theory, GR as thick-regime effective theory).

### Circular-definition flags

1. **"Time" in the continuum-version "`dt`"** is itself an emergent concept that relational timing produces. The formulation uses local emergent-time coordinates for convenience; the fundamental definition is phase-only.
2. **"Oscillation frequency" language** is standard physics vocabulary imported for clarity; the ED-base language is phase-increment-per-commitment.

---

## 4. Measurable Signature

- **Interference fringes.** The phase relation between recombined channels after branching is relational timing in action. Stable fringes = stable relational timing.
- **Oscillation frequencies.** Rabi, Larmor, Josephson, Ramsey, optical transitions — all are relational timing rates.
- **Clock synchronization and relativity.** Gravitational and kinematic time-dilation are relational-timing differences between thick regions of different ρ / b structure.
- **Spectroscopic line positions.** ω_{transition} is the relational timing between two bound-state channel configurations.
- **Coherence times T2.** How long relational phase between system and reference channel stays locked.
- **Cosmological expansion rate.** Hubble-rate H is a relational-timing quantity at cosmological scale — how the thick-regime reference rhythm evolves against local channel rhythms.

### Operational handle

- **ED-Arch:** implicit — the simulator's time coordinate is relational, set by site-update counts.
- **GR-SC / ED-SC 3.x:** snapshot-scheduling is a relational-timing choice; half-decay time for ξ determines canonical sampling.

---

## 5. Example Applications

### 5.1 Interference as relational-timing-preserved recombination

Two-channel recombination (double-slit, Mach-Zehnder) produces fringes because the relational timing between the two branches is preserved from split to recombine. Decoherence destroys fringes by randomizing the relational phase.

### 5.2 Oscillation as phase-cycling coupling

Rabi oscillation = atom-field channel pair with mutual phase that advances at Rabi frequency. Josephson oscillation = two superconducting channels coupled with mutual phase advancing at the Josephson frequency (V-dependent). Neutrino flavor oscillation = three channels with mutual phases set by mass-eigenstate structure.

### 5.3 Relativity as region-dependent reference rhythm

A clock in a gravitational well ticks slower because the local reference rhythm of the thick regime runs slower — participation bandwidth in the well is compressed, commitment rate relative to far-away reference is reduced. Time dilation is a structural statement about bandwidth-rescaled relational timing.

### 5.4 Spectroscopy as relational-timing measurement

An atomic transition at frequency ω corresponds to the relational timing between two bound channel configurations. Laser spectroscopy probes this timing directly.

### 5.5 Cosmological time as large-scale reference rhythm

Cosmological time emerges from the thick-regime commitment-rate at cosmological scale. Hubble rate measures how the reference rhythm evolves; inflation corresponds to a very high commitment-rate epoch; reheating and matter-domination are progressive slowdowns and structural changes of the reference.

### 5.6 Gravitational waves as propagating timing perturbation

A gravitational wave is a propagating perturbation in the local participation-structure that carries a perturbation of the local relational-timing reference. LIGO detects the timing-shift between its arm channels as the wave passes.

---

## 6. Simulator / PDE Instantiation

- **ED-Arch:** simulator steps are discrete time; relational rhythm between cores = phase-lock dynamics of orbiting / hovering configurations.
- **Q-C PDE:** implicit; phase-coherence of the propagating chain is relational-timing content.
- **GR-SC / ED-SC 3.x:** snapshot-sampling intervals = relational-timing choices for measurement.

### What's missing

- Explicit relational-timing field in the PDE layer.
- Formal connection between discrete phase and emergent continuous time.
- Cosmological-scale relational-timing dynamics for inflation and baryogenesis eras.

---

## 7. Open Questions

1. **Emergent-time derivation.** Formal derivation of the thick-regime global time coordinate from relational-timing statistics.
2. **Relational timing and tension polarity.** Unified phase-structure treatment?
3. **Gravitational time dilation explicit formula.** From bandwidth compression + ρ structure to slower reference rhythm — leading-order derivation.
4. **Cosmological clock.** What sets the large-scale reference rhythm? CMB-era? Horizon-scale phase synchronization? Open.
5. **Inflation-era timing.** Very high commitment rate implies very fast reference rhythm. Does the inflation-end transition correspond to a rhythm-freeze as thickening kicks in? Plausible, needs treatment.
6. **Quantum Zeno and timing.** The Zeno effect is a timing phenomenon — external commitment rate vs. internal rule-phase. Formal treatment as relational-timing limit.

---

## 8. One-line summary

> **Relational timing is the phase-coupling structure between participation channels — the rhythm of commitment events in coupled chains, the origin of oscillation frequencies and interference fringes, and the structural source from which the thick-regime coordinate called "time" emerges as a coarse-grained relational statistic.**
