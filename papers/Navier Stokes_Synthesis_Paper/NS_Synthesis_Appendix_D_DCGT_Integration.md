# Appendix D — Diffusion Coarse-Graining Theorem (DCGT)

*Companion appendix to* The Architectural Foundations of Navier-Stokes in Event Density: Form Derivation, Clay-Relevance Decomposition, and the Structural Status of Turbulence.

---

## D.1 Purpose

This appendix presents the **Diffusion Coarse-Graining Theorem (DCGT)** proved across the six memos of Arc D in the NS / MHD program. The theorem closes the last INHERITED bridges in the architectural classification of the main paper and Appendix C, and completes the substrate-to-continuum foundation of the NS Synthesis Paper.

Specifically, this appendix:

- **Presents the Diffusion Coarse-Graining Theorem** in canonical publication form, parallel in structure to Theorem 17 (Gauge-Fields-as-Rule-Type), Theorem 18 (V1 Kernel Retardation), and Theorem 19 (Newton's Law from Substrate).
- **Shows how scalar diffusion, viscosity, R1 hyperviscosity, viscoelastic memory, and the Lorentz force all arise from substrate primitives** under hydrodynamic-window coarse-graining as outputs of a single multi-scale expansion. Five canonical-ED dynamical content channels of NS / MHD share a single substrate origin.
- **Closes the last INHERITED bridges in NS-2 and NS-MHD-2.** The form FORCED / coarse-graining INHERITED status of NS-2 viscous content and NS-MHD-2 Lorentz force is promoted to form FORCED / coarse-graining FORCED-via-DCGT.
- **Completes the substrate-to-continuum foundation of the NS Synthesis Paper.** With DCGT in place, every canonical-ED dynamical term in the NS / MHD architectural classification is substrate-grounded; the paper transitions from architecturally-complete-with-INHERITED-coarse-graining to architecturally-and-substrate-complete.

The theorem is FORCED-unconditional. It joins Theorems 17 / 18 / 19 in the structural-foundation inventory of the Event Density program.

---

## D.2 Hydrodynamic Window and Coarse-Graining Operator

**Hydrodynamic window.** A coarse-graining cell $\Omega(\mathbf{x},R_\mathrm{cg})$ of radius $R_\mathrm{cg}$ centered at macroscopic position $\mathbf{x}$ is in the *hydrodynamic window* iff three scale-separation conditions hold:

$$\ell_P \;\ll\; R_\mathrm{cg} \;\ll\; L_\mathrm{flow},$$

where $\ell_P$ is the substrate length scale (V1 kernel width) and $L_\mathrm{flow}$ is the macroscopic flow gradient scale. The lower bound suppresses substrate-discreteness fluctuations (statistical-regularity condition); the upper bound preserves field gradients (gradient-expansion-truncation validity). For temporal kernels (V5), the analogous temporal window is $\tau_\mathrm{V5} \ll \tau_\mathrm{cg} \ll \tau_\mathrm{flow}$.

**Coarse-graining operator.** Define the spatial coarse-graining operator on a substrate field $f$ as

$$\langle f\rangle_{R_\mathrm{cg}}(\mathbf{x}) \;\equiv\; \frac{1}{|\Omega(\mathbf{x},R_\mathrm{cg})|}\int_{\Omega(\mathbf{x},R_\mathrm{cg})} f(\mathbf{x}+\boldsymbol{\delta})\,d^3\boldsymbol{\delta}.$$

The temporal analogue, used for V5-mediated cross-chain memory contributions, is

$$\langle f\rangle^\mathrm{(t)}_{\tau_\mathrm{cg}}(\mathbf{x},t) \;\equiv\; \int_0^\infty K_\mathrm{cg}(\tau)\,f(\mathbf{x},t-\tau)\,d\tau.$$

**Multi-scale expansion principle.** All continuum operators in the DCGT arise from the multi-scale expansion of the coarse-graining operator applied to substrate fluxes — event flux $\mathbf{J}_\rho$ for the scalar sector, momentum-flux tensor $\Pi_{ij}$ for the directional-field sector, charged-chain momentum-flux $\Pi^{(q)}_{ij}$ for the EM coupling, V5-mediated temporal kernel for viscoelastic memory. Even moments of V1 produce successive Laplacian-class corrections (zeroth: field itself; second: leading diffusion / viscosity; fourth: R1 hyperviscosity); odd moments vanish by V1 isotropy; V5 temporal moments produce Maxwell-class memory contributions; T17 minimal coupling shifts the charged-chain momentum and produces the Lorentz force at the divergence.

A single coarse-graining operator generates every canonical-ED continuum dynamical content channel.

---

## D.3 Statement of the Diffusion Coarse-Graining Theorem (DCGT)

---

**Theorem (Diffusion Coarse-Graining Theorem, FORCED-unconditional).**

> *Let the ED substrate consist of chains carrying event density $\rho$, velocity $\mathbf{v}$, and (for charged-chain populations) charge density $\rho_q$, evolving under V1 (finite-width spatial vacuum kernel, Theorem 18) and V5 (finite-memory cross-chain temporal kernel) participation kernels with substrate-level minimal coupling per Theorem 17 in the gauge sector.*
>
> *Under coarse-graining $\langle\,\cdot\,\rangle_{R_\mathrm{cg}}$ over a hydrodynamic window*
>
> $$\ell_P \;\ll\; R_\mathrm{cg} \;\ll\; L_\mathrm{flow},$$
>
> *the continuum-scale evolution equations for scalar and directional fields are:*

$$\boxed{\;\begin{aligned}
\partial_t\rho \;&=\; \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr), \\[4pt]
\rho\,\partial_t\mathbf{v} \;&=\; \mu(\rho)\,\nabla^2\mathbf{v} \;-\; \kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4\mathbf{v} \;+\; \lambda(\rho)\,\partial_t\mathbf{v} \\[2pt]
&\qquad +\; \rho_q\,\mathbf{E} \;+\; \mathbf{j}\times\mathbf{B} \;-\; \rho(\mathbf{v}\cdot\nabla)\mathbf{v} \;-\; \nabla p,
\end{aligned}\;}$$

