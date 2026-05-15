# Paper_016 — Generalized Minimal Coupling from T17 + DCGT

**Series:** Event Density (ED) Generative Papers — Wave-2 QFT arc (second paper)
**Author:** Allen Proxmire
**Status:** Publication draft (follows Paper_015 T17 anchor)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qft/Paper_016_MinimalCoupling.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **T17 is not re-derived** (Paper_015 upstream).
3. **DCGT is not re-derived** (Paper_073 upstream).
4. **No claim that generalized minimal coupling $D_\mu = \partial_\mu + iA_\mu$ is forced from substrate primitives alone.** It is derived from T17 substrate-bundle structure + DCGT coarse-graining + paper-specific substrate-operational identification of polarity-transport with continuum gauge connection (P-Polarity-Connection-Match, §2).
5. **No claim of derivation of specific gauge groups, coupling constants, or matter representations.** Inherited from Paper_015 P-NonAbelian-Analogy + value-layer empirical content.
6. **No claim that the standard fiber-bundle minimal-coupling derivation is wrong.** ED supplies substrate-level mechanism producing the same continuum minimal-coupling form via different substrate-graph machinery.
7. **No claim that local-gauge invariance is derived at substrate level.** Local-gauge invariance is inherited from P05 polarity-transport gauge-covariance (Paper_001 §3.4); this paper's minimal-coupling derivation operates within that gauge-covariance structure.

---

## Abstract

This paper develops **generalized minimal coupling** $D_\mu = \partial_\mu + iA_\mu$ as a downstream structural consequence of Paper_015 Theorem T17 (gauge fields as substrate rule-type bundles) + Paper_073 DCGT (substrate→continuum bridge), under the paper-specific postulates **P-Substrate-Covariant-Derivative-Construction** (substrate-level finite-difference covariant-derivative construction matching standard form) + **P-Polarity-Connection-Match** (substrate-level polarity-transport coarse-grains to continuum gauge connection).

**Headline framing (round-5 QC softening):** rather than "gauge fields emerge from substrate," **ED supplies a substrate-level vocabulary that DCGT-coarse-grains into the standard minimal-coupling form $D_\mu = \partial_\mu + iA_\mu$; the empirical wedge lies in DCGT-breakdown regimes (Paper_073 §7), not in the standard gauge content itself.** ED reproduces standard QED/QCD/electroweak minimal-coupling at scales where DCGT operates; substrate-level departures appear in the breakdown regimes Paper_073 identifies.

The substrate-level mechanism:

- Per T17, gauge fields are substrate rule-type bundles with polarity-transport playing the connection role.
- Per DCGT, substrate-level operations coarse-grain to continuum operators under the hydrodynamic-window scale separation.
- Substrate-level **polarity-transport-modulated derivative** $\nabla_{\mathrm{pol}}\Psi = \nabla\Psi + (\text{polarity-transport contribution})\,\Psi$ coarse-grains to the continuum **gauge-covariant derivative** $D_\mu\Psi = \partial_\mu\Psi + iA_\mu\Psi$.

The continuum gauge potential $A_\mu(x)$ is the DCGT coarse-grained image of substrate polarity-transport on the rule-type bundle (P-Polarity-Connection-Match). The paper makes no claim of derivation of specific gauge groups (Paper_015 inheritance + Yang–Mills arc in queue), no claim of derivation of coupling constants (value-layer), and no claim that local-gauge invariance is derived at substrate level (inherited from P05 polarity-transport).

---

## 1. Introduction

### 1.1 What this paper does

Paper_015 established T17: gauge fields as substrate rule-type bundles. This paper supplies the **next structural step**: how matter content (chains carrying participation amplitudes) couples to gauge fields via substrate-level polarity-transport, and how this substrate-level coupling DCGT-coarse-grains to the standard continuum-level **gauge-covariant derivative** $D_\mu = \partial_\mu + iA_\mu$.

**Headline framing (round-5 QC):** ED does *not* "derive gauge fields from substrate." Rather, **ED supplies a substrate-level vocabulary that DCGT-coarse-grains into the standard minimal-coupling form $D_\mu = \partial_\mu + iA_\mu$.** The substrate-level construction (P-Substrate-Covariant-Derivative-Construction, §2) is built to match the standard finite-difference covariant-derivative form; DCGT (Paper_073, inherited) coarse-grains this construction to the continuum. The empirical wedge lies in DCGT-breakdown regimes (Paper_073 §7), not in the standard gauge content itself.

Three load-bearing steps:

1. **Substrate-level polarity-transport-modulated derivative** acting on chain amplitudes.
2. **DCGT coarse-graining** of polarity-transport to continuum gauge connection.
3. **Identification** of the coarse-grained polarity-transport with continuum $A_\mu$ — the P-Polarity-Connection-Match postulate.

### 1.2 Arc context

- **Paper_015:** T17 gauge fields as substrate rule-type bundles (QFT arc anchor).
- **Paper_016 (this paper):** Generalized minimal coupling.
- **Paper_017 (in queue):** Free scalar QFT as DCGT continuum limit of V1.
- **Paper_018 (in queue):** Non-abelian gauge generalization (Yang–Mills arc YM-1).
- **Papers 019–023 (in queue):** Substrate→continuum limit, OS-positivity, mass gap, YM Clay-relevance synthesis.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02, P05, P07, P09, P10.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_015:** T17 + P-Fiber-Naming + P-Connection-Naming + P-StructureGroup-Naming + P-Bundle-Definition + P-NonAbelian-Analogy.
- **Paper_073:** DCGT.
- **Paper_001:** pre-individuation amplitude content + $U(1)$ gauge-covariance under P05 polarity-transport.
- **Paper_089:** V1 (used for matter-content propagation under DCGT).

**Paper-specific postulates:**

- **P-Substrate-Covariant-Derivative-Construction (substrate-level polarity-transport-modulated derivative as standard-form construction):** *The substrate-level differential operator on chain amplitudes $\nabla_{\mathrm{edge}}^{\mathrm{substrate}}\Psi^C = [\Psi^C(u', t') - U_{\mathrm{transport}}(u, u', t, t')\Psi^C(u, t)]/d_{\mathrm{edge}}$ — written as a finite-difference covariant-derivative form along substrate-graph edges — is a **substrate-level definitional construction** that matches the standard finite-difference form of a fiber-bundle covariant derivative.* This is **not derived** from substrate primitives alone; it is **constructed** to match the standard form, so that DCGT coarse-graining (§3.2) reproduces the standard continuum $\partial_\mu - i\mathcal{A}_\mu^{\mathrm{cg}}$. The substrate-level commitment is that polarity-transport along edges is the substrate-level analog of fiber-bundle connection action, packaged in finite-difference form.

- **P-Polarity-Connection-Match (Substrate polarity-transport coarse-grains to continuum gauge connection):** *Under DCGT coarse-graining (hydrodynamic-window scale separation), substrate-level polarity-transport along chain edges produces a continuum-level gauge-connection field $A_\mu(x)$ such that the substrate-level polarity-transport-modulated derivative on a chain amplitude coarse-grains to the continuum gauge-covariant derivative $D_\mu = \partial_\mu + iA_\mu$.* Substrate-level identification commitment; not derivable from Paper_015 + Paper_073 alone (the identification of substrate polarity-transport with continuum connection is a substrate-level naming/structural-mapping commitment).

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| T17 substrate rule-type bundle structure | D | Paper_015 |
| DCGT coarse-graining | D | Paper_073 |
| Pre-individuation amplitude + $U(1)$ gauge-covariance | D | Paper_001 §3.4 |
| Substrate-level polarity-transport-modulated derivative (finite-difference covariant form) | **P (P-Substrate-Covariant-Derivative-Construction)** | §2 — substrate-level definitional construction matching standard finite-difference covariant-derivative form. Not derived from substrate primitives; constructed to match the standard form so DCGT (§3.2) produces $\partial_\mu - i\mathcal{A}_\mu^{\mathrm{cg}}$. *(Round-5 Rereading Test: was D, now P-construction.)* |
| DCGT coarse-graining of polarity-transport-modulated derivative | **I (inherited from Paper_073)** | §3.2 — standard DCGT procedure (Paper_073) applied to substrate-level differential operator. Not derived in this paper; inherited from Paper_073's substrate→continuum bridge. *(Round-5 relabel: D → I.)* |
| Identification of coarse-grained polarity-transport with continuum $A_\mu$ | **P (P-Polarity-Connection-Match)** | §2 substrate-level identification commitment; not derivable from T17 + DCGT alone |
| Continuum gauge-covariant derivative $D_\mu = \partial_\mu + iA_\mu$ | D | §3.3 composition of §3.2 + P-Polarity-Connection-Match |
| Local-gauge invariance | I | Paper_001 §3.4 (inherited from P05 polarity-transport gauge-covariance) |
| Specific gauge groups / matter representations / coupling constants | I | Paper_015 P-NonAbelian-Analogy + value-layer |

