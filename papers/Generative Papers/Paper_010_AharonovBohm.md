# Paper 010 — Aharonov–Bohm Phase from Rule-Type Circulation

**Series:** Wave-2 Generative Papers (QM-Kinematics Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_008 (Phase Structure), Paper_009 (Berry phase), Paper_015 (T17), Paper_089 (V1 kernel).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the AB phase numerical coefficient ($e/\hbar$ in standard units); the coefficient is INHERITED via empirical matching.
2. It does **not** claim a substrate mechanism for the electromagnetic flux $\Phi_{\mathrm{EM}}$ itself; flux is a coarse-grained gauge-field invariant inherited from T17.
3. It does **not** claim novel empirical predictions distinguishing the substrate AB phase from standard AB phase.
4. It does **not** introduce new substrate primitives.
5. "AB phase" here means: the $U(1)$ phase $\Delta\phi_{\mathrm{AB}} = \oint_C A_\mu\, dx^\mu$ acquired by a rule-type carrier traversing a loop $C$ enclosing a region of gauge-field flux, with the carrier excluded from the flux region.

---

## Abstract

The Aharonov–Bohm phase is FORM-FORCED in ED as the circulation of the rule-type bundle connection (Paper_015 / T17) around a closed substrate-level loop encircling a flux-supporting region. P05 (polarity-transport) supplies the substrate connection; P09 ($U(1)$-valued polarity) supplies the target group; T17 supplies the rule-type bundle on which the connection lives. The phase depends on the enclosed flux even when the carrier path lies entirely in a flat-connection region — this is FORCED by the bundle structure, not derived from local field strengths. The numerical coefficient is INHERITED.

---

## §1 Introduction

The Aharonov–Bohm effect demonstrates that gauge potentials carry observable consequences even where field strengths vanish: a charged particle encircling a solenoid acquires a phase $e \Phi/\hbar$ even though the magnetic field on its path is zero. This paper supplies the substrate-level origin: the phase is the circulation of the rule-type bundle connection around the loop, FORCED by the global topology of the bundle rather than by local field data.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P05 (Polarity-transport along edges)** — substrate-level parallel transport.
- **P07 (Channel structure)** — gauge-rule-type bundle structure.
- **P09 (U(1)-valued polarity)** — target group of the connection.
- **P10 (Rule-type primitive)** — rule-type carrier and composition.

### 2.2 Upstream dependencies

- **I-T17:** Gauge fields as connections on rule-type bundles (Paper_015).
- **I-Phase:** Rule-type phase structure $S^1$ (Paper_008).
- **I-Holonomy:** Standard fiber-bundle holonomy (standard math).
- **I-Flux:** Standard EM flux quantization / Stokes-theorem machinery (standard math).

### 2.3 Paper-specific postulates

- **P-Excluded-Region:** The flux-supporting region $R_\Phi$ is structurally excluded from the carrier's substrate-level edge-set (the carrier path does not traverse $R_\Phi$). Definitional construction of the AB setup.
- **P-Flat-Outside:** Outside $R_\Phi$, the rule-type bundle connection is flat (curvature vanishes). Definitional regime.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P05 polarity-transport | P | Primitive (Paper_087). |
| 2 | P09 $U(1)$ polarity | P | Primitive. |
| 3 | T17: gauge fields = rule-type bundle connections | I | Paper_015. |
| 4 | Rule-type carrier traverses loop $C$ outside $R_\Phi$ | P-Excluded-Region | Definitional setup. |
| 5 | Connection flat outside $R_\Phi$ | P-Flat-Outside | Definitional regime. |
| 6 | Loop $C$ encircles $R_\Phi$ | P (topological setup) | Definitional. |
| 7 | Holonomy around $C$ via standard fiber-bundle theorem | I | Standard math (I-Holonomy). |
| 8 | Holonomy non-trivial despite local flatness (global topology) | I | Standard fiber-bundle topology. |
| 9 | AB phase $\Delta\phi_{\mathrm{AB}} = \oint_C A_\mu\, dx^\mu$ | D-via-I | Application of I-Holonomy + I-T17 to the AB setup. |
| 10 | Stokes-theorem expression $\Delta\phi_{\mathrm{AB}} = \int_S F$ over surface $S$ bounding $C$ | I | Standard math (I-Flux). |
| 11 | Numerical coefficient $e/\hbar$ | I | Empirical matching. |

---

## §3 The Derivation

### 3.1 Setup

A rule-type carrier traverses a closed loop $C$ in substrate space. The loop encircles a region $R_\Phi$ containing gauge-field flux. By P-Excluded-Region, the carrier's substrate-level edge-set lies entirely outside $R_\Phi$. By P-Flat-Outside, the rule-type bundle connection is flat on the carrier's path.

### 3.2 Holonomy

The bundle connection's holonomy around $C$ is, by I-Holonomy applied to I-T17:
$$U_C = \exp\!\left(i \oint_C A_\mu\, dx^\mu\right) .$$

### 3.3 Non-triviality from global topology

Even though the connection is flat on $C$ (P-Flat-Outside), $U_C$ is non-trivial when $C$ encircles $R_\Phi$. This is a structural feature of fiber-bundle holonomy (I-Holonomy) — flat-but-not-trivial connections on non-simply-connected base spaces — not a substrate-level surprise.

### 3.4 Phase and flux

The AB phase $\Delta\phi_{\mathrm{AB}} = \oint_C A_\mu\, dx^\mu$ equals the enclosed flux $\Phi_{\mathrm{EM}} = \int_S F$ by standard Stokes-theorem application (I-Flux). The numerical coefficient relating $\Phi_{\mathrm{EM}}$ to the dimensionless phase is $e/\hbar$ — INHERITED.

---

## §4 Distinguishing Definitional vs Derived

- **Definitional (P):** The AB setup itself — carrier path excluded from flux region, connection flat outside, loop encircling flux. These are P (definitional) features of "the AB experiment," not derived predictions.
- **Inherited (I):** Holonomy theory, Stokes theorem, numerical $e/\hbar$.
- **Derived (D-via-I):** The phase formula $\Delta\phi_{\mathrm{AB}} = \oint_C A_\mu\, dx^\mu$ as the application of holonomy theory to the AB setup under T17.

The honest framing: ED does **not** newly predict the AB phase; it supplies a substrate-level audit showing the phase emerges from the same fiber-bundle structure standard QM uses, with the bundle structure itself sourced from T17 / P05 / P09.

---

## §5 Open Structural Questions

- **O-AB-1:** Non-Abelian AB generalization (rule-type carriers in higher-rank irreps).
- **O-AB-2:** Substrate audit of fractional / non-trivial-topology AB effects.
- **O-AB-3:** Substrate derivation of $e/\hbar$ from substrate normalization rather than empirical matching.

---

## §6 Falsification Criteria

- **F1:** Empirical detection of AB phase in a setup where P-Excluded-Region fails (carrier actually traverses flux region) and the substrate predicts a different phase — would refute the substrate audit.
- **F2:** Empirical AB phase that violates fiber-bundle holonomy structure (e.g., phase-dependent on rate of traversal beyond standard adiabatic corrections) — would refute the I-Holonomy application.
- **F3:** AB phase detected in a system with no rule-type carrier (e.g., classical fluid) — would refute T17's identification of gauge fields with rule-type bundle connections.

---

## §7 Position Statement

The Aharonov–Bohm phase is **FORM-FORCED** in ED as the circulation of the T17 rule-type bundle connection around a flux-enclosing loop. P05 + P09 + T17 supply the bundle structure; standard fiber-bundle holonomy supplies the phase. Numerical content is **INHERITED**.

The result composes with Paper_008 (rule-type phase), Paper_009 (Berry phase — AB is the parameter-space-loop case with parameter = position), and Paper_015 (T17).

---

**End Paper 010 (FIXED).**