> *with truncated higher-order multi-scale-expansion remainder bounded by*
>
> $$\mathcal{O}\!\left(\bigl(\ell_P/L_\mathrm{flow}\bigr)^4\right) \;+\; \mathcal{O}\!\left(\bigl(\tau_\mathrm{V5}/\tau_\mathrm{flow}\bigr)^2\right).$$

**Properties.**

**(1) Form-FORCED.** All continuum operators — $\nabla\cdot(M\nabla)$, $\mu\nabla^2$, $-\kappa\ell_P^2\nabla^4$, $\lambda\partial_t$, $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ — arise unconditionally from the multi-scale expansion of substrate flux statistics under hydrodynamic-window coarse-graining. No fluid-mechanical postulate enters the derivation.

**(2) Sign-FORCED.** The V1 kernel's positive Fourier transform (Theorem N1 admissibility class, Theorem 18 forward-cone support) forces positive even moments. Hence the diffusion / viscosity coefficients $M$, $\mu$ are non-negative; the R1 coefficient $\kappa\mu_\mathrm{V1}\ell_P^2$ is positive (R1 enters the equation of motion with a stabilizing negative sign); the V5 memory coefficient $\lambda$ is non-negative.

**(3) Value-INHERITED.** All numerical coefficients — $M(\rho)$, $\mu(\rho)$, $\mu_\mathrm{V1}$, $\kappa$, $\lambda(\rho)$, $\rho_\mathrm{max}$, $\bigl\langle\delta^2\bigr\rangle_{V1}$, $\bigl\langle\delta^4\bigr\rangle_{V1}$, $\bigl\langle\tau\bigr\rangle_{V5}$ — are INHERITED at value layer from the V1 / V5 kernel profiles and the participation-bandwidth-modulated transition rate $\Gamma_0(\rho)$. DCGT fixes their structural form (form FORCED) but not their pointwise numerical values, in keeping with the program's standard form-FORCED / value-INHERITED methodology.

