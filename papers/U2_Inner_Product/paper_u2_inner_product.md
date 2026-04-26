# The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion

**Allen Proxmire**

*April 2026*

---

## Abstract

We establish that the sesquilinear inner product on the participation-measure complex span — designated upstream commitment U2 in the Event-Density (ED) QM-emergence framework — is a forced structural consequence of ED's primitive stack rather than an independent postulate. The result is delivered in two parts. **Part I** treats the discrete participation-graph regime: decomposing U2 into linearity (C3a), conjugate-bilinearity (C3b), and the specific channel-and-vertex aggregated form (C3c), we show that C3a is automatic from the complex-valued construction $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$, that C3b is forced by the joint action of Primitive 04 (bandwidth as non-negative real) plus Primitive 09 ($U(1)$-valued polarity) plus four-band additivity, and that C3c is forced by three independent primitive-level arguments — counting measure on channels (Primitive 07 ontology + diagonal-equals-bandwidth), counting measure on vertices (graph-symmetry + diagonal constraint), and local pointwise complex-conjugate pairing (four-band orthogonality + non-contextuality + kinematic/dynamic separation). The discrete result is the **U2-Discrete Theorem**: the sesquilinear inner product $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$ is uniquely forced by the primitive stack, with no new structural commitment introduced. **Part II** lifts the result to the continuum regime via Primitive 12 thickening and the Phase-3 acoustic-metric construction. The continuum channel measure (L1) and local pointwise pairing (L3) are forced by direct transfer of the discrete arguments plus continuum-specific checks. The continuum position measure (L2) admits a one-parameter conformal redundancy $(b_K, d\mu) \sim (\Omega^{-D} b_K, \Omega^D d\mu)$ under which the participation measure transforms as $P_K \to \Omega^{-D/2} P_K$ and every inner-product value is invariant; the conformal class itself is fixed by the bandwidth-gradient ratio structure of the acoustic metric. The continuum result is the **U2-Continuum Theorem**: the continuum inner product is forced with explicit gauge structure, structurally analogous to Weyl rescaling in conformal field theory or lattice-spacing renormalisation in lattice QFT, with all physical content gauge-invariant. **Part III** documents the downstream cascade: Born (Theorem 10), Bell/Tsirelson, and Heisenberg uncertainty are all promoted from forced-conditional-on-U2 to forced-unconditional across both discrete and continuum regimes, with the conformal gauge as a description-level convention that does not enter physical predictions. The combined result eliminates one of five upstream structural commitments from the QM-emergence program and represents the program's most substantial structural-foundations completion to date for non-relativistic single-particle quantum mechanics.

---

# PART I — DISCRETE REGIME

## 1. Introduction and Motivation

Quantum mechanics is conventionally formulated as a theory of vectors in a complex Hilbert space. The Hilbert-space arena — its complex-vector-space structure, sesquilinear inner product, and induced norm topology — is not derived in standard formulations; it is postulated. Subsequent results that depend on Hilbert-space structure (Gleason's theorem for the Born rule [1], Cauchy–Schwarz inequalities underlying Bell–Tsirelson bounds, Fourier-uncertainty inequalities underlying Heisenberg's principle) inherit the postulational status of the underlying inner product.

The Event-Density (ED) program [2, 3, 4] aims to derive the structural content of quantum mechanics from a smaller and more concrete primitive ontology: a participation graph $G = (V, E)$ on a $3{+}1$-dimensional event manifold, with vertices corresponding to micro-events (Primitive 01), edges corresponding to participation relations (Primitive 03), bandwidth as edge-weight (Primitive 04), channels as primitive ontological sub-structures (Primitive 07), polarity phase as $U(1)$-valued angular content (Primitive 09), and commitment as a discrete channel-selecting event (Primitive 11). In this framework, the natural complex-valued field is the participation measure

$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)} \qquad (1)
$$

with bandwidth $b_K = |P_K|^2$ by construction and aggregated state $\Psi(x, t) = \sum_K P_K(x, t)$.

A prior companion paper [5] established the Born rule as a forced structural consequence of the primitive stack via the Gleason–Busch route, but the result was conditional on a single inherited upstream commitment: the sesquilinear inner product on the participation-measure complex span,

$$
\langle P \mid Q \rangle = \sum_K \int dx \; P_K^*(x) Q_K(x), \qquad (2)
$$

referred to in the QM-emergence framework as **upstream commitment U2** [3, §4]. The same inner product is required by the Bell–Tsirelson result (which uses Cauchy–Schwarz on the bipartite Hilbert space) and the Heisenberg uncertainty result (which uses the $L^2$-norm structure inherited from the inner product). Three downstream theorems share U2 as a single residual structural conditionality.

The present paper establishes U2 as forced rather than postulated. The argument is delivered in two parts. Part I (Sections 2–8) treats the discrete participation-graph regime, deriving the inner product on the vertex-level structure of $G$. Part II (Sections 9–14) lifts the result to the continuum regime via Primitive 12 thickening and the Phase-3 acoustic-metric construction; here a one-parameter conformal redundancy emerges, but it is a description redundancy that leaves all inner-product values invariant rather than a physical ambiguity. Part III (Sections 15–18) documents the downstream cascade: Born, Bell, and Heisenberg promote from forced-conditional-on-U2 to forced-unconditional in both regimes, with the gauge structure as a description-level convention.

The structural pattern of the derivation parallels the Born/Gleason result of [5]. Both arcs decompose a single upstream commitment into sub-claims, find most automatic or interpretive, and concentrate the load on a small number of substantive items closed by primitive-level arguments. Both introduce no new structural commitments. The methodology demonstrates compositional reach: arguments developed for one regime transfer to adjacent regimes when the underlying primitives are regime-independent.

The paper is organised as follows. Section 2 introduces the relevant primitive stack and notation. Section 3 decomposes U2 into three sub-commitments. Sections 4–7 derive each in turn for the discrete regime. Section 8 states the U2-Discrete Theorem. Section 9 introduces the continuum-lift inputs (Primitive 12, Phase-3 acoustic metric). Sections 10–12 treat the three continuum sub-features. Section 13 explicitly characterises the gauge structure. Section 14 states the U2-Continuum Theorem. Section 15 documents the downstream cascade. Section 16 places the result in the broader ED program. Section 17 provides a non-technical explainer. Section 18 is the appendix mapping paper sections to the underlying derivation memos.

---

## 2. Primitive Stack and Notation

### 2.1 Primitives drawn upon

The U2 derivation invokes the following primitives:

- **Primitive 01 (Micro-Event):** discrete events on the event manifold; supplies the vertex set $V$ of the participation graph.
- **Primitive 03 (Participation):** the participation relation between micro-events; supplies the edge set $E$.
- **Primitive 04 (Bandwidth):** the graded measure of participation as edge weighting $w : E \to \mathbb{R}_{\geq 0}$. Bandwidth admits a four-band orthogonal decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ (internal-rule, adjacency, environmental, commitment-reserve), with conservation along chains in their persistence regime.
- **Primitive 07 (Channel):** stable, bandwidth-preserving sub-structures of the participation graph along which a chain's update rule can be repeatedly instantiated. Channels are *primitive ontological objects*: their identity is intrinsic to the graph, not basis-relative. Channels are countable in any region for any given rule-type.
- **Primitive 08 (Multiplicity):** the effective channel count $M_\mathrm{eff} = (\sum |P|^2)^2 / \sum |P|^4$.
- **Primitive 09 (Tension Polarity):** the $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction; supplies the phase factor $e^{i \pi_K}$ in (1). Primitive 09 is explicit that polarity is phase-valued ("not a binary in general — it is a phase in the full treatment"; "not a scalar"), with the structural commitment to $U(1)$.
- **Primitive 11 (Commitment):** the discrete event in which a chain selects one channel from those available, with selection probability weighted by channel bandwidth.
- **Primitive 12 (Thickening):** the accumulation of committed micro-events into stable persistent structure, supporting the emergence of a smooth continuum manifold $M$ with thickness field $\tau(x, t)$ on which classical-field descriptions become valid. Used in Part II only.

### 2.2 The participation measure and its space

The participation measure (1) places each $(K, x, t)$-slot value in $\mathbb{C}$, fusing Primitive 04's non-negative magnitude $\sqrt{b_K}$ with Primitive 09's $U(1)$ phase $e^{i \pi_K}$. Let $\mathcal{P}$ denote the space of participation-measure arrays $\{P_K(u, t) : K \in \mathcal{K}, u \in V\}$ at a given time $t$ (time-dependence will be suppressed in what follows; the analysis is at fixed $t$).

The structural claim of Part I is that $\mathcal{P}$ admits a unique sesquilinear inner product forced by the primitive stack, taking the form (2) with discrete sums $\sum_u$ in place of integrals $\int dx$. Part II lifts this to the continuum form (2) with explicit gauge structure.

### 2.3 The available-channel set

For a chain $C$ of rule-type $\tau$ at vertex $u \in V$, let $\mathcal{K}_\tau(u)$ denote the set of channels available to $C$ at $u$ — the set of $\tau$-compatible sub-structures meeting at $u$ with rule-compatibility, bandwidth-coherence, and stability conditions per Primitive 07. The local channel-space at $u$ is the complex linear span $\mathcal{H}(u) = \mathrm{span}_\mathbb{C}\{|K\rangle : K \in \mathcal{K}_\tau(u)\}$. Per Primitive 07 §1, $|\mathcal{K}_\tau(u)|$ is finite or countably infinite for any concrete physical chain.

