# Paper 009 — Berry Phase as Holonomy of the Substrate Connection

**Series:** Wave-2 Generative Papers (QM-Kinematics Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087 canonical enumeration) + paper-specific postulates declared in §2.
**Companions:** Paper_008 (Phase Structure), Paper_010 (Aharonov–Bohm), Paper_015 (T17), Paper_016 (Polarity-connection match), Paper_089 (V1 kernel).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim to derive the numerical value of Berry-phase observables for specific Hamiltonians from substrate primitives; values are INHERITED from standard QM-instantiation matching.
2. It does **not** claim that Berry phase is a uniquely substrate-distinguishable observable; the operational predictions match standard QM.
3. It does **not** claim a complete theory of geometric phases (non-Abelian, off-diagonal, mixed-state extensions are not addressed).
4. It does **not** introduce new substrate primitives.
5. "Berry phase" here means: the holonomy acquired by a substrate-level polarity-transport around a closed loop in a parameter manifold $\mathcal{M}$ over which the rule-type carrier varies adiabatically.

---

## Abstract

Berry phase is FORM-FORCED in ED as the holonomy of the substrate polarity-transport connection (Paper_016) when the carrier rule-type is adiabatically transported around a closed loop in a parameter manifold. P05 (polarity-transport along edges) supplies the substrate-level connection; P06 (spatial dimension primitive D=3+1) supplies the manifold structure on which the loop is defined; Paper_016's polarity-connection match identifies the substrate connection with the standard Berry connection at leading-order coarse-graining. The numerical coefficient and Hamiltonian-specific value are INHERITED.

---

## §1 Introduction

Berry phase is the geometric phase $\gamma_C = \oint_C \mathcal{A}\cdot d\mathbf{R}$ acquired by an eigenstate transported adiabatically around a closed loop $C$ in parameter space, with $\mathcal{A}$ the Berry connection. This paper supplies the substrate-level origin: $\mathcal{A}$ is the coarse-grained polarity-transport connection of P05 (per Paper_087); the holonomy of this connection around $C$ is the Berry phase.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087 canonical enumeration)

- **P05 (Polarity-transport along edges)** — supplies substrate-level parallel transport of polarity along chain edges.
- **P06 (Spatial dimension D=3+1)** — supplies the manifold structure for parameter-space loops.
- **P09 (U(1)-valued polarity)** — supplies the $U(1)$ target of polarity-transport.
- **P10 (Rule-type primitive)** — supplies the rule-type carrier whose polarity is transported.

### 2.2 Upstream dependencies (inheritances)

- **I-016:** Polarity-connection match (Paper_016) — substrate polarity-transport coarse-grains to a gauge connection on rule-type bundles.
- **I-Phase:** Rule-type phase structure (Paper_008) — $S^1$-valued internal phase on rule-types.
- **I-Adiabatic:** Standard adiabatic-theorem machinery (standard math).
- **I-Holonomy:** Standard fiber-bundle holonomy theory (standard math).

### 2.3 Paper-specific postulates

- **P-Adiabatic-Coarse-Graining:** Adiabatic transport of the carrier rule-type across the parameter manifold corresponds, at leading-order coarse-graining, to slow variation of the substrate edge-set carrying the polarity.
- **P-Loop-Closure:** The parameter-space loop $C$ closes at the substrate level (initial and final rule-type configurations match), so holonomy is well-defined.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P05 supplies polarity-transport along edges | P | Primitive (Paper_087). |
| 2 | Rule-type phase structure ($S^1$) | I | Paper_008. |
| 3 | Substrate polarity-transport ↔ gauge connection | I | Paper_016 polarity-connection match. |
| 4 | Adiabatic coarse-graining identification | P-Adiabatic-Coarse-Graining | Postulate, declared. |
| 5 | Loop closure at substrate level | P-Loop-Closure | Postulate, declared. |
| 6 | Holonomy of connection around closed loop | I | Standard fiber-bundle theorem (I-Holonomy). |
| 7 | Adiabatic-theorem regime | A→regime | Slow-parameter regime. |
| 8 | Berry phase $\gamma_C = \oint_C \mathcal{A}\cdot d\mathbf{R}$ as the holonomy | D-via-I | Application of I-Holonomy to coarse-grained connection from I-016 + P-Adiabatic-Coarse-Graining. |
| 9 | Numerical value of $\gamma_C$ for specific Hamiltonian | I | Empirical/standard-QM matching. |
| 10 | Non-Abelian / off-diagonal generalizations | OPEN | Not claimed. |

