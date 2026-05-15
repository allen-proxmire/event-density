# From Primitives to the Limits of Quantum Computation

## A Walkthrough of the Event Density Architectural Classification (UR-1 and the Multiplicity-Cap Function)

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1982, Richard Feynman proposed that quantum systems should be simulated by quantum computers. In 1994, Peter Shor proved that a sufficiently large quantum computer would break public-key cryptography in polynomial time. In the four decades since, an industry has formed around building such machines. Superconducting transmons at IBM and Google. Trapped ions at IonQ and Quantinuum. Photonic qubits at PsiQuantum and Xanadu. Topological qubits at Microsoft. Neutral atoms at QuEra and Atom Computing. The largest current devices have on the order of one thousand to ten thousand physical qubits, with substantial engineering effort directed at error correction, isolation from environmental noise, and gate-fidelity improvements.

The question that hangs over the entire program is: how far can it go? Is there a structural ceiling — a fundamental, framework-independent limit on the number of qubits that can be held in coherent superposition, or on the depth of circuits that can be executed before decoherence overwhelms the computation? Or is the limit purely engineering — better materials, better isolation, better error correction will eventually deliver fault-tolerant quantum computation at arbitrary scales?

Standard physics tells the story this way. Decoherence is environmental coupling. A qubit interacts with its surroundings — thermal photons, lattice vibrations, stray fields — and gradually loses its coherent superposition state to entanglement with the environment. The decoherence rate depends on coupling strength and environmental temperature. Engineering can reduce these factors, but never eliminate them. Quantum error correction can tolerate finite decoherence rates as long as they fall below specific thresholds, and the existence of fault-tolerant thresholds proven by Aharonov, Ben-Or, Kitaev, and others suggests that arbitrarily large quantum computers should be possible in principle. The remaining question, in the standard view, is engineering: can we cross the fault-tolerance threshold and build error-corrected qubits whose effective error rates are below the threshold for arbitrarily complex computation?

This is a coherent picture, and it has guided the field's development. But it leaves a structural question unanswered. Is the substrate of the universe indifferent to whether a system is in a coherent superposition or not? Or does the substrate place its own constraints on coherent superposition — constraints that engineering cannot work around because they are not engineering problems?

The Event Density framework provides an answer. The substrate has finite local participation density, finite cross-chain bandwidth, finite-width V1 and V5 kernels, and primitive commitment-irreversibility. These primitives are not silent on quantum computation. They jointly impose a substrate-level set of conditions that any system performing coherent quantum computation must satisfy. When the conditions are satisfied, the system holds the unresolved low-multiplicity regime in which coherent operations are possible. When any condition fails, the system individuates and the computation collapses.

The conditions are codified by Theorem UR-1 (Unresolved-Regime Characterization). They are three: bounded multiplicity, sustained cross-chain bandwidth, and commitment-injection below the individuation threshold. The conditions are jointly necessary and sufficient. Each can fail through a specific substrate failure mode. Each can be held against failure by a specific architectural strategy. The architectures are exhaustive at the substrate level: any quantum-computing platform is, structurally, one of three classes, or a composition of techniques over those classes. The classes have specific predictions, including a structural ceiling for one class that matches the empirically open matter-wave quantum-classical boundary at 140-250 kDa molecular mass.

This is not a claim that quantum computation is impossible. It is a claim that the substrate provides specific, falsifiable architectural constraints on what quantum computation can look like, and that the same substrate machinery that produces black-hole horizons and bipartite entanglement monogamy also produces the architectural classification of quantum-computing platforms. The cross-domain unification — quantum computing and black-hole physics governed by the same substrate $\Gamma_\mathrm{cross}$ structure at scales separated by fifty orders of magnitude — is the framework's strongest piece of cross-platform mechanism identity.

The chain has six structural moves:

1. The substrate has primitive load-bearing invariants — multiplicity $\mathcal{M}$, unresolvedness $\mathcal{U}$, gradient sparsity $\sigma$, cross-chain bandwidth $\Gamma_\mathrm{cross}$ — that govern any system's substrate-level state.

2. Quantum computation is, in the framework's reading, the deliberate occupation of a low-multiplicity unresolved regime where coherent operations on the substrate's participation rule can be performed before commitment is forced.

3. UR-1 establishes the three-condition gate: a substrate region $\mathcal{S}$ admits $\mathcal{U}(\mathcal{S},t) \approx 1$ if and only if multiplicity is bounded, cross-chain bandwidth is sustained, and commitment-injection is below the individuation rate.

4. Three substrate failure modes drive the three conditions to failure: premature individuation from environmental ED-injection (F1), cross-endpoint decoupling from $\Gamma_\mathrm{cross}$ collapse (F2), and commitment-pressure cascade from accumulated P11 events (F3).

5. Three architectural classes — engineered-low-multiplicity (A), global-geometric-rigidity (B), high-multiplicity-redundancy (C) — are exhaustive substrate-permitted strategies for holding the conditions against the failure modes. Meta-architectures (error correction, dynamical decoupling, reservoir engineering, hybrids) are compositions over the three classes, not separate classes.

6. The multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ relates the architectural class, system multiplicity load, environmental coupling, and operational structure to the maximum coherent-computation timescale, with three sharp predictions: a Class A wall at the substrate-multiplicity threshold, a Class B exponential coherence advantage in the topological-protection regime, and a Class C correlation-budget plateau for redundancy-architecture systems.

