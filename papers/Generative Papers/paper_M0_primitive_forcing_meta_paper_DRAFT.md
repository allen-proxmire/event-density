# Why the ED Substrate Primitives Are Themselves FORCED

**Paper #M0 (Meta-Paper) of the Event Density Forcing Series — DRAFT**

**Author:** Allen Proxmire
**Status:** Draft — opening sections only. Sections 6–10 (Constructive Necessity, Exclusion Arguments, Falsifiers, Appendix) to be developed.
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Meta-Paper position
**Genre:** Meta-forcing paper. Standalone. Cold-reader accessible. Addresses the displaced-postulate question that the Wave-1 and Wave-2 Forcing Papers (Papers #1–#19) leave open.

---

## Abstract

The Event Density (ED) Forcing Papers (#1–#19) establish that, *given* a small set of substrate primitives, every load-bearing structure of standard non-relativistic and relativistic quantum mechanics, the gauge structure, the Hamiltonian / mass framework, Newton's law of gravitation, the MOND-class transition acceleration $a_0$, the slope-4 baryonic Tully-Fisher relation, the substrate-level Hawking spectrum, black-hole architecture, and the kernel-level arrow of time are forced — i.e., admit no consistent alternative on a substrate satisfying the named primitives. This leaves an unforced root: *why those primitives, and not others?* This meta-paper opens the program-level investigation of upstream forcing for the load-bearing substrate primitives — specifically, the four-band partition (P04 §1.5), the $U(1)$-valued polarity (P09), bandwidth additivity (P04), the discrete-channel adjacency structure (P03 + P07), commitment irreversibility (P11), and the V1/V5 kernel rule-types. Five candidate forcing routes are identified: **symmetry-minimality**, **operational adequacy**, **compositional closure**, **information-theoretic constraints**, and **category-theoretic necessity**. The paper provides the framing, claim, scope, vocabulary, substrate-class definitions, and roadmap for the full forcing argument to be developed in sections 6–10 (constructive necessity, exclusion arguments, falsifiers, appendix). The methodology mirrors the Wave-1 and Wave-2 papers: enumerate alternatives, exclude each by an explicit structural argument, and identify the unique survivor. The honest expectation: not every primitive will turn out to be fully upstream-forced from a deeper structural layer. Some will reduce to "minimum operational adequacy" + "necessary for compositional closure" — which is itself a defensible structural position, replacing displaced postulates with explicitly named structural commitments. The paper's role in the ED program is to convert the QM-reconstruction face of ED from "substrate-vocabulary variant of operational reconstruction" to "substrate ontology with upstream-forced primitives" — eliminating the displaced-postulate critique without overclaim.

---

## 1. Framing

### 1.1 The unforced root left by Forcing Papers #1–#19

Each of the 19 forcing papers in the Event Density (ED) program closes by stating that its result is conditional on the substrate satisfying a small set of named primitives. Paper #1 forces the participation measure *given* P04 (bandwidth) + P09 (polarity) + P03 + P07 (channel structure). Paper #2 forces the Born rule *given* Paper #1's result + P11 (commitment with environmental phase-randomization). Paper #9 forces Newton's $G$ + $a_0$ + BTFR *given* Papers #1–#8 + holographic counting + decoupling-surface dipole projection + stability-landscape primitive.

Each conditional is honest. Each is also structurally incomplete. *Why those primitives?* Why does the substrate have a $U(1)$-valued polarity rather than a $\mathbb{Z}_n$-valued or $\mathbb{R}$-valued one? Why does bandwidth partition into four bands rather than three or five? Why does the substrate have commitment with environmental phase-randomization on a uniform $U(1)$ distribution, rather than a non-uniform distribution? Why retarded V1 kernel and not advanced or symmetric (already addressed in Paper #19, but conditional on P11 which is itself a primitive)?

A reviewer reading the Wave-1 and Wave-2 papers in honest mode arrives quickly at this question. The papers *individually* eliminate the postulates of standard physics (state space, dynamics, measurement, composition, gauge structure, gravitational coupling, BH thermodynamics, arrow of time) — but they replace them with substrate primitives that are themselves unforced. **The displaced-postulate critique**, which targets the QM-reconstruction face most directly, applies in this form: ED has relocated postulates from the QM level to the substrate level, but has not derived the substrate from a deeper layer.

The present paper is the program's response to this critique. The response has two parts:

1. **Identify the load-bearing primitives.** Which primitives are doing the forcing work, and which are auxiliary or derived from others? The Forcing Series Phase-1 revisions (REVISIONS_PHASE1_abstracts_claims_scope.md) make this explicit per paper. The present paper consolidates the inventory.

2. **Attempt upstream forcing for each load-bearing primitive.** For each primitive, enumerate candidate alternatives, attempt to exclude each by structural argument, and identify the unique (or smallest equivalence class of) survivor. Where full upstream forcing is not achievable, name the structural commitment honestly and locate it as a "structural commitment of minimum operational adequacy" or similar honest-residual category.

The methodological move is the same one used throughout the Forcing Series — enumerate, exclude, identify the survivor — but applied to the substrate's primitives themselves rather than to a downstream structure on top of them.

### 1.2 The puzzle

The deeper question: *can a substrate have less primitive structure than ED's current set, while still supporting the program's downstream results?*

A program seeking to derive the substrate from a deeper layer needs:

1. **An audit of which primitives are load-bearing.** Some primitives may be derivable from others. The audit phase identifies the minimal set of *independently load-bearing* primitives.

2. **A class of admissible alternative substrates.** For each load-bearing primitive, what alternatives could a substrate adopt? Real-valued polarity instead of $U(1)$? Discrete cyclic polarity ($\mathbb{Z}_n$) instead of continuous? Three-band partition instead of four? Non-additive bandwidth? No commitment primitive?

3. **An exclusion argument per alternative.** Why does each alternative fail to support the downstream forcing chain? Does it violate a meta-constraint (e.g., compositional closure of the substrate's category-theoretic structure)? Does it produce a substrate that cannot recover known physics (e.g., the Born rule's quadratic form, or Lorentz invariance)?

4. **A honest accounting of irreducible residue.** If full upstream forcing fails for some primitive, what is the honest structural commitment that remains? "Minimum operational adequacy"? "Necessary for compositional closure"? "Empirically necessary to recover known physics"? Each of these is a defensible structural position, more honest than displaced postulate.

The present paper identifies the load-bearing primitives, the candidate forcing routes, and the roadmap. Full execution of sections 6 (Constructive Necessity), 7 (Exclusion Arguments), 8 (Falsifiers), and 9 (Appendix) is the subject of subsequent work.

### 1.3 What this paper does

This meta-paper:

1. **Identifies the load-bearing primitives** (§5 Substrate Class $\{C^*\}$, the *meta-substrate* on which the forcing argument operates).
2. **Names five candidate forcing routes** for upstream derivation of those primitives:
   - **Symmetry-minimality** (Route A)
   - **Operational adequacy** (Route B)
   - **Compositional closure** (Route C)
   - **Information-theoretic constraints** (Route D)
   - **Category-theoretic necessity** (Route E)
3. **Provides a roadmap** for full forcing argument development in sections 6–10.

**Honest framing.** This paper does *not* claim that all load-bearing substrate primitives can be fully upstream-forced. Some will likely reduce to "minimum operational adequacy" (e.g., the substrate must support enough structure to recover known physics, and the smallest such substrate is the one ED adopts). That is a defensible position — substantially stronger than displaced postulate — and the present paper makes that residue explicit rather than hiding it.

**Series context.** This meta-paper sits at position #M0 in the Forcing Series, upstream of all Wave-1 and Wave-2 Forcing Papers. It closes (or honestly bounds) the displaced-postulate critique by treating the substrate primitives as themselves the object of structural analysis. The methodological pattern — enumerate alternatives, exclude each, identify the survivor — applies recursively to the substrate.

---

## 2. Claim

> **Meta-Forcing Claim (Provisional, Sections 6–10 To Be Developed).** Let any meta-substrate satisfy the conditions $\{C^*\}$ stated in §5 — *in particular: a generic primitive-level substrate-ontology framework with no specific commitment to any particular primitive structure*. Then the load-bearing primitives of the Event Density substrate ($P04, P09, P03 + P07, P11, P13, P06$, four-band partition, V1 retarded kernel, V5 cross-chain correlation kernel) are, by combinations of the five candidate routes:
>
> - **Route A (Symmetry-Minimality).** The substrate's primitive symmetry content is forced as the *minimal* primitive-level symmetry structure supporting downstream forcing of Galilean (non-relativistic) + Poincaré (relativistic) covariance + the four-postulate QM unification.
> - **Route B (Operational Adequacy).** Each load-bearing primitive is forced as *necessary* for the substrate to recover empirically observed physics at the downstream level. Removing any one primitive leaves the substrate incapable of recovering at least one well-established empirical fact.
> - **Route C (Compositional Closure).** The substrate's primitive structure is forced as *closed* under the category-theoretic compositional operations the program requires (channel-graph composition, bandwidth-allocation across orthogonal partitions, polarity-transport along edges).
> - **Route D (Information-Theoretic Constraints).** Bandwidth-additivity, polarity-as-$U(1)$, and the four-band partition each satisfy information-theoretic constraints (Shannon-Khinchin entropy axioms, single-shot information capacity bounds, the Holevo bound) that exclude alternative primitive structures violating those constraints.
> - **Route E (Category-Theoretic Necessity).** The substrate's primitive structure realizes a specific monoidal-category-theoretic structure (channels as objects, polarity-transport as morphisms, four-band partition as biproduct structure) whose forcing is examined via the Coecke-Kissinger / categorical-QM framework.
>
> Whether full forcing is achievable or whether some primitives reduce to "honest structural commitments of minimum operational adequacy" is the subject of Sections 6–10. The present paper provides the framing and roadmap; the exclusion arguments are pending.
>
> *The meta-substrate primitives in $\{C^*\}$ are themselves load-bearing inputs to this meta-paper. The meta-paper does not claim derivation-from-nothing; it claims to push the unforced root one level deeper than the Forcing Series Papers #1–#19.*

---

## 3. Scope

### 3.0 Meta-Substrate Inputs (load-bearing, not derived in this paper)

The meta-paper's forcing argument is conditional on the following meta-substrate-level structural commitments:

- **The existence of a substrate.** That there is a pre-quantum primitive-level structural layer with channels, primitives, kernel rule-types. The meta-paper does not derive substrate-existence from a deeper "pre-substrate" layer.
- **The mathematical infrastructure** of group theory (especially Lie groups + their classification), category theory (especially monoidal categories), information theory (Shannon-Khinchin axioms + capacity bounds), and standard real analysis. Treated as background mathematics.
- **The structural goal of recovering empirically observed physics.** The meta-forcing's "Route B" (Operational Adequacy) is conditional on the assumption that the substrate must support derivation of known physics. This is a normative-empirical structural commitment, not derived from any deeper principle.

**Honest reading.** The meta-paper does not eliminate all unforced roots. It pushes the unforced root one level deeper — from "substrate primitives are postulated" to "the meta-substrate's structural-commitment-to-recover-empirical-physics is taken as given, and the primitives are forced by exclusion arguments within that context."

### 3.1 What is FORCED (or scoped for forcing in §§6–10)

- **The minimal set of independently load-bearing substrate primitives.** Section 5 will identify these; the present opening sections sketch the inventory.
- **For each load-bearing primitive: the unique (or smallest equivalence class of) survivor under one or more of Routes A–E.** Sections 6–8 will develop the exclusion arguments.
- **The reduction of any "remaining" displaced postulates to honest structural-commitment categories** ("minimum operational adequacy," "necessary for compositional closure," "empirically necessary to recover known physics").

### 3.2 What is INHERITED

- **Numerical values of substrate-level constants** ($\ell_P$, the V5 cutoff frequency, the four-band partition's specific allocation ratios). These remain value-layer empirical inputs.
- **Specific identification of substrate primitives with empirical observables.** That bandwidth-additivity corresponds to observed conservation laws, that polarity-as-$U(1)$ corresponds to electromagnetic gauge structure, etc., is the value-layer correspondence treated throughout the Forcing Series.
- **The mathematical infrastructure** of group theory, category theory, information theory.

### 3.3 What is OUT OF SCOPE

- **Derivation of the meta-substrate itself.** The meta-paper does not derive "why is there a substrate at all" from any deeper layer. This is the recursion-stopping commitment.
- **Derivation of mathematics from non-mathematical primitives.** Group theory, category theory, information theory, real analysis are taken as background mathematics, not derived in the present paper.
- **Derivation of the empirical-recovery goal.** Route B's "the substrate must support known physics" is a structural-normative commitment, not derived.
- **Resolution of specific downstream-physics open problems** (e.g., why three generations of fermions, why specific Standard Model gauge group $SU(3) \times SU(2) \times U(1)$, why three spatial dimensions at the cosmological scale). These remain downstream content, separate from substrate-primitive forcing.

---

## 4. Key Vocabulary

For the reader new to the Event Density (ED) program:

- **Substrate.** The pre-quantum primitive structural layer on which ED is built. Not a Hilbert space, not a manifold, not a field theory. A discrete graph-like structure with primitive scalar, set-valued, and relational quantities.
- **Substrate primitive.** A structural commitment at the substrate level — bandwidth, polarity, channels, commitment events, four-band partition, kernel rule-types, etc. The substrate has 13 numbered primitives (P01–P13) plus the four-band partition (P04 §1.5) and the V1/V5 kernel structure.
- **Load-bearing primitive.** A primitive whose removal or modification breaks at least one downstream Forcing Theorem in Papers #1–#19. The Phase-1 revisions identify load-bearing primitives per paper; this meta-paper consolidates the union.
- **Auxiliary primitive.** A primitive that is derivable from other primitives or is not load-bearing for any Forcing Theorem. The audit phase of §5 will identify these (preliminary expectation: most P-primitives are load-bearing; some structural commitments — e.g., specific labeling conventions — are auxiliary).
- **Meta-substrate.** The framework within which the meta-paper's forcing argument operates: a generic primitive-level substrate-ontology framework. The meta-substrate makes minimal commitments — essentially, that there is a substrate, that mathematics exists as infrastructure, and that the structural-normative goal is to recover empirical physics.
- **Forcing route.** A specific argument-pattern for upstream-forcing a substrate primitive. The five candidate routes are A (Symmetry-Minimality), B (Operational Adequacy), C (Compositional Closure), D (Information-Theoretic Constraints), E (Category-Theoretic Necessity).
- **Honest structural commitment.** A primitive whose full upstream-forcing is not achievable, but which can be reduced to an explicitly named structural-normative category ("minimum operational adequacy," "necessary for compositional closure," "empirically necessary"). This is the residue category — substantially more honest than displaced postulate.
- **Displaced postulate.** The reconstruction-program pattern in which the postulates of the framework being reconstructed (e.g., complex Hilbert space, Born rule's quadratic form) are not eliminated but *relocated* into the reconstructive axioms. The meta-paper's purpose is to convert displaced postulates into either upstream-forced structural results or honestly-named structural commitments.
- **Operational reconstruction.** The genre of work (Hardy 2001, Masanes-Müller 2011, Chiribella-D'Ariano-Perinotti, Coecke-Kissinger, GPT) that reconstructs quantum mechanics from operational primitives without committing to substrate-level ontology. ED's QM-reconstruction face is a substrate-vocabulary variant of this genre.
- **Substrate ontology.** ED's distinguishing structural feature: a substrate-level pre-quantum ontological commitment to channels, bandwidth, polarity, and commitment, from which the Hilbert-space arena is reconstructed rather than postulated.

---

## 5. Substrate Class $\{C^*\}$ — The Meta-Substrate

The meta-paper's forcing argument applies to any meta-substrate satisfying the following meta-conditions. None of these meta-conditions assumes any specific substrate primitive (bandwidth-additivity, $U(1)$-polarity, four-band partition, etc.) at the outset.

### C*1. Substrate framework

The meta-substrate is a *framework* for specifying substrate-level structural commitments: a structural-language plus a class of admissible substrate-models within that language. Specific substrate-models are obtained by selecting specific structural commitments (primitives) within the framework. The meta-substrate itself is the *space of admissible substrate-models* — generic at the primitive level, before any particular primitive choice is made.

### C*2. Mathematical infrastructure

The meta-substrate has access to standard mathematics: real analysis, group theory (especially compact Lie groups and their classification), category theory (especially monoidal categories and the Coecke-Kissinger framework), information theory (Shannon-Khinchin entropy axioms, capacity bounds, the Holevo bound). This infrastructure is *background*, not derived.

### C*3. Structural-normative goal

The meta-substrate operates under the structural-normative commitment that admissible substrate-models must support derivation of empirically observed physics — at minimum, the four QM postulates, special-relativistic kinematics, the gauge structure of the Standard Model, and Newton's law of gravitation in its weak-field-non-relativistic limit. Substrate-models that fail to support these derivations are excluded from the admissible class.

### C*4. Load-bearing audit

The meta-substrate supports the audit operation: given a substrate-model $S$ and a downstream Forcing Theorem $T$, determine whether $T$ would still hold under modifications to $S$'s primitives. The audit identifies load-bearing primitives (modifications break $T$) vs. auxiliary primitives (modifications preserve $T$).

### C*5. Five candidate forcing routes

The meta-substrate admits the following five candidate forcing routes for substrate primitives:

#### Route A: Symmetry-Minimality

A substrate primitive is *symmetry-minimality-forced* if it is the smallest primitive-level structural commitment supporting the symmetry content required downstream (Galilean group, Poincaré group, internal gauge groups). Example candidate forcing: the spatial-dimension primitive (P06) is symmetry-minimality-forced as the smallest spatial dimension supporting both the Galilean group's three-dimensional rotation subgroup and the spatial-translation primitive of P03.

#### Route B: Operational Adequacy

A substrate primitive is *operational-adequacy-forced* if it is necessary for the substrate to recover empirically observed physics. Removing the primitive leaves the substrate unable to derive at least one well-established empirical fact. Example candidate forcing: bandwidth-additivity (P04) is operational-adequacy-forced because $\sigma$-additivity of probability (a directly observed empirical regularity in repeated experiments) cannot be derived without it.

#### Route C: Compositional Closure

A substrate primitive is *compositional-closure-forced* if it is required for the substrate's primitives to compose into the category-theoretic structures the program uses. Example candidate forcing: the discrete-channel adjacency structure (P03 + P07) is compositional-closure-forced because the substrate-level monoidal-category composition (channels-as-objects, polarity-transport-as-morphisms) requires discrete adjacency for the categorical structure to be well-defined.

#### Route D: Information-Theoretic Constraints

A substrate primitive is *information-theoretic-forced* if it satisfies a derivable information-theoretic constraint (Shannon-Khinchin entropy axioms, single-shot capacity bounds, the Holevo bound) and alternative primitives violate the constraint. Example candidate forcing: the four-band partition (P04 §1.5) is information-theoretic-forced because the four bands (internal, adjacency, environmental, commitment-reserve) realize the minimum information-theoretic decomposition supporting the substrate-derived Hilbert-space arena's tensor-product structure plus the substrate-level decoherence-by-commitment mechanism.

#### Route E: Category-Theoretic Necessity

A substrate primitive is *category-theoretic-forced* if it realizes a specific monoidal-category-theoretic structure that is necessary for the substrate to support the program's downstream content. The Coecke-Kissinger framework (categorical QM) provides the technical machinery: dagger-symmetric-monoidal categories, complementary observables, classical structures, frobenius algebras. Example candidate forcing: the $U(1)$-valued polarity (P09) is category-theoretic-forced as the smallest continuous-classical structure on a dagger-symmetric-monoidal category supporting the substrate-level phase-rotation interference content.

### C*6. Honest residue category

The meta-substrate admits the residue category: primitives whose full upstream-forcing under Routes A–E is not achievable, but which can be honestly named as "minimum operational adequacy," "necessary for compositional closure," "empirically necessary to recover known physics," or other named structural-commitment categories. The residue category is *not* displaced postulate — it is an explicitly named structural commitment, with the structural-normative context that produces the commitment made transparent.

---

# Sections 6–10 (Roadmap; To Be Developed)

The following sections require full development; the present draft provides the architectural outline only.

## 6. Constructive Necessity (Section To Be Written)

For each load-bearing substrate primitive, develop the constructive argument: starting from the meta-substrate $\{C^*\}$, show that one (or more) of Routes A–E *constructs* the primitive as the unique (or smallest-equivalence-class) survivor.

### 6.1 Bandwidth-additivity (P04 core)

**Candidate route:** B (Operational Adequacy) + D (Information-Theoretic Constraints).

**Sketch.** Bandwidth must be additive across disjoint channel decompositions for the substrate-level probability rule (Paper #2) to be $\sigma$-additive. Non-additive bandwidth alternatives fail to support the Born rule's $\sigma$-additivity, which is operationally adequate-necessary. The Shannon-Khinchin entropy axioms (specifically axiom 4, additivity over independent events) provide the information-theoretic constraint excluding non-additive bandwidth.

### 6.2 $U(1)$-valued polarity (P09)

**Candidate route:** A (Symmetry-Minimality) + E (Category-Theoretic Necessity).

**Sketch.** Polarity must be a *continuous angular* primitive (rules out $\mathbb{Z}_n$) for the substrate to support continuous phase-rotation interference. It must be *compact* (rules out $\mathbb{R}$) for the Frobenius classification of substrate-level division algebras to yield $\mathbb{C}$ rather than $\mathbb{H}$ in Paper #1's argument. The unique compact continuous abelian Lie group is $U(1)$. The Coecke-Kissinger framework supplies the category-theoretic infrastructure: $U(1)$ is the unique continuous-classical-structure-on-a-dagger-symmetric-monoidal-category whose self-dual basis matches the substrate-level interference content.

**Residue.** If full Route A + E forcing fails, the honest residue is: "$U(1)$ polarity is *minimum operational adequacy* for the substrate to recover continuous-phase interference content, which is empirically observed."

### 6.3 Four-band partition (P04 §1.5)

**Candidate route:** D (Information-Theoretic Constraints) + C (Compositional Closure).

**Sketch.** The four bands (internal, adjacency, environmental, commitment-reserve) realize the minimum information-theoretic decomposition supporting:
- **Internal** band: chain's self-sustaining content (rule-type identity).
- **Adjacency** band: chain's coupling to local participation neighborhood (kinematic content).
- **Environmental** band: chain's coupling to broader bath (decoherence content).
- **Commitment-reserve** band: chain's allocation toward commitment events (measurement content).

A three-band partition would conflate at least two of these structurally distinct content categories; a five-band partition would split one category artificially. The four-band structure is therefore *information-theoretic-minimum* + *compositional-closure-forced* (it is the smallest partition supporting the program's downstream operational categories without conflation).

**Residue.** If full forcing fails, the honest residue is: "Four-band partition is *necessary for compositional closure* of the substrate's primitive operational categories — fewer bands conflate, more bands split artificially."

### 6.4 Commitment-with-uniform-$U(1)$-phase-randomization (P11)

**Candidate route:** B (Operational Adequacy) + D (Information-Theoretic Constraints).

**Sketch.** Commitment events are operational-adequacy-required for the substrate to support measurement outcomes (without commitment, no substrate-level mechanism for observed discrete-outcome experiments). Phase-randomization at commitment is operational-adequacy-required for the substrate to produce the observed quadratic Born rule. Uniform-$U(1)$ phase-randomization is information-theoretic-minimum (the Haar measure on $U(1)$ maximizes phase-uncertainty entropy and is invariant under the substrate's polarity primitive).

**Residue.** If full forcing fails, the honest residue is: "Uniform-$U(1)$ phase-randomization at commitment is *minimum operational adequacy* for the substrate to recover the observed Born rule's quadratic form via the substrate-level decoherence mechanism."

### 6.5 Discrete-channel adjacency structure (P03 + P07)

**Candidate route:** C (Compositional Closure) + E (Category-Theoretic Necessity).

**Sketch.** The substrate's primitive structure is a discrete graph-like layer (channels at vertices, polarity-transport along edges). Continuous-channel alternatives (without discrete adjacency) fail to support the category-theoretic monoidal structure the program uses; in particular, polarity-transport-as-morphisms requires discrete adjacency for morphism composition to be well-defined.

**Residue.** If full forcing fails, the honest residue is: "Discrete-channel adjacency is *necessary for compositional closure* of the substrate's monoidal-categorical structure."

### 6.6 Time-homogeneity (P13) and spatial-homogeneity (P03 + P06)

**Candidate route:** A (Symmetry-Minimality) + B (Operational Adequacy).

**Sketch.** Stone's theorem requires strongly continuous one-parameter symmetry groups. Time-homogeneity is the smallest symmetry primitive supporting Stone's theorem on time-translations (Paper #4); spatial-homogeneity is the smallest supporting Stone on spatial-translations (Paper #12). Without these symmetries, the Schrödinger equation and momentum operator are not derivable from substrate primitives.

**Residue.** If full forcing fails, the honest residue is: "Time- and spatial-homogeneity are *minimum operational adequacy* for the substrate to support the symmetry-based derivations of Schrödinger and momentum."

### 6.7 Spatial dimension $D = 3$ (P06)

**Candidate route:** B (Operational Adequacy) + A (Symmetry-Minimality).

**Sketch.** The substrate's spatial axis is $\mathbb{R}^3$. The dimension three is load-bearing for:
- $\pi_1(Q_2) = \mathbb{Z}_2$ in two-fermion configuration space (Paper #7, spin-statistics dichotomy). In $D = 2$, $\pi_1$ is the braid group (anyons); in $D \geq 4$, $\pi_1$ is trivial (only bosons).
- The $g = 2$ result (Paper #7) requires $SL(2, \mathbb{C})$ as the universal cover of $SO(3,1)$ — specific to $D = 3+1$.
- The Newton's law derivation (Paper #9) uses the area scaling $4\pi R^2$ of a 2-sphere in $\mathbb{R}^3$.

Operational adequacy: empirically, observed physics is in $D = 3+1$. Forcing this from a deeper principle (e.g., anthropic arguments, holographic arguments, dynamical-stability arguments) is open and not attempted in the present draft.

**Residue.** The honest residue is: "$D = 3+1$ is *empirically necessary* to recover observed physics. Deeper structural forcing (anthropic, holographic, dynamical) is open."

### 6.8 V1 retarded kernel rule-type

**Candidate route:** B (Operational Adequacy) + C (Compositional Closure).

**Sketch.** Already addressed substantially in Paper #19 (V1 retarded support). The retarded support is forced by P11 commitment-irreversibility acting on the kernel-level structure; symmetric V1 is non-constructible at the substrate level. The forcing reduces to: *given* P11 + the existence of V1 as a kernel rule-type, the support is retarded. Forcing of V1's existence as a rule-type itself is upstream-content of Routes C (Compositional Closure: V1 is required for the substrate's vacuum sector) and B (Operational Adequacy: required to recover QFT vacuum content).

### 6.9 V5 cross-chain correlation kernel rule-type

**Candidate route:** B (Operational Adequacy) + C (Compositional Closure).

**Sketch.** V5 does three jobs (soft-matter Maxwell viscoelasticity, Hawking spectrum cutoff, entanglement bandwidth) across ~40 orders of magnitude — a structural unification not present in any reconstruction program. The operational adequacy argument: each of the three jobs is empirically necessary, and the V5 unification realizes the smallest-equivalence-class of kernel rule-types supporting all three. Full upstream-forcing of V5 as a primitive (vs. forcing it as the smallest cross-chain correlation rule-type satisfying the three constraints) requires Section 6 development.

## 7. Exclusion Arguments (Section To Be Written)

For each load-bearing primitive, develop explicit exclusion arguments against alternative primitives. Each exclusion takes the form: "Alternative primitive $X'$ violates condition $Y$ in Route $Z$; therefore $X'$ is excluded; the unique survivor is $X$."

**Outline of exclusion table:**

| Primitive | Alternatives considered | Exclusion route |
|---|---|---|
| P09 ($U(1)$ polarity) | $\mathbb{Z}_n$, $\mathbb{R}$, no angular primitive | A (compactness + continuity), E (Coecke-Kissinger classification) |
| P04 (bandwidth additivity) | Non-additive bandwidth, multi-valued bandwidth | B (Born rule's $\sigma$-additivity), D (Shannon-Khinchin axiom 4) |
| Four-band partition | 3-band, 5-band, non-orthogonal partition | C (compositional closure), D (information-theoretic minimum) |
| P11 (commitment with uniform-$U(1)$ phase-randomization) | Non-uniform phase, no commitment, non-irreversible commitment | B (Born rule recovery), D (Haar-measure entropy maximization) |
| P03 + P07 (discrete adjacency) | Continuous adjacency, no adjacency | C (categorical morphism composition), E (monoidal category structure) |
| P13 (time homogeneity) | Time-inhomogeneous primitive structure | A (Stone's theorem applicability), B (Schrödinger derivation) |
| P06 ($D = 3$) | $D = 2$, $D \geq 4$ | A (spin-statistics dichotomy), B (empirical $D = 3+1$) |

## 8. Falsifiers (Section To Be Written)

Identify falsifying conditions: empirical or structural observations that would refute specific claims about substrate primitives being upstream-forced.

**Examples to develop:**

- **Falsifier for P09 $U(1)$-forcing.** Discovery of a physical system whose phase content is genuinely $\mathbb{Z}_n$-valued (not approximately, not effectively) at the substrate level — e.g., a discrete-anyon system not reducible to continuous-$U(1)$ effective description — would refute Route A's symmetry-minimality forcing.
- **Falsifier for four-band partition.** Discovery of a physical phenomenon requiring a five-band substrate partition (e.g., a substrate-level operational category not subsumed by internal / adjacency / environmental / commitment-reserve) would refute Route D's minimum-partition forcing.
- **Falsifier for V5 universality.** Discovery of a soft-matter Maxwell relaxation profile inconsistent with the same kernel that produces Hawking spectrum cutoffs (suitably scaled) would refute the V5 cross-scale unification claim.

## 9. Appendix (Section To Be Written)

- A.1 Cross-reference table: which Forcing Papers depend on which substrate primitives.
- A.2 Inventory of all 13 P-primitives + auxiliary primitives, with load-bearing status per Forcing Theorem.
- A.3 Glossary of meta-substrate vocabulary.
- A.4 Methodological note on the recursion-stopping commitment.

## 10. Concluding Remarks (Section To Be Written)

The meta-paper's role in the ED program is structural: it converts the displaced-postulate critique from "ED has unforced roots" to "ED's unforced roots are explicitly named and located at the deepest possible level given the structural-normative goal of recovering empirical physics." This is honest, defensible, and substantially stronger than the displaced-postulate framing.

The full execution of Sections 6–10 is the program's next structurally substantial item. The opening sections (1–5) presented here provide the framing, claim, scope, vocabulary, and meta-substrate definition. The rest is exclusion-argument development per load-bearing primitive.

---

# Status

**Sections 1–5: Complete (this draft).**

**Sections 6–10: Outlined (this draft).** Full development requires:

- Per-primitive Constructive Necessity arguments (§6).
- Per-primitive Exclusion Arguments excluding alternative primitive structures (§7).
- Per-claim Falsifiers (§8).
- Cross-reference appendix + load-bearing audit (§9).
- Methodological closing remarks (§10).

Estimated total length at full development: 12,000–18,000 words (this is genre-establishing program-level synthesis territory; longer than typical Forcing Papers is appropriate per the revised length policy of 2026-05-13).

**Honest closing.** This draft does not yet *force* the substrate primitives. It provides the framework within which forcing arguments can be developed and identifies the candidate routes. Whether each load-bearing primitive will be fully upstream-forced or will reduce to an honest residue category is the subject of the full Sections 6–10 development. The honest expectation: some primitives will be fully forced under one or more of Routes A–E; others will reduce to honest residue ("minimum operational adequacy," "necessary for compositional closure"). Either outcome converts displaced postulates to explicitly named structural commitments — eliminating the critique in its strongest form even where full upstream-forcing fails.
