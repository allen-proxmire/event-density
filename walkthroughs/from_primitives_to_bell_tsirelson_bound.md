# From Primitives to the Bell-Tsirelson Bound

## A Walkthrough of the Event Density Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1964, John Bell showed that any local hidden-variable theory must satisfy a specific inequality on correlations between distant measurements. In its CHSH form (Clauser, Horne, Shimony, Holt 1969), the inequality reads:

$$
|S| = |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \leq 2
$$

where E(a, b) is the correlation between measurement outcomes at two separated parties using settings a and b. Any local realist theory respects this bound.

Quantum mechanics violates it. Experiments confirm the violation. The standard quantum prediction for a maximally entangled state with optimal measurement angles is $|S| = 2\sqrt{2} \approx 2.828$.

In 1980, Boris Tsirelson proved that $2\sqrt{2}$ is not just one quantum prediction — it is the *maximum* value that any quantum correlation can produce. No quantum state, no measurement scheme, no clever protocol can push $|S|$ beyond $2\sqrt{2}$. The bound is sharp, the value is exact, and it has been measured in laboratories around the world to within experimental precision.

The Tsirelson bound is one of the deepest empirical structures in physics. It tells us that quantum correlations exceed classical correlations by a specific, finite amount — there is room to violate Bell's inequality, but only so much room. The number $2\sqrt{2}$ has no obvious physical interpretation. It does not appear in the formulation of quantum mechanics. It emerges from the mathematics of the bipartite Hilbert space when the CHSH operator is constructed and bounded.

The question this document addresses is: where does $2\sqrt{2}$ come from?

In standard quantum mechanics, the answer is: it falls out of the Hilbert-space structure plus the Cauchy-Schwarz inequality plus an operator-norm bound on the CHSH operator. That answer is technically correct, and Tsirelson's 1980 proof remains the canonical derivation. But it leaves the deeper structure unanswered. The Hilbert space is postulated. The inner product that makes Cauchy-Schwarz available is postulated. The bipartite tensor-product structure on $H_A \otimes H_B$ is postulated. Each of these is a separate axiomatic commitment, and the $2\sqrt{2}$ value is what those commitments produce when run through the CHSH operator.

The Event Density framework derives the Tsirelson bound from a smaller set of structural commitments about what reality is made of. The Hilbert-space structure, the inner product, and the bipartite tensor-product structure all emerge as forced consequences of the substrate ontology rather than being postulated. With those structures forced rather than assumed, Tsirelson's 1980 argument applies directly, and the $2\sqrt{2}$ value is no longer the output of a chain of postulates but the output of a chain of derived theorems.

The structural shape of this derivation is different from Born or Schrödinger. Born had T14's Cauchy argument as a substantive new derivation — the framework genuinely earns the squared exponent through a primitive-level argument. Schrödinger had the Galilean integration producing the factor of 1/(2m) — again a substantive new derivation step. Bell-Tsirelson is different. The framework's contribution here is upstream: it forces the Hilbert-space structure that Tsirelson's argument operates on. The argument itself, including the operator-norm bound that produces $2\sqrt{2}$, is mathematical physics that's already in the literature. What changes is the foundational status of the structures that argument requires.

That's worth being honest about. The Tsirelson bound is not a place where ED produces a new derivation step beyond standard quantum mechanics. It is a place where ED removes the postulational status of the structures that the standard derivation already uses. The $2\sqrt{2}$ value is now a derived consequence of the substrate ontology, all the way down.

The chain has four steps:

1. The participation measure form is forced by T14, giving the complex-valued structure on which Hermitian operators act.

2. The inner product is forced by U2, giving the participation-measure space its Hilbert-space structure.

3. The bipartite tensor-product structure on $H_A \otimes H_B$ is forced by extending U2 to multi-system arrangements — same primitive-level arguments, applied to the joint participation graph of separated chains.

