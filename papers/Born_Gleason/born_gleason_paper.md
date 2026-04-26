# The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles

**Allen Proxmire** and **Claude** (AI collaborator)

*April 2026*

---

## Abstract

We derive the Born rule of quantum mechanics as a forced structural consequence of the Event-Density (ED) primitive stack, via the Gleason–Busch route. Standard formulations of quantum mechanics treat the Born rule as an independent postulate, and Gleason's 1957 theorem reduces it (for Hilbert spaces of dimension $d \geq 3$) to a non-contextuality assumption that is itself postulated. We show that ED's primitive ontology — channels as primitive ontological sub-structures of the participation graph (Primitive 07) and bandwidth as an edge-weight on those sub-structures (Primitive 04) — *forces* the non-contextuality assumption rather than postulating it: the per-channel bandwidth $b_K(u)$ is a function of the channel and locus alone, partition-independent by construction. Combined with the σ-additivity and dimensional admissibility checks supplied directly by the primitive stack, and with Busch's 2003 POVM extension closing the $d = 2$ edge case (qubits, photon polarisation, spin-$\tfrac{1}{2}$), we establish **Theorem #10 (Born Rule from Primitives, via Gleason–Busch):** *for any chain at locus $u$ with effective dimension $d \geq 2$ in the thin-participation regime, there exists a unique density operator $\rho(u)$ such that the bandwidth-fraction map equals $\mathrm{Tr}(\rho(u)\, E)$ for every effect $E$.* The squared exponent of the Born rule is not arbitrary; it is a definitional consequence of $b_K = |P_K|^2$ in the participation-measure construction. The result supersedes the earlier Phase-1 Step-3 derivation by eliminating its phase-independence CANDIDATE residual and extending coverage from projective measurements to general POVMs. Theorem #10 takes its place as the tenth FORCED structural theorem in the ED inventory and is the program's first complete primitive-level reduction of an axiomatic-grade quantum-mechanical postulate to structural consequences of the participation-measure framework. The result is conditional on a single inherited upstream item (the sesquilinear inner product, a separate structural derivation addressed elsewhere) and on the ontological-primitive status of channels as supplied by Primitive 07.

---

## 1. Introduction

The Born rule occupies a distinctive position in the foundations of quantum mechanics. Together with the Schrödinger equation, it is the most directly empirically tested postulate of the theory: every quantum prediction in every laboratory experiment, from atomic spectroscopy to Bell tests to single-photon interference, is compared to experiment via the Born expression for outcome probabilities. Yet it is also among the most epistemically opaque. The squared-amplitude form $\mathrm{Prob}(K) = |\langle K | \psi \rangle|^2$ is taken as primitive in the Copenhagen formulation; alternative formulations (Many-Worlds via decision theory, QBism via Bayesian credences, Bohmian mechanics via guidance equations) each face their own well-known difficulties in deriving rather than assuming the rule. Gleason's 1957 theorem [1] partially closes the gap: any non-contextual probability measure on the closed subspaces of a Hilbert space of dimension $d \geq 3$ is necessarily of the form $\mathrm{Tr}(\rho P)$ for some density operator $\rho$. Busch's 2003 extension [2] closes the $d = 2$ edge case via positive operator-valued measures (POVMs).

Gleason's reduction is significant but incomplete. It moves the explanatory burden from "why squared amplitudes?" to "why non-contextuality?" but leaves the latter unexplained: standard quantum mechanics postulates non-contextuality operationally (measurement outcomes do not depend on what other measurements happen to be in the experimental context) without a deeper structural account.

The Event-Density (ED) program [3,4,5] supplies such a structural account. ED's primitive ontology specifies a participation graph $G = (V, E)$ on a $3+1$-dimensional event manifold, with vertices corresponding to micro-events (Primitive 01), edges corresponding to participation relations (Primitive 03), bandwidth as edge-weight (Primitive 04), and channels as primitive ontological sub-structures of the graph (Primitive 07). In this ontology, *channels are real graph-substructures, not basis-relative labels*: a channel $K$ is a particular subgraph $(V_K, E_K) \subset G$ satisfying rule-compatibility, bandwidth-coherence, and stability conditions; its identity is intrinsic to the graph and does not depend on any decomposition of the available-channel set imposed from outside. Bandwidth $b_K(u)$, similarly, is an edge-weight integral along $K$'s edges incident to vertex $u$ — a function of the (channel, locus) pair alone.

These two structural facts, taken together, *force* Gleason's non-contextuality assumption. The bandwidth-fraction probability rule $\mathrm{Prob}(K \mid u) = b_K(u) / \sum_{K'} b_{K'}(u)$ depends on the channel and locus alone, never on which other channels happen to be in the resolution against which $K$ is measured. The "context" — the surrounding decomposition — is an external organisational choice that cannot reach the bandwidth assignment. ED therefore *explains* what standard quantum mechanics postulates.

This paper establishes the full chain from ED primitives to the Born rule. We show that

1. ED's primitive structure forces the non-contextuality assumption Gleason requires;
2. The remaining Gleason admissibility conditions (σ-additivity, dimension $\geq 3$) are met automatically by the primitive stack;
3. Busch's POVM extension closes the $d = 2$ edge case via the same primitive arguments applied to weighted channel-subsets;
4. Combining (1)–(3), Gleason's and Busch's theorems apply directly to ED's bandwidth-fraction map, yielding the Born rule for both projective and POVM measurements at all $d \geq 2$.

The result is **Theorem #10 (Born Rule from Primitives, via Gleason–Busch)**, which takes its place as the tenth FORCED structural theorem in ED's ongoing program inventory. Earlier work [3, §3.3] derived the Born rule via a primitive-level decoherence argument conditional on an environmental phase-independence assumption; the present derivation supersedes that result by anchoring the proof in the channel-as-primitive ontology directly, eliminating the phase-independence residual, and extending coverage from projective measurements to general POVMs.

The paper is organised as follows. §2 introduces the relevant primitive stack and notation. §3 presents the structural non-contextuality derivation: the inventory of Gleason's load-bearing assumptions, the primitive-level argument forcing non-contextuality, and the σ-additivity and dimensional admissibility verifications. §4 extends the Gleason mapping to the Busch POVM framework, closing the $d = 2$ edge case. §5 states Theorem #10 with a proof sketch and discusses what it supersedes. §6 places the result within the broader ED program and identifies downstream implications. §7 presents a non-technical explainer suitable for a general scientific audience. The appendix contains a mapping between the present paper's sections and the underlying derivation memos.

---

## 2. The Primitive Stack and Notation

### 2.1 Primitive ontology

ED constructs physics as forced structural consequences of a small primitive stack on a $3+1$-dimensional event manifold. The primitives relevant to the Born derivation are:

- **Primitive 01 (Micro-Event):** discrete events on the event manifold; supplies the vertex set $V$ of the participation graph.
- **Primitive 03 (Participation):** the participation relation between micro-events; supplies the edge set $E$ of the participation graph $G = (V, E)$.
- **Primitive 04 (Bandwidth):** the graded measure of participation, supplied as an edge weighting $w : E \to \mathbb{R}_{\geq 0}$. Bandwidth admits a four-band orthogonal decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ corresponding to internal-rule, adjacency, environmental, and commitment-reserve bandwidth respectively, with conservation along the chain's persistence regime.
- **Primitive 07 (Channel):** stable, bandwidth-preserving sub-structures of the participation graph along which a chain's update rule can be repeatedly instantiated. Channels are *primitive ontological objects*: their identity is intrinsic to the graph, not basis-relative. Channels are countable in any region for any given rule-type.
- **Primitive 08 (Multiplicity):** the effective channel count $M_\mathrm{eff} = (\sum |P|^2)^2 / \sum |P|^4$ supplied by the participation-measure structure.
- **Primitive 09 (Tension Polarity):** the $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction; supplies the phase factor $e^{i\pi_K}$ in the participation measure.
- **Primitive 11 (Commitment):** the discrete event in which a chain selects one channel from those available, with selection probability weighted by channel bandwidth.

### 2.2 The participation measure

The participation measure, central to the Phase-1 QM-emergence framework [3], fuses Primitives 04 and 09 into a complex-valued field:

$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)} \qquad (1)
$$

