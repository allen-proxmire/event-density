# Gauge Fields are FORCED (Theorem 17)

**Paper #5 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #5 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The gauge structure of standard physics — local symmetry, gauge potentials $A_\mu$, covariant derivatives, field strengths, minimal coupling — is normally a list of postulates. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the substrate's primitive rule-type structure (the substrate supports multiple structural rule-types $\tau_g$ with their own participation measures)**, the entire gauge architecture is forced as Theorem 17 with nine load-bearing clauses: the gauge potential is the participation measure of a rule-type $\tau_g$; the group structure admits non-Abelian Lie algebras with Killing-form / Jacobi closure; the matter-gauge vertex is vertex-anchored minimal coupling; the field strength is the commutator of transported phases; the worldline structure for massless excitations is lightlike; the vacuum sector carries a gauge-invariant UV-finite V1-form fluctuation envelope; all four channels respect a single unified gauge-quotient. The specific gauge group (U(1), SU(2), SU(3), or otherwise) and coupling magnitudes are inherited from the value layer. The claim is conditional: the rule-type primitive — that the substrate supports gauge-rule-types alongside matter-rule-types — is itself a primitive-level structural commitment, not derived here. Postulated-gauge, global-only-symmetry, non-connection-based, and quaternionic alternatives are each excluded *given that primitive*. Whether the rule-type primitive itself is necessary (and what forces it from a deeper layer) is upstream content for the Primitive-Forcing Meta-Paper.

---

## 1. Framing

### 1.1 What standard physics postulates about gauge fields

Every undergraduate textbook on quantum field theory presents the gauge structure as a list of axioms. To couple a matter field to electromagnetism, one introduces a U(1) gauge potential $A_\mu(x)$, replaces every ordinary derivative $\partial_\mu$ with a covariant derivative $D_\mu = \partial_\mu + ieA_\mu$, builds the field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, and forms the Lagrangian $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi$. For non-Abelian theories, the same construction repeats with a non-commutative gauge potential $A_\mu^a T^a$, a non-Abelian field strength $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - gf^{abc}A_\mu^b A_\nu^c$, and the Yang-Mills Lagrangian.

Five structural facts are bundled into this construction:

1. **Existence of a gauge potential $A_\mu$.** The potential is a primary field, distinct from the matter field and from the observable field strength.
2. **Local symmetry.** The Lagrangian is invariant under $\psi \to U(x)\psi$, $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$, with $U(x)$ varying from point to point — *local*, not global.
3. **Field strength as curvature.** $F_{\mu\nu} \propto [D_\mu, D_\nu]$ — the commutator of covariant derivatives produces the gauge-invariant observable.
4. **Minimal coupling.** Matter couples to the gauge field exactly through the replacement $\partial \to D$ — no Pauli term, no anomalous magnetic moment by hand, no extra interaction structure.
5. **Specific gauge group.** Nature uses U(1) for electromagnetism, SU(2)×U(1) in the electroweak sector, SU(3) for QCD. Each is a compact simple (or product of compact simple) Lie group with Killing-form / Jacobi closure.

These five facts arrived historically as inferences from experiment and were later organized into the modern formalism. Where they come from — why local rather than global symmetry, why minimal coupling rather than non-minimal, why compact Lie groups rather than discrete groups or non-compact ones — is not derived in standard quantum field theory. They are part of the package.

### 1.2 The puzzle

Several programs have attempted to motivate parts of the gauge structure from deeper principles:

- **Weyl's gauge-principle argument** (1929): if the matter-field phase is locally redefinable, the covariant derivative + gauge potential structure follows by demanding that the dynamics remain invariant. The local-phase-redefinability is the input; gauge structure is the consequence.
- **Fiber-bundle reconstruction**: gauge theories are reformulated as connections on principal bundles. The Lie group, the bundle, and the connection form are mathematical inputs.
- **Emergent-gauge programs** in condensed matter (spin liquids, lattice gauge models): gauge-field-like structures emerge as effective descriptions of highly entangled states. The microscopic Hamiltonian and the emergence mechanism are inputs.

None of these programs derives the gauge structure from a *substrate of pre-quantum, pre-field-theoretic primitive structure*. The deeper question — why the world has rule-types whose participation measures behave like connections on bundles, with curvatures and minimal couplings — remains unaddressed.

A program that wants to settle the question structurally needs:

1. A pre-quantum substrate that contains structural rule-types as primitives, but no gauge group, no covariant derivative, no field strength.
2. An argument that polarity transport on the participation manifold, plus bandwidth conservation, forces the connection structure.
3. An explicit exclusion of alternatives — no-gauge-fields, global-only-symmetry, non-minimal-coupling, real-valued, quaternionic — by substrate-condition violation.

### 1.3 What this paper does

The Event Density (ED) framework supplies the first ingredient. Papers #1-#4 establish the participation measure, the Born rule, the sesquilinear inner product on the participation manifold, and the Schrödinger evolution equation — all forced from substrate primitives. The present paper takes this machinery as input and proves **Theorem 17 (T17)** — the Gauge-Field-as-Rule-Type Hypothesis — as a substrate-level forcing theorem with nine load-bearing clauses (C1-C9):

- **C1 (Carrier)**: $A_\mu$ is the participation measure of a substrate-level rule-type $\tau_g$.
- **C2 (Group structure)**: $\tau_g$ admits a non-Abelian-capable gauge group with Killing-form / Jacobi closure.
- **C3 (Vertex)**: matter-gauge interactions are vertex-anchored minimal-coupling vertices.
- **C4 (Worldline)**: $\tau_g$ excitations with $\sigma = 0$ propagate on lightlike worldlines.
- **C5 (Vacuum kernel)**: the vacuum sector carries a UV-finite V1-form gauge-invariant fluctuation envelope.
- **C6 (Vacuum classification)**: three admissible vacuum classes on two orthogonal axes; excitation-vacuum is the minimal FORCED class.
- **C7 (Vacuum commitment)**: the vacuum is strict-non-committing; a gauge-invariant background functional $B[v;\tau_g]$ contributes additively to vertex-anchored commitment rates.
- **C8 (Unified quotient)**: all four channels (group, vertex, worldline, vacuum) respect a single unified gauge-quotient.
- **C9 (Acyclic derivability)**: clauses C1-C8 are derivable from substrate primitives + Papers #1-#4 alone, with no downstream input.

Each clause traces explicitly to substrate primitives. Alternative structures — no-gauge-fields, global-only-symmetry, non-connection-based transport, non-curvature field strength, non-minimal coupling, real-valued or quaternionic gauge structure, non-compact Lie groups — are excluded by explicit substrate-condition violation.

**The specific gauge group** (U(1), SU(2), SU(3), or other compact-simple-Lie group) and **coupling magnitudes** are INHERITED from the value layer; T17 commits only to the *admissible class* (non-Abelian-capable compact-simple-Lie-group-with-Killing-form-closure structure), not to any specific member of it.

**Series context.** Paper #1 forced the amplitude carrier. Paper #2 forced the probability rule. Paper #3 forced the inner product and the Tsirelson ceiling. Paper #4 forced the Schrödinger dynamics. The present paper forces the first interaction structure: gauge fields appear as forced rule-types coupling to the matter participation measure via vertex-anchored commitment. Together, Papers #1-#5 cover the complete kinematic + dynamical + interaction backbone of non-relativistic gauge-coupled quantum mechanics.

---

## 2. Claim

