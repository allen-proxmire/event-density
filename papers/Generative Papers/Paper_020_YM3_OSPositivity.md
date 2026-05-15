# Paper 020 — Osterwalder–Schrader Positivity Audit for Substrate-Level Yang–Mills (YM-3) — FIXED

**Series:** Wave-2 Generative Papers (Yang–Mills Arc, YM-3)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087 canonical enumeration) + paper-specific postulates declared in §2.
**Companion papers:** Paper_015 (T17), Paper_016 (non-Abelian composition), Paper_017 (Lorentz covariantization), Paper_018 (DCGT non-Abelian), Paper_019 (substrate→continuum YM limit), Paper_073 (DCGT), Paper_089 (V1 kernel), Paper_090 (V5 kernel).

**FIXED notes (2026-05-13):**
- Audit-table relabels: OS1/OS2/OS5 rows previously labeled D are now I (upstream-paper inheritance + standard-math).
- Primitive enumeration aligned with Paper_087 canonical list.
- Template "Flexibility & Correction Block" deleted; revision triggers folded into Open Questions.
- §X.5 P-postulates inventory folded into §2.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a constructive proof that the Osterwalder–Schrader axioms hold for the continuum-limit YM theory of Paper_019.
2. It does **not** claim that the conditional-positive audit verdict here is equivalent to OS-positivity in the standard constructive-QFT sense.
3. It does **not** claim novel content for OS axioms OS1, OS2, OS4, OS5 beyond inheritance from upstream substrate-level papers + standard mathematical machinery.
4. It does **not** claim a derivation of OS3 (reflection positivity); OS3 is made explicit as a substrate-level postulate.
5. It does **not** introduce new substrate primitives.
6. "Conditional-positive" means: all five OS axioms structurally audited, with substrate-level inheritance lines identified and the two non-inherited content items declared as postulates.
7. The audit is per-axiom and channel-by-channel where appropriate (rule-type bundle sector decomposition).
8. This paper supplies the YM-3 step of the Yang–Mills arc and feeds Paper_021 (mass-gap mechanism) and Paper_023 (Clay-relevance synthesis).

---

## Abstract

We audit the five Osterwalder–Schrader axioms (OS1 regularity, OS2 Euclidean covariance, OS3 reflection positivity, OS4 symmetry/cluster, OS5 clustering) for the substrate-level Yang–Mills theory constructed in Paper_019. OS1, OS2, OS5 are inherited from upstream substrate-level results (V1 finite width, Lorentz covariantization, V5 finite memory) combined with standard mathematical machinery (Wick rotation, exponential clustering). OS4 partially inherits from the rule-type bundle channel decomposition of Paper_015. OS3 is the only axiom not inheritable from upstream substrate content; we declare it as P-OS-Reflection-Positivity. A second declared postulate P-OS-Reflection-Symmetry codifies the substrate's invariance under Euclidean-time reflection. The composite verdict is **structural-positive-conditional**: every OS axiom has a substrate-level audit, with two explicit declared postulates and no hidden assumptions.

---

## §1 Introduction

The Osterwalder–Schrader axioms specify when a Euclidean field theory's Schwinger functions correspond to a Wightman QFT via Wick rotation. The five axioms are:

- **OS1 (Regularity):** Schwinger functions are tempered distributions with appropriate growth.
- **OS2 (Euclidean covariance):** Schwinger functions transform covariantly under Euclidean isometries.
- **OS3 (Reflection positivity):** A reflection-positivity inequality holds.
- **OS4 (Symmetry/cluster):** Permutation symmetry of Schwinger functions.
- **OS5 (Clustering):** Decay of correlations at large separation.

This paper audits each axiom against the substrate-level YM theory of Paper_019.

---

## §2 Primitive Inputs, Paper-Specific Postulates, Inheritance

### 2.1 Primitives invoked (per Paper_087 canonical enumeration)

- **P02 (Participation)** — pre-individuation amplitudes support Schwinger functionals.
- **P07 (Channel structure)** — supplies the gauge-rule-type bundle structure.
- **P10 (Rule-type primitive)** — supplies V1 and V5 kernels as kernel rule-types (specific kernels in Papers_089/090).
- **P11 (Commitment-irreversibility)** — supplies retarded-kernel structure.

### 2.2 Inherited closed-arc results

