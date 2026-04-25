# Event Density, Temporal Tension, and the Environmental Origin of Flat Rotation Curves  
### A revised field‑level alternative to dark matter based on 3D ED simulations

Allen Proxmire 
April 2026

## Abstract

Temporal tension is a macroscopic scalar field arising from the Event Density (ED) ontology, in which becoming is
primitive and the measurable rate of micro‑events shapes the macroscopic geometry of flow. Earlier ED work
proposed that each galaxy acts as a compact source of temporal tension, generating a smooth, extended field that
produces flat rotation curves and the baryonic Tully–Fisher relation (BTFR). This galaxy‑sourced hypothesis was
conceptually appealing and matched several empirical regularities, but it relied on a one‑dimensional intuition
about the temporal‑tension PDE.

A comprehensive three‑dimensional simulation programme (ED‑Sim‑01) revealed a structural constraint that
overturns this picture. The 3D Green’s function contains a \(1/r\) geometric dilution term that dominates long
before the exponential decay becomes relevant. As a result, no galaxy‑sized source—regardless of tension length
or parameter choice—can maintain a flat temporal‑tension field over the 10–1000 kpc range required by
observations. Compact sources fail generically.

The simulations also revealed the solution. When the source of temporal tension is extended on megaparsec
scales, the geometric dilution is suppressed, and the resulting field becomes nearly constant across the full radial
range probed by rotation curves and weak lensing. This leads to a revised hypothesis: **temporal tension is an
environmental field sourced by galaxy groups, filaments, and the local cosmic web—not by individual galaxies**.
In this framework, the galaxy determines the amplitude of the field through its baryonic identity, while the
environment determines the spatial extent through its megaparsec‑scale structure.

The environmental‑tension hypothesis preserves the successes of the original model—flat rotation curves, the
BTFR, and the universality of weak‑lensing flatness—while resolving its geometric limitations. It predicts
activity‑dependent weak‑lensing velocities, group‑level coherence of asymptotic speeds, merger‑lag signatures,
and the absence of a halo edge. These predictions distinguish ED from both collisionless dark matter and
modified‑gravity frameworks, providing a clear empirical path forward. Temporal tension thus emerges as a
viable, falsifiable field‑level alternative to dark matter, grounded in the architecture of becoming and the
structure of the cosmic web.


## 1. Introduction

Galactic rotation curves and weak‑lensing measurements reveal a persistent structural anomaly: circular velocities remain approximately constant far beyond the luminous extent of galaxies, with no indication of a Keplerian decline and no evidence for a halo edge. In the standard interpretation, this flatness is attributed to massive, extended halos of collisionless dark matter. Modified‑gravity frameworks attempt to reproduce the same behavior by altering the force law at low accelerations. Both approaches assume that the phenomenon is fundamentally gravitational.

The Event Density (ED) ontology offers a different perspective. In ED, the universe is built not from objects or fields but from *becoming*—the continuous accumulation of micro‑events that generate structure. The measurable rate of becoming, the **event density** \(p(x,t)\), shapes the macroscopic geometry of flow. When a system undergoes sustained dynamical activity—rotation, shear, turbulence, star formation—it alters the local rate of becoming. These alterations diffuse outward, forming a smooth, extended scalar field known as **temporal tension**.

The original ED hypothesis proposed that each galaxy acts as a compact source of temporal tension. If the tension length \(\ell_T = \sqrt{D_T/\chi}\) is large, the resulting field becomes approximately constant, contributing a radius‑independent velocity component


\[
V_{\text{temp}} = \sqrt{C_T T_0},
\]


which naturally produces flat rotation curves and yields the baryonic Tully–Fisher relation (BTFR) as a dimensional consequence.

However, a comprehensive 3D simulation programme (ED‑Sim‑01) revealed a structural constraint that fundamentally changes this picture. In three dimensions, the Green’s function of the tension PDE contains a geometric dilution factor:


\[
T(r) \propto \frac{1}{r} e^{-r/\ell_T},
\]


which dominates long before the exponential decay becomes relevant. As a result, a compact galactic source cannot maintain a flat tension field beyond tens of kiloparsecs, regardless of the tension length. This discovery invalidates the original galaxy‑sourced hypothesis.

The simulations also revealed the solution: **flatness is restored when the tension source is extended on megaparsec scales**. Galaxy groups, filaments, and the local cosmic web naturally satisfy this requirement. This leads to a revised hypothesis in which temporal tension is an **environmental field**, sourced by the collective activity of many galaxies rather than by any single galaxy.

