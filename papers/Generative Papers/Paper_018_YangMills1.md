# Paper_018 — Non-Abelian Gauge Generalization (Yang–Mills Arc YM-1)

**Series:** Event Density (ED) Generative Papers — Wave-2 Yang–Mills arc opening
**Author:** Allen Proxmire
**Status:** Publication draft (opens YM arc; cashes Paper_015 P-NonAbelian-Analogy)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qft/Paper_018_YangMills1.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim of full Yang–Mills mass-gap theorem (Clay-relevance) derivation.** This paper opens the YM arc with YM-1; full Clay-relevance synthesis is Paper_023 (in queue).
3. **No claim that the specific Standard-Model gauge group $SU(3) \times SU(2) \times U(1)$ is derived.** This paper supplies the substrate-level non-abelian extension framework; specific empirical gauge groups are inherited (Paper_015 P-NonAbelian-Analogy + value-layer matching).
4. **No claim of OS-positivity proof.** OS-positivity audit is in-queue (Paper_020 in queue).
5. **No claim of confinement / asymptotic-freedom mechanisms.** Substrate-level YM extension to confinement is downstream (Paper_021 in queue).
6. **Paper_015 P-NonAbelian-Analogy is now cashed:** this paper supplies the substrate-level **multi-rule-type composition mechanism** with explicit substrate-graph commutator structure, converting Paper_015's A→analogy row to a **D conditional on new postulates** in this paper.

---

## Abstract

This paper opens the **Yang–Mills arc (YM-1)** by deriving the substrate-level non-abelian gauge extension from Paper_015 T17 (gauge fields as rule-type bundles) + Paper_016 (generalized minimal coupling) + Paper_073 (DCGT) + this paper's **multi-rule-type composition mechanism** with explicit substrate-graph commutator structure.

The substrate-level mechanism (cashing Paper_015 P-NonAbelian-Analogy):