The structural payoff: quantum computation has a substrate-level architectural classification with falsifiable predictions. The three classes are exhaustive. The Class A wall is at the matter-wave quantum-classical boundary of 140-250 kDa molecular mass — currently 5-10 times beyond the largest demonstrated coherent superposition, with active experimental programs targeting that range. The Class B exponential advantage is the substrate-level reason topologically-protected qubits (Majorana fermions, Fibonacci anyons) outperform Class A qubits at sufficiently low temperatures relative to topological gap. The Class C plateau is the substrate-level constraint on how far redundancy-based architectures (large-scale error correction, neutral-atom arrays) can push qubit count before cross-bandwidth budget saturates.

---

## 2. The Primitives That Matter

The framework rests on substrate-level ontological commitments. The quantum-computing walkthrough uses the same working subset that Born, Schrödinger, and the gauge-fields walkthrough used, plus the substrate-level invariants that recur across the program's mid-level structural results.

**Micro-events (P01).** Discrete acts of becoming, vertices in a graph spanning the event manifold.

**Chains (P02).** Stable subgraphs along which a chain repeatedly instantiates its update rule.

**Bandwidth (P04).** The graded measure of participation, with bandwidth-additivity for independent contributions.

**Polarity / U(1) phase (P09).** $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction.

**ED gradient.** Continuous spatial axis with no preferred origin.

**Commitment irreversibility (P11).** Once a chain selects one channel from those available, the commitment is irreversible. This is the substrate primitive that makes the unresolved/individuated distinction sharp.

**Continuous time (P13).** The substrate's temporal evolution is continuous.

**Substrate locality.** Participation contributions at one substrate region combine with those at another only via mediating substrate structure (chains, V1 kernel, channels).

**Rule-type (Primitive 07).** Each chain carries a primitive label classifying the structural form of its update rule.

Three forced theorems load-bear specifically here:

**T18 (V1 forward-cone-only retardation).** The V1 substrate kernel is forward-cone-only, mediating cross-chain correlations causally.

**T17 (Gauge-field-as-rule-type connection).** Establishes that gauge fields are the substrate's rule-type connection. Used implicitly when discussing topologically-protected qubit architectures.

**T19 (Newton's $G = c^3 \ell_P^2/\hbar$).** Identifies the Planck length $\ell_P$ as the substrate's irreducible length scale.

The Diffusion Coarse-Graining Theorem (DCGT) is a structural prerequisite: the substrate-to-continuum bridge that makes $\Gamma_\mathrm{cross} \sim \exp[-\alpha \int \sigma\, d\ell]$ a substrate-derived rather than postulated quantity.

Four substrate-level invariants load-bear specifically for the quantum-computing arc.

**Multiplicity $\mathcal{M}(\mathcal{S})$.** The count of substrate-resolvable participation channels available to a system $\mathcal{S}$. Operationally, this is the substrate's analogue of statistical-mechanical entropy — it counts the distinct ED-gradient pathways the system's current ED-structure can support. $\mathcal{M} \to 1$ corresponds to a hyper-coherent regime (a single viable participation pathway); $\mathcal{M} \to \infty$ corresponds to the classical thermal regime.

**Unresolvedness $\mathcal{U}(\mathcal{S}, t) \in[0, 1]$.** The integrity of a participation rule that spans multiple endpoints of $\mathcal{S}$ at substrate time $t$. $\mathcal{U} \to 1$ when the rule remains coherently un-individuated across all designated endpoints. $\mathcal{U} \to 0$ when the rule has fully individuated. $\mathcal{U}$ is the dynamical state quantifier; $\mathcal{M}$ is the capacity quantifier.

**Gradient sparsity $\sigma(\mathbf{x}) = |\nabla\rho|\, \ell_P^2 / \rho_\mathrm{local}$.** The substrate-scale steepness of participation density.

**Cross-chain bandwidth $\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2) \sim \exp[-\alpha \int_\mathrm{path} \sigma\, d\ell]$.** The DCGT-derived substrate-level bandwidth between two regions, with the integral running along the substrate-locality-permitted path between them.

That's the structural setup. The quantum-computing argument runs on this.

---

## 3. The Substrate Reading of Quantum Computation

A "quantum computer," in standard language, is a device that maintains a coherent superposition over many degrees of freedom, performs unitary operations on that superposition, and reads out a classical result. Three of those four words require translation into substrate language.

**Coherent superposition** is, in the framework's reading, the persistence of an unresolved participation rule spanning multiple endpoints. It is not a state being in two places at once; it is the absence of individuation across a participation structure that has not yet committed. In substrate terms, $\mathcal{U} \approx 1$ across the system's qubit-spanning rules.

**Unitary operation** is evolution in the thin-participation regime — substrate dynamics where commitment has not yet occurred and the participation geometry can be reconfigured reversibly. Unitarity is the regime-property of substrate dynamics in the unresolved sector, not a postulate. The same Stone-theorem machinery that produces unitarity in standard quantum mechanics applies here, because the substrate's evolution operators commute with the participation measure's normalization in the unresolved regime.

**Readout** is, in the framework's reading, an ED-injection event that forces individuation: environmental ED-flow proliferates gradients into the system, the system's participation rule must individuate to one of its compatible endpoints, and the result is committed irreversibly. The result is not "extracted from a superposition"; rather, the superposition's substrate structure is forced by ED-injection to commit to one of its compatible outcomes.

A quantum computer, in this reading, is a deliberately engineered region of substrate where a participation rule is held in the unresolved low-multiplicity regime long enough for its geometry to be manipulated, before being committed via ED-injection at readout. The challenge of building one is the challenge of holding $\mathcal{U} \approx 1$ over a multi-endpoint participation rule for a sufficient duration, against the substrate's natural tendency to drive $\mathcal{U}$ toward 0 through environmental ED-injection.

