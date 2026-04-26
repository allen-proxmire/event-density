# The U1 Theorem: Deriving the Participation Measure from Primitive Structure

**Allen Proxmire**

*April 2026*

---

## Abstract

We establish that the participation-measure construction $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ — the foundational structural carrier of the Event-Density (ED) QM-emergence framework — is a forced structural consequence of the ED primitive stack rather than a postulate. The construction's four structural properties — its complex-valued range, its polar decomposition, its squared-magnitude relation $b_K = |P_K|^2$, and its identification of the phase with Primitive 09's polarity — are each derived from primitive-level kinematic content (Primitives 03, 04, 07, 09) plus standard mathematical infrastructure (Frobenius's classification of finite-dimensional associative real division algebras, the polar-decomposition theorem on $\mathbb{C}$, $U(1)$ representation theory, and quadratic-form classification). The complex-valued range is forced by Primitive 09's commitment to $U(1)$-valued polarity combined with Frobenius's enumeration: $\mathbb{R}$ admits no faithful $U(1)$ action, and $\mathbb{H}$ carries $\mathrm{SU}(2)$ structure incompatible with Primitive 09's $U(1)$-only content. The squared-magnitude relation is forced by Primitive 04's kinematic bandwidth additivity over disjoint channel-subsets combined with Primitive 09's $U(1)$-invariance of bandwidth and the Cauchy functional equation, which uniquely selects the exponent 2 from among admissible alternatives. The derivation operates with the leanest structural inputs of any arc in the QM-emergence program — no downstream item (U2, Theorem 10, U5, Bell, Heisenberg) appears as input — establishing that the participation measure is the most upstream theorem-grade structural commitment of the framework. The downstream cascade is the largest in the program: U2-Discrete, U2-Continuum, Theorem 10 (Born), U5, Bell–Tsirelson, and Heisenberg uncertainty all promote simultaneously from forced-conditional-on-U1 to forced-unconditional. The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces to two items (U3, U4) plus a description-level continuum gauge, with the participation-measure layer and the Hilbert-space layer of the framework now structurally complete at theorem grade. Three of the four foundational quantum-mechanical postulates — Born, Bell–Tsirelson, Heisenberg — are now FORCED-unconditional structural consequences of the ED primitive ontology.

---

## 1. Introduction

The Event-Density (ED) program seeks to derive the structural content of standard quantum mechanics from a primitive ontology consisting of micro-events, participation relations, bandwidth, channels, polarity, and a small number of additional kinematic and dynamical primitives. The QM-emergence Phase-1 framework [1] presents non-relativistic single-particle quantum mechanics — Schrödinger evolution, the Born rule, Bell-inequality-violating correlations at the Tsirelson bound, the Heisenberg uncertainty relation — as structural consequences of a single primitive-level object: the *participation measure*

$$P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}.$$

This complex-valued field, indexed by channel $K$, position $x$, and time $t$, fuses Primitive 04 (bandwidth $b_K$, a non-negative real edge-weight on the participation graph) with Primitive 09 (tension polarity $\pi$, a $U(1)$-valued phase). The squared magnitude recovers the bandwidth content: $b_K = |P_K|^2$.

The participation measure has been the load-bearing carrier of the QM-emergence framework since its initial development. Every downstream structural result — the sesquilinear inner product on the participation-measure space (U2), the Born rule via the Gleason–Busch path (Theorem 10), the adjacency-band Fourier-conjugate partition (U5), the Bell–CHSH bound at $|S| \leq 2\sqrt{2}$, the Heisenberg uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ — uses $P_K$ as a constructed object and inherits a structural conditionality on the participation-measure construction itself.

In the original development, the participation-measure construction was adopted provisionally as **upstream commitment U1** of the QM-emergence Phase-1 framework, with nine constraints (C1–C9) enumerated as structural commitments the construction must satisfy. The framework's synthesis paper subsequently classified U1 as the most fundamental of the program's five upstream commitments: "U1 alone generates most of the downstream structure; U2–U5 refine specific aspects" [1, §4.2]. Promoting U1 from CANDIDATE to FORCED was identified as the highest-leverage open structural question in the QM-emergence program — its closure would propagate through the entire framework, promoting six downstream theorems simultaneously.

This paper presents the U1 derivation and its verdict. We establish that the participation-measure construction is forced by the joint action of Primitives 03, 04, 07, 09 in their kinematic content, plus Frobenius's classification of finite-dimensional associative real division algebras, plus standard $U(1)$ representation theory and quadratic-form classification on $\mathbb{C}$. The derivation operates with the leanest structural inputs of any arc in the QM-emergence program: U1 is upstream of every downstream item, so none of those items can be used as inputs without circularity. The methodological constraint is acute, but the derivation closes cleanly.

The four sub-features of the U1 construction — complex-valued range, polar decomposition, squared-magnitude exponent, phase-equals-polarity identification — are each treated separately. Two of the four (polar decomposition; phase identification) close via standard mathematical and primitive-enumeration arguments. The two load-bearing items are the algebraic-structure question (why $\mathbb{C}$ rather than $\mathbb{R}$ or $\mathbb{H}$?) and the magnitude-exponent question (why is the exponent exactly 2?). Both close via a combination of primitive-level kinematic content and well-established mathematical theorems.

The downstream cascade is the most substantive single-arc consequence in the structural-foundations cycle. Once U1 is forced, every theorem in the QM-emergence Phase-1 program that previously carried a structural conditionality on U1 promotes to FORCED-unconditional status. The Hilbert-space arena of standard non-relativistic quantum mechanics — the wavefunction's complex-valued range, the inner product on its space, the Born-rule probability assignment, the Bell correlation bound, the Heisenberg uncertainty inequality — becomes structurally derivable from the ED primitive ontology rather than postulated alongside the wavefunction.

The paper is organised as follows. Section 2 introduces the primitive-level inputs, the relevant mathematical infrastructure, and the methodological constraint of operating with primitives only. Section 3 states the U1 theorem in formal style. Section 4 presents the derivations: F1 (complex-valued range), F2 (polar decomposition), F3 (magnitude exponent), F4 (phase = polarity). Section 5 audits the falsifiers attached to each sub-feature. Section 6 documents the downstream cascade with an explicit dependency diagram. Section 7 discusses the interpretive significance of the result and its sensitivity flags. Section 8 concludes. The appendix contains the memo-to-theorem mapping documenting the four-memo arc structure underlying the present paper.

---

## 2. Background

### 2.1 The ED primitive stack

The Event-Density program builds physics as forced structural consequences of a small primitive stack on a $3{+}1$-dimensional event manifold. The primitives load-bearing for the U1 derivation are:

- **Primitive 01 (Micro-Event):** discrete events on the event manifold; supplies the vertex set $V$ of the participation graph.
- **Primitive 03 (Participation):** the participation relation between micro-events; supplies the edge set $E$ of the participation graph $G = (V, E)$ along with its homogeneity structure (the relation does not privilege any particular vertex). Primitive 03's homogeneity supports translation symmetry as a kinematic property of the graph.
- **Primitive 04 (Bandwidth):** the graded measure of participation, supplied as an edge weighting $w : E \to \mathbb{R}_{\geq 0}$. Bandwidth admits a four-band orthogonal decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ corresponding to internal-rule, adjacency, environmental, and commitment-reserve components, with conservation along chains in their persistence regime. **Crucially for the U1 derivation, bandwidth is additive over disjoint channel-subsets at the kinematic graph level** — for two disjoint channel-subsets $S_1, S_2 \subseteq \mathcal{K}_\tau(u)$, the bandwidth assigned to their union satisfies $b(S_1 \cup S_2) = b(S_1) + b(S_2)$. This additivity is a primitive-level property of the participation graph, independent of any participation-measure construction or any downstream item.
- **Primitive 07 (Channel):** stable, bandwidth-preserving sub-structures of the participation graph along which a chain's update rule can be repeatedly instantiated. Channels are primitive ontological objects whose identity is intrinsic to the graph, not basis-relative; they supply the channel index set $\mathcal{K}$.
- **Primitive 09 (Tension Polarity):** the phase relation between a chain's update rule and the local ED-flow direction. Primitive 09 commits explicitly to $U(1)$-valued polarity. The primitive's defining text states that polarity is "not a binary in general — it is a phase in the full treatment" and confirms that polarity is "not a scalar" — i.e., polarity is phase-valued, with the $U(1)$ Lie group as its symmetry, not a higher-dimensional angular variable. The participation-measure construction places the polarity phase in the phase factor $e^{i \pi(K, x, t)}$.

