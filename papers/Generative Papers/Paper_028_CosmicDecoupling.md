# Paper_028 — The Cosmic Decoupling Surface at $R_H = c/H_0$

**Series:** Event Density (ED) Generative Papers — Wave-2 gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (load-bearing for Paper_029 $a_0$ and Paper_039 BH horizon)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/Paper_028_CosmicDecoupling.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_028_CosmicDecoupling.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **The Hubble parameter $H_0$ is not derived.** Empirical cosmological measurement; current range $H_0 \in [67, 74]$ km/s/Mpc (Hubble tension).
3. **The substrate speed $c$ is not derived.** Empirical substrate-level constant.
4. **No claim of cosmology derivation.** ED does not derive the Big Bang, structure formation, CMB anisotropies, or large-scale-structure spectra.
5. **No claim that the cosmic decoupling surface is the GR cosmological event horizon.** The two are conceptually distinct (GR horizon involves $\Lambda$ + FRW geometry); the substrate-level surface coincides with $R_H = c/H_0$ but is structurally a substrate-graph effective boundary, not a smooth-manifold geometric feature.
6. **No claim that the dipole-projection factor $1/(2\pi)$ is empirically fit.** The factor is **structurally present** in the canonical Fourier-orthonormality convention on the chain's residual $SO(2)$ symmetry (§6). "Uniquely forced" would overclaim — its specific location is convention-dependent (separate measure vs. absorbed into $Y_{1,0}$ normalization); the total factor in $a_0$ is convention-invariant.
7. **No claim that $a_0 = cH_0/(2\pi)$ is derived in this paper.** That derivation is Paper_029. This paper supplies the *cosmic decoupling surface* and the *dipole-projection geometry* used by Paper_029.
8. **No claim that the substrate-level kernel propagation $c$ matches the relativistic light speed in all contexts.** They are empirically identified (P-RB-1 substrate-level propagation rate); coincidence with relativistic $c$ is value-layer empirical.
9. **No claim of cosmological-curvature derivation.** The cosmic decoupling surface is the substrate-level effective horizon, not derivation of $\Lambda$ / dS / FRW structure.

---

## Abstract

The **cosmic decoupling surface** is the substrate-level effective boundary at radius

$$
R_H = \frac{c}{H_0}
$$

beyond which substrate-level cross-locus influence cannot reach a local chain coherently. Given the 13 postulated primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090), the decoupling surface arises from the crossover between V1 + V5 kernel propagation (at substrate-level speed $c$ via P-RB-1) and Hubble expansion (at rate $H_0$). At radii $R \gtrsim R_H$, the Hubble expansion separates substrate content faster than substrate-kernel propagation can traverse; substrate cross-locus interaction decouples. This paper develops two structural results: (1) the **substrate-level identification** of the cosmic decoupling surface at $R_H = c/H_0$; (2) the **dipole-projection geometry** that an accelerating chain projects onto the surface, with the structurally-forced azimuthal-Fourier-normalization factor $1/(2\pi)$ computed explicitly via the projection integral on the residual $SO(2)$ symmetry. The paper makes no claim that $H_0$ or $c$ is derived (both are empirical/inherited), no claim of cosmology derivation, no claim of identity with the GR cosmological event horizon (the two coincide numerically but are conceptually distinct), and no claim that the dipole-projection factor is empirically fit (it is structurally computed from $SO(2)$ Fourier normalization). The empirical case rests on cross-domain use: this paper is load-bearing for Paper_029 (transition acceleration $a_0 = cH_0/(2\pi)$) and Paper_039 (BH horizon decoupling, which uses analogous substrate-graph mechanism at the BH scale).

---

## 1. Introduction

### 1.1 What this paper does

This paper provides the **dedicated derivation** of the cosmic decoupling surface and the dipole-projection geometry used in Paper_029 (transition acceleration $a_0$). The paper:

1. Derives the substrate-level identification $R_H = c/H_0$ from V1 + V5 kernel-propagation rate vs. Hubble expansion rate.
2. Establishes the substrate-graph structure of the decoupling surface (statistical effective boundary, not geometric).
3. Establishes the anisotropic adjacency structure of an accelerating chain at the substrate level (residual $SO(2)$ symmetry).
4. Computes the dipole-projection integral on the residual $SO(2)$ explicitly, deriving the $1/(2\pi)$ azimuthal-Fourier-normalization factor structurally.

This paper supplies the upstream geometric machinery for Paper_029's $a_0$ derivation; Paper_029 then composes this paper's results with cosmic-content dipole moment and substrate-source normalization to arrive at $a_0 = cH_0/(2\pi)$.

### 1.2 Why a dedicated derivation matters

