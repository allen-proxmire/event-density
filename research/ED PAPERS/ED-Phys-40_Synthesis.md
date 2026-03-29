# ED-Phys-40: Architectural Synthesis of Event Density

## Canonical Sources

| Source | Content Synthesised |
|--------|-------------------|
| ED-Phys-01 (Update Rule) | Canonical PDE, constitutive functions, operator structure |
| ED-Phys-05 (Axioms) | Foundational axioms, system triple |
| ED-Phys-12.5 (Compositional Rule) | Local-global coupling, compositional structure |
| ED-Phys-35 (2D/3D Extension) | Empirical atlas, dimensional laws, morphological taxonomy |
| ED-Phys-36 (Analytical Grounding) | Partial derivations, nondimensionalisation, nine laws |
| ED-Phys-37 (Geometric Analogues) | Structural parallels to MCF, Ricci, PME |
| ED-Phys-38 (Cross-Framework Comparison) | Distance metrics, proximity hierarchy, uniqueness catalogue |
| ED-Phys-39 (Higher-Dimensional Extension) | 4D laws, 4D morphology, asymptotic analysis |

---

# 0. Purpose and Scope

This chapter is the culmination of the ED-Phys series. It consolidates forty chapters of development — from the initial update rule (ED-Phys-01) through the higher-dimensional extension (ED-Phys-39) — into a single architectural statement of what Event Density is as a mathematical and physical framework.

The chapter has five goals.

**Goal 1.** Synthesise the entire ED-Phys program into a coherent architectural theory. The individual chapters developed the PDE, the constitutive functions, the invariants, the spectral analysis, the dimensional extension, the geometric analogues, and the cross-framework comparisons as separate investigations. This chapter unifies them into a single structure.

**Goal 2.** State the nine architectural laws in their final, unified form. Each law is given a precise mathematical statement, a derivation status, a dimensional dependence, and a universality classification. Together, the nine laws constitute the axiom set of the ED architecture.

**Goal 3.** Present the dimensional laws ($d = 1$ through $d = 4$, with asymptotic extensions to $d \to \infty$) as a single structural package. The factorial complexity law, the gradient-dominance law, the horizon-threshold law, and the topological conservation law are the four pillars of the dimensional theory.

**Goal 4.** Integrate the geometric, spectral, invariant, and morphological results from ED-Phys-37 through ED-Phys-39 into a unified positioning of ED within the landscape of nonlinear parabolic PDEs.

**Goal 5.** Identify the irreducible features that define ED as a distinct mathematical object — the minimum set of properties that cannot be obtained from any simpler or more established PDE framework.

This chapter completes the ED-Phys series. It defines the ED architecture as a reproducible, extensible, and falsifiable scientific framework — one that can be implemented, tested, compared, and extended by any researcher with access to the canonical PDE and a numerical solver.

---

# I. The ED Architecture

---

## I.1 The Canonical ED System

The Event Density framework is built on a single PDE system defined on a bounded domain $\Omega \subset \mathbb{R}^d$ with smooth boundary:

$$\partial_t \rho = D\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H\,v,$$

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr),$$

where $\rho(\mathbf{x}, t)$ is the event density, $v(t)$ is the participation variable, $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^d\!x$ is the domain-averaged density operator, and the constitutive functions are

$$M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0\,(\rho - \rho^*).$$

The system has three constitutive components, each with a distinct architectural role.

**Mobility $M(\rho)$.** The degenerate mobility controls the local diffusion rate. It vanishes at the capacity bound $\rho = \rho_{\max}$, producing dynamically isolated regions (horizons). It is maximal at $\rho = 0$, allowing rapid diffusion in low-density regions. The mobility is the mechanism through which ED generates free boundaries and spatially heterogeneous dynamics.

**Penalty $P(\rho)$.** The linear penalty drives the density toward the unique equilibrium $\rho^*$. It is the mechanism through which ED selects a single attractor and prevents the system from sustaining permanent spatial patterns. The penalty is monostable: unlike the Allen-Cahn double-well potential, it has no secondary equilibrium and no pattern-forming instability.

**Participation coupling $v(t)$.** The global variable $v$ is driven by the domain-averaged operator $\bar{F}$ and feeds back into the density equation through the coupling constant $H$. It is the mechanism through which ED encodes non-local awareness: the density at any point is influenced not only by its local neighbourhood but by the aggregate state of the entire field. This global coupling is the architectural feature that distinguishes ED from all comparison PDEs studied in ED-Phys-38.

The density operator $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$ can be written equivalently in divergence form as $F[\rho] = \nabla\!\cdot\!(M(\rho)\nabla\rho) - P(\rho)$. This form reveals the operator as a nonlinear diffusion with degenerate mobility and a zeroth-order reaction term — the invariant core of the ED architecture.

---

## I.2 The ED System Triple

The ED framework is defined by the system triple

$$(\Omega,\; F[\rho],\; v),$$