The U1 derivation operates from these primitives in their *kinematic* content — properties of the participation graph at a fixed time, independent of any dynamical evolution rule. The participation-measure construction itself, the inner product on the participation-measure space, the Born rule, Bell correlations, Heisenberg uncertainty, and the participation-measure evolution equation are all *downstream* of U1 and cannot be invoked as inputs to U1's derivation. This methodological constraint is acute: the U1 arc operates with the leanest available structural inputs of any arc in the QM-emergence program.

### 2.2 The Frobenius classification

The carrier algebra $\mathcal{A}$ in which the participation measure $P_K(x, t)$ takes its slot-level values must be a finite-dimensional associative real division algebra — finite-dimensional for tractable linear-algebra structure, associative to support standard linear-algebra constructions on the participation-measure space, and a division algebra to support multiplicative structure required by phase factors. The classification of such algebras is the content of a classical theorem due to Frobenius:

**Theorem (Frobenius, 1878).** *Up to isomorphism, the only finite-dimensional associative real division algebras are $\mathbb{R}$ (the real numbers, 1-dimensional), $\mathbb{C}$ (the complex numbers, 2-dimensional), and $\mathbb{H}$ (the quaternions, 4-dimensional).*

The classification reduces the carrier-algebra question to a finite enumeration. Each candidate must be audited for compatibility with Primitive 09's $U(1)$-only commitment and with the structural content the participation-measure construction must carry. The non-associative octonions $\mathbb{O}$ (8-dimensional) are excluded by the associativity requirement and are discussed only briefly in Section 4.1.6.

### 2.3 Quadratic-form classification on $\mathbb{C}$

For the magnitude-exponent question (F3 below), the structural content concerns non-negative real-valued functions $Q : \mathbb{C} \to \mathbb{R}_{\geq 0}$ subject to two constraints: (i) $U(1)$-invariance, $Q(e^{i \alpha} z) = Q(z)$ for all $\alpha$; and (ii) additivity under disjoint-channel combination, $Q(z_1) + Q(z_2)$ when $|z_1|^2 + |z_2|^2$ corresponds to a combined-channel magnitude.

The first constraint reduces $Q(z)$ to a function of $|z|^2$ alone — equivalently, a function $f : \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$ such that $Q(z) = f(|z|^2)$. The $U(1)$ orbits on $\mathbb{C}$ are circles of constant $|z|$; any $U(1)$-invariant function is constant on orbits, hence a function of the orbit-parameter $|z|^2$.

The second constraint forces $f$ to satisfy the **Cauchy functional equation**

$$f(a + b) = f(a) + f(b) \qquad \forall\, a, b \in \mathbb{R}_{\geq 0}.$$

Under non-negativity ($f \geq 0$) and the natural continuity inherited from the participation-graph structure, the unique solution to the Cauchy equation on $\mathbb{R}_{\geq 0}$ is linear: $f(a) = c \cdot a$ for some constant $c \geq 0$. (The pathological discontinuous solutions of the Cauchy equation, constructed using Hamel bases, do not satisfy the non-negativity constraint and are physically irrelevant to the present derivation.) Substituting back: $Q(z) = c \cdot |z|^2$. Setting the overall normalisation $c = 1$ by convention recovers the squared-modulus form.

The mathematical fact that the squared modulus is the unique $U(1)$-invariant additive non-negative form on $\mathbb{C}$ (up to overall scaling) is the foundational content of F3's argument. Alternative exponents $|z|^\alpha$ with $\alpha \neq 2$ fail the additivity constraint, as we show explicitly in Section 4.3.

### 2.4 $U(1)$ representation theory

The $U(1)$ structure of Primitive 09's polarity supports several mathematical facts that load-bear in the U1 derivation:

- **Faithful representations on $\mathbb{C}$.** $U(1)$ acts faithfully on $\mathbb{C}$ by multiplication: $e^{i \alpha} \cdot z \mapsto e^{i \alpha} z$. The action is continuous, linear, and faithful (the kernel of the representation is trivial: $e^{i \alpha} = 1$ only when $\alpha \in 2\pi \mathbb{Z}$).

- **No faithful representation on $\mathbb{R}$.** The continuous group homomorphisms $U(1) \to \mathbb{R}^\times$ (the multiplicative group of nonzero reals, the automorphism group of $\mathbb{R}$ as a 1-dimensional real vector space) are the trivial homomorphism (constant 1) and the sign character $\rho_\pm$ mapping $U(1) \to \{\pm 1\}$. Neither is faithful: the trivial homomorphism collapses all of $U(1)$ to a point, and the sign character has a large nontrivial kernel.

- **Continuous endomorphisms of $U(1)$.** The continuous group homomorphisms $U(1) \to U(1)$ are integer-character maps: $f_n(\theta) = n \theta \pmod{2\pi}$ for some integer $n \in \mathbb{Z}$. The $n = 1$ case (identity) is the natural choice; non-identity choices ($n = 0, n \neq \pm 1$) require primitive-level structural content not supplied by the ED stack.

- **Embeddings of $U(1)$ into higher-dimensional Lie groups.** The Lie group $\mathrm{SU}(2)$ (which is the natural angular structure of the quaternions $\mathbb{H}$) admits $U(1)$ as a 1-parameter subgroup; the set of admissible embeddings is parameterised by the unit 2-sphere $S^2$ of imaginary unit quaternions. No primitive in the ED stack supplies a basis for selecting a specific embedding.

These facts support the F1 and F4 derivations in Section 4.

---

## 3. Statement of the U1 Theorem

We state the U1 theorem in the formal style adopted across the QM-emergence Phase-1 program.

**Theorem (U1; Participation-Measure Construction).** *Let the ED primitive stack supply: bandwidth $b_K(x, t) \in \mathbb{R}_{\geq 0}$ as edge-weight on the participation graph (Primitive 04, with kinematic additivity over disjoint channel-subsets); $U(1)$-valued polarity phase $\pi(K, x, t) \in U(1)$ (Primitive 09, the unique primitive-level angular variable in the stack); and the supporting indexing structure (Primitive 03 participation relations supplying graph homogeneity, Primitive 07 channel index set $\mathcal{K}$). Then the participation-measure carrier and its construction are uniquely forced:*

1. ***Carrier algebra.*** *$P_K(x, t) \in \mathbb{C}$ — the participation measure takes values in the complex numbers. $\mathbb{C}$ is the unique minimal carrier supporting faithful $U(1)$ action with no surplus structure.*

2. ***Polar decomposition.*** *$P_K(x, t) = r_K(x, t) \cdot e^{i \theta_K(x, t)}$ with $r_K \in \mathbb{R}_{\geq 0}$ and $\theta_K \in U(1)$, by the standard polar-decomposition theorem on $\mathbb{C}$.*

3. ***Magnitude exponent.*** *$r_K^2 = |P_K|^2 = b_K$, i.e., the squared magnitude equals bandwidth. The exponent 2 is uniquely forced by Primitive 04 kinematic bandwidth additivity, Primitive 09 $U(1)$-invariance, and the Cauchy functional equation.*

