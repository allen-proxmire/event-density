# From Primitives to the Born Rule

## A Walkthrough of the Event Density Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

Quantum mechanics says: when you measure a system, the probability of an outcome is the squared modulus of that outcome's amplitude.

Squared. Not absolute value, not cubed, not some other power. The exponent is two, and it has been two since Born wrote it down in 1926.

For a hundred years, this has been a postulate. The Copenhagen formulation accepts it as a brute fact about how the world works. Many-Worlds tries to derive it from decision theory. QBism reframes it as Bayesian credence. Zurek derives it from environmental symmetries. Hardy derives it from operational axioms about probability. Each program has its strengths, and each leaves at least part of the question unanswered: *why squared, and not some other exponent?*

Gleason's 1957 theorem went part of the way. If you accept a few structural conditions about how probabilities can be assigned to quantum measurement outcomes, the squared form is mathematically forced. There is no other consistent choice. But Gleason's theorem leans on one substantive assumption: non-contextuality. The probability of an outcome cannot depend on which other outcomes happen to be in the surrounding measurement context. It can only depend on the outcome itself.

Standard quantum mechanics postulates non-contextuality. It seems true experimentally, and assuming it makes the math work. But nothing about standard quantum mechanics's underlying ontology *forces* it. It is an extra ingredient, not a derived consequence.

This document walks through how the Event Density framework derives the Born rule — including the squared exponent and the non-contextuality assumption underneath it — from a smaller set of structural commitments about what reality is made of. The derivation has three load-bearing steps, taken from three companion papers, and this is the first time they have been assembled into a single self-contained narrative.

The three steps:

1. The participation measure is forced to have the form √b · e^(iπ). This is where the squared exponent enters. The Cauchy functional equation on bandwidth additivity forces the square root; the Frobenius theorem on real division algebras forces the complex-valued phase.

2. The sesquilinear inner product on the participation-measure space is forced. This delivers the Hilbert-space structure that Gleason's theorem operates on. No new commitment is introduced beyond what's already in the primitives.

3. Non-contextuality of the bandwidth-fraction probability rule is forced by the channel-as-primitive ontology. With non-contextuality forced rather than postulated, Gleason's theorem (and Busch's 2003 extension covering qubits) applies directly. The Born rule follows.

That's the chain. Each step has its own argument, each step is written out below, and at the end the squared exponent is a consequence of the framework rather than a separate postulate.

---

## 2. The Primitives That Matter

Event Density is built on a small set of primitive ontological commitments. Most of them aren't needed for this derivation. The ones that are:

**Micro-events.** Reality consists of discrete acts of becoming. Each micro-event is a vertex in a graph that spans the event manifold.

**Participation.** Micro-events don't exist in isolation; they participate in one another's becoming. Participation is the relation that connects micro-events. The graph's edges encode participation relations between vertices.

**Channels.** A channel is a stable subgraph along which a chain (the substrate-level object that the framework calls a "particle") can repeatedly instantiate its update rule. Channels are *primitive ontological objects* — their identity is intrinsic to the graph, not a basis-relative label imposed from outside. A channel either exists as a graph substructure or it does not. Two observers looking at the same graph with different labeling conventions see the same channels.

**Bandwidth.** Bandwidth is the graded measure of participation, supplied as a non-negative real edge weight. Each channel K at vertex u has a bandwidth b_K(u), computed as an edge-weight integral along K's edges incident to u. Bandwidth admits a four-band orthogonal decomposition (internal-rule, adjacency, environmental, commitment-reserve) with conservation along chains.

**Polarity.** Polarity is the U(1)-valued phase relation between a chain's update rule and the local ED-flow direction. It supplies the phase content that, in the participation measure, becomes the e^(i$\pi_K$) factor. Polarity is *phase-valued*, not scalar — this is a structural commitment, not a representational choice.

**Commitment.** Commitment is the discrete event in which a chain selects one channel from those available at a vertex. Selection is probabilistic, weighted by channel bandwidth. Commitments are irreversible: once made, never unmade.

That's the working set. From these alone, the derivation runs.

A note on what's *not* in the working set. The framework has primitives for thickening (the accumulation of commitments into smooth continuum manifolds), individuation, Lorentz covariance, and other items needed elsewhere in the program. None of them enter the discrete-regime Born derivation. The continuum lift uses thickening, but only to identify the manifold on which the inner product is defined — the structural argument runs through without it.

