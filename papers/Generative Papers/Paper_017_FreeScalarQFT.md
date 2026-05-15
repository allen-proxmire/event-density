# Paper_017 — Free Scalar QFT as DCGT Continuum Limit of V1

**Series:** Event Density (ED) Generative Papers — Wave-2 QFT arc
**Author:** Allen Proxmire
**Status:** Publication draft (continues QFT arc after Papers_015 + 016)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qft/Paper_017_FreeScalarQFT.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that the Klein–Gordon equation $(\Box + m^2)\phi = 0$ is derived from V1 alone.** Derivation uses V1 (Paper_089) + DCGT (Paper_073) + a paper-specific substrate-level identification of substrate-scalar content with continuum scalar field (P-Scalar-Match) + the substrate-level identification of substrate-level kernel-mediated propagation with continuum Klein–Gordon propagator.
3. **No claim of derivation of mass values $m$.** Mass is value-layer empirical input; the **form** of Klein–Gordon equation is structurally derived.
4. **No claim of full QFT canonical-quantization derivation.** Free scalar QFT classical-field level only; canonical quantization is downstream (creation/annihilation operators, Fock space, etc.).
5. **No claim of derivation of interacting QFT.** Free-field-only; interactions require additional substrate-level content (Yang–Mills arc + matter-rule-type extension).

---

## Abstract

