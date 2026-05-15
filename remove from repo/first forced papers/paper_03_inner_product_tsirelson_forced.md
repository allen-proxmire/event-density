# The Sesquilinear Inner Product and the Tsirelson Bound are FORCED

**Paper #3 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #3 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The sesquilinear inner product on the state space of quantum mechanics and the Tsirelson bound $|S| \leq 2\sqrt{2}$ on bipartite CHSH correlations are normally either postulated (in the case of the inner product) or derived from operator algebra that assumes it (in the case of Tsirelson's bound). This paper shows that, **given the substrate primitives of Papers #1–#2 plus the four-band orthogonality structure of Primitive P04 §1.5**, both facts are forced: the sesquilinear inner product is the unique pairing on the participation manifold consistent with the substrate's four-band orthogonality and bandwidth-additivity primitives, and the Tsirelson bound is its structural consequence via the Landau-Khalfin operator-norm algebra. Real-bilinear, non-sesquilinear, non-positive, PR-box, and superquantum alternatives are each excluded. The bound $2\sqrt{2}$ is forced as the unique ceiling — neither relaxed nor strengthened — by the joint action of the substrate-derived inner-product structure and bandwidth normalization. The claim is conditional on the substrate primitives; in particular, on the four-band partition's primitive-level orthogonality, which the substrate adopts as a structural commitment and which is itself upstream content for the Primitive-Forcing Meta-Paper.

---

## 1. Framing

### 1.1 What standard quantum mechanics assumes about the inner product

The state space of a quantum system is a complex Hilbert space $\mathcal{H}$, equipped with an inner product $\langle \cdot \mid \cdot \rangle : \mathcal{H} \times \mathcal{H} \to \mathbb{C}$ satisfying four standard axioms:

1. **Sesquilinearity.** $\langle \psi \mid \alpha \phi_1 + \beta \phi_2 \rangle = \alpha \langle \psi \mid \phi_1 \rangle + \beta \langle \psi \mid \phi_2 \rangle$ — linear in the second slot. Combined with axiom (2), this gives *conjugate-linear* behavior in the first slot.
2. **Conjugate symmetry.** $\langle \psi \mid \phi \rangle = \overline{\langle \phi \mid \psi \rangle}$.
3. **Positivity.** $\langle \psi \mid \psi \rangle \geq 0$, with equality if and only if $\psi = 0$.
4. **Orthogonality structure.** Vectors $\psi, \phi$ are orthogonal when $\langle \psi \mid \phi \rangle = 0$; the inner product induces a decomposition of $\mathcal{H}$ into orthogonal subspaces.

These four facts are not independent. (2) and (3) together fix the *sesquilinear* form rather than allowing bilinear, antisymmetric, or non-positive alternatives. Sesquilinearity is what makes the Born rule — the squared-modulus $|\langle K \mid \psi \rangle|^2$ — well-defined as a non-negative number consistent with phase rotations. Without it, the standard machinery of quantum probability does not work.

The standard presentation states these axioms together as a single postulate: "states are vectors in a complex Hilbert space." Where the sesquilinear structure comes from, why it is sesquilinear rather than bilinear, and why the inner product is positive rather than indefinite — these are not derived. They are part of the package.

### 1.2 What standard quantum mechanics observes about the Tsirelson bound

The Bell-CHSH inequality (Clauser-Horne-Shimony-Holt 1969) gives a constraint on the correlations achievable by classical theories: for any local hidden-variable (LHV) theory with binary outcomes $\pm 1$,
$$
|S| := |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \leq 2,
$$
where $E(a, b) = \langle s_A(a) \cdot s_B(b) \rangle$ is the expected product of binary outcomes for measurement settings $(a, b)$.

Quantum mechanics permits values up to $|S| = 2\sqrt{2} \approx 2.828$ — the **Tsirelson bound** (Tsirelson 1980), achieved by appropriate measurement angles on a maximally entangled bipartite state. This is one of the most empirically confirmed inequalities in physics: loophole-free Bell tests (Hensen et al. 2015; Giustina et al. 2015; Shalm et al. 2015) have measured $|S|$ values matching the Tsirelson prediction within statistical error.

But the bound itself is, in standard quantum mechanics, a *consequence* of the operator algebra applied to the Hilbert space — and the Hilbert space is assumed at the outset. The deeper question — *why does nature saturate $2\sqrt{2}$ but never exceed it?* — has remained open. PR-boxes (Popescu-Rohrlich 1994) are mathematical correlation tables that respect no-signaling but reach $|S| = 4$; they are consistent with relativistic causality but inconsistent with quantum mechanics. The Tsirelson bound is what separates the two regimes, but standard quantum mechanics does not explain why this particular value is the ceiling.

Programs that have tried to derive Tsirelson from deeper principles include:

- **Information causality** (Pawłowski et al. 2009): post-quantum correlations would violate a particular information-theoretic principle.
- **Macroscopic locality** (Navascués-Wolfe 2010): post-quantum correlations would produce non-classical statistics at macroscopic scales.
- **Local quantum mechanics** (Barnum et al.): the bound emerges from a class of generalized probabilistic theories.

These programs are powerful but typically operate at the level of generalized probabilistic theories rather than at the level of a substrate from which the Hilbert-space arena itself is derived. The question of where the inner product comes from in the first place is left unaddressed.

### 1.3 What this paper does

The Event Density (ED) framework supplies a pre-quantum substrate. Paper #1 of this series forces the amplitude carrier on every channel — the **participation measure** $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ — from substrate primitives alone. Paper #2 forces the **Born rule** $\text{Prob}(K \mid u) = |P_K(u)|^2/\sum_{K'} |P_{K'}(u)|^2$ from the same substrate plus the participation-measure result.

The present paper supplies the next step. Given the participation measure and the Born rule, it forces:

1. **The sesquilinear inner product** on the participation manifold:
   $$
   \langle P \mid Q \rangle := \sum_K \sum_u P_K^*(u)\, Q_K(u).
   $$
   Sesquilinearity, conjugate symmetry, positivity, and orthogonality structure all fall out of substrate primitives. The form is unique.

2. **The Tsirelson bound** $|S| \leq 2\sqrt{2}$ on bipartite CHSH correlations, via the Landau-Khalfin operator-norm algebra applied to the participation-manifold Hilbert space. The classical bound $|S| \leq 2$ for factorizable joint participation, the quantum bound $|S| \leq 2\sqrt{2}$ for arbitrary joint participation, and the exclusion of PR-box-like superquantum correlations $|S| > 2\sqrt{2}$ are all consequences of the substrate-derived inner-product structure.

Alternative inner products — bilinear real, non-sesquilinear, non-positive — and alternative correlation rules — PR-box, hidden-variable models, superquantum — are each excluded by explicit structural argument.

**Series context.** Paper #1 forced the amplitude carrier. Paper #2 forced the probability rule. The present paper forces the Hilbert-space arena and its first quantitative ceiling. Paper #4 will then force the Schrödinger equation as the dynamics on this arena. Together, Papers #1-#4 constitute the structural foundation of non-relativistic quantum mechanics.

---