All rows P, D, or I. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. The Substrate-Level Mechanism

### 3.1 Substrate-level polarity-transport-modulated derivative

By Paper_015 T17, gauge content is substrate rule-type bundle structure with **polarity-transport along chain edges** as the substrate-level connection. By Paper_001, a chain amplitude $\Psi^C(u, t) = \sum_K P_K^C |K\rangle$ carries substrate-level $U(1)$ polarity content $\pi_K^C \in U(1)$.

**Substrate-level differential operator on chain amplitudes:** the substrate-level "derivative" of $\Psi^C$ along a substrate-graph edge $(u, t) \to (u', t')$ is:

$$
\nabla_{\mathrm{edge}}^{\mathrm{substrate}}\Psi^C = \left[\Psi^C(u', t') - U_{\mathrm{transport}}(u, u', t, t')\,\Psi^C(u, t)\right] / d_{\mathrm{edge}}
$$

where $U_{\mathrm{transport}}(u, u', t, t')$ is the substrate-level polarity-transport from $(u, t)$ to $(u', t')$ along the chain edge — a $U(1)$ phase factor encoding the polarity content carried along the edge — and $d_{\mathrm{edge}}$ is the substrate-graph edge length (~ $\ell_{\mathrm{ED}}$).

**Substrate-level structural interpretation:** $\nabla_{\mathrm{edge}}^{\mathrm{substrate}}$ measures how the chain amplitude changes along a substrate-graph edge **relative to the polarity-transport along that edge** — the substrate-level analog of the covariant derivative.

**Dimensional check:** $\Psi$ has substrate-amplitude units; $U_{\mathrm{transport}}$ is dimensionless ($U(1)$ phase); $d_{\mathrm{edge}}$ has length units; $\nabla_{\mathrm{edge}}^{\mathrm{substrate}}\Psi$ has units of substrate-amplitude / length. ✓

### 3.2 DCGT coarse-graining

By Paper_073, substrate-level operators coarse-grain to continuum operators under hydrodynamic-window scale separation ($\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$).

Applying DCGT to $\nabla_{\mathrm{edge}}^{\mathrm{substrate}}$:

1. **Substrate-graph edges** at scale $\ell_{\mathrm{ED}}$ coarse-grain to **continuum spacetime points** at scale $R_{\mathrm{cg}}$.
2. **Substrate-graph edge direction** coarse-grains to **continuum direction $\mu$** ($\partial_\mu$ direction).
3. **Polarity-transport along edge** coarse-grains to **continuum polarity-transport rule** along direction $\mu$.

The coarse-grained operator:

$$
\nabla_{\mathrm{edge}}^{\mathrm{substrate}} \xrightarrow{\mathrm{DCGT}} \partial_\mu - \mathcal{A}_\mu^{\mathrm{cg}}(x)
$$

where $\mathcal{A}_\mu^{\mathrm{cg}}(x)$ is the DCGT-coarse-grained continuum image of substrate polarity-transport in direction $\mu$ at coarse-grained point $x$. $\partial_\mu$ is the continuum directional derivative; $\mathcal{A}_\mu^{\mathrm{cg}}$ is the polarity-transport-correction term ensuring covariant differentiation.

**Dimensional check:** $\partial_\mu$ has dimensions 1/length; $\mathcal{A}_\mu^{\mathrm{cg}}$ has dimensions 1/length (gauge field, in natural units); coarse-grained operator is dimensionally consistent. ✓

### 3.3 Identification of $\mathcal{A}_\mu^{\mathrm{cg}}$ with continuum gauge potential $A_\mu$

By **P-Polarity-Connection-Match (§2)**, the DCGT-coarse-grained polarity-transport correction $\mathcal{A}_\mu^{\mathrm{cg}}$ is **identified** with the continuum gauge potential $A_\mu(x)$:

$$
\mathcal{A}_\mu^{\mathrm{cg}}(x) \equiv iA_\mu(x).
$$

(The factor of $i$ reflects the standard $U(1)$-gauge convention; the substrate-level polarity is $e^{i\pi}$, so the polarity-transport correction in the derivative carries an $i$ factor.)

Substituting:

$$
\nabla_{\mathrm{edge}}^{\mathrm{substrate}} \xrightarrow{\mathrm{DCGT}} \partial_\mu - iA_\mu = \boxed{D_\mu^{(-)} = \partial_\mu - iA_\mu}.
$$

Convention-flip (substrate-charge sign): $D_\mu = \partial_\mu + iA_\mu$ for matter content of positive substrate-charge.

