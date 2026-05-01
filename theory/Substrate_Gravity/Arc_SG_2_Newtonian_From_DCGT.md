# Arc_SG_2 — Newtonian Potential from DCGT-Consistent Coarse-Graining

**Date:** 2026-04-30
**Status:** First technical derivation memo of the Substrate Gravity Extension Arc. Re-derives Newton's gravitational potential $\Phi(r) = -GM/r$ from ED substrate primitives via DCGT scalar-diffusion machinery; confirms consistency with T19's substrate derivation of $G = c^3\ell_P^2/\hbar$. **Result: Newton's $1/r$ potential FORCED by DCGT scalar Laplacian + 3D Green's function; $G$ value INHERITED from T19; DCGT-gravity interface established.**
**Companions:** [`Arc_SG_1_Opening.md`](Arc_SG_1_Opening.md), [`../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md`](../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md), [`../../arcs/arc-SG/`](../../arcs/arc-SG/) (closed substrate-gravity arc memos), [`../../papers/ED_QFT_Overview/ED_QFT_Unified_Overview.md`](../../papers/ED_QFT_Overview/ED_QFT_Unified_Overview.md) §10.

---

## 1. Purpose

This memo:

- **Re-derives Newton's gravitational potential** $\Phi(r) = -GM/r$ from ED substrate primitives via the DCGT scalar-diffusion machinery established in Arc_D_2.
- **Confirms consistency with T19** — the closed-arc derivation of Newton's gravitational constant $G = c^3\ell_P^2/\hbar$ from substrate primitives via the cumulative-strain mechanism + holographic participation-count bound.
- **Identifies which derivation steps are FORCED** at substrate level (operator structure, $1/r$ Green's function, inverse-square imbalance) **vs INHERITED** at value layer (gravitational coupling $G$, mass parameter $M$, participation-flux normalization).
- **Establishes the DCGT-gravity interface** that SG-3 through SG-6 will build on. The flat-background substrate-gravity sector now operates under the same substrate-to-continuum machinery as the NS / MHD / YM sectors.

The memo is structurally parallel to Arc_D_2 (scalar diffusion from substrate event-flux statistics) and Arc_YM_2 (substrate → continuum non-Abelian gauge equation). Same coarse-graining machinery; different sector (substrate gravity); same form-FORCED / value-INHERITED structural verdict.

---

## 2. Inputs

- **T19 (Newton's law from substrate, 2026-04-27).** $G = c^3\ell_P^2/\hbar$ derived from substrate participation-imbalance + cumulative-strain + holographic-bound mechanism. Provides the substrate origin of the gravitational coupling.
- **T20 (transition acceleration, 2026-04-27).** $a_0 = c\,H_0/(2\pi)$ derived from substrate primitives via cosmological-horizon participation-density connection. Required for SG-3 (kernel-profile scaling); not directly used in the Newtonian derivation here.
- **ED Combination Rule (ECR, 2026-04-28).** $a = \sqrt{a_N\,a_0}$ — substrate-level composition rule. Required for SG-4 / SG-5 (consolidated equation + BTFR robustness); not directly used here.
- **T21 (slope-4 BTFR, 2026-04-28).** $v^4 = G\,M\,a_0$ — empirical-anchor result. Required for SG-5; not directly used here.
- **DCGT (Arc D closure 2026-04-30).** Substrate-to-continuum coarse-graining theorem. The scalar-diffusion sub-result (Arc_D_2) is the load-bearing input for the present memo. DCGT supplies the hydrodynamic-window machinery, the multi-scale expansion methodology, the form-FORCED / value-INHERITED structural split, and the sign-FORCED kernel-positivity arguments.
- **ED-I-06 (Fields and Forces in Event Density, Feb 2026).** §4 scalar-field-as-density-gradient ontology. Mass density $\rho_m$ is a scalar-field-class participation density; gravitational potential $\Phi$ is the corresponding scalar-field gradient bias. Provides the ontological reading of the Newtonian potential.
- **Arc_SG_1 (Opening).** Six-memo arc plan; scope item SG-2 (Newtonian potential from DCGT-consistent coarse-graining); load-bearing structural questions Q1 and Q2.

---

## 3. Step 1 — Substrate Participation Imbalance

A localized mass distribution at the origin sources a substrate-level participation imbalance via the cumulative-strain mechanism of T19. Specifically, mass $M$ at position $\mathbf{r}_0$ produces a substrate participation-channel density bias that propagates outward through the chain network, reflecting the holographic participation-count bound that ties mass-energy content to substrate-level commitment density.

**Geometric dilution of chain-flux participation.** The substrate participation imbalance from a point mass propagates radially through 3D space. The participation-flux density at radius $r$ — the rate per unit area at which substrate participation-channel commitments cross outward through a sphere of radius $r$ — dilutes geometrically:

$$\delta\Pi(r) \;\propto\; \frac{1}{r^2}.$$

The proportionality is fixed by the substrate-derivation chain of T19: the mass content $M$ sets the total substrate participation-flux through any enclosing sphere; spherical dilution at radius $r$ produces the $1/r^2$ flux density; the substrate participation-imbalance follows the flux-density structure.

**Status of this step.** The inverse-square structure $\delta\Pi(r) \propto 1/r^2$ is **FORCED** at substrate level by:

- (a) Geometric dilution: any radial flux through $\mathbb{R}^3$ scales as $1/r^2$ by Gauss-class arguments at the substrate-level chain network.
- (b) Substrate participation conservation: the total participation flux through any enclosing sphere is conserved under chain-network propagation (analogous to Gauss's law for mass-flux in standard gravitation).
- (c) Spherical isotropy: substrate isotropy at large scales (relative to $\ell_P$) ensures the radial-dilution form is exact.

The numerical proportionality constant in $\delta\Pi(r) \propto M/r^2$ is INHERITED from substrate normalization conventions; it is set by T19's substrate-derivation of $G$.

This is the substrate origin of the inverse-square law of Newtonian gravitation.

---

## 4. Step 2 — DCGT Scalar Coarse-Graining

Apply DCGT scalar-diffusion machinery (Arc_D_2) to the substrate participation density. The DCGT scalar-sector master equation is

$$\partial_t\rho \;=\; \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr) \;+\; \mathcal{O}(\ell_P^2\,\nabla^4\rho),$$

with $M(\rho)$ the substrate-derived mobility coefficient (per Arc_D_2 §4) and the higher-order corrections suppressed at hydrodynamic scales.

**Static-limit reduction.** Under the gravitational-static-source assumption — a localized mass distribution at fixed position — the time-derivative vanishes and the equation reduces to a balance between the participation-flux divergence and the source term. Including a source term proportional to mass density $\rho_m$ (the localized-mass substrate participation imbalance):

$$0 \;=\; \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr) \;-\; (\text{source} \propto \rho_m).$$

For a uniform far-field background ($\rho \to \rho_*$ as $r \to \infty$, with $M(\rho_*) = M_*$ a constant background mobility), the equation linearizes to

$$0 \;=\; M_*\,\nabla^2\rho \;-\; (\text{source} \propto \rho_m),$$

i.e., a Poisson-class equation for the participation-density perturbation with the substrate-derived mobility setting the proportionality constant.

**Identification with the gravitational potential.** Identify the participation-density perturbation $\rho - \rho_*$ with the gravitational-potential field $\Phi$ via the substrate-to-continuum mapping that ED-I-06 §4 supplies: scalar-field gradients $\nabla\rho$ are the substrate origin of force-from-stability biases; the gravitational potential $\Phi$ is the canonical scalar-field-class continuum object whose gradient produces the gravitational force. Up to a normalization fixed by T19, the identification is

$$\Phi(\mathbf{r}) \;\propto\; \rho_*(\mathbf{r}) - \rho(\mathbf{r}),$$

with the proportionality constant absorbed into the gravitational coupling $G$.

The Poisson-class equation in standard normalization becomes

$$\boxed{\;\nabla^2\Phi(\mathbf{r}) \;=\; 4\pi G\,\rho_m(\mathbf{r}).\;}$$

This is the standard Newtonian Poisson equation, derived from ED substrate primitives via DCGT scalar-diffusion machinery.

**Three structural identifications.**

- **Divergence-of-participation-imbalance** → Laplacian operator. The substrate participation-flux $\nabla\cdot\mathbf{J}_\rho$ becomes $\nabla\cdot(M_*\nabla\rho) = M_*\nabla^2\rho$ at hydrodynamic scales under DCGT, the standard scalar-diffusion divergence-gradient structure.
- **DCGT scalar Laplacian structure** → second-order spatial differential operator. FORCED by DCGT scalar-sector multi-scale expansion (Arc_D_2 §4–§5).
- **$\Phi$ as coarse-grained participation potential** → scalar-field-class continuum object. ED-I-06 §4 reading. The gravitational potential is structurally a participation-density gradient bias on chain propagation.

**Status of this step.**

- The **Laplacian operator structure** $\nabla^2\Phi$ is FORCED by DCGT scalar-diffusion + static-limit reduction. Form-FORCED at substrate level via the same mechanism that produced $\nabla\cdot(M(\rho)\nabla\rho)$ for general scalar-diffusion in Arc_D_2.
- The **coupling constant $G$** is INHERITED from T19. DCGT does not by itself derive $G$; it inherits the value from the substrate-derivation chain of T19 ($G = c^3\ell_P^2/\hbar$).
- The **factor $4\pi$** in the source term is the standard normalization fixed by the conventional definition of $G$ at the level of the gravitational force law $F = GMm/r^2$.

---

## 5. Step 3 — Recovering the Newtonian Potential

For a point mass $M$ at the origin, the mass-density distribution is $\rho_m(\mathbf{r}) = M\,\delta^{(3)}(\mathbf{r})$. Substituting into the substrate-derived Poisson equation:

$$\nabla^2\Phi \;=\; 4\pi G\,M\,\delta^{(3)}(\mathbf{r}).$$

The Green's function of the Laplacian in 3D is $G(\mathbf{r}) = -1/(4\pi r)$ — the standard mathematical result: $\nabla^2(1/r) = -4\pi\,\delta^{(3)}(\mathbf{r})$.

Convolving the source against the Green's function,

$$\Phi(\mathbf{r}) \;=\; \int d^3\mathbf{r}'\;G(\mathbf{r}-\mathbf{r}')\,(4\pi G M)\,\delta^{(3)}(\mathbf{r}') \;=\; -\frac{GM}{|\mathbf{r}|},$$

i.e.,

$$\boxed{\;\Phi(r) \;=\; -\frac{GM}{r}.\;}$$

This is the standard Newtonian gravitational potential, recovered from ED substrate primitives via DCGT scalar-diffusion machinery + 3D Green's-function inversion.

**Status of this step.**

- The **$1/r$ functional form** is FORCED by the Green's function structure of the Laplacian in $D = 3$ spatial dimensions. The substrate-derivation depends on the spatial dimensionality being $D = 3$, which is itself FORCED at substrate level by the NS-1 Path B-strong dimensional-forcing argument (T20 mechanism degeneracy at $d \le 2$ + Polya recurrence at $d = 3$ + T19/T20 empirical-consistency at $d = 3$).
- The **coefficient $GM$** is INHERITED from substrate normalization. $G$ is INHERITED from T19; $M$ is INHERITED at the level of mass-content specification (the mass parameter is empirical-input, not predicted by substrate physics).
- **Newton's force law** $\mathbf{F} = -\nabla\Phi = -GM/r^2\,\hat r$ follows by gradient + standard normalization.

The ED substrate-derivation reproduces Newton's law of gravitation cleanly: form FORCED by DCGT + 3D Green's function; values INHERITED from T19 + mass-content specification.

---

## 6. Step 4 — Consistency with T19

T19 derives the gravitational constant from substrate primitives:

$$G \;=\; \frac{c^3\,\ell_P^2}{\hbar}.$$

This identification has three structural anchors:

- **$\ell_P$** — substrate length scale (V1 kernel width per Theorem N1).
- **$c$** — substrate-level light-speed scale (light-cone causal-structure scale via T18 forward-cone support).
- **$\hbar$** — substrate-level participation-quantum scale (Arc Q.7 canonical-commutation scale).

T19's derivation routes through (a) substrate participation-imbalance produced by mass-content $M$, (b) cumulative-strain mechanism reading the holographic participation-count bound, and (c) dimensional-analysis closure fixing the $\ell_P$, $c$, $\hbar$ combination. The result is the substrate-level value of $G$.

**Consistency check with DCGT scaling.** DCGT's scalar-diffusion machinery produces the Laplacian operator structure with mobility coefficient $M_*$ that has dimensions of [length²/time]. For the gravitational-potential identification, the dimensional consistency works out as follows:

- $[\Phi] = [\text{velocity}^2]$ (gravitational potential has units of energy per unit mass, equivalently $\text{velocity}^2$).
- $[\rho_m] = [\text{mass}/\text{length}^3]$.
- $[G] = [\text{length}^3 / (\text{mass}\cdot\text{time}^2)]$.
- The combination $G\rho_m$ has units of $1/\text{time}^2$, which matches $\nabla^2\Phi$'s units of $\text{velocity}^2/\text{length}^2 = 1/\text{time}^2$.

Substituting T19's $G = c^3\ell_P^2/\hbar$:

$$[G] \;=\; \frac{[c]^3\,[\ell_P]^2}{[\hbar]} \;=\; \frac{(\text{length}/\text{time})^3\,\text{length}^2}{\text{mass}\cdot\text{length}^2/\text{time}} \;=\; \frac{\text{length}^3}{\text{mass}\cdot\text{time}^2} \;\checkmark$$

Dimensionally consistent. T19's substrate-derivation of $G$ is consistent with DCGT scaling.

**V1 kernel width and participation-flux normalization.** The substrate length scale $\ell_P$ enters T19 as the V1 kernel's spatial width (Theorem N1). DCGT's scalar-diffusion uses the same $\ell_P$ as the substrate-discreteness scale below which gradient-expansion truncation breaks down (Arc_D_2 §3, hydrodynamic-window lower bound $R_\mathrm{cg} \gg \ell_P$). The two scales are the same; T19 and DCGT inherit the same substrate length-scale.

**Status of this step.** DCGT does *not* modify the value of $G$ — it inherits the value from T19 and supplies the continuum operator structure ($\nabla^2\Phi$ Laplacian) that T19 alone did not derive. T19 establishes the substrate origin of $G$; DCGT establishes the substrate origin of the Poisson equation that uses $G$. The two results are complementary structural derivations at different layers of the substrate-to-continuum pipeline: T19 is at the value-layer for the coupling; DCGT is at the operator-structure layer for the field equation.

The Newtonian gravitational sector of ED is now substrate-grounded end-to-end: T19 supplies the coupling; DCGT supplies the equation; together they reproduce Newton's gravitational potential as a substrate-derived continuum result.

---

## 7. Step 5 — FORCED vs INHERITED Classification

Following the program's standard form-FORCED / value-INHERITED methodology, classify each derivation step:

**FORCED at substrate level:**

- **Inverse-square participation imbalance** $\delta\Pi(r) \propto 1/r^2$ (Step 1). FORCED by geometric dilution of chain-flux through 3D space + substrate participation conservation + spherical isotropy.
- **Laplacian operator structure** $\nabla^2\Phi$ (Step 2). FORCED by DCGT scalar-diffusion + static-limit reduction + ED-I-06 §4 scalar-field identification.
- **Poisson-equation form** $\nabla^2\Phi = 4\pi G\rho_m$ (Step 2). FORCED by DCGT mobility-channel structure + standard $G$-normalization convention.
- **$1/r$ Green's function** $\Phi(r) = -GM/r$ (Step 3). FORCED by 3D Green's-function structure of the Laplacian operator. Spatial dimensionality $D = 3$ is itself FORCED at substrate level by NS-1 Path B-strong dimensional forcing.
- **Newton's force law** $\mathbf{F} = -GMm\hat r/r^2$ (Step 3). FORCED by gradient + standard normalization.

**INHERITED at value layer:**

- **Value of $G$**: $G = c^3\ell_P^2/\hbar$ from T19. ED's structural derivation does not predict the numerical value of $G$ at value layer; the value comes from the substrate-level cumulative-strain + holographic-bound mechanism, with $\ell_P$ + $c$ + $\hbar$ as substrate inputs.
- **Normalization of participation flux**: the proportionality constant in $\delta\Pi(r) \propto M/r^2$ is set by T19's value-layer; not derived independently here.
- **Mass parameter $M$**: empirical-input quantity. ED does not predict the mass content of any specific gravitational source; mass-content is a value-layer specification.

The classification preserves the program's standard methodology: the *form* of Newton's gravitational potential ($1/r$, Laplacian operator, Poisson equation, gradient force law) is FORCED; the *values* (gravitational coupling, mass-content) are INHERITED. This matches the form-FORCED / value-INHERITED pattern across NS / MHD (mobility coefficient $\mu(\rho)$ form-FORCED, value-INHERITED), YM (gauge coupling $g$, mass-gap value INHERITED), and the closed substrate-gravity arc (T19 + T20 + ECR + T21 produced FORCED forms with INHERITED values).

---

## 8. Step 6 — Consequences for SG-3 through SG-6

The Arc_SG_2 Newtonian re-derivation has four downstream consequences for the remaining sub-arcs:

**(i) SG-3 (transition acceleration scaling).** SG-3 will analyze how the transition acceleration $a_0 = c\,H_0/(2\pi)$ scales with $\ell_P$ and the V1 kernel profile under the continuum limit. Working a-priori for SG-3: unlike YM mass gap (which scales as $\ell_P^{-2}$ at substrate level requiring kernel-profile rescaling to survive), $a_0$ involves cosmological-horizon scales, so the kernel-profile dependence may be qualitatively different. The DCGT-gravity interface established here provides the methodology.

**(ii) SG-4 (substrate-gravity field equation in flat background).** The Poisson-equation derivation here is the *Newtonian* component of the consolidated substrate-gravity field equation that SG-4 will produce. SG-4 will extend the present derivation by adding (a) the transition-regime $a_0$ corrections that produce MOND-class behavior in the appropriate limit, and (b) the cross-term ECR composition $a = \sqrt{a_N\,a_0}$ that interpolates between Newtonian and MOND regimes. The consolidated equation will recover Newton at $a \gg a_0$ and MOND-class behavior at $a \ll a_0$.

**(iii) SG-5 (BTFR slope-4 robustness).** SG-5 will audit the slope-4 result $v^4 = G\,M\,a_0$ for robustness under variations of the V1 kernel profile, the mobility modulation $\Gamma_0(\rho)$, and the substrate-discreteness assumptions. The Newtonian re-derivation here establishes that the $G$-content of slope-4 is structurally robust (Newton's $G$ is FORCED at substrate level via T19); the $a_0$-content's robustness is the SG-3 question; the slope-4 power itself follows from the dimensional combination $G\,M\,a_0$ via the geometric-mean ECR composition.

**(iv) SG-6 (synthesis + ED-10 implications).** SG-6 will aggregate the five sub-arc results and identify the structural prerequisites for ED-10. The Newtonian re-derivation here establishes one prerequisite: ED-10's curvature-emergence arc must, in its weak-field / flat-background limit, recover the Poisson equation derived here. This gives ED-10 a clean checkable structural target.

---

## 9. Recommended Next Step

Proceed to **Arc_SG_3 (Transition Acceleration $a_0$ Under Kernel-Profile Scaling)**. File: `theory/Substrate_Gravity/Arc_SG_3_Transition_Acceleration_Scaling.md`. Scope: analyze how $a_0 = c\,H_0/(2\pi)$ behaves under the continuum limit $\ell_P \to 0$ + V1 kernel profile variation. Working a-priori: $a_0$ involves cosmological-horizon scales, so kernel-profile dependence may be qualitatively different from YM mass-gap scaling. Identify the load-bearing structural conditions for $a_0$ stability under the continuum limit.

Estimated 1 session for Arc_SG_3.

### Decisions for you

- **Confirm Newtonian re-derivation.** Newton's potential $\Phi(r) = -GM/r$ derived from ED substrate primitives via DCGT scalar-diffusion machinery; consistent with T19's $G = c^3\ell_P^2/\hbar$.
- **Confirm FORCED vs INHERITED classification.** Form (Laplacian, Poisson, $1/r$ Green's function, force law) FORCED at substrate level; values ($G$, $M$, normalization) INHERITED.
- **Confirm proceeding to Arc_SG_3 ($a_0$ kernel-profile scaling) as the next deliverable.**

---

*Arc_SG_2 closes the Newtonian re-derivation under DCGT. Substrate participation imbalance $\delta\Pi(r) \propto 1/r^2$ FORCED by 3D geometric dilution + substrate participation conservation + spherical isotropy. DCGT scalar-diffusion machinery + static-limit reduction + ED-I-06 §4 scalar-field identification produces Poisson equation $\nabla^2\Phi = 4\pi G\rho_m$ with Laplacian operator structure FORCED at substrate level. 3D Green's function inversion gives Newton's potential $\Phi(r) = -GM/r$ — $1/r$ form FORCED by Laplacian Green's-function structure + NS-1 Path B-strong $D = 3$ forcing; coefficient $GM$ INHERITED from T19's $G = c^3\ell_P^2/\hbar$ + mass-content specification. T19 supplies the coupling value; DCGT supplies the equation operator structure; together they reproduce Newton's gravitational potential as a substrate-derived continuum result. FORCED-vs-INHERITED classification preserves program-standard methodology: form FORCED, values INHERITED. DCGT-gravity interface established for SG-3 ($a_0$ scaling), SG-4 (consolidated equation), SG-5 (BTFR robustness), SG-6 (synthesis). Arc_SG_3 (transition acceleration kernel-profile scaling) is the next deliverable.*
