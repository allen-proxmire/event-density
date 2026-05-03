# Chapter 5 — Phase-1 Closure of Quantum Mechanics: T1–T16

## 5.1 Chapter Overview

Phase-1 of the Event Density program closes the four postulates of quantum mechanics as *derived theorems* rather than as independent axioms. Sixteen forced theorems (T1–T16) collectively establish that the **Born rule**, the **Schrödinger equation**, the **Heisenberg uncertainty principle**, and the **no-collapse measurement rule** all emerge from substrate primitives plus standard mathematical structure. The substrate primitives consumed are those of Chapter 1 (especially P04 bandwidth update, P11 commitment-irreversibility, P01 event discreteness); the mathematical bridges are Gleason's 1957 theorem on quantum measures and Stone's 1932 theorem on one-parameter unitary groups. The Born rule's squared form, the Schrödinger equation's specific functional form (linearity, first-order-in-time character, Hamiltonian content), the Heisenberg lower bound's $\hbar/2$ factor, and the irreversibility of measurement all become structural consequences rather than postulates. There is no separate collapse postulate in the Phase-1 framework — measurement is identified as the coarse-grained signature of substrate-level commitment events through P11.

The chapter integrates the Phase-1 closure work and identifies its position in the broader Event Density program. It does not reproduce the formal proofs (those live in `papers/Phase_1/` and the U1–U5 paper chain). It exposes the structural arguments behind each of the four QM-postulate derivations, identifies the substrate primitives consumed, locates the mathematical bridges, and clarifies the Phase-1 inventory of sixteen forced theorems plus extensions covering spin-statistics, the Dirac equation, the $g=2$ electron magnetic moment, and the canonical commutation relations. After this chapter, every subsequent chapter can refer to Phase-1 as the foundational closure of the quantum-mechanical sector — and Chapters 6 (form-level QFT) and 7 (quantum computation) build directly on its content.

## 5.2 Why Phase-1 Closure Matters Structurally

### 5.2.1 The QM-postulate problem

Standard quantum mechanics rests on four postulates that have been in textbooks since the 1920s. Each is presented as an axiom:

- **The Born rule.** Probability of an outcome equals the squared amplitude. Why squared? The textbooks do not say.
- **The Schrödinger equation.** Wavefunctions evolve in time according to $i\hbar\partial_t |\psi\rangle = \hat H |\psi\rangle$. Why this specific functional form — linearity, first-order in time, Hamiltonian content? The textbooks do not say.
- **The Heisenberg uncertainty principle.** $\Delta x \cdot \Delta p \geq \hbar/2$. Why $\hbar/2$? Why this specific lower bound? The textbooks do not say.
- **The measurement rule.** When a quantum system is measured, the wavefunction "collapses" into a single outcome, and the collapse is irreversible. Why is collapse irreversible? Why is it a separate postulate from unitary evolution? The textbooks do not say.

Each postulate is correct as far as it goes; the empirical content of quantum mechanics is exquisitely well-confirmed. But the postulates are not derived from anything; they are taken as axioms, and the structural origin of their specific forms is treated as outside the theory's scope. Decades of work on the foundations of quantum mechanics — interpretations, hidden variables, decoherence programs — have not produced a consensus structural account.

### 5.2.2 ED's structural position

The Event Density program treats the four QM postulates as *consequences* of a deeper substrate ontology. The postulates are not axioms; they are derived theorems. The framework's structural commitment: each postulate's specific form is form-FORCED by substrate primitives plus standard mathematical theorems, and the specific numerical content of each (the squared form, the linearity, the $\hbar/2$ factor, the irreversibility) is a substrate-level structural consequence rather than an unmotivated axiom.

The structural payoff is significant. Phase-1 closure means quantum mechanics is not a self-contained framework with four postulates floating above an unspecified substrate; it is the coarse-grained reading of substrate dynamics in the *thin-participation regime* — the regime where participation is uncommitted and substrate dynamics admit unitary, reversible evolution. The transition from substrate to standard QM is auditable through the U1–U5 paper chain, and the substrate-level analogues of every QM postulate are explicit.

### 5.2.3 The sixteen-theorem closure