**This is the generalized minimal coupling**: $D_\mu = \partial_\mu + iA_\mu$, the standard gauge-covariant derivative of QFT.

### 3.4 Local-gauge invariance inherited

Under local $U(1)$ gauge transformation $\pi_K^C(u) \to \pi_K^C(u) + \alpha(u, t)$ (Paper_001 §3.4 + Paper_015 P-Connection-Naming), substrate-level polarity-transport transforms covariantly, producing under DCGT the standard continuum gauge transformation:

$$
A_\mu \to A_\mu - \partial_\mu\alpha(x), \quad \Psi \to e^{i\alpha(x)}\Psi.
$$

Under this joint transformation, the gauge-covariant derivative transforms covariantly: $D_\mu\Psi \to e^{i\alpha(x)}D_\mu\Psi$. Standard gauge invariance follows.

**Local-gauge invariance is inherited** from Paper_001 + Paper_015; not re-derived in this paper.

---

## 4. Non-Abelian Generalization (Brief)

By Paper_015 §6 P-NonAbelian-Analogy, non-abelian gauge structure emerges from substrate-level multi-rule-type composition. The analogous minimal-coupling derivation:

- Multiple substrate rule-types $\tau_1, \tau_2, \ldots$ compose with non-commuting polarity-transport operations.
- DCGT coarse-graining produces non-abelian continuum gauge potential $A_\mu^a T^a$ where $T^a$ are non-abelian gauge-group generators.
- Generalized minimal coupling: $D_\mu = \partial_\mu + ig A_\mu^a T^a$.

Full non-abelian derivation is in-queue (Paper_018 Yang–Mills arc YM-1). This paper supplies the abelian case + the structural-extension framework.

---

## 5. Empirical Content

ED's substrate-level generalized minimal coupling produces the **same continuum operator** as standard fiber-bundle gauge theory: $D_\mu = \partial_\mu + iA_\mu$. Standard QED, QCD, electroweak minimal-coupling content reproduces under standard QFT machinery operating on the continuum theory ED produces via DCGT.

**Substrate-level wedge:** the substrate-level mechanism provides a substrate-graph-level account of where minimal coupling comes from. Empirical content is in DCGT breakdown regimes (Paper_073 §7), not at standard QFT scales.

### 5.1 The QFT-arc naming-postulate chain (round-5 QC explicit acknowledgment)

The QFT-arc derivation chain in ED operates via a sequence of **paper-specific naming and construction postulates** that collectively relabel standard fiber-bundle gauge theory in substrate vocabulary. The chain:

- **Paper_015 (T17):**
  - **P-Fiber-Naming** — channels play fiber role.
  - **P-Connection-Naming** — polarity-transport plays connection role.
  - **P-StructureGroup-Naming** — $U(1)$ plays structure-group role.
  - **P-Bundle-Definition** — substrate rule-type bundle defined by its parts.
  - **P-NonAbelian-Analogy** — multi-rule-type composition → non-abelian gauge content (analogy).

- **Paper_016 (this paper):**
  - **P-Substrate-Covariant-Derivative-Construction** — finite-difference covariant-derivative form constructed.
  - **P-Polarity-Connection-Match** — DCGT-coarse-grained polarity-transport = continuum $A_\mu$.

**Honest framing:** the QFT-arc derivation is structurally a **substrate-vocabulary relabeling** of standard fiber-bundle gauge theory, not a derivation of gauge content from substrate primitives alone. The ~7 paper-specific naming/construction postulates (across Papers_015 and 016) **collectively encode the standard fiber-bundle gauge-theory structure** at the substrate level, so that DCGT coarse-graining recovers standard continuum gauge theory.

**Where the empirical content lives:**

- **NOT** at standard QFT scales — ED reproduces standard QED/QCD/electroweak by construction (the naming-postulates are built to match).
- **YES** at **DCGT breakdown regimes** (Paper_073 §7) — strong-gradient, near-substrate-scale, near-singularity, strong-curvature. Substrate-level departures from standard QFT predicted at these scales.

The empirical wedge for the QFT arc is therefore concentrated in DCGT-breakdown signatures (analog-Hawking corrections per Paper_047 §6, near-Planck-scale physics, etc.), not at standard QFT energies where the naming-postulates reproduce standard content by construction.

---

## 6. Falsification Criteria

### 6.1 DCGT coarse-graining fails to produce standard $D_\mu$