4. With the Hilbert-space structure forced, Tsirelson's argument applies: Cauchy-Schwarz on the inner product plus operator-norm bounds on the CHSH operator produces $|S| \leq 2\sqrt{2}$ as the maximum quantum correlation.

Steps 1 and 2 are carried over from prior walkthroughs. Step 3 is new but lightweight — it extends U2's primitive-level arguments to bipartite systems without introducing new structural commitments. Step 4 is the standard Tsirelson argument, walked here for completeness because it's where the $2\sqrt{2}$ value actually emerges.

The structural payoff: $|S| \leq 2\sqrt{2}$ is what falls out of Cauchy-Schwarz applied to the inner product on the bipartite participation-measure Hilbert space, evaluated against the CHSH operator. The bound is a consequence of inner-product geometry plus operator algebra, both of which are derived structures in the framework rather than postulates.

---

## 2. The Primitives That Matter

The framework rests on substrate-level ontological commitments. The Bell-Tsirelson walkthrough uses the same working subset that Born and Schrödinger used:

**Micro-events.** Discrete acts of becoming, vertices in a graph spanning the event manifold.

**Participation.** The relation connecting micro-events. The participation graph's edges encode this relation. Participation is homogeneous — no vertex is privileged at the primitive level.

**Channels.** Stable subgraphs along which a chain can repeatedly instantiate its update rule. Channels are primitive ontological objects — their identity is intrinsic to the graph, not basis-relative.

**Bandwidth.** The graded measure of participation, supplied as a non-negative real edge weight. Bandwidth has a four-band orthogonal decomposition with conservation along chains.

**Polarity.** The U(1)-valued phase relation between a chain's update rule and the local ED-flow direction. Supplies the $e^{i\pi_K}$ phase in the participation measure.

**Commitment.** The discrete event in which a chain selects one channel from those available.

Two ingredients arrive as forced consequences of these primitives:

The participation measure form, $P_K = \sqrt{b_K}\cdot e^{i\pi_K}$, forced by T14. The Cauchy functional equation on bandwidth additivity fixes the square root; Frobenius's theorem on real division algebras fixes the complex-valued phase.

The sesquilinear inner product on the participation-measure space, forced by U2. The structural arguments — counting measure on channels and vertices, local pointwise pairing forced by four-band orthogonality plus non-contextuality plus kinematic/dynamic separation, sesquilinearity forced by U(1) invariance — give the U2 Hilbert space H its complete structure.

That's the same working set as before. The new question is what happens when there are two chains.

---

## 3. Forcing the Bipartite Hilbert Space

Bell's inequality concerns correlations between measurements on two separated systems. Alice has one system, Bob has another, and they perform measurements at spacelike separation. The CHSH form of the inequality involves four correlation values, each computed from joint measurement outcomes.

To talk about quantum correlations, we need a Hilbert space that describes the joint state of Alice's and Bob's systems together. In standard quantum mechanics, this is constructed as the tensor product $H_A \otimes H_B$ of the two single-system Hilbert spaces. The construction is postulated — it's what the standard formalism uses for composite systems.

The framework derives the bipartite tensor-product structure from the same primitive-level arguments that derived the single-system inner product. The argument is not new structural work — it's U2 applied to a joint system instead of a single system.

### 3.1 The bipartite participation graph

When two chains exist at spatial separation, the participation graph contains both. There is one graph $G$ with two distinguishable subgraphs $G_A$ and $G_B$ associated with Alice's and Bob's chains respectively. Each chain has its own available-channel set: $K_{\tau_A}(u)$ at Alice's locus, $K_{\tau_B}(v)$ at Bob's. Each has its own bandwidth assignments and polarity phases.

The joint participation measure on the bipartite system is constructed channelwise on the product structure. For a joint state describing Alice and Bob together, the participation measure has components indexed by pairs $(K_A, K_B)$ of channels — one from each chain's available-channel set:

$$
P_{K_A, K_B}(x_A, x_B) = \sqrt{b_{K_A, K_B}(x_A, x_B)} \cdot e^{i\pi(K_A, K_B, x_A, x_B)}
$$

This is T14 applied to the joint system. The Cauchy argument on bandwidth additivity runs identically — bandwidth on the joint system is a non-negative real edge weight on the joint graph, and additivity over disjoint joint-channel-pairs forces the square-root structure. The Frobenius argument on the phase runs identically — U(1)-valued polarity on the joint system supports the same complex-valued structure.

The joint participation-measure space $P_{AB}$ is the set of all such complex-valued arrays indexed by $(K_A, K_B)$ channel pairs and joint vertex configurations.

### 3.2 The bipartite inner product

U2's argument extends to the joint space without modification. The three pieces of U2 — linearity, sesquilinearity, specific aggregation form — each transfer.

**Linearity.** $P_{AB}$ is a complex vector space because the joint participation measures take values in $\mathbb{C}$, and complex-valued function spaces inherit complex-vector-space structure pointwise. Same argument as the single-system case.

**Sesquilinearity.** The diagonal-equals-bandwidth constraint forces the diagonal pointwise structure to be the squared modulus on the joint slot — same structural fact as the single-system case applied to the joint slot. The U(1) invariance argument eliminates complex-bilinear and reduces real-bilinear to a strictly weaker form, leaving sesquilinearity as the unique structure that survives. Band additivity confirms slot-wise additivity. All four sesquilinearity properties are forced by primitive-level inputs on the joint system.

**Specific form.** The aggregation arguments transfer:

Channel measure — counting measure on joint channel pairs $(K_A, K_B)$, forced by absence of primitive-level inter-channel-pair weighting plus the diagonal constraint.

Position measure — counting measure on joint vertex configurations $(u_A, u_B)$, forced by absence of primitive-level inter-vertex-pair weighting plus graph symmetry.

Local pointwise pairing — strict locality on the joint slot, forced by four-band orthogonality (now applied per chain), non-contextuality (per-channel-pair bandwidth is partition-independent on the joint structure), and kinematic/dynamic separation.

The bipartite inner product is:

$$
\langle P \mid Q \rangle_{AB} = \sum_{K_A, K_B} \sum_{u_A, u_B} P^{*}_{K_A, K_B}(u_A, u_B) \cdot Q_{K_A, K_B}(u_A, u_B)
$$

in the discrete regime, with the obvious continuum lift carrying the same conformal gauge structure as the single-system case.

### 3.3 The tensor-product structure

The bipartite Hilbert space $H_{AB}$ constructed this way is naturally isomorphic to the tensor product $H_A \otimes H_B$. The isomorphism is the standard one: a joint state $P_{K_A, K_B}(u_A, u_B)$ that factors as a product $P^A_{K_A}(u_A) \cdot P^B_{K_B}(u_B)$ corresponds to the tensor product $|P^A\rangle \otimes |P^B\rangle$, and general joint states are linear combinations of such factored states.

The inner product respects the tensor-product structure:

$$
\langle P^A \otimes P^B \mid Q^A \otimes Q^B \rangle_{AB} = \langle P^A \mid Q^A \rangle_A \cdot \langle P^B \mid Q^B \rangle_B
$$

This follows directly from the bipartite inner product's local pointwise structure: the joint product $P^{*}_{K_A, K_B}(u_A, u_B) \cdot Q_{K_A, K_B}(u_A, u_B)$ factorizes when both states factorize, and the sums over $(K_A, K_B)$ and $(u_A, u_B)$ decouple into separate sums over $A$ and $B$ variables.

Entangled states — states that don't factorize as $P^A \otimes P^B$ — exist in $H_{AB}$ exactly because the bipartite participation graph admits joint states that are not products of single-chain states. The framework doesn't forbid entanglement; it accommodates entanglement structurally as the natural consequence of joint participation graphs supporting non-factorizable bandwidth assignments.