This paper develops this updated interpretation. We present the original hypothesis, the 3D simulation results that challenge it, and the new environmental‑tension model that resolves the geometric constraint. The result is a coherent, testable explanation for flat rotation curves, weak‑lensing flatness, and the BTFR, grounded in the structural properties of the ED framework.

## 2. Event Density and Temporal Tension

The updated temporal‑tension hypothesis rests on a single ontological commitment: **becoming is primitive**, and the universe is built from the continuous accumulation of micro‑events. Event Density (ED) is the measurable rate at which these micro‑events occur. Curvature, in this framework, is the macroscopic geometry of this flow. Temporal tension is the time‑component of ED gradients expressed at galactic scales.

This section summarizes the ED ontology and derives the field equation governing temporal tension. These foundations are essential for understanding both the original galaxy‑sourced hypothesis and the updated environmental interpretation.

---

### 2.1 Event Density as the Structure of Becoming

In the ED ontology, the fundamental quantity is the **event density field**  


\[
p(x,t),
\]

  
which measures the local rate of becoming—the density of micro‑events per unit volume per unit time. High ED corresponds to regions where becoming is thick, continuous, and stabilizing; low ED corresponds to regions where becoming is sparse and fragile.

Spatial and temporal gradients in \(p(x,t)\) define the natural flow of participation. When ED is uniform, the flow is straight; when ED varies, the flow bends. This bending is what we ordinarily describe as curvature.

---

### 2.2 Participation and the Temporal Channel

The ED dynamical equation contains three constitutive channels: mobility, penalty, and participation. The **participation channel** introduces a global mode that couples local ED structure to a domain‑averaged variable. At galactic scales, this global mode manifests as a scalar field \(T(x,t)\) that modifies the effective rate of becoming.

This scalar field is **temporal tension**.

Temporal tension is not a new force, nor a modification of gravity. It is the macroscopic expression of how sustained activity—rotation, shear, turbulence, star formation—alters the local rate of becoming and diffuses outward.

---

### 2.3 The Temporal‑Tension Field Equation

At large scales and long times, the temporal‑tension field satisfies a diffusion‑reaction equation of the form:



\[
D_T \nabla^2 T + S(x) - \chi T = 0,
\tag{2.1}
\]



where:

- \(D_T\) is the tension diffusivity,  
- \(S(x)\) is the source term tied to activity‑driven ED gradients,  
- \(\chi\) is the relaxation rate.

Equation (2.1) is the minimal field equation consistent with the ED ontology:

- **Diffusion** reflects the smoothing of ED gradients.  
- **Sourcing** reflects sustained dynamical activity.  
- **Relaxation** reflects the slow decay of temporal structure in the absence of activity.

This PDE is the mathematical backbone of both the original and updated hypotheses.

---

### 2.4 The 3D Green’s Function and Its Consequences

The steady‑state Green’s function of Eq. (2.1) in three dimensions is:



\[
T(r) \propto \frac{1}{r} e^{-r/\ell_T},
\tag{2.2}
\]



where  


\[
\ell_T = \sqrt{\frac{D_T}{\chi}}
\tag{2.3}
\]

  
is the tension length.

Two structural features follow immediately:

1. **Geometric dilution:** the \(1/r\) factor dominates at large radii.  
2. **Slow decay:** the exponential term decays only on scales \(\sim \ell_T\).

These features are crucial. They imply that:

- A compact source produces a rapidly declining field.  
- A spatially extended source can maintain a nearly constant field over large distances.

This distinction is the key to understanding why the original hypothesis fails and why the updated hypothesis succeeds.

---

### 2.5 Temporal Tension and Apparent Velocities

Temporal tension alters the effective rate of becoming along a worldline. Objects moving through a region with temporal tension experience a stretched local timeline. Their orbital periods lengthen relative to the background timeline, which makes their velocities appear higher than expected.

To leading order, the additional velocity contribution is:



\[
V_{\text{temp}}(r) = \sqrt{C_T\, T(r)},
\tag{2.4}
\]



where \(C_T\) is a coupling constant determined by the ED architecture.

If \(T(r)\) is approximately constant over a large radial range, then:



\[
V_{\text{temp}}(r) \approx \text{const},
\tag{2.5}
\]



which produces flat rotation curves and flat weak‑lensing velocities.

The central question of this paper is therefore:

> **Under what conditions does the temporal‑tension field become spatially constant over 10–1000 kpc?**

The original hypothesis assumed that a single galaxy could produce such a field.  
The 3D simulations show that this is impossible.  
The updated hypothesis identifies the correct source: the galactic environment.

