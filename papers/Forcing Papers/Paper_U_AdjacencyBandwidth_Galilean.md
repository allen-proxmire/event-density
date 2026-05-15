# Paper U-AdjacencyBandwidth — Adjacency-Bandwidth Asymmetry from Spatial Homogeneity

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, methodological complement to U4)
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_U4 (Hamiltonian form $\hat T = \hat p^2/(2m)$), Paper_U5 (momentum operator), Paper_RQM_T5 (KG), Paper_017 (Lorentz covariantization).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the adjacency-bandwidth boost-asymmetry from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** deliver the Galilean / Bargmann cohomology computation — that derivation is OPEN. The paper is restricted to the adjacency-bandwidth boost-asymmetry observation from P03 spatial homogeneity.
5. Bandwidth-asymmetry observation FORCED by P03 spatial homogeneity (adjacency invariant; propagation transforming); Galilean boost structure is **not** derived (P03 is necessary, not sufficient). Numerical $m$ values INHERITED.

---

## Abstract

This paper records the substrate-level adjacency-bandwidth partition: under Galilean boost, P03 spatial-homogeneity forces adjacency content (position-locus) to be boost-invariant while P04 propagation content (translation-rate) transforms. The resulting Jacobian asymmetry underlies the factor-of-2 in the non-relativistic kinetic form $\hat T = \hat p^2/(2m)$ (consistent with Paper_U4's Taylor-expansion derivation). The structural decomposition is FORM-FORCED by P03 + P04; the full Galilean / Bargmann cohomology computation is OPEN. Verdict: **M3 as-is** (retitled scope; Bargmann OPEN) per Paper_095's three-tier verdict grammar. Key falsifier **F1**: empirical non-relativistic kinetic energy with factor different from $1/(2m)$.

---

## §1 Statement of Result

**Scope clarification.** Earlier drafts framed this paper around the Galilean / Bargmann central extension. The current content does NOT deliver the Bargmann cohomology computation; the paper is restricted to the adjacency-bandwidth boost-asymmetry observation from P03 spatial homogeneity. A full Galilean / Bargmann substrate-cohomology derivation is **OPEN** (deferred to a future paper). The paper records the observed bandwidth-asymmetry component only.

**Claim.** The substrate-level adjacency-bandwidth partition — separating P03 adjacency content (position-locus structure) from P04 propagation content (translation-rate structure) — produces, under DCGT coarse-graining to the non-relativistic regime, the standard quadratic kinetic-energy form:
$$\hat T = \frac{\hat p^2}{2m} .$$

The factor-of-2 arises from the **Galilean Jacobian** of the partition: under a Galilean boost $v \to v + u$, the adjacency content is invariant (P03 spatial homogeneity), while the propagation content transforms with Jacobian $\partial(p^2)/\partial p = 2p$, producing the factor $1/(2m)$.

FORM-FORCED by P03 + P04 + Galilean-Jacobian + DCGT. Factor-of-2 is a **structural consequence** of the substrate partition. Numerical $m$ and specific $\hat T$ per system are INHERITED.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies the adjacency (position-locus) sector of the partition.
- **P04 (Bandwidth)** — supplies the propagation (translation-rate) sector.
- **P10 (Rule-type primitive)** — supplies rule-type carriers.

### 2.2 Upstream Dependencies

- **I-U4:** Hamiltonian form $\hat T = \hat p^2/(2m)$ derived from Galilean-Jacobian of relativistic dispersion.
- **I-U5:** Momentum operator.
- **I-RQM-T5:** Klein–Gordon equation (relativistic source).
- **I-017:** Substrate Lorentz covariantization → acoustic metric.
- **I-073:** DCGT coarse-graining.
- **I-Galilean:** Standard Galilean-group transformation theory.

---

## §3 Derivation

### 3.1 Adjacency-bandwidth partition

At substrate level, the measurement content of substrate cells separates into:

**Adjacency content (P03):** The content distinguishing substrate cells by their **locus indexing** — which channel + locus a cell belongs to. This is the "where" content; it provides position-information.

**Propagation content (P04):** The content distinguishing substrate cells by their **translation-rate** — how quickly polarity propagates across the cell. This is the "how-fast" content; it provides momentum-information.

The two sectors are **orthogonal** in the substrate Hilbert space: an operator measuring adjacency content (position $\hat x$) and an operator measuring propagation content (momentum $\hat p$) act on different aspects of substrate cells.

This is the substrate-level basis for the canonical commutation $[\hat x, \hat p] = i\hbar$ (Paper_RQM_T8).

### 3.2 Boost-asymmetry from P03 spatial homogeneity

**Note on symmetry distinction.** P03 spatial homogeneity ≠ Galilean boost invariance. P03 is invariance under spatial translation; Galilean boost invariance is a distinct symmetry. The paper observes the bandwidth-asymmetry consequence of P03 (adjacency content boost-invariant, propagation content boost-transforming), which is **necessary but not sufficient** for full Galilean boost structure. The full Galilean / Bargmann substrate cohomology is OPEN.


Under a Galilean boost $v \to v + u$ (substrate-level low-velocity transformation):

- **Adjacency content is invariant.** P03 spatial homogeneity (substrate is translation-invariant; positions and translations of positions are equivalent) implies that the **identity** of each substrate cell is unchanged by the boost. Substrate cells are at different spatial positions in the boosted frame, but their **intrinsic adjacency** content is preserved.

- **Propagation content transforms.** P04 propagation content shifts: a cell that was propagating at rate $v$ in the original frame propagates at rate $v + u$ in the boosted frame. The propagation-rate is **frame-dependent**.

This asymmetry between adjacency (invariant) and propagation (transforming) is the substrate-level Galilean-Jacobian content.

### 3.3 The kinetic-energy partition

The substrate-level kinetic energy is the energy content carried by **propagation** (P04) — the rate at which substrate cells exchange polarity content under translation.

For non-relativistic dispersion (Paper_RQM_T5 NR limit, Paper_U4):
$$E_{\mathrm{kin}} = \frac{p^2}{2m} .$$

The substrate-level interpretation:
- $p$ is the propagation-rate eigenvalue (momentum, from P04 propagation content).
- $m$ is the substrate-bandwidth content per cell at rest (Paper_RQM_ArcM_H1 mass structural form).
- $p^2$ is the squared propagation rate.
- $/(2m)$ is the **Galilean Jacobian factor**.

### 3.4 Substrate origin of the factor-of-2

The Galilean Jacobian under boost $v \to v + u$ of the kinetic-energy partition:
$$\frac{\partial E_{\mathrm{kin}}}{\partial p^2}\bigg|_{m} = \frac{1}{2m} .$$

This is the **rate of energy change per unit squared-momentum change** at fixed mass. The factor $1/2$ arises because $p = mv$ and $E_{\mathrm{kin}} = \tfrac{1}{2} mv^2 = p^2/(2m)$: the relationship between energy and momentum is quadratic, producing the factor $1/2$ via the antiderivative $\int v \, dp = vp/2$.

At substrate level, this Jacobian content is **structurally determined** by:
1. P03 adjacency invariance under boost (the position-content does not shift kinetically).
2. P04 propagation transforming under boost (momentum content shifts linearly with $u$).
3. The substrate-level dispersion relation $E^2 = p^2c^2 + m^2c^4$ (Paper_RQM_T5) expanded to leading order in $p/(mc)$.

The factor of 2 is therefore the substrate-level structural content of "kinetic energy is quadratic in momentum at low velocity" — it is not an arbitrary normalization.

### 3.5 Connection to Paper_U4

Paper_U4 derived the factor-of-2 via the Taylor expansion of the relativistic dispersion:
$$\sqrt{1 + (p/mc)^2} \approx 1 + \tfrac{1}{2}(p/mc)^2 .$$

This paper supplies the **substrate-structural** account of the same factor: the $\tfrac{1}{2}$ in the Taylor expansion is the Galilean-Jacobian content of the adjacency-bandwidth partition, where adjacency is boost-invariant and propagation transforms.

Both accounts (Taylor expansion + substrate partition) are consistent. The Taylor expansion is the calculation; the substrate partition is the structural reason.

### 3.6 Why the factor is exactly $\tfrac{1}{2}$

The factor of $\tfrac{1}{2}$ is forced by:
- **Quadratic dispersion** $E \propto p^2$ at low velocity (substrate dispersion + non-relativistic limit).
- **Linear momentum transformation** under Galilean boost ($p \to p + mu$).
- **Antiderivative integration** $\int v\, dp = \tfrac{1}{2} v p$ (calculus).

All three are FORM-FORCED at substrate level. The combination produces exactly $\tfrac{1}{2}$, not any other coefficient.

### 3.7 Numerical content

- $m$: VALUE-INHERITED (Paper_RQM_ArcM_H1 + empirical mass values).
- Factor $1/(2m)$ in $\hat T$: FORM-FORCED.
- Specific $\hat T$ for specific systems: INHERITED.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 spatial homogeneity (adjacency) | P | Primitive. |
| 2 | P04 bandwidth (propagation) | P | Primitive. |
| 3 | P10 rule-type | P | Primitive. |
| 4 | Adjacency content invariant under Galilean boost | D-via-I | From P03. |
| 5 | Propagation content transforms under Galilean boost | D-via-I | From P04 + Galilean group. |
| 6 | Galilean Jacobian asymmetry | D | Composition of steps 4–5. |
| 7 | $E^2 = p^2c^2 + m^2c^4$ relativistic dispersion | I | Paper_RQM_T5. |
| 8 | Taylor expansion at low velocity → $E_{\mathrm{kin}} = p^2/(2m)$ | I | Paper_U4. |
| 9 | Factor $1/2$ from Jacobian + antiderivative | D | Calculus. |
| 10 | $\hat T = \hat p^2/(2m)$ operator form | D-via-I | Composition with Paper_U5. |
| 11 | Substrate origin of factor structurally identified | D | Composition. |
| 12 | $m$ values per system | I | Empirical. |
| 13 | Substrate Galilean / Bargmann cohomology derivation | OPEN | Not delivered in this paper; deferred. |
| 14 | Verdict M3 (restricted to observed bandwidth-asymmetry component) | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Empirical detection of non-relativistic kinetic energy with factor different from $1/(2m)$ — refutes the substrate partition structural account.
- **F2:** Substrate evidence that adjacency content transforms under Galilean boost — refutes step 4.
- **F3:** Substrate evidence that propagation content does NOT transform under boost — refutes step 5.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the **substrate-structural** complement to Paper_U4's Taylor-expansion derivation of the factor-of-2 in $\hat T = \hat p^2/(2m)$. The two papers are consistent; this one identifies the substrate-level partition (adjacency vs propagation) underlying the factor.

**Relationship to other ED papers:**
- **Paper_U4:** companion (Taylor-expansion derivation).
- **Paper_U5:** supplies the $\hat p$ operator.
- **Paper_RQM_T5:** supplies the relativistic dispersion.
- **Paper_RQM_T8:** canonical commutation $[\hat x, \hat p] = i\hbar$ is the substrate-level statement of adjacency-propagation orthogonality.

**Numerical content INHERITED.** Mass $m$ values. **Form FORCED.** Adjacency-bandwidth partition fixing the Galilean kinetic structure.

Verdict: **M3**.

---

**End Paper U-AdjacencyBandwidth.**