### 3.4 What this delivers

The bipartite Hilbert space $H_{AB} = H_A \otimes H_B$ is now derived from the same primitive-level arguments that derived the single-system Hilbert space. No new structural commitment was introduced — U2's machinery extended to the joint system gives the tensor-product structure as a forced consequence.

Operators on $H_{AB}$ include local operators of the form $\hat{A} \otimes I_B$ (acting only on Alice's system) and $I_A \otimes \hat{B}$ (acting only on Bob's). Bipartite operators that mix the two systems, like $\hat{A}_1 \otimes \hat{B}_1 + \hat{A}_2 \otimes \hat{B}_2$, are linear combinations of these tensor products. The CHSH operator that drives Tsirelson's argument is built from such combinations.

---

## 4. The CHSH Operator and the Bell Inequality

With the bipartite Hilbert space in hand, the question is: what does the framework predict for correlations between measurements on Alice's and Bob's systems?

This section sets up the CHSH operator that encodes the Bell inequality, and shows where the bipartite structure enters.

### 4.1 The CHSH setup

Alice has two binary measurement settings, denoted $A$ and $A'$, each producing outcomes $\pm 1$. Bob has two binary measurement settings, $B$ and $B'$, each producing outcomes $\pm 1$. The four settings give four possible correlation experiments: $(A, B)$, $(A, B')$, $(A', B)$, $(A', B')$.

For each pair, the correlation $E(X, Y)$ is the expectation value of the product of outcomes:

$$
E(X, Y) = \langle XY \rangle
$$

The CHSH expression $S$ combines these four correlations:

$$
S = E(A, B) + E(A, B') + E(A', B) - E(A', B')
$$

Bell's inequality, derived under the assumption of local hidden variables, states that $|S| \leq 2$ for any local realist theory.

### 4.2 The CHSH operator in quantum mechanics

In quantum mechanics, each measurement setting is represented by a self-adjoint operator with eigenvalues $\pm 1$. Alice's settings are represented by $\hat{A}$ and $\hat{A}'$ on $H_A$; Bob's settings by $\hat{B}$ and $\hat{B}'$ on $H_B$. The correlation $E(\hat{X}, \hat{Y})$ for a joint state $|\psi\rangle \in H_{AB}$ is:

$$
E(\hat{X}, \hat{Y}) = \langle \psi | \hat{X} \otimes \hat{Y} | \psi \rangle
$$

The CHSH operator on $H_{AB}$ is:

$$
\hat{S} = \hat{A} \otimes \hat{B} + \hat{A} \otimes \hat{B}' + \hat{A}' \otimes \hat{B} - \hat{A}' \otimes \hat{B}'
$$

The CHSH expression $S = \langle\psi|\hat{S}|\psi\rangle$ is the expectation value of this operator in the joint state $|\psi\rangle$.

Note what's happening here. The CHSH operator is built from tensor products of single-system operators, summed and subtracted in the specific pattern Bell's analysis requires. The operator lives on $H_{AB}$. Computing $\langle S\rangle$ uses the bipartite inner product. The whole construction relies on the tensor-product Hilbert-space structure that Section 3 established.

In standard quantum mechanics, this construction is straightforward because the tensor-product structure is postulated. In the framework, the construction is identical but the underlying structure is now derived rather than postulated.

### 4.3 What the bound has to be

The Tsirelson bound asserts:

$$
|S| = |\langle \psi | \hat{S} | \psi \rangle| \leq 2\sqrt{2}
$$

for any normalized state $|\psi\rangle \in H_{AB}$ and any choice of self-adjoint $\pm 1$-eigenvalued operators $\hat{A}$, $\hat{A}'$, $\hat{B}$, $\hat{B}'$.

To prove this, we need to show that the operator norm of $\hat{S}$ is at most $2\sqrt{2}$:

$$
\|\hat{S}\| \leq 2\sqrt{2}
$$