---

## §3 The Derivation

### 3.1 Substrate connection from P05

P05 (per Paper_087) supplies polarity-transport along chain edges: each edge carries a transport rule that updates $U(1)$-valued polarity (P09) across the edge. The collection of such edge-rules, indexed over the substrate, defines a substrate-level connection $\omega_{\mathrm{sub}}$.

### 3.2 Coarse-graining to a smooth connection

By Paper_016, the substrate connection $\omega_{\mathrm{sub}}$ coarse-grains under DCGT (Paper_073) to a smooth $U(1)$-valued connection one-form $\mathcal{A}_\mu\, dx^\mu$ on the rule-type bundle (I-016).

### 3.3 Parameter-space loop and adiabatic transport

Let $C \subset \mathcal{M}$ be a closed loop in a parameter manifold $\mathcal{M}$ (e.g., external-field configuration space). Adiabatic transport of the carrier rule-type along $C$ corresponds, by P-Adiabatic-Coarse-Graining, to slow variation of the substrate edge-set; the coarse-grained connection pulls back to $C$ as $\mathcal{A}|_C$.

By P-Loop-Closure, the initial and final substrate configurations match, so holonomy is well-defined.

### 3.4 Holonomy and Berry phase

Standard fiber-bundle holonomy theory (I-Holonomy) gives the holonomy of $\mathcal{A}$ around $C$ as
$$U_C = \exp\!\left(i \oint_C \mathcal{A}\cdot d\mathbf{R}\right) .$$

Acting on a $U(1)$-valued polarity, this multiplies the polarity by the phase
$$\gamma_C = \oint_C \mathcal{A}\cdot d\mathbf{R} .$$

This is the Berry phase. The FORM is FORCED by the connection structure (I-016) + holonomy (I-Holonomy); the numerical VALUE for any specific Hamiltonian is INHERITED via standard QM matching.

---

## §4 What the Derivation Supplies and Does Not Supply

**Supplies:** Substrate origin of the Berry connection $\mathcal{A}$ as the coarse-grained P05 polarity-transport. Substrate audit of holonomy as the geometric (path-dependent) phase.

**Does not supply:** Numerical $\gamma_C$ for specific Hamiltonians (INHERITED). Non-Abelian or off-diagonal Berry phase (OPEN). Mixed-state / open-system geometric phases (OPEN).

---

## §5 Open Structural Questions

- **O-Berry-1:** Non-Abelian Berry-Wilczek-Zee phase via T17 non-Abelian rule-type bundles.
- **O-Berry-2:** Off-diagonal Berry phase (Manini-Pistolesi).
- **O-Berry-3:** Mixed-state geometric phase (Uhlmann) via V5-modulated open-system dynamics.
- **O-Berry-4:** Substrate-level derivation of P-Adiabatic-Coarse-Graining from a quantitative slow-parameter scaling.

---

## §6 Falsification Criteria

- **F1:** Demonstration that the coarse-grained P05 polarity-transport does NOT match the standard Berry connection at leading order — refutes I-016 application.
- **F2:** Empirical detection of a geometric phase that violates standard fiber-bundle holonomy structure — would falsify the audit.
- **F3:** Adiabatic transport that violates P-Loop-Closure (initial/final substrate states mismatched) producing a well-defined Berry phase — refutes P-Loop-Closure's necessity.
- **F4:** Numerical mismatch between substrate-coarse-grained $\mathcal{A}$ and standard Berry connection in any tested system — refutes the identification.

---

## §7 Position Statement

Berry phase is **FORM-FORCED** in ED as the holonomy of the coarse-grained substrate polarity-transport connection. P05 supplies the substrate connection; Paper_016 supplies the identification with the standard Berry connection; standard fiber-bundle holonomy delivers the phase. Numerical content is **INHERITED**.

The result composes with Paper_008 (rule-type phase), Paper_010 (Aharonov–Bohm — a special case where the loop encloses flux), and Paper_015 (T17 — non-Abelian extension is the natural generalization).

---

**End Paper 009 (FIXED).**
