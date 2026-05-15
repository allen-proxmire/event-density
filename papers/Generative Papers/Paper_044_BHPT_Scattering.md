# Paper 044 — BHPT Scattering Structure

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_039 (horizon as decoupling surface), Paper_045 (helicity at horizons), Paper_046 (Kerr twist), Paper_047 (Hawking spectrum).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of specific BHPT cross-sections / phase shifts for concrete black-hole spacetimes; numerical content is INHERITED via standard BHPT calculations.
2. It does **not** claim that the substrate-level BHPT is equivalent to standard BHPT in all regimes; near-horizon trans-Planckian regimes differ via Paper_040 / Paper_042.
3. It does **not** introduce new substrate primitives.
4. "BHPT" = Black-Hole Perturbation Theory: linearized perturbations on a black-hole background (Schwarzschild, Kerr), producing scattering phase shifts, quasi-normal modes, and gray-body factors.
5. "BHPT scattering structure" = the substrate audit of: (i) incoming/outgoing mode decomposition; (ii) potential scattering off the curvature; (iii) gray-body / transmission factor from horizon to infinity.

---

## Abstract

BHPT scattering structure (Regge-Wheeler / Teukolsky equations + transmission/reflection coefficients) is FORM-FORCED in ED as the substrate-level perturbation theory of V1-modulated field propagation on the curved acoustic background (Paper_014) with decoupling-surface boundary condition at the horizon (Paper_039). The substrate audit composes: (i) V1 propagation on $g^{\mathrm{ac}}$ with N1/GR1 (Paper_014); (ii) decoupling-surface condition supplying ingoing-only boundary at the horizon (Paper_039); (iii) standard partial-wave decomposition + WKB scattering analysis (standard math). The structural form of BHPT (Regge-Wheeler potential, frequency-dependent transmission coefficient) is FORCED; specific phase shifts and gray-body factors are INHERITED via standard BHPT calculations.

---

## §1 Introduction

BHPT supplies the linearized theory of perturbations on black-hole backgrounds. Standard derivations (Regge-Wheeler 1957, Teukolsky 1973) decompose perturbations into partial waves and produce scattering equations with a potential barrier between horizon and infinity.

This paper supplies the substrate audit: BHPT on the acoustic-metric background is the substrate-level theory of V1-mode propagation under decoupling-surface boundary conditions. Structural form FORCED; numerical content INHERITED.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — substrate-level mode content.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck cutoff.
- **P10 (Rule-type primitive)** — supplies V1 / V5.
- **P11 (Commitment-irreversibility)** — retardation.

### 2.2 Upstream dependencies

- **I-014:** V1 in curved acoustic background (Paper_014).
- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-047:** Hawking spectrum substrate-Unruh (Paper_047).
- **I-Acoustic:** ED-Phys-10 acoustic-metric guardrails (Paper_035).
- **I-BHPT:** Standard BHPT machinery (Regge-Wheeler, Teukolsky equations, standard math).
- **I-WKB:** Standard WKB scattering / matching machinery (standard math).

### 2.3 Paper-specific postulates

- **P-Horizon-Ingoing-Only:** At the substrate-level decoupling surface (horizon), the boundary condition for BHPT modes is ingoing-only (consistent with Paper_039 horizon-as-decoupling).
- **P-Asymptotic-Outgoing:** At spatial infinity, BHPT modes are asymptotically outgoing / plane-wave.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 propagation on curved acoustic background | I | Paper_014. |
| 2 | Acoustic-metric guardrails active | I | Paper_035. |
| 3 | Horizon = decoupling surface | I | Paper_039. |
| 4 | Substrate mode-content supports BHPT decomposition | P (definitional) | Standard-form construction. |
| 5 | Partial-wave decomposition | I | Standard math. |
| 6 | Regge-Wheeler / Teukolsky equation form | I | Standard math (I-BHPT). |
| 7 | Ingoing-only horizon boundary condition | P-Horizon-Ingoing-Only | Postulate. |
| 8 | Asymptotic outgoing boundary at infinity | P-Asymptotic-Outgoing | Postulate. |
| 9 | Scattering / transmission coefficient structure | D-via-I | Application of WKB / matching machinery (I-WKB) under boundary conditions. |
| 10 | Specific phase shifts / gray-body factors | I | Standard BHPT numerical content. |
| 11 | Substrate trans-Planckian corrections | OPEN | Paper_040 + Paper_042 connection. |

---

## §3 The Substrate Audit

### 3.1 Substrate-level BHPT setup

By I-014, V1 modulates rule-type-carrier propagation on the curved acoustic background. Linearized perturbations around a black-hole acoustic-metric configuration produce a substrate-level BHPT.

By I-039, the horizon is a decoupling surface: substrate modes from inside cannot influence modes outside. This **forces** the ingoing-only boundary condition at the horizon (P-Horizon-Ingoing-Only).

### 3.2 Standard BHPT machinery applies

Under the substrate audit, standard BHPT machinery (I-BHPT: Regge-Wheeler potential, Teukolsky equation) applies. Partial-wave decomposition + WKB matching produces the standard transmission / reflection coefficients.

### 3.3 Substrate corrections

Substrate-level corrections enter in two regimes:
- **Near-horizon trans-Planckian (Paper_040):** Modes with effective frequency approaching $\omega_c = c/\ell_P$ at the horizon receive V5-cutoff corrections.
- **Substrate-interior (Paper_042):** For $r < \ell_P$, substrate description breaks down; BHPT description ceases to apply.

Outside these regimes, BHPT is structurally consistent with the substrate framework.

---

## §4 Distinguishing Structural vs Numerical Content

- **Structural (D-via-I):** BHPT decomposition, Regge-Wheeler-form scattering potentials, ingoing-only horizon boundary.
- **Inherited (I):** Specific transmission coefficients, quasi-normal-mode frequencies, gray-body factors. Standard BHPT numerical content.
- **OPEN:** Substrate trans-Planckian corrections, substrate-interior structure.

---

## §5 Falsification Criteria

- **F1:** Empirical detection of BHPT scattering inconsistent with standard Regge-Wheeler / Teukolsky predictions (outside the substrate-corrected regimes) — would refute the BHPT-substrate consistency.
- **F2:** Substrate evidence that the horizon does NOT impose ingoing-only boundary — refutes P-Horizon-Ingoing-Only.
- **F3:** Empirical detection of substrate trans-Planckian corrections at scales inconsistent with $(\ell_P/M)^2$ — refutes Paper_040 application.
- **F4:** Detection of modes traversing the horizon outward — refutes Paper_039 decoupling-surface property.

---

## §6 Position Statement

BHPT scattering structure is **FORM-FORCED** in ED as the substrate-level perturbation theory of V1-modes on curved acoustic background with decoupling-surface horizon boundary. Numerical content INHERITED. Substrate trans-Planckian corrections are at $(\ell_P/M)^2$ for macroscopic black holes — negligible.

---

**End Paper 044 (FIXED).**