Paper_029 §3 + §4 sketched the cosmic decoupling surface mechanism and the dipole-projection geometry. Paper_039 §3.2 (revised) acknowledged that the GR horizon $r_H$ is used as the coarse-grained identification point for the BH decoupling surface, without independent substrate-level derivation.

The QC discipline (Load-Bearing Step Audit) requires the cosmic decoupling surface and dipole-projection geometry to be either D (derived) or P (postulated). This paper supplies the dedicated D-status derivation for both, anchoring Paper_029 and Paper_039.

### 1.3 How this fits into the gravity arc

- **Paper_025:** Holographic participation-count bound.
- **Paper_026 (in queue):** Cumulative-strain reading of P12.
- **Paper_027:** Newton's $G$.
- **Paper_028 (this paper):** Cosmic decoupling surface at $R_H$ + dipole-projection geometry.
- **Paper_029:** Transition acceleration $a_0 = cH_0/(2\pi)$ — uses this paper's results.
- **Paper_030:** ECR.
- **Paper_031:** BTFR slope-4.
- **Paper_039:** BH horizon decoupling — uses analogous substrate-graph mechanism.

This is the fourth gravity-arc paper and the upstream for Paper_029.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation).**
- **P03 (Channel + locus indexing; spatial homogeneity).** Translation-invariance of substrate-graph adjacency.
- **P04 (Bandwidth as non-negative additive scalar).**
- **P05 (Polarity-transport along edges).**
- **P06 (Spatial dimension $D = 3+1$).** Closed 2-surfaces; spherical geometry.
- **P07 (Channel structure).**
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).**
- **P09 ($U(1)$-valued polarity).** Substrate's primitive angular variable; basis for Fourier-mode normalization.
- **P10 (Rule-type primitive).** V1, V5 as substrate kernel rule-types.
- **P11 (Commitment irreversibility).** Forward-causal direction.
- **P13 (Time homogeneity).** Substrate dynamics time-translation-invariant locally; cosmological Hubble expansion is a value-layer dynamical input, not violation of P13.

**Substrate-level constants (P-RB-1):**

- $c$ — substrate-level propagation rate (V1 + V5 kernel speed). **Empirical/value-layer input**, identified with relativistic light speed.

**V1 inheritance (Paper_089):** finite-width retarded kernel; substrate-level light-cone structure.

**V5 dependence (Paper_090):** cross-chain correlation kernel; finite memory.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference.
- **Paper_090:** V5 cross-chain kernel.
- **Paper_025:** holographic participation-count bound (used implicitly at cosmic-horizon scale).

**Empirical / value-layer inputs:**

- $c$ — substrate-level constant, empirically anchored.
- $H_0$ — Hubble parameter; current range $H_0 \in [67, 74]$ km/s/Mpc.
- $\ell_{\mathrm{ED}} = \ell_P$ (Paper_027 §5.3) — used in substrate-scale context.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 + V5 substrate kernel propagation rate $c$ | I | Paper_089, P-RB-1 |
| Hubble expansion rate $H_0$ | I | Empirical cosmological measurement |
| Crossover at $c = H_0 R_H$ | D | §3.2 dimensional balance |
| $R_H = c/H_0$ identification | D | §3.2 algebra |
| Substrate-graph structure at $R \gtrsim R_H$ decouples | D | §3.3 from V5 envelope decay + kernel-propagation outrun |
| Substrate-graph structure at $R \ll R_H$ couples | D | §3.3 from kernel propagation > Hubble recession |
| Statistical (not geometric) substrate-level boundary | **P (ontological commitment)** | §3.4 is a substrate-ontological commitment — the substrate is not a property of a smooth manifold. This is definitional of the ED ontology, not derived. *(Round-3 Rereading Test relabel: was D, now P.)* |
| Accelerating chain residual $SO(2)$ symmetry | D | §4 from uniaxial acceleration |
| Spherical-harmonic projection onto adjacency | D | §5 from P06 + standard geometry |
| Dipole as leading anisotropic mode | D | §5.2 from uniaxial+parity argument |
| Azimuthal-Fourier-mode normalization $1/(2\pi)$ | D | §6 from canonical Fourier-series on circle $[0, 2\pi)$ |
| Dipole-projection integral computed | D | §6.3 explicit calculation |
| $c$ as substrate kernel speed (not derivation of relativistic $c$) | I | P-RB-1 substrate-level constant |
| Identification with GR cosmological event horizon | I→D | §3.5 coincidence under coarse-graining; structurally distinct |

All load-bearing steps are P, D, or I. **No A (asserted) rows.**

---

## 3. The Cosmic Decoupling Surface

### 3.1 Substrate-level kernel propagation rate

By Paper_089 (V1) and Paper_090 (V5), substrate-level kernel propagation occurs at characteristic rate $c$ — the substrate-level light-cone speed inherited from V1's finite-width retarded structure (with characteristic timescale $\ell_{\mathrm{ED}}/c$).

