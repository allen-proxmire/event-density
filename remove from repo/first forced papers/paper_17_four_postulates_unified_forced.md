# The Four Postulates of Quantum Mechanics Are Unified and FORCED by the Participation Measure

**Paper #17 of the Event Density Forcing Series (Wave 2, Paper 7)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #17 of the program
**Genre:** Synthesis / forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

Standard quantum mechanics is built on four logically independent postulates: state space, dynamics, measurement, and composition. This paper shows that, **given the full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$ together with the four-band partition (P04 §1.5) and the participation-measure result of Paper #1**, all four postulates arise jointly and uniquely from a single substrate object — the participation measure $P_K(u) = \sqrt{b_K(u)} \cdot e^{i\pi_K(u)}$ — together with its associated substrate-level primitives. The unification is structural rather than rhetorical: two foundational substrate-level identities — the squared-modulus identity $|P_K|^2 = b_K$ and the joint symmetry-and-partition content (time + spatial homogeneity, four-band orthogonality, commitment events) — together force all four postulates as facets of one structure. Mainstream axiomatic and reconstruction programs (Dirac-von Neumann, Hardy 2001, Masanes-Müller 2011, Chiribella-D'Ariano-Perinotti, Coecke-Kissinger, QBism, GPT) are compared substantively, with ED's distinguishing features located in *(i)* the substrate-level origin of the Hilbert-space arena (vs. operational reconstruction taking the arena as given), and *(ii)* the structural rather than postulational character of the four-postulate unification. **The honest framing**: ED is a substrate-ontology + reconstruction program. The "four postulates" of standard QM are unified at the substrate level, but the substrate primitives that do the unifying (especially P04, P09, P11, P13, and the four-band partition) are themselves load-bearing inputs, not consequences of this paper. Why those specific primitives — and not others — is the subject of the Primitive-Forcing Meta-Paper.

---

## 1. Framing

### 1.1 The four standard QM postulates

Every graduate textbook in quantum mechanics presents the framework as a list of four foundational postulates:

1. **State space.** The state of a quantum system is a vector $|\psi\rangle$ in a complex separable Hilbert space $\mathcal{H}$, with $\|\psi\| = 1$. Equivalently, for mixed states, a positive trace-class operator (density operator) $\rho$ with $\text{Tr}(\rho) = 1$.

2. **Dynamics.** The state evolves in time according to the Schrödinger equation
$$
i\hbar\,\frac{d}{dt}|\psi(t)\rangle = \hat{H}\,|\psi(t)\rangle,
$$
with $\hat{H}$ a self-adjoint Hamiltonian operator.

3. **Measurement.** Measurement of an observable corresponding to a self-adjoint operator $\hat{A}$ with eigenstates $|a_i\rangle$ and eigenvalues $a_i$ yields outcome $a_i$ with probability $|\langle a_i \mid \psi\rangle|^2$ (the Born rule).

4. **Composition.** The state space of a joint system is the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$ of the subsystems' state spaces, with joint states represented as elements of this tensor product.

In the standard presentation, these four postulates are *logically independent*. Each is a separate structural commitment; the framework is built by adopting all four simultaneously.

### 1.2 Why their independence is a puzzle

The axiomatic presentation has obvious advantages: it isolates the framework's structural commitments, makes them subject to independent test, and supports systematic generalization (e.g., replacing $\mathbb{C}$ with $\mathbb{R}$ or $\mathbb{H}$ to study modified frameworks).

But the independence is also a *puzzle*. Three sub-questions:

1. **Why these four specifically?** A theory could in principle have three postulates, or five, or fifteen. The number "four" reflects how the framework was historically discovered, not a structural fact about the underlying world.

2. **Why these specific forms?** Why complex rather than real or quaternionic state space? Why linear-and-unitary dynamics rather than nonlinear? Why quadratic measurement rule rather than linear or cubic? Why tensor product rather than Cartesian product?

3. **Are they really independent?** Several mainstream programs (Hardy 2001, Masanes-Müller 2011, Chiribella et al.) show that *given some of the postulates plus operational/information-theoretic axioms*, the others follow. This suggests the four are not as independent as the axiomatic presentation claims — but the analyses operate within a framework that already assumes a Hilbert-space-like or GPT-like setting.

A deeper question: is there a *non-postulational* substrate from which all four postulates jointly emerge? If so, the appearance of four independent axioms is an artifact of the presentation; the underlying world has *one* structural commitment, viewed through the four postulates as four facets.

### 1.3 What this paper does

Papers #1-#16 of the Event Density (ED) Forcing Series have individually established each of the four postulates as a substrate-level FORCED result, each derived from a small set of substrate primitives. The present paper makes the unification *explicit*: all four are facets of a single substrate object — the **participation measure** $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ — together with its associated substrate-level primitives (bandwidth, polarity, channels, commitment, four-band partition).

The synthesis runs through two structural pillars:

**Pillar 1**: The **squared-modulus identity** $|P_K|^2 = b_K$ (Paper #1) is the substrate-level fact that:
- Forces the complex state-space carrier (because $b_K$ must be real and non-negative, while the substrate has $U(1)$ polarity, so the carrier must be $\mathbb{C}$).
- Forces the Born rule's quadratic form (because $|P_K|^2$ is the substrate quantity that gets averaged at commitment).
- Forces the $U(1)$ gauge redundancy (because the squared modulus is phase-invariant).
- Forces the Heisenberg uncertainty's $\hbar/2$ bound (because $|P_K|^2$ enters bandwidth-spread inequalities with the Fourier-transform's $\hbar$-normalization).

