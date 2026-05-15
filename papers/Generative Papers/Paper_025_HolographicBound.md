# Paper_025 — The Holographic Participation-Count Bound

**Series:** Event Density (ED) Generative Papers — Wave-2 gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (load-bearing for Paper_027 Newton's $G$)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/Paper_025_HolographicBound.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_025_HolographicBound.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087 position commitment).
2. **The substrate scale $\ell_{\mathrm{ED}}$ is not derived.** Empirically identified with $\ell_P$ via Newton-recovery (Paper_027 §5.3). Value-layer empirical content.
3. **No claim that the holographic bound is forced from nothing.** Conditional on P02 + P03 + P06 + P07 + P08.
4. **No claim that the bound is identical to the Bekenstein–Hawking entropy bound.** The two have the same area-scaling form, but ED derives its bound from substrate channel-counting on the participation graph, not from BH thermodynamics. The identification with the BH bound is empirical (via $\ell_{\mathrm{ED}} = \ell_P$ matching), not derivation.
5. **No claim about substrate-level entropy.** This paper derives a *channel-count* bound, not an entropy bound. Whether the substrate's channel count is informationally equivalent to BH entropy is downstream content.
6. **No claim that 3D spatial dimension is derived here.** P06 ($D = 3+1$) is a substrate primitive (Paper_087 §5.6); the $4\pi R^2$ area scaling follows from P06 + standard geometry.
7. **No claim that the bound holds in non-$D=3+1$ substrates.** In other spatial dimensions, the holographic bound takes different form ($\Omega_{D-1} R^{D-1}/\ell_{\mathrm{ED}}^{D-1}$). The specific $4\pi R^2$ form is $D=3+1$-specific.
8. **No claim of derivation of standard quantum-gravity holography.** ED's substrate-level counting and BH-thermodynamic holography arrive at the same area-scaling form via different routes; the structural parallel is a cross-domain coherence claim, not a unification claim.

---

## Abstract

The **holographic participation-count bound** is a substrate-level structural result in the Event Density Generative Substrate Ontology: given a localized source region and a test chain at distance $R$, the number of distinct substrate channels connecting source to test is bounded by

$$
N(R) \leq \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

Given the postulated primitives P02 (participation) + P03 (channel + locus indexing + spatial homogeneity) + P06 (spatial dimension $D=3+1$) + P07 (channel structure) + P08 (substrate scale $\ell_{\mathrm{ED}}$), the bound follows from substrate-level channel-counting on closed 2-surfaces at substrate-graph resolution. The derivation has three steps: (1) channels connecting two substrate loci must cross a closed 2-surface enclosing the source; (2) by P06, the 2-surface has area $4\pi R^2$ in the substrate-graph's spatial structure; (3) by P08, channels are resolved at substrate-graph scale, so the number of distinct channels through the surface is bounded by area/$\ell_{\mathrm{ED}}^2$. The bound is **load-bearing for Paper_027** (Newton's $G$ via cumulative-strain reading with holographic substrate-source resolution). The paper makes no claim that the bound is forced from nothing, no claim of identity with Bekenstein–Hawking entropy (the area-scaling form is the same; the derivation route differs), and no claim about substrate-level entropy.

---

## 1. Introduction

### 1.1 What this paper does

This paper supplies the **dedicated derivation** of the holographic participation-count bound:

$$
N(R) \leq \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