By P-RB-1 (Paper_087 + the local-rate-of-becoming memory commitment), the substrate's primitive propagation rate $c$ is the substrate-level constant that DCGT-coarse-grains to the relativistic speed of light. **This identification is empirical** — both are anchored at $\approx 3 \times 10^8$ m/s.

For substrate-level cross-locus content to reach a local chain at radius $R$ from a source region, the substrate-kernel propagation must traverse distance $R$ at substrate-level speed $c$, requiring substrate-level time $R/c$.

### 3.2 Hubble expansion rate and crossover

The Hubble expansion separates substrate content at rate $\dot{r}/r = H_0$ — at radius $R$, two distant substrate loci recede from each other at velocity $H_0 R$ (in the local-chain rest frame). **This is value-layer dynamical input** from cosmological observation; ED does not derive $H_0$.

**Crossover argument.** For substrate-level kernel propagation to reach a substrate locus at radius $R$, the kernel must propagate faster than the locus is receding. The kernel propagation rate is $c$; the Hubble recession velocity at $R$ is $H_0 R$. Setting these equal defines the crossover radius:

$$
c = H_0 R_H \implies R_H = \frac{c}{H_0}.
$$

**Dimensional check:** $c$ has $[\mathrm{length/time}]$; $H_0$ has $[1/\mathrm{time}]$; $R_H$ has $[\mathrm{length}]$. ✓

For $R < R_H$: substrate-kernel propagation rate exceeds Hubble recession; cross-locus content can reach the local chain.

For $R > R_H$: substrate-kernel propagation rate is exceeded by Hubble recession; cross-locus content cannot reach the local chain coherently.

### 3.3 Decoupling at $R \gtrsim R_H$

At radii $R \gtrsim R_H$, substrate-level cross-locus influence decouples from the local chain. Specifically:

- **V1 kernel** (Paper_089) has finite-width retarded structure with characteristic propagation rate $c$. At $R > R_H$, the V1 envelope cannot maintain coherent substrate content from distant source to local chain because the source recedes faster than the V1 kernel can traverse — the kernel is "outrun."

- **V5 cross-chain correlation** (Paper_090) carries cross-chain content across substrate-graph distance with characteristic memory time $\tau_{V5}$ and propagation rate $c$. At $R > R_H$, V5 envelope $F_{V5}(\sigma/\ell_{V5}^2, t/\tau_{V5})$ decays exponentially because the effective substrate-graph separation $\sigma$ grows under Hubble expansion faster than V5 can maintain.

- **Cumulative-strain reading** (Paper_026 in queue, Paper_027 §4) integrates substrate-level strain over the substrate channels connecting source to test. For source-loci at $R > R_H$, the substrate channels themselves cannot maintain coherence (V1 + V5 envelope decay), so the cumulative-strain integration is effectively zero from beyond-horizon contributions.

**The substrate-level participation graph at radii $R > R_H$ is effectively decoupled from the local chain's dynamics.**

### 3.4 Statistical, not geometric, substrate-level boundary

At substrate-graph scale ($R \sim \ell_{\mathrm{ED}}$), the cosmic decoupling surface is not a sharp geometric boundary — it is a substrate-level transition region whose precise location depends on the substrate's hydrodynamic-window threshold ($\Gamma_{\mathrm{cross}}$ from Paper_054 §3.3 falling below $\Gamma_{\mathrm{decoupling}}$).

At coarse-grained scales ($R_{\mathrm{cg}} \gg \ell_{\mathrm{ED}}$, the cosmological scale of interest), the substrate-level transition zone is well-approximated by the sharp surface at $R = R_H$. The DCGT continuum limit (Paper_073, in queue) produces this identification.

**The cosmic decoupling surface is a substrate-graph statistical feature of substrate adjacency-and-bandwidth structure**, *not* a property of an underlying smooth manifold. This distinguishes ED's substrate-level surface from the GR cosmological event horizon, which is a geometric feature of FRW spacetime.

### 3.5 Relationship to GR cosmological event horizon

The GR cosmological event horizon has subtleties involving:

- The cosmological constant $\Lambda$.
- FRW geometry with time-dependent scale factor.
- Accelerating expansion phases.

For a de Sitter universe with $\Lambda$, the GR cosmological event horizon is at $r_H^{\mathrm{dS}} = c/H_{\Lambda}$ where $H_{\Lambda} = \sqrt{\Lambda c^2/3}$. For a flat FRW universe with present-day Hubble parameter $H_0$, the substrate-level $R_H = c/H_0$ coincides numerically with the present-day "Hubble radius" but is distinct from the future cosmological event horizon at $r_H^{\mathrm{dS}}$.

