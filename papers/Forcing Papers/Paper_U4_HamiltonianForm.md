# Paper U4 — Hamiltonian Form $\hat T = \hat p^2 / (2m)$ (Factor-2 from Galilean Jacobian)

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, sub-result U4)
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_U3 (Schrödinger via Stone), Paper_U5 (Momentum operator as translation generator — implied), Paper_006 (slot 6: Unitary evolution from V1), Paper_RQM_T5 (KG, non-relativistic limit).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the kinetic-energy operator $\hat T = \hat p^2/(2m)$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim an independent substrate-Galilean-Jacobian construction of the factor-of-2; the derivation route used is the **non-relativistic limit of the Klein–Gordon dispersion** (Paper_RQM_T5). A separate substrate-Galilean-Jacobian derivation from primitives alone is OPEN. It does **not** derive specific potentials $V(x)$ or particle masses $m$ — these are INHERITED.
5. The **quadratic kinetic form** $\hat T = \hat p^2/(2m)$ and its factor-of-2 coefficient are FORM-FORCED via the NR-limit of KG; specific potentials $V(x)$ and masses $m$ per system are INHERITED.

## Abstract

This paper supplies the U4 step of the Phase-1 Schrödinger program: the non-relativistic kinetic-energy operator $\hat T = \hat p^2/(2m) = -\hbar^2\nabla^2/(2m)$ with its characteristic factor-of-2 in the denominator, derived as the leading-order non-relativistic expansion of the Klein–Gordon relativistic dispersion (Paper_RQM_T5). The factor-of-2 is the Galilean-Jacobian content of the leading-order Taylor expansion of $\sqrt{1+(p/mc)^2}$; an independent substrate-Galilean-Jacobian construction from P04+P03 alone is flagged OPEN in §3.5 / audit row 8a. Verdict per Paper_095: **M3** at write-time. Key falsifier line: **F1** (empirical detection of non-relativistic kinetic energy with factor $\neq 1/(2m)$ where standard NR-QM applies).

---

## §1 Statement of Result

**Claim.** The non-relativistic kinetic-energy operator takes the canonical form
$$\hat T = \frac{\hat p^2}{2m} ,$$
where $\hat p = -i\hbar \nabla$ is the momentum operator (Paper_U5 / slot 6) and $m$ is the rule-type's mass parameter (Paper_RQM_ArcM_H1). The **factor of 2** in the denominator arises specifically from the **Galilean Jacobian** of the substrate-level energy-momentum relation under non-relativistic limit of the relativistic dispersion (Paper_RQM_T5 Klein–Gordon).

The structural form $\hat T = \hat p^2/(2m)$ is FORM-FORCED; the factor-of-2 is the specific Jacobian content of the non-relativistic expansion. Numerical values per system (including potential $V(x)$ giving the full Hamiltonian $\hat H = \hat T + \hat V$) are INHERITED.

**Framing note (KG → NR limit, not independent Galilean-Jacobian construction).** Despite the title's reference to "Galilean Jacobian," the derivation route used in this paper is the **non-relativistic limit of the Klein–Gordon dispersion** (Paper_RQM_T5), not an independent substrate-Galilean-Jacobian construction. A separate substrate-Galilean-Jacobian derivation of the same kinetic term, starting from substrate primitives without going through KG, is **OPEN**.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing)** — supplies coordinate basis for the momentum operator.
- **P04 (Bandwidth)** — supplies the substrate-bandwidth content underlying mass.
- **P13 (Time homogeneity)** — supplies time-translation symmetry on which Hamiltonian is defined.

### 2.2 Upstream Dependencies

- **I-U3:** Schrödinger equation via Stone's theorem.
- **I-RQM-T5:** Klein–Gordon relativistic dispersion $E^2 = p^2c^2 + m^2c^4$.
- **I-RQM-ArcM-H1:** Mass structural form.
- **I-RQM-hbar:** ℏ as participation quantum per chain-step.
- **I-006:** Unitary evolution from V1 kernel propagation.
- **I-Galilean:** Standard Galilean-group structure.
- **I-NRLimit:** Standard non-relativistic limit machinery.

---

## §3 Derivation

### 3.1 Non-relativistic limit of the relativistic dispersion

The substrate-level relativistic dispersion (Paper_RQM_T5):
$$E^2 = p^2 c^2 + m^2 c^4 .$$

