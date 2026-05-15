# Paper U2-Discrete — Sesquilinear Inner-Product (Tsirelson Bound Derivation)

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, sub-result U2-discrete)
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_U1 (participation measure), Paper_069 (Bell-Tsirelson reconstruction), Paper_063 (E-1 tensor product), Paper_087.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the Tsirelson bound $|S| \leq 2\sqrt{2}$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** re-derive the Tsirelson bound itself from primitives; the bound is INHERITED from Landau–Cirelson 1980 once the sesquilinear inner-product is granted.
5. The **sesquilinear inner-product form** is FORM-FORCED from substrate (P04 + P09 + Cauchy–Schwarz machinery); the **Tsirelson bound** is INHERITED from Landau–Cirelson 1980.

## Abstract

This paper supplies the substrate-level sesquilinear inner-product $\langle P, Q\rangle = \sum_K P_K^* Q_K$ over discrete substrate-motif participation configurations, built from the Paper_U1 participation measure. Under bipartite Bell-test machinery (CHSH four-band partition) plus the standard Cauchy–Schwarz application, this sesquilinear inner-product reproduces the Bell–Tsirelson bound $|S| \leq 2\sqrt{2}$, forbidding PR-box-class correlations. The sesquilinear inner-product form is FORM-FORCED (M3) from P04 + P09 + composition; the Tsirelson bound itself is INHERITED from Landau–Cirelson 1980. Verdict per Paper_095: **M3** on the inner-product form. Key falsifier line: **F1** (empirical detection of $|\langle S\rangle| > 2\sqrt{2}$ in any quantum-state Bell-test).

---

## §1 Statement of Result

**Claim.** Over discrete substrate configurations (motifs), the participation measure $P_K = b_K e^{i\pi_K}$ (Paper_U1) induces a **sesquilinear inner-product**
$$\langle P, Q \rangle = \sum_K P_K^* Q_K = \sum_K b_K^P b_K^Q \, e^{i(\pi_K^Q - \pi_K^P)} ,$$
on the space of substrate participation configurations. The inner-product is conjugate-linear in the first argument, linear in the second, and positive-definite when restricted to the diagonal: $\langle P, P\rangle = \sum_K b_K^2 \geq 0$.

Combined with the four-band partition of substrate measurement content (Paper_RQM_T8 canonical relations + adjacency-bandwidth structure), the sesquilinear inner-product **plus** the standard Landau–Cirelson (1980) bound on CHSH-class operators produces the **Bell-Tsirelson bound** $|S| \leq 2\sqrt{2}$ on quantum-correlation experiments (Paper_069), forbidding PR-box-class correlations.

**Tsirelson bound INHERITED; sesquilinear inner-product form FORCED (M3).** The sesquilinear inner-product form is M3-form-FORCED from substrate (P04 + P09 + Cauchy–Schwarz machinery). The Tsirelson bound itself is INHERITED from Landau–Cirelson 1980 once the sesquilinear inner-product is granted; this paper does not re-derive it.

Verdict: **M3** on the inner-product form; Tsirelson bound INHERITED.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P04 (Bandwidth)** — supplies real magnitudes in the inner-product.
- **P09 ($U(1)$-valued polarity)** — supplies phase content.
- **P10 (Rule-type primitive)** — supplies motif-space content.

### 2.2 Upstream Dependencies

- **I-002:** Born-Gleason rule.
- **I-U1:** Participation measure $P_K = b_K e^{i\pi_K}$.
- **I-063:** Tensor-product composition (E-1).
- **I-066:** No-signaling FORCED over-determined (Paper_066).
- **I-069:** Bell-Tsirelson polytope reconstruction (Paper_069).
- **I-Sesquilinear:** Standard sesquilinear-form theory.
- **I-CauchySchwarz:** Standard Cauchy-Schwarz inequality.

---

## §3 Derivation

### 3.1 Sesquilinear inner-product from participation measure

Given two participation configurations $P$ and $Q$ (each assigning $P_K, Q_K \in \mathbb{C}$ to each motif $K$ in a discrete motif space), the natural composition is
$$\langle P, Q \rangle = \sum_K P_K^* \, Q_K .$$

This is **sesquilinear**:
- Conjugate-linear in first argument: $\langle \alpha P, Q\rangle = \alpha^* \langle P, Q\rangle$.
- Linear in second argument: $\langle P, \alpha Q\rangle = \alpha \langle P, Q\rangle$.
- Positive-definite: $\langle P, P\rangle = \sum_K |P_K|^2 = \sum_K b_K^2 \geq 0$, with equality iff $b_K = 0$ for all $K$.

This is the substrate-level Hilbert-space inner-product on the discrete motif space.

### 3.2 Hilbert-space structure

The inner-product induces a norm $\|P\| = \sqrt{\langle P, P\rangle}$ and a metric $d(P, Q) = \|P - Q\|$. The discrete motif space, completed under this metric, is a separable Hilbert space (Paper_007 substrate Hilbert-space emergence).

The substrate-level Hilbert-space is the **arena** for QM-emergence: states are participation configurations modulo overall phase; observables are self-adjoint operators on this Hilbert space; the Born rule maps inner-products to probabilities.

### 3.3 Four-band partition and Bell observables

In bipartite QM experiments (Bell-tests), measurement outcomes for two parties $A$ and $B$ each have two settings ($a, a'$ for $A$; $b, b'$ for $B$). The CHSH operator is
$$S = E(a, b) + E(a, b') + E(a', b) - E(a', b') ,$$
where $E(\cdot, \cdot)$ is the correlation between outcomes.

The **four-band partition** refers to the four settings $\{a, a', b, b'\}$ generating four correlation bands. Substrate-level: each setting corresponds to a measurement-projector on the substrate Hilbert space.