because then $|\langle\psi|\hat{S}|\psi\rangle| \leq \|\hat{S}\|$ for any normalized state.

This is where Tsirelson's 1980 argument enters.

---

## 5. Tsirelson's Bound: The Operator Argument

The operator-norm bound $\|\hat{S}\| \leq 2\sqrt{2}$ is a result about self-adjoint operators on Hilbert spaces with specific algebraic properties. The derivation uses Cauchy-Schwarz, the spectral theorem, and the algebra of tensor products. None of these are framework-specific — they're standard mathematical physics that operates on the Hilbert-space structure regardless of how that structure was obtained.

Walking the argument here is worth doing because the $2\sqrt{2}$ value emerges in a specific way, and understanding where it comes from is part of understanding what the bound means.

### 5.1 Squaring the CHSH operator

Tsirelson's strategy is to compute $\hat{S}^2$ and bound it using operator algebra.

Starting from:

$$
\hat{S} = \hat{A} \otimes \hat{B} + \hat{A} \otimes \hat{B}' + \hat{A}' \otimes \hat{B} - \hat{A}' \otimes \hat{B}'
$$

Squaring requires expanding all sixteen cross terms. The key facts to use:

Each of $\hat{A}$, $\hat{A}'$, $\hat{B}$, $\hat{B}'$ is self-adjoint with eigenvalues $\pm 1$, so each squares to the identity:

$$
\hat{A}^2 = \hat{A}'^2 = I_A, \qquad \hat{B}^2 = \hat{B}'^2 = I_B
$$

Operators on different systems commute (they live on different tensor factors):

$$
[\hat{A} \otimes I, I \otimes \hat{B}] = 0, \qquad [\hat{A}' \otimes I, I \otimes \hat{B}'] = 0, \qquad \text{etc.}
$$

But $\hat{A}$ and $\hat{A}'$ do not generally commute on $H_A$, and similarly for $\hat{B}$ and $\hat{B}'$ on $H_B$. Their commutators $[\hat{A}, \hat{A}']$ and $[\hat{B}, \hat{B}']$ are non-trivial in general.

After expanding and using the squaring identities for the diagonal terms, the result is:

$$
\hat{S}^2 = 4\, I_A \otimes I_B - [\hat{A}, \hat{A}'] \otimes [\hat{B}, \hat{B}']
$$

The diagonal terms each contribute $\hat{A}^2 \otimes \hat{B}^2 = I \otimes I$, and there are four of them, giving $4\, I \otimes I$. The cross terms collect into the commutator product $[\hat{A}, \hat{A}'] \otimes [\hat{B}, \hat{B}']$ with the right sign structure from the $+,+,+,-$ pattern of the CHSH expression.

This is a remarkable identity. The square of the CHSH operator decomposes into a constant $4\, I \otimes I$ plus a term involving the commutators of the local operators. If the local operators commuted ($\hat{A}$ with $\hat{A}'$, $\hat{B}$ with $\hat{B}'$), the commutator term would vanish and $\|\hat{S}^2\| = 4$, giving $\|\hat{S}\| = 2$ — the classical Bell bound. The quantum violation comes from the non-commuting local operators.

### 5.2 Bounding the commutator term