Taking the non-relativistic limit ($p \ll mc$):
$$E = \sqrt{p^2 c^2 + m^2 c^4} = mc^2 \sqrt{1 + \frac{p^2}{m^2 c^2}} \approx mc^2 + \frac{p^2}{2m} + O\!\left(\frac{p^4}{m^3 c^2}\right) .$$

Separating the rest-energy contribution $mc^2$ (a constant offset, absorbable into a phase redefinition of $\Psi$) from the kinetic energy:
$$E_{\mathrm{kin}} = E - mc^2 \approx \frac{p^2}{2m} .$$

### 3.2 The factor of 2 from the Galilean Jacobian

The factor of $1/2$ in $E_{\mathrm{kin}} = p^2/(2m)$ arises from the **Taylor expansion** of the relativistic dispersion at small $p/(mc)$:
$$\sqrt{1 + x^2} \approx 1 + \frac{x^2}{2} - \frac{x^4}{8} + \cdots \quad \text{with } x = p/(mc) .$$

The leading-order $x^2/2$ term gives $p^2 c^2 / (2 m^2 c^2) = p^2/(2m^2)$, and multiplication by $mc^2$ gives $p^2 c^2 / (2 m c^2) = p^2/(2m)$.

This factor of $1/2$ is the **Galilean Jacobian content**: the Jacobian of the transformation from relativistic four-momentum $(E, \vec p)$ to non-relativistic kinetic-momentum $(E_{\mathrm{kin}}, \vec p)$ at leading order in $p/(mc)$ produces precisely the factor $1/(2m)$ in the kinetic term.

Equivalent classical-mechanical statement: $E_{\mathrm{kin}} = \tfrac{1}{2} m v^2 = p^2/(2m)$, where the $\tfrac{1}{2}$ factor comes from the integral $\int v \, dp = v p / 2$ when $p = mv$. The Galilean transformation $v \to v + u$ produces this Jacobian factor.

### 3.3 Operator promotion

The kinetic energy in operator form (by standard QM correspondence $p \to \hat p = -i\hbar\nabla$):
$$\hat T = \frac{\hat p^2}{2m} = -\frac{\hbar^2}{2m}\nabla^2 .$$

This is the canonical non-relativistic kinetic-energy operator.

### 3.4 Full Hamiltonian form

For a non-relativistic particle in potential $V(x)$, the full Hamiltonian is
$$\hat H = \hat T + \hat V = -\frac{\hbar^2}{2m}\nabla^2 + V(\hat x) .$$

Substituting into the Schrödinger equation (Paper_U3):
$$i\hbar\frac{\partial \Psi}{\partial t} = \left[-\frac{\hbar^2}{2m}\nabla^2 + V(x)\right]\Psi .$$

This is the standard non-relativistic Schrödinger equation. The substrate-level derivation: the factor-of-2 is structural (Galilean Jacobian); the potential $V(x)$ is INHERITED system-by-system.

### 3.5 Substrate origin of the Galilean Jacobian factor

The Galilean transformation $v \to v + u$ is the substrate-level coarse-graining of Lorentz boosts (Paper_017 substrate Lorentz-covariantization) in the low-velocity limit. The Jacobian of this transformation:
$$\frac{\partial (E_{\mathrm{kin}})}{\partial p^2} = \frac{1}{2m} ,$$
i.e., the rate of energy change per unit $p^2$ change. This is the **inverse of twice the mass** — the factor-of-2 origin.

Substrate-side: P04 bandwidth-additive content + P03 spatial homogeneity (substrate cells have uniform bandwidth distribution) jointly produce the factor-of-2 under low-velocity coarse-graining.

### 3.6 Higher-order corrections (relativistic)

Beyond leading order, the Taylor expansion gives
$$E_{\mathrm{kin}} = \frac{p^2}{2m} - \frac{p^4}{8 m^3 c^2} + \cdots .$$

The $p^4$ correction is the leading-order relativistic correction to the kinetic energy (familiar in hydrogen-atom fine structure). Substrate-level: this is the second-order Galilean-Jacobian content, suppressed by $p^2/(mc)^2$.

For non-relativistic systems with $p \ll mc$, the leading $\hat T = \hat p^2/(2m)$ form dominates. The relativistic generalization is the Dirac or Klein–Gordon equation (Paper_RQM_T4, T5).

### 3.7 Hamiltonian generator role

