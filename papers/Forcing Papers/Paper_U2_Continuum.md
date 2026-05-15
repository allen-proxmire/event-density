# Paper U2-Continuum — Inner-Product Extension to Continuum Configurations

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, sub-result U2-continuum)
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_U1, Paper_U2_Discrete, Paper_073 (DCGT), Paper_087.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the continuum $L^2(\mathcal{M}, d\mu)$ Hilbert-space inner-product from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates (P-ScaleSeparation, §2).
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim derivation of the specific volume element $d\mu(x)$ for arbitrary configuration manifolds (Euclidean, curved, Lorentzian); these are INHERITED via standard-QM matching.
5. The **continuum sesquilinear inner-product form** on $L^2(\mathcal{M}, d\mu)$ is FORM-CONSISTENT under DCGT (form-FORCED in the A→regime); the **measure conventions** for specific manifolds are INHERITED.

## Abstract

This paper extends the discrete sesquilinear inner-product (Paper_U2_Discrete) to the continuum-configuration regime via DCGT coarse-graining (Paper_073), yielding the continuum form $\langle\Psi,\Phi\rangle = \int_{\mathcal{M}} \Psi^*(x)\Phi(x)\,d\mu(x)$ on the standard $L^2(\mathcal{M},d\mu)$ Hilbert space. The extension is form-CONSISTENT under the paper-local postulate P-ScaleSeparation ($\ell_{ED} \ll R_{cg} \ll L_{flow}$) and preserves sesquilinearity, gauge invariance under $U(1)$ phase rotation, and the Tsirelson bound. Verdict per Paper_095: **M3** at write-time. Key falsifier line: **F1** (substrate evidence that DCGT fails to preserve sesquilinearity in the continuum limit would refute the extension).

---

## §1 Statement of Result

**Claim.** The sesquilinear inner-product over discrete substrate motifs (Paper_U2_Discrete) extends, under DCGT coarse-graining (Paper_073), to the continuum-configuration regime. The continuum inner-product takes the form
$$\langle \Psi, \Phi \rangle = \int_{\mathcal{M}} \Psi^*(x) \, \Phi(x) \, d\mu(x) ,$$
where $\Psi, \Phi$ are continuum participation-amplitude wavefunctions, $\mathcal{M}$ is the continuum configuration manifold, and $d\mu(x)$ is a **gauge-invariant integration measure** inherited from substrate-level participation budget content (P04).

The structural form is form-CONSISTENT under DCGT A→regime, given the scale separation $\ell_{ED} \ll R_{cg} \ll L_{flow}$ (P-ScaleSeparation, see §2) + P04 + sesquilinear discrete inner-product (Paper_U2_Discrete) + DCGT coarse-graining. The measure $d\mu(x)$ is INHERITED via standard-QM matching for specific configuration manifolds (Euclidean, Lorentzian, etc.).

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies continuum-coordinate structure.
- **P04 (Bandwidth)** — supplies integration-measure content.
- **P09 ($U(1)$-valued polarity)** — supplies gauge-invariance content.
- **P-ScaleSeparation (paper-local postulate, DCGT A→regime):** $\ell_{ED} \ll R_{cg} \ll L_{flow}$ — the substrate cell scale, the coarse-graining radius, and the continuum-flow length-scale form a clean three-tier hierarchy. The DCGT continuum limit is only form-CONSISTENT inside this regime.

### 2.2 Upstream Dependencies

- **I-U1:** Participation measure $P_K = b_K e^{i\pi_K}$.
- **I-U2-Discrete:** Sesquilinear discrete inner-product.
- **I-073:** DCGT coarse-graining bridge.
- **I-089:** V1 finite-width retarded kernel (supplies smoothness).
- **I-002:** Born-Gleason rule.
- **I-Hilbert:** Standard Hilbert-space completion machinery.

---

## §3 Derivation

### 3.1 Discrete-to-continuum transition