consisting of a spatial domain $\Omega$, a local density operator $F[\rho]$, and a global participation variable $v$.

The triple encodes a compositional structure (ED-Phys-12.5): the full dynamics is composed of a local component (the operator $F[\rho]$ acting pointwise on the density field) and a global component (the variable $v$ responding to the domain average of $F$ and feeding back uniformly). Neither component alone reproduces the ED architecture. The local operator $F[\rho]$ without participation reduces to a porous-medium equation with penalty — a well-studied PDE with no global coupling. The participation variable $v$ without the local operator is an ODE with no spatial structure. The composition of local and global is what generates the full invariant atlas.

This compositional structure connects to the foundational axioms of ED-Phys-05, which require that the update rule be:

- **Local in coupling:** the operator $F[\rho]$ depends only on $\rho$ and its spatial derivatives at each point.
- **Global in awareness:** the participation variable $v$ depends on the spatial average $\bar{F}$.
- **Bounded:** the density satisfies $0 \leq \rho \leq \rho_{\max}$.
- **Dissipative:** the Lyapunov functional decreases monotonically.

The system triple $(\Omega, F[\rho], v)$ is the minimal structure that satisfies all four axioms simultaneously.

---

## I.3 Architectural Invariants

The ED architecture defines a set of invariants — quantities computed from the density field and its derivatives — that serve as the coordinate system of the theory. These invariants are the observables through which the ED system is measured, compared, and classified.

**Lyapunov functional.** The energy

$$\mathcal{E}[\rho] = \int_\Omega \Phi(\rho)\,d^d\!x, \qquad \Phi(\rho) = \int_{\rho^*}^\rho \frac{P(s)}{M(s)}\,ds,$$

decreases monotonically along trajectories of the density equation. It is the master invariant from which the energy-monotonicity law and the dissipation-channel decomposition are derived.

**ED-complexity.** The gradient energy

$$C_{\mathrm{ED}} = \int_\Omega |\nabla\rho|^2\,d^d\!x$$

measures the total spatial inhomogeneity of the density field. It decreases monotonically and satisfies the factorial scaling law $C^{(d)} = C^{(1)}/d!$.

**Dissipation channels.** The total dissipation rate decomposes into three channels:

$$\dot{\mathcal{E}} = -\underbrace{D\int M|\nabla\rho|^2\,d^d\!x}_{R_{\mathrm{grad}}\cdot|\dot{\mathcal{E}}|} \;-\; \underbrace{D\int P(\rho)^2/M(\rho)\,d^d\!x}_{R_{\mathrm{pen}}\cdot|\dot{\mathcal{E}}|} \;-\; \underbrace{H\int v\,\partial_v\Phi\,d^d\!x}_{R_{\mathrm{part}}\cdot|\dot{\mathcal{E}}|},$$

with $R_{\mathrm{grad}} + R_{\mathrm{pen}} + R_{\mathrm{part}} = 1$. The gradient-dissipation ratio $R_{\mathrm{grad}}$ satisfies the derived law $R_{\mathrm{grad}}^{(d)} = d\pi^2/(d\pi^2 + P_0^2/M^*)$.

**Spectral entropy.** The modal entropy

$$H_{\mathrm{spec}} = -\sum_{\mathbf{k}} p_{\mathbf{k}}\,\ln p_{\mathbf{k}}, \qquad p_{\mathbf{k}} = \frac{|\hat{\rho}_{\mathbf{k}}|^2}{\sum_{\mathbf{k}'}|\hat{\rho}_{\mathbf{k}'}|^2},$$

measures the spectral concentration of the density field. It converges to a dimension-dependent attractor value as the field relaxes.

**Morphology fractions.** The Hessian eigenvalue structure classifies each spatial point into a morphological type (filament, sheet, pancake, blob). The volume fractions $f_{\mathrm{fil}}, f_{\mathrm{sht}}, f_{\mathrm{pan}}, f_{\mathrm{blb}}$ are the morphological coordinates of the field.

**Euler characteristic.** The topological invariant

$$\chi = \sum_{k=0}^{d-1}(-1)^k\,\beta_k$$

of the excursion set $\{\rho \geq \rho_{\mathrm{thresh}}\}$ is conserved in time ($d\chi/dt = 0$) for all dimensions tested.

---

# II. The Nine Architectural Laws (Final Form)

The nine laws are stated here in their final, unified form. Each law is accompanied by its derivation status, dimensional dependence, universality classification, and connection to the ED-Phys chapters where it was established.

---

## Law 1: Unique Attractor

**Statement.** The ED system possesses a unique globally attracting equilibrium: $\rho(\mathbf{x}, t) \to \rho^*$ uniformly as $t \to \infty$, and $v(t) \to 0$.

