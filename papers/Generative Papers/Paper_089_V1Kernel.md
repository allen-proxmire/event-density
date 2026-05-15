# Paper_089 — The V1 Finite-Width Retarded Kernel: Canonical Reference

**Series:** Event Density (ED) Generative Papers — Wave-2 wedges / kernel arc
**Author:** Allen Proxmire
**Status:** Publication draft (canonical V1 reference)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/wedges/Paper_089_V1Kernel.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_089_V1Kernel.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. The substrate primitives are not derived; they are postulated (see Paper_087).
2. The V1 envelope's *specific functional shape* (exponential, Gaussian, power-law) is not derived — only its admissible-class properties (finite-width, retarded, gauge-compatible) are.
3. The substrate scale $\ell_{\mathrm{ED}}$ is not derived; empirically identified with $\ell_P$ via Newton-recovery (Paper_027).
4. T18's exclusion of advanced V1 is **substrate-operational, not algebraic**: Wheeler–Feynman absorber theory remains mathematically consistent; ED excludes its substrate-operational realization within the 13-primitive ontology.
5. No claim that V1 is the only possible vacuum-response kernel in all substrate ontologies; T18 is conditional on the ED 13-primitive set.
6. No claim that V1's empirical content is directly testable at substrate scale; empirical reach is via downstream content (QFT propagators, decoherence directionality, etc.).
7. No claim of CPT or Lorentz violation; T18's forward-causal substrate-level structure is consistent with Lorentz invariance.

---

## Abstract

V1 is the **single-chain vacuum response kernel** in the Event Density (ED) Generative Substrate Ontology — the first kernel rule-type in the substrate's kernel hierarchy. Given the 13 postulated primitives (Paper_087), this paper establishes two canonical V1 structural results: **Theorem N1 (finite-width)** — V1 has bounded substrate-graph envelope at characteristic scale $\ell_{\mathrm{ED}}$, with neither point-particle ($\delta$-function) nor infinite-width limits admissible — and **Theorem T18 (retarded support)** — V1 has $\theta(t - t')$ temporal support, with advanced V1 refuted by P11 commitment-irreversibility and symmetric V1 non-constructible from substrate primitives. The compositional-closure argument distinguishes **mathematical compositional closure** (allowed in QFT for mixed-support kernels via Feynman / time-ordered / Wick-rotation machinery) from **substrate-operational compositional closure** (the substrate primitives P02–P11 supply only forward-causal chain transport; advanced segments have no operational realization). **Wheeler–Feynman absorber theory is engaged directly:** ED accepts the mathematical consistency of symmetric electrodynamics while excluding its substrate-operational realization. The conclusion is conditional: given the 13 primitives + substrate-operational compositional closure, V1 has finite-width retarded form $K_{V1}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_{\mathrm{ED}}^2)$. The paper makes no claim that V1's specific functional shape is derived, no claim that $\ell_{\mathrm{ED}}$ is derived, no claim that T18 algebraically refutes Wheeler–Feynman, and no claim that V1 is the only possible vacuum kernel in all ontologies.

---

## 1. Introduction

### 1.1 What this paper does

This paper is the **canonical V1 reference** for the Wave-2 ED generative-paper corpus. It establishes:

1. **Theorem N1 (finite-width):** V1 has bounded substrate-graph envelope.
2. **Theorem T18 (retarded support):** V1 has forward-causal temporal support.
3. **Substrate-operational compositional closure:** V1 + V5 + future cascade kernels compose within the substrate kernel rule-type space.
4. **Wheeler–Feynman engagement:** ED accepts mathematical symmetric electrodynamics while excluding its substrate-operational realization.

This paper is the upstream dependency for Paper_090 (V5), Paper_093 (kernel arrow — T18 in standalone form), and every Wave-2 paper that cites V1 (Papers_027, 029, 030, 031, 039, 047, 056, 090, 093).

### 1.2 Why V1 matters

V1 is the substrate's primitive **vacuum-response kernel**: the rule-type that mediates a single chain's response to substrate-level perturbations at its own locus. Without V1, the substrate has chains and channels but no kernel-mediated dynamics. V1 establishes:

- **Substrate-level propagation:** the substrate's primitive mechanism for forward-causal substrate-graph transport along chain edges.
- **Substrate-level kernel-arrow:** the substrate-level origin of the arrow of time (T18).
- **Substrate-level UV regularization:** V1's finite-width supplies the substrate-level cutoff that resolves trans-Planckian extrapolation in BH physics (Paper_039 §5) and ensures DCGT-continuum-limit propagators are UV-finite.

