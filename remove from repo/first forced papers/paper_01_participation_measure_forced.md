# The Participation Measure is FORCED

**Paper #1 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #1 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

Standard quantum mechanics opens with a postulate: the state of a system is a complex-valued wavefunction $\psi(x)$ whose squared modulus is a probability density. The complex-valued range, the squared exponent, and the inner-product structure are all assumed. This paper shows that, **given substrate primitives that supply (i) a non-negative additive bandwidth quantity $b_K$ (Primitive P04), (ii) a $U(1)$-valued angular polarity $\pi_K$ (Primitive P09) as the unique angular primitive in the substrate, and (iii) a channel structure on which both live (Primitives P03 + P07)**, the wavefunction-class object is not a postulate but a uniqueness theorem. Real-valued, quaternionic, signed-measure, phase-only, and non-quadratic alternatives are each excluded by an explicit structural argument. The unique survivor — the **participation measure** $P_K(x,t) = \sqrt{b_K(x,t)} \cdot e^{i\pi_K(x,t)}$ — has squared modulus equal to bandwidth and phase equal to polarity. The claim is conditional: the substrate primitives themselves (in particular the $U(1)$-valued character of P09 and the additive non-negative character of P04) are upstream commitments, not consequences of this paper. Why those primitives and not others is the subject of a separate Primitive-Forcing Meta-Paper. What this paper establishes is that *no other amplitude carrier is consistent with those primitives*, and that every Hilbert-space-arena theorem downstream (Born, Bell-Tsirelson, Heisenberg, Schrödinger) rests structurally on this conditional uniqueness.

---

## 1. Framing

### 1.1 What standard quantum mechanics postulates

Every introductory course on quantum mechanics opens with the same handed-down structure. A physical system is described by a **state vector**, written most often as a complex-valued function $\psi(x)$ on configuration space or, equivalently, as a vector in a complex Hilbert space. The Born rule says that the probability density of finding the system in configuration $x$ is the squared modulus $|\psi(x)|^2$. Inner products on the state space are sesquilinear (linear in one slot, conjugate-linear in the other), and observables are self-adjoint operators acting on this space.

This is the architecture inside which every quantum prediction is computed. It is also, on inspection, a list of assumptions:

1. **The state space is complex.** Not real. Not quaternionic. Not a higher division algebra. The state vector is $\psi(x) \in \mathbb{C}$.
2. **The probability rule is quadratic.** $\text{Prob}(x) \propto |\psi(x)|^2$, not $|\psi(x)|^1$ or $|\psi(x)|^3$ or any other exponent.
3. **The inner product is sesquilinear.** Not bilinear, not antisymmetric, not real.
4. **Phase content is independent of magnitude.** The state has both an amplitude and a phase, and the phase rotates continuously through the circle group $U(1)$, not through some other group.

These four facts are usually presented together as a single postulate ("the state is a vector in a complex Hilbert space"), but they are structurally independent. The exponent 2 could in principle be a different number. The phase could in principle take values in a different group. The carrier algebra could in principle be a different field.

The empirical content of quantum mechanics — interference, entanglement, the Born rule — gets pinned down once these four facts are fixed. But where the four facts come from is, in the standard presentation, a matter of historical convention and "what makes the math work."

### 1.2 The puzzle

A century of attempts to derive the postulates has produced partial results:

- **Gleason's theorem** (1957) derives the quadratic Born rule on a Hilbert space of dimension at least three, taking the Hilbert-space structure as given.
- **Busch's theorem** (1999) extends Gleason's result to dimension two via POVMs.
- **Hardy's axioms** (2001), **Masanes-Müller** (2011), and the **CBH theorem** (2003) derive parts of the structure from operational and information-theoretic axioms.
- **Reconstruction programs** (Dakic-Brukner, Chiribella-D'Ariano-Perinotti) reproduce the full Hilbert-space arena from a set of operational primitives.

These programs are powerful. None of them, however, answers the question at the root: *why a complex Hilbert space, rather than a real or quaternionic one?* The standard answer is "because experiment". The honest answer is "because the alternatives that have been tried do not reproduce quantum mechanics" — which is not the same as showing they are structurally impossible.

A program that wants to settle this question structurally needs three things:

1. A pre-quantum substrate — a layer of primitive structure not itself committed to complex Hilbert spaces.
2. An explicit enumeration of alternative encodings of the amplitude carrier — not just real and complex, but *every* candidate that satisfies the same substrate conditions.
3. A structural exclusion argument that knocks out everything except the complex-valued case.

### 1.3 What this paper does

The Event Density (ED) framework supplies the first ingredient: a substrate built from a small number of primitive structural commitments, none of which mentions complex numbers, Hilbert spaces, or the Born rule. This paper supplies the other two. It identifies the minimal substrate conditions for an amplitude carrier, enumerates the alternative encodings consistent with those conditions, and excludes each alternative by an explicit structural argument. The unique survivor is the complex-valued participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.

The claim is not that quantum mechanics has been derived from nothing. The claim is that, *given the substrate conditions named in §5*, the amplitude carrier is forced. The substrate conditions themselves are upstream commitments — primitive structural facts about participation, bandwidth, polarity, and channels — that the ED framework adopts and that this paper takes as given.

What gets eliminated is the conventional move of postulating the complex Hilbert space directly. What gets exposed downstream is everything in the Hilbert-space arena: the Born rule, the Bell-Tsirelson bound, the Heisenberg inequality, the Schrödinger equation. Each of these stands or falls on the result of this paper. None of them is used as input to it.

**Series context.** This is Paper #1 of the first-wave Event Density Forcing Series. The present paper forces the amplitude carrier on the substrate — the foundational result on which subsequent papers build. Paper #2 forces the Born rule using the carrier; Paper #3 forces the sesquilinear inner product and the Tsirelson bound; Paper #4 forces the Schrödinger equation; Papers #5-#10 extend through gauge fields, mass and the Hamiltonian, the Dirac equation with $g = 2$, the substrate-to-continuum bridge, substrate gravity, and black-hole architecture with Hawking radiation. Each downstream paper takes the participation measure as input from this one.

---

## 2. Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: bandwidth (P04) as a non-negative additive scalar, polarity (P09) as the unique $U(1)$-valued angular primitive, and channel structure (P03+P07)*. Then the amplitude carrier on that substrate is, uniquely up to a global phase convention, the complex-valued participation measure
> $$
> P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i\pi_K(x, t)}
> $$
> with $|P_K|^2 = b_K$ and $\arg(P_K) = \pi_K$.
>
> *The substrate primitives are load-bearing inputs to this theorem and are themselves treated upstream in the Primitive-Forcing Meta-Paper. The present paper establishes conditional uniqueness given those primitives.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **P03 (channel + locus indexing):** the substrate supplies a discrete index set of channels $\mathcal{K}$ and a (discrete or continuous) index set of loci.
- **P04 (bandwidth as non-negative additive scalar):** each channel carries a real-valued non-negative quantity $b_K \geq 0$, additive under channel decomposition.
- **P07 (channel structure as ontological primitive):** channels are structurally distinguishable carriers of substrate content, with identities intrinsic to the participation graph.
- **P09 ($U(1)$-valued polarity):** each channel carries an angular variable $\pi_K \in U(1) \cong S^1$, the substrate's unique angular primitive.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper (*The Event Density Framework: A 13-Primitive Substrate Ontology and Its Cross-Domain Reach*). The empirical case for the postulates rests on their downstream reach across domains (QM kinematics, gravitational dynamics, soft-matter rheology, black-hole architecture, multiplicity walls). This paper's contribution: given the four primitives above, the complex polar participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is the unique amplitude carrier consistent with the postulates. Alternatives (real-valued, quaternionic, signed-measure, phase-only, non-quadratic) are excluded by structural argument in §§7–8.