In the discrete regime (Paper_U2_Discrete), participation configurations $P$ assign $P_K \in \mathbb{C}$ to each motif $K$ in a discrete motif space. The discrete inner-product is
$$\langle P, Q \rangle_{\mathrm{discrete}} = \sum_K P_K^* \, Q_K .$$

Under DCGT coarse-graining (Paper_073), the discrete motif space transitions to a continuum configuration manifold $\mathcal{M}$. Each substrate motif corresponds to a small region of $\mathcal{M}$; the discrete sum $\sum_K$ becomes a continuum integral $\int_{\mathcal{M}}$; the discrete $P_K$ becomes a continuum wavefunction $\Psi(x)$.

The natural extension:
$$\langle \Psi, \Phi \rangle = \int_{\mathcal{M}} \Psi^*(x) \, \Phi(x) \, d\mu(x) .$$

### 3.2 The integration measure $d\mu(x)$

The measure $d\mu(x)$ inherits from the substrate-level bandwidth-content distribution. In the canonical case (spatially homogeneous substrate, P03), $d\mu(x) = d^3x$ (standard Lebesgue measure on $\mathbb{R}^3$).

For configuration manifolds with non-trivial geometry (e.g., curved spacetime, configuration spaces with topological structure), $d\mu(x)$ includes the appropriate geometric volume element:
$$d\mu(x) = \sqrt{|\det g(x)|} \, d^d x ,$$
with $g(x)$ the configuration-space metric.

### 3.3 Gauge invariance of the measure

By P09 ($U(1)$-valued polarity), substrate participation phases transform under $U(1)$ gauge transformations $\Psi \to e^{i\alpha(x)}\Psi$. The inner-product is gauge-invariant:
$$\langle e^{i\alpha}\Psi, e^{i\alpha}\Phi \rangle = \int (e^{i\alpha}\Psi)^* (e^{i\alpha}\Phi) \, d\mu = \int \Psi^* e^{-i\alpha} e^{i\alpha} \Phi \, d\mu = \int \Psi^* \Phi \, d\mu = \langle \Psi, \Phi\rangle .$$

The gauge-invariance is automatic. The measure $d\mu(x)$ is also gauge-invariant — it inherits from the substrate-bandwidth content (P04), which is gauge-invariant.

This is the substrate origin of the gauge-invariance of the standard QM inner-product.

### 3.4 Continuum Hilbert space

The continuum inner-product defines a Hilbert space $L^2(\mathcal{M}, d\mu)$ of square-integrable wavefunctions:
$$\mathcal{H} = \{\Psi : \mathcal{M} \to \mathbb{C} \,|\, \int |\Psi|^2 d\mu < \infty\} .$$

Standard properties:
- Completeness under the $L^2$-norm.
- Separability (countable basis exists, e.g., via Hermite functions for harmonic-oscillator basis).
- Self-adjoint operator theory (position, momentum, Hamiltonian).

The substrate-level Hilbert space at continuum is therefore the standard $L^2(\mathcal{M})$ — exactly the standard QM arena.

### 3.5 Sesquilinearity preservation

The continuum inner-product is sesquilinear by direct verification:
- Conjugate-linear in first argument: $\langle \alpha\Psi, \Phi\rangle = \int (\alpha\Psi)^* \Phi \, d\mu = \alpha^* \int \Psi^*\Phi \, d\mu = \alpha^* \langle\Psi,\Phi\rangle$.
- Linear in second argument: $\langle \Psi, \alpha\Phi\rangle = \alpha \langle\Psi,\Phi\rangle$.
- Positive-definite: $\langle\Psi,\Psi\rangle = \int |\Psi|^2 d\mu \geq 0$.

The Tsirelson bound (Paper_U2_Discrete §3.4) carries over to the continuum: for bounded Hermitian operators, the CHSH-class operator norm is bounded by $2\sqrt{2}$.

### 3.6 Born-rule consistency

The Born rule (Paper_002) at continuum:
$$\text{Prob}(\text{configuration in region } R) = \int_R |\Psi(x)|^2 d\mu(x) .$$