- **I-V1:** V1 kernel has finite width and acts as UV regulator (Paper_089).
- **I-V5:** V5 kernel has finite bandwidth/memory (Paper_090).
- **I-DCGT:** Diffusion Coarse-Graining Theorem (Paper_073).
- **I-LorCov:** Substrate→continuum Lorentz covariantization (Paper_017).
- **I-T17:** Gauge fields as rule-type bundle connections (Paper_015).
- **I-YM-Cont:** Continuum YM action obtained at leading order (Paper_019).
- **I-Wick:** Standard Wick-rotation machinery (standard math).

### 2.3 Paper-specific postulates

- **P-OS-Reflection-Positivity:** The substrate-level Schwinger functional satisfies a reflection-positivity inequality $\langle \Theta F, F \rangle \geq 0$ for all admissible test functionals $F$ with support on positive Euclidean time, where $\Theta$ is the Euclidean-time reflection. This is the non-inheritable OS-content; declared, not derived.
- **P-OS-Reflection-Symmetry:** The substrate is invariant under Euclidean-time reflection. Codifies the symmetry underlying $\Theta$'s action.

---

## §2.5 Load-Bearing Step Audit Table (Per-Axiom)

| OS axiom | Substrate-level audit | Label | Notes |
|---|---|---|---|
| OS1 (Regularity) | V1 finite width + DCGT regularization | I | Inherited from Paper_089 + Paper_073; no new derivation step in this paper. |
| OS2 (Euclidean covariance) | Substrate Lorentz covariantization + Wick rotation | I | Inherited from Paper_017 + standard Wick rotation (standard math, I). |
| OS3 (Reflection positivity) | Substrate Euclidean-time reflection positivity | P-OS-Reflection-Positivity | Declared postulate. The non-inheritable OS-content. |
| OS3 supporting | Substrate reflection symmetry | P-OS-Reflection-Symmetry | Declared postulate. |
| OS4 (Symmetry/cluster, permutation) | Rule-type bundle channel decomposition | I | Inherited from Paper_015 (T17); permutation symmetry of Schwinger functions follows. |
| OS5 (Clustering) | V5 finite-memory implies exponential clustering | I | Inherited from Paper_090; cluster decay rate is V5-bandwidth-controlled. |
| Composite verdict: structural-positive-conditional | Per-axiom audit composes to verdict | A→position | Honest position statement, not algebraic derivation. |

No structural-analogy mislabel. The strengthened D-row rereading test confirms: OS1, OS2, OS4, OS5 rows are applications of upstream results / standard math, not new derivations in this paper, hence I. OS3 is explicit P. The composite verdict is A→position (honest framing).

---

## §3 The Per-Axiom Audit

### 3.1 OS1 (Regularity)

Schwinger functions on the substrate-level YM theory are constructed from V1-regulated correlation functionals. The V1 kernel's finite second moment (Paper_089) supplies the UV regularization; DCGT (Paper_073) supplies the hydrodynamic-window validity. The standard tempered-distribution property follows from V1+DCGT applied to the YM-action functional of Paper_019.

**Label: I.** This is an application of Papers_073/089 to the YM-action functional, not a new derivation step.

### 3.2 OS2 (Euclidean covariance)

Substrate Lorentz covariantization (Paper_017) supplies the Minkowski covariance of the substrate-level fields. Wick rotation to Euclidean signature is standard mathematical machinery; the Euclidean covariance of Schwinger functions follows.

**Label: I.** Inherited from Paper_017 + standard Wick rotation (standard math). No new substrate-level derivation here.

### 3.3 OS3 (Reflection positivity) — the non-inheritable axiom

This is the single OS axiom for which no upstream substrate paper supplies inheritance content. Reflection positivity is a non-trivial requirement on the Euclidean Schwinger functional and is not automatic from V1/V5/T17/DCGT/Paper_017.

We declare two postulates:

- **P-OS-Reflection-Symmetry:** The substrate is invariant under Euclidean-time reflection.
- **P-OS-Reflection-Positivity:** $\langle \Theta F, F \rangle \geq 0$ for all admissible $F$.

These are the two non-inheritable content items. Their declaration is the principal new content of this paper at the OS-audit level.

### 3.4 OS4 (Symmetry/cluster, permutation symmetry)

Permutation symmetry of Schwinger functions follows from the rule-type bundle channel decomposition (Paper_015). The bundle structure equips channels with a symmetric-functor structure that descends to symmetric Schwinger functions.

**Label: I.** Inherited from T17 (Paper_015).

### 3.5 OS5 (Clustering)

V5 kernel finite bandwidth (Paper_090) supplies exponential clustering of substrate-level correlations at separation beyond $\ell_{V5}$. This descends to Schwinger-function clustering after Wick rotation.