The norm of $[\hat{A}, \hat{A}']$ is bounded using the fact that $\hat{A}$ and $\hat{A}'$ are self-adjoint with eigenvalues $\pm 1$. The commutator $[\hat{A}, \hat{A}'] = \hat{A}\hat{A}' - \hat{A}'\hat{A}$ is anti-Hermitian, and its norm satisfies:

$$
\|[\hat{A}, \hat{A}']\| \leq \|\hat{A}\hat{A}'\| + \|\hat{A}'\hat{A}\| \leq 2\, \|\hat{A}\|\, \|\hat{A}'\| = 2
$$

since $\|\hat{A}\| = \|\hat{A}'\| = 1$ (eigenvalues $\pm 1$ means the operator norm is 1). Similarly, $\|[\hat{B}, \hat{B}']\| \leq 2$.

For the tensor product:

$$
\|[\hat{A}, \hat{A}'] \otimes [\hat{B}, \hat{B}']\| = \|[\hat{A}, \hat{A}']\| \cdot \|[\hat{B}, \hat{B}']\| \leq 2 \cdot 2 = 4
$$

### 5.3 The $2\sqrt{2}$ bound

Combining Sections 5.1 and 5.2:

$$
\|\hat{S}^2\| \leq \|4\, I \otimes I\| + \|[\hat{A}, \hat{A}'] \otimes [\hat{B}, \hat{B}']\| \leq 4 + 4 = 8
$$

For a self-adjoint operator (which $\hat{S}$ is, as a real linear combination of self-adjoint tensor products):

$$
\|\hat{S}\|^2 = \|\hat{S}^2\| \leq 8 \quad \implies \quad \|\hat{S}\| \leq \sqrt{8} = 2\sqrt{2}
$$

This is the Tsirelson bound. For any normalized state $|\psi\rangle \in H_{AB}$:

$$
|\langle \psi | \hat{S} | \psi \rangle| \leq \|\hat{S}\| \leq 2\sqrt{2}
$$

The $2\sqrt{2}$ value emerges from two combined facts: the diagonal terms in $\hat{S}^2$ contribute $4$ (because there are four $\pm 1$-eigenvalued operators each squaring to $I$), and the operator-norm bound on the commutator product contributes another $4$. The square root produces $2\sqrt{2}$.

### 5.4 The bound is tight

The $2\sqrt{2}$ bound is sharp — there exist quantum states that saturate it. The maximally entangled Bell state:

$$
|\psi\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr)
$$

with measurement angles chosen at $45^\circ$ offsets between Alice and Bob, achieves $|S| = 2\sqrt{2}$ exactly. This is what experiments measure when they violate Bell's inequality: a value approaching $2\sqrt{2}$ from below, limited only by experimental noise and detector efficiency.

The tightness of the bound is what makes the Tsirelson value physically meaningful. It's not just an upper bound that quantum correlations happen to satisfy — it's the exact ceiling, achievable in principle and approached in practice.

### 5.5 What the argument required

Walking through Tsirelson's argument, several structural ingredients were used:

The bipartite Hilbert space $H_{AB}$ with its tensor-product structure (Section 3).

The inner product $\langle\psi|\hat{S}|\psi\rangle$ that lets us compute expectation values (U2).

The operator norm $\|\hat{A}\|$ on each Hilbert space, which the inner product induces.

The spectral theorem for self-adjoint operators with eigenvalues $\pm 1$, which gives the squaring identity $\hat{A}^2 = I$.

The tensor-product algebra that lets us compute $(\hat{A} \otimes \hat{B})^2 = \hat{A}^2 \otimes \hat{B}^2$ and $\|\hat{A} \otimes \hat{B}\| = \|\hat{A}\| \cdot \|\hat{B}\|$.

In standard quantum mechanics, every one of these ingredients is part of the postulated formalism. In the framework, every one is derived: the Hilbert space comes from U2, the inner product comes from U2, the tensor-product structure comes from the bipartite extension of U2, the operator norm comes from the inner product, and the algebra of self-adjoint operators is standard mathematical physics that operates on whatever Hilbert space it's given.

The $2\sqrt{2}$ bound is therefore a derived consequence of the substrate ontology, all the way down. The structures Tsirelson's argument requires are now forced rather than postulated.

---

## 6. What the Framework Adds

It's worth being precise about what changes when the framework is in place versus when it isn't.

In standard quantum mechanics, the Tsirelson bound is a theorem given the postulated formalism. The Hilbert space is postulated. The inner product is postulated. The bipartite tensor-product structure is postulated. Tsirelson's 1980 argument runs on these postulates and produces $2\sqrt{2}$ as a sharp upper bound on quantum correlations. The bound is real, the value is exact, and the argument is valid.

In the framework, the same Tsirelson argument runs on the same Hilbert-space structure — but that structure is now derived from a smaller set of substrate-level commitments rather than postulated as part of the formalism. The complex-valued participation measure is forced by T14. The inner product is forced by U2. The bipartite tensor-product structure is forced by U2 applied to joint participation graphs. Each step has its load-bearing argument, and no step introduces a separate axiomatic commitment about Hilbert spaces or inner products.

What this changes:

The $2\sqrt{2}$ value is no longer the output of a chain of postulates ending at "and these structures fit together with this much room for quantum correlations." It is the output of a chain of derived theorems beginning at the substrate primitives and producing the same value through the same operator-algebraic argument. The mathematical content of Tsirelson's proof is unchanged. What changes is the foundational status of the structures the proof operates on.

This is a smaller payload than what Born or Schrödinger's walkthroughs delivered. Born had T14's Cauchy argument as substantive new structural content — the framework genuinely earned the squared exponent through a primitive-level argument. Schrödinger had the Galilean integration producing the factor of 1/(2m) — again substantive new structural content. Bell-Tsirelson doesn't have a comparable hinge. The framework's contribution here is upstream: it forces the Hilbert-space structure that Tsirelson's argument requires.

That's an honest accounting. The Tsirelson bound is not a place where ED produces a new derivation step beyond standard quantum mechanics. It is a place where ED removes the postulational status of the structures the standard derivation already uses. For a reader who's already convinced that $2\sqrt{2}$ is the right answer and just wants to know why the underlying machinery is valid, this is what the framework offers: the machinery is no longer an article of faith. Every piece of the derivation traces back to substrate primitives.

For a reader interested in the deeper question of *why* quantum correlations exceed classical correlations by exactly this much — why $2\sqrt{2}$ rather than some other value — the framework's answer is the same as standard quantum mechanics: because Cauchy-Schwarz on a Hilbert space, applied to operators with the algebraic properties that $\pm 1$-eigenvalued self-adjoint operators have, on a tensor-product Hilbert space, produces this specific bound through this specific argument. The $2\sqrt{2}$ comes from the operator algebra, not from ED-specific structural commitments. ED ensures the Hilbert space is real; what happens on it is then standard mathematics.

This is a fair description of what the walkthrough delivers, and it's worth stating plainly rather than overselling.

---

## 7. The Place of This Result

The Bell-Tsirelson bound sits in a specific position in the framework's QM-emergence program.

The Born walkthrough established the probability rule of quantum mechanics from substrate primitives. The Schrödinger walkthrough established the dynamical evolution rule. Both involved substantive new derivation steps — Cauchy on bandwidth additivity in Born, Galilean integration in Schrödinger. They demonstrated that the framework can derive structural content rather than just rearranging it.

Bell-Tsirelson is a different kind of result. It doesn't introduce new structural derivation; it shows that an established consequence of the Hilbert-space structure — the $2\sqrt{2}$ ceiling on quantum correlations — survives and remains derivable when that Hilbert-space structure is itself derived rather than postulated. The result extends the framework's coverage to cover correlation experiments and Bell tests without requiring new machinery. U2 was already doing the work; this walkthrough just documents what U2 buys you for entangled systems.

The Heisenberg uncertainty inequality, $\Delta x \cdot \Delta p \geq \hbar/2$, has the same structural shape. It's a consequence of the Fourier-conjugacy of position and momentum, which is itself a consequence of U5's identification of $\hat{p}$ as the spatial-translation generator on the U2 Hilbert space. The framework forces the structures that the standard Fourier-uncertainty argument operates on; the bound itself is mathematical physics that's already in the literature. A walkthrough of Heisenberg would have the same character as this one: structural setup forced by substrate primitives, mathematical argument that produces the specific bound, payoff that the bound is now derived rather than postulated.

Together, Born, Schrödinger, Bell-Tsirelson, and Heisenberg cover all four foundational postulates of non-relativistic single-particle quantum mechanics. With this walkthrough, three of the four are in standalone form. The fourth (Heisenberg) follows the same pattern.

---

## 8. What This Argument Establishes

The chain runs:

Primitives (micro-events, participation, channels, bandwidth, polarity, commitment) → T14 (participation measure form forced) → U2 (inner product on single-system space forced) → bipartite extension of U2 (tensor-product Hilbert space $H_{AB}$ forced) → CHSH operator construction on $H_{AB}$ (standard quantum mechanics) → Tsirelson's argument: $\hat{S}^2 = 4\, I + (\text{commutator term})$, operator-norm bound $2$ on commutators, squared norm bound $8$ on $\hat{S}^2$, square root gives $\|\hat{S}\| \leq 2\sqrt{2}$.

The $2\sqrt{2}$ bound is now a derived consequence of substrate ontology rather than a consequence of postulated Hilbert-space structure. The mathematical content of Tsirelson's 1980 proof is unchanged — what changes is the foundational status of the Hilbert space the proof operates on.

The framework reproduces Bell-Tsirelson exactly. It does not predict any new violation pattern, any new bound, or any deviation from standard quantum correlations in regimes where standard quantum mechanics has been tested. Quantum correlations are bounded by $2\sqrt{2}$ in the framework just as in standard QM. What changes is that the bound is now traceable to the substrate primitives without invoking the Hilbert-space postulate.

For experimentally verified Bell-test violations, every value measured in laboratories — from Aspect's 1981 experiment through the loophole-free tests of 2015 and beyond — sits at or below $2\sqrt{2}$ within experimental precision. The framework predicts the same. The Tsirelson bound is not a place where ED differs from standard quantum mechanics; it's a place where ED derives the structures that produce the bound rather than assuming them.

Whether the substrate commitments themselves are right is a separate question, and as with Born and Schrödinger, it's the load-bearing one. The framework stands or falls on whether participation, bandwidth, channels, polarity, and the rest are the correct foundational concepts. The empirical exposure of the framework lives elsewhere — in the soft-matter mobility law's prediction of sub-Fickian recovery in concentrated BSA, in the substrate-gravity prediction of MOND's transition acceleration, in other channels where the framework makes predictions that depart from standard physics in regimes not yet tested.

For Bell-Tsirelson specifically, the structural case is closed. The $2\sqrt{2}$ bound is what Cauchy-Schwarz on the U2-derived bipartite Hilbert space produces when evaluated on the CHSH operator. The Hilbert space is no longer a postulate; the bound is no longer suspended above an axiomatic gap. Every piece traces back to substrate primitives.

Combined with Born and Schrödinger, three of the four foundational postulates of non-relativistic single-particle quantum mechanics are now derived. The fourth — Heisenberg uncertainty — follows the same pattern and would close the set.

---

## 9. References

- Bell, J. S. "On the Einstein Podolsky Rosen Paradox." *Physics Physique Физика* 1, 195–200 (1964).
- Clauser, J. F., Horne, M. A., Shimony, A., and Holt, R. A. "Proposed Experiment to Test Local Hidden-Variable Theories." *Physical Review Letters* 23, 880–884 (1969).
- Tsirelson, B. S. "Quantum generalizations of Bell's inequality." *Letters in Mathematical Physics* 4, 93–100 (1980).
- Aspect, A., Grangier, P., and Roger, G. "Experimental Tests of Realistic Local Theories via Bell's Theorem." *Physical Review Letters* 47, 460–463 (1981).
- Hensen, B., et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." *Nature* 526, 682–686 (2015).
- Proxmire, A. *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* April 2026.
- Proxmire, A. *The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion.* April 2026.
- Proxmire, A. *Theorem 14: The Participation Measure Form.* (T14 derivation memo.)
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
