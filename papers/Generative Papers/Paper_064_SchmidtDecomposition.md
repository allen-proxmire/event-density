# Paper_064 — Schmidt Decomposition (E-3)

**Series:** Event Density (ED) Generative Papers — Wave-2 entanglement arc
**Author:** Allen Proxmire
**Status:** Publication draft (entanglement arc continuation; strengthens Paper_063 E-2 irreducibility claim)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/entanglement/Paper_064_SchmidtDecomposition.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that Schmidt decomposition is derived from substrate primitives alone.** The standard Schmidt decomposition theorem is **inherited** from linear-algebra; this paper supplies the substrate-level mapping of Paper_063 P-Bipartite-Mapping joint amplitudes to Schmidt form.
3. **No claim of derivation of Schmidt rank as a substrate-level observable.** Schmidt rank is computed via standard linear-algebraic SVD on the joint amplitude matrix; this is inherited mathematical procedure.
4. **The strengthening of Paper_063 E-2 irreducibility is partial.** Schmidt rank > 1 implies non-factorizability, so Paper_063's E-2 irreducibility claim becomes a **mathematical theorem** (Schmidt-rank-based) rather than a substrate-level assertion. The substrate-level commitment that V5-bilocal content $\Delta_{KL}^{AB}$ has Schmidt rank > 1 in the entangled regime is still **substrate-level**.
5. **No claim that all bipartite entangled states have substrate-level analog.** Pure-state Schmidt decomposition only; mixed-state Schmidt requires extension.

---

## Abstract

This paper develops **Schmidt decomposition (E-3)** for bipartite substrate-level joint amplitudes, continuing the entanglement arc opened by Paper_063 (E-1, E-2). Given Paper_063 P-Bipartite-Mapping + standard linear-algebraic SVD machinery (inherited), the joint amplitude $\Psi_{KL}^{AB}$ in the bipartite product basis admits the standard **Schmidt decomposition**:

$$
\Psi^{AB} = \sum_{i=1}^{r} \lambda_i\,|u_i\rangle_A \otimes |v_i\rangle_B
$$

where $r$ is the **Schmidt rank**, $\lambda_i > 0$ are the **Schmidt coefficients** ($\sum_i \lambda_i^2 = 1$ in normalized state), and $\{|u_i\rangle_A\}, \{|v_i\rangle_B\}$ are orthonormal Schmidt bases for the two subsystems.

**Schmidt rank as entanglement indicator:**
- $r = 1$ → factorizable state (Paper_063 E-1).
- $r > 1$ → non-factorizable / entangled state (Paper_063 E-2).

**Strengthening Paper_063 E-2 irreducibility:** Paper_063's E-2 irreducibility claim (round-6 A→assertion) is **strengthened** by Schmidt: any state with $r > 1$ is **mathematically provably** non-factorizable (no choice of $f^A, g^B$ can write $\Psi$ as $f^A \cdot g^B$ if Schmidt rank exceeds 1). The substrate-level claim that V5-mediated bilocal $\Delta_{KL}^{AB}$ has Schmidt rank > 1 generically is still a substrate-level commitment, but the **irreducibility-given-Schmidt-rank > 1** is now a mathematical theorem.

The paper makes no claim of derivation of standard Schmidt theorem (inherited), no claim of mixed-state generalization (downstream), and no claim that all V5-correlated states have Schmidt rank > 1 (specific V5-content-dependent).

---

## 1. Introduction

### 1.1 What this paper does

Paper_063 opened the entanglement arc with E-1 (factorizable) + E-2 (non-factorizable via V5). The E-2 irreducibility claim was round-6-relabeled **A→assertion** because no explicit irreducibility theorem was provided. This paper supplies the **standard Schmidt decomposition machinery** (inherited from linear algebra) and uses it to **strengthen Paper_063 E-2 irreducibility** to a Schmidt-rank-based mathematical theorem.

### 1.2 Arc context

- **Paper_063 (upstream):** E-1, E-2 (tensor product + non-factorizability).
- **Paper_064 (this paper):** E-3 Schmidt decomposition.
- **Paper_065 (in queue):** E-4 Monogamy via cross-chain bandwidth.
- **Papers_066–072 (in queue):** No-signaling, von Neumann entropy, Bell-Tsirelson, bipartite synthesis.

---