Phase-1's deliverable is sixteen forced theorems labeled T1 through T16. Forced means: the conclusion of each theorem is uniquely produced by the substrate inputs combined with standard mathematical structure. The theorems are not chosen; they are constructed. Symmetric, advanced, or modified versions of QM that contradict any of T1–T16 are not merely refuted — they are *non-constructible* from the substrate primitives.

The four-postulate closure groups within T1–T16 are:

- **T-Born group.** The substrate-level theorems leading to the Born rule's squared form. Mathematical bridge: Gleason's theorem (1957).
- **T-Schrödinger group.** The substrate-level theorems leading to the Schrödinger equation's specific form. Mathematical bridge: Stone's theorem (1932).
- **T-Uncertainty group.** The substrate-level theorems leading to the Heisenberg lower bound with the $\hbar/2$ coefficient.
- **T-Measurement group.** The substrate-level theorems leading to the no-collapse measurement rule via P11 commitment-irreversibility.

Chapter 5 takes each group in turn, identifies the substrate primitives consumed, exposes the structural argument, and clarifies what is form-FORCED and what is value-INHERITED.

## 5.3 The Born Rule: Substrate Non-Contextuality + Gleason 1957

### 5.3.1 The structural question

Why is probability the *squared* amplitude rather than the linear amplitude, the fourth power, or the absolute value? Standard QM treats this as a postulate; the squared form is an empirical fact that is built into the theory's axioms.

ED reframes the question. The "amplitude" in standard QM is the participation-bandwidth content of a substrate region distributed across the orthogonal decomposition associated with a measurement basis. The probability of an outcome is the bandwidth that *commits* to that outcome under P11. The structural question becomes: how is bandwidth distributed across an orthogonal decomposition, and what functional form does the distribution take?

### 5.3.2 The substrate inputs

Two substrate-level commitments are load-bearing:

- **Substrate non-contextuality.** The bandwidth assigned to a measurement outcome cannot depend on which other outcomes are simultaneously being considered (i.e., which orthogonal decomposition the outcome appears in). The substrate's bandwidth distribution is a property of the outcome itself relative to the substrate state, not a property of the measurement context. This is a direct substrate-ontological consequence of P04 (bandwidth update rule applied at chain endpoints) plus the participation-channel structure committed by the participation primitives.
- **Bandwidth conservation across orthogonal decompositions.** The total bandwidth across any complete orthogonal decomposition equals the substrate region's total bandwidth. This is the substrate-level non-contextuality condition combined with bandwidth boundedness from P04.

Together, these two commitments force the bandwidth distribution to satisfy specific structural constraints when evaluated at any orthogonal decomposition.

### 5.3.3 The mathematical bridge: Gleason 1957

Gleason's theorem (1957) establishes that any non-contextual measure on the projection lattice of a Hilbert space of dimension $\geq 3$, satisfying the conservation condition (total measure = constant across orthogonal decompositions), must take the form

```math
P(|\psi\rangle) = \mathrm{tr}(\hat\rho \hat P_\psi)
```

where $\hat\rho$ is a density matrix and $\hat P_\psi$ is the projector onto $|\psi\rangle$. Specialized to pure states, this reduces to the squared amplitude form $P = |\langle\psi|\phi\rangle|^2$.

The theorem is a mathematical structural result; it does not depend on quantum mechanics' empirical content. What it requires is non-contextuality plus the conservation condition. ED supplies both at the substrate level (Section 5.3.2). Gleason supplies the mathematical bridge from the substrate-level conditions to the squared functional form.

### 5.3.4 Why the squared form is FORCED

