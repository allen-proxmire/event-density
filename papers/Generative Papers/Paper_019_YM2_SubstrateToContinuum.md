# Paper 019 — Substrate→Continuum Yang–Mills Limit (YM-2) — FIXED

**Series:** Wave-2 Generative Papers (Yang–Mills Arc, YM-2)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087 canonical enumeration) + paper-specific postulate declared in §2.

**FIXED notes (2026-05-13):**
- Primitive enumeration aligned with Paper_087 canonical list.
- §3.4 Euler-Lagrange derivation labeled D (standard variational derivation from the P-postulated action), with explicit acknowledgment that the action itself is constructed via P-YM-Action-Coarse-Graining.
- Template "Flexibility & Correction Block" deleted; revision triggers folded into Open Questions.
- §X.5 P-postulates inventory folded into §2.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a constructive proof of the continuum-limit existence of the YM measure.
2. It does **not** claim that the continuum limit is unique (different choices of coarse-graining produce different effective actions at sub-leading order).
3. It does **not** claim derivation of the YM coupling-constant value from substrate primitives.
4. It does **not** claim OS-positivity or mass gap; those are addressed in Papers_020 and 021.
5. It does **not** introduce new substrate primitives.
6. "Substrate→continuum YM limit" refers to: coarse-graining of substrate-level rule-type dynamics yields the continuum YM action at leading order, under a declared coarse-graining postulate.

---

## Abstract

We construct the leading-order continuum-limit Yang–Mills action $S_{\mathrm{YM}} = -\tfrac{1}{4}\int F^a_{\mu\nu} F^{a\mu\nu}\, d^4x$ as a coarse-graining of the substrate-level rule-type dynamics. The construction composes: (i) T17 gauge-fields-as-rule-type-bundle-connections (Paper_015); (ii) non-Abelian rule-type composition (Paper_016); (iii) DCGT generalized to non-Abelian (Paper_018); (iv) substrate→continuum Lorentz covariantization (Paper_017). The coarse-graining identification — that substrate rule-type action coarse-grains to the YM action at leading order — is the declared postulate P-YM-Action-Coarse-Graining. The continuum YM equations $D_\mu F^{\mu\nu} = J^\nu$ follow via standard variational principles from the postulated action.

---

## §1 Introduction

The substrate→continuum YM step is YM-2 of the Yang–Mills arc. It supplies the construction route for the continuum YM theory whose OS-positivity (Paper_020) and mass gap (Paper_021) are audited downstream.

The construction is **not** a re-derivation of the YM action from a deeper substrate principle. It is a **coarse-graining identification**: the leading-order coarse-graining of the substrate rule-type dynamics matches the standard YM action functional. This identification is declared as P-YM-Action-Coarse-Graining.

---

## §2 Primitive Inputs and Paper-Specific Postulate

### 2.1 Primitives invoked (per Paper_087 canonical enumeration)

- **P02 (Participation)** — supplies substrate-level field content.
- **P07 (Channel structure)** — supplies gauge-rule-type bundle structure.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the UV cutoff $\omega_c = c/\ell_{\mathrm{ED}}$.
- **P09 (U(1)-valued polarity)** — supplies the Abelian phase structure, extended to non-Abelian via P10.
- **P10 (Rule-type primitive)** — supplies composition, V1, V5, non-Abelian rule-type extension (per YM-1 amendment for compact simple groups).
- **P11 (Commitment-irreversibility)** — supplies retarded-kernel structure.

### 2.2 Inherited closed-arc results

- **I-T17:** Gauge fields as rule-type bundle connections (Paper_015).
- **I-NonAb:** Non-Abelian rule-type composition (Paper_016).
- **I-LorCov:** Substrate→continuum Lorentz covariantization (Paper_017, with P-Lorentz-Covariant-Continuum postulate).
- **I-DCGT-NA:** DCGT generalized to non-Abelian (Paper_018).
- **I-V1:** V1 kernel finite width (Paper_089).
- **I-UV-Cutoff:** Substrate-level UV cutoff $\omega_c = c/\ell_{\mathrm{ED}}$ via P08.

### 2.3 Paper-specific postulate

- **P-YM-Action-Coarse-Graining:** The leading-order coarse-graining of the substrate-level rule-type action under DCGT-NA + Lorentz covariantization yields the standard YM action functional $S_{\mathrm{YM}} = -\tfrac{1}{4}\int F^a_{\mu\nu} F^{a\mu\nu}\, d^4x$ with field strength $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g f^{abc} A^b_\mu A^c_\nu$.

The Wilson-loop substrate-graph identification is a **definitional construction**: Wilson loops on the substrate-level rule-type bundle are identified with the standard Wilson-loop observables of continuum YM.

