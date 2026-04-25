# Primitive 02 — Chain

**Role in the framework:** The first composite structure built from micro-events. A chain is what makes "identity across events" possible in ED. Everything that persists, propagates, or maintains itself — particles, photons, atoms, Cooper pairs, neutrinos, macroscopic bodies — is a chain or a system of chains.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

A **chain** is a sequence of micro-events bound together by a consistent update rule. A chain is not the micro-events alone and not the rule alone — it is the pair. The sequence gives the chain its trajectory; the rule gives the chain its identity.

### What a chain *is*

A chain is defined by three things:

- **A totally-ordered sequence of micro-events** connected by commitment-order edges in the participation graph (Primitive 01 §2).
- **An update rule** — a relation that determines, given the previous committed micro-event, how the next micro-event will integrate with the participation structure. The update rule is the chain's identity.
- **A coherence condition** — the update rule must be instantiable by the surrounding ED-flow at every step. If the ED-flow cannot support the rule, the chain cannot continue.

The chain's identity is encoded entirely in the update rule. Two chains with the same update rule are the same kind of chain regardless of which micro-events they traverse. Two chains with different update rules are different kinds of chains even if they traverse overlapping regions.

### What a chain is *not*

- **Not a world-line.** A world-line presupposes spacetime as a background manifold. A chain does not; the chain is prior to spacetime (see Primitive 01 §1, ED-10 §2.3). In the thick-participation regime, chains project onto world-lines — that's the correspondence — but the chain is the ontologically basic object, and the world-line is the coarse-grained shadow.
- **Not a sequence of particles.** A particle is what a stable chain looks like when coarse-grained. The chain is the underlying structure; the particle is the name for it at the macroscopic level (ED-09 §2.2).
- **Not a collection of parts.** A chain has no internal parts in the decomposable sense. It has no substructure to open up. Its identity is the update rule, and the update rule is irreducible — it either generates the next micro-event or it doesn't.
- **Not a physical trajectory through space.** Space emerges from stable participation adjacency (ED-10 §2). A chain's propagation is the sequential commitment of new micro-events along participation pathways; the apparent spatial trajectory is the thick-regime summary of that sequence.
- **Not a continuous entity.** The sequence is discrete because the underlying micro-events are discrete (Primitive 01 §1). Continuity in classical and quantum formalisms comes from coarse-graining over many discrete chain steps.

### Why the chain, not the micro-event, is where persistence lives

A single micro-event does not persist — it commits, contributes to the structure, and is done (Primitive 01 §1). Nothing in ED persists at the micro-event level. Persistence enters the framework at the chain level: it is the update rule that persists across the sequence of micro-events. This is the ED reading of *why anything continues to exist* — not because its constituents persist, but because a generating rule keeps producing new constituents that integrate the same way.

An electron does not persist because its "electron-particle" persists. It persists because its update rule (the electron chain rule) keeps producing new micro-events in the same relational pattern, until the environment disrupts the rule's instantiability (measurement, annihilation, decay).

---

## 2. Mathematical Object

### Candidate structure

A chain is a **pair** `(P, R)` where:

- `P` is a directed path in the participation graph: an ordered sequence of vertices (micro-events) connected by commitment-order edges.
- `R` is the chain's update rule: a function (or relation) that takes the chain's current state and the local ED-gradient structure, and produces the next micro-event's participation integration.

Schematically:

> `m_{n+1} = R(m_n, local_ED_gradient_at_m_n)`

where `m_n` is the n-th micro-event and `R` is the rule. The chain is the set `{m_0, m_1, m_2, ...}` together with `R`. Neither alone is the chain.

### Why `(sequence, rule)` rather than just a sequence

If the chain were only the sequence, then different chains with the same trajectory through the participation graph would be indistinguishable — which is false. A photon chain and a massive-particle chain can traverse the same region but have different update rules, and therefore are genuinely different chains. The update rule is what distinguishes them.

