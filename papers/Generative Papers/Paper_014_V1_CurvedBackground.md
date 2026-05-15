# Paper 014 — V1 in a Curved Acoustic Background (N1 / GR1)

**Series:** Wave-2 Generative Papers (QFT Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_013 (V1 QFT-arc form), Paper_089 (V1 canonical reference), Paper_073 (DCGT), Paper_039 (horizon as decoupling surface).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that the curved-background V1 propagation derives the Einstein equation; the "curved acoustic background" is a coarse-grained kinematic frame inherited from Paper_017 / ED-Phys-10, not GR's dynamical metric.
2. It does **not** claim novel curved-spacetime QFT predictions beyond what standard quantum-field-in-curved-spacetime (QFCS) reproduces.
3. It does **not** claim that V1 propagation in a curved background is the substrate-level theory of gravity; substrate gravity is addressed in arc SG (Papers_027–038).
4. It does **not** introduce new substrate primitives.
5. "Curved acoustic background" = the acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ obtained from substrate-level coarse-graining per Paper_017 / ED-Phys-10; **not** the GR metric.
6. "N1 / GR1" refers to the V1-finite-width-in-curved-spacetime theorems N1 (substrate-level finite-width preservation) and GR1 (curved-acoustic-metric Wightman-function audit), inherited from the foundational-theorem inventory.

---

## Abstract

The V1 finite-width retarded vacuum kernel extends to a curved acoustic background via DCGT coarse-graining (Paper_073) of the substrate kernel onto a slowly-varying acoustic metric (Paper_017 / ED-Phys-10). Theorems N1 (finite-width preservation under curved-background propagation) and GR1 (Wightman two-point function on curved acoustic metric satisfies tempered-distribution + spectral structure analogous to Paper_013) follow as conditional derivations under the slow-variation regime and acoustic-metric-coarse-graining inheritance. The result feeds Paper_039 (horizon as decoupling surface) and Paper_047 (Hawking spectrum via substrate-Unruh).

---

## §1 Introduction

The acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ emerges in ED as a coarse-grained kinematic frame (Paper_017 / ED-Phys-10). V1 propagation in this curved background supplies the substrate-level analog of QFT-in-curved-spacetime (QFCS). Theorems N1 and GR1 audit that V1 retains its finite-width + spectral structure when the background is slowly varying.

This paper supplies the substrate audit of N1 and GR1, with explicit declared postulates marking the slow-variation regime.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — width scale $\ell_{V1}$.
- **P10 (Rule-type primitive)** — V1 kernel rule-type.
- **P11 (Commitment-irreversibility)** — retardation.
- **P13 (Time homogeneity)** — locally on slow-variation patches.

### 2.2 Upstream dependencies

- **I-013:** V1 QFT-arc form (Paper_013) — flat-background presentation.
- **I-089:** V1 canonical reference (Paper_089).
- **I-073:** DCGT (Paper_073) — substrate→continuum bridge.
- **I-017:** Substrate→continuum Lorentz covariantization producing acoustic metric (Paper_017 / ED-Phys-10).
- **I-039:** Horizon as decoupling surface (Paper_039) — downstream consumer of curved-background V1.
- **I-QFCS:** Standard QFT-in-curved-spacetime machinery (standard math).
- **I-HK:** Standard Hadamard-state machinery / point-splitting renormalization (standard math).

### 2.3 Paper-specific postulates

- **P-Slow-Variation:** The acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ varies slowly on the V1 width scale: $\ell_{V1} |\partial g^{\mathrm{ac}}| / |g^{\mathrm{ac}}| \ll 1$.
- **P-Hadamard-Preservation:** The substrate vacuum state's two-point function in the curved acoustic background satisfies the Hadamard short-distance condition (singular structure matches Paper_013's flat-background two-point function at coincidence).

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 flat-background two-point function | I | Paper_013. |
| 2 | Acoustic metric from substrate coarse-graining | I | Paper_017 / ED-Phys-10. |
| 3 | DCGT coarse-graining bridge | I | Paper_073. |
| 4 | Slow-variation regime $\ell_{V1}|\partial g| \ll |g|$ | P-Slow-Variation | Regime postulate. |
| 5 | Hadamard short-distance preservation | P-Hadamard-Preservation | Postulate. |
| 6 | V1 finite-width preservation (N1) | D-via-I | Application of I-073 + P-Slow-Variation to I-013. |
| 7 | Curved-background two-point function (GR1) | D-via-I | Application of I-QFCS + I-HK to V1 with P-Hadamard-Preservation. |
| 8 | Tempered-distribution character preserved | I | Standard QFCS + I-Tempered. |
| 9 | Spectral content (locally Källén-Lehmann-like) | D-via-I | Local-frame application of Paper_013 P-V1-Spectral. |
| 10 | Numerical curvature corrections | I | Standard QFCS perturbation. |
| 11 | Backreaction on $g^{\mathrm{ac}}$ | OPEN | Not claimed (would be substrate-gravity arc content). |