The YM-regime condition (sub-Planckian, kinematic regime) is A→regime.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | T17 rule-type bundle connections | I | Paper_015. |
| 2 | Non-Abelian rule-type composition | I | Paper_016. |
| 3 | Substrate→continuum Lorentz covariantization | I | Paper_017. |
| 4 | DCGT-NA hydrodynamic window | I | Paper_018 + Paper_073. |
| 5 | Substrate-level UV cutoff $\omega_c = c/\ell_{\mathrm{ED}}$ | I | Via P08. |
| 6 | YM-action coarse-graining identification | P-YM-Action-Coarse-Graining | Postulate, declared. |
| 7 | Wilson-loop substrate-graph identification | P (definitional) | Definitional construction. |
| 8 | YM-regime applicability | A→regime | Sub-Planckian kinematic regime. |
| 9 | Continuum YM equations $D_\mu F^{\mu\nu} = J^\nu$ via Euler–Lagrange | D | Standard variational derivation from the P-postulated action of step 6. |
| 10 | Numerical value of $g_{\mathrm{YM}}$ | I — empirical | Inherited from empirical YM matching. |

The §3.4 Euler–Lagrange step is **D (standard math derivation)** from the postulated action; the action itself is **P** (step 6). This distinction is now explicit.

---

## §3 The Construction

### 3.1 Substrate rule-type action

From T17 (Paper_015), gauge fields are connections on rule-type bundles. From Paper_016, the non-Abelian rule-type composition produces a substrate-level action functional $S_{\mathrm{sub}}[\text{rule-types}]$ on the bundle.

### 3.2 DCGT-NA coarse-graining

DCGT (Paper_073), generalized to non-Abelian (Paper_018), supplies the substrate→continuum bridge. The hydrodynamic window $\ell_P \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ applies.

### 3.3 The coarse-graining identification

**P-YM-Action-Coarse-Graining declares:** The leading-order coarse-grained action matches $S_{\mathrm{YM}}$ as stated in §2.3.

This is the substantive declared content. It is not derivable from §3.1+§3.2 without an explicit matching computation; the postulate states the matching identifies with the standard YM action.

### 3.4 Continuum YM equations

Given the postulated action $S_{\mathrm{YM}}$, the Euler–Lagrange variational principle yields
$$D_\mu F^{\mu\nu} = J^\nu .$$

This is a **standard variational derivation** (D) from the postulated action. The action is **P** (step 6 of audit); the EL step is **D** applied to that P. The honest framing: equations are derived from a postulated action; the action is not itself derived from substrate primitives without P-YM-Action-Coarse-Graining.

---

## §4 What the Construction Does and Does Not Supply

**Supplies:**
- Leading-order YM action via coarse-graining identification.
- Continuum YM equations via standard variational principle.
- Wilson-loop substrate-graph identification.
- UV cutoff inherited from substrate scale.

**Does not supply:**
- Constructive proof of continuum-measure existence.
- Numerical value of $g_{\mathrm{YM}}$.
- Sub-leading corrections beyond leading order.
- OS-positivity or mass gap (downstream papers).

---

## §5 Open Structural Questions

- **O-YM2-1:** Sub-leading corrections to $S_{\mathrm{YM}}$ from V1/V5 finite-width effects.
- **O-YM2-2:** Constructive derivation of P-YM-Action-Coarse-Graining from a deeper coarse-graining principle.
- **O-YM2-3:** Group-dependent matching of $g_{\mathrm{YM}}$ from substrate to empirical value.
- **O-YM2-Revision:** If a constructive derivation of P-YM-Action-Coarse-Graining appears, step 6 of audit strengthens to D and §3.3 strengthens accordingly.

---

## §6 Falsification Criteria

- **F1:** Demonstration that DCGT-NA coarse-graining does **not** match $S_{\mathrm{YM}}$ at leading order — refutes P-YM-Action-Coarse-Graining.
- **F2:** Demonstration that the Wilson-loop substrate-graph identification produces observables inconsistent with continuum YM Wilson loops — refutes the definitional step.
- **F3:** Demonstration that the YM-regime is empty (no admissible substrate parameter range produces YM-class behavior) — refutes A→regime.

---

## §7 Position Statement

The substrate-level YM construction supplies the continuum YM action at leading order under the declared postulate P-YM-Action-Coarse-Graining. The continuum YM equations follow via standard variational principle. The construction is a **leading-order coarse-graining identification**, not a deeper-than-action substrate derivation.

This feeds Paper_020 (OS-positivity audit) and Paper_021 (mass-gap mechanism) for the structural-positive Clay-relevance verdict synthesized in Paper_023.

---

## Appendix — The Coarse-Graining Identification in Detail

P-YM-Action-Coarse-Graining identifies the leading-order coarse-grained substrate-level action with $S_{\mathrm{YM}}$. The identification has three components:

| Component | Substrate origin | Continuum target |
|---|---|---|
| Kinetic term $-\tfrac{1}{4} F_{\mu\nu} F^{\mu\nu}$ | V1-regulated rule-type bundle curvature | YM kinetic term |
| Non-Abelian quartic $g f^{abc} A^b_\mu A^c_\nu$ inside $F_{\mu\nu}$ | Non-Abelian rule-type composition (Paper_016) | YM non-Abelian self-interaction |
| Lorentz covariance | Substrate→continuum acoustic-metric (Paper_017) | YM Lorentz invariance |

The identification is **declared**, not derived from a deeper principle. Future work (O-YM2-2) could derive it; this paper postulates it explicitly.

---

**End Paper 019 (FIXED).**