## 2. Primitive Inputs

**Substrate primitives:** P02, P03, P04, P07, P09.

**Upstream paper dependencies:** Paper_087, Paper_001 (amplitudes), Paper_007 (Hilbert-space arena), Paper_063 (P-Bipartite-Mapping + E-1/E-2).

**Inherited mathematical inputs:**

- **Singular Value Decomposition (SVD):** standard linear-algebra theorem; any complex matrix admits SVD $M = U \Sigma V^\dagger$ with $\Sigma$ diagonal non-negative.
- **Schmidt decomposition theorem:** standard QM linear-algebra theorem; bipartite pure states admit Schmidt form via SVD on the joint amplitude matrix.

**Paper-specific postulate:**

- **P-V5-Schmidt-Generic (V5-bilocal joint content has Schmidt rank > 1 generically):** *For substrate-level bipartite states with non-zero V5 cross-chain correlation amplitude $\Delta_{KL}^{AB}$ (Paper_063 §3.3), the Schmidt rank of the joint amplitude $\Psi_{KL}^{AB} = P_K^A P_L^B + \Delta_{KL}^{AB}$ is generically $> 1$.* Substrate-level commitment about V5-content; specific V5-envelope configurations could give Schmidt rank = 1 (special cases), but generic V5 correlation produces non-trivial Schmidt structure.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives + Paper_087 | P | Paper_087 |
| Paper_063 P-Bipartite-Mapping | P | Paper_063 |
| Joint amplitude $\Psi_{KL}^{AB}$ as matrix on $\mathcal{K}_A \times \mathcal{K}_B$ | D | §3.1 from P-Bipartite-Mapping indexing |
| Standard SVD theorem applicable | **I (inherited from linear algebra)** | Mathematical theorem; not derived in this paper |
| Schmidt decomposition form $\Psi^{AB} = \sum_i \lambda_i |u_i\rangle_A \otimes |v_i\rangle_B$ | **I (inherited via standard SVD applied to substrate-level joint amplitude matrix)** | §3.2 — Schmidt form is constructed by applying inherited SVD theorem; not a substrate-level derivation. *(Round-7 relabel: was D conditional on SVD, now I — SVD is standard math inheritance, not derivation.)* |
| Schmidt rank $r = 1$ ↔ factorizability | **I (standard linear algebra)** | §3.3 — standard linear-algebraic fact: rank-1 matrix is outer product. Not substrate-derived. |
| Schmidt rank $r > 1$ ↔ non-factorizability (mathematically provable) | **D** | §3.3 — **substantive content of this paper:** given Schmidt rank > 1, mathematical irreducibility (no $f^A_K g^B_L$ factorization) is the substrate-relevant theorem. Strengthens Paper_063 E-2 from A→assertion to D under P-V5-Schmidt-Generic. |
| V5-bilocal joint content has Schmidt rank > 1 generically | **P (P-V5-Schmidt-Generic)** | §2 substrate-level commitment about V5 content |
| Mixed-state Schmidt generalization | NOT CLAIMED | preamble item 5 |

All rows P, D, I. **No A (asserted) rows.**

---

## 3. Schmidt Decomposition

### 3.1 Joint amplitude as matrix

By Paper_063 P-Bipartite-Mapping, the joint substrate-level amplitude $\Psi_{KL}^{AB}$ is indexed by $(K_A, K_B) \in \mathcal{K}_A \times \mathcal{K}_B$. **Treating this as a complex matrix** $M$ with $M_{KL} = \Psi_{KL}^{AB}$ enables standard SVD machinery.

For finite $|\mathcal{K}_A|, |\mathcal{K}_B|$, $M$ is a finite complex matrix. For countable substrate channel sets, $M$ is a Hilbert-Schmidt-class operator on the Hilbert-space-completion (Paper_007).

### 3.2 SVD → Schmidt form

By standard SVD (inherited mathematical theorem): any complex matrix $M$ admits decomposition $M = U \Sigma V^\dagger$ with $U, V$ unitary and $\Sigma$ diagonal with non-negative entries (the singular values).

Applied to $M_{KL} = \Psi_{KL}^{AB}$:

$$
\Psi_{KL}^{AB} = \sum_{i=1}^{r} U_{Ki}\,\lambda_i\,V_{Li}^*
$$