---

## 3. Decomposition of U2 into C3a, C3b, C3c

The single-line statement of U2 — "complex-valued $P_K(u)$ with sesquilinear inner product $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$" — packages three structurally distinct commitments. Treating them as a single block obscures which parts are derivable from primitives and which would be genuine additional choices. The three-part decomposition:

- **C3a — Linearity.** The space $\mathcal{P}$ admits complex-vector-space structure under componentwise sum and complex-scalar multiplication.
- **C3b — Conjugate-bilinearity (sesquilinearity).** A pairing $\langle \cdot \mid \cdot \rangle : \mathcal{P} \times \mathcal{P} \to \mathbb{C}$ exists satisfying conjugate-linearity in the first argument, linearity in the second argument, conjugate symmetry, and positive-definiteness.
- **C3c — Specific form.** $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) \cdot Q_K(u)$ — channel-summed (counting measure on $\mathcal{K}$), vertex-summed (counting measure on $V$), and locally pointwise (complex-conjugate product at each $(K, u)$-slot, with no cross-slot kernel terms).

C3a is a structural-typing statement. C3b is an algebraic-form statement given the typing. C3c is a specific-aggregation statement given the algebraic form. Each downstream theorem leans on a different combination: the Born rule needs all three; Bell–Tsirelson needs C3a + C3b for Cauchy–Schwarz; Heisenberg needs the full structure for $L^2$-norm control.

A clean U2-FORCED verdict requires deriving all three. We derive C3a in Section 4, C3b in Section 5, and C3c (with its three sub-features) in Section 6, then state the theorem in Section 7. (Note: the original outline sequence numbers Sections 4–8; we follow the structural decomposition in the text.)

---

## 4. C3a — Linearity is Automatic

The participation-measure construction (1) produces a complex value at each $(K, u)$ slot:

$$
P_K(u) = \sqrt{b_K(u)} \cdot e^{i \pi(K, u)} \in \mathbb{C}. \qquad (3)
$$

The space $\mathcal{P}$ is the set of all such arrays — equivalently, complex-valued functions on $\mathcal{K} \times V$. We claim $\mathcal{P}$ admits componentwise sum and complex-scalar multiplication satisfying the standard complex-vector-space axioms.

**Sum.** For $P, Q \in \mathcal{P}$, define $(P + Q)_K(u) := P_K(u) + Q_K(u)$. Each summand is in $\mathbb{C}$, so the sum is in $\mathbb{C}$, and the result is in $\mathcal{P}$.

**Scalar multiplication.** For $\alpha \in \mathbb{C}$ and $P \in \mathcal{P}$, define $(\alpha \cdot P)_K(u) := \alpha \cdot P_K(u)$. The product of complex numbers is complex; result in $\mathcal{P}$.

**Vector-space axioms.** Componentwise operations on a function space valued in a field inherit all field axioms (associativity, commutativity, distributivity, identities, inverses) pointwise from the codomain. Since $\mathbb{C}$ is a field, all complex-vector-space axioms hold for $\mathcal{P}$.

Two structural concerns warrant explicit dismissal. First, sums of participation measures need not separately satisfy a normalisation condition; this is the standard distinction between the linear span $\mathcal{P}$ (on which the inner product lives) and the unit-norm physical-state subset, identical to the wavefunction/$L^2$-state distinction in standard quantum mechanics. Second, complex scalar multiplication scales bandwidth by $|\alpha|^2$, which is non-negative; this is a re-normalisation, not a primitive violation.

**C3a is established.** The participation-measure space is a complex vector space, automatically.

---

## 5. C3b — Sesquilinearity is FORCED

We require a pairing $\langle \cdot \mid \cdot \rangle : \mathcal{P} \times \mathcal{P} \to \mathbb{C}$ satisfying:

- **(S1) Conjugate-linearity in the first argument:** $\langle \alpha P + \beta Q \mid R \rangle = \alpha^* \langle P \mid R \rangle + \beta^* \langle Q \mid R \rangle$.
- **(S2) Linearity in the second argument:** $\langle R \mid \alpha P + \beta Q \rangle = \alpha \langle R \mid P \rangle + \beta \langle R \mid Q \rangle$.
- **(S3) Conjugate symmetry:** $\langle P \mid Q \rangle = \langle Q \mid P \rangle^*$.
- **(S4) Positive-definiteness:** $\langle P \mid P \rangle \geq 0$, with equality iff $P = 0$.

The derivation proceeds in three steps. Step A fixes the diagonal pairing on each slot. Step B uses $U(1)$ invariance to rule out non-sesquilinear alternatives. Step C uses band-additivity to fix the slot-asymmetric linearity structure.

### 5.1 Step A: diagonal pairing equals bandwidth

Primitive 04 §2 establishes bandwidth as a non-negative real edge weight, with $b_K(u) = |P_K(u)|^2 \geq 0$ by construction (1). The diagonal of any inner product on $\mathcal{P}$ must produce a non-negative real that reduces, on each $(K, u)$ slot, to the bandwidth at that slot. The pointwise requirement is

$$
[\text{diagonal pairing on slot } (K, u)] \text{ applied to } P_K(u) = b_K(u) = |P_K(u)|^2.
$$

For $P_K(u) = a + ib \in \mathbb{C}$, this requires the diagonal pointwise function to satisfy $f(a + ib) = a^2 + b^2 = (a + ib)^* (a + ib)$. Up to overall positive scaling, the unique pointwise function on $\mathbb{C}$ satisfying this is the squared modulus, equivalent to the complex-conjugate product $P_K^*(u) \cdot P_K(u)$. This forces the diagonal pairing's pointwise structure; the aggregation (sum over $K$, sum over $u$) is C3c material, addressed in Section 6.

**(S4) positive-definiteness is forced** by Primitive 04 non-negativity and the construction (1) requirement that bandwidth be the diagonal norm-squared.

### 5.2 Step B: $U(1)$ invariance forces sesquilinearity

Primitive 09 establishes polarity as $U(1)$-valued. The participation measure carries the phase factor $e^{i \pi_K}$ in (1). Bandwidth is invariant under global phase rotation $P \to e^{i \alpha} P$:

$$
|e^{i \alpha} P_K(u)|^2 = e^{-i\alpha} e^{i\alpha} |P_K(u)|^2 = |P_K(u)|^2 = b_K(u). \qquad (4)
$$

This is the structural statement that bandwidth does not depend on the absolute phase of the participation measure: phase rotation does not change magnitudes. The inner product must respect this — specifically, the diagonal $\langle P \mid P \rangle$ must be $\alpha$-invariant under global rotation, since it equals an aggregation of bandwidths.

We examine three candidate pairing types under global phase rotation.

**(B-bilinear) Complex-bilinear pairing** $\beta(P, Q)$, linear in both slots:

$$
\beta(e^{i\alpha} P, e^{i\alpha} P) = e^{i\alpha} \cdot e^{i\alpha} \cdot \beta(P, P) = e^{2i\alpha} \cdot \beta(P, P).
$$

For arbitrary $\alpha$ this is not equal to $\beta(P, P)$ unless $\beta(P, P) = 0$. **Complex-bilinearity is incompatible with $U(1)$ invariance of the diagonal — eliminated.**

**(B-real-bilinear) Real-bilinear pairing**, treating $\mathbb{C}$ as $\mathbb{R}^2$ and bilinear over $\mathbb{R}$. A general such pairing has the form (on a single slot)

$$
\beta(z, w) = a \, \mathrm{Re}(z) \mathrm{Re}(w) + b \, \mathrm{Im}(z) \mathrm{Im}(w) + c \, \mathrm{Re}(z) \mathrm{Im}(w) + d \, \mathrm{Im}(z) \mathrm{Re}(w)
$$

with $a, b, c, d \in \mathbb{R}$. Demanding $\beta(z, z) \geq 0$ for all $z$ requires $a, b \geq 0$ and $4ab \geq (c+d)^2$. Demanding $\beta(e^{i\alpha} z, e^{i\alpha} z) = \beta(z, z)$ for all $\alpha$ and all $z$ forces (matching coefficients of $\mathrm{Re}(z)^2$ at $\alpha = \pi/2$) $b = a$, then $c + d = 0$, then $c = d = 0$. The resulting $U(1)$-invariant real-bilinear form is

$$
\beta(z, w) = a \left( \mathrm{Re}(z) \mathrm{Re}(w) + \mathrm{Im}(z) \mathrm{Im}(w) \right) = a \cdot \mathrm{Re}(z^* w).
$$

This is exactly the *real part* of the sesquilinear pairing $z^* w$, scaled by $a$. The imaginary part is missing. But physical interference — superpositions $P + Q$, off-diagonal phase relationships, the relative-phase content underlying interferometry, Bell correlations, and Fourier-uncertainty — depends on both $\mathrm{Re}(P^* Q)$ and $\mathrm{Im}(P^* Q)$. **A $U(1)$-invariant real-bilinear pairing is strictly weaker than sesquilinearity and cannot encode the full physical content of the participation-measure framework.**

**(B-sesquilinear) Sesquilinear pairing** $\langle P \mid Q \rangle$, conjugate-linear in the first slot, linear in the second:

$$
\langle e^{i\alpha} P \mid e^{i\alpha} P \rangle = e^{-i\alpha} \cdot e^{i\alpha} \cdot \langle P \mid P \rangle = \langle P \mid P \rangle, \qquad (5)
$$

and on the off-diagonal,

$$
\langle e^{i\alpha} P \mid e^{i\alpha} Q \rangle = e^{-i\alpha} \cdot e^{i\alpha} \cdot \langle P \mid Q \rangle = \langle P \mid Q \rangle. \qquad (6)
$$

Both diagonal and off-diagonal pairings are $U(1)$-invariant under global rotation, matching the physical content: global phase has no observable consequences, but relative phase does, and sesquilinearity preserves relative-phase information in the imaginary part of $\langle P \mid Q \rangle$.

**Conclusion of Step B.** Among the three candidate pairing types, complex-bilinear is eliminated by $U(1)$-violation on the diagonal; real-bilinear that satisfies $U(1)$ reduces to the strictly-weaker real part of sesquilinearity; sesquilinearity is $U(1)$-invariant on both diagonal and off-diagonal and preserves all relative-phase information. **Sesquilinearity (S1) + (S2) is forced.**

### 5.3 Step C: band additivity confirms the slot-asymmetric structure

Primitive 04 §1.5 establishes the four-band orthogonal decomposition and, more broadly, bandwidth additivity over disjoint channel-subsets. For two participation measures $P, Q$ with disjoint support (i.e., $P_K(u) = 0$ wherever $Q_K(u) \neq 0$ and vice versa), the diagonal pairing of $P + Q$ decomposes as

$$
\langle P + Q \mid P + Q \rangle = \langle P \mid P \rangle + \langle Q \mid Q \rangle, \qquad (7)
$$

since the cross-terms $\langle P \mid Q \rangle + \langle Q \mid P \rangle$ vanish: the slot-product $P_K^*(u) Q_K(u) = 0$ pointwise on disjoint-support measures.

For (7) to follow from a pairing, the pairing must be additive in each slot — the (S1)/(S2) content for arbitrary scalar combinations. Combined with Step B's selection of sesquilinear over bilinear, additivity-in-each-slot yields conjugate-linearity in the first slot (S1 forced) and linearity in the second slot (S2 forced). Conjugate symmetry (S3) follows automatically:

$$
\langle P \mid Q \rangle^* = \left( \sum_\text{slots} P_K^*(u) Q_K(u) \right)^* = \sum_\text{slots} P_K(u) Q_K^*(u) = \langle Q \mid P \rangle. \qquad (8)
$$

The choice of which slot is conjugated is convention; physics is invariant under relabeling. We adopt the standard convention (first slot conjugated).

### 5.4 Joint conclusion

All four sesquilinearity properties (S1)–(S4) are forced by primitive-level inputs:

| Property | Forced by |
|---|---|
| (S1) Conjugate-linearity (first slot) | P-04 band additivity (Step C) + P-09 $U(1)$ invariance (Step B) |
| (S2) Linearity (second slot) | P-04 band additivity (Step C) + P-09 $U(1)$ invariance (Step B) |
| (S3) Conjugate symmetry | (S1) + (S2) algebraic consequence |
| (S4) Positive-definiteness on diagonal | P-04 non-negativity (Step A) + construction (1) diagonal-equals-bandwidth |

**C3b is forced** by Primitives 04 and 09 plus the participation-measure construction (1), with no new structural commitment beyond those already in the primitive stack.

---

## 6. C3c — Specific Form FORCED in the Discrete Regime

C3b establishes the *type* of pairing (sesquilinear with diagonal equal to aggregated bandwidth). What remains is the *aggregation form* — the specific channel measure, the specific position measure, and the locality of the pointwise pairing. Three sub-features:

- **(c1)** Channel measure: counting measure $\sum_K$ versus possibly weighted alternatives.
- **(c2)** Position measure: counting measure on vertices $\sum_u$ versus possibly weighted alternatives.
- **(c3)** Pointwise pairing: strictly local complex-conjugate product $P_K^*(u) Q_K(u)$ versus possibly cross-slot kernel mixing.

Each closes FORCED via independent primitive-level arguments. Two structural devices recur: (i) the diagonal-equals-bandwidth constraint inherited from §5.1, and (ii) the absence of primitive-level features distinguishing channels or vertices beyond bandwidth itself.

### 6.1 (c1) Channel counting measure

Could the channel-aggregation be $\sum_K w(K) \sum_u P_K^*(u) Q_K(u)$ for some non-trivial weight $w : \mathcal{K}_\tau(u) \to \mathbb{R}_{>0}$ other than $w \equiv 1$?

A non-trivial $w(K)$ would have to be a structural feature of the participation graph that distinguishes one channel from another in a measure-theoretic sense — independent of bandwidth, which is already captured in the slot value. Within the primitive stack:

- *Bandwidth itself.* Already in the slot value; cannot be reused as an independent weight without double-counting.
- *Rule-type $\tau$.* All channels in $\mathcal{K}_\tau(u)$ are $\tau$-compatible by definition (Primitive 07 §1: rule-type-selective). Within the restricted set, rule-type does not distinguish.
- *Channel topology / connectivity.* Primitive 07 §1 establishes channels as primitive ontological objects; their identity is intrinsic, but no measure-theoretic weighting beyond bandwidth is supplied by the primitives.
- *Environmental coupling.* Captured in the four-band decomposition (b_env contribution); not an independent weight.

**No primitive-level source supplies a non-trivial $w(K)$.** Independently, the diagonal-equals-bandwidth constraint of §5.1 forces $\sum_K w(K) \sum_u |P_K(u)|^2 = b_\mathrm{total}$ for arbitrary bandwidth profiles, which requires $w(K) = 1$ on operationally relevant channels. Both arguments converge: counting measure is the unique channel-aggregation consistent with the primitive structure.

**(c1) is forced.**

### 6.2 (c2) Vertex counting position measure

Could the position-aggregation be $\sum_K \sum_u w(u) P_K^*(u) Q_K(u)$ for some non-trivial vertex weight $w : V \to \mathbb{R}_{>0}$?

Candidate alternatives within the primitive stack:

- *Local event density $\rho(u)$ (Primitive 05).* Vertex weight $w(u) = \rho(u)$ would weight vertices by their event density. Diagonal becomes $\sum_K \sum_u \rho(u) b_K(u)$ — bandwidth weighted by local density, not equal to total bandwidth.
- *Local total bandwidth $b(u) = \sum_K b_K(u)$.* Diagonal becomes $\sum_K \sum_u b(u) b_K(u) = \sum_u b(u)^2$, dimensionally and structurally inconsistent with the C3b derivation.
- *Vertex multiplicity / connectivity.* No primitive-level requirement forces such weighting.

Each candidate alternative conflicts with the diagonal-equals-bandwidth constraint, which forces $w(u) \equiv 1$ on every vertex with non-zero bandwidth presence.

A second, independent argument from graph symmetry: the participation graph is built from primitive vertices (Primitive 01 micro-events), individuated by identity but otherwise primitively equivalent. For two graph-isomorphic vertices, no primitive feature distinguishes them; a non-counting measure assigning different weights to isomorphic vertices would violate this primitive-level equivalence. For non-isomorphic vertices, the differences are already captured in $P_K(u)$ slot values; encoding them again in $w(u)$ would double-count.

**(c2) is forced** in the discrete regime.

### 6.3 (c3) Local complex-conjugate pointwise pairing

The most general sesquilinear pairing consistent with §6.1–§6.2 (counting measures fixed) is

$$
\langle P \mid Q \rangle = \sum_{K, K'} \sum_{u, u'} P_K^*(u) \cdot \mathcal{K}(K, K'; u, u') \cdot Q_{K'}(u') \qquad (9)
$$

with kernel $\mathcal{K}(K, K'; u, u') \in \mathbb{C}$. The local pointwise form has $\mathcal{K}(K, K'; u, u') = \delta_{KK'} \delta_{uu'}$. The question is whether non-trivial off-diagonal kernel components are forced to vanish.

The diagonal-equals-bandwidth constraint fixes $\mathcal{K}(K, K; u, u) = 1$ for every $(K, u)$. Off-diagonal components are not directly constrained by the diagonal; the structural arguments forbidding them come from elsewhere. Three independent arguments combine to force the local Kronecker-delta structure:

**Argument from four-band orthogonality** (cross-band terms). Primitive 04 §1.5 establishes four orthogonal bands (b_int, b_adj, b_env, b_com) with primitive-level orthogonality: bandwidth does not mix between bands. For the inner product to respect this, the kernel must be block-diagonal across bands; cross-band components $\mathcal{K}(K, K'; u, u')$ with $K, K'$ in different bands must vanish. Otherwise the inner product would generate cross-band coherences in $\langle P \mid P \rangle$ that violate primitive-level orthogonality.