This is structurally the same kind of object as a Josephson junction (engineered substrate gradient bottleneck), a bulk superconductor (lattice symmetry holding a low-multiplicity regime), and the inside of a saturated participation zone (black-hole interior). Each is a region of low-multiplicity ED-flow held against the substrate's natural tendency to proliferate gradients and force individuation. The differences are only in *what holds the low-multiplicity regime in place* and *what is being done with it while it persists*.

A bulk superconductor uses lattice symmetry to hold the regime and transports charge through it. A Josephson junction adds an engineered sparsity-bottleneck to enforce non-individuation across a barrier. A quantum computer uses the regime as an operating substrate on which to execute manipulations of the unresolved participation geometry. The structural classification of quantum-computing platforms is the classification of mechanisms for holding $\mathcal{U} \approx 1$ against the substrate's individuation pressure.

---

## 4. The Three Substrate Conditions for Coherent Computation

The unresolved-regime characterization theorem (UR-1) states the necessary and sufficient substrate conditions for $\mathcal{U}(\mathcal{S}, t) \approx 1$ to be sustainable.

> **UR-1 (Unresolved-Regime Characterization Theorem).** A substrate region $\mathcal{S}$ admits $\mathcal{U}(\mathcal{S}, t) \approx 1$ for some specified set of participation-rule endpoints if and only if:
>
> **(i) Multiplicity is bounded.** $\mathcal{M}(\mathcal{S}) \leq \mathcal{M}_\mathrm{crit}$ for some substrate-determined threshold $\mathcal{M}_\mathrm{crit}$.
>
> **(ii) Cross-endpoint cross-bandwidth is sustained.** $\Gamma_\mathrm{cross}(\mathbf{x}) \geq \Gamma_\mathrm{\min}$ for all $\mathbf{x}$ on the engineered participation pathways between designated endpoints.
>
> **(iii) Commitment-injection is below the individuation rate.** The rate of ED-injection from environment plus accumulated P11 commitments inside $\mathcal{S}$ is below the substrate-determined individuation threshold.
>
> Failure of any of (i)–(iii) drives $\mathcal{U} \to 0$ at a rate determined by which condition fails and by how much.

Each condition is a substrate-level statement about a different aspect of the unresolved regime.

### 4.1 Why multiplicity must be bounded

If $\mathcal{M}(\mathcal{S}) \gg \mathcal{M}_\mathrm{crit}$, the system has too many viable participation pathways. The substrate's natural tendency to populate available pathways drives the system into a high-multiplicity regime where coherent superposition cannot be sustained. The substrate analog: a system with too many internal degrees of freedom cannot maintain a single coherent participation rule because the rule is split across too many endpoints, and partial individuations along any subset of those endpoints break the coherent superposition.

The threshold $\mathcal{M}_\mathrm{crit}$ is INHERITED from V1-kernel parameters and substrate-channel statistics. The framework establishes that a threshold exists; the specific numerical value depends on the substrate's microscopic details. For the matter-wave Q-C boundary at 140-250 kDa, the empirical value of $\mathcal{M}_\mathrm{crit}$ is fixed by the molecular-mass range at which interference patterns persist.

### 4.2 Why cross-bandwidth must be sustained

The participation rule that defines the coherent superposition spans multiple substrate endpoints. The rule is *one rule expressed at multiple locations* (in the language of the entanglement walkthrough). Sustaining the rule requires sustained substrate cross-chain coupling between those locations.

The DCGT-derived form $\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2) \sim \exp[-\alpha \int_\mathrm{path} \sigma\, d\ell]$ tells us that cross-bandwidth depends exponentially on integrated gradient sparsity along the path between endpoints. When $\sigma$ is uniformly low along the rule-spanning pathway, $\Gamma_\mathrm{cross}$ is order one and the rule is sustainable. When $\sigma$ rises along the pathway — through environmental coupling, thermal fluctuation, decoherence-inducing physical processes — $\Gamma_\mathrm{cross}$ falls exponentially and the rule fragments.

The threshold $\Gamma_\mathrm{\min}$ is the substrate-determined minimum below which the rule no longer holds together as a coherent participation structure. It is INHERITED from the V1-kernel + DCGT closed-form details that the framework's structural-foundations program has not yet derived to closed numerical values.

### 4.3 Why commitment-injection must be bounded

The substrate's V1 vacuum kernel, even in perfect environmental isolation, supplies an irreducible commitment-injection rate $\Lambda_\mathrm{V1}$. Every participation rule, no matter how well-isolated, is subject to this baseline injection rate. P11 commitment-irreversibility means that when the cumulative injection exceeds the individuation threshold, the rule individuates and cannot be restored.

For a coherent computation to complete before forced individuation, the integrated commitment-injection over the computation's duration must be below the threshold:

$$
\int_0^{\tau_{\mathrm{compute}}} \Lambda_{\mathrm{total}}(t)\, dt < \Lambda_{\mathrm{individuation}}
$$

where $\Lambda_\mathrm{total} = \Lambda_\mathrm{V1} + \Lambda_\mathrm{environment} + \Lambda_\mathrm{accumulated\,P11}$ is the sum of vacuum contribution, environmental coupling, and accumulated commitment events from prior gates in the circuit.

The substrate ceiling on $\Lambda_\mathrm{V1}$ is what makes Class A's perfect-isolation limit a structural ceiling rather than an engineering target: even with perfect environmental isolation, the V1 vacuum's irreducible injection rate sets a floor on $\Lambda_\mathrm{total}$.

### 4.4 The QC timescale

The maximum quantum-computation timescale before forced individuation is the minimum of the three condition-failure timescales:

$$
\tau_QC = \min(\tau_(i), \tau_(ii), \tau_(iii))
$$