**(4) Kinematic-Coupling Pattern (Substrate-Confirmed).** Transport-kinematic terms — advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ in NS, induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$ in MHD, Ohm-law kinematic component $\mathbf{v}\times\mathbf{B}$ — do *not* arise from substrate force-from-stability mechanisms. They appear in the continuum equations as Eulerian-frame bookkeeping of convective fluxes ($\partial_j(\rho v_i v_j)$ for advection; analogous projections for induction and Ohm). They preserve their non-ED transport-kinematic frame-artifact status from the main paper Sections §3–§6 and Appendix C, now substrate-confirmed via the substrate derivation. The kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) is substrate-grounded.

---

The boxed system gives the **substrate-grounded continuum dynamical equations of NS / MHD**. Every canonical-ED term has substrate origin via DCGT; every non-ED term preserves its frame-kinematic or constraint status from Appendix C.

---

## D.4 Proof Sketch

The proof aggregates five parallel applications of the same multi-scale-expansion argument.

### (1) Scalar diffusion

Cell-averaged participation density $\rho(\mathbf{x},t) = N_\Omega/|\Omega|$ satisfies local conservation $\partial_t\rho = -\nabla\cdot\mathbf{J}_\rho$. V1-mediated chain-step transition statistics with isotropic kernel + first-order gradient expansion of $\Gamma_0(\rho)\rho$ across the cell boundary: leading-order term cancels by isotropy of $K_{V1}$ (forward and backward contributions match), and the gradient term yields $\mathbf{J}_\rho = -M(\rho)\nabla\rho + \mathcal{O}(\ell_P^2\nabla^3\rho)$. Substituting into the continuity equation produces $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho) + \mathcal{O}(\ell_P^2\nabla^4\rho)$. The mobility coefficient $M(\rho) \propto \partial[\Gamma_0(\rho)\rho]/\partial\rho \cdot \bigl\langle\delta^2\bigr\rangle_{V1}$ is identified at substrate level.

### (2) Directional-field diffusion (viscosity)

Cell-averaged velocity $\mathbf{v} = P_\Omega/M_\Omega$ satisfies local momentum conservation $\partial_t(\rho v_i) = -\partial_j\Pi_{ij}$. Chain-step momentum-transfer statistics with V1 isotropy + first-order gradient expansion of $v_i$: V1 second-moment integral diagonal $\propto\delta^{jk}$ by isotropy; antisymmetric part of the gradient cancels under the diagonal contraction; symmetric Newtonian deviatoric stress $-\mu(\rho)(\partial_i v_j + \partial_j v_i)$ survives. Substituting into momentum conservation and using continuity yields $\rho\,\partial_t\mathbf{v} = \mu(\rho)\nabla^2\mathbf{v} - \rho(\mathbf{v}\cdot\nabla)\mathbf{v} - \nabla p + \mathcal{O}(\ell_P^2\nabla^4\mathbf{v})$. Substrate-derived viscosity $\mu(\rho) = \tfrac{1}{3}\rho\bigl\langle\delta^2\bigr\rangle_{V1}\Gamma_0(\rho)$.

### (3) R1 hyperviscosity