If the chain were only the rule, then the chain would have no concrete instantiation in the participation graph — it would be an abstract form with no content. The sequence is what gives the rule its physical footprint.

### What the update rule actually contains

The rule `R` encodes:

- **Conservation laws** for that kind of chain (energy, momentum, charge, spin, flavor — whatever is conserved for that chain type).
- **The coupling to ED-gradients** that determines the chain's propagation (null chains couple to null-geodesic participation pathways; massive chains couple differently).
- **The chain's tension polarity** (Primitive 09) — the phase relation between the rule and the local relaxation direction of ED-flow. This is how matter and antimatter differ at the chain level (ED-I-11 §4).
- **The minimum participation bandwidth** required to maintain the rule (Primitive 04).

### What is *not yet* settled mathematically

- **Is `R` deterministic or stochastic?** Deterministic at the rule level but probabilistic in outcome because the ED-gradient environment the rule is applied in is not uniform. Needs formalization.
- **Composition of chains.** When two chains interact (scatter, bind, annihilate, split), what operation on their update rules produces the outcome? Natural formalism: rule algebra — but not yet written down.
- **Chain equivalence.** When are two chains "the same kind of chain" in the formal sense? Presumably: when their update rules are equivalent under some symmetry (translation, rotation, Lorentz boost in the thick regime). Not yet formalized.

These are Phase 1 and Phase 2 open questions. The load-bearing claim — **a chain is a sequence-plus-rule composite, and its identity lives in the rule** — does not depend on which refinement wins.

---

## 3. Relations to Other Primitives

### Chain is a composite of

| Primitive # | How Chain uses it |
|---|---|
| 01 Micro-event | The atomic units the chain is a sequence of |

Chain has exactly one upstream dependency (Primitive 01). Everything else relates to Chain from downstream or laterally.

### Chain relates laterally or downstream to

| Primitive # | Relation |
|---|---|
| 03 Participation | The rule's applicability depends on the surrounding participation structure |
| 04 Participation bandwidth | The rule's stability depends on having enough bandwidth available |
| 05 Event density (ED) | Local ED determines whether the rule can be instantiated; high-ED regions stabilize rules |
| 06 ED gradient | The rule's coupling to gradients determines the chain's trajectory |
| 07 Channel | A channel is a stable participation pathway on which a chain's rule can be continuously instantiated |
| 08 Multiplicity | A chain in a low-multiplicity region has few available channels; in high-multiplicity regions it explores many |
| 09 Tension polarity | A property of the chain's update rule — whether it is phase-aligned with the relaxation direction of ED-flow |
| 10 Individuation | A threshold condition on accumulated ED-structure that allows a chain to support a distinct update rule |
| 11 Commitment | The event in which a chain's micro-event selects a single channel from multiple uncommitted possibilities |
| 12 Thickening | The accumulation of many parallel/reinforcing chains produces classical macroscopic structure |
| 13 Relational timing | The phase rhythm of the chain's commitments relative to surrounding chains |

### Circular-definition flags — where Chain leans on not-yet-defined primitives

This is the honest accounting of where Chain's definition borrows from primitives that haven't been drafted yet. These are places to revisit in the tightening pass.

- **"Consistent update rule"** (§1) leans on Primitive 09 (Tension Polarity), which is where update-rule alignment with ED-flow is formally defined. Until 09 is drafted, "consistent update rule" means "a rule that continues to be instantiable," which is load-bearing but not fully formal.
- **"Coherence condition"** (§1) leans on Primitive 07 (Channel) — a channel is precisely the stable participation pathway that a chain's rule can ride on. Until 07 is drafted, "coherence condition" is defined operationally rather than structurally.
- **"Chain's identity"** (§1) leans on Primitive 10 (Individuation) — what it means for a chain to have a *distinct* identity (as opposed to being a fragment of a larger shared structure, as in entangled states) is formally handled by the individuation threshold. For chains in the individuated regime, identity is clean; for chains in the non-individuated (entangled) regime, identity is shared.
- **"Chain termination"** (§5.4) leans on Primitives 11 (Commitment) and 12 (Thickening) — a chain "ends" when either its rule becomes inconsistent with the environment (forced commitment into a different rule) or it merges into thickened classical structure (macroscopic absorption).