where $\tau_{(i)}$ is the timescale for multiplicity to grow past $\mathcal{M}_\mathrm{crit}$, $\tau_{(ii)}$ is the timescale for $\Gamma_\mathrm{cross}$ to fall below $\Gamma_\mathrm{\min}$ along some rule-spanning pathway, and $\tau_{(iii)}$ is the timescale for accumulated commitment-injection to exceed the individuation threshold.

Different physical platforms have different bottlenecks. Superconducting transmons are typically limited by $\tau_{(iii)}$ — accumulated commitment from microwave-photon coupling at non-zero effective temperature. Topological qubits would be limited by $\tau_{(i)}$ if the topological gap is large compared to thermal energy, or by $\tau_{(ii)}$ if the rule-spanning pathway crosses regions of high $\sigma$. Trapped ions with high gate fidelities approach the $\tau_{(iii)}$ bottleneck after sufficient circuit depth. The class to which a given platform belongs is determined by which condition is the limiting one, and by what mechanism is being used to prevent that condition from failing.

---

## 5. The Three Failure Modes

UR-1's three conditions can fail through three substrate-level mechanisms. Each is a separate dynamical pathway driving $\mathcal{U} \to 0$.

### 5.1 F1: Premature individuation from environmental ED-injection

Condition (iii) fails when environmental coupling injects ED into the system at a rate exceeding the individuation threshold. Standard physics calls this *decoherence from environmental coupling*.

The substrate mechanism: environmental ED-flow proliferates gradients into the system, the gradients populate previously-empty substrate channels, and the cumulative gradient population eventually exceeds the threshold at which individuation is forced. The rate of injection depends on the strength of environmental coupling, which depends on the system's spatial extent (more area for environmental contact), its temperature (more energy in environmental modes), and its specific coupling channels (susceptibility to thermal photons, lattice phonons, magnetic-field fluctuations).

Class A architectures (engineered-low-multiplicity) work primarily by minimizing F1. Cryogenic operating temperatures, electromagnetic shielding, vacuum-chamber pumping, vibration isolation — all are F1-mitigation techniques. The fundamental ceiling on F1 mitigation is the V1 vacuum's irreducible injection rate $\Lambda_\mathrm{V1}$: no isolation can drive the injection rate below this baseline.

### 5.2 F2: Cross-endpoint decoupling from $\Gamma_\mathrm{cross}$ collapse

Condition (ii) fails when $\Gamma_\mathrm{cross}$ along the rule-spanning pathway falls below $\Gamma_\mathrm{\min}$ at some point. The DCGT-derived exponential structure means that even small increases in path-integrated $\sigma$ produce large decreases in $\Gamma_\mathrm{cross}$.

The substrate mechanism: a transient gradient anomaly along the rule-spanning pathway — a phonon, a stray field, a thermal fluctuation — locally raises $\sigma$ along part of the path. The integrated $\sigma$ along the pathway increases. $\Gamma_\mathrm{cross}$ along the pathway falls exponentially. When it falls below $\Gamma_\mathrm{\min}$, the rule fragments at that location.

F2 is the dominant failure mode in spatially-extended quantum-computing architectures (large-scale ion-trap arrays, distributed superconducting registers connected via microwave waveguides, photonic networks). The longer the rule-spanning pathway, the higher the integrated $\sigma$, and the greater the F2 risk.

### 5.3 F3: Commitment-pressure cascade

Condition (iii) can also fail from accumulated P11 commitments inside the system, even without significant external coupling. Each commitment event contributes irreversibly to the substrate's individuation pressure.

The substrate mechanism: every gate operation in a quantum circuit involves substrate-level participation rule reconfiguration. Even when the gate is unitary at the continuum level, the underlying substrate processes involve discrete commitment events. As circuit depth grows, the cumulative commitment count grows, and eventually the system's substrate-level commitment pressure exceeds the individuation threshold.

F3 is the substrate-level reason quantum circuits have a maximum useful depth even at perfect gate fidelity. Even if every gate operation were perfectly unitary, the substrate's commitment-injection from gate operations would eventually drive the computation past the individuation threshold. F3-mitigation through error-correction protocols can reset the commitment-pressure budget at the logical-qubit level by detecting and erasing excess commitments, but the physical-qubit-level commitments accumulate regardless.

---

## 6. The Three Architectural Classes

The substrate-level mechanisms for holding $\mathcal{U} \approx 1$ against the failure modes are exhaustive at three classes. Any quantum-computing platform is, structurally, an instance of one of these three classes, or a composition of techniques over multiple classes.

### 6.1 Class A: Engineered-low-multiplicity

Class A architectures hold condition (i) by engineering the system to have intrinsically low multiplicity. The participation rule lives on a small number of designed substrate channels — for example, two energy levels of an atomic system, two flux states of a superconducting circuit, two polarization states of a photon. The system's multiplicity is bounded by design.

**Examples.** Superconducting transmons (two energy levels of a Josephson-junction circuit). Trapped ions in optical-lattice clocks (two hyperfine levels of an ion). Photonic qubits (two polarization states). Quantum dots (two charge states). NV centers in diamond (two spin states).

**Substrate mechanism.** $\mathcal{M}(\mathcal{S})$ is small by construction. The system's substrate participation is restricted to a small set of designed channels.

**Failure mode emphasis.** Class A architectures excel at condition (i) but are vulnerable to F1 (environmental ED-injection breaking condition (iii)). Most engineering effort in Class A platforms is directed at minimizing F1: cryogenic temperatures, electromagnetic shielding, vibration isolation.

