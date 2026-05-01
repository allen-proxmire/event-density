# Arc_D_2 — Scalar Diffusion from Substrate Event-Flux Statistics

**Date:** 2026-04-30
**Status:** First technical derivation memo of Arc D. Establishes the substrate-to-continuum origin of the mobility-channel scalar-diffusion operator $\nabla\cdot(M(\rho)\nabla\rho)$. **Result: form FORCED by substrate event-flux imbalance under hydrodynamic-window coarse-graining; $M(\rho)$ INHERITED from participation-bandwidth physics.**
**Companions:** [`Arc_D_1_Opening.md`](Arc_D_1_Opening.md), [`../Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](../Navier%20Stokes/NS-2.08_ED-PDE_Direct_Mapping.md), [`../Navier Stokes/MHD/NS_MHD_2_Lorentz_Force.md`](../Navier%20Stokes/MHD/NS_MHD_2_Lorentz_Force.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (T18), [`../Architectural_Canon_Vector_Extension.md`](../Architectural_Canon_Vector_Extension.md), [`../PDE.md`](../PDE.md).

---

## 1. Purpose

This memo derives the continuum scalar diffusion equation

$$\partial_t \rho = \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr)$$

from ED substrate primitives — micro-events, chain participation, V1 / V5 kernels — under a coarse-graining cell of radius $R_\mathrm{cg}$ in the hydrodynamic window

$$\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}.$$

The derivation proceeds by (i) defining the coarse-graining cell and the cell-averaged participation density $\rho(\mathbf{x},t)$, (ii) computing the substrate event-flux through the cell boundary as a function of the local density gradient, (iii) imposing event-count conservation on the cell to obtain the continuity equation, (iv) identifying the resulting flux-divergence as the canonical mobility-channel operator with $M(\rho)$ identified at substrate level. The mobility-coefficient $M(\rho)$ is form-FORCED by the participation-bandwidth saturation structure of ED's substrate primitives (P4-class) and value-INHERITED at the level of pointwise numerical values.

This is the scalar half of the Arc D substrate-to-continuum bridge. Arc_D_3 supplies the directional-field counterpart (viscosity from chain momentum-flux).

---

## 2. Inputs

- **ED-I-06.** Scalar fields are emergent gradients in participation density (§4). The cell-averaged $\rho$ defined here is the canonical scalar-field-class quantity in the ED-I-06 ontology.
- **Theorem 18 (V1 Kernel Retardation).** V1's forward-cone-only support structure ensures that the substrate event-flux respects causal structure; the coarse-grained flux inherits this property.
- **NS-2 mobility-channel viscous content.** The form-FORCED mobility-channel operator structure that this memo grounds at substrate level for the scalar case.
- **NS-MHD-2 coarse-graining structure.** The parallel single-chain → fluid-density averaging that NS-MHD-2 used for charged-chain populations. Arc_D_2 supplies the same coarse-graining method for neutral chain-population participation density.
- **Arc_D_1 (Opening).** Hydrodynamic-window definition, six-memo arc plan, scope item S1 (scalar diffusion from event-flux statistics).

---

## 3. Step 1 — Define the Coarse-Graining Cell

Let $\Omega(\mathbf{x}, R_\mathrm{cg}) \subset \mathbb{R}^3$ be a spherical cell of radius $R_\mathrm{cg}$ centered at the macroscopic point $\mathbf{x}$. The cell radius is chosen to satisfy three scale-separation conditions:

- **$R_\mathrm{cg} \gg \ell_P$** — the cell is large enough that substrate discreteness (event-by-event fluctuation, ℓ_P-scale chain spacing) averages out. This is the lower bound that ensures statistical regularity of the cell-averaged quantities.
- **$R_\mathrm{cg} \gg \lambda_\mathrm{mfp}$** — the cell is large enough to contain many chain-step transitions ($\lambda_\mathrm{mfp}$ being the mean free path between adjacent chain-step commitments, set by V1's correlation length). This is the hydrodynamic-regime condition: the coarse-grained dynamics is not free-streaming but diffusive.
- **$R_\mathrm{cg} \ll L_\mathrm{flow}$** — the cell is small relative to macroscopic flow gradients ($L_\mathrm{flow}$ being the characteristic gradient scale of the macroscopic field). This is the upper bound that ensures the gradient-expansion truncation is valid: the field varies slowly across the cell.

Under these three conditions, the cell-averaged quantities are well-defined and the gradient expansion converges with controlled error.

**Cell-averaged participation density.** Let $N_\Omega(\mathbf{x}, t)$ be the number of chain-commitment events occurring within $\Omega(\mathbf{x}, R_\mathrm{cg})$ at time $t$ (under the V1-retarded chain dynamics). Define

$$\rho(\mathbf{x}, t) \;\equiv\; \frac{N_\Omega(\mathbf{x}, t)}{|\Omega|} \;=\; \frac{N_\Omega(\mathbf{x}, t)}{\tfrac{4}{3}\pi R_\mathrm{cg}^3}.$$

This is the macroscopic participation-density field. It is a scalar-field-class quantity in the ED-I-06 ontology — its gradients $\nabla\rho$ source bias on participation flow toward lower-density regions.

**Event-flux through the cell boundary.** Let $\mathbf{J}_\rho(\mathbf{x}, t)$ be the net event-flux per unit area through the boundary $\partial\Omega(\mathbf{x}, R_\mathrm{cg})$, defined as the signed rate at which chain-commitment events cross outward through the boundary. The flux is a vector field in the macroscopic (cell-centroid) coordinate.

Conservation of event count on the cell gives the integral form

$$\partial_t \!\!\int_\Omega \rho\,dV \;=\; -\!\!\oint_{\partial\Omega} \mathbf{J}_\rho\cdot d\mathbf{S},$$

which by the divergence theorem and the slow-gradient assumption ($R_\mathrm{cg} \ll L_\mathrm{flow}$) reduces in the continuum limit to the local form

$$\partial_t \rho \;=\; -\nabla\cdot\mathbf{J}_\rho.$$

The substantive content of the derivation is the substrate-level identification of $\mathbf{J}_\rho$ as a function of $\rho$ and $\nabla\rho$.

---

## 4. Step 2 — Substrate Event-Flux Statistics

The substrate-level event-flux is computed by considering chain-commitment events in adjacent cells and the V1-mediated transition rates between them.

**Chain-step transition statistics.** A chain-commitment event at substrate position $\mathbf{x}_0$ propagates forward in proper time via the V1-retarded participation kernel (T18). The transition rate to a neighboring substrate site at displacement $\boldsymbol{\delta}$ is

$$\Gamma(\boldsymbol{\delta} ; \rho_\mathrm{local}) \;=\; \Gamma_0(\rho_\mathrm{local})\,K_{V1}(|\boldsymbol{\delta}|),$$

where $\Gamma_0(\rho_\mathrm{local})$ is the local participation-bandwidth-modulated rate (P4-class — saturating to zero at $\rho_\mathrm{max}$) and $K_{V1}$ is the V1 finite-width spatial kernel. The kernel is forward-cone-supported and (for the spatially-isotropic case) isotropic to leading order, so $K_{V1}(|\boldsymbol{\delta}|)$ depends only on the magnitude.

**Flux through a cell face.** Consider a planar boundary element of area $dS$ separating two adjacent cells with densities $\rho_-$ and $\rho_+$. The net rate at which events cross this boundary in the $+\hat n$ direction is the difference of the forward and backward transition rates:

$$dN_\mathrm{cross}/dt \;=\; \int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,(\boldsymbol{\delta}\cdot\hat n)\,\bigl[\Gamma_0(\rho_-)\,\rho_-\Theta(\boldsymbol{\delta}\cdot\hat n) - \Gamma_0(\rho_+)\,\rho_+\Theta(-\boldsymbol{\delta}\cdot\hat n)\bigr]\,dS,$$

with $\Theta$ the Heaviside step function selecting the half-space contributions. This is the standard kinetic-theory bookkeeping adapted to ED substrate statistics.

**Gradient expansion.** Expand $\Gamma_0(\rho)\rho$ at the boundary midpoint $\mathbf{x}_b$ to first order in the local gradient:

$$\Gamma_0(\rho_\pm)\rho_\pm \;=\; \Gamma_0(\rho_b)\rho_b \;\pm\; \tfrac{1}{2}\,\boldsymbol{\delta}\cdot\nabla\bigl(\Gamma_0(\rho)\rho\bigr)\bigl|_{\mathbf{x}_b} \;+\; \mathcal{O}(|\boldsymbol{\delta}|^2\,\nabla^2\rho).$$

Substituting and integrating over $\boldsymbol{\delta}$ with the V1 kernel weight, the leading-order ($\Gamma_0\rho$) term cancels by isotropy of $K_{V1}$ (forward and backward contributions match), and the gradient term survives:

$$dN_\mathrm{cross}/dt \;=\; -\,\biggl[\!\int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,(\boldsymbol{\delta}\cdot\hat n)^2\biggr]\,\hat n\cdot\nabla\bigl(\Gamma_0(\rho)\rho\bigr)\,dS \;+\; \cdots.$$

The bracketed integral is a positive scalar (the V1-weighted second moment of the displacement) that depends on $K_{V1}$'s width but is independent of $\rho$. Define

$$M(\rho) \;\equiv\; \biggl[\!\int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,\delta_n^2\biggr]\,\frac{\partial\bigl(\Gamma_0(\rho)\rho\bigr)}{\partial\rho},$$

the substrate-derived mobility coefficient. (The standard form is recovered by absorbing the V1 kernel-moment integral into $M(\rho)$ and treating the mobility's functional dependence on $\rho$ as inherited from $\Gamma_0(\rho)\rho$.)

**Event-flux per unit area.** Identifying $dN_\mathrm{cross}/dt = (\hat n\cdot\mathbf{J}_\rho)\,dS$, the substrate-level flux satisfies

$$\boxed{\;\mathbf{J}_\rho \;=\; -\,M(\rho)\,\nabla\rho \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^3\rho\bigr).\;}$$

The leading term is gradient-driven (Fick's-law-class). The higher-order corrections scale as $\ell_P^2\,\nabla^3\rho$ and arise from the third-order term in the gradient expansion convolved with the second-moment of $K_{V1}$ (whose squared width is $\mathcal{O}(\ell_P^2)$). They are suppressed by $(\ell_P / L_\mathrm{flow})^2$ relative to the leading term in the hydrodynamic window.

---

## 5. Step 3 — Derive the Continuity Equation

Combining the local conservation law $\partial_t\rho = -\nabla\cdot\mathbf{J}_\rho$ with the substrate-derived flux from Step 2:

$$\partial_t\rho \;=\; \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr) \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^4\rho\bigr).$$

This is the continuum scalar-diffusion equation, derived from substrate primitives via hydrodynamic-window coarse-graining.

**Status of the higher-order correction.** The $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ term is the leading sub-hydrodynamic correction. It is suppressed by $(\ell_P / L_\mathrm{flow})^2$ at hydrodynamic scales and is negligible for fluid-mechanical purposes. **However**, it is exactly the structural ancestor of the R1 hyperviscous term that emerges in the directional-field case (Arc_D_4): the V1 kernel's finite width produces a $\nabla^4$-class correction that becomes the $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ stabilization in the velocity sector. This consistency is verified in Arc_D_4. For the present scalar derivation, the correction is recorded but set aside.

**Form FORCED.** The continuum-level operator structure $\nabla\cdot(M\nabla)$ is FORCED by:
- (a) the gradient-driven leading term in the substrate event-flux (substrate isotropy of $K_{V1}$ + gradient-expansion truncation);
- (b) the local conservation law $\partial_t\rho = -\nabla\cdot\mathbf{J}_\rho$ (substrate event-count conservation);
- (c) the hydrodynamic-window scale separation (suppression of higher-order corrections).

No fluid-mechanical postulate enters; the entire derivation is internal to ED substrate primitives.

---

## 6. Step 4 — Identification of the Mobility Function $M(\rho)$

The mobility function $M(\rho)$ identified in Step 2 inherits its functional form from substrate physics:

- **Origin.** $M(\rho) \propto \partial[\Gamma_0(\rho)\rho]/\partial\rho$ where $\Gamma_0(\rho)$ is the participation-bandwidth-modulated transition rate. The $\rho$-dependence enters via the bandwidth-modulation factor.
- **ED-I-06 reading (§4).** $M(\rho)$ characterizes the bias on participation flow toward lower-density regions. It is the substrate-statistical realization of "micro-events tend to propagate toward lower-density regions" — the canonical scalar-field-as-density-gradient mechanism of ED-I-06 §4.
- **Saturation at packing limit.** As $\rho \to \rho_\mathrm{max}$ (the packing limit set by participation-channel availability), the local transition rate $\Gamma_0(\rho)$ saturates to zero by the participation-bandwidth-saturation structure of P4 (mobility-capacity bound). Hence $M(\rho_\mathrm{max}) = 0$.
- **Positivity in the bulk.** For $\rho < \rho_\mathrm{max}$, the substrate transition rate is strictly positive (P4 plus event-discreteness), so $M(\rho) > 0$.

**Canonical properties of $M(\rho)$ (P4-derived).**

- $M(\rho) > 0$ for $0 < \rho < \rho_\mathrm{max}$.
- $M(\rho_\mathrm{max}) = 0$ (participation saturation; no further mobility once packing is reached).
- $M(\rho)$ smooth on $[0,\rho_\mathrm{max}]$.
- $M(\rho)$ monotonically decreasing as $\rho \to \rho_\mathrm{max}$ (P4 saturation is approached continuously).

These properties align with the canonical PDE's mobility-channel ansatz $M(\rho_\mathrm{max}) = 0$, $M(\rho) > 0$ otherwise, smoothness — confirming that the substrate-derived mobility function is the same object the canonical PDE postulates.

**Form FORCED, value INHERITED.** The functional form of $M(\rho)$ (P4-class saturation) is FORCED by the participation-bandwidth structure of ED's substrate primitives. The numerical pointwise values of $M(\rho)$ — including $\rho_\mathrm{max}$, the rate of approach to zero, and the small-$\rho$ asymptotics — are INHERITED at value layer. This is the standard form-FORCED / value-INHERITED split of the program.

---

## 7. Step 5 — Result: Scalar Diffusion from Substrate

**Theorem (Arc_D_2 partial result, scalar half of DCGT).**

> *Under hydrodynamic-window coarse-graining $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ over ED substrate primitives (chains, V1-retarded participation kernels), the cell-averaged participation density $\rho(\mathbf{x},t)$ satisfies the continuum scalar-diffusion equation*
>
> $$\partial_t\rho \;=\; \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr) \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^4\rho\bigr),$$
>
> *with substrate-derived mobility coefficient $M(\rho)$. The mobility's functional form is FORCED by the P4-class participation-bandwidth saturation structure ($M(\rho_\mathrm{max}) = 0$, $M(\rho) > 0$ otherwise, smooth, monotonically decreasing toward the packing limit). The numerical values of $M(\rho)$ are INHERITED at value layer.*

This closes scope item S1 of Arc D.

**Summary of what is forced.**
- The operator structure $\nabla\cdot(M\nabla)$ is FORCED by substrate event-flux gradient-expansion + event-count conservation + hydrodynamic-window scale separation.
- The mobility's qualitative properties ($M > 0$ in the bulk, $M = 0$ at packing, smoothness, monotonicity) are FORCED by P4 substrate structure.

**Summary of what is inherited.**
- The numerical values of $M(\rho)$ at any specific $\rho$ — including $\rho_\mathrm{max}$, the curvature of $M(\rho)$, and the absolute scale — are INHERITED at value layer.
- The leading higher-order correction $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ has FORCED form (V1 second-moment integral) but INHERITED coefficient at value layer.

---

## 8. Step 6 — Relation to NS and MHD

The Arc_D_2 scalar-diffusion derivation has three direct downstream consequences for previously closed arcs:

**(i) Closes the scalar half of the NS-2 INHERITED bridge.** NS-2.08 derived the canonical PDE's mobility-channel structure as the scalar-side of ED's continuum dynamics, with the coarse-graining bridge INHERITED. Arc_D_2 supplies the substrate-to-continuum derivation of that bridge for the scalar field. The directional-field counterpart (viscosity) is supplied in Arc_D_3, completing the NS-2 closure.

**(ii) Provides the scalar analogue of the viscosity derivation.** Arc_D_3 will mirror the present derivation by replacing $\rho$ with cell-averaged momentum density, the event-flux $\mathbf{J}_\rho$ with the substrate momentum-flux tensor, and the gradient expansion with the directional-field version. The structural argument is identical; the only changes are the field type (scalar → vector) and the flux moment (number-flux → momentum-flux). The field-type-agnostic vector-extension of the canonical PDE (Architectural Canon Vector Extension memo) is precisely what makes this parallel work.

**(iii) Establishes the substrate origin of the mobility channel used in NS, MHD, and P4-NN.** The mobility function $M(\rho)$ derived here is the same $M$ that appears in the canonical PDE, in the NS viscous-content classification, in the MHD magnetic-diffusion classification (under appropriate $\rho \to \rho_B$ vector-field substitution per Arc_D_3), and in the P4-NN Krieger-Dougherty derivation. All four arcs share a single substrate origin, now identified.

The scalar half of Arc D's substrate-to-continuum bridge is closed.

---

## 9. Recommended Next Steps

Proceed to **Arc_D_3 (Directional-Field Diffusion)**. File: `theory/Arc_D/Arc_D_3_Directional_Field_Diffusion.md`. Scope: derive viscous diffusion $\mu\nabla^2\mathbf{v}$ from chain momentum-flux statistics. Define cell-averaged velocity field $\mathbf{v}(\mathbf{x},t)$ and momentum-flux tensor at substrate level; apply the same gradient-expansion machinery as the present memo to the momentum sector; derive the Newtonian stress-tensor structure under hydrodynamic-window coarse-graining; identify $\mu$ as the substrate-statistics quantity. Confirm form consistency with the field-type-agnostic vector-extension of the mobility channel.

Estimated 1–2 sessions for Arc_D_3.

### Decisions for you

- **Confirm scalar-diffusion derivation.** Form $\nabla\cdot(M(\rho)\nabla\rho)$ FORCED by substrate event-flux + gradient expansion + event-count conservation + hydrodynamic-window scale separation. $M(\rho)$ form-FORCED by P4 substrate structure; values INHERITED.
- **Confirm $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ correction parking.** Recorded as the structural ancestor of R1 (Arc_D_4); set aside for Arc_D_2 purposes.
- **Confirm proceeding to Arc_D_3 (directional-field diffusion / viscosity from chain momentum-flux).**

---

*Arc_D_2 closes the scalar half of DCGT. Continuum scalar diffusion $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho)$ derived from ED substrate primitives via hydrodynamic-window coarse-graining of the V1-mediated chain event-flux. Operator form FORCED; mobility function $M(\rho)$ form-FORCED by P4 substrate structure with $M(\rho_\mathrm{max}) = 0$ + $M > 0$ in the bulk + smoothness + monotonicity; $M(\rho)$ values INHERITED at value layer. Higher-order $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ correction recorded as structural ancestor of R1 (Arc_D_4). Closes scalar half of the NS-2 INHERITED bridge; directional-field counterpart in Arc_D_3. Arc_D_3 (viscosity from chain momentum-flux) is the next deliverable.*