**Derivation status:** Full. The Lyapunov functional $\mathcal{E}[\rho]$ is strictly convex with a unique minimum at $\rho = \rho^*$, and $\dot{\mathcal{E}} \leq 0$ with equality only at equilibrium. LaSalle's invariance principle gives global asymptotic stability.

**Dimensional dependence:** None. The attractor is $\rho^*$ in all dimensions.

**Universality:** Universal across all constitutive parameters satisfying $M > 0$ on $(0, \rho_{\max})$ and $P(\rho^*) = 0$ with $P'(\rho^*) > 0$.

**Source:** ED-Phys-01, ED-Phys-36 (Section I.4).

---

## Law 2: Energy Monotonicity

**Statement.** The Lyapunov functional $\mathcal{E}[\rho]$ is strictly monotone decreasing along non-equilibrium trajectories:

$$\frac{d\mathcal{E}}{dt} \leq 0, \qquad \text{with equality iff } \rho = \rho^*.$$

**Derivation status:** Full. Direct computation from the PDE gives $\dot{\mathcal{E}} = -\int [M|\nabla\rho|^2 + P^2/M]\,d^d\!x \leq 0$.

**Dimensional dependence:** None. The energy decreases in all dimensions.

**Universality:** Universal for all constitutive parameters with $M \geq 0$, $P_0 > 0$.

**Source:** ED-Phys-36 (Section I.4), Appendix C.

---

## Law 3: Exponential Modal Decay

**Statement.** Each Fourier/cosine mode $\hat{\rho}_{\mathbf{k}}$ of the linearised system decays exponentially:

$$|\hat{\rho}_{\mathbf{k}}(t)| \leq |\hat{\rho}_{\mathbf{k}}(0)|\,\exp\!\bigl(-\sigma_{\mathbf{k}}\,t\bigr), \qquad \sigma_{\mathbf{k}} = D(M^*\mu_{\mathbf{k}} + P_0) > 0.$$

High-wavenumber modes decay faster than low-wavenumber modes.

**Derivation status:** Full (linearised). The linearised ED system about $\rho^*$ is diagonal in the Neumann eigenbasis with eigenvalues $-\sigma_{\mathbf{k}}$, all negative.

**Dimensional dependence:** The decay rate $\sigma_{\mathbf{k}}$ increases with $d$ for the fully-excited mode $\mathbf{k} = (k,\ldots,k)$, because $\mu_{\mathbf{k}} = dk^2\pi^2/L^2$.

**Universality:** Universal for the linearised system. Nonlinear effects can modify decay rates but not their sign.

**Source:** Appendix C, ED-Phys-36.

---

## Law 4: Factorial Complexity Dilution

**Statement.** The initial ED-complexity scales with dimension as

$$C_{\mathrm{ED}}^{(d)} = \frac{C_{\mathrm{ED}}^{(1)}}{d!}.$$

**Derivation status:** Partial. A structural argument based on mode-counting, gradient-energy distribution across $d$ orthogonal axes, and Neumann eigenvalue scaling produces the factorial suppression (ED-Phys-36, Section I.1). The argument is confirmed empirically at $d = 1, 2, 3$ (ED-Phys-35) and predicted at $d = 4$ (ED-Phys-39).

**Dimensional dependence:** Explicit: $d!$ suppression.

**Universality:** Holds for isotropic initial conditions with $N_m$ modes per axis. The factorial structure is a consequence of the Neumann eigenbasis and may not hold for anisotropic or non-modal initial conditions.

**Empirical record:**

| $d$ | Predicted $C^{(d)}/C^{(1)}$ | Measured | Agreement |
|-----|---------------------------|----------|-----------|
| 1 | 1 | 1 | exact |
| 2 | 1/2 | 0.498 | 0.4% |
| 3 | 1/6 | 0.164 | 1.6% |
| 4 | 1/24 | *(predicted: $\pm 5\%$)* | — |

**Source:** ED-Phys-35, ED-Phys-36 (Section I.1), ED-Phys-39 (Section II.1).

---

## Law 5: Gradient-Dissipation Dominance

**Statement.** The gradient-dissipation ratio satisfies