---

## 3. Forcing the Participation Measure: √b · e^(iπ)

The participation measure is the framework's central complex-valued object:

$$
P_K(x, t) = \sqrt{b_K}(x, t) \cdot e^{i\pi(K, x, t})
$$

This equation is doing enormous work. The square root is what generates the squared exponent in the Born rule. The complex-valued phase is what makes interference possible. If either piece were a free choice — if you could equally well write P = b · e^(iπ) or P = √b · e^(2iπ) without breaking anything — then the squared exponent in the Born rule would be a downstream consequence of an upstream choice, and the framework wouldn't be deriving it any more than standard QM does.

The claim is that both pieces are *forced* by primitive-level structural commitments. Here's the argument.

### 3.1 The Cauchy step: forcing the square root

Bandwidth admits a structural relation to amplitude through the participation measure. The question is what relation. Suppose we don't yet know whether b = |P|^n for some exponent n, and we want to derive n from the primitives.

Consider two channels K_1 and K_2 with disjoint support. Their bandwidths combine additively:

$$
b(K_1 \cup K_2) = b(K_1) + b(K_2)
$$

This additivity is forced by Primitive 04. Bandwidth is an edge-weight on disjoint subgraphs; the bandwidth of a union of disjoint subgraphs is the sum of their bandwidths. Disjoint sets of edges have additive total weight. Nothing controversial here.

Now suppose b = f(|P|) for some monotonic continuous function f. Then the additivity of bandwidth on disjoint channels imposes:

$$
f(|P_1 + P_2|) = f(|P_1|) + f(|P_2|)
$$

— *when* the channels are orthogonal in the sense that their cross-coherence vanishes. For orthogonal channels with cross-coherence c_{12} = 0, the magnitude of the combined participation measure satisfies |P_1 + P_2|² = |P_1|² + |P_2|².

Substituting m_i = |P_i|², the additivity equation becomes:

$$
f(\sqrt{m_1 + m_2}) = f(\sqrt{m_1}) + f(\sqrt{m_2})
$$

Letting g(m) = f(√m), this reduces to:

$$
g(m_1 + m_2) = g(m_1) + g(m_2)
$$

This is the Cauchy functional equation. Its monotonic, continuous solutions are exactly the linear functions: g(m) = c·m for some constant c > 0. Therefore f(|P|) = c·|P|², which means:

$$
b = c \cdot|P|^{2}
$$

The constant c can be absorbed into the amplitude normalization without loss of generality, leaving b = |P|², or equivalently P = √b · e^(iπ) up to phase.

The exponent 2 is not chosen. It is the unique solution to the functional equation that's compatible with how independent channels' bandwidths compose. Any other exponent — 1, 3, π, anything — would violate either bandwidth additivity or amplitude composition for orthogonal channels. The squared form is forced at the participation-measure level, before any quantum-mechanical structure has entered the picture.

This is the philosophically distinctive step in the framework. Most other derivations of the Born rule don't address why the exponent is 2; they show that some structural commitment forces a probability rule, but the squared form ends up encoded in the Hilbert-space machinery that gets assumed at the start. Here the exponent emerges from a Cauchy argument on bandwidth itself, before any Hilbert space appears.

### 3.2 The Frobenius step: forcing the complex phase

The square root is half the participation measure. The other half is the phase factor e^(i$\pi_K$). We need this to be complex-valued, not real-valued or quaternionic, and we need an argument that forces it.

Polarity (Primitive 09) supplies a phase relation between a chain's update rule and the local ED-flow direction. The question is what algebraic structure that phase lives in.

Three structural requirements pin it down:

The phase must support magnitude composition that's compatible with bandwidth additivity (just established). The phase factor's modulus must be 1 — otherwise it would contribute to the magnitude and wreck the b = |P|² relation.

The phase must support a continuous symmetry. Polarity is U(1)-valued by Primitive 09, meaning it admits continuous rotation. Discrete phases (like ±1) don't satisfy this.

The phase must support interference. Two channels with the same bandwidth but different phases must be able to combine constructively or destructively, producing the observed interference patterns of standard QM.

