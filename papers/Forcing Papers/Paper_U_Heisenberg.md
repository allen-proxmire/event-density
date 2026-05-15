# Paper U-Heisenberg — Heisenberg Uncertainty $\Delta x \, \Delta p \geq \hbar/2$ from Four-Band Partition

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program)
**Status:** Wave-3 generative paper; **M3** verdict (form-FORCED from canonical commutation + Cauchy-Schwarz; numerical $\hbar/2$ INHERITED; declares P-FourBand)
**Companions:** Paper_U5 (momentum operator), Paper_RQM_T8 (canonical commutation), Paper_U2_Continuum, Paper_RQM_hbar.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the Heisenberg uncertainty bound $\Delta x\,\Delta p \geq \hbar/2$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim derivation of the bare Heisenberg bound from substrate — the Robertson 1929 standard operator-algebra derivation is INHERITED. ED's contribution is the four-band refinement (P-FourBand declared).
5. Form INHERITED via Robertson 1929 from canonical commutation $[\hat x, \hat p] = i\hbar$ + Cauchy-Schwarz; numerical $\hbar/2$ INHERITED; substrate-level four-band partition is declared as P-FourBand (§2.3) with substrate-derivation OPEN.

---

## Abstract

This paper derives the Heisenberg uncertainty principle $\Delta x\,\Delta p \geq \hbar/2$ as a direct consequence of canonical commutation $[\hat x, \hat p] = i\hbar$ + Cauchy-Schwarz on substrate state-vectors, with ED's distinctive contribution being a four-band partition (position / momentum / time / energy) of substrate measurement content declared as P-FourBand (§2.3). The Robertson 1929 form is INHERITED; the structural form is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3); the numerical $\hbar/2$ is VALUE-INHERITED. The four-band orthogonality postulate has substrate-derivation OPEN. Verdict: **M3** per Paper_095's three-tier verdict grammar. Key falsifier **F1**: empirical detection of a substrate-conditioned four-band refinement violation beyond standard Robertson form.

---

## §1 Statement of Result

**Claim.** The Heisenberg uncertainty principle
$$\Delta x \,\Delta p \geq \frac{\hbar}{2}$$
is **form-IDENTIFIED** in ED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) as a direct mathematical consequence of:
1. The canonical commutation relation $[\hat x, \hat p] = i\hbar$ (Paper_RQM_T8 / Paper_U5).
2. The Cauchy-Schwarz inequality applied to substrate state-vectors in the continuum Hilbert space (Paper_U2_Continuum).
3. The substrate-level **four-band partition** of measurement content — the distinction between **adjacency-bandwidth** (position-sector) and **propagation-bandwidth** (momentum-sector) at the substrate-cell level.

The structural form is form-IDENTIFIED. The constant $\hbar$ is VALUE-INHERITED (Paper_RQM_hbar).

Verdict: **M3** — form FORCED via Cauchy-Schwarz on canonical commutation; numerical $\hbar/2$ INHERITED; the four-band partition is declared as P-FourBand (§2.3).

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies adjacency-bandwidth structure (position content).
- **P04 (Bandwidth)** — supplies propagation-bandwidth structure (momentum content).
- **P10 (Rule-type primitive)** — supplies rule-type carriers.

### 2.2 Upstream Dependencies

- **I-U2-Continuum:** Continuum sesquilinear inner-product.
- **I-U5:** Momentum operator $\hat p = -i\hbar\nabla$.
- **I-RQM-T8:** Canonical commutation $[\hat x, \hat p] = i\hbar$.
- **I-RQM-hbar:** $\hbar$ as participation quantum.
- **I-CauchySchwarz:** Standard Cauchy-Schwarz inequality.
- **I-Robertson:** Standard Robertson-Schrödinger uncertainty machinery (Robertson 1929).

### 2.3 Declared paper-specific postulates

- **P-FourBand:** Substrate-level four-band partition of bandwidth $b_K$ — orthogonal independent partitions into position-band (P03 adjacency), momentum-band (P04 propagation), time-band (P13), and energy-band (P-RB-1). Substrate-level derivation of the four-band orthogonality from the 13 primitives alone is **OPEN**.

---

## §3 Derivation

### 3.1 Four-band partition