**Substrate ceiling.** The Class A ceiling is the substrate-multiplicity threshold $\mathcal{M}_\mathrm{crit}$. As system size grows — adding more qubits, increasing molecular complexity, increasing spatial extent — the system's intrinsic multiplicity grows. At some scale, intrinsic multiplicity exceeds $\mathcal{M}_\mathrm{crit}$ and condition (i) fails regardless of engineering effort.

### 6.2 Class B: Global-geometric-rigidity (topological protection)

Class B architectures hold condition (i) by encoding the participation rule in a global geometric property of the substrate that is robust to local perturbations. Local environmental coupling cannot easily change a global topological invariant; the rule is protected by the rigidity of the substrate's geometric structure.

**Examples.** Majorana fermions in topological superconductors. Fibonacci anyons in quantum-Hall systems. Surface-code logical qubits at the topological-protection level (where the logical encoding is geometric rather than physical). Flux qubits at sufficiently large scale to be in the topologically-protected limit.

**Substrate mechanism.** The participation rule is encoded in global topological data — winding numbers, Chern integers, anyonic exchange phases — that are stable against local fluctuations of $\sigma$. Local F1 events do not change the global topology; only sufficiently large fluctuations that span the topological gap can disrupt the rule.

**Failure mode emphasis.** Class B excels against F1 in the topological-protection regime where temperature is low compared to the topological gap. Class B is vulnerable to F2 if rule-spanning pathways are forced through high-$\sigma$ regions.

**Substrate prediction.** Class B's coherence advantage over Class A is exponential in the topological-gap to thermal-energy ratio: $\tau_\mathrm{B}/\tau_\mathrm{A} \sim \exp(\Delta_\mathrm{top}/T_\mathrm{eff})$. At $\Delta_\mathrm{top}/T_\mathrm{eff} \gtrsim 10$–20, Class B overtakes Class A in coherence-time performance. This prediction is the substrate-level reason the topological-qubit research program is structurally compelling: the coherence advantage is not modest but exponential in the protection ratio.

### 6.3 Class C: High-multiplicity-redundancy

Class C architectures abandon the strategy of keeping individual-qubit multiplicity low, and instead encode the logical computation in highly-redundant correlations across many physical qubits. Errors at the physical-qubit level are corrected by the redundancy structure before they propagate to the logical-qubit level.

**Examples.** Surface-code error-corrected logical qubits at the quantum-error-correction protocol level. Stabilizer codes implemented via thousands of physical qubits per logical qubit. Neutral-atom array architectures with large physical-qubit counts. Dynamical-decoupling protocols at large redundancy factor.

**Substrate mechanism.** The logical-qubit participation rule is supported by a highly-redundant set of physical-qubit channels. Local F1 events corrupt individual physical qubits but cannot corrupt the global redundancy structure as long as the corruption rate is below the code's error-correction threshold. The logical rule survives even when many physical channels fail.

**Failure mode emphasis.** Class C tolerates F1 at the physical-qubit level by design. Class C is fundamentally limited by condition (ii): the cross-chain bandwidth budget across the redundancy-supporting substrate is finite. As $N_\mathrm{phys}$ grows, the per-channel cross-bandwidth share decreases, and at some $N_\mathrm{corr}$ the budget saturates.

**Substrate prediction.** Class C's logical-qubit performance saturates at a correlation-budget plateau. Adding more physical qubits beyond $N_\mathrm{corr}$ does not improve logical-qubit coherence because the per-channel cross-bandwidth share has fallen below $\Gamma_\mathrm{\min}$. This is the substrate-level constraint on how far redundancy-based architectures can push.

### 6.4 Why three classes are exhaustive

The three classes are exhaustive because UR-1 has three conditions. Each class corresponds to a different strategy for which condition is the primary substrate-level lock against failure.

Class A locks condition (i) by design — multiplicity is intrinsically bounded.
Class B locks condition (i) by global geometry — multiplicity is bounded by topological rigidity.
Class C does not lock condition (i) at the physical level but locks the system's *effective* logical-qubit condition (i) through redundancy.

Any architectural strategy that does not lock condition (i) at the physical, geometric, or redundancy level fails to hold $\mathcal{U} \approx 1$ at the logical-qubit level for any sustained computation. There is no fourth substrate-level strategy because there are no other ways to bound multiplicity at the substrate level.

### 6.5 Meta-architectures are compositions

Meta-architectures — quantum error correction at the protocol level, dynamical decoupling, reservoir engineering, hybrid platforms — are compositions of the three classes, not separate classes. Quantum error correction is Class A physical qubits + Class C logical-redundancy structure. Dynamical decoupling is Class A + a time-domain technique that resets condition (iii) periodically. Reservoir engineering is Class A + an environmentally-coupled state-stabilization technique. Hybrid platforms (e.g., topological + transmon) are Class B + Class A composed at different layers.

The decisive falsifier for the three-class classification: a platform that has no class assignment, is irreducible to meta-composition over A/B/C, and matches the multiplicity-cap function $M$ in a way no class projection of $M$ predicts. Such a platform would refute the three-class exhaustiveness. None has been identified to date.

---

## 7. The Multiplicity-Cap Function and Cross-Class Transitions

The multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ relates the system's substrate state, architectural class, environmental coupling, and operational structure to the maximum coherent-computation timescale. It has three projections, one per class, with cross-class transition behavior at specific substrate thresholds.

### 7.1 The function's structure

$$
M(S, K, E, O) = \min(M_A(S, E), M_B(S, K, E), M_C(S, K, E, O))
$$

where each projection captures the limiting behavior in its corresponding class. $M_A$ depends primarily on the system's intrinsic multiplicity and environmental coupling. $M_B$ depends additionally on the topological-gap to thermal-energy ratio. $M_C$ depends additionally on the redundancy structure and operational complexity.