- Multiple substrate gauge rule-types $\tau_a$ ($a = 1, \ldots, N$) compose at substrate-graph level (P10 multi-rule-type primitive).
- Substrate-level polarity-transport for distinct rule-types $\tau_a$ uses distinct $U(1)$ phases $\pi_K^a$, with **non-commuting transport rules** at the substrate-graph level (P-MultiRT-NonCommute, this paper's substrate-level commitment).
- DCGT coarse-graining produces continuum gauge potential $A_\mu = A_\mu^a T^a$ with structure constants $f^{abc}$ inherited from substrate multi-rule-type commutator structure.
- Standard non-abelian Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ with $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu + ig[A^\mu, A^\nu]$ emerges as DCGT continuum limit.

The paper makes no claim of mass-gap theorem (Paper_023 in queue), no claim of confinement (downstream), and no claim of specific empirical gauge groups (Standard Model inherited).

---

## 1. Introduction

### 1.1 What this paper does

Paper_015 introduced T17 + P-NonAbelian-Analogy as a substrate-level analogy for non-abelian gauge content. This paper **cashes P-NonAbelian-Analogy** by supplying the explicit substrate-graph mechanism: **multi-rule-type composition with non-commuting polarity-transport rules**.

### 1.1.1 QFT-arc naming-postulate-chain cross-reference (round-8)

This paper extends the QFT-arc naming-postulate chain referenced in Paper_016 §5.1. The full chain across the QFT arc (Papers_015 + 016 + 017 + 018) operates via approximately 8–9 paper-specific naming/identification/construction postulates:

- **Paper_015:** P-Fiber-Naming, P-Connection-Naming, P-StructureGroup-Naming, P-Bundle-Definition, P-NonAbelian-Analogy.
- **Paper_016:** P-Substrate-Covariant-Derivative-Construction, P-Polarity-Connection-Match.
- **Paper_017:** P-Scalar-Match (+ P-Lorentz-Covariant-Continuum added round-8, see Paper_017 §2).
- **Paper_018 (this paper):** P-MultiRT-Compose, P-MultiRT-NonCommute, P-StructureConstants-Match.

These postulates **collectively relabel standard fiber-bundle gauge theory + Yang–Mills in substrate vocabulary**. The substrate-level mechanism reproduces standard QFT content **by construction** via the naming-postulates; empirical content lives in **DCGT-breakdown regimes** (Paper_073 §7), not at standard QFT scales where the naming-postulates reproduce standard physics by construction.

### 1.2 Arc context

- **Paper_015:** T17 gauge fields + P-NonAbelian-Analogy.
- **Paper_016:** Generalized minimal coupling.
- **Paper_017:** Free scalar QFT.
- **Paper_018 (this paper):** Yang–Mills arc YM-1.
- **Papers_019–022 (in queue):** Substrate→continuum YM limit, OS-positivity, mass gap mechanism.
- **Paper_023 (in queue):** YM Clay-relevance synthesis.

---

## 2. Primitive Inputs

**Substrate primitives:** P02, P05, P07, P09, P10.

**Upstream paper dependencies:** Paper_087, Paper_015 (T17 + P-NonAbelian-Analogy), Paper_016 (minimal coupling), Paper_073 (DCGT), Paper_089 (V1).

**Paper-specific postulates:**

- **P-MultiRT-Compose (Multi-rule-type composition):** *Substrate-level gauge content with $N$ distinct rule-types $\tau_a$ ($a = 1, \ldots, N$) composes at substrate-graph level via parallel substrate channels each carrying a distinct rule-type label.* Substrate-level commitment about how multi-rule-type content is structured (P10 multi-rule-type primitive supplies the rule-type-multiplicity; this postulate specifies the composition rule).

- **P-MultiRT-NonCommute (Non-commuting polarity-transport rules for distinct rule-types):** *Substrate-level polarity-transport for distinct rule-types $\tau_a, \tau_b$ does **not commute** at substrate-graph level: $[U_{\mathrm{transport}}^a, U_{\mathrm{transport}}^b] \neq 0$. The substrate-level commutator structure carries content that DCGT-coarse-grains to standard Lie-algebra structure constants $f^{abc}$.* Substrate-level commitment about how multi-rule-type transport rules relate.

- **P-StructureConstants-Match (Substrate commutator → continuum structure constants):** *The substrate-level commutator structure of multi-rule-type polarity-transport (P-MultiRT-NonCommute) DCGT-coarse-grains to continuum Lie-algebra structure constants $[T^a, T^b] = if^{abc}T^c$ for the empirical gauge group.* Substrate-level identification commitment for gauge-group structure constants.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives + V1 + DCGT + T17 | P / D / I | Paper_087, 089, 073, 015 |
| Paper_015 P-NonAbelian-Analogy | P | Paper_015 §2 |
| Paper_016 generalized minimal coupling (abelian) | D | Paper_016 |
| Multi-rule-type composition | **P (P-MultiRT-Compose)** | §2 substrate-level commitment |
| Non-commuting polarity-transport for distinct rule-types | **P (P-MultiRT-NonCommute)** | §2 substrate-level commitment |
| Substrate-graph commutator structure | **P (postulational consequence of P-MultiRT-NonCommute)** | §3.2 — restates P-MultiRT-NonCommute's content; no additional algebraic derivation step. *(Round-8 relabel per Restated-Postulate Rule.)* |
| Substrate commutator → continuum structure constants | **P (P-StructureConstants-Match)** | §2 substrate-level identification |
| Continuum non-abelian gauge potential $A_\mu = A_\mu^a T^a$ | **P (definitional construction matching standard non-abelian form) under P-StructureConstants-Match + I (DCGT from Paper_073)** | §3.3 — writing $A_\mu = A_\mu^a T^a$ is constructing the standard form via P-StructureConstants-Match identification; DCGT coarse-graining inherited from Paper_073. *(Round-8 relabel: was D, now P-construction + I.)* |
| Continuum field strength $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu + ig[A^\mu, A^\nu]$ | **P (definitional construction matching standard non-abelian field strength) under composed P-postulates** | §3.4 — writing down the standard non-abelian field-strength form is construction, not derivation. The commutator term inherits structure-constant content via P-StructureConstants-Match. *(Round-8 relabel: was D, now P-construction.)* |
| Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ | **P (definitional construction matching standard YM equation) under composed P-postulates + I (Paper_016 minimal coupling)** | §3.5 — YM equation assembled by composing the substrate-level P-postulates with inherited Paper_016 minimal-coupling content. *(Round-8 relabel: was D, now P-construction + I.)* |
| Specific empirical gauge groups | I | Value-layer + Paper_015 P-NonAbelian-Analogy + Standard-Model matching |
| Mass gap | NOT CLAIMED in YM-1 | Paper_021 (in queue) |
| OS-positivity | NOT CLAIMED in YM-1 | Paper_020 (in queue) |

All rows P, D, I, or labeled. **No A (asserted) rows.**

---

## 3. Substrate-Level Non-Abelian Yang–Mills

### 3.1 Multi-rule-type substrate-graph structure

By P10 + P-MultiRT-Compose (§2), substrate-level gauge content with $N$ rule-types $\tau_a$ has $N$-fold substrate-channel structure at each substrate locus:

- Substrate channels $K_a$ ($a = 1, \ldots, N$) at each locus $u$, each labeled by a rule-type $\tau_a$.
- Polarity content $\pi_{K_a}^a(u, t) \in U(1)$ for each rule-type.
- Per-rule-type polarity-transport along chain edges (P05).

### 3.2 Non-commuting substrate commutator structure

By P-MultiRT-NonCommute (§2), for distinct rule-types $a \neq b$:

$$
[U_{\mathrm{transport}}^a(u, u'),\,U_{\mathrm{transport}}^b(u, u')] \neq 0.
$$

The substrate-level commutator $[U^a, U^b]$ has substrate-graph content that depends on **which rule-types are involved** — substrate-level analog of Lie-algebra structure constants.

**Explicit substrate-level form:** for each pair $(a, b)$, the substrate-level commutator at substrate-graph scale gives:

$$
[U_{\mathrm{transport}}^a, U_{\mathrm{transport}}^b] = i\sum_c c_{ab}^c\,U_{\mathrm{transport}}^c \cdot (\text{substrate-scale infinitesimal})
$$

where $c_{ab}^c$ are substrate-level commutator coefficients — substrate-graph content carried in multi-rule-type transport composition.

### 3.3 DCGT continuum limit → non-abelian gauge potential

By Paper_073 DCGT applied to multi-rule-type polarity-transport:

- Substrate channel set $\{K_a\}$ → continuum gauge-algebra basis $\{T^a\}$.
- Per-rule-type polarity-transport coefficient → continuum gauge-potential component $A_\mu^a(x)$.
- Total gauge potential: $A_\mu(x) = A_\mu^a(x)\,T^a$.

By P-StructureConstants-Match (§2): the substrate commutator coefficients $c_{ab}^c$ DCGT-coarse-grain to standard **Lie-algebra structure constants** $f^{abc}$:

$$
[T^a, T^b] = if^{abc}T^c.
$$

For empirical gauge group $G$ (e.g., $SU(N)$), $f^{abc}$ are the standard group-theoretic structure constants. Specific values are inherited (value-layer) — different empirical groups have different structure constants.

### 3.4 Continuum field strength

Standard non-abelian field strength:

$$
\boxed{F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu + ig[A^\mu, A^\nu]}
$$

emerges from substrate-graph multi-rule-type curvature content (non-trivial polarity-transport around closed substrate-graph loops with multiple rule-type labels) under DCGT. The commutator term $[A^\mu, A^\nu]$ encodes the substrate-level non-commutativity from P-MultiRT-NonCommute.

**Coupling constant $g$:** inherited from empirical gauge-coupling values (value-layer; $g_{SU(3)}, g_{SU(2)}, g_{U(1)}$ different for different gauge sectors).

### 3.5 Yang–Mills equation

Combining §3.3 + §3.4 + Paper_016 generalized minimal coupling:

$$
\boxed{D_\mu F^{\mu\nu} = J^\nu}
$$

where $D_\mu = \partial_\mu + ig[A_\mu, \cdot]$ is the non-abelian gauge-covariant derivative + adjoint action on $F$, and $J^\nu$ is the matter-current source.

**This is the standard Yang–Mills equation.** Standard QFT non-abelian-gauge content reproduces under standard QFT machinery operating on this substrate-level-derived continuum theory.

### 3.6 Where the empirical content lives

Following the QFT-arc naming-postulate-chain framing (Paper_016 §5.1):

- Standard Yang–Mills equation reproduces by construction at standard QFT scales — the substrate-level naming postulates (P-NonAbelian-Analogy from Paper_015 + this paper's postulates) are built to match.
- **Empirical wedge** lies in **DCGT breakdown regimes** (Paper_073 §7) — substrate-level departures from standard YM predicted at strong-gradient / near-substrate-scale / near-singularity scales.

---

## 4. Status of Mass Gap, OS-Positivity, Confinement

**Not in this paper.** Paper_018 opens the YM arc with the substrate-level Yang–Mills equation form derivation. Downstream:

- **Paper_019 (in queue):** Substrate→continuum limit refinement (Wilsonian / OS-construction).
- **Paper_020 (in queue):** OS-positivity audit.
- **Paper_021 (in queue):** Mass gap mechanism (V1 second-moment + non-abelian quartic).
- **Paper_022 (in queue):** Gauge-fixing via T17 C8 substrate gauge-quotient.
- **Paper_023 (in queue):** YM Clay-relevance synthesis.

This paper supplies YM-1: the substrate-level YM equation form.

---

## 5. Falsification Criteria

### 5.1 Multi-rule-type composition fails

**Falsifier sentence:** *Empirical demonstration that substrate-level multi-rule-type content cannot consistently compose at substrate-graph level — would falsify P-MultiRT-Compose.*

### 5.2 Substrate-graph commutator structure trivial

**Falsifier sentence:** *Demonstration that multi-rule-type polarity-transport rules commute at substrate-graph level — would falsify P-MultiRT-NonCommute and reduce substrate-level gauge content to abelian-only.*

### 5.3 DCGT does not produce standard YM equation

**Falsifier sentence:** *Demonstration that DCGT coarse-graining of substrate-graph multi-rule-type content does NOT produce the standard Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ — would falsify §3.5 + P-StructureConstants-Match.*

### 5.4 Empirical gauge group not realizable

**Falsifier sentence:** *Demonstration that the Standard-Model gauge group $SU(3) \times SU(2) \times U(1)$ cannot be realized by any consistent substrate-level multi-rule-type composition under P-MultiRT-Compose + P-MultiRT-NonCommute + P-StructureConstants-Match — would falsify the substrate-level YM scope.*

---

## 6. Position Statement

**Yang–Mills YM-1: substrate-level non-abelian gauge generalization** is opened by cashing Paper_015 P-NonAbelian-Analogy into the explicit substrate-graph mechanism: P-MultiRT-Compose + P-MultiRT-NonCommute + P-StructureConstants-Match. Standard Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ emerges via DCGT coarse-graining.

**Empirical content** follows Paper_016 §5.1 framing: standard YM reproduces by construction at standard QFT scales; substrate-level wedge in DCGT-breakdown regimes.

What this paper claims:

- Paper_015 P-NonAbelian-Analogy cashed via explicit substrate-graph multi-rule-type mechanism.
- Standard YM equation form derived via DCGT.
- Specific gauge groups inherited (value-layer).

What this paper does *not* claim:

- Mass gap not derived (Paper_021 in queue).
- OS-positivity not derived (Paper_020 in queue).
- Confinement not derived (downstream).
- Standard-Model gauge group not derived; inherited.

**Series context.** Paper_018 of YM arc. **Opens YM arc.**

---

## Appendix

**Cross-references:** Paper_087, Paper_015, Paper_016, Paper_017, Paper_073, Paper_089.

**Glossary:**
- **Yang–Mills equation.** $D_\mu F^{\mu\nu} = J^\nu$ — non-abelian gauge field equation.
- **P-MultiRT-Compose.** Substrate-level multi-rule-type composition rule.
- **P-MultiRT-NonCommute.** Distinct rule-types' polarity-transport non-commutes at substrate-graph level.
- **P-StructureConstants-Match.** Substrate commutator → continuum Lie-algebra structure constants.

---

**End of Paper_018.**