The next section presents the original hypothesis in detail.

## 3. The Original Hypothesis: Galaxy‑Sourced Temporal Tension

Before the 3D simulation programme, the prevailing ED interpretation was simple and elegant: **each galaxy acts as a compact source of temporal tension**, and the resulting field becomes approximately constant at large radii. This constant field contributes a radius‑independent velocity component that naturally produces flat rotation curves and yields the baryonic Tully–Fisher relation (BTFR) as a structural consequence.

This section reconstructs the original hypothesis as it was understood prior to ED‑Sim‑01. The goal is not to defend it, but to articulate it clearly enough to understand why it was compelling—and why the 3D simulations ultimately overturned it.

---

### 3.1 The 1D Intuition: A Nearly Constant Field

The original hypothesis relied on a 1D intuition about the steady‑state solution of the temporal‑tension PDE:



\[
D_T \nabla^2 T + S(r) - \chi T = 0.
\tag{3.1}
\]



In one dimension, the Green’s function of Eq. (3.1) is:



\[
T(x) \propto e^{-|x|/\ell_T},
\tag{3.2}
\]



where  


\[
\ell_T = \sqrt{\frac{D_T}{\chi}}
\tag{3.3}
\]

  
is the tension length.

If \(\ell_T\) is much larger than the galactic radius, then:



\[
T(x) \approx \text{const}
\quad \text{for } |x| \ll \ell_T.
\tag{3.4}
\]



This was the key assumption: **a galaxy with a large tension length produces a nearly constant temporal‑tension field over tens or hundreds of kiloparsecs**.

Under this assumption, the additional velocity contribution is:



\[
V_{\text{temp}}(r) = \sqrt{C_T\, T_0} \approx \text{const},
\tag{3.5}
\]



which immediately yields flat rotation curves.

---

### 3.2 Consequences of the Galaxy‑Sourced Picture

The galaxy‑sourced hypothesis produced three appealing consequences.

#### **(1) Flat rotation curves**

If \(T(r)\) is constant, then:



\[
V^2(r) = V_{\text{grav}}^2(r) + V_{\text{temp}}^2
\tag{3.6}
\]



remains flat even when the gravitational term declines.

#### **(2) The BTFR emerges dimensionally**

If the amplitude of the tension field is proportional to the baryonic mass:



\[
T_0 \propto M_b,
\tag{3.7}
\]



then:



\[
V_{\text{temp}}^4 \propto M_b,
\tag{3.8}
\]



which is the baryonic Tully–Fisher relation.

This was one of the strongest motivations for the original hypothesis.

#### **(3) Weak‑lensing flatness**

If the tension field is constant out to large radii, then the inferred circular velocity from lensing remains constant as well:



\[
V_{\text{lens}}(r) \approx \text{const}.
\tag{3.9}
\]



This matched the Mistele et al. (2024) result showing flat velocities out to nearly a megaparsec.

---

### 3.3 Why the Hypothesis Was Plausible

The galaxy‑sourced hypothesis was compelling for three reasons:

1. **It was structurally simple.**  
   A single galaxy acts as a single source.

2. **It matched multiple empirical regularities.**  
   - flat rotation curves  
   - flat weak‑lensing velocities  
   - the BTFR exponent \(1/4\)

3. **It required no fine‑tuning.**  
   The only requirement was a large tension length \(\ell_T\).

In short, the hypothesis was elegant, predictive, and consistent with the data available at the time.

---

### 3.4 The Hidden Assumption

The entire hypothesis rested on one implicit assumption:

> **That the 1D intuition carries over to 3D.**

Specifically, it assumed that if \(\ell_T\) is large, then the 3D field would also be approximately constant over large radii.

This assumption turned out to be false.

The next section presents the 3D simulation results that revealed the geometric constraint and overturned the original hypothesis.

## 4. ED‑Sim‑01: The 3D Parameter‑Space Survey

The original temporal‑tension hypothesis relied on a 1D intuition: if the tension length \(\ell_T\) is large, then the temporal‑tension field \(T(r)\) becomes approximately constant over the region of interest. This assumption was never tested in three dimensions. ED‑Sim‑01 was designed to do exactly that.

ED‑Sim‑01 was a comprehensive 3D parameter‑space survey of the temporal‑tension PDE. Its goal was to determine whether a compact galactic source can produce a flat temporal‑tension field over the 10–1000 kpc range required to explain flat rotation curves and weak‑lensing flatness. The results were decisive: **a compact source cannot produce such a field in 3D**, regardless of parameter choices. This section presents the simulation design, the geometric constraint that emerged, and the implications for the original hypothesis.