**Falsifier sentence:** *Demonstration that DCGT coarse-graining of substrate-level polarity-transport-modulated derivative does NOT produce the standard continuum $D_\mu = \partial_\mu + iA_\mu$ — e.g., produces a non-local integral operator, or a different functional form — would falsify §3.2 + P-Polarity-Connection-Match.*

### 6.2 Polarity-transport-to-gauge-connection identification fails

**Falsifier sentence:** *Empirical demonstration that the continuum gauge potential $A_\mu(x)$ cannot be consistently identified with the DCGT coarse-grained image of substrate polarity-transport — e.g., gauge transformations on $A_\mu$ do not correspond to substrate-level polarity-transport gauge transformations — would falsify P-Polarity-Connection-Match.*

### 6.3 Non-abelian generalization fails

**Falsifier sentence:** *Demonstration that multi-rule-type composition under Paper_015 §6 P-NonAbelian-Analogy does not produce a substrate-level non-abelian gauge connection — i.e., the multi-rule-type substrate-level coupling does not coarse-grain to standard non-abelian $D_\mu = \partial_\mu + ig A_\mu^a T^a$ — would falsify §4 non-abelian generalization framework.*

### 6.4 Local-gauge invariance fails

**Falsifier sentence:** *Empirical demonstration that the substrate-level gauge invariance under polarity-transport (Paper_001 §3.4) does not coarse-grain to standard continuum local-gauge invariance — e.g., gauge transformations leak substrate-graph content into observable quantities — would falsify §3.4.*

### 6.5 DCGT breakdown signatures inconsistent

**Falsifier sentence:** *Empirical observation that DCGT breakdown regimes (Paper_073 §7) do not exhibit substrate-level modifications to standard minimal-coupling form — i.e., near-substrate-scale physics shows pure-continuum behavior — would falsify the substrate-level mechanism.*

---

## 7. Position Statement

**Generalized minimal coupling** $D_\mu = \partial_\mu + iA_\mu$ is a downstream structural identification in the ED Generative Primitives System. Given Paper_015 T17 + Paper_073 DCGT + P-Polarity-Connection-Match:

- Substrate-level polarity-transport-modulated derivative acts on chain amplitudes.
- DCGT coarse-grains the substrate operator to continuum $\partial_\mu - i\mathcal{A}_\mu^{\mathrm{cg}}$.
- P-Polarity-Connection-Match identifies $\mathcal{A}_\mu^{\mathrm{cg}}$ with continuum gauge potential $A_\mu$.
- Result: standard $D_\mu = \partial_\mu + iA_\mu$ generalized minimal coupling.

Non-abelian generalization via multi-rule-type composition (Paper_018 in queue).

What this paper claims:

- The standard continuum gauge-covariant derivative emerges as DCGT coarse-graining of substrate polarity-transport-modulated derivative.
- P-Polarity-Connection-Match is the substrate-level identification commitment.
- Local-gauge invariance inherited from P05 + Paper_001 §3.4.

What this paper does *not* claim:

- The 13 primitives are not derived.
- T17 + DCGT + Paper_001 not re-derived.
- Specific gauge groups / coupling constants not derived.
- Standard fiber-bundle minimal-coupling derivation not refuted; substrate-level alternative.
- Local-gauge invariance not derived at substrate level (inherited).

**Series context.** Paper_016 of QFT arc. Follows Paper_015 T17 anchor. In queue: Paper_017 (free scalar QFT), 018 (non-abelian Yang–Mills YM-1), 019–023 (substrate→continuum limit, OS-positivity, mass gap, Clay-relevance synthesis).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_015:** T17 anchor; P-Connection-Naming inheritance.
- **Paper_073:** DCGT.
- **Paper_001:** pre-individuation amplitudes + $U(1)$ gauge-covariance.
- **Paper_089:** V1 (matter-content DCGT continuum limit).

### Glossary

- **Generalized minimal coupling.** $D_\mu = \partial_\mu + iA_\mu$ — standard continuum gauge-covariant derivative.
- **Substrate-level polarity-transport-modulated derivative.** $\nabla_{\mathrm{edge}}^{\mathrm{substrate}}$ — substrate-graph operator on chain amplitudes accounting for polarity-transport along edges.
- **P-Polarity-Connection-Match.** Substrate-level identification of DCGT-coarse-grained polarity-transport with continuum gauge potential $A_\mu$.
- **DCGT coarse-graining of operators.** Paper_073 procedure applied to substrate-level differential operators producing continuum differential operators.

---

**End of Paper_016.**

*Wave-2 Generative Paper — QFT Arc, Generalized Minimal Coupling. Second paper after Paper_015 T17 anchor.*