Frobenius's theorem on real associative division algebras states that the only finite-dimensional real associative division algebras are R, C, and H (the quaternions). The phase has to live in one of these.

R is eliminated because it doesn't support a U(1) symmetry — a real-valued phase admits only the trivial discrete symmetry ±1. C is preserved. H is eliminated because the U(1) embedding in H is not unique and introduces additional structure (left-right multiplication asymmetry) that the primitives don't support; moreover, H lacks the commutativity required for the additive composition of phases that interference demands.

The phase factor is therefore complex-valued, e^(i$\pi_K$) ∈ U(1) ⊂ C.

### 3.3 Putting it together

The participation measure is:

$$
P_K(x, t) = \sqrt{b_K}(x, t) \cdot e^{i\pi(K, x, t})
$$

The square-root structure is forced by the Cauchy functional equation on bandwidth additivity. The complex-valued phase is forced by Frobenius plus the U(1) symmetry of polarity. Neither piece is a chosen convention — both are uniquely determined by the primitive structure.

This is what the framework calls Theorem 14. It is the upstream structural foundation on which everything else in the Born derivation rests.

---

## 4. Forcing the Inner Product

With the participation measure fixed, the next step is the inner product. Quantum mechanics is conventionally formulated as a theory of vectors in a complex Hilbert space, with a sesquilinear inner product that takes two states and returns a complex number. Standard QM postulates this structure. We need to derive it.

The inner product to derive is:

$$
\langle P | Q\rangle= \sum_K \sum_u P*_K(u) \cdot Q_K(u)
$$

(in the discrete regime; the continuum version replaces the sum over u with an integral over the manifold).

This packages three structurally distinct claims:

**Linearity.** The participation-measure space P forms a complex vector space under componentwise addition and scalar multiplication.

**Sesquilinearity.** The inner product is conjugate-linear in the first argument, linear in the second, conjugate-symmetric, and positive-definite on the diagonal.

**Specific form.** The aggregation is by counting measure on channels and vertices, with strictly local pointwise pairing (no cross-slot kernels).

Each is established separately.

### 4.1 Linearity is automatic

The participation measure produces complex values at each (K, u) slot:

$$
P_K(u) = \sqrt{b_K}(u) \cdot e^{i\pi(K,u}) \in C
$$

The space P is the set of all such arrays — equivalently, complex-valued functions on the (channel, vertex) product space. Componentwise sum and complex-scalar multiplication on a function space valued in a field inherit all field axioms pointwise from the codomain. C is a field, so all complex-vector-space axioms hold for P automatically.

There's nothing to force here. The complex-valued construction of T14 directly delivers a complex vector space.

### 4.2 Sesquilinearity is forced

We need a pairing $\langle \cdot| \cdot \rangle$ : P × P → C satisfying:

- Conjugate-linearity in the first argument
- Linearity in the second argument
- Conjugate symmetry
- Positive-definiteness on the diagonal

The argument runs in three steps.

**Step A: the diagonal is forced to be the squared modulus.**

The diagonal pairing must reproduce bandwidth, since bandwidth is the diagonal norm-squared by T14. For P_K(u) = a + ib, this requires the diagonal pointwise function to satisfy f(a + ib) = a² + b². The unique pointwise function on C (up to overall positive scaling) satisfying this is the squared modulus, equivalent to the complex-conjugate product P*_K(u) · P_K(u). This forces the diagonal pointwise structure. Positive-definiteness follows automatically from non-negativity of bandwidth.

**Step B: U(1) invariance eliminates non-sesquilinear alternatives.**

Polarity is U(1)-valued. The participation measure carries the phase factor e^(i$\pi_K$). Bandwidth is invariant under global phase rotation P → e^(iα)P:

$$
|e^{i\alpha} P_K(u)|^{2} = e^{-i\alpha} e^{i\alpha} |P_K(u)|^{2} = |P_K(u)|^{2} = b_K(u)
$$

This is structural: the inner product's diagonal must respect global phase invariance because bandwidth does.

Three candidate pairing types are tested against this constraint:

*Complex-bilinear* (linear in both slots): Under global rotation, β(e^(iα)P, e^(iα)P) = e^(2iα) β(P, P). For this to equal β(P, P) for arbitrary α requires β(P, P) = 0 — meaning the diagonal would have to vanish, which contradicts the diagonal-equals-bandwidth requirement. Eliminated.