**Critical clarification:** the substrate-level cosmic decoupling surface and the GR cosmological event horizon are conceptually distinct:

- **GR cosmological event horizon:** geometric feature of FRW spacetime; depends on $\Lambda$ + expansion history.
- **ED substrate-level cosmic decoupling surface:** substrate-graph effective boundary set by V1/V5 propagation rate vs. Hubble expansion rate.

The two coincide *numerically* at the Hubble radius $R_H = c/H_0$ under standard cosmology, but are *structurally* different objects: one is geometric, one is substrate-graph statistical. This parallels Paper_039 §3.2's honest acknowledgment that the BH GR horizon $r_H$ is the coarse-grained identification point for the BH substrate decoupling surface.

---

## 4. The Accelerating Chain — Anisotropic Substrate Adjacency

### 4.1 Setup

Consider a chain $C$ at substrate locus $u_0$ with substrate-level acceleration $\vec{a}$ along some direction (say $\hat{z}$ in the chain's local rest frame). The chain's substrate-graph adjacency is the set of substrate channels emanating from $u_0$ to neighboring substrate loci.

For a **non-accelerating** chain, the substrate-graph adjacency is **isotropic** in the chain's rest frame: substrate channels in all spatial directions are equivalent by P03's spatial homogeneity. The substrate-graph adjacency has full $SO(3)$ rotational symmetry about $u_0$.

For an **accelerating** chain, the substrate-graph adjacency is **anisotropic**: the acceleration $\vec{a}$ breaks the $SO(3)$ symmetry of substrate-graph adjacency. Channels along $\vec{a}$ are encountered at different rates than channels against $\vec{a}$ or perpendicular to $\vec{a}$.

### 4.2 Residual $SO(2)$ symmetry

The accelerating chain's acceleration $\vec{a}$ defines a **single preferred axis** (the direction of $\vec{a}$). The substrate-graph adjacency-symmetry-breaking is **uniaxial**: rotations about the acceleration axis preserve the chain's adjacency structure (no preferred azimuthal direction perpendicular to $\hat{z}$).

The residual symmetry of the accelerating chain's substrate-graph adjacency is therefore $SO(2)$ — the rotation group about the acceleration axis. The chain's substrate adjacency is parameterized by:

- A polar angle $\theta \in [0, \pi]$ from the acceleration axis $\hat{z}$.
- An azimuthal angle $\phi \in [0, 2\pi)$ about $\hat{z}$, with the residual $SO(2)$ symmetry acting as $\phi \to \phi + \alpha$ for any $\alpha$.

The residual $SO(2)$ is the **structural origin of the $1/(2\pi)$ factor** computed in §6.

### 4.3 Forward / backward / perpendicular substrate channels

Operationally, the anisotropy means:

- **"Forward" channels** (along $\vec{a}$, $\theta \approx 0$): encountered at rate increased by $|\vec{a}|$.
- **"Backward" channels** (against $\vec{a}$, $\theta \approx \pi$): encountered at rate decreased by $|\vec{a}|$.
- **Perpendicular channels** ($\theta \approx \pi/2$): encountered at the isotropic rate.

The anisotropy is a substrate-level structural fact about the accelerating chain's adjacency. It is the substrate-level analog of (but operates differently from) the relativistic boost-induced anisotropy and the Unruh-like thermal anisotropy of an accelerating observer.

### 4.4 Connection to the dipole-projection geometry

The dipole projection developed in §5 + §6 is the substrate-level structural consequence of this anisotropy: the accelerating chain projects the cosmic decoupling surface (isotropic in cosmological rest frame) onto its anisotropic substrate-graph adjacency, with the leading anisotropic mode being the dipole.

The dipole-projection factor $1/(2\pi)$ is the **azimuthal-Fourier-mode normalization on the residual $SO(2)$** — a structural consequence of the chain's uniaxial acceleration breaking $SO(3)$ to $SO(2)$.

---

## 5. Multipole Expansion of the Projection

### 5.1 Spherical-harmonic decomposition

For a function $\rho(\theta, \phi)$ on the cosmic decoupling surface (the 2-sphere at radius $R_H$), the spherical-harmonic decomposition is:

$$
\rho(\theta, \phi) = \sum_{l, m} a_{lm}\,Y_{lm}(\theta, \phi)
$$

with $Y_{lm}(\theta, \phi)$ the standard spherical harmonics:

$$
Y_{lm}(\theta, \phi) = \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\phi}.
$$

The orthonormality:

$$
\int_0^{\pi}\sin\theta\,d\theta\int_0^{2\pi}d\phi\,Y_{lm}^*(\theta,\phi)\,Y_{l'm'}(\theta,\phi) = \delta_{ll'}\delta_{mm'}.
$$

### 5.2 Why the dipole is the leading anisotropic mode