The conclusion: Primitives 01, 02, 03 form the relational triad, and then 07, 09, 10 are the next layer that sharpens Chain's definition. Everything downstream of those is clean.

---

## 4. Measurable Signature

### What is observable

Chains manifest as **persistent identities** — anything that can be tracked, followed, or re-identified across time. This is the empirical handle.

- **Particle tracks in detectors.** The trail an electron, muon, or charged hadron leaves in a detector is the thick-regime signature of the chain's committed micro-events. The track is not the chain; the track is what the chain's commitment pattern looks like when coarse-grained against the detector medium.
- **Quantum numbers conserved along a process.** Whenever a quantum number is conserved (electric charge, baryon number, lepton number, spin, flavor within interactions that respect it), that conservation law is the observable expression of an invariant in the chain's update rule. Conservation = rule invariance.
- **Coherence times in atomic and molecular systems.** How long an atom or molecule maintains a stable quantum state (coherence time, T₂) measures how long the chain's update rule can remain instantiable before environmental ED injection disrupts it (ED-09 §6).
- **Photon flight through vacuum.** A photon traversing empty space is a null-chain whose update rule is perfectly stable as long as the participation bandwidth (vacuum bandwidth) is uniform. Photons stop being chains when they couple into absorbing matter — that's the rule's termination.

### Decoupled observables — what chains *do not* directly give you

- **Field amplitudes.** A field amplitude in QFT is an aggregate measure over many chain-like excitations and their relational participation structure. It's a coarse-grained quantity. The chain is the microscopic ingredient.
- **Waves and wavelengths.** A wave is a pattern in chain population density or chain phase structure across space. Not a chain itself. Wave-particle duality (Primitive 01 §1 "Why this inversion matters") is the apparent paradox of chains-as-particles vs. chain-population-statistics-as-waves; dissolved once you realize these are two coarse-grainings of the same underlying chain structure (ED-09 §2.2).

### Operational handle (simulator / PDE)

In the ED-Arch simulator, a **core** (the emergent localized ED-structure in Scenario E) functions operationally as a chain's manifestation at the macro level. Each core has a persistent identity through the simulation time steps; cores can merge, annihilate, or hover/orbit; and their identity is maintained by the local update rule (γ-stiffened curvature well). This is the closest the existing simulation comes to a direct empirical handle on chains.

In the Q-C Boundary PDE (ED-Phys-16/17, P6, 00.3), the effective channel weight `D(x)` is the parameter that controls when a chain is in the thin-uncommitted regime (D < 0.1, chain explores many participation channels) versus the thick-committed regime (D > 0.5, chain commits to a single channel). The sharp D = 0.5 transition is the chain's regime change from quantum-like to classical-like behavior.

---

## 5. Example Applications

### 5.1 Particle identity

An electron is a chain whose update rule encodes the electron quantum numbers — charge −1, spin ½, lepton number +1, etc. — and whose coupling to ED-gradients determines how it propagates. The "same electron" at t=0 and t=1 is the same chain, not because any micro-event persisted, but because the electron update rule kept producing new micro-events in the electron-characteristic participation pattern. Electron stability is the stability of its update rule against environmental disruption.

Particle decay is the event in which the chain's update rule becomes inconsistent with local ED-flow (for an unstable particle) and is replaced by product chains whose rules *are* consistent. The original electron chain terminates; muon, photon, etc., chains begin. Quantum numbers are conserved across the transition because the rule-algebra must balance (see §2 open question on rule composition).

### 5.2 Photon propagation

A photon is a **null chain** — a chain whose update rule couples to null-participation pathways (the ED-gradient structure that, in the thick regime, corresponds to null geodesics). Photons move at c because the null-chain rule is the one that saturates the causal participation limit (ED-10 §8.1, §8.6). The photon's "straight-line" travel in vacuum is the null chain's trajectory through a uniform participation manifold.

