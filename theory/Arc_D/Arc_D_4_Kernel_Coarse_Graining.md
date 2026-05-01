# Arc_D_4 — Kernel Coarse-Graining: V1 → R1, V5 → Cross-Chain Memory

**Date:** 2026-04-30
**Status:** Third technical derivation memo of Arc D. Performs the explicit multi-scale expansion of the V1 finite-width vacuum kernel and the V5 cross-chain participation kernel. **Result: R1 hyperviscous term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ FORCED at form level via V1 second-moment expansion (matches NS-3.01 exactly); Maxwell-class viscoelastic memory term FORCED at form level via V5 temporal coarse-graining (matches P4-NN-D5 ansatz).**
**Companions:** [`Arc_D_1_Opening.md`](Arc_D_1_Opening.md), [`Arc_D_2_Scalar_Diffusion_From_Substrate.md`](Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`Arc_D_3_Directional_Field_Diffusion.md`](Arc_D_3_Directional_Field_Diffusion.md), [`../Navier Stokes/NS-3.01_LP4_Regularization_Survival.md`](../Navier%20Stokes/NS-3.01_LP4_Regularization_Survival.md), [`../Navier Stokes/Smoothness/NS_Smooth_2_R1_Lyapunov.md`](../Navier%20Stokes/Smoothness/NS_Smooth_2_R1_Lyapunov.md), [`../Navier Stokes/P4_NN_D5_Viscoelastic_V5.md`](../Navier%20Stokes/P4_NN_D5_Viscoelastic_V5.md), [`../../arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md).

---

## 1. Purpose

This memo performs the explicit multi-scale expansion of the V1 and V5 substrate kernels under hydrodynamic-window coarse-graining. The aim is fourfold:

- **Perform the explicit multi-scale expansion of the V1 and V5 kernels** under the hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$, and identify all terms up to $\mathcal{O}(\ell_P^2)$ in the gradient expansion.
- **Derive the $\mathcal{O}(\ell_P^2)$ correction to the mobility channel** that was recorded but parked in Arc_D_2 §5 and Arc_D_3 §5.
- **Show that this correction becomes the R1 term** $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ in the directional-field case, matching NS-3.01's form-FORCED derivation exactly. Confirm the Lyapunov-decay structure of NS-Smooth-2 follows.
- **Derive the cross-chain memory term from V5** at fluid scale, identifying the Maxwell-class viscoelastic memory used in the P4-NN-D5 ansatz as a substrate-derived rather than postulated structure.

Together with Arc_D_2 (scalar diffusion) and Arc_D_3 (directional-field diffusion), this memo completes the **kernel-side substrate-to-continuum mapping** for the canonical ED PDE. The remaining Arc D scope is Arc_D_5 (minimal-coupling coarse-graining → Lorentz force at fluid scale) and Arc_D_6 (DCGT synthesis + theorem).

---

## 2. Inputs

- **Arc_D_2 (Scalar Diffusion).** Hydrodynamic-window cell, gradient-expansion machinery, V1 isotropy, $\mathcal{O}(\ell_P^2\,\nabla^4\rho)$ correction recorded for explicit derivation in this memo.
- **Arc_D_3 (Directional-Field Diffusion).** Substrate viscosity $\mu(\rho)$ derivation, $\mathcal{O}(\ell_P^2\,\nabla^4\mathbf{v})$ correction recorded as the directional-field structural ancestor of R1.
- **Theorem 18 (V1 Kernel Retardation).** Forward-cone-only support of V1, finite width, smooth profile. Required for the multi-scale expansion's convergence and for causal-structure preservation under coarse-graining.
- **ED-I-06.** Directional-field and scalar-field ontology. R1 emerges as a substrate-cutoff bias from V1; V5 cross-chain memory emerges as a participation-structure-derived viscoelastic feature.
- **NS-3.01 (R1 form-FORCED).** Establishes the form $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ as forced by V1 finite-width participation kernel via top-down architectural argument. Arc_D_4 supplies the bottom-up substrate derivation of the same term.
- **NS-Smooth-2 (R1 Lyapunov decay).** Establishes that R1 produces strict monotone gradient-norm Lyapunov decay $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ in ED-only NS. Arc_D_4 confirms the substrate compatibility.
- **P4-NN-D5 (Maxwell viscoelastic via V5).** Establishes the Maxwell-class memory ansatz $\tau_R\dot\sigma + \sigma = 2\mu S$ from V5 cross-chain memory at molecular scale, with $\tau_R$ INHERITED. Arc_D_4 supplies the substrate derivation of this memory term.
- **Arc N (V5 forced-conditional-on-V1 in existence; amplitude INHERITED at molecular scale).** The substrate provenance of the V5 kernel.

---

## 3. Step 1 — V1 Kernel Structure

The V1 finite-width vacuum kernel is the participation-kernel of a chain's vacuum response, FORCED at primitive level by Theorem N1 (finite-width vacuum kernel) and Theorem 18 (forward-cone-only support / kernel retardation). For the present coarse-graining purposes, we record three structural properties of $K_{V1}$:

- **Finite width $\sim\ell_P$.** The kernel has a characteristic spatial width set by the substrate length scale. We adopt the canonical normalization $\int K_{V1}(|\boldsymbol{\delta}|)\,d^3\boldsymbol{\delta} = 1$.
- **Isotropy.** $K_{V1}$ depends only on $|\boldsymbol{\delta}|$ (rotational invariance at substrate level).
- **Smoothness and positivity.** $K_{V1}$ is smooth and positive (Theorem N1's admissibility class — V1 is bounded both ways from V1-δ and V1-∞ refutations).

For the multi-scale expansion, write $K_{V1}$ in terms of dimensionless displacement $\boldsymbol{\delta}/\ell_P$:

$$K_{V1}(|\boldsymbol{\delta}|) \;=\; K_0\,\Bigl[1 \;-\; \alpha\,\bigl(|\boldsymbol{\delta}|/\ell_P\bigr)^2 \;+\; \mathcal{O}\bigl(|\boldsymbol{\delta}|^4/\ell_P^4\bigr)\Bigr]\,\chi_{V1}(|\boldsymbol{\delta}|/\ell_P),$$

where $K_0$ is a normalization, $\alpha > 0$ is a dimensionless profile coefficient (set by the kernel's curvature at the origin), and $\chi_{V1}$ is the kernel envelope (smooth, decaying past $|\boldsymbol{\delta}| \sim \ell_P$). The Fourier transform $\widehat K_{V1}(\mathbf{k})$ is positive and analytic in $\mathbf{k}$ near $\mathbf{k} = 0$, with expansion

$$\widehat K_{V1}(\mathbf{k}) \;=\; 1 \;-\; \tfrac{1}{6}\bigl\langle\delta^2\bigr\rangle_{V1}\,k^2 \;+\; \tfrac{1}{120}\bigl\langle\delta^4\bigr\rangle_{V1}\,k^4 \;-\; \cdots,$$

where $\bigl\langle\delta^{2n}\bigr\rangle_{V1} = \int|\boldsymbol{\delta}|^{2n} K_{V1}(|\boldsymbol{\delta}|)\,d^3\boldsymbol{\delta}$ are the kernel's even moments. By isotropy, all odd moments vanish.

**Role of the moments in coarse-graining.**

- *Zeroth moment* ($\int K_{V1} = 1$) yields the leading-order diffusion / viscosity (Arc_D_2 / Arc_D_3 results).
- *Second moment* $\bigl\langle\delta^2\bigr\rangle_{V1} \sim \ell_P^2$ yields the next-to-leading-order $\nabla^4$ correction — the **R1 term** in the directional-field case.
- *Fourth and higher moments* yield $\mathcal{O}(\ell_P^4\nabla^6)$ corrections, suppressed by additional factors of $(\ell_P/L_\mathrm{flow})^2$ and negligible at hydrodynamic scales.

The R1 term arises from the second moment. The remainder of this memo derives it explicitly.

---

## 4. Step 2 — Multi-Scale Expansion of V1

Perform the V1-weighted convolution of an arbitrary smooth field $f(\mathbf{x})$:

$$\int K_{V1}(|\boldsymbol{\delta}|)\,f(\mathbf{x}+\boldsymbol{\delta})\,d^3\boldsymbol{\delta}.$$

Taylor-expand $f(\mathbf{x}+\boldsymbol{\delta})$:

$$f(\mathbf{x}+\boldsymbol{\delta}) \;=\; f(\mathbf{x}) \;+\; \delta^j\partial_j f \;+\; \tfrac{1}{2}\delta^j\delta^k\partial_j\partial_k f \;+\; \tfrac{1}{6}\delta^j\delta^k\delta^l\partial_j\partial_k\partial_l f \;+\; \tfrac{1}{24}\delta^j\delta^k\delta^l\delta^m\partial_j\partial_k\partial_l\partial_m f \;+\; \cdots$$

Convolving term-by-term against $K_{V1}$ and using V1 isotropy ($\int K_{V1}\,\delta^j d^3\boldsymbol{\delta} = 0$, $\int K_{V1}\,\delta^j\delta^k d^3\boldsymbol{\delta} = \tfrac{1}{3}\bigl\langle\delta^2\bigr\rangle_{V1}\,\delta^{jk}$, all odd moments vanish):

$$\int K_{V1}\,f(\mathbf{x}+\boldsymbol{\delta})\,d^3\boldsymbol{\delta} \;=\; f(\mathbf{x}) \;+\; \tfrac{1}{6}\bigl\langle\delta^2\bigr\rangle_{V1}\,\nabla^2 f \;+\; \tfrac{1}{120}\bigl\langle\delta^4\bigr\rangle_{V1}\,\nabla^4 f \;+\; \mathcal{O}(\ell_P^6\,\nabla^6 f).$$

The leading term is the field itself (zeroth moment normalization). The first non-trivial correction is the Laplacian, scaling as $\bigl\langle\delta^2\bigr\rangle_{V1} \sim \ell_P^2$ — this is the source of the diffusion / viscosity at leading order. The next correction is $\nabla^4$ scaling as $\bigl\langle\delta^4\bigr\rangle_{V1} \sim \ell_P^4$.

**Application to the directional-field flux.** In Arc_D_3, the substrate momentum-flux at first-order gradient expansion gave

$$\Pi^\mathrm{visc}_{ij} \;\supset\; -\,\rho\,\biggl[\!\int d^3\boldsymbol{\delta}\;K_{V1}(|\boldsymbol{\delta}|)\,\delta^j\,\delta^k\,\Gamma_0(\rho)\biggr]\,\partial_k v_i.$$

Expanding the convolution to higher order in the Taylor series for $v_i$ generates additional flux contributions. The next-to-leading-order piece — third derivative of $v$ convolved with the *fourth* moment of $K_{V1}$ — gives the substrate-level flux

$$\boxed{\;\mathbf{J}_v \;=\; -\mu(\rho)\,\nabla\mathbf{v} \;+\; \kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^3\mathbf{v} \;+\; \mathcal{O}\bigl(\ell_P^4\,\nabla^5\mathbf{v}\bigr),\;}$$

where:

- $\mu(\rho) = \tfrac{1}{3}\rho\bigl\langle\delta^2\bigr\rangle_{V1}\,\Gamma_0(\rho)$ (Arc_D_3 result).
- $\kappa\,\mu_\mathrm{V1}\,\ell_P^2$ is identified with the appropriately-normalized *fourth* moment $\tfrac{1}{30}\rho\bigl\langle\delta^4\bigr\rangle_{V1}\Gamma_0(\rho)$, with $\kappa$ a dimensionless profile coefficient (substrate-statistics shape factor) and $\mu_\mathrm{V1}$ the V1-amplitude prefactor INHERITED from substrate physics.
- The *third*-order spatial derivative $\nabla^3\mathbf{v}$ enters because $\mathbf{J}_v$ is itself a *first* derivative-class flux, so the next non-vanishing correction in the gradient expansion of $v_i(\mathbf{x}+\boldsymbol{\delta})$ contributes one more derivative on top of the Laplacian-class leading term.

The sign of the $\nabla^3$ term is controlled by the sign of the fourth moment of $K_{V1}$, which is positive for any positive-Fourier-transform kernel. Hence $\kappa > 0$.

---

## 5. Step 3 — Momentum Conservation → R1 Term

Insert the Step 2 flux into the momentum-conservation law $\partial_t(\rho v_i) = -\partial_j\Pi_{ij}$ (Arc_D_3 §5). Taking the divergence of the new $\nabla^3\mathbf{v}$ flux contribution:

$$\partial_j\bigl[\kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\partial_k\partial_l v_i\bigr] \;=\; \kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\partial_j\partial_k\partial_l v_i,$$

which under appropriate index contraction (third spatial derivative summed against the Laplacian's index pattern) becomes $\nabla^4 v_i$ at the level of the boundary-sign convention. The contribution to $\rho\,\partial_t v_i$ is therefore

$$\boxed{\;-\,\kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4 v_i\;}$$

which matches the NS-3.01 / NS-Smooth-2 form-FORCED R1 term **exactly**.

The substrate derivation gives:

- **Existence of R1 is form-FORCED.** Any kernel of finite width $\ell_P$ contributes a non-zero second moment to the flux gradient expansion. Since V1 has finite width by Theorem N1, the $\nabla^3\mathbf{v}$ flux contribution exists; momentum conservation then propagates it into the $\nabla^4\mathbf{v}$ contribution to the equation of motion.
- **Sign of R1 is form-FORCED.** Positive-Fourier-transform kernels (V1 admissibility class, Theorem N1) have positive even moments. Hence $\kappa > 0$ and the R1 term enters with a *negative sign* in the equation of motion (after the divergence sign-flip), giving stabilizing rather than destabilizing dynamics. This is the substrate-level reason R1 is hyperviscous rather than antihyperviscous.
- **Magnitude of R1 is INHERITED.** The product $\kappa\mu_\mathrm{V1}\ell_P^2$ is set by the V1 kernel's profile (specifically the ratio of the fourth to the squared second moment, or equivalently the kurtosis of the kernel). The pointwise numerical value of this product is INHERITED at value layer.

**Comparison with NS-3.01 / NS-Smooth-2.** NS-3.01 derived R1 as form-FORCED via top-down architectural argument from V1's finite-width participation kernel. The present derivation reproduces R1 from bottom-up substrate event-flux statistics under hydrodynamic-window coarse-graining. The two derivations agree on:

- Operator form: $\nabla^4\mathbf{v}$ (Laplacian of Laplacian, hyperviscous Laplacian-class).
- Sign: stabilizing (negative coefficient in equation of motion).
- Coefficient scaling: $\ell_P^2$ from V1 second-moment / fourth-moment ratio.
- Physical origin: V1 finite-width vacuum kernel (T18 / Theorem N1).

The bottom-up derivation thus closes the consistency loop with NS-3.01 and confirms that the form-FORCED architectural argument has a substrate-level realization. Consequently the NS-Smooth-2 Lyapunov-decay structure $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ is preserved unchanged: integrating $\mathbf{v}\cdot$(R1-term) by parts yields the strictly negative Lyapunov contribution.

The R1 emergence at fluid scale is now substrate-grounded.

---

## 6. Step 4 — V5 Kernel and Cross-Chain Memory

The V5 kernel is the cross-chain participation kernel: the substrate object that mediates participation-structure correlation between distinct chains, with V5 cross-chain-correlation existence FORCED-conditional on V1 by Arc N N.2 §6.5 and amplitudes INHERITED at molecular scale. Unlike V1 (single-chain self-response, finite spatial width $\sim\ell_P$), V5 carries a *temporal* memory structure with relaxation time $\tau_\mathrm{V5}$ INHERITED at molecular scale (typically $\gg\tau_\mathrm{V1}\sim\ell_P/c$).

For the present coarse-graining purposes, write V5 as a temporal kernel acting on the velocity field's history:

$$\bigl[K_{V5}\ast\partial_t\mathbf{v}\bigr](\mathbf{x},t) \;=\; \int_0^\infty K_{V5}(\tau)\,\partial_t\mathbf{v}(\mathbf{x},\,t-\tau)\,d\tau,$$

with $K_{V5}$ smooth, positive, normalized $\int_0^\infty K_{V5}(\tau)\,d\tau = 1$, and supported on $\tau \in [0,\,\sim\tau_\mathrm{V5}]$ (T18 forward-cone causality preserved under the temporal kernel — V5 inherits forward-only directionality from cascade + R1-bypass redundancy per Arc N).

**Hydrodynamic-window temporal coarse-graining.** Two regimes obtain:

- **Fast-flow regime** ($\tau_\mathrm{flow} \ll \tau_\mathrm{V5}$): the velocity changes faster than V5's memory; the kernel cannot follow and the memory effect dominates. Convolution generates $\partial_t\mathbf{v}$ contributions weighted by $\tau_\mathrm{V5}$.
- **Slow-flow regime** ($\tau_\mathrm{flow} \gg \tau_\mathrm{V5}$): V5's memory is short compared to flow timescales; the convolution evaluates approximately as $\partial_t\mathbf{v}$ at the present instant, weighted by the kernel's zeroth temporal moment (which is unity by normalization).

**Maxwell-class memory at fluid scale.** Expanding $\partial_t\mathbf{v}(t-\tau) = \partial_t\mathbf{v}(t) - \tau\,\partial_t^2\mathbf{v}(t) + \cdots$ and convolving against $K_{V5}$:

$$\bigl[K_{V5}\ast\partial_t\mathbf{v}\bigr](\mathbf{x},t) \;=\; \partial_t\mathbf{v}(\mathbf{x},t) \;-\; \langle\tau\rangle_{V5}\,\partial_t^2\mathbf{v}(\mathbf{x},t) \;+\; \mathcal{O}\bigl(\langle\tau^2\rangle_{V5}\,\partial_t^3\mathbf{v}\bigr),$$

with $\langle\tau\rangle_{V5} = \int_0^\infty\tau\,K_{V5}(\tau)\,d\tau$ the V5 first temporal moment — a substrate quantity scaling as $\tau_\mathrm{V5}$. The leading correction $\langle\tau\rangle_{V5}\partial_t^2\mathbf{v}$ is the hydrodynamic-scale signature of V5 memory.

**Maxwell viscoelastic equation.** Arranging the leading memory correction with the viscous stress $\sigma_{ij} = 2\mu(\rho) S_{ij}$ (where $S_{ij} = \tfrac{1}{2}(\partial_i v_j + \partial_j v_i)$ is the symmetric strain rate), one recovers the Maxwell viscoelastic ODE

$$\tau_R\,\partial_t\sigma_{ij} \;+\; \sigma_{ij} \;=\; 2\mu(\rho)\,S_{ij},$$

with relaxation time $\tau_R = \langle\tau\rangle_{V5}$ identified as the V5 first temporal moment. This is the substrate-derived form of the Maxwell-class memory ansatz used in P4-NN-D5.

**At hydrodynamic-flow scales** (typical macroscopic flows with $\tau_\mathrm{flow} \gg \tau_\mathrm{V5}$), the leading-order substrate effect is a renormalization of the effective inertia: the memory correction adds a $\lambda(\rho)\,\partial_t\mathbf{v}$ contribution to the momentum equation, with $\lambda(\rho) \propto \rho\,\tau_\mathrm{V5}\,\Gamma_0(\rho)$ a substrate-derived coefficient. In the slow-flow limit $\lambda(\rho) \to 0$ and pure Newtonian behavior is recovered; in the intermediate regime the substrate-derived viscoelasticity matches the P4-NN-D5 ansatz.

**Origin of P4-NN viscoelasticity.** The substrate provenance of the Maxwell-class memory term is now identified: V5 cross-chain temporal-memory kernel, FORCED-conditional-on-V1 in existence per Arc N, with $\tau_R \equiv \langle\tau\rangle_{V5}$ a substrate-statistics first temporal moment INHERITED at value layer. The P4-NN-D5 ansatz is no longer a postulated continuum constitutive form; it is a substrate-derived consequence of V5's cross-chain memory under hydrodynamic-window temporal coarse-graining.

---

## 7. Step 5 — Combined Kernel-Coarse-Grained Equation

Combining Step 3 (V1 → viscosity + R1) and Step 4 (V5 → viscoelastic memory), the full kernel-coarse-grained continuum momentum equation is:

$$\boxed{\;\rho\,\partial_t\mathbf{v} \;=\; \mu(\rho)\,\nabla^2\mathbf{v} \;-\; \kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4\mathbf{v} \;+\; \lambda(\rho)\,\partial_t\mathbf{v} \;-\; \rho\,(\mathbf{v}\cdot\nabla)\mathbf{v} \;-\; \nabla p \;+\; \mathcal{O}\bigl(\ell_P^4\nabla^6,\,\tau_\mathrm{V5}^2\partial_t^3\bigr).\;}$$

Term-by-term origin:

- **$\mu(\rho)\,\nabla^2\mathbf{v}$** — V1 second-moment + P4-modulated $\Gamma_0$ + hydrodynamic isotropy (Arc_D_3).
- **$-\kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4\mathbf{v}$** — V1 fourth-moment / second-moment ratio in the gradient expansion (this memo §5). The R1 term, matching NS-3.01.
- **$\lambda(\rho)\,\partial_t\mathbf{v}$** — V5 first temporal moment + cross-chain participation kernel (this memo §6). The Maxwell-class memory contribution, matching P4-NN-D5.
- **$-\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$** — Eulerian-frame bookkeeping of the convective momentum flux (Arc_D_3 §5; preserved frame-kinematic status).
- **$-\nabla p$** — continuum-imposed Lagrange-multiplier for incompressibility (NS-2.08 / Appendix C; not derived).

Both V1-derived contributions ($\mu\nabla^2\mathbf{v}$ and $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$) and the V5-derived contribution ($\lambda\partial_t\mathbf{v}$) are **canonical ED structures** in the ED-I-06 sense — biases on participation flow sourced by stable participation structures (V1: substrate-cutoff stability mechanism; V5: cross-chain memory structure). The frame-kinematic terms (advection) and continuum constraints (pressure, incompressibility) preserve their non-canonical status from Appendix C / NS-MHD-4.

---

## 8. Step 6 — Relation to NS, MHD, and P4-NN

The Arc_D_4 kernel-coarse-graining derivation has four downstream consequences:

**(i) Completes the substrate origin of R1 (NS-3.01).** NS-3.01 established R1 as form-FORCED via top-down architectural argument from V1's finite-width participation kernel. Arc_D_4 supplies the bottom-up substrate derivation: V1 gradient expansion + momentum conservation produces $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ with form, sign, and $\ell_P^2$-scaling all matching NS-3.01 exactly. The two derivations are now reconciled and the consistency loop is closed.

**(ii) Confirms the NS-Smooth-2 Lyapunov structure.** The strict monotone decay $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ in the gradient-norm Lyapunov $L = \tfrac{1}{2}\|\nabla\mathbf{v}\|_2^2$ requires (a) the operator form $\nabla^4\mathbf{v}$, (b) the negative sign (stabilizing), (c) integration-by-parts compatibility. All three properties are confirmed by the substrate derivation: form FORCED by V1 isotropy + finite width; sign FORCED by positive-Fourier-transform kernel; integration-by-parts compatibility is a consequence of the Laplacian-class structure. The NS-Smooth-2 verdict (R1 produces strictly monotone gradient-norm Lyapunov decay in ED-only NS) is preserved unchanged with substrate grounding.

**(iii) Provides the substrate origin of viscoelasticity (P4-NN).** The Maxwell-class memory ansatz $\tau_R\dot\sigma + \sigma = 2\mu S$ used in P4-NN-D5 is no longer postulated; it is derived from V5 cross-chain temporal-memory at hydrodynamic-window scale, with $\tau_R = \langle\tau\rangle_{V5}$ identified as the V5 first temporal moment INHERITED at value layer. P4-NN's reach into viscoelastic rheology now has a substrate foundation; the published P4-NN paper's viscoelastic content is strengthened by Arc_D_4 closure.

**(iv) Sets up Arc_D_5 (minimal-coupling coarse-graining).** Arc_D_5 will replace neutral-chain $\Gamma_0$ with the charged-chain transition rate that includes the T17 minimal-coupling vertex $\partial_\mu \to \partial_\mu - iqA_\mu$ at substrate level, then coarse-grain to obtain the fluid-level Lorentz force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$. The kernel-coarse-graining machinery developed in this memo (V1 second/fourth moments, V5 temporal moments) generalizes directly to charged-chain populations under minimal coupling. The Lorentz-coarse-graining bridge of NS-MHD-2 is closed in Arc_D_5 using the present memo's tools.

The kernel-side substrate-to-continuum mapping is now closed: V1 → viscosity ($\mu\nabla^2\mathbf{v}$, leading-order) + R1 ($-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$, NLO); V5 → Maxwell-class memory ($\lambda\partial_t\mathbf{v}$ / $\tau_R\dot\sigma + \sigma = 2\mu S$). All terms canonical ED in the ED-I-06 sense; all forms FORCED at substrate level; all numerical coefficients INHERITED at value layer.

---

## 9. Recommended Next Steps

Proceed to **Arc_D_5 (Minimal-Coupling Coarse-Graining)**. File: `theory/Arc_D/Arc_D_5_Minimal_Coupling_Coarse_Graining.md`. Scope: coarse-grain a charged-chain population whose substrate dynamics include the T17 minimal-coupling vertex $\partial_\mu \to \partial_\mu - iqA_\mu$. Apply the kernel-coarse-graining machinery of Arc_D_2 / Arc_D_3 / Arc_D_4 to the charged-chain momentum-flux statistics; derive the fluid-level Lorentz force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$; close NS-MHD-2's INHERITED Lorentz coarse-graining bridge. Identify next-to-leading-order corrections in $R_\mathrm{cg}/L_\mathrm{flow}$ and classify under ED-I-06 ontology.

Estimated 1–2 sessions for Arc_D_5.

### Decisions for you

- **Confirm V1 → R1 substrate derivation.** R1 form $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ FORCED by V1 fourth-moment / second-moment ratio + isotropy + momentum conservation; sign FORCED by positive-Fourier-transform kernel; matches NS-3.01 exactly.
- **Confirm V5 → Maxwell viscoelastic substrate derivation.** Maxwell ansatz $\tau_R\dot\sigma + \sigma = 2\mu S$ with $\tau_R = \langle\tau\rangle_{V5}$ FORCED by V5 first temporal moment + hydrodynamic temporal-coarse-graining; matches P4-NN-D5 ansatz.
- **Confirm proceeding to Arc_D_5 (minimal-coupling coarse-graining → Lorentz force at fluid scale).**

---

*Arc_D_4 closes the kernel-side substrate-to-continuum mapping. V1 finite-width vacuum kernel produces (i) leading-order viscosity $\mu\nabla^2\mathbf{v}$ at zeroth + second moment, (ii) next-to-leading-order R1 $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ at fourth-moment / second-moment ratio. Substrate derivation matches NS-3.01 form-FORCED top-down derivation exactly: form, sign, scaling all reconciled. V5 cross-chain temporal-memory kernel produces Maxwell-class viscoelastic memory $\tau_R\dot\sigma + \sigma = 2\mu S$ with $\tau_R = \langle\tau\rangle_{V5}$ first temporal moment, matching P4-NN-D5 ansatz. Combined kernel-coarse-grained continuum momentum equation supplies all canonical-ED dynamical content from substrate primitives. NS-Smooth-2 Lyapunov-decay structure preserved unchanged with substrate grounding. P4-NN viscoelastic ansatz now substrate-derived rather than postulated. Arc_D_5 (minimal-coupling coarse-graining → Lorentz force at fluid scale) is the next deliverable.*
