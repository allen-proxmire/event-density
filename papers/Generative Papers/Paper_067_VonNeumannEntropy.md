# Paper 067 — Von Neumann Entropy via Shannon–Khinchin (E-6)

> **⚠️ MERGED into Paper_068 (2026-07-05).** This file and `Paper_068_VonNeumannEntropy.md` were the same E-6 result under two numbers, sitting side by side unmarked. Paper_068 occupies the canonical Paper_087 slot and is now the sole canonical reference — its §5 Open Structural Questions was backfilled from this file's fuller list. Kept here for provenance; do not cite this file going forward, cite Paper_068.

**Series:** Wave-2 Generative Papers (Entanglement Arc, E-6)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_063 (E-1 tensor product), Paper_064 (E-3 Schmidt), Paper_065 (E-4 monogamy), Paper_066 (E-5 no-signaling).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that von Neumann entropy is the unique substrate-derivable entanglement measure; alternative measures (Rényi, min-entropy, etc.) are admissible and address different operational regimes.
2. It does **not** claim derivation of specific entropy values for concrete states; values are INHERITED via standard QM matching.
3. It does **not** claim novel empirical predictions beyond standard quantum-information theory.
4. It does **not** introduce new substrate primitives.
5. "Von Neumann entropy" means: $S(\rho) = -\mathrm{Tr}[\rho \log \rho] = -\sum_i \lambda_i \log \lambda_i$ where $\{\lambda_i\}$ are eigenvalues of $\rho$.

---

## Abstract

Von Neumann entropy is FORM-FORCED in ED via the Shannon–Khinchin axioms applied to the substrate participation-measure structure. P02 (Participation) supplies the substrate-level state-content measure; P04 (Bandwidth) supplies the additivity structure; P11 (Commitment-irreversibility) supplies the concavity/monotonicity content; Schmidt decomposition (Paper_064) supplies the diagonal eigenvalue structure on which the entropy is computed. Standard Shannon–Khinchin axioms (continuity, additivity for independent systems, sub-additivity, maximality on uniform distributions) then uniquely fix the entropy function up to a normalization constant; the FORM $-\sum \lambda_i \log \lambda_i$ is FORCED. The COEFFICIENT (base of logarithm, $k_B$-normalization for thermodynamic applications) is INHERITED.

---

## §1 Introduction

Von Neumann entropy is the load-bearing measure of quantum mixedness / entanglement / information content. Standard axiomatic characterization via Shannon–Khinchin axioms uniquely fixes it (up to normalization) among functions of probability distributions.

This paper supplies the substrate audit: the Shannon–Khinchin axioms are FORCED by the substrate's participation-measure structure (P02 + P04 + P11), Schmidt decomposition (Paper_064) supplies the eigenvalue distribution to which the axioms apply, and the von Neumann form follows.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — supplies the substrate-level state-measure content.
- **P04 (Bandwidth)** — supplies additivity for independent systems.
- **P11 (Commitment-irreversibility)** — supplies monotonicity / second-law-like content.

### 2.2 Upstream dependencies

- **I-064:** Schmidt decomposition (Paper_064, E-3) — supplies diagonal eigenvalue structure $\{\lambda_i\}$ of reduced state.
- **I-063:** Tensor-product structure (Paper_063, E-1) — supplies bipartite framework.
- **I-Born:** Born rule (Paper_002) — supplies probability assignment.
- **I-SK:** Shannon–Khinchin axiomatization of entropy (standard math).
- **I-Khinchin:** Khinchin's uniqueness theorem for entropy functions (standard math).

### 2.3 Paper-specific postulates

- **P-Continuity:** The substrate-participation-measure entropy function is continuous in the probability distribution (Shannon–Khinchin axiom 1 analog).
- **P-Additivity:** For independent substrate subsystems (P04 bandwidth-additive), the entropy is additive: $S(\rho_A \otimes \rho_B) = S(\rho_A) + S(\rho_B)$.
- **P-Maximality:** Entropy is maximized on uniform distributions for fixed dimension.

These three axioms are the substrate-level analog of the Shannon–Khinchin axioms; they are declared at the substrate level, then standard Khinchin uniqueness fixes the functional form.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Schmidt decomposition supplies $\{\lambda_i\}$ | I | Paper_064. |
| 2 | Born rule supplies probability content | I | Paper_002. |
| 3 | P02 supplies state-measure content | P | Primitive (Paper_087). |
| 4 | P04 supplies additivity (bandwidth-additive) | P | Primitive. |
| 5 | P11 supplies monotonicity content | P | Primitive. |
| 6 | Substrate-participation-measure entropy continuous | P-Continuity | Postulate. |
| 7 | Entropy additive on independent subsystems | P-Additivity | Postulate. |
| 8 | Entropy maximized on uniform distributions | P-Maximality | Postulate. |
| 9 | Shannon–Khinchin axioms in place | D-via-I | Application of P-Continuity + P-Additivity + P-Maximality (plus implicit sub-additivity from substrate combinatorics). |
| 10 | Unique entropy form $-\sum_i \lambda_i \log \lambda_i$ via Khinchin uniqueness | I | Standard math (I-Khinchin). |
| 11 | Von Neumann entropy $S(\rho) = -\mathrm{Tr}[\rho \log \rho]$ | D-via-I | Application of step 10 to Schmidt eigenvalues. |
| 12 | Base-of-logarithm / $k_B$ normalization | I | Conventional / empirical matching. |
| 13 | Specific entropy values for concrete states | I | Empirical. |