The bound is used as a load-bearing structural step in Paper_027 (Newton's $G$ via cumulative-strain reading), in Paper_028 (Cosmic Decoupling Surface), and throughout the gravity arc. Paper_027 cited the bound but did not derive it dedicatedly; this paper supplies the derivation.

The structure is: (1) substrate-level channels connecting source to test cross a closed 2-surface; (2) the 2-surface has area set by P06's spatial-dimension primitive; (3) channels are resolved at substrate scale per P08; (4) the bound follows by area-divided-by-substrate-scale-squared.

### 1.2 Why a dedicated derivation matters

Paper_027 (Newton's $G$) uses the holographic bound in §3 to set up the channel-counting that produces the inverse-square law via holographic substrate-source resolution + V1 kernel. The bound is **load-bearing**: removing it breaks Paper_027's derivation chain.

The QC discipline (Load-Bearing Step Audit, item 8 of the QC checklist) requires every load-bearing step to be either D (derived) or P (postulated) — not A (asserted). Paper_027's holographic count is currently stated with a sketch derivation in its §3.2. This paper provides the dedicated, full-rigor derivation, converting Paper_027's holographic-count step from "sketched derivation" to "fully-backed derivation via Paper_025."

### 1.3 How this fits into the gravity arc

- **Paper_025 (this paper):** Holographic participation-count bound.
- **Paper_026 (in queue):** Cumulative-strain reading of P12 (Newton's $G$ mechanism).
- **Paper_027:** Newton's $G$ — uses bound from this paper + cumulative-strain reading from Paper_026.
- **Paper_028 (next):** Cosmic decoupling surface at $R_H = c/H_0$.
- **Paper_029:** Transition acceleration $a_0$ — uses cosmic decoupling.
- **Paper_030:** ED Combination Rule.
- **Paper_031:** Slope-4 BTFR.

This paper is the second wedge-arc paper (after Paper_087 position paper) and the load-bearing upstream for Paper_027.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation as primitive relation).** Chains participate in channels.
- **P03 (Channel + locus indexing; spatial homogeneity).** Discrete channel index, locus index, translation-invariance.
- **P06 (Spatial dimension $D = 3+1$).** Substrate has 3 spatial dimensions; closed 2-surfaces have area $4\pi R^2$ at radius $R$.
- **P07 (Channel structure as ontological primitive).** Channels are structurally distinguishable.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).** Substrate has characteristic edge length; channels resolved at this granularity.

**Postulates specific to this paper (added per round-2 QC Rereading Test):**

- **P-Codim-1 (Channel codimension-1 structure):** *Substrate channels are codimension-1 substrate-graph objects: when a channel crosses an $n$-dimensional substrate-graph surface, it occupies a region of $n$-dimensional extent at the substrate scale, not a point.* This is a substrate-level structural commitment about what channels *are* — required for the area-divided-by-footprint-area combinatorial argument (§4.1). It is **not** derivable from P02 + P07; it is a substrate-level postulate, labeled here for transparency. (For 2-surfaces in $D=3+1$: channel footprint = $\ell_{\mathrm{ED}}^2$.)
- **P-Sat (Substrate-saturation regime assumption):** *In applications where the bound is used as an equality (Paper_027's holographic substrate-source resolution, Paper_039 BH horizon counting), the substrate is taken to be in the **substrate-saturated regime** — every substrate-graph footprint region on the 2-surface contains exactly one distinct channel.* This is a regime assumption, not a substrate-level derivation; the bound is non-strict in general and equality holds only at substrate saturation.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 (used implicitly via substrate-graph structure, but not load-bearing for this paper's combinatorial derivation).

**Empirical / value-layer inputs:**

- $\ell_{\mathrm{ED}}$ empirically identified with $\ell_P$ via Paper_027 §5.3. **Value-layer empirical content.**

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Channels connect substrate loci through participation graph | D | §3.1 from P02 + P07 |
| Channels crossing a closed surface enclose interior loci | D | §3.2 from P03 spatial-homogeneity |
| Closed 2-surface at radius $R$ has area $4\pi R^2$ | D | §3.3 from P06 ($D=3+1$) + standard geometry |
| Channels resolved at substrate scale $\ell_{\mathrm{ED}}$ | D | §3.4 from P08 |
| Two channels at separation $< \ell_{\mathrm{ED}}$ merge | D | §3.4 from P08 substrate-resolution |
| Channels are codimension-1 substrate-graph objects (2D footprint on a 2-surface) | **P (P-Codim-1)** | **§2 postulate.** Structural commitment about what channels *are*; not derivable from P02+P07. Required for area-divided-by-footprint-area combinatorics. |
| Per-channel "footprint area" on 2-surface = $\ell_{\mathrm{ED}}^2$ | D | §4.1 from P-Codim-1 + P08 (codim-1 channel × substrate-scale resolution in each tangent direction) |
| Bound $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$ | D | §4.2 area-divided-by-footprint-area, given P-Codim-1 |
| Saturation limit (equality) for downstream-paper applications | **P (P-Sat)** | **§2 regime postulate.** Substrate-saturated regime; the bound is non-strict in general. Required where Paper_027 / Paper_039 use the bound as equality. |
| $D \neq 3+1$ alternative form | D | §5.2 dimensional generalization (codim-1 footprint in $(D-1)$-dimensional surface = $\ell_{\mathrm{ED}}^{D-1}$) |
| $\ell_{\mathrm{ED}} = \ell_P$ identification | I | Paper_027 §5.3 empirical |

All load-bearing steps are P, D, or I. **No A (asserted) rows.** *Round-2 Rereading Test applied: the per-channel footprint area row (previously labeled D) was relabeled as derived from the **P-Codim-1** postulate now stated explicitly in §2.*

---

## 3. Substrate-Level Channel Geometry

### 3.1 Channels through the participation graph

By P02, chains participate in channels. By P07, channels are structurally distinguishable carriers with intrinsic identities. A **substrate channel** is a substrate-graph object connecting substrate loci via the participation-graph structure.

For two distinct substrate loci $u_M$ (source) and $u_R$ (test, at separation $R = |u_R - u_M|$ along the substrate-graph spatial direction), any substrate-level cross-locus interaction between source and test proceeds through some specific set of substrate channels that connect $u_M$ to $u_R$.

**The cross-locus interaction structure:** the substrate's primitive operational mechanism for source-to-test influence is channel-mediated. By P02 + P07, the substrate has no other primitive cross-locus mechanism — chains and channels are the substrate's primitive ontological content.

### 3.2 Channels crossing closed 2-surfaces

By P03 (spatial homogeneity), the substrate's participation-graph adjacency is translation-invariant locally. Consider a closed 2-surface $\Sigma_R$ enclosing source locus $u_M$, parameterized at substrate-graph radius $R$ (the substrate-graph distance from $u_M$).

**Topological observation:** any channel connecting $u_M$ to a locus $u_R$ outside $\Sigma_R$ (i.e., at substrate-graph distance $\geq R$ from $u_M$) **must cross** $\Sigma_R$ at some substrate-level point on the surface.

This is a substrate-level statement of a standard topological fact: a continuous path from an interior point to an exterior point of a closed surface must cross the surface. In the substrate-graph setting, the "continuous path" is the substrate channel, parameterized by substrate-graph edges, and "crossing" means the channel has a substrate-graph edge with one endpoint inside $\Sigma_R$ and the other outside.

**Therefore the number of channels connecting $u_M$ to anything at radius $\geq R$ is bounded by the number of channels crossing $\Sigma_R$.**

### 3.3 Area of the closed 2-surface

By P06 (spatial dimension $D = 3+1$), the substrate has 3 spatial dimensions. The closed 2-surface $\Sigma_R$ at substrate-graph radius $R$ is the substrate-graph analog of a 2-sphere of radius $R$ in 3D Euclidean space (modulo coarse-graining at substrate scale).

In $D = 3$ spatial dimensions, the area of a 2-sphere of radius $R$ is:

$$
A(\Sigma_R) = 4\pi R^2.
$$

**This is the area of $\Sigma_R$ measured in substrate-graph terms at coarse-grained scales** (scales $R \gg \ell_{\mathrm{ED}}$ where the substrate-graph becomes effectively continuous via DCGT). At substrate-graph scale, the surface has finite combinatorial structure (a set of substrate-graph faces); the $4\pi R^2$ value is the DCGT-continuum-limit area.

**Dimensional check:** $A$ has dimensions $[\mathrm{length}]^2$; $R$ has $[\mathrm{length}]$; $4\pi$ dimensionless; so $4\pi R^2$ has $[\mathrm{length}]^2$. ✓

### 3.4 Substrate-scale resolution of channels

By P08, the substrate has characteristic edge length $\ell_{\mathrm{ED}}$. Substrate channels are resolved at this granularity: **two distinct channels through $\Sigma_R$ must be separated by at least $\ell_{\mathrm{ED}}$ on the surface**; otherwise they merge into a single substrate channel at the resolution limit.

**Operational statement:** for any two channels $K_1, K_2$ crossing $\Sigma_R$ at substrate-graph points $p_1, p_2$ on $\Sigma_R$, if the substrate-graph separation $|p_1 - p_2|_{\Sigma_R} < \ell_{\mathrm{ED}}$, then $K_1$ and $K_2$ are identified as a single substrate channel.

This is the substrate-graph analog of saying the substrate has finite discretization resolution: below $\ell_{\mathrm{ED}}$, the substrate has no further resolved structure.

---

## 4. The Holographic Bound — Combinatorial Derivation

### 4.1 Per-channel "footprint area" on the surface — derivation from P-Codim-1

The per-channel footprint area $A_{\mathrm{channel\,footprint}}$ on the 2-surface $\Sigma_R$ is derived from two upstream commitments:

**Step 1 (P-Codim-1):** By the codimension-1 channel postulate (§2 P-Codim-1), substrate channels are codimension-1 substrate-graph objects. When a channel crosses an $n$-dimensional substrate-graph surface, it occupies $n$-dimensional extent at the substrate scale — *not* a point-like crossing.

For the 2-surface $\Sigma_R$ ($n = 2$), each channel's crossing region has **2D extent** on the surface.

**Step 2 (P08 substrate resolution):** By P08, the substrate-graph resolution scale is $\ell_{\mathrm{ED}}$ in each substrate-graph spatial direction. The channel's 2D footprint region on $\Sigma_R$ therefore has linear extent $\geq \ell_{\mathrm{ED}}$ in each of the two tangent directions along the surface (otherwise, by §3.4, the footprint region would merge with adjacent channel footprints at the substrate-resolution limit).

**Combining Steps 1 + 2:** the minimum per-channel 2D footprint area on $\Sigma_R$ is:

$$
A_{\mathrm{channel\,footprint}} = \ell_{\mathrm{ED}} \cdot \ell_{\mathrm{ED}} = \ell_{\mathrm{ED}}^2.
$$

**Dimensional check:** $A_{\mathrm{channel\,footprint}}$ has $[\mathrm{length}]^2$; $\ell_{\mathrm{ED}}^2$ has $[\mathrm{length}]^2$. ✓

**Why P-Codim-1 is required.** If channels were codimension-0 (occupying full 3D substrate-graph regions), they would not have well-defined "crossings" of 2-surfaces at all. If channels were codimension-2 or codimension-3 (1D lines or 0D points), the per-crossing footprint on $\Sigma_R$ would be 1D ($\ell_{\mathrm{ED}}$) or 0D (point), giving bounds $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}$ (linear in $R^2$ but linear in $1/\ell_{\mathrm{ED}}$) or unbounded — different scaling forms with different empirical consequences. The codimension-1 commitment (P-Codim-1) is what produces the standard area-scaling $A/\ell_{\mathrm{ED}}^2$ bound. **P-Codim-1 is the load-bearing structural commitment about what channels *are*.**

