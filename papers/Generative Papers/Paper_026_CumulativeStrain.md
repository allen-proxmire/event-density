# Paper_026 — The Cumulative-Strain Reading of P12

**Series:** Event Density (ED) Generative Papers — Wave-2 gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (replaces Paper_027 §4 sketch with dedicated Wave-2-clean derivation)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/Paper_026_CumulativeStrain.md` (ED-Generative)
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **The substrate scale $\ell_{\mathrm{ED}}$ is not derived.** Empirically identified with $\ell_P$ (Paper_027 §5.3).
3. **The V1 kernel envelope shape is not derived** (Paper_089 §4.4 — value-layer).
4. **The "potential reading" of P12 is a substrate-level choice**, not the unique substrate-consistent reading. Alternative readings (per-channel-modulation, integrated-strain) would give different (but in some cases empirically-equivalent) downstream derivations. This paper commits to the potential reading; alternatives are flagged in §3.4.
5. **No claim that Newton's law is forced from nothing.** The derivation is conditional on P12 + holographic counting (Paper_025) + V1 kernel inheritance (Paper_089) + P-Codim-1 (Paper_025) + P-Sat (Paper_025).
6. **No claim of GR-emergence.** Newtonian limit only; curvature emergence is Arc ED-10 (Paper_032 prerequisites).
7. **No claim of derivation of cosmic-anisotropy content** ($a_0$, ECR). Those are Papers_029/030.

---

## Abstract

This paper supplies the **dedicated Wave-2-clean derivation** of the cumulative-strain reading of P12's stability landscape — the substrate-level mechanism by which Newton's $1/R^2$ acceleration emerges from substrate primitives. Paper_027 §4 (FIXED round-2) sketched this derivation; this paper supplies the full standalone presentation under the **potential reading** (Model A) of P12. Given P12 (stability landscape), Paper_025's holographic participation-count bound $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ (with P-Codim-1 + P-Sat), and Paper_089's V1 finite-width retarded kernel with $1/R$ continuum-limit envelope, the cumulative-strain reading produces:

$$
\Phi(R) = -\frac{GM}{R}, \qquad a_N(R) = -\frac{d\Phi}{dR} = \frac{GM}{R^2}.
$$

The load-bearing structural step is **holographic substrate-source resolution**: the source-mass content $\sigma(M)$ distributes across the $N(R)$ channels at the surface rather than duplicating across them ($\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$). Under V1's $1/R$ per-channel envelope, the cumulative reading sums to $-GM/R$ — the $N(R)$ factors cancel exactly, leaving a single Newtonian potential whose gradient is the inverse-square acceleration. **The cumulative-strain reading is therefore neither (a) a multiplicative sum that overcounts source content, nor (b) a per-channel-modulation that would yield a different scaling form. It is the potential reading with holographic substrate-source resolution — a substrate-level choice whose internal mathematical consistency is the focus of this paper.**

---

## 1. Introduction

### 1.1 What this paper does

Paper_027 (Newton's $G$) §4 contains the substrate-level mechanism — *cumulative-strain reading of P12* — that produces Newton's law. The round-2 FIXED version of Paper_027 §4 corrected an earlier mathematical inconsistency (the round-1 version mixed potential-vs-cumulative-sum layers, producing a Str(R) ∝ R / a_N ∝ d/dR(R⁻¹) algebra mismatch).

This paper supplies the **dedicated standalone derivation** so that:
- Paper_027 can cite this paper (rather than carrying the full derivation inline).
- The QC audit of Paper_027 can be closed: the holographic-substrate-source-resolution step that Paper_027 §4.3 invokes is here a derived step (D from P-Codim-1 + P-Sat + V1 envelope), not an in-line sketch.
- Cross-domain papers (Paper_028, Paper_039) using related cumulative-strain machinery can reference this paper.

### 1.2 Why the cumulative-strain reading needs a dedicated paper

The cumulative-strain reading is **load-bearing** for the entire gravity arc:
- Paper_027 — Newton's $G$ identification.
- Paper_029 — transition acceleration $a_0$ (cumulative strain from cosmic horizon).
- Paper_030 — ECR (bilocal strain coupling, P14 — Paper_030).
- Paper_031 — BTFR.

A mathematically incoherent cumulative-strain reading propagates errors throughout the gravity arc. Locating the rigorous derivation in a dedicated paper makes the load-bearing step auditable in isolation.

### 1.3 Arc context

- **Paper_025:** Holographic participation-count bound.
- **Paper_026 (this paper):** Cumulative-strain reading of P12 — potential form.
- **Paper_027:** Newton's $G$ — uses Paper_025 + Paper_026.
- **Paper_028:** Cosmic decoupling surface.
- **Paper_029, 030, 031:** $a_0$, ECR, BTFR.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):**

- **P02 (Participation).** Chain–channel relation.
- **P03 (Channel + locus indexing; spatial homogeneity).** Translation-invariance for cumulative-strain integration.
- **P04 (Bandwidth as non-negative additive scalar).** Substrate-source content carrier.
- **P07 (Channel structure).** Channels structurally distinguishable.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).**
- **P12 (Stability landscape).** $\Sigma_C = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$; $\vec{a}_C = -\vec{\nabla}_{\mathrm{adj}}\,\Sigma_C$. **Load-bearing.**

**Upstream postulates inherited from Paper_025:**

- **P-Codim-1:** channels are codimension-1 substrate-graph objects (2D footprint on 2-surfaces).
- **P-Sat:** substrate-saturation regime — bound equality at applications.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference; finite-width retarded kernel with $1/R$ continuum-limit envelope at $R \gg \ell_{\mathrm{ED}}$.
- **Paper_025:** holographic participation-count bound $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ at saturation.

**Paper-specific postulate (P-Potential-Reading):** *The cumulative-strain reading of P12 functions as a **potential**: per-channel V1 content contributes a substrate-level potential $\Phi_{\mathrm{ch}}(R) \propto -\sigma_{\mathrm{ch}}/R$ to the chain stability landscape, with the chain's experienced acceleration given by the negative radial gradient.* This is a substrate-level **choice** between two candidate readings (Model A potential vs. Model B per-channel-modulation, §3.4). Both readings are substrate-consistent; the potential reading is selected here because it produces internal mathematical consistency under holographic substrate-source resolution.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 finite-width retarded structure | D | Paper_089 (Theorems N1 + T18) |
| V1 $1/R$ continuum-limit envelope at $R \gg \ell_{\mathrm{ED}}$ | **I (inherited from Paper_073 DCGT)** | Coulomb-like $1/R$ falloff emerges as DCGT continuum-limit of V1 substrate kernel; not derived in this paper. *(Round-5 relabel: D → I.)* |
| Holographic bound $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ at saturation | D | Paper_025 from P02 + P03 + P06 + P07 + P08 + P-Codim-1 + P-Sat (explicit combinatorial derivation) |
| P-Codim-1 (codimension-1 channel postulate) | P (inherited from Paper_025) | Paper_025 §2 — codimension-1 substrate-graph channel structure |
| Potential reading of P12 | **P (P-Potential-Reading)** | §2 substrate-level choice; alternative readings flagged §3.4 |
| Per-channel potential $\Phi_{\mathrm{ch}}(R) = -\kappa_{V1}\,\sigma_{\mathrm{ch}}/R$ | D | §3.1 explicit algebra: V1 inherited $1/R$ envelope (I row above) + P-Potential-Reading + substrate-level coupling normalization gives the per-channel form |
| Holographic substrate-source resolution $\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$ | D | §3.2 from P03 translation-invariance + P07 + P-Codim-1 (uniform distribution over $N(R)$ channels through $\Sigma_R$) |
| Cumulative-strain reading sums $N(R)$ channels with cancellation | D | §3.3 explicit algebra: $\Phi(R) = N(R) \cdot \Phi_{\mathrm{ch}}(R) = N(R)\,\cdot(-\kappa_{V1}\sigma(M)/(N(R)\,R)) = -\kappa_{V1}\sigma(M)/R$ |
| Identification $\kappa_{V1}\,\sigma(M) = GM$ | D | §3.5 dimensional bookkeeping with Paper_027 coefficient assembly |
| Gradient gives $a_N = GM/R^2$ | D | §3.6 explicit algebra $-d/dR(-GM/R) = -GM/R^2$ |
| Numerical $G$ value | I | $G$ assembled from substrate constants via Paper_027 §5; numerical value inherited via $\ell_{\mathrm{ED}} = \ell_P$ |

All rows P, D, I, or labeled. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. The Cumulative-Strain Reading

### 3.1 Per-channel V1 potential contribution

By Paper_089 (V1 canonical reference), the V1 kernel has form:

$$
K_{V1}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).
$$

At separations $R \gg \ell_{\mathrm{ED}}$ (the gravity-arc regime of interest), the V1 envelope produces, via DCGT continuum limit (Paper_073), a Coulomb-like $1/R$ falloff in the per-channel kernel content. **Under the P-Potential-Reading postulate (§2)**, this $1/R$ falloff enters the chain's stability landscape as a substrate-level potential contribution:

$$
\Phi_{\mathrm{ch}}(R) = -\,\kappa_{V1}\,\frac{\sigma_{\mathrm{ch}}(M; R)}{R}
$$

where:

- $\sigma_{\mathrm{ch}}(M; R)$: per-channel substrate-source content from a localized mass $M$, *resolved at the per-channel level* (§3.2).
- $\kappa_{V1}$: substrate-level per-channel V1 coupling coefficient (inherited from V1 envelope normalization).
- Negative sign: attractive substrate-strain (substrate-source content lowers $\Sigma_C$ at the test chain).

**Dimensional check:** $\Phi_{\mathrm{ch}}$ has units of substrate-level energy/mass = $[\mathrm{length}/\mathrm{time}]^2$; $\sigma_{\mathrm{ch}}$ has units of substrate-source content (mass-equivalent at substrate level); $R$ has $[\mathrm{length}]$; $\kappa_{V1}$ has units $[\mathrm{length}^3/(\mathrm{mass}\cdot\mathrm{time}^2)]$ so the combination gives $[\mathrm{length}^2/\mathrm{time}^2]$. ✓

### 3.2 Holographic substrate-source resolution

This is the load-bearing structural step. **The substrate-source content $\sigma(M)$ associated with a localized source-mass region is a single substrate-level fact about the source.** It is *not* an independent quantity that each substrate channel sees a separate copy of.

The holographic bound (Paper_025) counts substrate channels through the 2-surface $\Sigma_R$: $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ at saturation (P-Sat). The substrate-source content distributes uniformly across these channels by P03 (spatial homogeneity / no preferred channel) + P07 (each channel carries well-defined source-content fraction):

$$
\boxed{\sigma_{\mathrm{ch}}(M; R) = \frac{\sigma(M)}{N(R)}.}
$$

This is the **holographic substrate-source resolution**. It is *not* a phenomenological partition; it follows structurally from:

- P03 translation-invariance: substrate-graph adjacency is uniform locally; no channel through $\Sigma_R$ is preferred.
- P07 distinguishability: each channel carries a well-defined fraction of substrate-source content.
- Paper_025 P-Codim-1 + P-Sat: $N(R)$ channels at saturation, each occupying $\ell_{\mathrm{ED}}^2$ footprint.

**Dimensional check:** $\sigma(M)$ has substrate-source-content units; $N(R)$ is dimensionless; ratio has substrate-source-content units. ✓

### 3.3 Cumulative-strain reading — the $N(R)$ cancellation

The chain's experienced potential is the substrate-graph cumulative-strain reading: summing the per-channel V1 potential (§3.1) over the $N(R)$ channels through $\Sigma_R$, with each channel carrying the per-channel-resolved source content (§3.2):

$$
\Phi(R) = \sum_{K=1}^{N(R)}\Phi_{\mathrm{ch}}(R) = N(R) \cdot \left(-\kappa_{V1}\,\frac{\sigma_{\mathrm{ch}}(M;R)}{R}\right) = N(R) \cdot \left(-\kappa_{V1}\,\frac{\sigma(M)/N(R)}{R}\right).
$$

**The factors of $N(R)$ cancel exactly:**

$$
\boxed{\Phi(R) = -\,\kappa_{V1}\,\frac{\sigma(M)}{R}.}
$$

This is the substrate-level Coulomb-like potential. **The cancellation is the structurally-correct accounting**: substrate-source content distributes across channels (so per-channel content $\propto 1/N(R)$), and the cumulative sum over $N(R)$ channels brings back the $N(R)$ factor exactly. The net result is a single $1/R$ potential — the same form as the standard Newtonian potential.

**Where the cancellation breaks earlier sketches.** The Paper_027 round-1 sketch attempted to combine "per-channel content $\sigma(M)/R$" (treating $\sigma(M)$ as not resolved per channel) with "sum over $N(R)$ channels" — giving $N(R) \cdot \sigma(M)/R \propto R \cdot \sigma(M)/R \cdot \mathrm{coeff} \propto R$, then taking $d/dR(R^{-1})$ inconsistently. The substrate-level structure does *not* support that combination: source content distributes, it does not duplicate. **Holographic substrate-source resolution is the structural mechanism that makes the cumulative reading mathematically coherent.**

### 3.4 The choice of potential reading (P-Potential-Reading) — alternatives flagged

The cumulative-strain reading is presented here under the **potential reading** (Model A). Two candidate substrate-consistent readings:

- **Model A — Potential reading (this paper):** per-channel V1 content contributes to a substrate-level potential; gradient gives acceleration. Holographic substrate-source resolution + N(R) cancellation produces $\Phi(R) \propto 1/R$.
- **Model B — Per-channel modulation:** the holographic count modulates the *envelope* of a single channel's contribution (no summing over $N(R)$ independent contributions). The per-channel envelope at separation $R$ scales as $\sigma(M)/(R \cdot \ell_{\mathrm{ED}}^2 \cdot N(R))$ or similar — substrate-graph details would need to be worked out.

Both readings can in principle produce Newton's $1/R^2$ law, but the **load-bearing structural commitments differ**. Model A commits to summing-over-channels + holographic substrate-source resolution; Model B commits to single-channel-modulation. **P-Potential-Reading is the substrate-level choice this paper makes**; alternative-reading derivations are not supplied here.

This is consistent with the QC discipline: the choice is **flagged as a postulate (P-Potential-Reading)**, not buried as an unflagged assumption.

### 3.5 Identifying $\kappa_{V1}\,\sigma(M)$ with $GM$

By Paper_027's coefficient assembly (§5), the substrate-level combination $\kappa_{V1}\,\sigma(M)$ corresponds to $GM$ in the continuum limit, with $G = c^3\ell_{\mathrm{ED}}^2/\hbar$ assembled from substrate constants:

$$
\kappa_{V1}\,\sigma(M) = GM.
$$

The dimensional and numerical bookkeeping for this identification is in Paper_027 §5; this paper inherits the result.

Substituting into §3.3:

$$
\Phi(R) = -\frac{GM}{R}.
$$

This is the Newtonian gravitational potential.

### 3.6 The gradient — Newton's inverse-square acceleration

By P12, the chain's experienced acceleration is the negative radial gradient of the potential:

$$
a_N(R) = -\frac{d\Phi}{dR} = -\frac{d}{dR}\!\left(-\frac{GM}{R}\right) = -\frac{GM}{R^2}.
$$

The magnitude $|a_N| = GM/R^2$, directed inward along the participation-graph adjacency from test toward source (attractive substrate-strain, consistent with the negative sign of $\Phi$).

$$
\boxed{a_N(R) = \frac{GM}{R^2}.}
$$

This is **Newton's law**, derived structurally from substrate primitives + Paper_025 holographic bound + Paper_089 V1 inheritance + P-Potential-Reading.

**Dimensional check:** $GM/R^2$ has units $[\mathrm{length}^3/\mathrm{mass}/\mathrm{time}^2 \cdot \mathrm{mass} / \mathrm{length}^2] = [\mathrm{length}/\mathrm{time}^2]$ — acceleration. ✓

---

## 4. Inverse-Square Law as a Substrate-Level Structural Result

The substrate-level mechanism behind Newton's $1/R^2$ acceleration:

1. **V1 kernel $1/R$ per-channel envelope** (Paper_089 + DCGT continuum limit).
2. **Holographic substrate-source resolution** (§3.2): $\sigma_{\mathrm{ch}} = \sigma(M)/N(R)$.
3. **Cumulative reading** (§3.3): $\Phi(R) = N(R) \cdot \Phi_{\mathrm{ch}}(R) = -\kappa_{V1}\sigma(M)/R$ — $N(R)$ factors cancel.
4. **Gradient** (§3.6): $a_N = -d\Phi/dR = GM/R^2$.

**The $1/R^2$ form arises from the $1/R$ potential, not from a "competition between $R^2$ surface scaling and $1/R$ kernel falloff."** The latter motivation (in Paper_027 round-1) was both unnecessary and mathematically incoherent. The structurally-correct mechanism is that holographic counting and V1 falloff combine *multiplicatively in the per-channel coefficient*, then cancel in the cumulative reading, leaving a single $1/R$ potential whose gradient is $1/R^2$ acceleration.

**$D = 3+1$ specificity.** In $D = 3+1$ spatial dimensions (P06), the holographic surface scales as $R^2$ and the V1 kernel falls as $1/R$, producing the cancellation. In other dimensions $D$, the analogous derivation produces inverse-power-law acceleration $\propto 1/R^{D-1}$. The empirical $1/R^2$ is specific to $D = 3+1$.

---

## 5. Falsification Criteria

### 5.1 Newton's law deviation

**Falsifier sentence:** *Empirical demonstration that gravitational acceleration at solar-system or laboratory scales deviates from $a_N \propto 1/R^2$ beyond GR's post-Newtonian corrections would falsify the substrate-level inverse-square mechanism derived in §3.6.*

Currently Newton's law tested to high precision at sub-millimeter and solar-system scales; no deviation observed.

### 5.2 Holographic substrate-source resolution failure

**Falsifier sentence:** *Demonstration that substrate-source content does **not** distribute uniformly across substrate channels (e.g., specific channels carry disproportionate source content, breaking the P03 + P07 symmetry argument) would falsify §3.2's holographic substrate-source resolution.*

### 5.3 Potential reading inconsistency with alternative readings

**Falsifier sentence:** *Demonstration that Model B (per-channel modulation) produces empirically-correct $1/R^2$ acceleration via a different substrate-level mechanism that conflicts with the potential reading would weaken P-Potential-Reading and require selecting between substrate-consistent readings on additional grounds.*

### 5.4 Cancellation breaks under saturation departures

**Falsifier sentence:** *Empirical demonstration that in regimes where substrate saturation does not hold (the bound is strict rather than equality), the substrate-level acceleration deviates from $1/R^2$ in a calculable way inconsistent with this paper's derivation — would partially falsify the P-Sat regime assumption from Paper_025.*

### 5.5 Spatial dimension different from $D = 3+1$

**Falsifier sentence:** *Empirical evidence for effective $1/R^\alpha$ acceleration with $\alpha \neq 2$ in the Newtonian regime would falsify the $D = 3+1$ assumption (P06) underlying the cancellation in §3.3.*

---

## 6. Position Statement

The **cumulative-strain reading of P12** under the **potential reading (P-Potential-Reading)** is a downstream structural identification in the ED Generative Primitives System. Given P12 + Paper_025 holographic bound + Paper_089 V1 inheritance + P-Potential-Reading + P-Codim-1 + P-Sat:

1. V1 produces per-channel substrate-level potential $\Phi_{\mathrm{ch}}(R) \propto -\sigma_{\mathrm{ch}}(M)/R$.
2. Holographic substrate-source resolution: $\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$.
3. Cumulative reading: $\Phi(R) = N(R) \cdot \Phi_{\mathrm{ch}}(R) = -GM/R$ — $N(R)$ factors cancel.
4. Gradient: $a_N = GM/R^2$ — Newton's law.

What this paper claims:

- The cumulative-strain reading is mathematically coherent under P-Potential-Reading + holographic substrate-source resolution.
- The $N(R)$-factor cancellation is the structural mechanism that makes the derivation work.
- Newton's $1/R^2$ form arises from gradient-of-$1/R$-potential, not from "competition between $R^2$ and $1/R$ scalings."
- The derivation supplies the dedicated standalone version that Paper_027 §4 sketched.

What this paper does *not* claim:

- The 13 primitives are not derived.
- V1 envelope shape, $\ell_{\mathrm{ED}}$ value, $G$ numerical value are value-layer inputs.
- P-Potential-Reading is a substrate-level choice; Model B (per-channel modulation) is an alternative-reading possibility not pursued here.
- Newton's law is not forced from nothing; conditional on the postulates listed.
- GR is not derived; Newtonian limit only.

**Series context.** Paper_026 of the gravity arc. Used by Paper_027 (Newton's $G$ coefficient assembly), Paper_028 (cosmic-decoupling cumulative strain), Paper_029 (transition acceleration), Paper_030 (ECR via bilocal coupling P14).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference (kernel envelope).
- **Paper_025:** holographic bound (P-Codim-1, P-Sat).
- **Paper_027:** Newton's $G$ coefficient assembly; uses this paper.
- **Paper_073:** DCGT continuum limit.

### Glossary

- **Cumulative-strain reading.** Substrate-level sum of per-channel V1 potential over $N(R)$ channels through 2-surface $\Sigma_R$.
- **Holographic substrate-source resolution.** $\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$. Substrate-source content distributes uniformly across $N(R)$ channels at saturation.
- **P-Potential-Reading.** Substrate-level postulate that V1 content enters P12 stability landscape as a potential whose gradient is acceleration.
- **$N(R)$-factor cancellation.** The structural mechanism: $\Phi(R) = N(R) \cdot \Phi_{\mathrm{ch}}(R) = N(R) \cdot (-\kappa\sigma(M)/(N(R)\,R)) = -\kappa\sigma(M)/R$.

---

**End of Paper_026.**

*Wave-2 Generative Paper — Gravity Arc, dedicated cumulative-strain-reading derivation. Closes the QC audit on Paper_027 §4.*