---

## §3 The Derivation

### 3.1 Setup

The substrate produces an acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ via coarse-graining (I-017 / ED-Phys-10). The V1 kernel, originally defined on the substrate edge-set (Paper_089), propagates rule-type-carrier amplitudes on this background.

By P-Slow-Variation, the metric varies slowly on the V1 width scale: locally on patches of size $\ell \sim \ell_{V1}$, the metric is approximately Minkowski.

### 3.2 N1: Finite-width preservation

DCGT (I-073) coarse-grains the substrate kernel onto the smooth manifold equipped with $g^{\mathrm{ac}}$. By P-Slow-Variation, the V1 second moment $\ell_{V1}^2$ is preserved at leading order (variations in $g$ produce $O(\ell_{V1}|\partial g|)$ corrections, suppressed by P-Slow-Variation).

**Theorem N1 (substrate-level):** V1's finite-width property survives DCGT coarse-graining onto a slowly-varying acoustic metric.

This is **D-via-I**: application of standard slow-variation perturbation theory (I) to the V1 kernel + DCGT (I) under P-Slow-Variation (P).

### 3.3 GR1: Curved-background two-point function

The two-point function $W_{V1}(x, y; g^{\mathrm{ac}})$ on curved background is constructed via standard QFCS machinery (I-QFCS). By P-Hadamard-Preservation, its short-distance singular structure matches the flat-background Paper_013 form.

**Theorem GR1 (substrate-level):** $W_{V1}(x, y; g^{\mathrm{ac}})$ is a tempered distribution; its short-distance Hadamard structure is preserved; its locally-Källén-Lehmann spectral content matches Paper_013 on slow-variation patches.

This is **D-via-I**: application of I-QFCS + I-HK to V1 under P-Hadamard-Preservation.

### 3.4 Downstream propagation

N1 + GR1 supply the curved-background V1 needed by:
- Paper_039 (horizon as decoupling surface) — V1 retardation on horizon-crossing trajectories.
- Paper_047 (Hawking spectrum via substrate-Unruh) — KMS condition in curved acoustic metric.
- Paper_017 (Lorentz covariantization) — consistency check.

---

## §4 What This Paper Supplies and Does Not Supply

**Supplies:** Substrate audit of V1 propagation in curved acoustic background. N1 + GR1 as conditional derivations under slow-variation regime.

**Does not supply:** Backreaction (V1 affecting $g^{\mathrm{ac}}$). Substrate-level Einstein equation (Phase-3 SPECULATIVE). Fast-variation regime (near singularities, deep horizons) — would require additional postulates.

---

## §5 Open Structural Questions

- **O-N1-1:** Quantitative derivation of P-Hadamard-Preservation from substrate kernel data.
- **O-N1-2:** Fast-variation regime where P-Slow-Variation fails.
- **O-N1-3:** Backreaction (would feed Phase-3 GR emergence).
- **O-GR1-1:** Substrate audit of QFCS Unruh effect — partially in Paper_047 / Arc Hawking.

---

## §6 Falsification Criteria

- **F1:** Demonstration that V1's finite second moment fails under curved-background coarse-graining at leading order — refutes N1.
- **F2:** Demonstration that the curved-background two-point function violates Hadamard structure — refutes P-Hadamard-Preservation.
- **F3:** Detection of a regime where $\ell_{V1}|\partial g| \sim |g|$ produces predictions inconsistent with substrate-level audit — would flag P-Slow-Variation's limits.

---

## §7 Position Statement

V1's curved-background presentation (N1 + GR1) is **FORM-FORCED** in ED under P-Slow-Variation + P-Hadamard-Preservation. Standard QFCS machinery (I) supplies the curved-background two-point-function structure; the substrate adaptation under V1 + DCGT is the new content (D-via-I). Numerical curvature corrections INHERITED from standard QFCS.

This supplies the curved-background V1 consumed by Papers_017, 039, 047.

---

**End Paper 014 (FIXED).**