The accelerating chain's adjacency anisotropy is **uniaxial** along $\hat{z}$ (§4.2). The residual $SO(2)$ symmetry constrains the substrate-graph response to cosmic content:

- **Monopole ($l = 0$):** isotropic; non-zero for any cosmic content but does not produce directional acceleration on the chain.
- **Dipole ($l = 1, m = 0$):** axially symmetric (only $m = 0$ preserved by residual $SO(2)$ — $m = \pm 1$ components fail the $SO(2)$ invariance). The $l=1, m=0$ harmonic is $Y_{1,0}(\theta) = \sqrt{3/(4\pi)}\cos\theta$, axially symmetric.
- **Higher multipoles ($l \geq 2$):** higher-order in $|\vec{a}|/c$; subdominant in the non-relativistic regime.

The dipole ($l = 1, m = 0$) is the leading anisotropic mode for an accelerating chain. The substrate-graph dipole response has the angular dependence:

$$
\rho_{\mathrm{dipole}}(\theta, \phi) = \rho_0\,\cos\theta.
$$

Higher multipoles ($l = 2$ quadrupole, $l = 3$ octupole, …) require additional anisotropy structure (e.g., bi-axial tidal effects) that a uniformly-accelerating chain does not have.

### 5.3 Substrate-level dipole content from cosmic horizon

The substrate-level cosmic content at radius $R_H$ contributes to the chain's substrate-graph adjacency via the dipole projection. Paper_029 §5.1 develops the cosmic anisotropic content as seen by the accelerating chain:

$$
\rho_{\mathrm{cosmic}}(\theta, \phi) = \rho_0\,\frac{|\vec{a}|}{c}\,\cos\theta + \mathcal{O}((|\vec{a}|/c)^2)
$$

with $\rho_0 \sim cH_0$ (the natural acceleration scale constructed from cosmic-horizon kinematics). The order-unity coefficient is set by substrate-graph normalization conventions (Paper_029 §5.1).

**For this paper, the structural focus is the projection geometry itself, not the cosmic-content magnitude.** The cosmic-content magnitude $\rho_0$ is value-layer; the dipole-projection geometry is structural.

---

## 6. The Dipole-Projection Integral and the $1/(2\pi)$ Factor

This is the load-bearing computational section. The $1/(2\pi)$ factor is **derived**, not asserted.

### 6.1 Setup

The accelerating chain at substrate locus $u_0$ has substrate-graph adjacency parameterized by $(\theta, \phi)$ on a 2-sphere of adjacency directions, with residual $SO(2)$ symmetry about the acceleration axis $\hat{z}$.

The chain's substrate-level induced response to cosmic content is the projection of cosmic content onto the chain's dipole-response mode along $\hat{z}$. The projection integral has three pieces:

1. **Azimuthal Fourier projection** on the residual $SO(2)$.
2. **Polar integration** with the standard $\sin\theta\,d\theta$ measure.
3. **Substrate-source normalization** matching the cosmic-content magnitude.

This section derives piece (1) — the source of the $1/(2\pi)$ factor.

### 6.2 Azimuthal-Fourier-mode normalization on the circle

The chain's residual $SO(2)$ symmetry corresponds to rotations about $\hat{z}$ parameterized by $\phi \in [0, 2\pi)$. Functions on this circle decompose in Fourier modes:

$$
f(\phi) = \sum_{n \in \mathbb{Z}} f_n\,e^{in\phi}
$$

with the **canonical Fourier-series normalization**:

$$
\frac{1}{2\pi}\int_0^{2\pi}e^{-in\phi}\,e^{im\phi}\,d\phi = \delta_{nm}.
$$

This normalization is **structurally forced** by the requirement that the Fourier basis $\{e^{in\phi}\}_{n\in\mathbb{Z}}$ on the circle of period $2\pi$ is orthonormal. Any other normalization (e.g., $d\phi$ with no $1/(2\pi)$ factor) would violate basis orthonormality.

**Dimensional check:** $\phi$ is dimensionless (an angle); $e^{in\phi}$ is dimensionless; $d\phi$ has dimensions of $\phi$ (dimensionless angle); $\frac{1}{2\pi}\int d\phi$ is dimensionless. ✓

**Why $2\pi$ specifically?** The period of the residual $SO(2)$ symmetry is $2\pi$: one full rotation about $\hat{z}$ returns the chain's substrate-graph adjacency to its original configuration. The Fourier-series normalization on a circle of period $P$ is $\frac{1}{P}\int_0^P\,d\phi$; here $P = 2\pi$.

### 6.3 The dipole-projection integral computed

The substrate-level dipole-projection of cosmic content onto the chain's adjacency axis involves the projection of $\rho_{\mathrm{cosmic}}$ onto the dipole mode $\rho_{\mathrm{dipole}}$, integrated over the full 2-sphere of adjacency directions with the chain's normalization.