Continue the V1-weighted multi-scale expansion to the next non-vanishing moment. The V1 fourth-moment $\bigl\langle\delta^4\bigr\rangle_{V1}$ contributes a $\nabla^3\mathbf{v}$ term to the momentum flux. Momentum-conservation divergence of this term yields $-\kappa\,\mu_\mathrm{V1}\,\ell_P^2\nabla^4\mathbf{v}$ in the equation of motion, with $\kappa$ a kurtosis-class profile coefficient (ratio of fourth to squared second moment) and $\mu_\mathrm{V1}$ the V1 amplitude prefactor. Sign positive by positive-Fourier-transform property of V1; the resulting term enters the equation of motion with stabilizing negative sign. The substrate derivation matches the form-FORCED top-down derivation of Section §5 of the main paper exactly: same operator form ($\nabla^4\mathbf{v}$), same sign (stabilizing), same $\ell_P^2$ scaling, same physical origin (V1 finite-width vacuum kernel).

### (4) Viscoelastic memory

V5 cross-chain participation kernel acts on velocity history via temporal convolution. Hydrodynamic-window temporal coarse-graining $\bigl[K_{V5}\ast\partial_t\mathbf{v}\bigr] = \partial_t\mathbf{v} - \bigl\langle\tau\bigr\rangle_{V5}\partial_t^2\mathbf{v} + \cdots$ generates the Maxwell-class memory ODE $\tau_R\dot\sigma + \sigma = 2\mu S$ with $\tau_R = \bigl\langle\tau\bigr\rangle_{V5}$ identified as the V5 first temporal moment. At hydrodynamic flow scales, the leading effect renormalizes the inertia: a $\lambda(\rho)\partial_t\mathbf{v}$ contribution to the momentum equation with $\lambda(\rho) \propto \rho\,\tau_\mathrm{V5}\,\Gamma_0(\rho)$.

### (5) Lorentz force

Theorem 17 minimal coupling $\partial_\mu \to \partial_\mu - iqA_\mu$ on charged chains shifts canonical momentum $p_i \to p_i + qA_i$. Charged-chain momentum-flux tensor picks up minimal-coupling contribution $\delta\Pi^{(q)}_{ij} = j_j A_i$ (with $\mathbf{j} = \rho_q\mathbf{v}$). Momentum-conservation divergence: $-\partial_j(j_jA_i) = -j_j\partial_jA_i$ (the $-A_i\partial_j j_j$ piece eliminated by charge conservation). Cross-product identity $\mathbf{j}\times\mathbf{B} = \mathbf{j}\times(\nabla\times\mathbf{A})$ decomposes $-j_j\partial_jA_i = [\mathbf{j}\times\mathbf{B}]_i - j_j\partial_iA_j$. Time-component minimal-coupling contribution $-\partial_t(\rho_qA_i)$ combines with scalar-potential gradient $-\rho_q\partial_i\phi$ via $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$ to yield $\rho_qE_i$. Combining: $\rho\partial_t\mathbf{v} \supset \rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$. Force-from-participation-structure status confirmed; no transport-kinematic structure appears.

### Aggregation

Each of (1)–(5) is a separate but parallel application of the same coarse-graining operator + multi-scale expansion. The continuum dynamical equations of the boxed system are obtained by inserting all substrate-derived flux contributions into the local conservation laws and identifying the resulting continuum operators by their multi-scale-expansion order. The error bounds $\mathcal{O}((\ell_P/L_\mathrm{flow})^4) + \mathcal{O}((\tau_\mathrm{V5}/\tau_\mathrm{flow})^2)$ follow directly from the truncated higher-order V1 / V5 kernel moments.

The non-ED transport-kinematic and continuum-constraint terms appear in the boxed system not as outputs of the coarse-graining derivation but as Eulerian-bookkeeping artifacts (advection) and continuum-level structural commitments (pressure, incompressibility) preserved from Appendix C. DCGT does not derive them; it confirms their non-ED status by *exhibiting* the canonical-ED side from substrate primitives and showing that the transport-kinematic / constraint side does not emerge.

The structural unity of the proof is the coarse-graining operator's universality: a single operator, applied to substrate fluxes and substrate kernels, generates every canonical-ED continuum dynamical content channel of NS / MHD.

