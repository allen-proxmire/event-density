# Paper 035 — Acoustic-Metric Guardrails (ED-Phys-10) Under Continuum Limit

**Series:** Wave-2 Generative Papers (Gravity Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_017 (Lorentz covariantization), Paper_039 (horizon as decoupling surface), Paper_073 (DCGT), Paper_033 (Arc ED-10).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that the acoustic metric is the GR metric; it is a coarse-grained kinematic frame.
2. It does **not** claim that the guardrails are physically necessary for empirical correctness; they are theoretical guardrails for substrate-consistency.
3. It does **not** introduce new substrate primitives.
4. It does **not** claim that the guardrails fully characterize the admissible regime; six guardrails are formalized as load-bearing; further extensions are OPEN.
5. "Acoustic-metric guardrails" = the six conditions (C1)-(C6) under which the substrate-coarse-grained acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ produces consistent kinematic predictions without violating substrate primitives.

---

## Abstract

We formalize six acoustic-metric guardrails (C1)-(C6) under which the substrate-coarse-grained acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ (Paper_017) supports the substrate-gravity machinery (Papers_027–034). The guardrails are: (C1) substrate-$c$ constancy, (C2) sub-Planckian gradient, (C3) hyperbolic signature preservation, (C4) ghost-free kinetic term, (C5) DCGT hydrodynamic-window validity, (C6) decoupling-surface admissibility. (C1)-(C6) are declared as paper-specific postulates with explicit substrate-consistency justifications. Under (C1)-(C6), the acoustic-metric framework is consistent; outside, predictions degrade.

---

## §1 Introduction

The acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ emerges in ED via DCGT coarse-graining of substrate transport (Paper_073) + substrate→continuum Lorentz covariantization (Paper_017). It is **not** the GR metric; it is a kinematic frame for dressed-object propagation in the substrate.

The acoustic-metric framework supports:
- V1 propagation in curved background (Paper_014).
- Horizon as decoupling surface (Paper_039).
- Substrate gravity flat-background field equation (Paper_036).
- Arc ED-10 scalar-tensor covariantization (Paper_033).
- Hawking spectrum (Paper_047).

This paper formalizes the guardrails (C1)-(C6) under which the framework operates consistently.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — substrate-level transport carrier.
- **P03 (Channel + locus indexing; spatial homogeneity)** — continuum manifold structure.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck-scale gradient cutoff.
- **P10 (Rule-type primitive)** — supplies V1 and V5 kernels.

### 2.2 Upstream dependencies

- **I-017:** Substrate→continuum Lorentz covariantization (Paper_017).
- **I-073:** DCGT (Paper_073).
- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-014:** V1 in curved acoustic background (Paper_014).
- **I-RB-1:** P-RB-1 substrate-$c$ constancy (Paper_012).

### 2.3 Paper-specific postulates (the six guardrails)

- **(C1) Substrate-$c$ constancy:** P-Substrate-c-Constancy (inherited from Paper_012) holds — substrate $c$ is constant under acoustic-metric variations.
- **(C2) Sub-Planckian gradient:** $\ell_{\mathrm{ED}} |\partial g^{\mathrm{ac}}|/|g^{\mathrm{ac}}| \ll 1$ everywhere in the regime of applicability.
- **(C3) Hyperbolic signature:** $g^{\mathrm{ac}}_{\mu\nu}$ has Lorentzian signature $(-,+,+,+)$.
- **(C4) Ghost-free kinetic term:** The scalar-mode kinetic term in any extension (e.g., Arc ED-10) is positive-definite on physical perturbations.
- **(C5) DCGT hydrodynamic window:** $\ell_{V1}, \ell_{V5} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$.
- **(C6) Decoupling-surface admissibility:** Where horizons exist, the decoupling-surface condition of Paper_039 holds.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Acoustic metric emerges via coarse-graining | I | Paper_017. |
| 2 | DCGT hydrodynamic window | I | Paper_073. |
| 3 | Substrate-$c$ constancy | C1 / I-RB-1 | Inherited from Paper_012. |
| 4 | Sub-Planckian gradient | C2 (postulate) | Postulate. |
| 5 | Hyperbolic signature preservation | C3 (postulate) | Postulate. |
| 6 | Ghost-free kinetic term in extensions | C4 (postulate) | Postulate. |
| 7 | Hydrodynamic-window regime | C5 (postulate) | Postulate. |
| 8 | Decoupling-surface admissibility | C6 (postulate) | Postulate. |
| 9 | Under (C1)-(C6): acoustic-metric framework consistent | D-via-I | Composition of guardrails + inheritances. |
| 10 | Outside (C1)-(C6): framework breaks down | D | Negation of step 9. |

---

## §3 The Six Guardrails In Detail

### 3.1 (C1) Substrate-$c$ constancy

Inherited from Paper_012 P-Substrate-c-Constancy: substrate $c$ does not vary with $g^{\mathrm{ac}}$. Acoustic-metric phenomena (gravitational time dilation, redshift) are coarse-graining effects, not substrate-$c$ variations.

### 3.2 (C2) Sub-Planckian gradient

The acoustic metric varies slowly on the substrate scale: $\ell_{\mathrm{ED}} |\partial g^{\mathrm{ac}}| / |g^{\mathrm{ac}}| \ll 1$. Outside this regime, DCGT coarse-graining fails to produce a smooth metric.

### 3.3 (C3) Hyperbolic signature

$g^{\mathrm{ac}}_{\mu\nu}$ must have Lorentzian signature for the acoustic-metric framework to support physical dressed-object propagation. Euclidean-signature regions are non-physical artifacts of pathological coarse-graining.

### 3.4 (C4) Ghost-free kinetic term

In scalar-tensor extensions (Paper_033), the kinetic-term coefficient must be positive-definite on physical scalar perturbations. Negative-norm modes (ghosts) signal a pathological theory.

### 3.5 (C5) DCGT hydrodynamic window

The hydrodynamic-window condition $\ell_{V1}, \ell_{V5} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ (Paper_073) must hold for the coarse-grained acoustic-metric description to be valid.

### 3.6 (C6) Decoupling-surface admissibility

At horizons (where they exist), the decoupling-surface condition of Paper_039 must hold for the acoustic metric to support horizon-crossing kinematics.

---

## §4 What Breaks Outside the Guardrails

| Guardrail violation | Failure mode |
|---|---|
| (C1) Substrate-$c$ variation | Apparent-$c$ variation conflated with substrate $c$; P-RB-1 fails. |
| (C2) Trans-Planckian gradient | Acoustic-metric description not smooth; substrate microstructure exposed. |
| (C3) Non-hyperbolic signature | Closed timelike curves / non-causal regions. |
| (C4) Ghost modes | Negative-norm scalar perturbations; theory pathological. |
| (C5) Hydrodynamic-window violation | DCGT coarse-graining not valid; substrate dynamics directly relevant. |
| (C6) Decoupling-surface failure | Horizon framework breaks; Hawking-arc predictions invalidated. |

---

## §5 Falsification Criteria

- **F1:** Empirical detection of substrate-$c$ variation — refutes (C1) / P-Substrate-c-Constancy.
- **F2:** Detection of physical regime with $\ell_{\mathrm{ED}}|\partial g^{\mathrm{ac}}| \sim |g^{\mathrm{ac}}|$ producing predictions consistent with substrate gravity — refutes (C2)'s necessity.
- **F3:** Substrate-consistent acoustic metric with non-hyperbolic signature in an empirically accessible regime — refutes (C3).
- **F4:** Substrate-consistent kinetic-term modification with ghost modes that nonetheless produces correct empirical predictions — refutes (C4).
- **F5:** Empirical evidence that DCGT coarse-graining holds outside the hydrodynamic window — refutes (C5).
- **F6:** Horizon physics inconsistent with Paper_039 decoupling-surface — refutes (C6).

---

## §6 Position Statement

Six guardrails (C1)-(C6) declared as load-bearing for the acoustic-metric framework's consistency. Inside the guardrails, the framework supports substrate-gravity (Papers_027–038), V1 curved-background (Paper_014), and Hawking arc (Papers_047–049). Outside, predictions degrade. The guardrails are paper-specific postulates with explicit substrate-consistency justifications.

---

**End Paper 035 (FIXED).**
