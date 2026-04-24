# Primitive 07 — Channel

**Role in the framework:** A channel is a stable pathway through participation structure — a locally coherent, bandwidth-preserving sub-pattern of the participation graph that supports chain propagation. Where Primitive 02 establishes what a chain *is* (atoms + rule) and Primitive 06 establishes the directional landscape chains move through, Primitive 07 establishes the *tracks*. Channels are the infrastructure that chains ride on: every propagation, every tunneling event, every superposition branch, every emission-absorption process, every superconducting pathway, every photonic mode is a channel or a channel network. Channels are the operational object connecting the ontological primitives (01–06) to the phenomenological apparatus of quantum mechanics (amplitudes, branches, modes, transitions).

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**A channel** is a stable, bandwidth-preserving sub-structure of the participation graph along which a chain's update rule can be instantiated repeatedly without rule-incompatibility. Operationally: a channel is *"a direction a chain can keep going in."* It is a locally coherent alignment of participation adjacency, bandwidth, and gradient structure that supports repeated, rule-consistent micro-event addition.

Channels are not the chains themselves. A chain is the rule and the sequence of micro-events instantiating it; a channel is the pre-existing pathway structure that allows the chain's next micro-event to participate rule-consistently with the previous one. A chain *uses* a channel. Multiple chains can use the same channel; a single chain can span multiple channels (by transitioning); a single channel can support alternative chain rules depending on which rule-types the channel's structure permits.

### What a channel *is*

- **A sub-structure of the participation graph.** Specifically: a locally coherent region of participation adjacency whose bandwidth kernel and ∇ρ structure support a specific rule-type.
- **Stable.** A channel persists beyond the passage of any individual chain — it is infrastructure, not a trail left by traffic. (A trail would be the thickening (Primitive 12) laid down by a committed chain; a channel is the structure that invited the chain in the first place.)
- **Rule-type-selective.** A channel admits chains with rule-types compatible with its structure and excludes incompatible rule-types. A photon-type channel supports null-chain propagation; a Cooper-pair-type channel supports paired-electron rules; a gravitational-wave-type channel supports bulk-ρ-oscillation rules.
- **Directional (usually).** Because channels form preferentially along ∇ρ or bandwidth-gradient structure, they carry a natural direction of propagation in the thick regime. In deeply-isotropic regions channels can be directionless, but these are limiting cases.
- **Countable.** In any given region, the number of available channels of a given rule-type is finite (usually small). This countability is what Primitive 08 (Multiplicity) captures.

### What a channel is *not*

- **Not a chain.** See above.
- **Not a field mode.** In QFT, a "mode" is a pre-existing basis function on a pre-existing manifold. A channel is a structural feature of the participation graph itself. In the thick regime, the mode decomposition of a QFT field emerges from the channel spectrum — but the channel is prior.
- **Not a wavefunction.** A QM wavefunction is a distribution of participation weight across the available channels for a given chain. The channels are the indices being summed over; the wavefunction is the weighting. Different object, different role.
- **Not a world-line.** A world-line is the trajectory a chain *did* take. A channel is a trajectory a chain *could* take — all channels a chain didn't use still exist, still affect dynamics (via interference), and still count for multiplicity.
- **Not a gauge orbit.** Gauge-orbit language in standard physics packages equivalence classes of field configurations. Channels are concrete structural features of the participation graph — not equivalence classes. Gauge-like behavior arises from channel topology (Primitive 03 §7.2; Primitive 06 §7.6), not from channel identity.

### The channel / chain / commitment triangle

Three objects, three roles:

- **Channel (07)**: the pre-existing pathway (infrastructure)
- **Chain (02)**: the thing that uses the pathway (traffic + identity-rule)
- **Commitment (11)**: the act of selecting one pathway at a given step (decision)

All three are needed to recover QM phenomenology. A chain in a multi-channel region is in superposition (multiple channels contributing bandwidth); a commitment event selects one channel; the post-commitment chain is "in" that channel; thickening (12) locks the choice into classical structure.

---

## 2. Mathematical Object

### Discrete version

In the participation graph `G = (V, E, w = b, ρ)`:

