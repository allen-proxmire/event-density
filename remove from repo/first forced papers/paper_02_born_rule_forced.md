# The Born Rule is FORCED

**Paper #2 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #2 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The Born rule — that the probability of a measurement outcome $K$ is the squared modulus $|\psi_K|^2$ of the corresponding amplitude — is the bridge between the wavefunction and observable frequencies. Gleason's theorem (1957) and Busch's POVM extension (2003) derive its quadratic form, but only by *assuming* the complex Hilbert space at the outset. This paper shows that, **given the substrate primitives of Paper #1 plus Primitive P11 (commitment as a discrete substrate-level event with environmental phase-randomization at commitment) and the participation-measure result $|P_K|^2 = b_K$**, the Born rule is forced via two parallel routes — a direct definitional route from bandwidth fractions, and a Gleason-Busch reconstruction performed on the participation manifold rather than on a postulated Hilbert space. Linear, higher-power, contextual, signed, non-additive, and phase-dependent alternatives are each excluded. The unique survivor is $\text{Prob}(K) = |P_K|^2/\sum_K |P_K|^2$. The claim is conditional: the quadratic form is forced *given* the substrate's bandwidth-additivity primitive (P04) and the commitment-with-phase-randomization mechanism (P11). These primitives are themselves load-bearing inputs; why they have the structural character they do is upstream content for the Primitive-Forcing Meta-Paper. The present paper establishes that no *other* probability rule on commitment outcomes is consistent with those primitives.

---

## 1. Framing

### 1.1 What standard quantum mechanics postulates about probability

Every introductory quantum-mechanics course states the Born rule as a separate postulate, usually labeled the **measurement postulate** or **statistical interpretation postulate**:

> *If a quantum system is in state $\psi$ and a measurement is performed with respect to an observable having eigenstates $\{|K\rangle\}$, the probability of obtaining outcome $K$ is $|\langle K | \psi \rangle|^2$.*

This is the bridge between the wavefunction and observable frequencies. Without it, the wavefunction is a mathematical object without empirical content. With it, every quantum prediction in every laboratory becomes computable.

But the form of the rule is, on inspection, a list of choices:

1. **The rule is quadratic.** Probability is $|\langle K | \psi \rangle|^2$, not $|\langle K | \psi \rangle|^1$, not $|\langle K | \psi \rangle|^3$, not any other power of the amplitude.
2. **The rule is non-contextual.** The probability of outcome $K$ depends only on the state and the projector onto $|K\rangle$, not on which other outcomes are being considered alongside it.
3. **The rule is additive.** Probabilities of disjoint outcomes sum, allowing the rule to extend coherently from projective to generalized (POVM) measurements.
4. **The rule is phase-blind.** Multiplying $\psi$ by a global phase $e^{i\alpha}$ leaves all probabilities unchanged.

Each of these is structurally independent. The exponent could in principle be different. The rule could be contextual. Probability rules failing additivity have been studied. Phase-dependent rules are a priori possible. The empirical content of quantum mechanics pins all four down — but in the standard presentation, they arrive as a single postulate, taken whole and unexplained.

### 1.2 The puzzle

A century of attempts to derive the rule has produced partial results:

- **Gleason's theorem** (1957) derives the quadratic form from three axioms on probability measures over projection operators on a Hilbert space of dimension $\geq 3$: non-negativity, normalization, and finite/$\sigma$-additivity. It is a deep result but requires the **Hilbert space as input** — Gleason does not derive the Hilbert-space arena itself.
- **Busch's theorem** (2003) extends Gleason to dimension two via POVMs, again with Hilbert space as input.
- **Many-Worlds / decision-theoretic** derivations (Deutsch 1999; Wallace 2003) attempt to derive Born from rationality axioms in the Everett interpretation. These derivations are technically subtle and remain contested.
- **Zurek envariance** (2003) derives Born from environment-induced symmetries of entangled states, requiring assumptions about environmental coupling structure.

None of these programs answers the upstream question: *why is the state space a complex Hilbert space in the first place, and why does the probability rule have the form it has at the substrate level — not just on the Hilbert space?* The standard answer is that the postulate matches experiment. The honest answer is that no derivation from a deeper structural layer has been delivered.

A program that wants to settle the question structurally needs:

1. A pre-quantum substrate from which the amplitude carrier itself is derived.
2. An argument that the probability rule on that substrate is forced by substrate-level structural facts, not by assumed Hilbert-space axioms.
3. An explicit exclusion of alternative rules (linear, higher-power, contextual, signed) by substrate-condition violations.

### 1.3 What this paper does

The Event Density (ED) framework supplies the first ingredient. Paper #1 of this series establishes, from substrate primitives alone, that the amplitude carrier on every channel of the participation graph is the complex-valued **participation measure**
$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i\pi_K(x, t)},
$$
where $b_K$ is the substrate-level bandwidth (a primitive non-negative real-valued quantity) and $\pi_K$ is the substrate-level polarity (a primitive $U(1)$-valued angular quantity).

The present paper supplies the other two. It derives the Born rule
$$
\text{Prob}(K \mid \text{commitment at } x) = \frac{|P_K(x)|^2}{\sum_{K'} |P_{K'}(x)|^2} = \frac{b_K(x)}{\sum_{K'} b_{K'}(x)}
$$
from substrate primitives plus the participation-measure result, via two parallel routes that converge on the same answer:

- A **direct route**: the squared-modulus identity $|P_K|^2 = b_K$ from Paper #1 means that any probability rule based on bandwidth fractions is automatically quadratic in amplitude. Bandwidth additivity at the substrate level + environmental decoherence at commitment produces the normalized form.
- A **Gleason-Busch route**: substrate-level channel structure forces non-contextuality (independently of postulating Hilbert space); bandwidth additivity forces $\sigma$-additivity; the participation-measure result supplies the Hilbert-space arena Gleason and Busch require. The standard Gleason-Busch reconstruction then applies, producing the quadratic rule as a unique density operator $\rho(u)$ with $f(E) = \text{Tr}(\rho E)$.

The two routes are complementary. The direct route shows the rule is forced *definitionally* by the participation-measure construction. The Gleason-Busch route shows it is forced *structurally* by primitive-level non-contextuality and additivity. Either alone would suffice; together they establish forcing over-determined, in the same sense that a theorem with two independent proofs is more robust than a theorem with one.

Alternative rules — linear amplitude, $\alpha \neq 2$ power, contextual probability assignments, signed measures, non-additive rules, phase-dependent rules — are each excluded by explicit substrate-condition violation. The unique survivor is the Born rule in its standard form.

**Series context.** Paper #1 of this series forced the amplitude carrier on the substrate. Paper #3 will force the sesquilinear inner product and the Tsirelson bound on the resulting Hilbert space. The present paper sits structurally between them, forcing the probability rule that bridges the amplitude carrier to observable frequencies.

---

