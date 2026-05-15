# Paper 085 — Universal Mobility Law (Empirical Anchor)

**Series:** Wave-2 Generative Papers (Soft-Matter Arc, Empirical Anchor)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_074 (V5 viscoelastic Maxwell), Paper_079 (P4-NN rheology), Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of numerical mobility-law coefficients from first principles; the empirical anchor provides matching, not derivation.
2. It does **not** claim that the Universal Mobility Law is operationally universal across all material classes; it is **structurally** universal under the substrate-derived dissipation pattern.
3. It does **not** introduce new substrate primitives.
4. "Universal Mobility Law" = the empirical-matching anchor identified in the soft-matter arc (per `project_ed_framework.md`) connecting particle / molecular mobility to substrate-derived friction structure.
5. "Empirical anchor" = a published / measurable relation that serves as the substrate-level matching point for the soft-matter arc.

---

## Abstract

The Universal Mobility Law is structurally connected in ED to: (i) V1 finite-second-moment supplying friction coefficient $\zeta \sim m/\tau_{V1}$ (Paper_089); (ii) V5 finite-memory supplying viscoelastic relaxation $\tau_M \sim \tau_{V5}$ (Paper_074 + Paper_090); (iii) P4-NN rheology supplying concentration-dependent corrections (Paper_079). At dilute limit, mobility $\mu = 1/\zeta$ follows from the Einstein–Smoluchowski form. Substrate program supplies the **structural origin** of the friction-mobility relation from V1 + V5 + P04 substrate content; numerical coefficients are INHERITED via empirical matching at the canonical operating point.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)**, **P04 (Bandwidth)**, **P10 (Rule-type primitive)** [V1, V5], **P11 (Commitment-irreversibility)**.

### 2.2 Upstream dependencies

- **I-074:** V5 viscoelastic Maxwell ansatz (Paper_074).
- **I-079:** P4-NN rheology (Paper_079).
- **I-089:** V1 finite second moment (Paper_089).
- **I-090:** V5 finite memory (Paper_090).
- **I-Einstein:** Einstein–Smoluchowski mobility-friction relation (standard statistical mechanics).

### 2.3 Paper-specific postulates

- **P-Mobility-V1-Friction:** The substrate-level friction coefficient $\zeta \sim m/\tau_{V1}$ inherits from V1 finite second moment at dilute limit.
- **P-Mobility-Maxwell-Correction:** At finite frequency, the effective mobility acquires a Maxwell-viscoelastic correction from V5 finite memory.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 finite second moment | I | Paper_089. |
| 2 | V5 finite memory | I | Paper_090. |
| 3 | P4-NN concentration-dependent rheology | I | Paper_079. |
| 4 | Friction $\zeta \sim m/\tau_{V1}$ | P-Mobility-V1-Friction | Postulate. |
| 5 | Einstein–Smoluchowski $\mu = 1/\zeta$ at dilute | I | Standard math. |
| 6 | Maxwell viscoelastic correction at finite frequency | P-Mobility-Maxwell-Correction | Postulate. |
| 7 | Concentration-dependent Krieger–Dougherty mobility decrease | I | Paper_079. |
| 8 | Specific numerical coefficients | I | Empirical matching. |

---

## §3 The Mobility Law

### 3.1 Dilute limit friction

By P-Mobility-V1-Friction, friction coefficient at dilute limit is $\zeta \sim m/\tau_{V1}$ — V1 finite second moment supplies the timescale, and substrate participation supplies the mass-content content.

Einstein–Smoluchowski (I-Einstein): $\mu = 1/\zeta$, $D = k_B T \mu$.

### 3.2 Finite-frequency Maxwell correction

At finite frequency, V5 finite-memory (Paper_090) supplies viscoelastic relaxation. By P-Mobility-Maxwell-Correction, the effective mobility acquires
$$\mu(\omega) = \mu_0 / (1 + i \omega \tau_M) ,$$
with $\tau_M \sim \tau_{V5}$.

### 3.3 Concentrated regime

At finite concentration / packing fraction, Krieger–Dougherty divergence (Paper_079) modifies the effective friction:
$$\zeta_{\mathrm{eff}}(\phi) = \zeta_0 (1 - \phi/\phi_{\max})^{-n} ,$$
inducing concomitant mobility decrease.

### 3.4 Universal Mobility Law

Composing §3.1–§3.3, the Universal Mobility Law in ED's framing is:
$$\mu(\omega, \phi) = \mu_0(\phi) / (1 + i\omega\tau_M) \,\mathrm{with}\, \mu_0(\phi) = \mu_0^{(0)} (1 - \phi/\phi_{\max})^{n} .$$

Numerical $\mu_0^{(0)}$, $\tau_M$, $n$, $\phi_{\max}$ inherited via empirical matching at the canonical operating point.

---

## §4 Falsification Criteria

- **F1:** Empirical detection of mobility-friction relation NOT of Einstein–Smoluchowski form at dilute limit — refutes the substrate framework.
- **F2:** Empirical detection of finite-frequency mobility NOT Maxwell-corrected — refutes P-Mobility-Maxwell-Correction.
- **F3:** Concentration-dependent mobility behavior inconsistent with Krieger–Dougherty divergence — refutes Paper_079 inheritance.

---

## §5 Position Statement

The Universal Mobility Law is **structurally connected** to V1 friction (P-Mobility-V1-Friction) + V5 Maxwell correction (P-Mobility-Maxwell-Correction) + Krieger–Dougherty concentration dependence (Paper_079). Form FORCED; numerical content INHERITED.

---

**End Paper 085 (FIXED).**
