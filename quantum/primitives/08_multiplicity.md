# Primitive 08 — Multiplicity

**Role in the framework:** The count of distinct channels available to a chain in a region. Where Primitive 07 establishes what a channel is, Primitive 08 establishes *how many*. Multiplicity is the integer (or integer-valued field, in coarse-grained form) that distinguishes the thin uncommitted regime (many channels) from the thick committed regime (one channel dominant). It is the quantity that crosses threshold at the Q-C boundary, the quantity that collapses at a measurement event, and the quantity that distinguishes a coherent superposition from a definite outcome. The whole thin/thick language of the program bottoms out in multiplicity.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Multiplicity** `M(R, τ)` is the count of distinct channels of rule-type `τ` available in region `R`. A region with `M = 1` supports only one way for a τ-chain to continue — a committed, single-track regime. A region with `M ≫ 1` supports many competing channels — the uncommitted, coherent-superposition regime.

Multiplicity is integer-valued at the discrete-graph level. In the coarse-grained continuum it becomes a real-valued effective-multiplicity field, but its foundational character is counting.

### What multiplicity *is*

- **An integer count of channels.** At the discrete graph, `M(R, τ) = |𝒞_τ(R)|` — the cardinality of the rule-type-τ channel set in region R.
- **The regime-identifier variable.** Thin regime, thick regime, Q-C transition — all are multiplicity regimes. "Uncommitted" means M > 1; "committed" means M = 1 (effectively).
- **The quantity that collapses at commitment.** A commitment event (Primitive 11) reduces M from several to one for the committing chain. This is the structural content of "wavefunction collapse."
- **Region- and type-relative.** Always indexed by a region R and a rule-type τ. A region with high photon-channel multiplicity may have low electron-channel multiplicity. Multiplicity is not a single scalar per region.

### What multiplicity is *not*

- **Not a Hilbert-space dimension.** In QM, Hilbert-space dimension is the number of orthogonal basis states of a system. Multiplicity is the number of *available local continuations* for a specific chain in a specific region. They are related — the thick-regime Hilbert-space dimension for a chain's local state is bounded by the multiplicity — but they are not identical.
- **Not degeneracy.** Degeneracy in energy levels is a specific refinement (channels of equal bandwidth weight). Multiplicity is the raw count regardless of weight distribution.
- **Not a probability.** Born-rule weights are channel-specific bandwidth distributions (Primitive 04). Multiplicity is the count over which those weights are distributed, not the weights themselves.
- **Not discrete-only.** At the coarse-graining threshold, effective multiplicity can be treated as a smooth field. The discreteness re-emerges at fine scales and at commitment events.

### Multiplicity regimes

Three operational bands:

- `M = 1` — committed / classical / single-track. A chain has one way forward; the chain is "in" that channel; thick-regime classical behavior obtains.
- `M small (2 – a few)` — interference regime. The chain distributes across a small number of channels with bandwidth-coherent recombination on re-merging. Double-slit, Mach-Zehnder, neutrino-oscillation flavor-mixing are all `M = 2` or `M = 3` cases.
- `M large (≫ 1)` — thin/ensemble regime. The chain distributes across many channels. Thermal, diffusive, path-integral-like phenomenology. Stat-mech and coarse-grained QFT emerge here.

The Q-C Boundary PDE transition (D = 0.5) sits where effective multiplicity contracts from many to one. N_osc ≈ 9 at D < 0.1 is approximately the effective multiplicity count the PDE finds at the low-D edge.

---

## 2. Mathematical Object

### Discrete version

`M : (Regions) × (rule-types) → ℕ`
`M(R, τ) = |𝒞_τ(R)|` where `𝒞_τ(R)` is the set of τ-channels in R (Primitive 07 §2).

### Coarse-grained version

In the thick regime, effective multiplicity becomes a density-like field:

`μ(x, τ) = dM / d(coarse-graining volume)`