At substrate level, measurement-bandwidth content separates into four bands:
1. **Position-band (P03 adjacency):** content distinguishing substrate cells by spatial-locus indexing.
2. **Momentum-band (P04 propagation):** content distinguishing substrate cells by translation-rate (P05 polarity-transport rate).
3. **Time-band (P13):** content distinguishing substrate cells by temporal indexing.
4. **Energy-band:** content distinguishing substrate cells by rate-of-becoming (P-RB-1, Paper_012).

The position-band and momentum-band are **orthogonal partitions** of the substrate measurement content: a substrate cell has independent adjacency content (position) and propagation content (momentum). The four-band partition makes this orthogonality explicit at substrate level.

### 3.2 Variance and standard deviation in substrate Hilbert space

For a substrate state $|\Psi\rangle \in \mathcal{H}$ (Paper_U2_Continuum), the **expectation value** of operator $\hat O$ is $\langle\hat O\rangle = \langle\Psi|\hat O|\Psi\rangle$. The **variance** is
$$(\Delta O)^2 = \langle\hat O^2\rangle - \langle\hat O\rangle^2 = \langle(\hat O - \langle\hat O\rangle)^2\rangle .$$

Define centered operators $\hat A = \hat x - \langle\hat x\rangle$ and $\hat B = \hat p - \langle\hat p\rangle$. Then $(\Delta x)^2 = \langle\hat A^2\rangle$ and $(\Delta p)^2 = \langle\hat B^2\rangle$.

### 3.3 Cauchy-Schwarz application

By Cauchy-Schwarz on inner products: for vectors $|\alpha\rangle = \hat A|\Psi\rangle$ and $|\beta\rangle = \hat B|\Psi\rangle$,
$$|\langle\alpha|\beta\rangle|^2 \leq \langle\alpha|\alpha\rangle \cdot \langle\beta|\beta\rangle = \langle\hat A^2\rangle \cdot \langle\hat B^2\rangle = (\Delta x)^2 (\Delta p)^2 .$$

The inner product $\langle\alpha|\beta\rangle = \langle\Psi|\hat A\hat B|\Psi\rangle$. Its imaginary part is
$$\mathrm{Im}\langle\alpha|\beta\rangle = \frac{1}{2i}\langle\Psi|[\hat A, \hat B]|\Psi\rangle = \frac{1}{2i}\langle[\hat x, \hat p]\rangle ,$$
using $[\hat A, \hat B] = [\hat x, \hat p]$ (constants commute).

### 3.4 Substituting the canonical commutator

By Paper_RQM_T8, $[\hat x, \hat p] = i\hbar$. Therefore
$$\mathrm{Im}\langle\alpha|\beta\rangle = \frac{1}{2i}(i\hbar) = \frac{\hbar}{2} .$$

Since $|\langle\alpha|\beta\rangle|^2 \geq (\mathrm{Im}\langle\alpha|\beta\rangle)^2 = \hbar^2/4$:
$$(\Delta x)^2 (\Delta p)^2 \geq \frac{\hbar^2}{4} ,$$
$$\Delta x \,\Delta p \geq \frac{\hbar}{2} .$$

This is the **Heisenberg uncertainty principle**.

### 3.5 Substrate origin of the uncertainty

The substrate-level account: the four-band partition (§3.1) establishes that position-bandwidth (P03 adjacency) and momentum-bandwidth (P04 propagation) are **orthogonal independent partitions** of substrate measurement content. Their canonical commutation $[\hat x, \hat p] = i\hbar$ is the substrate-level statement that **simultaneous determination** of position-bandwidth AND momentum-bandwidth is bounded by the substrate participation quantum $\hbar$.

The substrate participation budget per chain-step ($\hbar$, Paper_RQM_hbar) sets the minimal **joint indeterminacy** between position and momentum content. This is the substrate-level structural origin of Heisenberg uncertainty.

### 3.6 Saturation condition

Heisenberg uncertainty is saturated ($\Delta x\,\Delta p = \hbar/2$) by **minimum-uncertainty states** — Gaussian wavepackets centered on $\langle\hat x\rangle, \langle\hat p\rangle$. Substrate-level: these states represent the **most-tightly-localized** substrate participation content consistent with the canonical commutation constraint.