This is the standard QM probability density. Inherits directly from the continuum inner-product structure derived here.

Normalization: $\int_{\mathcal{M}} |\Psi(x)|^2 d\mu(x) = 1$ for normalized states. The substrate-level participation budget per configuration is matched empirically.

### 3.7 Specific cases inherited

- **Non-relativistic QM** ($\mathcal{M} = \mathbb{R}^3$, $d\mu = d^3x$): $\langle\Psi,\Phi\rangle = \int \Psi^*\Phi \, d^3x$.
- **Relativistic QM on Lorentzian background** ($\mathcal{M} =$ spacetime, $d\mu = \sqrt{-g}\, d^4x$): Standard relativistic inner-product.
- **QM on curved spacetime** (Paper_014 V1 in curved acoustic background): $\mathcal{M}$ is the curved acoustic-metric manifold; $d\mu$ is the corresponding volume form.

Each case is a specialization of the general continuum inner-product to a specific configuration manifold.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 channel + locus indexing | P | Primitive. |
| 2 | P04 bandwidth | P | Primitive. |
| 3 | P09 $U(1)$ polarity | P | Primitive. |
| 3a | P-ScaleSeparation: $\ell_{ED} \ll R_{cg} \ll L_{flow}$ | P | Paper-local postulate; DCGT A→regime assumption. |
| 4 | Discrete sesquilinear inner-product | I | Paper_U2_Discrete. |
| 5 | DCGT coarse-graining | I | Paper_073. |
| 6 | $\sum_K \to \int_{\mathcal{M}} d\mu(x)$ continuum transition | D-via-I | Standard analysis under DCGT. |
| 7 | Continuum inner-product $\int \Psi^*\Phi \, d\mu$ | D | Direct extension. |
| 8 | $d\mu$ as gauge-invariant volume element | D-via-I | From P04 + standard geometry. |
| 9 | Gauge-invariance under $U(1)$ phase rotation | I | Routine algebraic verification (standard math). |
| 10 | $L^2(\mathcal{M}, d\mu)$ as continuum Hilbert space | I | Standard Hilbert-space theory. |
| 11 | Sesquilinearity preserved at continuum | I | Routine algebraic verification (standard math). |
| 12 | Tsirelson bound carries over | I | Paper_U2_Discrete §3.4 extended. |
| 13 | Born rule at continuum | I | Paper_002. |
| 14 | Specific configuration-manifold cases | I | Standard QM. |
| 15 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1: Substrate evidence that DCGT does NOT preserve sesquilinearity in the continuum limit.** Would refute step 11.

- **F2: Empirical detection of QM operations that violate continuum-inner-product gauge invariance.** Would refute step 9.

- **F3: Continuum-limit inner-product shown to be non-positive-definite.** Would refute step 7 and break Hilbert-space structure.

- **F4: $d\mu(x)$ shown to be non-gauge-invariant for any substrate-consistent gauge transformation.** Would refute the gauge-invariant measure claim.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper completes the U2-continuum step of the Phase-1 Schrödinger program: the sesquilinear inner-product over discrete motifs extends to the continuum $L^2(\mathcal{M}, d\mu)$ Hilbert space under DCGT coarse-graining.

**Relationship to other ED papers:**
- **Paper_U1, Paper_U2_Discrete:** supply the discrete-regime starting point.
- **Paper_073 (DCGT):** supplies the coarse-graining bridge.
- **Papers U3, U4, U5:** build on this continuum Hilbert space for Schrödinger evolution, Hamiltonian form, and momentum operator.

**Numerical content INHERITED.** Specific volume-element conventions for specific configuration manifolds. **Form FORCED.** Continuum sesquilinear inner-product on $L^2(\mathcal{M}, d\mu)$ with gauge-invariant measure.

**Future work.** Substrate-level audit of distributional inner-products (Dirac delta normalization, scattering-state continuum); substrate-level inner-product on curved acoustic-metric backgrounds (companion to Paper_014).

Verdict: **M3**.

---

**End Paper U2-Continuum.**