Two channels with overlapping footprint regions are merged into a single substrate channel by P08 (substrate-resolution merging).

### 4.2 Channel-count bound

The total area of $\Sigma_R$ is $4\pi R^2$ (§3.3). Each distinct channel occupies footprint area $\ell_{\mathrm{ED}}^2$ (§4.1). The maximum number of distinct channels crossing $\Sigma_R$ is bounded by area divided by per-channel footprint area:

$$
N(R) \leq \frac{A(\Sigma_R)}{A_{\mathrm{channel\,footprint}}} = \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

**Dimensional check:** $4\pi R^2$ has $[\mathrm{length}]^2$; $\ell_{\mathrm{ED}}^2$ has $[\mathrm{length}]^2$; ratio is dimensionless. $N(R)$ is a count (dimensionless). ✓

**This is the holographic participation-count bound.**

$$
\boxed{N(R) \leq \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.}
$$

### 4.3 Saturation: substrate-saturated limit

The bound is *non-strict* in general; equality holds in the **substrate-saturated limit**, where the substrate's primitive channel content fully populates the surface — every substrate-graph footprint region of size $\ell_{\mathrm{ED}}^2$ on $\Sigma_R$ contains exactly one distinct channel:

$$
N(R)\big|_{\mathrm{saturated}} = \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.
$$