with $b_K = |P_K|^2$ by construction. Aggregating over channels yields the wavefunction-candidate $\Psi(x, t) = \sum_K P_K(x, t)$, with coherent-sum interpretation in the thin-participation regime.

The space of participation measures $\mathcal{P}$ admits a sesquilinear inner product

$$
\langle P \mid Q \rangle = \sum_K \int dx\; P_K^*(x)\, Q_K(x) \qquad (2)
$$

establishing $\mathcal{P}$ as a complex Hilbert space upon completion. The structural status of (2) — its derivability from primitives — is the subject of a separate program arc, addressed in companion work [6, 7]. For the present paper we adopt (2) as an inherited upstream commitment, noting that all Born-derivation results of this paper inherit the same conditionality.

### 2.3 The available-channel set

For a chain $C$ of rule-type $\tau$ at vertex $u \in V$, let $\mathcal{K}_\tau(u)$ denote the set of channels available to $C$ at $u$ — the set of $\tau$-compatible sub-structures of the participation graph meeting at $u$ with rule-compatibility, bandwidth-coherence, and stability conditions per Primitive 07. The local channel-space at $u$ is the complex linear span $\mathcal{H}(u) = \mathrm{span}_\mathbb{C}\{|K\rangle : K \in \mathcal{K}_\tau(u)\}$, with $d(u) = \dim \mathcal{H}(u) = |\mathcal{K}_\tau(u)|$.

### 2.4 The bandwidth-fraction probability rule

ED's natural probability assignment for commitment outcomes at locus $u$ is the bandwidth-fraction:

$$
f(K \mid u) = \frac{b_K(u)}{\sum_{K' \in \mathcal{K}_\tau(u)} b_{K'}(u)} \qquad (3)
$$

The structural claim of this paper is that (3) is identical to the Born rule under the participation-measure identification $\Psi = \sum_K P_K$, and that this identification is forced by the primitive stack rather than postulated.

---

## 3. The Structural Non-Contextuality Derivation

This section establishes that the primitive stack supplies all of Gleason's load-bearing assumptions, with the substantive content concentrated in a single non-contextuality argument forced by Primitives 04 and 07.

### 3.1 Gleason's theorem and its assumptions

We recall Gleason's theorem in the form needed here.

**Theorem (Gleason, 1957).** Let $\mathcal{H}$ be a separable Hilbert space over $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$ with $\dim \mathcal{H} \geq 3$. Let $f : \mathcal{P}(\mathcal{H}) \to [0, 1]$ be a frame function on the lattice of closed subspaces (equivalently, orthogonal projectors) satisfying:

- **(A5) Non-negativity:** $f(P) \geq 0$ for every projector $P$.
- **(A6) Normalisation:** $f(I) = 1$.
- **(A7) σ-additivity:** for any countable family $\{P_i\}$ of mutually orthogonal projectors, $f(\sum P_i) = \sum f(P_i)$.

(The non-contextuality content is built into the typing of $f$: $f(P)$ depends on $P$ alone, not on which orthogonal resolution $P$ appears in.) Then there exists a unique density operator $\rho$ on $\mathcal{H}$ such that $f(P) = \mathrm{Tr}(\rho P)$ for every $P$.

A complete inventory of Gleason's load-bearing assumptions, including those that the standard three-axiom presentation packages implicitly, decomposes into eight items: (A1) Hilbert-space arena; (A2) dimension $\geq 3$; (A3) projector lattice structure; (A4) frame-function domain (the typing constraint encoding non-contextuality); (A5) non-negativity; (A6) normalisation; (A7) σ-additivity; (A8) frame-sum constancy (operational form of A4). We address each in turn.

### 3.2 Assumptions automatic or interpretive in ED

Five of the eight Gleason assumptions admit immediate or interpretive correspondents in the ED primitive stack:

- **(A1) Hilbert-space arena.** Supplied by the participation-measure framework via construction (1) and inner product (2) (the latter conditional on the inherited upstream commitment described in §2.2).
- **(A2) Dimension $\geq 3$.** Supplied generically by Primitive 07's channel countability combined with Primitive 08's effective-multiplicity structure: every standard quantum subsystem with non-trivial internal or spatial degrees of freedom yields $d \geq 3$ at any non-degenerate locus. The $d = 2$ edge case (qubits, polarisation, spin-$\tfrac{1}{2}$) is real, named, and addressed in §4 via Busch's POVM extension.
- **(A3) Projector lattice structure.** The lattice of closed subspaces of $\mathcal{H}(u)$ corresponds to the partition lattice of channel-subsets at locus $u$. Orthogonality of projectors maps to disjointness of channel-subsets (a structural disjointness at the participation-graph level, Primitive 03); joins, meets, and complements correspond to channel-subset unions, intersections, and complements within $\mathcal{K}_\tau(u)$. Orthomodularity follows from disjoint-union structure.
- **(A5) Non-negativity.** Automatic from Primitive 04: bandwidth is a non-negative real edge weight, so $|P_K|^2 = b_K \geq 0$ for every channel.
- **(A6) Normalisation.** Automatic by construction of the bandwidth-fraction probability rule (3): $\sum_K f(K \mid u) = 1$ trivially.