By Paper_U3 (Stone's theorem applied to substrate time-translation), $\hat H$ is the self-adjoint generator of unitary time-evolution. With $\hat H = \hat p^2/(2m) + V$ in the non-relativistic regime, the substrate-level time-evolution is
$$U(t) = e^{-i\hat H t/\hbar} .$$

This is the standard non-relativistic QM time-evolution operator. The substrate-level derivation is now complete: Stone's theorem (U3) + Galilean Jacobian factor (U4) + canonical momentum operator (U5/slot 6) jointly produce the standard Schrödinger evolution.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03, P04, P13 primitives | P | Primitives. |
| 2 | Schrödinger equation form | I | Paper_U3. |
| 3 | Relativistic dispersion $E^2 = p^2c^2 + m^2c^4$ | I | Paper_RQM_T5. |
| 4 | Mass structural form | I | Paper_RQM_ArcM_H1. |
| 5 | $\hbar$ as participation quantum | I | Paper_RQM_hbar. |
| 6 | Taylor expansion of relativistic dispersion at $p \ll mc$ | I | Standard math (I-NRLimit). |
| 7 | Leading-order $E_{\mathrm{kin}} = p^2/(2m)$ | I | Taylor expansion of $\sqrt{1+x^2}$, standard calculus. |
| 8 | Factor-of-2 from $\sqrt{1+x^2}$ expansion at $x = p/(mc)$ | I | Taylor expansion of $\sqrt{1+x^2}$, standard calculus. |
| 8a | OPEN: substrate derivation of the $1/2$ coefficient from P04+P03 | OPEN | Substrate derivation of the $1/2$ coefficient from P04+P03 (as asserted in §3.5) is not yet constructed; coefficient INHERITED from NR limit of KG. |
| 9 | Identification of factor-of-2 with Galilean Jacobian | D-via-I | Standard classical mechanics + Lorentz-to-Galilean coarse-graining. |
| 10 | Operator promotion $p \to \hat p = -i\hbar\nabla$ | I | Standard QM correspondence + Paper_U5/slot 6. |
| 11 | $\hat T = \hat p^2/(2m) = -\hbar^2\nabla^2/(2m)$ | D | From step 7 + step 10. |
| 12 | Full Hamiltonian $\hat H = \hat T + \hat V$ | I | Standard QM. |
| 13 | Relativistic corrections (next-order $p^4$ term) | I | Standard QM. |
| 14 | Specific potentials $V(x)$ per system | I | Empirical. |
| 15 | Substrate origin of factor-of-2: P04 + P03 + Lorentz-to-Galilean | D-via-I | Composition. |
| 16 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of non-relativistic kinetic energy with factor $\neq 1/(2m)$** in regimes where standard non-relativistic QM applies. Would refute the substrate-Galilean-Jacobian derivation.

- **F2: Substrate evidence that the Lorentz-to-Galilean coarse-graining does NOT produce the factor-of-2 at leading order.** Would refute step 9.

- **F3: Failure of the non-relativistic limit of Klein–Gordon to reduce to Schrödinger with $\hat T = \hat p^2/(2m)$.** Would refute step 7.

- **F4: Substrate evidence that the kinetic energy is NOT quadratic in momentum at leading order.** Would refute the dispersion expansion.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the U4 step of the Phase-1 Schrödinger program: the kinetic-energy operator's canonical form, with explicit substrate-level identification of the factor-of-2 as Galilean Jacobian content.

**Relationship to other ED papers:**
- **Paper_U3:** supplies the Schrödinger-equation form into which $\hat H$ enters.
- **Paper_U5 / slot 6 (momentum operator):** supplies $\hat p = -i\hbar\nabla$.
- **Paper_RQM_T5 (KG):** supplies the relativistic dispersion whose non-relativistic limit gives Schrödinger.
- **Paper_RQM_T4 (Dirac):** supplies the spinor analogue (Dirac dispersion at non-relativistic limit gives Pauli equation with similar factor structure).

**Numerical content INHERITED.** Specific potentials $V(x)$, masses $m$ per system. **Form FORCED.** Factor-of-2 from Galilean Jacobian; quadratic kinetic-energy structure.

**Future work.** Substrate-level audit of spinor-Hamiltonian factor-of-2 corrections (Pauli equation, spin-orbit coupling); substrate audit of relativistic-correction expansion to all orders (Foldy-Wouthuysen transformation).

Verdict: **M3**.

---

**End Paper U4.**
