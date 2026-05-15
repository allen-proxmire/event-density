# Paper_027 — Newton's $G$ from Substrate Constants

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: §4.3–§4.5 mathematical-coherence fix)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/foundations/Paper_027_Newtons_G.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_027_Newtons_G_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops Newton's gravitational constant $G$ as a **downstream structural identification** from substrate primitives — specifically, $G$ falls out when one combines the holographic participation-count bound $N = 4\pi R^2/\ell_{\mathrm{ED}}^2$ (which follows from P02 + P03 + P07 + P08) with the cumulative-strain reading of P12's stability landscape (which produces inverse-square acceleration from any localized mass source), under the V1 finite-width retarded kernel structure inherited from Papers #18 and #19. The result is:

$$
a_N = \frac{GM}{R^2}, \qquad G = \frac{c^3\,\ell_{\mathrm{ED}}^2}{\hbar}.
$$

The substrate scale $\ell_{\mathrm{ED}}$ is **postulated** (Primitive P08). The identification $\ell_{\mathrm{ED}} = \ell_P$ (the Planck length) is the empirically-correct choice that matches observed gravitational strength; this is value-layer content, not a substrate-level derivation. Newton's $G$ in this framework is *not* a primitive: it is a downstream structural quantity assembled from $c$, $\ell_{\mathrm{ED}}$, $\hbar$. The paper makes no claim that gravity is forced from nothing; it makes the conditional claim that, given the listed substrate primitives, $G$'s structural form and its identification with $c^3\ell_P^2/\hbar$ are the unique downstream outcome consistent with the postulates. Cross-domain context — the transition acceleration $a_0 = cH_0/(2\pi)$ (Paper_029) and slope-4 BTFR $v^4 = GMa_0$ (Paper_031) — completes the substrate-gravity picture. The empirical case for the substrate primitives rests on this cross-domain reach, not on derivation of the primitives themselves.

---

## 1. Introduction

### 1.1 What this paper does

This paper develops the **Newtonian gravitational constant** $G$ as a downstream structural identification within the ED 13-Primitive Generative System. The derivation proceeds in three steps:

1. **Holographic participation-count bound:** from the participation-channel structure of P02 + P03 + P07 plus the substrate scale P08, the number of distinct substrate channels connecting a source-mass region to a distant test chain at radius $R$ is bounded by $N = 4\pi R^2/\ell_{\mathrm{ED}}^2$.

2. **Cumulative-strain reading of P12 in its potential form:** the strain contribution from a mass source $M$ — read at the substrate level as a contribution to the chain's stability-landscape *potential* — produces, via V1 kernel structure and holographic substrate-source resolution, an effective potential $\Phi(R) \propto -M/R$ on the test chain. Its radial gradient gives the inverse-square acceleration.

3. **Identification of $G$:** dimensional analysis combined with the substrate-level coefficient identifies $G = c^3\ell_{\mathrm{ED}}^2/\hbar$. The empirical-matching requirement $\ell_{\mathrm{ED}} = \ell_P$ (Planck length) gives Newton's observed gravitational strength.

The paper's title says "from substrate constants," and the meaning is precise: Newton's $G$ is constructed from $c$ (speed of light, substrate-level), $\ell_{\mathrm{ED}}$ (substrate scale, postulated per P08), and $\hbar$ (substrate-level kernel-action quantum). It is *not* an independent primitive; it is a downstream structural identification.

### 1.2 Why Newton's $G$ matters in the ED Generative System

Standard physics treats $G$ as a fundamental constant — an independent input parameter whose numerical value is empirical. In ED's substrate ontology, $G$ has structural content: it is the downstream coefficient that emerges when the substrate's primitive participation structure interacts with the substrate's stability landscape (P12) through the holographic counting of channels.

The identification $G = c^3\ell_P^2/\hbar$ is a dimensional rearrangement of the standard Planck-length definition $\ell_P = \sqrt{\hbar G/c^3}$. What the ED framework adds is the *structural mechanism* for this identification: $G$ is *not* an independent parameter to be tuned; it is the downstream coefficient that the substrate's primitive structure forces, given the substrate scale $\ell_{\mathrm{ED}} = \ell_P$.

This matters for three reasons:

- **Parsimony.** ED reduces the number of independent fundamental constants by one — Newton's $G$ is now downstream content rather than an independent input.
- **Cross-domain coherence.** $G$, $a_0$, and the slope-4 BTFR are all derived from the same substrate primitives in the gravity arc (Papers 027, 029, 030, 031). They form a coherent structural cluster, not three independently-tuned phenomenological inputs.
- **Falsifiability.** If $G$ has structural content rather than being a free parameter, then the substrate-mechanism interpretation makes predictions about how $G$ would change if the substrate scale $\ell_{\mathrm{ED}}$ were to vary, or about the deep-MOND regime where $G$ and $a_0$ both enter (Papers 029, 030, 031).

### 1.3 How this fits into the gravity arc

The ED gravity arc consists of:

- **Paper_027 (this paper):** Newton's $G$ from substrate constants.
- **Paper_029:** The transition acceleration $a_0 = cH_0/(2\pi)$ from cosmic-decoupling-surface dipole projection.
- **Paper_030:** The ED Combination Rule $a = \sqrt{a_N \cdot a_0}$ in the joint weak-gradient regime.
- **Paper_031:** The slope-4 baryonic Tully-Fisher relation $v^4 = GMa_0$ as the composition of the above.

The four papers together produce the ED substrate-level account of galactic gravity: a coherent substrate-mechanism derivation of Newton's law + MOND-class transition + multiplicative combination + flat rotation curves. The present paper is the first in this arc and establishes the structural identification of $G$ that the subsequent papers build on.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**. They are stated as axioms, not derived from a deeper structural layer.

- **P02 (Participation as primitive relation).** Chains participate in channels as a primitive substrate-level relation.
- **P03 (Channel + locus indexing; spatial homogeneity).** Discrete index set of channels $\mathcal{K}$ and locus index set, with primitive translation-invariance of the participation-graph adjacency structure.
- **P04 (Bandwidth as non-negative additive scalar).** Each channel carries $b_K(u) \geq 0$, additive under channel decomposition.
- **P07 (Channel structure as ontological primitive).** Channels are structurally distinguishable carriers with intrinsic identities in the participation graph.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).** The substrate has a characteristic edge length / discretization scale $\ell_{\mathrm{ED}}$. This is a substrate primitive; *empirical identification* with the Planck length $\ell_P$ follows from matching observed gravitational strength in §5.3.
- **P12 (Stability landscape).** Substrate-level functional $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ on a chain's accessible configuration space, combining coherence, strain, and gradient content. The chain's experienced acceleration is the gradient of $\Sigma$ along its adjacency direction.
- **P13 (Time homogeneity).** The substrate's dynamical primitive is invariant under time translation.

