# Primitive 04 — Participation Bandwidth

**Role in the framework:** The quantitative measure of participation. Where Primitive 03 establishes *that* micro-events participate, Primitive 04 establishes *how much*. Bandwidth is the graded scalar that turns the relational fact of participation into something that can be large or small, thick or thin, coherent or disrupted. It is what coherence times measure, what decoherence consumes, what entanglement strength quantifies, and what sits underneath the quantum-classical transition as a graded variable rather than a binary one.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Participation bandwidth** is the graded measure of how richly two (or more) micro-events, chains, or regions integrate one another's becoming. It is not the relation itself (Primitive 03), but the magnitude of the relation — a scalar (or scalar field in the thick regime) that captures how much participation is present.

Bandwidth is inherently comparative. A chain isolated from its environment has *low* bandwidth with the environment and *high* bandwidth internally along its update rule. A measurement device coupled to a quantum system has *high* bandwidth with that system. A vacuum region between two detectors has *some* non-zero residual bandwidth; a causally disconnected region has none.

### What bandwidth *is*

- **A graded scalar.** Unlike participation (present / absent as a structural fact), bandwidth is continuous-valued. A pair of micro-events can have strong or weak integration; two regions can share dense or sparse participation structure.
- **The substance of coherence.** Coherence in the quantum sense is bandwidth maintained internally to a system without being bled into the environment. Coherence time = the characteristic time over which a system's internal bandwidth stays higher than its environmental bandwidth.
- **The substance of entanglement strength.** The degree of correlation between two entangled subsystems is the bandwidth of the participation structure they share. Bell inequality violations (CHSH ≈ 2.828) quantify this shared bandwidth against the classical bound.
- **The substance of decoherence.** Decoherence is the transfer of bandwidth from a system's internal participation to its environmental participation. Nothing is destroyed; bandwidth is redistributed into environmental channels too numerous to track.

### What bandwidth is *not*

- **Not energy.** Energy is a thick-regime bookkeeping quantity that tracks, among other things, the commitment cost associated with chain dynamics. Bandwidth is prior. Energy-like quantities emerge from bandwidth gradients through coarse-graining, not the other way around.
- **Not information (directly).** Information presupposes committed, distinguishable states. Bandwidth exists before commitment and is what makes distinguishable states possible. The Shannon / von Neumann information content of a system is a thick-regime summary of its bandwidth distribution across channels.
- **Not probability.** Born-rule probabilities (|ψ|²) are channel-specific participation weights at the moment of commitment. Bandwidth is the pre-commitment distribution that those weights are drawn from. Probability is what bandwidth looks like after a commitment event forces channel selection.
- **Not a single number per system.** A system has *different bandwidths with different partners*. The bandwidth an isolated qubit shares with its cryogenic shield is distinct from the bandwidth it shares with an incoming photon. Bandwidth is always a relation, never an intrinsic property.

### The four-band structure

A recurring empirical pattern across the ED-I papers: quantum behavior exhibits a **four-band bandwidth structure** that sets the scale of the uncertainty relations. At the core-chain level, bandwidth partitions into:

1. **Internal rule-bandwidth** — the participation sustaining the chain's own update rule (identity-maintenance bandwidth).
2. **Adjacency bandwidth** — the participation the chain shares with its immediate participation-adjacent neighbors (positional / kinematic coupling).
3. **Environmental bandwidth** — the participation with the broader bath (decoherence reservoir).
4. **Commitment-reserve bandwidth** — the participation available to be consumed by a commitment event without disrupting the other three.

The uncertainty relations are structural constraints across these four bands. Heisenberg Δx·Δp ≥ ℏ/2 is a lower bound on the product of two bandwidth allocations (adjacency-position vs. adjacency-momentum) because each draws from the same finite adjacency budget. Energy-time uncertainty is a constraint across internal rule-bandwidth and commitment-reserve. Number-phase uncertainty constrains commitment-reserve against internal rule-bandwidth.

This is developed further in §5 below and is the load-bearing structural claim of this primitive.

---

## 2. Mathematical Object

### Candidate structure

In the participation-graph formulation:

- Primitive 01 supplied vertices (micro-events)
- Primitive 03 supplied edges (participation relations)
- **Primitive 04 supplies edge weights** — a positive real number on each edge measuring bandwidth

At the graph level: `w: E → ℝ≥0` where `E` is the edge set of the participation graph.

In the thick regime (Primitive 12), where edges are dense enough to coarse-grain, bandwidth becomes a **scalar field**:

`b(x, y) : M × M → ℝ≥0`

where `M` is the emergent manifold and `b(x, y)` is the bandwidth density between regions near `x` and near `y`. Locality in the thick regime forces `b(x, y)` to decay rapidly with distance (distance itself being inverse adjacency-bandwidth; see Primitive 03 §5.2 and ED-10 §3.2), so the effective description usually reduces to a local bandwidth density `b(x)` plus a short-range kernel.

### Integration over bands

The four-band decomposition partitions bandwidth by participation-partner type. Formally, for a chain `C`:

- `b_int(C)` = bandwidth along C's own update-rule participation
- `b_adj(C, N)` = bandwidth with adjacency-neighborhood `N`
- `b_env(C, E)` = bandwidth with environment `E`
- `b_com(C)` = commitment-reserve bandwidth

Total chain-bandwidth budget: `b_total(C) = b_int + b_adj + b_env + b_com`, subject to a conservation-like constraint in the chain's persistence regime.

The uncertainty relations appear as **allocation inequalities** of the form:

`b_A · b_B ≥ K_{AB}`

where A, B index two allocations drawing from the same parent band, and `K_{AB}` is a structural constant derived from the participation graph topology local to C. The Heisenberg ℏ/2 is the thick-regime universal value of `K_{pos,mom}` once the adjacency budget is normalized.

### Measure-theoretic version

For rigorous treatment of aggregate quantities (coherence time integrals, entanglement entropy), bandwidth should be treated as a **positive measure** on the edge set, with the associated integration theory:

- Coherence lifetime: `τ_coh = ∫ dt [b_int(t) / (b_env(t) + ε)]` with appropriate normalization
- Entanglement strength: `E(A, B) = ∫_{E_shared} dw` over the shared-participation edge set
- Decoherence rate: `Γ_dec = db_env/dt` at the expense of `b_int`

### What is *not yet* settled

- **Normalization.** Is there a natural absolute unit of bandwidth (the bandwidth per single participation edge at a single micro-event), or is bandwidth only ever defined up to an overall scale that gets fixed by matching to ℏ?
- **Additivity vs. sublinearity.** When two chains share participation with a third, is the combined bandwidth strictly the sum, or does interference / destructive composition reduce it? Evidence from interferometry (ED-I-07) suggests sublinear composition is possible.
- **Negative / signed bandwidth.** All bandwidth is non-negative by the definition above, but the *net flow* of bandwidth can have a direction. Whether a signed refinement is useful — or whether direction should always be carried by a separate object (tension polarity, Primitive 09) — is open.
- **Band-count universality.** The four-band structure is motivated empirically. Whether it is mathematically forced by the participation-graph structure, or whether other partitions are possible in principle, is not yet settled.

---

## 3. Relations to Earlier Primitives

### Upstream dependencies

| Primitive # | Role |
|---|---|
| 01 Micro-event | Bandwidth is a measure on edges, and edges connect micro-events |
| 02 Chain | Chain persistence is measured against internal rule-bandwidth; the chain is the unit for which band allocation is defined |
| 03 Participation | Participation is the relation; bandwidth is the measure of the relation. Without participation there is no edge to weight |

Primitive 04 is the first primitive that is explicitly *quantitative* rather than structural. 01–03 establish what exists; 04 is what "how much" means for what exists.

### Downstream — primitives built on bandwidth

| Primitive # | How it uses bandwidth |
|---|---|
| 05 Event density | ED as scalar count pairs with bandwidth to form the local PDE substrate (bandwidth describes edges; ED describes vertices; together they give the full graph state) |
| 06 ED gradient | A gradient requires both a scalar field and a direction; bandwidth defines the coupling that makes gradients produce dynamics |
| 07 Channel | A channel is a locally coherent bandwidth-preserving pathway; channel stability is bandwidth-coherence over the pathway |
| 08 Multiplicity | Multiplicity counts channels, but channels are bandwidth-defined; high bandwidth in many directions = high multiplicity |
| 09 Tension polarity | Tension is a phase of rule-bandwidth relative to local relaxation-bandwidth direction |
| 10 Individuation | Individuation threshold is a bandwidth threshold: enough internal bandwidth relative to shared to distinguish "this system" from "that one" |
| 11 Commitment | A commitment event draws from commitment-reserve bandwidth and converts channel-distributed bandwidth into single-channel concentrated bandwidth |
| 12 Thickening | Thickening is the accumulation of committed bandwidth into locally persistent structure |
| 13 Relational timing | Phase coupling of bandwidth oscillations across participating chains |

