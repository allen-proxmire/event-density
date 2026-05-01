# NS-MHD-3 — Induction Equation Analysis (H3 Audit)

**Date:** 2026-04-30
**Status:** Three-angle convergence audit on the induction equation's kinematic term $\nabla\times(\mathbf{v}\times\mathbf{B})$. **Verdict: H3 holds. The induction-equation kinematic term is structurally non-ED at architectural, dynamical, and spectral levels — the MHD analogue of NS advection.**
**Companions:** [`NS_MHD_1_Opening.md`](NS_MHD_1_Opening.md), [`NS_MHD_2_Lorentz_Force.md`](NS_MHD_2_Lorentz_Force.md), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../Smoothness/NS_Smooth_3_Vortex_Stretching.md`](../Smoothness/NS_Smooth_3_Vortex_Stretching.md), [`../Turbulence/P7_Triads_NS_Turb_4_Spectral.md`](../Turbulence/P7_Triads_NS_Turb_4_Spectral.md).

---

## 1. Purpose

This memo evaluates **H3** for MHD:

> **H3.** *The induction equation's kinematic term $\nabla\times(\mathbf{v}\times\mathbf{B})$ is structurally non-ED — a fluid-mechanical addition parallel to NS advection rather than a canonical ED feature like the Lorentz force.*

This is the **MHD analogue of the NS advection audit**. NS-Smooth-3 + NS-Turb-4 + NS-2.08 jointly established three-angle convergence on advection-as-non-ED in pure NS (architectural, dynamical, spectral). The same three-lens analysis is applied here to the induction term.

The goal is to determine whether the induction term is **canonical ED** (like the Lorentz force, derived in NS-MHD-2 via T17 minimal coupling) or a **fluid-mechanical addition** (like advection, established non-ED in NS-2.08 / NS-Smooth-3 / NS-Turb-4).

The structural distinction surfaced in NS-MHD-2 — *minimal-coupling-derived* velocity-dependence (canonical) vs. *transport-kinematic* velocity-dependence (non-ED) — predicts that the induction term, which is a transport-kinematic coupling, falls in the non-ED class. This memo audits that prediction at all three levels.

---

## 2. Inputs

- **NS-MHD-1.** Maxwell field structure and magnetic-diffusion content; standard MHD induction equation form.
- **NS-MHD-2.** Lorentz force canonical ED via T17 minimal coupling. Established the *minimal-coupling-derived vs. transport-kinematic* distinction for velocity-dependent terms.
- **NS-2.08.** Architectural classification of velocity-dependent terms in pure NS. Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ is a fluid-mechanical addition with no canonical-channel origin.
- **NS-Smooth-3.** Dynamical-level analysis: vortex-stretching $\int\omega\cdot S\omega\,dV$ is the unique indefinite-sign contribution to $dL/dt$ and arises from advection in 3D NS.
- **NS-Turb-4.** Spectral-level analysis: NS advection has a bilinear Fourier triad structure incompatible with P7-class symmetric quadratic mapping.

These inputs supply the three-angle framework and the established non-ED status of NS advection. The audit asks whether the induction term replicates that pattern.

---

## 3. Step 1 — Write the Induction Equation

The standard MHD induction equation is

$$\partial_t \mathbf{B} = \nabla\times(\mathbf{v}\times\mathbf{B}) + \eta\nabla^2\mathbf{B}, \qquad \nabla\cdot\mathbf{B} = 0.$$

The right-hand side decomposes cleanly into two structurally distinct terms:

**(I) Transport-kinematic term:** $\nabla\times(\mathbf{v}\times\mathbf{B})$

In the incompressible case ($\nabla\cdot\mathbf{v}=0$, $\nabla\cdot\mathbf{B}=0$), this expands to

$$\nabla\times(\mathbf{v}\times\mathbf{B}) = (\mathbf{B}\cdot\nabla)\mathbf{v} - (\mathbf{v}\cdot\nabla)\mathbf{B}.$$

The first piece $(\mathbf{B}\cdot\nabla)\mathbf{v}$ is the *magnetic-tension stretching* term (the magnetic analogue of vortex-stretching). The second piece $(\mathbf{v}\cdot\nabla)\mathbf{B}$ is the *advection of the magnetic field by the fluid velocity*. Both are velocity-dependent transport-kinematic couplings.

**(II) Magnetic diffusion:** $\eta\nabla^2\mathbf{B}$

A Laplacian-class dissipative term applied component-wise to $\mathbf{B}$. This is structurally identical to the NS-2 viscous-diffusion application of the mobility channel to velocity. It is canonical ED (mobility channel applied to $\mathbf{B}$); the audit is completed in NS-MHD-4. It is *not* the subject of this memo.

The architectural audit of this memo concerns term **(I)** alone.

---

## 4. Step 2 — Architectural Audit of ∇ × (v × B)

The audit proceeds at three levels in parallel to the NS advection three-angle convergence (architectural NS-2.08 / dynamical NS-Smooth-3 / spectral NS-Turb-4).

### 4.1 Architectural level

**Index structure.** Componentwise,

$$\bigl[\nabla\times(\mathbf{v}\times\mathbf{B})\bigr]_i = \partial_j\bigl(v_i B_j - v_j B_i\bigr) = B_j\partial_j v_i - v_j\partial_j B_i$$

(using $\nabla\cdot\mathbf{v} = \nabla\cdot\mathbf{B} = 0$). The internal antisymmetric structure $v_i B_j - v_j B_i$ is the standard Levi-Civita-projected outer product — the index pattern is antisymmetric in $(i,j)$ on the velocity-field × magnetic-field tensor product.

**Comparison with the canonical channels.** The Architectural Canon principles P1–P7 (operator structure / channel complementarity / penalty equilibrium / mobility capacity bound / participation feedback / damping discriminant / nonlinear triad coupling) generate operator structures of the following forms when applied to a vector field $\mathbf{X}$:

| Canonical channel | Operator structure |
|---|---|
| Mobility (P-class) | $\nabla^2\mathbf{X}$, $\nabla(\nabla\cdot\mathbf{X})$ |
| V1 vacuum kernel (form-FORCED) | $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{X}$ |
| Penalty equilibrium | quadratic in $\mathbf{X}$ symmetric + diagonal |
| Participation feedback | $f(\rho_q)\mathbf{X}$, scalar-coupled |
| T17 minimal coupling | $D_\mu = \partial_\mu - iqA_\mu$ → $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ at semiclassical limit |

None of these channels produces an operator of the form $B_j\partial_j v_i - v_j\partial_j B_i$. The structural class of the induction-kinematic term is *bilinear in two distinct vector fields with antisymmetric index coupling and a derivative on each*. No canonical channel generates this combination:

- Mobility channels are linear in the field they act on; they cannot produce bilinear couplings between two distinct fields.
- V1 kernel produces a self-action $\nabla^4$ stabilization on a single field; it is not bilinear in two fields.
- Minimal coupling (T17) produces velocity-dependence via the gauge-coupling $q\mathbf{A}\cdot\mathbf{v}$, but the velocity in the resulting Lorentz force enters as a *participation measure of the charged rule-type*, not as a *transport field acting on another transport field*.

**The transport-kinematic structural class is exactly the class that NS-2.08 catalogued as fluid-mechanical-addition for advection.** Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ is bilinear in velocity with a derivative on one factor; the induction kinematic term $(\mathbf{B}\cdot\nabla)\mathbf{v} - (\mathbf{v}\cdot\nabla)\mathbf{B}$ is bilinear in $(\mathbf{v},\mathbf{B})$ with a derivative on one factor in each piece. They are the same structural class — **transport-kinematic bilinear couplings**.

**Architectural verdict:** the induction term is non-ED. No P1–P7 canonical channel produces its index-and-derivative structure. It is structurally identical to NS advection in being a transport-kinematic bilinear coupling, and it is unrelated to the minimal-coupling structure that produces the canonical Lorentz force.

### 4.2 Dynamical level

**Energy decomposition.** Take the magnetic energy $E_M = \tfrac{1}{2}\int|\mathbf{B}|^2\,dV$. Differentiating using the induction equation,

$$\frac{dE_M}{dt} = \int \mathbf{B}\cdot\partial_t\mathbf{B}\,dV = \int \mathbf{B}\cdot\nabla\times(\mathbf{v}\times\mathbf{B})\,dV - \eta\int|\nabla\mathbf{B}|^2\,dV.$$

The diffusion term is sign-definite (negative) — clean Lyapunov-class dissipation, identical to the NS viscous Lyapunov decay structure (NS-Smooth-2 / NS-MHD-4).

The kinematic contribution

$$\int \mathbf{B}\cdot\nabla\times(\mathbf{v}\times\mathbf{B})\,dV = -\int (\mathbf{v}\times\mathbf{B})\cdot(\nabla\times\mathbf{B})\,dV = \int \mathbf{v}\cdot[(\nabla\times\mathbf{B})\times\mathbf{B}]\,dV$$

is **indefinite in sign**. The integrand pulls energy between fluid kinetic energy and magnetic energy (the standard MHD energy-exchange channel), but its sign is set by the joint geometry of $\mathbf{v}$, $\mathbf{B}$, and $\nabla\times\mathbf{B}$ and is not bounded by any canonical-channel inequality.

**Comparison with NS-Smooth-3.** NS-Smooth-3 identified vortex-stretching $\int\omega\cdot S\omega\,dV$ as the unique indefinite-sign contribution to the gradient-norm Lyapunov $dL/dt$ in 3D NS, arising from the advective term. The structural picture is parallel:

| Lyapunov | Definite-sign part | Indefinite-sign part | Source of indefinite part |
|---|---|---|---|
| 3D NS gradient-norm $L=\tfrac{1}{2}\|\nabla\mathbf{v}\|^2$ | viscous + V1 kernel decay | $\int\omega\cdot S\omega\,dV$ | advection |
| MHD magnetic energy $E_M = \tfrac{1}{2}\int|\mathbf{B}|^2$ | $-\eta\int|\nabla\mathbf{B}|^2$ | $\int\mathbf{B}\cdot\nabla\times(\mathbf{v}\times\mathbf{B})$ | induction-kinematic term |

Both indefinite-sign Lyapunov contributions arise from transport-kinematic bilinear couplings, and both are absent from the canonical ED dissipation structure. This is the **dynamical-level non-ED signature**: the induction kinematic term plays the same role for the magnetic Lyapunov that advection plays for the velocity Lyapunov — the unique indefinite-sign obstruction.

**A second dynamical signature: the magnetic-tension stretching piece.** The $(\mathbf{B}\cdot\nabla)\mathbf{v}$ piece is the *direct magnetic analogue of vortex-stretching*. It produces magnetic-field intensification along velocity gradients, structurally identical to how vortex-stretching produces vorticity intensification along velocity gradients. The magnetic version is the dynamical core of the kinematic dynamo. The structural parallel is exact: both terms are 3D-only (vanish in 2D for the standard reasons) and both supply the dynamical channel by which transport-kinematic couplings can break monotone Lyapunov decay.

**Dynamical verdict:** the induction kinematic term supplies the unique indefinite-sign contribution to magnetic energy evolution, structurally identical to advection's role in supplying the unique indefinite-sign contribution to velocity-gradient Lyapunov evolution. It is non-ED at the dynamical level by the same criterion that NS-Smooth-3 used for advection.

### 4.3 Spectral level

**Fourier symbol.** In Fourier space, with $\mathbf{B}(\mathbf{k},t)$ the Fourier transform of $\mathbf{B}(\mathbf{x},t)$,

$$\widehat{\nabla\times(\mathbf{v}\times\mathbf{B})}(\mathbf{k}) = i\mathbf{k}\times\bigl[\widehat{\mathbf{v}\times\mathbf{B}}(\mathbf{k})\bigr] = i\mathbf{k}\times\int_{\mathbf{p}+\mathbf{q}=\mathbf{k}} \mathbf{v}(\mathbf{p})\times\mathbf{B}(\mathbf{q})\,d\mathbf{p}.$$

This is **bilinear** in $(\widehat{\mathbf{v}},\widehat{\mathbf{B}})$ and is supported on triadic interactions $\mathbf{p}+\mathbf{q}=\mathbf{k}$ — exactly the triad structure that NS-Turb-4 catalogued for the NS advective interaction coefficient $M_{ijm}(\mathbf{k}) = -ik_j P_{im}(\mathbf{k})$.

**Structural class.** The induction-kinematic Fourier symbol is a bilinear-with-projection operator on a triad. Specifically, writing the cross-product structure component-wise,

$$\bigl[\widehat{\nabla\times(\mathbf{v}\times\mathbf{B})}\bigr]_i(\mathbf{k}) = i\,\varepsilon_{ijk}\varepsilon_{klm}\,k_j\!\!\int_{\mathbf{p}+\mathbf{q}=\mathbf{k}} v_l(\mathbf{p})\,B_m(\mathbf{q})\,d\mathbf{p}.$$

The interaction kernel $\varepsilon_{ijk}\varepsilon_{klm}k_j$ is bilinear with a single antisymmetric Levi-Civita projection — the same algebraic class as NS advection's $-ik_j P_{im}(\mathbf{k})$ (which is bilinear with a transverse-projector $P_{im}$ projection).

**Incompatibility with P7 nonlinear-triad-coupling channel.** P7 generates *symmetric quadratic* nonlinear couplings (NS-Turb-3): the canonical P7-class triad symbol is symmetric in its two field arguments and produces real-valued symmetric tensor couplings. The induction-kinematic symbol is *antisymmetric in $(\mathbf{v},\mathbf{B})$* (cross-product → antisymmetric exchange) and uses a Levi-Civita projection rather than a symmetric tensor structure. **No P7-class symmetric quadratic mapping reproduces this symbol.**

This is exactly the spectral-level diagnosis that NS-Turb-4 applied to NS advection: the bilinear-with-antisymmetric-projection triad structure is incompatible with P7's symmetric quadratic class. The induction-kinematic term replicates the diagnosis on the magnetic side.

**Spectral verdict:** the induction term is non-ED at the spectral level. Its bilinear triad symbol is structurally identical to NS advection's and is incompatible with the only canonical nonlinear-coupling channel (P7).

---

## 5. Step 3 — Three-Angle Convergence

The three independent analyses converge:

| Lens | NS advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | MHD induction $\nabla\times(\mathbf{v}\times\mathbf{B})$ |
|---|---|---|
| **Architectural** | No P1–P7 channel; bilinear transport-kinematic | No P1–P7 channel; bilinear transport-kinematic |
| **Dynamical** | Unique indefinite-sign contribution to gradient-norm Lyapunov | Unique indefinite-sign contribution to magnetic-energy Lyapunov |
| **Spectral** | Bilinear triad incompatible with P7 symmetric-quadratic | Bilinear triad incompatible with P7 symmetric-quadratic |
| **Verdict** | **non-ED (NS-2.08 / NS-Smooth-3 / NS-Turb-4)** | **non-ED (this memo, three-angle convergence)** |

Three-angle convergence on the induction-kinematic term as **non-ED** mirrors the NS advection convergence. The result is the magnetic-side image of the same structural pattern.

This is now the **second** three-angle convergence on a transport-kinematic non-ED term in the NS / MHD program. The pattern is generalizing as expected: transport-kinematic bilinear couplings between physical fields are systematically non-ED.

---

## 6. Step 4 — H3 Verdict

**H3 holds.** The induction equation's kinematic term $\nabla\times(\mathbf{v}\times\mathbf{B})$ is structurally non-ED at architectural, dynamical, and spectral levels. It is the magnetic-side analogue of NS advection.

**The MHD architectural split.** Combining NS-MHD-1 + NS-MHD-2 + this memo + the impending NS-MHD-4 audit:

| MHD content channel | Status |
|---|---|
| Viscous diffusion $\mu\nabla^2\mathbf{v}$ | Canonical ED (mobility channel on $\mathbf{v}$, NS-2.08) |
| Magnetic diffusion $\eta\nabla^2\mathbf{B}$ | Canonical ED (mobility channel on $\mathbf{B}$, NS-MHD-4 to confirm) |
| Maxwell field structure | Canonical ED (T17, NS-MHD-1) |
| Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ | Canonical ED (T17 minimal coupling, NS-MHD-2) |
| Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | Non-ED (NS-2.08 / NS-Smooth-3 / NS-Turb-4) |
| Pressure $-\nabla p$ | Non-ED (NS-2.08, Lagrange-multiplier) |
| Incompressibility $\nabla\cdot\mathbf{v}=0$ | Non-ED (NS-2.08, fluid constraint) |
| Induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$ | **Non-ED (this memo)** |
| Ohm $\mathbf{v}\times\mathbf{B}$ component | Non-ED (transport-kinematic, NS-MHD-4 to confirm) |

MHD inherits the same structural split as NS:

- **Canonical ED side:** Maxwell, magnetic diffusion, viscous diffusion, Lorentz force.
- **Non-ED side (transport-kinematic):** advection, induction kinematic, Ohm kinematic, plus pure-NS pressure and incompressibility.

**The kinematic-coupling pattern (refined in NS-MHD-2 §6.2) is fully validated.** Velocity-dependence has two structurally distinct origins:

- *Minimal-coupling-derived* velocity-dependence (Lorentz $\mathbf{v}\times\mathbf{B}$): canonical ED via T17.
- *Transport-kinematic* velocity-dependence (advection, induction kinematic, Ohm kinematic): non-ED, fluid-mechanical-specific.

The induction-equation audit confirms that the latter class is systematically non-ED at all three levels of analysis.

---

## 7. Recommended Next Steps

1. **Proceed to NS-MHD-4 (Full MHD Architectural Classification).** File: `theory/Navier Stokes/MHD/NS_MHD_4_Magnetic_Diffusion.md`. Confirm magnetic diffusion $\eta\nabla^2\mathbf{B}$ as canonical ED (mobility channel applied to $\mathbf{B}$); confirm Maxwell field structure as canonical via T17; classify the Ohm's-law $\mathbf{v}\times\mathbf{B}$ component as transport-kinematic non-ED; deliver the consolidated MHD architectural classification table.

2. **NS-MHD-5 (Synthesis + Arc Closure).** File: `theory/Navier Stokes/MHD/NS_MHD_5_Synthesis.md`. Aggregate verdict; final architectural decomposition of MHD; honest catalogue of ED-canonical vs. fluid-mechanical-specific content; arc-level summary parallel to NS-Synthesis closures.

### Decisions for you

- **Confirm H3 verdict.** Induction-kinematic term structurally non-ED at architectural / dynamical / spectral levels; three-angle convergence on the magnetic side mirrors NS advection's three-angle convergence.
- **Confirm the MHD architectural split.** EM-side additions all canonical ED via T17 + mobility channel; transport-kinematic terms (advection, induction kinematic, Ohm kinematic) all non-ED.
- **Confirm proceeding to NS-MHD-4 as the next deliverable.**

---

*NS-MHD-3 closes the H3 audit. Three-angle convergence on $\nabla\times(\mathbf{v}\times\mathbf{B})$ as non-ED at architectural (no P1–P7 channel for bilinear transport-kinematic structure), dynamical (unique indefinite-sign contribution to magnetic-energy Lyapunov, structural parallel to vortex-stretching), and spectral (bilinear triad incompatible with P7 symmetric-quadratic) levels. Result mirrors the NS advection convergence and validates the kinematic-coupling-pattern refinement from NS-MHD-2: minimal-coupling-derived velocity-dependence is canonical ED; transport-kinematic velocity-dependence is fluid-mechanical-specific. NS-MHD-4 is the next deliverable.*