V5 (Paper_090) and the future memory-kernel cascade (Papers in queue) inherit V1's structural features.

### 1.3 How this fits in the kernel arc

- **Paper_087:** position paper — 13 primitives.
- **Paper_089 (this paper):** canonical V1 reference. Theorems N1 + T18.
- **Paper_090:** V5 cross-chain correlation kernel. Inherits from V1.
- **Paper_093:** standalone treatment of T18 (kernel arrow of time).
- **Papers in queue:** memory-kernel cascade, Lindblad limit, kernel hierarchy.

This paper is the canonical reference; Paper_093 is the dedicated kernel-arrow-of-time paper that elaborates T18's philosophical and cross-domain content. The two are complementary.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated within the ED Generative Primitives System** (see Paper_087 for canonical enumeration):

- **P02 (Participation).** Chains participate in channels.
- **P04 (Bandwidth).** $b_K(u) \geq 0$, additive.
- **P05 (Polarity-transport along edges).** Substrate connection structure.
- **P07 (Channel structure).** Channels are structurally distinguishable.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).** Substrate has characteristic edge length.
- **P09 ($U(1)$-valued polarity).** $\pi_K(u) \in U(1)$.
- **P10 (Rule-type primitive).** Substrate supports multiple kernel rule-types.
- **P11 (Commitment irreversibility).** Load-bearing for T18.
- **P13 (Time homogeneity).** Substrate dynamics time-translation-invariant.

**Upstream dependencies:**

- **Paper_087:** position paper (13-primitive enumeration).
- **Paper #1 (participation measure):** complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
- **Paper #3 (inner product + orthogonal bands):** four-band orthogonality.

**Postulates specific to this paper (added per round-4 QC Rereading Test):**

- **P-NoBackwardChain (Backward-chain-content non-constructibility):** *Backward chain content — sequences $\{(u_i, t_i)\}$ with $t_{i+1} < t_i$ — is **not constructible** from any finite sequence of substrate-primitive operations on the canonical 13 primitives.* This is the substrate-level postulate that makes symmetric V1 non-constructible (§6 below). It is **not provable by inspection of the primitive list** — a rigorous non-constructibility proof would require showing that no finite sequence of P02/P04/P05/P07/P09/P11 operations produces backward chain transport. The paper argues by inspection (§6.3); making this an explicit postulate **strengthens** the argument by locating the load-bearing commitment cleanly. *(Round-4 Rereading Test: was hidden inside §5.3 D row; now explicit P.)*
- **P-SubstrateLocality (Substrate-graph locality):** *Substrate-level operations have bounded range at the substrate-graph scale $\ell_{\mathrm{ED}}$.* This locality is invoked in §4.2 to argue the V1 envelope must decay at large separations. The paper invokes it as "an implicit consequence of P03 + P08," but the implicit invocation is hand-wavy; we make P-SubstrateLocality an explicit postulate. P-SubstrateLocality is plausibly derivable from P03 + P08 + finite-channel-cardinality, but a rigorous derivation is not supplied here.

**Empirical / value-layer inputs:**