### 3.3 σ-additivity (A7)

For two disjoint channel-subsets $S_1, S_2 \subseteq \mathcal{K}_\tau(u)$, the bandwidth assigned to their union is

$$
b(S_1 \cup S_2 \mid u) = \sum_{K \in S_1 \cup S_2} b_K(u) = \sum_{K \in S_1} b_K(u) + \sum_{K \in S_2} b_K(u) = b(S_1 \mid u) + b(S_2 \mid u). \qquad (4)
$$

Equation (4) is set-theoretic disjoint-sum decomposition of a non-negative function over a finite (or finite-at-this-step) index set; it does not invoke any structural commitment beyond the non-negativity of bandwidth.

Countable extension requires (i) the union of countably many disjoint channel-subsets is itself a channel-subset (immediate from set-theoretic closure under arbitrary unions, with $\mathcal{K}_\tau(u)$ at-most-countable per Primitive 07), and (ii) the infinite sum converges (immediate from non-negativity of bandwidth and finiteness of total chain-bandwidth $b_\mathrm{total}(C) < \infty$ in the chain's persistence regime per the Primitive 04 four-band conservation). Both conditions hold, yielding

$$
b\!\left(\bigcup_{i=1}^\infty S_i \,\Big|\, u\right) = \sum_{i=1}^\infty b(S_i \mid u). \qquad (5)
$$

Dividing through by the total bandwidth at $u$ gives σ-additivity of the bandwidth-fraction map. **A7 is satisfied automatically.**

### 3.4 The non-contextuality argument

The substantive content of the derivation is concentrated in assumptions A4 and A8 — equivalent statements of non-contextuality — which are the same load-bearing question stated two ways. We give the argument forcing both.

**Premise (P-Channel)** (from Primitive 07). A channel $K$ is a sub-structure $(V_K, E_K) \subset G$ of the participation graph. Its identity is intrinsic to the graph and does not depend on any external decomposition of $\mathcal{K}_\tau(u)$ in which $K$ appears.

**Premise (P-Bandwidth)** (from Primitive 04). The bandwidth $b_K(u)$ is the integrated edge-weight along $K$'s edges incident to vertex $u$. It is a function of the (channel-subgraph $K$, vertex $u$) pair, computed from the graph's edge weights at $u$ along $K$'s edges. It does not depend on which other channels are present at $u$, except through the mechanical definition of "edges incident to $u$" — which itself involves only $K$'s edges, not other channels' edges.

**Premise (P-Commitment)** (from Primitive 11). Commitment uses $\{b_K(u) : K \in \mathcal{K}_\tau(u)\}$ as inputs. The available-channel set $\mathcal{K}_\tau(u)$ is intrinsic to $u$ per (P-Channel).

**Derivation.** By (P-Bandwidth), $b_K(u)$ is a function of $(K, u)$ alone. By (P-Channel), the identity of $K$ is intrinsic to the graph; $K$ is the same channel-substructure regardless of which decomposition $\mathcal{D}$ of $\mathcal{K}_\tau(u)$ it appears in. Decomposition $\mathcal{D}$ is an organisational choice imposed externally onto $\mathcal{K}_\tau(u)$; it does not alter the graph-substructure that $K$ is. Therefore for any two complete decompositions $\mathcal{D}, \mathcal{D}'$ of $\mathcal{K}_\tau(u)$ both containing $K$:

$$
b_K^{(\mathcal{D})}(u) = b_K(u) = b_K^{(\mathcal{D}')}(u). \qquad (6)
$$

The bandwidth assignment to $K$ is partition-independent. The commitment-selection probability $\mathrm{Prob}(K \mid u, \mathcal{D}) = b_K(u) / \sum_{K' \in \mathcal{D}} b_{K'}(u)$ has a numerator that is partition-independent by (6). The denominator — the sum $\sum_{K' \in \mathcal{D}} b_{K'}(u)$ — depends on $\mathcal{D}$ only through which channels are summed; for any complete decomposition spanning $\mathcal{K}_\tau(u)$, the sum equals the total bandwidth at $u$ along the chain's rule-type, a single intrinsic number. Both the typing form of non-contextuality (A4) and the operational form (A8, frame-sum constancy) follow.

**Loophole audit.** Three potential loopholes warrant explicit dismissal:

- *Sublinear bandwidth composition.* The composition rule $b_\mathrm{combined}^2 = b_1^2 + b_2^2 + 2 c_{12} b_1 b_2$ applies when channels merge into an effective coarse-grained channel; it is a constructor for $b_{K_1 \cup K_2}$ from its constituents, not a redefinition of $b_{K_1}$ alone. For orthogonal channels under environmental phase-randomisation, the cross-coherence $c_{12} = 0$ and clean σ-additivity is recovered. The composition rule does not introduce partition-dependence.
- *Context-dependent available-channel set.* An external apparatus brings its own channels and bandwidth into the locus, modifying the local edge-weights and selecting which of the system's channels are amplified into commitment. It does not retroactively reorganise the system's existing channel structure into a different basis, nor does it alter the system's per-channel bandwidth $b_K(u)$ for any channel $K$.
- *Channel-to-ray correspondence.* If ED's channels are coarse-grainings of finer structures (or one-to-one with rays), partition-independence at the ED level transfers cleanly to the QM level via summation over coarse-graining classes; no failure mode exists in the relevant correspondence.

**Conclusion.** Non-contextuality of the bandwidth-fraction probability rule is FORCED by the joint action of Primitives 04 and 07. Primitive 11 supplies the operational role; Primitives 04 and 07 supply the structural content. This is stronger than the standard QM treatment, in which non-contextuality is an operational postulate: ED *forces* it ontologically, because channels are graph-substructures and bandwidth is an edge-weight, both intrinsic to the graph and not to any external organisational choice.

### 3.5 Summary of admissibility

After §3.2–§3.4, all eight Gleason assumptions are satisfied by the ED primitive stack for $d \geq 3$. Five (A1, A3, A5, A6, A7) are automatic or interpretive; A2 is automatic generically with the $d = 2$ edge case deferred to §4; A4 and A8 are forced by the non-contextuality argument of §3.4. Gleason's theorem applies directly.

---

## 4. The Busch POVM Extension and the $d = 2$ Edge Case

Two-channel systems — single qubits, photon polarisation, spin-$\tfrac{1}{2}$ — are physically central but lie outside the scope of Gleason's original 1957 theorem, which fails for $d = 2$ because the projector lattice on $\mathbb{C}^2$ is structurally too sparse to constrain a frame function (the rank-1 projectors form a Bloch sphere with full rotational symmetry). Busch's 2003 extension closes this gap by replacing projectors with positive operator-valued measures.

### 4.1 Busch's theorem

**Theorem (Busch, 2003).** Let $\mathcal{H}$ be a separable complex Hilbert space of dimension $d \geq 2$. Let $\mathcal{E}(\mathcal{H}) = \{E : 0 \leq E \leq I\}$ be the set of effects (positive operators bounded above by the identity). Let $\mu : \mathcal{E}(\mathcal{H}) \to [0, 1]$ be a generalised probability measure satisfying:

- **(B1) Positivity / Boundedness:** $\mu(E) \in [0, 1]$ for every effect $E$.
- **(B2) Normalisation:** $\mu(I) = 1$.
- **(B3) σ-additivity:** for any countable family $\{E_i\}$ of effects with $\sum E_i \leq I$, $\mu(\sum E_i) = \sum \mu(E_i)$.
- **(B4) Domain typing:** $\mu(E)$ depends only on $E$ itself, not on which POVM resolution enumerates it.

Then there exists a unique density operator $\rho$ on $\mathcal{H}$ such that $\mu(E) = \mathrm{Tr}(\rho E)$ for every effect $E$.

The advantage over Gleason: the set of effects in $\mathcal{H} = \mathbb{C}^2$ is a continuous family rich enough to constrain $\mu$ to be linear in $E$ without requiring $d \geq 3$. The cost: ED must supply a generalised probability assignment on effects, not merely on projectors.

### 4.2 The ED–Busch dictionary

The required extension of ED's bandwidth-fraction map is mechanical. Define a **weighted channel-subset** at $u$ as a pair $(S, w)$ where $S \subseteq \mathcal{K}_\tau(u)$ is a channel-subset and $w : S \to [0, 1]$ is a weighting on $S$. The bandwidth assigned to $(S, w)$ is

$$
b(S, w \mid u) = \sum_{K \in S} w(K) \cdot b_K(u) \qquad (7)
$$

and the corresponding effect-value is

$$
f(S, w \mid u) = \frac{b(S, w \mid u)}{b(\mathcal{K}_\tau(u) \mid u)}. \qquad (8)
$$

When $w \equiv 1$ on $S$, (7) and (8) reduce to the unweighted forms used in §3. The dictionary mapping ED objects to Busch objects is:

| Busch object | ED correspondent |
|---|---|
| Hilbert space $\mathcal{H}$ | Local channel-space $\mathcal{H}(u)$ at locus $u$ |
| Effect $E$ with $0 \leq E \leq I$ | Weighted channel-subset $(S, w)$ |
| Effect-decomposition $\{E_i\}$, $\sum E_i \leq I$ | Family of weighted channel-subsets with per-channel total weight $\leq 1$ |
| POVM ($\sum E_i = I$) | Complete weighted channel-decomposition |
| Generalised probability $\mu(E)$ | Effect-value $f(S, w \mid u)$ |
| Density operator $\rho$ | Bandwidth-distribution profile at $u$ |

### 4.3 Verification of Busch's axioms

Each Busch axiom inherits directly from §2–§3:

- **B1 (positivity / boundedness):** automatic from non-negativity of bandwidth (Primitive 04) plus weights $w(K) \in [0, 1]$. The normaliser $b(\mathcal{K}_\tau(u) \mid u) > 0$ in any non-degenerate regime, so $f(S, w \mid u) \in [0, 1]$.
- **B2 (normalisation):** the identity effect corresponds to the complete weighted subset $(\mathcal{K}_\tau(u), 1)$, with $f(\mathcal{K}_\tau(u), 1 \mid u) = 1$ by construction.
- **B3 (σ-additivity):** for two weighted subsets $(S_1, w_1)$ and $(S_2, w_2)$ with pointwise weights summing to $\leq 1$, the effect-sum $(S_1 \cup S_2, w_1 + w_2)$ satisfies $b(S_1 \cup S_2, w_1 + w_2 \mid u) = b(S_1, w_1 \mid u) + b(S_2, w_2 \mid u)$ by linearity in weights, extending §3.3's σ-additivity to weighted families. Countable extension follows by the same boundedness-and-monotonicity argument used there.
- **B4 (effect-domain typing):** the effect-value $f(S, w \mid u)$ depends on $(S, w, u)$ alone; the per-channel bandwidth $b_K(u)$ entering (7) is partition-independent by §3.4, and the weights $w(K)$ are properties of the apparatus's coupling structure at $u$, not of any decomposition. Non-contextuality on effects inherits directly from non-contextuality on projectors.

### 4.4 The $d = 2$ closure

For a two-channel chain at locus $u$ with $\mathcal{K}_\tau(u) = \{K_+, K_-\}$ — for example, spin-up and spin-down along some quantisation axis, horizontal and vertical polarisation, or qubit basis states — the required rich effect structure on $\mathbb{C}^2$ is generated as follows. For each angle $\theta$ on the Bloch sphere, there is a complete decomposition $\mathcal{D}_\theta$ of $\mathcal{K}_\tau(u)$ into channels $K_+(\theta), K_-(\theta)$ that diagonalise the corresponding spin operator; these derived channels are coherent superpositions parameterised by $\theta$ in the complex linear span of the primitive channels. For each such $\mathcal{D}_\theta$, weighted subsets with $w(K_\pm(\theta)) \in [0, 1]$ generate a continuous family of effects diagonal in the $\theta$-basis. The union over all $\theta$ generates all effects diagonal in some basis — which, by the spectral theorem for positive operators on $\mathbb{C}^2$, is *all* effects in $\mathcal{E}(\mathbb{C}^2)$.

The non-contextuality result of §3.4 ensures that the effect-value $f(S, w \mid u)$ is the same number regardless of which $\mathcal{D}_\theta$ enumerates a given effect $(S, w)$. Busch's theorem then forces $f$ to be linear in the effect operator $E$, yielding a density operator $\rho(u)$ such that

$$
f(S, w \mid u) = \mathrm{Tr}(\rho(u) \cdot E) \qquad (9)
$$

for every effect $E \in \mathcal{E}(\mathbb{C}^2)$. For a Stern-Gerlach measurement at arbitrary spin direction $\mathbf{n}$, the corresponding effect $E_\mathbf{n}$ yields the standard Born expression $\mathrm{Tr}(\rho(u) E_\mathbf{n})$ from the per-channel bandwidth structure at $u$.

The same construction applies verbatim to photon polarisation and to general single-qubit systems. The $d = 2$ edge case is closed uniformly.

### 4.5 Joint admissibility status

After §3 and §4, the admissibility table is fully populated:

| Assumption | Status |
|---|---|
| A1 — Hilbert-space arena | Interpretive (conditional on inherited upstream item §2.2) |
| A2 / A2' — dimension $\geq 3$ / $d = 2$ closed via Busch | Automatic generically; $d = 2$ closed in §4 |
| A3 — Projector / effect lattice | Interpretive (channel-subset / weighted-subset lattice) |
| A4 / B4 — Domain typing (non-contextuality) | **FORCED** by §3.4 |
| A5 / B1 — Non-negativity / boundedness | Automatic (Primitive 04 domain) |
| A6 / B2 — Normalisation | Automatic (bandwidth-fraction construction) |
| A7 / B3 — σ-additivity | Automatic (Primitive 04 + 07 + bandwidth conservation) |
| A8 — Frame-sum constancy | **FORCED** by §3.4 |

Every Gleason and Busch admissibility condition is met or forced for all $d \geq 2$ in the thin-participation regime, conditional only on the inherited upstream item identified in §2.2.

---

## 5. Theorem #10 and Its Status

### 5.1 Statement

> **Theorem 10 (Born Rule from Primitives, via Gleason–Busch).** Let $G = (V, E)$ be a participation graph and let $C$ be a chain at vertex $u \in V$ in the thin-participation regime, where environmental phase-randomisation at commitment averages cross-channel coherences to zero. Assume the ED primitive stack (Primitives 03, 04, 07, 08, 11) and the participation-measure framework's sesquilinear inner product on the local channel-space at $u$. Let $\mathcal{K}_\tau(u)$ be the available-channel set at $u$ and let $\{b_K(u) : K \in \mathcal{K}_\tau(u)\}$ be the per-channel bandwidths supplied by Primitive 04. Let $\mathcal{H}(u)$ denote the complex linear span of $\{|K\rangle : K \in \mathcal{K}_\tau(u)\}$, with $d = \dim \mathcal{H}(u) \geq 2$.
>
> Then there exists a unique density operator $\rho(u)$ on $\mathcal{H}(u)$ such that for every effect $E \in \mathcal{E}(\mathcal{H}(u))$ — equivalently, for every weighted channel-subset $(S, w)$ at $u$ — the bandwidth-fraction map satisfies
>
> $$
> f(S, w \mid u) = \frac{b(S, w \mid u)}{b(\mathcal{K}_\tau(u) \mid u)} = \mathrm{Tr}(\rho(u) \cdot E). \qquad (10)
> $$
>
> In particular, for any projective measurement specified by an orthonormal channel-decomposition $\mathcal{D} = \{K_1, \ldots, K_d\}$ of $\mathcal{K}_\tau(u)$, the probability of commitment outcome $K_* \in \mathcal{D}$ is
>
> $$
> \mathrm{Prob}(K_* \mid u) = \frac{b_{K_*}(u)}{\sum_{K' \in \mathcal{D}} b_{K'}(u)} = |\langle K_* | \psi(u) \rangle|^2 \qquad (11)
> $$
>
> where $|\psi(u)\rangle \in \mathcal{H}(u)$ is the participation-measure pure-state representative when $\rho(u) = |\psi(u)\rangle\langle\psi(u)|$. Equation (10) is the Born rule for general (POVM) measurements; equation (11) is the Born rule for standard projective measurements.

### 5.2 Proof sketch

The proof has four links. The first three were established in §3–§4; the fourth is direct quotation of established results.

**Link 1 — Primitives 04 + 07 force non-contextuality.** §3.4's syllogism: channels are intrinsic to the participation graph, bandwidth is an edge-weight on those graph-substructures, hence per-channel bandwidth $b_K(u)$ is partition-independent. Loophole audit dismisses sublinear composition, context-dependent available-channel sets, and channel-to-ray correspondence concerns. Establishes Gleason / Busch typing assumptions A4, A8, B4.

**Link 2 — σ-additivity (A7) and dimension (A2).** §3.3 establishes σ-additivity automatically from non-negativity of bandwidth, at-most-countable channel sets at any locus (Primitive 07), finiteness of total chain-bandwidth (Primitive 04 four-band conservation), and Memo 02's partition-independence. §3.2 establishes $d \geq 3$ generically for any non-trivial quantum subsystem; the $d = 2$ edge case is named explicitly and addressed via Busch.

**Link 3 — Busch closure for $d = 2$.** §4 transfers ED's weighted-channel-subset effect structure into Busch's framework. All four Busch axioms B1–B4 inherit directly from the discrete-counting and non-contextuality results of §3 plus weight-linearity. The continuous Bloch-sphere effect structure that pure projectors cannot supply in $d = 2$ is generated by varying both the channel-decomposition $\mathcal{D}_\theta$ and the weights $w$; the union over all $\theta$ generates the full effect lattice on $\mathbb{C}^2$ by spectral decomposition.

**Link 4 — Application of Gleason / Busch.** With Links 1–3 supplying every structural admissibility condition, Gleason's theorem ($d \geq 3$, projector form) and Busch's theorem ($d \geq 2$, effect form) apply directly to the bandwidth-fraction map. Both yield a unique density operator $\rho(u)$ on $\mathcal{H}(u)$ such that $f(E) = \mathrm{Tr}(\rho(u) E)$ for every effect $E$. For projective measurements, restriction to rank-1 projectors $|K\rangle\langle K|$ recovers (11), the standard Born rule. $\square$

### 5.3 Scope conditions

The theorem is established subject to the following scope conditions:

1. **Thin-participation regime.** The argument applies where environmental phase-randomisation at commitment averages cross-channel coherences to zero — the standard decoherence regime in which ED reproduces standard QM exactly. Outside the thin regime (Q–C boundary, saturation), σ-additivity acquires correction terms. This is an empirical-content open question, not a structural defect.
2. **Inherited upstream sesquilinear inner product.** The theorem is conditional on the participation-measure framework's inner-product structure (§2.2); a separate program arc establishes the inner product itself as forced by primitives [6, 7], which when promoted makes the present theorem unconditional.
3. **Discrete-channel case.** The argument applies to discrete (finite or countable) channel sets; continuous-spectrum extensions (position measurements, continuous-channel POVMs) require additional measure-theoretic work analogous to standard Gleason extensions.
4. **Channel-as-primitive ontology.** A future amendment to Primitive 07 weakening "channel identity is intrinsic to the graph" would invalidate Link 1's syllogism. The present theorem's strength is precisely that of the channel-as-primitive ontology of Primitive 07.

### 5.4 What this derivation supersedes

The Phase-1 Step-3 derivation [3, §3.3] established the Born rule via a primitive-level decoherence argument: environmental phase-randomisation at commitment averages cross-channel coherences to zero, leaving the bandwidth-fraction probability rule on the post-decoherence diagonal mixture. That derivation was FORCED conditional on a single CANDIDATE — the phase-independence of environmental random phases across channels — which was the structural-derivation residual.

Theorem 10 supersedes Step 3 in three ways:

1. **Eliminates the phase-independence CANDIDATE.** §3.4's non-contextuality argument is more fundamental: it derives the partition-independence of per-channel bandwidth from the channel-as-primitive ontology directly, without needing to invoke environmental decoherence as the mechanism. Step 3's derivation works in the thin-participation regime via decoherence; Theorem 10 works in the same regime via the more basic structural fact that channels are graph-substructures whose bandwidths are intrinsic.
2. **Extends to POVM measurements.** Step 3 covered projective measurements only (single-channel commitment outcomes). Theorem 10 covers all generalised measurements via Busch — including partial measurements, joint measurements of incompatible observables, and continuous monitoring with finite efficiency.
3. **Anchors the result in established mathematical-physics theorems.** Step 3 was a primitive-level derivation; Theorem 10 is a primitive-level admissibility check followed by quotation of Gleason and Busch. The latter is structurally cleaner and more transferable to readers familiar with the standard QM-foundations literature.

Step 3's derivation is not invalidated — it remains correct as an alternative route to the projective-Born case. Theorem 10 is the structurally superior derivation and should be cited as the canonical Born-rule result from this point forward.

### 5.5 Why the squared exponent is FORCED, not arbitrary

A persistent puzzle in QM foundations is the specific squared form of the Born rule: why $|\psi|^2$ and not $|\psi|$, $|\psi|^3$, or any other exponent? Various formulations of QM offer accounts: Many-Worlds via decision theory, Zurek's envariance via environmental symmetries, QBism via Bayesian credences. Each requires its own auxiliary commitments.

In ED, the squared exponent is not a separately-justified choice; it is a *definitional consequence* of the participation-measure construction (1). The construction defines $b_K = |P_K|^2$. Bandwidth is the Primitive-04 quantity — the graded measure of participation. The bandwidth-fraction probability rule (3) is the natural classical-probability measure on the post-decoherence incoherent mixture of channel-indexed states. Therefore the probability of commitment outcome $K$ is bandwidth-fraction, which is squared-amplitude-fraction, which is the Born expression.

The same exponent 2 appears, by the same definitional commitment, in:

- the sublinear bandwidth composition rule $b_\mathrm{combined}^2 = b_1^2 + b_2^2 + 2 c_{12} b_1 b_2$;
- the Madelung decomposition $\Psi = \sqrt{\rho} \cdot e^{i S / \hbar}$ of the wavefunction;
- the Schrödinger kinetic term $\hat{H}_\mathrm{kinetic} = -\hbar^2 \nabla^2 / (2m)$;
- the Heisenberg uncertainty inequality $(\Delta x)^2 (\Delta p)^2 \geq (\hbar/2)^2$.

All five "2"s are the same 2 — the structural commitment that bandwidth equals amplitude squared. This is the *Exponent-2 Thread* that runs through the QM-emergence framework's principal results: a single primitive-level commitment manifested in five canonical contexts. Theorem 10 establishes that the Born rule's exponent is not an independent choice but one face of this single commitment.

---

## 6. Discussion

### 6.1 Position within the ED program

Theorem 10 takes its place as the tenth FORCED structural theorem in the ongoing ED program inventory, alongside spin-statistics ($\eta = (-1)^{2s}$, R.2.5), Cl(3,1) frame uniqueness (R.2.4), anyon prohibition in 3+1D (R.2.3), Dirac equation emergence (R.3), GRH unconditional (Q.1+Q.8), canonical (anti-)commutation (Q.7), UV-FIN (Q.8), the V1 finite-width vacuum kernel (Theorem N1, N.5), and V1 with Synge world function (Theorem GR1, GR.5).

The result is the program's first complete primitive-level reduction of an axiomatic-grade quantum-mechanical postulate to structural consequences of the participation-measure framework. Earlier QM-emergence work [3] derived all four foundational QM postulates (Schrödinger evolution, Born rule, Bell-Tsirelson correlations, Heisenberg uncertainty) from a small set of upstream CANDIDATE structural commitments; the present paper promotes the Born derivation specifically to theorem grade by anchoring it in Gleason/Busch.

### 6.2 Comparison with other Born-rule derivations

For context, we situate Theorem 10 against the principal alternative derivation programs:

- **Gleason's theorem (1957).** Derives Born from non-contextuality + σ-additivity + normalisation on Hilbert-space projectors of dimension $\geq 3$. Does not derive the Hilbert-space structure itself; assumes it. Treats non-contextuality as an unmotivated postulate.
- **Many-Worlds / Deutsch-Wallace decision-theoretic derivations.** Derive Born via rationality axioms on agents in branching-universe scenarios. Wallace's derivation has been disputed; the rationality axioms are contested.
- **Zurek envariance.** Derives Born from environmental symmetries of entangled states. Requires assuming specific symmetry properties of system-environment couplings.
- **Hardy-style five-axiom reconstructions.** Derive QM (and Born within it) from operational axioms about probability theory plus a "continuity" axiom selecting QM over classical theories. Operationally elegant but not connected to a deeper ontology.
- **ED (this paper).** Derives Born from the participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$ (forcing $b_K = |P_K|^2$) plus environmental phase-randomisation at commitment plus the channel-as-primitive ontology forcing non-contextuality.

The ED derivation's distinctive feature is that the squared-amplitude exponent is not an emergent property requiring decision-theoretic, symmetry, or operational justification. It is a definitional consequence of how the participation measure is constructed from the underlying primitives. The "exponent 2" is the same 2 that appears in the sublinear-composition rule, the Madelung decomposition, and the Dimensional-Atlas anchoring $\rho \leftrightarrow |\psi|^2$. The structural unification is more economical than the post-hoc justifications standard QM-foundations programs offer.

### 6.3 Downstream implications

Theorem 10 unblocks several downstream items in the QM-emergence program:

- **Bell / Tsirelson (Phase-1 Step 4).** The Bell-CHSH inequality $|S| \leq 2\sqrt{2}$ at the Tsirelson bound was previously derived [3, §3.4] conditional on the same inherited upstream sesquilinear-inner-product item that conditions Theorem 10. Tsirelson's bound derives from operator-norm / Cauchy-Schwarz inequalities on the bipartite Hilbert space; once the inner-product structure is in place (separately addressed [6, 7]), Bell-Tsirelson promotes to fully unconditional, joining Theorem 10 as a structural consequence.
- **Heisenberg uncertainty (Phase-1 Step 5).** $\Delta x \cdot \Delta p \geq \hbar/2$ derives from the Fourier-conjugate decomposition of the adjacency-band bandwidth budget plus the Fourier-uncertainty theorem applied to wavefunctions in the $L^2$ inner product. Same conditionality structure as Bell; same simultaneous promotion path.
- **POVM-based quantum-information protocols.** Theorem 10's extension from projective measurements to POVMs gives ED structural derivations of standard quantum-information results that depend on POVM structure — specifically, generalised measurements in continuous-monitoring protocols, joint measurements of incompatible observables, and tomographic completeness arguments.

Across the QM-emergence Step-1 program, the upstream CANDIDATE inventory now stands at four items (the participation-measure construction itself; the participation-measure evolution equation; the momentum-basis identification; the adjacency-band conjugate partition) plus the inherited inner-product item. The Born / Bell / Heisenberg suite is unified under the same gating structure, with the present paper supplying the cleanest derivation of the most fundamental of the three.

### 6.4 What ED legitimately claims

In the spirit of methodological honesty established in earlier ED publications [4]:

- The squared-amplitude form of the Born rule is FORCED by the participation-measure construction.
- Non-contextuality of the bandwidth-fraction probability rule is FORCED by the channel-as-primitive ontology + bandwidth-as-edge-weight structure.
- The Gleason/Busch reconstruction makes Theorem 10 transferable to readers familiar with the standard QM-foundations literature.
- Coverage extends from projective measurements to general POVMs.
- The derivation supersedes Step 3 by eliminating its phase-independence CANDIDATE.

### 6.5 What ED does NOT claim

- Theorem 10 does not predict any deviation from standard Born probabilities at any current empirical regime. ED reproduces QM exactly at the tested level.
- ℏ is not derived from ED primitives; it is inherited from the Dimensional-Atlas Madelung anchoring $D_\mathrm{phys} = \hbar / (2m)$.
- The specific Schrödinger Hamiltonian form $H = p^2/(2m) + V$ is inherited, not derived.
- The sesquilinear inner product is adopted in the present paper as an inherited upstream item; its primitive-level derivation is the subject of separate work [6, 7].
- The relativistic and QFT extensions of the Born derivation are out of scope here.

---

## 7. A Non-Technical Explainer

*This section is intended for a general scientific audience and is not part of the formal derivation.*

### 7.1 The hundred-year puzzle

The Born rule says: when you measure a quantum system, the probability of any outcome is the squared magnitude of that outcome's amplitude. *Squared.* Not absolute value, not cubed — squared.

For nearly a century, that exponent has been a postulate. Quantum mechanics asks us to accept it as a brute fact about how the world works. Gleason's 1957 theorem went part of the way toward explaining it: if you accept a few structural conditions about how probabilities can be assigned to quantum measurement outcomes, then the Born rule's squared form is mathematically forced — there is no other consistent choice.

But Gleason's theorem leans on one substantive assumption: **non-contextuality**. The probability of an outcome cannot depend on which other outcomes happen to be in the surrounding measurement context. It can only depend on the outcome itself.

Standard quantum mechanics postulates non-contextuality. It seems true experimentally, and assuming it makes the math work. But nothing about standard quantum mechanics's underlying ontology *forces* non-contextuality. It is an extra ingredient.

### 7.2 What Event Density adds

Event Density starts from a different ontology. Instead of treating the quantum state as the primitive object, ED treats the underlying participation graph as primitive — and inside that graph, *channels* (the pathways along which the quantum system's evolution rule can play out) are themselves ontologically primitive sub-structures.

A channel, in ED, is not a basis label that some observer chose to slap onto the state. It is a real structural feature of the graph — a particular subgraph with particular bandwidth-coherence properties — that exists whether anyone is measuring or not.

**Bandwidth** is an edge-weight on the graph. The bandwidth of a channel is an integral of edge-weights along that channel's edges. It is a property of the channel itself, not of any organisational scheme imposed onto it from outside.

Once you accept these two structural facts, non-contextuality follows automatically. The probability of selecting channel $K$ is the bandwidth of $K$ divided by the total bandwidth at the measurement locus. The numerator depends on $K$ alone. The denominator is the total bandwidth at that locus — a single number that does not change depending on how someone chooses to enumerate the channels.

There is no room for the probability to depend on the surrounding context. The "context" is an external organisational choice; the bandwidth is intrinsic.

### 7.3 What this gives us

With non-contextuality forced rather than postulated, Gleason's theorem (and its Busch extension covering qubit-like two-state systems) applies directly to ED. The conclusion is the Born rule — squared amplitudes, the same exponent that has been mysterious for a century — now derived as a structural consequence of the participation-graph ontology rather than postulated as a separate axiom.

The squared exponent is not arbitrary. It is the same squared exponent that defines bandwidth as squared amplitude in the participation-measure construction. Once you have channels as primitive ontological objects with bandwidth as their edge-weight property, the Born rule is not a new ingredient — it is a consequence of how the framework is built.

### 7.4 The honest framing

This result does not predict that quantum mechanics will behave differently in any current laboratory experiment. The Born rule is the Born rule, and ED reproduces it exactly.

What changes is the *grammar* of the answer to the question "why?" In standard quantum mechanics: "because we postulate it." In ED: "because channels are graph-substructures, bandwidth is their edge-weight, and what you call probability is the bandwidth fraction at the measurement locus — and that fraction is, by structural necessity, partition-independent and squared."

The explanatory burden moves from the Born rule itself to the deeper structural commitment underneath it. That is what physics has always called progress when it has worked: Maxwell unifying electricity and magnetism, Einstein unifying space and time, the Standard Model unifying the weak and electromagnetic forces. Each move replaced a brute postulate with a structural consequence of a deeper framework. The present paper applies the same kind of move to one of quantum mechanics's most famous brute postulates.

---

## 8. Recommended Next Steps

For the author and the broader ED program, the following near-term items are flagged in light of Theorem 10:

1. **Promote the inherited inner-product item.** Theorem 10's single residual conditionality is the participation-measure framework's sesquilinear inner product (§2.2). A focused arc establishing this inner product as forced by primitives — completed in companion work [6, 7] — promotes Theorem 10 to fully unconditional. The bundled promotion also unblocks Bell-Tsirelson and Heisenberg simultaneously.

2. **Update the QM-emergence synthesis paper.** The synthesis paper [3]'s §3.3 (Step 3 — Born rule) and §4 (upstream CANDIDATEs) require revision to cite Theorem 10 as the canonical Born derivation, note Step 3's supersession, and update the upstream-CANDIDATE inventory accordingly.

3. **Distinguishing experimental predictions in regimes where the thin limit breaks down.** Theorem 10 reproduces standard Born probabilities exactly in the thin-participation regime. ED's distinguishing-content predictions live at the Q–C boundary, in cosmological saturation regimes, and in extended-source environments where the thin limit fails. Identifying clean experimental falsifiers of ED-specific corrections remains an open program-level item.

4. **Extension to the relativistic and QFT regimes.** The present paper is non-relativistic and single-particle. Extending the Born derivation to relativistic single-particle systems (using Arc R's framework [4]) and to multi-particle QFT (using Arc Q's framework [5]) is the natural follow-up structural arc.

---

## Appendix: Section-to-Memo Mapping

The present paper integrates the results of a six-memo derivation arc (the *born_gleason* arc). For traceability, the mapping between paper sections and underlying memos is as follows.

| Paper section | Underlying memo | Memo content summary |
|---|---|---|
| §3.1 (Gleason's assumptions) | Memo 01 | Inventory of Gleason's eight load-bearing assumptions; classification by ED-correspondent status (automatic / interpretive / load-bearing) |
| §3.2 (Automatic / interpretive items) | Memo 01 | Mapping of A1, A2, A3, A5, A6 to ED primitives |
| §3.3 (σ-additivity) | Memo 03 | Verification of A7 via non-negativity, countable channel sets, finite total bandwidth, partition-independence |
| §3.4 (Non-contextuality) | Memo 02 | Three-premise syllogism forcing partition-independence of $b_K(u)$; loophole audit (sublinear composition, context-dependent channel set, channel-to-ray correspondence) |
| §3.5 (Admissibility summary) | Memo 03 | Joint admissibility status table for $d \geq 3$ case |
| §4 (Busch extension, $d = 2$) | Memo 04 | Translation of weighted channel-subsets into Busch's POVM framework; verification of B1–B4; Bloch-sphere effect generation; spin-$\tfrac{1}{2}$ / polarisation / qubit closure |
| §5.1 (Theorem statement) | Memo 05 | Full theorem-grade statement with scope conditions |
| §5.2 (Proof sketch) | Memo 05 | Four-link chain assembling the structural derivation |
| §5.3 (Scope conditions) | Memo 05 | Thin-participation regime, inherited inner-product conditionality, discrete-channel restriction, Primitive-07 ontological-status sensitivity |
| §5.4 (Supersession of Step 3) | Memo 05 | Three-way comparison: phase-independence elimination, POVM extension, Gleason/Busch anchoring |
| §5.5 (Exponent-2 thread) | Memo 04 §3 + Memo 05 §5 | Definitional origin of squared-amplitude form; five-context manifestation |
| §6 (Discussion) | Memo 06 | Position in ED program, comparison with alternative derivations, downstream implications |
| §7 (Non-technical explainer) | Memo 06 §6 | Lifted with light editing from the closure-memo public-explainer section |

---

## References

[1] A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," *Journal of Mathematics and Mechanics* **6**, 885–893 (1957).

[2] P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," *Physical Review Letters* **91**, 120403 (2003).

[3] *QM Emergence Structural Completion.* `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.{md,tex,pdf}`. Internal ED program reference establishing the Phase-1 five-step QM-emergence framework.

[4] *Arc R: Relativistic Kinematics and Dynamics in Event Density.* `papers/Arc_R/paper_arc_r.{md,tex,pdf}`.

[5] *Arc Q: QFT Extension in Event Density.* `papers/Arc_Q/paper_arc_q.{md,tex,pdf}`.

[6] *The Inner Product as a Forced Structure: Sesquilinearity and the ED Participation Measure (Discrete Regime).* Companion paper, in preparation; establishes the sesquilinear inner product (Theorem 11) as forced by the primitive stack on the participation-graph vertex set.

[7] *Gauge-Invariant Continuum Inner Product in Event Density: Conformal Redundancy and Forced Structure.* Companion paper, in preparation; establishes the continuum inner-product lift (Theorem 12) as forced with explicit gauge structure under Primitive 12 thickening.

[8] S. Kochen and E. P. Specker, "The Problem of Hidden Variables in Quantum Mechanics," *Journal of Mathematics and Mechanics* **17**, 59–87 (1967).

[9] C. M. Caves, C. A. Fuchs, K. K. Manne, and J. M. Renes, "Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements," *Foundations of Physics* **34**, 193–209 (2004).

[10] *Arc N: Non-Markovian Structure as a Forced Memory-Kernel Layer of Event-Density Theory.* `papers/Arc_N/arc_n_paper.{md,tex,pdf}`.

[11] *Phase-3: Gravitational Sector of Event-Density Theory.* `papers/Phase_3/` (in preparation).

---

*Manuscript prepared April 2026. Source materials: `arcs/born_gleason/` six-memo derivation arc, integrated into a single publishable document.*