## 2. Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#2 results plus four-band orthogonality (P04 §1.5)*. Then:
> - **(IP)** The unique inner product on the participation manifold consistent with substrate primitives is sesquilinear:
>   $$
>   \langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u)\, Q_K(u).
>   $$
> - **(Ts)** For any bipartite joint participation measure $P^{AB}$ normalized to $\langle P^{AB} \mid P^{AB} \rangle = 1$, the CHSH correlation satisfies $|S| \leq 2\sqrt{2}$.
>
> *The four-band orthogonality is a primitive-level substrate fact (P04 §1.5), not derived here. Why the substrate partitions into exactly four mutually orthogonal bands is upstream content (Primitive-Forcing Meta-Paper).*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **P04 (bandwidth as non-negative additive scalar):** provides the $\ell^2$ summation structure supporting the sesquilinear pairing.
- **P04 §1.5 (four-band partition):** bandwidth decomposes into four mutually orthogonal substrate-level bands (internal, adjacency, environmental, commitment-reserve). Source of inner-product orthogonality on the participation manifold.
- **Papers #1–#2 results:** the complex polar participation measure and the Born rule. Supply the structural arena on which the inner product is built.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, the sesquilinear inner product is the unique pairing on the participation manifold, and the Tsirelson bound $|S| \leq 2\sqrt{2}$ is its structural consequence via standard Landau-Khalfin operator-norm algebra. The Landau-Khalfin machinery is standard; the novelty is the substrate-level origin of the arena on which it operates.

### 3.1 What is FORCED

- **Sesquilinearity** of the inner product: linear in one slot, conjugate-linear in the other.
- **Conjugate symmetry**: $\langle P \mid Q \rangle = \overline{\langle Q \mid P \rangle}$.
- **Positivity**: $\langle P \mid P \rangle \geq 0$, with equality iff $P = 0$.
- **Orthogonality structure**: four-band orthogonality of bandwidth (Primitive 04 §1.5) is preserved as inner-product orthogonality on the participation manifold.
- **Classical bound** $|S| \leq 2$ for factorizable joint participation, via standard Bell-CHSH algebra applied to product probabilities.
- **Tsirelson bound** $|S| \leq 2\sqrt{2}$ for arbitrary joint participation, via the Landau-Khalfin operator-norm algebra on the inner-product structure.
- **Exclusion** of superquantum correlations $|S| > 2\sqrt{2}$: structurally forbidden by the inner-product + normalization structure.

### 3.2 What is INHERITED

- **Normalization conventions**: setting $\langle P \mid P \rangle = 1$ (rather than $= \sum_K \sum_u b_K(u)$) is a choice of scale; the structural content of the bound is invariant under rescaling.
- **Labeling of basis vectors**: the identification of channel index $K$ with a specific orthonormal basis vector $|K\rangle$ in the participation-manifold Hilbert space is a labeling choice; the inner-product structure does not depend on which channels are called "first" or "second."
- **Measurement-setting parametrization**: the identification of a measurement setting $a$ with a Hermitian unit-norm observable $\sigma_a$ is the standard quantum-mechanical correspondence; the present paper uses it without rederiving it from substrate dynamics.

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive the Schrödinger equation. The dynamics of the participation measure in time is the subject of Paper #4.
- This paper does **not** derive gauge structure, gravity, or anything beyond non-relativistic bipartite kinematics.
- This paper does **not** address the measurement problem at the level of interpretation. The substrate-level commitment primitive (Paper #2) plays the role of "what happens at measurement"; whether this is consistent with collapse, decoherence, or pilot-wave interpretations is a separate philosophical question.
- This paper does **not** treat Bell-inequality variants beyond CHSH. Multi-setting, multi-outcome, and high-dimensional Bell inequalities have their own quantum-mechanical bounds (Tsirelson's polytope, the NPA hierarchy); the structural-foundation result of this paper applies to CHSH specifically. Extensions follow the same machinery but are not redone here.
- This paper does **not** treat continuous-spectrum joint measurements. The forcing argument is stated for discrete channel outcomes; continuous-spectrum extensions follow standard measure-theoretic routes.

---

## 4. Key Vocabulary

For the reader new to Event Density, the following terms are sufficient for the body of the paper. A full alphabetized glossary appears in Appendix A.

- **Substrate.** The pre-quantum layer of primitive structure on which the ED framework is built. Not a Hilbert space; not a manifold.
- **Channel.** A primitive structural pathway in the substrate, indexed by a label $K$. Channels are ontologically primitive — their identity is intrinsic to the participation graph.
- **Participation bandwidth $b_K(u)$.** A non-negative real-valued primitive quantity on each channel at each locus, additive across disjoint channel decompositions.
- **Polarity $\pi_K(u)$.** A primitive $U(1)$-valued angular variable on each channel at each locus, the unique angular primitive in the substrate.
- **Participation measure $P_K(u)$.** The complex-valued object $\sqrt{b_K(u)}\,e^{i\pi_K(u)}$ established in Paper #1 as the unique amplitude carrier consistent with substrate conditions.
- **Joint participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$.** The complex-valued object on the product of two subsystems' channel and locus indices. *Factorizable* if $P^{AB} = P^A \cdot P^B$; *non-factorizable* (entangled) otherwise.
- **Correlation functional $E(a, b)$.** The expected product of binary measurement outcomes for setting pair $(a, b)$: $E(a, b) = \langle s_A(a) \cdot s_B(b) \rangle$ averaged over commitment outcomes.
- **CHSH operator $\hat{S}$.** The bipartite operator $\sigma_a \otimes \sigma_b + \sigma_a \otimes \sigma_{b'} + \sigma_{a'} \otimes \sigma_b - \sigma_{a'} \otimes \sigma_{b'}$ whose expectation value on a joint state gives the CHSH statistic $S$.
- **Sesquilinearity.** A bilinear-like form on a complex vector space that is linear in one slot and conjugate-linear (anti-linear) in the other. The standard structural property of inner products on complex Hilbert spaces.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying the following conditions.

### C1. Participation graph + channel structure (Primitives P03 + P07)

The substrate supplies a participation graph $G = (V, E)$ with vertex set $V$ (loci) and edge set $E$ (participation relations). At each locus $u \in V$ there is an available-channel set $\mathcal{K}(u)$ of channels at $u$, at most countable, with channels ontologically primitive.

### C2. Bandwidth with additivity and four-band orthogonality (Primitive P04)

The substrate supplies non-negative bandwidth $b_K(u) \in \mathbb{R}_{\geq 0}$ on each channel at each locus, with primitive-level additivity over disjoint channel decompositions. Bandwidth has a four-band decomposition (internal, adjacency, environmental, commitment-reserve) with the bands mutually orthogonal in their structural roles; this orthogonality is needed for the inner-product orthogonality structure (FORCED item §7.1.4).

### C3. Polarity (Primitive P09)

The substrate supplies a $U(1)$-valued angular variable $\pi_K(u) \in U(1)$ on each channel, the unique angular primitive in the substrate. $U(1)$-invariance of bandwidth (which depends only on the magnitude content of the participation measure, not on its phase) is the load-bearing structural fact for sesquilinearity (FORCED item §7.1.2).

### C4. Commitment events with locality (Primitive P11)

The substrate supports discrete commitment events at which a chain's multi-channel participation collapses to a single channel. Commitment events are *local*: a commitment at locus $u_A$ on subsystem A is independent of any commitment event at locus $u_B$ on subsystem B. This locality is the substrate-level origin of no-signaling (a structural consequence of C4, not an additional postulate).

### C5. The participation-measure result (Paper #1)

The amplitude carrier on each channel is the complex-valued participation measure
$$
P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)} \in \mathbb{C},
$$
with $|P_K|^2 = b_K$ and $\arg(P_K) = \pi_K$. Paper #1 establishes this as the unique carrier consistent with C1-C3.