$$R_{\mathrm{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*},$$

and approaches unity as $d \to \infty$: all dissipation flows through the gradient-diffusion channel in the high-dimensional limit.

**Derivation status:** Derived. The formula follows from the linearised dissipation-rate decomposition using the Neumann eigenvalues (ED-Phys-36, Section I.2).

**Dimensional dependence:** Explicit: monotonically increasing with $d$, approaching 1.

**Universality:** Depends only on the constitutive parameters $P_0$ and $M^*$, not on $A$, $N_m$, or $N$.

**Empirical record:**

| $d$ | $R_{\mathrm{grad}}$ (derived) | $R_{\mathrm{grad}}$ (measured) |
|-----|-------------------------------|-------------------------------|
| 1 | 0.712 | 0.71 |
| 2 | 0.832 | 0.83 |
| 3 | 0.881 | 0.88 |
| 4 | 0.908 | *(predicted)* |
| $\infty$ | 1.000 | — |

**Source:** ED-Phys-35, ED-Phys-36 (Section I.2), ED-Phys-39 (Section II.2).

---

## Law 6: Topological Conservation

**Statement.** The Euler characteristic of the excursion set $\{\rho \geq \rho_{\mathrm{thresh}}\}$ is conserved:

$$\frac{d\chi}{dt} = 0 \qquad \text{for all } d.$$

**Derivation status:** Partial. The argument relies on the smoothness and parabolicity of the ED flow: no shocks, no finite-time singularities, no topology-changing bifurcations. The Morse-theoretic argument (non-degenerate critical points are preserved under smooth flow) supports this, but a full proof requires ruling out Hessian degeneracies along the entire trajectory (ED-Phys-36, Section I.3).

**Dimensional dependence:** None. The conservation holds in all dimensions where $\chi = \sum_{k}(-1)^k\beta_k$ is defined.

**Universality:** Expected to hold for all smooth initial conditions with non-degenerate critical points. May fail for pathological initial data with exactly degenerate Hessians.

**Source:** ED-Phys-35, ED-Phys-36 (Section I.3), ED-Phys-39 (Section II.4).

---

## Law 7: Horizon Formation

**Statement.** Horizons — regions where $M(\rho) \to 0$ and diffusion halts — form when the local density approaches $\rho_{\max}$. The effective amplitude for horizon formation scales as

$$A_{\mathrm{eff}} \sim \frac{A}{\sqrt{N_m^d}},$$

and horizon formation is exponentially suppressed with dimension.

**Derivation status:** Empirical with structural explanation. The amplitude-dilution argument (each of $N_m^d$ modes carries amplitude $\sim A/\sqrt{N_m^d}$) explains the scaling. Full horizon-formation criteria depend on the nonlinear dynamics near $\rho_{\max}$.

**Dimensional dependence:** Explicit: exponential suppression $\sim N_m^{-d/2}$.

**Universality:** Depends on $A$, $N_m$, and $\rho_{\max}$. For canonical parameters, horizons are common in 2D, suppressed in 3D, absent in 4D.

**Source:** ED-Phys-35, ED-Phys-39 (Section II.3).

---

## Law 8: Morphological Hierarchy

**Statement.** The Hessian eigenvalue structure of the density field classifies spatial structure into $d$ morphological types. In each dimension, one type dominates:

| Dimension | Dominant morphology | Fraction |
|-----------|-------------------|----------|
| 2D | Blob | 58% |
| 3D | Filament | 58% |
| 4D | Filament | ~45% |

The morphological fractions are determined by the interplay between the combinatorial weight $\binom{d}{k}$ of each codimension-$k$ class and the modal structure of the initial condition.

**Derivation status:** Empirical (2D, 3D) with combinatorial prediction (4D).

**Dimensional dependence:** Explicit: the number of morphological classes equals $d$, and the dominant class shifts with $d$.

**Universality:** Depends on the initial-condition structure ($N_m$, phase distribution). The combinatorial weights provide a baseline prediction.

**Source:** ED-Phys-35, ED-Phys-39 (Section III).

---

## Law 9: Sheet-Filament Oscillation

**Statement.** In $d \geq 3$, the morphology fractions of adjacent Hessian classes oscillate out of phase during the transient relaxation:

$$\Delta f_{\mathrm{sht}}(t) \approx -\Delta f_{\mathrm{fil}}(t).$$

In 4D, this generalises to a three-way oscillation among filaments, sheets, and pancakes.

**Derivation status:** Empirical. The oscillation is observed in 3D simulations (ED-Phys-35) and predicted in 4D (ED-Phys-39). A structural explanation connects it to the eigenvalue relaxation hierarchy of the Hessian, but no closed-form derivation exists.

**Dimensional dependence:** Requires $d \geq 3$ (insufficient eigenvalue structure in 2D). The number of oscillating classes increases with $d$.

**Universality:** Observed across all tested parameter regimes in 3D. Expected to be robust but amplitude-dependent.

**Source:** ED-Phys-35 (3D findings), ED-Phys-39 (Section III.3).

---

## Summary Table: The Nine Laws

| # | Law | Status | $d$-dep. | Universal? |
|---|-----|--------|----------|------------|
| 1 | Unique attractor | **Derived** | None | Yes |
| 2 | Energy monotonicity | **Derived** | None | Yes |
| 3 | Exponential modal decay | **Derived** (linear) | $\sigma_\mathbf{k} \sim d$ | Yes |
| 4 | Factorial complexity | **Partial** | $d!$ | Conditional |
| 5 | Gradient dominance | **Derived** | $R \sim d/(d+c)$ | Yes |
| 6 | Topological conservation | **Partial** | None | Expected |
| 7 | Horizon formation | **Empirical** | $\exp(-d)$ | Conditional |
| 8 | Morphological hierarchy | **Empirical** | $d$ classes | Conditional |
| 9 | Sheet-filament oscillation | **Empirical** | $d \geq 3$ | Expected |

Three laws are fully derived (1, 2, 3). Two are derived with specific structural assumptions (4, 5). One has a partial theoretical basis (6). Three are empirical with structural explanations (7, 8, 9). The architecture is mathematically grounded at its core and empirically rich at its periphery.

---

# III. Dimensional Synthesis ($d = 1 \to 4$)

---

## III.1 Complexity Scaling

The factorial complexity law

$$C_{\mathrm{ED}}^{(d)} = \frac{C_{\mathrm{ED}}^{(1)}}{d!}$$

is the most striking dimensional result of the ED program. It states that the spatial inhomogeneity of the density field is suppressed by a factorial factor as the dimension increases. The suppression is dramatic: by $d = 4$, the complexity is $1/24$ of its one-dimensional value; by $d = 10$, it is less than one part in three million.

The physical mechanism is geometric dilution. In $d$ dimensions, the gradient energy $C = \int|\nabla\rho|^2\,d^d\!x$ distributes across $d$ orthogonal axes. Each axis carries a fraction $\sim 1/d$ of the total gradient energy. The total number of active modes scales as $N_m^d$, and each mode carries amplitude $\sim A/\sqrt{N_m^d}$. When the squared amplitudes are summed with eigenvalue weights $\mu_{\mathbf{k}}$, the $d$-fold axis distribution and the $N_m^d$-fold amplitude dilution combine to produce the factorial suppression.

The complete dimensional record:

| $d$ | $d!$ | $C^{(d)}/C^{(1)}$ (predicted) | $C^{(d)}/C^{(1)}$ (measured) | Error |
|-----|------|-------------------------------|------------------------------|-------|
| 1 | 1 | 1.000 | 1.000 | — |
| 2 | 2 | 0.500 | 0.498 | 0.4% |
| 3 | 6 | 0.167 | 0.164 | 1.6% |
| 4 | 24 | 0.042 | *(pending)* | — |

The law is falsifiable at $d = 4$: the predicted value $C^{(4)}/C^{(1)} = 0.042$ must hold to within 5% for the law to be confirmed.

---

## III.2 Gradient Dominance

The gradient-dissipation law

$$R_{\mathrm{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*}$$

describes how the fraction of total energy dissipation carried by the gradient-diffusion channel increases monotonically with dimension. In the high-dimensional limit:

$$R_{\mathrm{grad}}^{(d)} = 1 - \frac{P_0^2/M^*}{d\pi^2} + O(1/d^2).$$

The correction to unity is $O(1/d)$, meaning that gradient diffusion becomes the sole dissipation mechanism as $d \to \infty$. The penalty channel, which contributes $\sim 29\%$ of dissipation in 1D, shrinks to $\sim 9\%$ in 4D and becomes negligible for $d \gg 1$.

The physical interpretation is that the Laplacian grows stronger with dimension (it sums $d$ second derivatives), while the penalty $P(\rho) = P_0(\rho - \rho^*)$ is a pointwise zeroth-order term that does not scale with $d$. The diffusion operator dominates the penalty by a factor of $d\pi^2 M^*/P_0^2$, which grows linearly with dimension.

The dimensional record:

| $d$ | $R_{\mathrm{grad}}$ (derived) | $R_{\mathrm{grad}}$ (measured) | $1 - R_{\mathrm{grad}}$ |
|-----|-------------------------------|-------------------------------|--------------------------|
| 1 | 0.712 | 0.71 | 0.288 |
| 2 | 0.832 | 0.83 | 0.168 |
| 3 | 0.881 | 0.88 | 0.119 |
| 4 | 0.908 | *(pending)* | 0.092 |
| 10 | 0.961 | — | 0.039 |
| $\infty$ | 1.000 | — | 0 |

---

## III.3 Horizon Threshold Scaling

Horizons — regions of vanishing mobility — are the most geometrically dramatic feature of the ED system. Their formation depends on the local density approaching $\rho_{\max}$, which requires constructive interference among the initial-condition modes. The effective amplitude available for this interference is

$$A_{\mathrm{eff}} = \frac{A}{\sqrt{N_m^d}}.$$

The dimensional record:

| $d$ | $N_m^d$ ($N_m = 2$) | $A_{\mathrm{eff}}$ ($A = 0.03$) | Horizons? |
|-----|---------------------|-------------------------------|-----------|
| 1 | 2 | 0.0212 | Marginal |
| 2 | 4 | 0.0150 | Common |
| 3 | 8 | 0.0106 | Suppressed |
| 4 | 16 | 0.0075 | Absent |

The transition from common (2D) to absent (4D) occurs over two dimensions. The mechanism is geometric: in higher dimensions, more modes must align constructively to produce a density peak, and the probability of such alignment decreases exponentially with the number of independent phase variables.

For $d \gg 1$, $A_{\mathrm{eff}} \sim A \cdot N_m^{-d/2}$, which decays faster than any polynomial. Horizon formation becomes a rare-event phenomenon, accessible only for anomalously large amplitudes $A \gg A_{\mathrm{crit}} \cdot N_m^{d/2}$.

---

## III.4 Topological Conservation

The Euler characteristic $\chi = \sum_{k=0}^{d-1}(-1)^k\beta_k$ of the excursion set $\{\rho \geq \rho_{\mathrm{thresh}}\}$ is conserved in time for all dimensions tested. The conservation is a consequence of the smooth, parabolic, and monotone character of the ED flow, which preserves the Morse structure of the density field.

| $d$ | $\chi$ definition | Conserved? | Method |
|-----|------------------|------------|--------|
| 1 | $\beta_0$ (components) | Yes | Direct count |
| 2 | $\beta_0 - \beta_1$ | Yes | Pixel Euler number |
| 3 | $\beta_0 - \beta_1 + \beta_2$ | Yes | Marching cubes |
| 4 | $\beta_0 - \beta_1 + \beta_2 - \beta_3$ | *(predicted)* | Cubical homology |

The conservation is expected to hold for all $d$, because the structural argument (smooth parabolic flow with non-degenerate Hessian preserves Morse structure) is dimension-independent. A violation would require a degenerate Hessian along the trajectory — a codimension-1 event that is generically absent for fixed constitutive parameters.

---

# IV. Geometric and Cross-Framework Synthesis

---

## IV.1 Geometric Analogues (ED-Phys-37)

The ED PDE shares structural features with three families of geometric evolution equations. These analogies are structural, not physical: they identify shared mathematical properties without claiming dynamical equivalence.

**Mean curvature flow.** The ED diffusion term $M(\rho)\nabla^2\rho$ is the scalar analogue of curvature-driven surface evolution $\partial_t X = H\hat{n}$. Both are parabolic, smoothing, and energy-dissipating. The ED system differs by its degenerate mobility ($M \to 0$ at capacity), its penalty term ($-P(\rho)$), and its global participation coupling ($v$). Mean curvature flow can shrink surfaces to extinction; ED relaxes to a uniform equilibrium.

**Ricci flow.** The Ricci flow $\partial_t g_{ij} = -2R_{ij}$ smooths curvature on a Riemannian manifold. Both Ricci flow and ED dissipate gradient energy and have parabolic character. The fundamental difference is that Ricci flow evolves a metric tensor (a symmetric 2-tensor field), while ED evolves a scalar density. There is no tensorial structure, no curvature tensor, and no geodesic equation in ED.

**Porous-medium and thin-film equations.** The ED operator, under the substitution $\delta = \rho_{\max} - \rho$, has exactly the PME principal part $\nabla\!\cdot\!(\delta^\beta\nabla\delta)$. The two systems share degenerate mobility, finite-speed propagation, and free-boundary formation. The thin-film equation shares the degeneracy but is fourth-order ($k^4$ decay), making it spectrally distant from ED.

---

## IV.2 Cross-Framework Distances (ED-Phys-38)

The quantitative comparison of ED-Phys-38 established four distance metrics (operator, spectral, invariant, morphological) and evaluated them against six PDE families. The distance hierarchy is consistent across all metrics and all dimensions tested:

$$\text{PME} \;\approx\; \text{FP} \;<\; \text{AC} \;<\; \text{CH} \;\approx\; \text{TFE} \;<\; \text{MCF/Ricci}.$$

**PME is closest in operator space.** The principal operators of ED and PME are identical for $\beta = m$ in the $\delta = \rho_{\max} - \rho$ variable. The total operator distance is controlled by the penalty and participation terms, which are sub-principal.

**AC is closest spectrally.** Both ED and AC have linearised decay rates of the form $\sigma_k = \alpha k^2 + \gamma$ (diffusive scaling plus constant offset from reaction/penalty). The spectral-distance metric is minimised when the parameters are matched: $D\,M^* \leftrightarrow \epsilon^2$ and $D\,P_0 \leftrightarrow f''(u^*)$.

**CH (spinodal) is closest morphologically.** During spinodal decomposition, the Cahn-Hilliard equation produces filament-dominated structure with minority sheets and blobs, morphology fractions close to ED's. The morphological distance is $d_{\mathrm{morph}} = 0.14$ in 3D and $d_{\mathrm{morph}} = 0.07$ in 4D. This proximity is structural (both classify via Hessian eigenvalues of multi-modal scalar fields) rather than dynamical (CH coarsens, ED decays).

---

## IV.3 ED's Position in PDE Space

The synthesis of geometric analogues and cross-framework distances locates ED precisely within the landscape of nonlinear parabolic PDEs. It occupies a specific position defined by the intersection of features borrowed from multiple families:

| Feature | Source PDE family | ED form |
|---------|------------------|---------|
| Degenerate mobility | PME | $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ |
| Diffusive spectral decay | AC | $\sigma_k = DM^*k^2\pi^2 + DP_0$ |
| Filamentary morphology | CH (spinodal) | Hessian-classified, filament-dominated |
| Curvature-driven smoothing | MCF | $M(\rho)\nabla^2\rho$ Laplacian term |
| Gradient-flow structure | FP | $\partial_t\rho = \nabla\!\cdot\!(M\nabla\delta\mathcal{E}/\delta\rho)$ |
| Unique architectural laws | **ED only** | Laws 1–9 |

The ED system is not reducible to any single comparison PDE. It is a PME with a penalty; or an AC without bistability; or a CH without the biharmonic; or a gradient flow with degenerate mobility and global coupling. No single simplification captures the full architecture. The nine laws are the irreducible remainder — the properties that survive when all shared features are accounted for.

---

# V. Irreducible Features of ED

Seven features of the ED system cannot be reproduced by any of the six comparison PDEs studied in ED-Phys-38. These features define ED as a distinct mathematical object.

---

**Feature 1: Penalty-driven unique attractor.** The penalty $P(\rho) = P_0(\rho - \rho^*)$ selects a unique, globally stable equilibrium $\rho^*$. The PME has self-similar (Barenblatt) attractors, not a fixed equilibrium. AC and CH have two stable equilibria. FP has a Boltzmann distribution. MCF can shrink to extinction. Only ED drives every initial condition to a single, specified, spatially uniform state.

**Feature 2: Participation coupling.** The global variable $v(t)$, coupled to the domain-averaged operator, introduces non-local feedback that is qualitatively distinct from mean-field models or spatial averaging. The participation variable is not a Lagrange multiplier for mass conservation (that role is filled by the boundary conditions); it is an independent dynamical degree of freedom that modulates the local density evolution. No comparison PDE has an analogous global mode.

**Feature 3: Factorial complexity dilution.** The law $C^{(d)} = C^{(1)}/d!$ is specific to the ED constitutive structure and the isotropic Neumann eigenbasis. While other PDEs exhibit dimensional effects on their solutions (e.g., the PME Barenblatt profile becomes broader in higher $d$), the factorial scaling of gradient energy has not been observed or derived for any comparison system.

**Feature 4: Gradient-dissipation law.** The formula $R_{\mathrm{grad}}^{(d)} = d\pi^2/(d\pi^2 + P_0^2/M^*)$ is a consequence of the specific ED decomposition of dissipation into gradient, penalty, and participation channels. No comparison PDE has an analogous three-channel decomposition, because none has the ED penalty-participation architecture.

**Feature 5: Sheet-filament oscillation.** The transient oscillatory exchange between morphological classes in $d \geq 3$ is a dynamical phenomenon not reported in any comparison framework. AC/CH produce morphological transitions (spinodal to coarsened), but these are monotone, not oscillatory. PME produces monotone front evolution. The ED oscillation reflects a non-trivial coupling between the Hessian eigenvalue relaxation rates along different axes.

**Feature 6: Topological conservation.** While smooth parabolic PDEs generically preserve excursion-set topology, the explicit verification and architectural elevation of $d\chi/dt = 0$ is unique to the ED program. In AC/CH, topology changes as interfaces merge during coarsening. In PME, topology changes as the support evolves. ED's penalty drives the system toward uniformity without topological transitions — a direct consequence of the unique attractor (Law 1).

**Feature 7: Horizon threshold scaling.** The dimensional scaling $A_{\mathrm{eff}} \sim A/\sqrt{N_m^d}$ and the resulting exponential suppression of horizon formation are specific to the ED multi-modal initial-condition structure and the degenerate mobility. While the PME has free boundaries in all dimensions, their formation does not depend on mode-count combinatorics and is not exponentially suppressed with $d$.

These seven features are not independent. Features 1 (unique attractor) and 6 (topological conservation) are logically connected: the unique attractor ensures monotone relaxation, which prevents topology changes. Features 3 (factorial complexity) and 5 (sheet-filament oscillation) both arise from the multi-modal eigenvalue structure. Features 4 (gradient dominance) and 7 (horizon suppression) both reflect the growing strength of the Laplacian relative to sub-principal terms as $d$ increases. The seven features form a coherent package, not a list of disconnected properties.

---

# VI. Architectural Map of ED

The full architecture of Event Density can be represented as a map with seven interconnected layers.

---

## Layer 1: Operator Structure

$$F[\rho] = \nabla\!\cdot\!\bigl(M(\rho)\,\nabla\rho\bigr) - P(\rho)$$

- Quasilinear, second-order, parabolic
- Degenerate mobility: $M \to 0$ at $\rho = \rho_{\max}$
- Monostable penalty: $P = 0$ at $\rho = \rho^*$
- Global coupling: $v(t)$ driven by $\bar{F}$

## Layer 2: Invariant Structure

| Invariant | Type | Monotone? | Dimension-dependent? |
|-----------|------|-----------|---------------------|
| $\mathcal{E}[\rho]$ | Energy | Decreasing | No |
| $C_{\mathrm{ED}}$ | Complexity | Decreasing | $d!$ scaling |
| $H_{\mathrm{spec}}$ | Entropy | Convergent | Attractor $d$-dependent |
| $R_{\mathrm{grad}}$ | Dissipation ratio | Increasing with $d$ | Explicit |
| $\chi$ | Topology | Conserved | None |
| $f_\alpha$ | Morphology | Transient | $d$ classes |

## Layer 3: Dimensional Laws

$$C^{(d)} = \frac{C^{(1)}}{d!}, \qquad R_{\mathrm{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*}, \qquad A_{\mathrm{eff}} \sim \frac{A}{\sqrt{N_m^d}}, \qquad \frac{d\chi}{dt} = 0.$$

## Layer 4: Geometric Analogues

| Analogue | Shared feature | Structural difference |
|----------|---------------|----------------------|
| MCF | Laplacian smoothing | Degenerate mobility, penalty, participation |
| Ricci | Curvature dissipation | Scalar vs tensor, no geodesics |
| PME | Degenerate diffusion | Penalty, participation, unique attractor |

## Layer 5: Cross-Framework Distances

$$\text{PME} \approx \text{FP} < \text{AC} < \text{CH} \approx \text{TFE} < \text{MCF/Ricci}$$

Measured across four metrics: operator, spectral, invariant, morphological. Dimensionally stable ($d = 1$–$4$).

## Layer 6: Morphological Taxonomy

| $d$ | Classes | Dominant | Transient dynamics |
|-----|---------|----------|-------------------|
| 1 | — | — | Monotone decay |
| 2 | Sheet, Blob | Blob (58%) | Monotone exchange |
| 3 | Filament, Sheet, Blob | Filament (58%) | Sheet-filament oscillation |
| 4 | Filament, Sheet, Pancake, Blob | Filament (~45%) | Three-way oscillation |

## Layer 7: Topological Invariants

$$\chi^{(d)} = \sum_{k=0}^{d-1}(-1)^k\,\beta_k, \qquad \frac{d\chi}{dt} = 0 \quad \forall\;d.$$

Minkowski functionals: $(d+1)$ per dimension, providing complete geometric characterisation of excursion sets.

---

The seven layers are not independent. The operator structure (Layer 1) determines the invariant structure (Layer 2) through the Lyapunov theory. The dimensional laws (Layer 3) emerge from the eigenvalue structure of the operator. The geometric analogues (Layer 4) and cross-framework distances (Layer 5) locate the operator within the PDE landscape. The morphological taxonomy (Layer 6) and topological invariants (Layer 7) are computed from the density field that the operator produces. The architecture is a single, coherent mathematical structure — not a collection of independent results.

---

# VII. Closing Summary

ED-Phys-40 has accomplished five things.

**Unified the ED-Phys program.** Forty chapters of development — from the initial update rule to the 4D extension — have been consolidated into a single architectural statement. The canonical PDE, the constitutive functions, the system triple, and the nine laws form the invariant core. The dimensional laws, geometric analogues, cross-framework distances, morphological taxonomy, and topological invariants form the structural periphery.

**Stated the nine laws in final form.** Three laws are fully derived (unique attractor, energy monotonicity, exponential decay). Two are derived with structural assumptions (factorial complexity, gradient dominance). One has a partial theoretical basis (topological conservation). Three are empirical with structural explanations (horizon formation, morphological hierarchy, sheet-filament oscillation). The architecture is mathematically grounded where it can be and empirically anchored where it must be.

**Synthesised the dimensional program.** The four dimensional laws — factorial complexity ($d!$), gradient dominance ($d/(d+c)$), horizon suppression ($N_m^{-d/2}$), topological conservation ($d\chi/dt = 0$) — are presented as a unified package with complete empirical records for $d = 1$–$3$, quantitative predictions for $d = 4$, and asymptotic extensions to $d \to \infty$.

**Integrated the cross-framework results.** The distance hierarchy PME $\approx$ FP $<$ AC $<$ CH $\approx$ TFE $<$ MCF/Ricci is dimensionally stable and consistent across all four metrics. The PME is the nearest structural relative; the seven irreducible features define the gap between ED and every comparison PDE.

**Defined ED's mathematical identity.** Event Density is a degenerate parabolic diffusion system with monostable penalty and global participation coupling, possessing a unique attractor, factorial complexity dilution, gradient-dissipation dominance, topological conservation, and a morphological hierarchy that oscillates during transient relaxation. This definition is precise, testable, and irreducible. Any system exhibiting all nine laws is, architecturally, an ED system. Any system lacking even one of the seven irreducible features is not.

The ED-Phys series is complete.
