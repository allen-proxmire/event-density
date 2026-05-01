# NS-MHD-4 — Full MHD Architectural Classification

**Date:** 2026-04-30
**Status:** Consolidated architectural classification of the incompressible MHD system. Integrates NS-MHD-1 (Maxwell + magnetic diffusion), NS-MHD-2 (Lorentz canonical via T17), NS-MHD-3 (induction kinematic non-ED). **Verdict: MHD is partially ED-architectural with the same canonical/non-canonical boundary as NS — but with strictly more canonical content on the EM side.**
**Companions:** [`NS_MHD_1_Opening.md`](NS_MHD_1_Opening.md), [`NS_MHD_2_Lorentz_Force.md`](NS_MHD_2_Lorentz_Force.md), [`NS_MHD_3_Induction_Equation.md`](NS_MHD_3_Induction_Equation.md), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../Smoothness/NS_Smooth_5_Synthesis.md`](../Smoothness/NS_Smooth_5_Synthesis.md), [`../Turbulence/P7_Triads_NS_Turb_4_Spectral.md`](../Turbulence/P7_Triads_NS_Turb_4_Spectral.md).

---

## 1. Purpose

This memo consolidates the architectural status of every term in the incompressible MHD system. Specifically:

- **Which MHD terms are ED-canonical** — i.e., FORCED at form level by P1–P7 canonical channels (mobility, V1 kernel, P7 nonlinear-coupling) or by T17 minimal coupling.
- **Which MHD terms are fluid-mechanical additions** — non-canonical but non-obstructive (pressure as Lagrange multiplier, incompressibility constraint).
- **Which MHD terms are transport-kinematic non-ED** — non-canonical and obstructive at the dynamical / spectral levels (advection, induction kinematic, Ohm kinematic component).
- **How the full MHD system decomposes structurally** as a partial-ED system parallel to NS-2.08's classification of pure NS.

The output is a consolidated classification table and an architectural verdict for MHD. This is the load-aggregating memo that feeds NS-MHD-5 (synthesis + arc closure) and Appendix C of the NS Synthesis Paper.

---

## 2. Inputs

- **NS-MHD-1.** Standard MHD content channels enumerated; magnetic diffusion identified as Laplacian-class (mobility channel applied to $\mathbf{B}$); Maxwell field structure traced to T17 gauge content.
- **NS-MHD-2.** H2 verdict: Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ is canonical ED via T17 minimal coupling; FORCED at form level, INHERITED at coarse-graining bridge (parallel to NS-2 viscous content). Kinematic-coupling-pattern refinement: minimal-coupling-derived velocity-dependence is canonical; transport-kinematic velocity-dependence is fluid-mechanical-specific.
- **NS-MHD-3.** H3 verdict: induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$ is non-ED at architectural / dynamical / spectral levels — three-angle convergence on the magnetic side mirroring the NS advection convergence.
- **NS-2.08.** NS architectural classification: viscous diffusion canonical; advection, pressure, incompressibility fluid-mechanical-additions.
- **NS-Smoothness.** Dynamical classification: vortex-stretching is the unique indefinite-sign Lyapunov contribution in 3D NS, arising from advection. R1 term ($-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$) supplies form-FORCED Lyapunov decay.
- **NS-Turb-4.** Spectral classification: NS advection is bilinear-with-projection triad incompatible with P7's symmetric quadratic class.

These inputs collectively cover every MHD content channel.

---

## 3. Step 1 — Write the Full Incompressible MHD System

The standard incompressible resistive MHD equations are:

**Momentum equation (Navier-Stokes with Lorentz force):**

$$\rho\bigl(\partial_t\mathbf{v} + (\mathbf{v}\cdot\nabla)\mathbf{v}\bigr) = -\nabla p + \mu\nabla^2\mathbf{v} + (\nabla\times\mathbf{B})\times\mathbf{B} + \rho\mathbf{f}^\mathrm{ext}.$$

(Here $(\nabla\times\mathbf{B})\times\mathbf{B} = \mu_0\mathbf{j}\times\mathbf{B}$ is the Lorentz force per unit volume in the MHD limit, with the constant $\mu_0$ absorbed into normalization.)

**Induction equation:**

$$\partial_t\mathbf{B} = \nabla\times(\mathbf{v}\times\mathbf{B}) + \eta\nabla^2\mathbf{B}.$$

**Constraints:**

$$\nabla\cdot\mathbf{v} = 0, \qquad \nabla\cdot\mathbf{B} = 0.$$

**ED-augmented momentum equation** (with R1 substrate-cutoff regularization):

$$\rho\bigl(\partial_t\mathbf{v} + (\mathbf{v}\cdot\nabla)\mathbf{v}\bigr) = -\nabla p + \mu\nabla^2\mathbf{v} + (\nabla\times\mathbf{B})\times\mathbf{B} - \kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v} + \rho\mathbf{f}^\mathrm{ext}.$$

The R1 term is the form-FORCED V1 finite-width vacuum-kernel stabilization established in NS-3.01 and NS-Smooth-2; it enters MHD's momentum equation by inheritance from the underlying canonical PDE, not as a new MHD-specific commitment.

The **generalized Ohm's law** (resistive form) is

$$\mathbf{j} = \sigma\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr).$$

The $\mathbf{v}\times\mathbf{B}$ piece is a transport-kinematic component that we audit alongside the induction kinematic term.

---

## 4. Step 2 — Architectural Classification of Each Term

### 4.1 Canonical ED terms

Each of the following terms is FORCED at form level by a canonical ED channel:

**(a) Viscous diffusion $\mu\nabla^2\mathbf{v}$** — *Mobility channel applied to velocity.* The canonical PDE's mobility channel is a Laplacian-class operator on the participation measure. NS-2.08 established that vector-extending the canonical PDE component-wise to fluid velocity produces $\mu\nabla^2\mathbf{v}$ as the FORCED viscous structure. Form FORCED; coarse-graining bridge INHERITED (deferred Arc D); coefficient $\mu$ INHERITED at value layer.

**(b) Magnetic diffusion $\eta\nabla^2\mathbf{B}$** — *Mobility channel applied to magnetic field.* The vector-extension of the mobility channel is field-type-agnostic per the Architectural Canon Vector Extension memo. Applying it component-wise to $\mathbf{B}$ produces $\eta\nabla^2\mathbf{B}$ at the same FORCED status as viscous diffusion. The coefficient $\eta = 1/(\sigma\mu_0)$ is INHERITED at value layer; the resistivity $\sigma$ is a fluid-property INHERITED quantity.

**(c) Lorentz force $(\nabla\times\mathbf{B})\times\mathbf{B}$** — *T17 minimal coupling.* NS-MHD-2 established that the substrate-level minimal coupling $\partial_\mu \to \partial_\mu - iqA_\mu$ on charged chains produces the classical force $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ at semiclassical limit, with coarse-graining to fluid scale yielding $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$. In the MHD limit $\rho_q\mathbf{E}$ is suppressed by quasi-neutrality, leaving $\mathbf{j}\times\mathbf{B} = \mu_0^{-1}(\nabla\times\mathbf{B})\times\mathbf{B}$. Form FORCED by T17; coarse-graining bridge INHERITED in parallel to NS-2 viscous content.

**(d) Maxwell field structure $\partial_t\mathbf{B}$, $\nabla\times\mathbf{B}$, $\nabla\cdot\mathbf{B} = 0$** — *T17 directly.* T17 (Arc Q closure) FORCES the gauge field $A_\mu$ as the participation measure of $\tau_g$, with the four-channel content of any gauge theory (group structure, vertex/coupling, worldline, vacuum) FORCED by primitives + Theorems 1–16. The Maxwell equations follow from T17 at gauge-quotient level. Form FORCED at canon; field amplitudes INHERITED.

**(e) R1 substrate-cutoff term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$** — *V1 finite-width vacuum kernel.* Established in NS-3.01 / NS-Smooth-2 as the form-FORCED hyperviscous stabilization arising from V1's finite-width vacuum kernel structure. Inherits into MHD's momentum equation by virtue of being a canonical-ED augmentation of the velocity sector that is independent of EM coupling. Form FORCED; coefficient $\kappa$ INHERITED.

### 4.2 Fluid-mechanical additions (non-canonical but non-obstructive)

These terms are not derivable from any canonical ED channel, but they are not dynamically or spectrally obstructive:

**(f) Pressure $-\nabla p$** — *Lagrange multiplier for incompressibility.* NS-2.08 catalogued pressure as a fluid-mechanical addition: it is a passive, derived field set by the incompressibility constraint via the projection onto divergence-free flow. It does not introduce indefinite-sign Lyapunov contributions or spectral bilinear couplings. It is structurally extra commitment relative to ED canon, but it is non-obstructive.

**(g) Incompressibility constraint $\nabla\cdot\mathbf{v} = 0$** — *Fluid-mechanical kinematic constraint.* Imposed at fluid level by the assumption of incompressible flow. Not derivable from canonical ED channels (the canonical PDE does not commit to divergence-free participation-measure evolution). The MHD analogue $\nabla\cdot\mathbf{B} = 0$ is *different in status* — see (h) below.

**(h) $\nabla\cdot\mathbf{B} = 0$** — *Maxwell constraint, FORCED by T17.* Unlike the velocity incompressibility $\nabla\cdot\mathbf{v}=0$, the magnetic divergence-free constraint is FORCED by Maxwell field structure (the absence of magnetic monopoles in the canonical $U(1)$ gauge content). It is canonical ED, not a fluid-mechanical addition. We classify it under the *canonical ED* row of the table for clarity, but note that its status is distinct from the velocity-incompressibility constraint.

### 4.3 Transport-kinematic non-ED terms (obstructive class)

These terms share a single structural class — bilinear-with-projection couplings between two transport fields, not produced by any canonical channel and dynamically / spectrally obstructive:

**(i) Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$** — *Bilinear in velocity with directional derivative.* NS-2.08 architectural / NS-Smooth-3 dynamical / NS-Turb-4 spectral established three-angle convergence on advection as non-ED.

**(j) Induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$** — *Bilinear in $(\mathbf{v},\mathbf{B})$ with cross-product + curl.* NS-MHD-3 established three-angle convergence on the magnetic side: no canonical channel, unique indefinite-sign contribution to magnetic-energy Lyapunov, bilinear-with-Levi-Civita-projection triad incompatible with P7.

**(k) Ohm-law kinematic component $\mathbf{v}\times\mathbf{B}$** — *Cross-product velocity-magnetic coupling.* The $\mathbf{v}\times\mathbf{B}$ piece in the generalized Ohm's law is the same structural class as the induction kinematic and as advection: bilinear with antisymmetric Levi-Civita projection between two transport fields, not produced by any canonical channel. Three-angle status: architecturally non-canonical (no P1–P7 channel for bilinear $\mathbf{v}\times\mathbf{B}$), dynamically a kinematic-transport contribution to current evolution, spectrally bilinear-with-projection identical class to advection / induction kinematic.

**Common structural class.** All three transport-kinematic terms share:

- **Architectural:** No P1–P7 canonical channel produces their bilinear-with-projection structure.
- **Origin:** Not produced by minimal coupling either — they involve velocity as a *transport field* acting on another transport field, not as the participation measure of a charged rule-type entering via a gauge-coupling Lagrangian.
- **Algebraic structure:** Bilinear in two transport fields with a projection operator (transverse projector $P_{ij}$ for advection; Levi-Civita $\varepsilon_{ijk}$ for induction kinematic and Ohm kinematic).
- **Spectral incompatibility:** P7 generates symmetric-quadratic triad couplings; the transport-kinematic class is antisymmetric / projector-mediated; no P7 mapping reproduces their Fourier symbols.

This is the **non-ED transport-kinematic class** that NS-MHD-2 and NS-MHD-3 jointly identified. It is a single structural class with three concrete instances in the MHD system.

---

## 5. Step 3 — Consolidated Classification Table

| Term | Equation | Origin | Architectural Status | Notes |
|---|---|---|---|---|
| Viscous diffusion | $\mu\nabla^2\mathbf{v}$ | Mobility channel applied to $\mathbf{v}$ | **Canonical ED** | Form FORCED; coefficient $\mu$ INHERITED; coarse-graining INHERITED (deferred Arc D) |
| Magnetic diffusion | $\eta\nabla^2\mathbf{B}$ | Mobility channel applied to $\mathbf{B}$ | **Canonical ED** | Field-type-agnostic vector-extension; coefficient $\eta$ INHERITED |
| Lorentz force | $(\nabla\times\mathbf{B})\times\mathbf{B}$ | T17 minimal coupling | **Canonical ED** | NS-MHD-2 H2 verdict; form FORCED, coarse-graining INHERITED; minimal-coupling-derived velocity-dependence |
| R1 substrate cutoff | $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ | V1 finite-width vacuum kernel | **Canonical ED** | NS-3.01 / NS-Smooth-2; form FORCED; coefficient $\kappa$ INHERITED |
| Magnetic time-evolution | $\partial_t\mathbf{B}$ | T17 gauge-field dynamics | **Canonical ED** | Standard time-derivative on gauge participation measure |
| Magnetic divergence-free | $\nabla\cdot\mathbf{B} = 0$ | T17 / Maxwell field structure | **Canonical ED** | Distinct status from $\nabla\cdot\mathbf{v}=0$; FORCED by gauge content |
| Pressure | $-\nabla p$ | Lagrange multiplier for $\nabla\cdot\mathbf{v}=0$ | **Fluid-mechanical addition** (non-obstructive) | NS-2.08; passive derived field; sign-definite contribution to energy |
| Velocity incompressibility | $\nabla\cdot\mathbf{v} = 0$ | Fluid-mechanical kinematic constraint | **Fluid-mechanical addition** (non-obstructive) | NS-2.08; not derivable from canonical channels |
| Advection | $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | Transport-kinematic bilinear | **Non-ED (obstructive)** | NS-2.08 / NS-Smooth-3 / NS-Turb-4 three-angle convergence |
| Induction kinematic | $\nabla\times(\mathbf{v}\times\mathbf{B})$ | Transport-kinematic bilinear | **Non-ED (obstructive)** | NS-MHD-3 three-angle convergence; magnetic-side analogue of advection |
| Ohm kinematic | $\mathbf{v}\times\mathbf{B}$ in Ohm's law | Transport-kinematic bilinear | **Non-ED (obstructive)** | Same structural class; Levi-Civita-projected bilinear |

**Summary counts (incompressible MHD):**

- *Canonical ED:* 6 of 11 content items (viscous, magnetic diffusion, Lorentz, R1, $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$).
- *Fluid-mechanical additions (non-obstructive):* 2 of 11 (pressure, $\nabla\cdot\mathbf{v}=0$).
- *Non-ED (obstructive transport-kinematic):* 3 of 11 (advection, induction kinematic, Ohm kinematic).

---

## 6. Step 4 — Architectural Verdict for MHD

**MHD inherits the same structural split as NS, but with strictly more canonical content on the EM side.**

Specifically:

- **All EM-side additions are ED-canonical.** Magnetic diffusion (mobility channel on $\mathbf{B}$), Maxwell field structure (T17 directly), Lorentz force (T17 minimal coupling), magnetic divergence-free constraint (Maxwell). The MHD upgrade does *not* add any new fluid-mechanical addition or non-ED obstructive term on the EM side.

- **All transport-kinematic terms are non-ED.** Advection (pure-NS), induction kinematic (MHD-specific), Ohm kinematic (MHD-specific) form a single structural class with the same architectural / dynamical / spectral non-ED signatures.

- **MHD is partially ED-architectural.** ED supplies canonical content for the dissipative and EM-coupling sectors; transport-kinematic couplings between physical fields remain fluid-mechanical-specific structural commitments, parallel to but enlarged from the pure-NS catalogue.

- **The canonical/non-canonical boundary is the same in NS and MHD.** It runs along the line *minimal-coupling-derived velocity-dependence vs. transport-kinematic velocity-dependence*. Minimal-coupling velocity dependence (Lorentz) is canonical ED via T17; transport-kinematic velocity dependence (advection, induction kinematic, Ohm kinematic) is non-ED, with three-angle convergence on each.

- **EM content tilts the balance toward canonical.** Pure NS has 1 canonical-ED term (viscous) and 3 non-canonical terms (advection, pressure, incompressibility) in the momentum equation: a 1:3 ratio. MHD adds 4 canonical-ED items (magnetic diffusion, Lorentz, $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$) and 2 non-canonical items (induction kinematic, Ohm kinematic) — a 4:2 ratio for the EM upgrade. The aggregate MHD ratio is 6:5, dominated by canonical content.

The structural picture is that **MHD is *more* ED-architectural than pure NS**, in the precise sense that the EM-side additions are predominantly canonical (Maxwell + Lorentz + magnetic diffusion all canonical) while the new fluid-mechanical-specific structural commitments (induction kinematic, Ohm kinematic) belong to a single class with a single architectural origin (transport-kinematic) and a single architectural defect (no canonical channel).

The **kinematic-coupling pattern** (NS-MHD-2 §6.2, validated NS-MHD-3 §6) is now the load-bearing architectural insight of the entire NS / MHD program: the canonical/non-canonical boundary in continuum fluid mechanics, as ED sees it, runs along the distinction between minimal-coupling-derived and transport-kinematic velocity-dependence. MHD has supplied two additional concrete instances of the latter class (induction kinematic, Ohm kinematic) on top of NS's advection, all sharing identical three-angle architectural status.

---

## 7. Recommended Next Steps

1. **Proceed to NS-MHD-5 (Synthesis + Arc Closure).** File: `theory/Navier Stokes/MHD/NS_MHD_5_Synthesis.md`. Aggregate the four classification verdicts (NS-MHD-1 / 2 / 3 / 4) into a single arc-closing memo: state the architectural decomposition, the kinematic-coupling-pattern result, the comparison to NS-2.08, and the open questions (MHD turbulence, kinematic dynamo, magnetic reconnection — none ED-resolvable but architecturally illuminated).

2. **Integrate MHD classification into NS Synthesis Paper as Appendix C.** Once NS-MHD-5 closes, the consolidated classification table and the MHD architectural verdict are publication-ready material for an appendix to the NS Synthesis Paper, parallel to how P4-NN material would feed an empirical-rheology companion paper. Appendix C scope: (i) MHD content channels enumerated; (ii) ED architectural classification (this memo's table); (iii) kinematic-coupling pattern as the unified canonical/non-canonical boundary; (iv) honest non-goals (no dynamo theory, no MHD turbulence cascade, no reconnection rate).

### Decisions for you

- **Confirm the consolidated MHD classification.** 6:2:3 split (canonical : fluid-mechanical-non-obstructive : non-ED-obstructive) across the 11 content items.
- **Confirm the architectural verdict.** MHD is *partially ED-architectural*, with strictly more canonical content on the EM side than pure NS has on the velocity side; the canonical/non-canonical boundary runs along minimal-coupling-derived vs. transport-kinematic velocity-dependence.
- **Confirm proceeding to NS-MHD-5 (synthesis + arc closure) as the next deliverable.**

---

*NS-MHD-4 closes the consolidated classification. 11 MHD content items classified: 6 canonical ED (viscous, magnetic diffusion, Lorentz via T17, R1, $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$), 2 fluid-mechanical-additions (pressure, $\nabla\cdot\mathbf{v}=0$), 3 non-ED obstructive (advection, induction kinematic, Ohm kinematic — a single transport-kinematic structural class). Architectural verdict: MHD is partially ED-architectural with strictly more canonical content on the EM side than pure NS; canonical/non-canonical boundary runs along minimal-coupling-derived vs. transport-kinematic velocity-dependence. NS-MHD-5 (synthesis + arc closure) is the next deliverable; Appendix C of the NS Synthesis Paper is the publication target for this material.*