---

## §3 The Derivation

### 3.1 Schmidt eigenvalues from substrate

By I-064, the reduced state $\rho_A = \mathrm{Tr}_B[|\psi\rangle\langle\psi|]$ has Schmidt decomposition with eigenvalues $\{\lambda_i\}$, $\sum_i \lambda_i = 1$, $\lambda_i \geq 0$. These are the substrate-level participation probabilities for the orthogonal Schmidt-basis configurations.

### 3.2 Shannon–Khinchin axioms from substrate primitives

- **P-Continuity:** Substrate-participation entropy is continuous in $\{\lambda_i\}$ (standard regularity).
- **P-Additivity:** For independent subsystems (P04 bandwidth-additive on the substrate side), the entropy is additive. This is the substrate-level expression of P04's "additive scalar" character.
- **P-Maximality:** Entropy is maximized on uniform $\lambda_i = 1/N$ for fixed Schmidt rank $N$. **P-Maximality is declared as the substrate-level analog of the second-law-like content carried by P11 (commitment-irreversibility); uniform distributions correspond to maximum "non-committedness" of the participation measure.** Deriving P-Maximality from P11 quantitatively is **O-vN-2** (OPEN); the analogical justification here is not a derivation.

These three postulates, declared at the substrate level, are the standard Shannon–Khinchin axioms.

### 3.3 Khinchin uniqueness

Khinchin's theorem (I-Khinchin, standard math) states: a function $H(\{p_i\})$ satisfying continuity, additivity, and maximality (plus standard regularity) has the unique form
$$H(\{p_i\}) = -k \sum_i p_i \log p_i$$
for some positive constant $k$ (normalization).

Applied to the Schmidt eigenvalues $\{\lambda_i\}$:
$$S(\rho_A) = -k \sum_i \lambda_i \log \lambda_i = -k \, \mathrm{Tr}[\rho_A \log \rho_A] .$$

### 3.4 Coefficient inheritance

The constant $k$ is INHERITED:
- Information-theory convention: $k = 1$, $\log = \log_2$ (bits) or $\log_e$ (nats).
- Thermodynamic convention: $k = k_B$ (Boltzmann's constant).

The substrate program does not derive $k$ from first principles.

---

## §4 What This Paper Supplies and Does Not Supply

**Supplies:** Substrate origin of the Shannon–Khinchin axioms (P02 + P04 + P11). Substrate audit of von Neumann entropy form via Khinchin uniqueness.

**Does not supply:** Rényi entropies (different axiomatic relaxation — would require alternative postulates). Min-entropy / smooth entropy variants. Numerical values for concrete states. Thermodynamic / black-hole entropy connection (Bekenstein–Hawking) — addressed in Arc BH.

---

## §5 Open Structural Questions

- **O-vN-1:** Substrate derivation of P-Additivity from P04 bandwidth-additivity at quantitative level.
- **O-vN-2:** Substrate derivation of P-Maximality from P11 commitment-irreversibility.
- **O-vN-3:** Rényi-entropy substrate audit (relax P-Additivity to $\alpha$-additivity).
- **O-vN-4:** Connection to Bekenstein–Hawking entropy (Arc BH, Paper_043 area-law).
- **O-vN-5:** Substrate derivation of thermodynamic $k_B$ normalization.

---

## §6 Falsification Criteria

- **F1:** Demonstration that P02 + P04 + P11 do NOT support P-Continuity, P-Additivity, P-Maximality — refutes the substrate origin of Shannon–Khinchin axioms.
- **F2:** Empirical detection of an entropy-like quantum quantity that violates Khinchin uniqueness — would refute the application (and standard quantum information).
- **F3:** Demonstration that Schmidt eigenvalues do NOT give the load-bearing probability content for the entropy — refutes I-064 application.

---

## §7 Position Statement

Von Neumann entropy is **FORM-FORCED** in ED via Shannon–Khinchin axioms applied to the substrate participation-measure structure. P02 + P04 + P11 supply the substrate-level analogs of Shannon–Khinchin axioms; Schmidt decomposition (Paper_064) supplies the eigenvalue distribution; Khinchin uniqueness fixes the form. **Coefficient INHERITED**.

This is the E-6 step of the Entanglement Arc.

---

**End Paper 067 (FIXED).**