For substrate regions with less than full channel saturation (e.g., regions far from any significant cross-locus interaction structure), $N(R)$ is strictly less than the bound.

In the gravity-arc applications (Paper_027), the substrate is taken to be near-saturated for the purposes of holographic substrate-source resolution; the bound and the substrate-resolved channel count are equated up to substrate-level coefficient absorption.

### 4.4 Combinatorial summary

The derivation is summarized:

1. (§3.1) Substrate channels are the primitive cross-locus mechanism (P02 + P07).
2. (§3.2) Channels from source to test cross a closed 2-surface (substrate-graph topology + P03).
3. (§3.3) The closed 2-surface has area $4\pi R^2$ (P06 + standard geometry).
4. (§3.4) Channels resolved at substrate scale $\ell_{\mathrm{ED}}$ (P08).
5. (§4.1) Per-channel footprint area = $\ell_{\mathrm{ED}}^2$.
6. (§4.2) Bound: $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$.

The bound is **structural** (follows from substrate primitives + standard geometry + combinatorial argument), not phenomenological.

---

## 5. Discussion

### 5.1 Why this is structural rather than thermodynamic

The bound $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$ has the **same area-scaling form** as the Bekenstein–Hawking entropy bound:

$$
S_{\mathrm{BH}} \leq \frac{A}{4 \ell_P^2} = \frac{4\pi R_{\mathrm{horizon}}^2}{4\ell_P^2}
$$

