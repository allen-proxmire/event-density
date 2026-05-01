# Arc_D_3 — Directional-Field Diffusion from Substrate Chain Momentum-Flux Statistics

**Date:** 2026-04-30
**Status:** Second technical derivation memo of Arc D. Establishes the substrate-to-continuum origin of the mobility-channel viscous operator $\mu\nabla^2\mathbf{v}$. **Result: Laplacian form FORCED by substrate momentum-flux gradient expansion + isotropy + momentum conservation; $\mu(\rho)$ form-FORCED by V1 second-moment + P4 substrate structure; numerical $\mu(\rho)$ values INHERITED.**
**Companions:** [`Arc_D_1_Opening.md`](Arc_D_1_Opening.md), [`Arc_D_2_Scalar_Diffusion_From_Substrate.md`](Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`../Navier Stokes/NS-2.04_Momentum_Balance.md`](../Navier%20Stokes/NS-2.04_Momentum_Balance.md), [`../Navier Stokes/NS-2.05_Stress_Tensor.md`](../Navier%20Stokes/NS-2.05_Stress_Tensor.md), [`../Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](../Navier%20Stokes/NS-2.08_ED-PDE_Direct_Mapping.md), [`../Architectural_Canon_Vector_Extension.md`](../Architectural_Canon_Vector_Extension.md).

---

## 1. Purpose

This memo derives the continuum viscous operator

$$\mu\nabla^2\mathbf{v}$$

from substrate-level chain momentum-flux statistics, under hydrodynamic-window coarse-graining

$$\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}.$$

The derivation is the directional-field counterpart of Arc_D_2's scalar-diffusion derivation. The structural logic is identical: cell-averaging of a substrate field, gradient expansion of the substrate flux, isotropy-mediated cancellation of leading-order terms, identification of a transport coefficient from the V1-kernel second moment, application of the local conservation law to obtain the continuum dynamical equation. The differences are bookkeeping: scalar field $\rho$ replaced by vector field $\mathbf{v}$; number-flux $\mathbf{J}_\rho$ replaced by momentum-flux tensor $\Pi_{ij}$; resulting transport coefficient is the kinematic viscosity $\mu(\rho)$ rather than the mobility $M(\rho)$.

Together with Arc_D_2, this memo closes the NS-2 INHERITED bridge for the canonical mobility channel: ED's substrate primitives plus hydrodynamic-window coarse-graining yield, FORCED at form level, both the scalar-diffusion structure $\nabla\cdot(M\nabla\rho)$ and the directional-field viscous structure $\mu\nabla^2\mathbf{v}$. The two derivations are unified by the field-type-agnostic vector-extension of the canonical PDE (Architectural Canon Vector Extension memo) — applying the same gradient-expansion machinery to scalar and vector fields produces identically-structured Laplacian-class operators.

---

## 2. Inputs

- **ED-I-06.** Directional fields as orientation-bearing participation structures (§3). The cell-averaged velocity $\mathbf{v}(\mathbf{x},t)$ defined here is the canonical directional-field-class quantity in the ED-I-06 ontology — vorticity-like fluid structures are explicitly cited as directional-field instances.
- **Theorem 17 (Gauge-Fields-as-Rule-Type).** Directional-field structure of $\tau_g$ as participation measure of a structural rule-type. The general lesson — that vector-valued participation measures admit canonical-channel structure — applies here for the velocity field.
- **Theorem 18 (V1 Kernel Retardation).** V1's forward-cone-only support and finite spatial width. Required for the second-moment integral that supplies the viscosity coefficient.
- **NS-2 viscous-content classification.** The form-FORCED viscous-diffusion result (NS-2.04 momentum balance, NS-2.05 stress tensor, NS-2.07 synthesis, NS-2.08 ED-PDE mapping) that this memo grounds at substrate level.
- **NS-MHD-2 coarse-graining structure.** Parallel charged-chain coarse-graining for Lorentz force; informs Step 6 of this memo and is the direct upstream of Arc_D_5.
- **Arc_D_2 (Scalar Diffusion).** Cell definition, gradient-expansion machinery, V1 second-moment integral form, coarse-graining-cell scale-separation conditions. Re-used directly here with vector-field replacements.
- **Arc_D_1 (Opening).** Hydrodynamic-window definition; arc structure; scope item S2 (directional-field diffusion from chain momentum-flux statistics).

---

## 3. Step 1 — Coarse-Graining Cell for Directional Fields

Let $\Omega(\mathbf{x}, R_\mathrm{cg}) \subset \mathbb{R}^3$ be the same spherical coarse-graining cell as in Arc_D_2, satisfying $R_\mathrm{cg} \gg \ell_P$, $R_\mathrm{cg} \gg \lambda_\mathrm{mfp}$, $R_\mathrm{cg} \ll L_\mathrm{flow}$.

**Cell-averaged velocity field.** Let $P_\Omega^i(\mathbf{x}, t)$ be the total chain momentum (i-th component) within the cell at time $t$ under V1-retarded chain dynamics, and let $M_\Omega(\mathbf{x},t)$ be the total chain mass within the cell. Define

$$v^i(\mathbf{x}, t) \;\equiv\; \frac{P_\Omega^i(\mathbf{x}, t)}{M_\Omega(\mathbf{x}, t)} \;=\; \frac{\langle p^i\rangle_\Omega}{m},$$

the mass-weighted cell-averaged momentum per unit mass — the macroscopic velocity field. With $\rho(\mathbf{x},t)$ the cell-averaged participation (mass) density (Arc_D_2), the corresponding momentum density is $\rho\,\mathbf{v}$.

**Chain momentum-flux tensor.** Let $\Pi_{ij}(\mathbf{x}, t)$ be the substrate-level momentum flux: the rate per unit area at which $j$-component momentum crosses outward through a unit-normal-$\hat e_j$-oriented boundary element, carrying $i$-component momentum. By construction $\Pi_{ij}$ is a rank-2 tensor field on the macroscopic coordinate.

**Goal.** Compute the deviatoric part of $\Pi_{ij}$ under small gradients of $\mathbf{v}$, i.e., expand $\Pi_{ij}$ to first order in $\partial_k v_l$ at the cell boundary midpoint. The convective (advective) piece $\rho v_i v_j$ enters at zeroth order in the gradient; the viscous piece enters at first order; higher-order pieces enter at $\mathcal{O}(\ell_P^2)$ and are recorded for Arc_D_4.

The rest of the derivation follows the Arc_D_2 pattern with vector-field bookkeeping.

---

## 4. Step 2 — Substrate Chain Momentum-Flux Statistics

The substrate-level momentum flux is computed by considering chain commitments transferring momentum across the cell boundary under V1-retarded propagation.

**Chain-step momentum-transfer statistics.** A chain commitment at substrate position $\mathbf{x}_0$ with momentum $\mathbf{p}$ propagates to a neighboring substrate site at displacement $\boldsymbol{\delta}$ with V1-mediated rate $K_{V1}(|\boldsymbol{\delta}|)\,\Gamma_0(\rho_\mathrm{local})$ (parallel to Arc_D_2). The chain carries its momentum $\mathbf{p}$ during the step. Bulk-averaging over the local chain population at the cell boundary produces the cell-boundary momentum-flux tensor.

**Flux through a planar cell face.** Consider a planar boundary element of area $dS$ separating two adjacent cells with bulk velocities $\mathbf{v}_-$ and $\mathbf{v}_+$ (and densities $\rho_-$, $\rho_+$). The net rate at which $i$-component momentum crosses this boundary in the $+\hat n$ direction has two pieces:

- **Convective piece** (zeroth order in gradient): chains crossing the boundary carry their bulk velocity, so the convective momentum flux per unit area is $\rho v_i v_j \hat n^j$ at boundary midpoint, evaluated on the upstream side of the chain step. Symmetrically averaged across the boundary, this gives $\rho v_i v_j$ as the convective part of $\Pi_{ij}$.

- **Diffusive piece** (first order in gradient): the velocity differs across the cell, so chains crossing in the $+\hat n$ direction carry a slightly different momentum than chains crossing in $-\hat n$. Expanding $v_i$ at the boundary midpoint $\mathbf{x}_b$:

$$v_i(\mathbf{x}_\pm) \;=\; v_i(\mathbf{x}_b) \pm \tfrac{1}{2}\,\boldsymbol{\delta}\cdot\nabla v_i\bigl|_{\mathbf{x}_b} \;+\; \mathcal{O}(|\boldsymbol{\delta}|^2\,\nabla^2 v).$$

The net first-order contribution to the momentum flux is

$$\Pi^\mathrm{visc}_{ij} \;=\; -\rho\,\biggl[\!\int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,\delta^j\,\delta^k\biggr]\,\partial_k v_i \;+\; \cdots.$$

By isotropy of $K_{V1}$, the second-moment integral is diagonal:

$$\int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,\delta^j\,\delta^k \;=\; \tfrac{1}{3}\bigl\langle\delta^2\bigr\rangle_{V1}\,\delta^{jk},$$

where $\bigl\langle\delta^2\bigr\rangle_{V1} \equiv \int K_{V1}(|\boldsymbol{\delta}|)\,|\boldsymbol{\delta}|^2\,d^3\boldsymbol{\delta}$ is the V1-weighted second moment (a positive scalar, scaling as $\ell_P^2$ given V1's finite kernel width). Define the substrate-level kinematic viscosity

$$\mu(\rho) \;\equiv\; \tfrac{1}{3}\,\rho\,\bigl\langle\delta^2\bigr\rangle_{V1}\,\Gamma_0(\rho),$$

where the $\rho$- and $\Gamma_0$-dependence enters through the local participation-bandwidth-modulated transition rate (parallel to Arc_D_2's $M(\rho)$).

**Symmetric-gradient form.** Combining the two equivalent first-order expansions ($\partial_k v_i$ and $\partial_i v_k$, related by relabeling of contracted indices and by isotropy), the viscous flux can be written in symmetric form

$$\Pi^\mathrm{visc}_{ij} \;=\; -\mu(\rho)\,\bigl(\partial_i v_j + \partial_j v_i\bigr) \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^3 v\bigr),$$

the canonical Newtonian deviatoric stress (up to a trace contribution that is absorbed into the bulk viscosity / pressure when the incompressible limit is taken). The antisymmetric part cancels by V1 isotropy: the tensor $\int K_{V1}\,\delta^j\delta^k\,d^3\boldsymbol{\delta}$ is symmetric in $(j,k)$, so it cannot generate antisymmetric coupling between $\nabla v$ components.

**Total momentum flux.** Combining convective and viscous pieces:

$$\boxed{\;\Pi_{ij} \;=\; \rho\,v_i v_j \;-\; \mu(\rho)\,\bigl(\partial_i v_j + \partial_j v_i\bigr) \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^3 v\bigr) \;+\; p\,\delta_{ij}.\;}$$

Pressure $p\,\delta_{ij}$ enters as the isotropic part of $\Pi_{ij}$; it is the continuum-imposed Lagrange multiplier for incompressibility per the NS-2.08 / Appendix C classification (continuum constraint, not derived here).

The higher-order $\mathcal{O}(\ell_P^2\,\nabla^3 v)$ correction comes from the third-order term of the gradient expansion convolved with the second-moment of $K_{V1}$ (whose squared width is $\mathcal{O}(\ell_P^2)$). It is suppressed by $(\ell_P/L_\mathrm{flow})^2$ relative to the leading viscous term in the hydrodynamic window.

---

## 5. Step 3 — Momentum Conservation → Viscous Term

The coarse-grained momentum-conservation law on the cell is

$$\partial_t(\rho v_i) \;=\; -\partial_j \Pi_{ij}.$$

This is local conservation of substrate chain momentum, integrated over $\Omega$ with the slow-gradient assumption ($R_\mathrm{cg} \ll L_\mathrm{flow}$) reducing the surface-flux integral to a local divergence.

**Substitute the flux.** Using the Step 2 form $\Pi_{ij} = \rho v_i v_j - \mu(\rho)(\partial_i v_j + \partial_j v_i) + \mathcal{O}(\ell_P^2\nabla^3 v) + p\,\delta_{ij}$:

$$\partial_t(\rho v_i) \;=\; -\partial_j\bigl(\rho v_i v_j\bigr) \;+\; \partial_j\bigl[\mu(\rho)\bigl(\partial_i v_j + \partial_j v_i\bigr)\bigr] \;-\; \partial_i p \;+\; \mathcal{O}(\ell_P^2\,\nabla^4 v).$$

Under incompressibility $\partial_j v_j = 0$, the symmetric-gradient term simplifies to $\mu(\rho)\,\partial_j\partial_j v_i = \mu(\rho)\nabla^2 v_i$ (with subleading $\partial_j\mu\,\partial_i v_j$ pieces absorbed into a $\rho$-dependence correction). Combining with the continuity equation $\partial_t\rho = -\partial_j(\rho v_j)$ (Arc_D_2) to extract $\rho\,\partial_t v_i$ from $\partial_t(\rho v_i)$:

$$\boxed{\;\rho\,\partial_t v_i \;=\; \mu(\rho)\,\nabla^2 v_i \;-\; \rho(v_j\partial_j) v_i \;-\; \partial_i p \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^4 v\bigr).\;}$$

This is the standard Newtonian-fluid Navier-Stokes momentum equation (incompressible form), now derived from substrate primitives via hydrodynamic-window coarse-graining.

**Status of the higher-order correction.** The $\mathcal{O}(\ell_P^2\,\nabla^4 v)$ term is the directional-field counterpart of the scalar-side $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ correction recorded in Arc_D_2 §5. It is the **structural ancestor of R1**: under the V1 second-moment expansion, the next-to-leading-order coefficient produces the form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ stabilization (NS-3.01 / NS-Smooth-2). The explicit identification is reserved for Arc_D_4. For the present memo the correction is recorded but set aside; it is negligible at hydrodynamic scales but exactly the term that becomes load-bearing in the Clay-NS smoothness analysis.

**Note on classification.** The advective $-\rho(v_j\partial_j)v_i$ term in the boxed equation is the substrate-coarse-graining origin of the convective derivative — it is the divergence of the convective piece of $\Pi_{ij}$, $-\partial_j(\rho v_i v_j) = -\rho(v_j\partial_j)v_i - v_i\partial_j(\rho v_j)$, with the second piece vanishing in the incompressible limit. The substrate derivation thus *exhibits* advection as the Eulerian-coordinate bookkeeping of the convective momentum flux — confirming the NS-2.08 / NS-MHD-3 / Appendix C classification of advection as a frame-kinematic artifact rather than a force-from-stability. Arc D's scope is the canonical-side derivation; advection's frame-kinematic status is preserved unchanged.

---

## 6. Step 4 — Identification of the Viscosity $\mu(\rho)$

The viscosity function $\mu(\rho)$ identified in Step 2 inherits its structure from substrate physics:

- **Origin.** $\mu(\rho) = \tfrac{1}{3}\,\rho\,\bigl\langle\delta^2\bigr\rangle_{V1}\,\Gamma_0(\rho)$. Three substrate contributions: (i) the local mass density $\rho$ (linear), (ii) the V1-weighted second moment of the chain-step displacement $\bigl\langle\delta^2\bigr\rangle_{V1}$ (a substrate constant scaling as $\ell_P^2$), (iii) the participation-bandwidth-modulated transition rate $\Gamma_0(\rho)$ (P4-class, saturating to zero at $\rho_\mathrm{max}$).
- **ED-I-06 reading (§3).** $\mu(\rho)$ characterizes the bias on participation flow that smooths velocity-orientation gradients — the canonical directional-field-class force-from-stability sourced by the chain-population's directional-field structure on $\mathbf{v}$.
- **Form-FORCED structure.** The $\nabla^2$ Laplacian operator structure is FORCED by isotropy of V1 (second-moment integral diagonal) plus finite kernel width plus momentum conservation. The substrate-statistics realization gives $\mu(\rho)$ the form-FORCED dependence on V1 second-moment + $\Gamma_0(\rho)$.
- **Saturation at packing limit.** Like the scalar mobility $M(\rho)$, $\mu(\rho)$ inherits P4-class saturation: as $\rho \to \rho_\mathrm{max}$, $\Gamma_0(\rho) \to 0$ and hence $\mu(\rho) \to 0$. Physically: at participation-channel saturation, no chain-step momentum transfer can occur, so the bulk viscous transport coefficient vanishes.
- **Numerical values INHERITED.** All numerical factors — including $\bigl\langle\delta^2\bigr\rangle_{V1}$ (set by V1 kernel width), $\rho_\mathrm{max}$, the $\rho$-dependence shape of $\Gamma_0$ — are INHERITED at value layer per the program's standard form-FORCED / value-INHERITED methodology.

**Canonical properties of $\mu(\rho)$ (parallel to scalar $M(\rho)$).**

- $\mu(\rho) > 0$ for $0 < \rho < \rho_\mathrm{max}$.
- $\mu(\rho_\mathrm{max}) = 0$ (parallel to $M(\rho_\mathrm{max}) = 0$, same P4 substrate origin).
- $\mu(\rho)$ smooth on $[0,\rho_\mathrm{max}]$ (inherited from $\Gamma_0$ smoothness).
- $\mu(\rho)$ vanishes only at packing limit (parallel to scalar-mobility property).

These properties align exactly with the canonical PDE's mobility-channel ansatz applied to the velocity sector via the field-type-agnostic vector-extension (Architectural Canon Vector Extension memo). The substrate-derived $\mu(\rho)$ is the same object the canonical PDE postulates.

---

## 7. Step 5 — Result: Directional-Field Diffusion from Substrate

**Theorem (Arc_D_3 partial result, directional-field half of DCGT).**

> *Under hydrodynamic-window coarse-graining $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ over ED substrate primitives (chains, V1-retarded participation kernels, chain momentum-flux statistics), the cell-averaged velocity field $\mathbf{v}(\mathbf{x},t)$ satisfies the continuum Navier-Stokes momentum equation*
>
> $$\rho\,\partial_t\mathbf{v} \;=\; \mu(\rho)\,\nabla^2\mathbf{v} \;-\; \rho\,(\mathbf{v}\cdot\nabla)\mathbf{v} \;-\; \nabla p \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^4\mathbf{v}\bigr),$$
>
> *with substrate-derived kinematic viscosity $\mu(\rho) = \tfrac{1}{3}\,\rho\,\bigl\langle\delta^2\bigr\rangle_{V1}\,\Gamma_0(\rho)$. The Laplacian operator structure is FORCED by V1 isotropy + finite-width kernel + momentum conservation. The viscosity's qualitative properties ($\mu > 0$ in the bulk, $\mu = 0$ at packing, smoothness, P4-class saturation) are FORCED by substrate structure. Numerical values of $\mu(\rho)$ are INHERITED at value layer.*

This closes scope item S2 of Arc D and, paired with Arc_D_2's scalar-diffusion result, completes the substrate-to-continuum bridge for the canonical mobility channel in both scalar and directional-field cases.

**Summary of what is forced.**
- The Laplacian operator structure $\mu\nabla^2\mathbf{v}$ is FORCED by substrate momentum-flux gradient-expansion + isotropy + momentum conservation + hydrodynamic-window scale separation.
- The viscosity's qualitative properties ($\mu > 0$, $\mu \to 0$ at packing, smoothness) are FORCED by P4 substrate structure and the V1 kernel's finite width.
- The convective derivative $-\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ exhibits as the divergence of the convective momentum flux $\rho v_i v_j$, confirming its frame-kinematic Eulerian-bookkeeping status (NS-2.08 / Appendix C classification preserved).

**Summary of what is inherited.**
- The numerical values of $\mu(\rho)$ — including the V1 second-moment $\bigl\langle\delta^2\bigr\rangle_{V1}$, $\rho_\mathrm{max}$, $\Gamma_0$'s functional form — are INHERITED at value layer.
- The leading $\mathcal{O}(\ell_P^2\,\nabla^4\mathbf{v})$ correction has FORCED form (V1 kernel-moment expansion) but value-INHERITED coefficient. This is the **directional-field structural ancestor of R1**, made explicit in Arc_D_4.
- Pressure and incompressibility remain continuum-imposed constraints (NS-2.08 / Appendix C classification preserved).

---

## 8. Step 6 — Relation to NS and MHD

The Arc_D_3 directional-field-diffusion derivation has four direct downstream consequences:

**(i) Closes the directional-field half of the NS-2 INHERITED bridge.** Paired with Arc_D_2 (scalar diffusion), the NS-2 mobility-channel coarse-graining is now derived end-to-end from substrate primitives. NS-2.04 (momentum balance), NS-2.05 (stress tensor), NS-2.07 (synthesis), NS-2.08 (ED-PDE direct mapping) all read as substrate-grounded; the INHERITED bridge becomes FORCED-via-Arc-D.

**(ii) Provides the substrate origin of viscosity.** The kinematic viscosity $\mu$ that appears in the NS momentum equation, in the MHD magnetic-diffusion classification (under the appropriate $\rho_B \to \mathbf{B}$ vector-field substitution per Arc_D_4), and in the P4-NN Krieger-Dougherty derivation is identified as a substrate quantity: the $\rho$-modulated V1-second-moment integral. The four arcs share a single substrate origin, now identified in canonical form.

**(iii) Sets up Arc_D_4 (kernel coarse-graining → R1 emergence).** The $\mathcal{O}(\ell_P^2\,\nabla^4\mathbf{v})$ correction recorded in Step 5 is the structural ancestor of R1. Arc_D_4 will explicitly identify the next-to-leading-order V1 kernel moment as the source of the $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ form-FORCED hyperviscous stabilization (NS-3.01 / NS-Smooth-2). The consistency loop is: Arc_D_2 / Arc_D_3 record the correction → Arc_D_4 derives R1's coefficient → consistency with NS-3.01's form-FORCED derivation confirms the substrate-bridge.

**(iv) Provides the substrate-level foundation for Lorentz coarse-graining in Arc_D_5.** The chain-momentum-flux machinery developed here generalizes directly to charged-chain populations under T17 minimal coupling. Arc_D_5 will replace neutral-chain $\Gamma_0$ with the charged-chain transition rate that includes the gauge-coupling vertex $\partial_\mu \to \partial_\mu - iqA_\mu$ at the substrate level, then coarse-grain to obtain the fluid-level Lorentz force density. The coarse-graining method is the same as the present memo's, with charge degree of freedom added.

The directional-field half of Arc D's substrate-to-continuum bridge is closed.

---

## 9. Recommended Next Steps

Proceed to **Arc_D_4 (Kernel Coarse-Graining)**. File: `theory/Arc_D/Arc_D_4_Kernel_Coarse_Graining.md`. Scope: explicitly coarse-grain V1 finite-width vacuum kernel and V5 cross-chain kernel to identify (i) the R1 hyperviscous emergence at fluid scale ($-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$, consistency with NS-3.01 / NS-Smooth-2 form-FORCED derivation) and (ii) the V5 cross-chain-memory contribution at fluid scale (consistency with P4-NN-D5 viscoelastic ansatz $\tau_R\dot\sigma + \sigma = 2\mu S$). Verify causal-structure preservation under coarse-graining (T18 inherited).

Estimated 1–2 sessions for Arc_D_4.

### Decisions for you

- **Confirm directional-field diffusion derivation.** Laplacian form $\mu\nabla^2\mathbf{v}$ FORCED by V1 isotropy + finite-width kernel + momentum conservation + hydrodynamic-window scale separation. $\mu(\rho)$ form-FORCED by V1 second-moment + P4 substrate structure; values INHERITED.
- **Confirm $\mathcal{O}(\ell_P^2\,\nabla^4\mathbf{v})$ correction parking.** Recorded as directional-field structural ancestor of R1; explicit derivation in Arc_D_4.
- **Confirm preservation of advection's frame-kinematic status.** Substrate derivation exhibits $-\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ as Eulerian bookkeeping of the convective momentum flux $\rho v_i v_j$; NS-2.08 / Appendix C classification preserved.
- **Confirm proceeding to Arc_D_4 (kernel coarse-graining → R1 emergence + V5 memory at fluid scale).**

---

*Arc_D_3 closes the directional-field half of DCGT. Continuum NS momentum equation $\rho\,\partial_t\mathbf{v} = \mu(\rho)\nabla^2\mathbf{v} - \rho(\mathbf{v}\cdot\nabla)\mathbf{v} - \nabla p + \mathcal{O}(\ell_P^2\nabla^4\mathbf{v})$ derived from ED substrate primitives via hydrodynamic-window coarse-graining of V1-mediated chain momentum-flux. Laplacian form FORCED; viscosity $\mu(\rho) = \tfrac{1}{3}\rho\bigl\langle\delta^2\bigr\rangle_{V1}\Gamma_0(\rho)$ form-FORCED by V1 second-moment + P4 substrate; numerical values INHERITED. Higher-order $\mathcal{O}(\ell_P^2\nabla^4\mathbf{v})$ correction recorded as directional-field structural ancestor of R1 (Arc_D_4). Convective derivative $-\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ exhibits as Eulerian bookkeeping of the convective momentum flux — NS-2.08 / Appendix C frame-kinematic classification preserved. Closes directional-field half of NS-2 INHERITED bridge; paired with Arc_D_2, completes NS-2 mobility-channel substrate-bridge. Arc_D_4 (kernel coarse-graining: V1 → R1, V5 → memory) is the next deliverable.*