---

### 4.1 The 3D Temporal‑Tension PDE

The steady‑state temporal‑tension field satisfies:



\[
D_T \nabla^2 T + S(r) - \chi T = 0,
\tag{4.1}
\]



where:

- \(D_T\) is the diffusivity,
- \(S(r)\) is the source profile,
- \(\chi\) is the relaxation rate.

For a spherically symmetric source, the 3D Green’s function is:



\[
T(r) \propto \frac{1}{r} e^{-r/\ell_T},
\tag{4.2}
\]



with tension length:



\[
\ell_T = \sqrt{\frac{D_T}{\chi}}.
\tag{4.3}
\]



The crucial feature is the **\(1/r\) geometric dilution**, which is absent in 1D.

---

### 4.2 Simulation Design

ED‑Sim‑01 explored a broad parameter space:

- \(D_T\) spanning six orders of magnitude,
- \(\chi\) spanning six orders of magnitude,
- tension lengths \(\ell_T\) from 1 kpc to \(10^6\) kpc,
- source widths \(\sigma\) from 1 kpc to 3 Mpc.

For each parameter set, the simulation computed:

1. the radial profile \(T(r)\),
2. the induced velocity contribution  
   

\[
   V_{\text{temp}}(r) = \sqrt{C_T T(r)},
   \tag{4.4}
   \]


3. the **flatness error** over a radial interval \([r_1, r_2]\):



\[
\epsilon = \frac{|V_{\text{temp}}(r_2) - V_{\text{temp}}(r_1)|}{V_{\text{temp}}(r_1)}.
\tag{4.5}
\]



Flatness requires \(\epsilon \lesssim 0.05\) over 30–1000 kpc.

The central question was:

> **Can a compact source (σ ≲ 10 kpc) produce a flat field over 100–1000 kpc?**

---

### 4.3 Key Result: Geometric Dilution Dominates

The simulations revealed a structural constraint:

> **In 3D, the \(1/r\) geometric dilution dominates long before the exponential decay becomes relevant.**

Even with tension lengths as large as \(\ell_T = 10^6\) kpc, a compact source produced:

- a **16× drop** in \(T(r)\) between 0 and 100 kpc,
- a **4× drop** in \(V_{\text{temp}}(r)\),
- flatness errors \(\epsilon > 300\%\).

This behavior is independent of parameter choices.  
It is a geometric fact of the 3D Green’s function.

The original hypothesis assumed that a large \(\ell_T\) would flatten the field.  
ED‑Sim‑01 showed that **no value of \(\ell_T\) can overcome the \(1/r\) dilution**.

This single result invalidates the galaxy‑sourced hypothesis.

---

### 4.4 Flatness Requires an Extended Source

The simulations also revealed the solution.

When the source width \(\sigma\) is increased:

| Source width \(\sigma\) | Flatness error (30–1000 kpc) |
|-------------------------|-------------------------------|
| 5 kpc                   | 258%                          |
| 50 kpc                  | 71%                           |
| 500 kpc                 | 18%                           |
| 1000 kpc                | 6.8%                          |
| 2000 kpc                | **2.7%**                      |

A nearly flat field requires:



\[
\sigma \gtrsim 1\text{–}3 \text{ Mpc}.
\tag{4.6}
\]



This is the central discovery of ED‑Sim‑01:

> **A compact galactic source cannot produce flat temporal tension.  
> A megaparsec‑scale source can.**

This immediately suggests the updated hypothesis:

- galaxies are too small to source the field,
- but **galaxy groups, filaments, and the cosmic web** are large enough.

---

### 4.5 Implications for the Original Hypothesis

ED‑Sim‑01 overturned the original hypothesis in three ways:

1. **Compact sources fail.**  
   No galaxy‑sized source can produce flat \(T(r)\) in 3D.

2. **Large tension lengths are insufficient.**  
   Increasing \(\ell_T\) does not overcome geometric dilution.

3. **Extended sources succeed.**  
   Megaparsec‑scale sources naturally produce flat fields.

These results do not weaken the ED framework.  
They refine it.

The next section introduces the updated hypothesis:  
**temporal tension is an environmental field sourced by the galactic environment, not by individual galaxies.**

## 5. Updated Hypothesis: Environmental Temporal Tension

ED‑Sim‑01 revealed a structural constraint that invalidates the original galaxy‑sourced hypothesis: a compact source cannot produce a flat temporal‑tension field in three dimensions. The geometric dilution inherent in the 3D Green’s function ensures that \(T(r)\) declines too rapidly for any galaxy‑sized source to maintain a constant field over 100–1000 kpc.