**Argument from non-contextuality** (cross-channel-within-band terms). The companion paper [5] established that per-channel bandwidth $b_K(u)$ is partition-independent — a function of $(K, u)$ alone, with no contribution from other channels at $u$. The channel-as-primitive ontology of Primitive 07 forces this. Within a single band, a non-zero cross-channel kernel term $\mathcal{K}(K, K'; u, u)$ for $K \neq K'$ would contribute $P_K^*(u) \mathcal{K}(K, K'; u, u) Q_{K'}(u)$ to $\langle P \mid Q \rangle$, making the inner-product diagonal depend on inter-channel coherences and reintroducing contextuality. Cross-channel-within-band kernel terms are forbidden.

**Argument from kinematic/dynamic separation** (cross-vertex terms). Inner products encode kinematic content (norms, orthogonalities, probabilities at a single time). Time-evolution and channel-mixing dynamics are encoded separately, in the participation-measure evolution equation. A non-local kernel $\mathcal{K}(K, K; u, u')$ with $u \neq u'$ would couple participation values at distinct vertices in the inner product — i.e., the inner product would carry propagation/dynamical information. This conflates kinematics with dynamics. Cross-vertex kernel terms are forbidden.

The three arguments combine to force $\mathcal{K}(K, K'; u, u') = \delta_{KK'} \delta_{uu'}$:

| Kernel component | Forbidden by |
|---|---|
| Cross-band ($K, K'$ in different bands) | Four-band orthogonality |
| Same-band cross-channel ($K \neq K'$ within a band) | Non-contextuality / channel primitivity |
| Same-channel cross-vertex ($K = K'$, $u \neq u'$) | Kinematic/dynamic separation |

The basic inner product is therefore

$$
\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) \cdot Q_K(u). \qquad (10)
$$

**(c3) is forced.**

### 6.4 Summary

All three sub-features of C3c close FORCED in the discrete regime via independent primitive-level arguments. The full sesquilinear inner product (10) is uniquely determined by the primitive stack on the participation-graph vertex set.

---

## 7. (Continued in §6.4)

*[The discrete derivation is complete with §6. The original outline numbers items 4–7 as Sections 4–7; the integrated text combines C3a (§4 in outline) with the exposition of §3, C3b (§5 / §6 in outline) into Section 5 here, and C3c (§7 in outline) into Section 6 here. We renumber as the U2-Discrete Theorem statement in Section 8.]*

## 8. Theorem: U2-Discrete

> **Theorem (U2-Discrete; Sesquilinear Inner Product on the Participation Graph).** Let $G = (V, E)$ be a participation graph with vertex set $V$ (Primitive 01 micro-events) and edge set $E$ (Primitive 03 participation relations). For a chain $C$ of rule-type $\tau$ with available-channel set $\mathcal{K}_\tau(u)$ at each $u \in V$ (Primitive 07), construct the participation measure $P_K(u, t) = \sqrt{b_K(u, t)} \cdot e^{i \pi(K, u, t)}$ from Primitive 04 (bandwidth $\geq 0$) and Primitive 09 ($U(1)$ polarity phase), and let $\mathcal{P}$ be the complex-vector-space span of all such arrays.
>
> Then there exists a unique sesquilinear inner product on $\mathcal{P}$ forced by the primitive stack:
>
> $$
> \langle P \mid Q \rangle_\mathrm{disc} = \sum_K \sum_{u \in V} P_K^*(u) \cdot Q_K(u), \qquad (11)
> $$
>
> satisfying conjugate-linearity in the first slot, linearity in the second, conjugate symmetry, and positive-definiteness. Its diagonal recovers the chain's total bandwidth: $\langle P \mid P \rangle = \sum_K \sum_u b_K(u)$. The induced norm topology yields a Hilbert space $\mathcal{H}_C$ on completion. The four-band orthogonality of Primitive 04 §1.5 is preserved as inner-product orthogonality between band-restricted projections; the non-contextuality of per-channel bandwidth is preserved as basis-independence of the channel-resolved diagonal.

**Proof outline.** C3a (linearity) is automatic from the complex-valued construction (1) and closure of complex-valued function spaces under componentwise sum and complex-scalar multiplication (§4). C3b (sesquilinearity) is forced via the joint action of Primitive 04 non-negativity (Step A: forces diagonal = squared modulus), Primitive 09 $U(1)$ invariance (Step B: eliminates complex-bilinear, reduces real-bilinear to strictly weaker real part of sesquilinearity), and Primitive 04 §1.5 band additivity (Step C: forces slot-wise additivity), giving sesquilinearity uniquely (§5). C3c — channel counting measure (§6.1 forced by absence of primitive-level inter-channel weighting + diagonal constraint), vertex counting measure (§6.2 forced by absence of primitive-level inter-vertex weighting + diagonal constraint + graph symmetry), local pointwise pairing (§6.3 forced by four-band orthogonality + non-contextuality + kinematic/dynamic separation) — is forced in the discrete regime (§6). $\square$

The U2-Discrete Theorem is forced in the discrete participation-graph regime with no new structural commitment introduced. All inputs (Primitives 01, 03, 04, 07, 09, 11; the four-band orthogonality of Primitive 04 §1.5; the non-contextuality result of [5]) are already present in the primitive stack or derived in companion work.

---

# PART II — CONTINUUM REGIME

## 9. Primitive 12 and Phase-3 Acoustic-Metric Mapping

The continuum target — used implicitly in matter-wave, Bose–Einstein condensate, and cosmological-scale applications — is

$$
\langle P \mid Q \rangle_\mathrm{cont} = \sum_K \int_M d\mu(x) \cdot P_K^*(x) \cdot Q_K(x) \qquad (12)
$$

where $M$ is the emergent manifold supplied by Primitive 12 thickening and $d\mu(x)$ is its volume form. Three sub-features must lift uniquely from the discrete result:

- **L1.** Channel aggregation $\sum_K$ in the continuum (still $\sum_K$ for discrete spectra; $\int d\nu(K)$ for continuous spectra).
- **L2.** Position aggregation $\sum_u \to \int_M d\mu(x)$ with uniquely determined volume form. *Load-bearing.*
- **L3.** Pointwise pairing $P_K^*(u) Q_K(u) \to P_K^*(x) Q_K(x)$ without acquiring smearing kernels.

### 9.1 Inputs from Primitive 12

Primitive 12 establishes thickening as the accumulation of committed micro-events into stable persistent structure. Its discrete form is $T(R, t) = \sum_{\varepsilon \in \mathrm{commitments}\, \mathrm{in}\, R} w(\varepsilon)$ — region-summed commitment weights. The thick-regime field $\tau(x, t) : M \times \mathbb{R} \to \mathbb{R}_{\geq 0}$ is the density of accumulated thickness. When $\tau$ is large and smooth, the participation graph admits a coarse-graining yielding a smooth emergent manifold $M$ with bandwidth fields and channel structures inheriting continuum descriptions.

Primitive 12 supplies the *existence* of $M$ when the thickening field is sufficiently large and smooth. Primitive 12 does *not* by itself supply a uniquely determined volume form; the metric structure on $M$ comes from the Phase-3 acoustic-metric construction. Primitive 12's open items (precise commitment-weighting, threshold $\tau$ for continuum-field validity, un-thickening rates, saturation behaviour) concern thickening dynamics rather than the inner-product structure on a given $M$ at a given time.

### 9.2 Phase-3 acoustic-metric inputs

The Phase-3 framework [6] supplies a kinematic acoustic metric $g_{ab}(x)$ on $M$, derived from bandwidth gradients (Primitive 06 ED-gradient + Primitive 04 bandwidth field) following the standard Unruh-style construction. The acoustic metric is kinematic, not dynamical: ED has a kinematic acoustic metric only, with no Einstein equations forced and no Schwarzschild solution. The metric is sufficient to define orthogonality, lengths, and a candidate volume form $\sqrt{|g(x)|} \, d^D x$ via the standard differential-geometric construction.

Phase-3 supplies a *candidate* metric and volume form. Whether the volume form is uniquely fixed — in particular, whether the metric admits conformal-rescaling freedom — is the substantive Memo-3-of-the-continuum question, addressed in Section 12 below.

### 9.3 Falsifier inventory

Three falsifiers structure the continuum-lift verification:

- **F2-cont.** Alternative continuum channel measure (non-Lebesgue-on-channel-space). Attaches to L1; addressed in Section 10.
- **F3-cont.** Alternative continuum position measure (most likely conformal rescaling of $d\mu$). Attaches to L2; addressed in Section 12.
- **F1$'$-cont.** Non-local cross-slot terms in the continuum (smearing kernels from Primitive 12 coarse-graining or cross-channel/cross-position contributions). Attaches to L3; addressed in Section 11.

A fourth potential falsifier — Primitive 12 internal residuals propagating into ambiguity in $d\mu$ — is dispatched in Section 12 by examining each open item and verifying independence from the inner-product structure.

---

## 10. L1 — Channel Measure FORCED in the Continuum

### 10.1 Discrete-channel transfer

The discrete-counting argument (§6.1) had two prongs: (i) no primitive-level source for non-trivial inter-channel weighting, and (ii) the diagonal-equals-bandwidth constraint forces unit weight on operationally relevant channels.

Both prongs are regime-independent. They invoke Primitive 04 (bandwidth), Primitive 07 (channel ontology), and the C3b sesquilinearity result — none of which acquires new content in the continuum. Primitive 12 thickening accumulates commitments and densifies the graph but does not assign extra weights to channels. **Both prongs transfer to the continuum verbatim**, with the spatial argument changed from $u \in V$ to $x \in M$.

For discrete-channel cases (e.g., spin states, internal atomic levels, photon polarisation), the conclusion is immediate: counting measure on $\mathcal{K}_\tau(x)$ is forced in the continuum.

### 10.2 Continuous-channel case

For continuous channel spectra (e.g., continuous momentum modes for matter waves, continuous position-basis channels for spatially-extended systems), the natural analog of "counting measure on a discrete set" is "Lebesgue measure on the continuous channel space." The diagonal-equals-bandwidth constraint becomes

$$
\int d\nu_x(K) \cdot b_K(x) = b_\mathrm{total}(x), \qquad (13)
$$

requiring $\nu_x(K)$ to be the unique measure consistent with this for arbitrary bandwidth profiles. Up to overall normalisation, this is Lebesgue measure on the continuum channel space; any non-Lebesgue alternative would conflict with (13) for some bandwidth profile.

Independently, no primitive-level source supplies a non-Lebesgue weighting on continuous channel spaces — the same arguments applied to the discrete case extend to the continuum.

**Falsifier F2-cont is dispatched.** L1 is forced in the continuum: counting measure on discrete channel sets, Lebesgue measure on continuous channel spaces, both forced by the same primitive-level arguments.

---

## 11. L3 — Local Pairing FORCED in the Continuum

The continuum-most-general sesquilinear pairing consistent with L1 + L2 is

$$
\langle P \mid Q \rangle = \sum_{K, K'} \int_M \int_M d\mu(x) d\mu(x') \cdot P_K^*(x) \cdot \mathcal{K}(K, K'; x, x') \cdot Q_{K'}(x'). \qquad (14)
$$

The pointwise local form has $\mathcal{K}(K, K'; x, x') = \delta_{KK'} \delta(x - x')$. We verify this is forced.

### 11.1 Transfer of the discrete-regime arguments

The three discrete-regime arguments forbidding cross-slot kernel terms (§6.3) are all regime-independent:

- **Four-band orthogonality** (forbids cross-band terms). Primitive 04 §1.5 four-band partition applies in the continuum verbatim. Continuum bandwidth field $b(x)$ inherits the partition into $b_\mathrm{int}(x) + b_\mathrm{adj}(x) + b_\mathrm{env}(x) + b_\mathrm{com}(x)$ with the same orthogonality structure. Cross-band kernel components must vanish.
- **Non-contextuality** (forbids same-band cross-channel terms). The channel-as-primitive ontology of Primitive 07 §1 applies in the continuum: at point $x \in M$, channels are continuum sub-structures of the thickened participation manifold but remain primitive ontological objects. Per-channel bandwidth $b_K(x)$ is partition-independent. Same-band cross-channel kernel terms reintroduce contextuality and are forbidden.
- **Kinematic/dynamic separation** (forbids cross-position terms). The structural separation between kinematic norm and dynamical evolution is regime-independent. In the continuum, dynamics is encoded in the participation-measure evolution equation (Schrödinger / Klein–Gordon / Dirac thick-regime limits), which carries its own propagators. Cross-position kernel terms in the inner product conflate kinematics with dynamics and are forbidden.

### 11.2 Continuum-specific check: Primitive 12 coarse-graining smearing

Primitive 12's coarse-graining could in principle introduce finite-resolution smearing — short-range correlation kernels at the thickening scale $\ell_\mathrm{thick}$, analogous to UV-cutoff effects in QFT. The structural question: does Primitive 12's coarse-graining inherently introduce a smearing kernel, or does the strict thickening limit recover pointwise locality?

Primitive 12 is *accumulation*: each commitment adds a vertex; thickening counts commitments that persist. In the strict $\tau \to \infty$ limit, the graph becomes infinitely dense and the discrete vertex measure refines into a continuum measure. At each refinement step, the discrete inner product is strictly pointwise (per §6.3 above): $P_K^*(u) Q_K(u)$ only at matching vertices, never at distinct vertices. The continuum inner product is the strict $\tau \to \infty$ limit of the discrete inner product, not a finite-resolution coarse-graining; smearing kernels arise only if one stops at finite $\tau$ and uses the resulting finite-resolution structure. The strict continuum limit removes the smearing scale entirely and recovers exact pointwise locality.

This is the structural analog of the standard fact that the continuum limit of a lattice quantum field theory recovers a local QFT, not a smeared one — but here the underlying ontology already supplies the discrete structure, no regularisation choice is involved, and the continuum is genuinely a limit rather than a regularisation scheme.

Two corner cases warrant explicit treatment. (1) *Could finite-thickness corrections matter?* Finite $\tau < \infty$ corresponds to incompletely-thickened regions (very early universe, deep vacuum, Q–C boundary), where the continuum inner product (12) is not the appropriate description anyway — the discrete inner product (11) is. (2) *Could pointwise locality fail on measure-zero sets?* The four-band orthogonality and non-contextuality arguments above forbid any cross-position or cross-channel term, even on a measure-zero set; pointwise locality is exact, not just almost-everywhere.

**Falsifier F1$'$-cont is dispatched in all sub-classes.** L3 is forced in the continuum:

$$
\langle P \mid Q \rangle = \sum_K \int_M d\mu(x) \cdot P_K^*(x) \cdot Q_K(x). \qquad (15)
$$

---

## 12. L2 — Position Measure FORCED Up to Conformal Gauge

The remaining substantive question is the continuum position measure. The discrete-counting argument that forced vertex-counting in §6.2 does not directly transfer: the continuum analog of "vertex-counting" is $\int d\mu$, and the question is precisely whether $d\mu$ is uniquely fixed by the primitive structure.

### 12.1 The dimensional-content question

In the discrete regime, $b_K(u)$ is a bandwidth value at vertex $u$ — interpretable as an edge-weight integral (Primitive 04 §2: $w : E \to \mathbb{R}_{\geq 0}$) that is unambiguous and primitive-level fixed. The discrete total $b_\mathrm{total} = \sum_K \sum_u b_K(u)$ is similarly unambiguous.

In the continuum regime, $b_K(x)$ is a bandwidth *density* — a value per unit volume on $M$. To define a density, a reference measure on $M$ is required: the density's value depends on what "unit volume" means. This is the standard density/measure relationship in differential geometry: a volume form $d\mu$ and a density $f$ satisfy $f \cdot d\mu = (\text{invariant content})$ together, but neither factor is independently invariant.

**Implication for the continuum lift.** The combination $b_K(x) \cdot d\mu(x)$ is the well-defined invariant local bandwidth content at $x$ — established as the continuum limit of the discrete edge-weight integral over a thickened-vertex neighborhood. But the *separate factors* $b_K(x)$ and $d\mu(x)$ are co-defined: choosing a different volume form $d\mu' = \Omega^D d\mu$ requires correspondingly rescaling $b_K' = \Omega^{-D} b_K$ to keep the product invariant.

This is not an ED-specific issue. It is the standard density/measure gauge structure inherent to differential geometry. Lattice-to-continuum lifts in any field theory exhibit it; lattice spacing serves as a fiducial scale absorbed into field renormalisation.

### 12.2 The diagonal-equals-bandwidth constraint, re-examined

The diagonal-equals-bandwidth constraint reads

$$
\langle P \mid P \rangle = \sum_K \int_M d\mu(x) \cdot b_K(x) = b_\mathrm{total}. \qquad (16)
$$

The constraint is conformally invariant under the simultaneous rescaling

$$
d\mu \to \Omega^D \, d\mu, \quad b_K \to \Omega^{-D} \, b_K, \qquad (17)
$$

which keeps $b_K \cdot d\mu$ invariant. The constraint fixes the *combination* but not the *separate factors*. **The diagonal-equals-bandwidth argument therefore does not by itself force $d\mu$ uniquely.** It forces $d\mu$ up to a conformal gauge choice, with the gauge choice corresponding to a choice of $b_K$ normalisation.

This is the substantive structural finding of the continuum lift: the lift is *not* a single answer but a one-parameter family of equivalent descriptions related by (17). The remaining question is whether this family represents a physical ambiguity (different gauge choices giving different physical predictions) or a description redundancy (all gauge choices giving identical predictions).

### 12.3 Resolution: the gauge is description redundancy

We compute the inner product under (17). The participation measure transforms as $P_K = \sqrt{b_K} \cdot e^{i \pi_K} \to \sqrt{\Omega^{-D} b_K} \cdot e^{i \pi_K} = \Omega^{-D/2} P_K$ (the phase is unaffected). Then

$$
\langle P \mid Q \rangle' = \sum_K \int_M (\Omega^D \, d\mu) \cdot (\Omega^{-D/2} P_K)^* \cdot (\Omega^{-D/2} Q_K) = \sum_K \int_M d\mu \cdot P_K^* Q_K = \langle P \mid Q \rangle. \qquad (18)
$$

**Every inner-product value is invariant.** Both diagonal $\langle P \mid P \rangle$ and off-diagonal $\langle P \mid Q \rangle$ for arbitrary $P, Q$ take the same numerical values regardless of which conformal representative of $d\mu$ is chosen, provided $b_K$ is correspondingly rescaled.

The conformal "freedom" is gauge redundancy, not physical ambiguity. Two observers using conformally-related $(b_K, d\mu)$ pairs compute identical inner products for identical states.

### 12.4 What is fixed and what is gauge

The conformal redundancy (17) operates *within* a conformal class of $(b_K, d\mu)$ pairs. The conformal class itself is fixed by the *ratio structure* of bandwidth gradients on $M$:

- The acoustic metric $g_{ab}$ on $M$ is constructed from bandwidth gradients (Primitive 06 + Primitive 04) in the Phase-3 framework.
- The angles defined by $g$ — which orthogonality relations hold among tangent vectors — are determined by ratios $b_i / b_j$ of bandwidth gradients in different directions.
- These ratios are conformally invariant under (17): the $\Omega^{-D}$ factor cancels in any ratio, leaving primitive-level invariants.

**The conformal class of $g$ — and hence of $d\mu$ — is fixed by the primitives.** What remains gauge-redundant is the choice of representative within the class — equivalently, the choice of "absolute scale" for $d\mu$ given the physically-fixed angle structure.

This is the standard structure of a gauge theory: a primitive-level invariant content (the conformal class) and a description-level redundancy (the representative within the class). The gauge is fixed by convention, not by additional primitive commitments.

### 12.5 Primitive 12 internal residuals

We address the remaining concern: do Primitive 12's open items propagate into ambiguity in $d\mu$? Each is examined for independence from the inner-product structure:

- **Commitment weighting $w(\varepsilon)$** determines how each commitment contributes to the thickening field $\tau$. This is a property of thickening *dynamics*, not of the inner-product structure on $M$. Different choices of $w(\varepsilon)$ yield different $\tau$ profiles and different $M$'s, but each $M$ has its own well-defined inner product per (15). Different $M$'s are different physical settings, not different inner products on the same setting. **Independent of inner-product structure.**
- **Continuum-validity threshold for $\tau$** specifies when the continuum description is valid versus the discrete graph description. This is a regime-boundary question, not an inner-product structure question. Below threshold, the discrete inner product applies; above, the continuum. **Independent of inner-product structure.**
- **Local un-thickening rates** affect the time-evolution of $M$ and $\tau$, not the inner-product structure on a given $M$ at a given time. **Independent of inner-product structure.**
- **Saturation at $\tau_\mathrm{max}$** affects thick-regime asymptotics, not the inner-product structure at any specific finite $\tau$. **Independent of inner-product structure.**

**All Primitive-12 internal residuals are independent of the inner-product structure on $M$.** They affect what $M$ looks like, when continuum-field descriptions are valid, and how $M$ evolves — but not the structural form of the inner product on a given $M$.

### 12.6 Verdict

L2 is forced up to a conformal gauge redundancy (17) that leaves all inner-product values invariant. The conformal class of $d\mu$ is fixed by the bandwidth-gradient ratio structure of the acoustic metric. Primitive 12's internal residuals are independent of the inner-product structure and do not propagate.

**Falsifiers F3-cont and F-thickening are both dispatched.** F3-cont is reframed: the conformal redundancy is real but is gauge-redundancy, not physical ambiguity. F-thickening is dispatched directly: each P12 §2.13 residual is independent of the inner-product structure.

---

## 13. The Gauge Structure, Made Explicit

This section consolidates §12's findings into an explicit characterisation of the gauge structure for downstream reference.

### 13.1 The transformation rule

The conformal gauge acts on the pair $(b_K(x), d\mu(x))$ by

$$
(b_K(x), d\mu(x)) \to (\Omega^{-D}(x) \cdot b_K(x), \Omega^D(x) \cdot d\mu(x)) \qquad (19)
$$

where $\Omega(x) > 0$ is an arbitrary smooth scalar field and $D = \dim M$. The rule preserves the local bandwidth content $b_K(x) \cdot d\mu(x)$ — the invariant quantity inherited as the continuum limit of the discrete edge-weight integral.

### 13.2 The participation-measure transformation

The participation measure (1) transforms as

$$
P_K(x) = \sqrt{b_K(x)} \cdot e^{i \pi_K(x)} \to \Omega^{-D/2}(x) \cdot P_K(x), \qquad (20)
$$

with the phase factor $e^{i \pi_K}$ unchanged.

### 13.3 The inner-product invariance

Substituting (19) and (20) into (15):

$$
\langle P \mid Q \rangle' = \sum_K \int_M (\Omega^D d\mu) (\Omega^{-D/2} P_K)^* (\Omega^{-D/2} Q_K) = \sum_K \int_M d\mu \cdot P_K^* Q_K = \langle P \mid Q \rangle. \qquad (21)
$$

The inner product is invariant under (19)–(20). Both diagonal and off-diagonal pairings for arbitrary $P, Q$ are invariant.

### 13.4 What this implies for physical content

Born probabilities are bandwidth ratios $b_K / \sum b$ and are explicitly gauge-invariant by cancellation of $\Omega$. Bell correlations are inner-product overlaps and are invariant per (21). Heisenberg variances are bandwidth allocations and are invariant by the same cancellation as Born. **No physical quantity carries gauge dependence.**

### 13.5 Structural analogs in physics

The gauge structure (19)–(20) is structurally analogous to several familiar examples from established physics:

- **Weyl rescaling in conformal field theory.** Fields and metrics co-transform under local rescalings; primary fields carry conformal weights. Physical correlators are conformally invariant up to a known anomalous factor.
- **Lattice-spacing renormalisation in lattice QFT.** Lattice spacing is a fiducial scale absorbed into field renormalisation; physical predictions are independent of the spacing once the continuum limit is taken.
- **Coordinate freedom in general relativity.** Different coordinate systems yield different metric components, but invariant quantities (curvatures, scalars) carry physical content.

In each case, the redundancy is acknowledged, named, and either fixed by convention or quotiented out. None of those frameworks is considered "not derived" because of the redundancy. The U2-continuum gauge sits in the same family.

---

## 14. Theorem: U2-Continuum

> **Theorem (U2-Continuum; Continuum Inner Product, Gauge-Invariant Form).** Let $G = (V, E)$ be a participation graph thickened by Primitive 12 to an emergent manifold $M$ with bandwidth fields $b_K(x)$ and the acoustic metric supplied by the Phase-3 framework. Then there exists a unique sesquilinear inner product on the participation-measure space $\mathcal{P}(M)$,
>
> $$
> \langle P \mid Q \rangle_\mathrm{cont} = \sum_K \int_M d\mu(x) \cdot P_K^*(x) \cdot Q_K(x), \qquad (22)
> $$
>
> with the following structural properties:
>
> 1. **Existence.** The continuum inner product is the strict $\tau \to \infty$ limit of the U2-Discrete inner product, with no smearing kernels surviving the lift.
> 2. **Uniqueness up to conformal gauge.** The pair $(b_K(x), d\mu(x))$ admits a one-parameter rescaling (19) for any smooth $\Omega(x) > 0$.
> 3. **Gauge invariance of inner-product values.** Every inner-product value $\langle P \mid Q \rangle$ (diagonal and off-diagonal) is invariant under the gauge per (21).
> 4. **Conformal class fixed.** The conformal class of $d\mu$ is fixed by the bandwidth-gradient ratio structure of the acoustic metric.
> 5. **Independence from Primitive 12 internal residuals.** The structural form of the inner product does not depend on Primitive 12's open items (commitment weighting, continuum-validity threshold, un-thickening rates, saturation behaviour).
>
> **The continuum inner product is forced in every sense relevant to physical content.** The gauge (19) is a description redundancy structurally analogous to gauge fixing in any geometric / field-theoretic framework; it does not affect any inner-product value, any Born probability, any Bell correlation, or any Heisenberg variance.

**Proof outline.** Section 9 establishes Primitive 12 + Phase-3 inputs supplying the existence of $M$ with a candidate metric and volume form. Section 10 closes L1 (continuum channel measure) by transferring discrete arguments verbatim to discrete-channel cases and applying the diagonal constraint to continuous channel spectra to force Lebesgue-on-channel-space. Section 11 closes L3 (local pointwise pairing) by transferring the four-band orthogonality, non-contextuality, and kinematic/dynamic separation arguments verbatim to the continuum, and dispatching the Primitive-12-smearing concern via the strict $\tau \to \infty$ limit. Section 12 closes L2 (continuum position measure) by showing that the diagonal-equals-bandwidth constraint forces only the combination $b_K \cdot d\mu$, with the conformal redundancy (17) emerging as a description-level gauge under which the inner product (21) is invariant; the conformal class itself is fixed by bandwidth-gradient ratios; Primitive-12 internal residuals are verified independent of the inner-product structure. Section 13 consolidates the gauge structure. $\square$

---

# PART III — IMPLICATIONS

## 15. Downstream Cascade

The U2 derivation was opened because U2 was the single shared structural conditionality on three downstream theorems: the Born rule (Theorem 10 of [5]), the Bell–Tsirelson bound (Phase-1 Step 4 of [3]), and the Heisenberg uncertainty principle (Phase-1 Step 5 of [3]). With both the discrete (Section 8) and continuum (Section 14) results in hand, the conditionalities are fully resolved.

### 15.1 Born rule (Theorem 10)

**Pre-U2 status.** The Born rule was derived in [5] via the Gleason–Busch route, conditional on the participation-measure framework's sesquilinear inner product. The single residual conditionality was the U2 commitment.

**Post-U2 status.** The Hilbert-space arena (Gleason assumption A1) is now forced: in the discrete regime by §8 directly; in the continuum regime by §14 with all inner-product values gauge-invariant. The Born rule promotes from forced-conditional-on-U2 to forced-unconditional across both regimes. Born probabilities are bandwidth ratios and are explicitly gauge-invariant; the continuum gauge does not introduce any conditionality on physical predictions.

### 15.2 Bell–Tsirelson

**Pre-U2 status.** The Bell–CHSH bound $|S| \leq 2\sqrt{2}$ at the Tsirelson value was derived [3, §3.4] using Cauchy–Schwarz and operator-norm bounds on the bipartite Hilbert space, conditional on U2 supplying the Hilbert-space structure on $\mathcal{H}_A \otimes \mathcal{H}_B$.

**Post-U2 status.** With U2 forced (discrete regime) or forced-up-to-gauge (continuum regime), Bell–Tsirelson promotes to forced-unconditional across both regimes. Bell correlations are inner-product overlaps; per (21), they are gauge-invariant.

### 15.3 Heisenberg uncertainty

**Pre-U2 status.** The Heisenberg uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ was derived [3, §3.5] from the Fourier-conjugate decomposition of the adjacency-band bandwidth budget, with the bound saturated by Gaussian wavepackets. The derivation used the $L^2$-norm structure inherited from U2.

**Post-U2 status.** With U2 forced, Heisenberg promotes to forced-unconditional across both regimes. Variance bounds are bandwidth allocations and are gauge-invariant by the same mechanism as Born.

### 15.4 Consolidated table

| Theorem | Pre-U2 status | Post-U2 (discrete) | Post-U2 (continuum) |
|---|---|---|---|
| Born rule (Theorem 10) | Forced on U2 | **Forced unconditional** | **Forced unconditional** (gauge-invariant) |
| Bell–Tsirelson | Forced on U2 | **Forced unconditional** | **Forced unconditional** (gauge-invariant) |
| Heisenberg uncertainty | Forced on U2 | **Forced unconditional** | **Forced unconditional** (gauge-invariant) |

**Three of the QM-emergence program's foundational theorems are now forced-unconditional across both discrete and continuum regimes**, with the conformal gauge as a description-level convention that does not enter physical predictions.

---

## 16. Discussion

### 16.1 What U2-FORCED supersedes

The QM-emergence framework [3] presented its Phase-1 results conditional on five upstream structural commitments labelled U1–U5. U2 — the sesquilinear inner product — has now been derived rather than postulated, reducing the upstream-commitment inventory from five to four (U1, U3, U4, U5) plus a description-level continuum-lift conformal-gauge convention.

U2's removal from the active commitment list has substantial leverage:

- **Born / Bell / Heisenberg promoted simultaneously.** All three downstream theorems share U2 as a single structural conditionality. Promoting U2 promotes all three.
- **Hilbert-space arena no longer postulated.** The Hilbert-space structure that all of standard quantum mechanics rests on — and that prior derivations of the Born rule (Gleason, Busch, Caves–Fuchs–Manne–Renes) take as ambient — is now structurally derived rather than assumed.
- **Methodological pattern established.** The decomposition-and-derivation pattern used here parallels the Born/Gleason result of [5]: a single upstream commitment is decomposed into automatic, interpretive, and load-bearing sub-claims; each load-bearing item is closed by independent primitive-level arguments; no new structural commitments are introduced.

The pattern composes well across regimes when the underlying primitives are regime-independent, as demonstrated explicitly by the discrete-to-continuum transfer of L1 and L3 in Sections 10–11. Future arcs targeting U1, U3, U4, or U5 should be expected to follow the same pattern.

### 16.2 The continuum gauge: structural significance

The conformal gauge (19) is the most distinctive structural finding of the continuum-lift derivation. It is worth being precise about its character.

A *conditional* result would mean: different gauge choices give different physical predictions, and a residual structural commitment is needed to nail down predictions.

A *forced-up-to-gauge* result means: different gauge choices give *identical* physical predictions; the framework is complete; the gauge is a description redundancy.

Section 12.3's calculation establishes the second case unambiguously. Born probabilities, Bell correlations, and Heisenberg variances all depend only on conformally-invariant ratios or inner-product overlaps. The bare expressions for $b_K(x)$ and $d\mu(x)$ carry the gauge; their physical content does not.

This is the structural pattern of any well-formulated gauge theory. The redundancy is real and worth naming explicitly — pretending it does not exist would misrepresent the structure. But naming it does not weaken the result; it strengthens the result by making the structure of the lift explicit and downstream-citable.

### 16.3 Distinguishing from "the inner product is just postulated"

A potential reading of the U2 result: "ED's inner product is one specific choice among many, with the choice partially fixed by gauge." This reading is incorrect.

The correct reading: ED's inner product is uniquely determined by the primitive structure up to a description redundancy that does not affect any physical prediction. The conformal class of $d\mu$ is fixed by bandwidth-gradient ratios; the relative orientations of vectors in $\mathcal{H}(x)$ are fixed by the four-band orthogonality and non-contextuality structures; the diagonal-equals-bandwidth constraint links the inner product to the primitive-level bandwidth content. Multiple gauge representatives describe the same unique physical structure; they are not multiple physical structures.

Compare: in general relativity, a metric tensor $g_{\mu\nu}$ has different components in different coordinate systems, but the underlying geometry is unique. The coordinate freedom is a description redundancy, not an indeterminacy of the geometry.

### 16.4 What U2-FORCED does not claim

In the spirit of methodological honesty established in earlier ED publications [4, 6]:

- U2-FORCED does not make any new empirical predictions. ED reproduces standard QM exactly at the tested level for both regimes.
- U2-FORCED does not derive $\hbar$ from primitives; $\hbar$ remains inherited from the Dimensional-Atlas Madelung anchoring.
- U2-FORCED does not address the remaining four upstream commitments (U1, U3, U4, U5); those are separate structural derivations.
- U2-FORCED does not eliminate the *need* to choose a gauge for explicit computations; it shows that the choice is convention rather than structural commitment.

### 16.5 What U2-FORCED legitimately claims

- The sesquilinear inner product $\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u) Q_K(u)$ is forced by Primitives 01 + 03 + 04 + 07 + 09 + 11 + the four-band orthogonality of Primitive 04 + the non-contextuality result of [5], with no new structural commitment.
- The continuum lift is forced under Primitive 12 thickening + Phase-3 acoustic metric, with explicit gauge structure (19).
- The Hilbert-space structure underlying standard QM derivations is now structurally derivable rather than postulated within the ED framework.
- Three downstream theorems (Born, Bell–Tsirelson, Heisenberg) are simultaneously promoted to forced-unconditional in both regimes.
- The structural-derivation methodology is replicable: future arcs targeting U1, U3, U4, U5 can apply the same decomposition-and-derivation pattern.

---

## 17. A Non-Technical Explainer

*This section is intended for a general scientific audience and is not part of the formal derivation.*

### 17.1 The hidden bookkeeping question

Quantum mechanics is famously the theory of vectors in a complex Hilbert space. Wavefunctions are vectors; observables are operators on those vectors; probabilities come from inner products between vectors. This setup is so standard that it is rarely questioned — it is just what quantum mechanics *is*.

But there is a piece of the structure that is rarely spelled out. To say two quantum states "agree" or "disagree" — to combine two amplitudes into a single real-valued probability — you need a specific operation called the *sesquilinear inner product*. It takes two complex-valued vectors and returns a single complex number, with a particular asymmetric structure (one vector gets complex-conjugated, the other does not).

Standard quantum mechanics gives you this inner product on a silver platter. It is part of what defines a Hilbert space; you use it without asking where it came from.

The Event Density framework asks: where *does* it come from? If we are claiming to derive quantum mechanics from a deeper ontology — a participation graph with bandwidth on its edges and channels as primitive sub-structures — then the inner product had better be derivable too. Otherwise, the framework would be quietly assuming exactly what it claims to derive.

### 17.2 Three layers, three structural commitments

The derivation has three layers, each a separate structural question.

The first layer is whether the participation-measure values can be added and rescaled consistently — whether they form a complex vector space at all. This is answered automatically: bandwidth and phase combine into complex numbers, and complex numbers are closed under addition and complex multiplication. No primitive obstacle.

The second layer is whether the inner product has the right asymmetric type — sesquilinear rather than some other complex bilinear form. This is forced by two structural facts working together. First, bandwidth — which is the diagonal of the inner product — must be a non-negative real number. Second, bandwidth does not depend on overall phase: rotating the participation measure by $e^{i\alpha}$ does not change any physical content. The combination of "non-negative diagonal" and "phase-rotation invariance" eliminates other candidate pairings (complex-bilinear violates phase invariance; real-bilinear is too weak to encode interference). Sesquilinearity is the unique structure that survives.

The third layer is the specific way the inner product aggregates over channels and over positions. Three sub-questions: how do channels contribute (with what weighting), how do positions contribute (with what weighting), and is the basic pairing strictly local at each (channel, position) slot? Each closes via independent primitive-level arguments. There is no source within the primitives for non-trivial channel weighting. There is no source for non-trivial vertex weighting (in the discrete regime). And four-band orthogonality, channel non-contextuality, and the basic separation between kinematics and dynamics together forbid any cross-slot kernel mixing. The local Kronecker-delta structure is uniquely forced.

The discrete result is: the inner product is forced by the primitive structure. No new structural commitment is introduced anywhere in the derivation.

### 17.3 The continuum lift and its gauge

For continuum applications — particles moving through smooth space, beams of light propagating along continuous trajectories, cosmological structures evolving over continuous spacetime — the discrete inner product needs to lift to a continuum form. Most of the lift is straightforward: the channel-aggregation transfers cleanly, the local-pairing structure transfers cleanly. The substantive question is the position-aggregation: does the discrete vertex-counting lift uniquely to a continuum integral with a uniquely determined volume form?

Here a subtle phenomenon emerges. In the continuum, "bandwidth at point $x$" becomes a *density* — a value per unit volume — and densities require a reference measure to be defined. The combination "bandwidth density times volume measure" is the well-defined invariant; the separate factors are co-defined and admit a one-parameter rescaling.

This is a familiar phenomenon in modern physics. Lattice quantum field theories have a "lattice spacing" that gets absorbed into field renormalisation. Conformal field theories have a "Weyl rescaling" symmetry. General relativity has coordinate freedom. In each case, the redundancy is real but is a description redundancy: physical predictions are independent of the choice.

The U2-continuum gauge sits in the same family. We checked the explicit calculation: under the simultaneous rescaling of bandwidth density and volume measure (with the participation measure itself rescaling by half the exponent), every inner-product value is exactly invariant. Born probabilities, Bell correlations, Heisenberg variances — all gauge-invariant by construction.

### 17.4 What this gives us

With the inner product forced — discretely outright, in the continuum up to a description-level gauge that affects no physical prediction — three of quantum mechanics's most famous results become unconditional. The Born rule (probability of a measurement outcome equals squared amplitude). The Bell–Tsirelson bound (the maximum quantum correlation between two entangled systems). The Heisenberg uncertainty principle (the floor on the product of position and momentum uncertainties). All three were previously derivable in ED conditional on the inner product being granted; with this paper they become unconditional in the discrete regime where ED's primitive ontology lives most naturally, and unconditional with explicit gauge structure in the continuum.

Quantum mechanics, on this view, is no longer a collection of postulates that happen to fit experiment. It is what the participation-graph ontology produces, all the way down — including the inner-product structure that makes any of it work.

### 17.5 The honest framing

The framework still rests on its primitives. Whether *those* are right — whether participation, bandwidth, channels, polarity, commitment, and thickening are the correct foundational concepts — is a separate question and remains the load-bearing one. ED's claim is not that quantum mechanics is reducible to nothing; it is that quantum mechanics's *postulates* (Schrödinger evolution, Born probabilities, Bell correlations, Heisenberg uncertainty, the Hilbert-space structure underlying all of them) are reducible to a smaller set of *structural commitments* about participation, bandwidth, and channels.

That smaller set is still load-bearing. The framework stands or falls on whether the primitives are the right ones. But the postulates of quantum mechanics no longer have to be assumed independently — they emerge from the framework as structural consequences. The U2 result, presented here, completes the structural-foundations case for the inner product itself, both discretely and in the continuum, with explicit honesty about the gauge that the continuum lift introduces.

---

## 18. Recommended Next Steps

For the author and the broader ED program, the following items follow from the U2 result:

1. **Update the QM-emergence synthesis paper.** The synthesis paper [3] presents Phase-1 results conditional on five upstream commitments U1–U5. With U2 derived, the upstream-commitment inventory should be updated to four items (U1, U3, U4, U5) plus the description-level continuum-lift conformal-gauge convention. Sections 3.3 (Born), 3.4 (Bell), and 3.5 (Heisenberg) should cite the present paper for the unconditional promotion. Section 4 (upstream commitments) requires the substantive revision.

2. **Open arcs for the remaining upstream commitments.** With the methodological pattern now established and replicable, the next-most-leveraged structural arcs target U1 (the participation-measure construction itself), U3 (the participation-measure evolution equation), U4 (the momentum-basis identification), and U5 (the adjacency-band conjugate partition). Recommended priority: U5 first (cleanest per the synthesis paper's program-priority assessment), then U1 (highest leverage — promoting it would make the entire QM-emergence program structurally complete in the participation-measure framework). U3 and U4 require additional Step-2 (Schrödinger emergence) context.

3. **Gauge-fixing convention for downstream applications.** The U2-Continuum Theorem is forced-up-to-gauge; downstream applications requiring explicit calculations may benefit from a fixed gauge convention. The natural choice is the gauge in which $b_K(x)$ carries its discrete-counting normalisation at the $\tau \to \infty$ limit, preserving the diagonal-equals-bandwidth interpretation in its most natural form. This is convention work, not derivation work, and can be deferred until a specific application motivates it.

4. **Sensitivity to Primitive 09 amendments.** The C3b derivation (Section 5) relies critically on Primitive 09's polarity being $U(1)$-valued. Any future amendment widening the polarity symmetry (e.g., for SM-gauge-group emergence work) would require re-deriving C3b under the new structure. Future SM-gauge or extended-polarity arcs should know this dependency exists; the C3b derivation provides a template for the re-derivation.

---

## Appendix: Section-to-Memo Mapping

The present paper integrates the results of two derivation arcs (the *U2-discrete* arc with five memos and the *U2-continuum* arc with four memos). For traceability, the mapping between paper sections and underlying memos is as follows.

| Paper section | Underlying arc / memo | Memo content summary |
|---|---|---|
| §3 (Decomposition into C3a/C3b/C3c) | U2-discrete Memo 01 | Three-part decomposition; primitive mapping; classification by structural status |
| §4 (C3a linearity) | U2-discrete Memo 02 (§2) | Complex-vector-space closure of $\mathcal{P}$ from construction (1) |
| §5 (C3b sesquilinearity) | U2-discrete Memo 02 (§3) | Three-step derivation: Step A diagonal-equals-bandwidth, Step B $U(1)$-invariance ruling out alternatives, Step C band-additivity forcing slot asymmetry |
| §6.1 (c1 channel measure) | U2-discrete Memo 03 (§2) | No primitive-level inter-channel weighting + diagonal constraint |
| §6.2 (c2 vertex measure) | U2-discrete Memo 03 (§3) | No primitive-level inter-vertex weighting + diagonal constraint + graph symmetry |
| §6.3 (c3 local pointwise pairing) | U2-discrete Memo 03 (§4) | Three independent arguments forbidding cross-slot kernels |
| §8 (U2-Discrete Theorem) | U2-discrete Memos 04, 05 | Theorem-grade synthesis + closure-and-summary |
| §9 (Primitive 12 + Phase-3 mapping) | U2-continuum Memo 01 | Decomposition into L1/L2/L3; Primitive 12 / Phase-3 inputs |
| §10 (L1 channel measure) | U2-continuum Memo 02 (§2) | Discrete-argument transfer + continuous-channel-spectrum extension |
| §11 (L3 local pairing) | U2-continuum Memo 02 (§3) | Three discrete arguments transferring + Primitive-12-smearing dispatch |
| §12 (L2 position measure) | U2-continuum Memo 03 | Diagonal constraint, conformal redundancy emergence, gauge as description redundancy, Primitive-12 internal residuals examined |
| §13 (Gauge structure) | U2-continuum Memo 03 (§§3, 4) | Explicit gauge transformation, inner-product invariance, what is fixed vs gauge, structural analogs |
| §14 (U2-Continuum Theorem) | U2-continuum Memo 03, Memo 04 | Theorem-grade synthesis with five structural properties |
| §15 (Downstream cascade) | U2-discrete Memo 04, U2-continuum Memo 03 | Three-theorem promotion across both regimes |
| §16 (Discussion) | U2-continuum Memo 04 | Position in ED program, methodological pattern, distinguishing from "just postulated" |
| §17 (Public explainer) | U2-discrete Memo 05 §6, U2-continuum Memo 04 §6 | Lifted with light editing from the closure-memo public-explainer sections |

---

## References

[1] A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," *Journal of Mathematics and Mechanics* **6**, 885–893 (1957).

[2] *Phase-1: QM Emergence Structural Completion.* `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.{md,tex,pdf}`. Internal ED program reference establishing the Phase-1 five-step QM-emergence framework.

[3] *Arc R: Relativistic Kinematics and Dynamics in Event Density.* `papers/Arc_R/paper_arc_r.{md,tex,pdf}`.

[4] *Arc Q: QFT Extension in Event Density.* `papers/Arc_Q/paper_arc_q.{md,tex,pdf}`.

[5] *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* `papers/Born_Gleason/born_gleason_paper.{md,tex,pdf}`. Companion paper establishing Theorem 10.

[6] *Arc N: Non-Markovian Structure as a Forced Memory-Kernel Layer of Event-Density Theory.* `papers/Arc_N/arc_n_paper.{md,tex,pdf}`.

[7] P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," *Physical Review Letters* **91**, 120403 (2003).

[8] C. M. Caves, C. A. Fuchs, K. K. Manne, and J. M. Renes, "Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements," *Foundations of Physics* **34**, 193–209 (2004).

[9] *Phase-3: Gravitational Sector of Event-Density Theory.* `papers/Phase_3/` (in preparation).

[10] *Arc M: Chain-Mass Structure in Event Density.* `papers/Arc_M/paper_arc_m.{md,tex,pdf}`.

---

*Manuscript prepared April 2026. Source materials: `arcs/U2/` five-memo discrete-regime arc and `arcs/U2_continuum/` four-memo continuum-lift arc, integrated into a single publishable document.*