> **Theorem 17 (Gauge-Field-as-Rule-Type, T17).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results plus the rule-type primitive (the substrate supports multiple structural rule-types $\tau_\bullet$ with their own participation measures)*. Then there exists a structural rule-type $\tau_g$ whose participation measure $A_\mu$ is FORCED to satisfy the nine clauses C1-C9:
>
> 1. **(C1)** $\tau_g$ is a rule-type with non-empty participation measure on the gauge-Lie-algebra fibre.
> 2. **(C2)** $\tau_g$ admits a non-Abelian-capable gauge group with Killing-form / Jacobi closure.
> 3. **(C3)** Commitment events for $\tau_g$ are vertex-anchored, with structural minimal-coupling vertex.
> 4. **(C4)** $\sigma = 0$ excitations of $\tau_g$ propagate on lightlike worldlines with second-quantization lifting.
> 5. **(C5)** The vacuum sector carries a UV-finite V1-form gauge-invariant fluctuation envelope.
> 6. **(C6)** Three admissible vacuum classes; excitation-vacuum is the minimal FORCED class.
> 7. **(C7)** Vacuum is strict non-committing; gauge-invariant $B[v;\tau_g]$ contributes additively to commitment rates.
> 8. **(C8)** All four channels respect a single unified gauge-quotient under the $\tau_g$ gauge group.
> 9. **(C9)** C1-C8 derivable from substrate primitives + Theorems 1-16 alone.
>
> The form of the gauge structure is FORCED. The specific gauge group and coupling magnitudes are INHERITED.
>
> *The rule-type primitive is load-bearing; why the substrate has multiple rule-types is upstream content (Primitive-Forcing Meta-Paper).*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **P09 ($U(1)$-valued polarity):** substrate-level structural source of the $U(1)$ phase content downstream-derived as the gauge group of electromagnetism.
- **P10 (rule-type primitive):** the substrate supports multiple structurally distinct rule-types $\tau_\bullet$, each with its own participation measure. Matter rule-types and gauge rule-types are *different rule-types*, not different states of the same one.
- **P05 (polarity-transport between adjacent loci):** the substrate-level connection structure — mechanism by which polarity at one locus is transported to a neighboring locus along edges of the participation graph.
- **Papers #1–#4 results:** the participation-manifold Hilbert space and its dynamics.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, Theorem 17 (T17) — the Gauge-Field-as-Rule-Type result with nine clauses C1–C9 — follows. The admissible class of gauge groups (compact simple Lie groups with Killing-form / Jacobi closure) is structurally fixed; the specific gauge group (U(1), SU(2)×U(1), SU(3)) and coupling magnitudes are inherited from value-layer empirical content.

### 3.1 What is FORCED

- The **existence of a gauge potential** $A_\mu$ as the participation measure of a substrate-level rule-type $\tau_g$ (C1).
- **Non-Abelian-capable group structure** with Killing-form / Jacobi closure (C2). The substrate admits compact simple Lie groups as the admissible class.
- **Vertex-anchored minimal coupling** between matter and gauge rule-types (C3). No non-minimal terms at the substrate level.
- **Lightlike worldlines** for massless $\tau_g$ excitations (C4).
- **UV-finite V1-form vacuum kernel** with gauge-invariant fluctuation envelope (C5).
- **Three vacuum classes** on two orthogonal axes; excitation-vacuum minimal (C6).
- **Strict non-committing vacuum** + gauge-invariant background functional $B[v]$ contributing additively to commitment rates (C7).
- **Unified gauge-quotient** across all four channels (C8).
- **Acyclic derivability** from primitives + Theorems 1-16 (C9).
- **Field strength as curvature**: $F_{\mu\nu} \propto [D_\mu, D_\nu]$ as the structural-derivative consequence.
- **Local gauge-quotient invariance**: structurally-identical configurations are not distinguished by the substrate.

### 3.2 What is INHERITED

- **Specific gauge group.** U(1) for electromagnetism, SU(2)×U(1) for electroweak, SU(3) for QCD. The choice of specific group is empirical (or inherited from value-layer commitments such as the matter-rule-type content of the Standard Model). T17 commits only to the *non-Abelian-capable group structure* admissible class, not to any specific member of it.
- **Coupling constants** $e$, $g$, $g'$, $g_s$, the gauge couplings of the Standard Model. Inherited from the value layer.
- **V1 kernel parameters** for the gauge-field vacuum sector. Inherited from the substrate vacuum-kernel structure of the ED program's Arc N.
- **$B[v;\tau_g]$ amplitude.** The background functional's specific amplitude is INHERITED from substrate microscopic details.
- **Vacuum energy density.** Inherited from V1 kernel parameter; cosmological constant $\Lambda$ value lives in Arc N + Phase-3 GR territory.
- **Specific labeling of generators.** The basis of generators $T^a$ in the Lie algebra is a labeling choice; the structural content is the algebra itself.

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive the full Standard Model. Specific gauge group (SU(3)×SU(2)×U(1)), matter content (quarks, leptons, three generations), and coupling values are inherited from the value layer. T17 commits only to the structural existence of gauge-field-class rule-types and their interface property.
- This paper does **not** derive the Higgs mechanism. Symmetry breaking and the Higgs sector require additional substrate content (the matter-rule-type sector and its vacuum-condensate structure) not addressed here.
- This paper does **not** derive gravity. Gravitational coupling lives in a separate ED-program sector (substrate-gravity arc) treating curvature emergence as a different forcing chain.
- This paper does **not** derive specific propagator forms or scattering amplitudes. The Feynman-diagram machinery operates downstream of the structural commitments forced here.
- This paper does **not** address full QFT vacuum content (Higgs VEV, QCD condensates, instantons, $\theta$-vacua). The substrate vacuum-kernel structure forces a gauge-invariant V1-form fluctuation envelope; the specific vacuum content of the Standard Model is value-layer empirical.

---

## 4. Key Vocabulary

For the reader new to Event Density:

- **Substrate.** Pre-quantum layer of primitive structure on which the ED framework is built. Not a Hilbert space, manifold, or field theory.
- **Rule-type.** A substrate primitive (P02) class of structural pathway — a kind of channel admitting its own participation measure. Matter fields and gauge fields are participation measures of distinct rule-types.
- **Participation measure.** The complex-valued amplitude carrier on each channel of the participation graph; for the matter sector, $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ (Paper #1); for the gauge sector, the gauge potential $A_\mu$.
- **Polarity.** A primitive $U(1)$-valued angular variable on each channel at each locus.
- **Polarity transport.** The structural action by which a polarity value is carried along a path on the participation manifold from one locus to another.
- **Connection.** A geometric object encoding the path-dependence of polarity transport: parallel transport over a path produces a phase factor determined by the connection.
- **Curvature.** The 2-form $F = dA + A \wedge A$ measuring the path-dependence of transport around an infinitesimal loop. Equivalently, the commutator $F_{\mu\nu} \propto [D_\mu, D_\nu]$ of covariant derivatives.
- **Holonomy.** The phase factor accumulated by polarity transport around a closed loop. Equal to $\exp(\oint A_\mu dx^\mu)$ in the U(1) case.
- **Minimal coupling.** The substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu T^a$ in the matter dynamics. In ED language: matter-gauge interactions enter through the substrate-level vertex-anchored commitment vertex, with no separate non-minimal interaction terms.
- **Gauge potential.** The connection 1-form $A_\mu$; the gauge field as opposed to the gauge field strength.
- **Gauge-quotient.** The equivalence relation identifying structurally-identical gauge configurations $A_\mu \sim A_\mu - g^{-1}(\partial_\mu U)U^{-1}$ for $U(x)$ in the gauge group. Local symmetry is the substrate-level fact that this quotient is respected.
- **Killing form.** Bilinear form $K(X, Y) = \text{tr}(\text{ad}_X\,\text{ad}_Y)$ on a Lie algebra; non-degenerate on semisimple Lie algebras. Load-bearing for the gauge-invariant action $\text{tr}(F_{\mu\nu}F^{\mu\nu})$.
- **Jacobi identity.** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$ for the Lie bracket; characterizes Lie algebras.
- **V1 kernel.** Substrate-level finite-width spatial vacuum kernel (Paper-series item: Theorem N1); load-bearing for the gauge-field vacuum-kernel structure.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Participation graph + channel structure (Primitives P03 + P07)

The substrate supplies a participation graph $G = (V, E)$ with vertex set $V$ (loci) and edge set $E$ (participation relations). At each locus $u \in V$ there is an available-channel set $\mathcal{K}(u)$ of channels at $u$, at most countable, with channels ontologically primitive.

### C2. Bandwidth with additivity (Primitive P04)

The substrate supplies non-negative bandwidth $b_K(u) \in \mathbb{R}_{\geq 0}$ on each channel at each locus, with primitive-level additivity over disjoint channel decompositions. Bandwidth has a four-band decomposition (internal, adjacency, environmental, commitment-reserve) with total bandwidth conserved along an isolated chain's persistence regime.

### C3. Polarity (Primitive P09)

The substrate supplies a $U(1)$-valued angular variable $\pi_K(u) \in U(1)$ on each channel — the unique angular primitive in the substrate. $U(1)$-invariance of bandwidth (which depends only on the magnitude content of the participation measure, not on its phase) is the load-bearing structural fact (Paper #16).

### C4. Time homogeneity (Primitive P13)

The substrate supplies a continuous time axis with homogeneous structure, supplying the dynamics of Paper #4.

### C5. Commitment events (Primitive P11)

The substrate supports discrete commitment events at which a chain's multi-channel participation collapses to a single channel. Two operational features of commitment are required:

- **Vertex-anchored**: each commitment event occurs at a specific locus (a "vertex" in the participation-graph sense), and the rule-type's contribution to the commitment-rate enters through that vertex.
- **Environmental phase-randomization**: during commitment, environmental coupling acts on the participation phases as independent random shifts. (Paper #14 §7.3.)

These features are substrate-level operational content of the commitment primitive; they are not gauge-field-specific.

### C6. Rule-type primitive (Primitive P02)

The substrate supplies a structural primitive class of **rule-types** $\{\tau\}$ — kinds of channel structure admitting their own participation measures. The matter rule-type $\tau_m$ and the gauge rule-type $\tau_g$ are distinct elements of this class. Rule-types have **interface properties**: structural facts about a rule-type that govern its interaction with other rule-types via shared substrate content (vertices, vacuum kernels, gauge-quotient identifications).

### C7. Inherited results from Papers #1-#4

- **Paper #1**: complex-valued participation measure on each channel.
- **Paper #2**: Born rule for commitment outcomes.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #4**: linear unitary first-order Schrödinger dynamics with self-adjoint generator.

A reader who has not read Papers #1-#4 may take C7 as a definitional premise: the matter sector of the substrate carries a complex Hilbert-space arena with unitary time evolution.

### C8. Theorems 1-16 inherited from earlier ED arcs

The forcing argument additionally inherits from:
- **Theorem 5** (form-level GRH, $A_\mu$ as participation measure of $\tau_g$ — the form-level antecedent of T17).
- **Theorem 6** (canonical (anti-)commutation relations for second quantization).
- **Theorem 7** (UV-finiteness, $\ell_P$ substrate cutoff — load-bearing for C5).
- **Theorem 8 / N1** (V1 finite-width vacuum kernel — load-bearing for C5).
- **Theorems 1-4** (spin-statistics, Cl(3,1), anyon prohibition, Dirac equation — relativistic structure).
- **Theorems 10-16** (Born / U2 / U3 / U4 / U5 / Heisenberg — QM-emergence structural foundations).

These are inherited as established results; their derivations are in prior ED-program work.

### C9. No gauge structure as input

The forcing argument invokes only C1-C8. No gauge group, no covariant derivative, no field strength, no gauge invariance, no Yang-Mills Lagrangian, no fiber-bundle structure is assumed. These are produced by the forcing chain.

The argument additionally uses standard mathematical infrastructure: Lie-algebra theory (Frobenius classification of real division algebras was used in Paper #1; for non-Abelian gauge structure we additionally invoke the classification of compact simple Lie groups by Cartan); the Killing-form non-degeneracy criterion; the Jacobi identity for Lie brackets; and the standard differential-geometric machinery of connections and curvatures on principal bundles.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. No gauge fields.** No rule-type $\tau_g$ distinct from the matter rule-type $\tau_m$. Matter fields exist; gauge potentials do not. Interactions, if any, are non-gauge — direct contact terms or non-derivative couplings.

**A2. Global-only symmetry.** A rule-type $\tau_g$ exists, but its symmetry group acts globally only: $\psi \to U\psi$ with $U$ independent of position. Local gauge transformations $\psi \to U(x)\psi$ are not respected.

**A3. Non-connection-based transport.** Polarity transport along the participation manifold is path-independent (a global phase, not a connection), or path-dependent but in a way that fails the composition law for parallel transport.

**A4. Non-curvature-based field strength.** The observable field strength is defined other than as the commutator $[D_\mu, D_\nu]$ — for instance, as $\partial_\mu A_\nu$ alone (failing antisymmetry) or as $A_\mu A^\mu$ (failing gauge invariance).

**A5. Non-minimal coupling.** Matter-gauge interactions include extra non-minimal terms beyond $\partial \to D$ — Pauli moments inserted by hand, additional $F_{\mu\nu}F^{\mu\nu}\bar{\psi}\psi$ terms, contact interactions not derivable from a covariant derivative.

**A6. Real or quaternionic gauge structure.** Gauge potentials are real-valued (no phase content) or quaternion-valued ($SU(2)$-or-larger angular structure at the carrier level).

**A7. Non-U(1)/non-SU(n) phase transport.** Gauge groups outside the compact-simple-Lie class — discrete groups (e.g., $\mathbb{Z}_n$ at the gauge level), non-compact groups (e.g., $SL(n, \mathbb{R})$ as a gauge group), or non-Lie group structures.

**A8. Non-vertex-anchored interactions.** Matter-gauge interactions distributed across multiple loci or non-localized in the participation graph, violating the vertex-anchored commitment structure.

**A9. Massive gauge excitations only.** All $\tau_g$ excitations have $\sigma \neq 0$; no lightlike worldlines admitted at substrate level. (Empirically, photons are massless; this is a non-trivial substrate-level commitment.)

**A10. Non-UV-finite vacuum kernel.** The vacuum sector has divergent UV behavior, requiring regularization-dependent counterterms.

### 6.2 Mainstream alternatives

**B1. Classical electromagnetism as postulate.** Maxwell's equations adopted as fundamental. Gauge potential and field strength are inputs; their existence and structure are not derived.

**B2. Yang-Mills as postulate.** The Yang-Mills Lagrangian and the gauge group adopted as fundamental. Non-Abelian structure is postulated by analogy with electromagnetism.

**B3. Fiber-bundle gauge theory as assumption.** Gauge fields are connections on a principal $G$-bundle. The bundle, the group $G$, and the connection are mathematical inputs.

**B4. Emergent gauge fields from condensed matter.** Gauge-field-like structures emerge as effective descriptions of microscopically non-gauge systems (e.g., $\mathbb{Z}_2$ gauge theory in spin liquids, emergent photons in dimer models). The microscopic substrate is non-gauge; gauge structure is emergent in a long-wavelength limit.

**B5. Hidden-variable gauge-like models.** Hidden-variable formulations reproducing gauge predictions via non-local hidden variables, without committing to a substrate-level gauge structure.

**B6. Nonlocal gauge potentials.** Action-at-a-distance reformulations (e.g., Aharonov-Bohm-class theories) that retain observable predictions but reject the local-potential ontology.

---

## 7. Constructive Necessity

The argument establishes T17's nine clauses (C1-C9) in sequence. Each clause traces to substrate primitives + Theorems 1-16 inherited; no input from gauge field theory or fiber-bundle geometry is assumed.

### 7.1 (C1) Carrier: rule-types and their participation measures

The substrate primitive class of rule-types (C6 from P02) supplies a discrete index $\tau \in \{\tau_m, \tau_g, \ldots\}$. Each rule-type $\tau$ has its own channel-and-locus structure $\mathcal{K}_\tau(u)$ and its own participation measure $P_K^{(\tau)}(u)$ on that structure. Paper #1's result applies separately to each rule-type: the unique amplitude carrier is the complex-valued participation measure $\sqrt{b_K^{(\tau)}}\,e^{i\pi_K^{(\tau)}}$.

The matter rule-type $\tau_m$ carries the matter wavefunction $\psi(u) := \sum_K P_K^{(\tau_m)}(u)$. The gauge rule-type $\tau_g$ carries a participation measure on its own channel structure; we denote it $A_\mu^{(\tau_g)}$ — the **gauge potential**.

**Sub-step C1a: existence of $\tau_g$.** The rule-type primitive (C6) supplies multiple rule-types as elements of its class. The gauge rule-type $\tau_g$ is *one specific element* of this class. That it exists (rather than being merely admissible) follows from the substrate-level structural commitment that the rule-type class is non-trivial: it contains at least the matter rule-type $\tau_m$ and at least one further rule-type — the gauge rule-type — required to mediate matter-matter interactions (the substrate-level analog of forces).

The empirical observation that gauge interactions exist (electromagnetism, weak, strong) is consistent with this substrate-level commitment; it is one of the empirical motivations for the rule-type primitive's non-triviality.

**Sub-step C1b: $A_\mu$ as participation measure of $\tau_g$ on the gauge-Lie-algebra fibre.** Paper #1's forcing applied to $\tau_g$ produces a complex-valued amplitude carrier. The carrier indexed by gauge-Lie-algebra generators $T^a$ is the gauge potential $A_\mu^a T^a$. The Lie-algebra-valued structure (rather than scalar-valued) is necessary because $\tau_g$ couples to matter through internal indices (color, weak isospin, etc.), and the coupling must respect the algebraic structure of those internal indices.

**Provenance**: P02 (rule-type primitive) + Theorem 5 (form-level GRH, $A_\mu$ as participation measure of $\tau_g$, established in prior ED-program work). Paper #1 forces the complex-valued amplitude carrier; T17's C1 specializes this to the gauge rule-type.

### 7.2 (C2) Group structure: non-Abelian-capable Lie group with Killing-form / Jacobi closure

The substrate-level structural commitment for $\tau_g$'s group structure is forced by three structural facts:

**Sub-step C2a: Multi-channel composition forces Lie-algebra structure.** When matter has multiple channels indexed by an internal label (e.g., color, weak isospin), the gauge transport rule must act on all internal channels coherently. The composition rule for multi-channel transport requires an *associative composition* of infinitesimal transports. Associativity of composition of infinitesimal generators forces the Jacobi identity:
$$
[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0.
$$
The composition structure is therefore a Lie algebra.

**Sub-step C2b: Non-Abelian capability.** For Abelian groups, $[X, Y] = 0$ for all $X, Y$ in the algebra. This is structurally permitted but not required: the substrate's multi-channel rule-type composition is *capable* of non-Abelian structure, with $[X, Y] \neq 0$ generally. Which specific algebra (Abelian U(1) for electromagnetism, non-Abelian SU(2) for weak isospin, non-Abelian SU(3) for color) is realized empirically depends on the matter-rule-type internal-index content — inherited from the value layer.

The structural commitment of T17 is that *both* Abelian and non-Abelian structures are admissible: $\tau_g$ admits a *non-Abelian-capable* group, not a specifically-non-Abelian one.

**Sub-step C2c: Compact + simple structure.** Compactness of the gauge group is forced by the substrate's bandwidth-non-negativity (C2): the gauge-invariant action $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ must be bounded below (otherwise the substrate would have an unbounded negative-energy sector, contradicting bandwidth structure). Compact Lie groups produce positive-definite Killing forms via the trace structure of their adjoint representation; non-compact groups have indefinite Killing forms that fail this requirement.

Simple-or-product-of-simple structure is forced by the substrate's primitive minimality: the gauge group does not factor into smaller substrate-level pieces unless those pieces are themselves substrate-level rule-types. The substrate admits direct products of compact simple Lie groups (e.g., $SU(3) \times SU(2) \times U(1)$ in the Standard Model) but each factor is itself a simple Lie group at the substrate level.

**Sub-step C2d: Killing-form non-degeneracy and Jacobi closure.** The Killing form $K(X, Y) = \text{tr}(\text{ad}_X\,\text{ad}_Y)$ on the Lie algebra must be non-degenerate for the gauge-invariant action $\mathcal{L}_\mathrm{gauge} = -\tfrac{1}{2g^2}\text{tr}(F_{\mu\nu}F^{\mu\nu})$ to be well-defined. Cartan's classification of semisimple Lie algebras shows that non-degenerate Killing forms occur exactly on semisimple Lie algebras (which are direct sums of simple Lie algebras with non-Abelian structure, plus possibly Abelian factors).

The Jacobi identity (sub-step C2a) is automatic for Lie algebras. The combination of Killing-form non-degeneracy + Jacobi identity restricts the admissible class to compact semisimple Lie groups (possibly with Abelian factors), with simple components having one of the four classical types ($A_n$, $B_n$, $C_n$, $D_n$) or one of the five exceptional types ($E_6$, $E_7$, $E_8$, $F_4$, $G_2$).

**Provenance**: P02 + P04 (bandwidth non-negativity for compactness) + P10 (interface property) + Q.2 verdict + R-2 partial + R-4 (closed-arc inheritance from Arc Q). The specific gauge group (which compact simple Lie group) is INHERITED from value-layer commitments — the empirical content of the Standard Model fixes SU(3)×SU(2)×U(1) at low energies.

### 7.3 Connection structure from polarity transport

Polarity (C3) is a $U(1)$-valued angular variable on each channel at each locus. To compare polarity at distinct loci $u$ and $u'$, the substrate must provide a **transport rule** along paths $\gamma$ on the participation manifold connecting $u$ to $u'$.

Two structural facts constrain the transport rule:

- **Continuity (from C4).** Time homogeneity supplies a continuous parameter along time-like paths; spatial homogeneity (the participation-graph translation invariance underwriting Paper #4's continuum regime) supplies the same along spatial paths. Polarity transport must therefore be continuous along smooth paths.
- **Bandwidth preservation (from C2).** Transport must preserve the substrate-level bandwidth content of each channel; bandwidth is a non-negative invariant of each channel-locus pair, and parallel transport cannot create or destroy bandwidth in the absence of commitment events (C5).

Under these constraints, parallel transport of the matter participation measure $\psi$ along a path $\gamma$ from $u$ to $u'$ is uniquely (up to gauge fixing) a path-dependent unitary action on $\psi$:
$$
\psi(u') = U_\gamma\,\psi(u), \qquad U_\gamma \in G \subseteq U(1)\ \text{or non-Abelian generalization}.
$$
The unitarity follows from bandwidth preservation; the path-dependence is the structural source of the connection.

The transport rule along an infinitesimal path $u \to u + dx^\mu$ is parameterized by a Lie-algebra-valued one-form $A_\mu(u)$:
$$
U_{u \to u+dx} = \mathbb{1} + ig A_\mu(u) dx^\mu + O(dx^2),
$$
where $g$ is a coupling constant (inherited). The object $A_\mu$ is the **gauge potential** — the participation measure of $\tau_g$ at the infinitesimal-transport level.

### 7.4 Curvature from the commutator of transports

Consider transport around an infinitesimal closed loop in the participation manifold, spanned by $dx^\mu$ and $dy^\nu$. The two paths $u \to u + dx \to u + dx + dy$ and $u \to u + dy \to u + dx + dy$ differ by a phase factor $\Omega$ whose first non-trivial order is
$$
\Omega = \mathbb{1} + ig\,(\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu])\,dx^\mu dy^\nu + O(dx^3).
$$
The bracketed quantity is the **field strength**
$$
F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu] = -\frac{i}{g}[D_\mu, D_\nu],
$$
with $D_\mu := \partial_\mu + igA_\mu$ the covariant derivative.

The field strength is therefore the commutator of covariant derivatives — equivalently, the curvature 2-form of the connection. Its form is forced by the substrate-level structure of polarity transport plus the Lie-algebra composition rule (§7.2); no separate axiom is required.

**Gauge invariance of $F_{\mu\nu}$**: under a local gauge transformation $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$, the curvature transforms covariantly: $F_{\mu\nu} \to U F_{\mu\nu} U^{-1}$. The trace $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ is therefore gauge-invariant — the substrate-level observable, and the Killing-form-based action of §7.2 is well-defined.

### 7.5 (C3) Vertex: vertex-anchored minimal coupling

The substrate-level commitment primitive (C5) is **vertex-anchored**: each commitment event occurs at a specific locus. The rule-type's contribution to the commitment-rate enters through that vertex.

For the matter-gauge interaction, the vertex is the locus at which matter participation interacts with gauge participation. The structural content of the vertex is forced to be a single bilinear coupling between matter and gauge participation measures, of the form
$$
\mathcal{L}_\mathrm{int} = -g\,\bar{\psi}\,\gamma^\mu\,T^a\,\psi\,A_\mu^a
$$
in the relativistic case (Paper #7 inheritance), or its non-relativistic analog. The factor $T^a$ is the Lie-algebra generator selected by the matter rule-type's internal-symmetry content.

This is **minimal coupling**: matter couples to gauge via the single substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu^a T^a$. No separate Pauli term, no $F_{\mu\nu}F^{\mu\nu}\bar{\psi}\psi$ contact term, no non-derivative coupling. The substrate-level vertex is unique: the commitment primitive supplies one vertex per matter-gauge pair, and the vertex's bilinear structure is fixed by the rule-type composition rule.

**Sub-step C3a: Vertex-gauge-quotient invariance.** Under a gauge transformation $\psi \to U\psi$, $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$, the vertex transforms as:
$$
\bar{\psi}\,\gamma^\mu\,T^a\,\psi\,A_\mu^a \to \bar{\psi}\,U^{-1}\,\gamma^\mu\,U\,T^a\,U^{-1}\,U\,\psi\,A_\mu^a = \bar{\psi}\,\gamma^\mu\,T^a\,\psi\,A_\mu^a
$$
(using $U^{-1}T^a U$ rotation of generators absorbed by the corresponding rotation of $A_\mu^a$). The vertex is gauge-invariant.

**Sub-step C3b: Vertex-quotient is pullback of group-quotient.** The gauge-quotient at the vertex level is the pullback of the gauge-quotient at the group level (C2) through the bilinear coupling. The vertex structure preserves the group-quotient identification across all matter-gauge interactions.

Non-minimal-coupling alternatives would require multiple vertices, or non-bilinear vertex structures, neither of which is supplied by C5. Non-minimal couplings appear in *effective* field theories as integrated-out contributions from heavier sectors, but at the substrate level the rule-type interaction is minimal-coupling-only.

**Provenance**: P06 + P07 + P10 + Q.3 verdict + R-2 completion + R-3 Q.3-side.

### 7.6 (C4) Worldline: lightlike for $\sigma = 0$ excitations

The substrate-level $\tau_g$ rule-type produces excitations that propagate through the participation graph. The excitations carry a substrate-level energy-content parameter $\sigma$ (the bandwidth-signature functional from Paper #6, evaluated for the gauge rule-type).

**Sub-step C4a: $\sigma = 0$ excitations propagate on lightlike worldlines.** The substrate-level mass identification $m = \sigma/c^2$ (Paper #6) gives:
- $\sigma > 0$: massive excitations propagate on timelike worldlines.
- $\sigma = 0$: massless excitations propagate on lightlike worldlines (null geodesics in the emergent acoustic-metric continuum).

For the gauge sector, the form-level structural commitment is that $\tau_g$ admits $\sigma = 0$ excitations — the substrate-level photon, gluon, etc. The empirical content (photons are massless; gluons are massless before confinement) is consistent with this commitment.

**Sub-step C4b: Vertex ledger lifts to worldline ledger.** The vertex-anchored commitment ledger (C3) lifts onto worldline structure: each $\tau_g$ excitation traces a worldline through the participation graph, with commitment events occurring at specific loci on the worldline. The ordered sequence of commitment events $\{v_i\}$ on a worldline gives the excitation's history.

**Sub-step C4c: Second-quantization lifting.** Theorem 6 (canonical (anti-)commutation relations) supplies the second-quantization structure: the substrate admits a Fock-style excitation count for $\tau_g$. Each excitation is a quantum of the gauge field; multi-quantum states are constructed via the second-quantization machinery. For gauge fields (which are bosonic — Case-P rule-types per Paper #7), the canonical commutation relations apply.

**Provenance**: P13 + Q.7 verdict + Theorem 6 + R-1 + R-3 Q.7-side + R-5 partial.

### 7.7 (C5-C7) Vacuum sector: UV-finite kernel + three classes + strict non-committing + $B[v]$

The vacuum sector of $\tau_g$ requires substantive structural treatment, covering three of T17's clauses.

**Sub-step C5a: Vacuum kernel form (C5).** The no-excitation sector of $\tau_g$ carries a substrate-level fluctuation envelope — the vacuum kernel. Six structural constraints fix its form:

(i) **Non-vacuity**: the substrate is non-trivial in the vacuum sector; the kernel is not identically zero.

(ii) **UV-finiteness**: Theorem 7 (UV-FIN) supplies the substrate UV cutoff at $\ell_P$. The vacuum kernel is finite at all frequencies up to $\omega_c = c/\ell_P$; no regularization-dependent counterterms are needed.

(iii) **V1-form**: The vacuum kernel inherits the V1 finite-width structure (Theorem 8 / N1, Arc N). Explicitly,
$$
V_1^{(\tau_g)}(t) = \mathcal{V}_0^{(\tau_g)}\,\theta(t)\,e^{-t/\tau_{V1}}\,\psi(t/\tau_{V1})
$$
with $\tau_{V1}$ the V1 timescale and $\psi$ a substrate-derived profile function.

(iv) **Gauge-invariance**: the vacuum kernel is invariant under the gauge-quotient (C2). Specifically, the vacuum-kernel structure respects gauge transformations: $V_1^{(\tau_g)}$ transforms covariantly under local gauge transformations such that the gauge-invariant action remains well-defined.

(v) **Bandwidth additivity**: the vacuum kernel contributes additively to the substrate-level bandwidth content (Primitive P04).

(vi) **Stationarity**: in the absence of external perturbations, the vacuum kernel is stationary (time-translation invariant).

These six constraints jointly fix the form of the gauge-field vacuum kernel as a V1-form gauge-invariant fluctuation envelope, parallel to the gravity-sector V1 kernel from Arc N but specialized to the gauge sector via the Lie-algebra-valued structure of $A_\mu$.

**Sub-step C6a: Vacuum classification (C6).** The vacuum sector admits three structural classes on two orthogonal axes:

- **Axis 1: Background expectation value $\langle A_\mu\rangle_\mathrm{vac}$**. Either zero (no condensate) or nonzero (Higgs-class condensate).
- **Axis 2: Worldline support**. Either no worldlines in the vacuum (excitation-vacuum) or worldline structure in the vacuum (additional excitations).

The three admissible classes:

- **Class 1: Excitation-vacuum, no condensate.** $\langle A_\mu\rangle_\mathrm{vac} = 0$, no worldlines in vacuum. The minimal FORCED vacuum class — the natural ground state at substrate level.
- **Class 2: Background-vacuum.** $\langle A_\mu\rangle_\mathrm{vac} \neq 0$, no worldlines in vacuum. Inhomogeneous vacuum with nonzero gauge-field expectation; the structural locus of Higgs-style vacuum condensates.
- **Class 3: Mixed-vacuum.** Both nonzero $\langle A_\mu\rangle_\mathrm{vac}$ and worldlines in vacuum. The most general admissible class.

The **excitation-vacuum (Class 1)** is the substrate-level minimal FORCED class: it requires no additional structure beyond the V1 kernel. Classes 2 and 3 are admissible but require additional substrate content (Higgs sector for Class 2, multi-rule-type interactions for Class 3) inherited from the value layer.

**Sub-step C7a: Strict non-committing vacuum (C7).** The vacuum sector of $\tau_g$ is **strict non-committing**: no commitment events occur in the vacuum. This is forced by:

- **P06 + P07**: commitment events occur at loci with non-trivial participation content. The vacuum, by definition, has trivial participation content (or only the V1-kernel fluctuation envelope, which is below the commitment-event threshold).
- **P11**: commitment events require an anchor — a locus where the chain's participation participates non-trivially with the substrate. The vacuum sector provides no such anchor.

Strict non-commitment is a substrate-level structural fact about the gauge-rule-type vacuum sector.

**Sub-step C7b: Background functional $B[v;\tau_g]$.** Although the vacuum is strict non-committing, the **vacuum kernel contributes additively** to commitment rates in non-vacuum states. The contribution takes the form of a gauge-invariant background functional:
$$
\Gamma_\mathrm{global}[v;s] = \Gamma_\mathrm{excitation}[v;\tau_g,s] + B[v;\tau_g],
$$
where $\Gamma_\mathrm{global}$ is the global commitment rate at locus $v$ in state $s$; $\Gamma_\mathrm{excitation}$ is the rate from excitation-content; and $B[v;\tau_g]$ is the vacuum-kernel-mediated background contribution.

$B[v;\tau_g]$ inherits the V1-form gauge-invariance from C5: it is gauge-invariant under the gauge-quotient (C2), additive (P04), and V1-form (Theorem 8).

The structural form of $B[v;\tau_g]$ is forced; the specific amplitude is INHERITED from the V1 kernel's amplitude parameter $\mathcal{V}_0^{(\tau_g)}$.

**Provenance** (C5-C7): P02 + P04 + P06 + P07 + P10 + P11 + P13 + Theorem 7 + Theorem 8 + Q.8 verdict + R-3 Q.8-side + R-5 completion.

### 7.8 (C8) Unified gauge-quotient across all four channels

The gauge-quotient invariance — local symmetry — is the **interface property** of the rule-type $\tau_g$: the substrate does not distinguish between structurally-identical gauge configurations.

T17's clause C8 establishes that *all four channels* of $\tau_g$ — group structure, vertex, worldline, and vacuum — respect a **single unified gauge-quotient identification** under the gauge group of C2.

**Sub-step C8a: Group-quotient identification.** Under a local gauge transformation $U(u) \in G$, $A_\mu(u) \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$. Gauge-equivalent configurations are identified at the substrate level: the participation manifold of $\tau_g$ is modulo the gauge group action.

**Sub-step C8b: Vertex-quotient identification.** Under the same gauge transformation, the matter-gauge vertex transforms gauge-covariantly (C3a above): the vertex is invariant under the gauge action.

**Sub-step C8c: Worldline-quotient identification.** $\tau_g$ excitations propagating on lightlike worldlines (C4) transform covariantly under gauge transformations: the worldline structure is preserved, with the gauge phase along the worldline absorbed into the gauge-quotient identification.

**Sub-step C8d: Vacuum-quotient identification.** The vacuum kernel (C5) and background functional (C7) are gauge-invariant under the gauge group. The vacuum sector respects the same gauge-quotient.

**Sub-step C8e: Six-pair cross-channel audit.** All six pairs of channels (group-vertex, group-worldline, group-vacuum, vertex-worldline, vertex-vacuum, worldline-vacuum) are checked for consistency under the gauge-quotient. The Synthesis Memo 01 §4 audit (closed-arc inheritance from Arc Q) verifies all six pairs PASS: the unified gauge-quotient is well-defined across the four-channel structure.

That this quotient is *local* (with $U(u)$ varying from point to point) and not global (with $U$ position-independent) follows from the substrate-level locality of the participation graph (C1): channels at different loci are structurally independent, so polarity-redefinitions at different loci are also independent. A global-only symmetry would require the substrate to distinguish loci by their absolute polarity values, which violates the substrate-level translation invariance underwriting C3.

**Provenance**: P10 + Q.8 verdict + Synthesis Memo 01 §4 + R-2 + R-4.

### 7.9 (C9) Acyclic derivability + matter-rule-type internal-index content

**Sub-step C9a: Acyclicity of the derivation chain.** All eight content-clauses (C1-C8) trace exclusively to upstream items:
- Primitives P02-P13.
- Theorems 1-16 from Arc R (relativistic structure), Arc N (vacuum kernel), Arc Q form-level baselines (Theorems 5, 6, 7), and Arc U1-U5 + Born_Gleason + U2 (QM-emergence structural foundations).
- Q-substage verdicts (Q.1 + Q.2 + Q.3 + Q.7 + Q.8) closed in prior ED-program work.
- Refinements R-1 + R-2 FULL + R-3 FULL + R-4 + R-5 FULL.

**No downstream item is invoked.** The derivation does not use Arc M (the mass arc) or any downstream content. SFal-5 (the synthesis falsifier checking Arc M circularity) is dispatched: F-M8 (Arc M mass-form item) is NOT invoked anywhere in the T17 derivation; F-M8's promotion is a *consequence* of T17, not an input.

**Sub-step C9b: Matter-rule-type internal-index content.** The specific gauge group realized in nature — SU(3) for color, SU(2)×U(1) for electroweak — depends on the matter-rule-type internal-index content. Specifically:

- Quark-like matter rule-types carry an SU(3) color index → SU(3) gauge sector (QCD).
- Lepton-like matter rule-types carry an SU(2) weak-isospin index + U(1) hypercharge → SU(2)×U(1) electroweak gauge sector.
- All charged matter rule-types carry a U(1) electric-charge index → U(1) electromagnetic gauge sector (after electroweak symmetry breaking).

The internal-index content of matter rule-types is INHERITED from the value layer (the empirical content of the Standard Model). T17 forces the *form*: matter rule-types with internal indices induce gauge rule-types with corresponding gauge groups. The *specific* internal indices (and hence specific gauge groups) are empirical.

**Sub-step C9c: Promotion to FORCED-unconditional.** With C1-C8 derivable from upstream items + C9a acyclicity check, T17 is FORCED-unconditional at structural level. All twelve substage falsifiers and all six synthesis falsifiers (from prior arc-Q closure work) are NOT TRIGGERED.

**The composite result of §§7.1-7.9**: T17's nine clauses are all forced by the substrate. The gauge structure of standard physics — including local symmetry, gauge potentials, curvature, minimal coupling, and the non-Abelian-capable group structure — is a substrate-level forcing theorem with explicit primitive-level provenance.

---

## 8. Exclusion Arguments

### 8.1 A1 — No gauge fields

A substrate satisfying C6 (rule-type primitive supplying multiple rule-types $\{\tau_m, \tau_g, \ldots\}$) but lacking $\tau_g$ contradicts C6: the rule-type primitive supplies the gauge rule-type as one element of its class. Equivalently, polarity transport on the participation manifold (§7.3) cannot be defined without a connection, and the connection *is* the gauge potential — its existence is structurally tied to transport consistency. Empirically, observed gauge interactions (EM, weak, strong) confirm the substrate's non-trivial rule-type class.

### 8.2 A2 — Global-only symmetry

A global-only symmetry would require all polarity-redefinitions across the participation manifold to be tied together by a single $U \in U(1)$ (or non-Abelian analog). This contradicts C1's structural independence of channels at distinct loci: there is no substrate-level mechanism for enforcing a global tying of polarity values across the manifold. The locality of polarity is forced by the locality of the participation graph.

### 8.3 A3 — Non-connection-based transport

If polarity transport were path-independent (a global phase) or path-dependent but not satisfying the composition law $U_{\gamma_1 \circ \gamma_2} = U_{\gamma_1} U_{\gamma_2}$, then transport around closed loops would fail to compose consistently. Bandwidth-preserving (C2), continuous (C4), unitary transport on a complex carrier (C7/Paper #1) forces the composition law; the transport rule is a connection in the standard differential-geometric sense.

### 8.4 A4 — Non-curvature-based field strength

If the observable field strength were defined other than as the commutator $[D_\mu, D_\nu]$, gauge-invariance would fail: the bare derivative $\partial_\mu A_\nu$ is not gauge-invariant; the bilinear $A_\mu A^\mu$ transforms inhomogeneously. The unique gauge-invariant (up to covariant transformation) object built from $A_\mu$ at first order in derivatives is the commutator. The substrate-level requirement that observables respect the gauge-quotient invariance (C8) forces the field strength to be the curvature.

### 8.5 A5 — Non-minimal coupling

The vertex-anchored commitment primitive (C5) supplies a single vertex per matter-gauge rule-type pair. Non-minimal couplings would require either additional substrate-level vertices (violating C5's structural single-vertex content per rule-type pair) or non-bilinear vertex structure (violating the rule-type composition rule of C6, which produces bilinear matter-gauge couplings).

Non-minimal couplings observed in effective field theories (e.g., Pauli moments at low energies in heavy-quark physics) arise from integrated-out heavy sectors and are not substrate-level commitments. At the substrate level, the coupling is minimal.

### 8.6 A6 — Real or quaternionic gauge structure

Real-valued gauge potentials lack the phase content required by polarity transport (C3); the substrate's $U(1)$ polarity primitive cannot be carried by real-valued transport. Paper #1's exclusion of real-valued amplitude carriers applies directly: real-valued $A_\mu$ fails to faithfully represent the polarity-transport content.

Quaternionic gauge potentials would carry $SU(2)$-or-larger angular structure at the carrier level, exceeding what polarity supplies. Paper #1's exclusion of quaternionic carriers (no primitive-level basis for the $U(1) \subset SU(2)$ embedding choice; surplus angular content unsupported by the substrate) applies. Non-Abelian gauge structure at the *group* level is permitted; non-quaternionic *carriers* are required.

### 8.7 A7 — Non-U(1)/non-SU(n) phase transport

Discrete gauge groups ($\mathbb{Z}_n$ at the gauge level) fail the continuity requirement of C4: polarity transport along a continuous path must produce a continuous family of unitary transformations, which discrete groups cannot supply.

Non-compact gauge groups (e.g., $SL(n, \mathbb{R})$) fail the Killing-form non-degeneracy required for the bilinear gauge-invariant action $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ to be positive-definite. Non-positive-definite actions violate the bandwidth-non-negativity (C2) that propagates to the gauge sector's vacuum-kernel structure.

Non-Lie group structures (e.g., quasigroups, loops) fail the associativity required for transport-rule composition; the connection construction of §7.3 requires Lie-algebra structure.

The admissible class is therefore compact simple Lie groups (and their direct products), which is exactly the class of standard gauge theories.

### 8.8 A8 — Non-vertex-anchored interactions

Distributed matter-gauge interactions across multiple loci would require either (i) non-local substrate-level structure (violating C1's local channel structure) or (ii) additional commitment-event vertices (violating C5's single-vertex commitment primitive). The substrate forces interactions to be vertex-anchored.

### 8.9 A9 — Massive gauge excitations only

A substrate admitting only massive gauge excitations (no $\sigma = 0$ excitations) would require an additional structural commitment forbidding the $\sigma = 0$ slot. The substrate's mass-form structure (Paper #6) admits $\sigma = 0$ as a structurally accessible solution; forbidding it would require a primitive-level mass-gap that the substrate does not supply.

Empirically: photons are massless (consistent with substrate-level $\sigma = 0$). Higgs-mechanism-style mass generation operates *downstream* of the substrate forcing — gauge bosons acquire mass through coupling to a Higgs field, not through a substrate-level prohibition of $\sigma = 0$.

### 8.10 A10 — Non-UV-finite vacuum kernel

A divergent vacuum kernel would require regularization-dependent counterterms, contradicting the substrate's UV-finiteness (Theorem 7). The substrate has a fundamental UV cutoff at $\ell_P$; vacuum kernels respect this cutoff structurally. Non-UV-finite alternatives are excluded by C8 (Theorem 7 inheritance).

### 8.11 B1, B2 — Classical electromagnetism / Yang-Mills as postulate

Maxwell's equations and the Yang-Mills construction are taken as fundamental in the postulate-based formulations. Under the substrate-conditions test, these are *downstream* of the forcing chain: the gauge-field rule-type $\tau_g$ with its structural content (§7) produces Maxwell or Yang-Mills as the dynamical content. They are not alternative substrate-level commitments; they are consequences of the substrate-level rule-type structure.

### 8.12 B3 — Fiber-bundle gauge theory as assumption

The fiber-bundle formalism is a *reformulation* of standard gauge theory in differential-geometric language. The principal $G$-bundle, the group $G$, and the connection form are mathematical objects that ED's forcing chain *produces*: the participation manifold acquires a connection structure under polarity transport (§7.3); the group $G$ is the rule-type's gauge group (inherited from value-layer); the bundle structure is the geometric expression of the rule-type's interface property.

Fiber-bundle theory is therefore the appropriate mathematical *language* for the forced result, not an alternative to it.

### 8.13 B4 — Emergent gauge fields from condensed matter

Spin-liquid and dimer-model gauge fields are emergent at long wavelengths from non-gauge microscopic Hamiltonians. Under the substrate-conditions test, these systems are *higher-level* effective descriptions: the microscopic Hamiltonian itself is a participation-graph realization at the substrate level, and the emergent gauge field is a coarse-grained signature of a substrate-level rule-type that becomes visible only at long wavelengths.

Emergent gauge theory and substrate-level gauge theory are therefore consistent rather than competing: the substrate forces the rule-type structure; condensed-matter realizations exhibit different specific gauge groups (e.g., $\mathbb{Z}_2$ in some spin liquids) than the Standard Model. The non-Abelian-capable group structure admits both.

### 8.14 B5 — Hidden-variable gauge-like models

Hidden-variable formulations reproducing gauge predictions via non-local hidden variables do not derive the gauge structure from a substrate; they postulate it alongside hidden-variable supplementation. Under the substrate-conditions test, these are downstream interpretations of the forced gauge-field structure (analogously to Bohmian mechanics being downstream of the forced Schrödinger equation in Paper #4). Not in the alternative-encodings space.

### 8.15 B6 — Nonlocal gauge potentials

Action-at-a-distance reformulations (Wheeler-Feynman-style absorber theories, certain Aharonov-Bohm interpretations) retain observable predictions but reject the local-potential ontology. Under the substrate-conditions test, these are reformulations within the same equivalence class of theories that ED forces: the gauge potential is a substrate-level participation measure with local structure; observable predictions match because both formulations sit in the same gauge-quotient class. Nonlocal reformulations are not substrate-level alternatives; they are equivalent descriptions of the forced structure.

### 8.16 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 no gauge fields | C6 | Rule-type primitive supplies $\tau_g$ as element of the rule-type class. |
| A2 global-only symmetry | C1 | Channel locality forces local polarity-redefinition independence. |
| A3 non-connection transport | C2, C4 | Bandwidth-preserving continuous unitary transport satisfies the composition law. |
| A4 non-curvature field strength | C8 gauge-quotient | Only the commutator is gauge-invariant at first derivative order. |
| A5 non-minimal coupling | C5 | Vertex-anchored commitment supplies a single bilinear vertex per matter-gauge pair. |
| A6 real/quaternionic carrier | C3 (Paper #1) | Excluded at carrier level: real fails phase content, quaternionic has surplus $SU(2)$ structure. |
| A7 non-U(1)/non-SU(n) groups | C2, C4, §7.2 Jacobi | Discrete fails continuity, non-compact fails Killing positivity, non-Lie fails associativity. |
| A8 non-vertex-anchored | C1, C5 | Local channel structure + single-vertex commitment forbid distributed interactions. |
| A9 only massive gauge | Paper #6 mass-form | $\sigma = 0$ structurally accessible; no primitive supplies mass-gap prohibition. |
| A10 non-UV-finite vacuum | Theorem 7 (UV-FIN) | Substrate UV cutoff at $\ell_P$ forces finite kernel. |
| B1 classical EM postulate | not in space | Downstream of forced rule-type structure; consequence rather than alternative. |
| B2 Yang-Mills postulate | not in space | Same as B1 with non-Abelian group; downstream consequence. |
| B3 fiber-bundle gauge theory | reformulation | Mathematical language for the forced result, not an alternative substrate. |
| B4 emergent gauge fields | not in space | Higher-level coarse-grained signature of substrate-level rule-type. |
| B5 hidden-variable models | not in space | Downstream interpretation of forced gauge structure. |
| B6 nonlocal gauge potentials | reformulation | Equivalent description in the same gauge-quotient class. |

**The gauge-field-as-rule-type structure (T17) is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard gauge field theory: any observed violation of minimal coupling, local gauge invariance, or the commutator-defined field strength.

Specific constraints:

- **Anomalous magnetic moments**: precision measurements of the electron $g - 2$ and muon $g - 2$ agree with QED to ~$10^{-12}$ relative precision (electron) and ~$10^{-9}$ (muon), with all observed contributions accounted for by minimal-coupling QED + higher-order radiative corrections.
- **Tests of local U(1) gauge invariance**: experimental bounds on photon mass ($< 10^{-18}$ eV) and on possible Lorentz-violating photon couplings constrain gauge-invariance violations to extraordinary precision.
- **Aharonov-Bohm experiments**: the holonomy structure of gauge transport (§7.4) is directly measured in AB-type interference experiments; observed phase shifts agree with $\exp(i\oint A_\mu dx^\mu)$.
- **Non-Abelian gauge tests**: precision tests of the electroweak sector (W and Z masses, $\sin^2\theta_W$ measurements, $W$ helicity in pion decay) constrain non-Abelian gauge structure to high precision.
- **Vacuum-kernel-mediated B[v] background**: in principle, the substrate-derived background functional $B[v;\tau_g]$ contributes to vertex-anchored commitment rates. Detection of $B[v]$ contributions in precision measurements would confirm §7.7 directly. Currently a speculative empirical target.

If any of these were experimentally violated — if non-minimal coupling, broken local invariance, or non-commutator field strengths were observed — the substrate-level forcing would be refuted along with standard gauge theory.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C9 (channel-primitive participation graph, bandwidth additivity, $U(1)$ polarity, time homogeneity, vertex-anchored commitment, rule-type primitive, Papers #1-#4 inherited, Theorems 1-16 inherited, no gauge structure as input) but supporting no gauge-field rule-type, or supporting one with non-curvature field strength, or non-minimal coupling, or non-local symmetry, or a divergent vacuum kernel, that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists; each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures of the present forcing:

**Electromagnetism.** The Maxwell equations $\partial_\mu F^{\mu\nu} = J^\nu$ and $\partial_{[\rho} F_{\mu\nu]} = 0$ follow from the variational principle applied to the gauge-invariant action $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} + J^\mu A_\mu$ on the substrate-derived gauge potential. Every electromagnetic experiment — from Coulomb's law to laser interferometry to synchrotron radiation — tests the resulting dynamics.

**Yang-Mills.** The non-Abelian gauge sector of the Standard Model — SU(3) QCD for strong interactions, SU(2)×U(1) for electroweak — is realized as the substrate-level rule-type structure with the value-layer-inherited specific gauge group. Every hadron-collider experiment, every test of QCD running coupling, every electroweak precision measurement, tests this realization.

**Berry phase.** Holonomy around closed loops in parameter space — the geometric Berry phase — is the substrate-level signature of the gauge connection in adiabatic quantum mechanics. AB experiments, molecular Berry-phase measurements, and topological-phase experiments in condensed matter test the substrate-derived connection structure.

**Arc M F-M8 cascade.** T17 closure unblocks Arc M's F-M8 mass-form item: the τ_g-mediated mass-form contribution via the V1 vacuum kernel is now substrate-grounded. The promotion of F-M8 from FORCED-conditional to FORCED-via-T17 is a direct downstream consequence.

---

## Appendix A — Derivation Chain and Glossary

### A.1 Connection from polarity transport

Polarity (C3) is a $U(1)$-valued angular variable on each channel at each locus. Define the parallel-transport operator $U_\gamma: \mathcal{H}_u \to \mathcal{H}_{u'}$ along a smooth path $\gamma$ from $u$ to $u'$ on the participation manifold. Three substrate-level constraints:

1. **Unitarity** (from C2 bandwidth preservation + Paper #3 inner product): $U_\gamma^\dagger U_\gamma = \mathbb{1}$.
2. **Continuity** (from C4 time homogeneity + spatial homogeneity): $\gamma \mapsto U_\gamma$ continuous in path topology.
3. **Composition** (from path concatenation $\gamma_1 \circ \gamma_2$): $U_{\gamma_1 \circ \gamma_2} = U_{\gamma_1} U_{\gamma_2}$.

These constraints define a connection on the participation manifold. For an infinitesimal path $u \to u + dx^\mu$:
$$
U_{u \to u + dx} = \mathbb{1} + ig A_\mu(u) dx^\mu + O(dx^2),
$$
with $A_\mu(u)$ a Lie-algebra-valued one-form — the **gauge potential**. Unitarity at infinitesimal order requires $A_\mu^\dagger = A_\mu$ (Hermitian connection). Path-dependence at second order produces the curvature derived in A.2.

### A.2 Curvature from commutator of transports

Compare two paths from $u$ to $u + dx + dy$: (i) $u \to u + dx \to u + dx + dy$, (ii) $u \to u + dy \to u + dx + dy$. The transports are:

(i) $U_2^{(2)} U_1^{(1)} = [\mathbb{1} + igA_\mu(u + dx)dy^\mu] [\mathbb{1} + igA_\nu(u)dx^\nu]$
(ii) $U_2^{(1)} U_1^{(2)} = [\mathbb{1} + igA_\nu(u + dy)dx^\nu] [\mathbb{1} + igA_\mu(u)dy^\mu]$

Subtracting at second order:
$$
U_2^{(2)} U_1^{(1)} - U_2^{(1)} U_1^{(2)} = ig\,[\partial_\mu A_\nu - \partial_\nu A_\mu + ig(A_\mu A_\nu - A_\nu A_\mu)]\,dx^\nu dy^\mu = ig F_{\mu\nu} dx^\nu dy^\mu,
$$
with
$$
F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu].
$$
Equivalently, $F_{\mu\nu} = (1/ig)[D_\mu, D_\nu]$ with $D_\mu = \partial_\mu + igA_\mu$. The field strength is the curvature of the connection — the obstruction to commuting infinitesimal transports.

### A.3 Killing-form / Jacobi closure — Cartan classification

The compact simple Lie algebras are classified by Cartan (1894) into nine series / exceptional types:
- Classical series $A_n$ = $\mathfrak{su}(n+1)$ for $n \geq 1$.
- Classical series $B_n$ = $\mathfrak{so}(2n+1)$ for $n \geq 2$.
- Classical series $C_n$ = $\mathfrak{sp}(2n)$ for $n \geq 3$.
- Classical series $D_n$ = $\mathfrak{so}(2n)$ for $n \geq 4$.
- Exceptional types: $E_6$, $E_7$, $E_8$, $F_4$, $G_2$.

Each has a non-degenerate Killing form (positive-definite up to sign convention) and satisfies the Jacobi identity. Direct products of these algebras (with possibly Abelian U(1) factors) form the admissible class for gauge structure at the substrate level.

The Standard Model's SU(3)×SU(2)×U(1) is one specific direct-product realization: SU(3) ∈ $A_2$, SU(2) ∈ $A_1$, U(1) Abelian. Whether this specific combination is forced or could be replaced by other admissible combinations (e.g., grand-unified $SU(5)$, $SO(10)$, $E_6$) is empirical content not committed by T17.

### A.4 Minimal coupling from vertex-anchored commitment

The substrate-level commitment primitive (C5) is vertex-anchored: each commitment event occurs at a specific locus. The matter-gauge interaction enters through the substrate-level vertex, which is structurally a single bilinear coupling between matter and gauge participation measures.

In the relativistic case, the matter rule-type $\tau_m$ has Dirac-spinor structure (forced by the ED program's Arc R), and the matter-gauge vertex is $\bar{\psi}\gamma^\mu T^a \psi A_\mu^a$. Substituting into the matter Schrödinger / Dirac equation gives the minimal-coupling substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu^a T^a$.

In the non-relativistic case (Paper #4 scope), the matter-gauge vertex enters the Hamiltonian as $\hat{H} \to \hat{H} + g\hat{A}_\mu \hat{j}^\mu$ with $\hat{j}^\mu$ the matter current. The vertex is unique: C5 supplies a single vertex per matter-gauge rule-type pair, and the bilinear structure is fixed by rule-type composition.

### A.5 Glossary

- **$A_\mu$ (gauge potential).** The participation measure of the gauge rule-type $\tau_g$; a Lie-algebra-valued one-form on the participation manifold.
- **$B[v;\tau_g]$ (background functional).** Gauge-invariant V1-form background contribution to commitment rates from the vacuum kernel. Form FORCED; amplitude INHERITED.
- **Bandwidth $b_K(u)$.** Primitive non-negative real-valued substrate quantity on each channel.
- **Commutator.** $[A, B] = AB - BA$, the antisymmetric product of operators.
- **Compact simple Lie group.** A Lie group that is compact, connected, and has no non-trivial closed normal subgroups. U(1) (Abelian), SU(2), SU(3), and the exceptional groups are examples.
- **Connection.** A rule for parallel transport along paths on the participation manifold; equivalently, the gauge potential $A_\mu$.
- **Covariant derivative.** $D_\mu = \partial_\mu + igA_\mu^a T^a$; the gauge-invariant derivative replacing $\partial_\mu$.
- **Curvature.** The 2-form $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$; the commutator of covariant derivatives.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional structural commitments.
- **Gauge group $G$.** The compact simple Lie group acting on the matter rule-type's internal indices. U(1), SU(2), SU(3) in the Standard Model.
- **Gauge potential $A_\mu$.** See "$A_\mu$".
- **Gauge-quotient.** Equivalence class of gauge configurations $A_\mu \sim A_\mu - g^{-1}(\partial_\mu U)U^{-1}$; the substrate identifies all members of the same class.
- **Holonomy.** Phase factor accumulated by transport around a closed loop: $\exp(i\oint A_\mu dx^\mu)$ for Abelian, path-ordered exponential for non-Abelian.
- **INHERITED.** Quantitative content (specific gauge group, coupling values, kernel parameters, $B[v]$ amplitude) not derived in this paper.
- **Jacobi identity.** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$; characterizes Lie algebras.
- **Killing form.** A bilinear form on a Lie algebra, $K(X, Y) = \text{tr}(\text{ad}_X \text{ad}_Y)$; non-degenerate on semisimple Lie algebras.
- **Minimal coupling.** Matter-gauge interaction via $\partial \to D$; structural single-vertex coupling.
- **Participation measure.** Complex-valued amplitude carrier on each channel (Paper #1).
- **Polarity $\pi_K(u)$.** $U(1)$-valued angular primitive on each channel at each locus.
- **Rule-type.** Substrate primitive class of channel structure; matter and gauge are distinct rule-types.
- **Strict non-committing vacuum.** Vacuum sector where no commitment events occur. Substrate-level structural fact about gauge-rule-type vacuum.
- **T17 (Theorem 17).** Gauge-Field-as-Rule-Type theorem with nine clauses C1-C9; the main content of this paper.
- **V1 kernel.** Substrate-level finite-width spatial vacuum kernel (Theorem N1, Arc N).
- **Vertex.** A locus on the participation graph at which a commitment event occurs; the substrate-level "interaction point."
- **Vertex-anchored.** Property of commitment events: each occurs at a specific locus, with the rule-type's contribution entering through that vertex.

### A.6 Source-repository citations (for ED-internal readers)

- `papers/Gauge_Fields_Theorem_17/paper_gauge_fields_theorem_17.md` — publication-grade T17 paper (predecessor genre).
- `arcs/arc-Q/19_synthesis_memo_02_theorem_17.md` — Arc Q synthesis memo establishing T17 as FORCED-unconditional with full C1-C9 derivation.
- `arcs/arc-Q/17_synthesis_memo_00_scoping.md` and `18_synthesis_memo_01_global_integration.md` — synthesis prerequisites.
- `arcs/arc-Q/arc_q_synthesis.md` — Arc Q overview.
- `arcs/arc-Q/02_Q2_memo_01_non_abelian.md` and `04_Q2_memo_03_verdict.md` — Q.2 substage (non-Abelian gauge structure, C2 forcing).
- `arcs/arc-Q/06_Q3_memo_01_vertex_minimal_coupling.md` — Q.3 substage (vertex-anchored minimal coupling, C3 forcing).
- `arcs/arc-Q/10_Q7_memo_01_lightlike_worldline.md` and `12_Q7_memo_03_verdict.md` — Q.7 substage (lightlike worldlines, C4 forcing).
- `arcs/arc-Q/14_Q8_memo_01_zeropoint_vacuum_classification.md` and `16_Q8_memo_03_verdict.md` — Q.8 substage (vacuum classification + commitment, C5-C7 forcing).
- `walkthroughs/from_primitives_to_gauge_fields.md` — public-facing walkthrough.
- `theorems/T17.md` — theorem-level index entry; status FORCED-unconditional, ratified 2026-04-27.

These are *not* required reading for the present paper.

---

*End of Paper #5.*
