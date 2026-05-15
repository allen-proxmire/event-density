# Paper 046 — Kerr Twist and Axisymmetric Substrate Geometry

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_039 (horizon as decoupling surface), Paper_044 (BHPT scattering), Paper_045 (helicity), Paper_017 (Lorentz covariantization).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the Kerr metric from substrate primitives; the Kerr acoustic-metric form is INHERITED from standard rotating-acoustic-metric machinery.
2. It does **not** claim a substrate-level audit of the Kerr interior structure (ergosphere, ring singularity); interior structure is OPEN.
3. It does **not** introduce new substrate primitives.
4. "Kerr twist" = the substrate-level expression of axisymmetric rotation, manifesting as the off-diagonal $g_{t\phi}$ component of the acoustic metric and the helical structure of substrate-level transport.
5. "Axisymmetric substrate geometry" = the substrate edge-set + rule-type bundle structure under rotation, supplying the off-diagonal metric component.

---

## Abstract

The Kerr twist — axisymmetric rotational off-diagonal $g_{t\phi}$ component of the acoustic metric — is FORM-FORCED in ED by P05 (polarity-transport along edges) + P09 ($U(1)$-valued polarity) under axisymmetric substrate edge-set rotation. The substrate audit composes: (i) substrate-level rotational vorticity carried by rule-type bundle automorphisms; (ii) coarse-graining of vorticity to a connection one-form via Paper_016 polarity-connection match + DCGT; (iii) the connection one-form contributes the $g_{t\phi}$ off-diagonal acoustic-metric component. The structural form FORCED; numerical $a$ (Kerr angular-momentum parameter) INHERITED via matching.

---

## §1 Introduction

Kerr black holes are axisymmetric rotating solutions; the acoustic-metric analog has a characteristic off-diagonal $g_{t\phi}$ component encoding the frame-dragging. This paper supplies the substrate audit of the rotational structure: $g_{t\phi}$ arises from substrate-level vorticity carried by rule-type bundle automorphisms, coarse-grained to a connection one-form on the rotating background.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies axial-symmetry direction.
- **P05 (Polarity-transport along edges)** — substrate-level transport carrying vorticity.
- **P09 ($U(1)$-valued polarity)** — supplies the phase-rotation structure.
- **P10 (Rule-type primitive)** — supplies rule-type bundle and automorphisms.

### 2.2 Upstream dependencies

- **I-016:** Polarity-connection match (Paper_016).
- **I-017:** Substrate→continuum Lorentz covariantization (Paper_017).
- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-073:** DCGT (Paper_073).
- **I-Kerr:** Standard Kerr-metric machinery / Newman-Penrose formalism (standard math).

### 2.3 Paper-specific postulates

- **P-Substrate-Vorticity:** Axisymmetric substrate-level rotation produces a non-zero substrate-vorticity field $\omega_{\mathrm{sub}}$ along the symmetry axis, carried by rule-type bundle automorphisms.
- **P-Twist-Coarse-Graining:** Coarse-graining $\omega_{\mathrm{sub}}$ via DCGT + Paper_016 produces an off-diagonal connection one-form component identified with the Kerr $g_{t\phi}$ at leading order.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P05 polarity-transport on edges | P | Primitive. |
| 2 | P09 $U(1)$ polarity | P | Primitive. |
| 3 | Axisymmetric substrate edge-set | P (definitional setup) | Definitional. |
| 4 | Substrate-vorticity along symmetry axis | P-Substrate-Vorticity | Postulate. |
| 5 | Coarse-graining via DCGT + Paper_016 | I | Paper_073 + Paper_016. |
| 6 | Connection one-form off-diagonal component | P-Twist-Coarse-Graining | Postulate. |
| 7 | Acoustic-metric $g_{t\phi}$ from connection one-form | D-via-I | Application of I-017 acoustic-metric construction. |
| 8 | Kerr-metric form recovery at leading order | D-via-I | Standard rotating-acoustic-metric machinery (I-Kerr). |
| 9 | Numerical Kerr $a$ parameter | I | Empirical / standard matching. |
| 10 | Frame-dragging phenomenology | I | Standard Kerr predictions. |
| 11 | Interior ergosphere / ring-singularity structure | OPEN | Not claimed. |

---

## §3 The Substrate Audit

### 3.1 Axisymmetric substrate-vorticity

Under axisymmetric substrate edge-set rotation, P-Substrate-Vorticity declares that polarity-transport (P05) along edges acquires a non-zero substrate-vorticity component $\omega_{\mathrm{sub}}$ aligned with the symmetry axis. This is the substrate-level expression of rotation.

### 3.2 Coarse-graining to a connection one-form

By I-016 (polarity-connection match) + I-073 (DCGT), substrate vorticity coarse-grains to a smooth connection one-form $\mathcal{A}_\mu\, dx^\mu$. Under P-Twist-Coarse-Graining, the off-diagonal component of this one-form is identified with the Kerr $g_{t\phi}$ acoustic-metric component at leading order.

### 3.3 Acoustic-metric Kerr form

By I-017, the coarse-grained kinematic frame is the acoustic metric. With off-diagonal $g_{t\phi}$ supplied by §3.2, the acoustic metric takes the rotating form (Kerr-analog). Standard rotating-acoustic-metric machinery (I-Kerr) then produces the full Kerr-metric structure at leading order.

### 3.4 What is OPEN

The substrate-interior structure for $r < \ell_P$ inside the Kerr horizon — including ergosphere details and ring-singularity-analog (which would be a non-substrate-resolvable region per Paper_042) — is OPEN. The substrate audit here covers the **exterior** Kerr structure (outside the horizon), where acoustic-metric guardrails (Paper_035) hold.

---

## §4 Distinguishing Structural vs Numerical Content

- **Structural (D-via-I):** Kerr-metric form, off-diagonal $g_{t\phi}$ origin in substrate vorticity, frame-dragging phenomenology.
- **Inherited (I):** Numerical Kerr $a$ parameter; specific frame-dragging coefficients.
- **OPEN:** Substrate interior structure; ring-singularity analog.

---

## §5 Falsification Criteria

- **F1:** Empirical detection of frame-dragging phenomenology inconsistent with standard Kerr predictions outside substrate-corrected regimes — would refute the substrate identification.
- **F2:** Substrate evidence that axisymmetric rotation does NOT produce substrate-vorticity — refutes P-Substrate-Vorticity.
- **F3:** Substrate evidence that coarse-graining vorticity does NOT produce off-diagonal acoustic-metric component — refutes P-Twist-Coarse-Graining.
- **F4:** Detection of a rotating black-hole spacetime not described by acoustic-metric Kerr form — would refute the audit's structural claim.

---

## §6 Position Statement

Kerr twist is **FORM-FORCED** in ED via substrate-level vorticity (P-Substrate-Vorticity) + coarse-graining (P-Twist-Coarse-Graining) + acoustic-metric covariantization (Paper_017). Numerical content INHERITED. Substrate-interior structure OPEN.

---

**End Paper 046 (FIXED).**