*Real-bilinear* (treating C as R² and bilinear over R): The most general such pairing has four free parameters. Demanding U(1) invariance forces the form to reduce to a · Re(z*w), the real part of the sesquilinear pairing. But physical interference depends on both Re(P*Q) and Im(P*Q). The imaginary part encodes the relative-phase content underlying interferometry, Bell correlations, and Fourier-uncertainty. A U(1)-invariant real-bilinear pairing is strictly weaker than sesquilinearity and cannot encode the full physical content of the framework. Eliminated.

*Sesquilinear* (conjugate-linear in first slot, linear in second): Under global rotation, $\langle e^{i\alpha}P | e^{i\alpha}Q\rangle$ = e^(-iα) e^(iα) $\langle P|Q\rangle=\langle P|Q\rangle$. Both diagonal and off-diagonal pairings are U(1)-invariant under global rotation, and the off-diagonal preserves relative-phase information in the imaginary part. Survives.

Sesquilinearity is the unique structure that survives U(1) invariance and supports interference.

**Step C: band additivity confirms slot-wise additivity.**

For two participation measures with disjoint support, the diagonal pairing of their sum decomposes as $\langle P+Q|P+Q\rangle=\langle P|P\rangle$ + $\langle Q|Q\rangle$, since the cross-terms vanish by disjoint support. This forces additivity in each slot. Combined with Step B's selection of sesquilinear over bilinear, additivity-in-each-slot yields conjugate-linearity in the first slot and linearity in the second. Conjugate symmetry follows algebraically.

All four sesquilinearity properties are forced by primitive-level inputs. No new commitment is introduced.

### 4.3 The specific form is forced

What remains is the aggregation form: how the inner product sums over channels, how it sums over vertices, and whether the basic pairing is strictly local.

**Channel measure:** Could the channel-aggregation be $\sum_K$ w(K) · ... for some non-trivial weight w? A non-trivial weight would have to be a structural feature distinguishing channels beyond bandwidth itself. Within the primitive stack, no such feature exists. Bandwidth is already in the slot value; rule-type doesn't distinguish channels within Kτ(u) by definition; channel topology is intrinsic but supplies no measure-theoretic weighting; environmental coupling is captured in the four-band decomposition. No primitive-level source supplies a non-trivial w(K). The diagonal-equals-bandwidth constraint independently forces w(K) = 1. Counting measure on channels is forced.

**Vertex measure:** Same structure of argument. Could the vertex-aggregation be $\sum_u$ w(u) · ... for some non-trivial weight? Candidate alternatives — local event density, local total bandwidth, vertex multiplicity — each conflict with the diagonal constraint. Independently, the participation graph is built from primitive vertices that are individuated by identity but otherwise primitively equivalent under graph automorphism; a non-counting measure assigning different weights to isomorphic vertices would violate this primitive-level equivalence. Counting measure on vertices is forced in the discrete regime.

**Local pointwise pairing:** The most general sesquilinear pairing consistent with counting measures is:

$$
\langle P|Q\rangle= \sum_{K,K'} \sum_{u,u'} P*_K(u) \cdot K(K, K'; u, u') \cdot Q_{K'}(u')
$$

with kernel K(K, K'; u, u'). The local pointwise form has K = $\delta_{KK'}$ $\delta_{uu'}$. Three independent arguments forbid non-trivial off-diagonal kernel components.

*Four-band orthogonality* (forbids cross-band terms): Primitive 04 establishes four orthogonal bandwidth bands. The inner product must respect this orthogonality; cross-band kernel components would generate cross-band coherences in $\langle P|P\rangle$ that violate primitive-level orthogonality.

*Non-contextuality* (forbids same-band cross-channel terms): Per-channel bandwidth is partition-independent (Section 5 below). A non-zero cross-channel kernel within a band would make the inner product depend on inter-channel coherences, reintroducing contextuality.

*Kinematic/dynamic separation* (forbids cross-vertex terms): Inner products encode kinematic content (norms, orthogonalities, probabilities at a single time). Time-evolution and propagation are encoded separately, in the participation-measure evolution equation. A non-local kernel coupling distinct vertices would conflate kinematics with dynamics.