The minimum-over-classes structure means that any specific platform's actual $M$ value is governed by its dominant architectural class — usually Class A for current devices, with Class B and Class C contributing supplementary protection at specific operational regimes.

### 7.2 Cross-class transitions

**A → C is mandatory at the wall.** As system size grows toward $\mathcal{M}_\mathrm{crit}$, Class A's multiplicity becomes inadequate. The only substrate-permitted strategy at that point is to introduce redundancy — to switch to Class C operation. This is why fault-tolerant quantum computation at large scale requires error correction: it is the substrate-level necessity of crossing from Class A to Class C as the system's physical-qubit count approaches the substrate-multiplicity threshold.

**B overtakes A at $\Delta_\mathrm{top}/T_\mathrm{eff} \gtrsim 10$–20.** When the topological gap is sufficiently large compared to thermal energy, Class B's exponential coherence advantage produces $\tau_B \gg \tau_A$. Below this threshold, Class B's geometric protection does not offer a meaningful advantage over Class A's engineered low multiplicity. Above it, Class B is structurally superior.

**C saturates at $N_\mathrm{corr}$.** Class C's redundancy advantage grows with physical-qubit count $N_\mathrm{phys}$ until cross-bandwidth budget saturates at $N_\mathrm{corr}$. Beyond $N_\mathrm{corr}$, additional physical qubits do not improve logical-qubit performance.

These transitions are the substrate-level structural map of the quantum-computing architectural landscape. The transitions are forced by UR-1's substrate conditions and by the three-class exhaustiveness.

---

## 8. Predictions and Cross-Platform Unification

UR-1 plus the three-class classification produces three sharp predictions plus a cross-platform unification.

### 8.1 Class A wall at the substrate-multiplicity threshold

Class A architectures cannot maintain coherent superposition above $\mathcal{M}_\mathrm{crit}$. As system mass and complexity grow toward $\mathcal{M}_\mathrm{crit}$, coherence times fall sharply. The empirical anchor for $\mathcal{M}_\mathrm{crit}$ is the matter-wave quantum-classical boundary at 140-250 kDa molecular mass — the regime where coherent matter-wave interference patterns become impossible to sustain regardless of experimental effort.

This prediction aligns with the existing experimental program targeting matter-wave interference at 140-250 kDa, currently a factor of 5-10 beyond the largest demonstrated coherent superposition. If experiments in this range fail to produce interference patterns, Class A's substrate ceiling is empirically confirmed. If they succeed, the value of $\mathcal{M}_\mathrm{crit}$ is pushed higher and the framework's structural prediction is sharpened.

### 8.2 Class B exponential gap-suppression advantage

Class B architectures' coherence-time advantage over Class A grows as $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$. At $\Delta_\mathrm{top}/T_\mathrm{eff} \gtrsim 10$, Class B should outperform Class A by approximately four orders of magnitude in coherence time. At $\Delta_\mathrm{top}/T_\mathrm{eff} \gtrsim 20$, the advantage grows to nine orders of magnitude.

Current topological-qubit research operates at substantially smaller $\Delta_\mathrm{top}/T_\mathrm{eff}$ ratios. If the research program reaches the high-ratio regime, the framework predicts a structural transition at which Class B's coherence-time advantage becomes overwhelming. If Class B remains comparable to Class A even at high ratios, the framework's prediction is refuted.

### 8.3 Class C correlation-budget plateau at $N_\mathrm{corr}$

Class C architectures' logical-qubit coherence saturates at a correlation-budget plateau as physical-qubit count grows. Beyond $N_\mathrm{corr}$, additional physical qubits do not improve logical-qubit performance. The specific value of $N_\mathrm{corr}$ depends on the substrate-coupling pattern — on $\Gamma_\mathrm{\min}$ and the architectural details — but the existence of a plateau is structurally forced.

Current large-scale architectures (e.g., surface-code-protected logical qubits with $\sim 10^3$–$10^4$ physical qubits per logical qubit) are still in the pre-plateau regime where adding physical qubits improves logical-qubit performance. The framework predicts that this scaling does not extend indefinitely. At sufficient physical-qubit count, the cross-bandwidth budget saturates and further physical-qubit addition produces no improvement.

### 8.4 Cross-platform unification: matter-wave Q-C boundary and qubit-system multiplicity walls

The framework's strongest prediction is structural rather than numerical: the matter-wave quantum-classical boundary (a regime far from quantum-computing applications) and the qubit-system multiplicity wall (the boundary of Class A's applicability in quantum computation) are the *same* substrate phenomenon, governed by the same $\mathcal{M}_\mathrm{crit}$ via the same UR-1 condition (i).

Standard physics treats these as unrelated phenomena. Matter-wave interference is a fundamental-physics question about quantum coherence at molecular scales. Qubit decoherence is an applied-physics question about engineering performance. The framework identifies them as substrate-level instances of the same multiplicity-bound mechanism. Empirically: if matter-wave interference at 140-250 kDa is achieved, the framework predicts a corresponding extension of Class A qubit performance toward larger system sizes. If matter-wave interference fails at 140-250 kDa, the framework predicts that Class A's wall is at a corresponding system size in qubit architectures.

The cross-platform identity is the substrate-level reason these two empirical programs should be informative about each other. The framework's prediction is that they are not separate phenomena.

### 8.5 Cross-domain echo with black-hole physics

The cross-bandwidth structure $\Gamma_\mathrm{cross}$ that drives UR-1 condition (ii) is the same $\Gamma_\mathrm{cross}$ that governs black-hole horizon formation. A black-hole horizon is the substrate surface where $\Gamma_\mathrm{cross}$ across it falls below the hydrodynamic-window resolution. Quantum-computing condition (ii) failure is the substrate condition where $\Gamma_\mathrm{cross}$ across a rule-spanning pathway falls below $\Gamma_\mathrm{\min}$.