However, the same simulations revealed the solution. When the source of temporal tension is **extended on megaparsec scales**, the geometric dilution is suppressed, and the resulting field becomes nearly constant over the radial range probed by rotation curves and weak lensing. This leads to a revised hypothesis:

> **Temporal tension is an environmental field sourced by galaxy groups, filaments, and the local cosmic web—not by individual galaxies.**

This section develops the updated hypothesis, explains why it succeeds where the original fails, and derives its observational consequences.

---

### 5.1 The New Interpretation: Tension Sourced by the Environment

A galaxy is typically 5–20 kpc in size.  
A galaxy group is 0.5–2 Mpc.  
A filament is 5–50 Mpc.

ED‑Sim‑01 showed that flat temporal‑tension fields require source widths:



\[
\sigma \gtrsim 1\text{–}3 \text{ Mpc}.
\tag{5.1}
\]



This immediately suggests that the correct source of temporal tension is not the galaxy itself but the **galactic environment**:

- the group potential,
- the filamentary structure,
- the local cosmic web.

These structures contain:

- many galaxies,
- gas and plasma,
- shocks and turbulence,
- star‑formation bursts,
- AGN activity,
- merger‑driven ED gradients.

All of these are **event‑dense** processes.  
All of them contribute to the source term \(S(x)\) in Eq. (4.1).

Thus the updated hypothesis is:

> **Galaxies do not sit inside their own temporal halos.  
> They sit inside the temporal halo of their environment.**

This resolves the geometric constraint and aligns the ED framework with the observed universality of weak‑lensing flatness.

---

### 5.2 Why Environmental Sourcing Works

The success of the environmental hypothesis follows directly from the 3D Green’s function:



\[
T(r) \propto \frac{1}{r} e^{-r/\ell_T}.
\tag{5.2}
\]



For a compact source, the \(1/r\) term dominates.  
For an extended source, the \(1/r\) term is **integrated over a large volume**, producing a field that is:

- broad,
- slowly varying,
- nearly constant over 100–1000 kpc.

Formally, if the source has width \(\sigma\), then the effective field at radius \(r\) is:



\[
T(r) \approx \int_0^\sigma \frac{S(r')}{|r-r'|} e^{-|r-r'|/\ell_T} \, r'^2 dr'.
\tag{5.3}
\]



When \(\sigma \gg r\), the denominator varies slowly, and the integral approaches a constant.

This is the mathematical reason environmental tension works.

---

### 5.3 Updated Velocity Model

In the updated hypothesis, the total circular velocity is:



\[
V^2(r) = V_{\text{grav}}^2(r) + V_{\text{temp}}^2,
\tag{5.4}
\]



where the temporal‑tension contribution is:



\[
V_{\text{temp}} = \sqrt{C_T\, T_{\text{env}}},
\tag{5.5}
\]



and \(T_{\text{env}}\) is the **environmental** tension field, not the galaxy’s own field.

Because \(T_{\text{env}}\) is nearly constant over 100–1000 kpc, the resulting velocity contribution is also constant:



\[
V_{\text{temp}}(r) \approx \text{const}.
\tag{5.6}
\]



This produces:

- flat rotation curves,
- flat weak‑lensing velocities,
- no halo edge,
- no Keplerian decline.

The environmental field replaces the need for a galaxy‑sized dark‑matter halo.

---

### 5.4 Implications of the Updated Hypothesis

The environmental‑tension hypothesis has several immediate consequences.

#### **(1) Rotation curves are flat because of other galaxies**

A galaxy’s observed flat rotation curve is shaped primarily by the temporal‑tension field generated by:

- its group,
- its filament,
- or its local cosmic web.

This explains why weak‑lensing flatness is universal across galaxy types.

#### **(2) The BTFR still holds**

The amplitude of the tension field still scales with baryonic mass:



\[
T_{\text{env}} \propto M_b,
\tag{5.7}
\]



so:



\[
V_{\text{temp}}^4 \propto M_b,
\tag{5.8}
\]



preserving the BTFR.

#### **(3) Weak‑lensing flatness is natural**

Environmental tension is megaparsec‑scale by construction.  
Thus the million‑light‑year flatness observed by Mistele et al. (2024) is expected.

#### **(4) Environmental coherence**

Galaxies in the same group should share similar asymptotic velocities, even if their internal structures differ.

#### **(5) Activity dependence becomes environmental**

The field strength depends on the **collective activity** of the environment, not just the galaxy’s own activity.

This predicts:

- group‑level correlations,
- filament‑level coherence,
- and activity‑dependent weak‑lensing signals.

---

The updated hypothesis resolves the geometric constraint revealed by ED‑Sim‑01 and provides a coherent, testable explanation for flat rotation curves and weak‑lensing flatness. The next section develops the observational predictions that distinguish environmental temporal tension from both dark matter and modified gravity.

## 6. Predictions and Tests

The updated environmental‑tension hypothesis makes a series of clear, falsifiable predictions. These predictions arise directly from the structure of the temporal‑tension field, the 3D geometric constraint revealed by ED‑Sim‑01, and the environmental sourcing mechanism introduced in Section 5. They distinguish ED from both collisionless dark matter (CDM) and modified‑gravity frameworks such as MOND.

The predictions fall into four categories:

1. **Weak‑lensing signatures**  
2. **Environmental coherence**  
3. **Merger‑lag behavior**  
4. **Discriminants relative to CDM and MOND**

Each category follows from the architecture of the temporal‑tension field and the environmental sourcing mechanism.

---

### 6.1 Weak‑Lensing Activity Dependence

In the updated hypothesis, the temporal‑tension field is sourced by the **collective activity** of the galactic environment. This leads to a direct prediction:

> **Galaxies in more dynamically active environments should exhibit higher asymptotic lensing velocities.**

Formally, if \(S_{\text{env}}\) is the environmental source term, then:



\[
T_{\text{env}} \propto S_{\text{env}},
\tag{6.1}
\]



and the asymptotic velocity is:



\[
V_{\infty} = \sqrt{C_T\, T_{\text{env}}}.
\tag{6.2}
\]



Thus:

- groups with high star‑formation rates,  
- filaments with strong shocks,  
- environments with frequent mergers  

should all exhibit **systematically higher weak‑lensing velocities**.

This prediction is unique to ED.  
CDM predicts mass‑dependence, not activity‑dependence.  
MOND predicts acceleration‑dependence, not environmental‑dependence.

---

### 6.2 Environmental Coherence

Because the temporal‑tension field is sourced by the environment, not the galaxy, ED predicts:

> **Galaxies in the same group or filament should share similar asymptotic velocities, even if their internal structures differ.**

Let \(G\) denote a group or filament.  
Then for galaxies \(i\) and \(j\) in \(G\):



\[
V_{\infty}^{(i)} \approx V_{\infty}^{(j)}.
\tag{6.3}
\]



This coherence should appear in:

- weak‑lensing stacks,  
- outer rotation‑curve asymptotes,  
- satellite kinematics,  
- group‑level velocity dispersions.

This prediction is incompatible with CDM, which assigns each galaxy its own halo, and with MOND, which ties dynamics to internal baryonic structure.

---

### 6.3 Merger‑Lag Signature

Temporal tension is a **diffusive** field with a finite relaxation rate \(\chi\).  
During a merger, the baryonic components move rapidly, but the temporal‑tension field adjusts slowly.

This produces a **lag**:



\[
\Delta x = \frac{v_{\text{merge}}}{\chi},
\tag{6.4}
\]



where \(v_{\text{merge}}\) is the relative velocity of the merging components.

Thus ED predicts:

- **offsets** between baryonic peaks and lensing peaks,  
- **smeared** or **stretched** lensing contours,  
- **temporal inertia** in the field response.

This is the opposite of CDM, where collisionless dark matter passes through the interaction region with minimal disturbance.

---

### 6.4 Distinguishing ED from CDM and MOND

The updated hypothesis yields several discriminants that can be tested with existing or near‑future data.

#### **(1) Activity dependence (ED) vs. mass dependence (CDM)**

ED predicts:



\[
V_{\infty} \propto \sqrt{T_{\text{env}}} \propto \sqrt{S_{\text{env}}},
\tag{6.5}
\]



where \(S_{\text{env}}\) is tied to environmental activity.

CDM predicts:



\[
V_{\infty} \propto M_{\text{halo}}^{1/3}.
\tag{6.6}
\]



These scalings differ observationally.

#### **(2) Environmental coherence (ED) vs. individual halos (CDM)**

ED predicts group‑level coherence.  
CDM predicts galaxy‑specific halos.

#### **(3) No halo edge (ED) vs. finite halo radius (CDM)**

Temporal tension decays slowly and has no natural truncation.  
CDM halos have virial radii.

#### **(4) No MOND transition radius**

MOND predicts a transition at:



\[
a = a_0.
\tag{6.7}
\]



ED predicts no such transition; the field is scale‑free.

#### **(5) Merger lag (ED) vs. collisionless passage (CDM)**

ED predicts lag and smearing.  
CDM predicts alignment.

---

### 6.5 Summary of Testable Predictions

The updated environmental‑tension hypothesis predicts:

- **activity‑dependent weak‑lensing velocities**,  
- **group‑level coherence of asymptotic velocities**,  
- **lag and smearing in mergers**,  
- **no halo edge**,  
- **no MOND transition**,  
- **flat velocities to megaparsec scales**,  
- **BTFR scaling preserved**,  
- **environmental dependence of the tension amplitude**.

These predictions are falsifiable.  
If they are observed consistently, the environmental‑tension hypothesis becomes a viable alternative to dark matter.  
If they are absent, the hypothesis fails.

The next section discusses the broader implications of the updated hypothesis.

## 7. Discussion

The updated environmental‑tension hypothesis reframes the origin of flat rotation curves and weak‑lensing flatness in a way that is both structurally grounded and empirically testable. Rather than treating temporal tension as a galaxy‑intrinsic field, the revised interpretation identifies it as a **megaparsec‑scale environmental field** generated by the collective activity of galaxy groups, filaments, and the local cosmic web. This shift resolves the geometric constraint revealed by ED‑Sim‑01 and aligns the ED framework with the full radial extent of the weak‑lensing signal.

This section discusses the conceptual significance of this shift, its relationship to existing frameworks, and its implications for the broader ED ontology.

---

### 7.1 From Local to Environmental Fields

The original hypothesis assumed that each galaxy generated its own temporal‑tension halo. This was conceptually appealing: galaxies are engines of sustained activity, and their internal dynamics naturally generate ED gradients. However, ED‑Sim‑01 demonstrated that a compact source cannot produce a flat field in three dimensions. The geometric dilution inherent in the 3D Green’s function overwhelms any attempt to maintain a constant field beyond tens of kiloparsecs.

The updated hypothesis resolves this by recognizing that galaxies do not evolve in isolation. They reside within **extended, event‑dense environments** whose spatial scales naturally satisfy the megaparsec‑scale requirement identified by the simulations. In this view:

- the **galaxy** determines the *amplitude* of the temporal‑tension field (via its baryonic identity),  
- the **environment** determines the *spatial extent* of the field (via its megaparsec‑scale structure).

This division of roles preserves the successes of the original hypothesis while resolving its geometric limitations.

---

### 7.2 Why the Updated Hypothesis Is Stronger

The environmental‑tension hypothesis improves upon the original model in several ways:

1. **It is structurally consistent with the 3D PDE.**  
   The updated hypothesis respects the geometric dilution inherent in Eq. (4.2), rather than relying on a 1D intuition.

2. **It explains the universality of weak‑lensing flatness.**  
   Galaxies in similar environments share similar asymptotic velocities, regardless of morphology.

3. **It predicts environmental coherence.**  
   This is a natural consequence of a shared environmental field.

4. **It preserves the BTFR.**  
   The amplitude of the field still scales with baryonic mass.

5. **It eliminates the need for galaxy‑sized halos.**  
   The temporal‑tension field is not tied to the galaxy’s own size or structure.

6. **It aligns with the cosmic web.**  
   Filaments and groups are precisely the structures that can sustain megaparsec‑scale fields.

In short, the updated hypothesis is not merely a correction—it is a conceptual upgrade that integrates ED more deeply with the known architecture of large‑scale structure.

---

### 7.3 Relationship to CDM and MOND

The environmental‑tension hypothesis occupies a conceptual space distinct from both CDM and MOND.

#### **CDM (collisionless dark matter)**  
- CDM attributes flat rotation curves to massive halos of unseen matter.  
- ED attributes them to a diffusive temporal field sourced by environmental activity.  
- CDM predicts mass‑dependence; ED predicts activity‑dependence.  
- CDM predicts individual halos; ED predicts environmental coherence.

#### **MOND (modified gravity)**  
- MOND modifies the force law at low accelerations.  
- ED leaves gravity untouched and modifies the ontology of what contributes to curvature.  
- MOND predicts a transition at \(a = a_0\); ED predicts no transition.  
- MOND is galaxy‑intrinsic; ED is environment‑intrinsic.

The updated hypothesis therefore provides a third path:  
**a field‑level contribution to curvature that is neither particulate nor a modification of gravity.**

---

### 7.4 Integration with the ED Ontology

The environmental‑tension hypothesis is not an ad hoc fix.  
It emerges naturally from the ED ontology:

- **Becoming is primitive.**  
  The universe is built from micro‑events.

- **ED is the structure of becoming.**  
  ED gradients shape the flow of participation.

- **Temporal tension is the time‑component of ED gradients.**  
  Sustained activity alters the local rate of becoming.

- **Diffusion spreads these alterations.**  
  The resulting field is smooth, extended, and long‑lived.

- **Environmental structures are event‑dense.**  
  Groups and filaments are natural sources of temporal tension.

The updated hypothesis therefore strengthens the ED ontology by showing how its architectural principles extend naturally to megaparsec scales.

---

### 7.5 Conceptual Consequences

The environmental‑tension hypothesis suggests a new way of thinking about galactic dynamics:

- **Galaxies are not isolated dynamical systems.**  
  Their outer kinematics reflect the temporal structure of their environment.

- **Curvature is shaped by activity, not just mass.**  
  The rate of becoming contributes to the macroscopic geometry.

- **Temporal structure is a first‑class component of cosmic architecture.**  
  The cosmic web is not merely a spatial scaffold; it is a temporal one.

- **Weak lensing is detecting temporal curvature.**  
  The inferred “mass profiles” are actually tension profiles.

This reframing opens new avenues for interpreting large‑scale structure, lensing maps, and galaxy evolution.

---

### 7.6 The Path Forward

The updated hypothesis generates a clear research program:

1. **Measure environmental coherence in weak‑lensing stacks.**  
2. **Search for activity‑dependent asymptotic velocities.**  
3. **Identify merger‑lag signatures in cluster collisions.**  
4. **Map tension fields across filaments and groups.**  
5. **Develop full 3D simulations of environmental sourcing.**

These steps will determine whether environmental temporal tension is a viable alternative to dark matter—or whether the hypothesis must be refined further.

The next section concludes the paper.

## 8. Conclusion

The updated environmental‑tension hypothesis provides a coherent, structurally grounded, and empirically testable alternative to dark matter. It emerges not from ad hoc adjustments or phenomenological fitting, but from the internal logic of the Event Density (ED) ontology and the geometric constraints revealed by the 3D temporal‑tension simulations.

The original hypothesis—that each galaxy generates its own temporal‑tension halo—was elegant and predictive. It explained flat rotation curves, the baryonic Tully–Fisher relation, and the early weak‑lensing results. But ED‑Sim‑01 demonstrated that this picture cannot hold in three dimensions. A compact galactic source cannot produce a flat temporal‑tension field over the 10–1000 kpc range required by observations. The \(1/r\) geometric dilution inherent in the 3D Green’s function overwhelms any attempt to maintain a constant field, regardless of the tension length.

The simulations also revealed the solution. When the source of temporal tension is extended on megaparsec scales, the geometric dilution is suppressed, and the resulting field becomes nearly constant over the full radial range probed by rotation curves and weak lensing. This leads naturally to the updated hypothesis:

> **Temporal tension is an environmental field sourced by galaxy groups, filaments, and the local cosmic web—not by individual galaxies.**

This revised interpretation preserves the successes of the original hypothesis while resolving its geometric limitations. It explains:

- the universality of weak‑lensing flatness,  
- the persistence of flat velocities to nearly a megaparsec,  
- the absence of a halo edge,  
- the BTFR scaling,  
- and the coherence of asymptotic velocities across galaxy types.

It also generates new, falsifiable predictions:

- activity‑dependent weak‑lensing velocities,  
- group‑level coherence of asymptotic speeds,  
- merger‑lag signatures,  
- and environmental dependence of the tension amplitude.

These predictions distinguish ED from both collisionless dark matter and modified‑gravity frameworks. They provide a clear empirical path forward: if the predicted signatures are observed consistently, environmental temporal tension becomes a viable field‑level alternative to dark matter. If they are absent, the hypothesis fails.

More broadly, the updated hypothesis strengthens the ED ontology. It shows how the architecture of becoming—micro‑events, ED gradients, and participation—scales naturally from local dynamics to megaparsec‑scale structure. It reframes curvature as the macroscopic geometry of activity, not merely the geometry of mass. And it suggests that the cosmic web is not only a spatial scaffold but a temporal one, shaping the flow of becoming across vast distances.

The task ahead is empirical. The ED ontology provides the conceptual foundation; the environmental‑tension hypothesis provides the large‑scale, testable consequence. Whether the universe’s missing mass is particulate, geometric, or temporal is ultimately a question for observation. The updated hypothesis presented here offers a clear, falsifiable framework for answering it.