## 2. Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: the participation-measure structure of Paper #1, bandwidth additivity (P04), and commitment-with-environmental-phase-randomization (P11)*. Then the probability that a commitment event at locus $u$ selects channel $K^*$ from the available-channel set $\mathcal{K}(u)$ is, uniquely up to normalization convention,
> $$
> \text{Prob}(K^* \mid u) = \frac{|P_{K^*}(u)|^2}{\sum_{K \in \mathcal{K}(u)} |P_K(u)|^2}.
> $$
> Equivalently, there exists a unique density operator $\rho(u)$ on the Hilbert space $\mathcal{H}(u)$ spanned by $\{|K\rangle : K \in \mathcal{K}(u)\}$ such that for every effect $E \in \mathcal{E}(\mathcal{H}(u))$, the probability assignment satisfies $f(E) = \text{Tr}(\rho(u) E)$.
>
> *The phase-randomization at commitment is a substrate-level primitive (P11), not derived here. It is load-bearing in the operational route; why the substrate has commitment with this character is upstream content (Primitive-Forcing Meta-Paper).*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **P04 (bandwidth as non-negative additive scalar):** required for $\sigma$-additivity of the probability rule.
- **P11 (commitment with environmental phase-randomization):** discrete substrate-level events at which multi-channel participation collapses to a single channel, with phase-randomization on a uniform $U(1)$ distribution. Supplies the substrate-level mechanism producing observed measurement outcomes.
- **Paper #1 result** (the complex polar participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$): taken as input. The squared-modulus identity $|P_K|^2 = b_K$ makes the rule quadratic in amplitude by construction.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, the Born rule $\text{Prob}(K) = |P_K|^2/\sum_{K'} |P_{K'}|^2$ is the unique probability rule consistent with the postulates, derived via two complementary routes (a direct operational route from bandwidth fractions, and a Gleason-Busch reconstruction on the participation manifold). The Gleason-Busch route is honest: once Paper #1 supplies the Hilbert-space arena and bandwidth additivity supplies $\sigma$-additivity, standard Gleason 1957 + Busch 2003 produces the quadratic form. The novelty is the substrate-level origin of the arena, not the Gleason machinery itself.

### 3.1 What is FORCED

- The **quadratic form** $\text{Prob}(K) \propto |P_K|^2$. The exponent is exactly 2, not 1, not 3, not any non-quadratic number.
- **Non-contextuality**. The probability of outcome $K$ depends only on the local participation structure at $u$ and on the channel $K$ itself, not on the partition $\mathcal{D}$ of $\mathcal{K}(u)$ into which $K$ is embedded.
- **POVM compatibility**. The rule extends, by Busch's theorem applied to the participation manifold, to all generalized effect-valued measurements, with $f(E) = \text{Tr}(\rho E)$ for a unique density operator.
- **$\sigma$-additivity**. Probabilities of disjoint channel-subsets at the same locus sum, with countable additivity inherited from bandwidth additivity.
- **Phase-blindness**. The probability rule is invariant under the global $U(1)$ gauge $P_K \to e^{i\alpha} P_K$. Local relative phases $\pi_{K_1} - \pi_{K_2}$ do appear in the *interference* content of the participation measure, but they vanish from the *commitment-selection probability* by environmental phase-randomization.

### 3.2 What is INHERITED