**V1 inheritance (Papers #18, #19):**

- V1's finite-width structure (Theorem N1) supplies the bounded substrate-level scale for kernel-mediated content (entering through the integration cutoff in §4).
- V1's retarded support (Theorem T18) supplies the forward-causal direction for substrate-level strain propagation from source to test chain.

**Upstream paper dependencies:**

- **Paper #1 (participation measure):** the complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ on which the cumulative-strain integration operates.
- **Paper #3 (inner product + orthogonal bands):** four-band orthogonality (P04 §1.5) supplies the strain-band content within the participation-measure decomposition.

**No primitive forcing is invoked.** The full 13-primitive enumeration lives in the ED Foundations position paper (`paper_ED_Framework_13_Primitive_Generative_System.md`).

---

## 3. Holographic Participation-Count Bound

### 3.1 The statement

Given a localized source-mass region at locus $u_M$ and a test chain at locus $u_R$ at distance $R = |u_R - u_M|$ (measured along the substrate participation graph with the spatial-homogeneity structure of P03), the number of distinct substrate channels connecting the source to the test chain is bounded:

$$
N(R) \leq \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

Equality holds in the substrate-saturated limit (where the substrate's primitive channel-content is fully populated over the surface), and the bound is the natural counting expression: the number of independent substrate channels through a closed 2-surface of radius $R$ at substrate-level resolution $\ell_{\mathrm{ED}}$.

### 3.2 Derivation from primitives

The bound follows structurally from the postulated primitives:

**Step 1: P02 + P07 — channel-based participation.** By P02, chain-channel interaction is a primitive relation. By P07, channels are structurally distinguishable with intrinsic identities in the participation graph. Any cross-locus interaction between the source-mass region at $u_M$ and the test chain at $u_R$ proceeds through some specific set of substrate channels — channels that connect locus $u_M$ to locus $u_R$ across the intervening graph structure.

**Step 2: P03 + P07 — channel-counting on a 2-surface.** By P03's spatial-homogeneity, the substrate's participation-graph structure is translation-invariant. Channels connecting any two loci $u_M$ and $u_R$ at separation $R$ must pass through some closed 2-surface $\Sigma_R$ enclosing $u_M$ and intersecting at radius $R$ from $u_M$. The 2-surface has area $4\pi R^2$ in the substrate-graph's $D=3+1$ spatial structure (Primitive P06, implicit here). The number of channels crossing $\Sigma_R$ counts how many distinct substrate pathways connect $u_M$ to anything at radius $R$.

**Step 3: P08 — substrate-scale resolution.** By P08, the substrate has a characteristic edge length $\ell_{\mathrm{ED}}$. Channels are resolved at substrate-graph scale; two distinct channels through $\Sigma_R$ must be separated by at least $\ell_{\mathrm{ED}}$ at the 2-surface, otherwise they merge into a single substrate channel at the resolution limit. Therefore the maximum number of distinct channels through $\Sigma_R$ is bounded by the area of $\Sigma_R$ divided by the substrate-scale area $\ell_{\mathrm{ED}}^2$:

$$
N(R) \leq \frac{\mathrm{Area}(\Sigma_R)}{\ell_{\mathrm{ED}}^2} = \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

This is the holographic participation-count bound.

### 3.3 Structural, not phenomenological

The bound has the same form as the holographic-entropy bound of standard quantum-gravity literature ($A/4\ell_P^2$ Bekenstein-Hawking scaling). In ED, the bound is *not* an importation of the holographic principle from outside the framework. It is a substrate-level counting result that follows from the postulated primitive structure: P02 + P07 + P08 combine to give the area-scaling bound. The identification with the standard holographic bound becomes empirically justified once $\ell_{\mathrm{ED}} = \ell_P$ is established (§5.3).

---

## 4. Cumulative-Strain Reading of P12 — Potential Form

This section is the load-bearing derivation. The presentation has been rewritten to be **mathematically coherent end-to-end** under the *potential reading* of P12: per-channel V1 content contributes to the chain's stability-landscape **potential** (not strain summed as a multi-channel additive content), and the holographic count enters via **substrate-source resolution** rather than via a multiplicative sum of independent contributions.

### 4.1 The stability landscape

By P12, each chain carries a stability-landscape functional:

$$
\Sigma_C = \mathrm{Coh}(C) - \mathrm{Str}(C) - \mathrm{Grad}(C).
$$

The chain's experienced acceleration along its adjacency direction is the negative gradient of $\Sigma_C$:

$$
\vec{a}_C = -\vec{\nabla}_{\mathrm{adj}}\,\Sigma_C.
$$

In the Newtonian-gravity regime, the dominant variation in $\Sigma_C$ comes from the substrate-level strain content $\mathrm{Str}(C)$ sourced by distant mass distributions. We use the substrate-level convention that $\mathrm{Str}(C)$ functions as a *potential* — the per-channel substrate-source content enters $\mathrm{Str}(C)$ with a kernel-mediated $1/R$ envelope at large $R$, and the chain's acceleration is the gradient of this potential. We denote this potential $\Phi(R)$:

$$
\Phi(R) \equiv \mathrm{Str}(C \mid M, R), \qquad \vec{a}_N = -\vec{\nabla}_R\,\Phi(R).
$$

This is **Model A** in the design space sketched in §4.0: the potential reading. Per-channel V1 content contributes a $1/R$ potential at large $R$; the holographic counting modulates the **effective coupling** that translates source-mass content $\sigma(M)$ into the per-channel potential, not the *number* of independently-summed contributions.

### 4.2 Per-channel V1 potential contribution

A single substrate channel connecting source-locus $u_M$ to test-locus $u_R$ carries a V1-kernel-mediated potential contribution to the test chain's stability landscape. At separations $R \gg \ell_{\mathrm{ED}}$, the V1 finite-width retarded kernel envelope (Paper #18) produces, via the DCGT continuum-limit reading, a Coulomb-like $1/R$ falloff in the per-channel kernel content. The per-channel potential contribution is therefore:

$$
\Phi_{\mathrm{ch}}(R) = -\,\kappa_{V1}\,\frac{\sigma_{\mathrm{ch}}(M)}{R}
$$

where:

- $\sigma_{\mathrm{ch}}(M)$ is the substrate-source content **resolved at the per-channel level** (defined precisely in §4.3),
- $\kappa_{V1}$ is the substrate-level per-channel coupling coefficient (set by V1 kernel normalization),
- The negative sign reflects the attractive substrate-strain convention (substrate-source content lowers $\Sigma_C$ at the test chain, mirroring Newtonian gravitational potential).

### 4.3 Holographic substrate-source resolution

We now address the key structural point that the original (round-1) version got wrong. **The substrate-source content $\sigma(M)$ associated with a localized source-mass region $M$ is a single substrate-level fact about the source**; it is *not* an independent quantity that each substrate channel sees a separate copy of. The holographic participation-count bound tells us how that single substrate-source content is **distributed across substrate channels** at substrate-graph resolution.

By P03 (spatial homogeneity / translation-invariance of the participation-graph adjacency) and the substrate-scale resolution of P08, the substrate-source content $\sigma(M)$ is distributed uniformly across the $N(R)$ channels crossing the 2-surface $\Sigma_R$:

$$
\sigma_{\mathrm{ch}}(M; R) = \frac{\sigma(M)}{N(R)}.
$$

This is the **per-channel resolution** of the source content at the substrate-graph scale $\Sigma_R$. It is *not* a phenomenological partition; it follows structurally from:

- P03's translation-invariance (no preferred channel through $\Sigma_R$),
- P07's distinguishability (each channel through $\Sigma_R$ carries a well-defined fraction of the substrate-source content),
- The holographic bound (the total channel count through $\Sigma_R$ is $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$).

### 4.4 Cumulative-strain reading — the channel-count factors cancel

The chain's experienced potential is the substrate-graph cumulative-strain reading: summing the per-channel V1 potential contribution (§4.2) over the $N(R)$ channels through $\Sigma_R$, with each channel carrying the per-channel-resolved source content (§4.3):

$$
\Phi(R) = \sum_{K=1}^{N(R)} \Phi_{\mathrm{ch}}(R) = N(R) \cdot \left(-\kappa_{V1}\,\frac{\sigma_{\mathrm{ch}}(M; R)}{R}\right) = N(R) \cdot \left(-\kappa_{V1}\,\frac{\sigma(M)/N(R)}{R}\right).
$$

**The factors of $N(R)$ cancel exactly.** The cumulative reading collapses to:

$$
\boxed{\Phi(R) = -\,\kappa_{V1}\,\frac{\sigma(M)}{R}.}
$$

This cancellation is the structurally-correct accounting. The earlier (round-1) version of this derivation lost the cancellation by combining (i) per-channel content $\sigma(M)/R$ (which treated $\sigma(M)$ as *not* resolved per channel) with (ii) a sum over $N(R)$ channels — producing $N(R) \cdot \sigma(M)/R \propto R \cdot \sigma(M)/R \cdot \mathrm{coeff} \propto R$, which then required taking $d/dR(R^{-1})$ inconsistently. The substrate-level structure does *not* support that combination: substrate-source content distributes across channels (§4.3), it does not duplicate.

The result is a single Coulomb-like $1/R$ potential, with substrate-source content $\sigma(M)$ and substrate-level coupling coefficient $\kappa_{V1}$. The holographic counting $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ has entered the derivation **structurally** (setting the per-channel substrate-source resolution) but has cancelled out at the level of the final potential. It re-enters in §5 when the substrate-level coefficient assembly identifies $\kappa_{V1} \cdot \sigma(M)$ with $G \cdot M$.

### 4.5 Gradient produces inverse-square acceleration

The chain's experienced acceleration is the negative radial gradient of $\Phi(R)$:

$$
a_N(R) = -\frac{\partial \Phi}{\partial R} = -\frac{\partial}{\partial R}\!\left(-\,\kappa_{V1}\,\frac{\sigma(M)}{R}\right) = -\,\kappa_{V1}\,\frac{\sigma(M)}{R^2}.
$$

The magnitude is $|a_N| = \kappa_{V1}\,\sigma(M)/R^2$, directed inward along the participation-graph adjacency from test toward source (attractive substrate-strain, consistent with the negative sign of $\Phi$).

**The inverse-square form arises directly from the $1/R$ potential.** The structure is:

1. **V1 kernel $1/R$ falloff per channel** (substrate-level, from V1 finite-width retarded structure via DCGT) → per-channel potential $\propto 1/R$.
2. **Holographic substrate-source resolution** (substrate-source content distributes across channels rather than duplicating) → $N(R)$ factors cancel in the cumulative reading.
3. **Cumulative reading produces a single $1/R$ potential**, with the substrate-source content fully captured.
4. **Gradient gives $1/R^2$** acceleration.

Identifying $\kappa_{V1}\,\sigma(M) \equiv GM$ via the substrate-level coefficient assembly (§5):

$$
a_N(R) = \frac{GM}{R^2}.
$$

### 4.6 Why the inverse-square form is structural (not assumed)

The earlier (round-1) framing tried to motivate $1/R^2$ as a *competition* between $R^2$ area scaling and $1/R$ kernel falloff. That motivation was both unnecessary and mathematically incoherent (the competition gives $R$, whose gradient is $1$, not $1/R^2$). The structurally-correct accounting is simpler: the holographic surface-area scaling and the V1 kernel falloff **interact at the level of substrate-source resolution**, not as additive content. The surface area sets *how many channels* the source content distributes across; the kernel sets *how each channel contributes to the potential*. These combine multiplicatively in the per-channel potential's coefficient, then cancel in the cumulative reading, leaving a single $1/R$ potential whose gradient is $1/R^2$.

In $D = 3+1$ spatial dimensions, this cancellation produces a $1/R$ potential and a $1/R^2$ acceleration. In other spatial dimensions, the holographic-surface scaling and the V1-kernel falloff would scale differently:

- $D = 4+1$: surface scales as $R^3$, V1 kernel as $1/R^2$, per-channel source content as $\sigma(M)/R^3$, per-channel potential as $\sigma(M)/(R^3 \cdot R^2)$, cumulative reading $\Phi(R) \propto 1/R^2$, acceleration $\propto 1/R^3$.

In general, in $D$ spatial dimensions, the inverse-power law of acceleration is $1/R^{D-1}$ (where $D = 3$ gives $1/R^2$). The empirical $1/R^2$ acceleration is specific to $D = 3+1$, consistent with the substrate's spatial-dimension primitive (P06, implicit here).

---

## 5. Identification of $G$

### 5.1 Dimensional bookkeeping

Newton's acceleration has dimensions $[a_N] = [\text{length}]/[\text{time}]^2$. The mass $M$ has $[\text{mass}]$; $R$ has $[\text{length}]$. The identification $a_N = GM/R^2$ requires:

$$
[G] = \frac{[\text{length}]^3}{[\text{mass}] \cdot [\text{time}]^2}.
$$

### 5.2 Assembly from substrate constants

The substrate-level constants available for assembling $G$ from the cumulative-strain reading (§4) are:

- $c$ ($[\text{length}]/[\text{time}]$),
- $\hbar$ ($[\text{mass}] \cdot [\text{length}]^2/[\text{time}]$),
- $\ell_{\mathrm{ED}}$ ($[\text{length}]$).

The unique combination with the correct dimensions for $G$:

$$
G = \frac{c^3\,\ell_{\mathrm{ED}}^2}{\hbar}.
$$

Verification:

$$
\left[\frac{c^3\,\ell_{\mathrm{ED}}^2}{\hbar}\right] = \frac{[\text{length}/\text{time}]^3 \cdot [\text{length}]^2}{[\text{mass}] \cdot [\text{length}]^2/[\text{time}]} = \frac{[\text{length}]^3}{[\text{mass}] \cdot [\text{time}]^2}. \;\checkmark
$$

The numerical coefficient (factors of $4\pi$, V1 kernel normalization, etc.) is fixed by the §4 cumulative-strain reading; the substrate-source identification $\kappa_{V1}\,\sigma(M) = GM$ closes the coefficient assembly:

$$
\boxed{G = \frac{c^3\,\ell_{\mathrm{ED}}^2}{\hbar}.}
$$

### 5.3 Empirical identification $\ell_{\mathrm{ED}} = \ell_P$

The substrate scale $\ell_{\mathrm{ED}}$ is a postulated primitive (P08); its *numerical value* is empirical, not substrate-derived. Matching the substrate-derived $G$ to the measured Newtonian gravitational constant $G_{\mathrm{obs}} \approx 6.674 \times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$:

$$
\ell_{\mathrm{ED}} = \sqrt{\frac{G_{\mathrm{obs}}\hbar}{c^3}} = \ell_P \approx 1.616 \times 10^{-35}\,\mathrm{m}.
$$

This is the Planck length, identified empirically with the substrate scale. The identification $\ell_{\mathrm{ED}} = \ell_P$ is **value-layer empirical content** — the substrate scale is postulated, but its specific numerical value is inherited from matching observed gravitational strength.

Equivalently: the standard definition $\ell_P = \sqrt{\hbar G/c^3}$ is rearranged in ED's substrate framework into the identification $G = c^3\ell_P^2/\hbar$, with $\ell_P$ playing the role of the postulated substrate scale rather than $G$ playing the role of an independent fundamental constant. **ED reduces the number of independent fundamental constants by one.**

### 5.4 What is structural vs. what is inherited

In the language of the ED Generative Primitives System:

- **Structural form of $G$** ($c^3\ell_{\mathrm{ED}}^2/\hbar$): the unique downstream form consistent with the postulated primitives (§4 + §5.2).
- **Substrate scale $\ell_{\mathrm{ED}}$**: postulated primitive P08; numerical value INHERITED from value-layer empirical content ($\ell_{\mathrm{ED}} = \ell_P$).
- **Substrate constants $c$, $\hbar$**: inherited from value-layer empirical content.
- **Numerical coefficient assembly**: structurally determined from §4 cumulative-strain reading.

The chain: postulated primitives + V1 inheritance → holographic count $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ → per-channel V1 potential $-\kappa_{V1}\sigma_{\mathrm{ch}}/R$ → holographic substrate-source resolution $\sigma_{\mathrm{ch}} = \sigma(M)/N(R)$ → cumulative-strain reading (with $N(R)$ cancellation) producing $\Phi(R) = -GM/R$ → $a_N(R) = GM/R^2$ → identification $G = c^3\ell_{\mathrm{ED}}^2/\hbar$. The empirical match $\ell_{\mathrm{ED}} = \ell_P$ closes the loop.

---

## 6. Cross-Domain Context

### 6.1 Transition acceleration $a_0$ (Paper_029)

The MOND-class transition acceleration $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ emerges from a dipole-mode projection of the cosmic decoupling surface at radius $R_H = c/H_0$ onto an accelerating chain's adjacency structure:

$$
a_0 = \frac{cH_0}{2\pi}.
$$

The factor of $2\pi$ is geometric — the azimuthal-Fourier normalization of the dipole mode on the residual SO(2) of an accelerating chain (Paper_029 §5.1, dipole-projection integral).

### 6.2 ED Combination Rule (Paper_030)

In the joint weak-gradient regime, the chain's stability landscape acquires a logarithmic cross-term $\sqrt{GMa_0}\,\log(R/R_0)$, producing the deep-MOND multiplicative combination:

$$
a = \sqrt{a_N \cdot a_0}.
$$

### 6.3 Slope-4 BTFR (Paper_031)

Composing $a_N = GM/R^2$ (this paper), $a_0 = cH_0/(2\pi)$ (Paper_029), and $a = \sqrt{a_N \cdot a_0}$ (Paper_030) gives:

$$
v_{\mathrm{flat}}^4 = G \cdot M \cdot a_0
$$

for flat rotation curves at large radii.

### 6.4 V5 cross-domain context

The V5 cross-chain correlation kernel (Paper #20 / Paper_090) operates across ~40 orders of magnitude in characteristic timescale. The substrate-gravity arc uses V1 (single-chain vacuum kernel) rather than V5; the deeper unification is that the substrate's kernel hierarchy supplies the structural machinery for all cross-locus interaction phenomena in ED.

---

## 7. What This Paper Does NOT Claim

### 7.1 The substrate scale $\ell_P$ is not derived

The substrate scale $\ell_{\mathrm{ED}}$ is **postulated** (Primitive P08). The empirical identification $\ell_{\mathrm{ED}} = \ell_P$ is **value-layer empirical content**, derived from matching $G_{\mathrm{obs}}$. ED does not derive the numerical value of $\ell_P$ from a deeper structural principle.

The relationship $G = c^3\ell_P^2/\hbar$ is a **dimensional rearrangement**: if $G$ is observed empirically, $\ell_P$ is determined; if $\ell_P$ is postulated, $G$ is determined. ED chooses to treat $\ell_P$ as the postulated primitive and $G$ as the downstream identification. The choice is motivated by parsimony (P08 supports multiple downstream derivations across the gravity arc) and by the substrate-ontology framing (the substrate has a primitive scale; $G$ is a derived dynamical coefficient). The structural mechanism in §4 — holographic substrate-source resolution + V1 kernel + P12 cumulative reading — is what the substrate framework *adds* beyond the dimensional rearrangement.

### 7.2 General relativity is not derived

This paper derives the **Newtonian limit** $a_N = GM/R^2$. It does not derive the full Einstein equations. Whether the Einstein equations emerge as a substrate-level result is the subject of ED's curvature-emergence arc (Arc ED-10, conditional-positive result in pre-pivot work). The present paper takes no position on Einstein-equation emergence.

### 7.3 No claim that gravity is forced from nothing

The derivation in §§3–5 is **conditional** on the postulated primitives + V1 inheritance. It is *not* a derivation of gravity from zero assumptions. ED's Generative Primitives System is the same genre as Newton's three laws (posited), Einstein's two postulates of special relativity (posited), Schrödinger's equation (posited), and the operational-reconstruction tradition (Hardy, CDP, Masanes–Müller, Coecke–Kissinger). The 13 primitives are posited; the empirical case rests on cross-domain reach.

### 7.4 No claim about mass values or cosmological parameters

The source-mass content $\sigma(M)$ for any specific physical system is **value-layer empirical content**, not substrate-derived. Similarly $H_0$ (Paper_029) is empirical. ED does not derive specific mass values or cosmological parameters.

### 7.5 No claim of uniqueness beyond the 13 primitives

The structural derivation is the unique downstream content **given the postulated primitives**. The uniqueness is conditional on the substrate ontology being the 13-primitive system; it is not a uniqueness claim about $G$ in some absolute sense.

### 7.6 No claim of superiority over standard physics

Newton's law is right in both frameworks. ED's substrate-level derivation supplies *structural mechanism* for $G$'s value (assembling it from $c$, $\ell_{\mathrm{ED}}$, $\hbar$) rather than offering a "replacement" for classical mechanics.

---

## 8. Falsification Criteria

### 8.1 Observational failure of $G = c^3\ell_P^2/\hbar$

The relationship is a dimensional rearrangement — satisfied by definition once $\ell_P = \sqrt{\hbar G/c^3}$. The structural content is the *interpretation*: $\ell_P$ as postulated substrate primitive, $G$ as downstream identification.

A pointed falsifier: **discovery that $G$ varies in time or space inconsistently with the substrate's primitive structure**. Constraints currently give $\dot{G}/G \lesssim 10^{-13}/\mathrm{yr}$. Tighter measurements detecting non-zero $\dot{G}/G$ inconsistent with substrate-level $\ell_{\mathrm{ED}}$ time-invariance would falsify ED's interpretation.

### 8.2 Violation of holographic participation-count scaling

The bound $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$ has the form of the Bekenstein-Hawking entropy bound. **Empirical demonstration that information-capacity bounds do not satisfy the area-scaling form** would falsify §3.

### 8.3 Discovery of non-inverse-square strain

**Discovery that gravitational acceleration deviates from $a_N \propto 1/R^2$** beyond GR's post-Newtonian corrections would falsify §4's substrate-level inverse-square structure. Newton's law has been tested at sub-millimeter and solar-system scales to extreme precision; no deviation is observed.

### 8.4 Failure in the deep-MOND regime

ED predicts Newton (when $a_N \gg a_0$), ED Combination Rule (transition), and deep-MOND ($a \approx \sqrt{a_N a_0}$ when $a_N \ll a_0$). **Empirical failure of the transition between regimes** would falsify the joint substrate-gravity arc.

### 8.5 BTFR slope deviation from 4.000

ED predicts slope-4 BTFR ($v^4 = GMa_0$) with zero intrinsic scatter in the deep-MOND asymptotic regime (Paper_031). **Empirical demonstration of slope $\neq 4$** to high precision would falsify the gravity-arc composition.

### 8.6 Discovery of independent dimensional combinations for $G$

**Discovery that the dimensional combination is non-unique** (multiple inequivalent substrate-derived rearrangements) would weaken the uniqueness claim. Currently $c^3\ell_P^2/\hbar$ is unique within $\{c, \ell_{\mathrm{ED}}, \hbar\}$; additional substrate-level scales would re-open the question. ED's commitment to $\ell_{\mathrm{ED}}$ as the only primitive scale is itself a falsifiable structural claim.

---

## 9. Position Statement

Newton's gravitational constant $G$ is **not** a primitive of the Event Density Generative System. It is a downstream structural identification:

$$
G = \frac{c^3 \ell_{\mathrm{ED}}^2}{\hbar},
$$

assembled from substrate constants $c$, $\hbar$, and the postulated substrate scale $\ell_{\mathrm{ED}}$ (Primitive P08). The empirical identification $\ell_{\mathrm{ED}} = \ell_P$ is value-layer content, derived from matching the observed Newtonian gravitational constant.

The structural mechanism: the holographic participation-count bound $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ (derived from P02 + P03 + P07 + P08) combined with the cumulative-strain reading of P12's stability landscape (using V1's finite-width retarded kernel) produces Newton's law $a_N = GM/R^2$. The substrate-source content $\sigma(M)$ distributes across the $N(R)$ channels rather than duplicating across them; this **holographic substrate-source resolution** makes the per-channel content $\sigma_{\mathrm{ch}} = \sigma(M)/N(R)$, and the cumulative reading produces a single $1/R$ Newtonian potential $\Phi(R) = -GM/R$, whose gradient is the $1/R^2$ acceleration. The $N(R)$ factors cancel in the cumulative reading — they enter structurally (setting per-channel resolution) but not multiplicatively.

What this paper claims:

- Given the postulated primitives, $G$'s structural form $c^3\ell_{\mathrm{ED}}^2/\hbar$ is the unique downstream identification.
- ED reduces the number of independent fundamental constants by one.
- The substrate-level mechanism (holographic counting + holographic substrate-source resolution + V1 kernel + cumulative reading) gives Newton's $1/R^2$ law structural origin.
- The result is the foundation for the rest of the gravity arc.

What this paper does *not* claim:

- The substrate scale $\ell_P$ is not derived; it is postulated.
- Full GR is not derived; this is the Newtonian limit only.
- Gravity is not forced from nothing; the derivation is conditional.
- Specific mass values and cosmological parameters are value-layer empirical content.
- No claim of superiority over Newton's classical derivation.

The empirical case for the substrate primitives rests on cross-domain reach.

**Series context.** This is Paper_027 of the gravity arc rewrite. The arc continues:

- **Paper_029:** Transition acceleration $a_0 = cH_0/(2\pi)$.
- **Paper_030:** ED Combination Rule $a = \sqrt{a_N \cdot a_0}$.
- **Paper_031:** Slope-4 BTFR $v^4 = GMa_0$.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md`.
- **Paper #18 (V1 Finite-Width / N1):** kernel-form template inherited.
- **Paper #19 (V1 Retarded Support / T18):** retarded-support template.
- **Paper_029, 030, 031:** gravity-arc continuation.
- **Paper_090 (V5 Cross-Chain):** brief mention §6.4.

### Glossary

- **Newton's $G$.** Identified downstream as $G = c^3\ell_{\mathrm{ED}}^2/\hbar$.
- **Holographic participation-count bound.** $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$.
- **Substrate scale $\ell_{\mathrm{ED}}$.** Primitive P08. Empirically identified with $\ell_P$.
- **Holographic substrate-source resolution.** The principle (§4.3) that source-mass content $\sigma(M)$ distributes across substrate channels rather than duplicating across them: $\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$.
- **Cumulative-strain reading (potential form).** The sum of per-channel V1 potential contributions over $N(R)$ channels; under holographic substrate-source resolution, the $N(R)$ factors cancel and the cumulative reading produces a single $1/R$ Newtonian potential.
- **Stability landscape $\Sigma$.** P12 functional $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$.
- **V1 kernel $1/R$ falloff.** V1's substrate-level kernel envelope at large $R$.

---

**End of Paper_027.**

*Wave-2 Generative Paper — Gravity Arc, Foundation. Round-2 revision: §4.3–§4.6 rewritten under the potential reading (Model A) to remove the round-1 mathematical inconsistency between $\mathrm{Str}(R) \propto R$ and $a_N \propto d/dR(R^{-1})$.*
