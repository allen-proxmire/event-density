# Paper 079 — P4-NN: Krieger–Dougherty + Maxwell Viscoelastic

**Series:** Wave-2 Generative Papers (Soft-Matter Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_074 (V5 viscoelastic Maxwell ansatz), Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of numerical Krieger–Dougherty exponent (often $\approx 2$) or maximum-packing fraction from first principles; these are INHERITED via empirical matching.
2. It does **not** claim a complete theory of non-Newtonian rheology; the substrate audit covers Krieger–Dougherty viscosity divergence + Maxwell viscoelastic relaxation only.
3. It does **not** introduce new substrate primitives.
4. "P4-NN" = the non-Newtonian sector of the soft-matter arc inheriting from P04 bandwidth-additive structure.

---

## Abstract

Non-Newtonian rheology — viscosity divergence under packing-fraction increase (Krieger–Dougherty) + viscoelastic stress relaxation (Maxwell) — is FORM-FORCED in ED by P04 (Bandwidth) + V5 (cross-chain correlation kernel, Paper_090). P04 supplies the bandwidth-budget structure that saturates as packing-fraction approaches a maximum; the divergence form follows. V5 supplies the finite-memory cross-chain correlation that produces Maxwell viscoelastic relaxation $\sigma(t) = \int G(t - t')\,\dot{\gamma}(t')\,dt'$ with relaxation time $\tau_M \sim \tau_{V5}$. Structural form FORCED; numerical exponents / relaxation times INHERITED.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)**, **P04 (Bandwidth)**, **P10 (Rule-type primitive)** [V5], **P11 (Commitment-irreversibility)**.

### 2.2 Upstream dependencies

- **I-074:** V5 viscoelastic Maxwell ansatz substrate-grounded (Paper_074).
- **I-089:** V1 kernel (Paper_089).
- **I-090:** V5 kernel with finite memory $\tau_{V5}$ (Paper_090).
- **I-076:** NS-2 substrate→continuum (Paper_076).
- **I-KD:** Standard Krieger–Dougherty machinery (standard rheology).
- **I-Maxwell:** Standard Maxwell viscoelastic model (standard rheology).

### 2.3 Paper-specific postulates

- **P-Packing-Budget-Saturation:** As packing fraction $\phi$ approaches a substrate-level maximum $\phi_{\max}$, the P04 bandwidth budget per substrate cell saturates; effective viscosity diverges in the form $\eta(\phi) = \eta_0 (1 - \phi/\phi_{\max})^{-n}$ for some exponent $n$.
- **P-V5-Maxwell-Identification:** The V5 finite-memory kernel directly produces a Maxwell-form stress-relaxation response with $\tau_M \sim \tau_{V5}$.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04 bandwidth-additive | P | Primitive. |
| 2 | V5 finite memory | I | Paper_090. |
| 3 | Packing-saturation viscosity divergence form | P-Packing-Budget-Saturation | Postulate. |
| 4 | Krieger–Dougherty form $(1-\phi/\phi_{\max})^{-n}$ | I | Standard rheology + matching. |
| 5 | Maxwell viscoelastic stress integral | I | Paper_074 + standard math. |
| 6 | $\tau_M \sim \tau_{V5}$ identification | P-V5-Maxwell-Identification | Postulate. |
| 7 | Numerical $n$, $\phi_{\max}$, $\tau_M$ | I | Empirical. |

---

## §3 The Rheology

### 3.1 Krieger–Dougherty divergence

Under increasing packing $\phi$, the P04 bandwidth budget per substrate cell saturates: more matter occupies fewer admissible substrate configurations. By P-Packing-Budget-Saturation, the effective viscosity diverges as
$$\eta(\phi) = \eta_0 (1 - \phi/\phi_{\max})^{-n} ,$$
matching standard Krieger–Dougherty form (I-KD). The structural divergence is FORCED; the numerical exponent $n$ and packing limit $\phi_{\max}$ are INHERITED.

### 3.2 Maxwell viscoelastic relaxation

V5's finite memory $\tau_{V5}$ (Paper_090) supplies the substrate-level relaxation timescale. By P-V5-Maxwell-Identification + Paper_074, the stress response is
$$\sigma(t) = \int_{-\infty}^t G_0 e^{-(t-t')/\tau_M}\,\dot{\gamma}(t')\,dt' ,$$
with $\tau_M \sim \tau_{V5}$ at leading order.

Standard Maxwell viscoelastic model (I-Maxwell) applies; substrate program supplies the **origin** of $\tau_M$ from V5 kernel data.

### 3.3 Combined rheology

For systems with both effects (e.g., concentrated colloidal suspensions), the composite rheology combines Krieger–Dougherty divergence + Maxwell viscoelastic relaxation in a single substrate-derived framework.

---

## §4 Falsification Criteria

- **F1:** Empirical detection of viscosity divergence form different from $(1-\phi/\phi_{\max})^{-n}$ near packing limit — refutes P-Packing-Budget-Saturation.
- **F2:** Empirical detection of stress-relaxation form not Maxwell-class under V5-dominated regime — refutes P-V5-Maxwell-Identification.
- **F3:** Substrate evidence that P04 bandwidth-budget does NOT saturate near $\phi_{\max}$ — refutes the divergence mechanism.

---

## §5 Position Statement

Non-Newtonian rheology (Krieger–Dougherty + Maxwell viscoelastic) is **FORM-FORCED** in ED by P04 + V5 under P-Packing-Budget-Saturation + P-V5-Maxwell-Identification. Numerical content INHERITED.

---

**End Paper 079 (FIXED).**