4. ***Phase identification.*** *$\theta_K = \pi(K, x, t)$, i.e., the phase factor is exactly Primitive 09's polarity phase. Primitive 09 is the unique primitive-level $U(1)$-valued angular variable in the ED stack.*

*Together, the participation-measure construction*

$$P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$$

*is uniquely forced by the joint action of Primitives 03, 04, 07, 09 (in their kinematic content) plus standard mathematical infrastructure (Frobenius's classification, the polar-decomposition theorem on $\mathbb{C}$, $U(1)$ representation theory, quadratic-form classification on $\mathbb{C}$).*

**Status:** **FORCED.** No new structural commitment is introduced. No downstream item (U2, Theorem 10, U5, U3, U4, Schrödinger evolution, Bell–Tsirelson, Heisenberg uncertainty) is invoked.

**Scope.** The theorem holds in both the discrete regime (with $x$ ranging over the participation-graph vertex set $V$) and the continuum regime (with $x$ ranging over the emergent manifold $M$ supplied by Primitive 12 thickening). The construction is gauge-compatible with the description-level conformal redundancy identified in the U2-Continuum theorem [3]: under the conformal rescaling $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, the participation measure transforms as $P_K \to \Omega^{-D/2} P_K$, but the *form* of the U1 construction (polar decomposition with $|P|^2 = b$) is preserved.

**Sensitivity flags.** The verdict is conditional on the current primitive stack. Two specific sensitivities are flagged:

- *Primitive 09 widening.* If a future amendment widens Primitive 09's polarity symmetry from $U(1)$ to $\mathrm{SU}(2)$ or higher, F1's dismissal of $\mathbb{H}$ would need re-examination.
- *Primitive 04 weakening.* If a future amendment weakens or removes bandwidth additivity over disjoint channel-subsets, F3's exponent-2 argument would fail.

No current amendments are on the table; the verdict stands under the current primitive stack.

---

## 4. Derivation

We derive the four sub-features of the U1 construction, treating them in the order of structural dependency: F1 (complex-valued range) is derived first, since F2, F3, F4 each presuppose a complex-valued carrier; F2 (polar decomposition) follows immediately from F1 plus standard mathematics; F3 (magnitude exponent) requires the additivity argument; F4 (phase identification) closes via primitive enumeration.

### 4.1 F1 — Complex-Valued Range

#### 4.1.1 The carrier-algebra question

The participation-measure construction must carry, at each $(K, x, t)$ slot, two pieces of primitive-level structural content: the bandwidth magnitude $b_K(x, t) \in \mathbb{R}_{\geq 0}$ from Primitive 04, and the polarity phase $\pi(K, x, t) \in U(1)$ from Primitive 09. The slot-level algebraic carrier $\mathcal{A}$ must support both contents *faithfully*: it must contain (at least implicitly, via embedding) the non-negative reals for the magnitude, and it must support a faithful $U(1)$ action for the phase.

By Frobenius's theorem, the candidate finite-dimensional associative real division algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}$. We audit each.

#### 4.1.2 Dismissal of $\mathbb{R}$

For $\mathcal{A} = \mathbb{R}$, the automorphism group of $\mathbb{R}$ as a 1-dimensional real vector space is $\mathrm{GL}(1, \mathbb{R}) = \mathbb{R}^\times$, the multiplicative group of nonzero reals. The continuous group homomorphisms $U(1) \to \mathbb{R}^\times$ are:

- The trivial homomorphism $\rho \equiv 1$, which collapses all of $U(1)$ to the identity element.
- The sign character $\rho_\pm : U(1) \to \{\pm 1\}$, which has nontrivial kernel containing every $e^{i \alpha}$ with $\cos \alpha > 0$.

Neither homomorphism is faithful. Equivalently: under any continuous $U(1)$ action on $\mathbb{R}$, the orbit structure consists of fixed points only (every $r \in \mathbb{R}$ is mapped to itself or to $-r$, depending on the homomorphism). Primitive 09's polarity content — a continuous $U(1)$-valued phase — cannot be represented faithfully on a real-valued carrier. The phase content is lost.

One could attempt to encode the phase content separately, with a real-valued participation measure $P_K^\mathrm{real}$ stored alongside an explicit phase variable $\theta_K \in U(1)$. But this construction is not a single algebraic carrier — it is a pair $(r, \theta) \in \mathbb{R} \times U(1)$. The natural algebraic structure that combines real magnitude and $U(1)$ phase faithfully into a single object is precisely the polar form: identify $(r, \theta) \leftrightarrow r \cdot e^{i \theta} \in \mathbb{C}$. The "real-valued participation measure with separate phase" construction *is* the complex-valued participation measure under a different name; it is not a structurally distinct alternative.

**$\mathbb{R}$ is dismissed.**

#### 4.1.3 Dismissal of $\mathbb{H}$

For $\mathcal{A} = \mathbb{H}$, the natural angular structure is the Lie group $\mathrm{SU}(2)$ (the unit quaternions), which is 3-dimensional and topologically $S^3$. $\mathrm{SU}(2)$ admits $U(1)$ as a 1-parameter subgroup, but the embedding is not unique: every choice of unit pure-imaginary quaternion $\hat{u}$ (with $\hat{u}^2 = -1$) generates a distinct $U(1)$ subgroup $\{e^{\hat{u} \alpha} : \alpha \in [0, 2\pi)\}$. The set of admissible $\hat{u}$ is the unit 2-sphere $S^2$ in the imaginary part of $\mathbb{H}$.

For Primitive 09's $U(1)$-valued polarity to act on an $\mathbb{H}$-valued participation measure, the construction would have to *select* a specific $\hat{u} \in S^2$ — a specific imaginary unit — to embed $U(1)$ into $\mathrm{SU}(2)$. **This selection is structural content not supplied by any primitive in the ED stack.** Two consequences emerge:

1. **Underdetermination.** The construction would have a continuous family of admissible embeddings parameterised by $\hat{u} \in S^2$, with no structural reason to prefer one over another. The participation-measure construction would be underdetermined at the algebraic level.

2. **Surplus structure.** Even after a specific $\hat{u}$ is selected by fiat, the $\mathbb{H}$-valued participation measure carries $\mathrm{SU}(2)$ phase content beyond the $U(1)$ subgroup actually used by Primitive 09. The "extra" $\mathrm{SU}(2)/U(1) \simeq S^2$ degree of freedom is present in the carrier without primitive-level structural support. Either the participation measure has dynamical content along the surplus $S^2$ direction (requiring primitive-level evolution rules not supplied by the stack), or the surplus content is structurally inert (in which case it is unphysical and should not be in the carrier). Neither alternative is structurally coherent.

Primitive 09's commitment to $U(1)$-only polarity is explicit and load-bearing here. The primitive's defining text states polarity is phase-valued ("not a binary in general — it is a phase in the full treatment") and confirms the phase is one-dimensional ("not a scalar"). Primitive 09 does not supply $\mathrm{SU}(2)$ or higher-dimensional polarity content. A quaternionic carrier would commit the framework to structural content beyond what Primitive 09 supplies, violating the primitive-only methodology of the U1 arc.

**$\mathbb{H}$ is dismissed.**

#### 4.1.4 $\mathbb{C}$ as the unique minimal carrier

For $\mathcal{A} = \mathbb{C}$, the algebra admits a faithful $U(1)$ action by multiplication: $e^{i \alpha} \cdot z \mapsto e^{i \alpha} z$. The action is continuous (smooth in $\alpha$), linear (respects the $\mathbb{C}$-vector-space structure), and faithful (kernel is trivial). The orbit structure: $U(1)$ orbits on $\mathbb{C}$ are circles centered at the origin, plus the fixed point $z = 0$. The orbit space $\mathbb{C}/U(1) \simeq \mathbb{R}_{\geq 0}$ is parameterised by the magnitude $|z|$.

Crucially, $\mathbb{C}$'s automorphism structure as a 2-dimensional real vector space includes $\mathrm{SO}(2) = U(1)$ rotations. There is no surplus angular structure beyond $U(1)$ at the algebraic level — $\mathbb{C}$ is exactly the dimension needed to faithfully carry $U(1)$ action with no extra content. Compare to $\mathbb{H}$, which carries $\mathrm{SU}(2)$ content (3-dimensional Lie group) and forces selection of a $U(1)$ subgroup.

**$\mathbb{C}$ is the unique minimal carrier supporting faithful $U(1)$ action with no surplus structure.** F1 is established.

#### 4.1.5 Independence from downstream items

The argument uses Primitive 09 (supplying the $U(1)$-valued polarity), Frobenius's classification of real division algebras, and standard $U(1)$ representation theory. No downstream item — U2 inner product, Theorem 10 Born structure, U5 partition, Schrödinger evolution, Bell, Heisenberg — is invoked. The argument is fully primitive-level + mathematical.

#### 4.1.6 The octonionic alternative — briefly addressed

The octonions $\mathbb{O}$ are 8-dimensional but non-associative. Frobenius's classification excludes them by hypothesis. Even setting this aside:

- $\mathbb{O}$'s automorphism group is the exceptional Lie group $G_2$ (14-dimensional). Selecting a $U(1)$ subgroup requires choosing an embedding $U(1) \hookrightarrow G_2$ with substantial choice ambiguity (more than the $S^2$ ambiguity for $\mathbb{H}$).
- Non-associativity breaks standard linear-algebra constructions on the participation-measure space (the inner-product structure that U2 supplies has no clean analog over a non-associative algebra; multiplication of "matrices" of octonions is not associative).
- The surplus-structure objection from Section 4.1.3 applies a fortiori: $\mathbb{O}$ carries far more angular content than Primitive 09 supplies.

Octonions are dismissed by the same surplus-structure argument that dismisses $\mathbb{H}$, plus the additional structural cost of non-associativity. We do not consider octonions further.

### 4.2 F2 — Polar Decomposition

#### 4.2.1 The standard polar-decomposition theorem on $\mathbb{C}$

Every nonzero complex number $z \in \mathbb{C} \setminus \{0\}$ admits a unique representation

$$z = |z| \cdot e^{i \arg z}$$

with magnitude $|z| \in \mathbb{R}_{> 0}$ and argument $\arg z \in [0, 2\pi)$ (or any chosen branch of the multivalued $\arg$ function). For $z = 0$, the magnitude is 0 and the phase is conventionally taken as $0$ (or left undefined; the convention does not affect the structural content of the decomposition).

This is universal mathematical structure for $\mathbb{C}$, not an ED-specific commitment. Any complex-valued field admits this decomposition pointwise.

#### 4.2.2 Application to the participation measure

For $P_K(x, t) \in \mathbb{C}$ at each slot, define the slot-level magnitude and phase:

$$r_K(x, t) := |P_K(x, t)|, \qquad \theta_K(x, t) := \arg P_K(x, t)$$

with the convention $\theta_K = 0$ on the zero set of $P_K$. The pair $(r_K, \theta_K)$ supplies the polar decomposition of $P_K$ at every slot:

$$P_K(x, t) = r_K(x, t) \cdot e^{i \theta_K(x, t)}.$$

#### 4.2.3 Uniqueness up to global $U(1)$ gauge

The polar decomposition is unique once a branch of $\arg$ is chosen. A different branch shifts $\theta_K$ by a constant; equivalently, a global phase rotation $\theta_K \to \theta_K + \alpha$ is admissible without changing any structural content. This is the standard $U(1)$ gauge freedom inherent in any complex-valued field representation, identical to the gauge freedom in standard quantum mechanics's wavefunction.

This global $U(1)$ ambiguity is not an ED-internal structural commitment — it is the same gauge freedom that appears in every complex-valued representation in physics. It does not constitute a new structural commitment of F2 beyond what F1 already established.

#### 4.2.4 No new structural commitment

F2's content is exhausted by the polar-decomposition theorem's mathematical universality plus F1's commitment to $\mathbb{C}$-valued range. No primitive is invoked beyond what F1 invokes; no mathematical machinery is invoked beyond the polar-decomposition theorem; no downstream item is invoked. F2 establishes only *the existence and form of the decomposition* — that any complex-valued $P_K$ can be written as magnitude times phase. The specific functional forms of $r_K$ and $\theta_K$ are determined by F3 (which fixes $r_K = \sqrt{b_K}$) and F4 (which fixes $\theta_K = \pi_K$).

### 4.3 F3 — Magnitude Exponent $|P|^2 = b$

#### 4.3.1 The slot-level functional

Define $Q : \mathbb{C} \to \mathbb{R}_{\geq 0}$ as the function determining the slot-level bandwidth from the slot-level participation-measure value:

$$b_K(x, t) = Q(P_K(x, t)).$$

F3's content is to determine $Q$ uniquely (up to overall positive scaling) from primitive-level inputs.

#### 4.3.2 Three structural constraints on $Q$

**(C-I) Non-negativity.** $Q(z) \geq 0$ for every $z \in \mathbb{C}$, with $Q(0) = 0$. Inherited from Primitive 04 (bandwidth is non-negative) plus the natural identification that zero participation measure corresponds to zero bandwidth.

**(C-II) $U(1)$-invariance.** $Q(e^{i \alpha} z) = Q(z)$ for every $z \in \mathbb{C}$ and every $\alpha \in \mathbb{R}$. Inherited from Primitive 09: bandwidth is invariant under global polarity rotation $\pi \to \pi + \alpha$, which corresponds (per F4 below) to $P \to e^{i \alpha} P$. Bandwidth must not change under this rotation, since the rotation is unobservable at the level of bandwidth content.

**(C-III) Additivity over disjoint channel-subsets.** For two disjoint channel-subsets $S_1, S_2 \subseteq \mathcal{K}_\tau(u)$, the bandwidth assigned to their union is $b(S_1 \cup S_2) = b(S_1) + b(S_2)$. This is a *kinematic* property of Primitive 04 at the participation-graph level — the bandwidth additivity of edge-weights over disjoint-edge unions, lifted to channel-subsets via the channel-subgraph structure. The additivity is genuinely primitive-level and does not depend on any participation-measure construction or any downstream item.

#### 4.3.3 Reduction to a function of $|z|^2$

By (C-II), $Q$ is constant on $U(1)$ orbits in $\mathbb{C}$. The orbit space is $\mathbb{C}/U(1) \simeq \mathbb{R}_{\geq 0}$, parameterised by the squared magnitude $|z|^2$. (Equivalently: $|z|^2$ is the unique-up-to-monotone-reparametrisation $U(1)$-invariant non-trivial function on $\mathbb{C}$.) Therefore:

$$Q(z) = f(|z|^2)$$

for some function $f : \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$ with $f(0) = 0$ and $f \geq 0$ everywhere.

The remaining question: what fixes $f$?

#### 4.3.4 Bandwidth additivity forces $f$ to be linear

Consider two participation-measure values $P^{(1)}, P^{(2)} \in \mathbb{C}$ representing channel-subsets $S_1, S_2$ that are *bandwidth-disjoint* — i.e., their bandwidth contributions are independent, with no coherent inter-channel mixing. (At the participation-graph level, this corresponds to disjoint edge-supports.) The combined channel $K = K_1 \sqcup K_2$ has total bandwidth $b(K) = b(K_1) + b(K_2)$ by (C-III).

Combining the two values via the natural orthogonal-sum lift on the participation-measure space (which uses only the vector-space structure on $\mathbb{C}$, not the inner product on the participation-measure space — this is important to avoid a circular dependency on U2), the combined value has squared magnitude $|P^{(1)}|^2 + |P^{(2)}|^2$ (the Pythagorean structure of orthogonal sums in 2-dimensional complex spaces). The bandwidth-additivity constraint becomes:

$$f(|P^{(1)}|^2 + |P^{(2)}|^2) = f(|P^{(1)}|^2) + f(|P^{(2)}|^2).$$

Setting $a := |P^{(1)}|^2$ and $b := |P^{(2)}|^2$, this is the Cauchy functional equation:

$$f(a + b) = f(a) + f(b) \qquad \forall\, a, b \geq 0.$$

#### 4.3.5 Solution of the Cauchy equation

Under the non-negativity constraint $f \geq 0$ (from (C-I)), the Cauchy equation has unique solution

$$f(a) = c \cdot a$$

for some constant $c \geq 0$. (The pathological discontinuous solutions of the Cauchy equation, constructed using a Hamel basis of $\mathbb{R}$ as a $\mathbb{Q}$-vector space, do not respect $f \geq 0$ globally; they take both positive and negative values in any neighbourhood of any point. They are physically irrelevant to the present derivation.)

Substituting back into $Q$:

$$Q(z) = c \cdot |z|^2.$$

The constant $c$ is an overall normalisation. Setting $c = 1$ by convention recovers

$$b_K = Q(P_K) = |P_K|^2.$$

The exponent 2 is uniquely forced.

#### 4.3.6 Dismissal of $\alpha \neq 2$

Suppose alternatively that $Q(z) = c \cdot |z|^\alpha$ for some $\alpha > 0$. Substituting into the bandwidth-additivity constraint with $|P^\mathrm{combined}|^2 = |P^{(1)}|^2 + |P^{(2)}|^2$:

$$c \cdot (|P^{(1)}|^2 + |P^{(2)}|^2)^{\alpha/2} = c \cdot |P^{(1)}|^\alpha + c \cdot |P^{(2)}|^\alpha.$$

Setting $a := |P^{(1)}|^2$, $b := |P^{(2)}|^2$, the constraint becomes the power-additivity equation:

$$(a + b)^{\alpha/2} = a^{\alpha/2} + b^{\alpha/2}.$$

Setting $\beta := \alpha/2$, this reads $(a+b)^\beta = a^\beta + b^\beta$ for all non-negative $a, b$. The function $x \mapsto x^\beta$ is super-additive ($\beta > 1$), sub-additive ($0 < \beta < 1$), or linear ($\beta = 1$). Equality holds for all $a, b \geq 0$ if and only if $\beta = 1$, i.e., $\alpha = 2$.

**Alternative exponents $\alpha \neq 2$ violate bandwidth additivity over disjoint channels and are dismissed.** F3 is established.

#### 4.3.7 Independence from downstream items

The argument uses Primitive 04's kinematic bandwidth additivity (a property of the participation graph, independent of any participation-measure construction), Primitive 09's $U(1)$-invariance of bandwidth, F1's complex-vector-space structure (derived above), and the standard mathematical fact that the only continuous non-negative additive functions on $\mathbb{R}_{\geq 0}$ are linear. No U2 inner product, no Theorem 10 Born structure, no U5 partition, no Schrödinger, no Bell, no Heisenberg is invoked.

The orthogonal-sum lift in Section 4.3.4 uses only the vector-space structure on $\mathbb{C}$, not the U2 inner product. The Pythagorean magnitude relation $|z_1 + z_2|^2 = |z_1|^2 + |z_2|^2$ for orthogonal $z_1, z_2 \in \mathbb{C}$ holds at the level of the magnitude function alone, derivable from F1's commitment to $\mathbb{C}$-valued range without any further structural input.

### 4.4 F4 — Phase = Polarity

#### 4.4.1 Primitive enumeration

The phase slot of F2's polar decomposition $P_K = r_K \cdot e^{i \theta_K}$ requires a $U(1)$-valued angular variable $\theta_K(x, t)$. We audit the entire ED primitive stack for primitives supplying such a variable.

| Primitive | Supplies | Angular character |
|---|---|---|
| **Primitive 01 (Micro-Event)** | Discrete events; vertex set $V$ | None (set-valued, not angular) |
| **Primitive 02 (Chain)** | Chain identity-rule | None (rule-typed, not angular) |
| **Primitive 03 (Participation)** | Edge structure; relational adjacency | None (relational-typed, not angular) |
| **Primitive 04 (Bandwidth)** | Edge weighting $w : E \to \mathbb{R}_{\geq 0}$ | None ($\mathbb{R}_{\geq 0}$-valued, not angular) |
| **Primitive 05 (Event Density)** | Density field $\rho : V \to \mathbb{R}_{\geq 0}$ | None (real scalar, not angular) |
| **Primitive 06 (ED Gradient)** | $\nabla \rho$ on the participation graph | Vector-valued in tangent bundle; not $U(1)$-valued primitive variable |
| **Primitive 07 (Channel)** | Channel sub-structure labels | None (set/sub-graph-typed, not angular) |
| **Primitive 08 (Multiplicity)** | Effective channel count $M_\mathrm{eff}$ | None (real-positive scalar, not angular) |
| **Primitive 09 (Tension Polarity)** | Polarity phase $\pi(K, x, t) \in U(1)$ | **$U(1)$-valued — the unique angular primitive** |
| **Primitive 10 (Individuation)** | Threshold for distinguishing chains | None (threshold-valued, not angular) |
| **Primitive 11 (Commitment)** | Discrete commitment events | None (event-valued, not angular) |
| **Primitive 12 (Thickening)** | Thickening density $\tau : M \to \mathbb{R}_{\geq 0}$ | None (real scalar density, not angular) |
| **Primitive 13 (Relational Timing)** | Proper-time intervals | None (real-valued temporal, not angular) |

**Primitive 09 is the unique primitive-level source of a $U(1)$-valued angular variable in the ED stack.** No other primitive supplies one.

#### 4.4.2 Functional alternatives

A more refined challenge: could $\theta_K = f(\pi_K)$ for some non-trivial function $f$, rather than the direct identification $\theta_K = \pi_K$?

For $f$ to map $U(1)$-valued input to $U(1)$-valued output continuously, $f$ must be a continuous group homomorphism $U(1) \to U(1)$. The continuous endomorphisms of $U(1)$ are integer-character maps $f_n(\theta) = n \theta \pmod{2\pi}$ for some integer $n \in \mathbb{Z}$.

The cases:

- **$n = 0$.** Trivial homomorphism, $\theta_K \equiv 0$. Reduces $P_K$ to a real-valued field, contradicting F1's $\mathbb{C}$-valued commitment with non-trivial phase content. Dismissed.
- **$n = 1$.** Identity, $\theta_K = \pi_K$. The natural choice; corresponds to the U1 construction's phase factor.
- **$|n| > 1$.** Non-trivial winding; $\theta_K$ winds $n$ times faster than $\pi_K$. For such an $n$ to be primitive-level supported, there would have to be a primitive supplying an integer winding number distinct from polarity itself. The primitive enumeration of Section 4.4.1 finds no such primitive.
- **$n = -1$.** Complex conjugation, $\theta_K = -\pi_K$. Corresponds to the standard $z \leftrightarrow z^*$ ambiguity, which is a global gauge convention rather than a structurally distinct alternative. The two conventions describe the same physical content; we adopt $n = +1$.

Thus the identification $\theta_K = \pi_K$ is the unique structurally-supported choice, up to the global $U(1)$ gauge convention already accounted for in F2.

#### 4.4.3 Phase-shift alternatives

Another refinement: could $\theta_K = \pi_K + g(b_K, \rho, \ldots)$ for some real-valued function $g$ of other primitive quantities (bandwidth, density, gradient magnitudes, etc.)?

For $\theta_K$ to remain a $U(1)$-valued field, $g$ must take real values modulo $2\pi$. A non-trivial $g$ would shift the phase by a primitive-level scalar quantity.

Two cases:

- **Constant $g$.** A constant phase shift $\theta_K = \pi_K + \alpha$ is the standard global $U(1)$ gauge freedom of F2's polar decomposition (Section 4.2.3). It is not a structurally distinct alternative; conventionally $\alpha = 0$.
- **Non-constant $g(b_K, \rho, \ldots)$.** For $g$ to depend on real-valued primitive quantities like bandwidth, $g$ would have to be a primitive-level supported map $\mathbb{R} \to \mathbb{R} \pmod{2\pi}$. Such a map requires its own structural content — a primitive-level identification of "the right phase shift as a function of bandwidth," equipped with a dimensional conversion factor. No primitive supplies this. Real-valued primitives ($b$, $\rho$, $\tau$, etc.) are dimensionful magnitudes; their identification with phase shifts would require structural input not present in the stack.

No non-trivial $g$ is structurally supported. The phase is exactly $\pi_K$ up to the global $U(1)$ convention.

#### 4.4.4 F4 verdict

**The phase $\theta_K$ in U1's polar decomposition is exactly Primitive 09's polarity phase $\pi(K, x, t)$**, up to the standard global $U(1)$ gauge convention. F4 is established.

The argument uses Primitive 09 (the unique source) plus standard $U(1)$ representation theory plus a primitive-level enumeration over the entire ED stack. No downstream item is invoked.

---

## 5. Falsifier Analysis

We documented five potential failure modes for the U1 construction in the arc's outline phase. We now confirm that each is dispatched by the derivation.

### 5.1 Falsifier table

| Falsifier | Sub-feature | Description | Dispatch |
|---|---|---|---|
| **Fal-1** Real-valued | F1 | $P_K$ takes values in $\mathbb{R}$, with phase content separately encoded | Section 4.1.2: no faithful $U(1)$ action on $\mathbb{R}$ exists; alternative pair-storage is equivalent to $\mathbb{C}$ via polar form |
| **Fal-2** Quaternionic | F1 | $P_K$ takes values in $\mathbb{H}$, requiring $\mathrm{SU}(2)$ phase content | Section 4.1.3: $\mathbb{H}$'s $\mathrm{SU}(2)$ structure is incompatible with Primitive 09's $U(1)$-only commitment (underdetermined embedding or unsupported surplus structure) |
| **Fal-3** Different exponent | F3 | $|P|^\alpha = b$ for $\alpha \neq 2$ | Section 4.3.6: power-additivity constraint $(a+b)^{\alpha/2} = a^{\alpha/2} + b^{\alpha/2}$ holds only for $\alpha = 2$ |
| **Fal-4** Phase ≠ polarity | F4 | Phase factor uses some angular variable distinct from polarity | Section 4.4: primitive enumeration confirms Primitive 09 is the unique $U(1)$-valued angular variable; functional alternatives require unsupported primitive content |
| **Fal-5** Non-multiplicative fusion | F1 + F2 jointly | Bandwidth and polarity combined by an operation other than multiplication | Sections 4.1 + 4.2: once $\mathbb{C}$-valued range and polar decomposition are in place, the multiplicative form $r \cdot e^{i \theta}$ is the polar decomposition by definition; no alternative fusion produces the structurally-claimed magnitude/phase decomposition |

All five falsifiers are dispatched. No physical-distinction alternative survives the derivation.

### 5.2 Methodological discipline

Each falsifier dispatch uses only primitive-level inputs and standard mathematical infrastructure. No downstream item is invoked. The derivation is acyclic with respect to U2, Theorem 10, U5, U3, U4, Schrödinger, Bell, Heisenberg.

---

## 6. Downstream Cascade

### 6.1 Six theorems promoted simultaneously

The U1 derivation was undertaken because U1 is the most upstream commitment in the QM-emergence Phase-1 program. Every downstream theorem uses $P_K$ as a constructed object and inherits a structural conditionality on U1. With U1 now FORCED, these conditionalities are removed across all downstream theorems simultaneously.

| Theorem | Pre-U1 conditionality | Post-U1 conditionality |
|---|---|---|
| **U2-Discrete** [2] | FORCED conditional on U1 | **FORCED unconditional** |
| **U2-Continuum** [3] | FORCED-up-to-gauge conditional on U1 | **FORCED unconditional** (up to description-level conformal gauge) |
| **Theorem 10** (Born rule) [4] | FORCED conditional on U1 (via U2) | **FORCED unconditional** in discrete + continuum regimes |
| **U5** (adjacency partition) [5] | FORCED conditional on U1 (via U2 + Theorem 10) | **FORCED unconditional** in discrete + continuum regimes |
| **Bell–Tsirelson bound** [6, Step 4] | FORCED conditional on U1 (via U2) | **FORCED unconditional** |
| **Heisenberg uncertainty** [6, Step 5] | FORCED conditional on U1 (via U2 + U5) | **FORCED unconditional** in discrete + continuum regimes (gauge-invariant) |

Six theorems are promoted simultaneously by a single arc — the largest single-arc downstream cascade in the structural-foundations cycle of the QM-emergence Phase-1 program. The Born rule, Bell's correlation bound at $|S| \leq 2\sqrt{2}$, and Heisenberg's uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ are all now FORCED-unconditional structural consequences of the ED primitive stack.

### 6.2 Dependency diagram

The structural-foundations chain following the U1 arc closure:

```
                     [Primitives 03, 04, 06, 07, 09, ...]
                                    |
                                    v
                          U1 (this paper) — FORCED
                                    |
                  +-----------------+-----------------+
                  |                                   |
                  v                                   v
          U2-Discrete [2]                 U2-Continuum [3]
            FORCED                      FORCED (up to gauge)
                  |                                   |
                  +-----------------+-----------------+
                                    |
                  +-----------------+-----------------+
                  |                 |                 |
                  v                 v                 v
        Theorem 10 [4]          U5 [5]      Bell–Tsirelson
        Born rule        Adjacency partition       (Step 4)
            FORCED               FORCED               FORCED
                                    |
                                    v
                         Heisenberg uncertainty
                              (Step 5)
                              FORCED
                              
                          [U3, U4 — open]
                                    |
                                    v
                       Schrödinger evolution
                          (Step 2 — open)
```

Every arrow represents a structural-derivation chain: each downstream item derives from the items above it (and additional primitive-level inputs as appropriate). The chain is acyclic — no arrow goes backwards. With U1 now FORCED, every solid arrow's source is itself FORCED, so every solid arrow's destination is FORCED-unconditional.

The only remaining open structural items are U3 and U4, both specific to Schrödinger evolution. They lie below U1 in the derivation chain (they use $P_K$ as input) but operate on the dynamical content of the participation measure (its evolution equation, its momentum-basis identification) rather than on the kinematic content (its construction, its inner product, its band partition). Their derivation is the natural next foundational target.

### 6.3 No retroactive circularity

A potential concern: does promoting the most-upstream commitment after downstream derivations have completed introduce hidden circles into those prior arcs?

It does not. Each prior arc operated within its own structural-input scope and explicitly identified its conditionality on U1. The U2 arc derived U2 from primitives + U1-as-CANDIDATE, treating U1 as an inherited input but not assuming it was forced. Theorem 10 used U2 + U1; U5 used U2 + Theorem 10 + U1; Bell and Heisenberg used U2 + U1 (and U5 for Heisenberg). With U1 now derived from primitives + Frobenius + $U(1)$ representation theory + quadratic-form classification — none of which appears as input to any downstream arc — the conditionality is removed cleanly. The chain is acyclic; the structural-foundations program is self-consistent.

### 6.4 Updated upstream-CANDIDATE inventory

The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces:

| Pre-U1 | Post-U1 |
|---|---|
| {U1, U3, U4} + continuum gauge | **{U3, U4} + continuum gauge** |

Two upstream commitments remain. Both concern Schrödinger evolution:

- **U3.** The participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H}_K P_K + \sum_{K'} V_{KK'} P_{K'}$. Required for the dynamical content of the framework.
- **U4.** The thin-limit momentum-basis identification $H_k = \hbar^2 k^2 / (2m)$. Required for the specific kinetic-energy form of Schrödinger.

Promoting both U3 and U4 would close the QM-emergence Phase-1 structural-foundations program completely except for the description-level continuum gauge.

---

## 7. Discussion

### 7.1 Why complex numbers

Standard quantum mechanics assumes complex-valued wavefunctions on the first page of any textbook. The structural reason is rarely interrogated. In the present derivation, the choice is forced by exact matching between primitive content and carrier content.

Primitive 09 supplies $U(1)$-valued polarity. The polarity phase has the symmetry of a circle — one-dimensional rotation. To carry this content faithfully, the algebraic carrier must support faithful $U(1)$ action with no surplus structure. Among Frobenius-classified division algebras, $\mathbb{R}$ admits no faithful $U(1)$ action (its automorphism group is too small) and $\mathbb{H}$ carries surplus $\mathrm{SU}(2)$ structure incompatible with $U(1)$-only polarity (its automorphism group is too large). $\mathbb{C}$ is the unique algebra whose maximal angular structure is exactly $U(1)$ — neither too little nor too much.

This is a structural-commitment-counting argument: the carrier algebra must have *exactly* the structure the primitives supply, not less and not more. Less leaves primitive content uncarried (Fal-1). More commits the framework to structural content beyond what primitives supply (Fal-2). $\mathbb{C}$ is the unique choice.

### 7.2 Why squared magnitude

The Born rule $\mathrm{Prob}(\mathrm{outcome}) = |\psi|^2$ has been a postulate of standard quantum mechanics for a century. Its squared exponent has been the subject of substantial foundations-of-QM literature, including Gleason's theorem on probability measures over Hilbert-space projectors and Busch's POVM extension. Each of these derivations operates *given* a Hilbert-space arena with a complex-valued wavefunction; they do not derive the squared magnitude *de novo* from a deeper ontology.

The present derivation operates one level deeper. The squared-magnitude relation $b = |P|^2$ is forced by three primitive-level kinematic facts:

1. Bandwidth is a non-negative real (Primitive 04).
2. Bandwidth is invariant under global phase rotation (Primitive 09 $U(1)$-invariance, since global phase has no observable consequence at the bandwidth level).
3. Bandwidth is additive over disjoint channel-subsets (Primitive 04 kinematic additivity at the participation-graph level).

The first two facts together force the slot-level functional $Q$ to be a function of $|z|^2$ alone. The third fact forces this function to be linear via the Cauchy functional equation: $Q(z) = c \cdot |z|^2$. Setting $c = 1$ recovers $b = |P|^2$.

Crucially, the argument operates *upstream* of Born, Schrödinger, Madelung, and Heisenberg — the four downstream theorems where the same exponent 2 appears. The "Exponent-2 Thread" that runs through these theorems has its origin here: in the Cauchy functional equation applied to $U(1)$-invariant non-negative additive functions on $\mathbb{C}$. Each downstream theorem inherits the exponent; none of them generates it.

This is the most fundamental version of the "why squared?" question's answer that we are aware of. Born's exponent is squared because the participation-measure construction has $|P|^2 = b$, and the participation-measure construction has $|P|^2 = b$ because the only $U(1)$-invariant non-negative additive form on $\mathbb{C}$ is the squared modulus.

### 7.3 Why $U(1)$

A natural question: why does Primitive 09 commit specifically to $U(1)$-valued polarity, and not to a wider symmetry group like $\mathrm{SU}(2)$ or $\mathrm{SO}(3)$?

This is a question about the primitive itself, not about U1's derivation. The U1 arc takes Primitive 09's $U(1)$-only commitment as given and derives the carrier algebra accordingly. If a future amendment to Primitive 09 widens the polarity symmetry, the F1 dismissal of $\mathbb{H}$ would need re-examination — the carrier might then be $\mathbb{H}$, with the participation measure becoming quaternionic and the inner-product structure becoming the standard quaternionic Hilbert-space structure.

The present derivation establishes the conditional structure: *given* Primitive 09's $U(1)$-only polarity, the carrier algebra is forced to be $\mathbb{C}$. The primitive's commitment is itself a structural choice of the framework. We flag this sensitivity explicitly in Section 3.

### 7.4 Structural significance: layers 1 and 2 complete

The QM-emergence Phase-1 program decomposes into three structural layers:

1. **The participation-measure layer.** The carrier $P_K$ and its construction. Includes U1.
2. **The Hilbert-space layer.** The inner product, the Born rule, the orthogonal-decomposition structure, the uncertainty bound. Includes U2, Theorem 10, U5.
3. **The dynamical layer.** The participation-measure evolution equation and its specific form. Includes U3, U4.

With U1 now FORCED, **layers 1 and 2 are structurally complete at theorem grade.** The participation measure is forced; the inner product is forced (in both regimes, with explicit gauge structure for the continuum); the Born rule is forced; the adjacency partition is forced; Bell's bound and Heisenberg's bound are forced. The Hilbert-space arena of standard non-relativistic quantum mechanics is now structurally derivable from the ED primitive ontology rather than postulated alongside the wavefunction.

Layer 3 — Schrödinger evolution and its specific form — remains open. Its derivation requires U3 and U4. Promoting both would complete the entire QM-emergence Phase-1 structural-foundations program except for the description-level continuum gauge.

### 7.5 Sensitivity flags

Two specific sensitivities of the U1 verdict to the current primitive stack warrant flagging:

- **Primitive 09 widening.** F1's dismissal of $\mathbb{H}$ depends critically on Primitive 09's commitment to $U(1)$-only polarity. A future amendment widening Primitive 09's polarity to $\mathrm{SU}(2)$ or higher (e.g., for SM-gauge-group emergence work) would require re-deriving F1 under the amended primitive, with $\mathbb{H}$ becoming a viable carrier candidate.

- **Primitive 04 weakening.** F3's exponent-2 result depends critically on Primitive 04's kinematic bandwidth additivity over disjoint channel-subsets. A future amendment weakening or removing this additivity (e.g., introducing inherent inter-channel interference at the kinematic level) would invalidate the Cauchy-equation step of F3, allowing alternative exponents.

Neither amendment is currently on the table. The verdict stands under the current primitive stack.

### 7.6 Distinction from prior derivation programs

The U1 derivation differs from prior foundations-of-QM derivation programs in one structurally significant respect: it operates *de novo* from a primitive ontology rather than reformulating standard quantum mechanics. Most prior work — Gleason's theorem and its derivatives, the decision-theoretic Many-Worlds derivations of Born by Deutsch and Wallace, Hardy's five-axiom reconstruction, the operational reconstructions of Chiribella–D'Ariano–Perinotti, the Zurek envariance program — operates *given* a Hilbert-space arena with a complex-valued wavefunction and derives specific properties (probability assignments, dynamical evolution rules) from additional axioms. The Hilbert-space arena itself is taken as given.

The present derivation operates one level deeper. It does not assume a Hilbert space; it constructs the carrier algebra from primitive-level content. The complex-valued range, the polar decomposition, the squared-magnitude relation, and the phase-equals-polarity identification are each derived rather than assumed. Combined with the prior arcs of the structural-foundations cycle (U2-Discrete and U2-Continuum supplying the inner product on the participation-measure space; Theorem 10 supplying the Born rule on the resulting Hilbert space; U5 supplying the adjacency partition supporting Heisenberg), the entire Hilbert-space arena of standard non-relativistic quantum mechanics is structurally derived.

This is the substantive achievement of the structural-foundations cycle. The Hilbert-space arena is no longer a postulate floating above the framework; it is a theorem-grade structural consequence of the ED primitive ontology.

---

## 8. Conclusion

We have established the U1 theorem: the participation-measure construction $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ is a forced structural consequence of the ED primitive stack. The four sub-features of the construction — complex-valued range, polar decomposition, squared-magnitude relation, phase-equals-polarity identification — each derive from primitive-level kinematic content (Primitives 03, 04, 07, 09) plus standard mathematical infrastructure (Frobenius's classification, the polar-decomposition theorem on $\mathbb{C}$, $U(1)$ representation theory, quadratic-form classification).

The derivation operates with the leanest structural inputs of any arc in the QM-emergence program. As the most upstream commitment, U1 is upstream of every downstream item; none of those items can be used as inputs without circularity. The methodological constraint is acute, but the derivation closes cleanly: F1 (complex-valued range) is forced by Frobenius classification combined with Primitive 09's $U(1)$-only commitment; F2 (polar decomposition) follows from the standard mathematical theorem on $\mathbb{C}$; F3 (magnitude exponent) is forced by Primitive 04 kinematic bandwidth additivity combined with Primitive 09 $U(1)$-invariance and the Cauchy functional equation; F4 (phase identification) is forced by primitive-level enumeration confirming Primitive 09 as the unique source of a $U(1)$-valued angular variable.

All five falsifiers (Fal-1 real-valued, Fal-2 quaternionic, Fal-3 different exponent, Fal-4 phase ≠ polarity, Fal-5 non-multiplicative fusion) are dispatched.

The downstream cascade is the largest single-arc consequence in the structural-foundations cycle. With U1 now FORCED, six downstream theorems promote simultaneously to FORCED-unconditional: U2-Discrete, U2-Continuum, Theorem 10 (Born), U5, Bell–Tsirelson, and Heisenberg uncertainty. The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces from {U1, U3, U4} + gauge to **{U3, U4} + gauge**, with the participation-measure layer and the Hilbert-space layer of the framework now structurally complete at theorem grade.

Three of the four foundational quantum-mechanical postulates — the Born rule, Bell's correlation bound at $|S| \leq 2\sqrt{2}$, and Heisenberg's uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ — are now FORCED-unconditional structural consequences of the ED primitive ontology. The fourth, Schrödinger evolution, remains conditional on U3 and U4, the natural next foundational targets.

The Hilbert-space arena of standard non-relativistic quantum mechanics — the wavefunction's complex-valued range, the inner product on its space, the Born-rule probability assignment, the Bell correlation bound, the Heisenberg uncertainty inequality — is now structurally derivable from the ED primitive ontology. The framework still rests on its primitives. Whether *those* are the correct foundational concepts remains the load-bearing question. But the postulates of quantum mechanics no longer have to be assumed independently. They emerge from the framework as structural consequences. The U1 result, presented here, establishes the foundational layer on which the rest of the structural-foundations cycle rests.

---

## Appendix: Memo-to-Theorem Mapping

The U1 arc consisted of four memos plus a closure-and-summary memo, integrated here into a single publication paper. The mapping between memos and theorem components:

| Memo | Structural result | Section of this paper |
|---|---|---|
| Memo 00 (arc outline) | Decomposition into four sub-features (F1–F4); falsifier inventory; identification of leanest-inputs methodology; comparison to prior arcs | Section 1 (introduction) |
| Memo 01 (decomposition + circularity audit) | Refined decomposition with primitive-level mapping; sub-feature classification; falsifier-to-sub-feature attachment; circularity audit identifying which arguments in the original Step-1 memo's nine constraints C1–C9 used downstream items and required replacement | Sections 2 (background), 5 (falsifier table) |
| Memo 02 (F2, F4 derivations) | F2 (polar decomposition) conditional on F1 via standard polar-decomposition theorem; F4 (phase = polarity) unconditional via primitive enumeration over Primitives 01–13 | Sections 4.2, 4.4 |
| Memo 03 (F1, F3, verdict) | F1 (complex-valued range) via Frobenius + Primitive 09 $U(1)$-only with explicit dismissals of $\mathbb{R}$ and $\mathbb{H}$; F3 (magnitude exponent $|P|^2 = b$) via Primitive 04 kinematic additivity + Primitive 09 $U(1)$-invariance + Cauchy functional equation; falsifier dispatch; arc verdict | Sections 4.1, 4.3, 5 |
| Memo 04 (closure-and-summary) | Canonical narrative; theorem statement; downstream cascade integration; sensitivity flags; structural-foundations completion of layers 1 and 2 | Sections 3, 6, 7, 8 |

The four sub-features F1–F4 of the U1 construction map directly to the four structural properties of the U1 theorem stated in Section 3:

| Sub-feature | Theorem property | Derivation section |
|---|---|---|
| F1 (complex-valued range) | Carrier algebra: $P_K \in \mathbb{C}$ | Section 4.1 |
| F2 (polar decomposition) | $P_K = r_K \cdot e^{i \theta_K}$ | Section 4.2 |
| F3 (magnitude exponent) | $r_K^2 = |P_K|^2 = b_K$ | Section 4.3 |
| F4 (phase = polarity) | $\theta_K = \pi(K, x, t)$ | Section 4.4 |

---

## References

[1] *Phase-1: QM Emergence Structural Completion.* `papers/QM_Emergence_Structural_Completion/`. Internal ED program reference establishing the Phase-1 five-step QM-emergence framework, with the participation-measure construction adopted as upstream commitment U1 and the nine constraints C1–C9 enumerated in Section 4.1.

[2] *The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion.* `papers/U2_Inner_Product/paper_u2_inner_product.{md,tex,pdf}`. Establishes the U2-Discrete and U2-Continuum theorems on the sesquilinear inner product on the participation-measure space.

[3] U2-Continuum theorem; see [2].

[4] *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* `papers/Born_Gleason/born_gleason_paper.{md,tex,pdf}`. Establishes Theorem 10 (Born rule via the Gleason–Busch path).

[5] U5 theorem on the adjacency-band Fourier-conjugate partition; arc closure at `arcs/U5/04_closure_and_summary.md`.

[6] Phase-1 QM-emergence framework Steps 4 (Bell–Tsirelson) and 5 (Heisenberg uncertainty); see [1].

[7] F. G. Frobenius, *Über lineare Substitutionen und bilineare Formen*, J. Reine Angew. Math. 84, 1–63 (1878). Frobenius theorem on real division algebras.

[8] A. L. Cauchy, *Cours d'Analyse de l'École Royale Polytechnique* (Imprimerie Royale, Paris, 1821). Cauchy functional equation (relevant for F3).

[9] E. C. G. Stueckelberg, "Quantum theory in real Hilbert space," *Helv. Phys. Acta* **33**, 727 (1960). Real-QM literature (relevant for Fal-1).

[10] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995). Quaternionic-QM literature (relevant for Fal-2).

[11] A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," *J. Math. Mech.* **6**, 885–893 (1957). Gleason's theorem; cited in [4] as the structural anchor of the Born-rule derivation.

[12] P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," *Phys. Rev. Lett.* **91**, 120403 (2003). Busch's POVM extension; cited in [4] as the closure of the $d = 2$ edge case.

---

*Manuscript prepared April 2026. Source materials: `arcs/U1/` four-memo arc and closure memo, integrated into a single publishable document. The U1 arc is the fifth and most upstream of the structural-foundations cycle (born_gleason → U2-Discrete → U2-Continuum → U5 → U1) that collectively establishes the Hilbert-space arena of standard non-relativistic quantum mechanics as structurally derivable from the Event-Density primitive ontology.*