**Pillar 2**: The **substrate's symmetry-and-partition content** — time homogeneity (P13), spatial homogeneity (P03 + P06), four-band partition (P04 §1.5), commitment events (P11) — is the substrate-level fact that:
- Forces Schrödinger dynamics via Stone's theorem on time-translations (Paper #4) or via the thin-participation continuum limit (Paper #13).
- Forces the momentum operator via Stone's theorem on spatial translations (Paper #12).
- Forces the inner product via four-band orthogonality (Paper #3).
- Forces the kinetic operator via the adjacency-bandwidth partition (Papers #6, #15).
- Forces the operational Born rule via commitment-event phase-randomization (Paper #14).
- Forces the tensor-product composition via bipartite participation measures (Paper #3 §7.2).

Together, the two pillars force all four postulates jointly. The "four postulates" of standard QM are *four facets of one substrate object*, and recognizing the unification is one of the program's central rhetorical claims.

**Series context.** This is the Wave 2 synthesis paper. Papers #1-#16 establish individual forcings; the present paper makes their unification explicit and engages mainstream reconstruction programs (Dirac-von Neumann, Hardy, Masanes-Müller, Chiribella-D'Ariano-Perinotti, Coecke-Kissinger, QBism, GPT) at the structural level. After this, Wave 2 papers continue with extensions (specific QFT structures, classical-limit content, etc.), but the *foundational* substrate-level QM derivation is complete with the present synthesis.

---

## 2. Claim

> **Forcing Theorem (Unification of the Four QM Postulates, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$ + four-band partition (P04 §1.5) + participation-measure structure (Paper #1)*. Then the four standard QM postulates — state space, dynamics, measurement, composition — arise jointly and uniquely from the participation measure and its associated substrate primitives, via two foundational substrate-level identities:
> - **Pillar 1**: $|P_K|^2 = b_K$.
> - **Pillar 2**: substrate symmetry-and-partition content.
>
> *The substrate primitives are load-bearing; why those primitives (and not others) is upstream content (Primitive-Forcing Meta-Paper).*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated within the ED Generative Primitives System)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **The full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$:** each is doing load-bearing work in at least one of the four QM postulates.
- **P04 §1.5 (four-band partition):** load-bearing for inner-product orthogonality, kinetic structure, and adjacency-band uncertainty content.
- **Participation-measure structure ($|P_K|^2 = b_K$ from Paper #1):** load-bearing for the quadratic form of the Born rule, the global $U(1)$ gauge redundancy, and the Heisenberg $\hbar/2$ bound.

The full 13-primitive Generative Primitives System is enumerated in the ED Foundations position paper (*The Event Density Framework: A 13-Primitive Generative System and Its Cross-Domain Reach*). The empirical case for the primitives rests on their downstream reach across domains.

**This paper's substantive synthesis claim:** the four QM postulates, normally presented as logically independent, are *facets of one substrate object* — the participation measure $P_K(u) = \sqrt{b_K(u)} \cdot e^{i\pi_K(u)}$ — once the substrate primitives are in place. The unification is structural rather than rhetorical: two foundational substrate-level identities (the squared-modulus identity $|P_K|^2 = b_K$ and the joint symmetry-and-partition content) force all four postulates jointly. ED is best characterized as a **13-Primitive Generative System** whose downstream reach across QM kinematics, gravitational dynamics, soft-matter rheology, and black-hole architecture is the empirical case for the primitive set.

### 3.1 What is FORCED

The four standard QM postulates, jointly:

- **Hilbert-space state space** with complex amplitudes, sesquilinear inner product, and $U(1)$ phase redundancy.
- **Schrödinger dynamics** $i\hbar\,\partial_t\psi = \hat{H}\psi$ with linear, first-order, unitary structure and Hermitian generator.
- **Born rule** $\text{Prob}(K) \propto |P_K|^2$ with quadratic-in-amplitude form.
- **Tensor-product composition** $\mathcal{H}_A \otimes \mathcal{H}_B$ for joint bipartite systems, with bipartite participation measures supporting entangled states.

### 3.2 What is INHERITED

- **Numerical values** of $\hbar$, particle masses, coupling constants, and other empirical constants. Inherited from the Madelung anchoring + value-layer empirical content.
- **Physical identification of state-space basis vectors** with experimentally accessible eigenstates of specific observables.
- **Specific Hamiltonians** for particular systems. The form of $\hat{H}$ in general is forced (kinetic-plus-potential from Paper #6); the specific potential $V(x)$ for any given system is empirical.

### 3.3 What is OUT OF SCOPE

- **Relativistic QFT postulates** — Lorentz covariance, Wightman axioms, locality. Paper #7 covers the Dirac-equation extension; full QFT belongs to a separate sector.
- **Measurement-device modeling.** The substrate-level commitment primitive (P11) supplies the mechanism for measurement outcomes; modeling specific measurement devices (Stern-Gerlach apparatus, photon detectors, etc.) is a separate engineering problem.
- **Decoherence theory** as a foundational framework. The substrate-level phase-randomization mechanism (Paper #2 §7.1, Paper #14 §7.3) is *not* decoherence theory in the standard sense — it is a primitive substrate feature, not a derived consequence of system-environment Hamiltonian coupling.
- **Measurement-problem interpretation.** Whether commitment events are best understood as collapse, branching, or otherwise is a separate philosophical question.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum primitive layer of ED.
- **Participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$.** Complex amplitude carrier (Paper #1); the single substrate object from which all four postulates derive.
- **Squared-modulus identity.** $|P_K|^2 = b_K$ — the substrate-level fact that the squared modulus of the participation measure equals the bandwidth.
- **Bandwidth $b_K(u)$.** Primitive non-negative real-valued substrate quantity (P04); the substrate's primary physical content.
- **Polarity $\pi_K(u)$.** Primitive $U(1)$-valued angular substrate quantity (P09).
- **Four-band partition.** Substrate-level decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ (P04 §1.5).
- **Adjacency band.** Component of the four-band partition carrying kinematic content (Papers #11, #15).
- **Commitment event.** Discrete substrate-level event (P11) producing measurement outcomes.
- **Thin-participation limit.** Substrate-level continuum regime $M_\mathrm{eff} \to \infty$ where QM-like behavior emerges (Paper #13).
- **Joint participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$.** Bipartite extension of the single-system participation measure; supports tensor-product structure and entangled states (Paper #3 §7.2).
- **Two foundational identities.** Pillar 1 ($|P_K|^2 = b_K$) and Pillar 2 (substrate symmetry-and-partition content). The two substrate-level facts from which all four postulates jointly derive.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1-C5. Inherited substrate primitives

- **C1 (P03 + P07)**: participation graph with channels.
- **C2 (P04)**: non-negative bandwidth with four-band partition and additivity.
- **C3 (P09)**: $U(1)$-valued polarity primitive.
- **C4 (P11)**: commitment events with environmental phase-randomization.
- **C5 (P03 + P06 + P13)**: spatial and time homogeneity supplying translation symmetries.

### C6. Inherited results from Papers #1-#16

- **Paper #1**: participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ with $|P_K|^2 = b_K$.
- **Paper #2**: Born rule via Gleason-Busch.
- **Paper #3**: sesquilinear inner product + joint participation measure for bipartite systems + Tsirelson bound.
- **Paper #4**: Schrödinger equation via Stone's theorem on time-translations.
- **Paper #6**: Hamiltonian form $\hat{H} = \hat{p}^2/(2m) + V(\hat{x})$.
- **Paper #11**: Heisenberg uncertainty $\Delta x\,\Delta p \geq \hbar/2$.
- **Paper #12**: momentum operator $\hat{p} = -i\hbar\nabla$.
- **Paper #13**: Schrödinger as thin-participation continuum limit.
- **Paper #14**: Born rule via bandwidth-fraction.
- **Paper #15**: kinetic operator from adjacency-bandwidth partition.
- **Paper #16**: phase-independence of bandwidth → $U(1)$ gauge redundancy.

A reader who has not read Papers #1-#16 may take C6 as a definitional premise: the substrate carries the structures these papers establish.

### C7. No four-postulate axiomatization as input

The present paper does not assume the standard four-postulate axiomatization of QM. The argument shows that the four postulates emerge from C1-C5 + Paper-level inherited results, without taking them as separate inputs.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Four independent postulates.** The standard axiomatic presentation: state space, dynamics, measurement, and composition are *independent* structural commitments, with no shared substrate underpinning.

**A2. Real-valued participation measure.** Substrate carrier is real-valued, unforcing the complex Hilbert space, the Born rule's quadratic form, and the unitary dynamics. The four postulates would then be either modified or absent.

**A3. Nonlinear dynamics breaking unification.** Schrödinger equation replaced by a nonlinear evolution; the connection to the state-space linearity is broken.

**A4. Non-Born probability rule.** Probability map other than $|\psi|^2$; the connection to the bandwidth-fraction structure (Papers #2, #14) is broken.

**A5. Non-tensorial composition.** Joint-system state space is the Cartesian product $\mathcal{H}_A \times \mathcal{H}_B$ or some other non-tensorial construction, breaking the bipartite-participation-measure structure of Paper #3 §7.2.

**A6. No four-band partition.** Substrate lacks the internal / adjacency / environmental / commitment-reserve structure of P04 §1.5, unforcing the kinetic operator (Papers #6, #15), the Heisenberg uncertainty (Paper #11), and the inner-product orthogonality structure (Paper #3).

**A7. Phase-dependent bandwidth.** Bandwidth depends on phase content, breaking the $U(1)$ gauge redundancy of Paper #16 and unforcing the Born-rule phase-blindness.

**A8. Single-pillar unification (only Pillar 1 or only Pillar 2).** The substrate has only the squared-modulus identity, or only the symmetry-partition structure, but not both. The four-postulate unification would then be partial: some postulates would emerge, others would require independent axioms.

### 6.2 Mainstream alternatives

**B1. Dirac-von Neumann axiomatic QM.** Standard textbook presentation: four independent postulates. The substrate is silent; the framework is built by adopting axioms.

**B2. Hardy 2001 reconstruction.** Reconstructs QM from five "reasonable" operational axioms (information, simplicity, subspaces, composite systems, continuity). The reconstruction produces the four postulates jointly but takes the five operational axioms as input.

**B3. Masanes-Müller 2011 reconstruction.** Reconstructs QM from five operational axioms (different from Hardy's) emphasizing tomographic locality and continuous reversibility. Same general structure.

**B4. Chiribella-D'Ariano-Perinotti (CDP) information-theoretic reconstruction.** Reconstructs QM from six information-theoretic axioms (causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, purification). Purification is the load-bearing axiom.

**B5. Coecke-Kissinger categorical QM.** QM as a specific compact closed dagger category with biproducts. Categorical structural axioms taken as input.

**B6. QBism (Quantum Bayesianism).** QM postulates derived from agent rationality + coherence conditions; states as degrees of belief. Decision-theoretic substrate.

**B7. Generalized Probabilistic Theories (GPT).** QM as a specific point in the space of probabilistic theories satisfying additional structural axioms (state spaces as convex sets, effects as linear functionals, etc.). GPT framework taken as input.

---

## 7. Constructive Necessity

The argument is a structural synthesis of Papers #1-#16. The synthesis runs in three phases: §7.1 establishes Pillar 1 (squared-modulus identity) and its forcing reach; §7.2 establishes Pillar 2 (symmetry-partition content) and its forcing reach; §7.3 demonstrates how the two pillars jointly force all four postulates with shared substrate identities; §7.4 provides a worked example showing all four engaging simultaneously in a physical scenario.

### 7.1 Pillar 1: The squared-modulus identity and its forcing reach

The substrate-level identity
$$
|P_K(u)|^2 = b_K(u)
$$
is established in Paper #1 via a chain of structural arguments:

1. **Bandwidth $b_K$ is a non-negative real-valued substrate primitive** (Primitive P04). The substrate's primary physical content is bandwidth — the graded measure of participation.
2. **Polarity $\pi_K$ is a $U(1)$-valued angular substrate primitive** (Primitive P09). The substrate's angular content is the polarity phase.
3. **The participation measure must carry both**, in a single complex-valued object: $P_K(u) \in \mathbb{C}$. By Frobenius's classification of finite-dimensional associative real division algebras + the substrate's $U(1)$-only commitment, $\mathbb{C}$ is the unique carrier (real $\mathbb{R}$ fails to represent $U(1)$ faithfully; quaternionic $\mathbb{H}$ has $SU(2)$ surplus structure).
4. **The relationship between bandwidth and the complex carrier** is forced by three constraints: non-negativity of $b_K$ (C2), $U(1)$-invariance of $b_K$ (C3), and bandwidth additivity over disjoint channel decompositions (C2). The Cauchy functional equation on additivity yields $b_K = c|P_K|^2$ for some constant $c$; setting $c = 1$ is a normalization convention.

The identity $|P_K|^2 = b_K$ is *the* substrate-level structural fact about the participation measure. Pillar 1's forcing reach:

**Postulate 1 (state space)** — the carrier is $\mathbb{C}$ (Frobenius classification + $U(1)$ polarity), with $|P_K|^2$ as the real-valued bandwidth content. The state space's *complex* structure is forced.

**Postulate 3 (Born rule)** — outcome probabilities are bandwidth-fractions $b_K/\sum b_{K'}$; by the identity, these equal $|P_K|^2/\sum|P_{K'}|^2$. The Born rule's *quadratic* form is the same exponent 2 as in the squared-modulus identity.

**Postulate 1 (state space, phase-redundancy aspect)** — by Paper #16, bandwidth is $U(1)$-invariant: $|e^{i\theta}P_K|^2 = |P_K|^2 = b_K$. The state space's *projective* structure (physical states are rays, not vectors) is forced by the substrate-level phase-independence of bandwidth.

**Heisenberg uncertainty** — the $\hbar/2$ bound (Paper #11) emerges from the Cauchy-Schwarz inequality on bandwidth-weighted moments via the squared-modulus identity. The exponent 2 in $(\Delta x\,\Delta p)^2$ matches the exponent 2 in $|P_K|^2$.

**One identity, four consequences.** The complex state space, the quadratic Born rule, the $U(1)$ gauge redundancy, and the Heisenberg bound are not four independent facts. They are four downstream consequences of $|P_K|^2 = b_K$.

This is the substrate-level reason that *"why complex?", "why quadratic Born?", "why phase-independent?", and "why $\hbar/2$?"* have a single answer.

### 7.2 Pillar 2: Substrate symmetry-and-partition content

The substrate's symmetry-and-partition primitives jointly supply the dynamical, compositional, and observable structure of QM. Five primitive ingredients:

1. **Time homogeneity (P13)**: continuous time axis with substrate-level translation symmetry.
2. **Spatial homogeneity (P03 + P06)**: continuous spatial axis with substrate-level translation symmetry.
3. **Four-band partition (P04 §1.5)**: orthogonal decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$.
4. **Commitment events (P11)**: discrete substrate-level events with environmental phase-randomization producing outcomes.
5. **Channel-and-locus structure (P03 + P07)**: participation graph supporting bipartite extension.

Pillar 2's forcing reach:

**Postulate 2 (Schrödinger dynamics)** — via two independent routes:

(i) **Stone's theorem on time-translations** (Paper #4): time homogeneity (P13) supplies a strongly continuous one-parameter unitary group of time-translation operators on the participation manifold; Stone's theorem produces a unique self-adjoint generator $\hat{H}$; the differential form is $i\hbar\,\partial_t\Psi = \hat{H}\Psi$.

(ii) **Thin-participation continuum limit** (Paper #13): per-channel substrate dynamics $i\hbar\,\partial_t P_K = H_K P_K + \sum V_{KK'}P_{K'}$ (forced by bandwidth additivity + first-order time + complex coefficient), in the thin regime with momentum-basis identification $K \to k$ (Paper #12) and kinetic form $H_k = \hbar^2 k^2/(2m)$ (Paper #6 from Galilean Lie algebra), produces the Schrödinger PDE on the coherent-sum wavefunction.

The two routes converge: same equation, derived from different premises (Hilbert-space top-down vs. substrate-discrete bottom-up).

**Momentum operator (Paper #12)** — via Stone's theorem on spatial translations (P03 + P06): unique self-adjoint generator $\hat{p} = -i\hbar\nabla$.

**Heisenberg uncertainty (Paper #11)** — via the four-band partition (P04 §1.5) decomposed into Fourier-conjugate $b_x + b_p$ + Cauchy-Schwarz bandwidth-allocation inequality + Fourier-uncertainty theorem. The bound $\hbar/2$ emerges.

**Kinetic operator $\hat{T} = \hat{p}^2/(2m)$ (Papers #6, #15)** — via Galilean Lie algebra closure on bandwidth-flow + adjacency-bandwidth structure. The Laplacian form is forced.

**Inner product (Paper #3)** — via four-band orthogonality + $U(1)$-invariance + bandwidth additivity + Cauchy functional equation. The sesquilinear form $\langle P \mid Q\rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$ is forced.

**Postulate 4 (tensor-product composition)** — via bipartite participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$ on the product of subsystems' channel-locus indices. The tensor-product structure is forced by the substrate's *bilinear* extension to bipartite systems: joint states live on the Cartesian product of index spaces (channels and loci), and the natural carrier on the product is the tensor product of carriers.

**Postulate 3 (Born rule, operational route)** — via commitment-event environmental phase-randomization (P11) + post-decoherence diagonal mixture + bandwidth-fraction (Paper #14). The Born rule's *operational* form (long-run frequencies converge to $|P_K|^2/\sum|P_{K'}|^2$) is forced.

**Five primitives, six derived structures.** Pillar 2's primitive content (P03 + P04 + P11 + P13 + bipartite extension) jointly forces the Schrödinger dynamics, the momentum operator, Heisenberg uncertainty, the kinetic operator, the inner product, and the tensor-product composition — six structural results from five substrate primitives.

### 7.3 The unification

The two pillars together force all four QM postulates jointly:

**Postulate 1 (state space)** comes from Pillar 1 (complex carrier + Born quadratic + $U(1)$ redundancy) combined with Pillar 2 (inner product from four-band orthogonality). Both pillars contribute: Pillar 1 fixes the *carrier algebra* (complex) and the *phase redundancy* ($U(1)$); Pillar 2 fixes the *inner-product form* (sesquilinear, from four-band orthogonality).

**Postulate 2 (dynamics)** comes primarily from Pillar 2 (time homogeneity → Stone's theorem; spatial homogeneity → momentum operator; four-band partition → kinetic operator). Pillar 1 contributes the complex coefficient $i\hbar$ on the LHS of Schrödinger (because the carrier is complex from Pillar 1).

**Postulate 3 (Born rule)** comes from both pillars: Pillar 1 forces the quadratic *form* ($|P_K|^2 = b_K$); Pillar 2 forces the *operational interpretation* (commitment-event phase-randomization → bandwidth-fraction).

**Postulate 4 (composition)** comes primarily from Pillar 2 (bipartite participation measure on product index space → tensor product). Pillar 1 contributes the complex-carrier consistency at the tensor-product level (the joint carrier is $\mathbb{C}$-valued because both factor carriers are, by Pillar 1).

**A table of which substrate identity forces which postulate-aspect:**

| Postulate / aspect | Pillar 1 ($|P_K|^2 = b_K$) | Pillar 2 (symmetry + partition) |
|---|---|---|
| State-space carrier $\mathbb{C}$ | ✓ (Frobenius + $U(1)$ polarity) | — |
| Sesquilinear inner product | partial ($|P_K|^2$ identification) | ✓ (four-band orthogonality) |
| Phase redundancy ($U(1)$) | ✓ (squared modulus is $U(1)$-invariant) | — |
| Schrödinger PDE form | $i\hbar$ coefficient (Pillar 1 complex carrier) | ✓ (Stone on time-translations) |
| Linearity of dynamics | — | ✓ (bandwidth additivity + Stone) |
| Hermiticity of generator | — | ✓ (Stone produces self-adjoint generator) |
| Born rule quadratic form | ✓ ($|P_K|^2 = b_K$) | — |
| Born rule σ-additivity | — | ✓ (bandwidth additivity) |
| Born rule operational route | partial (quadratic from $|P|^2 = b$) | ✓ (commitment phase-randomization) |
| Tensor-product composition | partial (complex-carrier consistency) | ✓ (bipartite participation measure) |

Every cell in the "FORCED" matrix is either directly traced to Pillar 1 or Pillar 2, or jointly forced by both. No postulate-aspect requires an independent axiom beyond the substrate.

**Three sub-puzzles, one answer (revisited).** The standard puzzles —

- *Why complex Hilbert space?* Because $b_K$ must be real and non-negative, and the substrate has $U(1)$ polarity. The participation measure must be $\mathbb{C}$-valued to carry both.
- *Why quadratic Born?* Because $|P_K|^2 = b_K$ by construction. The "exponent 2" is built into the substrate.
- *Why linear unitary dynamics?* Because bandwidth additivity forces per-channel linearity, time-translation symmetry forces unitarity via Stone's theorem.
- *Why tensor-product composition?* Because bipartite participation measures live on the product of index spaces, and the natural bilinear extension is the tensor product.

Three of the four are forced jointly by Pillar 1; the fourth (composition) is forced by Pillar 2's bipartite extension. The unification is genuine: at the substrate level, *one* structural commitment (the participation measure with the two pillars supporting it) does the work that the four-postulate axiomatization assigns to four independent commitments.

### 7.4 Worked example: double-slit interference + measurement

To make the unification concrete, consider a standard double-slit experiment with a which-path detector. An electron passes through a screen with two slits; an interference pattern forms on a downstream detector; a which-path measurement at the slits destroys the interference. The standard analysis engages all four QM postulates simultaneously. We trace how each postulate's substrate-level forcing chain contributes.

**Setup.** The electron is a Case-R chain in the ED substrate, with channels $K \in \{1, 2\}$ corresponding to the two slits. At a locus $u$ between the slits and the detector, the participation measure is
$$
P_K(u, t) = \sqrt{b_K(u, t)}\,e^{i\pi_K(u, t)},
$$
with $K \in \{1, 2\}$.

**Postulate 1 engages.** The coherent sum wavefunction $\Psi(u, t) = P_1(u, t) + P_2(u, t)$ lives in the complex Hilbert space (Pillar 1: Frobenius + $U(1)$ polarity → $\mathbb{C}$-carrier). The state space is a two-dimensional complex Hilbert space spanned by $|1\rangle$ and $|2\rangle$. Sesquilinear inner product (Pillar 2: four-band orthogonality). Global phase invariance under $\Psi \to e^{i\theta}\Psi$ (Pillar 1: $U(1)$-invariance of bandwidth, Paper #16).

**Postulate 2 engages.** The chain evolves from the slits to the detector via the Schrödinger equation (Pillar 2: Stone's theorem on time-translations, Paper #4). The kinetic-energy operator $\hat{T} = -\hbar^2\nabla^2/(2m)$ (Pillar 2: Galilean Lie algebra + adjacency-bandwidth flow, Papers #6, #15) governs the propagation; potential terms account for the screen. The wavefunction develops position-dependent phase $\Psi(x) = (e^{i\phi_1(x)}\sqrt{b_1(x)} + e^{i\phi_2(x)}\sqrt{b_2(x)})/\sqrt{2}$ at the detector plane, with $\phi_1, \phi_2$ depending on the path lengths through each slit.

**Postulate 3 engages.** At the detector, a commitment event occurs (Pillar 2: P11). The Born rule (Pillar 1: $|P_K|^2 = b_K$ + Pillar 2: bandwidth-fraction at commitment) gives:
$$
\text{Prob}(\text{detector at position } x) = |\Psi(x)|^2 = \frac{1}{2}\Bigl[b_1(x) + b_2(x) + 2\sqrt{b_1(x) b_2(x)}\cos(\phi_2(x) - \phi_1(x))\Bigr].
$$
The cross-term $\cos(\phi_2 - \phi_1)$ is the **interference pattern** — bright fringes where the relative phase is $0 \mod 2\pi$, dark fringes where it is $\pi \mod 2\pi$. The cross-term depends on *relative phase* (which is observable via interference); the *global* phase of $\Psi$ remains unobservable (Pillar 1: $U(1)$-invariance).

**Now insert a which-path detector at the slits.** The which-path measurement is itself a commitment event at the slit (Pillar 2: P11). Environmental phase-randomization at the commitment kills the relative phase between paths 1 and 2: independent random phases $\delta_1, \delta_2$ on each path, with $\langle e^{i(\delta_2 - \delta_1)}\rangle = 0$ (Paper #14 §7.3). The cross-term in the downstream detection probability vanishes:
$$
\text{Prob}(\text{detector at } x \mid \text{which-path measured}) = \frac{1}{2}[b_1(x) + b_2(x)].
$$
Interference is destroyed. The substrate-level mechanism is the same environmental phase-randomization that produces the Born rule's operational form (Pillar 2: P11 + four-band $b_\mathrm{env}$ band).

**Postulate 4 engages.** If the experiment is run with two correlated electrons (an EPR setup), the joint participation measure is $P^{AB}_{K_A, K_B}(u_A, u_B)$ on the product of channel-locus indices. Tensor-product composition emerges (Pillar 2: bipartite participation measure on product index space). Entangled states $P^{AB} \neq P^A \otimes P^B$ produce Bell correlations bounded by Tsirelson (Paper #3 §7.2). For a Bell-state preparation:
$$
P^{AB} = \frac{1}{\sqrt{2}}\bigl(P_{\uparrow\downarrow}^{AB} - P_{\downarrow\uparrow}^{AB}\bigr),
$$
a measurement on $A$ instantaneously correlates with the result on $B$ via the joint participation structure, with no signal exchange (the marginals at $B$ are independent of the measurement setting at $A$ — Tsirelson + no-signaling, Papers #3 §7.2 + Paper #5 entanglement structure).

**The synthesis.** Across this single experimental scenario, all four QM postulates engage simultaneously:

- State space (Postulate 1) supplies the complex Hilbert space the participation measure lives in.
- Dynamics (Postulate 2) propagates the wavefunction through the apparatus.
- Measurement (Postulate 3) produces detector outcomes with Born-rule probabilities, including the interference cross-terms (when no which-path is measured) or their destruction (when which-path is measured).
- Composition (Postulate 4) supplies the bipartite structure for entangled-electron setups.

The substrate-level origin of each is *the same participation measure* with $|P_K|^2 = b_K$. The four postulates are four ways of *interrogating* the same substrate object — what's the carrier? how does it evolve? what's the measurement rule? how do joint systems combine? — not four separate axioms.

---

## 8. Exclusion Arguments

### 8.1 A1 — Four independent postulates

The standard axiomatic presentation treats the postulates as independent. Under the substrate-conditions test, this presentation is *downstream* of the substrate forcing: the postulates *appear* independent if one starts from the Hilbert-space arena, but they share substrate-level identities once one starts from the participation measure. The independence is an artifact of the axiomatic presentation, not a structural fact about the underlying world. The matrix of §7.3 explicitly shows the shared substrate-level forcing across the four postulates.

### 8.2 A2 — Real-valued participation measure

Excluded by Paper #1's substrate-level argument: real-valued carriers fail to represent the $U(1)$ polarity primitive faithfully. With real carriers, all four postulates would be modified: state space would be real (no complex linearity), the Born rule would have a different form (no $|z|^2$ structure on real numbers in the same way), dynamics would be non-unitary, and composition would lack the tensor-product complex structure. The unification would not exist at all. The substrate doesn't permit real-valued carriers.

### 8.3 A3 — Nonlinear dynamics

Excluded by Paper #4's unitarity result + the linearity-from-bandwidth-additivity argument of Paper #6 §8.1 + Paper #13 §7.2. Nonlinear dynamics breaks the substrate-level Schrödinger structure and the connection to state-space linearity.

### 8.4 A4 — Non-Born probability rule

Excluded by Papers #2, #14 + Cauchy functional equation on bandwidth additivity. Non-quadratic probability rules fail the substrate-level additivity constraint.

### 8.5 A5 — Non-tensorial composition

Excluded by Paper #3 §7.2: the bipartite participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$ lives on the product of the subsystems' channel/locus indices — this is the tensor-product structure at the substrate level. Cartesian-product or other non-tensorial compositions would require a different substrate-level joint structure, which the substrate does not supply.

### 8.6 A6 — No four-band partition

Excluded by Primitive P04 §1.5 (the four-band partition is a substrate primitive). Without the four-band partition: no kinetic operator (Papers #6, #15), no Heisenberg uncertainty (Paper #11), no inner-product orthogonality (Paper #3), no Born-rule operational route (Paper #14). The substrate-level forcing of the QM postulates would collapse.

### 8.7 A7 — Phase-dependent bandwidth

Excluded by Paper #16 §8.1. Phase-dependent bandwidth would break the $|P_K|^2 = b_K$ identity, breaking the chain of identities supporting Postulates 1-3 (Pillar 1).

### 8.8 A8 — Single-pillar unification

Hypothetically: a substrate has only Pillar 1 (the squared-modulus identity) but lacks Pillar 2's symmetry-partition content, or vice versa. Excluded because:

- *With only Pillar 1*: state space, Born rule, and $U(1)$ redundancy are forced; but the inner product (which requires four-band orthogonality), the dynamics (which requires Stone's theorem on time-translations), and the tensor-product composition (which requires bipartite extension) are not. Three of the four postulates are unforced.
- *With only Pillar 2*: dynamics, momentum operator, kinetic operator, inner product, and tensor product are forced; but the *complex* carrier (which requires Frobenius + $U(1)$ polarity from Pillar 1) is unforced, and the Born rule's *quadratic* form (which requires $|P_K|^2 = b_K$ from Pillar 1) is unforced.

Both pillars are required for the joint forcing. A substrate with only one pillar would produce a partial-QM theory.

### 8.9 B1 — Dirac-von Neumann axiomatic QM

Standard textbook presentation treating the four postulates as independent. Under the substrate-conditions test, this is downstream of the substrate forcing: the axiomatic presentation describes the same content the substrate produces, but as four separate axioms rather than as four facets of a single substrate object. The two presentations are equivalent at the level of empirical predictions; the substrate forcing is upstream in the sense of structural derivation.

**The key insight**: Dirac-von Neumann is not "wrong" — it correctly describes the formal structure of QM. What it *misses* is the substrate-level recognition that the four postulates share underlying identities. From an axiomatic-presentation perspective, the postulates are taken as starting points; from a substrate perspective, they are downstream consequences.

### 8.10 B2 — Hardy 2001

Hardy's reconstruction succeeds in deriving QM from five operational axioms (information, simplicity, subspaces, composite systems, continuity) plus assumptions about the relationship between distinguishable states and the dimension of a probability space. Hardy's "continuity" axiom — that there is a continuous reversible transformation between any two pure states — is the load-bearing axiom; it forces the complex Hilbert space over the alternatives (real, quaternionic).

Structural comparison with ED:
- **Hardy's continuity axiom** plays a role analogous to ED's $U(1)$ polarity (Primitive P09): both supply the continuous structure that selects $\mathbb{C}$ over $\mathbb{R}$.
- **Hardy's information axiom** plays a role analogous to ED's bandwidth-and-Born-rule chain: it forces the probabilistic structure.
- **Hardy's subspaces and composite-systems axioms** play roles analogous to ED's four-band partition + bipartite extension.

The two derivations are parallel: Hardy takes operational axioms as primitive; ED takes substrate primitives as primitive. The structural content is the same; the choice of "what's primitive" differs.

**Where they could be related**: if the operational axioms Hardy uses turn out to be themselves derivable from ED substrate primitives, then Hardy's reconstruction is downstream of ED. This is an open question.

### 8.11 B3 — Masanes-Müller 2011

Similar to Hardy: reconstructs QM from five operational axioms emphasizing tomographic locality and continuous reversibility. The continuous-reversibility axiom plays the load-bearing role.

Structural comparison: tomographic locality (M-M's information-completeness axiom) plays a role analogous to ED's bandwidth additivity over disjoint channels (Primitive P04). Continuous reversibility plays the role of $U(1)$ polarity + Stone's theorem on time-translations.

Same general open question: whether M-M's operational axioms are themselves substrate-derivable.

### 8.12 B4 — Chiribella-D'Ariano-Perinotti (CDP) information-theoretic reconstruction

CDP's six axioms (causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, **purification**) reconstruct QM. The purification axiom — that every mixed state is the marginal of a pure state on a larger system — is the load-bearing axiom.

Structural comparison with ED: CDP's purification axiom plays a role analogous to ED's bipartite participation measure (Paper #3 §7.2). Every "mixed state" at locus $u$ (an incoherent diagonal mixture from Paper #14) is structurally the marginal of a pure participation measure on a larger system that includes the environment.

CDP and ED converge on the same QM content via different primitives. The open question: whether CDP's purification (a strong information-theoretic axiom) is itself derivable from ED's substrate-level commitment-and-environment structure.

### 8.13 B5 — Coecke-Kissinger categorical QM

Categorical formulations describe QM as a compact closed dagger category with biproducts. The categorical axioms (dagger structure for inner products, compact closed for tensor product, biproducts for direct sums) capture the structural content of QM at a high level of abstraction.

Structural comparison: categorical QM is a *meta-theory* of QM's structural content — it identifies the algebraic-categorical features that QM possesses. ED supplies a *substrate* for those features. The two operate at different levels of abstraction: ED at the substrate level, categorical QM at the meta-structural level. They are mutually informative rather than competing: a substrate forcing of categorical structure would be a deeper result than either alone.

### 8.14 B6 — QBism

QBism derives QM postulates from agent rationality + coherence conditions, with states as degrees of belief. The decision-theoretic substrate (agent rationality) is fundamentally different from ED's physical substrate (participation graph).

Structural comparison: QBism operates on a *different kind of substrate*. ED's substrate is physical; QBism's is epistemic. Both succeed in producing QM postulates, but via different chains. Under the substrate-conditions test of the present paper (which specifies a *physical* substrate), QBism is not in the alternative-encodings space — it is an alternative *philosophical framework* operating on a different substrate.

ED's substrate forcing predicts that any rational agent reasoning coherently about substrate-level commitment outcomes will adopt degrees of belief consistent with the Born rule. The substrate is upstream; QBist degrees of belief are downstream.

### 8.15 B7 — Generalized Probabilistic Theories (GPT)

GPT formalizes QM as one specific point in the space of probabilistic theories satisfying additional structural axioms. The framework specifies state spaces as convex sets, effects as linear functionals, and identifies QM by additional structural commitments.

Structural comparison: GPT is a *parameterization space* of theories rather than a specific theory. ED supplies one specific theory (with one specific substrate); QM appears as a specific point in the GPT parameterization. The two are mutually informative: ED's substrate forces specific GPT structural commitments (convex state spaces with sesquilinear-inner-product structure, tensor-product composition, etc.); GPT supplies the parameterized framework in which the substrate-forced point sits.

### 8.16 Summary of exclusions

| Alternative | Violates / status | Reason |
|---|---|---|
| A1 four independent postulates | not in space | Axiomatic presentation is downstream; same content, different framing. |
| A2 real-valued $P_K$ | Paper #1 | Substrate $U(1)$ polarity excludes real-valued carriers. |
| A3 nonlinear dynamics | Papers #4, #13 | Bandwidth additivity + unitarity force linear dynamics. |
| A4 non-Born probability | Papers #2, #14 | Cauchy functional equation forces $\alpha = 2$. |
| A5 non-tensorial composition | Paper #3 §7.2 | Bipartite participation measure on product index space is tensorial. |
| A6 no four-band partition | P04 §1.5 | Four-band partition is substrate primitive. |
| A7 phase-dependent bandwidth | Paper #16 | $|P_K|^2 = b_K$ identity forces phase-independence. |
| A8 single-pillar unification | both pillars required | Either pillar alone produces partial-QM, not the full unification. |
| B1 Dirac-von Neumann | not in space | Axiomatic presentation downstream of substrate forcing. |
| B2 Hardy 2001 | parallel | Operational-axiom substrate; relationship to ED open. |
| B3 Masanes-Müller 2011 | parallel | Same general status as Hardy. |
| B4 CDP information-theoretic | parallel | Purification axiom; relationship to ED bipartite structure open. |
| B5 Coecke-Kissinger categorical | meta-theoretic | Different level of abstraction; mutually informative with ED. |
| B6 QBism | different substrate | Epistemic substrate vs. ED physical substrate. |
| B7 GPT | parameterization | ED is specific point in GPT space; mutually informative. |

**The four QM postulates are jointly forced by the participation measure and its substrate-level primitives via two foundational identities. The unification is structural, not rhetorical.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

Any empirical falsifier of one of the four postulates is simultaneously a falsifier of the substrate-level unification. Specifically:

- **State-space falsifier**: any observation requiring a non-complex (real-only or quaternionic) state space at the kinematic level.
- **Dynamics falsifier**: any observation of nonlinear, non-unitary, or higher-order-time evolution at the kinematic level.
- **Measurement falsifier**: any observation of non-quadratic probability rules.
- **Composition falsifier**: any observation of joint-system behavior incompatible with tensor-product structure (e.g., violation of no-signaling at the kinematic level, or interference patterns inconsistent with tensor-product entanglement).

None of these has been observed. Standard QM's empirical content is identical to the substrate-derived content; tests of one are tests of the other.

**Additional substrate-level falsifier**: any experiment showing that the four postulates are *not* simultaneously consistent — e.g., that the same physical system satisfies the Born rule but violates linearity, or satisfies linearity but violates the tensor-product composition. The substrate-level unification predicts that the four postulates are *jointly* coherent across all physical scenarios; any inconsistency between two of them would falsify the unification.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C7 (substrate primitives + Papers #1-#16 inherited + no four-postulate axiomatization as input) but for which the four QM postulates are *not* jointly forced — e.g., one postulate emerges but another does not, or the postulates emerge but with incompatible structural forms.

The author's claim is that no such substrate exists. The chain of inheritances in §7 closes: each postulate traces back to substrate primitives, with shared identities ensuring joint consistency.

### 9.3 Downstream exposure

The substrate-level unification underlies every quantitative prediction of QM:

- **Atomic physics, condensed-matter physics, quantum chemistry**: all rely on the joint application of state space + Schrödinger + Born rule + tensor product.
- **Quantum information theory**: protocols (teleportation, dense coding, quantum error correction) use all four postulates jointly.
- **Quantum-computing fidelity**: tests the joint substrate-level forcing of all four postulates in engineered systems.
- **Atomic-physics precision measurements** (electron magnetic moment, Lamb shift, etc.) test the joint application of all four postulates to many-digit precision.

Every quantitative quantum prediction tests the substrate-level forcing of all four postulates simultaneously.

---

## 10. Methodological Discussion: What the Unification Means

### 10.1 What unification adds beyond the individual forcings

Each of Papers #1-#16 establishes one or more of the QM postulates as a substrate-forced result. A natural question: what does the present synthesis paper *add* beyond the individual forcings?

The answer is structural recognition. Papers #1-#16 each force a *specific* result (the Born rule, the Schrödinger equation, etc.) from substrate primitives. The synthesis paper recognizes that the underlying *substrate identities* — Pillar 1 and Pillar 2 — are shared across the four postulates. This is not a new derivation; it is a structural observation about the derivations already done.

The observation matters because it changes the rhetorical status of QM's "axiomatic foundation":

- *Without the unification*: QM rests on four independent postulates, each requiring its own justification or empirical motivation. Standard treatments and reconstruction programs (Hardy, Masanes-Müller, CDP, etc.) each work to derive QM from a smaller set of axioms, but each ends up with a different starting point.

- *With the unification*: QM rests on a *single* substrate object with *two* foundational identities. The four postulates are not independent commitments but joint consequences. The question "why these four postulates and not others?" reduces to "why this substrate and not another?" — a single question, not four.

### 10.2 What unification does *not* claim

The unification does *not* claim that QM is derivable from nothing, or that all of physics is now explained, or that the ED substrate is empirically established. The claim is narrower:

- *Given the ED substrate primitives*, the four postulates are jointly forced.
- The substrate primitives themselves remain upstream commitments — they are not derived in this paper or in any of Papers #1-#16. The question "are the substrate primitives correct?" is the empirical question for the broader ED program (Papers #18+ and the empirical-test program).

The unification reduces the number of *axiomatic-level* commitments from four (the standard QM postulates) to a substrate with primitives that supply two foundational identities. Whether the substrate is empirically right is a separate, deeper question.

### 10.3 Relationship to mainstream reconstruction programs

Mainstream reconstruction programs (Hardy 2001, Masanes-Müller, Chiribella et al., Coecke-Kissinger) succeed in deriving QM from smaller sets of axioms. Each program's success demonstrates that the four postulates are not maximally independent — some can be derived from others plus structural axioms.

The ED program's contribution is *different in kind*: it derives the postulates from substrate primitives that are not themselves quantum-mechanical or operational. The reconstructions operate within a framework that already assumes either an information-theoretic primitive (Hardy, M-M, CDP), a categorical structure (Coecke-Kissinger), or an epistemic substrate (QBism). The ED substrate is physical — a participation graph with bandwidth, polarity, and channels — and the derivation chain runs from substrate to QM postulates without taking any QM-specific structure as primitive.

This is not to say ED is "better" than the reconstructions; it is to say ED is *different*. The reconstructions are upstream of the four-postulate axiomatization within QM's own conceptual framework; ED is upstream of QM itself within a physical-substrate framework.

A natural open question: are the reconstructions' axioms (Hardy's continuity, M-M's tomographic locality, CDP's purification, Coecke-Kissinger's categorical structure) themselves substrate-derivable from ED? If so, the reconstructions are downstream of ED. If not, the two are different routes to the same QM endpoint via different upstream substrates. This is an open structural question — important for the broader research program, beyond the scope of the present paper.

### 10.4 What follows

With the four QM postulates substrate-unified, the foundational substrate-level program for non-relativistic single-particle QM is structurally complete. Subsequent Wave 2 papers will extend this foundation:

- Relativistic extensions (Paper #7's Dirac + g=2 + Klein-Gordon).
- Field-theoretic extensions (Yang-Mills, gauge structure).
- Continuum-emergent classical limits (Ehrenfest, decoherence, classical mechanics).
- Many-body / statistical-mechanical extensions.
- Curved-spacetime extensions (substrate gravity, GR-emergent content).

Each builds on the substrate-unified foundation established here. The present paper is the structural-foundation capstone of the QM-emergence chain.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The two foundational substrate identities — explicit

**Identity 1: $|P_K|^2 = b_K$**.

Forced by Paper #1 via:
- $b_K$ as substrate non-negative real primitive (P04).
- $\pi_K$ as $U(1)$ polarity primitive (P09).
- Frobenius classification of finite-dimensional associative real division algebras → $\mathbb{C}$ is the unique carrier.
- Cauchy functional equation on bandwidth additivity → squared-modulus identity.

Forces:
- Complex state-space carrier (Postulate 1).
- Born rule's quadratic form (Postulate 3).
- $U(1)$ gauge redundancy (Paper #16).
- Heisenberg uncertainty's $\hbar/2$ bound (Paper #11).
- Phase-blindness of single-state observables.

**Identity 2: Substrate symmetry-and-partition content**.

Forced by Primitives P03 (homogeneity), P04 (bandwidth with four-band partition), P06 (spatial axis), P11 (commitment), P13 (time axis).

Forces:
- Stone's theorem on time-translations → Schrödinger dynamics (Postulate 2).
- Stone's theorem on spatial translations → momentum operator (Paper #12).
- Bandwidth additivity → linearity of dynamics + Born-rule σ-additivity.
- Four-band orthogonality → inner-product structure (Postulate 1) + adjacency-bandwidth partition.
- Commitment events → operational Born rule (Paper #14).
- Bipartite substrate structure → tensor-product composition (Postulate 4).

### A.2 Postulate-by-postulate cross-reference

| Postulate | Forcing source | Key papers |
|---|---|---|
| 1 — State space | Participation measure + $U(1)$ + IP + phase redundancy | #1, #3, #16 |
| 2 — Schrödinger dynamics | Stone on time-translations + thin-limit continuum + Hamiltonian form | #4, #6, #13 |
| 3 — Born rule | Gleason-Busch + bandwidth-fraction at commitment | #2, #14 |
| 4 — Tensor-product composition | Bipartite participation measure | #3 §7.2 + Paper #5 entanglement structure |

### A.3 Glossary

- **Adjacency band.** Component of the four-band partition carrying kinematic content.
- **Bandwidth $b_K(u)$.** Primitive non-negative real-valued substrate quantity.
- **Commitment event.** Primitive (P11) discrete substrate-level event producing outcomes.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **Four-band partition.** Substrate-level decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ (P04 §1.5).
- **Hilbert space.** Complete inner-product space; substrate-derived state space arena.
- **INHERITED.** Quantitative content not derived in the present paper.
- **Joint participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$.** Bipartite substrate object on the product of channel/locus index spaces.
- **Participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$.** Complex amplitude carrier; the single substrate object from which the four QM postulates derive.
- **Pillar 1.** Substrate identity $|P_K|^2 = b_K$.
- **Pillar 2.** Substrate symmetry-and-partition content (P03 + P04 + P11 + P13 + bipartite extension).
- **Polarity $\pi_K(u)$.** Primitive $U(1)$-valued angular substrate quantity.
- **Substrate.** Pre-quantum primitive layer of ED.
- **Tensor-product composition.** Joint state-space construction $\mathcal{H}_A \otimes \mathcal{H}_B$.
- **Thin-participation limit.** Substrate regime $M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$.

### A.4 Source-repository citations (for ED-internal readers)

- `arcs/U1/04_closure_and_summary.md` — participation measure forcing (Paper #1).
- `arcs/born_gleason/05_synthesis_theorem10.md` — Born rule via Gleason-Busch (Paper #2).
- `arcs/U2/04_synthesis_and_verdict.md` — sesquilinear inner product (Paper #3).
- `arcs/U3/04_closure_and_summary.md` — Schrödinger via Stone's theorem (Paper #4).
- `arcs/U4/04_closure_and_summary.md` — Hamiltonian form (Paper #6).
- `arcs/U5/04_closure_and_summary.md` — momentum operator (Paper #12).
- `arcs/arc-foundations/schrodinger_emergence.md` — thin-limit Schrödinger (Paper #13).
- `arcs/arc-foundations/born_rule_from_participation.md` — bandwidth-fraction Born (Paper #14).
- `arcs/arc-foundations/uncertainty_from_participation.md` — Heisenberg (Paper #11).
- `arcs/arc-foundations/bell_correlations_from_participation.md` — bipartite + Tsirelson (Paper #3).
- `papers/QM_Emergence_Structural_Completion/` — program-level synthesis paper.

These are *not* required reading for the present paper.

---

*End of Paper #17.*