— channels per unit volume per rule-type. Useful for path-integral-style calculations in the thin regime.

### Effective multiplicity in PDE form

The Q-C Boundary PDE operates on an effective `M_eff(x, τ)` that counts bandwidth-weighted channel participation:

`M_eff(x, τ) = [Σ_{K ∈ 𝒞_τ} b_K(x)]² / Σ_{K ∈ 𝒞_τ} b_K(x)²`

— the participation-ratio form, which equals the raw count when bandwidth is equally distributed and drops toward 1 when one channel dominates. This is the natural thick-regime smoothing of the discrete count.

`D(x)` in the PDE is related to `M_eff` by something like `D ≈ 1/M_eff` in the appropriate regime, so the critical `D = 0.5` corresponds to `M_eff ≈ 2` — the threshold where two channels still compete but are about to lose to a single dominant one.

### Multiplicity and commitment

At a commitment event, M drops. In the simplest case `M: n → 1`. The structural question: what selects which of the n channels survives? Born-rule weights (Primitive 04) determine the selection probability. The dynamical rule is formalized in Primitive 11.

### What is *not yet* settled

- **Exact relation between M_eff and D.** The formula above is approximate; the precise PDE-level functional needs explicit derivation.
- **Whether `M` is conserved under composition.** If two regions each with M₁, M₂ channels compose, does the composite have M₁ × M₂, M₁ + M₂, or something between? Likely type-dependent (multiplicative for independent subsystems, additive for continuations, sublinear for entangled).
- **Upper bounds.** Is there a structural maximum multiplicity per region? Plausibly tied to ρ saturation — saturated regions lose channel-distinctness.

---

## 3. Relations to Earlier Primitives

### Upstream

| Primitive | Role |
|---|---|
| 07 Channel | Multiplicity counts channels; without channels, nothing to count |
| 04 Bandwidth | M_eff uses bandwidth distribution (participation ratio) |
| 06 ED gradient | Steep ∇ρ suppresses multiplicity; smooth regions admit high M |
| 05 Event density | Near-saturation ρ suppresses distinct channels |

### Downstream

| Primitive | Role |
|---|---|
| 09 Tension polarity | Polarity determines which of M channels survive saturation selection |
| 10 Individuation | Distinct identities require M = 1 or near-1 in the boundary region |
| 11 Commitment | Commitment events reduce M |
| 12 Thickening | Thickening is accumulated commitment — accumulated M-reduction |
| 13 Relational timing | Phase coupling across the M available channels |

### Circular-definition flags

1. **"Commitment" in §1** forward-references Primitive 11. Used operationally: commitment = the event where M drops to 1.
2. **"Interference" in §1** forward-references the bandwidth-composition rule at channel merging (Primitive 07 §2), which is itself operational pending the sublinear-composition question (Primitive 04 §7).

---

## 4. Measurable Signature

- **Fringe visibility.** `V = (I_max - I_min)/(I_max + I_min)` in an interferometer measures the effective M across the apparatus. M = 2 coherent gives V = 1; M = 1 (which-path known) gives V = 0.
- **Spectral line count / level count.** An atomic system's discrete levels are its channel inventory — multiplicity by rule-type.
- **Number of open scattering channels.** A standard experimental quantity in nuclear and particle physics.
- **Density of states.** `ρ(E) = dM/dE` at a given energy — a direct thick-regime multiplicity derivative.
- **Decoherence onset.** The regime crossover from M ≫ 1 to M = 1 as environmental coupling increases.
- **Quantum-to-classical crossover (Q-C boundary).** The whole Q-C apparatus measures the multiplicity regime transition.

### Operational handle