### 3.1 What is FORCED

- The **carrier algebra is the complex numbers** $\mathbb{C}$. Not $\mathbb{R}$, not $\mathbb{H}$, not any signed or extended-real structure.
- The **polar form** $P = r\cdot e^{i\theta}$ with $r \geq 0$ and $\theta \in U(1)$. Magnitude and phase are independent and continuous.
- The **squared-modulus identity** $|P_K|^2 = b_K$. The exponent is exactly 2, not 1, not 3, not any non-quadratic number.
- The **phase identification** $\arg(P_K) = \pi_K$. The phase factor is exactly the substrate-level polarity variable, not a function of it, not a different angular variable.

### 3.2 What is INHERITED

- The **overall normalization** of bandwidth. The forcing argument fixes $|P_K|^2 = c \cdot b_K$ for some positive constant $c$; setting $c = 1$ is a unit convention, not a structural commitment.
- The **global phase convention** $P_K \to e^{i\alpha} P_K$ for a constant $\alpha$. The forcing argument identifies phase up to a global $U(1)$ gauge. The standard $\arg$ branch is a convention.
- The **identification of $b_K$ with empirical observables** (probabilities, intensities, decay rates). The forcing argument gives $|P_K|^2 = b_K$ structurally; the empirical content of $b_K$ is a separate question handled in later papers (notably Paper #2: The Born Rule).

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive the Born rule. The Born rule says that probabilities of commitment outcomes are proportional to $|P_K|^2$. That is the content of Paper #2. The present paper says only that the carrier object $P_K$ has the structural form $\sqrt{b_K}\,e^{i\pi_K}$. The connection to probability requires a further argument (Gleason-Busch on the Hilbert space this paper enables).
- This paper does **not** derive the Schrödinger equation. The dynamical evolution of $P_K$ in time is the content of Paper #4. The present paper is a kinematic uniqueness theorem; it does not say how $P_K$ evolves.
- This paper does **not** address whether the ED primitives themselves are correct. The substrate conditions $\{C\}$ in §5 are upstream commitments. Whether the world is in fact described by a substrate satisfying them is an empirical question for the ED program as a whole. What this paper shows is conditional: *if* the substrate conditions hold, *then* the amplitude carrier is forced.
- This paper does **not** address gauge fields, gravity, or any sector beyond non-relativistic single-chain kinematics. Those are content of later papers in the series (notably Papers #5, #8, #9).

---

## 4. Key Vocabulary

For the reader new to Event Density, the following short list of terms is sufficient to follow the body of the paper. A full alphabetized glossary is in the Appendix.

- **Substrate.** The pre-quantum layer of primitive structure on which the ED framework is built. The substrate is *not* itself a Hilbert space, *not* a manifold, *not* a field theory. It is a graph-like structure equipped with primitive scalar, set-valued, and relational quantities.
- **Channel.** A primitive structural pathway in the substrate, indexed by a label $K$. A chain (a persistent micro-event sequence) participates through one or more channels at each point in spacetime.
- **Participation bandwidth $b_K(x,t)$.** A non-negative real-valued primitive quantity on each channel at each spacetime point, measuring how strongly that channel is participated in. Bandwidth is *additive* across disjoint channels (a chain participating in two disjoint channels has total bandwidth equal to the sum). This additivity is a primitive structural fact, not a derived one.
- **Polarity $\pi_K(x,t)$.** A primitive $U(1)$-valued angular quantity on each channel at each spacetime point, encoding the orientation of the local participation flow relative to the chain's rule. Polarity is the *unique* primitive-level angular variable in the substrate.
- **Commitment.** A discrete event at which a chain's participation is reduced to a single channel. Commitment is the substrate-level mechanism that produces probability-like outcomes in observation.
- **Amplitude carrier.** The mathematical object the substrate must supply so that bandwidth and polarity, taken together, can support interference, composition, and the standard Hilbert-space machinery. *The identification of this object is the subject of this paper.*

These six terms are sufficient for §§5–9. Definitions for the remaining substrate vocabulary, including the full primitive stack, appear in Appendix A.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying the following five primitive conditions. Each is a structural fact about the substrate at the pre-quantum level; none assumes complex numbers, Hilbert spaces, the Born rule, or any downstream quantum-mechanical structure.

### C1. Participation indexing (Primitive P03 + P07)

The substrate supplies a participation relation with a discrete index set $\mathcal{K}$ of channels and a (discrete or continuous) index set of spacetime locations. The amplitude carrier is to be a quantity defined on the product of these index sets:
$$
P : \mathcal{K} \times \text{spacetime} \to \mathcal{A}
$$
for some carrier algebra $\mathcal{A}$ to be determined. The substrate fixes the *domain* but not the *codomain* $\mathcal{A}$.

### C2. Bandwidth (Primitive P04)

The substrate supplies a non-negative real-valued bandwidth function on each channel:
$$
b_K(x, t) \in \mathbb{R}_{\geq 0}.
$$
Bandwidth satisfies a kinematic additivity property: if channel $K$ decomposes into disjoint sub-channels $K = K_1 \sqcup K_2$, then
$$
b_K = b_{K_1} + b_{K_2}.
$$
This additivity holds at the substrate level. It is *not* a derived property of probabilities; it is a primitive structural fact about how participation aggregates across disjoint channels.

### C3. Polarity (Primitive P09)

The substrate supplies a $U(1)$-valued angular variable on each channel:
$$
\pi_K(x, t) \in U(1) \cong S^1.
$$
Polarity is the unique $U(1)$-valued angular variable in the primitive stack. No other primitive supplies an angular quantity. (This unique-source property is a primitive-level audit fact about the substrate; see Appendix A.)

### C4. Commitment events (Primitive P11)

The substrate supports discrete commitment events at which a chain's participation across multiple channels collapses to a single channel. The probability rule for which channel is selected is *not* required as input to this paper; it is the content of Paper #2. What C4 supplies is the *existence* of commitment as a substrate-level mechanism — needed to ensure that the amplitude carrier must be a quantity from which a probability-like rule can be extracted at all.

### C5. No additional inputs

This paper invokes only C1-C4 plus the following standard mathematical infrastructure:

- The Frobenius classification of finite-dimensional associative real division algebras (Frobenius 1878).
- The polar decomposition theorem on $\mathbb{C}$.
- The classification of continuous group homomorphisms $U(1) \to U(1)$ as integer windings.
- The Cauchy functional equation: continuous non-negative solutions of $f(a+b) = f(a)+f(b)$ are linear.
- The classification of $U(1)$-invariant non-negative real-valued functions on $\mathbb{C}$ as functions of $|z|^2$.

No quantum-mechanical structure (Born rule, Hilbert space, Schrödinger equation, Bell inequality, Heisenberg inequality) appears as an input. No additional primitives beyond P03, P04, P07, P09, P11 are used. The forcing argument is closed against circularity.

---

## 6. Alternative Encodings

The forcing argument requires an explicit enumeration of the alternatives to be excluded. This section lists them. §7 shows that the participation measure satisfies $\{C\}$ constructively. §8 dispatches each alternative.

### 6.1 Structural alternatives

These are abstract mathematical alternatives for the amplitude carrier, defined without reference to existing physical frameworks.

**A1. Real-valued amplitudes.** The carrier algebra is $\mathbb{R}$. Each channel carries a real number $P_K \in \mathbb{R}$, with bandwidth identified as $|P_K|^p$ for some exponent $p$. Phase content, if present, would be stored as a separate degree of freedom $\theta_K$ — for instance, a sign $\pm 1$, or a discrete $\mathbb{Z}_n$ variable, or a separate continuous angle paired with the real amplitude as a tuple $(r, \theta) \in \mathbb{R} \times S^1$.

**A2. Quaternion-valued amplitudes.** The carrier algebra is the quaternions $\mathbb{H}$. Each channel carries a quaternion $P_K \in \mathbb{H}$, with bandwidth identified as $|P_K|^2 = P_K \bar{P}_K$ (the standard quaternionic norm) and phase content given by the $SU(2)$ structure of unit quaternions.

**A3. Signed measures.** The carrier is a real-valued quantity that can take negative values, with bandwidth identified as $|P_K|$ or $P_K^2$. Phase content is reduced to a binary sign $\pm 1$.

**A4. Phase-only encodings.** The carrier is a pure $U(1)$ variable $\theta_K(x,t) \in S^1$, with bandwidth either constant or stored externally as a separate real-valued field.

**A5. Non-quadratic magnitude exponents.** The carrier is complex-valued $P_K \in \mathbb{C}$ with polar form $P_K = r_K e^{i\theta_K}$, but with bandwidth identified as $|P_K|^\alpha$ for some exponent $\alpha \neq 2$. The exponent could be 1 (linear-amplitude rule), 4 (quartic rule), or any non-integer or non-positive real.

**A6. Non-$U(1)$ phases.** The carrier is complex-valued, but the phase is taken modulo a different group structure. Examples: $\mathbb{Z}_n$ discrete phases (phase rotates by integer multiples of $2\pi/n$); $\mathbb{R}$-valued non-periodic phases (no closure of the phase circle); $U(n)$ for $n > 1$ (non-abelian phase content).

**A7. Multivalued or non-unique phases.** The carrier admits multiple phase assignments at the same point — for instance, branched covers of the phase circle, or fractional phases such as those produced in anyonic statistics.

### 6.2 Mainstream attempts

These are alternatives drawn from the existing literature on quantum foundations, included in the enumeration because a reader familiar with the field will want to see them addressed. Each is treated under the substrate-conditions test in §8.

**B1. Bohmian / pilot-wave theory.** The amplitude carrier is the standard complex-valued $\psi(x)$, supplemented by hidden trajectories $X(t)$ guided by the phase gradient. The complex-valued structure is *taken as given* in this framework; it is not derived.

**B2. GRW / CSL collapse theories.** The amplitude carrier is the standard complex-valued $\psi(x)$, supplemented by a stochastic collapse mechanism. As with Bohmian theory, the complex-valued structure is taken as given.

**B3. QBism / $\psi$-epistemic interpretations.** The carrier $\psi$ is interpreted not as a property of a physical system but as a degree-of-belief state of an agent. The complex-valued structure is again *not derived*; it is taken as a feature of the epistemic representation, justified by Dutch-book arguments or coherence conditions.

**B4. Madelung hydrodynamics.** The wavefunction is rewritten as $\psi = \sqrt{\rho}\,e^{iS/\hbar}$, treating $\rho$ and $S$ as primary. This is a *reformulation* of the standard complex-valued state, not a different carrier — the polar decomposition is equivalent to the complex form. As an alternative carrier, Madelung makes no independent commitment; it inherits whatever structure the underlying $\psi$ has.

**B5. Real-vector-space quantum mechanics (Stueckelberg 1960).** All amplitudes are real-valued vectors in $\mathbb{R}^n$, with the imaginary unit replaced by an auxiliary operator $J$ satisfying $J^2 = -1$. The construction works mathematically but introduces a superselection rule (the $J$-invariant subspace) that is structurally equivalent to a complex Hilbert space. Either Stueckelberg's $J$-operator is identified with multiplication by $i$ (reducing to standard complex QM — the forced answer) or it is hidden behind a superselection rule (which is content not present in the substrate conditions). See §8.

**B6. Quaternionic quantum mechanics (Adler 1995).** Amplitudes are quaternion-valued. This is the developed-literature version of A2. Adler's program shows that the construction is internally consistent for single-particle non-relativistic systems but produces structural pathologies (tensor-product anomalies, problems with multi-particle composition) in many-body settings. We address A2 = B6 directly in §8.

---

## 7. Constructive Necessity

Before excluding alternatives, we verify that the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ actually satisfies the substrate conditions $\{C\}$ and produces a coherent amplitude carrier. This is the positive half of the forcing theorem.

### 7.1 Definition

Define the **participation measure** as the complex-valued function on the product of channel index and spacetime,
$$
P_K(x, t) := \sqrt{b_K(x, t)} \cdot e^{i \pi_K(x, t)} \in \mathbb{C},
$$
where $b_K(x, t)$ is the substrate-level bandwidth (C2) and $\pi_K(x, t)$ is the substrate-level polarity (C3). The square root is the standard non-negative real square root; the exponential is the standard complex exponential.

### 7.2 Satisfaction of C1 (indexing)

The function $P_K(x, t)$ is well-defined on $\mathcal{K} \times \text{spacetime}$. The codomain is $\mathbb{C}$. C1 is satisfied.

### 7.3 Satisfaction of C2 (bandwidth)

By construction, $|P_K|^2 = b_K$. Bandwidth additivity over disjoint channels is preserved: if $K = K_1 \sqcup K_2$ with orthogonal participation contributions, then the squared modulus of the sum decomposes as
$$
|P_{K_1} + P_{K_2}|^2 = |P_{K_1}|^2 + |P_{K_2}|^2 + 2\,\text{Re}(P_{K_1}^* P_{K_2}).
$$
The cross-term vanishes when the two channel contributions are orthogonal under the inner product on $\mathbb{C}$ — that is, when they participate in disjoint phase regions, which is the substrate-level meaning of "disjoint channels." Bandwidth additivity is reproduced. C2 is satisfied.

### 7.4 Satisfaction of C3 (polarity)

By construction, $\arg(P_K) = \pi_K \in U(1)$. The phase factor is exactly the substrate-level polarity. C3 is satisfied.

### 7.5 Satisfaction of C4 (commitment compatibility)

The participation measure provides a non-negative quantity $|P_K|^2 = b_K$ on each channel. This quantity is structurally available as the weight for commitment-event probability extraction. Whether $|P_K|^2$ is the correct probability weight (the Born rule) is the content of Paper #2; the present requirement is only that the carrier supports a probability-like extraction at all, which it does. C4 is satisfied.

### 7.6 Well-posedness

The square root $\sqrt{b_K}$ is well-defined and unique because $b_K \geq 0$ (C2). The complex exponential $e^{i\pi_K}$ is well-defined and continuous on $U(1)$. The product is a well-defined element of $\mathbb{C}$ with modulus $\sqrt{b_K}$ and argument $\pi_K$. The construction is pointwise — there is no integrability or convergence question at this stage.

### 7.7 Existence

The participation measure exists for any substrate satisfying $\{C\}$. There is no obstruction. The construction is explicit. The forcing argument's positive half is complete.

What remains is the negative half: showing that no other carrier survives.

---

## 8. Exclusion Arguments

This section dispatches each alternative encoding listed in §6. The pattern is uniform: for each alternative, we identify the substrate condition it violates, the structural fact it cannot reproduce, or the surplus content it requires that the substrate does not supply.

### 8.1 A1 — Real-valued amplitudes

**Claim:** $\mathbb{R}$ is not viable as a carrier algebra for an amplitude that must carry $U(1)$-valued phase content.

**Argument.** The substrate supplies polarity $\pi_K \in U(1)$ as a primitive (C3). The carrier algebra $\mathcal{A}$ must support a faithful $U(1)$ action — that is, a continuous group homomorphism $\rho: U(1) \to \text{Aut}(\mathcal{A})$ that is injective. The automorphism group of $\mathbb{R}$ as a unital associative algebra is trivial (the identity only); as a real vector space, $\text{Aut}(\mathbb{R}) = \mathbb{R}^\times$, the nonzero reals under multiplication. The continuous group homomorphisms $U(1) \to \mathbb{R}^\times$ are classified: they are the trivial map and the sign character $\theta \mapsto \pm 1$. Neither is faithful.

The phase content of polarity cannot be carried by $\mathbb{R}$. C3 is violated.

**Tuple alternative.** One might attempt to evade this by storing the phase separately: let the carrier be the tuple $(r, \theta) \in \mathbb{R}_{\geq 0} \times U(1)$, with $r$ holding the amplitude and $\theta$ holding the phase. But this tuple is, by definition, the polar form of a complex number. The map $(r, \theta) \mapsto r e^{i\theta}$ is a bijection between $\mathbb{R}_{\geq 0} \times U(1)$ and $\mathbb{C}$. The tuple is *isomorphic to* $\mathbb{C}$ as a carrier — calling it "real-valued plus a separate phase" is a relabeling, not a genuinely distinct alternative.

Real-valued amplitudes either fail to carry the phase (violating C3) or are isomorphic to complex amplitudes (collapsing back to the forced answer). Excluded.

### 8.2 A2 / B6 — Quaternion-valued amplitudes

**Claim:** $\mathbb{H}$ is not viable as a carrier algebra because it has too much angular structure relative to what the substrate supplies.

**Argument.** The quaternions $\mathbb{H}$ have angular structure $SU(2)$, embedded as the unit quaternions $S^3 \subset \mathbb{H}$. This is a three-dimensional non-abelian Lie group, in contrast to the one-dimensional abelian $U(1)$.

The substrate supplies $U(1)$-valued polarity (C3) and *no other angular variable*. To use $\mathbb{H}$ as a carrier, one must do one of the following:

**Option B-1: Select a $U(1) \subset SU(2)$ embedding.** Pick a unit imaginary quaternion $\hat{u} \in S^2 \subset \mathbb{H}$ (the imaginary unit sphere) and let polarity rotate around $\hat{u}$: $\pi_K \mapsto e^{\pi_K \hat{u}}$. This gives a faithful $U(1)$ action. But the choice of $\hat{u}$ is unconstrained — any direction in $S^2$ gives a valid embedding, and the substrate provides no primitive-level basis for selecting one. The carrier is structurally underdetermined.

**Option B-2: Use the full $SU(2)$ structure.** Treat the quaternionic carrier as encoding non-abelian phase rotations beyond what polarity supplies. But then the carrier holds angular content that does not correspond to any primitive. Where does the extra structure come from? Not from any primitive in $\{C\}$. The carrier carries surplus structural content unsupported by the substrate.

Either way, $\mathbb{H}$ commits the framework to content beyond what C3 supplies. Excluded.

**On Adler's quaternionic QM.** Adler's program (1995) shows that quaternionic quantum mechanics is internally consistent for single-particle non-relativistic systems. But the consistency comes at the cost of additional structural choices (in particular, a fixed quaternionic phase convention across the entire system) that, under the substrate-conditions test, correspond exactly to selecting a $U(1) \subset SU(2)$ embedding — Option B-1 above. The Adler construction is mathematically consistent but structurally underdetermined relative to a substrate that supplies only $U(1)$ polarity.

### 8.3 A3 — Signed measures

**Claim:** A real-valued carrier admitting negative values can store only a $\mathbb{Z}_2$ phase, not a full $U(1)$ phase. Excluded by C3.

**Argument.** A signed measure $P_K \in \mathbb{R}$ has phase content reduced to the sign $\text{sgn}(P_K) \in \{+1, -1\}$. The substrate-level polarity $\pi_K \in U(1)$ is a continuous angular variable taking values in an uncountable set. The map $\pi_K \mapsto \text{sgn}(P_K)$ is a non-injective surjection onto $\{+1, -1\}$, losing almost all phase information.

Equivalently: signed measures admit only a $\mathbb{Z}_2$ faithful action ($P_K \to \pm P_K$). The full $U(1)$ is not faithfully represented. C3 is violated.

### 8.4 A4 — Phase-only encodings

**Claim:** A pure $U(1)$ carrier $\theta_K \in S^1$ cannot reproduce bandwidth content. Excluded by C2.

**Argument.** A pure phase variable $\theta_K \in S^1$ has no magnitude. The substrate supplies bandwidth $b_K \in \mathbb{R}_{\geq 0}$ as a primitive (C2). To reproduce the bandwidth additivity property $b_K = b_{K_1} + b_{K_2}$ from $\theta_K$ alone is impossible: $\theta_K$ takes values in a compact group with no additive structure that respects bandwidth additivity.

The only way to keep a phase-only carrier and still represent bandwidth is to store bandwidth externally — as a separate real-valued field. But then the amplitude carrier is the *pair* $(\theta_K, b_K)$, which by the same argument as in 8.1 is isomorphic to the complex polar form $\sqrt{b_K}\,e^{i\theta_K}$. The phase-only alternative collapses back to the forced answer.

### 8.5 A5 — Non-quadratic magnitude exponents

**Claim:** The exponent in $|P_K|^\alpha = b_K$ is forced to $\alpha = 2$ by the joint action of C2 (bandwidth additivity), C3 ($U(1)$ invariance), and the Cauchy functional equation.

**Argument.** Suppose the carrier is complex-valued $P_K \in \mathbb{C}$ with $P_K = r_K e^{i\theta_K}$ and bandwidth identified as
$$
b_K = c \cdot |P_K|^\alpha = c \cdot r_K^\alpha,
$$
for some exponent $\alpha > 0$ and normalization $c > 0$. We show $\alpha = 2$.

Let $Q : \mathbb{C} \to \mathbb{R}_{\geq 0}$ be the function supplying bandwidth, $Q(P_K) = b_K$. Three constraints:

**(i) Non-negativity.** $Q(z) \geq 0$ for all $z \in \mathbb{C}$. From C2.

**(ii) $U(1)$ invariance.** Bandwidth does not depend on the phase: $Q(e^{i\alpha} z) = Q(z)$ for all $\alpha \in U(1)$. From C3, which fixes phase as an independent variable not contributing to bandwidth.

By (ii), $Q$ is a function of $|z|$ alone (the unique $U(1)$-invariant on $\mathbb{C}$). Write $Q(z) = f(|z|^2)$ where $f : \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$. The choice of $|z|^2$ rather than $|z|$ as the argument of $f$ is for convenience; the substantive constraint will pin down $f$.

**(iii) Bandwidth additivity.** From C2: when channels $K$ and $K'$ decompose orthogonally, $b_{K \cup K'} = b_K + b_{K'}$. At the level of carriers, this corresponds to $|P_{K \cup K'}|^2 = |P_K|^2 + |P_{K'}|^2$ (the Pythagorean structure of orthogonal complex vectors). Substituting:
$$
f(|P_K|^2 + |P_{K'}|^2) = f(|P_K|^2) + f(|P_{K'}|^2).
$$
This is the Cauchy functional equation on $\mathbb{R}_{\geq 0}$. Continuous non-negative solutions are linear: $f(x) = c \cdot x$ for some $c > 0$.

Therefore $Q(z) = c |z|^2$, so $b_K = c |P_K|^2$. Choosing $c = 1$ is a unit convention. The exponent is forced to $\alpha = 2$.

**Alternative-exponent failure.** If $\alpha \neq 2$, the additivity constraint becomes
$$
(|P_K|^2 + |P_{K'}|^2)^{\alpha/2} = |P_K|^\alpha + |P_{K'}|^\alpha.
$$
By the Minkowski/Power-Mean inequality, this holds with equality only when $\alpha/2 = 1$, i.e., $\alpha = 2$. For $\alpha > 2$ the LHS is strictly greater (super-additive); for $\alpha < 2$ strictly less (sub-additive). In both cases the substrate-level additivity is violated.

The exponent 2 is forced. No other exponent satisfies C2.

### 8.6 A6 — Non-$U(1)$ phases

**Claim:** The phase group is forced to be $U(1)$ by C3, which specifies polarity as $U(1)$-valued at the primitive level.

**Argument.** This is essentially immediate from C3. The substrate primitive supplying angular content is polarity, with values in $U(1)$. Alternative phase groups would require a *different* primitive supplying the alternative angular structure.

**Subcase: $\mathbb{Z}_n$ discrete phases.** A discrete phase $\theta_K \in \mathbb{Z}_n$ takes values in a finite cyclic group of order $n$. This is a proper subgroup of $U(1)$ (specifically, the $n$-th roots of unity). To use $\mathbb{Z}_n$ as the phase group is to *restrict* polarity to a discrete subset of its primitive range. There is no primitive-level basis for this restriction; C3 supplies the full $U(1)$.

Furthermore, downstream the discrete-phase carrier fails to support Stone's theorem applied to continuous symmetries (used in deriving the Schrödinger equation in Paper #4), since Stone's theorem requires a strongly continuous one-parameter unitary group. A $\mathbb{Z}_n$ phase group cannot host such a group.

**Subcase: $\mathbb{R}$-valued non-periodic phases.** A non-periodic phase $\theta_K \in \mathbb{R}$ without identification $\theta \sim \theta + 2\pi$ does not close into a circle. C3 specifies that polarity is $U(1)$-valued — meaning periodic. A non-periodic carrier carries more information than polarity supplies, and there is no primitive supporting the additional content.

**Subcase: $U(n)$ for $n > 1$.** Non-abelian phase content corresponds to angular structure on $SU(n)$ or $U(n)$ for $n > 1$. This is the same problem as A2/quaternions: too much angular structure relative to what the substrate supplies. Excluded by the same argument as 8.2.

### 8.7 A7 — Multivalued or non-unique phases

**Claim:** A multivalued phase assignment violates the well-posedness of the polarity primitive (C3) and introduces structure not present in the substrate.

**Argument.** Polarity $\pi_K(x, t)$ is single-valued at each $(K, x, t)$ by C3. A multivalued phase carrier admits, at the same point, multiple phase assignments — for instance, a branched cover with $\theta_K$ and $\theta_K + 2\pi/3$ both valid. Such a structure carries content beyond what polarity supplies: which branch is selected, and how branches connect across the substrate, are additional structural commitments not present in the substrate primitives.

Anyonic statistics (fractional braiding phases) live in two spatial dimensions, where the configuration-space topology supports them. In 3+1 dimensions — which is the dimensionality the ED substrate forces by separate argument (Paper-series item: NS-1, B2 closure) — the configuration space of $n$ identical particles is simply connected modulo the standard $\mathbb{Z}_2$ exchange, and only bosonic and fermionic statistics survive. The substrate provides no primitive supporting multivalued phase content in 3+1 dimensions.

### 8.8 B1-B3 — Bohmian / GRW / QBism

**Claim:** These programs do not derive the amplitude carrier; they take it as given. Therefore they do not satisfy the substrate-conditions test, which requires that the carrier be derived from $\{C\}$.

**Argument.** All three programs adopt the standard complex-valued $\psi(x)$ as their starting object. Bohmian theory supplements it with hidden trajectories; GRW supplements it with stochastic collapse; QBism reinterprets it epistemically. *None* of them addresses the question "why is $\psi$ complex-valued with squared-modulus probability?" — each begins with that structure in hand.

Therefore, with respect to the forcing question in this paper, these programs are *consumers* of the participation-measure structure, not alternatives to it. If the substrate forces the complex-valued participation measure, then Bohmian, GRW, and QBism all become interpretive overlays on the same forced carrier. They take side in a different debate (about hidden variables, collapse, and the epistemic vs. ontic status of $\psi$) — not in this one.

This is not a dismissal of these programs. It is an observation that they are not in the alternative-encodings space; they live downstream of it.

### 8.9 B4 — Madelung hydrodynamics

**Claim:** Madelung is a reformulation of complex $\psi$, not an alternative carrier.

**Argument.** The Madelung decomposition writes $\psi(x) = \sqrt{\rho(x)}\,e^{iS(x)/\hbar}$ with $\rho$ and $S$ as the primary variables. This is mathematically equivalent to the polar decomposition of a complex number: $\rho$ is $|\psi|^2$ and $S$ is $\hbar \cdot \arg(\psi)$. The two representations carry the same information.

In fact, the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is *itself* the Madelung-form carrier, with $b_K$ playing the role of $\rho$ and $\pi_K$ playing the role of $S/\hbar$. The forcing argument of this paper can be read as a derivation of the Madelung form from substrate primitives. Madelung is not an alternative; it is the same object viewed in its polar coordinates.

### 8.10 B5 — Real-vector-space QM (Stueckelberg)

**Claim:** Stueckelberg's real-vector-space QM is structurally equivalent to standard complex QM, with the auxiliary $J$-operator playing the role of $i$.

**Argument.** Stueckelberg replaces $\psi(x) \in \mathbb{C}$ with $\Psi(x) \in \mathbb{R}^{2}$ (a two-component real vector) together with an operator $J$ acting on $\mathbb{R}^2$ satisfying $J^2 = -1$. The two-component real vector $\Psi$ is identified with the real and imaginary parts of $\psi$, and $J$ acts as multiplication by $i$. The construction is mathematically the standard complex Hilbert space rewritten in real-vector-space notation.

Under the substrate-conditions test: if $J$ is *not* identified with multiplication by $i$, then it is an additional structural commitment unsupported by primitives — i.e., where does $J$ come from? Not from any primitive in $\{C\}$. If $J$ *is* identified with multiplication by $i$, then we have reproduced standard complex QM, which is the forced answer.

Stueckelberg's program is consistent but not structurally distinct from the forced answer. It is, under any honest reading, complex quantum mechanics in real-vector notation.

### 8.11 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 $\mathbb{R}$ | C3 | No faithful $U(1)$ action; tuple form is $\mathbb{C}$ in disguise. |
| A2 / B6 $\mathbb{H}$ | C3 (over-supply) | $SU(2)$ surplus structure; $U(1) \subset SU(2)$ embedding underdetermined. |
| A3 signed measures | C3 | Only $\mathbb{Z}_2$ phase representable; loses full $U(1)$ content. |
| A4 phase-only | C2 | No bandwidth content; cannot represent magnitude. |
| A5 $\alpha \neq 2$ | C2 | Violates Cauchy additivity over disjoint channel decompositions. |
| A6 non-$U(1)$ phases | C3 | Wrong phase group; substrate supplies only $U(1)$. |
| A7 multivalued phases | C3 well-posedness | Surplus content unsupported by primitives; anyons forbidden in 3+1D. |
| B1-B3 Bohmian / GRW / QBism | not in space | Adopt the carrier as given; do not derive it from substrate. |
| B4 Madelung | reformulation | Polar decomposition of $\psi$; same object in different notation. |
| B5 Stueckelberg | collapses to forced | $J = i$ identification reduces to standard complex QM. |

**The participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

A forcing theorem is only worth stating if its claim is exposed — if there is some way the world could be that would refute it. This section identifies the exposure surfaces for the participation-measure forcing.

### 9.1 Structural falsifier

The most direct falsifier is structural: identify any substrate that satisfies the conditions $\{C\}$ of §5 — discrete channel indexing (C1), non-negative additive bandwidth (C2), $U(1)$-valued polarity (C3), and commitment events (C4) — but that admits a non-complex amplitude carrier surviving the exclusion arguments of §8.

If such a substrate exists, the forcing theorem is false. The argument of this paper would have a gap in §8 — some alternative encoding that we failed to address, or whose exclusion is incomplete.

The reader is invited to construct one. The author's claim is that the construction fails: every attempt either violates one of C1-C4 or is isomorphic to the complex participation measure under relabeling.

### 9.2 Substrate-condition falsifier

A different mode of falsification: show that the substrate conditions $\{C\}$ themselves are wrong — that bandwidth is *not* a non-negative additive primitive quantity, that polarity is *not* $U(1)$-valued, or that the substrate does *not* have the channel-indexed structure C1 specifies.

This is a falsifier of the ED program, not of this paper specifically. If the substrate primitives are wrong, then the conclusions drawn from them (including the participation measure) are correspondingly wrong. Whether the substrate primitives are right is a question for the larger program: the platform-bridge work (matter-wave interferometry, BEC dynamics, superconducting qubits), the empirical anchors (the Universal Mobility Law, the substrate-gravity transition acceleration), and the downstream forcing chain that runs from this paper through Born, Bell, Heisenberg, Schrödinger, gauge fields, kernel arrow, Dirac, DCGT, substrate gravity, and the black-hole-Hawking program.

### 9.3 Empirical exposure downstream

The forcing in this paper does not directly contact experiment; the participation measure as a kinematic object is observationally identical to the standard wavefunction. What contacts experiment is the *cascade* this paper enables.

Three immediate exposures:

**Born rule (Paper #2).** The squared-modulus identity $|P_K|^2 = b_K$ forced by this paper plus Gleason-Busch reconstruction on the Hilbert space this paper enables produces the Born rule as a theorem, not a postulate. Any empirical situation in which probability rules are *not* quadratic in amplitude is therefore a falsifier of the participation measure (since the quadratic rule is forced).

**Bell-Tsirelson bound (Paper #3).** The sesquilinear inner product on the participation-measure space, which is forced jointly by the complex-valued carrier and the squared-modulus identity, produces the Tsirelson bound $|S| \leq 2\sqrt{2}$ as a theorem. Any experimentally established Bell-CHSH value above $2\sqrt{2}$ would falsify the forcing chain — and would falsify quantum mechanics generally, since Tsirelson's bound is empirically observed up to current precision.

**Schrödinger evolution (Paper #4).** Stone's theorem on the participation-measure Hilbert space forces a linear unitary one-parameter group as the time-evolution generator. Any experimentally established non-linear or non-unitary evolution at the kinematic level would falsify the forcing chain — including the modifications proposed by GRW, CSL, and other collapse theories at their characteristic regimes. (These programs are currently consistent with experiment because the modifications are too small to detect; the falsifier sits at the boundary of their experimentally accessible regime.)

### 9.4 The structural-versus-empirical balance

This paper sits at the upstream end of the forcing chain. Its falsifier is primarily structural: produce a substrate alternative that the exclusion arguments miss. The empirical exposure comes downstream, through papers #2-#4 and beyond. This is appropriate for a foundational uniqueness theorem: empirical content is what the chain *produces*, not what the chain *consumes*.

If the participation-measure forcing is right, every quantum prediction continues to hold — because the participation measure *is* the wavefunction, structurally derived. If the forcing is wrong — if some alternative carrier survives the exclusion arguments and is empirically realized — then the substrate primitives need to be reconsidered, and the forcing chain has to be rebuilt from a different starting point.

The participation measure is the substrate-side of "complex Hilbert space." Its uniqueness, given the substrate conditions, is the result this paper establishes.

---

## Appendix A — Full Derivation Chain and Glossary

This appendix contains:
- A.1: Step-by-step derivation of the four structural properties of the participation measure (carrier algebra, polar form, magnitude exponent, phase identification), with all mathematical infrastructure made explicit.
- A.2: Alphabetized glossary of ED substrate vocabulary.
- A.3: Source repository citations (for ED-internal readers; not required for cold-readability of the main paper).

### A.1 The forcing chain in detail

The forcing theorem of §2 decomposes into four structural properties, each derived independently.

**Property 1: Carrier algebra is $\mathbb{C}$.**

The carrier $\mathcal{A}$ must:
- Support faithful $U(1)$ action (from C3, polarity is $U(1)$-valued and must act on the carrier).
- Carry no surplus structural content unsupported by primitives.
- Be a finite-dimensional associative real algebra (so that arithmetic on the carrier is meaningful and tractable).

Frobenius's theorem (1878) classifies finite-dimensional associative real division algebras as $\{\mathbb{R}, \mathbb{C}, \mathbb{H}\}$. The wider class of finite-dimensional associative real algebras includes also matrix algebras over these three, but adding matrix structure introduces additional angular content unsupported by primitives — the same problem as A2.

- $\mathbb{R}$: no faithful $U(1)$ action ($\text{Aut}(\mathbb{R})$ admits only trivial and sign representations). Excluded.
- $\mathbb{H}$: $SU(2)$ angular structure exceeds the $U(1)$ polarity. Excluded.
- $\mathbb{C}$: faithful $U(1)$ action via multiplication by $e^{i\theta}$; angular structure exactly $U(1)$. Survives.

Therefore $\mathcal{A} = \mathbb{C}$ uniquely.

**Property 2: Polar decomposition $P_K = r_K \cdot e^{i\theta_K}$.**

Conditional on Property 1, this is the standard polar decomposition theorem on $\mathbb{C}$: every nonzero $z \in \mathbb{C}$ admits a unique representation $z = r e^{i\theta}$ with $r > 0$ and $\theta \in U(1)$ (modulo the global $U(1)$ gauge for $\theta$). At $z = 0$, the representation is $r = 0$ with $\theta$ undefined; this corresponds to vanishing bandwidth $b_K = 0$, a kinematically isolated case.

The polar decomposition introduces no new structural commitment beyond Property 1.

**Property 3: Magnitude exponent $|P_K|^2 = b_K$.**

Derived in §8.5. The function $Q: \mathbb{C} \to \mathbb{R}_{\geq 0}$ giving bandwidth from carrier satisfies:
- Non-negativity (C2)
- $U(1)$-invariance (C3)
- Additivity over orthogonal channel decompositions (C2)

The first two imply $Q(z) = f(|z|^2)$ for some $f: \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$. The third gives Cauchy's functional equation $f(a+b) = f(a)+f(b)$, whose continuous non-negative solutions are $f(x) = c \cdot x$. Choosing $c = 1$ by unit convention, $|P_K|^2 = b_K$.

The exponent 2 is unique. Alternative exponents fail the additivity constraint by the power-mean inequality.

**Property 4: Phase identification $\arg(P_K) = \pi_K$.**

The polar decomposition gives a phase $\theta_K \in U(1)$ associated with the carrier. The substrate supplies a $U(1)$-valued primitive, polarity $\pi_K \in U(1)$. Primitive enumeration of the ED substrate (P01-P13) confirms that polarity is the *unique* $U(1)$-valued primitive variable.

Could $\theta_K$ be a function of $\pi_K$ rather than equal to it? The continuous group homomorphisms $U(1) \to U(1)$ are classified as integer windings $\theta \mapsto n\theta$ for $n \in \mathbb{Z}$. A non-trivial winding $n \neq 1$ would require a primitive-level integer $n$ to be supplied; the substrate provides no such primitive. Adding a constant offset (so $\theta_K = \pi_K + \alpha$ for some $\alpha \in U(1)$) is the global gauge freedom, treated as a convention.

Therefore $\theta_K = \pi_K$ uniquely, up to the global $U(1)$ gauge convention.

**The composite result.** Combining Properties 1-4:
$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i\pi_K(x, t)}.
$$
Forced, up to the global phase convention and the unit-normalization of bandwidth.

### A.2 Glossary

- **Amplitude carrier.** The mathematical object the substrate must supply so that participation bandwidth and polarity can be combined into a single quantity supporting interference and Hilbert-space machinery. This paper establishes that the amplitude carrier is the complex-valued participation measure.
- **Bandwidth $b_K(x,t)$.** A primitive-level (P04) non-negative real-valued quantity on each channel at each spacetime point, additive across disjoint channel decompositions.
- **Chain.** A persistent sequence of micro-events in the substrate. Chains are the substrate-level analog of particles/systems; participation, bandwidth, polarity, and commitment are all properties of chains.
- **Channel.** A primitive (P07) structural pathway in the participation graph, indexed by a label $K$. The discrete index set of channels is $\mathcal{K}$.
- **Commitment.** A primitive (P11) discrete event at which a chain's participation across multiple channels collapses to a single channel. Commitment is the substrate-level mechanism producing observed probabilities.
- **Event Density (ED).** The framework within which this paper is written. ED's substrate is a graph-like structure of primitive participation relations, equipped with the primitive scalar quantities listed in this glossary. The substrate is not a Hilbert space, not a manifold, not a quantum field theory.
- **FORCED.** A theorem-grade structural result derived from substrate primitives and standard mathematics, with no additional structural commitments. Contrasts with INHERITED (a value or coefficient not derived in the present paper) and OUT OF SCOPE (a claim explicitly not made).
- **INHERITED.** A quantitative content (value, coefficient, normalization) used in the paper but not derived in it. Typically traces to a different primitive, an empirical anchor, or a unit convention.
- **Participation graph.** The graph-like structure underlying the ED substrate: vertices are micro-event sites, edges are participation relations, and the channel index $K$ labels structural pathways.
- **Participation measure.** The complex-valued object $P_K(x,t) = \sqrt{b_K(x,t)}\,e^{i\pi_K(x,t)}$ derived in this paper as the unique amplitude carrier consistent with substrate conditions $\{C\}$.
- **Polarity $\pi_K(x,t)$.** A primitive-level (P09) $U(1)$-valued angular variable on each channel at each spacetime point, the unique angular variable in the substrate primitive stack.
- **Primitive.** A structural commitment of the ED framework not derived from anything more upstream. The substrate is built from 13 primitives (P01-P13); this paper uses P03, P04, P07, P09, P11.
- **Substrate.** The pre-quantum layer of structure underlying the ED framework. Not a Hilbert space; not a manifold; not a field theory. The substrate is built from primitives and supports the participation graph, bandwidth, polarity, and commitment.
- **Substrate conditions $\{C\}$.** The minimal set of substrate properties required for the forcing theorem of this paper: C1 indexing (P03+P07), C2 bandwidth (P04), C3 polarity (P09), C4 commitment (P11).

### A.3 Source-repository citations (for ED-internal readers)

For readers with access to the Event Density research repository, the following internal sources contain extended technical content underlying this paper:

- `papers/U1_Participation_Measure/paper_u1_participation_measure.md` — the original publication-grade derivation, predecessor genre (foundational-theorem paper rather than standalone forcing paper).
- `arcs/U1/04_closure_and_summary.md` — the U1 arc closure memo, with full derivation chain and downstream-cascade analysis.
- `arcs/U1/00_arc_outline.md` through `arcs/U1/03_F1_F3_and_verdict.md` — the four-memo derivation arc.
- `theorems/T14.md` — theorem-level index entry; status FORCED-unconditional, ratified 2026-04-26.
- `arcs/arc-foundations/participation_measure.md` — the original Step-1 definitional memo that the U1 arc was opened to audit.

These sources are *not* required reading for the present paper, which is designed to be self-contained. They are listed here for ED-internal cross-reference and for any future reader who wishes to verify the derivation against the program's full technical record.

---

## Appendix B — On the Series

This is Paper #1 of a planned first-wave series of standalone forcing papers, each addressing one major Event Density result in the structure laid out by the 10-section template used in this paper. The remaining nine papers, in logical order:

2. **The Born Rule from Substrate Primitives.** Gleason-Busch reconstruction on the participation-measure Hilbert space.
3. **Sesquilinear Inner Product and the Bell-Tsirelson Bound.** Composition rule for participation measures; the $2\sqrt{2}$ ceiling.
4. **The Schrödinger Equation as the Only Survivor.** Stone's theorem on time-translation symmetry; exclusion of non-linear and stochastic alternatives.
5. **Gauge Fields Are Not Fundamental.** The substrate-level derivation of $D_\mu = \partial_\mu + igA_\mu^a T^a$ as participation-measure of rule-type.
6. **The V1 Kernel and the Arrow of Time.** Retarded support of the vacuum memory kernel; the structural origin of temporal asymmetry.
7. **The Dirac Equation Falls Out — and So Does $g = 2$.** First-order Lorentz-invariant spinor PDE forced by substrate conditions.
8. **DCGT: The Substrate-to-Continuum Bridge.** The diffusion coarse-graining theorem unlocking classical-field-theory applications.
9. **Newton's $G$ Is a Theorem: $G = c^3\ell_P^2/\hbar$.** Plus the transition acceleration $a_0 = cH_0/(2\pi)$ and the slope-4 baryonic Tully-Fisher relation.
10. **Black-Hole Architecture and Hawking Radiation from Substrate.** Capstone: horizons as decoupling surfaces, information blocking without paradox, Hawking spectrum from substrate-Unruh.

Each paper in the series uses the same 10-section template:

1. Framing
2. Claim
3. Scope (FORCED / INHERITED / OUT OF SCOPE)
4. Key vocabulary
5. Substrate class $\{C\}$
6. Alternative encodings $\{A, B, C, \ldots\}$
7. Constructive necessity
8. Exclusion arguments
9. Falsifiers and empirical exposure
10. Appendix: derivation chain + glossary

The template enforces the forcing-paper genre: claim, substrate, alternatives, exclusion, uniqueness. Each paper stands alone. The series, read in order, exhibits the dependency structure of the forcing chain; read individually, each paper is self-contained.

---

*End of Paper #1.*