Essentially every downstream primitive operates on, measures, or transforms bandwidth. This is why 04 is the load-bearing quantitative primitive.

### Circular-definition flags

1. **"Coherence" in §1** — used informally; the full formal definition requires Primitive 07 (Channel) since coherence is bandwidth-preservation along channel structure.
2. **"Commitment-reserve"** — one of the four bands, defined by its role in Primitive 11 (Commitment). Until 11 is drafted, it is understood operationally as "the budget a commitment event can draw from without disrupting existing structure."
3. **"Environment"** in band decomposition — requires Primitive 10 (Individuation) for full formal definition of the system / environment cut. Until then, understood as "everything outside the chain that the chain shares non-negligible bandwidth with."

---

## 4. Measurable Signature

### Direct observable consequences

- **Coherence times (T1, T2, T2*).** All three standard coherence-time measures are bandwidth quantities: T1 is energy-relaxation time = rate at which internal rule-bandwidth bleeds to environment; T2 is phase-coherence time = rate at which internal-vs-adjacency bandwidth phase relations degrade; T2* includes inhomogeneous broadening from bandwidth variation across an ensemble.
- **Entanglement measures.** Concurrence, entanglement entropy, negativity — each is a specific functional on the shared-participation bandwidth between subsystems.
- **Decoherence rates.** Γ_φ, pure-dephasing rate, and related are `db_env/dt` quantities.
- **CHSH value.** The Bell-inequality CHSH statistic quantifies shared bandwidth against the classical factorization bound; the Tsirelson bound 2√2 ≈ 2.828 is the maximum bandwidth-sharing permitted by the participation-graph structure.
- **Uncertainty products.** Δx·Δp, ΔE·Δt, ΔN·Δφ — each is the empirical signature of an allocation inequality between two bandwidth draws from a common band.
- **Double-slit fringe visibility.** Visibility `V` measures bandwidth-coherence across the two-slit branches; `V = 1` means perfect bandwidth preservation, `V = 0` means complete environmental bandwidth exchange (which-path information).
- **Ramsey fringe amplitude.** Same category — amplitude measures surviving bandwidth coherence between free-evolution branches.

### Indirect consequences (partial list)

- Superconducting gap magnitude (bandwidth consolidation into a single macroscopic chain rule)
- Superfluid critical temperature (thermal bandwidth vs. chain-rule bandwidth crossover)
- Quantum Zeno effect magnitude (measurement-bandwidth forcing commitment before internal rule-bandwidth can redistribute)
- Aharonov-Bohm fringe shift (bandwidth-topology sensitivity around non-trivial participation geometry)

### Operational handle

- **ED-Arch simulator.** Effective bandwidth at a site = the integrated coupling weight of its neighborhood update. Gamma-sweep studies (ED-Arch-08) vary the suppression exponent, which directly modulates effective edge weights. Higher γ → stiffer bandwidth → sharper architectural quantization.
- **Q-C Boundary PDE.** The effective channel weight `D(x)` is a coarse-grained bandwidth variable. `D < 0.1` = bandwidth distributed across many channels (multi-channel thin regime). `D > 0.5` = bandwidth concentrated in one channel (committed regime). `D = 0.5` exactly = critical bandwidth concentration.

---

## 5. Example Applications

### 5.1 Coherence time as bandwidth retention

A qubit isolated in a dilution refrigerator maintains coherence for T2 seconds. In ED terms: the cryogenic shield maintains low environmental bandwidth with the qubit; the qubit's internal rule-bandwidth stays above the threshold at which adjacency-coherence is preserved. When phonon, photon, or two-level-system fluctuators bleed bandwidth across the shield, T2 drops.

Coherence engineering in quantum hardware is ED-bandwidth engineering: design the participation topology so that internal rule-bandwidth is well-shielded from environmental bandwidth bleeding. Every technique — dynamical decoupling, Purcell filtering, surface-loss mitigation — is a bandwidth isolation or bandwidth redirection strategy.

### 5.2 Entanglement strength as shared bandwidth

Two qubits prepared in a Bell state share a participation structure whose bandwidth is split across the two endpoints. Per Primitive 03 §5.1, this is not two separate systems coordinating; it is one structure whose bandwidth is instantiated at two locations.

Strength measures — concurrence, entanglement of formation — are functionals measuring how much total bandwidth is in the shared structure relative to what could be in local (individuated) bandwidth. A maximally entangled state has *all* the relevant bandwidth shared; a product state has none.