The squared form is not chosen; it is the unique non-contextual measure satisfying conservation on the projection lattice (in dimension $\geq 3$, where Gleason's theorem applies). Linear, fourth-power, or absolute-value forms violate either non-contextuality or conservation, both of which are substrate-level commitments. The squared form is therefore form-FORCED by the substrate inputs combined with Gleason's mathematical bridge.

The $\hbar/2$ content (relevant in subsequent uses of bandwidth-conservation arguments, including the Heisenberg derivation of Section 5.5) is the substrate-natural coefficient in bandwidth quantization at chain-substrate endpoints. The numerical value of $\hbar$ is INHERITED — it is a substrate input from outside the primitive layer — but the factor of $1/2$ in the Heisenberg bound is structurally fixed by the bandwidth-conservation argument.

### 5.3.5 Born-Gleason and the U1 paper

The full derivation of the Born rule from substrate non-contextuality plus Gleason's theorem is presented in `papers/Born_Gleason/` and in `papers/U1_Participation_Measure/`. The U1 paper establishes the substrate participation measure as the substrate-level analogue of the projective measure on Hilbert space; the Born-Gleason paper completes the bridge to the squared probability form.

## 5.4 The Schrödinger Equation: Time-Translation Symmetry + Stone 1932

### 5.4.1 The structural question

Why does the Schrödinger equation have the specific functional form

```math
i\hbar\frac{\partial}{\partial t}|\psi\rangle = \hat H |\psi\rangle?
```

The form contains four structural commitments: existence (a unique evolution rule exists), uniqueness (the evolution is determined by initial state plus generator), linearity ($|\psi\rangle$ enters linearly), first-order-in-time (only $\partial_t$, not $\partial_t^2$), and Hamiltonian content (the generator $\hat H$ is Hermitian). Standard QM treats the equation as a postulate; ED derives all four structural commitments.

### 5.4.2 The substrate inputs

The substrate-level inputs:

- **Substrate time-translation symmetry.** The substrate's dynamical rules do not depend on which moment is "now." This is a substrate-ontological commitment that follows from the participation primitives plus P13 proper-time ordering (the ordering is intrinsic to chains, not to an external time coordinate that breaks time-translation symmetry).
- **Bandwidth conservation under unitary evolution.** In the thin-participation regime (where commitments have not yet occurred), substrate dynamics preserve total bandwidth. This is the substrate-level analogue of probability conservation in standard QM, derived from P04 plus the absence of commitment events in the thin regime.
- **Continuity of the evolution rule.** The substrate's time-evolution generates a one-parameter family of unitary transformations that depends continuously on the time parameter. This is a substrate-level regularity condition that the substrate's chain dynamics satisfy.

### 5.4.3 The mathematical bridge: Stone 1932

Stone's theorem (1932) establishes that any one-parameter family of unitary transformations $U(t)$ that depends continuously on $t$ has the form

```math
U(t) = e^{-iHt/\hbar}
```

for some Hermitian generator $H$. Differentiating:

```math
i\hbar\frac{d U(t)}{dt} = H U(t),
```

which applied to a state $|\psi(t)\rangle = U(t)|\psi(0)\rangle$ gives the Schrödinger equation directly.

The theorem is a mathematical structural result on one-parameter unitary groups in Hilbert space. ED supplies the inputs at the substrate level: substrate time-translation symmetry yields a unitary one-parameter family; bandwidth conservation yields unitarity; continuity yields the smooth dependence on $t$. Stone supplies the mathematical bridge from these conditions to the Schrödinger equation's specific form.

### 5.4.4 Why the Schrödinger form is FORCED

Each structural commitment in the Schrödinger equation is forced:

- **Existence.** The substrate-level evolution exists because substrate dynamics evolve in time (this is what time-translation symmetry says).
- **Uniqueness.** Stone's theorem produces a unique generator $H$ for the one-parameter family.
- **Linearity.** Unitary evolution is linear by construction; the substrate-level bandwidth conservation under unitary evolution forces linearity.
- **First-order-in-time.** Stone's theorem produces a first-order ODE in $t$; second-order or higher would be a stronger continuity condition, but Stone's continuity hypothesis is the minimal condition for substrate time-translation symmetry to apply.
- **Hamiltonian content.** Stone's generator $H$ is Hermitian; this is the substrate's Hamiltonian content, identified through the U3 and U4 paper chain.

The full derivation is presented in `papers/U3_Time_Translation_Schrodinger/` and `papers/U4_Hamiltonian_Form/`. The U2 paper (`papers/U2_Inner_Product/`) establishes the substrate-level inner-product structure that makes Hilbert space the appropriate target for Stone's theorem; the U5 paper (`papers/U5_Translation_Momentum/`) extends the construction to spatial translations and identifies the substrate-level momentum content.

## 5.5 The Heisenberg Uncertainty Principle: Substrate Finite-Bandwidth

### 5.5.1 The structural question

Why is the lower bound on joint position-momentum precision exactly $\hbar/2$? Why this specific functional form

```math
\Delta x \cdot \Delta p \geq \frac{\hbar}{2}?
```

Standard QM derives the Heisenberg bound from the canonical commutation relation $[\hat x, \hat p] = i\hbar$ via the Cauchy-Schwarz inequality. The structural origin of the canonical commutation relation, however, is not derived in standard QM — it is a structural feature of the formalism imposed at the level of the Hilbert space construction.

ED derives the Heisenberg bound directly from substrate finite-bandwidth constraints, with the $\hbar/2$ coefficient emerging as the substrate-natural factor.

### 5.5.2 The substrate inputs

The substrate-level inputs:

- **P04 bandwidth update rule.** Participation channels carry bounded bandwidth; the bandwidth update rule constrains how the substrate's bandwidth distributes across complementary observables (position and momentum being one canonical pair).
- **Substrate position-momentum complementarity.** Position and momentum at the substrate level are complementary participation channels — sharper localization in position requires broader distribution in momentum, by a substrate-level bandwidth-conservation argument.
- **Bandwidth quantization.** Bandwidth at chain endpoints is quantized in units of $\hbar/2$. This is the substrate-natural quantization unit; its specific value $\hbar$ is INHERITED, but the factor of $1/2$ is structurally fixed.

### 5.5.3 The structural argument

The substrate-level argument: a chain endpoint's bandwidth is distributed across complementary observables in a manner constrained by P04. Sharper localization in one observable (smaller $\Delta x$) requires broader distribution in the conjugate observable (larger $\Delta p$). The product $\Delta x \cdot \Delta p$ is bounded below by the substrate-natural quantization unit $\hbar/2$.

The functional form follows from substrate bandwidth-conservation across the position-momentum complementary pair. The $\hbar/2$ coefficient is the substrate-natural lower bound; sharper bounds would require the substrate to support sub-$\hbar/2$ bandwidth, which P04 forbids; weaker bounds would underuse the substrate's bandwidth quantum.

### 5.5.4 Why the $\hbar/2$ factor is FORCED

The $\hbar/2$ factor is the same factor that appears in:

- **The Born rule derivation** (Section 5.3): bandwidth-conservation across orthogonal decompositions is normalized by the same substrate quantum that fixes the Heisenberg lower bound.
- **The Schrödinger equation's kinetic-energy term** (Section 5.4): the substrate-natural coupling between participation density and chain proper-time evolution is governed by the same substrate quantum.

The factor's recurrence across these three derivations is a substrate-level structural signature. The numerical value of $\hbar$ remains INHERITED — it is a substrate input — but the factor of $1/2$ at the lower bound is form-FORCED by the substrate's bandwidth-quantization structure.

## 5.6 The Measurement Rule: P11 Commitment-Irreversibility

### 5.6.1 The structural question

When a quantum system is measured, what is the substrate-level event that produces the definite outcome? Standard QM postulates wavefunction collapse: the wavefunction transitions discontinuously from a superposition to a single eigenstate, and the transition is irreversible. Why is collapse a separate postulate from unitary evolution? Why is it irreversible?

ED removes the postulate. Measurement is identified as the coarse-grained signature of substrate-level commitment events through P11.

### 5.6.2 The substrate-level mechanism

The substrate-level analogue of measurement:

- **The substrate region representing the system** has its participation channels distributed across the available outcomes — the substrate analogue of the wavefunction's superposition over measurement-basis states.
- **The measurement apparatus**, via its substrate coupling to the system, applies a structural constraint (effectively, an environmental ED-injection event) that triggers commitment events at the system's chain endpoints.
- **P11 commitment-irreversibility** says that once a substrate event commits, the commitment cannot be reversed. The system's chain endpoints commit to a specific outcome; the commitment is irreversible.
- **The commitment events**, when coarse-grained to the continuum level via DCGT (Chapter 3), produce the appearance of wavefunction collapse: the substrate-level participation across multiple outcomes is replaced by participation concentrated at a single committed outcome.

The collapse is not a separate postulate; it is the coarse-grained signature of P11 commitment events at the chain endpoints involved in the measurement.

### 5.6.3 Why this matters structurally

The measurement rule's status changes from postulate to derived theorem. The structural payoff:

- **No measurement-postulate problem.** Standard QM's "measurement problem" — the question of why measurement is a special process distinct from unitary evolution — dissolves. Measurement is unitary evolution in the thin-participation regime followed by P11 commitment events at chain endpoints; the apparent discontinuity is the coarse-grained signature of the commitment.
- **No observer dependence.** Standard QM's interpretive issues around observer dependence (does the wavefunction collapse when the observer looks?) dissolve. P11 commitment events occur at substrate chain endpoints; observers are themselves substrate regions whose chain endpoints commit. There is no privileged observer status.
- **No collapse postulate.** The framework derives what would otherwise need to be postulated. This is structurally cleaner.

### 5.6.4 The Theorem 18 connection

The kernel-level arrow of time established in Theorem 18 (Chapter 4) supplies the substrate-level structural foundation for the directional content of measurement. P11 commitment events have forward-only character through the V1 kernel's forward-cone-only support. The measurement rule's irreversibility is therefore not just a property of P11 in isolation; it is the kernel-level arrow of time evaluated at chain endpoints during measurement events.

The connection is structural: Phase-1's measurement rule consumes P11 directly; Theorem 18's kernel-level arrow supplies the substrate-level structural foundation that makes the direction of measurement irreversibility consistent with the rest of the substrate ontology.

## 5.7 The Sixteen-Theorem Inventory

### 5.7.1 The Phase-1 closure structure

Phase-1 closure delivers sixteen forced theorems, labeled T1 through T16, organized into the four QM-postulate groups. The exact distribution of theorems across groups varies — some theorems contribute to multiple groups, and the U1–U5 paper chain produces the formal derivation chain — but the structural roles cluster as follows:

- **T-Born group.** Substrate participation measure (U1); Hilbert-space inner-product structure (U2); substrate non-contextuality and bandwidth-conservation arguments; Gleason 1957 application; Born rule's squared form. The U1 paper supplies the substrate-level participation measure; U2 supplies the inner-product structure; Born_Gleason completes the bridge.
- **T-Schrödinger group.** Substrate time-translation symmetry; one-parameter unitary family; Stone 1932 application; Schrödinger equation in canonical form; Hamiltonian content (U4); spatial translations and momentum content (U5). The U3 paper supplies the time-translation closure; U4 supplies the Hamiltonian form; U5 extends to momentum.
- **T-Uncertainty group.** Substrate finite-bandwidth; complementary-observable structure; bandwidth-quantization at chain endpoints; Heisenberg lower bound with the $\hbar/2$ factor; canonical commutation relations as substrate-level structural consequence.
- **T-Measurement group.** P11 commitment-irreversibility; chain-endpoint commitment events; coarse-graining to continuum collapse; Theorem 18 kernel-level arrow connection; no separate collapse postulate.

The full sixteen-theorem inventory is presented in `papers/Phase_1/` and `papers/QM_Emergence_Structural_Completion/`. The inventory's structural significance is that the four postulates of QM are each closed at the substrate level — none requires axiomatic status; each is a derived theorem.

### 5.7.2 The forced-theorem methodology

Each of T1–T16 is a *forced theorem* in the program's methodological sense: its conclusion is uniquely produced by the substrate inputs combined with mathematical structure. Forced theorems differ from ordinary theorems in that:

- **The conclusion is not chosen.** Alternative conclusions are not just refuted by external constraint; they are non-constructible from the inputs.
- **The forcing chain is auditable.** Each step in the derivation is identified, and the substrate inputs at each step are listed.
- **The form-FORCED / value-INHERITED distinction is explicit.** Each theorem identifies which content is structurally fixed by the substrate (form-FORCED) and which content inherits from substrate constants whose specific values come from outside the primitive layer (value-INHERITED).

T1–T16 form the program's first major closed-arc inventory; subsequent forced theorems (T17, T18, T19, T20, ECR, T21, N1, GR1, DCGT, UR-1) follow the same methodology.

## 5.8 Extensions: Spin-Statistics, Dirac, $g=2$, Canonical Commutation

Beyond the four QM-postulate closure, Phase-1 establishes additional structural content covering relativistic and quantum-field-theoretic territory.

### 5.8.1 Spin-statistics

The substrate-level analogue of the spin-statistics theorem follows from the substrate's chain-statistics structure (R.2.5 in the Phase-1 inventory). Half-integer-spin chains and integer-spin chains have substrate-level statistical properties that, after coarse-graining, produce fermionic and bosonic statistics respectively. This is consistent with the standard spin-statistics theorem of relativistic QFT but derived from substrate principles.

### 5.8.2 The Dirac equation

The substrate-level derivation of the Dirac equation (R.3 in the Phase-1 inventory) follows from substrate-level relativistic structure on the spinor bundle. The Cl(3,1) signature is identified at the substrate level (R.2.4); the spinor structure is derived. The Dirac equation emerges as the substrate-level theorem describing relativistic chain dynamics on the spinor bundle.

### 5.8.3 The $g=2$ electron magnetic moment

The substrate-level derivation produces the electron's magnetic moment $g=2$ (or, with QED corrections, $g \approx 2.0023...$) as a structural consequence rather than a fitting parameter. The $g=2$ value follows from the substrate-level spinor structure plus the Dirac-equation derivation; corrections from substrate-level vacuum polarization match the standard QED expansion.

### 5.8.4 Canonical commutation relations

The canonical commutation relations $[\hat x, \hat p] = i\hbar$ follow from the substrate-level position-momentum complementarity used in the Heisenberg derivation (Section 5.5). The relations are not postulated; they are the substrate-level structural consequence of finite-bandwidth chain endpoints distributing participation across complementary observables.

### 5.8.5 What the extensions establish

Together, these extensions establish that Phase-1 closes more than the four QM postulates. The framework reaches into relativistic QFT territory at form level: spin-statistics, Dirac equation, and $g=2$ are derived rather than postulated. Chapter 6 develops the form-level QFT content further (T17 gauge-field-as-rule-type, UV-finiteness, ED-I-13 quantum information as channel geometry).

## 5.9 What Phase-1 Changes About Quantum Mechanics

### 5.9.1 No experiment runs differently

Standard QM's empirical content is preserved exactly. The Born rule is squared; the Schrödinger equation is unchanged; the Heisenberg bound is the same; measurement is irreversible. Every experiment that has ever validated quantum mechanics continues to validate it. The framework changes the *story underneath* the postulates, not the postulates' empirical content.

### 5.9.2 The interpretive frame shifts

Three structural changes:

- **The four postulates are no longer postulates.** They are derived theorems with substrate-level structural origin.
- **The measurement problem dissolves.** Wavefunction collapse is identified as the coarse-grained signature of substrate-level P11 commitment events; there is no separate collapse postulate, and no observer dependence is required.
- **Quantum mechanics becomes a coarse-grained reading of substrate dynamics in the thin-participation regime.** Standard QM is what substrate dynamics look like when commitment has not yet occurred and substrate dynamics admit unitary, reversible evolution. Departures from standard QM (decoherence, measurement, classical limits) are the substrate-level signatures of commitment events at chain endpoints.

### 5.9.3 The relationship to interpretations of quantum mechanics

ED's substrate-level framework is not an interpretation of standard QM. It is a structural framework that produces standard QM as a derived consequence. The traditional interpretive options (Copenhagen, many-worlds, Bohmian mechanics, decoherence-based interpretations, QBism, etc.) ask different questions about the same axiomatic QM. ED asks where the axioms come from and provides a substrate-level answer.

This positions ED outside the standard interpretive landscape. The framework does not adjudicate between interpretations; it supplies a structural foundation that makes the interpretive questions less load-bearing. If one accepts the substrate ontology, the four postulates are derived rather than chosen, and the interpretive puzzles around their status (especially around measurement) shift onto the substrate-ontological question instead.

### 5.9.4 The transition from substrate to QM

The transition is auditable:

1. **Substrate primitives** (Chapter 1).
2. **Load-bearing invariants** (Chapter 2).
3. **DCGT coarse-graining bridge** (Chapter 3).
4. **Theorem N1 + Theorem 18 kernel-level arrow** (Chapter 4).
5. **Phase-1 closure of QM postulates** (Chapter 5, this chapter).
6. **Form-level QFT and quantum information** (Chapter 6).
7. **Quantum computation architecture** (Chapter 7).

Each step in the chain identifies its substrate inputs and its mathematical bridges. By the end of the chain, standard QM is not a self-contained framework with axiomatic foundations; it is the coarse-grained reading of substrate dynamics in the thin-participation regime, and quantum computing (Chapter 7) is the engineered occupation of that regime.

## 5.10 Form-FORCED vs Value-INHERITED at the Phase-1 Closure

### 5.10.1 What is form-FORCED

The structural content of T1–T16 is form-FORCED by the substrate inputs combined with the mathematical bridges:

- **The Born rule's squared form.** Forced by substrate non-contextuality + bandwidth conservation + Gleason 1957.
- **The Schrödinger equation's structural content** (existence, uniqueness, linearity, first-order-in-time, Hamiltonian content). Forced by substrate time-translation symmetry + bandwidth conservation + continuity + Stone 1932.
- **The Heisenberg lower bound's functional form.** Forced by substrate finite-bandwidth + complementary-observable structure + bandwidth quantization at $\hbar/2$.
- **The measurement rule's irreversibility.** Forced by P11 commitment-irreversibility + the kernel-level arrow of Theorem 18.
- **The spin-statistics theorem at substrate level.** Forced by substrate chain-statistics structure.
- **The Dirac equation form.** Forced by substrate relativistic structure on the spinor bundle (Cl(3,1) signature derived from R.2.4).
- **The $g=2$ leading-order electron magnetic moment.** Forced by substrate-level spinor structure plus Dirac-equation derivation.
- **The canonical commutation relations.** Forced by substrate-level position-momentum complementarity.

### 5.10.2 What is value-INHERITED

Specific numerical values that the framework does not derive in closed form at the primitive layer:

- **The numerical value of $\hbar$.** Substrate input; not derived from other primitives. The factor of $1/2$ in $\hbar/2$ is form-FORCED; the value of $\hbar$ is INHERITED.
- **The specific functional shape of the V1 vacuum kernel.** Used in Phase-1 indirectly through the substrate-level vacuum-response structure that enters Born and Schrödinger arguments. Finite-width is FORCED; closed-form shape is INHERITED.
- **Particle-specific masses and coupling constants.** These appear in the Dirac equation and in the $g=2$ corrections; their specific values inherit from particle physics empirical input, not from substrate primitives.
- **The Standard Model gauge group.** Phase-1 establishes the form of QM; T17 (Chapter 6) establishes the form of gauge fields; the specific gauge group nature realizes is INHERITED empirical input. The framework derives the *form* of gauge invariance and gauge-field structure without committing to which specific group nature realizes.

### 5.10.3 The methodological consistency

The form-FORCED / value-INHERITED pattern at Phase-1 is consistent with the pattern at the primitive layer (Chapter 1), the load-bearing invariants layer (Chapter 2), the DCGT layer (Chapter 3), and the Theorem N1 + Theorem 18 layer (Chapter 4). The structural form of each derived QM postulate is fixed; specific numerical values inherit from substrate constants whose closed-form derivation either comes from outside the primitive layer (substrate inputs like $\hbar$) or remains downstream open work.

## 5.11 Dependencies

### 5.11.1 Upstream

- **Chapter 1.** Substrate primitives, especially P04 (bandwidth update rule, foundational for Born and Heisenberg derivations) and P11 (commitment-irreversibility, foundational for the measurement rule). Also P01 (event discreteness, contributing to UV-finiteness in Chapter 6 extensions).
- **Chapter 2.** Load-bearing invariants. Multiplicity $\mathcal{M}$ enters the Born-rule derivation through bandwidth-conservation structure. The V1 kernel mediates substrate-level vacuum response that enters the Schrödinger argument.
- **Chapter 4.** Theorem N1 + Theorem 18 kernel-level arrow. Supplies the substrate-level structural foundation for the directional content of measurement (through P11 + V1 forward-only support).

### 5.11.2 Downstream

- **Chapter 6 (Form-level QFT and Quantum Information).** Builds on Phase-1's QM closure to derive T17 (gauge-field-as-rule-type), UV-finiteness, and the channel-geometry account of quantum information (ED-I-13). Phase-1 supplies the substrate-level QM foundation; Chapter 6 extends to QFT-territory form-level content.
- **Chapter 7 (Quantum Computation).** Identifies quantum computation as the engineered occupation of the thin-participation regime that Phase-1 characterizes. Phase-1's substrate-level account of QM is the foundation on which UR-1's three substrate conditions are formulated.
- **Chapters 8, 9, 10, 11, 12, 13.** Each consumes Phase-1's QM closure indirectly through DCGT coarse-graining, since the substrate-to-continuum bridge produces standard QM in the thin-participation regime as a baseline.
- **Chapter 14 (Cross-platform unifications).** The form-FORCED / value-INHERITED methodology, including Phase-1's pattern of deriving QM postulates from substrate primitives, is one of the cross-domain consistency signatures developed in Chapter 14.

## 5.12 Canonical Sources

- `papers/Phase_1/`
- `papers/QM_Emergence_Structural_Completion/`
- `papers/Born_Gleason/`
- `papers/U1_Participation_Measure/`
- `papers/U2_Inner_Product/`
- `papers/U3_Time_Translation_Schrodinger/`
- `papers/U4_Hamiltonian_Form/`
- `papers/U5_Translation_Momentum/`

The Phase_1 paper presents the sixteen-theorem closure in publication-grade form. The QM_Emergence_Structural_Completion paper integrates the closure with extensions (spin-statistics, Dirac, $g=2$, canonical commutation relations). The Born_Gleason paper develops the Born-rule derivation. The U1–U5 paper chain develops the substrate-level construction underlying the Schrödinger equation: U1 (participation measure), U2 (inner-product structure), U3 (time-translation closure), U4 (Hamiltonian form), U5 (translation/momentum content).

The Monograph Shell's Appendix A theorem provenance map lists T1–T16 with their substrate-input dependencies and the Gleason / Stone mathematical bridges. The Notation Glossary in Appendix B lists all symbols used in the chapter.

## 5.13 Optional Figures

**Figure 5.1 — The four QM postulates and their substrate-level derivations.** A four-row diagram. Each row corresponds to one postulate (Born, Schrödinger, Heisenberg, Measurement). Columns: (i) Standard QM status (postulate); (ii) Substrate inputs consumed; (iii) Mathematical bridge (Gleason 1957 for Born, Stone 1932 for Schrödinger, internal substrate argument for Heisenberg, P11 + Theorem 18 for Measurement); (iv) ED Phase-1 status (derived theorem). The figure makes visible the structural transition from postulate to theorem across all four cases.

**Figure 5.2 — The U1–U5 paper chain.** A vertical flow diagram with five nodes: U1 (participation measure), U2 (inner-product structure), U3 (time-translation Schrödinger), U4 (Hamiltonian form), U5 (translation/momentum). Arrows show the dependency chain. A side-arrow from U1 leads to Born_Gleason; a side-arrow from U2 leads to the Hilbert-space embedding. The figure makes visible the explicit derivation chain from substrate primitives through to the Schrödinger equation.

**Figure 5.3 — The substrate-level analogue of measurement.** A two-panel diagram. Left panel: substrate region with participation distributed across multiple chain endpoints (the substrate analogue of a wavefunction superposition). Right panel: P11 commitment event at one chain endpoint, with surrounding endpoints showing reduced participation (the substrate analogue of post-measurement collapse). Arrows between panels indicate the time evolution from pre-measurement to post-measurement. A label notes that the apparent discontinuity is the coarse-grained signature of P11 commitment events; no separate collapse postulate is required.

**Figure 5.4 — The Phase-1 inventory and its extensions.** A circular diagram with sixteen-theorem closure in the center (T1–T16, organized into four quadrants for Born, Schrödinger, Heisenberg, Measurement). Outside the central circle, four extension theorems: spin-statistics (R.2.5), Dirac equation (R.3), $g=2$ electron magnetic moment, canonical commutation relations. Arrows from the central inventory to the extensions indicate the substrate-level connections.

**Figure 5.5 — The transition from substrate to standard QM.** A vertical flow diagram showing the seven-step chain: substrate primitives (Chapter 1) → load-bearing invariants (Chapter 2) → DCGT coarse-graining (Chapter 3) → kernel-level arrow (Chapter 4) → Phase-1 closure (Chapter 5) → form-level QFT (Chapter 6) → QC architecture (Chapter 7). Each step is annotated with its substrate inputs and outputs. The figure makes visible the explicit auditability of the transition from substrate ontology to standard QM and beyond.

**Figure 5.6 — Form-FORCED vs Value-INHERITED at Phase-1.** A two-column diagram. Left column ("Form-FORCED"): squared form of Born rule, Schrödinger equation structural content, Heisenberg lower bound functional form, measurement irreversibility, spin-statistics, Dirac form, $g=2$ leading order, canonical commutation relations. Right column ("Value-INHERITED"): numerical value of $\hbar$, V1 kernel functional shape, particle masses, gauge couplings, Standard Model gauge group. The figure makes visible the demarcation Phase-1 inherits from the broader program methodology.