where $r$ is the number of non-zero singular values, $\lambda_i > 0$ are the singular values (Schmidt coefficients), $U_{Ki}$ defines orthonormal vectors $|u_i\rangle_A = \sum_K U_{Ki}|K\rangle_A$, and $V_{Li}^*$ defines $|v_i\rangle_B = \sum_L V_{Li}|L\rangle_B$.

In ket form:

$$
\boxed{\Psi^{AB} = \sum_{i=1}^{r} \lambda_i\,|u_i\rangle_A \otimes |v_i\rangle_B.}
$$

This is the **standard Schmidt decomposition**.

**Normalization:** for normalized state $\|\Psi^{AB}\| = 1$, $\sum_i \lambda_i^2 = 1$.

**Dimensional check:** $\lambda_i$ are dimensionless Schmidt coefficients (substrate-amplitude-squared units, normalized to 1). ✓

### 3.3 Schmidt rank ↔ factorizability

**Schmidt rank $r = 1$:** $\Psi^{AB} = \lambda_1|u_1\rangle_A \otimes |v_1\rangle_B$ — **factorizable** (Paper_063 E-1).

**Schmidt rank $r > 1$:** $\Psi^{AB}$ is a sum of two or more orthogonal product states; **mathematically provably non-factorizable** (standard linear algebra: a rank-$r$ matrix with $r > 1$ cannot be written as outer product of two vectors).

**Therefore Paper_063 E-2 irreducibility claim is strengthened:** for bipartite states with Schmidt rank $> 1$, non-factorizability is a **mathematical theorem** (via SVD inheritance), no longer A→assertion. The substrate-level commitment is P-V5-Schmidt-Generic — that V5-correlated states generically have Schmidt rank > 1.

### 3.4 V5 content and Schmidt rank

By Paper_063 §3.3, the joint amplitude under V5 cross-chain correlation has form:

$$
\Psi_{KL}^{AB} = P_K^A\,P_L^B + \Delta_{KL}^{AB}.
$$

The first term is rank-1 ($P^A_K P^B_L$ is an outer product). The second term $\Delta_{KL}^{AB}$ is V5-mediated bilocal content.

**By P-V5-Schmidt-Generic (§2):** for non-zero $\Delta_{KL}^{AB}$, the total matrix $\Psi_{KL}^{AB}$ generically has Schmidt rank $> 1$. The substrate-level commitment is that V5 correlation produces non-trivial bilocal structure not absorbable into product-state form.

**Special cases** ($\Delta_{KL}^{AB}$ structured to keep Schmidt rank = 1) are non-generic; standard V5 envelope content produces full-rank Schmidt structure.

### 3.5 Schmidt rank as entanglement measure

- $r = 1$ → product state (no entanglement).
- $r > 1$ → entangled state.
- $r = \min(|\mathcal{K}_A|, |\mathcal{K}_B|)$ → maximally entangled state.

Schmidt rank is the **simplest entanglement measure**; von Neumann entropy + concurrence + negativity (downstream E-6 + entanglement-measures papers) provide refined measures.

---

## 4. Partial Strengthening of Paper_063 E-2

**Paper_063 E-2 irreducibility (round-6 label):** A→assertion — "V5-mediated $\Delta_{KL}^{AB}$ cannot be factored into $f^A_K \cdot g^B_L$."

**Paper_064 partial strengthening (round-7 clarification):** for joint amplitudes with **Schmidt rank > 1**, the mathematical irreducibility (no $f^A_K g^B_L$ factorization) is a **theorem from standard linear algebra** (I via SVD machinery applied to the substrate-level joint amplitude matrix). The substantive content under P-V5-Schmidt-Generic shifts from "V5-bilocal content is irreducible" (Paper_063 A→assertion) to "V5-bilocal content generically has Schmidt rank > 1" (P-V5-Schmidt-Generic) — and given Schmidt rank > 1, mathematical irreducibility follows by inherited SVD machinery.

**This is a partial strengthening, not a full proof.** Two structurally distinct claims are involved:

- **Mathematical-irreducibility given Schmidt rank > 1:** standard linear-algebra theorem (I), inherited.
- **V5-bilocal content generically has Schmidt rank > 1:** substrate-level commitment (P-V5-Schmidt-Generic), **not derived from V5 envelope structure alone in this paper**.