Bell-inequality tests measure how much shared bandwidth survives the local measurements. CHSH = 2 is the classical bound (no shared bandwidth); CHSH = 2√2 is the maximum the participation graph permits (saturated shared bandwidth consistent with no-signaling).

### 5.3 Decoherence as bandwidth redistribution

When a quantum system interacts with an environment it was previously isolated from, internal rule-bandwidth does not vanish — it redistributes into environmental bandwidth. The system loses access to its multi-channel coherent state because its internal bandwidth is no longer sufficient, relative to environmental bandwidth, to maintain the inter-channel phase relationships.

This is why decoherence is in principle reversible (the bandwidth still exists, now distributed across environmental degrees of freedom) but in practice irreversible (the number of environmental degrees of freedom is too large to recollect). Spin-echo sequences work because they invert the bandwidth-redistribution process over intervals where environmental bandwidth hasn't dispersed beyond recovery.

### 5.4 Uncertainty relations as allocation inequalities

Heisenberg: a chain has a finite adjacency bandwidth budget. Position information requires adjacency-bandwidth in the configuration-space direction; momentum information requires adjacency-bandwidth in the Fourier-dual direction. The two allocations compete for the same budget:

`b_x · b_p ≥ K_adj`

where `K_adj` is the adjacency-graph structural constant. In thick-regime limit, `K_adj → ℏ/2`.