Same substrate mechanism. Different platforms. Different scales. Same DCGT-derived exponential-in-integrated-sparsity structure. The framework's cross-domain unification — quantum-computing decoherence and black-hole horizon physics governed by the same substrate machinery at scales separated by fifty orders of magnitude — is the strongest piece of cross-platform mechanism identity in the framework's closed-arc inventory.

---

## 9. What's Forced, What's Inherited, What's Open

It is worth being precise about what changes when the UR-1 framework is in place versus when it isn't.

### 9.1 What's forced

UR-1 itself is forced. The three substrate conditions (bounded multiplicity, sustained cross-bandwidth, bounded commitment-injection) are necessary and sufficient for $\mathcal{U} \approx 1$ at the substrate level. Any system that satisfies all three holds the unresolved regime; any system that fails any one of them does not.

The three failure modes (F1, F2, F3) are exhaustive. Any substrate-level mechanism that drives $\mathcal{U} \to 0$ acts through one of them.

The three architectural classes (A, B, C) are exhaustive. Any platform that holds $\mathcal{U} \approx 1$ does so through engineered-low-multiplicity, global-geometric-rigidity, or high-multiplicity-redundancy. Meta-architectures are compositions over the three classes, not separate strategies.

The minimum-over-classes structure of the multiplicity-cap function $M$ is forced by the three-class exhaustiveness.

The cross-class transitions (A → C mandatory at the wall, B overtakes A at high $\Delta/T$, C saturates at $N_\mathrm{corr}$) are forced by UR-1's substrate conditions.

The form of the three predictions — Class A wall at multiplicity threshold, Class B exponential advantage, Class C plateau at correlation-budget saturation — is forced.

### 9.2 What's inherited

The numerical value of $\mathcal{M}_\mathrm{crit}$ is INHERITED from V1-kernel parameters and substrate-channel statistics. The framework establishes that a threshold exists; the specific value is set by substrate microscopic details.

The numerical value of $\Gamma_\mathrm{\min}$ is INHERITED from V1-kernel + DCGT closed-form details that have not been derived to closed numerical values.

The individuation-rate threshold (condition iii) is INHERITED from V1-kernel parameters.

The correlation-budget saturation count $N_\mathrm{corr}$ for Class C platforms is INHERITED from the substrate-coupling pattern at the architectural level.

The class assignment for any specific platform is INHERITED from the platform's engineering details. Whether transmon qubits are Class A or have Class B/C admixture is determined by the platform's physical structure, not by the framework alone.

The matter-wave Q-C boundary at 140-250 kDa, used as the empirical anchor for $\mathcal{M}_\mathrm{crit}$, is INHERITED from molecular-physics experimental data.

The exponent in the Class B exponential advantage is INHERITED from the topological-gap structure of the specific platform.

### 9.3 What's open

The closed-form derivation of $\mathcal{M}_\mathrm{crit}$ from V1-kernel + ED-I substrate constants is open. The framework has the matter-wave Q-C boundary at 140-250 kDa as an empirical anchor that calibrates $\mathcal{M}_\mathrm{crit}$, but a substrate-derived numerical value would make the boundary a substrate-derived rather than empirically anchored quantity.

The architecture-to-platform calibration program — predicting $N_\star$ values for canonical qubit platforms from the substrate-level $\mathcal{M}_\mathrm{floor}$ — is open. The framework predicts specific platform performance differences based on class assignment, but mapping the substrate-level theory to specific platform predictions requires additional bridge work.

The closed-form $g(N), h(N), c(N)$ functions for Class C platforms (the redundancy modifier functions) are INHERITED from substrate-coupling pattern; closed-form derivation requires extending DCGT to multi-axis redundancy structure.

A topology-stability theorem for Class B (the substrate-level account of $\tau_\mathrm{gap-stab}(\mathcal{T})$ for canonical topological structures like Majorana, Fibonacci anyons, Chern bands) is open.

The surface-code logical-qubit recursive-overlay derivation — the specific scaling of $\tau_\mathrm{QC}^\mathrm{logical}$ with code distance plus threshold from the substrate-level error-correction-as-meta-architecture analysis — is currently schematic rather than fully derived.