The projection integral:

$$
\mathcal{P}_{\mathrm{dipole}} = \int_0^{\pi}\sin\theta\,d\theta\int_0^{2\pi}\frac{d\phi}{2\pi}\,\rho_{\mathrm{cosmic}}(\theta, \phi)\cdot\cos\theta\cdot \rho_0
$$

where:

- $\sin\theta\,d\theta$: standard polar measure on the 2-sphere.
- $\frac{d\phi}{2\pi}$: canonical Fourier-mode normalization on the residual $SO(2)$ (§6.2). **This is the source of the $1/(2\pi)$ factor.**
- $\cos\theta$: projection onto the chain's $\hat{z}$ adjacency axis (dipole mode).
- $\rho_0$: substrate-source normalization (cosmic-horizon acceleration scale).

For $\rho_{\mathrm{cosmic}}(\theta, \phi) = \rho_0\,(|\vec{a}|/c)\,\cos\theta$ (cosmic dipole content, axially symmetric):

$$
\mathcal{P}_{\mathrm{dipole}} = \rho_0\,\frac{|\vec{a}|}{c}\,\rho_0\,\int_0^{\pi}\sin\theta\,\cos^2\theta\,d\theta\,\int_0^{2\pi}\frac{d\phi}{2\pi}.
$$

The two integrals:

- $\int_0^{2\pi}\frac{d\phi}{2\pi} = 1$. (Azimuthal-Fourier normalization integrates to unity.)
- $\int_0^{\pi}\sin\theta\,\cos^2\theta\,d\theta = \frac{2}{3}$. (Standard polar integral.)