Other states (e.g., position eigenstates, momentum eigenstates) saturate one of $\Delta x = 0$ or $\Delta p = 0$ but diverge in the conjugate variable.

### 3.7 Generalization to Robertson-Schrödinger

For arbitrary self-adjoint observables $\hat A, \hat B$, the Robertson-Schrödinger uncertainty relation is
$$\Delta A\,\Delta B \geq \frac{|\langle[\hat A, \hat B]\rangle|}{2} .$$

This paper's derivation specializes to $\hat A = \hat x, \hat B = \hat p$. The same Cauchy-Schwarz machinery applied to other commutator pairs (angular momentum, spin, etc.) produces the corresponding uncertainty relations. All inherit from the substrate-level four-band partition + canonical commutators.

### 3.8 Numerical content

- $\hbar/2$ in the uncertainty bound: INHERITED via $\hbar$ value.
- Form $\Delta x\,\Delta p \geq \hbar/2$: form-IDENTIFIED.
- Specific quantum states' uncertainty values: INHERITED via standard QM matching.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 spatial homogeneity (adjacency-bandwidth) | P | Primitive. |
| 2 | P04 bandwidth (propagation-bandwidth) | P | Primitive. |
| 3 | Four-band partition (position / momentum / time / energy) | P | P-FourBand (§2.3); substrate-derivation OPEN. |
| 4 | Continuum Hilbert space | I | Paper_U2_Continuum. |
| 5 | Momentum operator $\hat p = -i\hbar\nabla$ | I | Paper_U5. |
| 6 | Canonical commutation $[\hat x, \hat p] = i\hbar$ (CCR input) | I | Paper_RQM_T8 / Paper_U5. |
| 7 | Centered operators $\hat A = \hat x - \langle\hat x\rangle$, $\hat B = \hat p - \langle\hat p\rangle$ | I | Standard QM. |
| 8 | Variance $(\Delta x)^2 = \langle\hat A^2\rangle$ | I | Standard QM. |
| 9 | Cauchy-Schwarz $|\langle\alpha|\beta\rangle|^2 \leq \langle\alpha|\alpha\rangle\langle\beta|\beta\rangle$ | I | Standard math (I-CauchySchwarz). |
| 10 | Robertson inequality $\Delta A\,\Delta B \geq |\langle[\hat A,\hat B]\rangle|/2$ | I | Robertson 1929; standard operator algebra. |
| 11 | Composition: CCR + Robertson $\Rightarrow$ $\Delta x\,\Delta p \geq \hbar/2$ | D-via-I | Standard composition on substrate-adapted operators. |
| 12 | Saturation by Gaussian wavepackets | I | Standard QM. |
| 13 | Robertson-Schrödinger generalization | I | Standard math (I-Robertson). |
| 14 | Verdict M3 (form FORCED, value INHERITED in $\hbar$, P-FourBand declared) | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Discovery of an empirical violation of the substrate-conditioned four-band partition's predicted refinement of the Heisenberg bound (beyond the standard Robertson form) would falsify the four-band identification. (Violation of the Heisenberg bound itself falsifies QM globally, not ED-specifically.)
- **F2:** Canonical commutation $[\hat x, \hat p] \neq i\hbar$ (Paper_RQM_T8 falsifier) — propagates here.
- **F3:** Cauchy-Schwarz failing in substrate Hilbert space — refutes step 9.
- **F4:** Four-band partition shown inconsistent at substrate level — refutes §3.1.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level Heisenberg uncertainty principle as a direct consequence of canonical commutation + Cauchy-Schwarz applied to the substrate four-band partition.

**Relationship to other ED papers:**
- **Paper_U5:** supplies $\hat p$ operator.
- **Paper_RQM_T8:** supplies the canonical commutator.
- **Paper_RQM_hbar:** supplies $\hbar$.

**Numerical content INHERITED.** $\hbar/2$ via $\hbar$ value. **Form IDENTIFIED.** Heisenberg uncertainty structural form (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

**Future work.** Substrate audit of Robertson-Schrödinger generalization to arbitrary observable pairs; substrate audit of entropic uncertainty relations (Maassen-Uffink).

Verdict: **M3**.

---

**End Paper U-Heisenberg.**