Hybrid-architecture handoff dynamics (SC-photonic interconnects, topological-SC platforms, and other hybrid architectures' handoff boundaries as substrate-geometric transitions) are partially understood; specific handoff-loss accounting is open.

---

## 10. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, chains, bandwidth, polarity, ED gradient, commitment irreversibility, continuous time, locality, rule-type) → forced theorems (T18 forward-cone V1 kernel, T17 gauge-field-as-rule-type, T19 Newton-recovery $\ell_P$) → DCGT (substrate-to-continuum bridge supplying $\Gamma_\mathrm{cross}$) → substrate-level invariants ($\mathcal{M}, \mathcal{U}, \sigma, \Gamma_\mathrm{cross}$) → substrate reading of quantum computation as deliberate occupation of the unresolved low-multiplicity regime → UR-1 three-condition gate (multiplicity bounded, cross-bandwidth sustained, commitment-injection below individuation rate) → three failure modes (F1, F2, F3) → three architectural classes (A, B, C) as exhaustive substrate-permitted mechanisms for holding the conditions → multiplicity-cap function $M$ with three class-projections → three sharp predictions (Class A wall, Class B exponential advantage, Class C plateau) plus cross-platform unification.

Quantum computation now has a substrate-level architectural classification with falsifiable predictions. The mathematical content of the standard QM machinery — unitarity, Hilbert space, Born rule, decoherence — is unchanged. What changes is the foundational status: decoherence is not merely environmental coupling but the substrate-level mechanism by which UR-1 conditions fail. Architectural design choices are not arbitrary engineering but substrate-level strategies for which condition to lock against which failure mode.

The framework reproduces standard quantum-computing physics where it has been tested. Transmon qubits decohere at the rates measured. Trapped ions perform gates at the fidelities reported. Surface codes correct errors at the protocol-level rates derived from threshold theorems. UR-1 does not modify these results; it provides the substrate-level account that explains why they take the forms they do.

What's new is the architectural classification with its predictive content. Class A's substrate wall at $\mathcal{M}_\mathrm{crit}$ — empirically anchored at the 140-250 kDa matter-wave Q-C boundary — is a structural ceiling that engineering cannot work around. Class B's exponential coherence advantage at high $\Delta_\mathrm{top}/T_\mathrm{eff}$ is a structural prediction that aligns with the topological-qubit research program's structural rationale. Class C's correlation-budget plateau at $N_\mathrm{corr}$ is a structural constraint on how far redundancy-based architectures can scale.

The cross-domain unifications are the substantively new content. The same $\mathcal{M}_\mathrm{crit}$ governs both the matter-wave quantum-classical boundary and the qubit-system multiplicity wall. The same $\Gamma_\mathrm{cross}$ structure governs both quantum-computing decoherence and black-hole horizon formation. Standard physics treats these as unrelated. The framework identifies them as the same substrate mechanism applied at vastly different scales.

The conceptual shift the framework delivers is from a *decoherence-centric* account (focused on environmental coupling and how to minimize it) to a *multiplicity-centric* account (focused on the substrate's multiplicity structure and the architectural strategies for keeping it low against substrate-level failure modes). Decoherence remains real; it is now a specific substrate failure mode (F1) rather than the master concept of the field.

The factor that's worth emphasizing: UR-1 introduces no new substrate primitive. The micro-events, chains, bandwidth, polarity, kernels, commitment irreversibility, locality, and rule-type primitives were already in the framework's inventory, doing work in the QM emergence program, the gauge-fields arc, and the substrate-gravity arc. UR-1 reads the architectural classification of quantum-computing platforms off the same primitives that produce the QM postulates and Newton's law of gravitation. The substrate inventory is unchanged; the structural-foundations theorem inventory grows by one — and that one supplies a falsifiable architectural classification of an industry-relevant technology with structural predictions at the empirical frontier.

Whether the substrate primitives themselves are right is the load-bearing empirical question, as in every walkthrough. The framework stands or falls on whether participation, bandwidth, channels, polarity, locality, rule-type, V1 and V5 kernels, and commitment irreversibility are the correct foundational concepts. The empirical exposure of the framework lives across multiple sectors — soft-matter mobility predictions, substrate-derived gravity transitions, the three quantum-computing class predictions, Clay-relevance results in NS and Yang-Mills — not in any one of them.

For quantum-computing architecture specifically, the structural case is closed at the substrate level. UR-1 supplies the gate condition. The three classes are exhaustive. The three predictions are falsifiable. The cross-platform unifications align two empirical programs (matter-wave coherence and qubit-system performance) that standard physics treats as separate. The architectural classification is a substrate-level theorem, not a phenomenological framework for organizing engineering effort. Engineering effort is now framed by which substrate condition to lock against which failure mode through which class-permitted strategy. The empirical question is which platforms reach which class's structural ceiling first.

---

## 11. References

- Feynman, R. P. "Simulating Physics with Computers." *International Journal of Theoretical Physics* 21, 467–488 (1982).
- Shor, P. W. "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *Proceedings 35th Annual Symposium on Foundations of Computer Science*, 124–134 (1994).
- Aharonov, D., Ben-Or, M. "Fault-Tolerant Quantum Computation with Constant Error." *Proceedings of the 29th Annual ACM Symposium on Theory of Computing*, 176–188 (1997).
- Kitaev, A. Y. "Fault-Tolerant Quantum Computation by Anyons." *Annals of Physics* 303, 2–30 (2003).
- Nielsen, M. A., Chuang, I. L. *Quantum Computation and Quantum Information.* Cambridge University Press, 2000.
- Arndt, M., Hornberger, K. "Testing the Limits of Quantum Mechanical Superpositions." *Nature Physics* 10, 271–277 (2014).
- Fein, Y. Y., Geyer, P., Zwick, P., et al. "Quantum Superposition of Molecules Beyond 25 kDa." *Nature Physics* 15, 1242–1245 (2019).
- Eibenberger, S., Gerlich, S., Arndt, M., et al. "Matter-Wave Interference of Particles Selected from a Molecular Library with Masses Exceeding 10 000 amu." *Physical Chemistry Chemical Physics* 15, 14696–14700 (2013).
- Zurek, W. H. "Decoherence, Einselection, and the Quantum Origins of the Classical." *Reviews of Modern Physics* 75, 715–775 (2003).
- Proxmire, A. *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* April 2026.
- Proxmire, A. *Theorem 17: Gauge-Field-as-Rule-Type — The Substrate Origin of Gauge Fields and Minimal Coupling.* April 2026.
- Proxmire, A. *Theorem 18: V1 Kernel Retardation and the Kernel-Level Arrow of Time.* April 2026.
- Proxmire, A. *Theorem 19: Newton's Law from Substrate Holographic Counting and the Identification of $\ell_P$.* April 2026.
- Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.
- Proxmire, A. *Quantum Computing Foundations Paper, with the UR-1 Theorem and the Multiplicity-Cap Function.* May 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