**Label: I.** Inherited from Paper_090.

### 3.6 The composite verdict

Combining 3.1–3.5: every OS axiom has a substrate-level audit. Four (OS1, OS2, OS4, OS5) are inherited from upstream substrate papers + standard math. OS3 is declared (P-OS-Reflection-Positivity + P-OS-Reflection-Symmetry).

**Composite verdict:** structural-positive-conditional. The "conditional" refers to the two declared postulates; the "structural-positive" refers to the per-axiom audit completing without hidden assumptions.

This is **not** a constructive proof of OS-positivity. It is an audit with explicit declared content.

---

## §4 Channel-by-Channel OS3 Audit

The rule-type bundle structure (Paper_015) decomposes the YM sector into channels indexed by the gauge group's irreducible representations. P-OS-Reflection-Positivity is asserted **channel-by-channel**: each irrep channel's Schwinger functional satisfies the reflection-positivity inequality.

Channel-by-channel is the structurally suggestive level of audit. It is not constructive-positive — that would require explicit channel-functional computation, which is not supplied here.

---

## §5 What This Audit Does and Does Not Establish

**Establishes:**
- Per-axiom audit lines for all five OS axioms.
- Explicit identification of inheritance origin for OS1, OS2, OS4, OS5.
- Explicit declared-postulate identification for OS3.

**Does not establish:**
- A constructive proof of OS-positivity.
- A derivation of P-OS-Reflection-Positivity from substrate primitives.
- Quantitative bounds on cluster decay rates beyond exponential form.

---

## §6 Open Structural Questions

- **O-OS-1:** Constructive derivation of P-OS-Reflection-Positivity from substrate primitives (would strengthen audit from conditional-positive to OS-positive).
- **O-OS-2:** Channel-by-channel constructive audit (would strengthen §4 from suggestive-positive to constructive).
- **O-OS-3:** Connection to lattice-YM reflection-positivity theorems (Wilson action OS-positive at lattice level).
- **O-OS-4:** Whether P-OS-Reflection-Symmetry can be derived from P11 (commitment-irreversibility) — symmetry under time-reflection is non-trivial given P11's directional content.
- **O-OS-Revision:** If a constructive derivation of P-OS-Reflection-Positivity appears, §3.3 strengthens to I (derived) and the composite verdict strengthens to OS-positive.

---

## §7 Falsification Criteria

- **F1:** Demonstration that the V1+DCGT-regulated Schwinger functional **violates** reflection positivity in any channel — refutes P-OS-Reflection-Positivity.
- **F2:** Demonstration that the substrate is **not** invariant under Euclidean-time reflection — refutes P-OS-Reflection-Symmetry.
- **F3:** Demonstration that V5 finite memory does **not** imply exponential clustering of Schwinger functions — propagates from Paper_090 to here.
- **F4:** Demonstration that the rule-type bundle channel decomposition does **not** support symmetric Schwinger functions — propagates from Paper_015 to here.

Refutation of F1–F4 falsifies the audit verdict without refuting the substrate primitives.

---

## §8 Position Statement

The substrate-level YM theory of Paper_019 admits a **conditional-positive** OS-axiom audit. Four of the five OS axioms are inherited from upstream substrate papers (Papers_015/017/073/089/090) combined with standard mathematical machinery. The fifth, OS3 reflection positivity, is declared as P-OS-Reflection-Positivity supported by P-OS-Reflection-Symmetry.

The verdict is **above** mere structural analogy and **below** a constructive OS-positivity proof. It is the same epistemic level as Paper_021's mass-gap mechanism and Paper_020 (this paper) jointly feeding Paper_023's Clay-relevance synthesis at structural-positive level.

---

## Appendix — Channel-by-Channel OS3 Status

For compact simple gauge group $G$ with irreducible-representation decomposition $\bigoplus_\lambda V_\lambda$:

| Channel | Audit level | Notes |
|---|---|---|
| Trivial channel | P-OS-Reflection-Positivity (declared) | Vacuum sector. |
| Fundamental channel | P-OS-Reflection-Positivity (declared) | Standard physical channel. |
| Adjoint channel | P-OS-Reflection-Positivity (declared) | Gauge-bosons live here. |
| Higher irreps | P-OS-Reflection-Positivity (declared) | Audit extends; no channel-specific derivation. |

The channel-by-channel level is **structurally suggestive**, not constructive. Future O-OS-2 work would constructively audit per channel.

---

**End Paper 020 (FIXED).**