- **ED-Arch:** M is countable at simulator scale as the number of stable bandwidth-preferential paths a test chain can traverse between two locations.
- **Q-C PDE:** `M_eff(x, τ)` via the participation-ratio functional; D(x) = 0.5 ↔ M_eff = 2 approximately.
- **GR-SC motif work:** The `f(ρ | ξ, L_ray, α_filt, N_req)` distribution implicitly carries channel-motif multiplicity information; the shell-aware `L_eff` treatment is a multiplicity-geometry correction.

---

## 5. Example Applications

### 5.1 Double-slit as M = 2

Two channels (slits). Chain distributed across both. Coherent recombination produces fringes. Which-path measurement collapses M to 1, fringes vanish. The entire phenomenology is an M-transition.

### 5.2 Thermal state as high-M ensemble

A thermal state is a chain distributed across many environmentally-coupled channels with bandwidth-weight given by the Boltzmann distribution. Partition function `Z = Σ_K e^{-βE_K}` sums over the M channels. Classical thermodynamics is M-large phenomenology.

### 5.3 Q-C transition as M contraction

As environmental coupling grows (e.g., particle size, environment temperature, measurement bandwidth), effective M for a chain's local state drops from large (quantum) through intermediate (transition) to 1 (classical). The Q-C Boundary PDE tracks this contraction. N_osc ≈ 9 at the low-D (high-M) edge marks the approximate channel count the chain explores before contraction begins.

### 5.4 Decoherence as multiplicity transfer to environment

Decoherence does not reduce the total M of system-plus-environment. It redistributes: the system's visible-to-it M drops; the environment gains the corresponding M, spread across many degrees of freedom. The system behaves as if M = 1 because the phase relations among its would-be-coherent channels are now distributed into the environment.

### 5.5 Degenerate ground states

A degenerate ground state is a set of channels with identical bandwidth weight and identical rule-type. `M = g` where g is the degeneracy. Symmetry breaking is the spontaneous selection of one channel from the g — an M-contraction driven by fluctuation.

### 5.6 Scattering channels

In particle / nuclear scattering, the "number of open channels at energy E" is the channel-multiplicity for the rule-types kinematically accessible. Cross-section structure, resonances, and thresholds are all M-structure phenomena.

---

## 6. Simulator / PDE Instantiation

- **ED-Arch:** countable channel structure at simulator scale; γ-sweep modulates how sharply channels are distinguished.
- **Q-C PDE:** `M_eff(x, τ)` via participation ratio; D(x) = 0.5 at M_eff ≈ 2.
- **GR-SC F4 work:** lattice-discretisation constraints on effective multiplicity at small scales (Δr ≥ 0.5 lu on 64²). A real methodological finding of the arc.

### What's missing

- Explicit formula D(x) = f(M_eff) in closed form
- Rules for M under multi-chain composition
- Multiplicity at saturation — formal account of how M collapses as ρ → ρ_max

---

## 7. Open Questions

1. **Exact D–M_eff relation.** Phase 2 target.

2. **Multiplicity composition law.** Additive, multiplicative, or intermediate under chain composition? Needed for scattering, entanglement formation.

3. **Upper bound M_max(R).** Tied to ρ saturation. Structural constant or regime-dependent?

4. **Multiplicity and entropy.** `S ~ log M_eff` as the ED account of entropy. Formalize and connect to thermodynamic entropy in the thick regime.

5. **Gauge multiplicity.** If gauge structure is channel-topology (Primitive 03 §7, 07 §7), gauge-group dimension is a multiplicity-count of topology classes. Needs explicit treatment.

6. **η thread — multiplicity form.** Pre-saturation M is high (many possible chain rule-types); post-saturation M drops (only aligned-tension rules survive); the surviving-to-total ratio contributes to η. One more hook on the same Phase 4 target.

---

## 8. One-line summary

> **Multiplicity M(R, τ) counts distinct τ-channels available in region R. It is the regime-identifier (thin M ≫ 1 / thick M = 1), the quantity that collapses at commitment, and the structural basis for fringe visibility, density of states, Q-C transitions, and decoherence — all of which are M-regime phenomena.**