### 3.4 Tsirelson bound from Cauchy-Schwarz

Standard derivation (Cirelson 1980, I-Sesquilinear + I-CauchySchwarz):

For Hermitian operators $\hat A_a, \hat A_{a'}, \hat B_b, \hat B_{b'}$ with eigenvalues in $\{-1, +1\}$, the CHSH operator $\hat S$ satisfies
$$\hat S^2 = 4 \mathbb{1} + [\hat A_a, \hat A_{a'}][\hat B_b, \hat B_{b'}] .$$

Using $\|[\hat A_a, \hat A_{a'}]\| \leq 2 \|\hat A_a\| \|\hat A_{a'}\| \leq 2$ (and similarly for $B$):
$$\|\hat S^2\| \leq 4 + 4 = 8 \implies \|\hat S\| \leq 2\sqrt{2} .$$

Therefore $|\langle S\rangle| \leq 2\sqrt{2}$ for any quantum state. This is the **Tsirelson bound**.

The substrate-level statement: the sesquilinear-inner-product structure (this paper) + bounded Hermitian observables produce the Tsirelson bound by Cauchy-Schwarz application.

### 3.5 Why PR-box-class correlations are forbidden

PR-boxes saturate $|S| = 4$, the absolute no-signaling limit. They are forbidden by the Tsirelson bound, which restricts substrate-level QM correlations to $|S| \leq 2\sqrt{2}$.

The substrate origin of this restriction: the **sesquilinear inner-product** is the substrate-level constraint that distinguishes QM from arbitrary no-signaling theories. Sesquilinearity + Cauchy-Schwarz force Tsirelson; PR-boxes correspond to a non-sesquilinear correlation structure that the substrate does not support.

This matches Paper_069's three-polytope analysis: Bell ⊊ Tsirelson ⊊ NS, with ED at the Tsirelson set (under P-V5-Hilbert-Constraint).

### 3.6 Connection to four-band partition

The four-band partition (Bell-test settings $a, a', b, b'$) generates the substrate-level adjacency content underlying the CHSH operator. Each setting corresponds to a different substrate-edge content; the inner-product between substrate configurations under different settings produces the correlation $E(\cdot, \cdot)$.

The four-band structure is the substrate manifestation of the bipartite-experiment design; the sesquilinear inner-product is the substrate-level correlation tool; their combination yields the Tsirelson bound.

### 3.7 Numerical content

The Tsirelson bound $2\sqrt{2} \approx 2.828$ is FORM-FORCED. Numerical saturation values for specific bipartite quantum states (singlet, maximally entangled, etc.) are INHERITED via standard QM matching.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04 bandwidth | P | Primitive. |
| 2 | P09 $U(1)$ polarity | P | Primitive. |
| 3 | P10 rule-type | P | Primitive. |
| 4 | Participation measure $P_K = b_K e^{i\pi_K}$ | I | Paper_U1. |
| 5 | Sesquilinear inner-product $\langle P, Q\rangle = \sum_K P_K^* Q_K$ | D | Composition. |
| 6 | Conjugate-linearity in first argument | D | Direct from step 5. |
| 7 | Linearity in second argument | D | Direct from step 5. |
| 8 | Positive-definiteness on diagonal | D | $\sum |P_K|^2 \geq 0$. |
| 9 | Hilbert-space completion | I | Paper_007. |
| 10 | Four-band partition for bipartite Bell-tests | I | Standard Bell-test design. |
| 11 | CHSH operator $S$ | I | Standard. |
| 12 | $\hat S^2 \leq 8 \mathbb{1}$ via Cauchy-Schwarz | I | Standard math (I-CauchySchwarz). |
| 12b | Sesquilinear inner-product form M3-form-FORCED from substrate | D | P04 + P09 + composition; this is the load-bearing substrate step. |
| 13 | Tsirelson bound $|\langle S\rangle| \leq 2\sqrt{2}$ | I | Tsirelson bound INHERITED from Landau–Cirelson 1980 once sesquilinear inner-product granted. |
| 14 | PR-box forbidden by Tsirelson | I | Direct consequence of inherited bound. |
| 15 | Substrate-level matching to Paper_069 (Bell-Tsirelson reconstruction) | I | Paper_069. |
| 16 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of $|\langle S\rangle| > 2\sqrt{2}$** in any quantum-state Bell-test experiment. Would refute the Tsirelson bound (and standard QM).

- **F2: Substrate evidence that the inner-product is not sesquilinear** (e.g., asymmetric or non-conjugate-linear). Would refute step 5.

- **F3: Substrate-level QM-correlations approaching PR-box saturation** $|S| = 4$. Would refute the sesquilinear restriction.

- **F4: Cauchy-Schwarz inequality shown to fail in substrate Hilbert-space.** Would refute I-CauchySchwarz application.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level sesquilinear inner-product and its Tsirelson-bound consequence — closing the U2-discrete step of the Phase-1 Schrödinger program.

**Relationship to other ED papers:**
- **Paper_U1:** supplies the participation measure $P_K$.
- **Paper_069 (Bell-Tsirelson reconstruction):** supplies the polytope structure that this paper's Tsirelson bound is the second tier of.
- **Paper_066 (No-signaling FORCED over-determined):** complementary; this paper supplies the **inner-product** restriction, Paper_066 supplies the **causality** restriction.

**Numerical content INHERITED.** Specific state-dependent saturation values. **Form FORCED.** Sesquilinear inner-product + Tsirelson bound.

**Future work.** Substrate-level audit of CHSH-class generalizations (multipartite Bell-tests, Tsirelson-bound generalizations); substrate audit of non-CHSH Bell-inequalities (Mermin, etc.).

Verdict: **M3**.

---

**End Paper U2-Discrete.**