- The **overall normalization convention** $\sum_K \text{Prob}(K \mid u) = 1$ over the available-channel set $\mathcal{K}(u)$. The forcing argument gives probability fractions; setting the total to unity is a convention.
- The **empirical identification of $b_K$ with observed frequencies**. The forcing argument gives the structural form $\text{Prob}(K) = b_K / \sum b_{K'}$. That observed frequencies in a laboratory equal these substrate-level bandwidth fractions is an empirical fact connecting the substrate to measurement apparatus — required for the rule to have empirical content but not derived within this paper.
- The **participation-measure carrier** $P_K = \sqrt{b_K}\,e^{i\pi_K}$ itself. Paper #1 forces this; the present paper uses it as input.

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive the Schrödinger equation, the dynamics of $P_K$ in time. That is Paper #4.
- This paper does **not** derive the Bell-Tsirelson bound. The sesquilinear inner-product structure of the participation manifold and the $2\sqrt{2}$ bound are Paper #3.
- This paper does **not** derive the Heisenberg uncertainty inequality. Paper #4 (Schrödinger) and the orthogonal-partition structure of bandwidth handle this jointly.
- This paper does **not** address the measurement problem, the ontology of collapse, or the choice between collapse and decoherence interpretations. The substrate-level mechanism for commitment (a primitive of the ED framework) plays the role of "what happens at measurement"; whether this is consistent with any particular philosophical interpretation of quantum mechanics is a separate question.
- This paper does **not** address continuous-spectrum measurements (e.g., position measurements with continuous outcomes). The forcing argument is stated for discrete channel outcomes; extension to continuous-spectrum cases follows the standard measure-theoretic route used in extending Gleason's theorem and is not redone here.

---

## 4. Key Vocabulary

For the reader new to Event Density, the following terms are sufficient for the body of the paper. A full alphabetized glossary appears in Appendix A.

- **Substrate.** The pre-quantum layer of primitive structure on which the ED framework is built. Not a Hilbert space; not a manifold; not a quantum field theory.
- **Channel.** A primitive structural pathway in the substrate, indexed by a label $K$. Channels are *ontologically primitive* — their identity is intrinsic to the participation graph, not derived from any external organizational choice.
- **Available-channel set $\mathcal{K}(u)$.** The set of channels at locus $u$ that a chain can participate in.
- **Participation bandwidth $b_K(u)$.** A non-negative real-valued primitive quantity on each channel at each locus, additive across disjoint channel decompositions.
- **Participation measure $P_K(u)$.** The complex-valued object $\sqrt{b_K(u)}\,e^{i\pi_K(u)}$ established in Paper #1 as the unique amplitude carrier consistent with substrate conditions. $|P_K|^2 = b_K$ holds by construction.
- **Commitment.** A discrete substrate-level event at which a chain's participation across multiple channels collapses to a single channel. The mechanism that produces observed outcomes.
- **Non-contextuality.** The property that the probability of outcome $K$ is a function of $K$ alone, not of the partition of $\mathcal{K}(u)$ containing $K$.
- **POVM.** Positive Operator-Valued Measure. The generalized form of a quantum measurement, in which outcomes correspond to positive operators $E_i \geq 0$ summing to the identity, rather than orthogonal projectors. Standard projective measurements are a special case.
- **Effect.** An element $E$ of the effect algebra $\mathcal{E}(\mathcal{H})$ on a Hilbert space $\mathcal{H}$: a self-adjoint operator with $0 \leq E \leq \mathbb{1}$. Effects are the building blocks of POVMs.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying the following conditions.

### C1. Participation graph + channel structure (Primitives P03 + P07)

The substrate supplies a participation graph $G$ with a discrete index set $\mathcal{K}$ of channels. At each locus $u \in G$ there is an available-channel set $\mathcal{K}(u) \subseteq \mathcal{K}$ of channels participating at $u$, at most countable.

Critically, channels are **ontologically primitive**: the identity of each channel $K$ is intrinsic to the participation graph and does not depend on any organizational decomposition. If $K$ appears in two different complete decompositions $\mathcal{D}_1 \ni K$ and $\mathcal{D}_2 \ni K$ of $\mathcal{K}(u)$, it is the *same channel* in both.

### C2. Bandwidth with additivity (Primitive P04)

The substrate supplies non-negative bandwidth $b_K(u) \in \mathbb{R}_{\geq 0}$ on each channel at each locus, with primitive-level additivity:
$$
K = K_1 \sqcup K_2 \implies b_K = b_{K_1} + b_{K_2},
$$
where $\sqcup$ denotes disjoint decomposition into sub-channels.

Bandwidth has a four-band decomposition (internal, adjacency, environmental, commitment-reserve) with total bandwidth conserved along an isolated chain's persistence regime. The decomposition is used in §7 for the direct-route argument.

### C3. Polarity (Primitive P09)

The substrate supplies a $U(1)$-valued angular variable $\pi_K(u) \in U(1)$ on each channel, the unique angular primitive in the substrate. This is required for the participation-measure carrier of C5.

### C4. Commitment events (Primitive P11)

The substrate supports discrete commitment events at which a chain's multi-channel participation collapses to a single channel $K^*$. Two operational features of commitment are required:

- **Individuation threshold**: when environmental bandwidth grows past a structural threshold, the multi-channel coherent state becomes unsustainable and a single-channel outcome is forced.
- **Environmental phase-randomization**: during commitment, environmental coupling acts on the participation phases $\pi_K$ as independent random shifts $\delta_K$ on $[0, 2\pi)$, drawn from a distribution set by the environmental mode spectrum.

These features are substrate-level operational content of the commitment primitive; they are not Born-rule statements in disguise. The Born rule itself is what this paper is to derive.

### C5. The participation-measure result (Paper #1)

The amplitude carrier on each channel is the complex-valued participation measure
$$
P_K(u) = \sqrt{b_K(u)} \cdot e^{i\pi_K(u)} \in \mathbb{C},
$$
with $|P_K|^2 = b_K$ and $\arg(P_K) = \pi_K$. This is the FORCED result of Paper #1; the present paper uses it as input.

A reader who has not read Paper #1 may take C5 as a definitional premise: the amplitude carrier has the polar form $\sqrt{b}\,e^{i\pi}$, satisfying the squared-modulus identity. Paper #1 establishes that no other form survives the substrate-condition test on a substrate satisfying C1-C4.

### C6. No Hilbert space, no linearity, no unitarity, no Gleason axioms as inputs

The forcing argument invokes only C1-C5 plus the following standard mathematical infrastructure:

- The Cauchy functional equation: continuous non-negative solutions of $f(a+b) = f(a)+f(b)$ are linear.
- Gleason's theorem (1957) on probability measures over projection operators on a Hilbert space of dimension $\geq 3$.
- Busch's theorem (2003) extending Gleason to dimension two via the effect algebra.

The Hilbert-space arena that Gleason and Busch require is *supplied* by the participation-measure construction (C5 + C2), not assumed independently. The forcing argument is closed against the circularity of assuming what is to be derived.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

These are mathematical alternatives to the quadratic rule, defined without reference to existing physical frameworks.

**A1. Linear probability rule $\text{Prob}(K) \propto |P_K|^1$.** The probability is proportional to the modulus of the amplitude, not the squared modulus.

**A2. Higher-power rules $\text{Prob}(K) \propto |P_K|^\alpha$, $\alpha \neq 2$.** The exponent could be any positive real other than 2: linear ($\alpha = 1$, the case of A1), quartic ($\alpha = 4$), or some non-integer.

**A3. Contextual probability assignments.** The probability of outcome $K$ depends not just on $K$ and the state, but on the *partition* $\mathcal{D}$ of $\mathcal{K}(u)$ in which $K$ is embedded. That is, $\text{Prob}(K \mid \mathcal{D}) \neq \text{Prob}(K \mid \mathcal{D}')$ for distinct partitions $\mathcal{D}, \mathcal{D}'$ both containing $K$.

**A4. Signed or negative probabilities.** Probabilities are allowed to be negative; outcomes are weighted by quantities that can be positive or negative, with empirical frequencies extracted by some downstream sign-handling procedure (e.g., the Wigner quasi-probability distribution).

**A5. Non-additive probability rules.** Probabilities of disjoint channel-subsets do not sum: $\text{Prob}(K_1 \cup K_2) \neq \text{Prob}(K_1) + \text{Prob}(K_2)$ even when $K_1, K_2$ are disjoint.

**A6. Phase-dependent probability rules.** The probability depends on the absolute phase $\pi_K$, not just on the squared modulus. For instance, $\text{Prob}(K) \propto b_K \cdot (1 + \epsilon\cos\pi_K)$ for some $\epsilon$.

**A7. Non-POVM-compatible rules.** The rule covers projective measurements (sharp eigenstate outcomes) but does not extend coherently to generalized effect-valued measurements (partial measurements, joint measurements of incompatible observables, continuous monitoring with finite efficiency).

### 6.2 Mainstream alternatives

These are alternatives drawn from the existing literature on quantum foundations.

**B1. Bohmian / pilot-wave probability postulate.** Born is adopted as a separate "quantum equilibrium" postulate, motivated by typicality but not derived. Both the complex Hilbert space and the $|\psi|^2$ rule are inputs.

**B2. GRW / CSL collapse probabilities.** Spontaneous-localization models retain the standard $|\psi|^2$ rule while modifying the dynamics. The rule is preserved, not derived.

**B3. QBism / $\psi$-epistemic probability rules.** Born is interpreted as a coherence condition on agent degrees of belief, justified by Dutch-book arguments. The quadratic form is a coherence constraint, not a substrate-level result.

**B4. Everettian branch-weight rules.** Decision-theoretic derivations (Deutsch 1999; Wallace 2003) attempt to derive Born from rationality axioms applied to Everettian branches. Technical correctness and conceptual coherence remain disputed.

**B5. Real-vector-space QM probability rules (Stueckelberg-class).** A two-component real vector $\Psi \in \mathbb{R}^{2}$ with auxiliary operator $J$ ($J^2 = -1$). The probability rule reduces to standard $|\psi|^2$ once $J$ is identified with multiplication by $i$.

**B6. Quaternionic QM probability rules (Adler-class).** Quaternionic states with quaternionic Born-like rule $|\langle K | \psi \rangle|^2$. Internally consistent for single-particle non-relativistic systems (Adler 1995); produces composition pathologies in multi-particle settings.

---

## 7. Constructive Necessity

This section verifies that the substrate-level rule $\text{Prob}(K \mid u) = |P_K(u)|^2/\sum_{K'}|P_{K'}(u)|^2$ satisfies the requirements for a probability rule under conditions $\{C\}$, via two parallel routes converging on the same answer. Either route alone would establish the positive half of the forcing theorem. The two routes together establish it over-determinedly.

### 7.1 Route A — direct derivation from bandwidth fractions

**Definition.** The substrate-level commitment-selection rule is
$$
\text{Prob}(K^* \mid u) := \frac{b_{K^*}(u)}{\sum_{K \in \mathcal{K}(u)} b_K(u)} = \frac{|P_{K^*}(u)|^2}{\sum_{K \in \mathcal{K}(u)} |P_K(u)|^2},
$$
where the second equality uses the participation-measure identity $|P_K|^2 = b_K$ from C5.

**Step 1 (positivity).** $b_K \geq 0$ from C2. Therefore $\text{Prob}(K^* \mid u) \geq 0$ for every $K^*$.

**Step 2 (normalization).** Summing over $K^* \in \mathcal{K}(u)$:
$$
\sum_{K^* \in \mathcal{K}(u)} \text{Prob}(K^* \mid u) = \frac{\sum_{K^*} b_{K^*}(u)}{\sum_{K} b_K(u)} = 1.
$$

**Step 3 (additivity over disjoint channel-subsets).** Let $S, T \subseteq \mathcal{K}(u)$ with $S \cap T = \emptyset$. By bandwidth additivity (C2):
$$
\text{Prob}(S \cup T \mid u) = \frac{\sum_{K \in S \cup T} b_K(u)}{\sum_{K \in \mathcal{K}(u)} b_K(u)} = \text{Prob}(S \mid u) + \text{Prob}(T \mid u).
$$
Bandwidth additivity at the substrate level passes directly to $\sigma$-additivity of the probability rule.

**Step 4 (phase-blindness from environmental decoherence).** The participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ carries phase content, and the squared modulus $|\Psi|^2 = |\sum_K P_K|^2$ of a coherent sum contains cross-terms $P_K^* P_{K'}$ with relative-phase content. By the environmental phase-randomization feature of C4, each channel acquires an independent random phase shift $\delta_K$ during commitment; cross-terms with $K \neq K'$ average to zero over the environmental ensemble (see Appendix A.1 for the explicit calculation). The post-commitment state is the **incoherent diagonal mixture**
$$
\sum_K b_K(u) \cdot |K\rangle\langle K|,
$$
and the probability rule extracted from this mixture is the bandwidth fraction. Phase content drops out of the commitment-selection probability while remaining present in the pre-commitment interference of the participation measure.

**Step 5 (well-posedness).** The right-hand side of the definition is a well-defined ratio whenever $\sum_K b_K(u) > 0$, which holds in any non-trivial participation regime. At loci where the chain is not participating ($\sum_K b_K = 0$), no commitment event occurs, and the rule is not invoked.

The direct route is complete. The rule satisfies positivity, normalization, $\sigma$-additivity, phase-blindness, and well-posedness. The quadratic exponent is forced *definitionally* — it appears not as a choice of rule but as a consequence of $|P_K|^2 = b_K$ in C5.

### 7.2 Route B — Gleason-Busch reconstruction on the participation manifold

The Gleason-Busch reconstruction takes as input a Hilbert space $\mathcal{H}$ and a probability assignment $f: \mathcal{E}(\mathcal{H}) \to [0,1]$ on effects (or projectors), satisfying three axioms: non-contextuality, $\sigma$-additivity over disjoint effects, and normalization. The output: a unique density operator $\rho$ such that $f(E) = \text{Tr}(\rho E)$ for all $E$. The quadratic Born rule emerges as the special case where $\rho = |\psi\rangle\langle\psi|$ and $E = |K\rangle\langle K|$, giving $f(|K\rangle\langle K|) = |\langle K | \psi\rangle|^2$.

The Gleason-Busch route on the participation manifold proceeds in four links.

**Link 1: Non-contextuality from C1.** By C1, each channel $K$ is a graph-substructure with intrinsic identity, and its bandwidth $b_K(u)$ is the same in every decomposition $\mathcal{D}$ containing $K$. The bandwidth-fraction map is therefore non-contextual, satisfying Gleason's axioms A4/A8 (non-contextual typing and frame-sum constancy).

**Link 2: $\sigma$-additivity from C2.** Bandwidth additivity over disjoint channel-subsets (C2) gives $\sigma$-additivity of the bandwidth-fraction map over countable disjoint $K$-subsets at the same locus, satisfying Gleason's axiom A7.

**Link 3: Hilbert-space arena from C5.** Define $\mathcal{H}(u) := \text{span}_\mathbb{C}\{|K\rangle : K \in \mathcal{K}(u)\}$. The participation-measure result (C5) makes this construction well-posed: the carrier algebra is $\mathbb{C}$ and the inner product is sesquilinear (the latter is the content of Paper #3; this paper takes it as input). The participation-measure state at $u$ is $|\psi(u)\rangle = \sum_K P_K(u) |K\rangle$, with $\langle \psi(u) | \psi(u)\rangle = \sum_K |P_K(u)|^2 = \sum_K b_K(u)$.

**Link 4: Gleason for $d \geq 3$, Busch for $d = 2$.** With Links 1-3 in place, Gleason's theorem (1957) applies to the bandwidth-fraction map on $\mathcal{H}(u)$ for $d := \dim \mathcal{H}(u) \geq 3$, yielding a unique density operator $\rho(u)$ such that $f(P) = \text{Tr}(\rho(u) P)$ for every projector $P$. Busch's theorem (2003) extends this to $d = 2$ via the effect algebra $\mathcal{E}(\mathcal{H}(u))$, with the weighted-channel-subset effect structure obtained by varying both the channel-decomposition and the weights.

For projective measurements, restricting $\rho(u)$ to rank-1 projectors $|K\rangle\langle K|$ gives $\text{Prob}(K \mid u) = \langle K | \rho(u) | K\rangle$. In the pure-state case $\rho = |\psi\rangle\langle\psi|$, this reduces to
$$
\text{Prob}(K \mid u) = |\langle K | \psi(u)\rangle|^2 = |P_K(u)|^2 = b_K(u),
$$
matching Route A's bandwidth fraction after normalization.

The two routes converge. Route A traces the quadratic form to the participation-measure construction ($|P_K|^2 = b_K$); Route B traces it to the substrate-level Gleason-Busch axioms (non-contextuality and additivity). Either alone forces the rule; together they over-determine it.

### 7.3 POVM extension and well-posedness

Busch's theorem (Link 4 above) extends the result from projective measurements to the full effect algebra $\mathcal{E}(\mathcal{H}(u))$. In the participation-manifold setting, an effect $E \in \mathcal{E}(\mathcal{H}(u))$ corresponds to a weighted channel-subset $(S, w)$ at $u$: a subset $S \subseteq \mathcal{K}(u)$ of channels together with weights $w: S \to [0,1]$. The effect-value map is $f(S, w \mid u) = \sum_{K \in S} w(K) \cdot b_K(u) / \sum_{K \in \mathcal{K}(u)} b_K(u)$. This is non-negative (C2), bounded by 1 (normalization), and $\sigma$-additive over disjoint weighted subsets — Busch's axioms B1-B3. Non-contextuality of typing (B4) is inherited from Link 1.

Busch's theorem then gives: there exists a unique density operator $\rho(u)$ on $\mathcal{H}(u)$ such that $f(E) = \text{Tr}(\rho(u) E)$ for every effect $E$. This is the POVM-extended Born rule, covering all generalized measurements including partial measurements, joint measurements of incompatible observables, and continuous monitoring with finite efficiency.

The construction is well-posed: every effect has a well-defined probability, the assignment is jointly continuous in $(E, \rho)$, and the density operator $\rho(u)$ is uniquely determined by the probability assignment on a generating set of effects.

The positive half of the forcing theorem is complete via both routes.

---

## 8. Exclusion Arguments

This section dispatches each alternative encoding listed in §6, by identifying the substrate condition each violates.

### 8.1 A1, A2 — Non-quadratic exponents $\alpha \neq 2$

**Claim.** Any rule $\text{Prob}(K) \propto |P_K|^\alpha$ with $\alpha \neq 2$ violates C2 (bandwidth additivity).

**Argument.** The participation-measure identity (C5) gives $|P_K|^2 = b_K$. Suppose the probability rule is $\text{Prob}(K) \propto |P_K|^\alpha = b_K^{\alpha/2}$. For the rule to be additive over disjoint channel decompositions $K = K_1 \sqcup K_2$:
$$
(b_{K_1} + b_{K_2})^{\alpha/2} = b_{K_1}^{\alpha/2} + b_{K_2}^{\alpha/2}.
$$
This is the Cauchy functional equation in the exponent $\alpha/2$. For non-negative $b_{K_1}, b_{K_2}$, by the Minkowski / power-mean inequality, equality holds only when $\alpha/2 = 1$, i.e., $\alpha = 2$. For $\alpha > 2$ the left-hand side is strictly larger (super-additive); for $\alpha < 2$ strictly smaller (sub-additive). In either case, substrate-level bandwidth additivity is violated.

A1 ($\alpha = 1$, linear rule) is a special case: it gives $(b_{K_1} + b_{K_2})^{1/2} > b_{K_1}^{1/2} + b_{K_2}^{1/2}$ when both bandwidths are positive (Minkowski), so disjoint-channel probabilities would *not* sum. The rule is non-additive and violates C2.

The exponent $\alpha = 2$ is forced. This is the same Cauchy-functional-equation argument that forces $|P_K|^2 = b_K$ in Paper #1; here it propagates through to the probability rule via the participation-measure identity.

### 8.2 A3 — Contextual probability assignments

**Claim.** Contextual rules — probabilities depending on partition $\mathcal{D}$ as well as on $K$ — violate C1 (channels as ontologically primitive).

**Argument.** C1 specifies that channels are graph-substructures with intrinsic identity: if $K$ appears in two complete decompositions $\mathcal{D}_1 \ni K$ and $\mathcal{D}_2 \ni K$, it is the *same channel* in both, with the *same bandwidth*. Any probability assignment that depends on $\mathcal{D}$ rather than on $K$ alone is therefore a probability assignment to *partition labels*, not to channels.

The substrate has channels but not partition labels. Partitions are organizational decompositions imposed by an observer; channels are primitive. A rule whose values change under relabeling of partitions while $K$ remains the same channel is assigning probabilities to objects (labels) that do not have primitive ontological status.

Equivalently: contextual rules fail Gleason's non-contextual-typing axiom A4 (Link 1 of §7.2). The argument that forces non-contextuality at the substrate level — channels-as-primitives — does not admit any contextual exception.

### 8.3 A4 — Signed or negative probabilities

**Claim.** Signed-probability rules violate C2 (bandwidth non-negativity).

**Argument.** C2 specifies $b_K \in \mathbb{R}_{\geq 0}$ as a primitive substrate quantity. The participation-measure identity (C5) gives $|P_K|^2 = b_K$; squared moduli are intrinsically non-negative. Any probability rule built on bandwidth fractions inherits non-negativity automatically. A signed-probability rule would require either (i) reinterpreting $b_K$ as a signed quantity (violating C2 directly) or (ii) supplying a separate sign-carrying primitive (which the substrate does not provide).

The Wigner quasi-probability distribution, which is famously signed, is not a probability assignment on channels — it is a distribution on phase space whose marginals are probabilities. Signed quasi-probability *of phase-space distributions* is a different object from signed *channel-selection probability*. The latter is excluded by C2.

### 8.4 A5 — Non-additive probability rules

**Claim.** Non-additive rules violate C2 (bandwidth additivity).

**Argument.** Bandwidth additivity (C2) is a primitive substrate fact: disjoint sub-channels combine by addition of bandwidth. This passes directly to additivity of the probability rule built on bandwidth fractions (§7.1, Step 3). Any rule failing additivity would require either (i) modifying the underlying bandwidth-additivity primitive (violating C2) or (ii) using a non-bandwidth-based probability assignment, which violates the participation-measure identity (C5).

### 8.5 A6 — Phase-dependent probability rules

**Claim.** Rules in which $\text{Prob}(K)$ depends on the absolute phase $\pi_K$ violate the environmental phase-randomization feature of C4 and the $U(1)$-invariance of bandwidth from C3.

**Argument.** The environmental phase-randomization feature of commitment (C4) acts on each channel as an independent random phase shift $\delta_K$. Averaging over the environmental phase distribution kills all phase-dependence in the post-commitment outcome distribution (§7.1, Step 4 and Appendix A.1). Any rule that depended on the absolute phase $\pi_K$ after commitment would have to *survive* this averaging — but no $\pi_K$-dependent rule does, because $\delta_K$ is uniformly distributed on $[0, 2\pi)$ and the average of any non-constant $\pi_K$-dependent function over this distribution is the function's mean, which has no $\pi_K$-dependence by construction.

Furthermore, the bandwidth quantity $b_K$ is $U(1)$-invariant by C3 (polarity is the *independent* angular primitive, separate from the magnitude content of bandwidth). A probability rule built on bandwidth is automatically phase-blind. A phase-dependent rule would have to use the participation measure $P_K$ rather than the bandwidth $b_K$, but the participation-measure identity (C5) and Steps 1-4 of §7.1 force the rule to factor through $|P_K|^2 = b_K$.

Relative phases $\pi_K - \pi_{K'}$ do enter the *interference* structure of the participation measure (the coherent-sum content $|\Psi|^2$ before commitment). They do *not* enter the commitment-selection probability after environmental decoherence. The distinction is structural, not interpretive.

### 8.6 A7 — Non-POVM-compatible rules

**Claim.** A rule covering only projective measurements but failing to extend to POVMs violates the structural content of Link 4 in §7.2 (Busch's theorem).

**Argument.** Busch's theorem (2003) shows that the same axiom structure giving Born for projective measurements — non-contextuality, $\sigma$-additivity, normalization — gives the POVM form $f(E) = \text{Tr}(\rho E)$ for every effect $E$. The axioms are not strengthened to obtain the POVM extension; they are the *same axioms*, applied to the effect algebra rather than the projector lattice.

In the participation-manifold setting, the effect structure (weighted channel-subsets) inherits its admissibility from the same Link 1-3 facts that establish the projective case. A rule that fails on POVMs would have to *violate* one of those facts at the effect level — but the facts are substrate-level (C1 channel primitivity, C2 bandwidth additivity, C5 participation-measure carrier) and apply uniformly to projectors and effects alike.

A rule restricted to projective measurements only is therefore either consistent with Busch (in which case it extends, by Busch's theorem, to all effects — and is just the standard Born rule under-specified) or inconsistent with one of Link 1-3 (in which case it violates substrate conditions). The "non-POVM-compatible" alternative collapses: either it is Born, or it fails a substrate condition.

### 8.7 B1, B2 — Bohmian, GRW/CSL

**Claim.** Bohmian and GRW/CSL programs adopt $|\psi|^2$ as input rather than deriving it. Therefore they do not satisfy the substrate-conditions test (which requires that the rule be derived from $\{C\}$).

**Argument.** Both programs work entirely within the standard complex Hilbert-space arena, with $\psi(x)$ and $|\psi|^2$ taken as starting structure. Bohmian theory supplements with hidden trajectories guided by the phase gradient; GRW/CSL supplements with stochastic collapse. Neither addresses the substrate-level question "why is the rule quadratic on a complex amplitude?" — each begins with that rule in hand.

If the substrate forces the Born rule via the participation-measure structure (as established in §7), then Bohmian and GRW/CSL become interpretive overlays on the same forced rule. They take a position on a different question (the ontology of trajectories, the mechanism of collapse) and are not in the alternative-encodings space for the *forcing* question. This is not a dismissal of either program; it is a placement: they live downstream of the forcing chain, not in competition with it.

### 8.8 B3 — QBism / $\psi$-epistemic

**Claim.** QBist Born derivations argue for the quadratic rule as a coherence condition on agent belief; this is not a derivation from a physical substrate.

**Argument.** QBism interprets $\psi$ as a degree-of-belief state held by an agent, and derives the Born rule as a Dutch-book-style coherence condition on the agent's degrees of belief. Whether the resulting derivation is technically valid is contested; what is clear is that the substrate it operates on is *agent belief structure*, not the physical substrate of $\{C\}$.

Under the substrate-conditions test of the present paper, QBism is not in the alternative-encodings space because it does not derive the rule from the same kind of object. If the physical substrate forces the rule via $\{C\}$, then any agent reasoning coherently about that substrate will, by extension, have degrees of belief consistent with the Born rule — but the order of explanation is reversed from QBism's: the substrate forces the rule, and coherent agents adopt it because the substrate forces it, not because their belief structures alone require it.

### 8.9 B4 — Everettian branch-weight rules

**Claim.** Everettian branch-weight derivations (decision-theoretic, frequentist, typicality) are derivations *within* the standard complex Hilbert-space framework; they do not derive the Hilbert-space structure or the quadratic rule from a substrate.

**Argument.** Deutsch-Wallace and related programs attempt to derive Born within the Everett interpretation, using rationality axioms applied to agents in Everettian branches. Like B3 (QBism), the substrate of these derivations is decision-theoretic structure, not physical substrate. Whether the technical derivations are sound is contested (Albert, Price, and others have raised circularity concerns).

Under the substrate-conditions test, B4 is not in the alternative-encodings space for the same reason as B1-B3: it does not derive the rule from $\{C\}$. If the substrate forces Born, the Everettian branch-weight question becomes "what do agents in branches of the wavefunction infer?" — and the answer is structurally consistent with the substrate-forced rule.

### 8.10 B5 — Real-vector-space QM

**Claim.** Real-vector-space variants of QM with auxiliary $J$-operator are structurally equivalent to standard complex QM, and the corresponding Born rule reduces to $|\psi|^2$ once $J$ is identified with multiplication by $i$.

**Argument.** Stueckelberg's $\mathbb{R}^{2}$-valued state with operator $J$ ($J^2 = -1$) is isomorphic to the standard complex Hilbert space. The Born rule on this construction is mathematically the same rule, rewritten in real-vector notation. There is no genuinely distinct probability rule here — only a relabeling.

Under the substrate-conditions test: if $J$ is not identified with multiplication by $i$, then it is an additional structural commitment unsupported by primitives (no primitive in $\{C\}$ supplies $J$). If $J$ is identified with multiplication by $i$, then we have the standard complex Hilbert space and the standard Born rule — which is the forced answer.

### 8.11 B6 — Quaternionic QM

**Claim.** Quaternionic Born rules face two problems: (i) the underlying quaternionic carrier is excluded by Paper #1 (quaternions have $SU(2)$ angular structure exceeding what polarity supplies), and (ii) the multi-particle composition pathology is documented in Adler's program itself.

**Argument.** Paper #1 establishes that the substrate primitive supplying angular content is polarity, with values in $U(1)$. The quaternions $\mathbb{H}$ have $SU(2)$ angular structure — a three-dimensional non-abelian Lie group, in contrast to one-dimensional abelian $U(1)$. Using $\mathbb{H}$ as the amplitude carrier requires either (i) selecting a $U(1) \subset SU(2)$ embedding (unconstrained, structurally underdetermined) or (ii) using the full $SU(2)$ structure (introducing surplus content unsupported by primitives). Either way, $\mathbb{H}$ violates the substrate angular-content constraint.

Even if one ignored Paper #1's carrier-level exclusion and adopted quaternionic states postulationally, Adler's program documents structural pathologies in multi-particle composition (tensor-product anomalies, problems with relative-phase content across systems) that prevent quaternionic Born from extending coherently beyond single-particle non-relativistic systems. The composition pathology is itself a substrate-condition failure: bandwidth additivity across joint subsystems (C2 applied to product systems) does not work in the quaternionic setting.

### 8.12 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 linear $\|P\|^1$ | C2 | Sub-additive over disjoint channels (Minkowski). |
| A2 $\alpha \neq 2$ | C2 | Cauchy functional equation forces $\alpha = 2$. |
| A3 contextual | C1 | Channels are ontologically primitive; bandwidth is partition-independent. |
| A4 signed/negative | C2 | Bandwidth is non-negative; substrate supplies no sign-carrying primitive. |
| A5 non-additive | C2 | Bandwidth additivity propagates directly to the probability rule. |
| A6 phase-dependent | C3, C4 | Environmental phase-randomization at commitment kills phase dependence; bandwidth is $U(1)$-invariant. |
| A7 non-POVM-compatible | C1, C2 (via Busch) | Same axioms forcing projective Born force the POVM extension; restriction to projective only is inconsistent. |
| B1 Bohmian | not in space | Adopts $|\psi|^2$ as input rather than deriving it. |
| B2 GRW/CSL | not in space | Retains standard $|\psi|^2$; modifies dynamics, not the rule. |
| B3 QBism | not in space | Substrate is agent belief, not physical substrate. |
| B4 Everettian | not in space | Substrate is decision-theoretic, not physical. |
| B5 Stueckelberg | collapses to forced | $J = i$ identification reduces to standard complex QM. |
| B6 quaternionic | C3 (Paper #1) + C2 in multi-particle | Excluded at carrier level by Paper #1; composition pathology in multi-particle settings. |

**The Born rule $\text{Prob}(K \mid u) = |P_K(u)|^2/\sum_{K'} |P_{K'}(u)|^2$ is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The Born rule is the most experimentally tested rule in physics. Every quantum-mechanics experiment for the past century has measured outcome frequencies, and every measured frequency has matched the quadratic rule within statistical and systematic error. The empirical falsifier of this paper is therefore identical to the empirical falsifier of standard quantum mechanics: any observed deviation from $|\psi|^2$ in any properly controlled experiment.

Specific known constraints:

- **Atomic interferometry**: Born verified to $\sim 10^{-3}$ at the level of three-path interference (Sinha et al. 2010).
- **Multi-slit experiments**: deviations from $|\psi|^2$ constrained to be below $\sim 10^{-2}$ in coefficient (Sorkin third-order tests).
- **Trapped-ion and superconducting-qubit measurements**: Born verified to high precision in projective and POVM regimes.
- **Tests of the squared-amplitude rule against alternative-exponent rules**: no observed deviation.

If any of these constraints were experimentally relaxed — if a deviation from $|\psi|^2$ were reproducibly observed — the substrate-level rule of this paper would be refuted in the same way as the standard rule. The substrate derivation does not predict any sub-Born-rule corrections; it predicts the rule exactly.

### 9.2 Structural falsifier

A different falsifier is structural: identify a substrate satisfying conditions $\{C\}$ — channel-primitive participation graph (C1), non-negative additive bandwidth (C2), $U(1)$ polarity (C3), commitment with phase-randomization (C4), and the participation-measure carrier (C5) — but supporting a non-quadratic, contextual, signed, or phase-dependent probability rule that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. The exclusion chain in §8 is closed: each alternative is dispatched by a specific substrate-condition violation. A reader who can construct a substrate-satisfying alternative refutes the present paper, by exhibiting a counterexample.

### 9.3 Downstream exposure

The Born rule is upstream of essentially every quantitative quantum prediction. Three immediate exposures of the present forcing:

**Bell-Tsirelson bound (Paper #3).** The Tsirelson bound $|S| \leq 2\sqrt{2}$ on Bell-CHSH correlations is a consequence of the sesquilinear inner-product structure of the participation-measure Hilbert space combined with the Born rule. Any experimentally established Bell-CHSH value above $2\sqrt{2}$ would falsify the forcing chain — and would falsify quantum mechanics generally, since Tsirelson's bound has been observed up to current precision (e.g., Hensen et al. 2015 loophole-free Bell test).

**Schrödinger evolution (Paper #4).** Stone's theorem on the participation-measure Hilbert space forces a linear unitary one-parameter group as the time-evolution generator. Any experimentally established non-linear or non-unitary kinematic evolution at the level the substrate predicts would falsify the chain. GRW/CSL collapse modifications are consistent with current experiment because their characteristic rates are too small to detect; the falsifier sits at the boundary of their experimentally accessible regime.

**POVM measurements (this paper, Link 4).** The substrate-derived rule extends to POVMs via Busch's theorem. Every POVM measurement performed in a physics laboratory — partial measurements, joint measurements of incompatible observables, continuous monitoring with finite efficiency — is governed by $f(E) = \text{Tr}(\rho E)$ with $\rho$ the substrate-supplied density operator. Any POVM outcome statistics violating this form would falsify the chain.

The substrate-level Born rule is what supports every quantitative quantum prediction. Its empirical exposure is the entire empirical content of quantum mechanics.

---

## Appendix A — Full Derivation Chain and Glossary

### A.1 The two-route derivation in detail

**Route A (direct): environmental phase-randomization.**

Start from the participation-measure carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$. The coherent participation state at $u$ is
$$
|\Psi(u)\rangle = \sum_K P_K(u) |K\rangle.
$$
The squared modulus of this state, expanded:
$$
|\Psi(u)|^2 = \sum_K |P_K(u)|^2 + \sum_{K \neq K'} P_K^*(u) P_{K'}(u).
$$
The first term is the sum of bandwidths $\sum_K b_K(u)$ — real, non-negative. The second term contains cross-terms $P_K^* P_{K'} = \sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}$ with phase content.

Under the environmental phase-randomization feature of C4, each channel acquires an independent random phase shift $\delta_K(u, t)$ at commitment. Each cross-term becomes
$$
P_K^* P_{K'} \to \sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}\,e^{i(\delta_{K'} - \delta_K)}.
$$
Averaging over the environmental ensemble (independent uniform $\delta_K \sim [0, 2\pi)$):
$$
\langle e^{i(\delta_{K'} - \delta_K)}\rangle_{\text{env}} = \delta_{K, K'}.
$$
Cross-terms vanish on average. The post-commitment state is the diagonal mixture
$$
\rho_{\text{post}}(u) = \sum_K b_K(u) \cdot |K\rangle\langle K|.
$$
The probability of a specific single-channel outcome $K^*$ is then $b_{K^*}(u)/\sum_K b_K(u) = |P_{K^*}|^2/\sum_K |P_K|^2$. This is the Born rule.

**Route B (Gleason-Busch): non-contextuality + additivity → density operator.**

The bandwidth-fraction map $f(K, u) = b_K(u)/\sum_{K'} b_{K'}(u)$ is well-defined on $\mathcal{K}(u)$. Three properties:

- (i) **Non-negativity**: $f(K, u) \geq 0$ from C2.
- (ii) **Normalization**: $\sum_K f(K, u) = 1$ by construction.
- (iii) **$\sigma$-additivity**: for disjoint $S, T \subseteq \mathcal{K}(u)$, $f(S \cup T) = f(S) + f(T)$, from C2.
- (iv) **Non-contextuality**: $f(K, u)$ depends only on $(K, u)$, not on which partition $\mathcal{D}$ of $\mathcal{K}(u)$ contains $K$. From C1.

Define $\mathcal{H}(u) := \text{span}_\mathbb{C}\{|K\rangle : K \in \mathcal{K}(u)\}$ with sesquilinear inner product (the Hilbert-space arena supplied by the participation-measure structure C5). The four properties above are precisely Gleason's axioms on probability measures over the projector lattice of $\mathcal{H}(u)$.

For $d := \dim \mathcal{H}(u) \geq 3$: Gleason's theorem (1957) applies. There exists a unique density operator $\rho(u)$ on $\mathcal{H}(u)$ such that $f(P) = \text{Tr}(\rho(u) P)$ for every projector $P$ on $\mathcal{H}(u)$.

For $d = 2$ (qubits, spin-1/2, polarization): Gleason's theorem fails in dimension 2, but Busch's theorem (2003) extends it via the effect algebra. The weighted-channel-subset effect structure $(S, w)$ supplies the richness needed: varying both the channel-decomposition $\mathcal{D}_\theta$ and the weights $w$ generates the full effect lattice $\mathcal{E}(\mathbb{C}^2)$ on the Bloch sphere. Busch's axioms B1-B4 hold, and the conclusion follows: unique $\rho(u)$ with $f(E) = \text{Tr}(\rho(u) E)$ for every effect.

For projective measurements with $\rho(u) = |\psi(u)\rangle\langle\psi(u)|$ and $E = |K\rangle\langle K|$:
$$
f(|K\rangle\langle K|, u) = \text{Tr}(|\psi(u)\rangle\langle\psi(u)| \cdot |K\rangle\langle K|) = |\langle K | \psi(u)\rangle|^2 = |P_K(u)|^2.
$$
After normalization by $\langle \psi | \psi\rangle = \sum_K b_K$, this is the substrate-level Born rule.

The two routes converge.

### A.2 Why both routes matter

The two routes are not redundant; they expose different structural facts.

Route A makes the *definitional* origin of the exponent 2 explicit. The participation measure was constructed (in Paper #1) so that $|P_K|^2 = b_K$ — the squared modulus is bandwidth by construction. Any probability rule built on bandwidth fractions therefore has the quadratic form not as a choice but as a consequence of the carrier's structure. The exponent 2 is the same 2 that appears in Paper #1's Cauchy-functional-equation argument forcing $|P|^2 = b$.

Route B makes the *structural* origin explicit. Non-contextuality is forced by the channel-primitivity primitive (C1); $\sigma$-additivity is forced by bandwidth-additivity (C2); the Hilbert-space arena is supplied by the participation-measure result (C5). The Gleason-Busch theorem then applies, producing the unique density-operator form and extending to POVMs.

A reader who finds one route more compelling than the other may take either as the primary derivation. The forcing argument is over-determined: even if one route had a hidden flaw, the other would still establish the result. In a foundational uniqueness theorem, over-determination is a virtue.

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Primitive-level (P04) non-negative real-valued substrate quantity on each channel at each locus; additive across disjoint channel decompositions.
- **Born rule.** The probability rule $\text{Prob}(K \mid u) = |\langle K | \psi(u)\rangle|^2 / \langle \psi | \psi\rangle$ assigning outcome probabilities to projective measurements. Extends to POVMs as $f(E) = \text{Tr}(\rho E)$.
- **Chain.** A persistent sequence of micro-events in the substrate. Chains are the substrate-level analog of particles/systems.
- **Channel.** Primitive-level (P07) structural pathway in the participation graph; ontologically primitive (graph-substructure with intrinsic identity).
- **Commitment.** Primitive-level (P11) discrete event at which multi-channel participation collapses to a single channel; the substrate-level mechanism producing observed outcomes.
- **Density operator.** A self-adjoint, positive, trace-1 operator $\rho$ on a Hilbert space, representing the (possibly mixed) state of the system. Pure states correspond to rank-1 projectors $\rho = |\psi\rangle\langle\psi|$.
- **Effect.** An element of the effect algebra $\mathcal{E}(\mathcal{H})$ on Hilbert space $\mathcal{H}$: self-adjoint operator with $0 \leq E \leq \mathbb{1}$.
- **Environmental phase-randomization.** Substrate-level (C4) feature of commitment events: environmental coupling acts on each channel's polarity phase as an independent random shift drawn uniformly from $[0, 2\pi)$.
- **Event Density (ED).** The framework within which this paper is written.
- **FORCED.** A theorem-grade structural result derived from substrate primitives and standard mathematics, with no additional structural commitments. Contrasts with INHERITED and OUT OF SCOPE.
- **Gleason's theorem (1957).** Any probability measure on the projector lattice of a complex Hilbert space of dimension $\geq 3$ satisfying non-negativity, normalization, and $\sigma$-additivity has the form $f(P) = \text{Tr}(\rho P)$ for a unique density operator $\rho$.
- **Busch's theorem (2003).** Generalization of Gleason to dimension 2 via the effect algebra: any state-on-effects map satisfying non-negativity, normalization, $\sigma$-additivity, and non-contextual typing has the form $f(E) = \text{Tr}(\rho E)$.
- **INHERITED.** Quantitative content (value, coefficient, normalization, empirical identification) used in the paper but not derived in it.
- **Locus $u$.** A point in the participation graph at which a chain participates and at which commitment events occur.
- **Non-contextuality.** Property that the probability of outcome $K$ depends only on $K$ (and the state), not on the partition $\mathcal{D}$ of $\mathcal{K}(u)$ in which $K$ is embedded.
- **Participation graph.** The graph-like structure underlying the ED substrate.
- **Participation measure.** The complex-valued amplitude carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ derived in Paper #1 and used as input here.
- **Polarity $\pi_K(u)$.** Primitive-level (P09) $U(1)$-valued angular variable on each channel at each locus.
- **POVM.** Positive Operator-Valued Measure: generalized measurement in which outcomes correspond to effects $E_i \geq 0$ summing to $\mathbb{1}$.
- **Primitive.** Structural commitment of the ED framework not derived from anything more upstream. The substrate has 13 primitives (P01-P13); this paper uses P03, P04, P07, P09, P11.
- **$\sigma$-additivity.** Countable additivity over disjoint sets: $f(\bigcup_n S_n) = \sum_n f(S_n)$ for pairwise disjoint $S_n$.
- **Substrate.** Pre-quantum layer of structure underlying the ED framework.
- **Substrate conditions $\{C\}$.** The minimal substrate properties required for the forcing theorem of this paper: C1-C6 listed in §5.

### A.4 Source-repository citations (for ED-internal readers)

The following internal sources contain extended technical content:

- `papers/Born_Gleason/born_gleason_paper.md` — the original publication-grade derivation (predecessor genre, foundational-theorem paper).
- `arcs/born_gleason/05_synthesis_theorem10.md` — synthesis memo assembling the four-link Gleason-Busch chain.
- `arcs/born_gleason/02_noncontextuality_argument.md` — non-contextuality from channel-as-primitive.
- `arcs/born_gleason/03_sigma_additivity_and_dimension.md` — $\sigma$-additivity from bandwidth additivity; dimension argument.
- `arcs/born_gleason/04_busch_extension_d2.md` — Busch POVM extension for $d=2$.
- `arcs/arc-foundations/born_rule_from_participation.md` — Route A (direct) derivation via environmental phase-randomization.
- `theorems/T10.md` — theorem-level index entry; status FORCED-unconditional, ratified 2026-04-26.

These are *not* required reading for the present paper.

---

*End of Paper #2.*