with the substrate-level $\ell_{\mathrm{ED}} = \ell_P$ identification (Paper_027 §5.3). Up to the dimensionless coefficient (1 vs. 1/4 — order-unity), the two bounds have identical functional form.

**Critical clarification:** the two derivations arrive at the same form via **different routes**:

- **Bekenstein–Hawking:** derived from BH thermodynamics (Bekenstein 1972, Hawking 1975) via entropy-area scaling + temperature/horizon-area relation. The "holographic principle" of standard quantum gravity ('t Hooft 1993, Susskind 1995) generalizes this to a bound on information content of any region.
- **ED holographic participation-count:** derived from substrate-graph combinatorics (§3–§4) — number of distinct substrate channels resolvable on a 2-surface at substrate-graph resolution. **Not derived from BH thermodynamics; not derived from an entropy argument; not derived from a holographic-principle postulate.**

The structural parallel is a **cross-domain coherence claim**: substrate-level channel-counting and BH-thermodynamic entropy-counting arrive at the same area-scaling form via independent structural routes. This is consistent with the ED ontology where:

- BH entropy is the substrate-level channel-count at the horizon (via Paper_039 horizon decoupling).
- The holographic principle is the substrate-level structural consequence of P06 + P07 + P08, not a postulate.

The identification $\ell_{\mathrm{ED}} = \ell_P$ (Paper_027) is what makes the numerical coincidence empirical: under this identification, ED's substrate-level channel count and the BH-thermodynamic entropy bound have the same numerical scale.

### 5.2 Dimensional generalization to $D \neq 3+1$

The $4\pi R^2$ area-scaling form is **$D = 3+1$ specific** (P06). In other spatial dimensions:

- $D = 4+1$ (four spatial): closed surface is a 3-sphere of "area" $2\pi^2 R^3$; channels resolved at substrate scale; per-channel footprint is $\ell_{\mathrm{ED}}^3$ (three substrate-graph spatial dimensions on the surface); bound: $N(R) \leq 2\pi^2 R^3/\ell_{\mathrm{ED}}^3$.
- $D = 2+1$ (two spatial): closed curve is a 1-sphere (circle) of "length" $2\pi R$; channels resolved at substrate scale; per-channel footprint is $\ell_{\mathrm{ED}}$ (one substrate-graph spatial dimension on the curve); bound: $N(R) \leq 2\pi R/\ell_{\mathrm{ED}}$.

In general $D$ spatial dimensions:

$$
N(R) \leq \frac{\Omega_{D-1} R^{D-1}}{\ell_{\mathrm{ED}}^{D-1}}
$$

where $\Omega_{D-1}$ is the volume of the unit $(D-1)$-sphere.

The specific $4\pi R^2/\ell_{\mathrm{ED}}^2$ form for $D = 3+1$ is the empirical case of interest (consistent with observed spatial dimension); other dimensions are structurally available but empirically not realized.

**This is why Newton's law is $1/R^2$ in our universe** (Paper_027 §4.6): the inverse-square form follows from $N(R) \propto R^2$ in $D = 3+1$, combined with V1 kernel $1/R$ falloff producing per-channel content $\sim 1/(R \cdot N(R)) = 1/R^3$, and after holographic substrate-source resolution the cumulative potential is $\propto 1/R$, giving $a_N \propto 1/R^2$.

### 5.3 Relationship to substrate-saturation

The bound is non-strict; substrate regions can have less than full saturation. For the gravity-arc applications:

- **Vacuum substrate:** $N(R) \ll 4\pi R^2/\ell_{\mathrm{ED}}^2$ — vast under-saturation.
- **Source-influenced substrate near localized mass:** $N(R) \to 4\pi R^2/\ell_{\mathrm{ED}}^2$ — substrate-saturated regime relevant to Paper_027's holographic substrate-source resolution.
- **Near a substrate decoupling surface:** $N(R)$ drops as $\Gamma_{\mathrm{cross}} \to 0$ (Paper_028, Paper_039) — saturation reduced by V5 envelope decay across the surface.

The saturation level is regime-dependent; the bound is uniform.

### 5.4 What this bound is NOT

The holographic participation-count bound is **not**:

- A bound on substrate-level entropy (this paper derives a *channel-count* bound; entropy is downstream content).
- A bound on substrate-level information content (information requires additional structure beyond channel count).
- A bound on continuum-field excitations (no continuum fields in ED; channels are primitive).
- A derivation of the standard quantum-gravity holographic principle (the principle is structurally consistent with ED's substrate counting, but ED does not derive the principle's standard formulation).

---

## 6. Use in Downstream Papers

### 6.1 Paper_027 (Newton's $G$)

Paper_027 uses the holographic bound in §3 as part of the holographic substrate-source resolution mechanism. The per-channel substrate-source content is set as $\sigma_{\mathrm{ch}}(M; R) = \sigma(M)/N(R)$, where $\sigma(M)$ is the total substrate-source content from the localized mass and $N(R)$ is the holographic channel count at radius $R$. Under V1 kernel falloff and cumulative-strain reading, the $N(R)$ factors cancel, leaving a single Newtonian $1/R$ potential. The bound is load-bearing for the cancellation and for the inverse-square law's specific $1/R^2$ form.

### 6.2 Paper_028 (Cosmic Decoupling Surface)

Paper_028 uses the holographic bound at radius $R_H = c/H_0$ to characterize the substrate-level channel count at the cosmic-horizon scale. The bound at cosmic horizon $N(R_H) = 4\pi (c/H_0)^2/\ell_{\mathrm{ED}}^2$ is the substrate-level number of channels mediating cross-horizon content.

### 6.3 Paper_039 (Horizon Decoupling)

Paper_039 uses the bound at black-hole-horizon scale to count substrate-level channels at the decoupling surface. The bound at BH horizon $N(r_H) = 4\pi r_H^2/\ell_{\mathrm{ED}}^2$ is the substrate-level analog of the BH area-law entropy (Paper_039 §3 + standard $A/4\ell_P^2$ scaling).

### 6.4 Paper_056 (Class-A Wall)

Paper_056's multiplicity-cap function $M_{\mathrm{cap}}$ is *not* directly the holographic bound (different rate-quantity, see Paper_054). However, the substrate-level channel-count structure that supports $M_{\mathrm{eff}}$ counting is the same channel structure that the holographic bound counts on closed surfaces. The two share substrate-graph primitive content but operate at different scales.

---

## 7. Falsification Criteria

### 7.1 Substrate-level cross-locus interaction without channel-counting

**Falsifier sentence:** *Empirical demonstration of substrate-level cross-locus interaction mediated by something other than discrete substrate channels — e.g., a continuum-field mechanism not derivable as a coarse-grained limit of channels — would falsify the channel-counting basis of the bound.*

### 7.2 Failure of area-scaling at cross-domain scales

**Falsifier sentence:** *Empirical demonstration that cross-locus information-capacity / channel-count bounds at any scale do not satisfy the area-scaling form (e.g., volume-scaling rather than area-scaling) would falsify §4's combinatorial derivation.*

Current state: the area-scaling bound is empirically supported by BH thermodynamics + AdS/CFT-type holographic computations + entropy-area-law in many quantum-gravity frameworks. No empirical counter-evidence is known.

### 7.3 Different substrate scale at different applications

**Falsifier sentence:** *Discovery that the substrate scale operative in BH-horizon counting differs from the substrate scale operative in solar-system gravitational physics (after accounting for empirical $\ell_{\mathrm{ED}} = \ell_P$ identification) would falsify the universality of $\ell_{\mathrm{ED}}$ in the bound.*

### 7.4 Newton's law deviation traceable to bound failure

**Falsifier sentence:** *Discovery that Newton's law deviates from $1/R^2$ in a regime where the deviation is traceable to a substrate-level violation of the $4\pi R^2$ area-scaling (rather than to V1 kernel modifications or other substrate-level effects) would falsify the bound in $D = 3+1$.*

Current state: Newton's law has been tested at sub-millimeter and solar-system scales to extreme precision; no deviation from $1/R^2$ is observed in the Newtonian regime.

### 7.5 Spatial dimension different from $D = 3+1$

**Falsifier sentence:** *Empirical demonstration that the universe's spatial dimension differs from 3 in a way that affects the holographic-bound area-scaling (e.g., effective $R^{D-1}$ scaling with $D \neq 3$) would falsify P06 and require revising the bound to the appropriate $\Omega_{D-1} R^{D-1}/\ell_{\mathrm{ED}}^{D-1}$ form.*

### 7.6 Substrate-graph non-locality

**Falsifier sentence:** *Discovery of substrate-level cross-locus channels that do not pass through enclosing closed surfaces (i.e., that violate substrate-graph locality) would falsify §3.2's topological argument and invalidate the channel-counting basis of the bound.*

---

## 8. Position Statement

The **holographic participation-count bound**:

$$
\boxed{N(R) \leq \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}}
$$