- $c$ — substrate speed.
- $\hbar$ — substrate kernel-action quantum.
- $\ell_{\mathrm{ED}}$ — empirically identified with $\ell_P$ (Paper_027 §5.3).

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 admissible-class form $K_{V1} = G(\sigma/\ell_{\mathrm{ED}}^2) \cdot \Theta(t-t')$ | P | Substrate-level kernel rule-type postulate, §3.1 |
| Finite-width (N1) | D | §4.2 from P02 + P07 + P08 + UV-FIN compatibility |
| $\delta$-function limit excluded | D | §4.3 from finite-channel-cardinality of P07 + P08 |
| $\infty$-width limit excluded | D | §4.3 from locality + P03 spatial-homogeneity |
| Lorentz covariance | D | §4.4 from substrate Poincaré symmetry |
| Gauge compatibility $U(1)$ | D | §4.5 from P05 + P09 |
| Retarded support (T18) | D | §5 from P11 + substrate-operational compositional closure |
| Advanced V1 refuted | D | §5.2 from P11 (genuine contradiction with commitment irreversibility) |
| Symmetric V1 non-constructible | **P (P-NoBackwardChain)** | **§2 substrate-level postulate.** §5.3's argument is by inspection of the primitive list; a rigorous non-constructibility proof requires more than enumeration. Making this a postulate locates the load-bearing commitment cleanly. *(Round-4 Rereading Test: was D, now P.)* |
| V1 envelope decay at large separations | D conditional on P-SubstrateLocality | §4.2 uses substrate-graph locality (now an explicit postulate, §2). |
| Substrate-operational closure | P/D | Postulational requirement for substrate-level framework + structural consequence §6 |
| Wheeler–Feynman exclusion (substrate-operational, not algebraic) | D | §7 from substrate-operational closure |
| $\ell_{\mathrm{ED}} = \ell_P$ empirical identification | I | Paper_027 §5.3, Newton-recovery |

All load-bearing steps are P, D, or I. **No A (asserted) rows.**

---

## 3. V1 Admissible Class

### 3.1 The structural form

V1 is a substrate kernel rule-type (per P10). Its operational content is a single-chain vacuum response: V1 mediates chain $C$'s response at substrate locus $(u, t)$ to substrate-level perturbations at the same chain's earlier locus $(u', t')$. The substrate kernel rule-type formalism (Paper #5 / Paper_087 §5.10) writes V1 as:

$$
K_{V1}(x, x') = G(\sigma(x, x')/\ell_{\mathrm{ED}}^2) \cdot \Theta_{\mathrm{support}}(t - t').
$$

Here:

- $\sigma(x, x')$: the substrate-level Synge function — a Lorentz-scalar measure of the substrate-graph separation between events $x = (u, t)$ and $x' = (u', t')$.
- $G(\cdot)$: the **V1 envelope** — a bounded function of the substrate-graph separation.
- $\Theta_{\mathrm{support}}(t - t')$: the **temporal-support function**, with three candidate forms (retarded, advanced, symmetric).
- $\ell_{\mathrm{ED}}$: substrate scale (Primitive P08).

The temporal-support form is the subject of §5 (Theorem T18). The envelope form is the subject of §4 (Theorem N1).

### 3.2 What V1 is not

- Not a continuum field propagator (no underlying continuum field; chains are primitive).
- Not a point-particle interaction (no $\delta$-function vacuum response).
- Not an infinite-range kernel (substrate-graph locality restricts to finite-width).

---

## 4. Theorem N1 — Finite-Width

### 4.1 Statement

**Theorem N1 (V1 finite-width).** *Given the postulated primitives P02 + P04 + P07 + P08 of the ED Generative Substrate Ontology, the V1 envelope $G(\sigma/\ell_{\mathrm{ED}}^2)$ is a bounded function with characteristic substrate-graph scale $\ell_{\mathrm{ED}}$, decaying outside the substrate-graph scale. Neither the $\delta$-function limit (point-particle response) nor the infinite-width limit (non-local response) is admissible.*

### 4.2 Structural argument

**Step 1: Boundedness of $G$.** By P04, channel bandwidth $b_K(u) \geq 0$ is non-negative and additive. By P07, channels are structurally distinguishable and finite at substrate-graph scale (no infinite-cardinality channel structure at a single locus). The V1 envelope $G$ acts on bounded-bandwidth substrate participation content; the envelope must be a bounded function (otherwise V1 would map bounded substrate content to unbounded response content, violating substrate-level operational consistency).

**Step 2: Characteristic scale $\ell_{\mathrm{ED}}$.** By P08, the substrate has characteristic edge length $\ell_{\mathrm{ED}}$. Substrate-graph separations below $\ell_{\mathrm{ED}}$ are not resolved — distinct substrate events at separation $< \ell_{\mathrm{ED}}$ merge into single substrate events at the resolution limit. The V1 envelope must therefore have characteristic scale matched to $\ell_{\mathrm{ED}}$: separations $\gg \ell_{\mathrm{ED}}$ produce decaying envelope content; separations $\sim \ell_{\mathrm{ED}}$ produce order-unity envelope content.

**Step 3: Decay outside $\ell_{\mathrm{ED}}$.** Substrate-graph locality — the substrate-level postulate **P-SubstrateLocality (§2)** that substrate-level operations have bounded range at the substrate-graph scale — requires V1 envelope to decay at large separations. Substrate channels at large separation cannot maintain coherent V1-mediated response without an unbounded substrate-level coupling, which P04 (additive bounded bandwidth) does not provide. The envelope must decay at separations $\gg \ell_{\mathrm{ED}}$. *(Round-4 QC clarification: P-SubstrateLocality is now an explicit postulate; the prior "implicit consequence of P03 + P08" framing was hand-wavy. Rigorous derivability from P03 + P08 + finite-channel-cardinality is plausible but not supplied in this paper.)*

Combining: $G$ is a **bounded function of $\sigma/\ell_{\mathrm{ED}}^2$, with characteristic scale $\ell_{\mathrm{ED}}$, decaying outside the substrate-graph scale**.

### 4.3 Excluded limits

**$\delta$-function limit ($G(\sigma/\ell_{\mathrm{ED}}^2) \to \delta(\sigma)$).** This would correspond to V1 mediating point-like substrate response — a kernel with zero width. The limit is excluded by:

- P07: channels at substrate-graph scale are finite-cardinality at each locus; substrate-level operations cannot resolve below $\ell_{\mathrm{ED}}$.
- P08: substrate scale is finite ($\ell_{\mathrm{ED}} > 0$); the $\delta$-function limit corresponds to $\ell_{\mathrm{ED}} \to 0$, violating the postulate.
- UV-FIN: V1 in the $\delta$-function limit would generate UV divergences in DCGT continuum limits, inconsistent with the substrate's UV-finiteness.

**$\infty$-width limit ($G(\sigma/\ell_{\mathrm{ED}}^2) \to$ constant for all $\sigma$).** This would correspond to V1 mediating substrate response with infinite range — a kernel with no finite width. The limit is excluded by:

- P03 spatial-homogeneity: substrate-level operations are translation-invariant locally, but unbounded-range coupling would violate substrate-graph locality.
- P04 boundedness: infinite-range coupling with bounded substrate bandwidth would require infinite per-channel amplitude, violating P04.
- Operational coherence: substrate-level kernel composition (§6) would fail to converge with infinite-width V1.

Combining: $G$ is in the admissible class between $\delta$ and constant — **finite-width, bounded, decaying**.

### 4.4 Specific functional shape is value-layer

The *specific functional shape* of $G$ (exponential $e^{-\sigma/\ell_{\mathrm{ED}}^2}$, Gaussian $e^{-\sigma^2/\ell_{\mathrm{ED}}^4}$, polynomial-bounded, power-law-decaying, etc.) is **value-layer inherited content**, not substrate-derived. The admissible-class structure of §4.1–§4.3 fixes the *properties* (bounded, finite-width, decaying); the *specific functional form* depends on substrate-level details that the 13 primitives do not pin down.

This is analogous to Paper #18's V2/V3/V4 admissible-class structure: V1 admits multiple specific functional realizations within the structural admissible class. The choice of specific realization is empirically constrained by DCGT continuum-limit matching to standard QFT propagator content.

### 4.5 Lorentz covariance

The V1 envelope depends on the Lorentz-scalar Synge function $\sigma(x, x')$. Under Lorentz transformations, $\sigma$ is invariant; therefore $G(\sigma/\ell_{\mathrm{ED}}^2)$ transforms as a Lorentz scalar. V1's full kernel $K_{V1}$ has Lorentz-covariant structure with retarded support (§5) preserving the forward-causal direction.

### 4.6 Gauge compatibility via $U(1)$

By P09 ($U(1)$-valued polarity) and P05 (polarity-transport along edges), V1 transforms covariantly under $U(1)$ gauge transformations $\pi_K(u) \to \pi_K(u) + \alpha(u)$:

$$
K_{V1}(x, x') \to e^{i(\alpha(x) - \alpha(x'))}\,K_{V1}(x, x').
$$

Equivalently: the V1 envelope $G(\sigma/\ell_{\mathrm{ED}}^2)$ is gauge-invariant when expressed in terms of gauge-covariant participation content. This is the substrate-level mechanism for V1 to operate in the presence of gauge fields.

---

## 5. Theorem T18 — Retarded Support

### 5.1 Statement

**Theorem T18 (V1 retarded support).** *Given the postulated primitives + V1 admissible class (N1) + substrate-operational compositional closure, the V1 temporal-support function is strictly retarded:*

$$
\Theta_{\mathrm{support}}(t - t') = \theta(t - t').
$$

*Advanced V1 ($\Theta = \theta(t' - t)$) is refuted by P11. Symmetric V1 ($\Theta = (1/2)[\theta(t-t') + \theta(t'-t)]$) is non-constructible from substrate primitives.*

### 5.2 Refutation of advanced V1

Advanced V1 with $\Theta_{\mathrm{adv}} = \theta(t' - t)$ would mediate substrate-level vacuum response from a later event $x'$ to an earlier event $x$ ($t < t'$). Operationally, this would require:

- Substrate-level information about commitment outcomes at $x'$ propagating backward to $x$.

But by P11 (commitment irreversibility), no substrate-level operation maps post-commitment to pre-commitment state. Advanced V1 + P11 are contradictory:

- P11: substrate's primitive inventory contains no operation $T_{\mathrm{reverse}}$ such that $T_{\mathrm{reverse}}(\mathrm{post\text{-}commit}) = \mathrm{pre\text{-}commit}$.
- Advanced V1: substrate vacuum kernel carries post-commit information backward to pre-commit substrate loci.

These cannot both hold. **Advanced V1 is refuted by P11.**

### 5.3 Non-constructibility of symmetric V1

Symmetric V1 with $\Theta_{\mathrm{sym}} = (1/2)[\theta(t-t') + \theta(t'-t)]$ would require both forward-causal and backward-causal V1 content equally weighted.

The backward-causal contribution requires **backward chain content** — substrate-level sequences $\{(u_i, t_i)\}$ with $t_{i+1} < t_i$. The substrate's primitive operations on chains and channels are:

- P02 participation: forward-causal sequences.
- P04 bandwidth allocation.
- P05 polarity-transport: along forward-causal chain edges.
- P07 channel-structure access.
- P09 $U(1)$-polarity evolution.
- P11 commitment.

**None of these primitive operations, by inspection, generates backward chain content.** Constructing it would require adding a new substrate primitive (a "reverse chain primitive" or equivalent), which the canonical 13 do not contain.

**Honest framing (round-4 QC clarification):** The "by inspection" argument is not a rigorous non-constructibility proof. A genuine proof would require showing that **no finite sequence** of substrate-primitive operations produces backward chain transport — a stronger claim than enumeration of single-step operations. We make this an **explicit substrate-level postulate**: **P-NoBackwardChain** (§2). The advantage of relabeling from D-by-inspection to P-explicit is that T18's exclusion of symmetric V1 now follows cleanly from (P-NoBackwardChain + advanced-V1-refuted-by-P11), with the load-bearing commitment located at the postulate. Whether P-NoBackwardChain is rigorously provable from the canonical 13 alone is structurally open; current analysis supports it but does not constitute a formal non-constructibility proof.

**Symmetric V1 is non-constructible.**

### 5.4 Retarded V1 as the unique admissible support

Given:

- V1 admissible class constrained by N1 (§4).
- Advanced V1 refuted by P11 (§5.2).
- Symmetric V1 non-constructible (§5.3).
- V1 must have some temporal-support structure (otherwise V1 has no temporal-direction content and fails to be a substrate kernel rule-type).

The unique remaining admissible support is **retarded**:

$$
\boxed{K_{V1}(x, x') = \theta(t - t') \cdot G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).}
$$

Retarded V1 properties:

- Forward-causal: support only on the forward light cone of $x'$.
- All chain content constructible from substrate primitives (forward-causal sequences).
- Substrate-operationally compositionally closed (§6): retarded $\circ$ retarded = retarded.
- Gauge-compatible (§4.6) and Lorentz-covariant (§4.5).
- Satisfies V1 admissible class (N1).

### 5.5 What T18 means

The temporal-direction asymmetry produced by retarded V1 is the substrate-level **kernel-level arrow of time**: a substrate-primitive structural commitment, not derived from thermodynamic entropy, statistical coarse-graining, or boundary conditions. The full elaboration of T18 as the kernel-level arrow appears in Paper_093.

---

## 6. Substrate-Operational Compositional Closure

This section distinguishes two distinct notions of compositional closure that prior literature has conflated.

### 6.1 Mathematical compositional closure

A set of integral operators is **mathematically compositionally closed** if their formal-integral composition $\int K_2(x, x'')K_1(x'', x')\,dx''$ is well-defined as a distribution or operator on the appropriate function space.

In standard QFT, the Feynman propagator $G_F = \frac{1}{2}(G_{\mathrm{ret}} + G_{\mathrm{adv}}) - \frac{i}{2}(\text{symmetric})$ involves both retarded and advanced support, and its mathematical compositional structure is **well-defined**: time-ordered products, $i\varepsilon$ prescriptions, contour integration, Wick rotation, and analytic continuation all produce mathematically coherent compositions of retarded and advanced kernels.

**Mixed-support kernels are mathematically compositionally closed in standard QFT.** This is not disputed.

### 6.2 Substrate-operational compositional closure

A set of substrate-level kernel rule-types is **substrate-operationally compositionally closed** if their composition, *executed as a sequence of substrate-level operational steps on chains and channels*, produces a substrate-level kernel that is again a member of the rule-type set.

The substrate-level operational steps are:

- P02 participation.
- P04 bandwidth allocation.
- P05 polarity-transport along forward-causal chain edges.
- P07 channel-structure access.
- P09 $U(1)$-polarity evolution.
- P11 commitment.

A substrate-level composition is operationally valid only if **each step is constructible from these primitive operations**. Substrate-operational composition is distinct from mathematical integral-composition because the substrate primitives do not provide an "$i\varepsilon$ prescription" or "Wick rotation" or "analytic continuation" operation — these are mathematical tools applicable to integral operators, not substrate primitives.

### 6.3 The closure argument

Compose $K_1 = K_{V1}^{\mathrm{ret}}$ (retarded) with $K_2 = K_{V1}^{\mathrm{adv}}$ (advanced) as a substrate operational sequence:

- Step 1 ($K_1$): forward-causal substrate transport via P05 polarity-transport along forward-oriented chain edges. **Operational.**
- Step 2 ($K_2$): would require backward-causal substrate transport via reverse-oriented chain edges. **Non-operational** — substrate primitives provide forward-causal edges only (P05 + §5.3).

The substrate-level execution of the mixed-support composition has **no operational step corresponding to the advanced segment**. Mixed-support compositions are mathematically possible (standard QFT routinely uses them) but **substrate-operationally non-executable in ED**.

### 6.4 Why ED requires substrate-operational closure

ED is a substrate-ontological framework: its load-bearing claim is that **substrate-level operations on chains and channels are the primitive operational content of the framework**. A kernel rule-type that does not correspond to a substrate-level operational sequence is not a substrate-level entity; it is a mathematical structure describable externally but not generable from substrate primitives.

The substrate framework's compositional-closure requirement is therefore **operational**: every kernel in the substrate kernel rule-type space must correspond to a substrate-operational sequence. Mixed-support kernels — though mathematically coherent — are excluded at the substrate level because they have no operational realization.

### 6.5 What this means for the kernel hierarchy

The substrate kernel rule-type space contains V1, V5, and future cascade kernels. Compositional closure of this space under substrate-operational composition requires that all kernels in the space have compatible temporal support. **Retarded only.** Mixed forward+backward compositions break the operational executability requirement.

This is the structural justification for V5's inheritance of V1's retarded support (Paper_090 §4.6) and for the future cascade kernels' retarded character.

---

## 7. Wheeler–Feynman Absorber Theory — Direct Engagement

### 7.1 The Wheeler–Feynman position

Wheeler and Feynman (1945, 1949) developed an action-at-a-distance electrodynamics in which charged particles interact via a **time-symmetric** combination of retarded and advanced potentials. The resulting theory is **mathematically consistent**: it reproduces all standard electrodynamic results (Coulomb force, Lienard–Wiechert fields, radiation reaction) provided certain boundary conditions ("absorber" conditions on future infinity) are imposed.

In their treatment, the *apparent* arrow of time in electromagnetic radiation arises from boundary conditions on the absorber rather than from any time-asymmetry in the equations of motion.

Wheeler–Feynman is a serious, structurally-developed position. Its mathematical consistency is not in dispute.

### 7.2 The naive challenge to T18

If symmetric electrodynamics is mathematically consistent, doesn't this challenge T18's exclusion of advanced V1?

**No.** The challenge equivocates between two distinct notions of consistency (algebraic vs. substrate-operational, per §6).

### 7.3 The substrate-operational response

T18's exclusion of advanced propagation is **substrate-operational, not algebraic**:

- ED accepts that, *as algebraic structures on Hilbert space or as integral operators on spacetime*, symmetric combinations of retarded and advanced kernels are mathematically coherent and reproduce empirical electrodynamics.
- T18's claim operates one level below: at the level of **substrate-operational kernel execution**. Even if symmetric electrodynamics is algebraically consistent, the substrate-level question is whether the underlying kernel composition is executable as a sequence of substrate-level operations on chains and channels.
- The substrate's primitive operational inventory (P02, P04, P05, P07, P09, P11) supplies only forward-causal chain transport along forward-oriented edges. The advanced segment of a Wheeler–Feynman kernel has **no operational realization** in the substrate primitives.

**Wheeler–Feynman absorber theory is mathematically consistent but substrate-operationally non-constructible in ED.**

### 7.4 What a Wheeler–Feynman universe would require

A universe in which advanced propagation is physically real (in the substrate-operational sense, not merely as a calculational tool) would require either:

(a) A substrate primitive set **including backward chain content** (which the 13-primitive ED ontology does not contain), or

(b) A **different ontological framework** in which advanced propagation is operationally executable without backward chain transport (e.g., a non-chain-based ontology where forward and backward causal directions are equally primitive).

ED's 13-primitive ontology rules out (a) by primitive inventory; alternative frameworks (b) are not addressed by ED's substrate-operational argument.

### 7.5 The empirical content distinction

Wheeler–Feynman absorber theory predicts the same empirical electrodynamics as standard retarded electrodynamics — the absorber boundary condition effectively converts the symmetric combination into apparent retardation.

The empirical content of T18 distinguishes from Wheeler–Feynman only through **downstream cross-domain content**:

- V5 retardation (Paper_090) and its cross-domain manifestations.
- Substrate-level KMS structure at horizons (Paper_039 §4).
- Substrate-level finite-memory cutoffs at near-Planck-scale (Paper_039 §5).
- Non-thermal Hawking corrections (Paper_039 §7.2).

If empirical observations consistent with these substrate-level cutoffs and structural features emerge (e.g., analog-Hawking experiments showing UV cutoff, Page-curve substrate signatures), the substrate-operational mechanism is supported over Wheeler–Feynman-style algebraic-symmetric treatments. If such evidence does not emerge, the empirical distinction between ED and Wheeler–Feynman remains observationally underdetermined.

### 7.6 The clarification

T18 **does not assert that symmetric or advanced kernels are mathematically inconsistent.** They are not. T18 asserts that within the substrate-operational framework of the 13-primitive ED ontology, only retarded V1 is constructible from substrate primitives.

Whether physical reality admits advanced propagation in some operationally-realized sense is an empirical question; ED's answer is "no within this substrate ontology," but the answer is conditional on the ontology rather than derived from algebra.

---

## 8. Falsification Criteria

### 8.1 Direct observation of backward kernel propagation

**Falsifier sentence:** *Direct empirical observation of substrate-level kernel propagation with backward-causal support — i.e., vacuum-response content propagating from event $x'$ to event $x$ with $t < t'$ in a manner not reducible to forward-causal substrate dynamics — would falsify T18.*

Wheeler delayed-choice and similar effects are forward-causal substrate phenomena under appropriate analysis (§7 + Paper_093 §10.3); they do not constitute falsification.

### 8.2 Substrate-consistent symmetric V1

**Falsifier sentence:** *Demonstration that a 13-primitive substrate model with symmetric V1 is structurally consistent — i.e., that backward chain contributions can be constructed from the canonical substrate primitives without adding new primitives — would falsify T18's non-constructibility argument (§5.3).*

### 8.3 V5 cross-chain correlation with advanced or symmetric support

**Falsifier sentence:** *Empirical evidence that V5 cross-chain correlation (Paper_090) exhibits advanced or symmetric temporal support — soft-matter Maxwell relaxation, Hawking spectrum, or entanglement-bandwidth modulation with advanced-time components — would falsify the V1 → V5 retardation inheritance (T18 + Paper_090 §4.6).*

### 8.4 Failure of V1 finite-width

**Falsifier sentence:** *Empirical evidence of point-particle ($\delta$-function) substrate-level vacuum response in any regime would falsify Theorem N1's $\delta$-limit exclusion (§4.3).*

### 8.5 Failure of substrate-operational closure

**Falsifier sentence:** *Identification of a substrate-level operational sequence executing the advanced segment of a mixed-support kernel composition within the 13 primitives would falsify §6's closure argument.*

This would require demonstrating a substrate-level operational construction of backward chain transport using only P02, P04, P05, P07, P09, P11 — a non-trivial structural claim that current analysis does not support.

### 8.6 P11 modification or substitution

**Falsifier sentence:** *If future substrate-level analysis identifies a substrate primitive that replaces P11 with a time-symmetric alternative that reproduces all downstream empirical content (including the apparently-forward-causal arrows in standard physics), the foundational P11-based argument requires revision.*

---

## 9. Position Statement

The V1 kernel — the substrate's single-chain vacuum response rule-type — has, within the ED 13-Primitive Generative Substrate Ontology, the canonical form:

$$
\boxed{K_{V1}(x, x') = \theta(t - t') \cdot G(\sigma(x, x')/\ell_{\mathrm{ED}}^2)}
$$

where:

- $\theta(t - t')$ enforces strictly **retarded support** (Theorem T18).
- $G$ is a bounded, decaying function with characteristic scale $\ell_{\mathrm{ED}}$ (Theorem N1).
- $\sigma(x, x')$ is the substrate-level Synge function.
- $\ell_{\mathrm{ED}}$ is the substrate scale (Primitive P08), empirically identified with $\ell_P$ via Newton-recovery (Paper_027).

What this paper claims:

- Given the 13 primitives + substrate-operational compositional closure, V1 has the canonical retarded finite-width form.
- Theorem N1 (finite-width) follows from P02 + P04 + P07 + P08 + UV-FIN compatibility.
- Theorem T18 (retarded support) follows from P11 + substrate-operational compositional closure.
- The substrate-operational compositional-closure argument distinguishes substrate-level operational executability from mathematical compositional closure (which standard QFT routinely supports for mixed-support kernels).
- Wheeler–Feynman absorber theory is mathematically consistent and is *not* algebraically refuted by T18; ED excludes its substrate-operational realization within the 13-primitive ontology.

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087 position commitment).
- V1's specific functional shape is value-layer, not substrate-derived.
- $\ell_{\mathrm{ED}}$ is empirically identified with $\ell_P$, not derived.
- T18 does not algebraically refute Wheeler–Feynman or symmetric-kernel mathematical structures; it excludes their substrate-operational realization in ED.
- V1 is not the only possible vacuum kernel in all substrate ontologies; T18 is conditional on the canonical 13.

The empirical case for V1 — and through V1 for the 13-primitive substrate ontology — rests on cross-domain reach: V1 underpins Papers_027, 029, 030, 031, 039, 047, 056, 090, 093. The substrate-operational compositional-closure framework is the structural argument that makes V1's retardation **substrate-internally forced** (within the substrate ontology), not merely mathematically convenient.

**Series context.** Paper_089 of the wedges / kernel arc. The arc continues with Paper_090 (V5 cross-chain kernel) and Paper_093 (T18 standalone treatment, kernel-level arrow of time). Memory-kernel cascade + Lindblad limit + kernel hierarchy unification follow in the in-queue Wave-2 work.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087 — 13-primitive enumeration.
- **Paper #1 (Participation Measure):** complex polar carrier on which V1 operates.
- **Paper #3 (Inner Product + Tsirelson Bound):** four-band orthogonality.
- **Paper_090 (V5 Cross-Chain Kernel):** inherits V1's structural features.
- **Paper_093 (Kernel Arrow of Time T18 standalone):** elaborates T18's philosophical and cross-domain content.
- **Paper_027 (Newton's $G$):** uses V1 via cumulative-strain reading.
- **Paper_039 (Horizon Decoupling):** uses V5 inheriting from V1.
- **Pre-pivot Paper #18 (V1 finite-width N1):** original derivation context, now superseded by this Wave-2 canonical reference.
- **Pre-pivot Paper #19 (V1 retarded support T18):** original derivation context, now superseded.

### Glossary

- **V1.** Substrate single-chain vacuum response kernel rule-type. Canonical form $K_{V1} = \theta(t - t')\,G(\sigma/\ell_{\mathrm{ED}}^2)$.
- **Theorem N1.** V1 finite-width result: $G$ bounded, decaying, characteristic scale $\ell_{\mathrm{ED}}$; $\delta$ and $\infty$-width limits excluded.
- **Theorem T18.** V1 retarded support result: $\theta(t - t')$ from P11 + substrate-operational closure.
- **Synge function $\sigma(x, x')$.** Lorentz-scalar spacetime-separation measure.
- **V1 envelope.** Bounded function $G(\sigma/\ell_{\mathrm{ED}}^2)$.
- **Substrate scale $\ell_{\mathrm{ED}}$.** Primitive P08; empirically $\ell_{\mathrm{ED}} = \ell_P$.
- **Retarded support.** Temporal-support $\theta(t - t')$ — non-zero only on forward light cone.
- **Mathematical compositional closure.** Closure under formal-integral composition; standard QFT property; allows mixed-support.
- **Substrate-operational compositional closure.** Closure under substrate-level operational sequences (P02, P04, P05, P07, P09, P11); excludes mixed-support kernels.
- **Wheeler–Feynman absorber theory.** Action-at-a-distance electrodynamics with time-symmetric retarded + advanced; mathematically consistent; substrate-operationally non-realizable in ED.
- **Backward chain contributions.** Hypothetical substrate sequences with $t_{i+1} < t_i$; non-constructible from canonical 13 primitives.
- **Kernel-level arrow of time.** Substrate-primitive structural commitment to forward-causal kernel propagation; elaborated in Paper_093.

---

**End of Paper_089.**

*Wave-2 Generative Paper — Wedges, Canonical V1 Reference. Authoritative statement of Theorems N1 (finite-width) and T18 (retarded support), with substrate-operational compositional-closure justification and direct Wheeler–Feynman engagement.*