### C6. The Born rule (Paper #2)

The probability that a commitment event at locus $u$ selects channel $K^*$ from the available-channel set is
$$
\text{Prob}(K^* \mid u) = \frac{|P_{K^*}(u)|^2}{\sum_{K \in \mathcal{K}(u)} |P_K(u)|^2} = \frac{b_{K^*}(u)}{\sum_K b_K(u)}.
$$
Paper #2 establishes this as the unique probability rule consistent with C1-C5.

### C7. No additional structural hypotheses

The forcing argument invokes only C1-C6 plus the following standard mathematical infrastructure:

- The Cauchy-Schwarz inequality for inner-product spaces.
- The classical operator-norm bound $\|[A, B]\| \leq 2\|A\| \cdot \|B\|$ for bounded operators $A, B$.
- The Landau-Khalfin (1987) operator-algebraic derivation of the Tsirelson bound from a CHSH-operator structure.

No Hilbert-space *axioms* are assumed; the Hilbert-space arena is *produced* by the participation-manifold construction. No linearity or unitarity of dynamics is assumed (that is Paper #4). No measurement-problem interpretation is taken on.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Bilinear real inner product.** The inner product $\langle P \mid Q \rangle$ is bilinear over $\mathbb{R}$ rather than sesquilinear over $\mathbb{C}$: linear in both slots, with the imaginary content of the participation measure discarded or handled by a separate real-pair structure.

**A2. Non-sesquilinear pairings.** Pairings that are complex-valued but neither sesquilinear nor anti-sesquilinear: for instance, complex-bilinear forms $\langle P \mid Q \rangle = \sum_K P_K \cdot Q_K$ without complex conjugation in either slot, or asymmetric pairings that fail conjugate symmetry.

**A3. Non-positive inner products.** Pseudo-inner products satisfying sesquilinearity and conjugate symmetry but allowing $\langle P \mid P \rangle < 0$ on some non-zero $P$. The Krein-space and Pontryagin-space analogues of Hilbert spaces.

**A4. Non-orthogonal decomposition rules.** Decompositions of the participation manifold into "bands" that fail orthogonality under the inner product — that is, decompositions where the four-band structure of bandwidth (internal/adjacency/environmental/commitment-reserve) is not reflected as orthogonal subspaces.

**A5. Correlation rules allowing $|S| > 2\sqrt{2}$.** Bipartite correlation rules built on the participation manifold that violate the operator-norm bound underlying Tsirelson — for instance, by relaxing the constraint $\|\sigma_a\| = 1$ on measurement observables, or by allowing the commutator bound $\|[\sigma_a, \sigma_{a'}]\| \leq 2$ to be exceeded.

**A6. PR-box correlations.** Mathematical correlation tables (Popescu-Rohrlich 1994) that satisfy no-signaling but reach $|S| = 4$. These are not built from any specific Hilbert-space structure; they are abstract probability tables consistent with relativistic causality but inconsistent with quantum mechanics.

**A7. Non-$U(1)$-respecting inner products.** Pairings that do not respect the substrate-level $U(1)$ polarity — for instance, pairings that include non-trivial integer windings $\pi_K \to n\pi_K$ of polarity content, or pairings that introduce angular content beyond what polarity supplies.

### 6.2 Mainstream alternatives

**B1. Classical hidden-variable models (CHSH $\leq 2$).** Local-realist theories with hidden variables specifying outcome distributions independently for each measurement setting. Constrained by the standard Bell-CHSH inequality $|S| \leq 2$.

**B2. PR-box / superquantum models (CHSH $= 4$).** Non-physical correlation tables exhibiting maximum CHSH violation while respecting no-signaling. Not realized in any known physical theory.

**B3. Bohmian correlation rules.** Non-local pilot-wave theory reproducing standard quantum correlations including the Tsirelson bound, via explicit non-local hidden variables.

**B4. GRW / CSL correlation rules.** Spontaneous-collapse models preserving the standard quantum Tsirelson bound while modifying the dynamics.

**B5. Real-vector-space QM correlations (Stueckelberg-class).** Real-vector-space variants with auxiliary $J$-operator. Reproduces standard quantum correlations once $J$ is identified with multiplication by $i$.

**B6. Quaternionic QM correlations (Adler-class).** Quaternionic state vectors with quaternionic inner product. Modifies the CHSH bound in single-particle systems and produces composition pathologies in multi-particle settings.

---

## 7. Constructive Necessity

This section establishes the positive half of the forcing theorem in two steps. §7.1 derives the sesquilinear inner product from substrate primitives. §7.2 derives the Tsirelson bound from the inner product structure plus the Landau-Khalfin algebra.

### 7.1 The sesquilinear inner product

**Definition.** Let $\mathcal{P}$ be the complex linear span of all participation-measure arrays $\{P_K(u) : K \in \mathcal{K}(u), u \in V\}$. Define the candidate inner product:
$$
\langle P \mid Q \rangle := \sum_K \sum_u P_K^*(u) \cdot Q_K(u),
$$
where $\sum_u$ runs over loci where both $P$ and $Q$ are supported and $\sum_K$ runs over channels available at each locus.

The derivation has four sub-components, each tracing to substrate primitives.

**(7.1.1) Linearity of $\mathcal{P}$ (automatic).** The participation measure is complex-valued (C5), and complex-valued function spaces are closed under componentwise addition and complex-scalar multiplication. $\mathcal{P}$ is therefore a complex vector space without additional structural commitment. This is the C3a sub-feature of the U2 arc — automatic from the carrier structure.

**(7.1.2) Sesquilinearity (FORCED by U(1) invariance + bandwidth non-negativity + additivity).** A bilinear pairing $\langle \cdot \mid \cdot \rangle : \mathcal{P} \times \mathcal{P} \to \mathbb{C}$ must satisfy three substrate-level constraints:

- **Diagonal identity.** The diagonal $\langle P \mid P \rangle$ must reproduce the chain's total bandwidth $\sum_K \sum_u b_K(u) = \sum_K \sum_u |P_K(u)|^2$, by C5's participation-measure identity $|P_K|^2 = b_K$ and C2's bandwidth content. This forces the diagonal to be a non-negative real number equal to the sum of squared moduli.

- **$U(1)$ phase invariance.** The diagonal must be invariant under the global gauge $P_K \to e^{i\alpha} P_K$ from C3. Complex-bilinear pairings $\langle P \mid Q \rangle_\text{bil} = \sum_K \sum_u P_K(u) Q_K(u)$ — without conjugation in either slot — fail this: under $P \to e^{i\alpha} P$, the diagonal would acquire a factor $e^{2i\alpha} \neq 1$.

  Conjugate-linear pairings $\langle P \mid Q \rangle_\text{sesq} = \sum_K \sum_u P_K^*(u) Q_K(u)$ produce a diagonal $\sum P_K^* P_K = \sum |P_K|^2$ that is invariant under the global phase: $(e^{i\alpha} P_K)^* (e^{i\alpha} P_K) = P_K^* P_K$. The phase factor cancels.

  Real-bilinear pairings (the real part of a complex pairing) discard the imaginary content of the inner product, which carries the phase-correlation information needed for interference and downstream Bell-type correlations.

  Sesquilinearity is the unique pairing surviving both constraints.

- **Bandwidth additivity.** The diagonal must be additive over disjoint participation contributions, in keeping with C2's bandwidth-additivity primitive. For disjoint $P = P_1 + P_2$ (orthogonal participation supports), $\langle P \mid P \rangle = \langle P_1 \mid P_1 \rangle + \langle P_2 \mid P_2 \rangle$ — which is exactly the substrate-level statement that bandwidth adds across disjoint channel/locus regions. Sesquilinearity reproduces this via $\langle P_1 + P_2 \mid P_1 + P_2 \rangle_\text{sesq} = \langle P_1 \mid P_1 \rangle + \langle P_2 \mid P_2 \rangle + 2\,\text{Re}\langle P_1 \mid P_2 \rangle$, with the cross-term vanishing on disjoint supports.

The three constraints together force the inner product to be sesquilinear with form $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$, modulo overall normalization. This is the C3b sub-feature of the U2 arc.

**(7.1.3) Conjugate symmetry and positivity (automatic from sesquilinearity).** Once the form is sesquilinear with conjugation in the first slot:

- **Conjugate symmetry.** $\langle Q \mid P \rangle = \sum_K \sum_u Q_K^*(u) P_K(u) = \overline{\sum_K \sum_u P_K^*(u) Q_K(u)} = \overline{\langle P \mid Q \rangle}$. Conjugate symmetry follows immediately.

- **Positivity.** $\langle P \mid P \rangle = \sum_K \sum_u |P_K(u)|^2 = \sum_K \sum_u b_K(u) \geq 0$ by C2's non-negativity of bandwidth. Equality holds iff every $b_K(u) = 0$, i.e., $P = 0$.

Both properties are direct consequences of sesquilinearity + the substrate-level non-negativity of bandwidth.

**(7.1.4) Orthogonality structure (FORCED by four-band orthogonality).** The substrate-level bandwidth has four bands (Primitive 04 §1.5): **internal**, **adjacency**, **environmental**, and **commitment-reserve**. These bands correspond to disjoint structural channels at the substrate level, with mutually exclusive participation roles. The corresponding decomposition of the participation measure $P_K = P_K^\text{int} + P_K^\text{adj} + P_K^\text{env} + P_K^\text{com}$ inherits this orthogonality: cross-band inner products vanish. Substrate-level orthogonality lifts to inner-product orthogonality on the participation manifold.

**Composite result.** The sesquilinear inner product
$$
\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u)\, Q_K(u)
$$
is forced on the participation manifold by C1-C6. Sesquilinearity, conjugate symmetry, positivity, and orthogonality are all FORCED consequences of substrate primitives; no Hilbert-space axiom is imposed independently.

The participation manifold $\mathcal{P}$ equipped with this inner product is a pre-Hilbert space; its completion in the induced norm topology is a Hilbert space $\mathcal{H}$.

### 7.2 The Tsirelson bound

**Intuition.** The Tsirelson bound is fundamentally an operator-norm statement: the CHSH operator $\hat{S}$ has maximum operator norm $2\sqrt{2}$ on any Hilbert space equipped with unit-norm Hermitian observables. The derivation below shows how this ceiling emerges from the substrate-derived inner product of §7.1, with no additional structural commitment beyond what has already been forced.

With the sesquilinear inner product established, the Tsirelson bound $|S| \leq 2\sqrt{2}$ for bipartite CHSH correlations follows from a structural operator-algebraic argument.

**Setup.** Consider a bipartite system with subsystems A and B at separated loci $u_A$ and $u_B$. The joint participation measure is
$$
P^{AB}_{K_A, K_B}(u_A, u_B) \in \mathbb{C},
$$
with normalization $\langle P^{AB} \mid P^{AB} \rangle = \sum_{K_A, K_B, u_A, u_B} |P^{AB}_{K_A, K_B}(u_A, u_B)|^2 = 1$ (a choice of scale; the bound is invariant under rescaling).

A measurement setting on subsystem A corresponds to a Hermitian unit-norm observable $\sigma_a$ acting on A's channel space, with eigenvalues $\pm 1$ (binary outcomes). Similarly $\sigma_b$ on B. The correlation function is
$$
E(a, b) = \langle P^{AB} \mid \sigma_a \otimes \sigma_b \mid P^{AB} \rangle.
$$

The CHSH operator is
$$
\hat{S} := \sigma_a \otimes \sigma_b + \sigma_a \otimes \sigma_{b'} + \sigma_{a'} \otimes \sigma_b - \sigma_{a'} \otimes \sigma_{b'},
$$
and the CHSH statistic is $S = \langle P^{AB} \mid \hat{S} \mid P^{AB} \rangle$.

**Classical bound $|S| \leq 2$ (factorizable case).** When $P^{AB} = P^A \cdot P^B$ is factorizable, the joint commitment probability factorizes, and each subsystem's outcome is determined locally by its own participation measure plus environmental commitment randomness (C4). The CHSH statistic becomes a classical expectation over local hidden variables — exactly the structure the Bell-CHSH inequality applies to. The standard algebraic identity
$$
|s_B(b) + s_B(b')| + |s_B(b) - s_B(b')| = 2 \quad \text{for } s_B \in \{\pm 1\}
$$
gives $|S| \leq 2$. The classical ceiling is forced by factorizability + binary outcomes.

**Quantum bound $|S| \leq 2\sqrt{2}$ (general case) — the Landau-Khalfin algebra.** For arbitrary joint participation measures, compute the square of the CHSH operator:
$$
\hat{S}^2 = (\sigma_a \otimes \sigma_b + \sigma_a \otimes \sigma_{b'} + \sigma_{a'} \otimes \sigma_b - \sigma_{a'} \otimes \sigma_{b'})^2.
$$
Expanding using $\sigma_a^2 = \mathbb{1}$ and $\sigma_b^2 = \mathbb{1}$ (a consequence of unit-norm Hermitian observables with $\pm 1$ eigenvalues), the diagonal terms give $4 \cdot \mathbb{1}_A \otimes \mathbb{1}_B$. The cross-terms collect into commutators:
$$
\hat{S}^2 = 4\,\mathbb{1} + [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}].
$$
Taking operator norms and using the standard inequality $\|[A, B]\| \leq 2\|A\| \cdot \|B\|$ for unit-norm Hermitian $A, B$:
$$
\|\hat{S}^2\| \leq 4 + \|[\sigma_a, \sigma_{a'}]\| \cdot \|[\sigma_b, \sigma_{b'}]\| \leq 4 + 2 \cdot 2 = 8.
$$
Therefore $\|\hat{S}\| \leq 2\sqrt{2}$. By Cauchy-Schwarz on the inner-product space,
$$
|S| = |\langle P^{AB} \mid \hat{S} \mid P^{AB} \rangle| \leq \|\hat{S}\| \cdot \langle P^{AB} \mid P^{AB} \rangle = 2\sqrt{2}.
$$
The Tsirelson bound is forced.

**Saturation at $|S| = 2\sqrt{2}$.** The bound is achieved by the singlet joint participation measure
$$
P^{AB}_{K_A, K_B} = \frac{1}{\sqrt{2}}\big(\delta_{K_A, 0} \delta_{K_B, 1} - \delta_{K_A, 1} \delta_{K_B, 0}\big)
$$
with measurement settings $a = \hat{x}$, $a' = \hat{z}$, $b = (\hat{x}+\hat{z})/\sqrt{2}$, $b' = (\hat{x}-\hat{z})/\sqrt{2}$. The correlation function for the singlet is $E(a, b) = -a \cdot b$, giving $S = -2\sqrt{2}$. Saturation is achieved — the bound is tight.

**Exclusion of $|S| > 2\sqrt{2}$.** The algebraic chain above admits no slack: the operator-norm inequalities are tight on the participation-manifold Hilbert space with unit-norm Hermitian observables. Any rule allowing $|S| > 2\sqrt{2}$ would have to violate either the inner-product structure (which fixes $\|\hat{S}\| \leq 2\sqrt{2}$) or the unit-norm observable structure (which fixes $\|\sigma_a\| = 1$). Both are forced by substrate primitives plus the participation-measure result. PR-box correlations achieving $|S| = 4$ are excluded structurally: they are not implementable on the participation manifold.

**No-signaling.** Commitment events are local (C4): the marginal probability on subsystem A is independent of the measurement setting on B. Explicitly,
$$
\sum_{K_B} \text{Prob}(K_A, K_B \mid a, b) = \sum_{K_B} \text{Prob}(K_A, K_B \mid a, b'),
$$
which is the standard no-signaling property. It holds because commitment-event probabilities factorize across the bipartite split when the participation measure is held fixed, regardless of the measurement settings. This is a structural consequence of C4, not an additional postulate.

The Tsirelson bound is forced; its saturation is realized; its exclusion of superquantum correlations follows from the same operator-algebraic chain that produces it.

---

## 8. Exclusion Arguments

This section dispatches each alternative encoding listed in §6 by identifying the substrate condition it violates.

### 8.1 A1 — Bilinear real inner product

**Claim.** A real-bilinear pairing fails the substrate-level $U(1)$-invariance constraint of C3.

**Argument.** A real-bilinear pairing $\langle P \mid Q \rangle_\text{R-bil} = \sum_K \sum_u \text{Re}[P_K(u) Q_K(u)]$ discards the imaginary content of the inner product. Under the global $U(1)$ phase $P_K \to e^{i\alpha} P_K$, $Q_K \to e^{i\beta} Q_K$, the pairing transforms in a way that depends on $\alpha + \beta$ rather than being invariant. More importantly, the imaginary part of the inner product carries the phase-correlation content (relative-phase information between $P$ and $Q$) that is needed downstream for interference and for the CHSH-type correlations of §7.2. Real-bilinear inner products cannot support these structures.

Equivalently: a real-bilinear pairing on a complex carrier is, by definition, the real part of a sesquilinear form. Storing only the real part is a structural choice that the substrate does not motivate — the imaginary part is needed for downstream content, and discarding it violates the closure of the inner product under the substrate's natural operations.

### 8.2 A2 — Non-sesquilinear pairings

**Claim.** Complex-bilinear pairings (no conjugation) violate $U(1)$-invariance of the diagonal; asymmetric pairings violate substrate-level conjugate symmetry.

**Argument.** A complex-bilinear pairing $\sum_K P_K Q_K$ (no conjugation) gives diagonal $\sum_K P_K^2$, which transforms as $e^{2i\alpha} \sum_K P_K^2$ under $P \to e^{i\alpha} P$. The bandwidth diagonal $\sum_K b_K = \sum_K |P_K|^2$ requires $U(1)$-invariance: the substrate-level quantity is real and gauge-invariant. Complex-bilinear forms cannot reproduce this. C3 is violated.

Asymmetric pairings (failing conjugate symmetry) introduce a direction-dependent inner product, which the substrate does not motivate: the inner product is built from substrate quantities (bandwidth, polarity, channel/locus structure) that have no preferred direction. Conjugate symmetry is the unique symmetry consistent with the participation-measure construction.

### 8.3 A3 — Non-positive inner products

**Claim.** Indefinite inner products allow $\langle P \mid P \rangle < 0$ on some non-zero $P$, contradicting C2's non-negativity of bandwidth.

**Argument.** The diagonal $\langle P \mid P \rangle$ must equal $\sum_K \sum_u b_K(u) \geq 0$ by C2. A non-positive inner product would assign $\langle P \mid P \rangle < 0$ for some $P \neq 0$, which would mean either: (i) the diagonal does not equal the bandwidth (violating C5's participation-measure identity), or (ii) the bandwidth is allowed to be negative (violating C2 directly).

Krein-space and Pontryagin-space structures (with indefinite metrics) arise in some physical contexts (e.g., gauge-theory ghosts, indefinite-metric quantization). They are not consistent with a substrate in which the primitive structural quantity is non-negative bandwidth. C2 is violated.

### 8.4 A4 — Non-orthogonal decomposition rules

**Claim.** Decompositions of the participation manifold that fail to reflect the four-band orthogonality structure violate C2's primitive band decomposition.

**Argument.** The four-band decomposition of bandwidth (C2 §1.5) gives mutually exclusive structural roles to the four bands. A decomposition rule that lumps internal and environmental bands together — or splits a single band across different decomposed pieces — would introduce content beyond what the substrate primitives supply. The inner-product orthogonality structure must lift the substrate-level band orthogonality directly. C2 is violated by any decomposition rule that obscures this.

### 8.5 A5 — Correlation rules allowing $|S| > 2\sqrt{2}$

**Claim.** Any rule giving $|S| > 2\sqrt{2}$ must violate either the inner-product structure (forced in §7.1) or the unit-norm observable structure.

**Argument.** The Landau-Khalfin algebra of §7.2 has no slack: $\hat{S}^2 = 4\mathbb{1} + [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}]$, with operator norms $\|[\sigma_a, \sigma_{a'}]\| \leq 2$ and $\|[\sigma_b, \sigma_{b'}]\| \leq 2$. The bound $\|\hat{S}\| \leq 2\sqrt{2}$ is therefore tight on any participation manifold equipped with the sesquilinear inner product and unit-norm Hermitian observables.

A rule giving $|S| > 2\sqrt{2}$ would have to violate one of:
- The inner-product structure (excluded by §7.1's forcing).
- The unit-norm observable structure (i.e., $\|\sigma_a\| > 1$). Unit norm is forced by the binary $\pm 1$ outcomes of measurement-setting observables: $\sigma_a^2 = \mathbb{1}$ implies $\|\sigma_a\| = 1$.
- The Cauchy-Schwarz inequality (which holds universally on inner-product spaces).

None of these is available. $|S| > 2\sqrt{2}$ is structurally excluded.

### 8.6 A6 — PR-box correlations

**Claim.** PR-box correlations are not realizable on any inner-product space; they are excluded by the substrate-derived inner product structure.

**Argument.** A PR-box is a correlation table satisfying no-signaling and $|S| = 4$. Mathematically, a PR-box assigns outcome probabilities $P(s_A, s_B \mid a, b) = 1/2$ when $s_A \oplus s_B = a \cdot b$ (XOR product) and zero otherwise. This table cannot be reproduced by any density operator on any inner-product space: the algebraic constraint $\hat{S}^2 = 4\mathbb{1} + [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}]$ caps $|S|$ at $2\sqrt{2}$.

PR-boxes are post-quantum correlation tables defined abstractly; they are not implementations on a physical substrate. The forcing argument of §7.1 establishes that any physical substrate satisfying C1-C6 supports only the sesquilinear inner product, and the Landau-Khalfin algebra of §7.2 then caps CHSH at $2\sqrt{2}$. PR-box realizations are excluded structurally — not by an additional postulate, but by the same inner-product structure that forces Tsirelson.

### 8.7 A7 — Non-$U(1)$-respecting inner products

**Claim.** Inner products that fail to respect the substrate-level $U(1)$ polarity structure violate C3.

**Argument.** The substrate primitive supplying angular content is polarity, valued in $U(1)$. The inner product is built from substrate quantities, and must therefore respect the same angular structure. A pairing introducing integer windings $\pi_K \to n\pi_K$ ($n \neq 1$) would require a primitive-level integer $n$ to be supplied — but no such primitive exists. A pairing introducing angular content beyond $U(1)$ (e.g., $SU(2)$ phase rotations) would require a higher-dimensional angular primitive — but C3 supplies only $U(1)$.

Inner products on the participation manifold inherit the substrate's angular structure exactly. Anything else violates C3.

### 8.8 B1 — Classical hidden-variable models (CHSH $\leq 2$)

**Claim.** LHV models reproduce only the classical bound, not the full quantum content.

**Argument.** Local hidden-variable models assume that each subsystem's measurement outcome is a function of local hidden variables and the local measurement setting, with no non-local correlation channel. Bell's theorem shows that such models cannot exceed $|S| = 2$. The Tsirelson bound at $2\sqrt{2}$ is a strictly stronger statement: it allows correlations up to $2\sqrt{2}$ via entangled joint participation measures, which are non-factorizable structures at the substrate level (Paper #1's participation measure extended bipartitely).

LHV models are excluded from reproducing the full forcing of this paper because they cannot account for the structurally available correlations between $2$ and $2\sqrt{2}$ that are empirically observed. They are *consistent* with the classical bound (which the forcing argument also reproduces, for factorizable joint participation) but cannot reach the quantum bound, which experiments confirm.

### 8.9 B2 — PR-box / superquantum models

**Claim.** Superquantum correlations are excluded by the same forcing chain that produces Tsirelson; see A6.

**Argument.** Identical to A6. PR-boxes and superquantum correlation tables more generally assign $|S| > 2\sqrt{2}$. The Landau-Khalfin algebra rules these out structurally: no participation manifold supports them.

Information-causality and macroscopic-locality programs derive Tsirelson from generalized-probabilistic-theory considerations; the forcing chain of this paper derives it from substrate primitives. The two approaches converge on the same exclusion.

### 8.10 B3 — Bohmian correlation rules

**Claim.** Bohmian theory reproduces the standard quantum Tsirelson bound but does not derive it from a substrate.

**Argument.** Bohmian mechanics supplements the standard Hilbert space with non-local hidden trajectories guided by the phase gradient. Bell correlations are produced by the non-local guiding equation, with $|S| \leq 2\sqrt{2}$ matching the standard quantum value. Bohmian theory takes the Hilbert space, inner product, and operator structure as given; the Tsirelson bound emerges from the same operator algebra as in standard quantum mechanics.

Under the substrate-conditions test of this paper, Bohmian theory is *downstream* of the forcing chain rather than an alternative to it. It takes a position on hidden-variable ontology, not on where the inner-product structure or the Tsirelson bound come from. Not in the alternative-encodings space for the forcing question.

### 8.11 B4 — GRW / CSL correlation rules

**Claim.** Spontaneous-collapse models preserve the standard Tsirelson bound; they do not derive it from substrate primitives.

**Argument.** GRW and CSL modify the dynamics of the wavefunction by adding stochastic collapse mechanisms, but preserve the standard $|\psi|^2$ rule and the standard Hilbert-space inner product. The Tsirelson bound is inherited from the unchanged operator algebra. As with Bohmian theory, GRW/CSL is downstream of the forcing chain, taking the inner product as given.

### 8.12 B5 — Real-vector-space QM

**Claim.** Stueckelberg-class real-vector-space QM is structurally equivalent to standard complex QM once the auxiliary $J$-operator is identified with $i$.

**Argument.** The standard complex Hilbert space is rewritten as a real vector space with an auxiliary $J$ ($J^2 = -1$). The inner product becomes the real-bilinear form on the doubled real space combined with $J$-multiplication, reproducing the standard sesquilinear inner product. Tsirelson follows from the same operator algebra. Either $J = i$ (in which case we have the standard forced answer) or $J$ is an additional structural commitment unsupported by primitives (in which case Stueckelberg's program is not realized on the substrate).

### 8.13 B6 — Quaternionic QM correlations

**Claim.** Quaternionic inner products are excluded at the carrier level by Paper #1; the quaternionic Tsirelson bound has the same value or is structurally different depending on how the inner product is defined.

**Argument.** Paper #1 establishes that the amplitude carrier is uniquely $\mathbb{C}$-valued — quaternions have $SU(2)$ angular structure exceeding what polarity supplies. With $\mathbb{H}$ excluded at the carrier level, the question of quaternionic inner products does not arise on the substrate.

Even if one accepted quaternionic amplitudes postulationally, the quaternionic Tsirelson bound is mathematically equivalent to a higher-dimensional complex bound under standard embeddings — there is no genuinely different ceiling. Adler's program also notes composition pathologies in multi-particle quaternionic settings that prevent the construction from extending coherently to bipartite Bell experiments.

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 bilinear real IP | C3 | Discards imaginary content; fails global $U(1)$-invariance. |
| A2 non-sesquilinear pairings | C3 | Complex-bilinear forms violate diagonal $U(1)$-invariance; asymmetric forms violate conjugate symmetry. |
| A3 non-positive IP | C2 | Diagonal must equal non-negative bandwidth; indefinite metrics forbidden. |
| A4 non-orthogonal decomposition | C2 | Four-band orthogonality of bandwidth lifts to inner-product orthogonality. |
| A5 $\|S\| > 2\sqrt{2}$ rules | §7.2 algebra | Landau-Khalfin chain admits no slack; tight on participation manifold. |
| A6 PR-box correlations | inner-product structure | Not implementable on any inner-product space; $\hat{S}^2 = 4\mathbb{1} + [\sigma_a,\sigma_{a'}]\otimes[\sigma_b,\sigma_{b'}]$ caps $\|S\|$ at $2\sqrt{2}$. |
| A7 non-$U(1)$ IP | C3 | Inner product inherits substrate angular structure; no primitive supplies $\neq U(1)$ content. |
| B1 classical LHV | empirical | Capped at $\|S\| = 2$; cannot reach experimentally observed quantum values. |
| B2 PR-box / superquantum | inner-product structure | Same as A6. |
| B3 Bohmian | not in space | Adopts inner product as input; reproduces standard Tsirelson. |
| B4 GRW/CSL | not in space | Adopts inner product as input; preserves standard Tsirelson. |
| B5 Stueckelberg | collapses to forced | $J = i$ identification reduces to standard sesquilinear form. |
| B6 quaternionic | C3 (Paper #1) | Excluded at carrier level; multi-particle composition pathology. |

**The sesquilinear inner product $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$ and the Tsirelson bound $|S| \leq 2\sqrt{2}$ are the unique survivors.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier of this paper is identical to the empirical falsifier of the standard Tsirelson bound: any observed CHSH value $|S| > 2\sqrt{2}$ in a properly controlled Bell-CHSH experiment, exceeding statistical and systematic error.

Loophole-free Bell tests have measured $|S|$ values consistent with $2\sqrt{2}$ at the saturation level expected from quantum mechanics:

- Hensen et al. 2015 (Delft): loophole-free Bell test with entangled NV centers.
- Giustina et al. 2015 (Vienna): loophole-free Bell test with entangled photons.
- Shalm et al. 2015 (NIST): loophole-free Bell test with entangled photons.

All observed values are at or below the Tsirelson bound. No experiment has reproducibly observed $|S| > 2\sqrt{2}$. The forcing argument of this paper does not predict any sub-Tsirelson corrections or superquantum violations; it predicts exactly the standard bound.

### 9.2 Structural falsifier

A structural falsifier: construct a substrate satisfying C1-C6 (channel-primitive participation graph with bandwidth additivity, $U(1)$ polarity, commitment locality, participation-measure carrier, Born rule) but supporting a non-sesquilinear inner product, a non-positive inner product, or a correlation rule reaching $|S| > 2\sqrt{2}$.

The author's claim is that no such substrate exists. The exclusion chain in §8 is closed: each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

The inner product is upstream of essentially every quantitative quantum prediction beyond the Born rule. Three immediate exposures:

**Schrödinger evolution (Paper #4).** Stone's theorem on the participation-manifold Hilbert space requires the sesquilinear inner product as input. The unique linear unitary one-parameter group as the time-evolution generator is forced by Stone's theorem applied to this inner-product space. The inner-product result of this paper is therefore the substrate-side prerequisite for the Schrödinger forcing of Paper #4.

**Heisenberg uncertainty.** The standard $\Delta x \cdot \Delta p \geq \hbar/2$ inequality follows from Cauchy-Schwarz applied to the sesquilinear inner product, combined with the canonical commutation relation. Without the inner-product structure of this paper, the Heisenberg bound would not have its standard derivation.

**Loophole-free Bell tests.** Every Bell experiment to date measures correlations consistent with $|S| \leq 2\sqrt{2}$ and inconsistent with classical $|S| \leq 2$. The experimental signal for the forcing chain is the empirical realization of the Tsirelson bound — the structural-derivation result of this paper matches the strongest empirical constraint on quantum correlations.

The substrate-level inner product is what supports every quantitative bipartite-correlation prediction in quantum mechanics. Its empirical exposure is the entirety of Bell-correlation experiments.

---

## Appendix A — Full Derivation Chain and Glossary

### A.1 Sesquilinearity from $U(1)$ structure — explicit derivation

Define a candidate bilinear pairing on $\mathcal{P}$:
$$
B(P, Q) = \sum_K \sum_u K_{KK'}(u, u')\, P_K(u)\, Q_{K'}(u'),
$$
for some kernel $K_{KK'}(u, u') \in \mathbb{C}$. Substrate conditions constrain the kernel as follows.

**Step 1: Locality and channel-diagonal structure (from C2 four-band orthogonality + C1 channel primitivity).** The four-band orthogonality of bandwidth (C2 §1.5) and the channel-as-primitive structure (C1) require that the kernel be diagonal in both channel and locus:
$$
K_{KK'}(u, u') = \delta_{KK'}\,\delta_{uu'}\,k(K, u),
$$
for some weight $k(K, u)$. Off-diagonal kernel elements would correspond to cross-channel or cross-locus contributions to the inner product that have no substrate-level structural basis.

**Step 2: $U(1)$-invariance of the diagonal (from C3).** The diagonal $B(P, P) = \sum_K \sum_u k(K, u)\, P_K(u)^2$ must be invariant under $P_K \to e^{i\alpha} P_K$ (C3's polarity gauge). The substitution gives:
$$
B(P, P) \to e^{2i\alpha} \sum_K \sum_u k(K, u)\, P_K(u)^2,
$$
which is invariant only if $B(P, P) = 0$ for all $P$ — i.e., the bilinear form is degenerate. This is incompatible with the bandwidth identity $B(P, P) = \sum_K \sum_u b_K(u) > 0$ for non-zero $P$.

Therefore, a bilinear form with no conjugation cannot reproduce the bandwidth diagonal. The form must include conjugation in at least one slot.

**Step 3: Sesquilinear candidate.** Replace one slot with the complex conjugate:
$$
\langle P \mid Q \rangle = \sum_K \sum_u k(K, u)\, P_K^*(u)\, Q_K(u).
$$
Under $P_K \to e^{i\alpha} P_K$, $Q_K \to e^{i\beta} Q_K$:
$$
\langle P \mid Q \rangle \to e^{i(\beta - \alpha)} \langle P \mid Q \rangle.
$$
The diagonal $\alpha = \beta$ case gives invariance: $\langle P \mid P \rangle \to e^0 \langle P \mid P \rangle = \langle P \mid P \rangle$. C3 is satisfied.

**Step 4: Determining the weight $k(K, u)$ (from C5 + C2).** The diagonal must equal the substrate-level bandwidth: $\langle P \mid P \rangle = \sum_K \sum_u b_K(u) = \sum_K \sum_u |P_K(u)|^2$, by C5's participation-measure identity. Substituting into the sesquilinear candidate:
$$
\langle P \mid P \rangle = \sum_K \sum_u k(K, u)\, |P_K(u)|^2 = \sum_K \sum_u |P_K(u)|^2,
$$
which forces $k(K, u) = 1$ for all $K, u$ (modulo an overall constant absorbed into normalization conventions). The inner product is
$$
\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u)\, Q_K(u),
$$
with no remaining structural freedom. This is the standard counting-measure inner product.

The sesquilinear inner product is uniquely forced by substrate primitives. No additional structural commitment is introduced.

### A.2 Tsirelson bound — Landau-Khalfin algebra in full

The CHSH operator on the bipartite participation-manifold Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_B$ is
$$
\hat{S} = \sigma_a \otimes \sigma_b + \sigma_a \otimes \sigma_{b'} + \sigma_{a'} \otimes \sigma_b - \sigma_{a'} \otimes \sigma_{b'}.
$$

**Computing $\hat{S}^2$.** Expand:
$$
\hat{S}^2 = \sum_{\{a, a'\} \times \{b, b'\}}\,\pm\,(\sigma_a \otimes \sigma_b)(\sigma_{a'} \otimes \sigma_{b'}) + \text{diagonal terms}.
$$
The diagonal terms (where the same operator appears in both factors) give:
- $(\sigma_a \otimes \sigma_b)(\sigma_a \otimes \sigma_b) = \sigma_a^2 \otimes \sigma_b^2 = \mathbb{1}_A \otimes \mathbb{1}_B = \mathbb{1}$.

Each of the four diagonal terms contributes $\mathbb{1}$, with the signs $(+, +, +, -) \times (+, +, +, -) = (+, +, +, +)$ on the diagonal entries — sum $4\mathbb{1}$.

The off-diagonal terms involve products $(\sigma_a \otimes \sigma_b)(\sigma_{a'} \otimes \sigma_{b'}) = (\sigma_a \sigma_{a'}) \otimes (\sigma_b \sigma_{b'})$. Combining the eight off-diagonal pairs with their CHSH signs and using the antisymmetry $(\sigma_a \sigma_{a'} - \sigma_{a'} \sigma_a) = [\sigma_a, \sigma_{a'}]$:
$$
\sum_\text{off-diag} = [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}].
$$

Therefore:
$$
\hat{S}^2 = 4\mathbb{1} + [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}].
$$

**Bounding $\|\hat{S}^2\|$.** Operator-norm inequality:
$$
\|\hat{S}^2\| \leq 4 + \|[\sigma_a, \sigma_{a'}]\| \cdot \|[\sigma_b, \sigma_{b'}]\|.
$$
For unit-norm Hermitian operators $A, B$ with $\|A\|, \|B\| = 1$:
$$
\|[A, B]\| = \|AB - BA\| \leq \|AB\| + \|BA\| \leq 2 \|A\| \cdot \|B\| = 2.
$$
Therefore $\|[\sigma_a, \sigma_{a'}]\| \leq 2$ and $\|[\sigma_b, \sigma_{b'}]\| \leq 2$, giving:
$$
\|\hat{S}^2\| \leq 4 + 4 = 8 \implies \|\hat{S}\| \leq \sqrt{8} = 2\sqrt{2}.
$$

**Applying to the CHSH statistic.** For normalized $|P^{AB}\rangle$ with $\langle P^{AB} | P^{AB}\rangle = 1$:
$$
|S| = |\langle P^{AB} | \hat{S} | P^{AB}\rangle| \leq \|\hat{S}\| \cdot \langle P^{AB} | P^{AB}\rangle = 2\sqrt{2}.
$$
By Cauchy-Schwarz, this is the maximal CHSH value achievable on any inner-product space with the assumed structure.

**Saturation.** The singlet joint participation measure with measurement angles in the $\hat{x}$–$\hat{z}$ plane at $45°$ intervals saturates the bound: $|S| = 2\sqrt{2}$ exactly. Specific calculation in §7.2.

The Tsirelson bound is forced. Superquantum correlations ($|S| > 2\sqrt{2}$) require violating one of the inputs — either the inner-product structure (§7.1) or the unit-norm observable structure — neither of which is available given C1-C6.

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Primitive-level non-negative real-valued substrate quantity on each channel at each locus; additive across disjoint channel decompositions.
- **CHSH operator $\hat{S}$.** $\sigma_a \otimes \sigma_b + \sigma_a \otimes \sigma_{b'} + \sigma_{a'} \otimes \sigma_b - \sigma_{a'} \otimes \sigma_{b'}$; its expectation value on a joint state gives the CHSH statistic $S$.
- **CHSH statistic $S$.** $E(a, b) + E(a, b') + E(a', b) - E(a', b')$, the bipartite correlation functional whose maximum over LHV theories is 2 (classical bound) and over quantum theories is $2\sqrt{2}$ (Tsirelson bound).
- **Channel.** Primitive-level structural pathway in the participation graph; ontologically primitive.
- **Chain.** A persistent sequence of micro-events in the substrate.
- **Commitment.** Primitive-level discrete event at which multi-channel participation collapses to a single channel; the substrate-level mechanism producing observed outcomes. Commitment events are *local* (substrate-level no-signaling).
- **Conjugate symmetry.** $\langle P \mid Q \rangle = \overline{\langle Q \mid P \rangle}$ for all $P, Q$.
- **Correlation function $E(a, b)$.** $\langle P^{AB} \mid \sigma_a \otimes \sigma_b \mid P^{AB} \rangle$, the expected product of binary outcomes for setting pair $(a, b)$.
- **Event Density (ED).** The framework within which this paper is written.
- **FORCED.** A theorem-grade structural result derived from substrate primitives and standard mathematics, with no additional structural commitments.
- **Gleason's theorem.** Used in Paper #2; not directly invoked here.
- **Hilbert space.** Complete inner-product space. The participation manifold $\mathcal{P}$ equipped with the sesquilinear inner product of §7.1, completed in the induced norm topology, is a Hilbert space.
- **INHERITED.** Quantitative content (value, coefficient, normalization, labeling) used in the paper but not derived in it.
- **Inner product.** A pairing $\langle \cdot \mid \cdot \rangle : \mathcal{P} \times \mathcal{P} \to \mathbb{C}$ satisfying sesquilinearity, conjugate symmetry, and positivity.
- **Joint participation measure $P^{AB}_{K_A, K_B}(u_A, u_B)$.** Complex-valued object on the product of two subsystems' channel and locus indices. *Factorizable* if $P^{AB} = P^A \cdot P^B$; *non-factorizable* (entangled) otherwise.
- **Landau-Khalfin algebra.** The operator-algebraic derivation $\hat{S}^2 = 4\mathbb{1} + [\sigma_a, \sigma_{a'}] \otimes [\sigma_b, \sigma_{b'}]$ that bounds $\|\hat{S}\| \leq 2\sqrt{2}$. Originated in Landau 1987.
- **Locus $u$.** A point in the participation graph at which a chain participates.
- **No-signaling.** Marginal probability on one subsystem is independent of the measurement setting on the other. Substrate-level consequence of commitment locality (C4).
- **Participation graph.** The graph-like structure underlying the ED substrate.
- **Participation measure $P_K(u)$.** Complex-valued amplitude carrier $\sqrt{b_K(u)}\,e^{i\pi_K(u)}$ derived in Paper #1 and used as input here.
- **Polarity $\pi_K(u)$.** Primitive-level $U(1)$-valued angular variable on each channel at each locus.
- **Positivity.** $\langle P \mid P \rangle \geq 0$, with equality iff $P = 0$.
- **PR-box.** Popescu-Rohrlich correlation table satisfying no-signaling but achieving $|S| = 4$. Excluded by the inner-product structure on any physical substrate.
- **Sesquilinearity.** Bilinear-like form on a complex vector space that is linear in one slot and conjugate-linear in the other.
- **Substrate.** Pre-quantum layer of structure underlying the ED framework.
- **Tsirelson bound.** $|S| \leq 2\sqrt{2}$; the maximum CHSH value achievable by quantum theory, derived in §7.2 from the inner-product structure.

### A.4 Source-repository citations (for ED-internal readers)

The following internal sources contain extended technical content:

- `papers/U2_Inner_Product/paper_u2_inner_product.md` — original publication-grade U2 paper (predecessor genre).
- `arcs/U2/04_synthesis_and_verdict.md` — synthesis memo establishing U2 (sesquilinear inner product) as FORCED in the discrete regime.
- `arcs/U2/02_C3a_C3b_derivation.md` — C3a (automatic linearity) and C3b (forced sesquilinearity) derivations.
- `arcs/U2/03_C3c_discrete_regime.md` — discrete-regime closure of C3c (counting measure and pointwise pairing).
- `arcs/arc-foundations/bell_correlations_from_participation.md` — Bell/Tsirelson derivation from joint participation measures, including the Landau-Khalfin algebra.
- `walkthroughs/from_primitives_to_bell_tsirelson_bound.md` — public-facing walkthrough.
- `theorems/T11.md` — theorem-level index entry; status FORCED-unconditional, ratified 2026-04-26.

These are *not* required reading for the present paper.

---

*End of Paper #3.*