is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives P02 + P03 + P06 + P07 + P08, the bound follows from substrate-level channel-counting on closed 2-surfaces at substrate-graph resolution:

- Channels from source to test cross a closed 2-surface (substrate-graph topology + P03).
- The 2-surface has area $4\pi R^2$ in $D=3+1$ spatial dimensions (P06).
- Channels are resolved at substrate scale $\ell_{\mathrm{ED}}$ (P08); per-channel footprint area is $\ell_{\mathrm{ED}}^2$.
- The bound is area-divided-by-footprint-area.

What this paper claims:

- Given the postulated primitives, the holographic participation-count bound is the unique downstream structural consequence at the substrate level.
- The $4\pi R^2$ form is $D = 3+1$ specific (P06); general-$D$ forms are derivable.
- The bound has the same area-scaling form as the Bekenstein–Hawking entropy bound but is derived via independent substrate-graph combinatorics, not BH thermodynamics.
- The bound is load-bearing for Paper_027 (Newton's $G$), Paper_028 (cosmic decoupling), Paper_039 (BH horizon decoupling).

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- $\ell_{\mathrm{ED}}$ is empirically identified with $\ell_P$, not derived.
- The bound is not forced from nothing; conditional on the substrate ontology.
- The bound is not derived from BH thermodynamics or the standard holographic principle; the structural parallel is cross-domain coherence, not derivation.
- The bound is not a substrate-level entropy bound; it is a channel-count bound.
- The bound is not unique to $D = 3+1$; analogous bounds hold in other dimensions.

The empirical case rests on cross-domain reach: the bound's $4\pi R^2$ form is the structural foundation for Newton's inverse-square law (Paper_027), the cosmic decoupling structure (Paper_028), and the BH horizon area-counting (Paper_039).

**Series context.** Paper_025 of the gravity arc. The arc continues:

- **Paper_026 (in queue):** Cumulative-strain reading of P12.
- **Paper_027:** Newton's $G$ — uses bound + cumulative-strain reading.
- **Paper_028:** Cosmic decoupling surface.
- **Paper_029:** Transition acceleration $a_0$.
- **Paper_030:** ECR.
- **Paper_031:** BTFR slope-4.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1):** substrate kernel structure.
- **Paper_027 (Newton's $G$):** primary downstream user of the bound.
- **Paper_028 (Cosmic Decoupling):** uses bound at cosmic-horizon scale.
- **Paper_039 (BH Horizon Decoupling):** uses bound at BH-horizon scale.

### Glossary

- **Holographic participation-count bound.** $N(R) \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$.
- **Channel.** Substrate-level distinguishable carrier (P07).
- **Substrate-graph.** Discrete graph structure of substrate channels + loci (P03 + P07).
- **Closed 2-surface $\Sigma_R$.** Substrate-graph closed surface at substrate-graph radius $R$ from source locus.
- **Substrate scale $\ell_{\mathrm{ED}}$.** Primitive P08. Empirically $\ell_{\mathrm{ED}} = \ell_P$.
- **Substrate-saturated limit.** Substrate regime where channel count equals the holographic bound.
- **Channel footprint area.** $\ell_{\mathrm{ED}}^2$ — minimum substrate-graph area per distinct channel on a 2-surface.
- **Bekenstein–Hawking entropy bound.** $A/4\ell_P^2$ — standard quantum-gravity holographic bound. Same area-scaling form as ED's substrate-level bound; derived via different route.

---

**End of Paper_025.**

*Wave-2 Generative Paper — Gravity Arc Foundation. Dedicated combinatorial derivation of the holographic participation-count bound used in Paper_027 (Newton's $G$), Paper_028 (cosmic decoupling), Paper_039 (BH horizon).*