**Paper_063 audit table can be updated** to reflect the split:

- Old row: "Non-factorizable joint amplitude is irreducible | A→assertion".
- New rows (via Paper_064):
  - "V5-bilocal content generically has Schmidt rank > 1 | P (P-V5-Schmidt-Generic)" — substrate-level commitment.
  - "Schmidt rank > 1 implies mathematical irreducibility | I (standard SVD)" — inherited from linear algebra.

The substrate-level commitment is **sharpened and localized** to P-V5-Schmidt-Generic (a statement about V5 bilocal-content Schmidt structure), with the mathematical-irreducibility step now properly labeled as inherited. This is **honest accounting** of where substrate-level content sits vs. where standard math machinery applies.

**Whether P-V5-Schmidt-Generic is derivable from V5 envelope structure (Paper_090) alone is open** — future analysis of V5 bilocal-content matrix structure may convert P-V5-Schmidt-Generic from postulate to theorem (downstream entanglement-arc work).

---

## 5. Falsification Criteria

### 5.1 V5-correlated states with Schmidt rank = 1

**Falsifier sentence:** *Empirical demonstration that V5-correlated bipartite states **generically** have Schmidt rank = 1 — i.e., $\Delta_{KL}^{AB}$ generically produces a rank-1 perturbation absorbable into product-state form — would falsify P-V5-Schmidt-Generic and weaken the E-2 irreducibility claim.*

### 5.2 Standard Schmidt decomposition fails at substrate level

**Falsifier sentence:** *Empirical demonstration that bipartite substrate-level states do not admit Schmidt decomposition in the Hilbert-space-completion (Paper_007) — i.e., standard SVD inheritance fails — would falsify §3.2.*

### 5.3 Schmidt rank does not correlate with empirical entanglement measures

**Falsifier sentence:** *Empirical observation that Schmidt rank computed from substrate-level joint amplitudes does not correlate with empirical entanglement measures (von Neumann entropy, concurrence) at the Hilbert-space level — would suggest substrate-level Schmidt content is decoupled from empirical entanglement, falsifying §3.5.*

### 5.4 Entanglement without Schmidt rank > 1

**Falsifier sentence:** *Empirical observation of bipartite entanglement (non-factorizability + Bell-inequality violation + monogamy structure) without Schmidt rank > 1 — would falsify §3.3's identification of Schmidt rank with non-factorizability.*

---

## 6. Position Statement

**Schmidt decomposition (E-3)** is the standard linear-algebraic application of SVD to bipartite substrate-level joint amplitudes (Paper_063 P-Bipartite-Mapping arena). Under standard SVD inheritance + P-V5-Schmidt-Generic (V5-correlated states generically have Schmidt rank > 1):

- Bipartite pure states have Schmidt form $\Psi^{AB} = \sum_i \lambda_i|u_i\rangle_A \otimes |v_i\rangle_B$.
- Schmidt rank $r$ distinguishes factorizable ($r = 1$) from entangled ($r > 1$).
- Paper_063 E-2 irreducibility is **strengthened** from A→assertion to D-mathematical-irreducibility (via SVD theorem) under P-V5-Schmidt-Generic.

What this paper claims:

- Schmidt decomposition exists for substrate-level bipartite joint amplitudes.
- Schmidt rank is the simplest entanglement measure.
- Paper_063 E-2 irreducibility is mathematically provable for Schmidt-rank-> 1 states.

What this paper does *not* claim:

- Schmidt theorem not derived (inherited mathematical content).
- Mixed-state Schmidt extension not delivered.
- P-V5-Schmidt-Generic not derived from canonical 13 alone.

**Series context.** Paper_064 of entanglement arc. Strengthens Paper_063. Downstream: Papers_065 (monogamy), 066–072 in queue.

---

## Appendix

**Cross-references:** Paper_087, Paper_063, Paper_007, Paper_090.

**Glossary:**
- **Schmidt decomposition.** $\Psi^{AB} = \sum_i \lambda_i|u_i\rangle_A \otimes |v_i\rangle_B$ for bipartite pure states.
- **Schmidt rank $r$.** Number of non-zero Schmidt coefficients; entanglement indicator.
- **P-V5-Schmidt-Generic.** Substrate-level commitment that V5 bilocal content generically has Schmidt rank > 1.

---

**End of Paper_064.**