Bending of light near massive bodies is the null chain following a perturbed participation geometry — participation pathways curve near high-ED regions, and the null chain follows the available pathway. No force acts on the photon; the chain follows the geometry it's embedded in (Primitive 01 §1 "No singularity problem"; ED-10 §3.4).

### 5.3 Superconducting phase as a macroscopic chain

A superconducting region is a macroscopic chain — or more precisely, a hyper-coherent ED-structure whose internal participation has collapsed into a single shared update rule spanning the entire material (ED-I-23 §3). The "phase" of a superconductor is not a wavefunction property; it is the chain's relational timing (Primitive 13) across the extended structure.

Two superconductors separated by a Josephson junction are two regions of a single shared chain, because the barrier is too thin/sparse to force individuation between them (Primitive 10). The Josephson supercurrent is the flow of identity across the barrier — the chain reconciling timing differences between its two endpoints. No charge is transported in the classical sense; the chain's update rule continues across the barrier (ED-I-23 §3.3).

### 5.4 Neutrino oscillations as rule re-alignment along propagation

A neutrino is a chain whose update rule has a flavor component. As the chain propagates through regions with different participation environments (including vacuum with its residual ED structure), the flavor component of the rule re-aligns — the rule isn't identical at every step, it evolves coherently as the chain integrates new micro-events in different ED-contexts.

What we call "oscillation" is this re-alignment expressed in the observable flavor basis. The underlying chain is one chain throughout; its rule shifts gradually, producing the sinusoidal oscillation amplitude in the flavor-detection probability. No new chain is created; the old one doesn't end. The rule continues but with shifting internal structure.

### 5.5 Chain termination by environmental forcing

A chain ends when its update rule becomes incompatible with the surrounding ED-flow. Three mechanisms:

- **Measurement** — a measurement device is a high-multiplicity ED-structure that forces individuation (Primitive 10). The chain's multi-channel rule collapses to a single-channel committed rule. For a chain that was in a superposition-like state, this is the moment the chain's identity becomes definite.
- **Decoherence** — environmental ED injection proliferates channels and forces individuation across many sub-structures. The chain's rule becomes fragmented into many sub-chains (ED-I-02 §7; ED-09 §6).
- **Annihilation / decay** — the chain's rule becomes structurally unsustainable and terminates, producing daughter chains whose rules are sustainable in the local environment (see §5.1).

In all three, the chain does not vanish into nothing. Its rule either becomes a different rule (decay, measurement) or its structure is absorbed into thickened classical matter (decoherence into environment).

---

## 6. Simulator / PDE Instantiation

### Chains in the ED-Arch simulator

In Scenario E of the ED-Arch simulator, **emergent cores** — localized high-density regions that persist across update steps — are the operational instantiation of chains at the macroscopic-simulation level.

- A core has **persistent identity** across time steps (tracked by position/density threshold), which is the simulator's chain-identity handle.
- A core has an **update rule** (the Scenario E update rule applied to its local ED field), which is the simulator's analog of the chain's `R`.
- Cores **interact** (merge, annihilate, hover/orbit) — operations which are the simulator's realization of chain composition.
- ED-Arch-07 mapped the two-core interaction manifold; ED-Arch-08 extended this with the γ-sweep showing how curvature-well stiffness stabilizes core identity — which is, at the simulator level, the stabilization of chain identity against ED-flow disruption.

This is why ED-Arch simulations are so load-bearing for Chain as a primitive: the simulation is literally running chain dynamics at a coarse resolution where individual micro-events are below the lattice scale but core-chains are the emergent units.

### Chains in the Q-C Boundary PDE

The PDE (ED-Phys-16/17, P6, 00.3) treats the effective channel weight `D(x)` as the control parameter for a chain's regime:

- `D < 0.1`: chain is in the thin regime, multi-channel, showing quantum-like behavior (N_osc ≈ 9 transient oscillations, Q ≈ 3.5, 3–6% third-harmonic).
- `D > 0.5` (through the sharp transition at D = 0.5): chain is in the thick regime, single-committed, showing classical behavior.
- The triad coupling coefficient ≈ 0.03 is present in all regimes — a rule invariant.

The PDE is the continuum description of a chain's regime transition. The chain's behavior on either side of D = 0.5 is different not because the chain changes — it's still the same chain — but because the environment transitions from providing many viable channels (high multiplicity) to providing essentially one (low multiplicity).

### What's missing

- The derivation from micro-event discrete updates to the continuous PDE `D(x)`. Same Phase 2 / Phase 4 task flagged in Primitive 01 §6.
- The formal mapping between simulator `(α, m, γ)` parameters and PDE `D` — flagged in PROJECT_OUTLINE.md §6.
- A rule-algebra for chain composition (how two chains' update rules combine in scattering, binding, annihilation). Phase 2 open question.

---

## 7. Open Questions

1. **Rule algebra for chain interactions.** When two chains interact (scatter, bind, annihilate), what is the formal operation on their update rules that produces the outcome? Particle physics has scattering amplitudes; ED needs a rule-level analog that is more ontologically direct. Phase 2 target.

2. **Chain continuity across termination events.** When a chain "ends" via decay or measurement, the successor chains are new chains — but what is the precise formal relationship between the old rule and the new rule set? Conservation laws imply the rules are related by an invariant, but the invariant isn't yet written.

3. **Null chain vs. massive chain at the rule level.** What, formally, distinguishes a photon chain from an electron chain at the update-rule level? In the thick regime, it's mass and light-cone coupling; in the ED substrate it has to be something about how the rule couples to ED-gradients. Likely related to rule's tension polarity (Primitive 09) and relational timing (Primitive 13).

4. **Countability of chain types.** How many distinct update rules exist? Is there a finite taxonomy (corresponding to the Standard Model particle zoo)? A continuous family parameterized by ED-gradient coupling strength? This connects to the broader question of why the Standard Model has the particle content it does — an open problem ED could address but hasn't yet.

5. **Chain-count cosmological signatures — the η thread.** The baryon-to-photon ratio η ≈ 6 × 10⁻¹⁰ is, in ED terms, a ratio of two chain-count densities in the present universe: (surviving matter chains) / (photon chains). In the early universe's saturated regime, aligned-tension chains survived and anti-aligned-tension chains decohered (ED-I-11 §6–§7). The exact ratio 6 × 10⁻¹⁰ is the quantitative signature of the saturation-relaxation timeline. **Phase 4 derivation target.** Deriving this from ED dynamics with no free parameters would be the most consequential prediction in the program.

6. **Lorentz invariance of chain propagation.** Flagged in Primitive 01 §7.4 as a general concern. For chains specifically, the question is: does a chain's update rule transform consistently under Lorentz boosts in the thick regime? ED-09 §9.3 argues yes (because participation is relational and chains are not lattice-embedded); formal demonstration is Phase 2.

---

## 8. Citation format for other ED work

When citing this primitive from elsewhere:

> *Per `quantum/primitives/02_chain.md` §1* — for the definition of chain = (sequence, rule).
> *Per `quantum/primitives/02_chain.md` §2* — for the mathematical object.
> *Per `quantum/primitives/02_chain.md` §3* — for relations to other primitives (and circular-definition flags to revisit).
> *Per `quantum/primitives/02_chain.md` §4* — for the measurable signature.
> *Per `quantum/primitives/02_chain.md` §7 (5)* — for the η derivation thread.

---

## 9. One-line summary

> **A chain is a sequence of micro-events bound together by a consistent update rule. The sequence gives the chain its trajectory; the rule gives the chain its identity. The chain is the first composite structure in ED, and everything that persists — particles, photons, atoms, Cooper pairs, neutrinos, macroscopic bodies — is a chain or a system of chains. Identity lives in the rule; the rule is what the environment either sustains or disrupts.**
