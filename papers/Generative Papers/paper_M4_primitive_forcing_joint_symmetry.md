> **⚠️ ARCHIVED — 2026-05-13.** This paper is frozen as a historical artifact. See `ARCHIVED_M_SERIES_NOTICE.md` for context. External review identified that the M-series did not eliminate the displaced-postulate critique; it relocated the critique into the meta-substrate's C*4 empirical-recovery commitment. ED is now framed as an **axiomatic substrate ontology** (13 postulated primitives + cross-domain reach), not a forcing-from-nothing program. Do not cite this paper as "forcing" the symmetry cluster; do not build new work on its framework.

---

# Joint Symmetry Forcing — P03 (Adjacency Homogeneity), P13 (Time Homogeneity), GAL (Galilean Symmetry), and POI (Poincaré Compatibility) — are FORCED

**Paper M-4 of the Event Density Primitive-Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Primitive-Forcing M-Series — Paper M-4
**Position:** Fourth primitive-forcing paper. Downstream of M-1 (P09), M-2 (P04), M-3 (P11). Upstream of Forcing Papers #1–#19.
**Genre:** Primitive-level forcing paper. Joint-primitive forcing. Standalone. Cold-reader accessible. 10-section template.

---

## Abstract

The Event Density (ED) substrate is committed at the primitive level to a cluster of four interdependent symmetry structural commitments: **adjacency homogeneity (P03)** — the substrate's participation-graph adjacency structure is invariant under translation between loci; **time homogeneity (P13)** — the substrate's dynamical primitive is invariant under time translation; **Galilean symmetry (GAL)** — at non-relativistic scope, the substrate's symmetry group is the Galilean group with its central-extension Lie algebra closure; **Poincaré compatibility (POI)** — at relativistic scope, the substrate's symmetry group is the Poincaré group containing the Galilean group as the non-relativistic limit. These four commitments are *mutually load-bearing* — none can be forced independently of the others without invoking downstream Forcing Paper content circularly. They form a *joint forcing cluster* under the Meta-Paper M0 §5.2 priority ordering. This paper shows that, given the meta-substrate framework $\{C^*\}$, the previously-closed M-1 ($U(1)$ polarity), M-2 (four-band partition), and M-3 (commitment irreversibility) results, and standard background mathematics (Lie group classification, Stone's theorem, group contractions, maximum-entropy principle), the joint symmetry cluster is forced by four convergent routes: **information-theoretic uniformity (A)**, **symmetry-minimality + compositional closure of the substrate Lie algebra (B)**, **adjacency-preserving propagation (C)**, and **structural-normative requirement of recovering relativistic-and-non-relativistic physics jointly (D)**. Non-homogeneous, anisotropic, broken-Galilean, broken-Poincaré, and over-strong (conformal) symmetry alternatives are each excluded by explicit structural argument. The forcing chain is mixed: spatial-and-temporal homogeneity (P03 + P13) are cleanly forceable under Routes A + C; Galilean closure (GAL) is forceable under Route B + structural-normative non-relativistic-recovery; Poincaré compatibility (POI) is partially forceable, with the choice "Poincaré rather than de Sitter at relativistic scope" carrying honest residue under the structural-normative goal C*7. With M-4 closure, seven downstream papers (#1, #4, #6, #7, #12, #15, #17) shift their §3.0 status for the symmetry primitives from "load-bearing input" to "forced upstream by M-4"; the displaced-postulate critique no longer applies to the symmetry-primitive cluster.

---

## 1. Framing

### 1.1 What the four primitives are, and why they form a single cluster

The ED substrate carries structural commitments to four distinct symmetry primitives, each appearing as a load-bearing input in different Forcing Papers:

- **P03 (Adjacency Homogeneity).** The substrate's primitive adjacency relations between loci are invariant under translation: shifting all loci by a common displacement leaves the participation-graph adjacency structure intact. Specifically, the substrate's primitive operations on a locus $u$ are structurally identical to its operations on a translated locus $u + a$ for any admissible translation $a$. This is the substrate-level source of spatial homogeneity.

- **P13 (Time Homogeneity).** The substrate's primitive dynamical operations are invariant under time translation: applying the substrate's dynamics at time $t_1$ produces structurally identical results to applying them at time $t_2$. The substrate has no preferred absolute time origin.

- **GAL (Galilean Symmetry).** At non-relativistic scope, the substrate's full symmetry group is the Galilean group $G_{\mathrm{Gal}} = \mathbb{R} \times SO(3) \ltimes (\mathbb{R}^3 \rtimes \mathbb{R}^3)$ — the semidirect product structure of time translations, spatial rotations, spatial translations, and Galilean boosts. The Galilean Lie algebra carries the central-extension closure $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ with mass appearing as a central element.

- **POI (Poincaré Compatibility).** At relativistic scope, the substrate's symmetry group is the Poincaré group $\mathrm{ISO}(3,1) = O(3,1) \ltimes \mathbb{R}^{3,1}$ — Lorentz transformations + spacetime translations. The non-relativistic Galilean group emerges as the $c \to \infty$ contraction of Poincaré. The substrate must support both regimes: relativistic physics directly, and non-relativistic physics as the appropriate contraction limit.

These four primitives are **interdependent**, not independent. Specifically:

- **P03 + P13 together force Stone's theorem.** Stone's theorem applies to strongly continuous one-parameter unitary groups generated by self-adjoint operators. Without P13, the time-translation operator $\hat{U}_t$ has no Stone-theorem-applicable structure; without P03, the spatial-translation operator $\hat{T}_a$ likewise fails Stone. Either one alone is insufficient to derive Schrödinger or momentum — both must be substrate-level structural commitments.

- **GAL requires P03 + P13 as inputs.** The Galilean Lie algebra contains both time and spatial translations as Lie subalgebras. Without P03 + P13, the Galilean group cannot act on the substrate.

- **POI requires GAL as a limit.** The Poincaré group at $c \to \infty$ does *not* automatically contract to the Galilean group's *central-extension* with mass; the central-extension structure (which produces the $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ closure) is a *separate* substrate-level structural commitment. Both Poincaré (relativistic scope) and Galilean-with-central-extension (non-relativistic scope) must be simultaneous substrate commitments for the substrate to recover both regimes.

Therefore: **the four primitives cannot be forced independently.** Trying to force P03 alone would leave P13 dangling; trying to force GAL alone would presume P03 + P13 + the central-extension; trying to force POI alone would leave the non-relativistic limit unaccounted for. The natural structural unit is the joint cluster.

### 1.2 Why the cluster is load-bearing across the Forcing Series

The joint symmetry cluster appears as load-bearing input in multiple Forcing Papers (per Phase-1 §3.0 audit and Dependency Graph §2):

- **Paper #1 (Participation Measure).** P03 is invoked as channel-and-locus indexing, supplying the substrate-level structural domain on which the participation measure is defined.
- **Paper #4 (Schrödinger Equation via Stone).** P13 is directly invoked — Stone's theorem on time-translations requires P13 as primary substrate-level structural commitment.
- **Paper #6 (Hamiltonian + Mass).** GAL is invoked — the Galilean Lie algebra closure $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ is the structural source of the $1/(2m)$ coefficient and the structural identification of inertial mass.
- **Paper #7 (Dirac + g=2).** POI is invoked — Lorentz covariance is required for the Dirac equation; the Galilean group is recovered as the non-relativistic contraction.
- **Paper #12 (Momentum Operator).** P03 is directly invoked — Stone's theorem on spatial-translations requires P03 as primary substrate-level structural commitment.
- **Paper #15 (Adjacency Kinetic Structure).** GAL is invoked in the bandwidth-flow Galilean covariance argument.
- **Paper #17 (Four Postulates Unified).** All four — P03, P13, GAL, POI — appear in the synthesis paper's Pillar 2.

Per the Dependency Graph (DEPENDENCY_GRAPH_ED.md §5), closing the joint symmetry cluster updates **seven** downstream papers (a substantial cumulative impact, comparable to the M-1 + M-2 closure scope).

### 1.3 Why symmetry primitives must be forced, not assumed

The displaced-postulate critique applies to symmetry primitives in a particularly sharp form. Standard physics derives symmetries by Noether's theorem: time-translation invariance produces energy conservation, spatial-translation invariance produces momentum conservation, etc. But these derivations operate at the *Lagrangian-field-theoretic level*, downstream of the Hilbert-space arena. At the substrate level — pre-Hilbert-space, pre-field-theory — Noether is not available. The substrate must commit to symmetries *primitively*, and the displaced-postulate question becomes: why these symmetries?

The forcing routes operate at the meta-substrate level:

- **Route A (Information-Theoretic Uniformity).** Under no-additional-information assumption, the substrate's primitive structure must be uniform across loci and times. Maximum-entropy under translation symmetry produces P03 + P13.
- **Route B (Symmetry-Minimality + Compositional Closure).** The substrate's primitive symmetry group must be the *minimal* faithful symmetry compatible with the closed Lie-algebra structure required for downstream forcing of Schrödinger, momentum, Hamiltonian-with-mass, Dirac. Inönü-Wigner contraction analysis fixes the Galilean group as the smallest non-trivial Lie subgroup supporting these.
- **Route C (Adjacency-Preserving Propagation).** Substrate adjacency must be translation-invariant for forward-causal propagation (M-3 Route D) to be well-defined. Non-homogeneous adjacency would produce position-dependent causal structure, violating M-3.
- **Route D (Structural-Normative Recovery of Empirical Physics).** Both relativistic and non-relativistic physics are empirically observed regimes. The substrate must support both; the only known group structure achieving this with the Inönü-Wigner contraction property is Poincaré (relativistic) → Galilean (non-relativistic, $c \to \infty$ contraction).

The convergence of four routes provides over-determined forcing. Yet, honest residue remains: the choice "Poincaré rather than de Sitter / anti-de Sitter at relativistic scope" (specifically, the choice of curvature-zero rather than curvature-$\pm$ relativistic symmetry group) is *not* forced by the routes A–D. It reduces to operational adequacy + empirical observation that local relativistic physics is well-modeled by Poincaré at observed scales. The full structural forcing of "Poincaré rather than de Sitter" connects to cosmological-curvature questions outside this paper's scope; here it appears as named residue.

### 1.4 Why the joint cluster is the natural M-4 step

Meta-Paper M0 §5.2 placed the joint symmetry forcing at Tier 3 (M-5 in the original numbering). It is now M-4 in the present sequencing because:

- **Reason 1 — Mutual dependency forces joint treatment.** Per §1.1, the four primitives cannot be forced independently. Any attempt to split them into M-4 + M-5 + M-6 + M-7 would either invoke downstream Forcing Paper content circularly (for the missing primitives) or leave each as residue.

- **Reason 2 — Cumulative impact on the Forcing Series.** The joint cluster appears in 7 downstream papers. Closing it as M-4 brings cumulative coverage (M-1 + M-2 + M-3 + M-4) to approximately **15 of 19 Forcing Papers** — the displaced-postulate critique elimination crosses the 75% threshold with this closure.

- **Reason 3 — Inputs from M-1, M-2, M-3 are now available.** The forcing argument uses M-1's $U(1)$ structure (for unitary group representations of symmetry generators), M-2's four-band partition (for the substrate-level locus where homogeneity acts), and M-3's commitment-irreversibility (for the forward-causal-direction requirement of Route C).

**Series context.** This is Paper M-4 of the ED Primitive-Forcing M-series. With M-4 closed, four of the load-bearing items in the dependency graph (P09, P04 core, P04 §1.5, P11) plus the joint symmetry cluster (P03, P13, GAL, POI) will be upstream-forced. The remaining items (P07 channel structure, V1 + V5 existence as rule-types, HYD scale-separation, and the residue commitments P06, P10, P12, HOL, DEC, IND, THN) constitute M-5 through M-12.

---

## 2. Claim

> **Forcing Theorem M-4 (Joint Symmetry Cluster is FORCED).** Let any meta-substrate satisfy the conditions $\{C^*\}$ of Meta-Paper M0 §5, together with the M-1-forced $U(1)$-valued polarity (P09), the M-2-forced four-band partition + bandwidth additivity (P04), and the M-3-forced commitment irreversibility (P11). Then the substrate's symmetry content is forced to be: **(P03)** adjacency homogeneity — translation-invariance of participation-graph adjacency relations; **(P13)** time homogeneity — translation-invariance of substrate dynamics; **(GAL)** Galilean symmetry — at non-relativistic scope, the substrate carries the Galilean group with its central-extension Lie algebra closure; **(POI)** Poincaré compatibility — at relativistic scope, the substrate carries the Poincaré group containing Galilean as the $c \to \infty$ Inönü-Wigner contraction. Non-homogeneous, anisotropic, broken-Galilean, broken-Poincaré, and over-strong (e.g., full conformal) symmetry alternatives are each excluded by joint application of four independent forcing routes — information-theoretic uniformity (A), symmetry-minimality + compositional closure (B), adjacency-preserving propagation (C), and structural-normative recovery of empirical physics (D). The cluster form is FORCED. The choice "Poincaré rather than de Sitter / anti-de Sitter at relativistic scope" is identified as honest residue (operational adequacy + empirical local-flatness assumption).

---

## 3. Primitive Inputs and Upstream Dependencies

### 3.0 Meta-Substrate Inputs (load-bearing, not derived in this paper)

This paper's forcing argument invokes:

- **Meta-substrate framework $\{C^*\}$ (Meta-Paper M0 §5).**
- **M-1 closure: P09 ($U(1)$ polarity) is forced.** Supplies the substrate's continuous-compact-abelian angular structure on which strongly continuous unitary representations of symmetry generators operate.
- **M-2 closure: P04 (four-band partition + bandwidth additivity) is forced.** Supplies the substrate's bandwidth content that the homogeneity primitives act on uniformly.
- **M-3 closure: P11 commitment irreversibility is forced.** Supplies the forward-causal direction that the homogeneity primitives must respect (Route C).
- **Background mathematics.** Lie group classification (Cartan-Killing); Stone's theorem on strongly continuous unitary groups; Inönü-Wigner group contractions (1953); maximum-entropy principle on translation-invariant distributions; Wigner's classification of unitary irreducible representations of the Poincaré group (1939).
- **The structural-normative goal of empirical-physics recovery (C*7).** Specifically: the substrate must support both *non-relativistic* physics (Galilean kinematics, observed in standard quantum mechanics + classical mechanics at low velocities) and *relativistic* physics (Lorentz kinematics, observed in high-energy experiments + special relativity).

### 3.1 No downstream input — circularity audit

This paper does NOT invoke any result from Forcing Papers #1–#19. Specifically:

- **Paper #4 (Schrödinger via Stone).** Downstream — uses Stone's theorem with P13 as input.
- **Paper #6 (Hamiltonian + Mass).** Downstream — uses Galilean Lie algebra closure with GAL as input.
- **Paper #7 (Dirac + g=2).** Downstream — uses Poincaré covariance with POI as input.
- **Paper #12 (Momentum Operator).** Downstream — uses Stone's theorem with P03 as input.
- **Paper #15 (Adjacency Kinetic Structure).** Downstream.
- **Paper #17 (Four Postulates Unified).** Downstream synthesis.

The forcing argument operates purely on $\{C^*\}$ + M-1 + M-2 + M-3 + background mathematics. Stone's theorem appears in the constructive necessity argument as a mathematical infrastructure result (Stone 1932), not as a Forcing Paper result; this is consistent with the circularity discipline.

### 3.2 What is FORCED

- **P03 (Adjacency Homogeneity).** The substrate's primitive adjacency structure between loci is invariant under translation. Equivalently: the substrate's primitive operations at any locus are structurally identical to its operations at any translated locus.
- **P13 (Time Homogeneity).** The substrate's primitive dynamical operations are invariant under time translation. The substrate has no preferred absolute time origin.
- **GAL (Galilean Symmetry).** At non-relativistic scope (where chain velocities are much less than $c$), the substrate's full symmetry group is the Galilean group with central-extension Lie algebra closure including the mass-central-element structure.
- **POI (Poincaré Compatibility) — partially forced.** At relativistic scope, the substrate's symmetry group is the Poincaré group, with the Galilean group emerging as the $c \to \infty$ Inönü-Wigner contraction. **Residue:** the choice "Poincaré rather than de Sitter / anti-de Sitter" reduces to operational adequacy + empirical local-flatness assumption.

### 3.3 What is INHERITED

- **The numerical value of $c$ (speed of light).** Forced as a dimensional constant of the Poincaré group; numerical value is empirical.
- **The numerical value of $\hbar$.** Inherited via the Madelung anchoring + Wigner-classification's central-extension parameter.
- **The specific labeling of inertial reference frames** in which Galilean / Poincaré is presented.

### 3.4 What is OUT OF SCOPE

- This paper does NOT derive the cosmological-curvature commitment (Poincaré at observed-scale curvature-zero versus de Sitter / anti-de Sitter at finite cosmological curvature). The substrate-level choice of curvature-zero relativistic symmetry remains honest residue under operational adequacy.
- This paper does NOT derive specific *internal* symmetries (gauge group $U(1) \times SU(2) \times SU(3)$ of the Standard Model). Internal-gauge content is downstream (Paper #5's T17) and is value-layer empirical for specific group choice.
- This paper does NOT derive specific representations of the symmetry groups on substrate content. Representations are downstream Forcing Paper #1–#19 content.

---

## 4. Key Vocabulary

- **Adjacency Homogeneity (P03).** Structural property of the substrate's participation-graph: adjacency relations between loci are translation-invariant. Two loci that differ by a common displacement vector $a$ have structurally identical adjacency relations to their neighborhoods.

- **Time Homogeneity (P13).** Structural property of the substrate's dynamical primitive: dynamics applied at one time produce structurally identical results to dynamics applied at a translated time. The substrate has no preferred absolute time origin.

- **Galilean Symmetry (GAL).** The structural commitment that, at non-relativistic scope (chain velocities $|\vec{v}| \ll c$), the substrate's full symmetry group is the Galilean group $\mathbb{R} \times SO(3) \ltimes (\mathbb{R}^3 \rtimes \mathbb{R}^3)$ — the semidirect product of: time translations, spatial rotations, spatial translations, and Galilean boosts. The Galilean Lie algebra has the central-extension closure $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ with mass as a central element (Bargmann's classification).

- **Poincaré Compatibility (POI).** The structural commitment that, at relativistic scope, the substrate's symmetry group is the Poincaré group $\mathrm{ISO}(3,1) = O(3,1) \ltimes \mathbb{R}^{3,1}$. The Galilean group emerges as the $c \to \infty$ Inönü-Wigner contraction.

- **Symmetry-Minimality.** The structural requirement that the substrate's primitive symmetry group is the *smallest* faithful symmetry compatible with all other primitive-level commitments and the meta-substrate's structural-normative goal of recovering empirical physics. No symmetry larger than necessary is admitted.

- **Information-Uniformity.** The structural requirement that, in the absence of additional structural information, the substrate's primitive content is *uniformly* distributed across translation-equivalent loci and times. Maximum-entropy under the translation group action.

- **Compositional Closure.** For symmetry groups: the requirement that the substrate's primitive symmetry generators close into a Lie algebra under commutation. Without closure, repeated application of symmetry generators would produce structures outside the substrate's primitive operations — violating the substrate's structural self-consistency.

- **Causal Monotonicity.** The substrate-level requirement that dynamics advance information along a fixed causal direction in the participation graph (M-3 Routes D and E). Symmetry primitives must respect this monotonicity — i.e., translations and Lorentz boosts must preserve forward-causal structure.

- **Kernel-Propagation Invariance.** Substrate-level structural requirement that kernel rule-types (V1, V5) propagate consistently under the symmetry group: a kernel-mediated process at locus $u$ produces structurally identical content to the same process at locus $u + a$. Equivalent to saying that kernel structure is symmetry-equivariant.

- **Inönü-Wigner Contraction.** The standard mathematical procedure (Inönü-Wigner 1953) by which one Lie group $G$ is contracted to another Lie group $G'$ in a singular limit (e.g., $c \to \infty$ contracts Poincaré to Galilean). The contracted group's structure constants are limits of the parent group's structure constants.

- **Meta-substrate $\{C^*\}$.** Framework within which M-series forcing arguments operate (Meta-Paper M0 §5).

- **Central extension.** A Lie group / Lie algebra extension by a central element (typically real-valued). The Galilean group's *central extension* by mass is the structural source of the $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ commutator and the appearance of mass in the substrate's dynamical algebra.

---

## 5. Substrate Class $\{C^*\}$

### C*1. Meta-substrate framework

Per Meta-Paper M0 §5. Supplies structural-language plus admissible substrate-models.

### C*2. Existing closures: M-1, M-2, M-3

- M-1: P09 ($U(1)$ polarity) — substrate's continuous-compact-abelian angular primitive.
- M-2: P04 (four-band partition + bandwidth additivity) — substrate's bandwidth content structure.
- M-3: P11 commitment irreversibility — substrate's forward-causal-direction primitive.

These supply the structural content on which the symmetry primitives must act.

### C*3. Group-theoretic infrastructure

The meta-substrate has access to: Cartan-Killing classification of Lie groups; Stone's theorem on strongly continuous unitary groups; Inönü-Wigner group contractions; Wigner's classification of Poincaré unitary irreducible representations; Bargmann's classification of Galilean central extensions.

### C*4. Information-theoretic uniformity infrastructure

The meta-substrate provides max-entropy principle on translation-invariant distributions: under no-additional-information assumption, primitive content is uniformly distributed across translation-equivalent classes.

### C*5. Adjacency-graph infrastructure

Per M-2 + M-3 inputs. The substrate is a graph-like structure with channels at vertices and locus-adjacency relations between vertices, with forward-causal direction supplied by M-3.

### C*6. Structural-normative goal C*7

The substrate must support both non-relativistic physics (Galilean kinematics) and relativistic physics (Lorentz kinematics) as empirically observed regimes.

### C*7. Compositional-closure requirement

Substrate-level symmetry generators must close into a Lie algebra. Without closure, the substrate's primitive structure is not self-consistent under composition.

---

## 6. Alternative Encodings $\{A1-A6\}$ and $\{B1-B6\}$

This section enumerates structural alternatives to the joint symmetry cluster. Exclusion arguments appear in §8.

### 6.A. A-series — Structural alternatives within the substrate-ontology framework

**A1. Non-homogeneous adjacency.**
A substrate where adjacency relations vary structurally across loci: some loci have richer adjacency content (more neighbors, different bandwidth-coupling structure) than others. Translation symmetry is broken.

**A2. Non-homogeneous time.**
A substrate where dynamical operations vary structurally across time: the dynamics applied at $t_1$ differ from those at $t_2$. Time-translation symmetry is broken.

**A3. Anisotropic adjacency.**
A substrate where adjacency relations are translation-invariant but *direction-dependent*: adjacency along one spatial axis is structurally different from adjacency along another. Rotational symmetry is broken.

**A4. Broken Galilean symmetry.**
At non-relativistic scope, the substrate's symmetry group is *smaller* than Galilean — e.g., only the spatial-rotation subgroup $SO(3)$ + time translations $\mathbb{R}$, without spatial translations or Galilean boosts. Or alternatively, the Galilean Lie algebra closes *without* the central-extension structure — no mass-central-element appears.

**A5. Broken Poincaré compatibility.**
At relativistic scope, the substrate does not carry the full Poincaré group — e.g., only the Lorentz subgroup $O(3,1)$ without spacetime translations, or only the translation subgroup $\mathbb{R}^{3,1}$ without Lorentz transformations.

**A6. Over-strong symmetry (full conformal invariance).**
The substrate carries the full conformal group $O(4,2)$ — Poincaré plus dilations + special conformal transformations. Symmetry is *larger* than necessary, including scale transformations.

### 6.B. B-series — Mainstream alternatives from physics frameworks

**B1. Classical Newtonian absolute time.**
Newtonian framework with absolute time $t$ across all observers. Time-translation symmetry holds but there is a structural distinction between *absolute* time and *frame-dependent* time. Effectively: Galilean symmetry without the central-extension closure (mass appears as an independent inertial parameter, not as a Lie algebra central element).

**B2. Lorentz-violating field theories.**
Field theories with explicit Lorentz violation: a preferred frame, anisotropic propagation speeds, or modified dispersion relations $E^2 = p^2 c^2 + m^2 c^4 + \epsilon(p, E)$ with Lorentz-violating $\epsilon$. Examples: Hořava-Lifshitz gravity, Standard-Model-Extension (SME) frameworks.

**B3. Anisotropic condensed-matter analogs.**
Effective relativistic theories in anisotropic media (e.g., birefringent optical materials, Dirac materials with anisotropic dispersion). Symmetry is broken to a subgroup of Poincaré by the medium's anisotropy.

**B4. Non-invariant stochastic processes.**
Stochastic-mechanical frameworks (e.g., Nelson stochastic mechanics, GRW collapse models with explicit position-dependent collapse rates) in which the underlying stochastic process is not translation-invariant.

**B5. Non-uniform Markov kernels.**
Markov dynamics with kernels $P(u \to u')$ that vary structurally with absolute position $u$ rather than displacement $u' - u$. Translation invariance broken.

**B6. Non-stationary Hamiltonian flows.**
Hamiltonian dynamics with explicitly time-dependent $\hat{H}(t)$ such that no time-translation symmetry holds. Equivalent to A2 in the dynamical-physics context.

The A-series alternatives are structural variations within the substrate-ontology framework. The B-series alternatives operate from outside the framework in physics models that have been seriously considered in the literature.

---

## 7. Constructive Necessity

This section derives the joint symmetry cluster from $\{C^*\}$ + M-1 + M-2 + M-3 + background mathematics via four convergent forcing routes.

### 7.A. Route A: Information-Theoretic Uniformity

Under the meta-substrate's structural-normative goal C*7 + the no-additional-information assumption: in the absence of additional structural information distinguishing loci from each other or times from each other, the substrate's primitive content must be uniformly distributed across translation-equivalent classes.

**Argument.** The substrate's primitive structural commitments (M-1 $U(1)$ polarity, M-2 four-band partition + bandwidth additivity, M-3 commitment irreversibility) make no reference to specific loci or times — they are universal structural commitments applying everywhere. Under the maximum-entropy principle, the substrate's *distribution* of primitive content across loci and times must be the maximum-entropy distribution under whatever invariance the substrate respects.

If the substrate respects translation symmetry, the maximum-entropy distribution is the *uniform* distribution: every locus has structurally identical primitive content, every time has structurally identical dynamics. This forces **P03 (adjacency homogeneity)** and **P13 (time homogeneity)**.

If the substrate did *not* respect translation symmetry — i.e., if some loci or times had structurally different primitive content — the substrate would require *additional structural information* to specify what distinguishes them. The meta-substrate provides no such additional information; the structural-normative goal C*7 does not require it for recovering empirical physics.

Therefore: by no-additional-information + maximum-entropy, **the substrate respects translation symmetry uniformly across loci and times**.

**Conclusion of Route A.** P03 + P13 are forced.

### 7.B. Route B: Symmetry-Minimality + Compositional Closure

The substrate's symmetry generators must close into a Lie algebra (C*7 compositional closure). The Lie algebra must be the *minimal* faithful Lie algebra compatible with all other primitive-level commitments + the structural-normative goal of recovering empirical physics.

**Argument — non-relativistic scope.** At non-relativistic scope, the substrate must support: time translations (P13), spatial translations (P03), spatial rotations (empirical observation that physics is rotationally symmetric in 3D space — meta-substrate's C*7 with P06 $D = 3$ residue), and Galilean boosts (required to relate different inertial observers — empirical observation that physics is invariant across inertial frames at low velocities).

The Lie algebra generated by these four classes of generators is the **Galilean Lie algebra** $\mathfrak{g}_{\mathrm{Gal}}$. Compositional closure requires the algebra to close — for the four classes of generators to satisfy a Jacobi-identity-compatible set of commutators. The *minimal* closed Lie algebra containing these is the Galilean Lie algebra with its central extension by mass (Bargmann 1954):

$$[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i, \quad [\hat{p}_i, \hat{K}_j] = i m \delta_{ij}, \quad \text{other commutators standard}.$$

Without the central extension, the Lie algebra does not close consistently with the substrate's continuous-unitary-representation structure (M-1's $U(1)$ provides the unitary representation infrastructure; the central extension is what allows the substrate to support faithful continuous-unitary representations with discrete mass parameter).

**Argument — relativistic scope.** At relativistic scope, the analogous compositional-closure argument requires: time translations + spatial translations + spatial rotations + Lorentz boosts. The minimal closed Lie algebra containing these is the **Poincaré Lie algebra** $\mathfrak{iso}(3,1)$.

Inönü-Wigner contraction of the Poincaré Lie algebra in the $c \to \infty$ limit produces the Galilean Lie algebra. Specifically:

- Lorentz boosts $\hat{K}_i^{\mathrm{rel}}$ contract to Galilean boosts $\hat{K}_i^{\mathrm{Gal}}$ as $c \to \infty$ with appropriate scaling.
- The mass-shell condition $p^\mu p_\mu = m^2 c^2$ contracts to the Galilean dispersion $E = p^2/(2m)$ (the kinetic-energy form, downstream content in Paper #6).
- The central extension of the Galilean algebra by mass appears in the contraction limit as the substrate-level signature of the mass-shell condition.

**Conclusion of Route B.** GAL (Galilean Lie algebra with central extension) is forced at non-relativistic scope; POI (Poincaré Lie algebra) is forced at relativistic scope; the two are connected by Inönü-Wigner contraction.

### 7.C. Route C: Adjacency-Preserving Propagation

Per M-3 Route D + Route E: substrate dynamics must be forward-causal in the adjacency graph and must respect horizon-formation as one-way information barriers. Translations and boosts of the symmetry group must preserve this forward-causal structure.

**Argument.** A symmetry transformation $g \in G$ acts on substrate content by mapping channels-at-loci to channels-at-loci. If the symmetry is *non-homogeneous* (broken adjacency homogeneity, A1) or *anisotropic* (A3), the symmetry transformation produces position-dependent or direction-dependent shifts in adjacency. This in turn produces position-dependent or direction-dependent shifts in causal structure — chains at different loci would have different causal directions, or chains in different orientations would have different causal directions.

Such position-or-direction-dependent causal structure violates M-3's adjacency-preserving propagation (M-3 Route D): non-uniform adjacency relations produce non-uniform forward-causal propagation, which the substrate's primitive structure does not support.

For symmetry transformations to be admissible as substrate-level operations, they must preserve adjacency relations (P03 homogeneity) and the rotational structure (anisotropy is excluded by the requirement that adjacency is translation-invariant across direction-equivalent classes — equivalent to the substrate's spatial-axis primitive P06 supplying $D = 3$ with isotropic adjacency).

**Conclusion of Route C.** P03 + rotational invariance of adjacency follows from M-3's forward-causal-direction requirement.

### 7.D. Route D: Structural-Normative Recovery of Empirical Physics

The structural-normative goal C*7 + M0 §5 requires the substrate to support both non-relativistic and relativistic empirical physics.

**Argument.** Empirical physics has two well-established regimes:

- **Non-relativistic regime** ($|\vec{v}| \ll c$): classical mechanics, standard quantum mechanics, atomic physics. Symmetry group: **Galilean**.
- **Relativistic regime** ($|\vec{v}| \sim c$): special relativity, high-energy physics, QFT. Symmetry group: **Poincaré**.

The substrate must support both. The only known group-theoretic structure achieving this with mathematical consistency is **Poincaré at relativistic scope + Galilean as $c \to \infty$ Inönü-Wigner contraction**.

Alternative group structures fail at least one regime:

- *Conformal symmetry $O(4,2)$* (alternative A6): includes Poincaré as subgroup but also requires scale invariance. Mass is incompatible with scale invariance (mass introduces a scale); the substrate would not recover non-relativistic mechanics with massive particles. **Excluded.**
- *De Sitter / Anti-de Sitter symmetry* (cosmological-curvature alternatives): contracts to Poincaré only at zero curvature; the universe's curvature is empirically very small but not exactly zero. The "Poincaré rather than de Sitter at relativistic scope" choice is therefore *residue* under operational adequacy (local-flatness assumption at observed scales). **Honest residue.**
- *Galilean only without Poincaré* (alternative A5): fails to recover relativistic physics. **Excluded.**
- *Lorentz only (Lorentz subgroup of Poincaré without spacetime translations)* (alternative A5 variant): fails to recover spatial-translation invariance. **Excluded.**

**Conclusion of Route D.** POI is forced (with honest residue on de Sitter / anti-de Sitter alternatives at observed-flatness regime); GAL is forced as $c \to \infty$ Inönü-Wigner contraction.

### 7.E. Convergent forcing

Four routes converge on the joint symmetry cluster:

- Route A: information-theoretic uniformity forces P03 + P13.
- Route B: symmetry-minimality + compositional closure forces GAL (non-rel scope) and POI (rel scope), connected by Inönü-Wigner contraction.
- Route C: adjacency-preserving propagation (from M-3) forces P03 + rotational invariance.
- Route D: structural-normative recovery of empirical physics forces both Galilean (non-rel) and Poincaré (rel) jointly.

The forcing is **over-determined**: any one route alone establishes a subset of the cluster; the joint application of all four establishes the complete cluster. Honest residue: "Poincaré rather than de Sitter at relativistic scope" under operational adequacy.

**Conclusion of §7.** The joint symmetry cluster (P03 + P13 + GAL + POI) is forced under joint Routes A + B + C + D from $\{C^*\}$ + M-1 + M-2 + M-3 + background mathematics. The forcing is mixed: spatial-temporal homogeneity (P03 + P13) is cleanly forceable under Routes A + C; Galilean closure (GAL) is forceable under Route B + Route D non-rel; Poincaré compatibility (POI) is forceable under Routes B + D rel, with the cosmological-curvature choice (Poincaré vs. de Sitter) as named residue.

---

## 8. Exclusion Arguments

Each A-series and B-series alternative is excluded by one or more of the four forcing routes.

### 8.A. A-series exclusions

**A1. Non-homogeneous adjacency.**
- Violates Route A: under no-additional-information assumption, maximum-entropy distribution is uniform; non-homogeneous adjacency requires additional structural information the meta-substrate does not provide.
- Violates Route C: non-homogeneous adjacency produces position-dependent forward-causal structure, conflicting with M-3 Route D.
*Excluded by Routes A and C.*

**A2. Non-homogeneous time.**
- Violates Route A: same maximum-entropy argument applied to time-translation-equivalence classes.
- Violates Route D: empirical physics is time-translation-invariant at all observed scales; non-homogeneous time would prevent the substrate from recovering this.
*Excluded by Routes A and D.*

**A3. Anisotropic adjacency.**
- Violates Route C: anisotropic adjacency produces direction-dependent forward-causal structure, conflicting with M-3.
- Violates Route D: empirical physics is rotationally invariant at all observed scales (after accounting for environmental fields); anisotropic adjacency would prevent the substrate from recovering this.
- Violates Route A: under no-additional-information, no preferred direction is structurally singled out.
*Excluded by Routes A, C, and D.*

**A4. Broken Galilean symmetry.**
- Without central extension: violates Route B compositional closure. The Lie algebra generated by P03 + P13 + spatial rotations + Galilean boosts must close consistently with M-1's continuous-unitary-representation structure; without central extension, closure fails.
- Without spatial translations or boosts: violates Route D. Empirical physics requires inertial-frame equivalence; broken Galilean fails to support this at non-rel scope.
*Excluded by Routes B and D.*

**A5. Broken Poincaré compatibility.**
- Lorentz only (no translations): violates Route A (uniformity) + Route D (empirical physics is translation-invariant).
- Translations only (no Lorentz): violates Route D (empirical physics is Lorentz-invariant at relativistic scope).
*Excluded by Routes A and D.*

**A6. Over-strong symmetry (full conformal invariance).**
- Violates Route B symmetry-minimality: conformal symmetry is larger than the minimum required by structural-normative goal. The substrate's primitive structure does not require scale invariance.
- Violates Route D: conformal symmetry is incompatible with massive particles (mass introduces a scale, breaking scale invariance). Empirical physics has massive particles (electrons, protons, etc.); the substrate must support these. Conformal substrate fails.
*Excluded by Routes B and D.*

### 8.B. B-series exclusions

**B1. Classical Newtonian absolute time.**
- Operates outside the substrate-ontology framework with Galilean symmetry but *without* central extension. Newtonian absolute time treats mass as an independent inertial parameter, not as a Lie-algebra central element.
- Violates Route B: without central extension, the substrate cannot support faithful continuous-unitary representations with discrete mass (required for downstream Forcing Paper #6 / Bargmann classification, but argued here at the substrate level from compositional-closure).
*Excluded by Route B.*

**B2. Lorentz-violating field theories.**
- Operates with explicit Lorentz violation — preferred frames, anisotropic propagation, modified dispersion.
- Violates Route D: empirical physics is consistent with strict Lorentz invariance at all observed scales (current Lorentz-violation bounds: $|\epsilon| \lesssim 10^{-15}$–$10^{-30}$ depending on regime). The substrate's structural-normative goal of empirical recovery requires Lorentz invariance to the empirical bound; Lorentz-violating substrate would not recover this.
- Additionally violates Route A: maximum-entropy with no-additional-information cannot select a preferred frame.
*Excluded by Routes A and D.*

**B3. Anisotropic condensed-matter analogs.**
- Operates as *effective* theories in anisotropic media. Not primitive-level substrate commitments — anisotropy is a property of the *medium* (downstream content), not of the substrate.
- The substrate underlying anisotropic-medium effective theories must itself be isotropic and homogeneous (else recursion: where does the anisotropic medium's substrate come from?).
*Excluded by framework-level analysis: anisotropic-medium effective theories are downstream of an isotropic substrate.*

**B4. Non-invariant stochastic processes.**
- Operates with position-dependent stochastic process kernels. Violates Route A (uniformity) and Route C (adjacency-preserving propagation in a uniform manner).
*Excluded by Routes A and C.*

**B5. Non-uniform Markov kernels.**
- Same structural violation as B4: position-dependent kernels violate translation invariance.
- Additionally violates the substrate's compositional-closure structure: a non-uniform Markov kernel does not generate a closed translation-Lie-algebra action.
*Excluded by Routes A, B, C.*

**B6. Non-stationary Hamiltonian flows.**
- Equivalent to A2 in dynamical-physics context: explicit time-dependence in Hamiltonian breaks time-translation invariance.
*Excluded by Routes A and D (same arguments as A2).*

### 8. Summary

| Alternative | Violates | Excluded by |
|---|---|---|
| A1 Non-homogeneous adjacency | Maximum-entropy uniformity, causal direction | Routes A, C |
| A2 Non-homogeneous time | Maximum-entropy uniformity, empirical observation | Routes A, D |
| A3 Anisotropic adjacency | Causal direction, empirical observation, no-information | Routes A, C, D |
| A4 Broken Galilean symmetry | Compositional closure, inertial-frame equivalence | Routes B, D |
| A5 Broken Poincaré compatibility | Uniformity, empirical Lorentz invariance | Routes A, D |
| A6 Full conformal invariance | Symmetry-minimality, massive-particle existence | Routes B, D |
| B1 Newtonian absolute time | Compositional closure (no central extension) | Route B |
| B2 Lorentz-violating field theories | Empirical Lorentz invariance, preferred-frame violation | Routes A, D |
| B3 Anisotropic condensed-matter analogs | Downstream effective theories, isotropic substrate | Framework-level |
| B4 Non-invariant stochastic processes | Translation invariance, causal direction | Routes A, C |
| B5 Non-uniform Markov kernels | Translation invariance, compositional closure | Routes A, B, C |
| B6 Non-stationary Hamiltonian flows | Time-translation invariance, empirical observation | Routes A, D |

**Unique survivor: P03 + P13 + GAL + POI joint symmetry cluster (with honest residue on Poincaré-vs-de-Sitter cosmological-curvature choice).**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifiers

**F1. Empirical observation of position-dependent fundamental constants.**
Discovery that fundamental constants ($\hbar$, $c$, $\alpha$, etc.) vary structurally across spatial loci would falsify P03 adjacency homogeneity. *Honest assessment:* current bounds on variation of fundamental constants are extremely tight (e.g., $\dot{\alpha}/\alpha \lesssim 10^{-17}$/yr from atomic-clock experiments; spatial variation similarly bounded). No empirical evidence for position-dependence.

**F2. Empirical observation of time-dependent fundamental constants.**
Discovery that fundamental constants vary structurally over time at the substrate level (beyond cosmological-scale effects). Would falsify P13 time homogeneity. *Honest assessment:* same tight empirical bounds. No evidence.

**F3. Empirical observation of preferred-frame physics.**
Discovery of a structural preferred reference frame (e.g., anisotropic speed of light, preferred-frame Cherenkov radiation in vacuum). Would falsify POI Poincaré compatibility. *Honest assessment:* Lorentz-invariance tests are among the most thoroughly verified results in physics; bounds tighten continuously with no positive signal.

**F4. Empirical observation of conformal-invariance-required phenomena.**
Discovery of a fundamental phenomenon requiring full conformal invariance — i.e., a structural feature that cannot be accommodated by Poincaré alone, requiring dilations and special conformal transformations. Would falsify Route B symmetry-minimality (force A6 over-strong symmetry). *Honest assessment:* QCD's massless-quark conformal-anomaly aside, no empirical phenomena require full conformal invariance at the fundamental level. Massive particles are conformally non-invariant; their existence excludes A6.

**F5. Empirical observation of massive particles incompatible with central-extension Galilean structure.**
Discovery that mass does not appear as a central-element of the substrate's non-relativistic symmetry algebra. Would falsify Bargmann's classification application and force B1 (Newtonian absolute time). *Honest assessment:* Bargmann's classification is well-established mathematics; the central-extension structure is empirically supported by the appearance of $\hbar$ in the commutator $[\hat{x}, \hat{p}] = i\hbar$ (substrate-level: $[\hat{p}_i, \hat{K}_j] = i m \delta_{ij}$ in the Galilean algebra).

### 9.2 Structural falsifiers

**F6. Discovery of an alternative Lie-group structure recovering empirical physics with fewer / different generators.**
A more minimal symmetry group than Galilean (at non-rel) or Poincaré (at rel) that still recovers empirical physics would falsify Route B symmetry-minimality. *Honest assessment:* Group-theoretic classifications of admissible symmetry groups (Bargmann, Wigner, Inönü-Wigner) are mathematically thorough; alternative minimal-group constructions are not known.

**F7. Discovery of an empirically necessary symmetry group containing both Galilean and Poincaré as proper subgroups.**
A "bigger" structural symmetry group (e.g., the full conformal group $O(4,2)$, or a higher-dimensional Lie group) that is empirically required for unifying observed phenomena would falsify Route B + the present forcing argument. *Honest assessment:* current empirical physics is fully consistent with Poincaré-at-rel-scope + Galilean-at-non-rel-scope; no empirical phenomenon requires a larger symmetry group at the fundamental level.

### 9.3 Empirical exposure downstream

Closing the joint symmetry cluster upstream of Forcing Papers #1–#19 exposes the following downstream-level structures to empirical test:

- **Paper #4 (Schrödinger via Stone).** Empirical confirmation of unitary linear time evolution of quantum states (verified at $10^{-10}$ precision in Rabi oscillation experiments) confirms M-4's P13 forcing.
- **Paper #6 (Hamiltonian + Mass).** Empirical confirmation of the $\hat{p}^2/(2m)$ kinetic operator + Galilean covariance at non-rel scope (verified continuously in atomic-and-molecular physics) confirms M-4's GAL forcing.
- **Paper #7 (Dirac + g=2).** Empirical confirmation of $g = 2$ (and the QED corrections) confirms M-4's POI Poincaré forcing.
- **Paper #12 (Momentum Operator).** Empirical confirmation of $\hat{p} = -i\hbar\nabla$ + Fourier-conjugate position-momentum structure confirms M-4's P03 forcing.
- **All Forcing Papers involving translation-invariant kernel structure** (#18, #19, and downstream propagation analyses) confirm M-4's joint symmetry cluster.

---

## 10. Appendix: Derivation Chain + Glossary + Status

### 10.1 Derivation chain summary

```
Meta-Substrate Framework {C*}
       │
       ▼
M-1 (P09 U(1) polarity) FORCED ──┐
       │                          │
M-2 (P04 4-band partition) FORCED ┤
       │                          ├──► Joint inputs for M-4
M-3 (P11 irreversibility) FORCED ─┘
       │
       ▼
M-4 Five forcing routes (convergent):
   ├─── Route A: Information-Theoretic Uniformity   ──► P03, P13
   ├─── Route B: Symmetry-Minimality + Compositional Closure ──► GAL, POI
   ├─── Route C: Adjacency-Preserving Propagation (M-3 inheritance) ──► P03, rotational invariance
   └─── Route D: Structural-Normative Recovery of Empirical Physics ──► GAL (non-rel) + POI (rel)
       │
       ▼
M-4 OUTPUT: P03, P13, GAL, POI jointly FORCED
   (with honest residue: Poincaré vs. de Sitter at cosmological-curvature scope)
       │
       ▼
Downstream Updates:
   ├─── Paper #1 (P03 channel-locus indexing)
   ├─── Paper #4 (P13 time homogeneity for Stone's theorem on time-translations)
   ├─── Paper #6 (GAL Galilean Lie algebra for Hamiltonian + mass)
   ├─── Paper #7 (POI Poincaré covariance for Dirac + g=2)
   ├─── Paper #12 (P03 spatial homogeneity for Stone's theorem on spatial-translations)
   ├─── Paper #15 (GAL bandwidth-flow covariance for adjacency kinetic structure)
   └─── Paper #17 (Four postulates unified with full symmetry cluster)
```

### 10.2 Cross-references

**Meta-Paper M0** (`paper_M0_primitive_forcing_meta_paper_UPDATED.md`):
- §5.1: P03 (MED-centrality, 3 papers), P13 (LOW-centrality, 2 papers), GAL + POI (LOW-centrality, 3 papers combined).
- §5.2: original priority ordering placed joint symmetry forcing at M-5; bumped to M-4 in current sequencing.
- §6.5: roadmap for joint symmetry forcing under Route A symmetry-minimality, with note "Some residue likely on 'why Galilean and not Carrollian at non-rel scope.'"

**Dependency Graph** (`DEPENDENCY_GRAPH_ED.md`):
- §1.2: P03 + P13 (P-primitives); GAL + POI (auxiliary structural commitments).
- §2: P03 load-bearing in Papers #1, #12, #17. P13 load-bearing in Papers #4, #17. GAL in #6, #15. POI in #7.
- §4.2 Centrality tiers: P03 MED, others LOW; joint cluster MED via aggregation.
- §5: Downstream update map — closing joint cluster updates Papers #1, #4, #6, #7, #12, #15, #17 (7 papers).

**M-1 Paper, M-2 Paper, M-3 Paper.** Supply the structural inputs (P09 $U(1)$ polarity, P04 four-band partition + bandwidth additivity, P11 commitment irreversibility) on which M-4's joint forcing operates.

**Phase-1 Revisions** (`REVISIONS_PHASE1_abstracts_claims_scope.md`):
- Paper #4 §3.0 mentions P13 time-homogeneity as load-bearing input.
- Paper #6 §3.0 mentions GAL Galilean Lie algebra as load-bearing.
- Paper #7 §3.0 mentions POI Poincaré symmetry as load-bearing.
- Paper #12 §3.0 mentions P03 + P06 spatial-homogeneity as load-bearing.
- Paper #15 §3.0 mentions GAL Galilean covariance + rotational isotropy.

**Update Plan after M-4** (to be produced as `UPDATE_PLAN_after_M4.md`): per-paper surgical §3.0 update specifications for Papers #1, #4, #6, #7, #12, #15, #17.

### 10.3 Glossary extensions (beyond §4)

- **Galilean Lie algebra $\mathfrak{g}_{\mathrm{Gal}}$.** The Lie algebra of the Galilean group with central extension by mass: generators $\hat{H}$ (time translation), $\hat{p}_i$ (spatial translations), $\hat{K}_i$ (Galilean boosts), $\hat{J}_i$ (spatial rotations), $m$ (mass, central element). Commutators: $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$, $[\hat{p}_i, \hat{K}_j] = i m \delta_{ij}$, $[\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k$, $[\hat{J}_i, \hat{p}_j] = i\hbar \epsilon_{ijk} \hat{p}_k$, etc.

- **Poincaré Lie algebra $\mathfrak{iso}(3,1)$.** The Lie algebra of the Poincaré group: generators $\hat{P}^\mu$ (spacetime translations, $\mu = 0, 1, 2, 3$), $\hat{M}^{\mu\nu}$ (Lorentz transformations, antisymmetric in $\mu\nu$). Standard commutators per Poincaré-algebra structure.

- **Inönü-Wigner contraction.** Mathematical procedure (Inönü & Wigner 1953) for contracting one Lie algebra to another in a singular limit. For Poincaré $\to$ Galilean: rescale Lorentz boost $\hat{K}^{\mathrm{rel}} = c \hat{K}^{\mathrm{Gal}}$ and take $c \to \infty$; the resulting Lie algebra is the Galilean algebra with central extension by mass.

- **Bargmann's classification (1954).** Classification of central extensions of the Galilean group; identifies mass as the unique central-extension parameter consistent with continuous-unitary representations. Provides the structural basis for the Galilean Lie algebra's $[\hat{p}_i, \hat{K}_j] = i m \delta_{ij}$ commutator.

- **Wigner's classification (1939).** Classification of unitary irreducible representations of the Poincaré group; identifies mass and spin as the Casimir invariants $P^\mu P_\mu = m^2 c^2$ and $W^\mu W_\mu = -m^2 c^2 s(s+1)$ (Pauli-Lubanski). Provides the structural basis for the substrate-level identification of mass and spin as Casimir-invariant labels.

- **Stone's theorem.** A strongly continuous one-parameter unitary group $\{U_t\}$ on a Hilbert space has a unique self-adjoint generator $\hat{H}$ such that $U_t = e^{-i\hat{H}t/\hbar}$ (Stone 1932). Used in §7.B as mathematical infrastructure; the *Forcing Paper application* of Stone's theorem (Paper #4 for time-translations, Paper #12 for spatial-translations) is downstream and not invoked here.

- **Central extension.** A Lie algebra $\mathfrak{g}$ has a central extension $\tilde{\mathfrak{g}}$ if there exists a Lie algebra structure on $\tilde{\mathfrak{g}} = \mathfrak{g} \oplus \mathbb{R}$ such that the $\mathbb{R}$ summand is in the center (commutes with all elements) and $\tilde{\mathfrak{g}}$ contains $\mathfrak{g}$ as a quotient. The Galilean Lie algebra's central extension by mass is the substrate-level structural source of the mass-parameter appearing in non-relativistic dynamical equations.

- **Conformal group $O(4,2)$.** The group of conformal transformations on 4-dimensional Minkowski spacetime: Poincaré + dilations + special conformal transformations. Has 15 generators (10 Poincaré + 1 dilation + 4 special conformal). Excluded as over-strong in §8.A.6.

### 10.4 Status

This is Paper M-4 of the ED Primitive-Forcing M-series. With M-4 closed:

- **P03 (Adjacency Homogeneity) is FORCED** under Routes A + C.
- **P13 (Time Homogeneity) is FORCED** under Routes A + D.
- **GAL (Galilean Symmetry with central extension) is FORCED** under Routes B + D at non-relativistic scope.
- **POI (Poincaré Compatibility) is partially forced** under Routes B + D at relativistic scope; honest residue: choice "Poincaré rather than de Sitter / anti-de Sitter" under operational adequacy at empirical local-flatness.

### 10.5 Downstream Updates triggered by M-4 closure

Papers #1, #4, #6, #7, #12, #15, #17 require §3.0 Primitive Inputs updates. Per the pattern of `UPDATE_PLAN_after_M1.md`, adapted for M-4:

> "**Upstream status (2026 update):** The joint symmetry cluster (P03 adjacency homogeneity, P13 time homogeneity, GAL Galilean symmetry with central extension, POI Poincaré compatibility) is now forced upstream by Meta-Paper M-4 (2026), under joint Routes A (information-theoretic uniformity), B (symmetry-minimality + compositional closure with Bargmann central extension), C (adjacency-preserving propagation inherited from M-3), and D (structural-normative recovery of empirical relativistic-and-non-relativistic physics). The Inönü-Wigner contraction from Poincaré to Galilean at $c \to \infty$ supplies the connection between regimes. Honest residue: the choice of Poincaré rather than de Sitter / anti-de Sitter at relativistic scope reduces to operational adequacy + empirical local-flatness assumption. The present paper treats the symmetry cluster as a derived structural result of M-4."

A companion deliverable `UPDATE_PLAN_after_M4.md` should be produced.

### 10.6 Series Context

Cumulative status across the ED Primitive-Forcing M-series after M-4 closure:

- **M-1 (2026):** P09 $U(1)$ polarity — FORCED.
- **M-2 (2026):** P04 four-band partition + bandwidth additivity — FORCED.
- **M-3 (2026):** P11 commitment irreversibility — FORCED.
- **M-4 (this paper, 2026):** Joint symmetry cluster P03 + P13 + GAL + POI — FORCED (with honest cosmological-curvature residue).
- **M-5 (next):** P07 channel structure (under Routes C + E).
- **M-6 onward:** V1 + V5 existence as rule-types; HYD scale-separation; residue closures for P06, P10, P12, HOL, DEC, IND, THN.

After M-4, **the displaced-postulate critique no longer applies to** ~15 of 19 Forcing Papers — coverage crosses the 75% threshold. The remaining 4 papers (mainly #5 gauge fields, #8 DCGT, #9 substrate gravity, #10 BH-Hawking) depend on the residue-cluster primitives (P10 rule-type, HYD, HOL, DEC, V5) that will be addressed in M-5 onward.

### 10.7 Honest closing

This paper does not eliminate all unforced roots. The choice "Poincaré rather than de Sitter at relativistic scope" remains residue under operational-adequacy local-flatness. The meta-substrate framework $\{C^*\}$ itself remains the recursion-stopping commitment.

What M-4 achieves: the conversion of the joint symmetry cluster from "load-bearing input to seven Forcing Papers" to "forced structural result of joint-route convergence under $\{C^*\}$ + M-1 + M-2 + M-3 + standard background mathematics." The substrate's primitive symmetry content is now explicitly named and structurally derived; Stone's theorem applications in Papers #4 + #12 + the Galilean / Poincaré covariance arguments in Papers #6 + #7 + #15 all operate on substrate-derived rather than substrate-postulated symmetries.

The kernel-level structural coherence of the ED program advances another step. M-5 will address P07 (channel structure) and the remaining residue-cluster primitives.

---

**End of Paper M-4.**
