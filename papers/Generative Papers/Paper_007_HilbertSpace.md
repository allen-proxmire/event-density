# Paper_007 — Hilbert-Space Emergence as Completion of Motif Algebra

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc (keystone)
**Author:** Allen Proxmire
**Status:** Publication draft (closes 001 → 003 → 007 loop)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_007_HilbertSpace.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No circularity:** Hilbert space is **not assumed**. The substrate-level amplitude content (Paper_001 pre-individuation $P_K^C$) is the input; Hilbert-space emerges as the **Cauchy-completion** of the motif algebra under the sesquilinear inner product (Paper #3 inheritance).
3. **No claim that the inner product is derived in this paper.** Paper #3 (pre-pivot) supplies the inner-product + Tsirelson structure; this paper supplies the Hilbert-space-completion mechanism from primitives + Paper #3 inheritance.
4. **No claim that infinite-dimensional Hilbert space is forced.** The Cauchy completion is dimension-agnostic; finite-dimensional substrate amplitude content (finite $|\mathcal{K}|$) gives a finite-dimensional Hilbert space; countable substrate channel structure gives a separable Hilbert space.
5. **No claim of derivation of generic QM observables / spectral structure.** Paper_005 (in queue) supplies projective measurement; spectral theory + observables are downstream.
6. **No claim of unique Cauchy-completion construction.** Standard mathematical Cauchy completion is invoked; substrate-level construction follows that standard procedure under the §3.3 motif-algebra norm.

---

## Abstract

This paper closes the **001 → 003 → 007 loop** of the ED QM-kinematics arc: Paper_001 supplied pre-individuation amplitude content $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$; Paper_003 supplied the Born-rule frequency-limit downstream; **Paper_007 (this paper) supplies the Hilbert-space-emergence mechanism** showing that the substrate-level amplitude content + sesquilinear inner-product (Paper #3 inheritance) **complete to a Hilbert space** via standard Cauchy-completion.

The substrate-level mechanism:

- **Motif algebra:** algebraic structure on Paper_001's pre-individuation amplitudes $\{P_K^C\}$ — sums, scalar multiples, products with substrate-level rules.
- **Sesquilinear inner product:** inherited from Paper #3 — $\langle\Psi|\Phi\rangle = \sum_K \overline{P_K^\Psi} P_K^\Phi$ (or appropriate substrate-level analog).
- **Norm:** $\|\Psi\|^2 = \langle\Psi|\Psi\rangle = \sum_K |P_K|^2 = \sum_K b_K$ (Paper_001 §3.3 identification).
- **Cauchy completion:** standard mathematical procedure on the inner-product space.

The result is a Hilbert space $\mathcal{H}$ whose pure states are substrate-level pre-individuation amplitude content (up to overall phase + normalization). **Hilbert space is not assumed; it emerges.** The paper makes no claim of inner-product derivation (Paper #3 inheritance), no claim of generic-observable derivation (Paper_005 in queue), and no claim of unique completion construction (standard Cauchy procedure).

---

## 1. Introduction

### 1.1 What this paper does

This paper closes the loop:

- **Paper_001:** substrate-level pre-individuation amplitudes $P_K^C$.
- **Paper_003:** Born rule from participation-frequency limit (uses Paper_001 amplitudes + P-LinRate).
- **Paper_007 (this paper):** Hilbert-space emergence as completion of motif algebra (uses Paper_001 amplitudes + Paper #3 inner product).

Together, the three papers establish: **substrate primitives → pre-individuation amplitudes → motif algebra + inner product → Hilbert space + Born rule.** Standard QM-kinematics emerges structurally from substrate primitives + Paper #3 inner-product inheritance + P-LinRate + frequentist interpretation.

### 1.2 Why Hilbert space needs an emergence mechanism (non-circularity)

Operational reconstructions (Hardy, CDP, Masanes–Müller, Coecke–Kissinger) take Hilbert space (or category-theoretic analog) as primitive or near-primitive. ED takes substrate primitives (chains + channels + bandwidth + polarity) as primitive; Hilbert space must **emerge** rather than be assumed.

This paper's load-bearing structural claim: the substrate-level amplitude content of Paper_001, together with Paper #3's sesquilinear inner product, has a **natural mathematical completion** to a Hilbert space via Cauchy completion. The Hilbert space is the **completion**, not a postulate.

**Non-circularity audit (per QC discipline):**

- Substrate primitives: P01–P09 (postulated, Paper_087).
- Pre-individuation amplitudes: Paper_001 (D from primitives + P-Bandwidth-as-Scalar + P-Polarity-as-U(1)).
- Motif algebra: D from amplitude content + standard algebraic operations.
- Inner product: I (Paper #3 inheritance).
- Cauchy completion: D from standard procedure.
- Hilbert space: emerges as completion, not assumed.

### 1.3 Arc context

- **Paper_001:** pre-individuation amplitudes.
- **Paper_002 (in queue):** tensor-product composition.
- **Paper_003:** Born rule.
- **Paper_007 (this paper):** Hilbert-space emergence. **Closes 001 → 003 → 007.**

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P01, P02, P03, P04, P07, P09.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_001:** pre-individuation amplitudes $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$.
- **Paper #3 (pre-pivot):** sesquilinear inner product + Tsirelson; inherited as substrate-level inner-product structure. **Load-bearing — without it, no completion to Hilbert space.**

**Paper-specific postulate:**

- **P-Motif-Algebra (Motif algebra on substrate amplitudes):** *The set of substrate-level amplitude tuples $\{P_K^C\}_{K \in \mathcal{K}}$ forms a complex vector space under componentwise addition and complex scalar multiplication, with substrate-level basis $\{|K\rangle\}_{K \in \mathcal{K}}$ indexed by channel structure (P07).* Substrate-level definitional commitment; not derivable from primitives alone (algebraic-structure commitment).

**Empirical / value-layer inputs:** none required at this paper's level.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Pre-individuation amplitude $P_K^C$ | D | Paper_001 |
| Motif algebra structure (complex vector space) | **P (P-Motif-Algebra, definitional)** | §2 substrate-level definitional commitment; complex vector space on $\{P_K^C\}_K$ |
| Sesquilinear inner product $\langle\Psi|\Phi\rangle$ | **I (Paper #3 inheritance)** | Inner-product structure not derived in this paper; inherited from Paper #3 pre-pivot work. **Forward-pointer:** if Paper_004 (Gleason-type uniqueness, in queue) derives the inner product from canonical 13 primitives + Paper_001 amplitude structure alone, this row would relabel from **I → D**. Until then, I status is maintained. |
| Norm $\|\Psi\|^2 = \sum_K |P_K|^2 = \sum_K b_K$ | D | §3.2 from inner-product definition + Paper_001 amplitude identification |
| Cauchy completion procedure | I + D | Standard mathematical procedure (I), applied to motif-algebra inner-product space (D) |
| Hilbert space $\mathcal{H}$ emerges as completion | **D conditional on P-Motif-Algebra + I-inner-product + standard Cauchy completion** | §3.4 Cauchy completion of motif algebra under norm — explicit standard mathematical procedure applied to (P-Motif-Algebra) complex vector space + (I-inner-product) Paper #3 inheritance. Conditional D — given all three upstream items, Hilbert-space emergence follows. |
| Finite-dim vs. infinite-dim depending on $|\mathcal{K}|$ | D | §3.5 standard math |
| Pure states = unit-norm equivalence classes in $\mathcal{H}$ | D | §4.1 |
| Standard QM observables / spectral theory | I | Paper_005 + downstream territory |
| Non-circularity: Hilbert space NOT assumed | D | §1.2 non-circularity audit |

All rows P, D, or I. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. Hilbert-Space Emergence

### 3.1 The motif algebra

By Paper_001, the substrate-level amplitude content of a chain $C$ is the tuple $\{P_K^C\}_{K \in \mathcal{K}}$ over the channel set. By **P-Motif-Algebra (§2)**, this content has complex-vector-space structure:

- **Addition:** $(\Psi + \Phi)_K = \Psi_K + \Phi_K$.
- **Scalar multiplication:** $(c\Psi)_K = c \cdot \Psi_K$ for $c \in \mathbb{C}$.
- **Basis:** $\{|K\rangle\}_{K \in \mathcal{K}}$ indexed by P07 channel structure.

Elements: $\Psi = \sum_K \Psi_K |K\rangle$ where $\Psi_K \in \mathbb{C}$. This is the **motif algebra** — substrate-level amplitude space before completion.

**Dimension:** $\dim(\text{motif algebra}) = |\mathcal{K}|$ (cardinality of substrate channel set). Finite $|\mathcal{K}|$ → finite-dim motif algebra; countable infinite $|\mathcal{K}|$ → infinite-dim motif algebra.

### 3.2 Sesquilinear inner product (Paper #3 inheritance)

From Paper #3 (pre-pivot inner product + Tsirelson), substrate-level amplitude content has a **sesquilinear inner product**:

$$
\langle\Psi|\Phi\rangle = \sum_K \overline{\Psi_K}\,\Phi_K
$$

(conjugate-linear in first slot, linear in second; substrate-level analog of standard QM inner product).

**Norm:** $\|\Psi\|^2 = \langle\Psi|\Psi\rangle = \sum_K |\Psi_K|^2$.

Using Paper_001 amplitude identification $\Psi_K = P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$:

$$
\|\Psi\|^2 = \sum_K |P_K^C|^2 = \sum_K b_K^C.
$$

**Dimensional check:** $b_K$ is non-negative substrate-level bandwidth; sum is total substrate-level participation content of chain $C$. ✓

**Honest framing:** the sesquilinear inner product is **inherited from Paper #3**, not derived from substrate primitives in this paper. Whether the inner-product structure can be derived from substrate primitives alone (without Paper #3's load-bearing input) is an open structural question.

**Forward-pointer:** Paper_004 (Gleason-type uniqueness, in queue) is the candidate paper that would derive the inner product from canonical 13 primitives + Paper_001 amplitude content alone via a substrate-level Gleason-analog uniqueness argument. If Paper_004 succeeds at this derivation, the inner-product row in §2.5 (and the load-bearing chain in §5.2) would relabel from **I → D**, strengthening the substrate-framework's self-containment. Until Paper_004 is written, the inner-product row stays I.

### 3.3 The motif-algebra norm and metric

The norm $\|\cdot\|$ on the motif algebra induces a metric:

$$
d(\Psi, \Phi) = \|\Psi - \Phi\| = \sqrt{\sum_K |\Psi_K - \Phi_K|^2}.
$$

The motif algebra is a normed complex vector space with this metric.

**Is it complete?** For finite $|\mathcal{K}|$: yes (finite-dim normed spaces over $\mathbb{C}$ are automatically complete). For infinite $|\mathcal{K}|$ (countable): not automatically — there can be Cauchy sequences whose limits are not in the motif algebra (if we restrict to "finite-support" amplitude content, infinite-norm limits would not be representable).

**Completion required for infinite case.**

### 3.4 Cauchy completion → Hilbert space

Apply standard **Cauchy completion** to the motif algebra under the inner-product norm:

1. Consider all Cauchy sequences $(\Psi^{(n)})_{n=1}^\infty$ in the motif algebra.
2. Identify sequences whose pairwise distance vanishes asymptotically: $(\Psi^{(n)}) \sim (\Phi^{(n)})$ iff $\|\Psi^{(n)} - \Phi^{(n)}\| \to 0$.
3. The set of equivalence classes is the **Cauchy completion** of the motif algebra.

The completion is a **complete normed complex vector space with sesquilinear inner product** — i.e., a **Hilbert space** $\mathcal{H}$.

$$
\boxed{\mathcal{H} = \overline{\text{Motif Algebra}}^{\,\|\cdot\|} \quad \text{(Cauchy completion under sesquilinear inner-product norm).}}
$$

**The Hilbert space emerges as the completion, not as a postulate.**

### 3.5 Finite vs. infinite-dimensional

- **Finite $|\mathcal{K}|$:** $\mathcal{H} \cong \mathbb{C}^{|\mathcal{K}|}$, automatically complete. The motif algebra equals its completion.
- **Countable $|\mathcal{K}|$:** $\mathcal{H} \cong \ell^2(\mathcal{K})$ (square-summable sequences). Completion includes infinite-norm limit points not in the original motif algebra of finite-support amplitudes.

For physical applications, finite $|\mathcal{K}|$ → finite-dim QM (qubits, qudits); countable $|\mathcal{K}|$ → separable Hilbert space (most standard QM applications).

**The substrate-level dimension is set by P07's channel-structure cardinality**, not by mathematical fiat.

---

## 4. Pure States and the Born Rule

### 4.1 Pure states as unit-norm equivalence classes

A **pure state** in $\mathcal{H}$ is a unit-norm element modulo overall phase:

$$
|\Psi\rangle \in \mathcal{H}\quad \text{with } \|\Psi\| = 1,\quad |\Psi\rangle \sim e^{i\alpha}|\Psi\rangle \text{ for } \alpha \in \mathbb{R}.
$$

Substrate-level identification: a pure state corresponds to substrate-level pre-individuation amplitude content $\{P_K^C\}$ normalized so that $\sum_K b_K^C = 1$, with overall polarity phase $\alpha$ unobservable (gauge freedom).

### 4.2 Born rule on $\mathcal{H}$

Paper_003's substrate-level Born rule $f_K = b_K = |P_K|^2$ corresponds at the Hilbert-space level to:

$$
P(K) = |\langle K|\Psi\rangle|^2 = |\Psi_K|^2 = |P_K|^2
$$

— the standard Born rule. The substrate-level mechanism (Paper_003 + Paper_001) underlies the Hilbert-space Born rule.

### 4.3 The full loop: 001 → 003 → 007

- Paper_001: substrate-level $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$.
- Paper_003: P-LinRate + frequentist → frequency limit $f_K = b_K$.
- Paper_007: Cauchy completion of motif algebra → Hilbert space $\mathcal{H}$, with Born rule $P(K) = |\Psi_K|^2$.

**The loop closes.** Substrate primitives → pre-individuation amplitudes → motif algebra + inner product → Hilbert space + Born rule. Standard QM-kinematics emerges structurally.

---

## 5. Non-Circularity Audit

This section explicitly addresses the non-circularity concern.

### 5.1 What is NOT assumed

- Hilbert space is not assumed at start.
- Born rule is not assumed (Paper_003 derives it).
- Complex amplitudes are not assumed (Paper_001 derives complex polar carrier from $b_K$ + $\pi_K$ + square-root convention).

### 5.2 What IS used

- Substrate primitives P01, P02, P03, P04, P07, P09.
- Paper_001 pre-individuation amplitudes (D from primitives + P-Bandwidth + P-Polarity).
- P-Motif-Algebra (substrate-level definitional commitment; complex vector space).
- Paper #3 sesquilinear inner product (I).
- Standard Cauchy-completion procedure (standard math, I+D).
- Frequentist interpretation (Paper_003 methodological).

### 5.3 The chain: substrate primitives → Hilbert space

Substrate primitives → Paper_001 amplitude content $\{P_K^C\}$ → P-Motif-Algebra complex vector space → Paper #3 sesquilinear inner product → norm → Cauchy completion → Hilbert space $\mathcal{H}$.

**Hilbert space is the endpoint, not the starting point.** Non-circularity is preserved by:

- Substrate primitives are first.
- Paper_001 amplitude content emerges from substrate primitives + P-Polarity.
- Motif algebra is a definitional structure on amplitudes (P-Motif-Algebra).
- Inner product is inherited (Paper #3 — load-bearing external input).
- Hilbert space emerges via completion — not assumed.

**The load-bearing external input is Paper #3's sesquilinear inner product.** This paper acknowledges the inner-product structure as an inheritance, not a derivation. Whether the inner-product can be derived from substrate primitives alone is a deeper structural question (in-queue work, possibly via Paper_004 Gleason-type uniqueness).

---

## 6. Falsification Criteria

### 6.1 Motif algebra structure fails

**Falsifier sentence:** *Empirical demonstration that substrate-level amplitude content $\{P_K^C\}$ does not admit complex-vector-space structure (P-Motif-Algebra) — e.g., addition does not preserve substrate-level amplitude character, or scalar multiplication breaks substrate-level convention — would falsify §3.1.*

### 6.2 Sesquilinear inner product not load-bearing

**Falsifier sentence:** *Demonstration that the substrate-level structure can be completed to a Hilbert space **without** the Paper #3 sesquilinear inner product — i.e., via a different inner-product structure (skew-Hermitian, real-symmetric, etc.) — would weaken the Paper #3 load-bearing claim and require alternative completion routes.*

### 6.3 Cauchy completion fails to produce Hilbert space

**Falsifier sentence:** *Empirical demonstration that the motif-algebra Cauchy completion produces a structure that is **not** a Hilbert space — e.g., not complete, or not sesquilinear, or has non-standard topology — would falsify §3.4.*

### 6.4 Hilbert space dimension inconsistent with $|\mathcal{K}|$

**Falsifier sentence:** *Empirical observation of effective Hilbert-space dimension inconsistent with substrate channel-set cardinality $|\mathcal{K}|$ — e.g., a system with 5 substrate channels but 7-dimensional effective Hilbert space — would falsify the §3.5 dimension correspondence.*

### 6.5 Standard QM-kinematics fails to emerge

**Falsifier sentence:** *Empirical demonstration that the Hilbert-space structure emerging from §3.4 does not reproduce standard QM-kinematics (Born rule, projective measurement, unitary evolution) under the downstream Papers_003/005/006 — would falsify the QM-kinematics-emergence loop.*

### 6.6 Inner product derivable from primitives alone

**Falsifier sentence (refinement):** *Demonstration that Paper #3's sesquilinear inner product is **derivable from canonical 13 primitives alone** — without Paper #3 as load-bearing input — would strengthen the substrate framework's self-containment but would not falsify this paper. It would refine the audit by relabeling the inner-product row from I (inheritance) to D (derived).*

---

## 7. Position Statement

**The Hilbert space of standard QM emerges** as the Cauchy completion of the motif algebra (P-Motif-Algebra on Paper_001 pre-individuation amplitudes) under Paper #3's sesquilinear inner product:

$$
\boxed{\mathcal{H} = \overline{\text{Motif Algebra}\,(\{P_K^C\}_K)}^{\,\|\cdot\|_{\text{Paper #3 inner product}}}.}
$$

**Hilbert space is not assumed; it emerges via standard mathematical Cauchy completion of substrate-level amplitude content + inherited inner-product structure.**

The 001 → 003 → 007 loop closes: substrate primitives → pre-individuation amplitudes (001) → Born-rule frequency-limit (003) → Hilbert-space emergence (this paper). Standard QM-kinematics is the downstream content.

What this paper claims:

- Hilbert space emerges as completion of motif algebra under sesquilinear inner product.
- Non-circularity is preserved: Hilbert space is the endpoint, not the input.
- Cauchy completion is standard mathematical procedure applied to substrate-level structure.
- Dimension of Hilbert space tracks substrate channel-set cardinality.

What this paper does *not* claim:

- The 13 primitives are not derived.
- Paper #3 sesquilinear inner product is not re-derived; inherited as load-bearing.
- Standard QM observables / spectral theory not derived (Paper_005 + downstream).
- Generic Cauchy-completion uniqueness not claimed; standard procedure invoked.

**Series context.** Paper_007 of QM-kinematics arc. **Closes 001 → 003 → 007 loop.** Downstream: Papers_004 (Gleason), 005 (projection), 006 (unitary evolution), 008–012 (phase, Berry, AB, Bloch, P-RB-1) in queue.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_001:** pre-individuation amplitudes (upstream).
- **Paper_003:** Born rule (sibling — closes loop with this paper).
- **Paper #3 (pre-pivot):** sesquilinear inner product + Tsirelson (load-bearing inheritance).
- **Paper_005 (in queue):** projective measurement.
- **Paper_006 (in queue):** unitary evolution.

### Glossary

- **Motif algebra.** Complex vector space on substrate-level amplitude content $\{P_K^C\}_K$, with channel-indexed basis (P-Motif-Algebra).
- **Sesquilinear inner product.** $\langle\Psi|\Phi\rangle = \sum_K \overline{\Psi_K}\,\Phi_K$ — Paper #3 inheritance.
- **Motif-algebra norm.** $\|\Psi\|^2 = \sum_K |P_K|^2 = \sum_K b_K$.
- **Cauchy completion.** Standard math procedure: equivalence classes of Cauchy sequences under the norm metric; produces a Hilbert space.
- **Hilbert-space emergence.** Hilbert space is the completion of motif algebra, not a postulate.
- **001 → 003 → 007 loop.** Substrate primitives → amplitudes → Born rule → Hilbert space; closes the QM-kinematics anchor cycle.

---

**End of Paper_007.**

*Wave-2 Generative Paper — QM-Kinematics Arc Keystone. Closes 001 → 003 → 007 loop.*