Energy-time: energy is associated with internal rule-bandwidth (the rate at which the chain's rule advances). Time-resolution requires adjacency bandwidth (to distinguish nearby commitment events). The two draw from different but linked bands; the ℏ/2 constant reappears because of the same underlying participation-graph normalization.

Number-phase: commitment-reserve is finite. Number-definiteness allocates it across many commitment events (narrow per-event); phase-definiteness allocates it along a rule-phase relation (narrow per-rule-cycle). The product constraint is the number-phase uncertainty relation.

**All uncertainty relations are allocation inequalities on bandwidth partitions of a common budget, normalized to ℏ by the structural constants of the participation graph in the thick-regime limit.**

### 5.5 Quantum Zeno effect as bandwidth competition

Rapid repeated measurement introduces high environmental bandwidth at a frequency faster than the system's internal rule-bandwidth can drive state evolution. At each measurement, commitment-reserve is drained back into the currently dominant channel. The chain's rule never has enough internal bandwidth budget to complete a rule-cycle that would move the state off the initial channel.

Zeno freezing = bandwidth starvation of the internal rule by repeated environmental bandwidth injection.

### 5.6 The four-band structure as the architecture of QM uncertainty

The four-band decomposition is not a convenience. It's the structural reason QM has multiple independent uncertainty relations rather than just one. Each pair of conjugate variables corresponds to two allocations drawing from a specific pair of bands:

| Uncertainty pair | Bands involved |
|---|---|
| Δx · Δp ≥ ℏ/2 | Adjacency-configuration × Adjacency-momentum (same band, two allocations) |
| ΔE · Δt ≥ ℏ/2 | Internal rule × Commitment-reserve (linked bands) |
| ΔN · Δφ ≥ 1 | Commitment-reserve × Internal rule-phase |
| Spin components | Different directional allocations of the chain's internal rule-bandwidth |

This gives a unifying architecture for the "many faces of uncertainty" in QM: they are the geometry of bandwidth partition in a four-band structure, all tethered to the same global bandwidth-budget constraint, with ℏ playing the role of the universal thick-regime normalization.

---

## 6. Simulator / PDE Instantiation

### Bandwidth in ED-Arch

- **Local coupling weights.** The update equation at each lattice site weights neighbor contributions. These weights are bandwidth — how much each neighbor's state counts toward the site's own update. Uniform coupling = uniform bandwidth; position-dependent coupling = a bandwidth landscape.
- **γ-sweep.** In ED-Arch-08, γ controls how sharply the update suppresses far-from-equilibrium configurations. Higher γ = tighter concentration of effective bandwidth near each core's own update — internal rule-bandwidth dominating over adjacency. Lower γ = adjacency-bandwidth dominates, cores diffuse, architecture melts.
- **Core stability.** A stable core is a bandwidth configuration in which internal rule-bandwidth exceeds environmental by enough margin to maintain the core's shape. Core collisions are bandwidth-exchange events; whether they annihilate, merge, or orbit is a bandwidth-flow outcome.

### Bandwidth in the Q-C Boundary PDE

The effective channel weight `D(x)` is the *ratio* of single-channel bandwidth to total-chain bandwidth at position `x` along the chain's trajectory. Explicitly:

`D(x) = b_dominant_channel(x) / b_total(x)`

- `D < 0.1`: bandwidth is spread across many channels; chain is in the thin, multi-channel, uncommitted regime.
- `D = 0.5`: critical concentration — exactly half of total bandwidth is in the leading channel. Sharp transition.
- `D > 0.5`: bandwidth is concentrated, committed regime; chain behaves classically.

The predictions from the PDE — N_osc ≈ 9 at low D, Q ≈ 3.5 at critical D, 3–6% third-harmonic generation — are all bandwidth-redistribution dynamics. Third-harmonic generation at the critical point is a bandwidth-nonlinearity signature of the commitment transition.

### What's missing

- **Bandwidth-counting in the discrete graph.** Given a participation graph with edge weights, what exactly is the normalization that makes bandwidth match ℏ when coarse-grained? This is the ED analog of the "why ℏ takes this value" question, and it bottoms out in the participation-graph structural constants.
- **Multi-chain bandwidth exchange.** When two chains participate via a shared region, what's the update rule for their bandwidth partition? Needed for scattering, entanglement formation, and multi-particle dynamics.
- **Bandwidth conservation vs. commitment cost.** A commitment event draws from commitment-reserve and redistributes the chain's bandwidth. What's conserved, what's consumed, what's converted into thickened structure?

---

## 7. Open Questions

1. **Normalization constant to ℏ.** What structural quantity in the participation graph sets the thick-regime value of ℏ? Phase 2 target — ties to Path A (QM as thin-regime effective theory).

2. **Sublinear composition.** Do interference phenomena require bandwidth composition to be sublinear (< sum) rather than strictly additive? Evidence from double-slit visibility and multi-path interferometers suggests yes. If so, the bandwidth measure is not additive on edge sets — a significant mathematical refinement. Phase 1/2 open.

3. **Four-band universality.** Is the four-band decomposition mathematically forced (by the participation-graph structural topology for any stable chain), or contingent? If forced, the four-fold structure of QM uncertainty relations has a structural explanation. If contingent, the number of uncertainty relations is a regime-dependent feature. Phase 2 target.

4. **Bandwidth and entropy.** Von Neumann entropy of a quantum state is a bandwidth-partition quantity. What is the ED account of entropy, exactly? Likely: the log of the effective number of channels bandwidth is distributed across. Needs formal treatment; connects to thermodynamic entropy in the thick regime.

5. **Horizon-bandwidth bottleneck.** Participation bottlenecks at horizons (ED-10 §8.2) imply bandwidth flow across them is suppressed or zero. Entanglement-bandwidth can still be shared because it isn't flowing. How does this interact with the area-law scaling of horizon entropy? Connects to holographic / black-hole thermodynamics; Phase 4 target.

6. **Bandwidth quantization.** Is bandwidth fundamentally continuous or does it quantize at some scale? If quantized, the quantum of bandwidth is the structural analog of ℏ. If continuous, ℏ is a normalization constant rather than an intrinsic quantum. The empirical fact that ℏ is a fixed constant rather than a scale-dependent parameter weakly suggests quantization — but nothing forces it yet.

7. **The η thread, bandwidth form.** Per Primitive 03 §7.4, the participation selection rule in saturated ED flow selects aligned-tension chains. In bandwidth terms: in saturated regimes, available commitment-reserve bandwidth is below the threshold needed to instantiate anti-aligned rule updates. The ratio of survivable-chain count to total-commitment-event count yields η. Formalizing this bandwidth-threshold selection is the path to the first-principles η derivation. **Phase 4 priority target.**

---

## 8. Citation format for other ED work

> *Per `quantum/primitives/04_participation_bandwidth.md` §1* — for the four-band structural claim.
> *Per `quantum/primitives/04_participation_bandwidth.md` §2* — for the allocation-inequality formulation of uncertainty relations.
> *Per `quantum/primitives/04_participation_bandwidth.md` §5.4* — for the unifying account of Heisenberg / energy-time / number-phase uncertainty.
> *Per `quantum/primitives/04_participation_bandwidth.md` §7.7* — for the η bandwidth-selection derivation thread.

---

## 9. One-line summary

> **Participation bandwidth is the graded scalar measure of how richly participation connects micro-events, chains, and regions. It is what coherence retains, what entanglement shares, what decoherence redistributes, and what the four-band partition structure underlies — giving a unified account of the many uncertainty relations of QM as allocation inequalities on a common bandwidth budget normalized to ℏ in the thick regime.**