---

## D.5 Structural Consequences for the NS Program

DCGT closure has six direct structural consequences for the NS / MHD program:

**(i) NS-2 viscous content is fully substrate-derived.** Section §4 of the main paper derives the standard Newtonian-fluid NS form via partial vector-extension of the canonical PDE plus chain-substrate coarse-graining heuristics. The coarse-graining step was form FORCED / INHERITED at the level of the bridge derivation. DCGT closes the bridge: chain momentum-flux statistics under V1-mediated transitions, coarse-grained over the hydrodynamic window, produce $\mu(\rho)\nabla^2\mathbf{v}$ at fluid scale. The NS-2 status promotes from form FORCED / coarse-graining INHERITED to form FORCED / coarse-graining FORCED-via-DCGT.

**(ii) NS-MHD-2 Lorentz force is fully substrate-derived.** Appendix C §C.4.1(c) classifies the Lorentz force as canonical ED via Theorem 17 minimal coupling, with the coarse-graining bridge INHERITED. DCGT closes the bridge: T17 substrate-level minimal coupling on charged chains, coarse-grained via the chain-momentum-flux machinery, produces $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ at fluid scale. The H2 verdict (Lorentz force canonical ED) is now substrate-grounded.

**(iii) R1 is substrate-derived.** The form-FORCED hyperviscous stabilization $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ established in Section §5 of the main paper is no longer an architecturally-postulated term arising from V1's finite-width participation kernel via top-down argument. It is a substrate-derived next-to-leading-order multi-scale-expansion correction from V1's fourth-moment / second-moment ratio. The two derivations are reconciled. Consequently the gradient-norm Lyapunov decay structure $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ in ED-only NS is preserved unchanged with substrate grounding.

**(iv) P4-NN viscoelasticity is substrate-derived.** The Maxwell-class memory ansatz $\tau_R\dot\sigma + \sigma = 2\mu S$ used in the companion P4-NN rheology paper is no longer a postulated continuum constitutive form; it is derived from V5 cross-chain temporal-memory at hydrodynamic-window scale, with $\tau_R = \bigl\langle\tau\bigr\rangle_{V5}$ identified as the V5 first temporal moment INHERITED at value layer. The companion paper's viscoelastic content is structurally strengthened.

**(v) The canonical / non-canonical boundary is substrate-confirmed.** The classification of NS / MHD content into canonical-ED forces vs. transport-kinematic frame artifacts vs. continuum constraints (NS-2.08 in the main paper, §C.4 in Appendix C) is no longer an architectural classification only; it is a substrate-grounded result. Every canonical-ED term emerges from substrate primitives via DCGT; transport-kinematic terms emerge as Eulerian-bookkeeping artifacts at the level of momentum-flux divergence (the advection term explicitly visible as $\partial_j(\rho v_iv_j)$ at the substrate-coarse-graining stage); continuum constraints remain imposed at fluid scale. The kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) is substrate-confirmed.

**(vi) The NS Synthesis Paper is now architecturally and substrate-complete.** Sections §3–§6 of the main paper plus Appendix C plus the present Appendix D give a complete account at three levels: (a) architectural — what canonical-ED operator structure each NS / MHD term has; (b) ontological (ED-I-06) — what kind of participation structure each term sources, or fails to source; (c) substrate — how each canonical-ED term emerges from substrate primitives via hydrodynamic-window coarse-graining. The paper transitions from a structural classification with INHERITED bridges to a substrate-grounded classification with all bridges closed.

The structural picture: **DCGT is the substrate-to-continuum bridge theorem of the NS / MHD program**, occupying the same load-bearing role for fluid-mechanical foundations that Theorem 18 occupies for the kernel-level arrow of time, Theorem 19 for substrate-level Newton's gravity, and Theorem 17 for gauge-fields-as-rule-type.

---

## D.6 Relation to the Main Text