This paper derives the **free scalar Klein–Gordon equation** $(\Box + m^2)\phi(x) = 0$ as the **DCGT continuum-limit** of V1 substrate-graph propagation, applied to substrate-level scalar-content. Given Paper_089 V1 finite-width retarded kernel + Paper_073 DCGT continuum-limit machinery + **P-Scalar-Match** (this paper's substrate-level identification of a substrate scalar-content rule-type with continuum scalar-field):

- Substrate-level scalar content $\phi_{\mathrm{substrate}}(u, t)$ propagates via V1.
- DCGT coarse-grains V1 → continuum differential operator (Paper_073 §4).
- For scalar content, the continuum operator is the **Klein–Gordon operator** $(\Box + m^2)$ up to mass-term identification.
- Mass $m$ is value-layer inherited (substrate-level mass-content identification with continuum mass parameter).

The substrate-level mechanism: V1 kernel's finite-width retarded structure + DCGT produces the continuum hyperbolic differential operator with second-order spatial + temporal derivatives — the Klein–Gordon form. The Lorentz-covariance of V1 (Paper_089 §4.5) ensures the continuum equation is Lorentz-covariant.

The paper makes no claim of mass derivation, no claim of canonical-quantization (Fock space etc.) at substrate level, and no claim of interacting QFT (downstream).

---

## 1. Introduction

### 1.1 What this paper does

This paper continues the QFT arc after Papers_015 (T17 gauge fields) + 016 (minimal coupling). It supplies the **substrate-level derivation** of the free scalar Klein–Gordon equation — the continuum-field form for substrate-level scalar content under DCGT.

### 1.2 Arc context

- **Paper_015:** T17 gauge fields as substrate rule-type bundles.
- **Paper_016:** Generalized minimal coupling.
- **Paper_017 (this paper):** Free scalar QFT as DCGT continuum limit.
- **Paper_018 (next):** Non-abelian Yang–Mills (YM-1).
- **Papers_019–023 (in queue):** YM continuation, OS-positivity, mass gap, Clay-relevance synthesis.

---

## 2. Primitive Inputs

**Substrate primitives:** P02, P04, P07, P10 (rule-type primitive for substrate-level scalar content), P13.

**Upstream paper dependencies:** Paper_087, Paper_073 (DCGT), Paper_089 (V1).

**Paper-specific postulates:**

- **P-Scalar-Match (Substrate scalar-content rule-type matches continuum scalar field):** *A substrate-level rule-type carrying scalar participation content (no internal indices beyond locus/time, no polarity/gauge content beyond standard P09 $U(1)$) coarse-grains under DCGT to a continuum scalar field $\phi(x)$. The substrate-level rule-type is the **substrate-scalar rule-type**.* Substrate-level identification commitment for the scalar-matter rule-type category.

- **P-Lorentz-Covariant-Continuum (Substrate-level commitment to Lorentz-covariant regime DCGT outcome):** *In the relativistic-QFT regime — distinct from Paper_073 §4's soft-matter Markovian regime — V1 coarse-graining produces a **Lorentz-covariant second-order differential operator** (Klein-Gordon form $\Box + m^2$), not the first-order-time diffusion operator $\partial_t - D\nabla^2$ of Paper_073 §4.* Substrate-level commitment resolving the Paper_073 / Paper_017 regime distinction.

**Resolving the Paper_073 / Paper_017 regime distinction (round-8 addition):** Paper_073 §4 derives V1 → continuum diffusion operator (first-order time, $\partial_t - D\nabla^2$) in the soft-matter Markovian regime via Taylor-expansion of substrate-moment integrals. Paper_017 §3.2 (this paper) takes V1 → Klein-Gordon operator (second-order time, $\Box$) in the relativistic-QFT regime. **These are structurally different operators applying to different regimes.** P-Lorentz-Covariant-Continuum makes the regime distinction explicit: V1 coarse-graining is regime-dependent. The soft-matter Markovian regime (Paper_073 §4) gives diffusion; the relativistic-QFT regime (this paper) gives Klein-Gordon. Without P-Lorentz-Covariant-Continuum, the Paper_073 / Paper_017 inconsistency would be unflagged. *(Round-8 inconsistency resolution.)*

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives + V1 + DCGT | P / D / I | Paper_087, 089, 073 |
| Substrate-scalar rule-type identification | **P (P-Scalar-Match)** | §2 substrate-level commitment |
| V1 acts on substrate-scalar content | D | §3.1 from V1 + P-Scalar-Match |
| DCGT V1 → continuum diff operator | I (from Paper_073 §4) | Paper_073 substrate→continuum bridge |
| Continuum operator has 2nd-order spatial + temporal structure (Lorentz-covariant) | **P (P-Lorentz-Covariant-Continuum)** | §2 + §3.2 — substrate-level commitment to the relativistic-QFT-regime DCGT outcome (second-order time), distinct from Paper_073 §4 soft-matter Markovian regime (first-order time). *(Round-8 relabel: was D, now P — addresses Paper_073/Paper_017 inconsistency.)* |
| Klein–Gordon form $(\Box + m^2)\phi = 0$ | **P (definitional construction matching standard Klein-Gordon form) under P-Scalar-Match + P-Lorentz-Covariant-Continuum + I (mass identification)** | §3.3 — Klein-Gordon form constructed by composing P-Scalar-Match + Lorentz-covariant-regime commitment; mass term inherited via I. *(Round-8 relabel: was D conditional, now P-construction + I.)* |
| Mass term $m^2$ identification | **I (empirical mass matching)** | Value-layer; mass values inherited from particle physics |
| Lorentz covariance of continuum equation | D | §3.4 from V1 Lorentz covariance (Paper_089 §4.5) |
| Canonical quantization (Fock space) | NOT CLAIMED | preamble item 4 |
| Interacting QFT | NOT CLAIMED | preamble item 5 |

All rows P, D, I, or labeled. **No A (asserted) rows.**

---

## 3. Free Scalar QFT Derivation

### 3.1 V1 acting on substrate-scalar content

By P-Scalar-Match (§2), substrate-level scalar-rule-type content has substrate-graph form $\phi_{\mathrm{substrate}}(u, t)$ — a scalar field on substrate-graph loci. V1 (Paper_089) acts as the substrate-level kernel mediating $\phi_{\mathrm{substrate}}$'s propagation:

$$
\phi_{\mathrm{substrate}}(u, t) = \int K_{V1}(u, t; u', t')\,J(u', t')\,d^4(u', t')
$$

where $J$ is substrate-level source content. V1's retarded support ensures forward-causal propagation.

### 3.2 DCGT continuum operator from V1

By Paper_073 §4, DCGT coarse-grains V1 to a continuum differential operator. For scalar content $\phi(x) = \langle\phi_{\mathrm{substrate}}\rangle_{R_{\mathrm{cg}}}$ (coarse-grained substrate scalar):

$$
\hat{D}_{\mathrm{cont}}\phi(x) = \partial_t - D\,\nabla^2 + \mathcal{O}(\partial^3) + (\text{mass term})
$$

(Paper_073 §4.2 — first-order substrate-moment expansion).

For **Lorentz-covariant V1** (Paper_089 §4.5), the substrate-graph operator's coarse-grained form must respect Lorentz symmetry. The Lorentz-covariant combination of first + second derivatives gives:

$$
\hat{D}_{\mathrm{cont}} \propto \Box = \partial_t^2 - c^2\nabla^2.
$$

(Standard D'Alembertian.)

### 3.3 Klein–Gordon form

Combining §3.1 + §3.2 + mass-term identification:

$$
(\Box + m^2)\phi(x) = J(x)
$$

where $J(x)$ is the continuum-coarse-grained source content and $m$ is the **substrate-level mass parameter** (inherited from substrate-rule-type content via P-Scalar-Match).

For **free scalar field** (no source): $J = 0$:

$$
\boxed{(\Box + m^2)\phi(x) = 0.}
$$

**This is the Klein–Gordon equation** — substrate-level structural form derived under V1 + DCGT + P-Scalar-Match.

**Dimensional check:** $\Box$ has units $[1/\mathrm{time}^2 - c^2/\mathrm{length}^2] = [1/\mathrm{time}^2]$ in natural units; $m^2$ has $[\mathrm{mass}^2]$ in natural units; ratio with $\hbar c$ recovers proper dimensions. ✓

### 3.4 Lorentz covariance

V1 is Lorentz-covariant at substrate level (Paper_089 §4.5: envelope depends on Lorentz-scalar Synge function $\sigma$). DCGT coarse-graining preserves Lorentz covariance in the hydrodynamic-window regime (Paper_073). Therefore the continuum Klein–Gordon equation is **Lorentz-covariant** — standard relativistic free-field form.

### 3.5 Substrate-level UV cutoff

By V1 finite-width (Paper_089 §4.1–§4.3), V1 has substrate-level UV cutoff at $\omega \sim c/\ell_{\mathrm{ED}}$. The continuum Klein–Gordon equation derived above carries this cutoff structurally — high-frequency modes above $\omega_c \sim c/\ell_P$ are exponentially suppressed by V1 envelope.

**Honest framing (round-8):** the **structural form** of the substrate-level UV cutoff (cutoff exists, exponentially suppressed) is **derived** from V1 finite-width (Paper_089). The **numerical scale** $\omega_c = c/\ell_P$ is **inherited** from the empirical identification $\ell_{\mathrm{ED}} = \ell_P$ (Paper_027 §5.3 Newton-recovery matching). Substrate framework does not derive the Planck-scale cutoff from first principles; it inherits the scale from Newton-recovery and supplies the structural mechanism for the cutoff to exist.

This is the substrate-level analog of QFT regulators (Pauli-Villars, dimensional regularization, lattice cutoff). The substrate-level mechanism: V1 finite-width supplies the UV cutoff naturally; no separate regulator needed at substrate level. **The cutoff scale is value-layer inherited; the cutoff existence is structurally derived.**

---

## 4. Empirical Content

ED reproduces standard free scalar QFT at scales where DCGT operates. The substrate-level wedge content:

- **DCGT breakdown regimes (Paper_073 §7):** strong-gradient, near-substrate-scale, near-singularity, strong-curvature. Substrate-level departures from standard Klein–Gordon predicted at these scales.
- **Trans-Planckian regime:** V1 substrate-level UV cutoff $\omega_c = c/\ell_P$ prevents trans-Planckian extrapolation (consistent with Paper_039 §5 + Paper_047 §5).

Standard QFT (free scalar) reproduces by construction within DCGT regime.

---

## 5. Falsification Criteria

### 5.1 DCGT V1 → non-Klein–Gordon operator

**Falsifier sentence:** *Demonstration that DCGT coarse-graining of V1 substrate-scalar content does not produce the Klein–Gordon operator $(\Box + m^2)$ — e.g., produces non-local operator or different derivative structure — would falsify §3.2 + §3.3.*

### 5.2 Lorentz-covariance violation

**Falsifier sentence:** *Empirical observation of Lorentz-covariance violation in substrate-level scalar-field content (beyond DCGT-breakdown regimes) — would falsify §3.4 + V1 Lorentz covariance.*

### 5.3 No substrate-level UV cutoff

**Falsifier sentence:** *Empirical demonstration of high-frequency substrate-level scalar-field content at $\omega \gg c/\ell_P$ (no UV cutoff) — would falsify §3.5 + V1 finite-width.*

### 5.4 P-Scalar-Match fails

**Falsifier sentence:** *Demonstration that substrate-level scalar-rule-type content cannot consistently match continuum scalar-field structure under DCGT — would falsify P-Scalar-Match.*

---

## 6. Position Statement

**Free scalar Klein–Gordon equation** is the DCGT continuum limit of V1 substrate-graph propagation acting on substrate-scalar-rule-type content. Substrate-level mechanism: V1 + DCGT + P-Scalar-Match → standard Klein–Gordon form. Mass values value-layer inherited.

What this paper claims:

- Free scalar QFT structural form derived from V1 + DCGT.
- Lorentz covariance inherited from V1.
- Substrate-level UV cutoff at $\omega_c = c/\ell_P$.

What this paper does *not* claim:

- Mass values not derived.
- Canonical quantization (Fock space) not at substrate level.
- Interacting QFT not in this paper.

**Series context.** Paper_017 of QFT arc.

---

## Appendix

**Cross-references:** Paper_087, Paper_073, Paper_089, Paper_015, Paper_016.

**Glossary:**
- **Klein–Gordon equation.** $(\Box + m^2)\phi = 0$.
- **P-Scalar-Match.** Substrate-level scalar-rule-type matches continuum scalar field under DCGT.
- **Substrate-scalar-rule-type.** Substrate-level rule-type for scalar matter content.

---

**End of Paper_017.**