A channel `K` of rule-type `τ` is a pair `K = (V_K, E_K)` consisting of a connected subgraph of `G` satisfying:

- **Rule-compatibility:** the structure of `(V_K, E_K, b|_{E_K}, ρ|_{V_K})` supports the update rule `τ` — i.e., for any vertex `u ∈ V_K`, the rule `τ` can be instantiated by selecting an adjacent vertex `v ∈ V_K` whose bandwidth and ρ structure satisfies `τ`'s compatibility condition.
- **Bandwidth coherence:** the bandwidth along `E_K` satisfies a locally-preserved coherence condition — essentially, `b_{uv}` varies smoothly along adjacent edges in `E_K`, so that a chain traversing the channel doesn't hit sudden bandwidth drops.
- **Stability:** small perturbations of ρ or b within `V_K` do not destroy the channel's rule-compatibility.

The *rule-type* `τ` is a label drawn from a finite (structurally determined) set of compatible rule-classes. In the thick regime, these labels correspond to standard particle species, photon polarizations, phonon modes, Cooper pair states, etc.

### Continuum version

In the thick regime, channels become smooth tube-like structures on the emergent manifold, each labeled by:

- A rule-type / species label
- A local direction (tangent vector field along the channel axis)
- A local bandwidth profile
- A local ρ profile

The formal object is approximately a **fibered sub-manifold** of the emergent spacetime, fibered by the rule-type structure. Lattice / photonic / superconducting contexts give cleanly tractable examples.

### Channel space

At a given participation-graph region, the space of *all* available channels (across all rule-types) forms a labeled set with structure:

`𝒞(R) = { K : K is a channel in R }`

The multiplicity of a rule-type in R is `|𝒞_τ(R)|` — the count of channels of type τ in region R. This will be Primitive 08's central object. When `|𝒞_τ(R)| > 1` for a single chain of type τ, the chain sits in a superposition across those channels until a commitment event selects one.

### Channel composition

Channels can compose in several natural ways:

- **Sequential composition:** two channels sharing an endpoint can be traversed as a single extended channel
- **Branching:** a channel can fork into two (a Mach-Zehnder beamsplitter is a channel fork)
- **Merging:** two channels can merge (recombination at a beamsplitter's second stage)
- **Interference:** two merged channels produce bandwidth-coherent or -decoherent recombination depending on relative phase — the signature of single-chain double-channel propagation

These composition laws are the operational content of QM branch / path algebra.

### What is *not yet* settled

- **Classification of rule-types.** What is the complete structural classification of channel-compatible rule-types? This is the ED analog of the particle-species inventory. Bottom-up: derive from participation-graph structure. Not yet done.
- **Channel-stability condition formalism.** "Small perturbations do not destroy rule-compatibility" needs explicit mathematical form — a Lyapunov-like condition, a spectral gap, or similar.
- **Metric on channel space.** Channels can be "close" (differ by small structural deformations) or "far." A metric on 𝒞 would let us speak of channel continuity, channel transitions, and the geometry of the phenomenological channel landscape.

---

## 3. Relations to Earlier Primitives

### Upstream dependencies

| Primitive # | Role |
|---|---|
| 01 Micro-event | Channels are sub-structures on the vertex set |
| 02 Chain | Channels exist to support chains; rule-compatibility is definitionally tied to chain rule-types |
| 03 Participation | Channels are sub-structures of the participation graph |
| 04 Participation bandwidth | Channel coherence is a bandwidth-profile condition |
| 05 Event density | Channel viability depends on the ρ profile along the channel |
| 06 ED gradient | Channels preferentially form along ∇ρ structure; ∇ρ is the early-stage scaffolding of channel nucleation |

Primitive 07 is the first primitive that depends on *all* earlier primitives. This is why it sits where it does in the order: everything structural (atoms, rules, relations, weights, counts, directions) must be in place before we can talk about *stable pathways combining all of them*.

### Downstream

| Primitive # | How it uses channels |
|---|---|
| 08 Multiplicity | Counts channels in a region — the direct measure on the channel space |
| 09 Tension polarity | Polarity is a phase relation along a specific channel (the channel supplies the direction, polarity supplies the phase) |
| 10 Individuation | Individuation boundaries run along channels where bandwidth-coupling between inside and outside is sparse |
| 11 Commitment | A commitment event selects one channel from those available — channels are the thing being selected over |
| 12 Thickening | Thickening accumulates committed structure along selected channels |
| 13 Relational timing | Channels carry phase-coupling relations; timing is the rhythmic structure on channel dynamics |

### Circular-definition flags

1. **"Rule-type"** in §1 and §2 — the full taxonomy of rule-types is determined by what the participation graph structurally supports, which is a Phase 2 derivation target. Used here as a placeholder with operational meaning: rule-types are the labels that classical physics calls "species" (photon, electron, Cooper pair, phonon, etc.).
2. **"Stable"** in §1 — formal stability condition is open (see §2). Operationally: a channel is stable if small perturbations don't destroy rule-compatibility.
3. **"Superposition"** mentioned in §1 — forward-references Primitive 11 (Commitment) and Primitive 10 (Individuation). Here: a chain distributed across multiple channels before commitment.

---

## 4. Measurable Signature

### Direct observable consequences

- **Spectral lines / level structure.** Atomic, molecular, and solid-state spectra reflect the discrete channel structure available to a chain of a given rule-type in a given ρ / b environment. Each transition is between two channel configurations.
- **Scattering cross-sections.** The cross-section for a process is determined by the channel availability and bandwidth matching between initial and final states.
- **Tunneling rates.** A tunneling event is a chain traversing a channel whose bandwidth profile dips across a barrier region. The tunneling rate is a channel-structural quantity: wider bandwidth depression in the barrier → lower rate.
- **Interference fringes.** The two-slit experiment is single-chain double-channel propagation; fringes are the bandwidth-coherent recombination pattern at the screen.
- **Superconducting critical currents.** Determined by the bandwidth capacity of the channel spanning the superconductor; depairing is channel breakdown.
- **Photonic band structure.** In engineered photonic media, the bandgap is a ρ / b-structured region of the participation graph that does not support null-chain channels at certain frequencies.
- **Topological mode counting.** Chern numbers, topological invariants — count classes of channels distinguished by participation-graph topology (Primitive 03 §7.2; Primitive 06 §7.6). ED-I-14.
- **Neutrino oscillations.** Flavor oscillations are channel-transition dynamics: a chain's rule re-aligns coherently as it traverses different ρ environments, moving between flavor channels.

### Indirect consequences

- Chemical reaction rates (transition-state channels)
- Phonon dispersion relations (channel spectrum of bulk modes)
- Josephson oscillation frequency (channel-phase dynamics; ED-I-23)
- Cavity QED mode structure (channel discretization from geometric confinement; Haroche regime)
- Selection rules in atomic physics (rule-type matching conditions at a transition)

### Operational handle

- **ED-Arch simulator.** Channels appear as the stable bandwidth-preferential paths between cores in the simulator. Core-core interaction outcomes (hover, orbit, merge, annihilate) are channel-selection outcomes at the core scale.
- **Q-C Boundary PDE.** The PDE's effective channel weight D(x) is exactly a channel-count-and-dominance quantity. D < 0.1 = many channels contributing; D = 0.5 = critical; D > 0.5 = single-channel dominance.
- **Photonic simulations, superconductor models, atomic-structure calculations.** All of these are in-principle re-interpretable as channel-structure calculations with the standard methodology serving as a specific coarse-graining of the underlying channel apparatus.

---

## 5. Example Applications

### 5.1 The double-slit experiment as two-channel single-chain propagation

Each slit is a channel for null-chain (or massive-chain) propagation through the apparatus. A chain emerging from the source has non-negligible bandwidth in *both* channels simultaneously — the chain is distributed across both channels until a commitment event at the screen. The interference pattern is the bandwidth-coherent recombination of the two-channel distribution.

Which-path measurement = forcing a commitment event at one slit, which selects one channel and destroys the coherent multi-channel structure. No fringes.

The classical "wave-particle duality" question — what is the electron doing between source and screen — has a clean ED answer: the chain is *using two channels at once*. The channels are real structural features of the apparatus (carved out by the geometry and the ρ / b profile); the chain distributes across them per the usual bandwidth-preference rule; commitment forces selection.

### 5.2 Tunneling as channel continuity through a bandwidth-depressed region

A potential barrier in standard QM is, in ED, a region of depressed bandwidth for the relevant rule-type. The channel may still continue across the barrier — channel continuity is determined by whether any rule-compatible adjacency path exists, not by how much bandwidth it carries. If the path exists, the chain has non-zero probability of traversing it.

The exponential suppression of tunneling rate is a bandwidth-profile dependence: narrow barriers with modest depression allow substantial through-channel bandwidth; wide or deep barriers suppress it exponentially. WKB-type calculations are bandwidth-profile integrations along channel-continuation paths.

### 5.3 Superconductivity as a macroscopic channel

A superconductor supports a single macroscopic channel spanning the material, compatible with Cooper-pair rule-type. The channel is stable because the bandwidth profile and ρ structure resist perturbation (pair binding, BCS gap, coherence length). A current flows as chain traffic along this channel — no dissipation, because there are no competing channels to leak into at the rule-compatibility level.

Josephson effects are channel-pair dynamics: two superconducting channels separated by a thin insulating gap form a single composite channel with specific phase-relation dynamics. The AC Josephson frequency is channel-phase precession at a rate set by the bandwidth-asymmetry across the junction (ED-I-23).

### 5.4 Neutrino oscillation as channel-mixing along propagation

A neutrino is a chain of rule-type νᵢ (i ∈ {e, μ, τ}). The three flavor channels are nearly-but-not-exactly mutually exclusive at the participation-graph level — there is cross-coupling. As the chain propagates, its instantaneous rule-identity precesses among the flavor channels with the characteristic oscillation length. Detection events commit to one flavor channel.

Mass eigenstates are the fixed points of the propagation dynamics; flavor eigenstates are the commitment endpoints. The mixing angles are the channel-coupling strengths, structurally set by the participation-graph topology in the low-energy regime.

### 5.5 Atomic spectra as discrete channel configurations

An atom is a bound-state chain complex. The channels available to the electron-chain in the atom's ρ / b landscape are discrete (reflecting the compact geometry and the rule-compatibility conditions of the electromagnetic rule-type). Each channel is a stationary configuration. Transitions are commitment events that re-select channels, with bandwidth conservation forcing emission or absorption of a photon-chain of matching bandwidth-equivalent.

Selection rules (ΔL = ±1, ΔS = 0, etc.) are rule-type-matching conditions at the transition. Forbidden transitions are rule-type mismatches that require higher-order processes.

### 5.6 Photonic band structure as ρ-engineered channel landscape

In a photonic crystal, periodic ρ variations produce null-chain channel spectra with gaps: some frequencies have no channel, others have many. The propagation of light through the crystal is entirely determined by which channels exist at that frequency.

Topological photonic edge states — where null-chain channels exist only at boundaries and are robust against disorder — are channels stabilized by global participation-graph topology (ED-I-12, ED-I-14). Robustness follows because destroying them requires changing global topology, not local structure.

---

## 6. Simulator / PDE Instantiation

### Channels in ED-Arch

- Stable bandwidth-preferential paths between cores are emergent channels at the simulator scale
- Core-core interaction outcomes (hover, orbit, merge, annihilate) depend on whether the bandwidth structure between them supports a stable chain-connecting channel
- Scattering-grid studies are maps of channel availability as a function of core separation and approach angle
- The γ-sweep modulates channel stability: higher γ = sharper, more rigid channels; lower γ = diffuse, merging channel structure

### Channels in the Q-C Boundary PDE

- `D(x)` is the channel-dominance variable along a propagating chain
- D < 0.1: many channels contributing bandwidth; chain in multi-channel uncommitted state
- D = 0.5: critical — the transition from multi-channel to single-channel dominance
- D > 0.5: single-channel dominance; chain has effectively committed
- N_osc ≈ 9 at low D: the chain explores ~9 channels coherently before commitment begins
- Q ≈ 3.5 at critical: the sharpness of the channel-selection transition
- 3-6% third-harmonic: channel-nonlinearity signature at the selection transition

### Channels in other ED simulator / PDE work

- GR-SC 1.0+ arc implicitly uses channel-level quantities in the curvature-invariant measurements
- ED-SC 3.x arc's motif-based analysis probes the structure of committed vs. uncommitted channel configurations (the `f(ρ | ξ, L_ray, α_filt, N_req)` distribution is essentially a channel-commitment distribution)

### What's missing

- **Formal bridge from D(x) to channel-count.** D is operationally a channel-dominance variable, but the explicit map D ↔ channel-count structure hasn't been written out in full.
- **Channel-spectrum classification for typical rule-types.** Given a standard chain rule-type (Dirac-like, photon-like, Cooper-like), what is the predicted channel spectrum from the underlying ED structure? Phase 2 work.
- **Channel dynamics under commitment events.** How does the channel spectrum locally re-arrange when a commitment event occurs? The PDE handles this implicitly through D dynamics; the explicit channel-level bookkeeping is not yet written out.

---

## 7. Open Questions

1. **Rule-type taxonomy.** What is the structural classification of channel-compatible rule-types? The ED analog of the particle-physics species inventory. Deriving this from participation-graph structure would give ED its version of "why these particles and no others."

2. **Channel-space geometry.** A metric on 𝒞 would let us speak of channel continuity, transitions, and the manifold structure of the phenomenological channel landscape. Connects to the formal structure of QM Hilbert space in the thin regime (Phase 2 Path A).

3. **Stability condition formalism.** The operational "small perturbations don't destroy rule-compatibility" needs an explicit mathematical condition — likely a spectral gap or Lyapunov-type criterion tied to the (ρ, b, ∇ρ) structure at the channel.

4. **Channel topology and gauge structure.** Per ED-I-14, gauge-like phases arise from non-trivial channel topology. Developing this into an explicit participation-cohomology theory — showing that U(1), SU(2), SU(3) arise as specific channel-topology classes — is the route to the ED account of gauge theory. Phase 2 / 3 target.

5. **Channel-spectrum ↔ QFT mode-spectrum correspondence.** The thick-regime mode decomposition of a QFT field should reduce to the channel-spectrum of the underlying participation graph. Explicit correspondence is Phase 2 Path A work.

6. **Interference as bandwidth coherence on the channel lattice.** The formal statement that two-channel single-chain propagation produces interference fringes with the standard QM amplitude rule needs an explicit derivation from bandwidth-coherence conditions along the composed channels. Phase 2 Path A target.

7. **The η thread — channel survival in saturation.** Per Primitive 03 §7.4 and Primitive 06 §5.4, baryogenesis selection filters channels by tension polarity against ∇ρ in saturated regions. In channel terms: only channels whose rule-type is phase-aligned with ∇ρ survive the saturation transition. The ratio of surviving-channel count to total-channel count yields η. Phase 4 priority — this thread now has four hooks (ρ level in 05, gradient level in 06, bandwidth level in 04, and channel level here), all pointing at the same derivation.

---

## 8. Citation format

> *Per `quantum/primitives/07_channel.md` §1* — for channel as stable pathway infrastructure.
> *Per `quantum/primitives/07_channel.md` §1 (triangle)* — for the channel / chain / commitment relationship.
> *Per `quantum/primitives/07_channel.md` §2* — for the discrete-graph definition.
> *Per `quantum/primitives/07_channel.md` §5.1* — for two-channel single-chain propagation as the double-slit account.
> *Per `quantum/primitives/07_channel.md` §5.4* — for neutrino oscillations as channel-mixing.
> *Per `quantum/primitives/07_channel.md` §7 (7)* — for the channel-level framing of the η derivation.

---

## 9. One-line summary

> **A channel is a stable, bandwidth-preserving sub-structure of the participation graph that supports a specific chain rule-type — the infrastructure chains propagate along. Channels are countable, rule-selective, and compose by branching / merging to give the full phenomenology of superposition, interference, tunneling, flavor oscillation, superconductivity, photonic band structure, and topological modes.**