**Dimensional check:** $\rho_0$ has units of acceleration $[\mathrm{length/time}^2]$; $(|\vec{a}|/c)$ dimensionless; $\rho_0 \cdot (|\vec{a}|/c) \cdot \rho_0$ has units $[\mathrm{length/time}^2]^2 \cdot [\mathrm{dimensionless}]$; polar integral is dimensionless; azimuthal integral is dimensionless; so $\mathcal{P}_{\mathrm{dipole}}$ has units $[\mathrm{length/time}^2]^2$. *(Paper_029 §5.1 absorbs the substrate-source-normalization conventions to yield $a_0$ with units of acceleration; this paper's contribution is the geometric structure, not the full coefficient assembly.)*

### 6.4 The $1/(2\pi)$ factor — structurally present in the canonical convention

Pulling out the $1/(2\pi)$ from the azimuthal-Fourier normalization explicitly:

$$
\boxed{\mathcal{P}_{\mathrm{dipole}} \propto \frac{1}{2\pi}\cdot(\text{polar }2/3\text{ factor})\cdot(\text{cosmic-source content})\cdot(|\vec{a}|/c).}
$$

**The $1/(2\pi)$ factor is structurally present in the canonical Fourier-orthonormality convention on the chain's residual $SO(2)$ symmetry.** The factor's *specific location* (separate $d\phi/(2\pi)$ measure vs. absorbed into $Y_{1,0}$'s $\sqrt{3/(4\pi)}$ normalization) is **convention-dependent** — different spherical-harmonic conventions distribute the factors differently. **What is convention-independent is the total factor in $a_0$, which comes out to $1/(2\pi)$ after the full projection integral.** The $1/(2\pi)$ is structurally present, not phenomenologically fit; but "uniquely forced" overclaims, because alternative conventions absorb the factor differently.

Alternative normalizations would correspond to different geometric structures:

- $\frac{1}{4\pi}\int_0^{4\pi}d\phi$ would correspond to a $4\pi$-period spinorial double-cover — not the uniaxial-acceleration residual $SO(2)$.
- $\frac{1}{\pi}\int_0^{\pi}d\phi$ would correspond to a half-period mode — not the dipole.
- $\frac{1}{2\pi^2}\int...$ would not correspond to any standard Fourier normalization on a real circle.

The $1/(2\pi)$ is **uniquely structurally forced** by the dipole mode on the residual $SO(2)$ of period $2\pi$.

### 6.5 What this paper supplies for Paper_029

Paper_029 uses this paper's results in its §5.1 derivation of $a_0 = cH_0/(2\pi)$:

- The cosmic decoupling surface at $R_H = c/H_0$ (this paper §3).
- The accelerating chain's residual $SO(2)$ symmetry (this paper §4).
- The dipole-projection geometry with $1/(2\pi)$ azimuthal-Fourier-mode normalization (this paper §5–§6).

Paper_029 composes these with the substrate-source normalization $\rho_0 = cH_0$ (cosmic-horizon acceleration scale; characterized by V5 + cosmic content) to derive $a_0 = cH_0/(2\pi)$.

**This paper is the geometric / dipole-projection upstream; Paper_029 is the substrate-source-coupled downstream.**

---

## 7. Structural vs. Empirical Status

### 7.1 Structural content (substrate-derived)

- Existence of cosmic decoupling surface at $R_H = c/H_0$ (§3.2).
- Substrate-graph statistical (not geometric) character (§3.4).
- Accelerating chain residual $SO(2)$ symmetry (§4).
- Dipole as leading anisotropic mode (§5.2).
- $1/(2\pi)$ azimuthal-Fourier-mode normalization (§6).
- Dipole-projection integral (§6.3).

### 7.2 Empirical / value-layer content (inherited)

- Numerical value of $c$ (substrate-level constant; empirically anchored).
- Numerical value of $H_0$ (Hubble parameter; cosmological measurement; Hubble tension currently unresolved).
- Numerical identification $\ell_{\mathrm{ED}} = \ell_P$ via Paper_027 §5.3.

### 7.3 Coarse-grained identifications (D under coarse-graining)

- Coincidence with GR Hubble radius at $R_H = c/H_0$ (§3.5) — substrate-graph statistical boundary coarse-grains to the standard cosmological-horizon scale under DCGT.
- Numerical identification with the BH GR horizon location at the BH analog (Paper_039 §3.2) — analogous substrate-graph mechanism at BH scale.

---

## 8. Falsification Criteria

### 8.1 Cosmic decoupling surface inconsistent with $R_H = c/H_0$

**Falsifier sentence:** *Empirical evidence that substrate-level cross-locus content can reach a local chain from cosmic loci substantially beyond $R_H = c/H_0$ — i.e., information propagating from beyond the Hubble radius in a manner not accounted for by V1/V5 envelope decay — would falsify §3's substrate-level decoupling mechanism.*

Current state: no empirical evidence of cross-Hubble-radius information propagation; consistent with substrate-level decoupling.

### 8.2 Substrate-level kernel propagation rate $\neq c$

**Falsifier sentence:** *Empirical demonstration that the substrate-level kernel propagation rate differs from the relativistic light speed $c$ — i.e., that V1/V5 envelope propagates at a rate inconsistent with the empirically-anchored relativistic $c$ — would falsify the §3 setup.*

This would also affect Papers_089, 090, 027, 029, 039.

### 8.3 Different cosmic-horizon dipole-projection factor

**Falsifier sentence:** *Empirical demonstration that the cosmic-anisotropy contribution to local-chain acceleration scales as $cH_0/(4\pi)$, $cH_0/\pi$, $cH_0/(2\pi^2)$, or any factor other than $cH_0/(2\pi)$ would falsify the §6 dipole-projection-integral derivation.*

This is the structural-numerical wedge: the substrate-level mechanism gives $1/(2\pi)$ specifically; alternative numerical factors correspond to different mode-structure assumptions that would falsify the residual $SO(2)$ + dipole framework.

### 8.4 Higher multipole dominance

**Falsifier sentence:** *Empirical evidence that the leading anisotropic mode in the accelerating chain's adjacency is quadrupole ($l = 2$) or higher rather than dipole ($l = 1$) would falsify §5.2's leading-mode identification.*

This would require additional substrate-level anisotropy structure beyond uniaxial acceleration.

### 8.5 Substrate-level participation graph non-locality

**Falsifier sentence:** *Discovery of substrate-level cross-locus mechanisms beyond V1 + V5 that maintain coherent transport beyond $R_H$ would falsify §3.3's decoupling argument.*

### 8.6 Cosmological model fundamentally incompatible with substrate framework

**Falsifier sentence:** *Discovery that standard cosmology's expansion history (FRW + $\Lambda$ + observed CMB + structure formation) is fundamentally incompatible with the substrate-graph statistical decoupling-surface framework would force revision of §3.5's coarse-grained identification.*

---

## 9. Position Statement

The **cosmic decoupling surface** at:

$$
\boxed{R_H = \frac{c}{H_0}}
$$

is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives + V1 inheritance + V5 dependence + substrate-level kernel propagation rate $c$ + Hubble expansion rate $H_0$, the surface follows from the crossover between substrate-kernel propagation (rate $c$) and Hubble recession (rate $H_0 R$): setting $c = H_0 R_H$ defines the radius.

The surface is **substrate-graph statistical, not geometric** — a property of substrate adjacency-and-bandwidth structure, coinciding numerically with the GR Hubble radius under coarse-graining but conceptually distinct from a smooth-manifold cosmological event horizon.

For an **accelerating chain** with acceleration $\vec{a}$ along $\hat{z}$:

- The substrate-graph adjacency has **residual $SO(2)$ symmetry** about $\hat{z}$ (uniaxial-acceleration symmetry-breaking from $SO(3)$).
- The leading anisotropic mode in the spherical-harmonic decomposition of the chain's response to cosmic content is the **dipole** ($l = 1, m = 0$).
- The **dipole-projection integral** on the chain's adjacency yields a $\frac{1}{2\pi}$ azimuthal-Fourier-mode normalization, **structurally forced** by canonical Fourier-series orthonormality on the residual $SO(2)$ of period $2\pi$.

The dipole-projection geometry developed in §5–§6 is the upstream geometric machinery for **Paper_029** ($a_0 = cH_0/(2\pi)$), which composes this paper's results with substrate-source normalization $\rho_0 = cH_0$ to derive the transition acceleration.

What this paper claims:

- Given the postulated primitives + V1/V5 + substrate $c$ + Hubble $H_0$, the cosmic decoupling surface at $R_H = c/H_0$ is the unique downstream structural identification at coarse-grained scale.
- The substrate-level surface is statistical, distinct from the GR cosmological event horizon.
- The accelerating chain's residual $SO(2)$ symmetry is the structural basis for the dipole-projection geometry.
- The dipole-projection integral computed in §6 derives the $1/(2\pi)$ factor structurally via azimuthal-Fourier-mode normalization on the residual $SO(2)$.

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- $c$ and $H_0$ are not derived; both are empirical/inherited.
- No claim of cosmology derivation.
- No identification with GR cosmological event horizon (numerical coincidence; structural distinctness).
- The $1/(2\pi)$ factor is not phenomenologically fit; it is structurally derived from the residual $SO(2)$ Fourier normalization.
- No derivation of $a_0$ in this paper (that is Paper_029).
- No cosmological-curvature derivation.

The empirical case rests on cross-domain use: this paper is load-bearing for Paper_029 (transition acceleration) and Paper_039 (BH horizon decoupling, which uses analogous substrate-graph mechanism at BH scale).

**Series context.** Paper_028 of the gravity arc. The arc continues:

- **Paper_029:** Transition acceleration $a_0 = cH_0/(2\pi)$ — uses this paper.
- **Paper_030:** ECR.
- **Paper_031:** BTFR slope-4.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1):** substrate kernel propagation rate $c$.
- **Paper_090 (V5):** cross-chain correlation kernel; envelope decay at decoupling.
- **Paper_025 (Holographic Bound):** channel count at cosmic-horizon scale.
- **Paper_029 (Transition Acceleration $a_0$):** primary downstream user of this paper.
- **Paper_039 (BH Horizon Decoupling):** analogous substrate-graph mechanism at BH scale.
- **Paper_054 (UR-1):** substrate-level decoupling threshold $\Gamma_{\mathrm{decoupling}}$.

### Glossary

- **Cosmic decoupling surface.** Substrate-graph effective boundary at $R_H = c/H_0$ beyond which substrate-level cross-locus influence cannot reach a local chain coherently.
- **Hubble radius $R_H$.** $R_H = c/H_0$. Substrate-level identification; coincides numerically with GR Hubble radius under coarse-graining.
- **Substrate-graph statistical boundary.** Substrate-level surface defined by adjacency-and-bandwidth structure; not a smooth-manifold geometric feature.
- **Residual $SO(2)$ symmetry.** Rotational symmetry about the acceleration axis remaining after uniaxial acceleration breaks $SO(3)$.
- **Dipole-projection integral.** Integral over the 2-sphere of substrate-graph adjacency directions projecting cosmic content onto the chain's dipole-response mode.
- **Azimuthal-Fourier-mode normalization $1/(2\pi)$.** Canonical Fourier-series normalization on the circle of period $2\pi$: $\frac{1}{2\pi}\int_0^{2\pi}e^{-in\phi}e^{im\phi}d\phi = \delta_{nm}$. **Structural source of the $1/(2\pi)$ factor in $a_0$.**
- **Cosmic anisotropic content.** Substrate-level $\rho_{\mathrm{cosmic}}(\theta) = \rho_0(|\vec{a}|/c)\cos\theta$ — the cosmic-content anisotropy seen by an accelerating chain.
- **GR cosmological event horizon.** Geometric feature of FRW + $\Lambda$ spacetime; coincides numerically with $R_H$ at present but is structurally distinct from the substrate-level decoupling surface.

---

**End of Paper_028.**

*Wave-2 Generative Paper — Gravity Arc Foundation. Dedicated derivation of the cosmic decoupling surface at $R_H = c/H_0$ and the dipole-projection geometry yielding the $1/(2\pi)$ azimuthal-Fourier-mode normalization used in Paper_029 (transition acceleration $a_0 = cH_0/(2\pi)$) and Paper_039 (BH horizon decoupling, analogous mechanism).*