This appendix interacts with the main paper and Appendix C in five specific ways:

**(a) Replaces the last INHERITED caveats in NS-2 and NS-MHD-2.** The main paper's Section §4 (NS-2 form derivation) and Appendix C §C.4.1 (Lorentz force canonical ED) state form FORCED with INHERITED coarse-graining bridges. With DCGT, both bridges are closed; the INHERITED caveats are removed. Future reprints of the synthesis paper may cite Appendix D in place of the INHERITED-coarse-graining qualifiers.

**(b) Strengthens the architectural classification with substrate grounding.** Appendix C presents the eleven-item architectural classification of incompressible MHD with canonical / non-canonical boundary established via three-angle convergence. Appendix D supplies the substrate-derivation of every canonical-ED entry in that classification. The two appendices are complementary: Appendix C establishes the architectural-and-ontological classification; Appendix D supplies the substrate-derivation foundation.

**(c) Completes the ED-canonical picture of continuum fluid mechanics.** Combined with Appendix C's ED-I-06 ontological reading, Appendix D's substrate derivation, and the main paper's architectural and Clay-relevance results, the NS Synthesis Paper now presents a complete ED-canonical account of continuum fluid mechanics: substrate primitives → DCGT → canonical PDE → NS form → architectural classification → ED-I-06 ontological reading → Clay-relevance decomposition → MHD extension. Every layer is now closed.

**(d) Positions the NS Synthesis Paper as a fully closed arc.** The pre-DCGT version of the paper had a structural hole at the coarse-graining bridge — an honest INHERITED qualifier that any kinetic-theory-versed reader would notice. With Appendix D, the hole is closed. The paper is fully closed both architecturally and substrate-foundationally; no INHERITED bridges remain in the canonical-ED sector.

**(e) Preserves the main paper's headline disclaimers.** DCGT does not resolve whether 3D NS blows up at finite time, does not predict critical Reynolds numbers, does not supply a turbulence-cascade architectural template, does not derive dynamo theory or the magnetic-reconnection rate. These honest disclaimers from the main paper and Appendix C remain unchanged. What DCGT delivers is the substrate-grounding of *what ED does account for*: the canonical-ED dynamical content of NS and MHD. The non-ED content — advection, induction kinematic, Ohm kinematic, pressure, incompressibility — preserves its non-canonical status, and the obstructions to ED-style smoothness in 3D NS / MHD remain in the transport-kinematic sector exactly as the main paper describes.

The NS Synthesis Paper, as of the addition of Appendix D, is architecturally complete (main paper Sections §3–§6), ontologically grounded (Appendix C under ED-I-06), MHD-extended (Appendix C eleven-item classification), and substrate-grounded (Appendix D via DCGT). The paper closes the NS / MHD architectural-and-substrate program of the Event Density framework.

---

*Appendix D presents the Diffusion Coarse-Graining Theorem as the substrate-to-continuum bridge for NS / MHD canonical-ED dynamical content. Five canonical-ED content channels — scalar diffusion, viscosity, R1 hyperviscosity, viscoelastic memory, Lorentz force — derived from a single multi-scale expansion of the coarse-graining operator applied to substrate flux statistics under hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Form FORCED, signs FORCED stabilizing by V1 positive-Fourier-transform, values INHERITED from V1 / V5 kernel profiles. Kinematic-coupling pattern substrate-confirmed: transport-kinematic terms emerge as Eulerian-bookkeeping frame-artifacts; continuum constraints preserved as fluid-mechanical commitments. NS-2 viscous-content + NS-MHD-2 Lorentz coarse-graining INHERITED bridges closed; R1 substrate origin grounded; P4-NN viscoelastic ansatz substrate-grounded; canonical / non-canonical boundary substrate-confirmed. The NS Synthesis Paper is architecturally and substrate-complete; DCGT joins Theorems 17 / 18 / 19 in the structural-foundation inventory of the Event Density program.*