The three arguments combine to force the local Kronecker-delta structure. The discrete inner product is:

$$
\langle P|Q\rangle= \sum_K \sum_u P*_K(u) \cdot Q_K(u)
$$

### 4.4 The continuum and the conformal gauge

The continuum lift extends this to manifolds emerging from thickening of the participation graph. Most of the lift is direct: channel aggregation transfers cleanly, local pointwise pairing transfers cleanly. The substantive question is the position measure.

In the continuum, b_K(x) becomes a density — a value per unit volume — and densities require a reference measure to be defined. The combination b_K(x) · dμ(x) is the well-defined invariant inherited from the discrete edge-weight integral. The separate factors are co-defined and admit a one-parameter rescaling:

$$
(b_K(x), d\mu(x)) \to(\Omega^(-D)(x) \cdot b_K(x), \Omega^D(x) \cdot d\mu(x))
$$

Under this rescaling, the participation measure transforms as P_K → Ω^(-D/2) P_K, and every inner-product value is exactly invariant:

$$
\langle P|Q\rangle' = \sum_K \int(\Omega^D d\mu)(\Omega^(-D/2) P_K)*(\Omega^(-D/2) Q_K) = \sum_K \int d\mu \cdot P*_K Q_K = \langle P|Q\rangle
$$

This is a gauge structure. It's a description redundancy, not a physical ambiguity. Different observers using conformally-related (b_K, dμ) pairs compute identical inner products for identical states. Born probabilities, Bell correlations, and Heisenberg variances all depend only on conformally-invariant ratios or inner-product overlaps; the bare expressions for b_K(x) and dμ(x) carry the gauge, but their physical content does not.

The structural pattern is familiar. Weyl rescaling in conformal field theory, lattice-spacing renormalization in lattice QFT, coordinate freedom in general relativity — each carries a description redundancy that's named explicitly and either fixed by convention or quotiented out. None of these frameworks is considered "not derived" because of the redundancy. The continuum inner product sits in the same family.

The conformal class of dμ — meaning, which volume forms count as equivalent up to rescaling — is fixed by the bandwidth-gradient ratio structure of the acoustic metric. What's gauge is the choice of representative within the class. The framework is structurally complete.

---

## 5. Forcing Non-Contextuality

With the participation measure forced (Section 3) and the inner product forced (Section 4), Hilbert-space structure is in hand. Gleason's theorem can now be invoked — but only if non-contextuality is forced rather than postulated. This is the load-bearing step that distinguishes ED's Born derivation from Gleason's original 1957 result.

### 5.1 What Gleason's theorem requires

Gleason's theorem states: any frame function on the lattice of closed subspaces of a Hilbert space of dimension d ≥ 3, satisfying non-negativity, normalization, and σ-additivity, is necessarily of the form Tr(ρP) for some unique density operator ρ.

The non-contextuality content is built into the typing of the frame function: f(P) depends on P alone, not on which orthogonal resolution P appears in. Standard quantum mechanics postulates this typing as an operational fact about measurement outcomes. Gleason's theorem then uses it to derive the squared-amplitude form.

But postulating non-contextuality is not the same as deriving it. The framework's claim is that ED's primitive ontology forces the typing rather than postulating it.

### 5.2 The argument

The argument has three premises:

**P-Channel** (from the channel primitive). A channel K is a subgraph (V_K, E_K) ⊂ G of the participation graph. Its identity is intrinsic to the graph and does not depend on any external decomposition of K_τ(u) in which K appears.

**P-Bandwidth** (from the bandwidth primitive). The bandwidth b_K(u) is the integrated edge-weight along K's edges incident to vertex u. It is a function of the (channel-subgraph K, vertex u) pair, computed from the graph's edge weights at u along K's edges. It does not depend on which other channels are present at u, except through the mechanical definition of "edges incident to u" — which itself involves only K's edges.

**P-Commitment** (from the commitment primitive). Commitment uses {b_K(u) : K ∈ K_τ(u)} as inputs. The available-channel set K_τ(u) is intrinsic to u per P-Channel.

The derivation:

By P-Bandwidth, b_K(u) is a function of (K, u) alone. By P-Channel, the identity of K is intrinsic to the graph; K is the same channel-substructure regardless of which decomposition D of K_τ(u) it appears in. Decomposition D is an organizational choice imposed externally onto K_τ(u); it does not alter the graph-substructure that K is. Therefore for any two complete decompositions D, D' of K_τ(u) both containing K:

$$
b^(D)_K(u) = b_K(u) = b^(D')_K(u)
$$

The bandwidth assignment to K is partition-independent. The commitment-selection probability Prob(K | u, D) = b_K(u) / $\sum_{K' \in D}$ b_{K'}(u) has a numerator that's partition-independent, and a denominator that, for any complete decomposition spanning K_τ(u), equals the total bandwidth at u along the chain's rule-type — a single intrinsic number.

Both the typing form of non-contextuality and the operational form (frame-sum constancy) follow.

The substantive content is what's happening at the ontological level. In standard QM, "context" means "which other measurements happen to be in the experimental setup." That context could in principle reach into a measurement outcome, and we have to postulate that it doesn't. In ED, "context" is an external organizational choice — a way of enumerating channels — that simply has no causal route to the underlying graph structure. Channels are real graph substructures; bandwidth is intrinsic edge weight on those substructures. There's no opening through which external enumeration could affect either. Non-contextuality is a structural consequence of how the ontology is built, not a separate empirical assumption.

### 5.3 Loophole audit

Three potential loopholes warrant explicit dismissal.

*Sublinear bandwidth composition.* The composition rule b²_combined = b²_1 + b²_2 + 2c_12 b_1 b_2 applies when channels merge into an effective coarse-grained channel; it's a constructor for combining bandwidths from constituents, not a redefinition of any single channel's bandwidth. For orthogonal channels under environmental phase-randomization, the cross-coherence c_12 = 0 and clean σ-additivity is recovered. The composition rule does not introduce partition-dependence.

*Context-dependent available-channel set.* An external apparatus brings its own channels and bandwidth into the locus, modifying local edge-weights and selecting which of the system's channels are amplified into commitment. It does not retroactively reorganize the system's existing channel structure into a different basis, nor does it alter per-channel bandwidth b_K(u) for any channel K of the system.

*Channel-to-ray correspondence.* If ED's channels are coarse-grainings of finer structures, partition-independence at the ED level transfers cleanly to the QM level via summation over coarse-graining classes; no failure mode exists in the relevant correspondence.

Non-contextuality of the bandwidth-fraction probability rule is forced by the joint action of the bandwidth and channel primitives. This is stronger than the standard QM treatment, in which non-contextuality is an operational postulate: ED forces it ontologically, because channels are graph-substructures and bandwidth is an edge-weight, both intrinsic to the graph.

---

## 6. Closure: Gleason and Busch

With non-contextuality forced (Section 5), Hilbert-space structure forced (Section 4), and the participation measure forced (Section 3), every structural admissibility condition for Gleason's theorem is met by the ED primitive stack.

The remaining Gleason assumptions check trivially:

*Non-negativity.* Automatic from the bandwidth primitive: bandwidth is a non-negative real edge weight, so |P_K|² = b_K ≥ 0.

*Normalization.* Automatic by construction of the bandwidth-fraction probability rule: $\sum_K$ f(K|u) = 1.

*σ-additivity.* For disjoint channel-subsets, bandwidth on the union equals the sum of bandwidths on the parts (set-theoretic disjoint-sum decomposition of a non-negative function). Countable extension follows from non-negativity plus finiteness of total chain bandwidth in the chain's persistence regime.

*Dimension ≥ 3.* Generically satisfied for any non-trivial quantum subsystem with non-degenerate spatial or internal degrees of freedom. The d = 2 edge case (qubits, photon polarization, spin-½) is closed by Busch's 2003 POVM extension, which replaces projectors with positive operator-valued measures and applies to all d ≥ 2.

For each effect E ∈ E(H(u)) — equivalently, each weighted channel-subset (S, w) at u — the bandwidth-fraction map satisfies:

$$
f(S, w | u) = b(S, w | u) / b(K_\tau(u) | u) = Tr(\rho(u) \cdot E)
$$

For projective measurements specified by an orthonormal channel-decomposition D = {K_1, ..., K_d} of K_τ(u), the probability of commitment outcome K* ∈ D is:

$$
Prob(K* | u) = b_K*(u) / \sum_{K' \in D} b_{K'}(u) = |\langle K*|\psi(u)\rangle|^{2}
$$

where |ψ(u)⟩ is the participation-measure pure-state representative.

This is the Born rule. The squared exponent is the b = |P|² relation forced by T14's Cauchy step. The sum-over-channels normalization is forced by the inner product's counting measure and σ-additivity. The non-contextuality that lets Gleason apply is forced by the channel-as-primitive ontology. Each piece traces back to a structural commitment about what reality is made of at the substrate level, not to a separate axiomatic choice.

---

## 7. The Squared Exponent, Unified

The exponent 2 appears in five canonical contexts in the QM-emergence framework:

1. **Bandwidth-amplitude relation:** b_K = |P_K|². Forced by the Cauchy functional equation on bandwidth additivity (Section 3.1).

2. **Born rule:** Prob(K) = |$\langle K|\psi \rangle$|². Forced as the bandwidth-fraction probability rule under the b = |P|² relation, plus Gleason-Busch closure (Section 6).

3. **Sublinear composition rule:** b²_combined = b²_1 + b²_2 + 2c_12 b_1 b_2. The same squared-modulus structure governing how bandwidths combine when channels merge.

4. **Madelung decomposition:** ψ = √ρ · e^(iS/$\hbar$). The wavefunction's polar decomposition into amplitude (square root of probability density) and phase. The square root is the inverse of the Born rule's square.

5. **Heisenberg uncertainty:** (Δx)² (Δp)² ≥ ($\hbar$/2)². The squared-variance form of the uncertainty principle, derived from the L² norm structure of the inner product.

All five 2's are the same 2. They trace to a single structural commitment: bandwidth equals amplitude squared, forced by the Cauchy step. This is one of the framework's distinctive structural unifications. In standard QM, these five 2's appear in different contexts and are each accepted as part of the formalism. In ED, they're consequences of one upstream structural fact about how participation composes.

---

## 8. What This Argument Establishes

The chain runs:

Primitives → T14 (participation measure form forced) → U2 (inner product forced) → Born (non-contextuality forced, Gleason-Busch applies) → squared-amplitude probability rule.

Each step is written out. Each step has its load-bearing arguments rather than deferring to further documents. The conformal gauge in the continuum regime is named explicitly and shown to be a description redundancy that doesn't affect any physical prediction. Three downstream theorems — Born, Bell-Tsirelson, Heisenberg — promote from forced-conditional to forced-unconditional under this chain.

The framework reproduces standard quantum mechanics exactly in every regime where standard quantum mechanics has been tested. It does not predict any new laboratory result that differs from standard QM. What it does is replace a list of independent postulates — Hilbert-space structure, sesquilinear inner product, Born rule, non-contextuality — with a smaller list of structural commitments about participation, bandwidth, channels, and polarity. The QM postulates emerge from the framework as theorems rather than being assumed independently.

Whether the substrate commitments themselves are right is a separate question and remains the load-bearing one. The framework stands or falls on whether participation, bandwidth, channels, polarity, and commitment are the correct foundational concepts. The empirical exposure of the framework is through its other channels — the soft-matter mobility law's prediction of sub-Fickian recovery in concentrated BSA, the substrate-gravity prediction of MOND's transition acceleration, the kernel-level arrow of time, the V1 finite-width vacuum kernel structure. These are where reality gets to weigh in.

For the Born rule specifically, the case is closed at the structural level. The squared exponent is not arbitrary, the Hilbert-space structure is not assumed, and non-contextuality is not postulated. All three follow from the participation-graph ontology with no new commitment introduced anywhere in the derivation.

---

## 9. References

- Proxmire, A. *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* April 2026.
- Proxmire, A. *The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion.* April 2026.
- Proxmire, A. *Theorem 14: The Participation Measure Form.* (T14 derivation memo.)
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.
- Gleason, A. M. "Measures on the closed subspaces of a Hilbert space." *Journal of Mathematics and Mechanics* 6, 885–893 (1957).
- Busch, P. "Quantum states and generalized observables: a simple proof of Gleason's theorem." *Physical Review Letters* 91, 120403 (2003).
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
