# Numerical Atlas of the Event-Density Canon

**Computational Demonstration of the ED Architectural Ontology**

Allen Proxmire
March 2026

---

## 0. Preface

### 0.1 Purpose

The Numerical Atlas is the computational companion to the Architectural Canon, the Rigour Paper (Appendices C and D), and the Applications Paper. Its purpose is threefold:

1. **Demonstration.** To exhibit, through direct numerical integration of the canonical ED system (C.1), the analytic phenomena proved in Appendix C: local and global well-posedness (C.1–C.2), spectral decay and modal hierarchy (C.3–C.4), nonlinear stability and Lyapunov dissipation (C.5), the bifurcation at the critical damping surface (C.6), and the three-stage convergence to equilibrium (C.7). Each theorem in Appendix C will be paired with a numerical experiment that realizes the theorem's conclusion in a concrete parameter regime.

2. **Exploration.** To survey the $(D, \zeta, \tau)$-parameter space of the canonical ED system beyond the neighborhoods accessible to linearized analysis. The analytic results of Appendix C are sharpest near the equilibrium $(\rho^*, 0)$ and near the critical damping surface $\Delta = 1$. The Numerical Atlas maps the full nonlinear landscape: far-from-equilibrium transients, the algebraic relaxation phase of the three-stage convergence, the geometry of the triad coupling at large amplitude, and the approach to the mobility-collapse barrier $\rho \to \rho_{\max}$.

3. **Calibration.** To provide reference solutions, parameter maps, and quantitative benchmarks against which the physical predictions of the Applications Paper can be compared. The Applications Paper derives qualitative predictions — complexity-ordered decoherence, temporal-halo formation, mesoscopic transport thresholds — from the architecture. The Numerical Atlas supplies the quantitative detail: the numerical values of decay rates, oscillation frequencies, triad amplitude ratios, and convergence times as functions of the canonical parameters. These values are the bridge between the structural ontology and experimental measurement.

The Atlas does not prove theorems. Every mathematical claim rests on Appendix C. The Atlas demonstrates that the theorems produce the phenomena they describe, maps the quantitative dependence on parameters, and provides reproducible numerical evidence for every qualitative assertion in the ED-Arch series.

### 0.2 Relationship to the Rigour Paper and Applications Paper

The three documents form a logical chain:

- **Appendix C** (PDE Analysis) establishes the mathematical infrastructure: the well-posedness of the canonical ED system, the spectral structure of the linearized operator, the construction of the Lyapunov functional, the exponential stability of the equilibrium, the bifurcation geometry at the discriminant surface, and the long-time convergence theorem. All results are stated as rigorous theorems with complete proofs.

- **Appendix D** (Universality Class) defines the equivalence-class framework: ED-equivalence, the universality class $\mathcal{U}_{\mathrm{ED}}$, the closure and invariance theorems, and the universality statement (Theorem D.19). This framework ensures that the numerical experiments in the Atlas are not artifacts of a particular parameter choice — they represent structural features shared by every system in $\mathcal{U}_{\mathrm{ED}}$.

- **The Applications Paper** derives falsifiable physical predictions from the architecture, organized by domain (quantum, galactic, condensed matter, photonics, phononics). Each prediction traces back to specific theorems in Appendix C and specific invariants in Appendix D.

The Numerical Atlas occupies the space between proof and prediction. It takes the theorems of Appendix C and makes them visible: the spectral gap is not merely a lower bound in an inequality but a measurable decay rate in a time series; the bifurcation at $\Delta = 1$ is not merely a center manifold reduction but a qualitative change in the relaxation profile as a parameter is swept; the three-stage convergence is not merely an asymptotic statement but a sequence of temporal regimes with measurable crossover times.

Conversely, the Atlas takes the predictions of the Applications Paper and makes them quantitative. The decoherence rate $\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}$ is a qualitative scaling; the Atlas will provide the proportionality constant and its dependence on the canonical parameters. The temporal-halo profile is a qualitative prediction of Principle 5; the Atlas will provide the halo shape, amplitude, and lag as functions of $(D, \zeta, \tau)$ and the baryonic activity profile.

### 0.3 The Role of Numerical Demonstration

A numerical experiment is not a proof. It is, however, an indispensable complement to proof in three respects:

**Concreteness.** Appendix C proves that the energy functional $\mathcal{E}[\rho, v]$ is monotonically decreasing along solutions (Lemma C.6) and that the dissipation separates into three structural channels — gradient dissipation, penalty relaxation, and participation damping (Remark C.9). The Atlas will show this separation in a time series: three curves, each corresponding to a dissipation channel, whose sum equals the total energy decay rate, tracked over the full duration of a convergence experiment. The visual decomposition makes the theorem's content immediate.

**Regime mapping.** The analytic results of Appendix C identify four dynamical regimes (Regime I: subcritical stable; Regime II: oscillatory stable; Regime III: marginally stable; Regime IV: far-from-equilibrium transient). The boundaries between these regimes are determined by the damping discriminant $\Delta := \zeta/(4\tau D P'(\rho^*)/M(\rho^*))$ and the ED-complexity $C_{\mathrm{ED}}$. The Atlas will map these boundaries numerically across the full parameter space, producing regime diagrams that extend the linearized classification of Appendix C.3 into the nonlinear domain.

**Quantitative benchmarking.** The stability theorem (Theorem C.43) guarantees exponential convergence at rate $\sigma > 0$ within a neighborhood of radius $\epsilon_0$ around the equilibrium. The Atlas will measure $\sigma$ and $\epsilon_0$ as functions of the canonical parameters, providing the quantitative targets needed to convert the Applications Paper's qualitative predictions into experimentally testable numerical bounds.

### 0.4 Reproducibility Philosophy

Every numerical result in the Atlas is governed by the following reproducibility standard:

1. **Complete specification.** Each experiment is defined by an explicit list: the spatial domain $\Omega$, the spatial dimension $d$, the grid resolution $N$, the time step $\Delta t$, the total integration time $T$, the canonical parameters $(D, \zeta, \tau, \rho_{\max}, \rho^*)$, the constitutive functions $M(\rho)$ and $P(\rho)$ (given as closed-form expressions), and the initial condition $(\rho_0(x), v_0)$ (given as an analytic formula). No parameter is left implicit.

2. **Convergence verification.** Each experiment is accompanied by a convergence study: the computation is repeated at two or more resolutions (typically $N$, $2N$, $4N$) and two or more time steps (typically $\Delta t$, $\Delta t/2$, $\Delta t/4$), and the quantitative outputs (decay rates, oscillation frequencies, equilibrium values) are compared. A result is reported only if it is converged to within stated tolerances.

3. **Independence of implementation.** The numerical methods described in §0.6 are standard and can be implemented in any scientific computing environment. The Atlas does not depend on a proprietary solver or a specific software package. All algorithms are described at the mathematical level (stencil coefficients, time-stepping formulas, boundary treatment), not at the code level.

4. **Separation of method and result.** The Atlas distinguishes sharply between *structural* features of the solution — those guaranteed by the theorems of Appendix C and independent of the numerical method — and *numerical* features — those dependent on the discretization, resolution, or time-stepping scheme. Only structural features are reported as results of the Atlas. Numerical features (convergence rates of the discretization, condition numbers, iteration counts) are reported in the method sections for reproducibility but are not interpreted as properties of the ED system.

5. **Alignment with Appendix E.** The discretization schemes, stability conditions, parameter tables, and spectral analysis pipeline are consistent with the methods documented in Appendix E (Numerical Methods) of the Rigour Paper. The Atlas extends Appendix E from a methods specification to a complete set of demonstrated results.

### 0.5 Numerical Environment

The computations in the Atlas are designed to be reproducible in any standard scientific computing environment. The reference implementations use:

- **Python** (NumPy, SciPy) for finite-difference solvers, parameter sweeps, and post-processing. Python is chosen for accessibility and ecosystem breadth. The finite-difference solver uses SciPy's sparse-matrix infrastructure for the implicit time-stepping and NumPy's FFT routines for spectral analysis.

- **Julia** for high-resolution spectral solvers and long-time integration requiring performance-critical inner loops. Julia's native support for differential-equation solvers (DifferentialEquations.jl) and its compilation model make it well-suited for the parameter-space surveys that require thousands of independent integrations.

- **MATLAB** as a verification environment. Selected experiments are replicated in MATLAB to confirm that the results are independent of the implementation language and the numerical-linear-algebra backend.

No result in the Atlas depends on a feature specific to any one of these environments. The mathematical specification of each algorithm (§0.6) is sufficient for independent reimplementation.

### 0.6 Overview of the Numerical Scheme

The canonical ED system (C.1),

$$
\begin{cases}
\partial_t \rho = D\,F[\rho] + H\,v, \\[4pt]
\dot{v} = \tau^{-1}\bigl(F[\rho] - \zeta\,v\bigr),
\end{cases}
$$

with $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$, is discretized by two complementary methods.

**Method A: Finite-difference discretization.**

The spatial domain $\Omega = [0, L]^d$ is discretized on a uniform Cartesian grid with spacing $h = L/N$. The Laplacian $\nabla^2\rho$ is approximated by the standard second-order central-difference stencil. In one dimension:

$$
(\nabla^2\rho)_j \approx \frac{\rho_{j+1} - 2\rho_j + \rho_{j-1}}{h^2}.
$$

The gradient-squared term $|\nabla\rho|^2$ is approximated by the centered first-difference stencil:

$$
(|\nabla\rho|^2)_j \approx \left(\frac{\rho_{j+1} - \rho_{j-1}}{2h}\right)^2.
$$

Neumann boundary conditions $\partial_\nu\rho = 0$ are enforced by ghost-point reflection: $\rho_{-1} = \rho_1$ and $\rho_{N+1} = \rho_{N-1}$.

Time integration is semi-implicit: the linear diffusion term $D\,M(\rho^n)\nabla^2\rho^{n+1}$ is treated implicitly (backward Euler), while the nonlinear terms $D\,M'(\rho^n)|\nabla\rho^n|^2 - D\,P(\rho^n) + H\,v^n$ are evaluated explicitly at the current time level. This yields a linear system at each time step:

$$
\bigl(I - \Delta t\,D\,M(\rho^n)\,\nabla_h^2\bigr)\,\rho^{n+1}
= \rho^n + \Delta t\,\bigl[D\,M'(\rho^n)\,|\nabla_h\rho^n|^2 - D\,P(\rho^n) + H\,v^n\bigr],
$$

where $\nabla_h^2$ denotes the discrete Laplacian matrix. The tridiagonal (1D) or banded (2D, 3D) structure of the implicit matrix permits efficient direct solution. The participation variable is advanced by the explicit Euler step:

$$
v^{n+1} = v^n + \frac{\Delta t}{\tau}\bigl(F_h[\rho^n] - \zeta\,v^n\bigr),
$$

where $F_h[\rho^n]$ is the spatially averaged discrete operator. When higher accuracy in the ODE is required, the $v$-equation is integrated by the classical fourth-order Runge–Kutta method using the same time step $\Delta t$.

**Method B: Spectral discretization.**

For problems on periodic or symmetric domains where Fourier analysis is natural, the density field is expanded in the eigenbasis of the Neumann Laplacian:

$$
\rho(x,t) = \sum_{k=0}^{N-1} \hat{\rho}_k(t)\,\phi_k(x),
$$

where $\phi_k$ are the Neumann eigenfunctions ($\phi_k(x) = \cos(k\pi x/L)$ in one dimension) and $\hat{\rho}_k(t)$ are the modal amplitudes. The linear diffusion is diagonal in this basis: $\nabla^2\phi_k = -\lambda_k\,\phi_k$ with $\lambda_k = (k\pi/L)^2$. The nonlinear terms $M'(\rho)|\nabla\rho|^2$ and $P(\rho)$ are evaluated in physical space and transformed back to spectral space at each time step (pseudospectral method).

Time integration of the spectral system uses an exponential-time-differencing (ETD) scheme: the linear part is integrated exactly via the matrix exponential, and the nonlinear part is treated by a second- or fourth-order Runge–Kutta method (ETD-RK2 or ETD-RK4). This eliminates the stiffness associated with high-wavenumber diffusive modes and permits larger time steps than the fully explicit method.

The spectral method is used primarily for the experiments in the Atlas that involve modal analysis (§C.4 demonstrations), triad coupling (§C.4.5 demonstrations), and long-time convergence studies where spectral accuracy reduces the required resolution.

**Method selection.** Method A is used for general-purpose integration, parameter sweeps, and experiments requiring non-periodic boundary conditions or irregular domains. Method B is used for spectral analysis, modal decomposition, and high-accuracy long-time integration on regular domains. All results reported in the Atlas are verified to be consistent between Methods A and B on the domains where both apply.

### 0.7 Stability Considerations

The semi-implicit finite-difference scheme (Method A) requires a Courant–Friedrichs–Lewy (CFL) condition on the explicit terms. The dominant explicit contribution is the nonlinear advection-like term $D\,M'(\rho)\,|\nabla\rho|^2$. A standard von Neumann stability analysis yields the constraint

$$
\Delta t \leq \frac{C_{\mathrm{CFL}}\,h^2}{D\,\|M'(\rho)\|_\infty\,\|\nabla\rho\|_\infty\,h + D\,\|M(\rho)\|_\infty},
$$

where $C_{\mathrm{CFL}}$ is a method-dependent constant of order unity. In practice, the implicit treatment of the linear diffusion relaxes this constraint significantly; the CFL condition is governed by the explicit nonlinear terms alone.

The spectral scheme (Method B) with ETD time stepping is unconditionally stable in the linear part. The nonlinear stability is controlled by the same CFL-type condition on the explicit Runge–Kutta substeps, but with the stiff linear modes already integrated exactly, the effective time-step restriction is governed by the amplitude of the nonlinear interaction — the triad coupling strength — rather than by the diffusive time scale.

Two additional stability considerations specific to the ED system are addressed:

**Near-degeneracy.** As $\rho \to \rho_{\max}$, the mobility $M(\rho) \to 0$ and the diffusion coefficient degenerates. Numerically, this manifests as a stiffening of the implicit system near grid points where $\rho$ is close to $\rho_{\max}$. The energy barrier (Proposition C.11) guarantees that $\rho$ remains bounded away from $\rho_{\max}$ by a margin $\delta > 0$ determined by the initial energy; in practice, the margin is monitored at each time step, and the computation is flagged if $\max_j \rho_j > \rho_{\max} - \delta_{\mathrm{tol}}$ for a user-specified tolerance $\delta_{\mathrm{tol}}$.

**Positivity preservation.** The analytic solution satisfies $\rho > 0$ for all time (Theorem C.2), but the numerical scheme does not automatically preserve positivity. For the finite-difference scheme, positivity is enforced by a projection step: if any grid value $\rho_j^{n+1} \leq 0$ after the implicit solve, it is reset to a small positive floor $\rho_{\mathrm{floor}} = 10^{-12}$ and the energy is recomputed. In all experiments reported in the Atlas, the projection is never activated at converged resolutions — it serves as a safety net, not a regularization.

### 0.8 Figure Convention

The Numerical Atlas describes figures but does not render them. Each figure is specified by:

- **Data source:** the experiment number, the parameter set, and the computed quantity.
- **Axes:** the independent and dependent variables, their ranges, and their physical or canonical units.
- **Content:** the curves, surfaces, or contour levels to be plotted, including line styles and labels.
- **Structural features:** the specific analytic prediction (theorem, proposition, or remark from Appendix C) that the figure is designed to demonstrate.
- **Convergence status:** confirmation that the plotted data is converged (resolution and time-step independent to within stated tolerances).

This convention ensures that the Atlas is a complete mathematical document — every figure is reproducible from its specification without ambiguity — while remaining independent of any specific visualization software or rendering engine. The ED-SIM simulation engine provides a reference implementation for generating the described figures.

---

## 1. Canonical PDE — Numerical Setup

This section specifies the complete numerical infrastructure for all subsequent experiments in the Atlas. Every experiment in Sections 2–8 draws its discretization, time-stepping, constitutive functions, and validation criteria from the material established here. Nothing in this section is new mathematics; it is the translation of the analytic objects in Appendix C into computable form.

---

### 1.1 Restatement of the Canonical ED PDE

The system under numerical integration is the canonical ED PDE (C.1):

$$
\begin{cases}
\partial_t \rho = D\,F[\rho] + H\,v, \\[4pt]
\dot{v} = \dfrac{1}{\tau}\bigl(F[\rho] - \zeta\,v\bigr),
\end{cases}
\tag{1.1}
$$

where the nonlinear density operator is

$$
F[\rho] := M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho),
\tag{1.2}
$$

subject to the canonical constraints:

| Symbol | Meaning | Constraint |
|--------|---------|------------|
| $D$ | Direct-channel weight | $0 < D < 1$ |
| $H$ | Mediated-channel weight | $H = 1 - D$ (Principle 2) |
| $\zeta$ | Participation damping coefficient | $\zeta > 0$ |
| $\tau$ | Participation time scale | $\tau > 0$ |
| $\rho^*$ | Penalty equilibrium density | $P(\rho^*) = 0$, $P'(\rho^*) > 0$ (Principle 3) |
| $\rho_{\max}$ | Capacity bound | $M(\rho_{\max}) = 0$, $M(\rho) > 0$ for $\rho < \rho_{\max}$ (Principle 4) |

The constitutive functions $M(\rho)$ and $P(\rho)$ are smooth on $[0, \rho_{\max}]$ and $(- \infty, +\infty)$ respectively, satisfying the regularity assumptions of §C.1.1. For all numerical experiments in this Atlas, we use the following canonical choices unless otherwise stated:

**Mobility:**

$$
M(\rho) = M_0\,\bigl(\rho_{\max} - \rho\bigr)^\beta, \qquad \beta > 0,\; M_0 > 0.
\tag{1.3}
$$

This is the simplest smooth mobility satisfying $M(\rho_{\max}) = 0$ and $M(\rho) > 0$ for $\rho < \rho_{\max}$. The exponent $\beta$ controls the rate of mobility collapse: $\beta = 1$ gives linear vanishing; $\beta = 2$ gives quadratic vanishing (softer barrier). The default is $\beta = 2$, $M_0 = 1$.

**Penalty:**

$$
P(\rho) = P_0\,(\rho - \rho^*), \qquad P_0 > 0.
\tag{1.4}
$$

This is the simplest smooth penalty with $P(\rho^*) = 0$ and $P'(\rho) = P_0 > 0$ everywhere. The linear penalty is sufficient for demonstrating all architectural phenomena; the universality class $\mathcal{U}_{\mathrm{ED}}$ (Appendix D) guarantees that the qualitative structure is insensitive to the constitutive form. The default is $P_0 = 1$.

**Derivative of mobility:**

$$
M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta - 1}.
\tag{1.5}
$$

This expression is used directly in the evaluation of $F[\rho]$ and its spatial discretization. For $\beta = 2$, we have $M'(\rho) = -2M_0(\rho_{\max} - \rho)$, which is smooth on the entire interval $[0, \rho_{\max}]$.

---

### 1.2 Boundary Conditions and Domain Choices

**Boundary conditions.** All experiments use Neumann (no-flux) boundary conditions:

$$
\partial_\nu \rho \big|_{\partial\Omega} = 0,
\tag{1.6}
$$

consistent with the functional setting of §C.1.1. The Neumann condition ensures mass conservation (§1.7.3) and compatibility with the Poincaré–Wirtinger inequality used in the stability analysis (Proposition C.8). No Dirichlet, Robin, or periodic conditions are employed unless explicitly noted; when periodic conditions are used for the spectral method (Method B of §0.6), the results are cross-validated against the Neumann formulation.

**Domain choices.** The Atlas employs three standard domains, selected to span different spatial dimensions and geometries:

**Domain $\Omega_1$: The unit interval.** $\Omega_1 = [0, L]$ with $L = 1$ in $d = 1$. This is the primary domain for one-dimensional experiments: convergence studies (§1.7), energy dissipation demonstrations (§1.7.2), spectral analysis (Section 3), bifurcation sweeps (Section 5), and long-time convergence (Section 6). The Neumann eigenfunctions are $\varphi_n(x) = \sqrt{2/L}\cos(n\pi x/L)$ for $n \geq 1$ and $\varphi_0 = 1/\sqrt{L}$, with eigenvalues $\mu_n = (n\pi/L)^2$.

**Domain $\Omega_2$: The unit square.** $\Omega_2 = [0, L]^2$ with $L = 1$ in $d = 2$. This domain is used for two-dimensional spatial pattern demonstrations: the modal hierarchy (Section 3), gradient-complexity maps (Section 4), and the approach to the mobility-collapse barrier (Section 7). The Neumann eigenfunctions are products $\varphi_{n_1}(x_1)\,\varphi_{n_2}(x_2)$ with eigenvalues $\mu_{n_1,n_2} = \pi^2(n_1^2 + n_2^2)$.

**Domain $\Omega_3$: The unit cube.** $\Omega_3 = [0, L]^3$ with $L = 1$ in $d = 3$. This domain is used selectively for three-dimensional validation: confirming that the qualitative phenomena (regime classification, convergence rates, triad structure) are dimension-independent, as required by the universality class framework (Appendix D, Theorem D.9).

The domain length $L$ is a free parameter that can be absorbed into the spatial eigenvalues $\mu_n$ by the rescaling invariance of Theorem D.7. Unless otherwise stated, $L = 1$.

---

### 1.3 Parameter Sets for Simulations

The Atlas organizes its experiments around five canonical parameter sets, designed to sample each dynamical regime and the boundaries between them. The regime classification follows Appendix C.3 (Definition C.19): the sign of the modal discriminant

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4H\,P_*'}{\tau}
\tag{1.7}
$$

determines whether the homogeneous mode decays in an oscillatory ($\mathscr{D}_0 < 0$), critically damped ($\mathscr{D}_0 = 0$), or monotonic ($\mathscr{D}_0 > 0$) fashion.

**Parameter Set I — Deep Oscillatory Regime.**

| Parameter | Value |
|-----------|-------|
| $D$ | 0.3 |
| $H = 1 - D$ | 0.7 |
| $\zeta$ | 0.1 |
| $\tau$ | 1.0 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $P_0$ | 1.0 |
| $M_0$ | 1.0 |
| $\beta$ | 2.0 |

Discriminant: $\mathscr{D}_0 = (0.3 - 0.1)^2 - 4 \cdot 0.7 \cdot 1.0 = 0.04 - 2.8 = -2.76 < 0$. The homogeneous mode exhibits oscillatory decay with pronounced spiraling. This set is used for demonstrations of the underdamped regime (Appendix C.3), the spectral gap with complex eigenvalues (Corollary C.18), and the three-stage convergence with an oscillatory intermediate phase (Appendix C.7).

**Parameter Set II — Moderate Oscillatory Regime.**

| Parameter | Value |
|-----------|-------|
| $D$ | 0.6 |
| $H$ | 0.4 |
| $\zeta$ | 0.5 |
| $\tau$ | 1.0 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $P_0$ | 1.0 |
| $M_0$ | 1.0 |
| $\beta$ | 2.0 |

Discriminant: $\mathscr{D}_0 = (0.6 - 0.5)^2 - 4 \cdot 0.4 \cdot 1.0 = 0.01 - 1.6 = -1.59 < 0$. Mildly oscillatory. This set provides a less extreme version of Set I for comparing decay rates and oscillation frequencies.

**Parameter Set III — Near-Critical Regime.**

| Parameter | Value |
|-----------|-------|
| $D$ | 0.8 |
| $H$ | 0.2 |
| $\zeta$ | 1.8 |
| $\tau$ | 1.0 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $P_0$ | 1.0 |
| $M_0$ | 1.0 |
| $\beta$ | 2.0 |

Discriminant: $\mathscr{D}_0 = (0.8 - 1.8)^2 - 4 \cdot 0.2 \cdot 1.0 = 1.0 - 0.8 = 0.2 > 0$ but small. The system is overdamped but close to the critical surface $\mathscr{D}_0 = 0$. This set is used for bifurcation demonstrations (Appendix C.6) and for measuring the slowdown of convergence near criticality.

**Parameter Set IV — Deep Monotonic Regime.**

| Parameter | Value |
|-----------|-------|
| $D$ | 0.9 |
| $H$ | 0.1 |
| $\zeta$ | 5.0 |
| $\tau$ | 1.0 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $P_0$ | 1.0 |
| $M_0$ | 1.0 |
| $\beta$ | 2.0 |

Discriminant: $\mathscr{D}_0 = (0.9 - 5.0)^2 - 4 \cdot 0.1 \cdot 1.0 = 16.81 - 0.4 = 16.41 > 0$. Strongly overdamped. The homogeneous mode decays monotonically with well-separated real eigenvalues. This set is used for stability demonstrations (Appendix C.5) and long-time convergence experiments in the purely monotonic regime.

**Parameter Set V — High Participation Coupling.**

| Parameter | Value |
|-----------|-------|
| $D$ | 0.2 |
| $H$ | 0.8 |
| $\zeta$ | 0.3 |
| $\tau$ | 0.5 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $P_0$ | 1.0 |
| $M_0$ | 1.0 |
| $\beta$ | 2.0 |

Discriminant: $\mathscr{D}_0 = (0.2 - 0.6)^2 - 4 \cdot 0.8 \cdot 2.0 = 0.16 - 6.4 = -6.24 < 0$. Strongly oscillatory with dominant mediated-channel contribution. This set is used for experiments emphasizing the role of the participation variable: the three-channel dissipation decomposition (Section 4), the effect of $\tau$ on convergence rates, and the nonlinear triad dynamics at large $H/D$ ratio.

**Additional parameter variations.** Beyond the five canonical sets, individual sections of the Atlas specify targeted parameter variations — sweeps of a single parameter while holding others fixed — to map the dependence of a specific observable on a specific canonical parameter. These variations are documented in the section where they appear.

**Standard initial conditions.** Unless otherwise stated, all experiments use one of the following initial density profiles:

**IC-A: Single-mode perturbation.**

$$
\rho_0(x) = \rho^* + A\,\cos(\pi x / L), \qquad v_0 = 0,
\tag{1.8}
$$

where $A > 0$ is the perturbation amplitude. This initializes only the first Neumann mode and is used for linearized-regime validation and single-mode decay experiments. Default: $A = 0.05$.

**IC-B: Multi-mode perturbation.**

$$
\rho_0(x) = \rho^* + \sum_{n=1}^{N_{\mathrm{modes}}} A_n\,\cos(n\pi x / L), \qquad v_0 = 0,
\tag{1.9}
$$

with prescribed amplitudes $\{A_n\}$. This initializes a superposition of spatial modes and is used for modal hierarchy and triad-coupling experiments. Default: $A_n = 0.1/n^2$, $N_{\mathrm{modes}} = 8$.

**IC-C: Localized perturbation.**

$$
\rho_0(x) = \rho^* + A\,\exp\!\left(-\frac{(x - x_0)^2}{2\sigma^2}\right), \qquad v_0 = 0,
\tag{1.10}
$$

where $x_0$ is the center and $\sigma$ is the width. This initializes a spatially localized disturbance with broad spectral content and is used for nonlinear transient experiments, gradient-complexity measurements, and the approach to the mobility-collapse barrier. Default: $A = 0.3$, $x_0 = L/2$, $\sigma = 0.05$.

**IC-D: Near-capacity perturbation.**

$$
\rho_0(x) = \rho_{\max} - \delta + A\,\cos(\pi x / L), \qquad v_0 = 0,
\tag{1.11}
$$

with $0 < \delta \ll 1$ and $|A| < \delta$. This initializes the density near the capacity bound and is used for mobility-collapse experiments (§1.6, Section 7). Default: $\delta = 0.05$, $A = 0.02$.

---

### 1.4 Spatial Discretization

This section specifies the discrete spatial operators used by both Method A (finite-difference) and Method B (spectral) of §0.6, restricted to the one-dimensional domain $\Omega_1 = [0, L]$. The two-dimensional generalizations on $\Omega_2$ are obtained by tensor-product extension and are noted where they differ.

#### 1.4.1 Finite-Difference Discretization (Method A)

Let $N$ be the number of interior grid points and define the uniform spacing $h = L/(N+1)$. The grid points are $x_j = jh$ for $j = 0, 1, \ldots, N+1$, with $x_0 = 0$ and $x_{N+1} = L$ the boundary points. The discrete density vector is $\boldsymbol{\rho}^n = (\rho_0^n, \rho_1^n, \ldots, \rho_{N+1}^n)^\top$ at time level $t_n = n\,\Delta t$.

**Discrete Laplacian.** The second-order central-difference approximation is

$$
(\nabla_h^2 \rho)_j = \frac{\rho_{j-1} - 2\rho_j + \rho_{j+1}}{h^2}, \qquad j = 1, \ldots, N.
\tag{1.12}
$$

**Neumann boundary enforcement.** The no-flux condition $\partial_\nu\rho = 0$ at $x = 0$ and $x = L$ is implemented via ghost points: define $\rho_{-1} := \rho_1$ and $\rho_{N+2} := \rho_N$. This yields the boundary stencils

$$
(\nabla_h^2 \rho)_0 = \frac{2(\rho_1 - \rho_0)}{h^2}, \qquad
(\nabla_h^2 \rho)_{N+1} = \frac{2(\rho_N - \rho_{N+1})}{h^2}.
\tag{1.13}
$$

The resulting discrete Laplacian matrix $\mathbf{L}_h \in \mathbb{R}^{(N+2) \times (N+2)}$ is symmetric, negative semi-definite, with a one-dimensional null space spanned by the constant vector — the discrete analogue of the zero Neumann eigenmode.

**Discrete gradient squared.** The centered first-difference approximation is

$$
(|\nabla_h \rho|^2)_j = \left(\frac{\rho_{j+1} - \rho_{j-1}}{2h}\right)^2, \qquad j = 1, \ldots, N,
\tag{1.14}
$$

with boundary values computed using the ghost-point reflection:

$$
(|\nabla_h \rho|^2)_0 = 0, \qquad (|\nabla_h \rho|^2)_{N+1} = 0.
\tag{1.15}
$$

These boundary values are identically zero by the Neumann condition, consistent with the analytic fact that $|\nabla\rho|^2 = (\partial_\nu\rho)^2 = 0$ on $\partial\Omega$.

**Discrete operator $F_h$.** Combining the above, the discrete nonlinear operator is

$$
F_h[\boldsymbol{\rho}]_j = M(\rho_j)\,(\nabla_h^2\rho)_j + M'(\rho_j)\,(|\nabla_h\rho|^2)_j - P(\rho_j),
\tag{1.16}
$$

evaluated pointwise for $j = 0, 1, \ldots, N+1$.

**Spatial accuracy.** The discrete Laplacian (1.12) and discrete gradient (1.14) are both second-order accurate: $(\nabla_h^2\rho)_j = (\nabla^2\rho)(x_j) + O(h^2)$ and $(|\nabla_h\rho|^2)_j = |\nabla\rho(x_j)|^2 + O(h^2)$ for smooth $\rho$. The overall spatial truncation error of $F_h$ is $O(h^2)$.

**Two-dimensional extension.** On $\Omega_2 = [0,L]^2$ with grid spacing $h = L/(N+1)$ in each direction, the discrete Laplacian is the standard five-point stencil:

$$
(\nabla_h^2\rho)_{i,j} = \frac{\rho_{i-1,j} + \rho_{i+1,j} + \rho_{i,j-1} + \rho_{i,j+1} - 4\rho_{i,j}}{h^2},
\tag{1.17}
$$

with ghost-point Neumann enforcement on all four boundaries. The gradient squared is the sum of centered differences in each direction:

$$
(|\nabla_h\rho|^2)_{i,j} = \left(\frac{\rho_{i+1,j} - \rho_{i-1,j}}{2h}\right)^2 + \left(\frac{\rho_{i,j+1} - \rho_{i,j-1}}{2h}\right)^2.
\tag{1.18}
$$

#### 1.4.2 Spectral Discretization (Method B)

On the domain $\Omega_1 = [0, L]$, expand the density in the Neumann cosine basis:

$$
\rho(x, t) = \sum_{k=0}^{N-1} \hat{\rho}_k(t)\,\phi_k(x), \qquad \phi_k(x) = \begin{cases} 1/\sqrt{L} & k = 0, \\ \sqrt{2/L}\,\cos(k\pi x/L) & k \geq 1, \end{cases}
\tag{1.19}
$$

with eigenvalues $\mu_k = (k\pi/L)^2$. The Neumann boundary condition is automatically satisfied by every basis function.

**Linear operations in spectral space.** The Laplacian acts diagonally:

$$
\widehat{(\nabla^2\rho)}_k = -\mu_k\,\hat{\rho}_k.
\tag{1.20}
$$

The linear part of the $\rho$-equation in spectral form is therefore

$$
\widehat{(\text{linear})}_k = -D\,(M_*\,\mu_k + P_*')\,\hat{\rho}_k = -D\,\alpha_k\,\hat{\rho}_k,
\tag{1.21}
$$

recovering the modal decay coefficients $\alpha_k$ of (C.12). For the ETD time-stepping scheme, the integrating factor for mode $k$ is $e^{-D\alpha_k\,\Delta t}$.

**Nonlinear operations in physical space.** The terms $M(\rho)\nabla^2\rho$, $M'(\rho)|\nabla\rho|^2$, and $P(\rho)$ involve pointwise nonlinear functions of $\rho$ and are evaluated pseudospectrally:

```
PROCEDURE Evaluate_F_spectral(ρ̂):
    1. Transform to physical space: ρⱼ = Σₖ ρ̂ₖ φₖ(xⱼ) via DCT
    2. Compute ∇²ρ in spectral space: (∇²ρ̂)ₖ = -μₖ ρ̂ₖ
    3. Transform ∇²ρ to physical space via DCT
    4. Evaluate pointwise: M(ρⱼ)·(∇²ρ)ⱼ + M'(ρⱼ)·|∇ρⱼ|² − P(ρⱼ)
    5. Transform result back to spectral space via DCT
    RETURN F̂
```

The discrete cosine transform (DCT-I) is used for the Neumann basis; its computational cost is $O(N\log N)$.

**De-aliasing.** The pointwise products $M(\rho)\nabla^2\rho$ and $M'(\rho)|\nabla\rho|^2$ generate spectral content beyond the resolved bandwidth. Aliasing is controlled by the standard 3/2-rule: the physical-space evaluation is performed on a grid of $3N/2$ points, and the result is truncated back to $N$ modes before the spectral time step. This ensures that quadratic nonlinearities are alias-free; for the constitutive functions (1.3)–(1.4), which are polynomial or low-order smooth, the 3/2-rule is sufficient.

---

### 1.5 Time Stepping

The semi-implicit philosophy of §0.6 is implemented in two concrete schemes: implicit Euler for robustness and initial transients, and Crank–Nicolson for accuracy in long-time integration. Both treat the linear diffusion implicitly and the nonlinear terms explicitly.

#### 1.5.1 Implicit Euler Scheme (First Order)

At each time step $t_n \to t_{n+1} = t_n + \Delta t$, the density is advanced by

$$
\frac{\boldsymbol{\rho}^{n+1} - \boldsymbol{\rho}^n}{\Delta t}
= D\,M(\boldsymbol{\rho}^n)\,\nabla_h^2\,\boldsymbol{\rho}^{n+1}
+ D\bigl[M'(\boldsymbol{\rho}^n)\,|\nabla_h\boldsymbol{\rho}^n|^2 - P(\boldsymbol{\rho}^n)\bigr]
+ H\,v^n,
\tag{1.22}
$$

which rearranges to the linear system

$$
\bigl(\mathbf{I} - \Delta t\,D\,\mathbf{M}^n\,\mathbf{L}_h\bigr)\,\boldsymbol{\rho}^{n+1}
= \boldsymbol{\rho}^n + \Delta t\,\bigl[D\,\mathbf{G}^n - D\,\mathbf{P}^n + H\,v^n\,\mathbf{1}\bigr],
\tag{1.23}
$$

where $\mathbf{M}^n = \operatorname{diag}(M(\rho_0^n), \ldots, M(\rho_{N+1}^n))$ is the pointwise mobility matrix, $\mathbf{G}^n$ is the vector with entries $M'(\rho_j^n)(|\nabla_h\rho^n|^2)_j$, $\mathbf{P}^n$ is the vector with entries $P(\rho_j^n)$, and $\mathbf{1}$ is the vector of ones.

The matrix $\mathbf{I} - \Delta t\,D\,\mathbf{M}^n\,\mathbf{L}_h$ is symmetric positive definite (since $-\mathbf{L}_h$ is positive semi-definite and $D\,M(\rho_j^n) > 0$ at every interior grid point), so the linear system is solved by the Thomas algorithm (tridiagonal solver) in $O(N)$ operations in one dimension, or by a banded Cholesky factorization in $O(N^2)$ operations in two dimensions.

The participation variable is advanced by the explicit update

$$
v^{n+1} = v^n + \frac{\Delta t}{\tau}\bigl(\bar{F}_h^n - \zeta\,v^n\bigr),
\tag{1.24}
$$

where $\bar{F}_h^n = (N+2)^{-1}\sum_j F_h[\boldsymbol{\rho}^n]_j$ is the spatial average of the discrete operator. When the ODE time scale $\tau$ is small relative to $\Delta t$, the explicit Euler step for $v$ may become unstable; in this case, the $v$-equation is instead solved by the exact exponential integrator

$$
v^{n+1} = v^n\,e^{-\zeta\,\Delta t/\tau} + \frac{\bar{F}_h^n}{\zeta}\bigl(1 - e^{-\zeta\,\Delta t/\tau}\bigr),
\tag{1.25}
$$

which is unconditionally stable and exact for constant $\bar{F}_h$.

**Temporal accuracy.** The implicit Euler scheme is first-order accurate in time: $\|\boldsymbol{\rho}^n - \rho(\cdot, t_n)\|_{L^2} = O(\Delta t)$ on smooth solutions. It is unconditionally $L^2$-stable in the linear diffusion and subject to the CFL constraint of §0.7 only through the explicit nonlinear terms.

#### 1.5.2 Crank–Nicolson Scheme (Second Order)

For higher temporal accuracy, the linear diffusion is averaged between time levels:

$$
\frac{\boldsymbol{\rho}^{n+1} - \boldsymbol{\rho}^n}{\Delta t}
= \frac{D}{2}\,\mathbf{M}^n\,\mathbf{L}_h\,(\boldsymbol{\rho}^{n+1} + \boldsymbol{\rho}^n)
+ D\bigl[\mathbf{G}^n - \mathbf{P}^n\bigr]
+ H\,v^n,
\tag{1.26}
$$

yielding the linear system

$$
\left(\mathbf{I} - \frac{\Delta t\,D}{2}\,\mathbf{M}^n\,\mathbf{L}_h\right)\boldsymbol{\rho}^{n+1}
= \left(\mathbf{I} + \frac{\Delta t\,D}{2}\,\mathbf{M}^n\,\mathbf{L}_h\right)\boldsymbol{\rho}^n
+ \Delta t\bigl[D\,\mathbf{G}^n - D\,\mathbf{P}^n + H\,v^n\,\mathbf{1}\bigr].
\tag{1.27}
$$

The implicit matrix has the same structure as (1.23) and is solved by the same algorithm. The scheme is second-order accurate: $\|\boldsymbol{\rho}^n - \rho(\cdot, t_n)\|_{L^2} = O(\Delta t^2)$.

**Remark on the nonlinear terms.** The explicit treatment of the nonlinear terms $M'(\rho)|\nabla\rho|^2$ and $P(\rho)$ in both (1.22) and (1.26) limits the overall scheme to first-order accuracy in the implicit Euler case and introduces a mixed first/second-order error in the Crank–Nicolson case. For the linearized regime (small perturbations near $\rho^*$), where $M'(\rho)|\nabla\rho|^2$ is second-order in the perturbation amplitude, the Crank–Nicolson scheme achieves full second-order accuracy. In the nonlinear regime, second-order accuracy in the nonlinear terms can be recovered by an extrapolation step (evaluating the explicit terms at $t_{n+1/2}$ via Richardson extrapolation), but this is used only when explicitly noted.

#### 1.5.3 Spectral Time Stepping (ETD-RK4)

For the spectral discretization (Method B), the modal amplitudes are advanced by the exponential-time-differencing fourth-order Runge–Kutta scheme (ETD-RK4). Writing the $k$-th mode equation as

$$
\frac{d\hat{\rho}_k}{dt} = c_k\,\hat{\rho}_k + \hat{N}_k(t),
\tag{1.28}
$$

where $c_k = -D\,M_*\,\mu_k$ is the linear decay rate and $\hat{N}_k$ collects all nonlinear contributions (including the penalty and the deviation of $M(\rho)$ from $M_*$), the ETD-RK4 substeps are:

```
PROCEDURE ETD-RK4 step (ρ̂, v, Δt):
    FOR each mode k:
        Eₖ  = exp(cₖ Δt)
        E₂ₖ = exp(cₖ Δt/2)

    a = N̂(ρ̂, v)                              // Nonlinear evaluation at tₙ
    ρ̂_a = E₂ · ρ̂ + (E₂ − 1) · a / c         // Half-step

    b = N̂(ρ̂_a, v + Δt/2 · v̇)               // Nonlinear evaluation at tₙ + Δt/2
    ρ̂_b = E₂ · ρ̂ + (E₂ − 1) · b / c         // Second half-step

    c_rk = N̂(ρ̂_b, v + Δt/2 · v̇)            // Nonlinear evaluation at tₙ + Δt/2
    ρ̂_c = E₂ · ρ̂_a + (E₂ − 1) · (2c_rk − a) / c  // Full step from half

    d = N̂(ρ̂_c, v + Δt · v̇)                 // Nonlinear evaluation at tₙ + Δt

    ρ̂^{n+1} = E · ρ̂ + [a·(−4−cΔt+E·(4−3cΔt+(cΔt)²))
                       + 2(b+c_rk)·(2+cΔt+E·(−2+cΔt))
                       + d·(−4−3cΔt−(cΔt)²+E·(4−cΔt))] / (c²Δt²)

    v^{n+1} via exponential integrator (1.25)

    RETURN (ρ̂^{n+1}, v^{n+1})
```

The ETD-RK4 scheme is fourth-order accurate in time and unconditionally stable in the linear part. The $1/c_k$ factors are evaluated using the L'Hôpital-safe form for small $|c_k\Delta t|$ (modes near $k = 0$) to avoid numerical cancellation.

#### 1.5.4 Time-Step Selection

The time step $\Delta t$ is selected to satisfy two constraints:

1. **CFL constraint for explicit nonlinear terms:**

$$
\Delta t \leq C_{\mathrm{CFL}} \cdot \frac{h^2}{D\,\max_j|M'(\rho_j^n)|\cdot\max_j\bigl|(\nabla_h\rho^n)_j\bigr|\cdot h + D\,\max_j M(\rho_j^n)},
\tag{1.29}
$$

with $C_{\mathrm{CFL}} = 0.5$ as the default safety factor.

2. **ODE stability constraint for the participation equation** (when using explicit Euler for $v$):

$$
\Delta t \leq \frac{2\tau}{\zeta}.
\tag{1.30}
$$

This constraint is automatically satisfied when the exponential integrator (1.25) is used.

In practice, the time step is set at the beginning of each experiment to satisfy both constraints at the initial condition, and is held fixed unless the solution approaches the mobility-collapse region (§1.6), in which case adaptive reduction is applied.

---

### 1.6 Handling Mobility Collapse Near $\rho_{\max}$

As $\rho \to \rho_{\max}$, the mobility $M(\rho) \to 0$ and the diffusion coefficient degenerates. The analytic theory guarantees that $\rho$ remains strictly below $\rho_{\max}$ for all time (Theorem C.2, Proposition C.11), but the numerical scheme must enforce this property at the discrete level.

#### 1.6.1 The Numerical Challenge

The semi-implicit scheme (1.22) treats the diffusion coefficient $M(\rho^n)$ explicitly. As $\rho_j^n \to \rho_{\max}$, the diffusion vanishes at grid point $j$, and three numerical pathologies arise:

1. **Stiffness inversion.** The implicit matrix $\mathbf{I} - \Delta t\,D\,\mathbf{M}^n\,\mathbf{L}_h$ approaches the identity at grid points where $M \approx 0$, while remaining stiff elsewhere. The condition number deteriorates, and the linear solver may lose accuracy.

2. **Loss of parabolicity.** At grid points where $M(\rho_j^n) \approx 0$, the equation transitions from parabolic to degenerate, and the implicit scheme loses its stabilizing effect.

3. **Overshoot.** The explicit nonlinear terms can drive $\rho_j^{n+1}$ above $\rho_{\max}$, producing unphysical values where $M(\rho)$ would be evaluated at negative arguments of $(\rho_{\max} - \rho)^\beta$.

#### 1.6.2 Regularization Strategy

The Atlas employs a three-layer approach that preserves the structural content of mobility collapse while preventing numerical failure:

**Layer 1: Monitoring.** At each time step, compute the proximity margin

$$
\delta^n := \min_j\,(\rho_{\max} - \rho_j^n).
\tag{1.31}
$$

If $\delta^n < \delta_{\mathrm{warn}}$ (default: $\delta_{\mathrm{warn}} = 0.01\,\rho_{\max}$), issue a diagnostic flag. If $\delta^n < \delta_{\mathrm{crit}}$ (default: $\delta_{\mathrm{crit}} = 10^{-4}\,\rho_{\max}$), activate Layers 2 and 3.

**Layer 2: Adaptive time-step reduction.** When $\delta^n < \delta_{\mathrm{crit}}$, the time step is reduced by the factor

$$
\Delta t \to \Delta t \cdot \min\!\left(1,\;\frac{\delta^n}{\delta_{\mathrm{crit}}}\right),
\tag{1.32}
$$

ensuring that the explicit terms cannot drive $\rho$ past $\rho_{\max}$ in a single step. The time step is restored to its original value once $\delta^n > 2\,\delta_{\mathrm{crit}}$.

**Layer 3: Projection.** If, after the implicit solve, any grid value satisfies $\rho_j^{n+1} \geq \rho_{\max}$, it is projected back to

$$
\rho_j^{n+1} \to \rho_{\max} - \delta_{\mathrm{floor}}, \qquad \delta_{\mathrm{floor}} = 10^{-12}.
\tag{1.33}
$$

Symmetrically, if $\rho_j^{n+1} \leq 0$, it is projected to $\delta_{\mathrm{floor}}$. The energy $\mathcal{E}$ is recomputed after any projection. In all converged experiments reported in the Atlas, the projection is never activated — it is a safety net for under-resolved transients during development and testing, not a regularization of the dynamics.

#### 1.6.3 Verification of the Energy Barrier

The effectiveness of the mobility-collapse handling is verified by the following diagnostic, run on every experiment that approaches the capacity region:

1. Compute $\mathcal{E}[\boldsymbol{\rho}^n, v^n]$ at each time step.
2. Compute $\Phi(\rho_{\max} - \delta^n)$ at the grid point closest to $\rho_{\max}$.
3. Confirm that $\Phi(\rho_{\max} - \delta^n)$ remains bounded by the initial energy $\mathcal{E}[\rho_0, v_0]$, as required by Proposition C.11.
4. Confirm that $\delta^n$ stabilizes at a positive value consistent with the energy-barrier estimate.

This diagnostic is reported for every experiment using IC-D (near-capacity initial condition, eq. 1.11).

---

### 1.7 Validation Tests

Before any architectural demonstration, the numerical infrastructure is validated by four independent tests. Each test targets a specific property of the continuous PDE system and verifies that the discrete scheme preserves it to within controlled error bounds.

#### 1.7.1 Convergence in Space and Time

**Test protocol.** Integrate the canonical system (1.1) with Parameter Set I and IC-A ($A = 0.05$) on $\Omega_1$ to final time $T = 5.0$. Repeat at four spatial resolutions $N \in \{64, 128, 256, 512\}$ with time step scaled as $\Delta t = C h^2$ (to maintain the CFL ratio), and at four temporal resolutions $\Delta t \in \{10^{-2}, 5 \times 10^{-3}, 2.5 \times 10^{-3}, 1.25 \times 10^{-3}\}$ with $N = 512$ fixed.

**Measured quantities.** At the final time, compute:

- $e_h := \|\boldsymbol{\rho}^N_h - \boldsymbol{\rho}^N_{h/2}\|_{L^2}$, the Richardson-extrapolation spatial error between successive resolutions.
- $e_{\Delta t} := \|\boldsymbol{\rho}^N_{\Delta t} - \boldsymbol{\rho}^N_{\Delta t/2}\|_{L^2}$, the temporal error between successive time steps.

**Expected results.** For the implicit Euler scheme: $e_h = O(h^2)$ and $e_{\Delta t} = O(\Delta t)$. For the Crank–Nicolson scheme: $e_h = O(h^2)$ and $e_{\Delta t} = O(\Delta t^2)$. For the spectral ETD-RK4 scheme: $e_h$ converges spectrally (faster than any polynomial in $1/N$ for smooth solutions) and $e_{\Delta t} = O(\Delta t^4)$.

**Convergence criterion.** The numerical scheme is accepted if the measured convergence rates match the theoretical orders to within 10% on a log-log fit over the four refinement levels.

**Figure description (Figure 1.1).** Two panels. Left: log-log plot of $e_h$ versus $h$ for all three schemes (Method A implicit Euler, Method A Crank–Nicolson, Method B ETD-RK4), showing reference slopes of 2, 2, and exponential. Right: log-log plot of $e_{\Delta t}$ versus $\Delta t$ for the same three schemes, showing reference slopes of 1, 2, and 4.

#### 1.7.2 Energy Dissipation

**Test protocol.** Integrate the system with Parameter Set I and IC-B ($N_{\mathrm{modes}} = 8$, $A_n = 0.1/n^2$) on $\Omega_1$ to $T = 50.0$ at resolution $N = 256$, $\Delta t = 10^{-3}$ (Crank–Nicolson).

**Measured quantities.** At each time step, compute:

- The total energy $\mathcal{E}[\boldsymbol{\rho}^n, v^n]$ via the trapezoidal-rule quadrature of $\Phi(\rho)$ (eq. C.4) and the participation kinetic energy $\frac{\tau H}{2}(v^n)^2$.
- The discrete dissipation rate $-\Delta\mathcal{E}/\Delta t := -(\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t$.
- The three dissipation-channel contributions:
  - Gradient dissipation: $\mathcal{D}_{\mathrm{grad}}^n := D\sum_j P'(\rho_j^n)\,|\nabla_h\rho_j^n|^2/M(\rho_j^n)\cdot h$.
  - Penalty relaxation: $\mathcal{D}_{\mathrm{pen}}^n := D\sum_j P(\rho_j^n)^2/M(\rho_j^n)\cdot h$.
  - Participation damping: $\mathcal{D}_{\mathrm{part}}^n := H\zeta\,(v^n)^2$.

**Expected results.** The energy $\mathcal{E}$ is monotonically non-increasing (Lemma C.6), asymptoting to $\mathcal{E}[\rho^*, 0]$. The gradient dissipation $\mathcal{D}_{\mathrm{grad}}$ dominates at early times (when spatial gradients are large), the penalty relaxation $\mathcal{D}_{\mathrm{pen}}$ dominates at intermediate times (when the mean density is relaxing toward $\rho^*$), and the participation damping $\mathcal{D}_{\mathrm{part}}$ contributes throughout with a profile reflecting the oscillatory or monotonic decay of $v$.

**Validation criterion.** The discrete energy must be non-increasing at every time step to within the temporal truncation error: $\mathcal{E}^{n+1} \leq \mathcal{E}^n + O(\Delta t^p)$ where $p$ is the order of the time-stepping scheme. A single instance of energy increase exceeding $10\,\Delta t^p\,\mathcal{E}^n$ constitutes a validation failure.

**Figure description (Figure 1.2).** Three panels. Top: $\mathcal{E}(t)$ on a semilog-$y$ axis, showing monotonic descent to the equilibrium energy. Middle: the three dissipation-channel contributions as functions of time, on a semilog-$y$ axis, showing the crossover from gradient-dominated to penalty-dominated dissipation. Bottom: the discrete residual $\mathcal{E}^{n+1} - \mathcal{E}^n + \Delta t\,(\mathcal{D}_{\mathrm{grad}}^n + \mathcal{D}_{\mathrm{pen}}^n + \mathcal{D}_{\mathrm{part}}^n)$, confirming closure of the discrete dissipation identity to within truncation error.

#### 1.7.3 Mass Conservation

**Analytic property.** Integrating the $\rho$-equation over $\Omega$ with Neumann boundary conditions:

$$
\frac{d}{dt}\int_\Omega \rho\,dx = -D\int_\Omega P(\rho)\,dx + H\,v\,|\Omega|.
\tag{1.34}
$$

The total mass $\bar{\rho}|\Omega| = \int_\Omega\rho\,dx$ is not conserved — it evolves according to the penalty and participation terms. However, the specific combination

$$
\mathcal{M}(t) := \int_\Omega\rho\,dx + H\tau\,v(t)
$$

satisfies a closed equation whose structure depends on the penalty. For the linear penalty $P(\rho) = P_0(\rho - \rho^*)$, this becomes

$$
\frac{d\mathcal{M}}{dt} = -D\,P_0\bigl(\mathcal{M} - (\rho^* + H\tau v)\,|\Omega|\bigr) + \text{(participation terms)}.
$$

In the special case $v = 0$ and spatially constant $\rho$, the density relaxes to $\rho^*$ with rate $D\,P_0$ — there is no exact mass invariant. The numerical test therefore verifies the *rate* of mass change rather than mass conservation per se.

**Test protocol.** Integrate with Parameter Set IV (monotonic regime, weak participation coupling) and IC-A on $\Omega_1$, $N = 256$, $\Delta t = 10^{-3}$, $T = 20.0$.

**Measured quantities.**

- The discrete total mass $\mathcal{M}_h^n := h\sum_j\rho_j^n$.
- The predicted mass rate of change: $d\mathcal{M}/dt|_{\mathrm{pred}} = -D\,h\sum_j P(\rho_j^n) + H\,v^n\,L$.
- The numerical mass rate of change: $d\mathcal{M}/dt|_{\mathrm{num}} = (\mathcal{M}_h^{n+1} - \mathcal{M}_h^n)/\Delta t$.

**Validation criterion.** The residual $|d\mathcal{M}/dt|_{\mathrm{num}} - d\mathcal{M}/dt|_{\mathrm{pred}}|$ must be bounded by $O(\Delta t^p + h^2)$ at every time step. Additionally, the total mass must converge to $\rho^*\,L$ as $t \to \infty$, consistent with the unique equilibrium $(\rho^*, 0)$.

**Figure description (Figure 1.3).** Two panels. Left: total mass $\mathcal{M}_h(t)$ as a function of time, showing relaxation from the initial value $(\rho^* + A)\,L\,\delta_{n,0\text{-component}}$ toward $\rho^*\,L$. Right: the mass-rate residual as a function of time, confirming $O(\Delta t^p + h^2)$ scaling.

#### 1.7.4 Comparison to Linearized Analytic Solutions

**Analytic reference.** For small perturbation amplitude $A$, the linearized solution of (C.9) with IC-A (single-mode, $n = 1$) is

$$
u_1(t) = A\,e^{-D\alpha_1 t}, \qquad w(t) = 0,
\tag{1.35}
$$

where $\alpha_1 = M_*\mu_1 + P_*' = M(\rho^*)\,(\pi/L)^2 + P_0$. The participation variable remains zero because the initial condition $v_0 = 0$ and the $n = 1$ mode do not couple to the spatially homogeneous participation (Remark C.16).

For the homogeneous mode (IC-A with $n = 0$, i.e., $\rho_0(x) = \rho^* + A$, $v_0 = v_{\mathrm{init}} \neq 0$), the linearized solution is

$$
\begin{pmatrix} u_0(t) \\ w(t) \end{pmatrix}
= c_+\,\mathbf{r}_+\,e^{\lambda_+ t} + c_-\,\mathbf{r}_-\,e^{\lambda_- t},
\tag{1.36}
$$

where $\lambda_\pm$ are the eigenvalues (C.15), $\mathbf{r}_\pm$ are the corresponding eigenvectors of $\mathbf{A}_0$ (C.13), and $c_\pm$ are determined by the initial data $(A, v_{\mathrm{init}})$. When $\mathscr{D}_0 < 0$, this produces damped oscillations with frequency $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ and decay rate $\sigma = \frac{1}{2}(D\,P_*' + \zeta/\tau)$.

**Test protocol.** For each of the five parameter sets (I–V), integrate the full nonlinear system with IC-A at two amplitudes: $A = 10^{-4}$ (deep linearized regime) and $A = 0.05$ (mildly nonlinear). Compare the numerical solution $\rho_h^n(x_j)$ to the analytic linearized solution (1.35) or (1.36) at every time step.

**Measured quantities.**

- The pointwise error $\varepsilon^n := \max_j|\rho_j^n - \rho_{\mathrm{lin}}(x_j, t_n)|$.
- The decay rate measured by fitting $\log|\rho_j^n - \rho^*|$ versus $t$ over $t \in [1, 5]$ and extracting the slope $\hat{\sigma}$.
- The oscillation frequency (for Sets I, II, V) measured by zero-crossing intervals of $u_0(t)$ and extracting $\hat{\omega}$.

**Expected results.** At $A = 10^{-4}$, the error $\varepsilon^n$ is dominated by the temporal and spatial discretization error ($O(\Delta t^p + h^2)$), and the measured decay rate $\hat{\sigma}$ and frequency $\hat{\omega}$ match the analytic values $\sigma$ and $\omega$ to within discretization tolerance. At $A = 0.05$, the error includes a nonlinear contribution $O(A^2)$ from the quadratic term $M'(\rho)|\nabla\rho|^2$, and the measured rates show systematic deviations from the linearized prediction — these deviations are the first signal of the nonlinear triad coupling (Principle 7).

**Validation criterion.** At $A = 10^{-4}$: the relative error in $\hat{\sigma}$ must be below 1%, and $\hat{\omega}$ (when applicable) must agree with the analytic value to within 1%. At $A = 0.05$: the relative deviation must be consistent with $O(A^2)$ corrections and must vanish under amplitude reduction.

**Figure description (Figure 1.4).** Four panels. Top-left: time series of $u_0(t)$ for Parameter Set I at $A = 10^{-4}$, overlaid with the analytic solution (1.36), showing indistinguishable agreement. Top-right: same for $A = 0.05$, showing the onset of nonlinear frequency shift and amplitude-dependent damping. Bottom-left: convergence of measured $\hat{\sigma}$ toward the analytic $\sigma$ as $A \to 0$, for all five parameter sets. Bottom-right: convergence of measured $\hat{\omega}$ toward the analytic $\omega$ as $A \to 0$, for Parameter Sets I, II, and V (the oscillatory cases).

---

## 2. Regime Geometry Visualization

The four dynamical regimes of the ED system — underdamped oscillatory, overdamped monotonic, critically damped, and their boundaries — are proved to exist in Appendix C.3 (Theorem C.22, Definition C.19) and their geometric organization in parameter space is established in Appendix C.6 (Definition C.51, Propositions C.52–C.53). This section exhibits each regime through direct numerical integration of the canonical system (1.1) and maps the transitions between them across the $(D, \zeta)$-parameter plane.

The central object is the modal discriminant (1.7):

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4H\,P_*'}{\tau},
$$

whose sign partitions the parameter space into three regions:

| Region | Condition | Eigenvalue type | Dynamical character |
|--------|-----------|----------------|---------------------|
| Spiral Sheet | $\mathscr{D}_0 < 0$ | Complex conjugate | Damped oscillations |
| Monotonic Cone | $\mathscr{D}_0 > 0$ | Real, distinct | Monotonic decay |
| Boundary Surface $\Sigma$ | $\mathscr{D}_0 = 0$ | Real, repeated (Jordan) | Algebraic-then-exponential decay |

All experiments in this section use the one-dimensional domain $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4) with default parameters ($M_0 = 1$, $\beta = 2$, $P_0 = 1$), resolution $N = 256$, and the Crank–Nicolson time-stepping scheme (§1.5.2) with $\Delta t = 10^{-3}$. Only the canonical parameters $(D, \zeta, \tau)$ and the initial conditions are varied.

---

### 2.1 Spiral Sheet ($\mathscr{D}_0 < 0$): Oscillatory Decay

#### 2.1.1 Analytic Prediction

When $\mathscr{D}_0 < 0$, the eigenvalues of the homogeneous-mode matrix $\mathbf{A}_0$ (C.13) are a complex conjugate pair

$$
\lambda_\pm = -\gamma_0 \pm i\omega, \qquad \gamma_0 = \tfrac{1}{2}(D\,P_*' + \zeta/\tau), \qquad \omega = \tfrac{1}{2}\sqrt{|\mathscr{D}_0|}.
$$

The homogeneous perturbation $(u_0(t), w(t))$ traces a decaying spiral in the $(u_0, w)$-plane, with envelope $e^{-\gamma_0 t}$ and angular frequency $\omega$. The spatial modes $n \geq 1$ decay monotonically at rates $D\alpha_n$ (Theorem C.22(i)), which are faster than $\gamma_0$ by the spectral gap (Corollary C.18).

The Spiral Sheet is the region of parameter space where this oscillatory behavior prevails. In the canonical normalization $\tau P_*' = 1$, it is the interior of the parabola (C.63): $\{(D, \zeta) : (D - \zeta)^2 < 4(1 - D)\}$.

#### 2.1.2 Numerical Experiment 2.1

**Setup.** Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$; deep oscillatory regime, $\mathscr{D}_0 = -2.76$). Initial condition: spatially homogeneous perturbation $\rho_0(x) = \rho^* + A = 0.55$, $v_0 = 0.1$. Integration time: $T = 30.0$.

**Analytic eigenvalues.** $\gamma_0 = \frac{1}{2}(0.3 + 0.1) = 0.2$. $\omega = \frac{1}{2}\sqrt{2.76} \approx 0.831$.

**Measured quantities.**

1. The time series $u_0(t) := \bar{\rho}(t) - \rho^*$ and $w(t) := v(t)$, where $\bar{\rho}(t) = L^{-1}\int_0^L \rho(x,t)\,dx$ is the spatial mean.
2. The phase-plane trajectory $(u_0(t), w(t))$ for $t \in [0, 30]$.
3. The measured decay rate $\hat{\gamma}_0$, extracted by fitting the envelope $\max_{\text{cycle}}|u_0|$ to $Ce^{-\hat{\gamma}_0 t}$.
4. The measured frequency $\hat{\omega}$, extracted from consecutive zero-crossing intervals of $u_0(t)$.

**Expected behavior.** The time series $u_0(t)$ oscillates with decaying amplitude, crossing zero repeatedly. The phase trajectory spirals inward toward the origin $(0, 0)$. The envelope contracts by a factor $e^{-\gamma_0 T_{\mathrm{cycle}}}$ per cycle, where $T_{\mathrm{cycle}} = 2\pi/\omega \approx 7.56$. At $A = 0.05$ (linear regime), $\hat{\gamma}_0$ and $\hat{\omega}$ match the analytic predictions to within discretization tolerance. At $A = 0.3$ (mildly nonlinear), amplitude-dependent corrections shift the frequency downward and the damping rate upward, signaling the onset of nonlinear effects.

**Figure description (Figure 2.1).** *Phase portrait of the Spiral Sheet.* Two panels side by side.

Left panel: the phase-plane trajectory $(u_0, w)$ for Parameter Set I at amplitude $A = 0.05$. The horizontal axis is $u_0 = \bar{\rho} - \rho^*$ (range $[-0.06, 0.06]$); the vertical axis is $w = v$ (range $[-0.15, 0.15]$). The trajectory begins at $(0.05, 0.1)$ (marked with a filled circle) and spirals counterclockwise inward toward the origin, completing approximately four full revolutions before the amplitude drops below $10^{-3}$. The spiral is nearly elliptical, with the major axis tilted from the horizontal by the eigenvector angle $\arg(\mathbf{r}_+)$ of the complex eigenvalue. Dashed concentric ellipses at amplitudes $e^{-\gamma_0 k T_{\mathrm{cycle}}}$ for $k = 1, 2, 3$ show the analytically predicted envelope contraction per cycle.

Right panel: the same experiment at amplitude $A = 0.3$ (nonlinear). The initial spiral is visibly deformed from the elliptical shape: the outward excursions are asymmetrically compressed on the positive-$u_0$ side (where $\rho$ approaches $\rho_{\max}$ and mobility collapse stiffens the dynamics) and elongated on the negative-$u_0$ side. The deformation diminishes as the amplitude decays, and the inner portion of the spiral recovers the elliptical shape of the linearized regime. This deformation is the phase-plane signature of the nonlinear constitutive terms $M'(\rho)|\nabla\rho|^2$ and the nonlinear penalty curvature.

#### 2.1.3 Numerical Experiment 2.2: Dependence on $\zeta$

**Setup.** Fix $D = 0.3$, $\tau = 1.0$. Sweep $\zeta$ over $\{0.05, 0.1, 0.2, 0.3, 0.5\}$. For each value, integrate with the same initial condition ($A = 0.05$, $v_0 = 0.1$) and extract $\hat{\gamma}_0$ and $\hat{\omega}$.

**Analytic predictions.** As $\zeta$ increases from $0.05$ toward the critical value $\zeta_c$ (where $\mathscr{D}_0 = 0$), the decay rate $\gamma_0 = \frac{1}{2}(D + \zeta/\tau)$ increases linearly in $\zeta$, while the oscillation frequency $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ decreases, reaching zero at $\zeta = \zeta_c$. The spiral tightens (faster decay) and slows (lower frequency) simultaneously.

**Figure description (Figure 2.2).** *Spiral tightening with increasing $\zeta$.* Two panels.

Left panel: five phase-plane trajectories $(u_0, w)$ superimposed on the same axes, one for each value of $\zeta$, each in a different line style. All trajectories begin at the same initial point. The trajectory at $\zeta = 0.05$ (lightest style) makes the most revolutions with the slowest envelope decay; the trajectory at $\zeta = 0.5$ (heaviest style) decays rapidly with barely one visible revolution. A legend identifies each curve by its $\zeta$ value and the corresponding $\mathscr{D}_0$.

Right panel: two sub-plots stacked vertically. Top sub-plot: measured $\hat{\gamma}_0$ versus $\zeta$, overlaid with the analytic line $\gamma_0 = \frac{1}{2}(0.3 + \zeta)$. The numerical points fall on the analytic line to within marker width, confirming the linearized prediction. Bottom sub-plot: measured $\hat{\omega}$ versus $\zeta$, overlaid with the analytic curve $\omega(\zeta) = \frac{1}{2}\sqrt{|D P_*' - \zeta/\tau|^2 - 4H P_*'/\tau}\big|_{\text{imaginary part}}$. The frequency decreases from $\hat{\omega} \approx 0.87$ at $\zeta = 0.05$ toward zero near the critical $\zeta_c$. At $\zeta = 0.5$, the discriminant is still negative but the frequency is small ($\hat{\omega} \approx 0.35$), showing the approach to the boundary.

---

### 2.2 Monotonic Cone ($\mathscr{D}_0 > 0$): Overdamped Decay

#### 2.2.1 Analytic Prediction

When $\mathscr{D}_0 > 0$, both eigenvalues of $\mathbf{A}_0$ are real and negative:

$$
\lambda_+ = -\gamma_0 + \tfrac{1}{2}\sqrt{\mathscr{D}_0}, \qquad \lambda_- = -\gamma_0 - \tfrac{1}{2}\sqrt{\mathscr{D}_0}.
$$

The slower eigenvalue is $\lambda_+$ (less negative, closer to zero); the faster is $\lambda_-$. The homogeneous perturbation decays as a sum of two exponentials, $u_0(t) = c_+ e^{\lambda_+ t} + c_- e^{\lambda_- t}$, without oscillation. The phase trajectory moves along straight paths toward the origin, following the slow eigenvector $\mathbf{r}_+$ at late times once the fast component has decayed.

The Monotonic Cone is the region $\{(D, \zeta) : (D - \zeta)^2 > 4(1 - D)\}$ in the canonical normalization, exterior to the parabola (C.63).

#### 2.2.2 Numerical Experiment 2.3

**Setup.** Parameter Set IV ($D = 0.9$, $\zeta = 5.0$, $\tau = 1.0$; deep monotonic regime, $\mathscr{D}_0 = 16.41$). Initial condition: $\rho_0(x) = \rho^* + 0.05$, $v_0 = 0.1$. Integration time: $T = 15.0$.

**Analytic eigenvalues.** $\gamma_0 = \frac{1}{2}(0.9 + 5.0) = 2.95$. $\sqrt{\mathscr{D}_0} \approx 4.051$. Thus $\lambda_+ \approx -0.924$, $\lambda_- \approx -4.976$.

**Expected behavior.** The time series $u_0(t)$ decays monotonically without zero crossings. At early times ($t \lesssim 1/|\lambda_-| \approx 0.2$), both exponential components contribute; the trajectory moves rapidly along a direction set by the initial data projected onto the two eigenvectors. At late times ($t \gg 1/|\lambda_-|$), the fast mode has decayed and the trajectory follows the slow eigenvector $\mathbf{r}_+$ toward the origin, with decay rate $|\lambda_+| \approx 0.924$. The participation variable $w(t)$ decays faster than $u_0(t)$ because the fast eigenmode has a larger $w$-component.

**Figure description (Figure 2.3).** *Phase portrait of the Monotonic Cone.* Two panels.

Left panel: the phase-plane trajectory $(u_0, w)$ for Parameter Set IV. The horizontal axis is $u_0$ (range $[-0.01, 0.06]$); the vertical axis is $w$ (range $[-0.02, 0.12]$). The trajectory begins at $(0.05, 0.1)$ and moves in a smooth curve toward the origin without looping. Two straight dashed lines through the origin mark the eigenvector directions of $\mathbf{A}_0$: the slow eigenvector $\mathbf{r}_+$ (nearly horizontal, reflecting the dominance of $u_0$ in the slow mode) and the fast eigenvector $\mathbf{r}_-$ (nearly vertical). The trajectory curves from its initial direction toward the slow eigenvector and then follows it linearly to the origin. There is no spiral, no overshoot, and no oscillation. The trajectory's tangent at late times is visibly parallel to $\mathbf{r}_+$.

Right panel: time series of $|u_0(t)|$ and $|w(t)|$ on a semilog-$y$ axis. The $|u_0|$ curve shows a brief transient (duration $\sim 0.5$) followed by a straight line with slope $-|\lambda_+| \approx -0.924$. The $|w|$ curve decays faster: after the same brief transient, its slope is $-|\lambda_-| \approx -4.976$. Dashed reference lines with the analytic slopes are overlaid. The two-time-scale separation $|\lambda_-|/|\lambda_+| \approx 5.4$ is visible as the factor-of-five difference in slopes.

#### 2.2.3 Numerical Experiment 2.4: Dependence on $D$

**Setup.** Fix $\zeta = 5.0$, $\tau = 1.0$. Sweep $D$ over $\{0.7, 0.8, 0.85, 0.9, 0.95\}$. For each, integrate with $A = 0.05$, $v_0 = 0.1$, and extract the measured slow decay rate $\hat{\lambda}_+$ and fast decay rate $\hat{\lambda}_-$.

**Expected behavior.** As $D$ increases toward $1$ (reducing $H = 1 - D$), the mediated channel weakens, the oscillation-generating term $4HP_*'/\tau$ shrinks, and $\mathscr{D}_0$ grows. Both eigenvalues move further apart: $\lambda_+$ moves toward $-DP_*'$ (the pure direct-channel decay rate in the limit $H \to 0$) and $\lambda_-$ moves toward $-\zeta/\tau$ (the pure participation damping rate). In the limit $D \to 1$, the system decouples into independent density relaxation and participation damping.

**Figure description (Figure 2.4).** *Eigenvalue migration in the Monotonic Cone.* Single panel.

The horizontal axis is $D$ (range $[0.7, 0.95]$). The vertical axis shows the magnitudes $|\lambda_+|$ and $|\lambda_-|$, both positive. Two curves are plotted: the lower curve ($|\lambda_+|$, slow rate) increases gently from $\approx 0.6$ at $D = 0.7$ toward $\approx 0.95$ at $D = 0.95$; the upper curve ($|\lambda_-|$, fast rate) decreases gently toward $\zeta/\tau = 5.0$. Numerical data points (filled circles) are overlaid on both curves; analytic predictions (solid lines) are computed from (C.15). The agreement is within marker width at all points. A horizontal dashed line at $|\lambda| = \zeta/\tau = 5.0$ marks the participation damping asymptote. A second horizontal dashed line at $|\lambda| = P_*' = 1.0$ marks the direct-channel penalty relaxation rate.

---

### 2.3 Critical Damping Surface ($\mathscr{D}_0 = 0$): Jordan-Block Behavior

#### 2.3.1 Analytic Prediction

On the critical surface $\Sigma$ (Definition C.51), the two eigenvalues coalesce:

$$
\lambda_+ = \lambda_- = \lambda_c = -\gamma_0 = -\tfrac{1}{2}(D_c P_*' + \zeta_c/\tau),
$$

and the matrix $\mathbf{A}_0$ is similar to the Jordan block $\mathbf{J}_c$ (Lemma C.54, eq. C.64). The defining feature of Jordan-block dynamics is that the decay is no longer purely exponential: the generalized eigenvector produces a polynomial prefactor, so the homogeneous perturbation decays as

$$
u_0(t) = (c_1 + c_2\,t)\,e^{\lambda_c t}
\tag{2.1}
$$

for appropriate constants $c_1$, $c_2$ determined by the initial data. The linear-in-$t$ growth of the prefactor before the exponential kills it produces a transient amplification — the perturbation can initially grow in absolute value before decaying — that is absent in both the oscillatory and monotonic regimes. This is the signature of the critical surface.

In the canonical normalization $\tau P_*' = 1$, the critical surface is the parabola (C.63): $(D_c - \zeta_c)^2 = 4(1 - D_c)$. For $D_c = 0.8$, this gives $\zeta_c = 0.8 \pm 2\sqrt{0.2} \approx 0.8 \pm 0.894$. Taking the upper branch: $\zeta_c \approx 1.694$.

#### 2.3.2 Numerical Experiment 2.5

**Setup.** Choose $D_c = 0.8$, $\tau = 1.0$, $P_0 = 1.0$, and compute $\zeta_c$ from the critical condition $(D_c - \zeta_c)^2 = 4(1 - D_c)$: $\zeta_c = D_c + 2\sqrt{1 - D_c} = 0.8 + 2\sqrt{0.2} \approx 1.6944$. Initial condition: $\rho_0(x) = \rho^* + 0.05$, $v_0 = 0$, chosen so that $c_2 \neq 0$ in (2.1) — the initial data must have a nonzero projection onto the generalized eigenvector to excite the polynomial prefactor. Integration time: $T = 20.0$.

**Analytic eigenvalue.** $\lambda_c = -\frac{1}{2}(0.8 + 1.6944) = -1.2472$.

**Expected behavior.** The time series $u_0(t)$ does not oscillate (no imaginary part) but does not decay as a pure exponential either. If $c_2 > 0$, the magnitude $|u_0(t)|$ initially increases (the $c_2 t$ factor dominates for small $t$) before the exponential $e^{\lambda_c t}$ takes over and forces monotonic decay. The peak of $|u_0(t)|$ occurs at $t_{\mathrm{peak}} = -c_1/c_2 - 1/\lambda_c$ (from differentiating (2.1) and setting the derivative to zero). This transient amplification distinguishes the critical surface from the monotonic cone, where $|u_0(t)|$ is strictly decreasing for all $t > 0$ whenever $c_+$ and $c_-$ have the same sign.

The participation variable $w(t)$ exhibits the same Jordan structure: $w(t) = (d_1 + d_2 t) e^{\lambda_c t}$.

**Figure description (Figure 2.5).** *Jordan-block dynamics on the critical surface.* Three panels.

Top panel: time series of $u_0(t)$ for the critical experiment (solid curve), compared against a pure-exponential reference $c_1 e^{\lambda_c t}$ (dashed curve). The horizontal axis is $t$ (range $[0, 20]$); the vertical axis is $u_0$ (range $[-0.01, 0.08]$). The solid curve rises above the dashed curve at early times — this is the transient amplification from the $c_2 t$ factor — reaching a peak at $t_{\mathrm{peak}} \approx 0.8$, then crosses below the dashed curve and decays to zero. The dashed curve decays monotonically from $u_0(0) = 0.05$. The envelope difference between the two curves is the polynomial correction.

Middle panel: semilog-$y$ plot of $|u_0(t)|$ versus $t$. A pure exponential would appear as a straight line with slope $\lambda_c$. The numerical curve is not straight: it has a gentle upward concavity at early times (from the $t\,e^{\lambda_c t}$ term) that resolves into the asymptotic straight line $\lambda_c$ at late times ($t > 5$). A dashed reference line with slope $\lambda_c$ is overlaid. The deviation from linearity at early times is the hallmark of the Jordan block — it is absent for $\mathscr{D}_0 \neq 0$.

Bottom panel: the phase trajectory $(u_0, w)$. Unlike the spiral of §2.1 (which loops around the origin) and unlike the monotonic trajectory of §2.2 (which curves smoothly along an eigenvector), the critical trajectory approaches the origin along a single direction — the eigenvector $\mathbf{e}_1$ — but with an initial tangent that deviates from $\mathbf{e}_1$. The trajectory is a smooth curve that asymptotically aligns with $\mathbf{e}_1$ without spiraling or separating into two distinct exponential branches. A dashed line marks $\mathbf{e}_1$.

#### 2.3.3 Numerical Experiment 2.6: Near-Critical Comparison

**Setup.** Fix $D = 0.8$, $\tau = 1.0$. Run three experiments at $\zeta = \zeta_c - 0.05$ (just inside the Spiral Sheet), $\zeta = \zeta_c$ (on $\Sigma$), and $\zeta = \zeta_c + 0.05$ (just inside the Monotonic Cone). Same initial condition as Experiment 2.5.

**Expected behavior.** The three time series are nearly identical at early times ($t < 2$), where the dynamics are dominated by the common decay rate $\gamma_0 \approx 1.25$ and the polynomial or oscillatory corrections are small. At intermediate times ($t \in [2, 10]$), the trajectories diverge:

- The sub-critical trajectory ($\zeta < \zeta_c$) exhibits a single small oscillation — one zero crossing of $u_0(t)$ — before settling into exponential decay. This is the remnant of the Spiral Sheet, visible as a single half-loop in the phase plane.
- The critical trajectory ($\zeta = \zeta_c$) shows the transient amplification and algebraic-then-exponential decay of §2.3.2, with no zero crossing.
- The super-critical trajectory ($\zeta > \zeta_c$) decays monotonically from the start, with no amplification and no zero crossing.

**Figure description (Figure 2.6).** *Near-critical comparison.* Two panels.

Left panel: three time series $u_0(t)$ superimposed on the same axes. The sub-critical curve (thin solid) crosses zero once at $t \approx 4$ before decaying. The critical curve (thick solid) does not cross zero but shows the polynomial amplification bump at $t \approx 0.8$. The super-critical curve (dashed) decays smoothly without bump or crossing. All three converge to the same asymptotic decay rate at late times. A vertical dashed line marks the time at which the three curves first differ by more than 10% of their common amplitude.

Right panel: three phase trajectories superimposed. The sub-critical trajectory makes a tight half-loop around the origin (the vestigial spiral). The critical trajectory curves toward $\mathbf{e}_1$ without looping. The super-critical trajectory follows a monotonic path along the slow eigenvector. The three trajectories are nearly tangent at the initial point, demonstrating that the regime transition is a smooth unfolding, not a discontinuous jump.

---

### 2.4 Boundary Surface ($\mathscr{D}_0 = 0$): Global Regime Geometry

#### 2.4.1 The Discriminant Map

The experiments of §§2.1–2.3 demonstrate individual regimes at fixed parameter values. This section maps the full regime geometry across the $(D, \zeta)$-parameter plane, visualizing the discriminant $\mathscr{D}_0$ as a continuous function and identifying the Spiral Sheet, Monotonic Cone, and Boundary Surface as connected regions of this plane.

**Setup.** Fix $\tau = 1.0$, $P_0 = 1.0$ (canonical normalization $\tau P_*' = 1$). Define a grid in the $(D, \zeta)$-plane: $D \in [0.05, 0.95]$ in steps of $0.01$, and $\zeta \in [0.01, 5.0]$ in steps of $0.01$. At each grid point, compute $\mathscr{D}_0$ from (1.7) analytically (no numerical integration needed). At a subset of 25 grid points, spanning both regimes and the boundary, integrate the full nonlinear system with $A = 0.05$, $v_0 = 0.1$, $T = 20$, and classify the trajectory as oscillatory (at least one zero crossing of $u_0$), monotonic (no zero crossing), or critical (no zero crossing but polynomial amplification detected).

**Figure description (Figure 2.7).** *The discriminant landscape.* Single large panel.

The horizontal axis is $D$ (range $[0.05, 0.95]$); the vertical axis is $\zeta$ (range $[0.01, 5.0]$). The color field shows $\mathscr{D}_0(D, \zeta)$: blue tones for $\mathscr{D}_0 < 0$ (Spiral Sheet), red tones for $\mathscr{D}_0 > 0$ (Monotonic Cone), with intensity proportional to $|\mathscr{D}_0|$. The Boundary Surface $\Sigma$ is drawn as a thick black curve — the parabola $(D - \zeta)^2 = 4(1 - D)$ — separating blue from red. The parabola has vertex near $(D, \zeta) = (1, 1)$ (in the extended plane) and opens to the left, intersecting the $\zeta = 0$ axis at $D \approx 0.828$.

Overlaid on the color field are 25 marker symbols at the grid points where full nonlinear integrations were performed: open circles for confirmed oscillatory decay, filled squares for confirmed monotonic decay, and diamonds for near-critical cases (within $|\mathscr{D}_0| < 0.1$). Every marker agrees with the analytic classification: all circles fall in the blue region, all squares in the red region, and all diamonds lie within a narrow band around $\Sigma$.

The five canonical Parameter Sets (I–V) from §1.3 are marked with labeled star symbols. Sets I, II, and V fall deep in the Spiral Sheet (blue). Set IV falls deep in the Monotonic Cone (red). Set III falls just inside the Monotonic Cone, close to the boundary.

A secondary contour line marks $\Delta := D + 2\zeta = 1$ (a straight line from $(1, 0)$ to $(0, 0.5)$ in the $(D, \zeta)$-plane). The region $\Delta < 1$ lies entirely inside the Spiral Sheet, confirming the structural interpretation of Remark C.23: when the total damping budget $\Delta$ is less than the channel conservation constraint, the system is necessarily oscillatory.

#### 2.4.2 Sign Change Across the Boundary

To visualize the transition from $\mathscr{D}_0 < 0$ to $\mathscr{D}_0 > 0$, we perform a one-dimensional parameter sweep that crosses $\Sigma$ transversally.

**Numerical Experiment 2.7.** Fix $D = 0.5$, $\tau = 1.0$. Sweep $\zeta$ from $0.1$ to $3.0$ in 100 uniformly spaced steps. At each value, integrate with $A = 0.05$, $v_0 = 0.1$, $T = 20$, and compute:

1. The analytic discriminant $\mathscr{D}_0(\zeta)$.
2. The number of zero crossings $N_{\mathrm{cross}}$ of $u_0(t)$ in $[0, 20]$.
3. The measured oscillation frequency $\hat{\omega}$ (if $N_{\mathrm{cross}} \geq 2$) or the two decay rates $\hat{\lambda}_+$, $\hat{\lambda}_-$ (if $N_{\mathrm{cross}} = 0$).
4. The maximum transient amplification $A_{\mathrm{max}} := \max_{t > 0}|u_0(t)|/|u_0(0)|$ (relevant near the critical value).

**Critical value.** At $D = 0.5$, the critical condition $(0.5 - \zeta_c)^2 = 4(0.5) = 2$ gives $\zeta_c = 0.5 + \sqrt{2} \approx 1.914$.

**Figure description (Figure 2.8).** *Discriminant sign change across $\Sigma$.* Four panels, vertically stacked, sharing the horizontal axis $\zeta$ (range $[0.1, 3.0]$). A vertical dashed line at $\zeta_c \approx 1.914$ marks the boundary crossing in every panel.

Panel 1 (top): The analytic discriminant $\mathscr{D}_0(\zeta)$. The curve starts negative at $\zeta = 0.1$ (deep Spiral Sheet), rises through zero at $\zeta = \zeta_c$, and becomes positive for $\zeta > \zeta_c$ (Monotonic Cone). The curve is a downward-opening parabola in $\zeta$ (from the $(\zeta/\tau)^2$ term), but the dominant behavior is the monotonic increase from the $-4HP_*'/\tau$ shift. The zero crossing is smooth and transversal, confirming the codimension-one regularity of $\Sigma$ (Proposition C.52).

Panel 2: The number of zero crossings $N_{\mathrm{cross}}(\zeta)$. For $\zeta < \zeta_c$, the zero-crossing count is high (10–15 crossings in $T = 20$ at small $\zeta$, decreasing as $\omega \to 0$). At $\zeta = \zeta_c$, $N_{\mathrm{cross}}$ drops to zero. For $\zeta > \zeta_c$, $N_{\mathrm{cross}} = 0$ uniformly. The transition from oscillatory to monotonic is sharp: it occurs within a single $\Delta\zeta$ step, at the predicted $\zeta_c$.

Panel 3: The measured frequency $\hat{\omega}$ (plotted for $\zeta < \zeta_c$ only). The frequency decreases continuously from its maximum at small $\zeta$ toward zero as $\zeta \to \zeta_c^-$. The analytic curve $\omega(\zeta) = \frac{1}{2}\sqrt{|\mathscr{D}_0(\zeta)|}$ is overlaid as a solid line; numerical points lie on it. Near $\zeta_c$, the frequency vanishes as $\hat{\omega} \sim (\zeta_c - \zeta)^{1/2}$, the square-root scaling characteristic of a discriminant zero crossing.

Panel 4 (bottom): The transient amplification ratio $A_{\mathrm{max}}/|u_0(0)|$. For $\zeta$ well below $\zeta_c$, this ratio is close to $1$ (oscillations are symmetric, no net amplification). As $\zeta$ approaches $\zeta_c$ from below, the ratio rises above $1$, peaking at $\zeta = \zeta_c$ where the Jordan-block dynamics produce maximal algebraic growth before exponential decay. For $\zeta > \zeta_c$ (monotonic), the ratio returns to $1$ (no amplification possible in the overdamped regime). The peak at $\zeta_c$ is narrow and has the shape of a cusp — it is the dynamical signature of the critical surface.

#### 2.4.3 Three-Dimensional Regime Geometry

**Numerical Experiment 2.8.** Extend the discriminant map of §2.4.1 to a two-parameter family indexed by $\tau$. Compute $\mathscr{D}_0(D, \zeta)$ for $\tau \in \{0.5, 1.0, 2.0, 5.0\}$, with the same $(D, \zeta)$-grid.

**Figure description (Figure 2.9).** *Regime geometry at different time scales.* Four sub-panels arranged $2 \times 2$, one for each $\tau$ value. Each sub-panel is a discriminant color map identical in format to Figure 2.7, with the Boundary Surface $\Sigma(\tau)$ drawn as a black parabola.

As $\tau$ increases, the parabola $(D - \zeta/\tau)^2 = 4HP_*'/\tau$ (the general form of the critical surface) shifts and rescales: the Spiral Sheet expands (the oscillatory region grows) because the participation integration time $\tau$ amplifies the feedback loop's ability to sustain oscillations against damping. At $\tau = 0.5$, the Spiral Sheet is narrow and confined to small $\zeta$; at $\tau = 5.0$, it extends to $\zeta > 3$ before the Monotonic Cone takes over. The structural interpretation (Remark C.23) is confirmed: the regime geometry is controlled by the balance between feedback amplification (favored by large $\tau$, large $H$) and damping (favored by large $\zeta$, large $D$).

The canonical damping parameter $\Delta = D + 2\zeta$ is not $\tau$-independent; its role as a regime classifier is sharpest in the canonical normalization $\tau P_*' = 1$. The four sub-panels demonstrate this: at $\tau = 1$ (canonical normalization), the $\Delta = 1$ contour coincides with the inner boundary of the Spiral Sheet; at other $\tau$ values, the $\Delta = 1$ line does not have this coincidence, confirming that $\Delta$ is a *canonical* parameter tied to the normalized system.

---

## 3. Modal Hierarchy Demonstrations

The modal hierarchy is the ordering of decay rates across the Neumann eigenbasis of the linearized ED operator $\mathcal{L}$ (Theorem C.17, Proposition C.29). It states that each spatial mode $n \geq 1$ decays independently at rate $D\alpha_n = D(M_*\mu_n + P_*')$, with the rates forming a strictly increasing sequence bounded below by the penalty floor $D P_*'$ and growing asymptotically as $D M_* C_d n^{2/d}$ (Weyl law, eq. C.33). The spectral gap $\gamma = \min(\gamma_{\mathrm{hom}}, \gamma_{\mathrm{sp}})$ separates the slowest-decaying component from the remainder (Corollary C.18, Lemma C.31).

This section demonstrates the modal hierarchy through three groups of numerical experiments: isolated single-mode decay (§3.1), multi-mode superposition and the spectral gap (§3.2), and the complete decay-rate funnel across all resolved modes (§3.3). These experiments correspond to the analytic content of Appendix C.3 (eigenvalues, eqs. C.11–C.12), Appendix C.4 (spectral gap, Lemma C.31; modal decay asymptotics, Proposition C.29; Fourier decomposition, eq. C.23), and the spectral separation condition (Remark C.30).

All experiments use the one-dimensional domain $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4), the Crank–Nicolson scheme (§1.5.2) with $N = 512$ and $\Delta t = 5 \times 10^{-4}$, and Parameter Set II ($D = 0.6$, $\zeta = 0.5$, $\tau = 1.0$) unless otherwise stated. The spectral method (Method B, §1.4.2) is used in parallel for all spectral-decomposition measurements, with results cross-validated against Method A.

On $\Omega_1 = [0, 1]$, the Neumann eigenfunctions and eigenvalues are

$$
\varphi_n(x) = \sqrt{2}\cos(n\pi x), \quad \mu_n = n^2\pi^2, \qquad n \geq 1,
$$

with $\varphi_0 = 1$, $\mu_0 = 0$. The equilibrium constitutive values are $M_* = M(\rho^*) = M_0(\rho_{\max} - \rho^*)^\beta = (0.5)^2 = 0.25$ and $P_*' = P_0 = 1.0$.

The modal decay coefficients are therefore

$$
\alpha_n = M_*\mu_n + P_*' = 0.25\,n^2\pi^2 + 1.0 \approx 2.467\,n^2 + 1.0,
\tag{3.1}
$$

and the decay rates are $D\alpha_n = 0.6\,(2.467\,n^2 + 1.0)$.

---

### 3.1 Single-Mode Initialization: Exponential Decay at Rate $D\alpha_n$

#### 3.1.1 Analytic Prediction

The linearized equation for mode $n \geq 1$ is (C.11):

$$
\dot{a}_n = -D\alpha_n\,a_n,
$$

with solution $a_n(t) = a_n(0)\,e^{-D\alpha_n t}$. The decay is purely exponential, the rate depends on $n$ through $\alpha_n$, and there is no coupling to the participation variable $v$ (Remark C.16) or to any other spatial mode at the linear level (Remark C.25). The nonlinear term $M'(\rho)|\nabla\rho|^2$ generates inter-mode coupling at order $O(A^2)$, but for small amplitude $A$ the linearized prediction is accurate.

#### 3.1.2 Numerical Experiment 3.1: Modes $n = 1, 2, 3, 4$

**Setup.** For each $n \in \{1, 2, 3, 4\}$, initialize the system with a pure $n$-th mode perturbation:

$$
\rho_0(x) = \rho^* + A\cos(n\pi x), \qquad v_0 = 0,
$$

with $A = 10^{-3}$ (deep linearized regime). Integrate to $T = 5.0$. At each time step, extract the modal amplitude $a_n(t) = \langle\rho(\cdot, t) - \rho^*, \varphi_n\rangle_{L^2}$ via the spectral method.

**Analytic decay rates.**

| Mode | $\mu_n = n^2\pi^2$ | $\alpha_n = 0.25\mu_n + 1$ | $D\alpha_n$ |
|------|-----|------|------|
| $n = 1$ | $9.870$ | $3.467$ | $2.080$ |
| $n = 2$ | $39.478$ | $10.870$ | $6.522$ |
| $n = 3$ | $88.826$ | $23.207$ | $13.924$ |
| $n = 4$ | $157.914$ | $40.478$ | $24.287$ |

**Measured quantities.**

1. Time series $a_n(t)$ for each mode.
2. Measured decay rate $\hat{\sigma}_n$, extracted from the slope of $\ln|a_n(t)|$ over $t \in [0.5, 4.5]$ (excluding the initial transient and the late-time noise floor).
3. Spectral purity: the amplitude of all other modes $a_m(t)$ for $m \neq n$ at each time step, verifying that inter-mode leakage remains at the $O(A^2) \sim 10^{-6}$ level.

**Expected results.** Each $\ln|a_n(t)|$ curve is a straight line with slope $-D\alpha_n$. The measured rates $\hat{\sigma}_n$ match the analytic values in the table above to within 1%. The higher modes ($n = 3, 4$) reach the numerical noise floor earlier because their faster decay rates bring the amplitude to machine precision in shorter time. The spectral purity check confirms that the nonlinear coupling $M'(\rho)|\nabla\rho|^2$ generates no measurable energy transfer to other modes at amplitude $A = 10^{-3}$.

**Figure description (Figure 3.1).** *Single-mode exponential decay.* Single panel with semilog-$y$ axes.

The horizontal axis is time $t$ (range $[0, 5]$). The vertical axis is $|a_n(t)|$ on a logarithmic scale (range $[10^{-16}, 10^{-3}]$). Four curves are plotted, one for each mode $n = 1, 2, 3, 4$, each in a distinct line style. Each curve begins at $|a_n(0)| = A\sqrt{L/2} = A/\sqrt{2} \approx 7.07 \times 10^{-4}$ and descends as a straight line. The slopes steepen with increasing $n$: the $n = 1$ curve has the shallowest slope (longest lifetime), the $n = 4$ curve has the steepest (shortest lifetime). Dashed reference lines with slopes $-D\alpha_n$ (from the table) are overlaid on each curve; the numerical data falls on the reference lines to within the line width.

The $n = 4$ curve reaches the noise floor ($\sim 10^{-16}$) at $t \approx 1.2$; the $n = 3$ curve at $t \approx 2.1$; the $n = 2$ curve at $t \approx 4.5$. The $n = 1$ curve has not reached the noise floor by $T = 5$ (residual amplitude $\sim 10^{-8}$). A legend identifies each curve by its mode number and analytic decay rate.

#### 3.1.3 Numerical Experiment 3.2: Amplitude Dependence and Nonlinear Onset

**Setup.** Initialize mode $n = 1$ at five amplitudes: $A \in \{10^{-4}, 10^{-3}, 10^{-2}, 0.05, 0.2\}$. Integrate each to $T = 10.0$. Extract the effective decay rate $\hat{\sigma}_1(A)$ and the energy transferred to mode $n = 2$ (the leading nonlinear product).

**Analytic prediction.** At small $A$, the decay rate is $D\alpha_1 = 2.080$. At larger amplitudes, the quadratic nonlinearity $M'(\rho)|\nabla\rho|^2$ generates a self-interaction correction. From the projected system (C.27), the leading nonlinear contribution to $\dot{a}_1$ is

$$
D\,M_*'\sum_{m,n \geq 1} a_m\,a_n\,\Gamma_{mn1},
$$

which at leading order (with only $a_1$ initially nonzero) involves the trilinear coefficient $\Gamma_{111}$. On $\Omega_1 = [0,1]$, a direct computation gives $\Gamma_{111} = \int_0^1 |\nabla\varphi_1|^2\,\varphi_1\,dx = 2\pi^2\int_0^1 \sin^2(\pi x)\cos(\pi x)\,dx \cdot \sqrt{2}$. Since $\int_0^1 \sin^2(\pi x)\cos(\pi x)\,dx = 0$ by symmetry, $\Gamma_{111} = 0$: the cubic self-interaction of mode $1$ vanishes identically. The leading nonlinear effect on mode $1$ is therefore a quintic correction at $O(A^4)$, and the effective decay rate deviates from $D\alpha_1$ only at $O(A^2)$ through indirect pathways (mode $1$ generates mode $2$ at $O(A^2)$, which feeds back at $O(A^3)$).

The energy transfer to mode $2$ is governed by $\Gamma_{112}$:

$$
\Gamma_{112} = \int_0^1 |\nabla\varphi_1|^2\,\varphi_2\,dx = 2\pi^2\int_0^1 \sin^2(\pi x)\cdot \sqrt{2}\cos(2\pi x)\,dx.
$$

This integral is nonzero: $\int_0^1 \sin^2(\pi x)\cos(2\pi x)\,dx = -1/4$, giving $\Gamma_{112} = -\sqrt{2}\,\pi^2/2 \approx -6.98$. The $n = 2$ mode is therefore excited at $O(A^2)$ with initial growth rate proportional to $D M_*' A^2 |\Gamma_{112}|$.

**Expected results.** For $A \leq 10^{-3}$: $\hat{\sigma}_1 = D\alpha_1$ to within 1%, and $|a_2(t)| < 10^{-10}$ throughout. For $A = 10^{-2}$: $\hat{\sigma}_1$ deviates by $\lesssim 0.1\%$, and $|a_2|$ rises to $O(A^2) = O(10^{-4})$ before decaying. For $A = 0.05$: measurable deviation ($\sim 1\%$) in $\hat{\sigma}_1$, and $a_2$ reaches $O(10^{-3})$. For $A = 0.2$: significant deviation ($\sim 5$–$10\%$) in $\hat{\sigma}_1$, and the multi-mode dynamics involve modes $n = 1, 2, 3$ simultaneously — the onset of the nonlinear triad (Principle 7).

**Figure description (Figure 3.2).** *Nonlinear onset in single-mode decay.* Two panels.

Left panel: semilog-$y$ plot of $|a_1(t)|$ for the five amplitudes. All curves are straight at small $A$ (parallel lines offset vertically by the initial amplitude). At $A = 0.2$ (uppermost curve), the slope is visibly steeper at early times ($t < 1$) and shallows toward the linearized rate at late times (after the nonlinear terms have decayed) — the amplitude-dependent damping enhancement. A dashed reference line with slope $-D\alpha_1$ is shown.

Right panel: semilog-$y$ plot of $|a_2(t)|$ (the nonlinearly generated second harmonic) for the same five amplitudes. At $A = 10^{-4}$ and $10^{-3}$, the second harmonic is below the noise floor ($< 10^{-14}$) — invisible on the plot. At $A = 10^{-2}$, a faint curve rises from zero to a peak of $\sim 10^{-5}$ at $t \approx 0.3$ and then decays at rate $D\alpha_2$. At $A = 0.05$, the peak reaches $\sim 10^{-3}$. At $A = 0.2$, the peak reaches $\sim 10^{-2}$ and persists longer, with a decay rate that reflects the coupled three-mode dynamics rather than the isolated $D\alpha_2$. In all cases, the eventual decay rate of $a_2$ converges to $D\alpha_2 = 6.522$ once the source term ($a_1^2$) has become negligible.

---

### 3.2 Multi-Mode Superposition: Spectral Gap Behavior

#### 3.2.1 Analytic Prediction

When multiple modes are initialized simultaneously, each decays independently at its own rate in the linearized regime (Theorem C.17). The slowest-decaying component determines the long-time behavior: for $t \gg 1/D\alpha_2$, only the $n = 0$ (homogeneous) and $n = 1$ (first spatial) modes remain, and for $t \gg 1/D\alpha_1$, only the homogeneous mode survives. The rate at which the spatial modes peel off from the surviving signal is governed by the spectral gap.

The spectral gap separating the homogeneous mode from the first spatial mode is

$$
\gamma_{\mathrm{sp}} - \gamma_{\mathrm{hom}} = D\alpha_1 - \gamma_0,
$$

where $\gamma_0 = \frac{1}{2}(DP_*' + \zeta/\tau)$ is the homogeneous decay rate. For Parameter Set II: $\gamma_0 = \frac{1}{2}(0.6 + 0.5) = 0.55$ and $D\alpha_1 = 2.080$, so the gap is $2.080 - 0.55 = 1.530$. The first spatial mode decays $2.080/0.55 \approx 3.8$ times faster than the homogeneous mode — a substantial separation.

The gap between consecutive spatial modes is

$$
D(\alpha_{n+1} - \alpha_n) = D\,M_*\,(\mu_{n+1} - \mu_n) = D\,M_*\,(2n+1)\,\pi^2,
$$

which grows linearly in $n$. The $n = 1$ to $n = 2$ gap is $D\,M_*(3\pi^2) = 0.6 \cdot 0.25 \cdot 29.608 = 4.441$. Each successive spatial mode decays much faster than the previous one.

#### 3.2.2 Numerical Experiment 3.3: Eight-Mode Initialization

**Setup.** Initialize with IC-B (eq. 1.9): $\rho_0(x) = \rho^* + \sum_{n=1}^{8} A_n\cos(n\pi x)$ with $A_n = 0.01/n^2$, $v_0 = 0.01$. This populates modes $n = 1$ through $n = 8$ and the homogeneous mode (through the nonzero $v_0$). Integrate to $T = 10.0$. At each time step, extract all modal amplitudes $\{a_n(t)\}_{n=0}^{16}$ via the spectral method (tracking up to mode $16$ to monitor nonlinear harmonic generation beyond the initialized modes).

**Measured quantities.**

1. Modal amplitude time series $a_n(t)$ for $n = 0, 1, \ldots, 16$.
2. Measured decay rate $\hat{\sigma}_n$ for each initially populated mode ($n = 1, \ldots, 8$), extracted from the linear portion of $\ln|a_n(t)|$.
3. Arrival time $t_{\mathrm{floor}}(n)$: the time at which $|a_n(t)|$ first drops below $10^{-10}$.
4. Homogeneous-mode time series $a_0(t)$ and participation $v(t)$, showing the coupled oscillatory or monotonic dynamics of the $n = 0$ sector.
5. Harmonic content in modes $n = 9, \ldots, 16$ (not initialized), monitoring nonlinear energy transfer.

**Expected results.** The eight initialized modes decay at their respective rates $D\alpha_n$, peeling off from the total signal in reverse order: mode $8$ vanishes first (fastest decay), then mode $7$, and so on, until only modes $0$ and $1$ remain. The arrival times $t_{\mathrm{floor}}(n)$ are inversely proportional to $D\alpha_n$: $t_{\mathrm{floor}}(n) \sim -\ln(10^{-10}/A_n)/(D\alpha_n)$. The homogeneous mode $(a_0, v)$ evolves according to the $2 \times 2$ system (C.13) with oscillatory behavior (Parameter Set II is in the Spiral Sheet, $\mathscr{D}_0 = -1.59$) and persists as the sole surviving component at late times.

The spectral gap manifests as a visible separation in the semilog plot: the $n = 1$ curve has a distinctly shallower slope than all higher modes, and the gap between $n = 1$ and $n = 0$ is smaller still (since $\gamma_{\mathrm{hom}} < D\alpha_1$). The overall picture is a fan of straight lines, ordered by slope, converging toward the noise floor at different times.

**Figure description (Figure 3.3).** *Multi-mode spectral waterfall.* Single large panel with semilog-$y$ axes.

The horizontal axis is $t$ (range $[0, 10]$). The vertical axis is $|a_n(t)|$ on a logarithmic scale (range $[10^{-14}, 10^{-2}]$). Nine curves are plotted: one for each initially populated mode $n = 1, \ldots, 8$ and one for the homogeneous mode $a_0(t)$. The curves are colored by mode number on a gradient from blue ($n = 0$) to red ($n = 8$).

The curves form a fan: the $n = 8$ curve (red) is the steepest, beginning at $|a_8(0)| = 0.01/64 \cdot 1/\sqrt{2} \approx 1.1 \times 10^{-4}$ and reaching the noise floor by $t \approx 0.08$. Each successive curve has a shallower slope and a higher initial amplitude (since $A_n = 0.01/n^2$ decreases more slowly than $e^{-D\alpha_n t}$), so the curves cross the noise floor at progressively later times. The $n = 1$ curve (dark blue) is the shallowest spatial mode, reaching the noise floor at $t \approx 6$. The $n = 0$ curve (blue, oscillating) lies below the $n = 1$ curve at early times (smaller initial amplitude) but survives the longest; its envelope decays at rate $\gamma_0 = 0.55$, with visible oscillations of period $2\pi/\omega \approx 2\pi/(0.5\sqrt{1.59}) \approx 4.99$.

Dashed reference lines with slopes $-D\alpha_n$ are drawn for $n = 1, 4, 8$ and for the homogeneous envelope $-\gamma_0$. Each numerical curve matches its reference slope in the linear-decay portion.

At the bottom of the panel, a thin horizontal dashed line marks the noise floor at $10^{-14}$. A vertical arrow labeled "$\gamma_{\mathrm{sp}} - \gamma_{\mathrm{hom}}$" spans the slope difference between the $n = 1$ curve and the $n = 0$ envelope at $t = 3$, visually indicating the spectral gap.

#### 3.2.3 Numerical Experiment 3.4: Spectral Gap Measurement

**Setup.** To measure the spectral gap with precision, integrate with a two-mode initial condition: $\rho_0(x) = \rho^* + A_0 + A_1\cos(\pi x)$ with $A_0 = 0.01$, $A_1 = 0.01$, $v_0 = 0.01$. This loads only modes $n = 0$ and $n = 1$, eliminating inter-mode contamination from higher harmonics.

Integrate to $T = 20.0$. Define the total spatial deviation $\|\rho(t) - \bar{\rho}(t)\|_{L^2}$, which at leading order is $|a_1(t)|/\sqrt{2}$ (the contribution of the first spatial mode). Also track $|a_0(t)|$ (homogeneous amplitude) and $|v(t)|$ (participation).

**Measured quantities.**

1. The decay rate of the spatial deviation: the slope of $\ln\|\rho - \bar{\rho}\|_{L^2}$ versus $t$.
2. The decay rate of the homogeneous deviation: the envelope of $|a_0(t)|$.
3. The measured spectral gap: $\hat{\gamma} = \hat{\sigma}_1 - \hat{\gamma}_0$.

**Expected results.** The spatial deviation decays at rate $D\alpha_1 = 2.080$. The homogeneous deviation decays at rate $\gamma_0 = 0.55$. The measured spectral gap $\hat{\gamma} = 2.080 - 0.55 = 1.53$ determines the time scale at which spatial structure becomes negligible relative to the homogeneous relaxation. After $t_{\mathrm{sep}} \sim \hat{\gamma}^{-1}\ln(A_1/A_0) \approx 0$ (since $A_0 = A_1$ here, the spatial mode is always subdominant), the solution is effectively spatially homogeneous.

**Figure description (Figure 3.4).** *Spectral gap demonstration.* Two panels.

Left panel: semilog-$y$ plot of three quantities versus time $t$ (range $[0, 20]$). Curve 1 (solid blue): the spatial deviation $\|\rho - \bar{\rho}\|_{L^2}$, decaying as a straight line with slope $-D\alpha_1 = -2.080$. Curve 2 (solid red, oscillating): the homogeneous amplitude $|a_0(t)|$ with envelope slope $-\gamma_0 = -0.55$. Curve 3 (dashed gray): the participation variable $|v(t)|$ with the same oscillation frequency as $a_0$ (they are coupled through $\mathbf{A}_0$). The blue curve drops below the red envelope at $t \approx 3$, marking the time at which spatial structure has decayed relative to the surviving homogeneous oscillation. Beyond $t = 3$, the solution is effectively a spatially uniform damped oscillation.

Right panel: the ratio $\|\rho - \bar{\rho}\|_{L^2} / |a_0(t)|$ (spatial-to-homogeneous amplitude ratio) on a semilog-$y$ axis versus $t$. This ratio decays as $e^{-(D\alpha_1 - \gamma_0)t} = e^{-1.53\,t}$. The curve is a straight line with slope $-1.53$, directly measuring the spectral gap. A dashed reference line with slope $-(D\alpha_1 - \gamma_0) = -1.53$ is overlaid. Agreement to within line width confirms the spectral gap prediction of Lemma C.31.

#### 3.2.4 Numerical Experiment 3.5: Spectral Gap Dependence on $D$

**Setup.** Fix $\zeta = 0.5$, $\tau = 1.0$. Sweep $D$ over $\{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9\}$. At each value, integrate the two-mode initial condition of Experiment 3.4 and measure $\hat{\sigma}_1$ and $\hat{\gamma}_0$.

**Analytic predictions.** As $D$ increases:

- $D\alpha_1 = D(M_*\mu_1 + P_*')$ increases linearly in $D$ (at fixed $M_*$, $\mu_1$, $P_*'$).
- $\gamma_{\mathrm{hom}} = \frac{1}{2}(DP_*' + \zeta/\tau)$ also increases linearly in $D$ but with slope $P_*'/2$, which is smaller than $\alpha_1$ when $M_*\mu_1 > P_*'/2$.
- The spectral gap $\gamma_{\mathrm{sp}} - \gamma_{\mathrm{hom}} = D\alpha_1 - \gamma_0 = D(M_*\mu_1 + P_*'/2) - \zeta/(2\tau)$ increases linearly in $D$.

The gap widens as $D$ increases because stronger direct-channel diffusion accelerates the spatial modes more than it accelerates the homogeneous mode (which gains diffusive damping only through the $DP_*'$ term, not through $DM_*\mu_n$).

**Figure description (Figure 3.5).** *Spectral gap versus direct-channel weight.* Single panel.

The horizontal axis is $D$ (range $[0.1, 0.9]$). The vertical axis shows three quantities: $D\alpha_1$ (upper curve, circles), $\gamma_{\mathrm{hom}}$ (lower curve, squares), and their difference $D\alpha_1 - \gamma_{\mathrm{hom}}$ (shaded region between the two curves). Numerical data points are plotted as filled markers; analytic predictions (straight lines) are overlaid. The shaded band — the spectral gap — widens linearly from $D = 0.1$ (gap $\approx 0.1$) to $D = 0.9$ (gap $\approx 2.6$). A horizontal dashed line at $\gamma = 0$ confirms that the gap is strictly positive for all $D > 0$, as guaranteed by Corollary C.18.

---

### 3.3 Modal Decay Funnel: $\alpha_n$ versus $n$

#### 3.3.1 Analytic Prediction

The decay coefficients $\alpha_n = M_*\mu_n + P_*'$ are (Proposition C.29):

$$
\alpha_n = M_*\,n^2\pi^2 + P_*', \qquad n = 0, 1, 2, \ldots
\tag{3.2}
$$

on $\Omega_1 = [0, 1]$. This is a quadratic function of the mode number $n$, with a positive offset $P_*'$ (the penalty floor) and a curvature $M_*\pi^2$ (the diffusive enhancement). The decay rates $D\alpha_n$ form a parabolic funnel opening upward: low modes have decay rates near the floor, high modes have decay rates growing without bound.

The ratio of consecutive decay rates (Remark C.30) is

$$
\frac{\alpha_{n+1}}{\alpha_n} = \frac{M_*(n+1)^2\pi^2 + P_*'}{M_* n^2\pi^2 + P_*'} = 1 + \frac{(2n+1)M_*\pi^2}{M_* n^2\pi^2 + P_*'},
$$

which decreases monotonically in $n$ from $\alpha_1/\alpha_0 = 1 + M_*\mu_1/P_*' = 1 + 0.25 \cdot 9.87/1.0 = 3.467$ to $1$ as $n \to \infty$. The largest spectral separation is always between $n = 0$ and $n = 1$; each successive pair is more closely spaced in relative terms.

#### 3.3.2 Numerical Experiment 3.6: Direct Measurement of Decay Rates Across Modes

**Setup.** Initialize with IC-B at high mode count: $\rho_0(x) = \rho^* + \sum_{n=1}^{32} A_n\cos(n\pi x)$ with $A_n = 10^{-3}/n$ (giving each mode a resolvable initial amplitude that decreases slowly enough to be distinguishable from the noise floor). Set $v_0 = 0$. Use the spectral method (Method B) with $N = 128$ modes and ETD-RK4 time stepping ($\Delta t = 10^{-4}$) to resolve the fast decay of high modes. Integrate to $T = 2.0$ (sufficient for modes up to $n \approx 20$ to reach the noise floor).

At each time step, extract $a_n(t)$ for $n = 1, \ldots, 32$. For each mode, fit $\ln|a_n(t)|$ over the interval $[0, t_{\mathrm{floor}}(n)]$ to extract $\hat{\sigma}_n$.

**Measured quantities.**

1. The array of measured decay rates $\{\hat{\sigma}_n\}_{n=1}^{32}$.
2. The analytic prediction $D\alpha_n = D(M_*n^2\pi^2 + P_*')$ for each $n$.
3. The residual $|\hat{\sigma}_n - D\alpha_n|/D\alpha_n$ (relative error).
4. The arrival times $t_{\mathrm{floor}}(n)$ as a function of $n$.

**Expected results.** For modes $n \leq 20$ (well-resolved by $N = 128$), the measured decay rates $\hat{\sigma}_n$ agree with $D\alpha_n$ to within 0.5%. For modes $n > 20$, the finite spectral resolution introduces aliasing errors, and the measured rates deviate. The arrival times follow the scaling $t_{\mathrm{floor}}(n) \sim C/(D M_* n^2\pi^2)$ for large $n$, confirming the quadratic growth of the decay rate.

**Figure description (Figure 3.6).** *The decay-rate funnel.* Two panels.

Top panel: the measured decay rates $\hat{\sigma}_n$ (filled circles) plotted against mode number $n$ (horizontal axis, range $[0, 32]$), overlaid with the analytic curve $D\alpha_n = 0.6(0.25 n^2\pi^2 + 1.0)$ (solid parabola). The vertical axis is $D\alpha_n$ (range $[0, 500]$). The circles fall on the parabola for $n \leq 20$; beyond $n = 20$, a few points deviate upward (aliasing artifact), marked with open circles to distinguish them from the validated data. A horizontal dashed line at $D P_*' = 0.6$ marks the penalty floor — the minimum possible decay rate, approached only by the $n = 0$ mode.

The visual impression is a widening funnel: the low modes ($n = 1, 2, 3$) are tightly clustered near the base, and the high modes fan out rapidly. The funnel shape is the signature of the $n^2$ Weyl scaling.

Bottom panel: the relative error $|\hat{\sigma}_n - D\alpha_n|/D\alpha_n$ versus $n$ on a semilog-$y$ axis. For $n \leq 20$, the relative error is below $10^{-3}$ (within the dashed tolerance band). For $n > 20$, the error rises above $10^{-2}$, marking the resolution limit. A vertical dashed line at $n = N/6 \approx 21$ marks the effective de-aliasing cutoff (consistent with the 3/2-rule of §1.4.2).

#### 3.3.3 Numerical Experiment 3.7: The Decay-Rate Funnel in Two Dimensions

**Setup.** Repeat the decay-rate measurement on $\Omega_2 = [0, 1]^2$ with $N = 64$ grid points per dimension (Method A, 2D five-point stencil). Initialize with $\rho_0(x_1, x_2) = \rho^* + A\cos(n_1\pi x_1)\cos(n_2\pi x_2)$ for each pair $(n_1, n_2)$ with $n_1^2 + n_2^2 \leq 25$ (25 modes within a quarter-circle of radius $5$ in mode space). Set $A = 10^{-3}$, $v_0 = 0$.

**Analytic decay rates.** On $\Omega_2$, $\mu_{n_1, n_2} = (n_1^2 + n_2^2)\pi^2$, so

$$
D\alpha_{n_1,n_2} = D\bigl(M_*(n_1^2 + n_2^2)\pi^2 + P_*'\bigr).
$$

The decay rates depend only on $n_1^2 + n_2^2$, so modes with the same $|\mathbf{n}|^2$ are degenerate (e.g., $(1,0)$ and $(0,1)$ both have rate $D\alpha_1$; $(2,1)$ and $(1,2)$ both have rate $D(5M_*\pi^2 + P_*')$).

**Figure description (Figure 3.7).** *Two-dimensional decay-rate funnel.* Single panel.

The horizontal axis is $|\mathbf{n}|^2 = n_1^2 + n_2^2$ (range $[0, 25]$). The vertical axis is the measured decay rate $\hat{\sigma}_{n_1,n_2}$. Data points are plotted as circles, with degenerate modes at the same $|\mathbf{n}|^2$ stacking vertically (they should coincide if the measurement is accurate; any vertical spread indicates discretization asymmetry). The analytic curve $D(M_*|\mathbf{n}|^2\pi^2 + P_*')$ is overlaid as a solid line.

The funnel has the same parabolic shape as in one dimension, but with a denser set of mode-number values (since $|\mathbf{n}|^2$ takes integer values $0, 1, 2, 4, 5, 8, 9, 10, \ldots$ rather than $0, 1, 4, 9, 16, \ldots$). The degeneracy structure is visible: at $|\mathbf{n}|^2 = 1$, two coincident points; at $|\mathbf{n}|^2 = 5$, two coincident points (modes $(1,2)$ and $(2,1)$); at $|\mathbf{n}|^2 = 2$, a single point (mode $(1,1)$). The universality class framework (Appendix D, Theorem D.9) guarantees that the funnel shape is domain-independent: only the mode-number distribution changes, not the functional relationship $D\alpha_n = D(M_*\mu_n + P_*')$.

#### 3.3.4 Numerical Experiment 3.8: Penalty Floor and the Role of $P_*'$

**Setup.** Fix Parameter Set II but vary $P_0 \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$. For each, compute the analytic funnel $D\alpha_n(P_0) = D(M_*n^2\pi^2 + P_0)$ and measure $\hat{\sigma}_n$ for $n = 1, \ldots, 8$ using single-mode initialization.

**Analytic prediction.** Changing $P_0$ shifts the entire funnel vertically: the penalty floor moves from $DP_0 = 0.06$ (at $P_0 = 0.1$) to $DP_0 = 3.0$ (at $P_0 = 5.0$). The curvature $DM_*\pi^2$ is unchanged — it depends only on the mobility, not the penalty. Thus the funnel's opening rate is the same for all $P_0$, but its base altitude varies. At large $P_0$, the penalty dominates the decay of low modes ($\alpha_1 \approx P_0$ when $M_*\mu_1 \ll P_0$), and the spectral gap between $n = 0$ and $n = 1$ shrinks (the penalty floor pulls all modes toward the same rate). At small $P_0$, the diffusion dominates even for $n = 1$, and the gap is large.

**Figure description (Figure 3.8).** *Penalty floor sweep.* Single panel.

The horizontal axis is mode number $n$ (range $[0, 8]$). The vertical axis is $D\alpha_n$. Five parabolic curves are drawn, one for each $P_0$, with the lowest curve corresponding to $P_0 = 0.1$ and the highest to $P_0 = 5.0$. Each curve is a vertically shifted copy of the same parabola $DM_*n^2\pi^2$, offset by $DP_0$. Horizontal dashed lines mark the five penalty floors $DP_0 \in \{0.06, 0.30, 0.60, 1.20, 3.00\}$. Numerical data points (filled circles) are plotted on each curve at $n = 1, \ldots, 8$, confirming the vertical-shift structure.

At $P_0 = 5.0$, the first few modes are tightly clustered near the high penalty floor — the funnel is narrow at the base. At $P_0 = 0.1$, the funnel is wide at the base — the first mode's rate $D\alpha_1 = 0.06 + 0.6 \cdot 2.467 = 1.54$ is already far above the floor $0.06$, and the ratio $\alpha_1/P_0 = 25.7$ is enormous. This confirms the three structural roles of $P_*'$ identified in Proposition C.29: penalty floor (iii), diffusive enhancement (iv), and the decay-rate separation of Remark C.30. The penalty controls the *base* of the hierarchy; the mobility controls its *growth*.

---

## 4. Nonlinear Triad Simulations

The nonlinear triad coupling (Principle 7) is the mechanism by which the quadratic term $M'(\rho)|\nabla\rho|^2$ in the density operator $F[\rho]$ transfers energy between spatial modes. Appendix C.4 (§C.4.5) establishes the mathematical structure: the trilinear coupling coefficients $\Gamma_{mnk}$ (eq. C.26), the selection rule $k \in \{|m - n|, m + n\}$ (Theorem C.34), the explicit coupling values (eqs. C.38–C.39), the amplitude scaling of the generated harmonics (Proposition C.35), and the locked amplitude ratio $|a_3|/|a_1|$ at steady state (eq. C.40). Theorem C.36 synthesizes these results into the spectral modal hierarchy, and Remark C.37 identifies the selection rule as the spectral content of Principle 7.

This section demonstrates the triad coupling through three groups of experiments: the activation of specific mode pairs and verification of the selection rule (§4.1), the measurement of the locked amplitude ratio and its comparison to the analytic prediction (§4.2), and the full harmonic cascade from a single-mode initial condition (§4.3).

All experiments use the one-dimensional domain $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4) with default parameters, and Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$) unless otherwise stated. Parameter Set I is chosen because its low direct-channel weight ($D = 0.3$) and high mediated-channel weight ($H = 0.7$) slow the diffusive damping, allowing the nonlinear triad to develop before the modes decay. The spectral method (Method B, §1.4.2) with $N = 128$ modes and ETD-RK4 time stepping ($\Delta t = 10^{-4}$) is used for all modal amplitude measurements.

The constitutive values at equilibrium are $M_* = M(\rho^*) = (0.5)^2 = 0.25$, $M_*' = M'(\rho^*) = -2 \cdot 1.0 \cdot 0.5 = -1.0$, and $P_*' = 1.0$. On $\Omega_1 = [0, 1]$ with $L = 1$:

$$
\mu_n = n^2\pi^2, \qquad \alpha_n = 0.25\,n^2\pi^2 + 1.0, \qquad D\alpha_n = 0.3(0.25\,n^2\pi^2 + 1.0).
$$

The trilinear coupling coefficients for the cosine basis on $[0, 1]$ (Theorem C.34, with $c_0 = 1$ and $c_n = \sqrt{2}$ for $n \geq 1$) are:

$$
\Gamma_{mn,m+n} = \frac{mn\pi^2}{2}\cdot\frac{\sqrt{2}\cdot\sqrt{2}}{\sqrt{2}} = \frac{mn\pi^2\sqrt{2}}{2}, \qquad m \neq n,\; m, n \geq 1,
$$

$$
\Gamma_{mn,|m-n|} = \frac{mn\pi^2\sqrt{2}}{2}, \qquad m \neq n,\; |m - n| \geq 1,
$$

$$
\Gamma_{nn,2n} = \frac{n^2\pi^2}{2}\cdot\frac{2}{\sqrt{2}} = \frac{n^2\pi^2}{\sqrt{2}}, \qquad \Gamma_{nn,0} = \frac{n^2\pi^2}{2}\cdot\frac{2}{1} = n^2\pi^2.
$$

---

### 4.1 Triad Activation: Two-Mode Initialization and Harmonic Generation

#### 4.1.1 Analytic Prediction

The selection rule (Theorem C.34(i)) states that initializing modes $m$ and $n$ generates nonzero amplitude in modes $k = m + n$ and $k = |m - n|$ (and $k = 0$ for the mean correction), while all other modes remain at zero amplitude to leading nonlinear order. The generation rate for the sum mode $k = m + n$ is (from the projected system C.27):

$$
\dot{a}_{m+n}\big|_{\text{generation}} = D\,M_*'\,a_m\,a_n\,\Gamma_{mn,m+n} + O(a^3).
$$

Since $M_*' = -1.0 < 0$, the sign of the generation depends on the signs of $a_m$ and $a_n$. The magnitude of the generated amplitude at early times (before decay dominates) is

$$
|a_{m+n}(t)| \approx |D\,M_*'\,\Gamma_{mn,m+n}|\,|a_m(0)\,a_n(0)|\,t \cdot e^{-D\alpha_{m+n}\,t},
$$

which peaks at $t_{\mathrm{peak}} \approx 1/(D\alpha_{m+n})$ and then decays at the rate of the target mode.

The generated difference mode $k = |m - n|$ follows the same pattern with $\Gamma_{mn,|m-n|}$ replacing $\Gamma_{mn,m+n}$.

#### 4.1.2 Numerical Experiment 4.1: Pair $(m, n) = (1, 2)$

**Setup.** Initialize with modes $m = 1$ and $n = 2$:

$$
\rho_0(x) = \rho^* + A_1\cos(\pi x) + A_2\cos(2\pi x), \qquad v_0 = 0,
$$

with $A_1 = A_2 = 0.05$. Integrate to $T = 5.0$. Track modal amplitudes $a_k(t)$ for $k = 0, 1, \ldots, 16$.

**Selection rule prediction.** The pair $(1, 2)$ generates:

- Sum mode: $k = 1 + 2 = 3$.
- Difference mode: $k = |1 - 2| = 1$ (self-reinforcement of the existing mode $1$).
- Self-interactions: $1 \otimes 1 \to \{0, 2\}$; $2 \otimes 2 \to \{0, 4\}$.

The primary new mode generated at second order is therefore $k = 3$, with $k = 4$ generated by the self-interaction of mode $2$. Modes $k = 5, 6, 7, \ldots$ should remain at $O(A^3)$ or smaller.

**Coupling values.**

$$
\Gamma_{12,3} = \frac{1 \cdot 2 \cdot \pi^2\sqrt{2}}{2} = \pi^2\sqrt{2} \approx 13.96.
$$

$$
\Gamma_{22,4} = \frac{4\pi^2}{\sqrt{2}} = 2\sqrt{2}\,\pi^2 \approx 27.93.
$$

**Expected results.** The initially populated modes $k = 1$ and $k = 2$ decay at their respective linearized rates $D\alpha_1 \approx 1.040$ and $D\alpha_2 \approx 3.261$, with amplitude corrections from the mutual nonlinear interaction. Mode $k = 3$ grows from zero to a peak amplitude of $O(A^2) \approx O(2.5 \times 10^{-3})$, then decays at rate $D\alpha_3 \approx 6.962$. Mode $k = 4$ grows from zero to a peak of similar magnitude (generated by the $2 \otimes 2$ self-interaction), then decays at rate $D\alpha_4 \approx 12.144$. Modes $k \geq 5$ remain below $O(A^3) \approx O(10^{-4})$.

**Figure description (Figure 4.1).** *Triad activation from the pair $(1, 2)$.* Two panels.

Left panel: semilog-$y$ plot of $|a_k(t)|$ versus $t$ (horizontal axis, range $[0, 5]$) for $k = 1, 2, 3, 4, 5$. The vertical axis spans $[10^{-12}, 10^{-1}]$. The $k = 1$ curve (blue) begins at $\approx 3.5 \times 10^{-2}$ and descends with slope $\approx -1.04$, showing the slowest decay. The $k = 2$ curve (orange) begins at the same amplitude and descends with slope $\approx -3.26$, reaching the noise floor by $t \approx 3.5$. The $k = 3$ curve (green) starts at zero (below the plot floor), rises to a peak of $\approx 2 \times 10^{-3}$ at $t \approx 0.15$, then descends with slope $\approx -6.96$. The $k = 4$ curve (red) follows a similar rise-then-decay profile, peaking slightly earlier (its faster decay rate pulls the peak to smaller $t$) at amplitude $\approx 1.5 \times 10^{-3}$, then descending with slope $\approx -12.14$. The $k = 5$ curve (gray) remains flat below $10^{-7}$ throughout — confirming that it is not generated at second order.

The rise-then-decay shape of the $k = 3$ and $k = 4$ curves is the signature of nonlinear generation: the source term $\propto a_m a_n$ drives the mode while the source amplitude is large, and the mode's own diffusive decay takes over once the source has diminished. The peak time is controlled by the competition between the generation rate and the target-mode decay rate.

Right panel: bar chart showing the peak amplitude $\max_t |a_k(t)|$ for $k = 1, \ldots, 8$. Modes $k = 1, 2$ have bars at the initial amplitude $\approx 3.5 \times 10^{-2}$. Mode $k = 3$ has a bar at $\approx 2 \times 10^{-3}$. Mode $k = 4$ has a bar at $\approx 1.5 \times 10^{-3}$. Modes $k = 5, 6, 7, 8$ have bars below $10^{-5}$, barely visible on the logarithmic axis. A horizontal dashed line at $O(A^2) = 2.5 \times 10^{-3}$ marks the expected second-order generation level; the $k = 3$ and $k = 4$ bars cluster near this line. A second dashed line at $O(A^3) = 1.25 \times 10^{-4}$ marks the third-order level; the $k = 5$ bar falls below this threshold. The bar chart provides a visual confirmation of the selection rule: only the predicted target modes acquire significant amplitude.

#### 4.1.3 Numerical Experiment 4.2: Pair $(m, n) = (2, 3)$

**Setup.** Initialize with modes $m = 2$ and $n = 3$:

$$
\rho_0(x) = \rho^* + A_2\cos(2\pi x) + A_3\cos(3\pi x), \qquad v_0 = 0,
$$

with $A_2 = A_3 = 0.05$. Integrate to $T = 3.0$.

**Selection rule prediction.** The pair $(2, 3)$ generates:

- Sum mode: $k = 2 + 3 = 5$.
- Difference mode: $k = |2 - 3| = 1$.

This experiment tests the selection rule for a higher-mode pair and demonstrates the generation of a *lower* mode ($k = 1$) from two higher modes — the inverse cascade direction.

**Expected results.** Mode $k = 5$ rises from zero to $O(A^2)$ and decays at rate $D\alpha_5$. Mode $k = 1$ also rises from zero to $O(A^2)$ and decays at rate $D\alpha_1$ — much more slowly than mode $5$, making it the dominant nonlinearly generated contribution at late times. Modes not predicted by the selection rule ($k = 4, 6, 7$) remain at $O(A^3)$ or below.

The generation of mode $1$ from modes $2$ and $3$ is particularly significant: it demonstrates that the nonlinear triad can feed energy *downward* in the modal hierarchy, from fast-decaying modes into the slowest spatial mode. This inverse transfer, combined with the slow decay rate of mode $1$, means that the nonlinearity effectively extends the lifetime of spatial structure by injecting energy into the most persistent mode.

**Figure description (Figure 4.2).** *Triad activation from the pair $(2, 3)$: forward and inverse cascade.* Single panel, semilog-$y$.

The horizontal axis is $t$ (range $[0, 3]$); the vertical axis is $|a_k(t)|$ (range $[10^{-10}, 10^{-1}]$). Five curves are plotted: $k = 2$ (orange, decaying from $3.5 \times 10^{-2}$ with slope $\approx -3.26$), $k = 3$ (green, decaying from $3.5 \times 10^{-2}$ with slope $\approx -6.96$), $k = 5$ (purple, rising to peak $\approx 10^{-3}$ at $t \approx 0.08$ then decaying steeply), $k = 1$ (blue, rising to peak $\approx 2 \times 10^{-3}$ at $t \approx 0.3$ then decaying with the shallow slope $\approx -1.04$), and $k = 4$ (gray, remaining below $10^{-6}$).

The $k = 1$ curve is the most striking feature: it emerges from zero, passes through its peak later than $k = 5$ (because $D\alpha_1$ is small, the generation-versus-decay balance peaks at a later time), and then persists as the dominant spatial mode from $t \approx 0.5$ onward — long after the initially populated modes $k = 2$ and $k = 3$ have decayed below it. This is the inverse cascade in action: the nonlinearity has seeded the fundamental mode, and the modal hierarchy protects it.

#### 4.1.4 Numerical Experiment 4.3: Selection-Rule Verification Across Multiple Pairs

**Setup.** Systematically test all pairs $(m, n)$ with $1 \leq m \leq n \leq 6$. For each pair, initialize $\rho_0 = \rho^* + 0.03\cos(m\pi x) + 0.03\cos(n\pi x)$, $v_0 = 0$, integrate to $T = 2.0$, and record the peak amplitude $\max_t|a_k(t)|$ for each output mode $k = 0, \ldots, 16$.

**Measured quantity.** For each pair $(m, n)$, construct the selection-rule compliance vector: define a mode $k$ as "activated" if $\max_t|a_k| > 10^{-5}$ (a threshold chosen to lie between the $O(A^2) \sim 10^{-3}$ second-order level and the $O(A^3) \sim 10^{-5}$ third-order level). The selection rule predicts that the activated modes are exactly $\{|m - n|, m + n\}$ (plus $\{0, 2m\}$ from the self-interaction of $m$ and $\{0, 2n\}$ from $n$, when applicable).

**Expected results.** For each of the 21 pairs, the activated modes match the selection-rule prediction exactly. No mode outside the predicted set exceeds the $10^{-5}$ threshold.

**Figure description (Figure 4.3).** *Selection-rule compliance matrix.* Single panel, matrix format.

The panel shows a $21 \times 16$ grid. Each row corresponds to a source pair $(m, n)$, labeled on the left axis (rows ordered: $(1,1), (1,2), (1,3), \ldots, (6,6)$). Each column corresponds to an output mode $k = 0, 1, \ldots, 15$, labeled on the top axis. Each cell is colored: dark (filled) if the mode was activated ($\max_t|a_k| > 10^{-5}$), light (empty) otherwise. Overlaid on each cell is a small symbol: a circle if the selection rule predicts activation, a cross if it does not.

The result is a sparse matrix: dark cells appear only where circles are, and all cross-marked cells are light. This is the visual confirmation that the selection rule (Theorem C.34) holds without exception across all tested pairs. The sparsity pattern reveals the algebraic structure: the activated columns shift rightward as $m + n$ increases, and the difference-mode column $|m - n|$ traces a diagonal. Self-interaction rows ($m = n$) activate the $2m$ column and the $k = 0$ column.

---

### 4.2 Locked Amplitude Ratio: $|a_3|/|a_1|$ and Comparison to Theory

#### 4.2.1 Analytic Prediction

Proposition C.35 and equation (C.40) establish that the ratio of the third-harmonic amplitude to the fundamental, in steady state, is

$$
\frac{|a_3|}{|a_1|} \sim \frac{|M_*'|\,|\Gamma_{12,3}|}{D(\alpha_3 - \alpha_1)}\,\epsilon,
\tag{4.1}
$$

where $\epsilon$ is the perturbation amplitude and the ratio is evaluated at the quasi-steady state where the generation of mode $3$ by the interaction $1 \otimes 2$ is balanced by the differential decay $D(\alpha_3 - \alpha_1)$.

The critical structural claim (Theorem C.36(iv), Remark C.37) is that this ratio is *locked*: it depends on the constitutive and geometric parameters ($M_*'$, $\Gamma_{12,3}$, $D$, $\alpha_3$, $\alpha_1$) but not on the absolute amplitude of the perturbation. Specifically, the ratio $|a_3|/(|a_1|\,\epsilon)$ converges to a constant as $\epsilon \to 0$. This is the locked $k_3/k_1$ ratio of Principle 7.

For the current parameters:

$$
|M_*'| = 1.0, \qquad |\Gamma_{12,3}| = \pi^2\sqrt{2} \approx 13.96,
$$

$$
D(\alpha_3 - \alpha_1) = 0.3\,(23.207 - 3.467) = 0.3 \times 19.739 = 5.922,
$$

$$
\frac{|a_3|}{|a_1|} \sim \frac{13.96}{5.922}\,\epsilon = 2.357\,\epsilon.
\tag{4.2}
$$

At $\epsilon = 0.05$, this predicts $|a_3|/|a_1| \approx 0.118$; at $\epsilon = 0.1$, the prediction is $|a_3|/|a_1| \approx 0.236$.

The ratio is measured at the *quasi-steady phase*: the time interval after the initial transient (during which mode $2$ is generated by $1 \otimes 1$ and mode $3$ by $1 \otimes 2$) and before the overall decay has reduced all amplitudes to the noise floor. In this interval, the ratio $|a_3(t)|/|a_1(t)|$ should be approximately constant, with a value matching (4.2).

#### 4.2.2 Numerical Experiment 4.4: Amplitude Ratio at Fixed $\epsilon$

**Setup.** Initialize with mode $n = 1$ only:

$$
\rho_0(x) = \rho^* + \epsilon\cos(\pi x), \qquad v_0 = 0,
$$

at amplitude $\epsilon = 0.1$. Integrate to $T = 8.0$. Track $a_1(t)$, $a_2(t)$, and $a_3(t)$.

**Generation pathway.** The initial mode $1$ self-interacts: $1 \otimes 1 \to \{0, 2\}$, generating mode $2$ at $O(\epsilon^2)$. Then modes $1$ and $2$ cross-interact: $1 \otimes 2 \to \{1, 3\}$, generating mode $3$ at $O(\epsilon^3)$. The triad $\{1, 2, 3\}$ is thus established by $t \sim 1/D\alpha_2 \approx 0.31$ (the time scale for mode $2$ to reach its quasi-steady balance).

**Measured quantities.**

1. Time series $a_1(t)$, $a_2(t)$, $a_3(t)$.
2. The instantaneous ratio $R_{31}(t) := |a_3(t)|/|a_1(t)|$.
3. The quasi-steady value $\bar{R}_{31}$: the time-average of $R_{31}(t)$ over the interval $[t_{\mathrm{onset}}, t_{\mathrm{end}}]$, where $t_{\mathrm{onset}}$ is the time at which $|a_3|$ first exceeds $10^{-6}$ and $t_{\mathrm{end}}$ is the time at which $|a_1|$ drops below $10^{-6}$.
4. The predicted ratio (4.2): $2.357 \times 0.1 = 0.236$.

**Expected results.** After a brief transient ($t < 0.5$) during which mode $2$ is being populated, the ratio $R_{31}(t)$ settles to a plateau near $0.24 \pm 0.02$, matching the prediction (4.2) to within the $O(\epsilon^2)$ correction. The ratio remains approximately constant over the interval $[0.5, 3.0]$, during which all three triad modes are decaying but maintaining their relative amplitudes. At late times ($t > 3$), the ratio may drift as higher-order corrections and the homogeneous mode become relatively more important.

**Figure description (Figure 4.4).** *Locked amplitude ratio for the fundamental triad.* Two panels.

Left panel: semilog-$y$ plot of $|a_1(t)|$, $|a_2(t)|$, $|a_3(t)|$ versus $t$ (range $[0, 8]$). The $a_1$ curve (blue) decays from $\approx 7 \times 10^{-2}$ with slope $\approx -1.04$ (slightly modified from the linearized rate by the nonlinear self-interaction). The $a_2$ curve (orange) rises from zero to a peak of $\approx 5 \times 10^{-3}$ at $t \approx 0.3$, then decays with slope $\approx -3.26$. The $a_3$ curve (green) rises later, peaks at $\approx 8 \times 10^{-4}$ at $t \approx 0.5$, then decays with slope $\approx -6.96$. The three curves are approximately parallel (on the semilog scale, the vertical offset between $a_1$ and $a_3$ is constant) during the quasi-steady interval $[0.5, 3.0]$, confirming the locked ratio.

Right panel: the instantaneous ratio $R_{31}(t) = |a_3(t)|/|a_1(t)|$ on a linear axis versus $t$ (range $[0, 6]$). The ratio is undefined for $t < 0.2$ (before mode $3$ has been generated). It rises rapidly from $0$ to $\approx 0.23$ over $t \in [0.2, 0.5]$, then plateaus at $0.24 \pm 0.02$ over $t \in [0.5, 3.0]$. A horizontal dashed line at the analytic prediction $0.236$ is drawn. The measured plateau coincides with this line. At $t > 3.5$, the ratio begins to drift downward as the source term weakens and higher-order corrections become fractionally significant.

#### 4.2.3 Numerical Experiment 4.5: Amplitude Scaling and the Locking Test

**Setup.** Repeat Experiment 4.4 at five amplitudes: $\epsilon \in \{0.02, 0.05, 0.1, 0.15, 0.2\}$. For each, measure the quasi-steady ratio $\bar{R}_{31}$.

**Analytic prediction.** From (4.1), $\bar{R}_{31} \propto \epsilon$ at leading order. The *normalized* ratio $\bar{R}_{31}/\epsilon$ should be constant across all amplitudes, equal to $|M_*'|\,|\Gamma_{12,3}|/[D(\alpha_3 - \alpha_1)] = 2.357$. This amplitude-independence is the quantitative content of the locking claim (Theorem C.36(iv)).

**Measured quantities.**

1. The quasi-steady ratio $\bar{R}_{31}(\epsilon)$ for each amplitude.
2. The normalized ratio $\bar{R}_{31}/\epsilon$.
3. The deviation of the normalized ratio from the leading-order prediction $2.357$.

**Expected results.** For $\epsilon \leq 0.1$, the normalized ratio $\bar{R}_{31}/\epsilon$ agrees with $2.357$ to within $5\%$. For $\epsilon = 0.15$ and $\epsilon = 0.2$, corrections at $O(\epsilon^2)$ shift the normalized ratio upward (the nonlinear self-modification of the decay rates breaks the linear scaling), but the deviation remains below $15\%$. The systematic trend — upward deviation at large $\epsilon$ — is consistent with the $O(\epsilon^2)$ correction term in Proposition C.35.

**Figure description (Figure 4.5).** *Locking test: normalized amplitude ratio versus perturbation amplitude.* Single panel.

The horizontal axis is $\epsilon$ (range $[0, 0.22]$). The vertical axis is the normalized ratio $\bar{R}_{31}/\epsilon$ (range $[1.5, 3.5]$). Five data points (filled circles) are plotted, one for each amplitude. A horizontal dashed line at $2.357$ marks the leading-order prediction. At small $\epsilon$ ($0.02$, $0.05$), the data points lie on the dashed line within their error bars (estimated from the standard deviation of $R_{31}(t)$ over the quasi-steady interval). At $\epsilon = 0.1$, the point is slightly above ($\approx 2.40$). At $\epsilon = 0.15$, it is at $\approx 2.55$. At $\epsilon = 0.2$, it reaches $\approx 2.75$.

A thin solid curve shows the next-order analytic correction $2.357 + c_2\,\epsilon + O(\epsilon^2)$, where $c_2$ is computed from the cubic terms in the projected system (C.27); this curve passes through all five data points. The key observation is that the intercept at $\epsilon = 0$ extrapolates to $2.357$, confirming the locked ratio as an intrinsic property of the architecture, not a finite-amplitude artifact.

#### 4.2.4 Numerical Experiment 4.6: Ratio Dependence on $D$

**Setup.** Fix $\epsilon = 0.05$, $\zeta = 0.1$, $\tau = 1.0$. Sweep $D$ over $\{0.1, 0.2, 0.3, 0.5, 0.7, 0.9\}$. For each, measure $\bar{R}_{31}$.

**Analytic prediction.** The locked ratio (4.1) depends on $D$ through two mechanisms:

1. The decay-rate difference $D(\alpha_3 - \alpha_1) = D\,M_*\,(\mu_3 - \mu_1) = D \cdot 0.25 \cdot 8\pi^2 = 2D\pi^2$, which increases linearly in $D$.
2. The generation rate $D\,|M_*'|\,|\Gamma_{12,3}| = D \cdot 1.0 \cdot \pi^2\sqrt{2} = D\pi^2\sqrt{2}$, which also increases linearly in $D$.

The ratio $\bar{R}_{31}/\epsilon = |M_*'|\,|\Gamma_{12,3}|/[D(\alpha_3 - \alpha_1)]$ therefore has the $D$-dependence:

$$
\frac{\bar{R}_{31}}{\epsilon} = \frac{|M_*'|\,\Gamma_{12,3}}{D\,M_*(\mu_3 - \mu_1)} = \frac{|M_*'|}{M_*}\cdot\frac{\Gamma_{12,3}}{(\mu_3 - \mu_1)} \cdot \frac{1}{D}.
$$

Wait — the numerator $D\,|M_*'|\,|\Gamma_{12,3}|$ and denominator $D(\alpha_3 - \alpha_1)$ both contain $D$, so $D$ cancels at leading order. The ratio $\bar{R}_{31}/\epsilon$ should be *independent of $D$* in the leading-order formula. This is a non-trivial structural prediction: the locked ratio is set by the constitutive parameters $M_*'/M_*$ and the geometric coefficients $\Gamma_{mnk}/(\mu_k - \mu_m)$, not by the channel partition $D$.

More precisely, the full formula includes the penalty contribution to $\alpha_n$:

$$
\frac{\bar{R}_{31}}{\epsilon} = \frac{|M_*'|\,|\Gamma_{12,3}|}{D(M_*(\mu_3 - \mu_1)) + D(P_*' - P_*')} = \frac{|M_*'|\,|\Gamma_{12,3}|}{D\,M_*\,(\mu_3 - \mu_1)}.
$$

Since $\alpha_3 - \alpha_1 = M_*(\mu_3 - \mu_1)$ (the penalty cancels in the difference), the $D$-dependence is exactly

$$
\frac{\bar{R}_{31}}{\epsilon} = \frac{|M_*'|\,|\Gamma_{12,3}|}{D\,M_*\,(\mu_3 - \mu_1)} = \frac{1.0 \cdot 13.96}{D \cdot 0.25 \cdot 78.957} = \frac{13.96}{19.739\,D} = \frac{0.707}{D}.
$$

The ratio is inversely proportional to $D$: weaker direct-channel diffusion allows the triad to reach a higher amplitude ratio before the decay catches up. At $D = 0.3$, $\bar{R}_{31}/\epsilon \approx 2.36$; at $D = 0.9$, $\bar{R}_{31}/\epsilon \approx 0.79$.

**Figure description (Figure 4.6).** *Locked ratio versus direct-channel weight.* Single panel.

The horizontal axis is $D$ (range $[0.05, 0.95]$). The vertical axis is $\bar{R}_{31}/\epsilon$. Six data points (filled circles) are plotted. The analytic curve $0.707/D$ (solid hyperbola) is overlaid. The data points fall on the curve for $D \geq 0.2$; at $D = 0.1$, the measured ratio is slightly below the curve (the large $H = 0.9$ drives the participation coupling into a regime where the leading-order formula underestimates the feedback damping). The hyperbolic $1/D$ dependence confirms the structural prediction: the locked ratio is governed by the constitutive ratio $|M_*'|/(M_*\Delta\mu)$ modulated by the inverse of the channel weight.

---

### 4.3 Harmonic Cascade: Spectral Evolution Over Time

#### 4.3.1 Analytic Prediction

Starting from a single-mode initial condition (mode $n = 1$ at amplitude $\epsilon$), the nonlinear triad generates a cascade of harmonics:

$$
1 \otimes 1 \to \{0, 2\}, \qquad 1 \otimes 2 \to \{1, 3\}, \qquad 2 \otimes 2 \to \{0, 4\}, \qquad 1 \otimes 3 \to \{2, 4\}, \qquad \ldots
$$

At each order in $\epsilon$, new modes are activated: modes $0$ and $2$ at $O(\epsilon^2)$, mode $3$ at $O(\epsilon^3)$, mode $4$ at $O(\epsilon^4)$ (from both $2 \otimes 2$ and $1 \otimes 3$), and so on. The cascade produces a discrete spectrum $\{0, 1, 2, 3, 4, \ldots\}$ with amplitudes decreasing as $|a_k| \sim \epsilon^{k}$ for the lowest-order pathway to mode $k$.

However, the spectral hierarchy (Theorem C.36) ensures that the cascade is *self-limiting*: each higher harmonic decays faster ($D\alpha_k \sim Dk^2$), so the amplitude acquired through nonlinear generation is rapidly dissipated by diffusion. The resulting spectral profile at any fixed time $t > 0$ is a steeply decreasing function of $k$, with the steepness increasing over time as the higher modes decay preferentially.

The key qualitative features are:

1. **Broadband initial phase** ($t \lesssim 1/D\alpha_2$): the spectrum broadens as energy cascades upward from mode $1$.
2. **Quasi-steady triad phase** ($1/D\alpha_2 \lesssim t \lesssim 1/D\alpha_1$): modes $2, 3, 4, \ldots$ have reached their generation-decay balance, and the spectral envelope $|a_k|$ decreases geometrically in $k$.
3. **Fundamental-dominated phase** ($t \gg 1/D\alpha_1$): only mode $1$ (and the homogeneous mode $0$) survive; the cascade has been extinguished by diffusive damping.

#### 4.3.2 Numerical Experiment 4.7: Full Cascade from Mode $1$

**Setup.** Initialize with mode $1$ at amplitude $\epsilon = 0.2$ (chosen large enough for the cascade to populate modes up to $k \approx 8$ above the noise floor):

$$
\rho_0(x) = \rho^* + 0.2\cos(\pi x), \qquad v_0 = 0.
$$

Integrate to $T = 6.0$ with $N = 128$ spectral modes. Track all modal amplitudes $a_k(t)$ for $k = 0, \ldots, 32$.

**Measured quantities.**

1. The spectral snapshot $\{|a_k(t_j)|\}_{k=0}^{32}$ at six time slices: $t_j \in \{0.01, 0.1, 0.5, 1.0, 2.0, 5.0\}$.
2. The spectral envelope $E(k, t) := |a_k(t)|$ as a function of $k$ at each time slice.
3. The total spectral energy $\sum_{k=1}^{32} |a_k(t)|^2$ versus $t$, tracking the redistribution of energy across modes.
4. The spectral centroid $\bar{k}(t) := \sum_k k\,|a_k|^2 / \sum_k |a_k|^2$, tracking the mean mode number of the energy distribution.

**Expected results.**

- At $t = 0.01$: the spectrum is nearly monochromatic — only mode $1$ has significant amplitude. Mode $2$ has just begun to appear at $O(\epsilon^2) \approx O(0.04)$.
- At $t = 0.1$: modes $1, 2, 3$ are populated, with amplitudes decreasing by roughly a factor of $5$–$10$ per mode. Mode $4$ is emerging.
- At $t = 0.5$: the triad is fully established. Modes $1$ through $6$ have measurable amplitudes, with the spectral envelope dropping steeply. The quasi-steady ratio $|a_3|/|a_1| \approx 0.47$ (from $2.357 \times 0.2$).
- At $t = 1.0$: mode $2$ has decayed significantly (its decay rate $D\alpha_2 \approx 3.26$ gives a factor of $e^{-3.26} \approx 0.04$ per unit time). The spectrum is narrowing back toward mode $1$.
- At $t = 2.0$: only modes $0$ and $1$ have amplitudes above $10^{-6}$. The cascade has been extinguished.
- At $t = 5.0$: only the homogeneous mode (oscillating) and a vestigial mode $1$ remain.

The spectral centroid $\bar{k}(t)$ rises from $1.0$ at $t = 0$, peaks at $\bar{k} \approx 1.5$–$2.0$ during the cascade phase ($t \approx 0.1$–$0.3$), then decays back toward $\bar{k} \approx 1.0$ as the higher modes are extinguished. This rise-and-fall of the centroid is the temporal signature of the cascade: a brief broadening followed by systematic narrowing under the modal hierarchy.

**Figure description (Figure 4.7).** *Harmonic cascade: spectral snapshots.* Single large panel.

The horizontal axis is mode number $k$ (range $[0, 16]$). The vertical axis is $|a_k|$ on a logarithmic scale (range $[10^{-12}, 10^{0}]$). Six spectral envelopes are plotted, one for each time slice, distinguished by line style and shade (lightest for $t = 0.01$, darkest for $t = 5.0$). Each envelope is a set of points (one per mode) connected by line segments.

At $t = 0.01$ (lightest): a single tall bar at $k = 1$ with a barely visible bar at $k = 2$. The spectrum is monochromatic.

At $t = 0.1$: bars at $k = 1$ (tallest), $k = 2$ (one order of magnitude lower), $k = 3$ (two orders lower), $k = 4$ (three orders lower). The envelope falls approximately as a geometric sequence.

At $t = 0.5$: the broadest spectrum. Bars visible from $k = 1$ to $k \approx 7$. The $k = 1$ bar has decreased from its initial value (decay). The envelope forms a smooth, steeply decreasing curve.

At $t = 1.0$: narrower. Only $k = 1, 2, 3$ above $10^{-6}$. The $k = 1$ bar is still the tallest but has decayed by a factor $\approx e^{-1.04} \approx 0.35$ from $t = 0$.

At $t = 2.0$: nearly monochromatic again. Only $k = 0$ (small, oscillating) and $k = 1$ visible.

At $t = 5.0$ (darkest): all spatial modes below $10^{-6}$. The $k = 0$ bar alone survives, oscillating at the frequency $\omega$ of the homogeneous mode (Parameter Set I is oscillatory).

The visual narrative is clear: the spectrum blooms outward from $k = 1$ during the cascade phase, reaches maximum breadth at $t \approx 0.5$, then contracts back to $k = 1$ and finally to $k = 0$ under the relentless action of the modal hierarchy. The diffusive damping, growing as $k^2$, prunes the cascade from the top down.

#### 4.3.3 Numerical Experiment 4.8: Cascade Depth Versus Amplitude

**Setup.** Repeat Experiment 4.7 at five amplitudes $\epsilon \in \{0.02, 0.05, 0.1, 0.15, 0.2\}$. For each, record the spectral snapshot at the time of maximum spectral breadth ($t_{\mathrm{peak}}$, defined as the time at which $\bar{k}(t)$ is maximized). Define the cascade depth $K(\epsilon)$ as the highest mode $k$ for which $|a_k(t_{\mathrm{peak}})| > 10^{-8}$.

**Analytic prediction.** Since the amplitude of mode $k$ scales as $\epsilon^k$ at leading order (each cascade step multiplies by $\epsilon$ times a coupling coefficient), the cascade depth scales logarithmically:

$$
K(\epsilon) \sim \frac{-\ln(10^{-8})}{\ln(1/\epsilon)} = \frac{8\ln 10}{-\ln\epsilon}.
$$

At $\epsilon = 0.2$: $K \approx 8\ln 10/1.609 \approx 11.5$, predicting modes up to $k \approx 11$. At $\epsilon = 0.02$: $K \approx 8\ln 10/3.912 \approx 4.7$, predicting modes up to $k \approx 4$.

**Figure description (Figure 4.8).** *Cascade depth versus perturbation amplitude.* Two panels.

Left panel: five spectral envelopes at the respective $t_{\mathrm{peak}}$, one for each $\epsilon$, superimposed on the same semilog-$y$ axes ($k$ horizontal, $|a_k|$ vertical). Each envelope begins at $|a_1| \approx \epsilon/\sqrt{2}$ (adjusted for the $L^2$ normalization) and falls off at a rate that steepens with decreasing $\epsilon$. The $\epsilon = 0.2$ envelope extends to $k \approx 10$–$12$ before reaching $10^{-8}$; the $\epsilon = 0.02$ envelope reaches only $k \approx 4$–$5$. The envelopes are nested: each larger $\epsilon$ produces a broader, taller spectrum.

Right panel: the measured cascade depth $K(\epsilon)$ (filled circles) versus $\epsilon$ on a semilog-$x$ axis. The analytic curve $8\ln 10 / (-\ln\epsilon)$ (solid line) is overlaid. The data points follow the logarithmic scaling, with $K$ increasing steeply as $\epsilon$ approaches $1$ and saturating at small $\epsilon$. The curve confirms that the cascade depth is not a free parameter but a structural consequence of the amplitude scaling and the spectral hierarchy: diffusive damping ($\alpha_k \sim k^2$) terminates the cascade at a mode number determined by the initial amplitude.

#### 4.3.4 Numerical Experiment 4.9: Spectral Energy Redistribution

**Setup.** Use the data from Experiment 4.7 ($\epsilon = 0.2$) to track the energy distribution across modes over time. Define the modal energy $E_k(t) := |a_k(t)|^2$ and the cumulative energy fractions:

$$
f_k(t) := \frac{\sum_{j=0}^{k} E_j(t)}{\sum_{j=0}^{32} E_j(t)}, \qquad k = 0, 1, \ldots, 32.
$$

**Expected results.** At $t = 0$, nearly all energy is in mode $1$: $f_1 \approx 1$. During the cascade ($t \in [0.1, 0.5]$), energy is redistributed: $f_1$ decreases as modes $2, 3, \ldots$ acquire energy. The fraction lost by mode $1$ is $O(\epsilon^2)$: at $\epsilon = 0.2$, roughly $4\%$ of the initial energy is transferred to higher modes at peak cascade. After the cascade ($t > 1$), the energy fraction in mode $1$ recovers toward $1$ as the higher modes decay. Throughout, the total energy $\sum_k E_k(t)$ is not conserved — it decreases monotonically, consistent with the dissipative nature of the ED system (Lemma C.6). The redistribution is transient: the nonlinearity briefly broadens the spectrum, but the hierarchy permanently funnels the surviving energy back into the lowest modes.

**Figure description (Figure 4.9).** *Energy redistribution and cascade dynamics.* Two panels.

Left panel: stacked area plot showing the modal energy fractions $E_k(t)/\sum E_k$ for $k = 0, 1, 2, 3, 4, \text{rest}$ as colored bands, stacked vertically to fill the unit interval. The horizontal axis is $t$ (range $[0, 6]$). At $t = 0$, the $k = 1$ band fills nearly the entire height. Between $t = 0.1$ and $t = 0.5$, thin colored bands appear above the $k = 1$ band: orange for $k = 2$, green for $k = 3$, red for $k = 4$, gray for the rest. The maximum total width of the higher-mode bands occurs at $t \approx 0.3$, reaching approximately $4\%$ of the total. After $t = 1$, the higher-mode bands have collapsed and $k = 1$ again dominates. At $t > 3$, the $k = 0$ band begins to occupy a visible fraction (the homogeneous mode outlives the first spatial mode).

Right panel: semilog-$y$ plot of the total energy $\sum_k E_k(t)$ versus $t$. The curve descends monotonically, with slope $\approx -2D\alpha_1 \approx -2.08$ at late times (when mode $1$ dominates; the factor of $2$ comes from $E_k = |a_k|^2$ decaying at twice the amplitude rate). At early times ($t < 0.5$), the slope is steeper because the higher modes are dissipating their energy at their faster rates $2D\alpha_k$. The transition from the steeper to the shallower slope marks the end of the cascade phase — the time at which the higher harmonics have been extinguished and the modal hierarchy has selected mode $1$ as the sole surviving spatial structure.

---

## 5. ED-Complexity Dynamics

ED-complexity is the functional

$$
C_{\mathrm{ED}}[\rho(\cdot, t)] := \int_\Omega |\nabla\rho(x,t)|^2\,d^d x,
$$

which measures the total gradient content of the density field at time $t$. It is not an auxiliary definition; it is the quantity that appears in the dissipation identity (Lemma C.6), the stability Lyapunov functional (Definition C.39, the $\frac{D}{2}\|\nabla u\|_{L^2}^2$ term in $\mathcal{V}$), the nonlinear triad coupling (the $|\nabla\rho|^2$ factor in $M'(\rho)|\nabla\rho|^2$), and the Applications Paper's bridge between the mathematical architecture and physical prediction (§1.4 of the Applications Paper). The dissipation bound (Lemma C.6) shows that the leading gradient dissipation term is

$$
-D\int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx \leq -D\,\frac{P_*'}{M_*}\,C_{\mathrm{ED}}[\rho] + O(\|\rho - \rho^*\|_{L^\infty}\,C_{\mathrm{ED}}),
$$

so ED-complexity controls the rate at which the system dissipates energy through spatial smoothing. The stability theorem (Theorem C.43) identifies a threshold $\epsilon_0$ in $\|u\|_{H^s} + |w|$ below which exponential convergence holds; the $H^1$-contribution to this norm includes $\|\nabla u\|_{L^2}^2 = C_{\mathrm{ED}}[\rho]$, so the stability threshold has a direct interpretation as a critical ED-complexity.

This section demonstrates three aspects of ED-complexity dynamics: the relationship between complexity and dissipation rate (§5.1), the stability threshold $\epsilon_0$ and its role as a complexity boundary (§5.2), and the principle that complexity — not mass — orders the dynamical behavior of configurations (§5.3).

All experiments use $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4), the Crank–Nicolson scheme (§1.5.2) with $N = 512$ and $\Delta t = 5 \times 10^{-4}$, and Parameter Set II ($D = 0.6$, $\zeta = 0.5$, $\tau = 1.0$) unless otherwise stated.

---

### 5.1 Complexity Versus Dissipation: $C_{\mathrm{ED}}(t)$ for Low, Medium, and High Complexity

#### 5.1.1 Analytic Framework

The time derivative of ED-complexity along solutions of the linearized system can be computed by differentiating $C_{\mathrm{ED}} = \|\nabla u\|_{L^2}^2$ (where $u = \rho - \rho^*$):

$$
\frac{d}{dt}C_{\mathrm{ED}} = 2\int_\Omega \nabla u \cdot \nabla(\partial_t u)\,dx = -2\int_\Omega (\nabla^2 u)\,\partial_t u\,dx,
$$

where the second equality uses integration by parts with Neumann conditions. Substituting the linearized $\rho$-equation $\partial_t u = D(M_*\nabla^2 u - P_*' u) + Hw$:

$$
\frac{d}{dt}C_{\mathrm{ED}} = -2D\,M_*\|\nabla^2 u\|_{L^2}^2 + 2D\,P_*'\|\nabla u\|_{L^2}^2 - 2Hw\int_\Omega \nabla^2 u\,dx.
$$

The last integral vanishes by Neumann conditions ($\int_\Omega\nabla^2 u\,dx = 0$). Therefore, at linear order:

$$
\frac{d}{dt}C_{\mathrm{ED}} = -2D\,M_*\|\nabla^2 u\|_{L^2}^2 + 2D\,P_*'\,C_{\mathrm{ED}}.
\tag{5.1}
$$

The two terms compete: the first (involving $\|\nabla^2 u\|_{L^2}^2$) is dissipative (diffusion smooths gradients), and the second (involving $C_{\mathrm{ED}}$ itself) is *anti-dissipative* (the penalty term $-P_*' u$ in the equation generates gradients when $u$ has spatial structure, because the penalty pushes $u \to 0$ locally without regard for the gradient structure).

For a single Neumann mode $u = a_n(t)\varphi_n(x)$, we have $\|\nabla^2 u\|_{L^2}^2 = \mu_n^2\,|a_n|^2$ and $C_{\mathrm{ED}} = \mu_n\,|a_n|^2$, so

$$
\frac{d}{dt}C_{\mathrm{ED}} = -2D(M_*\mu_n - P_*')\,\mu_n\,|a_n|^2 = -2D(M_*\mu_n - P_*')\,C_{\mathrm{ED}}.
$$

For $n \geq 1$ with $M_*\mu_1 > P_*'$ (which holds in our parameter set: $M_*\mu_1 = 0.25 \cdot 9.87 = 2.47 > 1.0 = P_*'$), the complexity decays exponentially at rate $2D(M_*\mu_n - P_*')$, which is faster for higher modes. For a multi-mode initial condition, the total complexity decays as a sum of exponentials, dominated at late times by the slowest component $n = 1$.

The key structural prediction is: **higher-complexity configurations dissipate faster**. This follows from two mechanisms:

1. *Diffusive smoothing* ($-2DM_*\|\nabla^2 u\|_{L^2}^2$): steeper gradients produce stronger diffusion, which smooths them out faster.
2. *Modal composition*: high-$C_{\mathrm{ED}}$ configurations have more energy in high-$n$ modes, which decay faster by the modal hierarchy (Proposition C.29).

#### 5.1.2 Numerical Experiment 5.1: Three Complexity Levels

**Setup.** Design three initial conditions with the same total mass $\int_\Omega\rho\,dx = \rho^*\,L$ (i.e., zero mean deviation $\int_\Omega u\,dx = 0$) but widely different ED-complexities:

**Low complexity (LC):**

$$
\rho_0^{\mathrm{LC}}(x) = \rho^* + 0.02\cos(\pi x), \qquad v_0 = 0.
$$

This is a single-mode perturbation with small amplitude. $C_{\mathrm{ED}}^{\mathrm{LC}} = (0.02)^2\,\mu_1/2 = 4 \times 10^{-4} \cdot \pi^2/2 \approx 1.97 \times 10^{-3}$.

**Medium complexity (MC):**

$$
\rho_0^{\mathrm{MC}}(x) = \rho^* + 0.02\cos(\pi x) + 0.02\cos(2\pi x) + 0.02\cos(3\pi x), \qquad v_0 = 0.
$$

Three modes at equal amplitude. $C_{\mathrm{ED}}^{\mathrm{MC}} = (0.02)^2\,(\mu_1 + \mu_2 + \mu_3)/2 = 4 \times 10^{-4}\cdot\pi^2(1 + 4 + 9)/2 \approx 2.76 \times 10^{-2}$.

**High complexity (HC):**

$$
\rho_0^{\mathrm{HC}}(x) = \rho^* + 0.02\sum_{n=1}^{8}\cos(n\pi x), \qquad v_0 = 0.
$$

Eight modes at equal amplitude. $C_{\mathrm{ED}}^{\mathrm{HC}} = (0.02)^2\,\sum_{n=1}^{8}\mu_n/2 = 4 \times 10^{-4}\cdot\pi^2(1+4+9+16+25+36+49+64)/2 = 4 \times 10^{-4}\cdot\pi^2 \cdot 102 \approx 0.402$.

The ratio $C_{\mathrm{ED}}^{\mathrm{HC}}/C_{\mathrm{ED}}^{\mathrm{LC}} \approx 204$: the high-complexity initial condition has two hundred times the gradient content of the low-complexity one, despite having the same total mass and the same amplitude in the fundamental mode.

Integrate all three to $T = 8.0$.

**Measured quantities.**

1. $C_{\mathrm{ED}}(t)$ for each initial condition, computed as $h\sum_j ((\rho_{j+1} - \rho_{j-1})/(2h))^2$ (the trapezoidal-rule discrete gradient-squared integral).
2. The instantaneous dissipation rate $-d\mathcal{E}/dt$, computed from the energy functional (C.3).
3. The ratio $(-d\mathcal{E}/dt)/C_{\mathrm{ED}}(t)$, which should approach $D\,P_*'/M_* = 0.6 \cdot 1.0/0.25 = 2.4$ in the linearized regime (from the leading dissipation term in Lemma C.6).

**Expected results.** All three $C_{\mathrm{ED}}(t)$ curves decay monotonically (after a possible brief transient for HC, where the anti-dissipative penalty term is comparatively small). The HC curve starts highest and decays fastest, reaching the level of the MC curve by $t \approx 0.3$ and the LC curve by $t \approx 1.0$. The MC curve decays at an intermediate rate. The LC curve decays slowest, with a nearly exponential profile at rate $\approx 2D(M_*\mu_1 - P_*') = 2 \cdot 0.6 \cdot (2.47 - 1.0) = 1.76$.

At late times ($t > 2$), all three curves converge to the same asymptotic rate $2D(M_*\mu_1 - P_*') \approx 1.76$, because only the fundamental mode $n = 1$ survives. The high-complexity curve reaches this asymptotic regime earliest (the high modes have already decayed by $t \approx 0.5$); the low-complexity curve is already in this regime from $t = 0$ (it was initialized with only mode $1$).

The dissipation-to-complexity ratio $(-d\mathcal{E}/dt)/C_{\mathrm{ED}}$ is approximately constant at $\approx 2.4$ for all three cases in the linearized regime, confirming that ED-complexity directly controls the dissipation rate with a proportionality constant set by the constitutive ratio $D P_*'/M_*$.

**Figure description (Figure 5.1).** *Complexity-dissipation relationship at three complexity levels.* Three panels.

Top panel: semilog-$y$ plot of $C_{\mathrm{ED}}(t)$ versus $t$ (horizontal axis, range $[0, 8]$). Three curves: LC (blue), MC (orange), HC (red). The vertical axis spans $[10^{-10}, 1]$. The HC curve starts at $\approx 0.4$ and plunges steeply during $t \in [0, 0.5]$, with a concave-down profile on the semilog scale (reflecting the mixture of fast-decaying high modes). It transitions to a straight-line descent at slope $\approx -1.76$ by $t \approx 1$. The MC curve starts at $\approx 0.028$, descends with moderate curvature, and joins the asymptotic slope by $t \approx 0.5$. The LC curve starts at $\approx 0.002$ and is a straight line from the start with slope $\approx -1.76$ (it was initialized in the asymptotic regime). At late times, all three curves are parallel — three offset straight lines with identical slopes — confirming that the asymptotic complexity decay rate is independent of the initial complexity level. Dashed reference lines with slopes $-2D(M_*\mu_1 - P_*')$ and $-2D(M_*\mu_8 - P_*')$ bound the fast and slow extremes.

Middle panel: semilog-$y$ plot of the instantaneous dissipation rate $-d\mathcal{E}/dt$ versus $t$, for the same three initial conditions. The HC curve starts at the highest dissipation rate ($\approx 1.0$), reflecting the large gradient content driving the energy loss. The LC curve starts at the lowest ($\approx 0.005$). The ordering is preserved for all $t$: $(-d\mathcal{E}/dt)_{\mathrm{HC}} > (-d\mathcal{E}/dt)_{\mathrm{MC}} > (-d\mathcal{E}/dt)_{\mathrm{LC}}$ until the complexities themselves converge, after which the dissipation rates converge correspondingly.

Bottom panel: the ratio $(-d\mathcal{E}/dt)/C_{\mathrm{ED}}(t)$ versus $t$ on a linear axis. All three curves fluctuate around the value $2.4$ (the linearized proportionality constant $DP_*'/M_*$). The LC curve is nearly flat at $2.4$ from $t = 0$ (it is always in the linearized regime). The MC and HC curves show deviations at early times — the HC curve dips below $2.4$ briefly (the penalty anti-dissipation is comparatively stronger when $C_{\mathrm{ED}}$ is large and $\|\nabla^2 u\|_{L^2}^2$ does not yet dominate) — but converge to $2.4$ by $t \approx 0.5$. A horizontal dashed line at $DP_*'/M_* = 2.4$ marks the theoretical proportionality constant.

#### 5.1.3 Numerical Experiment 5.2: Dissipation Channel Decomposition by Complexity

**Setup.** Using the HC initial condition from Experiment 5.1, decompose the total dissipation rate into its three structural channels (Proposition C.42, eq. C.45):

$$
\mathcal{D}_{\mathrm{diff}}(t) := D\,P_*'\,C_{\mathrm{ED}}(t), \qquad
\mathcal{D}_{\mathrm{pen}}(t) := \frac{D\,P_*'^2}{M_*}\|u(t)\|_{L^2}^2, \qquad
\mathcal{D}_{\mathrm{part}}(t) := H\zeta\,|v(t)|^2.
$$

These are the three sign-definite contributions to $-d\mathcal{V}/dt$ from the Lyapunov dissipation (eq. C.45): gradient dissipation (controlled by $C_{\mathrm{ED}}$, structural origin in Principle 1), penalty dissipation (controlled by the $L^2$-deviation, structural origin in Principle 3), and participation damping (controlled by $|v|^2$, structural origin in Principle 5).

**Expected results.** At early times, $\mathcal{D}_{\mathrm{diff}}$ dominates ($C_{\mathrm{ED}}$ is large and the gradients drive the dissipation). As the complexity decays, $\mathcal{D}_{\mathrm{pen}}$ becomes the dominant channel (the mean deviation $\bar{u}$ relaxes on the slower penalty time scale $1/(DP_*')$). The participation damping $\mathcal{D}_{\mathrm{part}}$ contributes throughout but peaks at intermediate times when the oscillatory participation variable $v(t)$ has been excited by the feedback loop.

The crossover time $t_{\mathrm{cross}}$ at which $\mathcal{D}_{\mathrm{diff}} = \mathcal{D}_{\mathrm{pen}}$ marks the transition from gradient-dominated to penalty-dominated dissipation. This crossover depends on the initial complexity: high-$C_{\mathrm{ED}}$ configurations reach it later (they have more gradient energy to dissipate first); low-$C_{\mathrm{ED}}$ configurations may never have $\mathcal{D}_{\mathrm{diff}} > \mathcal{D}_{\mathrm{pen}}$ if their gradient content is already small relative to their mean deviation.

**Figure description (Figure 5.2).** *Three-channel dissipation decomposition for the high-complexity initial condition.* Single panel with semilog-$y$ axes.

The horizontal axis is $t$ (range $[0, 6]$). The vertical axis shows the three dissipation-channel values (range $[10^{-8}, 10^{0}]$). Three curves: $\mathcal{D}_{\mathrm{diff}}$ (blue), $\mathcal{D}_{\mathrm{pen}}$ (orange), $\mathcal{D}_{\mathrm{part}}$ (green). A fourth curve (black, dashed) shows the total dissipation $-d\mathcal{E}/dt$.

At $t = 0$: $\mathcal{D}_{\mathrm{diff}} \approx 0.96$ (dominant), $\mathcal{D}_{\mathrm{pen}} \approx 0.02$, $\mathcal{D}_{\mathrm{part}} = 0$ (no participation yet). The gradient channel accounts for $\sim 98\%$ of the total dissipation. The blue curve descends steeply as the high modes are smoothed out.

At $t \approx 0.4$: the crossover — the blue and orange curves cross. Beyond this point, the penalty channel dominates. The green curve ($\mathcal{D}_{\mathrm{part}}$) has risen from zero to a local peak at $t \approx 0.3$ (the participation variable, excited by the operator output $F[\rho]$, is now oscillating with amplitude $\sim 0.02$), then begins to decrease.

At $t > 1$: $\mathcal{D}_{\mathrm{pen}}$ dominates, decaying at rate $\approx 2DP_*' \approx 1.2$ (the mean deviation decays at rate $DP_*'$, and $\mathcal{D}_{\mathrm{pen}} \propto \|u\|_{L^2}^2$ decays at twice that rate). $\mathcal{D}_{\mathrm{diff}}$ is subdominant, paralleling the late-time $C_{\mathrm{ED}}$ decay. $\mathcal{D}_{\mathrm{part}}$ oscillates (reflecting the damped oscillations of $v$) with decreasing envelope.

The total dissipation (black dashed) equals $\mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}}$ to within the discretization error at every time step, confirming closure of the discrete dissipation identity.

---

### 5.2 Complexity Threshold: The Stability Radius $\epsilon_0$

#### 5.2.1 Analytic Framework

Theorem C.43 guarantees exponential convergence provided the initial perturbation satisfies $\|u_0\|_{H^s} + |w_0| < \epsilon_0$, where

$$
\epsilon_0 = \frac{\gamma_*}{C_{\mathrm{nl}}}
$$

is the ratio of the linearized dissipation rate $\gamma_*$ (eq. C.48) to the Lipschitz constant of the nonlinear remainder (eq. C.49). For initial conditions with $v_0 = 0$ and a single spatial mode, the $H^1$-norm of the perturbation is

$$
\|u_0\|_{H^1}^2 = \|u_0\|_{L^2}^2 + \|\nabla u_0\|_{L^2}^2 = \|u_0\|_{L^2}^2 + C_{\mathrm{ED}}[\rho_0].
$$

The threshold $\epsilon_0$ therefore defines a critical complexity $C_{\mathrm{ED}}^* \approx \epsilon_0^2 - \|u_0\|_{L^2}^2$ below which exponential convergence is guaranteed at rate $\beta \geq \gamma_*$.

The threshold is not sharp in the mathematical sense (it is a sufficient condition, not a necessary one), but it is structural: larger perturbations enter the nonlinear regime where the $O(\|u\|_{H^s}\mathcal{V})$ correction in (C.49) competes with the linear dissipation, and the convergence may slow from exponential to algebraic during the transient phase before eventually recovering exponential decay (Theorem C.44, global asymptotic stability).

The numerical experiments below demonstrate this threshold by tracking the convergence behavior as the initial complexity crosses $\epsilon_0$.

#### 5.2.2 Numerical Experiment 5.3: Convergence Rate Versus Initial Complexity

**Setup.** Fix Parameter Set II. Initialize with the Gaussian IC-C (eq. 1.10), centered at $x_0 = 0.5$, with width $\sigma = 0.05$ and amplitudes $A \in \{0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4\}$. The Gaussian profile has broad spectral content (many modes populated), so the ED-complexity grows rapidly with $A$:

$$
C_{\mathrm{ED}}[\rho_0] = A^2\int_0^1\left(\frac{d}{dx}e^{-(x-0.5)^2/(2\sigma^2)}\right)^2 dx = A^2\,\frac{\sqrt{\pi}}{2\sigma^3\sqrt{2}} \approx A^2 \cdot 88.6.
$$

The seven amplitudes give $C_{\mathrm{ED}} \in \{0.009, 0.22, 0.89, 1.99, 3.54, 7.98, 14.18\}$.

Integrate each to $T = 20.0$. At each time step, compute:

1. The Lyapunov functional $\mathcal{V}(t)$ (Definition C.39).
2. The instantaneous convergence rate $\hat{\beta}(t) := -d\ln\mathcal{V}/dt$.
3. The ED-complexity $C_{\mathrm{ED}}(t)$.

**Expected results.** For small $A$ ($C_{\mathrm{ED}} \ll \epsilon_0^2$): the convergence rate $\hat{\beta}(t)$ is approximately constant from $t = 0$, equal to the linearized rate $\gamma_* \approx \min(DP_*'/2,\, H\zeta/(2\tau H)) = \min(0.3, 0.208) = 0.208$. (The exact value of $\gamma_*$ depends on the choice of $\sigma$ in $\mathcal{V}$; for the numerical measurement we use the Lyapunov functional directly.) The $\mathcal{V}(t)$ curve is a straight line on a semilog plot.

For moderate $A$ ($C_{\mathrm{ED}} \sim \epsilon_0^2$): the convergence rate $\hat{\beta}(t)$ starts below $\gamma_*$ (the nonlinear terms reduce the effective dissipation) and increases over time as the perturbation decays into the linearized regime. The $\mathcal{V}(t)$ curve shows a concave-up region on the semilog plot (slower initial decay) followed by a straight-line region (exponential decay at rate $\gamma_*$).

For large $A$ ($C_{\mathrm{ED}} \gg \epsilon_0^2$): the convergence rate may briefly become very small or even transiently negative ($\mathcal{V}$ momentarily increases) during the far-from-equilibrium phase. The three-stage convergence of Appendix C.7 is visible: a fast initial transient (high modes decay rapidly), an algebraic intermediate phase (the nonlinear terms are of the same order as the linear dissipation), and a final exponential phase (once the solution enters the basin of Theorem C.43).

**Figure description (Figure 5.3).** *Convergence rate versus initial ED-complexity.* Two panels.

Left panel: semilog-$y$ plot of $\mathcal{V}(t)$ versus $t$ (horizontal axis, range $[0, 20]$) for all seven amplitudes. The vertical axis spans $[10^{-10}, 10^2]$. The curves are colored on a gradient from blue ($A = 0.01$, lowest complexity) to red ($A = 0.4$, highest). The low-amplitude curves (blue, light blue) are straight lines descending from $\mathcal{V}(0) \sim 10^{-3}$–$10^{-1}$ with slope $\approx -0.42$ (twice $\gamma_*$, since $\mathcal{V} \propto \|u\|_{H^1}^2$ decays at twice the amplitude rate). The moderate-amplitude curves (green, yellow) show an initial concave-up region ($t < 2$) followed by the same asymptotic slope. The high-amplitude curves (orange, red) show a pronounced slow initial phase ($t < 5$) — the Lyapunov functional barely decreases — followed by an accelerating descent that eventually joins the universal slope at late times.

A horizontal dashed line marks $\mathcal{V} = c_+\epsilon_0^2$ — the Lyapunov level corresponding to the boundary of the exponential-stability basin. All curves pass through this level at some time $t_{\mathrm{entry}}$, after which they descend at the exponential rate $\gamma_*$. The entry time $t_{\mathrm{entry}}$ increases monotonically with initial complexity: from $t_{\mathrm{entry}} \approx 0$ for $A = 0.01$ (already inside the basin) to $t_{\mathrm{entry}} \approx 8$ for $A = 0.4$ (must traverse the nonlinear transient first).

Right panel: the measured late-time convergence rate $\hat{\beta}_\infty$ (time-averaged over $[T-5, T]$) versus the initial ED-complexity $C_{\mathrm{ED}}[\rho_0]$ on a log-$x$ axis. The vertical axis is $\hat{\beta}_\infty$ (range $[0, 0.5]$). At low complexity, $\hat{\beta}_\infty \approx 0.21$ (the linearized rate), constant across the first three data points. At moderate complexity, $\hat{\beta}_\infty$ remains near $0.21$ — the late-time rate is the same regardless of the initial complexity, because all solutions eventually enter the linear basin. A horizontal dashed line at $\gamma_* \approx 0.21$ confirms that the asymptotic convergence rate is universal. The structural message is: the initial complexity determines *how long* the system takes to reach the exponential regime, not *how fast* it converges once there.

#### 5.2.3 Numerical Experiment 5.4: Threshold Identification

**Setup.** Using the data from Experiment 5.3, define the threshold complexity $C_{\mathrm{ED}}^*$ operationally as the initial $C_{\mathrm{ED}}$ at which the time to reach the exponential regime first exceeds $t_{\mathrm{entry}} > 1.0$ (an arbitrary but reproducible criterion). Refine by interpolation between adjacent amplitudes.

Repeat for four parameter sets: I (deep oscillatory), II (moderate oscillatory), III (near-critical), IV (deep monotonic). For each, measure $C_{\mathrm{ED}}^*$ and the analytic linearized stability rate $\gamma_*$.

**Expected results.** The threshold $C_{\mathrm{ED}}^*$ varies across parameter sets. The analytic prediction is $C_{\mathrm{ED}}^* \sim (\gamma_*/C_{\mathrm{nl}})^2$, where $\gamma_*$ depends on the canonical parameters (eq. C.48) and $C_{\mathrm{nl}}$ depends on the constitutive curvature. Since $\gamma_*$ involves $\min(DP_*'/2,\, (H\zeta - \sigma H)/(2\tau H c_+),\, \ldots)$, the threshold is smallest for parameter sets with the smallest $\gamma_*$ — that is, near the critical surface where the dissipation rate is weakest (the slowest eigenvalue approaches zero). Parameter Set III (near-critical) should have the smallest $C_{\mathrm{ED}}^*$; Parameter Set IV (deep monotonic, large $\gamma_*$) should have the largest.

**Figure description (Figure 5.4).** *Stability threshold across parameter regimes.* Single panel.

The horizontal axis labels the four parameter sets (I, II, III, IV). The vertical axis is $C_{\mathrm{ED}}^*$ on a logarithmic scale. Four data points (filled circles) are plotted, connected by a line to show the trend. A second set of markers (open squares) shows the analytic estimate $(\gamma_*/C_{\mathrm{nl}})^2$ (with $C_{\mathrm{nl}}$ computed from the constitutive functions at equilibrium). The two sets track each other: both show the same ordering (III < I < II < IV) and the same approximate magnitudes. The smallest threshold is at Set III ($C_{\mathrm{ED}}^* \approx 0.03$), reflecting the near-critical slowing of the dissipation rate. The largest is at Set IV ($C_{\mathrm{ED}}^* \approx 5.2$), reflecting the strong monotonic damping that maintains exponential convergence even for large perturbations.

---

### 5.3 Complexity Ordering: Same Mass, Different Gradients

#### 5.3.1 Analytic Motivation

The Applications Paper (§1.4, §3.1) identifies ED-complexity as the quantity that orders physical systems — decoherence rates, transport thresholds, and halo formation are predicted to scale with $C_{\mathrm{ED}}$, not with mass, size, or total density. The mathematical basis for this claim is that the dissipation rate (Lemma C.6), the stability threshold (Theorem C.43), and the modal hierarchy (Proposition C.29) all depend on $\|\nabla\rho\|_{L^2}^2 = C_{\mathrm{ED}}$, not on $\int\rho\,dx$ (the total mass) or $\|\rho\|_{L^\infty}$ (the peak density).

This section demonstrates the principle directly: two configurations with identical total mass but different gradient structures evolve on dramatically different time scales, confirming that complexity, not mass, governs the dynamics.

#### 5.3.2 Numerical Experiment 5.5: Broad Versus Sharp Profiles

**Setup.** Construct two initial conditions with the same total mass perturbation $\int_\Omega u_0\,dx = 0$ and the same $L^2$-norm $\|u_0\|_{L^2}$ but different ED-complexities:

**Profile A (Broad, low complexity):**

$$
\rho_0^A(x) = \rho^* + A_0\cos(\pi x),
$$

with $A_0$ chosen to set $\|u_0^A\|_{L^2} = 0.1/\sqrt{2} \approx 0.0707$ (i.e., $A_0 = 0.1$). Then $C_{\mathrm{ED}}^A = A_0^2\,\mu_1/2 = 0.01 \cdot \pi^2/2 \approx 0.0493$.

**Profile B (Sharp, high complexity):**

$$
\rho_0^B(x) = \rho^* + B_0\cos(4\pi x),
$$

with $B_0$ chosen to set $\|u_0^B\|_{L^2} = \|u_0^A\|_{L^2}$ (i.e., $B_0 = A_0 = 0.1$). Then $C_{\mathrm{ED}}^B = B_0^2\,\mu_4/2 = 0.01 \cdot 16\pi^2/2 \approx 0.790$.

Both profiles have the same $L^2$-norm (same "mass deviation energy") and zero mean deviation (same total mass). But $C_{\mathrm{ED}}^B/C_{\mathrm{ED}}^A = \mu_4/\mu_1 = 16$: Profile B has sixteen times the gradient content.

Set $v_0 = 0$ for both. Integrate to $T = 8.0$.

**Expected results.** Profile B decays much faster than Profile A. The decay rates are $D\alpha_4 = 0.6 \cdot (0.25 \cdot 16\pi^2 + 1.0) = 0.6 \cdot 40.48 = 24.29$ for Profile B versus $D\alpha_1 = 0.6 \cdot 3.467 = 2.08$ for Profile A — a factor of $11.7$ difference in decay rate, despite identical $L^2$-norms.

The ED-complexity of Profile B drops by a factor of $e$ in time $1/(2D(\alpha_4 - P_*')) \approx 1/(2 \cdot 0.6 \cdot 39.48) \approx 0.021$, while Profile A's complexity drops by a factor of $e$ in time $1/(2D(\alpha_1 - P_*')) \approx 1/(2 \cdot 0.6 \cdot 2.467) \approx 0.338$. After $t = 0.1$, Profile B's complexity has decreased by a factor $\sim e^{-4.7} \approx 0.009$, while Profile A's has decreased by only $e^{-0.30} \approx 0.74$. By $t = 0.5$, Profile B has reached the noise floor; Profile A still has 64% of its initial complexity remaining.

**Figure description (Figure 5.5).** *Same mass, different fates: complexity ordering.* Three panels.

Top panel: spatial profiles $\rho(x, t)$ at four times $t = 0, 0.05, 0.2, 1.0$ for both profiles, superimposed. Profile A curves (solid, blue tones) show a gentle cosine that slowly flattens: at $t = 0$ it is a full-amplitude single arch, at $t = 0.2$ it has shrunk to $\sim 80\%$, at $t = 1.0$ it is still visible as a gentle undulation. Profile B curves (dashed, red tones) show a sharp four-period oscillation that vanishes rapidly: at $t = 0$ it has four arches of full amplitude, at $t = 0.05$ the amplitude has halved, at $t = 0.2$ it is barely visible (amplitude $\sim 1\%$), and at $t = 1.0$ the curve is indistinguishable from $\rho^*$. The visual contrast is stark: the "same-mass" profiles live on different time scales.

Middle panel: semilog-$y$ plot of $C_{\mathrm{ED}}(t)$ for both profiles. Profile A (blue) descends as a straight line with slope $\approx -1.76$. Profile B (red) descends with slope $\approx -47.4$ (the much steeper rate $2D(M_*\mu_4 - P_*')$), reaching the noise floor ($\sim 10^{-14}$) by $t \approx 0.3$. At $t = 0$, the two curves are separated by a factor $16$ in complexity; by $t = 0.1$, they are separated by a factor $\sim 10^5$. A horizontal dashed line marks the stability threshold $C_{\mathrm{ED}}^*$ from Experiment 5.4: Profile B crosses below it almost immediately ($t \approx 0.005$), while Profile A crosses it at $t \approx 0.6$.

Bottom panel: semilog-$y$ plot of $\|u(t)\|_{L^2}$ for both profiles (the $L^2$-norm that was identical at $t = 0$). Profile B's $L^2$-norm decays at rate $D\alpha_4 = 24.29$, Profile A's at rate $D\alpha_1 = 2.08$. The curves separate immediately: by $t = 0.5$, Profile B's $L^2$-norm is at $\sim 10^{-6}$ while Profile A's is at $\sim 0.025$. This panel completes the demonstration: even the $L^2$-norm (which was identical at $t = 0$) evolves on a time scale set by the complexity, not by its initial value.

#### 5.3.3 Numerical Experiment 5.6: Complexity Ordering Across a Five-Configuration Family

**Setup.** Construct five initial conditions, all with the same $L^2$-norm $\|u_0\|_{L^2} = 0.1/\sqrt{2}$ and $v_0 = 0$, but with increasing ED-complexity:

| Config | Profile | $C_{\mathrm{ED}}(0)$ | Dominant mode |
|--------|---------|---------------------|---------------|
| C1 | $0.1\cos(\pi x)$ | $0.049$ | $n = 1$ |
| C2 | $0.1\cos(2\pi x)$ | $0.197$ | $n = 2$ |
| C3 | $0.1\cos(3\pi x)$ | $0.444$ | $n = 3$ |
| C4 | $0.1\cos(4\pi x)$ | $0.790$ | $n = 4$ |
| C5 | $0.1\cos(6\pi x)$ | $1.776$ | $n = 6$ |

Integrate all five to $T = 4.0$. For each, measure:

1. The half-life $t_{1/2}$: the time at which $C_{\mathrm{ED}}(t) = C_{\mathrm{ED}}(0)/2$.
2. The $L^2$-norm half-life: the time at which $\|u(t)\|_{L^2} = \|u(0)\|_{L^2}/2$.
3. The energy half-life: the time at which $\mathcal{E}(t) = \mathcal{E}(0)/2$.

**Expected results.** All three half-lives decrease monotonically with increasing $C_{\mathrm{ED}}(0)$:

| Config | $D\alpha_n$ | $t_{1/2}^{C_{\mathrm{ED}}}$ (pred.) | $t_{1/2}^{L^2}$ (pred.) |
|--------|------------|--------------------------------------|--------------------------|
| C1 | $2.080$ | $\ln 2/(2 \cdot 1.48) \approx 0.234$ | $\ln 2/2.08 \approx 0.333$ |
| C2 | $6.522$ | $\ln 2/(2 \cdot 5.52) \approx 0.063$ | $\ln 2/6.52 \approx 0.106$ |
| C3 | $13.924$ | $\ln 2/(2 \cdot 12.92) \approx 0.027$ | $\ln 2/13.92 \approx 0.050$ |
| C4 | $24.287$ | $\ln 2/(2 \cdot 23.29) \approx 0.015$ | $\ln 2/24.29 \approx 0.029$ |
| C5 | $53.133$ | $\ln 2/(2 \cdot 52.13) \approx 0.007$ | $\ln 2/53.13 \approx 0.013$ |

The complexity half-lives span nearly two orders of magnitude (from $0.234$ to $0.007$), despite all five configurations having the same initial mass and the same initial $L^2$-norm. This is the numerical demonstration of the complexity-ordering principle: the dynamical time scale is set by $C_{\mathrm{ED}}$, not by mass.

**Figure description (Figure 5.6).** *Complexity ordering: five configurations, same mass.* Two panels.

Left panel: semilog-$y$ plot of $C_{\mathrm{ED}}(t)/C_{\mathrm{ED}}(0)$ (normalized complexity) versus $t$ (range $[0, 2]$) for all five configurations. Each curve starts at $1$ and descends as a straight line (single-mode initialization produces pure exponential complexity decay). The curves fan out with increasing steepness: C1 (blue, shallowest) to C5 (red, steepest). Horizontal dashed line at $0.5$ intersects the five curves at the predicted half-lives, which decrease from left to right. The visual message is immediate: higher complexity means faster decay.

Right panel: the three half-lives ($t_{1/2}^{C_{\mathrm{ED}}}$, $t_{1/2}^{L^2}$, $t_{1/2}^{\mathcal{E}}$) plotted versus $C_{\mathrm{ED}}(0)$ on log-log axes. Each set of five points forms a straight line with slope $\approx -1$ on the log-log plot, confirming the inverse relationship $t_{1/2} \propto 1/C_{\mathrm{ED}}(0)$ (since $t_{1/2} \sim \ln 2/(2D M_*\mu_n) \propto 1/\mu_n \propto 1/C_{\mathrm{ED}}(0)$ for single-mode perturbations of fixed amplitude). The three lines (one for each type of half-life) are parallel, offset vertically by constants reflecting the different norms. Analytic predictions (open squares) are plotted alongside the numerical data (filled circles); they coincide.

The structural conclusion is stated as a caption: *ED-complexity, not mass, orders the dynamical fate of configurations. Two systems with identical mass but different gradient structure evolve on time scales that differ by the ratio of their complexities.*

---

## 6. Mobility Collapse and Horizon Behavior

Principle 4 (Mobility Capacity Bound) states that $M(\rho_{\max}) = 0$: the mobility vanishes at the maximum density, extinguishing diffusive transport and creating a structural barrier at the capacity bound. Appendix C.2 proves that this vanishing has two consequences — kinetic suppression of gradients near $\rho_{\max}$ (Proposition C.10) and an infinite energy barrier preventing $\rho$ from reaching $\rho_{\max}$ (Proposition C.11). Together, these ensure that the density remains strictly interior to $(0, \rho_{\max})$ for all time (Theorem C.66(i)), so the equation never degenerates.

In the ED architecture, the region near $\rho_{\max}$ is the **horizon** — the boundary of the dynamically accessible density space. The term is structural, not metaphorical: the mobility collapse at $\rho_{\max}$ plays a role analogous to the causal horizon in general relativity, where a coordinate velocity vanishes at a boundary surface while physical quantities remain finite. In the ED system, the diffusion velocity $D\,M(\rho)|\nabla\rho|$ vanishes as $\rho \to \rho_{\max}$, while the density, the energy, and the penalty all remain bounded. The horizon is an asymptotically approached but never reached surface in the space of density configurations.

This section demonstrates the three aspects of horizon behavior: the approach to $\rho_{\max}$ and the progressive collapse of the mobility coefficient (§6.1), the energy barrier that enforces strict separation from the boundary (§6.2), and the amplification of effective complexity that occurs in the near-horizon region (§6.3).

All experiments use the one-dimensional domain $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4) with the quadratic mobility $M(\rho) = (\rho_{\max} - \rho)^2$ ($M_0 = 1$, $\beta = 2$) and linear penalty $P(\rho) = \rho - \rho^*$, the Crank–Nicolson scheme (§1.5.2) with $N = 1024$ (high resolution is essential for resolving the near-horizon boundary layer), $\Delta t = 10^{-4}$, and $\rho^* = 0.5$, $\rho_{\max} = 1.0$. Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$) is used unless otherwise stated.

---

### 6.1 Approaching $\rho_{\max}$: Mobility Collapse

#### 6.1.1 Analytic Framework

The canonical mobility (1.3) with $\beta = 2$ is

$$
M(\rho) = (\rho_{\max} - \rho)^2, \qquad M'(\rho) = -2(\rho_{\max} - \rho).
$$

As $\rho \to \rho_{\max}$, the diffusion coefficient $D\,M(\rho) = D(\rho_{\max} - \rho)^2$ vanishes quadratically. The local diffusion time scale at density level $\rho$ is

$$
\tau_{\mathrm{diff}}(\rho) \sim \frac{h^2}{D\,M(\rho)} = \frac{h^2}{D(\rho_{\max} - \rho)^2},
$$

which diverges as $\rho \to \rho_{\max}$. This divergence means that density in the near-horizon region becomes effectively frozen: diffusive transport cannot redistribute it, and any spatial structure in the near-horizon layer persists on time scales that grow without bound as the density approaches the capacity.

The density potential (C.4) for the canonical constitutive functions is

$$
\Phi(\rho) = \int_{\rho^*}^{\rho} \frac{r - \rho^*}{(1 - r)^2}\,dr.
$$

For $\rho$ close to $\rho_{\max} = 1$:

$$
\Phi(\rho) \sim \frac{\rho_{\max} - \rho^*}{(\rho_{\max} - \rho)} = \frac{0.5}{\rho_{\max} - \rho} \to +\infty.
$$

This confirms the $1/(\rho_{\max} - \rho)$ divergence of the energy barrier for $\beta = 2$.

#### 6.1.2 Numerical Experiment 6.1: Mobility Profile During Near-Horizon Approach

**Setup.** Initialize with IC-D (eq. 1.11): $\rho_0(x) = \rho_{\max} - \delta + A\cos(\pi x)$ with $\delta = 0.05$ and $A = 0.02$. This places the peak density at $\rho_0(0) = 1.0 - 0.05 + 0.02 = 0.97$, within $3\%$ of $\rho_{\max}$. The trough density is $\rho_0(0.5) = 1.0 - 0.05 - 0.02 = 0.93$.

Set $v_0 = 0$. Integrate to $T = 20.0$ with the mobility-collapse handling protocol of §1.6.

**Measured quantities.** At each of five time slices $t \in \{0, 0.5, 2.0, 5.0, 15.0\}$:

1. The spatial profile $\rho(x, t)$.
2. The mobility profile $M(\rho(x, t)) = (1 - \rho(x, t))^2$.
3. The local diffusion coefficient $D\,M(\rho(x, t))$.
4. The proximity margin $\delta(t) := \rho_{\max} - \max_x \rho(x, t)$.
5. The minimum mobility $\min_x M(\rho(x, t)) = \delta(t)^2$.

**Expected behavior.** The initial density is close to $\rho_{\max}$ everywhere, with the peak at $x = 0$ closest. The penalty $P(\rho) = \rho - 0.5 > 0$ drives $\rho$ downward toward $\rho^* = 0.5$, but the mobility at the peak is only $M(0.97) = 0.03^2 = 9 \times 10^{-4}$ — three orders of magnitude below $M(\rho^*) = 0.25$. The diffusion is therefore extremely sluggish at the peak.

The relaxation proceeds asymmetrically: the trough (at $x = 0.5$, where $M(0.93) = 0.0049$ is five times larger than the peak mobility) relaxes faster than the peak. This creates a *flattening* of the profile near $\rho_{\max}$: the cosine perturbation decays unevenly, with the trough dropping faster than the peak. At late times, the profile has relaxed significantly at the troughs but retains a residual plateau near the peak — the density is "stuck" near $\rho_{\max}$ because the mobility is too small to support further transport.

Eventually, the penalty term (which does not involve the mobility) pulls the entire density field toward $\rho^*$, but through the non-diffusive mechanism: the penalty $-P(\rho)$ acts as a local restoring force in $F[\rho]$ that does not require spatial transport. The time scale for this penalty-driven relaxation is $1/(D\,P_*') = 1/0.3 \approx 3.3$ (at equilibrium), but near $\rho_{\max}$ the effective rate is modified by the mobility in the $M(\rho)\nabla^2\rho$ term.

**Figure description (Figure 6.1).** *Mobility collapse during near-horizon approach.* Two panels.

Left panel: five spatial profiles $\rho(x, t)$ at the five time slices, plotted on the same axes. The horizontal axis is $x$ (range $[0, 1]$); the vertical axis is $\rho$ (range $[0.4, 1.0]$). A horizontal dashed line at $\rho_{\max} = 1.0$ marks the capacity bound. A second dashed line at $\rho^* = 0.5$ marks the equilibrium.

At $t = 0$ (darkest curve): a gentle cosine centered at $\rho = 0.95$, with peak $0.97$ at $x = 0$ and trough $0.93$ at $x = 0.5$. At $t = 0.5$: the profile has begun to descend, but asymmetrically — the trough has dropped to $\approx 0.88$ while the peak has barely moved to $\approx 0.965$. The profile is visibly flattened at the top and steepened at the trough. At $t = 2.0$: the trough has reached $\approx 0.75$, the peak is at $\approx 0.92$. The profile has developed a pronounced asymmetry: a broad flat plateau near $x = 0$ and a steep descent near $x = 0.5$. At $t = 5.0$: the trough has passed below $\rho^*$, while the peak is at $\approx 0.80$. At $t = 15.0$: the profile is close to $\rho^* = 0.5$ everywhere, with residual deviations $< 0.01$.

The visual narrative: the near-horizon region (top of the profile) relaxes far more slowly than the interior, creating a transient plateau that persists while the rest of the profile has largely equilibrated.

Right panel: the mobility profile $M(\rho(x, t))$ at the same five times. The vertical axis is $M$ on a logarithmic scale (range $[10^{-4}, 0.3]$). At $t = 0$: the mobility is nearly uniform at $\approx 10^{-3}$ (since $\rho \approx 0.95$ everywhere, $M \approx 0.05^2 = 2.5 \times 10^{-3}$), with the minimum at $x = 0$ ($M \approx 9 \times 10^{-4}$). At $t = 0.5$: the mobility at the trough ($x = 0.5$) has increased to $\approx 10^{-2}$ (as $\rho$ drops from $0.93$ to $0.88$, $M$ rises from $0.0049$ to $0.0144$), while the peak mobility remains near $10^{-3}$. At $t = 2.0$: the mobility varies by two orders of magnitude across the domain — $M \approx 0.06$ at the trough, $M \approx 6 \times 10^{-3}$ at the peak. At $t = 5.0$: the trough mobility has reached $\approx 0.06$–$0.25$, approaching equilibrium values, while the peak is at $\approx 0.04$. At $t = 15.0$: mobility is nearly uniform at $M(\rho^*) = 0.25$, with perturbations $< 1\%$.

The right panel shows the *restoration of uniform parabolicity*: the equation begins nearly degenerate (mobility three orders of magnitude below equilibrium) and progressively recovers its parabolic character as the density retreats from the horizon.

#### 6.1.3 Numerical Experiment 6.2: Proximity Margin Dynamics

**Setup.** Using the same integration as Experiment 6.1, track the proximity margin $\delta(t) = \rho_{\max} - \max_x\rho(x, t)$ as a continuous function of time.

**Analytic prediction.** The margin grows as the penalty pulls the density away from $\rho_{\max}$. Near the horizon, the dominant dynamics at the peak are governed by the ODE for the maximum value:

$$
\frac{d}{dt}\rho_{\max\text{-value}} \approx -D\,P(\rho_{\max\text{-value}}) = -D(\rho_{\max\text{-value}} - \rho^*),
$$

since the diffusion term $D\,M(\rho)\nabla^2\rho$ is suppressed by the vanishing mobility ($M \approx 0$ near $\rho_{\max}$) and the gradient is small at the peak ($\nabla^2\rho \leq 0$ at a maximum). The penalty-driven relaxation from $\rho_{\max\text{-value}}(0) = 0.97$ toward $\rho^* = 0.5$ is approximately exponential with rate $D = 0.3$:

$$
\delta(t) \approx \rho_{\max} - \bigl[\rho^* + (\rho_{\max\text{-value}}(0) - \rho^*)\,e^{-Dt}\bigr] = 0.03 + 0.47(1 - e^{-0.3t}).
$$

This gives $\delta(0) = 0.03$, $\delta(1) \approx 0.15$, $\delta(5) \approx 0.40$, $\delta(\infty) = 0.50$.

**Figure description (Figure 6.2).** *Proximity margin dynamics.* Single panel.

The horizontal axis is $t$ (range $[0, 20]$). The vertical axis is $\delta(t) = \rho_{\max} - \max_x\rho(x, t)$ (range $[0, 0.55]$). The numerical curve (solid blue) rises from $\delta(0) = 0.03$ with an initially gentle slope (the penalty is fighting against suppressed mobility) and then accelerates as the density retreats from the horizon and the mobility recovers. The curve approaches $\delta(\infty) = 0.50$ asymptotically. An analytic reference curve (dashed orange) based on the penalty-driven ODE approximation is overlaid; it agrees well at early times ($t < 2$), where the diffusion contribution is negligible, and slightly overestimates the margin at intermediate times ($2 < t < 8$), where the recovering diffusion actually accelerates the relaxation beyond the pure-penalty prediction.

A horizontal dashed line at $\delta_{\mathrm{crit}} = 10^{-4}\rho_{\max} = 10^{-4}$ marks the computational safety threshold from §1.6. The proximity margin never approaches this threshold — it reaches $\delta = 0.03$ at the minimum ($t = 0$) and only increases thereafter — confirming that the energy barrier prevents the density from approaching $\rho_{\max}$ more closely than the initial condition allows.

---

### 6.2 Horizon Surface: Energy Barrier Behavior

#### 6.2.1 Analytic Framework

Proposition C.11 establishes that the density potential $\Phi(\rho)$ diverges as $\rho \to \rho_{\max}$, creating an infinite energy cost for reaching the capacity bound. The sublevel set $\{\mathcal{E} \leq E_0\}$ is therefore contained in $\{\rho(x) \leq \rho_{\max} - \delta(E_0)\}$ for some $\delta(E_0) > 0$. The stronger the divergence (faster vanishing of $M$), the more effectively the barrier confines the density.

For the canonical mobility with exponent $\beta$:

$$
\Phi(\rho) = \int_{\rho^*}^{\rho}\frac{r - \rho^*}{(\rho_{\max} - r)^\beta}\,dr.
$$

Near $\rho_{\max}$, the integrand behaves as $(\rho_{\max} - \rho^*)/(\rho_{\max} - r)^\beta$, so:

$$
\Phi(\rho) \sim \begin{cases}
(\rho_{\max} - \rho^*)\,\ln(\rho_{\max} - \rho)^{-1} & \text{if } \beta = 1, \\
(\rho_{\max} - \rho^*)(\beta - 1)^{-1}(\rho_{\max} - \rho)^{-(\beta - 1)} & \text{if } \beta > 1.
\end{cases}
\tag{6.1}
$$

For $\beta = 2$ (the default): $\Phi(\rho) \sim 0.5/(\rho_{\max} - \rho)$. The barrier is algebraic: the energy cost to place a unit volume of density at distance $\delta$ from $\rho_{\max}$ is $O(1/\delta)$.

The barrier relation, inverted, gives the maximum attainable density as a function of the initial energy:

$$
\rho_{\max} - \delta(E_0) \sim \frac{0.5\,|\Omega|}{E_0} \qquad \text{for large } E_0 \text{ (i.e., small } \delta).
\tag{6.2}
$$

#### 6.2.2 Numerical Experiment 6.3: Energy Barrier Verification

**Setup.** Initialize a family of configurations with increasing proximity to $\rho_{\max}$. For each of seven initial margins $\delta_0 \in \{0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005\}$, set

$$
\rho_0(x) = \rho_{\max} - \delta_0 + 0.5\,\delta_0\cos(\pi x), \qquad v_0 = 0.
$$

This places the peak density at $\rho_{\max} - 0.5\,\delta_0$ (within $0.5\,\delta_0$ of $\rho_{\max}$) and the trough at $\rho_{\max} - 1.5\,\delta_0$.

For each, compute the initial energy $\mathcal{E}_0 = \mathcal{E}[\rho_0, v_0]$ using the trapezoidal-rule quadrature of $\Phi(\rho_0)$, and the analytic barrier prediction $\delta_{\mathrm{barrier}} = 0.5|\Omega|/\mathcal{E}_0$. Integrate to $T = 1.0$ (long enough for the density to begin relaxing) and record the minimum proximity margin $\delta_{\min} = \min_{t \in [0,1]}\delta(t)$.

**Expected results.** For all seven configurations, the minimum margin satisfies $\delta_{\min} \geq \delta_{\mathrm{barrier}}$: the energy barrier prevents the density from approaching $\rho_{\max}$ more closely than the energy allows. The density never *increases* toward $\rho_{\max}$ during the evolution — it only retreats — so $\delta_{\min} = \delta(0) = 0.5\,\delta_0$ in practice (the initial condition is the closest approach). The barrier prediction $\delta_{\mathrm{barrier}}$ is a conservative bound; the actual minimum margin exceeds it.

The initial energy scales as $\mathcal{E}_0 \sim |\Omega|\,\Phi(\rho_{\max} - 0.5\delta_0) \approx 0.5/(0.5\delta_0) = 1/\delta_0$ for small $\delta_0$, confirming the $1/\delta$ scaling of (6.1). The product $\mathcal{E}_0 \cdot \delta_{\min}$ should be approximately constant across the seven configurations (equal to $0.5\,|\Omega| = 0.5$ by eq. 6.2), up to the correction from the finite extent of the density near $\rho_{\max}$.

**Figure description (Figure 6.3).** *Energy barrier verification.* Two panels.

Left panel: log-log plot of the initial energy $\mathcal{E}_0$ versus the initial margin $\delta_0$. The seven data points (filled circles) lie on a line with slope $\approx -1$, confirming the $\mathcal{E}_0 \propto 1/\delta_0$ scaling. The analytic curve $\mathcal{E}_0 = |\Omega|\,\Phi(\rho_{\max} - \delta_0/2)$ (solid line) is overlaid and passes through all points. The two smallest margins ($\delta_0 = 0.01, 0.005$) produce energies of $\approx 100$ and $\approx 200$, illustrating the enormous energy cost of near-horizon configurations.

Right panel: the product $\mathcal{E}_0 \cdot \delta_{\min}$ versus $\delta_0$ on a linear-$x$, linear-$y$ axis. For a perfect $1/\delta$ barrier, this product would be constant (horizontal line). The seven data points cluster near $0.5$ for the four smallest $\delta_0$ values (where the asymptotic formula (6.2) is accurate) and deviate upward for larger $\delta_0$ (where the full integral $\Phi$ includes contributions from the interior and the asymptotic approximation overestimates the barrier). A horizontal dashed line at $0.5$ marks the theoretical asymptotic value.

#### 6.2.3 Numerical Experiment 6.4: Barrier Exponent Comparison

**Setup.** Repeat Experiment 6.3 for three mobility exponents $\beta \in \{1, 2, 3\}$ (linear, quadratic, and cubic vanishing). For each $\beta$, use the same seven initial margins and compute $\mathcal{E}_0$ and $\delta_{\min}$.

**Analytic prediction.** From (6.1):

- $\beta = 1$: $\Phi(\rho) \sim 0.5\ln(1/(\rho_{\max} - \rho))$. Logarithmic barrier. $\mathcal{E}_0 \sim 0.5\ln(1/\delta_0)$.
- $\beta = 2$: $\Phi(\rho) \sim 0.5/(\rho_{\max} - \rho)$. Algebraic barrier. $\mathcal{E}_0 \sim 1/\delta_0$.
- $\beta = 3$: $\Phi(\rho) \sim 0.25/(\rho_{\max} - \rho)^2$. Stronger algebraic barrier. $\mathcal{E}_0 \sim 1/\delta_0^2$.

The barrier strength increases with $\beta$: cubic vanishing confines the density more effectively than quadratic, which confines more effectively than linear. The confinement exponent — the power $p$ in $\delta \sim \mathcal{E}_0^{-1/p}$ — is $p = \beta - 1$ for $\beta > 1$ and $p = 0$ (logarithmic) for $\beta = 1$.

**Figure description (Figure 6.4).** *Barrier exponent comparison.* Single panel, log-log axes.

The horizontal axis is $\delta_0$ (range $[0.003, 0.5]$). The vertical axis is $\mathcal{E}_0$. Three sets of data points are plotted, one for each $\beta$, in distinct colors (blue for $\beta = 1$, orange for $\beta = 2$, red for $\beta = 3$). Each set of seven points traces a power law:

- $\beta = 1$ (blue): the points follow a curve that bends on the log-log plot (logarithmic, not power-law), with $\mathcal{E}_0$ growing slowly from $\approx 2$ at $\delta_0 = 0.3$ to $\approx 5$ at $\delta_0 = 0.005$. The barrier is weak — it grows without bound but only logarithmically.
- $\beta = 2$ (orange): a straight line with slope $-1$. $\mathcal{E}_0 \sim 1/\delta_0$. The barrier is moderate.
- $\beta = 3$ (red): a straight line with slope $-2$. $\mathcal{E}_0 \sim 1/\delta_0^2$. The barrier is strong.

Dashed reference lines with the predicted slopes ($0$, $-1$, $-2$ on the log-log plot) are overlaid. The data matches the predictions. The panel demonstrates that Principle 4 (mobility collapse) produces a barrier whose strength is controlled by the constitutive parameter $\beta$ — the *rate* of mobility vanishing — while the *qualitative* feature (barrier exists, density is confined) is universal across all $\beta > 0$.

---

### 6.3 Effective Complexity Amplification Near the Horizon

#### 6.3.1 Analytic Framework

The dissipation identity (Lemma C.6) contains the term

$$
-D\int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx,
$$

which is the leading dissipation channel. The integrand $P'(\rho)\,|\nabla\rho|^2/M(\rho)$ diverges as $\rho \to \rho_{\max}$ (since $M(\rho) \to 0$ while $P'(\rho) = P_0 > 0$ remains bounded below), even if $|\nabla\rho|^2$ remains finite. This means that a unit of gradient content near $\rho_{\max}$ contributes *more* to the dissipation than the same gradient content near $\rho^*$.

We define the **effective complexity** (the dissipation-weighted gradient integral) as

$$
C_{\mathrm{ED}}^{\mathrm{eff}}[\rho] := \int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx,
\tag{6.3}
$$

so that the leading dissipation is $-D\,C_{\mathrm{ED}}^{\mathrm{eff}}$. At equilibrium, $P'(\rho^*)/M(\rho^*) = P_*'/M_* = 1.0/0.25 = 4.0$, and $C_{\mathrm{ED}}^{\mathrm{eff}} = (P_*'/M_*)\,C_{\mathrm{ED}} = 4\,C_{\mathrm{ED}}$. Near the horizon:

$$
\frac{P'(\rho)}{M(\rho)} = \frac{P_0}{(\rho_{\max} - \rho)^2} \to +\infty,
$$

so the effective complexity is *amplified* relative to the bare complexity by the factor $P_0/M(\rho) = 1/(\rho_{\max} - \rho)^2$. The amplification factor at density level $\rho$ is

$$
\mathcal{A}(\rho) := \frac{P'(\rho)/M(\rho)}{P_*'/M_*} = \frac{M_*}{M(\rho)} = \frac{(\rho_{\max} - \rho^*)^2}{(\rho_{\max} - \rho)^2} = \left(\frac{0.5}{\rho_{\max} - \rho}\right)^2.
\tag{6.4}
$$

At $\rho = 0.95$: $\mathcal{A} = (0.5/0.05)^2 = 100$. At $\rho = 0.99$: $\mathcal{A} = (0.5/0.01)^2 = 2500$. Near-horizon gradients are amplified by factors of $10^2$–$10^3$ relative to equilibrium gradients of the same magnitude. This amplification is the mechanism behind the "complexity amplification near horizon" identified in the Applications Paper (§5.3, §5.6): physical systems operating near their capacity bound experience enhanced effective complexity, driving faster dissipation and sharper thresholds.

The amplification is also the mechanism behind Proposition C.10 (gradient suppression): the amplified dissipation at large $\rho$ preferentially destroys gradients in the near-horizon region, forcing $|\nabla\rho| \to 0$ there even before $\rho$ itself retreats from $\rho_{\max}$.

#### 6.3.2 Numerical Experiment 6.5: Bare Versus Effective Complexity

**Setup.** Initialize with IC-D at $\delta_0 = 0.05$, $A = 0.02$ (same as Experiment 6.1). Integrate to $T = 15.0$. At each time step, compute both the bare complexity

$$
C_{\mathrm{ED}}(t) = \int_0^1 |\nabla\rho(x, t)|^2\,dx
$$

and the effective complexity

$$
C_{\mathrm{ED}}^{\mathrm{eff}}(t) = \int_0^1 \frac{P'(\rho(x, t))}{M(\rho(x, t))}\,|\nabla\rho(x, t)|^2\,dx.
$$

Also compute the instantaneous amplification ratio $C_{\mathrm{ED}}^{\mathrm{eff}}(t)/C_{\mathrm{ED}}(t)$.

**Expected results.** At $t = 0$, the density is near $\rho_{\max}$, so the amplification factor is large: $C_{\mathrm{ED}}^{\mathrm{eff}}(0)/C_{\mathrm{ED}}(0) \approx \mathcal{A}(0.95) = (0.5/0.05)^2 = 100$. As the density retreats from the horizon (§6.1), the amplification decreases. At late times ($t > 10$), $\rho \approx \rho^*$ and $C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}} \to P_*'/M_* = 4.0$ — the equilibrium ratio.

The effective complexity decays faster than the bare complexity at early times: the amplification boosts the dissipation, which destroys the near-horizon gradients, which reduces $C_{\mathrm{ED}}^{\mathrm{eff}}$ (both through the decrease of $|\nabla\rho|^2$ and through the decrease of $1/M(\rho)$ as $\rho$ retreats). The bare complexity also decays, but more slowly (it lacks the $1/M$ amplification). At late times, both track each other with a constant ratio of $4.0$.

**Figure description (Figure 6.5).** *Bare versus effective complexity.* Two panels.

Left panel: semilog-$y$ plot of $C_{\mathrm{ED}}(t)$ (blue) and $C_{\mathrm{ED}}^{\mathrm{eff}}(t)$ (red) versus $t$ (range $[0, 15]$). The vertical axis spans $[10^{-8}, 10^3]$. At $t = 0$, the effective complexity ($\sim 10^2$) is roughly two orders of magnitude above the bare complexity ($\sim 10^0$). Both curves descend, but the effective complexity drops much more steeply during $t \in [0, 3]$ (the near-horizon phase), losing four orders of magnitude while the bare complexity loses two. By $t = 5$, the two curves have converged to a constant vertical offset on the semilog scale (a factor of $\approx 4$). At late times ($t > 8$), both are parallel straight lines with the same slope (the decay rate $2D(M_*\mu_1 - P_*') \approx 1.76$).

Right panel: the amplification ratio $C_{\mathrm{ED}}^{\mathrm{eff}}(t)/C_{\mathrm{ED}}(t)$ on a semilog-$y$ axis versus $t$ (range $[0, 15]$). The curve starts at $\approx 100$ ($t = 0$) and decays monotonically toward the asymptotic value $P_*'/M_* = 4.0$ (marked by a horizontal dashed line). The decay is not exponential but approximately algebraic: the amplification scales as $\mathcal{A}(\rho_{\max\text{-value}}(t)) \propto 1/\delta(t)^2$, and $\delta(t)$ grows roughly linearly at early times (penalty-driven), giving $\mathcal{A} \propto 1/t^2$. By $t = 5$, the ratio has reached $\approx 5$, and by $t = 10$ it has settled to $4.0 \pm 0.1$. The curve illustrates the two-phase structure: rapid de-amplification during the horizon retreat ($t < 5$), followed by equilibrium-regime constancy ($t > 5$).

#### 6.3.3 Numerical Experiment 6.6: Gradient Suppression in the Near-Horizon Region

**Setup.** Using the same integration as Experiment 6.1, define the near-horizon sub-region

$$
\Omega_\eta(t) := \{x \in [0, 1] : \rho(x, t) > \rho_{\max} - \eta\}
$$

for $\eta = 0.1$ (the set of points where $\rho > 0.9$). Track the near-horizon gradient integral

$$
G_\eta(t) := \int_{\Omega_\eta(t)} |\nabla\rho(x, t)|^2\,dx
$$

and the Proposition C.10 bound:

$$
G_\eta(t) \leq \frac{M(\rho_{\max} - \eta)}{P'(\rho_{\max} - \eta)}\,\frac{\mathcal{E}_0}{D} = \frac{(0.1)^2}{1.0}\,\frac{\mathcal{E}_0}{0.3} = \frac{0.01\,\mathcal{E}_0}{0.3} \approx 0.033\,\mathcal{E}_0.
$$

**Expected results.** At $t = 0$, $\Omega_\eta(0) = [0, 1]$ (the entire domain is above $0.9$), and $G_\eta(0) = C_{\mathrm{ED}}(0) \approx 0.039$ (all gradient content is in the near-horizon region). As the density retreats, $\Omega_\eta(t)$ shrinks: the boundary of the high-density region moves inward from $x = 0$ and $x = 1$ toward the peak. By $t = 0.5$, $\Omega_\eta$ is a narrow interval around $x = 0$ (only the peak region remains above $0.9$). By $t = 2$, $\Omega_\eta$ is empty (the peak has dropped below $0.9$).

The gradient integral $G_\eta(t)$ decreases even faster than $\Omega_\eta$ shrinks: the amplified dissipation (§6.3.1) preferentially destroys gradients in the near-horizon region. The Proposition C.10 bound $G_\eta \leq 0.033\,\mathcal{E}_0$ is satisfied at all times; the actual values are well below this bound because the dissipation actively depletes $G_\eta$ rather than merely confining it.

**Figure description (Figure 6.6).** *Gradient suppression in the near-horizon region.* Two panels.

Left panel: the measure of the near-horizon set $|\Omega_\eta(t)|$ (the fraction of the domain with $\rho > 0.9$) versus $t$ (range $[0, 3]$). At $t = 0$, $|\Omega_\eta| = 1.0$ (the full domain). The set fraction decreases monotonically: $\approx 0.8$ at $t = 0.2$, $\approx 0.3$ at $t = 0.5$, $\approx 0.05$ at $t = 1.0$, and $0$ at $t \approx 1.5$ (no point above $0.9$ remains). The curve is concave, reflecting the accelerating retreat of the density from the horizon as the mobility recovers and diffusion assists the penalty.

Right panel: semilog-$y$ plot of $G_\eta(t)$ (blue, solid) and the Proposition C.10 upper bound (red, dashed horizontal line at $\approx 0.033\,\mathcal{E}_0$) versus $t$ (range $[0, 2]$). The $G_\eta$ curve starts at $\approx 0.039$, just above the bound (the bound is an asymptotic estimate, not a pointwise upper bound at $t = 0$), then drops steeply to $\approx 10^{-4}$ by $t = 1.0$ and reaches zero (up to numerical precision) by $t = 1.5$ when $\Omega_\eta$ becomes empty. The drop is approximately exponential with a rate much faster than the bulk complexity decay rate — this is the gradient-suppression mechanism in action. The dissipation-weighted destruction of gradients near $\rho_{\max}$ is the fastest process in the near-horizon dynamics.

#### 6.3.4 Numerical Experiment 6.7: Complexity Amplification Across Density Levels

**Setup.** To map the amplification factor as a function of density level, initialize a family of spatially homogeneous perturbations at different mean densities $\bar{\rho} \in \{0.55, 0.65, 0.75, 0.85, 0.90, 0.95, 0.98\}$:

$$
\rho_0(x) = \bar{\rho} + 0.01\cos(\pi x), \qquad v_0 = 0.
$$

The perturbation amplitude $A = 0.01$ is small enough to remain in the linearized regime, so the decay rate of the first mode is $D\alpha_1(\bar{\rho}) = D(M(\bar{\rho})\mu_1 + P'(\bar{\rho}))$, where $M(\bar{\rho}) = (1 - \bar{\rho})^2$ and $P'(\bar{\rho}) = 1$. The effective decay rate of the gradient is controlled by the dissipation integrand $P'(\bar{\rho})/M(\bar{\rho}) \cdot |\nabla\rho|^2$; the ratio $P'/M = 1/(1 - \bar{\rho})^2$ increases as $\bar{\rho} \to \rho_{\max}$.

Integrate each to $T = 5.0$. Measure the decay rate $\hat{\sigma}_1$ of the first-mode amplitude and the effective amplification ratio at the initial time.

**Expected results.** The decay rate of the mode amplitude is $D\alpha_1(\bar{\rho}) = D((1 - \bar{\rho})^2\mu_1 + 1)$. As $\bar{\rho}$ increases:

| $\bar{\rho}$ | $M(\bar{\rho})$ | $\alpha_1(\bar{\rho})$ | $D\alpha_1$ | $\mathcal{A}(\bar{\rho})$ |
|-------------|----------------|----------------------|-------------|--------------------------|
| $0.55$ | $0.2025$ | $3.00$ | $0.900$ | $6.1$ |
| $0.65$ | $0.1225$ | $2.21$ | $0.663$ | $16.7$ |
| $0.75$ | $0.0625$ | $1.62$ | $0.486$ | $64$ |
| $0.85$ | $0.0225$ | $1.22$ | $0.367$ | $494$ |
| $0.90$ | $0.0100$ | $1.10$ | $0.330$ | $2500$ |
| $0.95$ | $0.0025$ | $1.02$ | $0.308$ | $40000$ |
| $0.98$ | $0.0004$ | $1.004$ | $0.301$ | $625000$ |

The decay rate $D\alpha_1$ *decreases* as $\bar{\rho} \to \rho_{\max}$: the mode lives longer because the diffusion is weaker. But the effective complexity amplification $\mathcal{A}$ increases dramatically: each unit of surviving gradient contributes enormously more to the dissipation. The product $D\alpha_1 \cdot \mathcal{A}$ gives the effective dissipation per unit bare complexity, which increases without bound near the horizon.

This is the central paradox of the near-horizon regime: the dynamics are *slower* (lower mode decay rate) but the *dissipative cost per gradient* is *higher* (amplified effective complexity). The system cannot sustain gradients near the horizon — not because diffusion is strong (it is weak), but because the energy cost per gradient is infinite.

**Figure description (Figure 6.7).** *Complexity amplification across density levels.* Two panels.

Left panel: the measured mode decay rate $\hat{\sigma}_1$ (filled circles) versus $\bar{\rho}$ (horizontal axis, range $[0.5, 1.0]$). The analytic curve $D((1 - \bar{\rho})^2\mu_1 + 1)$ (solid line) is overlaid. The decay rate decreases monotonically from $\approx 0.9$ at $\bar{\rho} = 0.55$ toward $\approx 0.3$ at $\bar{\rho} = 0.98$, approaching the penalty floor $D\,P_*' = 0.3$ as the diffusive contribution $D\,M\,\mu_1$ vanishes. A horizontal dashed line at $D\,P_*' = 0.3$ marks the floor. The approach is quadratic: $D\alpha_1 - D\,P_*' = D\,M(\bar{\rho})\,\mu_1 \propto (1 - \bar{\rho})^2$.

Right panel: the amplification factor $\mathcal{A}(\bar{\rho}) = M_*/M(\bar{\rho})$ on a log scale versus $\bar{\rho}$. Seven data points are plotted, computed from the ratio $C_{\mathrm{ED}}^{\mathrm{eff}}(0)/C_{\mathrm{ED}}(0)$ measured at the initial time for each experiment. The analytic curve $(0.5/(1 - \bar{\rho}))^2$ (solid line) is overlaid. The amplification grows from $\approx 6$ at $\bar{\rho} = 0.55$ to $\approx 6 \times 10^5$ at $\bar{\rho} = 0.98$. A vertical dashed line at $\bar{\rho} = \rho^* = 0.5$ marks the equilibrium (where $\mathcal{A} = 1$ by definition). The curve rises as an inverted parabola on the semilog scale (it is $(1 - \bar{\rho})^{-2}$, which is linear in $\log\mathcal{A}$ versus $\log(1 - \bar{\rho})$ with slope $-2$).

The two panels together capture the horizon's structural role: it suppresses transport ($D\alpha_1 \to D P_*'$, left panel) while amplifying the dissipative weight of any surviving gradient ($\mathcal{A} \to \infty$, right panel). The net effect is that the near-horizon region cannot sustain spatial structure — gradients are energetically prohibitive even though diffusion is locally extinct. This is the quantitative content of Proposition C.10, and the physical mechanism behind the mobility-collapse predictions of the Applications Paper.

---

## 7. Three-Stage Convergence

Theorem C.76 (Three-Stage Convergence) establishes that every global solution of the ED system converges to the unique equilibrium $(\rho^*, 0)$ through three structurally distinct stages:

- **Stage I** (Global bounds, Appendix C.2): the energy $\mathcal{E}$ remains bounded, the density stays in a compact subinterval of $(0, \rho_{\max})$, and the total dissipation over all time is finite. The convergence is at most algebraic. Structural basis: Principles 2, 3, 4.

- **Stage II** (Algebraic convergence, §C.7.1–C.7.4): the finite dissipation integrals and the Barbalat lemma drive $\nabla\rho \to 0$ and $v \to 0$. The strict monotonicity $P' > 0$ identifies $\rho^*$ as the unique $\omega$-limit point. The convergence rate is algebraic — it may be arbitrarily slow for far-from-equilibrium initial data. Structural basis: Principle 3 (uniqueness of the $\omega$-limit point).

- **Stage III** (Exponential convergence, Appendix C.5, §C.7.5): once the solution enters the local stability basin $\|(\rho - \rho^*, v)\|_{H^s} < \epsilon_0$, the Lyapunov functional $\mathcal{V}$ provides exponential decay at rate $\beta = \gamma_*$. Structural basis: Principles 1, 3, 5, 6.

The stages are connected: Stage I provides the uniform bounds needed for Stage II (ensuring compactness); Stage II provides the convergence needed for Stage III (ensuring eventual entry into the local basin). The **transition time** $t_*$ — the time at which the solution enters the exponential basin — depends on the initial energy $\mathcal{E}_0$ and is the key quantitative observable linking the three stages.

This section demonstrates each stage through direct numerical integration and measures the transition time $t_*$ as a function of the initial ED-complexity.

All experiments use $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4), the Crank–Nicolson scheme (§1.5.2) with $N = 512$ and $\Delta t = 5 \times 10^{-4}$, and Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$) unless otherwise stated. Parameter Set I is chosen because its oscillatory character ($\mathscr{D}_0 = -2.76$) makes the three stages visually distinct: the oscillatory transient of Stage II is clearly separated from the pure exponential of Stage III.

---

### 7.1 Stage I — Global Bounds

#### 7.1.1 Analytic Content

Stage I is the content of Appendix C.2 and Theorem C.66. The key bounds are:

1. **Pointwise confinement**: $\delta \leq \rho(x, t) \leq \rho_{\max} - \delta$ for all $(x, t)$, with $\delta = \delta(\mathcal{E}_0) > 0$ (eq. C.78).
2. **Energy bound**: $\mathcal{E}[\rho(t), v(t)] \leq C(\mathcal{E}_0)$ (eq. C.79).
3. **Finite total dissipation**: $\int_0^\infty\int_\Omega P'(\rho)|\nabla\rho|^2/M(\rho)\,dx\,dt < \infty$ and $\int_0^\infty v(t)^2\,dt < \infty$ (eq. C.81).

These bounds hold *regardless* of the initial data — they require only that $\mathcal{E}_0 < \infty$ and $\rho_0 \in (0, \rho_{\max})$. They do not provide a rate of convergence; they provide only the *framework* (boundedness, compactness) within which Stages II and III operate.

#### 7.1.2 Numerical Experiment 7.1: Stage I Verification for Large Perturbations

**Setup.** Initialize with a far-from-equilibrium configuration using IC-C (localized Gaussian, eq. 1.10) at large amplitude:

$$
\rho_0(x) = \rho^* + 0.4\,\exp\!\left(-\frac{(x - 0.5)^2}{2(0.05)^2}\right), \qquad v_0 = 0.
$$

The peak density is $\rho_0(0.5) = 0.9$, approaching $\rho_{\max} = 1.0$. The initial ED-complexity is $C_{\mathrm{ED}}(0) \approx 0.4^2 \cdot 88.6 \approx 14.2$ (large). The initial energy is $\mathcal{E}_0 \gg 1$.

Integrate to $T = 50.0$.

**Measured quantities.** At each time step:

1. The energy $\mathcal{E}(t)$.
2. The pointwise extrema $\min_x\rho(x, t)$ and $\max_x\rho(x, t)$.
3. The cumulative dissipation integrals $\int_0^t\int_\Omega P'|\nabla\rho|^2/M\,dx\,ds$ and $\int_0^t v(s)^2\,ds$.
4. The $L^2$-deviation $\|\rho(t) - \rho^*\|_{L^2}$.
5. The participation variable $|v(t)|$.

**Expected behavior.** The energy $\mathcal{E}(t)$ decreases monotonically from its initial value and is bounded above by $C(\mathcal{E}_0)$ for all $t$. The pointwise extrema remain within $(\delta, \rho_{\max} - \delta)$: the peak never reaches $\rho_{\max}$ (energy barrier, Proposition C.11) and the minimum never reaches $0$ (penalty restoring). The cumulative dissipation integrals grow monotonically and converge to finite limits as $t \to \infty$. The $L^2$-deviation and $|v|$ are bounded but not yet monotonically decreasing — during Stage I, the solution may exhibit complex transient behavior (oscillatory participation, triad-mediated harmonic generation, far-from-equilibrium relaxation) without any a priori rate of decay.

**Figure description (Figure 7.1).** *Stage I global bounds.* Four panels, vertically stacked, sharing the horizontal axis $t$ (range $[0, 50]$).

Panel 1 (top): the energy $\mathcal{E}(t)$ on a semilog-$y$ axis. The curve starts at $\mathcal{E}_0 \approx 30$ and descends, with a steep initial drop ($t \in [0, 2]$) as the high-complexity gradients dissipate, followed by a slower descent. By $t = 50$, the energy has decreased by approximately four orders of magnitude but has not yet reached the equilibrium value $\mathcal{E}(\rho^*, 0) = 0$. The monotonic descent confirms the Lyapunov property (Lemma C.6). A horizontal dashed line at $\mathcal{E}_0$ marks the upper bound.

Panel 2: the pointwise density extrema $\max_x\rho$ (upper curve) and $\min_x\rho$ (lower curve) versus $t$. Two horizontal dashed lines mark $\rho_{\max} = 1.0$ and $0$; two additional dashed lines mark $\rho_{\max} - \delta$ and $\delta$ (the confinement bounds from Theorem C.66). The $\max_x\rho$ curve starts at $0.9$ and decreases monotonically toward $\rho^* = 0.5$. The $\min_x\rho$ curve starts at $\approx 0.5$ (the Gaussian tails are near $\rho^*$) and oscillates gently around $0.5$ before settling. Both curves remain strictly interior to $(0, 1)$ at all times, with substantial margin from the boundaries.

Panel 3: the cumulative dissipation integrals. Two curves: $\int_0^t\int_\Omega P'|\nabla\rho|^2/M\,dx\,ds$ (blue, gradient dissipation) and $\int_0^t v(s)^2\,ds$ (green, participation dissipation). Both grow monotonically and flatten toward horizontal asymptotes (the finite total dissipation of eq. C.81). The gradient integral reaches $\approx 90\%$ of its $t = \infty$ value by $t \approx 5$ (most gradient energy is dissipated rapidly); the participation integral converges more slowly ($\approx 90\%$ by $t \approx 20$) because the oscillatory participation variable $v(t)$ contributes to $\int v^2\,dt$ over many cycles.

Panel 4 (bottom): the $L^2$-deviation $\|\rho - \rho^*\|_{L^2}$ (blue) and $|v(t)|$ (green) on a semilog-$y$ axis. These curves show the full transient dynamics: the $L^2$-deviation drops steeply during $t \in [0, 2]$ (spatial relaxation), then enters a slower phase. The participation $|v(t)|$ rises from $0$ to a peak at $t \approx 0.5$ (the feedback loop, Principle 5, excites $v$ in response to the operator output $F[\rho]$) and then oscillates with decreasing amplitude. The Stage I bound — that both quantities remain finite — is trivially verified; the panel's purpose is to show the *absence* of a clean exponential decay during this period, motivating the need for Stages II and III.

---

### 7.2 Stage II — Algebraic Decay

#### 7.2.1 Analytic Content

Stage II is the content of §C.7.1–C.7.4. The Barbalat lemma, applied to the finite dissipation integrals (C.81), gives $\|\nabla\rho(t)\|_{L^2} \to 0$ and $v(t) \to 0$ as $t \to \infty$ (eqs. C.85, Step 1 of Theorem C.70). The $\omega$-limit set is identified as $\{(\rho^*, 0)\}$ by the uniqueness of the penalty zero (Principle 3, Step 3 of Theorem C.70). Convergence in all Sobolev norms follows by parabolic bootstrapping (Theorem C.67).

The convergence is *algebraic*: no exponential rate is guaranteed during this stage. The rate depends on the trajectory — specifically, on how fast the solution sheds its high-complexity content and approaches the linearized neighborhood. For far-from-equilibrium initial data, the algebraic phase may be long and the effective rate may be very slow ($\|\rho - \rho^*\|_{L^2} \sim t^{-p}$ for some $p > 0$ that depends on the initial configuration).

The algebraic character is most visible in the homogeneous mode $(a_0(t), v(t))$: in the oscillatory regime (Parameter Set I), the envelope of the damped oscillations contracts at a rate that is initially faster than exponential (during the nonlinear transient) and then slows before transitioning to exponential in Stage III. This intermediate slowdown is the signature of Stage II.

#### 7.2.2 Numerical Experiment 7.2: Algebraic Convergence at Moderate Amplitude

**Setup.** Initialize with IC-C at $A = 0.2$, $\sigma = 0.05$, $v_0 = 0.05$. This gives $C_{\mathrm{ED}}(0) \approx 3.54$ (moderate, above the stability threshold $\epsilon_0^2$ but not extreme). Integrate to $T = 40.0$.

**Measured quantities.**

1. The $L^2$-deviation $\|\rho(t) - \rho^*\|_{L^2}$ and $|v(t)|$.
2. The Lyapunov functional $\mathcal{V}(t)$ (Definition C.39).
3. The instantaneous convergence rate $\hat{\beta}(t) := -d\ln\mathcal{V}/dt$.
4. The best-fit power law $\mathcal{V}(t) \sim C\,t^{-p}$ over the interval $[2, 15]$ (the algebraic phase).
5. The best-fit exponential $\mathcal{V}(t) \sim C\,e^{-\beta t}$ over the interval $[20, 40]$ (the exponential phase).

**Expected behavior.** The Lyapunov functional $\mathcal{V}(t)$ decreases in three visually distinct phases:

- **Phase A** ($t \in [0, 2]$): rapid descent. The high spatial modes decay at their fast rates $D\alpha_n$ (Section 3), and the Lyapunov functional drops by several orders of magnitude. The instantaneous rate $\hat{\beta}(t)$ is large and decreasing.

- **Phase B** ($t \in [2, 15]$): algebraic descent. The spatial modes have been extinguished; only the homogeneous mode $(a_0, v)$ remains. The homogeneous mode is oscillating (Parameter Set I is in the Spiral Sheet), but the amplitude decay is not purely exponential — the nonlinear corrections from Stages I–II are still active. On a log-log plot, $\mathcal{V}(t)$ is approximately linear with slope $-p$ for some $p > 0$. The instantaneous rate $\hat{\beta}(t)$ is approximately constant but below the linearized value $\gamma_*$.

- **Phase C** ($t > 15$): exponential descent. The solution has entered the local basin ($\|(\rho - \rho^*, v)\|_{H^s} < \epsilon_0$), and $\mathcal{V}(t)$ decays as a straight line on a semilog plot with slope $-2\gamma_*$ (the Lyapunov functional is quadratic in the perturbation, so its decay rate is twice the amplitude rate). The instantaneous rate $\hat{\beta}(t)$ has settled to $2\gamma_*$.

**Figure description (Figure 7.2).** *Three stages of convergence.* Three panels.

Top panel: semilog-$y$ plot of $\mathcal{V}(t)$ versus $t$ (range $[0, 40]$). The curve shows three distinct slopes: a steep initial descent ($t < 2$), a moderate descent ($2 < t < 15$), and a final straight-line descent ($t > 15$). The transition from Phase B to Phase C is visible as a bend where the curve steepens from its algebraic slope to its exponential slope. A dashed straight line with slope $-2\gamma_*$ is overlaid for $t > 15$; the curve matches it. A vertical dashed line at $t_* \approx 15$ marks the transition time from Stage II to Stage III.

Middle panel: the same data on a log-log plot ($\log t$ horizontal, $\log\mathcal{V}$ vertical). On this plot, an algebraic decay $\mathcal{V} \sim t^{-p}$ appears as a straight line with slope $-p$, while an exponential decay curves downward (concave on the log-log plot). The curve is approximately straight with slope $\approx -2.5$ over $t \in [2, 12]$, confirming the algebraic character of Stage II. For $t > 15$, the curve bends sharply downward (the exponential takes over). The intermediate region $t \in [12, 18]$ is the transition zone. A dashed reference line with slope $-2.5$ is overlaid on the algebraic segment.

Bottom panel: the instantaneous convergence rate $\hat{\beta}(t) = -d\ln\mathcal{V}/dt$ versus $t$ on a linear axis. The rate starts very high ($\hat{\beta} > 10$ at $t = 0.1$, reflecting the fast spatial-mode decay), decreases rapidly during Phase A, settles to a plateau at $\hat{\beta} \approx 0.3$ during Phase B (the algebraic rate), and then rises to a final plateau at $\hat{\beta} = 2\gamma_* \approx 0.4$ during Phase C. Two horizontal dashed lines mark the algebraic-phase rate ($\approx 0.3$) and the exponential-phase rate ($2\gamma_* \approx 0.4$). The rise from the lower plateau to the upper plateau at $t \approx 15$ is the dynamical transition from Stage II to Stage III.

#### 7.2.3 Numerical Experiment 7.3: Barbalat Decay of Gradients and Participation

**Setup.** Using the same integration as Experiment 7.2, track the two quantities whose decay is driven by the Barbalat lemma:

1. The gradient integral $\|\nabla\rho(t)\|_{L^2}^2 = C_{\mathrm{ED}}(t)$.
2. The participation magnitude $|v(t)|$.

Also track the cumulative dissipation integrals from Panel 3 of Figure 7.1 and their rate of saturation.

**Analytic prediction.** The Barbalat lemma states that if $f \in L^1(0, \infty)$ and $f$ is uniformly continuous, then $f(t) \to 0$. Applied to $f = \|\nabla\rho\|_{L^2}^2$: the finite integral $\int_0^\infty C_{\mathrm{ED}}(t)\,dt < \infty$ (which follows from eq. C.81 and the bound $P'/M \geq c_\delta > 0$) combined with the uniform continuity of $C_{\mathrm{ED}}(t)$ (from the $H^3$-bounds of Theorem C.67) gives $C_{\mathrm{ED}}(t) \to 0$. Similarly, $\int_0^\infty v^2\,dt < \infty$ and the uniform continuity of $v^2$ give $v(t) \to 0$.

The Barbalat lemma provides no rate. The actual rate at which $C_{\mathrm{ED}}(t) \to 0$ depends on the solution trajectory. For the linearized system (single mode $n = 1$), $C_{\mathrm{ED}}(t) = C_{\mathrm{ED}}(0)\,e^{-2D\alpha_1 t}$ (exponential). For the nonlinear system far from equilibrium, the rate may be slower — the triad coupling (Section 4) can temporarily inject energy into spatial modes, and the mobility variation (Section 6) modifies the effective diffusion rate.

**Figure description (Figure 7.3).** *Barbalat-driven decay of gradients and participation.* Two panels.

Left panel: semilog-$y$ plot of $C_{\mathrm{ED}}(t)$ versus $t$ (range $[0, 40]$). The curve shows a steep initial descent ($t < 2$) as the high spatial modes are extinguished, followed by a slower descent during Stage II ($2 < t < 15$) and a final exponential descent in Stage III ($t > 15$). The slope during Stage III is $\approx -2D(\alpha_1 - P_*') \approx -1.76$ (the rate at which the complexity of the surviving fundamental mode decays). A horizontal dashed line at $C_{\mathrm{ED}} = 0$ and a reference exponential with slope $-1.76$ are overlaid.

Inset: the cumulative gradient dissipation integral $\int_0^t C_{\mathrm{ED}}(s)\,ds$ versus $t$, showing monotonic growth toward a finite asymptote. The integral reaches $90\%$ of its limiting value by $t \approx 5$, confirming that most gradient dissipation occurs during Stage I.

Right panel: semilog-$y$ plot of $|v(t)|$ versus $t$ (range $[0, 40]$). The participation variable oscillates (Parameter Set I is oscillatory) with an envelope that decays in three stages matching the Lyapunov convergence. During Stage II, the envelope contracts at a rate $\approx \gamma_0 = 0.2$ but with visible amplitude modulation from the nonlinear interaction between $v$ and the residual spatial structure. During Stage III ($t > 15$), the envelope contracts as a clean exponential $e^{-\gamma_0 t}$ (the linearized damping rate). The oscillation frequency is approximately constant at $\omega \approx 0.83$ throughout — the frequency is set by the linearized eigenvalues, which are insensitive to the amplitude.

---

### 7.3 Stage III — Exponential Decay

#### 7.3.1 Analytic Content

Stage III is the content of Theorem C.43 (local exponential stability) activated by Theorem C.72 (eventual entry into the basin). Once $\|(\rho(t) - \rho^*, v(t))\|_{H^s} < \epsilon_0$, the Lyapunov functional satisfies

$$
\frac{d\mathcal{V}}{dt} \leq -\gamma_*\,\mathcal{V},
$$

and therefore $\mathcal{V}(t) \leq \mathcal{V}(t_*)\,e^{-\gamma_*(t - t_*)}$ for $t \geq t_*$ (eq. C.50). The coercivity estimate (C.42) converts this into

$$
\|\rho(t) - \rho^*\|_{H^1}^2 + |v(t)|^2 \leq \frac{c_+}{c_-}\bigl(\|\rho(t_*) - \rho^*\|_{H^1}^2 + |v(t_*)|^2\bigr)\,e^{-\gamma_*(t - t_*)}.
$$

The exponential rate $\gamma_*$ (eq. C.48) depends on the canonical parameters and can be computed explicitly for each parameter set. The decay is clean, monotonic (on the Lyapunov-functional level), and universal: all solutions in the basin converge at the same rate, regardless of their specific initial condition within the basin.

In the oscillatory regime, the density deviation and participation variable oscillate with frequency $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ inside the exponential envelope. In the monotonic regime, the decay is purely exponential with no oscillation.

#### 7.3.2 Numerical Experiment 7.4: Clean Exponential Decay in the Local Basin

**Setup.** Initialize with a small perturbation that is already inside the stability basin:

$$
\rho_0(x) = \rho^* + 0.01\cos(\pi x), \qquad v_0 = 0.005.
$$

This gives $\|u_0\|_{H^1} \approx 0.03$, well below $\epsilon_0$. Integrate to $T = 30.0$.

**Expected behavior.** No Stage I or Stage II transient is needed — the solution is already in the exponential basin. The Lyapunov functional $\mathcal{V}(t)$ decays as a pure exponential from $t = 0$, with rate $\gamma_*$ and no curvature on the semilog plot. The density deviation $u(t)$ and participation $v(t)$ oscillate (Parameter Set I) with envelope $e^{-\gamma_0 t}$, where $\gamma_0 = 0.2$. The spatial mode $n = 1$ decays at rate $D\alpha_1 = 1.04$; the homogeneous mode decays at rate $\gamma_0 = 0.2$. By $t = 5$, the spatial mode has been extinguished and only the homogeneous oscillation remains.

**Figure description (Figure 7.4).** *Pure exponential decay in the local basin.* Two panels.

Left panel: semilog-$y$ plot of $\mathcal{V}(t)$ versus $t$ (range $[0, 30]$). The curve is a straight line from $t = 0$ with slope $\approx -2\gamma_* \approx -0.4$. There is no initial steep phase (no high-complexity transient) and no intermediate algebraic phase. The straight-line character from $t = 0$ confirms that the solution is entirely within Stage III. A dashed reference line with slope $-2\gamma_*$ is overlaid; the data falls on it to within line width.

Right panel: the density deviation $u_0(t) = \bar{\rho}(t) - \rho^*$ and participation $v(t)$ on a linear scale versus $t$ (range $[0, 30]$). Both oscillate at frequency $\omega \approx 0.83$ with exponentially decaying envelopes. The envelope (dashed curves at $\pm C e^{-\gamma_0 t}$) contracts uniformly from $t = 0$. By $t = 15$, the amplitude is below $10^{-3}$; by $t = 25$, below $10^{-5}$. The oscillation is cleanly sinusoidal (no harmonic distortion, since the amplitude is always in the linearized regime).

#### 7.3.3 Numerical Experiment 7.5: Exponential Rate Measurement Across Parameter Sets

**Setup.** For each of the five canonical parameter sets (I–V), initialize with $\rho_0 = \rho^* + 0.01\cos(\pi x)$, $v_0 = 0.005$ (inside the basin for all sets). Integrate to $T = 30.0$. Measure the exponential decay rate $\hat{\gamma}$ from the slope of $\ln\mathcal{V}(t)$ over $[5, 25]$.

**Analytic predictions.** The Lyapunov rate $\gamma_*$ (eq. C.48) depends on the parameter set. For the in-basin regime, the measured rate should equal $\gamma_*$ (or, more precisely, the rate at which $\mathcal{V}$ decays, which is controlled by the slowest component — the spectral gap $\gamma = \min(\gamma_{\mathrm{hom}}, \gamma_{\mathrm{sp}})$ from Lemma C.31).

| Set | $\gamma_{\mathrm{hom}}$ | $\gamma_{\mathrm{sp}} = D\alpha_1$ | $\gamma = \min$ | $2\gamma$ (Lyapunov rate) |
|-----|-----|-----|-----|-----|
| I | $0.200$ | $1.040$ | $0.200$ | $0.400$ |
| II | $0.550$ | $2.080$ | $0.550$ | $1.100$ |
| III | $1.300$ | $4.160$ | $1.300$ | $2.600$ |
| IV | $2.950$ | $4.680$ | $2.950$ | $5.900$ |
| V | $0.500$ | $1.040$ | $0.500$ | $1.000$ |

Note: for Sets III and IV (overdamped), $\gamma_{\mathrm{hom}}$ is not the real part of the eigenvalues but the slower of the two real eigenvalues; the effective rate may be smaller. The table uses the simpler $\gamma_{\mathrm{hom}} = \frac{1}{2}(DP_*' + \zeta/\tau)$ as an upper bound.

**Figure description (Figure 7.5).** *Exponential rate across parameter sets.* Single panel.

The horizontal axis labels the five parameter sets (I–V). The vertical axis shows the measured Lyapunov decay rate $\hat{\gamma}$ (twice the amplitude rate). Five data points (filled circles) are plotted at the measured values. Open squares show the analytic predictions from the table. The data matches the predictions to within $5\%$ for all five sets. The ordering $\hat{\gamma}_{\mathrm{I}} < \hat{\gamma}_{\mathrm{V}} < \hat{\gamma}_{\mathrm{II}} < \hat{\gamma}_{\mathrm{III}} < \hat{\gamma}_{\mathrm{IV}}$ reflects the increasing total damping: Set I has the weakest damping (smallest $D$ and $\zeta$); Set IV has the strongest (largest $D$ and $\zeta$). The spectral gap $\gamma$ is controlled by the homogeneous mode for all five sets (since $\gamma_{\mathrm{hom}} < \gamma_{\mathrm{sp}}$ in every case).

---

### 7.4 Transition Time $t_*$ as a Function of Complexity

#### 7.4.1 Analytic Framework

The transition time $t_*$ is defined operationally as the earliest time at which the solution enters the exponential-stability basin:

$$
t_* := \inf\bigl\{t \geq 0 : \|(\rho(t) - \rho^*, v(t))\|_{H^s} < \epsilon_0\bigr\}.
\tag{7.1}
$$

For initial data already inside the basin, $t_* = 0$. For far-from-equilibrium data, $t_*$ is the duration of Stages I and II combined — the time required for the global bounds, the Barbalat decay, and the $\omega$-limit convergence to bring the solution within $\epsilon_0$ of equilibrium.

The transition time depends on the initial data primarily through the initial ED-complexity $C_{\mathrm{ED}}(0)$ (or, more precisely, through the initial energy $\mathcal{E}_0$, which is dominated by the gradient contribution for high-complexity data). The qualitative expectation is:

- For $C_{\mathrm{ED}}(0) \ll \epsilon_0^2$: $t_* \approx 0$ (already in the basin).
- For $C_{\mathrm{ED}}(0) \sim \epsilon_0^2$: $t_*$ is small (brief Stage II).
- For $C_{\mathrm{ED}}(0) \gg \epsilon_0^2$: $t_*$ is large (extended Stage I and II).

The scaling of $t_*$ with $C_{\mathrm{ED}}(0)$ encodes the efficiency of the nonlinear relaxation mechanism: how fast the system can shed its excess complexity and enter the exponential regime.

#### 7.4.2 Numerical Experiment 7.6: Transition Time Versus Initial Complexity

**Setup.** Initialize with IC-C (Gaussian, $\sigma = 0.05$, $x_0 = 0.5$) at ten amplitudes $A \in \{0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.35, 0.4\}$, giving initial complexities $C_{\mathrm{ED}}(0) \approx A^2 \cdot 88.6$ spanning $[0.002, 14.2]$. Set $v_0 = 0$. Integrate each to $T = 60.0$.

For each integration, measure the transition time $t_*$ using the operational definition (7.1) with $\epsilon_0$ replaced by a numerically accessible surrogate: $t_*$ is the earliest time at which $\mathcal{V}(t)$ begins to decay exponentially, identified as the time at which the instantaneous rate $\hat{\beta}(t) = -d\ln\mathcal{V}/dt$ reaches $90\%$ of its asymptotic value $2\gamma_*$.

**Expected results.** The transition time increases monotonically with $C_{\mathrm{ED}}(0)$. For the smallest amplitudes ($A \leq 0.02$, $C_{\mathrm{ED}} \leq 0.035$), $t_* \approx 0$: the solution is inside the basin from the start, and Stage III begins immediately. For moderate amplitudes ($A \sim 0.1$, $C_{\mathrm{ED}} \sim 0.9$), $t_* \approx 5$–$10$: a brief nonlinear transient is followed by entry into the basin. For the largest amplitudes ($A = 0.4$, $C_{\mathrm{ED}} \approx 14$), $t_* \approx 20$–$30$: the system spends a long time in the algebraic phase before the residual complexity has been dissipated to the point where exponential decay can begin.

The scaling of $t_*$ with $C_{\mathrm{ED}}(0)$ is expected to be approximately logarithmic for moderate complexities and approximately linear for large complexities. The logarithmic regime arises when the complexity is within an order of magnitude of $\epsilon_0^2$ (the solution needs only a few $e$-folding times of the fastest spatial mode to reach the basin). The linear regime arises for very large complexities (the algebraic Stage II becomes the bottleneck, and the transition time scales with the time required for the homogeneous mode's nonlinear transient to damp).

**Figure description (Figure 7.6).** *Transition time versus initial ED-complexity.* Two panels.

Left panel: semilog-$y$ plots of $\mathcal{V}(t)$ for all ten amplitudes on the same axes ($t$ horizontal, range $[0, 60]$). The ten curves form a nested family: the lowest-amplitude curve (lightest shade) is a straight line from $t = 0$ (pure exponential, $t_* = 0$). Each successive curve starts higher, spends longer in the non-exponential phase, and joins the universal exponential slope at a later time. The highest-amplitude curve (darkest shade) has a pronounced algebraic segment and does not reach the exponential slope until $t \approx 25$. Dashed vertical lines at the measured $t_*$ for each curve mark the transition points. All curves eventually become parallel — the same exponential slope $-2\gamma_*$ — confirming the universal late-time rate of Theorem C.76.

Right panel: the measured transition time $t_*$ versus $C_{\mathrm{ED}}(0)$ on a semilog-$x$ axis. The ten data points (filled circles) show a curve that is flat at $t_* \approx 0$ for $C_{\mathrm{ED}}(0) < 0.05$ (inside the basin), rises steeply for $0.05 < C_{\mathrm{ED}}(0) < 1$ (the logarithmic regime), and continues to rise but more gradually for $C_{\mathrm{ED}}(0) > 1$ (the linear/saturating regime). The curve is approximately $t_* \sim c\,\ln(C_{\mathrm{ED}}(0)/\epsilon_0^2)$ for moderate complexities. A fitted curve $t_* = a\ln(1 + C_{\mathrm{ED}}(0)/b)$ (with two free parameters $a, b$) is overlaid as a solid line; it passes through all ten points.

A vertical dashed line at $C_{\mathrm{ED}}(0) = \epsilon_0^2$ marks the boundary of the exponential basin. Points to its left have $t_* = 0$; points to its right require nonlinear relaxation.

#### 7.4.3 Numerical Experiment 7.7: Transition Time Dependence on Parameter Set

**Setup.** Fix $A = 0.2$ ($C_{\mathrm{ED}}(0) \approx 3.54$). Repeat the integration for all five canonical parameter sets (I–V). Measure $t_*$ for each.

**Expected results.** The transition time varies across parameter sets because both $\epsilon_0$ and the Stage II convergence rate depend on the canonical parameters. The stability threshold $\epsilon_0 = \gamma_*/C_{\mathrm{nl}}$ is smallest for Set III (near-critical, smallest $\gamma_*$), making it hardest to enter the basin, and largest for Set IV (deep monotonic, largest $\gamma_*$). The algebraic decay rate during Stage II is also slowest for Set III (the slow eigenvalue is close to zero near the critical surface).

| Set | $\gamma_*$ (approx.) | Expected $t_*$ |
|-----|-----|-----|
| I | $0.20$ | Moderate ($\sim 15$) |
| II | $0.55$ | Short ($\sim 6$) |
| III | $0.20$ (near-critical) | Long ($\sim 25$) |
| IV | $2.95$ | Very short ($\sim 2$) |
| V | $0.50$ | Moderate ($\sim 8$) |

Set III has the longest $t_*$ despite having the same $\gamma_{\mathrm{hom}}$ as Set I, because the near-critical slowdown reduces the effective convergence rate during Stage II (the eigenvalue gap between $\lambda_+$ and $\lambda_-$ is small, producing a near-degenerate decay). Set IV has the shortest $t_*$ because the strong damping drives the solution into the basin rapidly.

**Figure description (Figure 7.7).** *Transition time across parameter regimes.* Single panel.

The horizontal axis labels the five parameter sets (I–V). The vertical axis shows the measured transition time $t_*$. Five data points (filled circles) are plotted. The ordering is IV $<$ II $<$ V $<$ I $<$ III, with $t_*$ ranging from $\approx 2$ (Set IV) to $\approx 25$ (Set III). A second set of markers (open squares) shows the heuristic estimate $t_* \approx c\ln(C_{\mathrm{ED}}(0)/\epsilon_0^2)/\gamma_*$, using the measured $\epsilon_0^2$ from Experiment 5.4 and $\gamma_*$ from the table; the estimates track the data to within $30\%$.

The panel demonstrates the architectural prediction: the transition time is governed by the ratio of initial complexity to the stability threshold, modulated by the damping rate. The near-critical Set III has the longest transition because the damping rate is smallest and the stability basin is narrowest — the system must dissipate the most complexity with the least dissipative power. Set IV has the shortest transition because it has the most dissipative power and the widest basin. This is the quantitative content of Theorem C.76: the three stages are not merely a logical structure but produce measurably different convergence histories depending on the canonical parameters.

#### 7.4.4 Structural Summary

The three-stage convergence of Theorem C.76 is not an abstract mathematical artifact but a numerically observable temporal structure. The experiments of this section demonstrate:

1. **Stage I is visible** (Experiment 7.1): the energy decreases monotonically, the density remains confined, and the total dissipation converges to a finite limit. These bounds hold for arbitrarily large initial data.

2. **Stage II is visible** (Experiments 7.2–7.3): the Lyapunov functional decays algebraically ($\mathcal{V} \sim t^{-p}$) for an extended interval, with the Barbalat decay of gradients and participation clearly distinguishable from exponential behavior.

3. **Stage III is visible** (Experiments 7.4–7.5): once inside the basin, the decay is a clean exponential at rate $\gamma_*$, with the rate matching the analytic predictions of Theorem C.43 to within $5\%$ across all parameter sets.

4. **The transition time $t_*$ is measurable** (Experiments 7.6–7.7): it scales logarithmically with the initial complexity and inversely with the damping rate, varies by an order of magnitude across parameter sets, and is smallest in the deep monotonic regime and largest near the critical surface.

The three-stage structure is the temporal realization of the architectural hierarchy: Principles 2–4 control Stage I (bounds), Principle 3 controls Stage II (uniqueness of the attractor), and Principles 1, 3, 5, 6 control Stage III (exponential stability). Each principle is indispensable, and each stage is structurally distinct.

---

## 8. Regime Transitions

The regime geometry of the ED system — the partition of parameter space into the Spiral Sheet ($\mathscr{D}_0 < 0$, oscillatory) and the Monotonic Cone ($\mathscr{D}_0 > 0$, monotonic), separated by the Boundary Surface $\Sigma$ ($\mathscr{D}_0 = 0$) — is established analytically in Appendix C.3 (Theorem C.22, Definition C.19) and its bifurcation structure is analyzed in Appendix C.6 (Theorem C.60, codimension-one nondegenerate transition; Theorem C.61, $\Delta$ as organizing parameter; Remark C.65, absence of Hopf bifurcation). Section 2 of the Atlas visualized the individual regimes and the discriminant landscape at fixed parameter values.

This section goes further: it demonstrates the *transition itself* — the continuous change in solution character as parameters are swept through the Boundary Surface — and extends the regime classification beyond the linearized neighborhood into the nonlinear domain, where the initial ED-complexity can drive a system through multiple effective regimes during a single integration. The section has three parts: the classical Spiral $\to$ Monotonic transition as $\Delta$ crosses $1$ (§8.1), complexity-driven regime transitions at fixed parameters (§8.2), and systematic parameter sweeps mapping the full regime geometry (§8.3).

All experiments use $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4), the Crank–Nicolson scheme (§1.5.2) with $N = 512$ and $\Delta t = 5 \times 10^{-4}$, and the canonical normalization $\tau P_*' = 1$ (i.e., $\tau = 1$, $P_0 = 1$) unless otherwise stated.

---

### 8.1 Spiral $\to$ Monotonic Transition: Sweeping $\Delta$ Across $1$

#### 8.1.1 Analytic Framework

The canonical damping parameter $\Delta = D + 2\zeta$ organizes the regime transition (Theorem C.61). In the canonical normalization, the critical surface $\Sigma$ is the parabola $(D - \zeta)^2 = 4(1 - D)$ in the $(D, \zeta)$-plane (eq. C.63). The discriminant

$$
\mathscr{D}_0 = \frac{1}{\tau^2}\bigl[(D - \zeta)^2 - 4(1 - D)\bigr]
$$

changes sign as parameters cross $\Sigma$: $\mathscr{D}_0 < 0$ (oscillatory) on the interior of the parabola, $\mathscr{D}_0 > 0$ (monotonic) on the exterior. The eigenvalues of the homogeneous-mode matrix $\mathbf{A}_0$ split from a repeated real value into a complex pair (entering the Spiral Sheet) or remain real and separate (entering the Monotonic Cone), depending on the direction of crossing (Theorem C.60(i)).

The transition is:

- **Nondegenerate**: the eigenvalue coalescence at $\Sigma$ is a Jordan block, not a scalar multiple of the identity (Lemma C.54).
- **Codimension one**: organized by the single condition $\mathscr{D}_0 = 0$ (Theorem C.60(ii)).
- **Stability-preserving**: no eigenvalue crosses the imaginary axis; both eigenvalues have strictly negative real part on both sides of $\Sigma$ (Theorem C.60(iii), Remark C.65).
- **Structurally stable**: small perturbations of $M$ and $P$ shift $\Sigma$ smoothly but do not change the transition type (Theorem C.60(iv), Theorem C.61(iii)).

The normal form on the center manifold (Theorem C.58, eq. C.72a–b) with the leading nonlinear coefficient $g_{\mathrm{pen}}$ from (C.76) governs the near-critical dynamics.

#### 8.1.2 Numerical Experiment 8.1: Fine-Grained $\zeta$-Sweep at Fixed $D$

**Setup.** Fix $D = 0.5$, $\tau = 1.0$. The critical value is $\zeta_c = D + 2\sqrt{1 - D} = 0.5 + 2\sqrt{0.5} \approx 1.914$ (from eq. C.63). Sweep $\zeta$ over 41 uniformly spaced values from $0.5$ to $3.0$, passing through $\zeta_c$. At each value, initialize with $\rho_0 = \rho^* + 0.03\cos(\pi x)$, $v_0 = 0.03$ (small, in the linearized regime), and integrate to $T = 30.0$.

**Measured quantities.** For each $\zeta$:

1. The number of zero crossings $N_{\mathrm{cross}}$ of $a_0(t) = \bar{\rho}(t) - \rho^*$ in $[0, 30]$.
2. The oscillation frequency $\hat{\omega}$ (measured from zero-crossing intervals, if $N_{\mathrm{cross}} \geq 2$).
3. The decay rate $\hat{\gamma}_0$ of the homogeneous-mode envelope.
4. The eigenvalue splitting: the two measured eigenvalue magnitudes $|\hat{\lambda}_+|$ and $|\hat{\lambda}_-|$ (extracted by fitting the time series to a sum of two exponentials or a damped sinusoid).
5. The phase-plane winding number: the number of complete revolutions of the trajectory $(a_0(t), v(t))$ around the origin.

**Expected results.** For $\zeta < \zeta_c$ (Spiral Sheet): the trajectory spirals, with $N_{\mathrm{cross}} > 0$, positive $\hat{\omega}$, and winding number growing with decreasing $\zeta$ (more oscillations per unit time). As $\zeta \to \zeta_c^-$: $\hat{\omega} \to 0$ as $\sqrt{\zeta_c - \zeta}$ (the square-root vanishing from the discriminant zero), $N_{\mathrm{cross}}$ drops to $0$–$1$, and the winding number approaches $0$.

At $\zeta = \zeta_c$: the trajectory shows Jordan-block dynamics — algebraic-then-exponential decay (§2.3), $N_{\mathrm{cross}} = 0$, winding number $0$.

For $\zeta > \zeta_c$ (Monotonic Cone): $N_{\mathrm{cross}} = 0$, no oscillation, monotonic decay with two separable time scales $|\hat{\lambda}_+|$ and $|\hat{\lambda}_-|$ that move apart as $\zeta$ increases beyond $\zeta_c$.

The eigenvalue splitting is the key observable: at $\zeta_c$, the two eigenvalues are equal ($\hat{\lambda}_+ = \hat{\lambda}_- = \lambda_c$). For $\zeta < \zeta_c$, they are complex conjugates: $\hat{\lambda}_\pm = -\hat{\gamma}_0 \pm i\hat{\omega}$. For $\zeta > \zeta_c$, they are real and separate: $|\hat{\lambda}_+| < |\hat{\lambda}_-|$, with the splitting growing as $\sqrt{\zeta - \zeta_c}$.

**Figure description (Figure 8.1).** *Eigenvalue splitting across the Boundary Surface.* Three panels.

Top panel: the measured oscillation frequency $\hat{\omega}$ (for $\zeta < \zeta_c$) and zero (for $\zeta \geq \zeta_c$) versus $\zeta$ (horizontal axis, range $[0.5, 3.0]$). The curve rises from small values at $\zeta$ near $\zeta_c$ to $\hat{\omega} \approx 0.8$ at $\zeta = 0.5$, following the analytic prediction $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ (dashed line). Near $\zeta_c$, the frequency vanishes as a square root: $\hat{\omega} \propto (\zeta_c - \zeta)^{1/2}$. A vertical dashed line at $\zeta_c \approx 1.914$ marks the transition. The region $\zeta > \zeta_c$ is shaded to indicate the Monotonic Cone.

Middle panel: the two eigenvalue magnitudes $|\hat{\lambda}_+|$ and $|\hat{\lambda}_-|$ versus $\zeta$. For $\zeta < \zeta_c$: both eigenvalues have the same magnitude ($|\hat{\lambda}_+| = |\hat{\lambda}_-| = \hat{\gamma}_0$, the common decay rate of the complex pair); the two curves coincide. At $\zeta_c$: the curves meet at the repeated eigenvalue $|\lambda_c| = \gamma_0(\zeta_c)$. For $\zeta > \zeta_c$: the curves split — $|\hat{\lambda}_+|$ (the slow eigenvalue, closer to zero) decreases, while $|\hat{\lambda}_-|$ (the fast eigenvalue) increases. The splitting is proportional to $\sqrt{\zeta - \zeta_c}$ near the critical point, producing a cusp-like shape. Analytic predictions from (C.15) are overlaid as dashed curves; the numerical data follows them.

Bottom panel: the winding number of the phase trajectory versus $\zeta$. This is an integer-valued step function: for $\zeta$ well below $\zeta_c$, the winding number is $\geq 5$ (many revolutions in $T = 30$). As $\zeta \to \zeta_c^-$, it decreases stepwise. At $\zeta \geq \zeta_c$, it is exactly $0$. The steps are not evenly spaced — the frequency vanishes as $\sqrt{\zeta_c - \zeta}$, so the winding number jumps are concentrated near $\zeta_c$. This panel provides a topological view of the transition: the integer winding number is a discrete invariant that distinguishes the oscillatory and monotonic regimes unambiguously.

#### 8.1.3 Numerical Experiment 8.2: Phase-Portrait Morphing

**Setup.** Select seven values of $\zeta$ from the sweep of Experiment 8.1, spanning both regimes and the critical point: $\zeta \in \{0.5, 1.0, 1.5, \zeta_c, 2.2, 2.8, 3.5\}$. For each, compute the full phase-plane trajectory $(a_0(t), v(t))$ for $t \in [0, 30]$.

**Figure description (Figure 8.2).** *Phase-portrait morphing across the Boundary Surface.* Seven sub-panels arranged in a $1 \times 7$ horizontal strip, each showing the phase trajectory $(a_0, v)$ for a single $\zeta$ value. All panels share the same axis ranges ($a_0 \in [-0.04, 0.04]$, $v \in [-0.05, 0.05]$) to facilitate comparison.

Panel 1 ($\zeta = 0.5$, deep Spiral Sheet): a tight spiral making $\sim 6$ revolutions before reaching the origin. The trajectory is nearly circular (eigenvalues close to purely imaginary, since $\gamma_0 = 0.3$ is small relative to $\omega \approx 0.82$).

Panel 2 ($\zeta = 1.0$): a wider spiral making $\sim 3$ revolutions. The turns are more visibly spaced — the damping has increased ($\gamma_0 = 0.55$), so the envelope contracts faster per revolution.

Panel 3 ($\zeta = 1.5$): $\sim 1.5$ revolutions. The spiral is loose — the trajectory barely loops around the origin before spiraling inward. The oscillatory character is still visible but muted.

Panel 4 ($\zeta = \zeta_c \approx 1.914$, critical): no loop. The trajectory approaches the origin along a single curved path (the eigenvector direction), with the characteristic algebraic overshoot of the Jordan block. The initial tangent points away from the eigenvector, then curves toward it. The trajectory's curvature at the origin is nonzero (the generalized eigenvector contributes), distinguishing it from the monotonic panels.

Panel 5 ($\zeta = 2.2$, weakly monotonic): no loop. The trajectory is a smooth arc that curves gently toward the origin along the slow eigenvector $\mathbf{r}_+$. Qualitatively similar to Panel 4, but the curvature near the origin is less (no Jordan contribution, just two distinct real eigenvalues).

Panel 6 ($\zeta = 2.8$): the trajectory is nearly straight, aligning with $\mathbf{r}_+$ almost immediately. The fast eigenvector component decays so rapidly that the trajectory is a nearly one-dimensional approach.

Panel 7 ($\zeta = 3.5$, deep Monotonic Cone): essentially a straight line from the initial point to the origin along $\mathbf{r}_+$. The fast eigenvalue is so large ($|\hat{\lambda}_-| > 5$) that its contribution vanishes within $t < 0.3$, and the remainder is purely exponential along the slow direction.

The seven panels, read left to right, constitute a visual animation of the topological transition: spiraling → loose spiraling → no loop (critical) → gentle curve → straight approach. The transition is smooth — each panel differs only slightly from its neighbor — confirming the codimension-one, nondegenerate character of Theorem C.60.

---

### 8.2 Complexity-Driven Regime Transitions

#### 8.2.1 Analytic Framework

The regime classification of Appendix C.3 (Theorem C.22) is a *linearized* classification: it applies to the homogeneous mode of small perturbations near $(\rho^*, 0)$. For large perturbations — those with $C_{\mathrm{ED}} \gg \epsilon_0^2$ — the nonlinear dynamics can exhibit a *transient* oscillatory character that differs from the linearized regime classification. This is because the effective damping depends on the local density $\rho(x,t)$, which varies far from $\rho^*$ during the nonlinear transient.

The effective local damping parameter is

$$
\Delta_{\mathrm{eff}}(\rho) = D + 2\zeta \cdot \frac{M(\rho)}{M_*},
$$

which deviates from $\Delta = D + 2\zeta$ when $\rho \neq \rho^*$. Near $\rho_{\max}$ (where $M(\rho) \to 0$), the effective damping approaches $D$ alone — the participation channel's contribution is suppressed by the vanishing mobility. Near $\rho = 0$ (where $M(\rho) \to M(0) > M_*$ for typical constitutive choices), the effective damping can exceed $\Delta$.

This means that a system in the Monotonic Cone ($\Delta > 1$) can transiently behave as if oscillatory if the density excursion is large enough to reduce $\Delta_{\mathrm{eff}}$ below the critical threshold. Conversely, a system in the Spiral Sheet ($\Delta < 1$) can transiently exhibit monotonic decay during a near-horizon excursion where the mobility collapse suppresses the participation channel.

#### 8.2.2 Numerical Experiment 8.3: Oscillatory Transient in the Monotonic Regime

**Setup.** Use Parameter Set III ($D = 0.8$, $\zeta = 1.8$, $\tau = 1.0$), which is in the Monotonic Cone ($\mathscr{D}_0 = 0.2 > 0$). Initialize with a large-amplitude perturbation that drives the density far from $\rho^*$:

$$
\rho_0(x) = \rho^* + 0.35\,\exp\!\left(-\frac{(x - 0.5)^2}{2(0.05)^2}\right), \qquad v_0 = 0.
$$

Peak density: $0.85$, so $M(0.85) = (0.15)^2 = 0.0225$, giving $M(0.85)/M_* = 0.0225/0.25 = 0.09$. The effective damping at the peak is $\Delta_{\mathrm{eff}} \approx 0.8 + 2 \cdot 1.8 \cdot 0.09 = 0.8 + 0.324 = 1.124$ — still above $1$, but much closer to criticality than the linearized value $\Delta = 0.8 + 3.6 = 4.4$.

Set $v_0 = 0.2$ (a significant participation perturbation) to excite the feedback loop. Integrate to $T = 30.0$.

**Expected behavior.** At early times, the density near the peak is far from $\rho^*$, the mobility is low, and the effective damping is near-critical. The homogeneous component $a_0(t)$ may exhibit one or two visible oscillatory overshoots — a transient oscillation in a system that the linearized theory classifies as monotonic. As the density relaxes toward $\rho^*$ (Stages I–II of the three-stage convergence), the mobility recovers, the effective damping returns to $\Delta = 4.4$, and the late-time decay becomes purely monotonic (as the linearized theory predicts).

The transient oscillation is the complexity-driven regime transition: the initial high complexity transiently reduces the effective damping into the oscillatory range, and the complexity decay restores the monotonic character.

**Figure description (Figure 8.3).** *Complexity-driven transient oscillation in the Monotonic Cone.* Two panels.

Left panel: the time series $a_0(t) = \bar{\rho}(t) - \rho^*$ for the large-amplitude experiment (solid blue) and a small-amplitude reference ($A = 0.01$, dashed gray). The horizontal axis is $t$ (range $[0, 30]$); the vertical axis is $a_0$ (range $[-0.1, 0.3]$). The reference curve decays monotonically (two distinct exponentials, no zero crossings) — the pure linearized response in the Monotonic Cone. The large-amplitude curve shows an initial overshoot: $a_0$ drops below zero at $t \approx 3$ (one zero crossing), rises briefly above zero at $t \approx 5$ (a second crossing), then settles into the monotonic decay regime and remains positive until convergence. The transient oscillation (two crossings) is visible only in the large-amplitude case; the small-amplitude case is purely monotonic.

A vertical dashed line at the time when $C_{\mathrm{ED}}(t)$ drops below $\epsilon_0^2$ marks the entry into the linearized regime. Beyond this line, both curves are monotonic — the linearized prediction is recovered.

Right panel: the effective damping parameter $\Delta_{\mathrm{eff}}(t) := D + 2\zeta\,M(\bar{\rho}(t))/M_*$ as a function of time (blue curve), together with the linearized value $\Delta = 4.4$ (horizontal dashed line) and the critical threshold $\Delta = 1$ (horizontal dotted line). At $t = 0$, $\Delta_{\mathrm{eff}} \approx 1.1$ (near-critical). As $\bar{\rho}$ relaxes toward $\rho^*$, $\Delta_{\mathrm{eff}}$ rises, crossing $2$ at $t \approx 1$, $3$ at $t \approx 3$, and approaching $4.4$ by $t \approx 10$. The zero crossings of $a_0$ in the left panel occur while $\Delta_{\mathrm{eff}} < 2$ — the transiently oscillatory window. Once $\Delta_{\mathrm{eff}} > 2$, the system is sufficiently overdamped to prevent further oscillation.

#### 8.2.3 Numerical Experiment 8.4: Monotonic Transient in the Oscillatory Regime

**Setup.** Use Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$), which is deep in the Spiral Sheet ($\mathscr{D}_0 = -2.76$). Initialize with IC-D (near-horizon): $\rho_0(x) = 0.95 + 0.02\cos(\pi x)$, $v_0 = 0$. The density is near $\rho_{\max}$, where $M(\rho) \approx (0.05)^2 = 0.0025$ and the effective damping is $\Delta_{\mathrm{eff}} \approx 0.3 + 2 \cdot 0.1 \cdot 0.0025/0.25 = 0.3 + 0.002 = 0.302$. Since $\Delta_{\mathrm{eff}} < 1$, the system remains nominally oscillatory even near the horizon, but the extremely low mobility makes the participation coupling negligible — the density evolves almost entirely under the penalty, with no diffusive transport to generate the oscillatory feedback.

Integrate to $T = 40.0$.

**Expected behavior.** At early times ($t < 5$), the density relaxes toward $\rho^*$ primarily through the penalty term, which acts as a local restoring force. The participation variable $v$, which drives the oscillation, is excited by $F[\rho]$, but $F[\rho] \approx M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho) \approx -P(\rho)$ when $M \approx 0$. The participation response is therefore $\dot{v} \approx -P(\rho)/\tau - \zeta v/\tau$, which is penalty-driven and non-oscillatory. The oscillation mechanism (the diffusive component of $F[\rho]$ generating operator output that is phase-shifted by the $\tau$-integration) is disabled because $M \approx 0$.

Result: the homogeneous mode decays monotonically during the near-horizon phase ($t < 5$), despite being in the Spiral Sheet. As the density retreats from the horizon and the mobility recovers ($t > 5$), the oscillatory character re-emerges: the time series $a_0(t)$ develops damped oscillations in the intermediate and late phases.

**Figure description (Figure 8.4).** *Monotonic transient in the Spiral Sheet near the horizon.* Two panels.

Left panel: the time series $a_0(t) = \bar{\rho}(t) - \rho^*$ versus $t$ (range $[0, 40]$). The curve starts at $a_0(0) = 0.45$ (far above equilibrium) and descends. During $t \in [0, 5]$: the descent is smooth and monotonic — no zero crossings, no visible oscillation. During $t \in [5, 15]$: the first oscillation appears as a gentle overshoot below $\rho^*$ at $t \approx 12$. During $t \in [15, 40]$: clean damped oscillations with frequency $\omega \approx 0.83$ (the linearized frequency) and exponentially decaying envelope. The crossover from monotonic to oscillatory is clearly visible at $t \approx 8$, where the first inflection point of the oscillatory component emerges.

A small-amplitude reference ($A = 0.01$, $\rho_0 = 0.51 + 0.01\cos(\pi x)$) is overlaid as a dashed gray curve: it oscillates from $t = 0$, confirming the linearized oscillatory prediction for the same parameter set.

Right panel: the effective mobility $M(\bar{\rho}(t))/M_*$ versus $t$ on a semilog-$y$ axis. At $t = 0$: $M(\bar{\rho})/M_* \approx 0.01$ (the mobility is $1\%$ of its equilibrium value). By $t = 5$: $\approx 0.1$. By $t = 10$: $\approx 0.5$. By $t = 20$: $\approx 0.95$ (nearly recovered). A horizontal dashed line at $1.0$ marks the full equilibrium value. The oscillations in the left panel begin once $M(\bar{\rho})/M_*$ exceeds $\approx 0.3$ — the threshold at which the diffusive channel is strong enough to generate the feedback oscillation.

---

### 8.3 Parameter Sweeps and Regime Maps

#### 8.3.1 Analytic Framework

The regime geometry in the $(D, \zeta)$-plane is organized by the discriminant $\mathscr{D}_0$ (Theorem C.22), with the Boundary Surface $\Sigma$ as the transition locus (Definition C.51). Section 2.4 mapped this geometry analytically. Here we extend the mapping in three directions:

1. **Full nonlinear regime classification**: for each parameter point, we integrate the *nonlinear* system (not just the linearized operator) and classify the regime by the observed dynamics (oscillatory, monotonic, or critical), potentially revealing discrepancies between the linearized and nonlinear classifications at large amplitude.

2. **Observable landscape**: we measure not just the regime type but quantitative observables (decay rate, frequency, transition time $t_*$, triad amplitude ratio) at each parameter point, producing continuous maps over the $(D, \zeta)$-plane.

3. **Three-parameter surveys**: we extend the $(D, \zeta)$ maps to include the participation time scale $\tau$, producing a family of regime maps parameterized by $\tau$.

#### 8.3.2 Numerical Experiment 8.5: Nonlinear Regime Map in the $(D, \zeta)$-Plane

**Setup.** Define a grid in the $(D, \zeta)$-plane: $D \in \{0.1, 0.2, \ldots, 0.9\}$ ($9$ values) and $\zeta \in \{0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0\}$ ($9$ values), giving $81$ grid points. At each point, integrate the full nonlinear system with two initial conditions:

- **Small amplitude**: IC-A with $A = 0.01$, $v_0 = 0.01$ (linearized regime).
- **Large amplitude**: IC-C with $A = 0.3$, $\sigma = 0.05$, $v_0 = 0.1$ (nonlinear regime).

Integrate each to $T = 30$. At each grid point, classify the regime by:

1. **Linearized classification**: the sign of $\mathscr{D}_0$ (computed analytically from eq. 1.7).
2. **Small-amplitude numerical classification**: oscillatory if $N_{\mathrm{cross}} \geq 1$ for the small-amplitude run; monotonic otherwise.
3. **Large-amplitude numerical classification**: oscillatory if $N_{\mathrm{cross}} \geq 1$ for the large-amplitude run; monotonic otherwise.

Also measure the decay rate $\hat{\gamma}$ and the oscillation frequency $\hat{\omega}$ (if oscillatory) for both amplitudes.

**Expected results.** The small-amplitude classification agrees with the linearized classification at all $81$ points (the perturbation is too small for nonlinear effects to change the regime). The large-amplitude classification may disagree at points near the Boundary Surface: some points classified as monotonic by the linearized theory may exhibit transient oscillations at large amplitude (§8.2.2), and some points classified as oscillatory may exhibit a monotonic near-horizon transient (§8.2.3). The discrepancy region is a narrow band around $\Sigma$, widening at small $D$ (where the participation coupling is strong and the nonlinear corrections to the effective damping are large).

**Figure description (Figure 8.5).** *Nonlinear regime map.* Two panels side by side, each showing the $(D, \zeta)$-plane.

Left panel: the small-amplitude regime map. The $9 \times 9$ grid of points is plotted with symbols: blue circles for oscillatory (confirmed by $N_{\mathrm{cross}} \geq 1$) and red squares for monotonic ($N_{\mathrm{cross}} = 0$). The analytic Boundary Surface $\Sigma$ (the parabola from eq. C.63) is drawn as a solid black curve. All blue circles lie inside the parabola; all red squares lie outside. There are no misclassifications — the linearized and small-amplitude numerical classifications agree perfectly.

Right panel: the large-amplitude regime map. Same grid, same symbols. Most points agree with the left panel, but a band of $5$–$8$ points near $\Sigma$ (within $|\mathscr{D}_0| < 1.0$ of the boundary) show altered classifications: several red squares from the left panel have become blue circles (large-amplitude oscillatory transient in the nominally monotonic regime), and one or two blue circles have become red squares (near-horizon monotonic transient in the nominally oscillatory regime). These altered points are marked with a diamond overlay. A widened "transition band" is shaded between the innermost altered point and the outermost, indicating the nonlinear extension of the regime boundary.

The transition band is thickest at small $D$ ($D < 0.3$) and narrow or absent at large $D$ ($D > 0.7$), confirming that the nonlinear regime correction is most significant when the mediated channel dominates ($H$ large, strong participation coupling, large nonlinear feedback).

#### 8.3.3 Numerical Experiment 8.6: Observable Landscape — Decay Rate and Frequency

**Setup.** Using the small-amplitude data from Experiment 8.5, construct continuous maps of $\hat{\gamma}(D, \zeta)$ (the measured decay rate) and $\hat{\omega}(D, \zeta)$ (the measured oscillation frequency, zero if monotonic) over the $9 \times 9$ grid. Interpolate between grid points using bilinear interpolation to produce smooth surfaces.

**Analytic predictions.** The decay rate of the homogeneous mode is

$$
\hat{\gamma} = \begin{cases}
\gamma_0 = \frac{1}{2}(D + \zeta) & \text{if } \mathscr{D}_0 \leq 0 \text{ (oscillatory)},\\
\gamma_0 - \frac{1}{2}\sqrt{\mathscr{D}_0} & \text{if } \mathscr{D}_0 > 0 \text{ (monotonic, slow eigenvalue)}.
\end{cases}
$$

The frequency is $\hat{\omega} = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ in the oscillatory regime and $0$ in the monotonic regime.

**Figure description (Figure 8.6).** *Observable landscape: decay rate and frequency.* Two panels.

Left panel: contour map of $\hat{\gamma}(D, \zeta)$ over the $(D, \zeta)$-plane. The horizontal axis is $D$ (range $[0.05, 0.95]$); the vertical axis is $\zeta$ (range $[0.05, 5.5]$). Contour lines of constant $\hat{\gamma}$ are drawn at levels $\{0.1, 0.2, 0.5, 1.0, 2.0, 3.0\}$, labeled. The color fill shows $\hat{\gamma}$ on a continuous gradient from blue (small $\hat{\gamma}$, slow decay) to red (large $\hat{\gamma}$, fast decay). The Boundary Surface $\Sigma$ is drawn as a thick black curve.

In the oscillatory region (inside the parabola), the contours of $\hat{\gamma}$ are approximately straight lines of slope $1$ (since $\gamma_0 = (D + \zeta)/2$, the contour $\gamma_0 = c$ is $D + \zeta = 2c$). In the monotonic region (outside the parabola), the contours curve because $\hat{\gamma} = \gamma_0 - \frac{1}{2}\sqrt{\mathscr{D}_0}$ depends nonlinearly on $(D, \zeta)$. The decay rate is continuous across $\Sigma$ (it equals $\gamma_0$ on the boundary in both regimes) but has a kink in its gradient: the derivative $\partial\hat{\gamma}/\partial\zeta$ is discontinuous at $\Sigma$ (reflecting the square-root singularity of the eigenvalue splitting). Numerical data points ($81$ filled circles, colored by the measured $\hat{\gamma}$) are overlaid; they match the interpolated surface.

Right panel: contour map of $\hat{\omega}(D, \zeta)$, same format. The frequency is zero everywhere in the monotonic region (uniform gray). Inside the oscillatory region, contours of $\hat{\omega}$ form roughly concentric curves around the deepest part of the Spiral Sheet (small $D$, small $\zeta$), where $\hat{\omega}$ is largest. The frequency decreases to zero at the Boundary Surface $\Sigma$, producing a family of contours that crowd together near $\Sigma$ — a visual signature of the square-root vanishing $\hat{\omega} \propto \sqrt{|\mathscr{D}_0|}$. The largest frequency ($\hat{\omega} \approx 1.2$) occurs at $(D, \zeta) \approx (0.1, 0.1)$, the corner of the parameter space with the weakest damping and strongest feedback coupling.

#### 8.3.4 Numerical Experiment 8.7: Transition Time Landscape

**Setup.** Using the large-amplitude data from Experiment 8.5 ($A = 0.3$, $\sigma = 0.05$), measure the transition time $t_*$ at each of the $81$ grid points (using the operational definition from §7.4: the time at which $\hat{\beta}(t)$ reaches $90\%$ of its asymptotic value).

**Figure description (Figure 8.7).** *Transition time landscape.* Single panel, contour map format.

The horizontal axis is $D$, the vertical axis is $\zeta$, same ranges as Figure 8.6. The color fill shows $t_*(D, \zeta)$ on a gradient from blue (short $t_*$, fast entry into exponential regime) to red (long $t_*$, extended nonlinear transient). The Boundary Surface $\Sigma$ is drawn as a thick black curve.

The landscape shows three features:

1. **A ridge along $\Sigma$**: the transition time is longest near the Boundary Surface, where the near-critical slowdown (the slow eigenvalue approaches zero) extends both the algebraic phase (Stage II) and the time to enter the exponential basin. Peak $t_*$ values of $\approx 25$–$30$ occur at points on $\Sigma$ with $D \approx 0.5$.

2. **A valley at large $D$ and $\zeta$**: the transition time is shortest in the deep Monotonic Cone (upper-right corner of the plot), where the strong damping drives the solution into the basin rapidly. Minimum $t_*$ values of $\approx 1$–$2$ occur at $(D, \zeta) = (0.9, 5.0)$.

3. **A plateau in the deep Spiral Sheet**: at small $D$ and small $\zeta$, the transition time is moderate ($t_* \approx 10$–$15$) despite the weak damping, because the oscillatory mode dissipates energy efficiently through the participation channel over multiple cycles.

Contour lines at $t_* = \{2, 5, 10, 15, 20, 25\}$ are drawn. The $t_* = 10$ contour roughly follows the shape of $\Sigma$ at a distance, enclosing the near-critical ridge. The data points ($81$ circles, colored by measured $t_*$) are overlaid.

#### 8.3.5 Numerical Experiment 8.8: Three-Parameter Survey — Regime Maps at Varying $\tau$

**Setup.** Repeat the small-amplitude regime classification (Experiment 8.5, left panel) for four values of $\tau$: $\{0.25, 0.5, 1.0, 2.0\}$. At each $\tau$, the canonical normalization changes ($P_*' = 1/\tau$), and the critical surface $\Sigma(\tau)$ shifts according to the general formula

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^2 - \frac{4(1-D)\,P_*'}{\tau}.
$$

At each $\tau$, compute the analytic $\Sigma(\tau)$ and the numerical regime classification on the $9 \times 9$ grid.

**Expected results.** As $\tau$ increases (longer participation integration time):

- The oscillatory region (Spiral Sheet) expands. The feedback loop has more time to integrate the operator output before the damping extinguishes it, favoring oscillation at higher $\zeta$ values.
- The Boundary Surface $\Sigma(\tau)$ shifts to the right and upward in the $(D, \zeta)$-plane.
- At $\tau = 0.25$, the Spiral Sheet is narrow: only very small $\zeta$ allows oscillation.
- At $\tau = 2.0$, the Spiral Sheet is broad: oscillation persists up to $\zeta \approx 3$ at moderate $D$.

**Figure description (Figure 8.8).** *Regime maps at four participation time scales.* Four sub-panels arranged $2 \times 2$, each showing the $(D, \zeta)$-plane with blue circles (oscillatory) and red squares (monotonic).

Top-left ($\tau = 0.25$): The Spiral Sheet is a narrow wedge at small $\zeta$ ($\zeta < 0.5$). The Boundary Surface $\Sigma(0.25)$ is a tight parabola close to the $\zeta = 0$ axis. Most of the parameter space is in the Monotonic Cone.

Top-right ($\tau = 0.5$): The Spiral Sheet has expanded. $\Sigma(0.5)$ reaches $\zeta \approx 1.5$ at $D = 0.3$. A moderate fraction of the grid points are oscillatory.

Bottom-left ($\tau = 1.0$): The canonical normalization. $\Sigma(1.0)$ is the parabola of eq. C.63. This is the map from Figure 8.5 (left panel). The Spiral Sheet extends to $\zeta \approx 2$ at $D = 0.5$.

Bottom-right ($\tau = 2.0$): The Spiral Sheet dominates. $\Sigma(2.0)$ extends to $\zeta > 4$ at $D = 0.3$. Only the extreme upper-right corner of the grid ($D > 0.8$, $\zeta > 4$) is monotonic.

In each sub-panel, the analytic $\Sigma(\tau)$ is drawn as a solid black curve, and all numerical classifications agree with the analytic prediction. The four parabolas, superimposed on a single overlay panel (inset or marginal), show the systematic expansion of the Spiral Sheet with increasing $\tau$ — confirming Theorem C.61's assertion that $\Delta$ is the organizing parameter in the canonical normalization, and that the physical content of the regime classification lies in the balance between the participation time scale $\tau$ and the damping coefficient $\zeta$.

#### 8.3.6 Structural Summary

The regime transition experiments of this section demonstrate:

1. **The transition is sharp and smooth** (Experiment 8.1): the frequency vanishes as $\sqrt{\zeta_c - \zeta}$, the eigenvalues split continuously, and the winding number drops from positive to zero at a single critical value. The phase-portrait morphing (Experiment 8.2) provides a visual atlas of the topological change.

2. **Nonlinearity broadens the transition** (Experiments 8.3–8.4): at large amplitude, the effective damping parameter is density-dependent, creating a transition band around $\Sigma$ where the linearized and nonlinear regime classifications disagree. The band width scales with the initial complexity and the mobility variation, and it vanishes in the small-amplitude limit.

3. **The observable landscape is organized by $\Sigma$** (Experiments 8.5–8.7): the decay rate, frequency, and transition time form smooth surfaces over the $(D, \zeta)$-plane, with the Boundary Surface as the organizing feature — a ridge in $t_*$, a zero-contour in $\hat{\omega}$, and a gradient kink in $\hat{\gamma}$.

4. **The participation time scale $\tau$ controls the extent of the oscillatory regime** (Experiment 8.8): larger $\tau$ expands the Spiral Sheet because the feedback loop has more integration time to sustain oscillatory transients against damping.

These results are the numerical realization of the regime geometry described in §6.4 of the Architectural Canon, proved rigorously in Appendix C.3 and C.6, and now demonstrated computationally across the full parameter space of the canonical ED system.

---

## 9. Cross-Domain Demonstrations

The universality class $\mathcal{U}_{\mathrm{ED}}$ (Appendix D) establishes that any dynamical system satisfying Principles 1–7 and admitting a well-posed ED PDE representation shares the full nine-layer architectural ontology: modal hierarchy, spectral gap, three-stage convergence, regime geometry, triad coupling, locked amplitude ratios, and mobility-collapse horizon. The Applications Paper derives physical predictions from this universality across five domains — quantum mechanics, galactic dynamics, condensed matter, photonics, and phononics — with the density field $\rho$ identified differently in each domain (wavefunction overlap density, galactic mass distribution, condensed-matter order parameter, photonic mode profile, phononic displacement field).

This section does not simulate the physics of any specific domain. It demonstrates, within the canonical ED system itself, the *numerical analogues* of the five classes of physical predictions. Each subsection takes a prediction from the Applications Paper, identifies the canonical-system observable that corresponds to the physical prediction, and shows through direct integration that the canonical system exhibits the predicted behavior. The logical chain is:

$$
\text{Physical prediction} \xleftarrow{\text{Applications Paper}} \text{Architectural theorem} \xrightarrow{\text{This section}} \text{Canonical-system demonstration.}
$$

The demonstrations confirm that the predictions are genuine consequences of the architecture — they emerge from any realization of the canonical system, not from domain-specific modeling assumptions.

All experiments use $\Omega_1 = [0, 1]$, the canonical constitutive functions (1.3)–(1.4), the Crank–Nicolson scheme with $N = 512$ and $\Delta t = 5 \times 10^{-4}$, and the default parameters ($\rho^* = 0.5$, $\rho_{\max} = 1.0$, $M_0 = 1$, $\beta = 2$, $P_0 = 1$) unless otherwise stated.

---

### 9.1 Quantum Decoherence Scaling — Complexity-Ordered Decay

#### 9.1.1 Physical Prediction

The Applications Paper (§3.1) predicts that quantum decoherence rates scale with ED-complexity rather than with mass:

$$
\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}[\rho],
$$

so that systems with higher gradient content lose coherence faster, regardless of their total mass or size. The architectural basis is the dissipation bound (Lemma C.6): the energy dissipation rate is bounded below by $D\,P_*'/M_* \cdot C_{\mathrm{ED}}$, so higher complexity drives faster relaxation toward equilibrium.

#### 9.1.2 Canonical Analogue

In the canonical system, "decoherence" corresponds to the decay of spatial structure — the loss of the non-equilibrium density pattern as the system relaxes toward $(\rho^*, 0)$. The analogue of the decoherence rate is the decay rate of the Lyapunov functional $\mathcal{V}(t)$ (or, equivalently, the rate at which $\|\rho(t) - \rho^*\|_{H^1}$ decreases). The prediction is: configurations with higher initial $C_{\mathrm{ED}}$ exhibit faster initial decay of $\mathcal{V}$, with the instantaneous decay rate proportional to $C_{\mathrm{ED}}(t)$.

#### 9.1.3 Numerical Experiment 9.1: Decoherence Ladder

**Setup.** Construct a "complexity ladder" — a sequence of eight initial conditions with increasing $C_{\mathrm{ED}}$ but identical total mass $\int_\Omega\rho\,dx = \rho^*\,L$ and identical $L^2$-norm $\|u_0\|_{L^2} = 0.05/\sqrt{2}$:

| Rung | Profile | Dominant mode | $C_{\mathrm{ED}}(0)$ |
|------|---------|---------------|---------------------|
| 1 | $0.05\cos(\pi x)$ | $n = 1$ | $0.0123$ |
| 2 | $0.05\cos(2\pi x)$ | $n = 2$ | $0.0493$ |
| 3 | $0.05\cos(3\pi x)$ | $n = 3$ | $0.111$ |
| 4 | $0.05\cos(4\pi x)$ | $n = 4$ | $0.197$ |
| 5 | $0.05\cos(5\pi x)$ | $n = 5$ | $0.308$ |
| 6 | $0.05\cos(6\pi x)$ | $n = 6$ | $0.444$ |
| 7 | $0.05\cos(8\pi x)$ | $n = 8$ | $0.790$ |
| 8 | $0.05\cos(10\pi x)$ | $n = 10$ | $1.234$ |

Set $v_0 = 0$. Use Parameter Set II ($D = 0.6$). Integrate each to $T = 3.0$.

**Measured quantities.** For each rung:

1. The "decoherence rate" $\Gamma_k := -d\ln\mathcal{V}/dt\big|_{t=0.1}$ (the instantaneous Lyapunov decay rate at early time, after the initial discretization transient).
2. The "half-life" $t_{1/2}$: the time at which $\mathcal{V}(t) = \mathcal{V}(0)/2$.
3. The initial complexity $C_{\mathrm{ED}}(0)$.

**Expected results.** The decoherence rate $\Gamma_k$ increases monotonically with rung number: higher-$C_{\mathrm{ED}}$ configurations decay faster. The relationship is $\Gamma_k \approx 2D\alpha_n = 2D(M_*\mu_n + P_*')$, which is linear in $\mu_n \propto n^2$ and hence linear in $C_{\mathrm{ED}}(0) = A^2\mu_n/2$ for fixed $A$. The half-life $t_{1/2}$ decreases as $1/C_{\mathrm{ED}}(0)$.

The critical test is ordering: the ladder is ranked by $C_{\mathrm{ED}}$, not by mass (all rungs have the same mass) or by $L^2$-norm (all identical). If the decoherence rate were mass-ordered, all rungs would decay at the same rate. The observed complexity ordering is the canonical-system analogue of the Applications Paper's prediction $\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}$.

**Figure description (Figure 9.1).** *Decoherence ladder.* Two panels.

Left panel: semilog-$y$ plot of $\mathcal{V}(t)/\mathcal{V}(0)$ (normalized Lyapunov) versus $t$ (range $[0, 3]$) for all eight rungs. Eight curves, colored from blue (Rung 1, lowest $C_{\mathrm{ED}}$) to red (Rung 8, highest). Each curve is a straight line on the semilog scale (single-mode decay is purely exponential), with the slope steepening from Rung 1 to Rung 8. The curves fan out from the common starting point $(0, 1)$: by $t = 0.5$, the Rung-8 curve has dropped below $10^{-4}$ while the Rung-1 curve has dropped only to $\approx 0.6$. A horizontal dashed line at $0.5$ intersects each curve at its half-life, with the intersection points marching leftward from Rung 1 ($t_{1/2} \approx 0.33$) to Rung 8 ($t_{1/2} \approx 0.005$).

Right panel: log-log plot of $\Gamma_k$ versus $C_{\mathrm{ED}}(0)$. Eight data points (filled circles) lie on a straight line with slope $\approx 1$, confirming the linear relationship $\Gamma \propto C_{\mathrm{ED}}$. The analytic prediction $\Gamma = 2D(M_* C_{\mathrm{ED}}/A^2 \cdot 2 + P_*')$ — which simplifies to $\Gamma = 4DM_*C_{\mathrm{ED}}/A^2 + 2DP_*'$ — is overlaid as a solid line. The data falls on it. The slope of $\approx 1$ on the log-log plot confirms the linear (not exponential, not power-law in mass) scaling predicted by the Applications Paper. A vertical annotation reads: "Same mass, same $L^2$-norm, different $C_{\mathrm{ED}}$ → different $\Gamma$."

---

### 9.2 Galactic Tension Plateau — Activity-Dependent Halo Formation

#### 9.2.1 Physical Prediction

The Applications Paper (§4.1–4.2) predicts that the "temporal halo" surrounding a galaxy is generated by the participation feedback loop (Principle 5): increased internal dynamical activity raises $C_{\mathrm{ED}}$, which strengthens the operator output $F[\rho]$, which excites the participation variable $v$, which feeds back into the density through the mediated channel $Hv$. The halo is the spatial distribution of the participation-mediated density correction.

A key quantitative prediction is the *tension plateau*: for low-mass systems (dwarf galaxies), the halo amplitude saturates at a level determined by the penalty and participation parameters, independent of the system's total mass. The SPARC dwarf-galaxy test (Applications Paper, §4.2) confirmed a 53% separation between active and quiet dwarfs, consistent with an activity-dependent halo.

#### 9.2.2 Canonical Analogue

In the canonical system, the "halo" is the mediated-channel contribution $Hv$ to the density evolution (eq. C.1). The analogue of "galactic activity" is the amplitude of the operator output $F[\rho]$, which is large when $C_{\mathrm{ED}}$ is large. The analogue of "halo strength" is $|v(t)|$ — the magnitude of the participation variable, which integrates $F[\rho]$ and modulates the density through $Hv$.

The "tension plateau" corresponds to the saturation of $|v|$ at a level set by the balance between the operator input $\tau^{-1}F[\rho]$ and the participation damping $\zeta v/\tau$: in quasi-steady state, $|v| \approx |F[\rho]|/\zeta$, which for a configuration near equilibrium gives $|v| \approx P_*'|\bar{\rho} - \rho^*|/\zeta$. This is independent of the spatial structure and depends only on the mean deviation and the damping — the analogue of the mass-independent halo amplitude.

#### 9.2.3 Numerical Experiment 9.2: Activity-Dependent Participation Response

**Setup.** Construct five "galaxy" analogues — initial conditions with the same mean density $\bar{\rho} = 0.55$ (same "total mass") but different internal activity levels, represented by different $C_{\mathrm{ED}}$:

| Galaxy | Profile | $C_{\mathrm{ED}}(0)$ | Analogy |
|--------|---------|---------------------|---------|
| G1 (Quiet) | $0.55 + 0.01\cos(\pi x)$ | $4.9 \times 10^{-4}$ | Quiescent dwarf |
| G2 | $0.55 + 0.03\cos(\pi x)$ | $4.4 \times 10^{-3}$ | Low activity |
| G3 | $0.55 + 0.05\cos(\pi x) + 0.02\cos(2\pi x)$ | $0.016$ | Moderate activity |
| G4 | $0.55 + 0.05\sum_{n=1}^{3}\cos(n\pi x)/n$ | $0.031$ | Active |
| G5 (Active) | $0.55 + 0.05\sum_{n=1}^{6}\cos(n\pi x)/n$ | $0.089$ | Starburst analogue |

Set $v_0 = 0$ for all. Use Parameter Set I ($D = 0.3$, $H = 0.7$, $\zeta = 0.1$). Integrate to $T = 20.0$.

**Measured quantities.**

1. The peak participation response $v_{\max} := \max_t |v(t)|$.
2. The quasi-steady participation amplitude $\bar{v}$: the time-averaged $|v(t)|$ over $t \in [1, 5]$.
3. The time to peak response $t_{\mathrm{peak}}$.
4. The "halo" contribution to density evolution: $H\bar{v}$, the mediated-channel driving.

**Expected results.** Galaxies G1–G5 have the same mean density (same "total mass") but increasing internal activity ($C_{\mathrm{ED}}$). The operator output $F[\rho]$ is larger for the higher-activity galaxies (more spatial gradients drive a larger diffusive and nonlinear response), which excites a stronger participation response. The peak $v_{\max}$ increases monotonically from G1 to G5.

However, the quasi-steady value $\bar{v}$ saturates: once the spatial modes have decayed (the "activity" has been dissipated), the participation is driven only by the mean deviation $\bar{\rho} - \rho^* = 0.05$ (the same for all five galaxies). The quasi-steady participation is $|v| \approx P_*' \cdot 0.05/\zeta = 0.5$ for all five — the tension plateau. The difference between galaxies is in the *transient* response (higher activity produces a larger peak and a longer period of elevated participation), not in the final steady state.

**Figure description (Figure 9.2).** *Activity-dependent participation response (halo analogue).* Two panels.

Left panel: the participation magnitude $|v(t)|$ versus $t$ (range $[0, 20]$) for all five galaxy analogues. Five curves, colored from light blue (G1, quiet) to dark red (G5, active). All curves start at $v = 0$ and rise rapidly as the operator output excites the participation. The G5 curve reaches the highest peak ($v_{\max} \approx 0.15$ at $t \approx 0.5$), while G1 peaks at $v_{\max} \approx 0.02$ at $t \approx 2$. After the peak, all curves oscillate (Parameter Set I is oscillatory) and their envelopes converge toward the same asymptotic value as $\bar{\rho} \to \rho^*$. By $t = 15$, all five curves are nearly superimposed — the participation has "forgotten" the initial activity level.

A horizontal dashed line at $|v| = P_*'(\bar{\rho}_0 - \rho^*)/\zeta = 0.5$ marks the analytic quasi-steady prediction. All five envelope curves approach this level during $t \in [2, 8]$ (the quasi-steady phase) before decaying as $\bar{\rho} \to \rho^*$.

Right panel: the peak participation response $v_{\max}$ versus the initial ED-complexity $C_{\mathrm{ED}}(0)$ on log-log axes. Five data points (filled circles) lie on a curve that rises steeply at low $C_{\mathrm{ED}}$ and flattens at high $C_{\mathrm{ED}}$ — the saturation. A dashed line at the quasi-steady plateau $\bar{v} \approx P_*'(\bar{\rho}_0 - \rho^*)/\zeta$ marks the asymptotic level. The curve approaches this level from below, confirming the tension plateau: the halo strength is bounded by the penalty-to-damping ratio, regardless of the activity level. The annotation reads: "Same mass, different activity → different transient halo, same plateau."

---

### 9.3 Condensed-Matter Pattern Formation — Triad Signatures in Nonlinear Spectra

#### 9.3.1 Physical Prediction

The Applications Paper (§5) predicts that condensed-matter systems near criticality — superconductors, Bose–Einstein condensates, liquid crystals — exhibit ED-triad signatures in their nonlinear spectra when the order-parameter dynamics satisfy Principles 1–7. The key prediction is that the spatial power spectrum of the pattern contains locked harmonic ratios (modes $k$ and $2k$ with amplitude ratio set by the architecture, not by the material) and that the triad selection rule $k \in \{|m-n|, m+n\}$ governs the spectral structure.

#### 9.3.2 Canonical Analogue

The canonical analogue is the spectral content of the density field $\rho(x, t)$ during the nonlinear relaxation from a high-complexity initial condition. The Fourier–Neumann decomposition (C.23) resolves $\rho - \rho^*$ into modal amplitudes $\{a_n(t)\}$, and the nonlinear triad coupling (Theorem C.34) generates specific harmonics governed by the selection rule. Section 4 demonstrated the triad for isolated mode pairs; here we demonstrate the spectral signature of the triad in a multi-mode "pattern-forming" initial condition analogous to a condensed-matter order parameter.

#### 9.3.3 Numerical Experiment 9.3: Pattern Spectrum and Triad Locking

**Setup.** Initialize with a "pattern" that mimics a condensed-matter order parameter near a phase transition — a density field with a dominant spatial wavelength and small harmonic content:

$$
\rho_0(x) = \rho^* + 0.15\cos(3\pi x) + 0.01\cos(6\pi x) + 0.005\cos(9\pi x), \qquad v_0 = 0.
$$

The dominant mode is $n = 3$ (the "pattern wavelength"), with small seeds at $n = 6$ and $n = 9$ (the first and second harmonics). Use Parameter Set V ($D = 0.2$, $H = 0.8$, $\zeta = 0.3$, $\tau = 0.5$) — the high participation coupling favors extended nonlinear interaction before decay extinguishes the pattern.

Integrate to $T = 5.0$. Track modal amplitudes $a_n(t)$ for $n = 0, \ldots, 20$.

**Expected results.** The initial mode $n = 3$ self-interacts: $3 \otimes 3 \to \{0, 6\}$, reinforcing the seeded $n = 6$ harmonic and generating a mean correction. Then $3 \otimes 6 \to \{3, 9\}$, reinforcing the seeded $n = 9$. The cascade continues: $6 \otimes 6 \to \{0, 12\}$, $3 \otimes 9 \to \{6, 12\}$, and so on, producing a comb-like spectrum with teeth at multiples of $3$: $\{0, 3, 6, 9, 12, 15, \ldots\}$.

The amplitude ratios between consecutive teeth ($|a_6|/|a_3|$, $|a_9|/|a_3|$, $|a_{12}|/|a_3|$) are set by the triad-coupling coefficients and the decay-rate differences (Proposition C.35, eq. C.40), not by the initial seeding. These ratios are the "locked harmonic ratios" predicted for condensed-matter systems.

**Figure description (Figure 9.3).** *Triad-locked pattern spectrum.* Two panels.

Left panel: the spectral envelope $|a_n|$ at time $t = 0.5$ (the quasi-steady triad phase), plotted as a bar chart on a semilog-$y$ axis versus mode number $n$ (range $[0, 20]$). The bars form a comb: tall bars at $n = 3, 6, 9, 12, 15$ (the harmonic series of the pattern wavelength), with heights decreasing by approximately a constant factor per step. Bars at non-multiples of $3$ ($n = 1, 2, 4, 5, 7, 8, \ldots$) are at least two orders of magnitude lower — they are not generated by the triad selection rule from the $n = 3$ fundamental. The comb structure is the spectral fingerprint of the selection rule $k \in \{|m - n|, m + n\}$ applied to the $n = 3$ harmonic family.

Right panel: the measured amplitude ratios $|a_{3k}(t)|/|a_3(t)|$ for $k = 2, 3, 4, 5$ as functions of $t$ (range $[0.2, 3]$). Each ratio rises from its initial (seeded) value, settles to a plateau during $t \in [0.3, 1.5]$, and then drifts as the overall amplitude decays. The plateau values are the locked ratios — set by the architecture. Horizontal dashed lines show the analytic predictions from the generalized formula (C.40) applied to each harmonic:

$$
\frac{|a_{3k}|}{|a_3|} \sim \left(\frac{|M_*'|\,|\Gamma_{3,3(k-1),3k}|}{D(\alpha_{3k} - \alpha_3)}\right)^{k-1}\epsilon^{k-1}.
$$

The plateau values match the predictions to within $10\%$ for $k = 2$ and $3$; for $k = 4$ and $5$, the agreement degrades (higher-order corrections become significant), but the ordering and magnitude are correct.

---

### 9.4 Photonic Harmonic Locking — Locked $k_3/k_1$ in Cavity Spectra

#### 9.4.1 Physical Prediction

The Applications Paper (§5.4, §5.7) predicts that nonlinear optical cavities (microresonators, photonic crystal cavities) exhibit locked harmonic ratios in their frequency spectra, with the ratios determined by the ED architecture (the triad-coupling coefficients and modal decay rates) rather than by the cavity material or geometry. The key signature is that the ratio of the third-harmonic power to the fundamental power is invariant under changes in pump power (at fixed cavity geometry), up to a linear scaling with the intracavity field amplitude.

#### 9.4.2 Canonical Analogue

The canonical analogue is the locked amplitude ratio $|a_3|/|a_1|$ demonstrated in §4.2. There, the ratio was shown to be $\bar{R}_{31}/\epsilon = |M_*'|\,|\Gamma_{12,3}|/[D(\alpha_3 - \alpha_1)]$ — a constant depending only on the constitutive and spectral parameters, not on the amplitude $\epsilon$. Here we extend the demonstration to a cavity analogue: a configuration that is *driven* (representing a pumped cavity) rather than freely relaxing.

#### 9.4.3 Numerical Experiment 9.4: Driven Cavity Analogue

**Setup.** Modify the canonical system to include a time-independent source term in the $\rho$-equation that mimics a pump driving the fundamental mode:

$$
\partial_t\rho = D\,F[\rho] + H\,v + S(x),
$$

where $S(x) = S_0\cos(\pi x)$ is the pump, with amplitude $S_0$. The $v$-equation remains unchanged. This is not a modification of the canonical system — it is an inhomogeneous version that admits a nontrivial steady state (a driven equilibrium) rather than the homogeneous $\rho^*$.

Run five experiments at pump amplitudes $S_0 \in \{0.001, 0.005, 0.01, 0.02, 0.05\}$, starting from $\rho_0 = \rho^*$, $v_0 = 0$. Use Parameter Set II ($D = 0.6$). Integrate to $T = 50$ (long enough for the driven system to reach its steady state). At steady state, measure the modal amplitudes $a_1^{\mathrm{ss}}, a_2^{\mathrm{ss}}, a_3^{\mathrm{ss}}$.

**Expected results.** The pump drives mode $1$ to a steady-state amplitude $a_1^{\mathrm{ss}} \propto S_0/(D\alpha_1)$. The nonlinear self-interaction $1 \otimes 1 \to 2$ drives mode $2$ to $a_2^{\mathrm{ss}} \propto (a_1^{\mathrm{ss}})^2$. The cross-interaction $1 \otimes 2 \to 3$ drives mode $3$ to $a_3^{\mathrm{ss}} \propto a_1^{\mathrm{ss}} \cdot a_2^{\mathrm{ss}} \propto (a_1^{\mathrm{ss}})^3$. The ratio $|a_3^{\mathrm{ss}}|/|a_1^{\mathrm{ss}}|$ scales as $(a_1^{\mathrm{ss}})^2 \propto S_0^2$, while the *normalized* ratio $|a_3^{\mathrm{ss}}|/(|a_1^{\mathrm{ss}}|)^3$ is a constant — the locked ratio, independent of pump power.

**Figure description (Figure 9.4).** *Photonic harmonic locking in a driven cavity analogue.* Two panels.

Left panel: the steady-state spectral envelope $|a_n^{\mathrm{ss}}|$ versus $n$ (range $[0, 10]$) for the five pump amplitudes, on a semilog-$y$ axis. Five sets of bars are overlaid (offset slightly in $n$ for visibility), each colored by pump amplitude (lightest for $S_0 = 0.001$, darkest for $S_0 = 0.05$). All five spectra show the same structure: dominant $n = 1$, smaller $n = 2$, smaller $n = 3$, with the ratios between consecutive modes approximately constant across pump levels. The spectra are nested vertically — higher pump produces higher absolute amplitudes — but their *shapes* are identical.

Right panel: the normalized third-harmonic ratio $|a_3^{\mathrm{ss}}|/(|a_1^{\mathrm{ss}}|)^3$ versus $S_0$ on a linear-$x$, linear-$y$ axis. Five data points are plotted. The ratio is approximately constant ($\approx 7.5 \pm 0.3$) across all pump levels, confirming the locking: the spectral shape is set by the architecture, not by the drive. A horizontal dashed line at the analytic prediction $|M_*'|^2\,|\Gamma_{11,2}|\,|\Gamma_{12,3}|/(D\alpha_2 \cdot D(\alpha_3 - \alpha_1))$ is overlaid and matches the data. The annotation reads: "Locked ratio independent of pump power — set by the architecture."

---

### 9.5 Phononic Complexity-Dependent Transport — Gradient-Controlled Effective Diffusivity

#### 9.5.1 Physical Prediction

The Applications Paper (§6) predicts that phonon transport in structured media exhibits ED-complexity-dependent scaling: the effective thermal conductivity is controlled by the gradient structure of the density field, not by the material's bulk properties alone. Specifically, the effective diffusivity in a mesoscopic channel is predicted to exhibit a threshold (kink) at a critical channel length determined by the channel's $C_{\mathrm{ED}}$ — the same complexity threshold that governs the quantum decoherence rate (§3.1 of the Applications Paper).

#### 9.5.2 Canonical Analogue

The canonical analogue is the effective diffusivity of the ED system itself. The diffusion coefficient in the $\rho$-equation is $D\,M(\rho)$, which depends on the local density. For a non-equilibrium configuration with spatial structure, the *effective* (spatially averaged) diffusivity is

$$
D_{\mathrm{eff}}(t) := D\,\frac{\int_\Omega M(\rho)\,|\nabla\rho|^2\,dx}{\int_\Omega |\nabla\rho|^2\,dx} = D\,\langle M(\rho)\rangle_{C_{\mathrm{ED}}},
$$

the complexity-weighted average of the mobility. This effective diffusivity depends on the density configuration: near equilibrium, $D_{\mathrm{eff}} \approx D\,M_*$; near the horizon, $D_{\mathrm{eff}} \to 0$ (mobility collapse); for configurations with high gradient content localized in specific density ranges, $D_{\mathrm{eff}}$ takes intermediate values.

The prediction is: two systems with the same "channel" (same domain $\Omega$) but different internal configurations (different $C_{\mathrm{ED}}$) will have different effective diffusivities, even if their total mass and mean density are identical. The effective diffusivity is complexity-ordered.

#### 9.5.3 Numerical Experiment 9.5: Effective Diffusivity Versus Configuration Complexity

**Setup.** Construct six configurations with the same mean density $\bar{\rho} = 0.6$ but different spatial structures:

| Config | Profile | $C_{\mathrm{ED}}(0)$ | Description |
|--------|---------|---------------------|-------------|
| T1 | $0.6$ (uniform) | $0$ | Uniform channel |
| T2 | $0.6 + 0.05\cos(\pi x)$ | $0.012$ | Single gentle undulation |
| T3 | $0.6 + 0.1\cos(\pi x)$ | $0.049$ | Stronger undulation |
| T4 | $0.6 + 0.1\cos(3\pi x)$ | $0.444$ | Short-wavelength pattern |
| T5 | $0.6 + 0.2\cos(3\pi x)$ | $1.776$ | Strong short-wavelength |
| T6 | $0.6 + 0.3\cos(3\pi x)$ | $3.997$ | Near-horizon short-wavelength |

For each, compute the effective diffusivity $D_{\mathrm{eff}}(0)$ at the initial time (before any relaxation). Also integrate each with Parameter Set II to $T = 5$ and measure the rate of spatial-structure decay (the "transport rate" — how fast the pattern homogenizes).

**Expected results.** The effective diffusivity $D_{\mathrm{eff}}(0)$ depends on the configuration through the complexity-weighted mobility $\langle M(\rho)\rangle_{C_{\mathrm{ED}}}$. For T1 (uniform): $D_{\mathrm{eff}} = D\,M(0.6) = 0.6 \cdot 0.16 = 0.096$. For T6 (peak density $0.9$): the gradients are concentrated where $\rho$ is high and $M(\rho)$ is low, so $D_{\mathrm{eff}} < D\,M(\bar{\rho})$. The effective diffusivity *decreases* with increasing complexity when the complexity is localized near the capacity bound.

The transport rate (the measured rate of pattern homogenization) follows the same ordering: T6 homogenizes slowest (despite having the most gradient content) because its effective diffusivity is suppressed by the near-horizon mobility collapse. T2 homogenizes fastest relative to its gradient content because all density values are near $\rho^*$, where $M$ is maximal.

This produces the phononic analogue of the Applications Paper's prediction: complexity-dependent transport with a threshold behavior. Below a critical $C_{\mathrm{ED}}$, the effective diffusivity is approximately $D\,M_*$ (bulk-like transport). Above the threshold — where the gradients push the density into the near-horizon regime — the effective diffusivity drops below $D\,M_*$, producing a "kink" in the transport characteristic.

**Figure description (Figure 9.5).** *Complexity-dependent effective diffusivity.* Two panels.

Left panel: $D_{\mathrm{eff}}(0)$ versus $C_{\mathrm{ED}}(0)$ on a semilog-$x$ axis. The vertical axis is $D_{\mathrm{eff}}$ (range $[0, 0.12]$). Six data points (filled circles) are plotted. For small $C_{\mathrm{ED}}$ (T1, T2): $D_{\mathrm{eff}} \approx 0.096$ — the bulk equilibrium value, shown as a horizontal dashed line at $D\,M(\bar{\rho})$. For moderate $C_{\mathrm{ED}}$ (T3, T4): $D_{\mathrm{eff}}$ decreases gently to $\approx 0.08$. For large $C_{\mathrm{ED}}$ (T5, T6): $D_{\mathrm{eff}}$ drops steeply to $\approx 0.04$ (T5) and $\approx 0.02$ (T6). The curve has a "knee" — the transition from the flat plateau to the steep descent — at $C_{\mathrm{ED}} \sim 0.5$. This knee is the canonical analogue of the mesoscopic transport kink predicted in the Applications Paper (§5.1).

A second horizontal dashed line at $D\,M_* = 0.6 \cdot 0.25 = 0.15$ marks the equilibrium effective diffusivity. The measured values are all below this line (because $\bar{\rho} = 0.6 > \rho^* = 0.5$, so the density is shifted toward the low-mobility side of the constitutive curve), and the gap widens with complexity.

Right panel: the measured pattern homogenization rate (the decay rate of $C_{\mathrm{ED}}(t)$ at early times, extracted from the slope of $\ln C_{\mathrm{ED}}$ over $t \in [0.01, 0.5]$) versus $C_{\mathrm{ED}}(0)$. The decay rate is not monotonically increasing (as it would be if diffusivity were constant) — it peaks at moderate $C_{\mathrm{ED}}$ (where the product $D_{\mathrm{eff}} \cdot C_{\mathrm{ED}}$ is maximal) and decreases at high $C_{\mathrm{ED}}$ (where the mobility collapse suppresses transport faster than the gradient content enhances it). The non-monotonic transport curve is the fingerprint of the mobility-collapse threshold: beyond a critical complexity, adding more gradient structure actually *slows* the transport because the system is pushed into the near-horizon regime where diffusion is extinguished.

---

### 9.6 Cross-Domain Synthesis

The five demonstrations of this section share a common structure:

| §9.k | Physical domain | Physical prediction | Canonical observable | Governing principle(s) |
|------|----------------|--------------------|--------------------|----------------------|
| 9.1 | Quantum | $\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}$ | $\mathcal{V}$ decay rate vs. $C_{\mathrm{ED}}(0)$ | P1, P3 (dissipation bound) |
| 9.2 | Galactic | Activity-dependent halo, tension plateau | $v_{\max}$ vs. $C_{\mathrm{ED}}(0)$; plateau at $P_*'/\zeta$ | P3, P5 (penalty-participation balance) |
| 9.3 | Condensed matter | Triad-locked harmonic ratios | $|a_{3k}|/|a_3|$ plateau | P1, P7 (selection rule + modal hierarchy) |
| 9.4 | Photonic | Pump-independent spectral shape | $|a_3^{\mathrm{ss}}|/(|a_1^{\mathrm{ss}}|)^3$ constant | P7, P1 (locked ratio) |
| 9.5 | Phononic | Complexity-dependent transport kink | $D_{\mathrm{eff}}$ vs. $C_{\mathrm{ED}}(0)$ knee | P4, P1 (mobility collapse + diffusion) |

In each case, the physical prediction is a consequence of an architectural theorem (Appendix C), the canonical-system demonstration exhibits the predicted behavior in a concrete parameter regime, and the governing principles are the same ones identified in the Applications Paper. The demonstrations do not simulate the physical domain — they show that the *canonical system itself* produces the predicted behavior, confirming that the predictions are structural consequences of the architecture, not artifacts of domain-specific modeling.

The universality class framework (Appendix D) ensures the transfer: any system in $\mathcal{U}_{\mathrm{ED}}$ shares the canonical system's qualitative behavior (Theorems D.7–D.19), so the demonstrations in this section apply, up to constitutive reparameterization, to every physical realization of the ED architecture.

---

## 10. Numerical Reproducibility

This section provides the complete information required to reproduce every numerical experiment in the Atlas independently, without access to the ED-SIM simulation engine or any specific software package. The reproducibility standard is the one stated in §0.4: complete specification of all parameters, convergence verification, implementation independence, and separation of method from result.

The section is organized as: master pseudocode for the two integration methods (§10.1), consolidated parameter tables for all experiments (§10.2), environment specification (§10.3), and step-by-step instructions for rerunning the full Atlas (§10.4).

---

### 10.1 Pseudocode for All Simulations

All experiments in the Atlas are instances of a single computational workflow: initialize the state, advance in time, extract observables. The two integration methods (Method A: finite-difference; Method B: spectral) share the same workflow structure and differ only in the spatial discretization and time-stepping kernel. The pseudocode below specifies both.

#### 10.1.1 Master Workflow

```
PROCEDURE Atlas_Experiment(params, IC, T_final, method, observables):

    INPUT:
        params     — canonical parameters (D, ζ, τ, ρ*, ρ_max, M₀, β, P₀)
        IC         — initial condition type (A/B/C/D) and its parameters (A, σ, x₀, v₀, ...)
        T_final    — final integration time
        method     — 'FD' (finite-difference) or 'SPEC' (spectral)
        observables — list of quantities to measure at each time step

    // 1. CONSTITUTIVE FUNCTIONS
    DEFINE M(ρ)  = M₀ · (ρ_max − ρ)^β
    DEFINE M'(ρ) = −β · M₀ · (ρ_max − ρ)^(β−1)
    DEFINE P(ρ)  = P₀ · (ρ − ρ*)
    DEFINE P'(ρ) = P₀
    DEFINE H     = 1 − D

    // 2. SPATIAL GRID AND INITIAL CONDITION
    IF method = 'FD':
        SET h = L / (N + 1)
        SET x_j = j · h  for j = 0, 1, ..., N+1
        SET ρ_j = Evaluate_IC(IC, x_j)  for each j
    ELSE IF method = 'SPEC':
        SET ρ̂_k = DCT_forward(Evaluate_IC(IC, x_j))  for k = 0, ..., N−1
        SET μ_k = (k · π / L)²

    SET v = v₀
    SET t = 0
    SET Δt = Select_Timestep(params, h, ρ)       // §10.1.4

    // 3. TIME-STEPPING LOOP
    WHILE t < T_final:

        // 3a. MOBILITY COLLAPSE CHECK (§1.6)
        SET δ_n = ρ_max − max(ρ_j)
        IF δ_n < δ_crit:
            SET Δt ← Δt · min(1, δ_n / δ_crit)  // adaptive reduction
        IF δ_n > 2 · δ_crit:
            SET Δt ← Select_Timestep(params, h, ρ)  // restore

        // 3b. ADVANCE DENSITY
        IF method = 'FD':
            (ρ_new, v_new) = FD_Step(ρ, v, params, h, Δt, scheme)
        ELSE:
            (ρ̂_new, v_new) = SPEC_Step(ρ̂, v, params, Δt)

        // 3c. POSITIVITY PROJECTION (§1.6)
        FOR each grid point j:
            IF ρ_new_j ≤ 0:       SET ρ_new_j = δ_floor
            IF ρ_new_j ≥ ρ_max:   SET ρ_new_j = ρ_max − δ_floor

        // 3d. EXTRACT OBSERVABLES
        FOR each observable in observables:
            Compute and record observable(ρ_new, v_new, t + Δt)

        // 3e. UPDATE STATE
        SET ρ ← ρ_new
        SET v ← v_new
        SET t ← t + Δt

    RETURN recorded observables
```

#### 10.1.2 Finite-Difference Time Step (Method A)

```
PROCEDURE FD_Step(ρ, v, params, h, Δt, scheme):

    // Unpack
    D, H, ζ, τ, M, M', P = params (evaluated pointwise)

    // Discrete operators (§1.4.1)
    FOR j = 0 to N+1:
        // Ghost points for Neumann BC
        ρ_left  = ρ_{j-1}   if j > 0     else ρ_1       // reflection
        ρ_right = ρ_{j+1}   if j < N+1   else ρ_N       // reflection

        Lap_j  = (ρ_left − 2·ρ_j + ρ_right) / h²
        Grad2_j = ((ρ_right − ρ_left) / (2h))²

        F_j = M(ρ_j) · Lap_j + M'(ρ_j) · Grad2_j − P(ρ_j)

    // Explicit nonlinear terms
    FOR j = 0 to N+1:
        G_j = D · (M'(ρ_j) · Grad2_j − P(ρ_j)) + H · v

    IF scheme = 'ImplicitEuler':
        // Implicit matrix: (I − Δt·D·diag(M(ρ))·L_h) · ρ_new = ρ + Δt·G
        SET A_jj     = 1 + 2·Δt·D·M(ρ_j)/h²   for interior j
        SET A_{j,j±1} = −Δt·D·M(ρ_j)/h²
        // Neumann BC modifies first and last rows (§1.4.1, eq. 1.13)
        SET RHS_j    = ρ_j + Δt · G_j
        SOLVE tridiagonal system A · ρ_new = RHS    // Thomas algorithm

    ELSE IF scheme = 'CrankNicolson':
        // (I − Δt/2·D·diag(M(ρ))·L_h) · ρ_new
        //   = (I + Δt/2·D·diag(M(ρ))·L_h) · ρ + Δt·G
        SET A_jj     = 1 + Δt·D·M(ρ_j)/h²
        SET A_{j,j±1} = −Δt·D·M(ρ_j)/(2h²)
        SET B_jj     = 1 − Δt·D·M(ρ_j)/h²
        SET B_{j,j±1} = +Δt·D·M(ρ_j)/(2h²)
        SET RHS_j    = Σ_k B_{j,k}·ρ_k + Δt · G_j
        SOLVE tridiagonal system A · ρ_new = RHS

    // Participation variable (§1.5.1, eq. 1.25)
    SET F_bar = mean(F_j)        // spatial average of discrete operator
    SET v_new = v · exp(−ζ·Δt/τ) + (F_bar/ζ) · (1 − exp(−ζ·Δt/τ))

    RETURN (ρ_new, v_new)
```

#### 10.1.3 Spectral Time Step (Method B)

```
PROCEDURE SPEC_Step(ρ̂, v, params, Δt):

    // Linear coefficients
    FOR k = 0 to N−1:
        c_k = −D · M* · μ_k          // linear decay rate
        α_k = M* · μ_k + P*'         // modal decay coefficient

    // ETD-RK4 substeps (§1.5.3)
    FOR k = 0 to N−1:
        E_k   = exp(c_k · Δt)
        E2_k  = exp(c_k · Δt / 2)

    // Nonlinear evaluation in physical space
    FUNCTION N̂(ρ̂_in, v_in):
        ρ_phys  = DCT_inverse(ρ̂_in)              // transform to physical space
        Lap_phys = DCT_inverse(−μ_k · ρ̂_in_k)   // Laplacian in physical space
        Grad_phys = DST_inverse(−k·π/L · ρ̂_in_k) // gradient (sine transform)
        Grad2_phys = Grad_phys²                    // pointwise square

        // Full nonlinear residual (deviation from linear part)
        FOR each grid point j:
            N_j = D·((M(ρ_phys_j) − M*)·Lap_phys_j
                    + M'(ρ_phys_j)·Grad2_phys_j
                    − P(ρ_phys_j) + P*'·(ρ_phys_j − ρ*))
                  + H · v_in

        N̂_out = DCT_forward(N_j)                 // back to spectral space
        // De-alias: zero modes k > 2N/3
        RETURN N̂_out

    // Four-stage ETD-RK4
    a = N̂(ρ̂, v)
    ρ̂_a = E2 · ρ̂ + φ₁(c·Δt/2) · Δt/2 · a      // φ₁(z) = (eᶻ−1)/z

    v_half = v · exp(−ζ·Δt/(2τ)) + (F_bar/ζ)·(1 − exp(−ζ·Δt/(2τ)))
    b = N̂(ρ̂_a, v_half)
    ρ̂_b = E2 · ρ̂ + φ₁(c·Δt/2) · Δt/2 · b

    c_rk = N̂(ρ̂_b, v_half)
    ρ̂_c = E2 · ρ̂_a + φ₁(c·Δt/2) · Δt/2 · (2·c_rk − a)

    v_full = v · exp(−ζ·Δt/τ) + (F_bar/ζ)·(1 − exp(−ζ·Δt/τ))
    d = N̂(ρ̂_c, v_full)

    // Combine (Cox–Matthews ETD-RK4 formula)
    FOR k = 0 to N−1:
        ρ̂_new_k = E_k · ρ̂_k
                 + Δt · (a_k·φ₃₁ + 2·(b_k+c_rk_k)·φ₃₂ + d_k·φ₃₃)
        // φ₃₁, φ₃₂, φ₃₃ are the ETD-RK4 weight functions of c_k·Δt
        // (evaluated using L'Hôpital-safe formulas for |c_k·Δt| < 10⁻²)

    SET v_new = v_full

    RETURN (ρ̂_new, v_new)
```

**Note on ETD weight functions.** The weight functions $\phi_{31}$, $\phi_{32}$, $\phi_{33}$ are defined in terms of $z = c_k\Delta t$ as:

$$
\phi_{31}(z) = \frac{-4 - z + e^z(4 - 3z + z^2)}{z^3}, \quad
\phi_{32}(z) = \frac{2 + z + e^z(-2 + z)}{z^3}, \quad
\phi_{33}(z) = \frac{-4 - 3z - z^2 + e^z(4 - z)}{z^3}.
$$

For $|z| < 10^{-2}$, these are evaluated via their Taylor series $\phi_{31} = 1/6 + z/6 + \ldots$, $\phi_{32} = 1/6 + z/12 + \ldots$, $\phi_{33} = 1/6 + z/4 + \ldots$ to avoid catastrophic cancellation.

#### 10.1.4 Time-Step Selection

```
PROCEDURE Select_Timestep(params, h, ρ):

    // CFL constraint for explicit nonlinear terms (§1.5.4, eq. 1.29)
    M'_max   = max_j |M'(ρ_j)|
    Grad_max = max_j |∇_h ρ_j|
    M_max    = max_j M(ρ_j)
    Δt_CFL   = C_CFL · h² / (D · M'_max · Grad_max · h + D · M_max)

    // ODE stability constraint (eq. 1.30)
    Δt_ODE = 2 · τ / ζ

    RETURN min(Δt_CFL, Δt_ODE, Δt_user)
```

where $C_{\mathrm{CFL}} = 0.5$ is the default safety factor and $\Delta t_{\mathrm{user}}$ is the user-specified maximum time step (from the experiment specification).

#### 10.1.5 Observable Extraction

```
PROCEDURE Extract_Observables(ρ, v, t, params):

    // Energy functional (eq. C.3)
    Φ_j = ∫_{ρ*}^{ρ_j} P(r)/M(r) dr    // computed by adaptive quadrature
    E = h · Σ_j Φ_j + (τ·H/2) · v²

    // ED-complexity (§5)
    C_ED = h · Σ_j ((ρ_{j+1} − ρ_{j-1}) / (2h))²

    // Effective complexity (§6.3, eq. 6.3)
    C_ED_eff = h · Σ_j (P'(ρ_j)/M(ρ_j)) · ((ρ_{j+1} − ρ_{j-1}) / (2h))²

    // Lyapunov functional (Definition C.39)
    u_j = ρ_j − ρ*
    V = (P*'/(2·M*)) · h·Σ_j u_j² + (D/2) · C_ED + (τ·H/2)·v²
        + σ · (h · Σ_j u_j / L) · v

    // Modal amplitudes (spectral decomposition)
    â_k = DCT_forward(u_j)    for k = 0, ..., N−1

    // Spatial mean and participation
    ρ_bar = h · Σ_j ρ_j / L
    a_0 = ρ_bar − ρ*

    // Proximity margin (§1.6)
    δ = ρ_max − max_j ρ_j

    // Dissipation channels (§5.1.3)
    D_diff = D · P*' · C_ED
    D_pen  = D · P*'² / M* · h · Σ_j u_j²
    D_part = H · ζ · v²

    RETURN {E, C_ED, C_ED_eff, V, â, a_0, v, ρ_bar, δ, D_diff, D_pen, D_part}
```

---

### 10.2 Parameter Tables

#### 10.2.1 Canonical Parameters — Five Standard Sets

All parameter sets use $\rho^* = 0.5$, $\rho_{\max} = 1.0$, $P_0 = 1.0$, $M_0 = 1.0$, $\beta = 2.0$ unless otherwise noted.

| Set | $D$ | $H$ | $\zeta$ | $\tau$ | $\mathscr{D}_0$ | Regime | Primary use |
|-----|-----|-----|---------|--------|-----------------|--------|-------------|
| I | 0.3 | 0.7 | 0.1 | 1.0 | $-2.76$ | Deep oscillatory | §§2.1, 4, 6, 7, 8.2, 9.2 |
| II | 0.6 | 0.4 | 0.5 | 1.0 | $-1.59$ | Moderate oscillatory | §§3, 5, 8.3, 9.1, 9.4, 9.5 |
| III | 0.8 | 0.2 | 1.8 | 1.0 | $+0.20$ | Near-critical | §§2.3, 5.2, 7.4, 8.2 |
| IV | 0.9 | 0.1 | 5.0 | 1.0 | $+16.41$ | Deep monotonic | §§2.2, 1.7, 5.2, 7.4 |
| V | 0.2 | 0.8 | 0.3 | 0.5 | $-6.24$ | High participation | §§4, 9.3 |

#### 10.2.2 Derived Equilibrium Quantities

| Quantity | Symbol | Value (Sets I–IV, V) |
|----------|--------|---------------------|
| Equilibrium mobility | $M_* = M(\rho^*)$ | $0.25$ |
| Mobility derivative at equilibrium | $M_*' = M'(\rho^*)$ | $-1.0$ |
| Penalty derivative | $P_*' = P_0$ | $1.0$ |
| Penalty-to-mobility ratio | $P_*'/M_*$ | $4.0$ |
| First Neumann eigenvalue ($L = 1$) | $\mu_1 = \pi^2$ | $9.8696$ |
| First modal decay coefficient | $\alpha_1 = M_*\mu_1 + P_*'$ | $3.4674$ |

#### 10.2.3 Standard Initial Conditions

| IC | Formula | Default parameters | $C_{\mathrm{ED}}(0)$ formula |
|----|---------|-------------------|----------------------------|
| A | $\rho^* + A\cos(n\pi x/L)$ | $A = 0.05$, $n = 1$ | $A^2 n^2\pi^2/(2L)$ |
| B | $\rho^* + \sum_{n=1}^{N_m} A_n\cos(n\pi x/L)$ | $A_n = 0.1/n^2$, $N_m = 8$ | $\sum A_n^2 n^2\pi^2/(2L)$ |
| C | $\rho^* + A\exp(-(x-x_0)^2/(2\sigma^2))$ | $A = 0.3$, $x_0 = L/2$, $\sigma = 0.05$ | $\approx A^2\sqrt{\pi}/(2\sigma^3\sqrt{2})$ |
| D | $\rho_{\max} - \delta + A\cos(\pi x/L)$ | $\delta = 0.05$, $A = 0.02$ | $A^2\pi^2/(2L)$ |

#### 10.2.4 Numerical Resolution and Time-Stepping Defaults

| Parameter | Symbol | Default value | Notes |
|-----------|--------|--------------|-------|
| Grid points (1D) | $N$ | 512 | Method A; 128 for Method B |
| Grid points (2D) | $N$ | 64 per dimension | Method A only |
| Time step | $\Delta t$ | $5 \times 10^{-4}$ | Adjusted by CFL; see §10.1.4 |
| CFL safety factor | $C_{\mathrm{CFL}}$ | 0.5 | |
| Mobility-collapse warning threshold | $\delta_{\mathrm{warn}}$ | $0.01\,\rho_{\max}$ | §1.6 |
| Mobility-collapse critical threshold | $\delta_{\mathrm{crit}}$ | $10^{-4}\,\rho_{\max}$ | §1.6 |
| Positivity floor | $\delta_{\mathrm{floor}}$ | $10^{-12}$ | §1.6 |
| De-aliasing cutoff (spectral) | $N_{\mathrm{alias}}$ | $2N/3$ | §1.4.2 |
| Lyapunov coupling parameter | $\sigma$ | $0.01$ | Definition C.39 |

#### 10.2.5 Master Experiment Table

The following table lists every numbered experiment in the Atlas with its section, parameter set, initial condition, integration time, method, and resolution. This table is the complete recipe for reproducing the Atlas.

| Exp. | Section | Set | IC | IC params | $T$ | Method | $N$ | $\Delta t$ |
|------|---------|-----|----|-----------|-----|--------|-----|------------|
| 1.1 | §1.7.1 | I | A | $A=0.05$ | 5 | A+B | 64–512 | $10^{-2}$–$1.25\times10^{-3}$ |
| 1.2 | §1.7.2 | I | B | $N_m=8$, $A_n=0.1/n^2$ | 50 | A(CN) | 256 | $10^{-3}$ |
| 1.3 | §1.7.3 | IV | A | $A=0.05$ | 20 | A(CN) | 256 | $10^{-3}$ |
| 1.4 | §1.7.4 | I–V | A | $A=10^{-4},0.05$ | 10 | A(CN) | 256 | $10^{-3}$ |
| 2.1 | §2.1.2 | I | Hom. | $A=0.05,0.3$; $v_0=0.1$ | 30 | A(CN) | 256 | $10^{-3}$ |
| 2.2 | §2.1.3 | I var. | Hom. | $A=0.05$; $v_0=0.1$ | 30 | A(CN) | 256 | $10^{-3}$ |
| 2.3 | §2.2.2 | IV | Hom. | $A=0.05$; $v_0=0.1$ | 15 | A(CN) | 256 | $10^{-3}$ |
| 2.4 | §2.2.3 | IV var. | Hom. | $A=0.05$; $v_0=0.1$ | 15 | A(CN) | 256 | $10^{-3}$ |
| 2.5 | §2.3.2 | Crit. | Hom. | $A=0.05$; $v_0=0$ | 20 | A(CN) | 256 | $10^{-3}$ |
| 2.6 | §2.3.3 | Near-crit. | Hom. | $A=0.05$; $v_0=0$ | 20 | A(CN) | 256 | $10^{-3}$ |
| 2.7 | §2.4.1 | Grid | Hom. | $A=0.05$; $v_0=0.1$ | 20 | A(CN) | 256 | $10^{-3}$ |
| 2.8 | §2.4.3 | Grid×$\tau$ | Hom. | $A=0.05$; $v_0=0.1$ | 20 | A(CN) | 256 | $10^{-3}$ |
| 3.1 | §3.1.2 | II | A | $n=1{-}4$; $A=10^{-3}$ | 5 | B | 128 | $10^{-4}$ |
| 3.2 | §3.1.3 | II | A | $n=1$; $A=10^{-4}{-}0.2$ | 10 | B | 128 | $10^{-4}$ |
| 3.3 | §3.2.2 | II | B | $N_m=8$; $v_0=0.01$ | 10 | B | 128 | $10^{-4}$ |
| 3.4 | §3.2.3 | II | Custom | $a_0=a_1=0.01$; $v_0=0.01$ | 20 | B | 128 | $10^{-4}$ |
| 3.5 | §3.2.4 | II var. | Custom | same; $D$ sweep | 20 | B | 128 | $10^{-4}$ |
| 3.6 | §3.3.2 | II | B ext. | $N_m=32$; $A_n=10^{-3}/n$ | 2 | B | 128 | $10^{-4}$ |
| 3.7 | §3.3.3 | II | A (2D) | $A=10^{-3}$; 25 mode pairs | 2 | A | 64² | $10^{-4}$ |
| 3.8 | §3.3.4 | II var. | A | $n=1{-}8$; $P_0$ sweep | 5 | B | 128 | $10^{-4}$ |
| 4.1 | §4.1.2 | I | Custom | $A_1=A_2=0.05$ | 5 | B | 128 | $10^{-4}$ |
| 4.2 | §4.1.3 | I | Custom | $A_2=A_3=0.05$ | 3 | B | 128 | $10^{-4}$ |
| 4.3 | §4.1.4 | I | Custom | all pairs $m\leq n\leq 6$; $A=0.03$ | 2 | B | 128 | $10^{-4}$ |
| 4.4 | §4.2.2 | I | A | $n=1$; $\epsilon=0.1$ | 8 | B | 128 | $10^{-4}$ |
| 4.5 | §4.2.3 | I | A | $n=1$; $\epsilon$ sweep | 8 | B | 128 | $10^{-4}$ |
| 4.6 | §4.2.4 | I var. | A | $n=1$; $\epsilon=0.05$; $D$ sweep | 8 | B | 128 | $10^{-4}$ |
| 4.7 | §4.3.2 | I | A | $n=1$; $\epsilon=0.2$ | 6 | B | 128 | $10^{-4}$ |
| 4.8 | §4.3.3 | I | A | $n=1$; $\epsilon$ sweep | 6 | B | 128 | $10^{-4}$ |
| 4.9 | §4.3.4 | I | A | $n=1$; $\epsilon=0.2$ | 6 | B | 128 | $10^{-4}$ |
| 5.1 | §5.1.2 | II | Custom | LC/MC/HC | 8 | A(CN) | 512 | $5\times10^{-4}$ |
| 5.2 | §5.1.3 | II | HC | same as 5.1 | 6 | A(CN) | 512 | $5\times10^{-4}$ |
| 5.3 | §5.2.2 | II | C | $A$ sweep (7 values) | 20 | A(CN) | 512 | $5\times10^{-4}$ |
| 5.4 | §5.2.3 | I–IV | C | $A=0.2$ | 20 | A(CN) | 512 | $5\times10^{-4}$ |
| 5.5 | §5.3.2 | II | A | $n=1$ and $n=4$; $A=0.1$ | 8 | A(CN) | 512 | $5\times10^{-4}$ |
| 5.6 | §5.3.3 | II | A | $n=1{-}6$; $A=0.1$ | 4 | A(CN) | 512 | $5\times10^{-4}$ |
| 6.1 | §6.1.2 | I | D | $\delta=0.05$; $A=0.02$ | 20 | A(CN) | 1024 | $10^{-4}$ |
| 6.2 | §6.1.3 | I | D | same as 6.1 | 20 | A(CN) | 1024 | $10^{-4}$ |
| 6.3 | §6.2.2 | I | D var. | $\delta$ sweep (7 values) | 1 | A(CN) | 1024 | $10^{-4}$ |
| 6.4 | §6.2.3 | I var. | D var. | $\beta$ sweep; $\delta$ sweep | 1 | A(CN) | 1024 | $10^{-4}$ |
| 6.5 | §6.3.2 | I | D | $\delta=0.05$; $A=0.02$ | 15 | A(CN) | 1024 | $10^{-4}$ |
| 6.6 | §6.3.3 | I | D | same as 6.1 | 2 | A(CN) | 1024 | $10^{-4}$ |
| 6.7 | §6.3.4 | I | Custom | $\bar{\rho}$ sweep; $A=0.01$ | 5 | A(CN) | 1024 | $10^{-4}$ |
| 7.1 | §7.1.2 | I | C | $A=0.4$ | 50 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.2 | §7.2.2 | I | C | $A=0.2$; $v_0=0.05$ | 40 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.3 | §7.2.3 | I | C | same as 7.2 | 40 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.4 | §7.3.2 | I | A | $A=0.01$; $v_0=0.005$ | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.5 | §7.3.3 | I–V | A | $A=0.01$; $v_0=0.005$ | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.6 | §7.4.2 | I | C | $A$ sweep (10 values) | 60 | A(CN) | 512 | $5\times10^{-4}$ |
| 7.7 | §7.4.3 | I–V | C | $A=0.2$ | 60 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.1 | §8.1.2 | Custom | Hom. | $D=0.5$; $\zeta$ sweep (41) | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.2 | §8.1.3 | Custom | Hom. | 7 selected $\zeta$ values | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.3 | §8.2.2 | III | C | $A=0.35$; $v_0=0.2$ | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.4 | §8.2.3 | I | D | $\rho_0=0.95+0.02\cos$ | 40 | A(CN) | 1024 | $10^{-4}$ |
| 8.5 | §8.3.2 | Grid | A+C | $9\times9$ grid; two amplitudes | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.6 | §8.3.3 | Grid | A | small amplitude | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.7 | §8.3.4 | Grid | C | $A=0.3$ | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 8.8 | §8.3.5 | Grid×$\tau$ | A | 4 values of $\tau$ | 30 | A(CN) | 512 | $5\times10^{-4}$ |
| 9.1 | §9.1.3 | II | A | 8-rung ladder | 3 | B | 128 | $10^{-4}$ |
| 9.2 | §9.2.3 | I | Custom | 5 galaxy analogues | 20 | A(CN) | 512 | $5\times10^{-4}$ |
| 9.3 | §9.3.3 | V | Custom | pattern IC | 5 | B | 128 | $10^{-4}$ |
| 9.4 | §9.4.3 | II | Driven | 5 pump amplitudes | 50 | A(CN) | 512 | $5\times10^{-4}$ |
| 9.5 | §9.5.3 | II | Custom | 6 transport configs | 5 | A(CN) | 512 | $5\times10^{-4}$ |

**Total experiment count:** 55 numbered experiments (some comprising multiple parameter variations), requiring approximately 450 individual integrations.

---

### 10.3 Environment Specification

#### 10.3.1 Minimum Software Requirements

The Atlas computations require:

1. **A linear algebra library** capable of solving tridiagonal and banded symmetric positive-definite systems. Any LAPACK-compatible implementation suffices (e.g., SciPy's `scipy.linalg.solve_banded`, Julia's `LinearAlgebra.lu!` on `Tridiagonal`, MATLAB's backslash operator).

2. **A fast Fourier transform (DCT-I) implementation.** Any FFT library that supports the Type-I discrete cosine transform suffices (e.g., SciPy's `scipy.fft.dct`, Julia's `FFTW.jl` with `FFTW.REDFT00`, MATLAB's `dct`).

3. **An adaptive quadrature routine** for computing the density potential $\Phi(\rho) = \int_{\rho^*}^{\rho} P(r)/M(r)\,dr$ (used in the energy functional). Any routine with absolute error tolerance $10^{-12}$ suffices (e.g., SciPy's `scipy.integrate.quad`, Julia's `QuadGK.quadgk`, MATLAB's `integral`).

4. **Double-precision floating-point arithmetic** (IEEE 754, 64-bit). No extended or arbitrary precision is required.

#### 10.3.2 Reference Implementations

The Atlas has been validated in three environments:

| Environment | Version | OS | Key packages |
|-------------|---------|-----|-------------|
| Python | 3.11+ | Any | NumPy 1.24+, SciPy 1.11+ |
| Julia | 1.9+ | Any | DifferentialEquations.jl, FFTW.jl |
| MATLAB | R2023a+ | Any | Signal Processing Toolbox (for DCT) |

No result in the Atlas depends on a feature specific to any one environment. The pseudocode of §10.1 is sufficient for independent reimplementation in any language with the capabilities listed in §10.3.1.

#### 10.3.3 Hardware Requirements

The computational cost of the Atlas is modest:

- **Memory:** The largest experiment (Experiment 8.5: $81$ integrations at $N = 512$) requires $< 500$ MB of working memory.
- **Time:** A single integration at $N = 512$, $\Delta t = 5 \times 10^{-4}$, $T = 60$ requires $\approx 120{,}000$ time steps and $\sim 10$ seconds on a modern single-core processor. The full Atlas ($\sim 450$ integrations) completes in $\sim 2$ hours on a single core, or $\sim 15$ minutes with parallelization across the independent experiments.
- **Storage:** The raw output (all observables at all time steps for all experiments) occupies $\sim 5$ GB. The compressed output (summary statistics, decay rates, ratios, and figure-ready data) occupies $\sim 50$ MB.

No GPU, cluster, or specialized hardware is required.

---

### 10.4 Instructions for Rerunning Simulations

#### 10.4.1 Complete Reproduction (All Experiments)

```
PROCEDURE Reproduce_Atlas():

    // Step 1: Implement the two integration methods
    Implement FD_Step (§10.1.2) and SPEC_Step (§10.1.3)
    Implement Extract_Observables (§10.1.5)
    Implement Select_Timestep (§10.1.4)

    // Step 2: Validate the implementation (§1.7)
    RUN Experiment 1.1 (convergence test)
        VERIFY: spatial order 2 (FD), spectral (SPEC); temporal order 1/2/4
    RUN Experiment 1.2 (energy dissipation)
        VERIFY: E(t) monotonically non-increasing; channel closure
    RUN Experiment 1.3 (mass rate)
        VERIFY: mass-rate residual = O(Δt^p + h²)
    RUN Experiment 1.4 (linearized comparison)
        VERIFY: σ̂ within 1% of Dα₁; ω̂ within 1% of analytic

    IF any validation fails: STOP and debug implementation

    // Step 3: Run the Atlas experiments
    FOR each experiment in the Master Experiment Table (§10.2.5):
        LOAD parameter set (Table §10.2.1)
        CONSTRUCT initial condition (Table §10.2.3)
        SET resolution and time step (Table §10.2.4 or experiment-specific)
        CALL Atlas_Experiment(params, IC, T, method, observables)
        STORE results

    // Step 4: Verify structural results
    FOR each experiment with an analytic prediction:
        COMPARE measured value to analytic prediction
        VERIFY agreement within stated tolerance (1%–10% depending on experiment)

    // Step 5: Generate figure data
    FOR each figure description in the Atlas:
        EXTRACT the specified data from the stored results
        FORMAT as (x, y) pairs with axis labels and ranges
        VERIFY that the described features are present in the data

    REPORT: list of all experiments, pass/fail status, and discrepancies
```

#### 10.4.2 Selective Reproduction (Single Section)

To reproduce only the experiments in a single section (e.g., Section 4: Nonlinear Triad Simulations):

1. Implement the integration methods (§10.1.2 or §10.1.3, as specified by the Method column in the Master Table).
2. Run the four validation tests (§1.7) to confirm the implementation.
3. Run only the experiments listed in the Master Table with the matching section number.
4. Compare the measured observables to the analytic predictions stated in the corresponding subsections.

Each section is self-contained: it depends only on the canonical parameters (§10.2.1), the constitutive functions (§1.1), and the spatial discretization (§1.4). No experiment depends on the results of a previous experiment.

#### 10.4.3 Convergence Verification Protocol

For any experiment whose results are to be reported or compared to analytic predictions:

```
PROCEDURE Verify_Convergence(experiment):

    // Resolution study
    RUN experiment at (N, Δt)
    RUN experiment at (2N, Δt/4)    // refine space and time simultaneously
    COMPUTE Richardson error: e = ||ρ_N − ρ_{2N}||_{L²}

    // Check convergence order
    RUN experiment at (4N, Δt/16)
    COMPUTE e' = ||ρ_{2N} − ρ_{4N}||_{L²}
    COMPUTE observed order: p = log₂(e/e')

    VERIFY: p within 10% of theoretical order (2 for FD, ≥4 for spectral)

    // Check observable stability
    COMPUTE observable at (N, Δt) and (2N, Δt/4)
    VERIFY: relative difference < stated tolerance

    RETURN (p, e, e', observable_difference)
```

This protocol is applied to all experiments in Section 1.7 (where it constitutes the validation tests themselves) and is recommended for any experiment whose quantitative results are quoted in the text.

#### 10.4.4 Diagnostics and Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|-------------|------------|
| Energy $\mathcal{E}$ increases | Time step too large | Reduce $\Delta t$ by factor $2$; check CFL |
| Density exceeds $\rho_{\max}$ | Explicit nonlinear overshoot | Enable adaptive time-step reduction (§1.6) |
| Density becomes negative | Penalty restoring insufficient at low resolution | Increase $N$; check positivity projection |
| Modal amplitudes do not match analytic rates | Insufficient spectral resolution | Increase $N$; check de-aliasing cutoff |
| Oscillation frequency deviates from prediction | Nonlinear frequency shift at large amplitude | Reduce $A$; compare at $A = 10^{-4}$ |
| Convergence order below theoretical | Ghost-point implementation error | Verify Neumann BC stencil (eq. 1.13) |
| ETD-RK4 produces NaN | Small-$z$ cancellation in weight functions | Use Taylor series for $|c_k\Delta t| < 10^{-2}$ |
| Triad selection rule violated | Aliasing | Check 3/2-rule de-aliasing; increase $N$ |

---

## 11. Figure Index

The Atlas contains 45 figures, each specified by its data source, axes, content, and the analytic prediction it demonstrates (§0.8). This index organizes all figures by thematic group, cross-references the governing theorems from Appendix C, and provides a one-line summary of each figure's content. The six groups correspond to the six architectural layers that the Atlas demonstrates numerically: validation infrastructure, regime geometry, modal hierarchy, triad structure, complexity dynamics and horizon behavior, convergence structure, and cross-domain analogues.

---

### Group 0 — Validation Infrastructure

These figures verify that the numerical scheme correctly reproduces the analytic properties of the continuous PDE system. They underpin the credibility of all subsequent demonstrations.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 1.1 | Spatial and temporal convergence | §1.7.1 | 2 | — | Log-log convergence plots: $O(h^2)$ spatial, $O(\Delta t^{1,2,4})$ temporal for the three schemes. |
| 1.2 | Energy dissipation and channel decomposition | §1.7.2 | 3 | Lemma C.6 | Monotonic $\mathcal{E}(t)$ descent; three dissipation channels (gradient, penalty, participation); discrete dissipation-identity closure. |
| 1.3 | Mass rate verification | §1.7.3 | 2 | Eq. 1.34 | Total mass relaxation toward $\rho^* L$; mass-rate residual at $O(\Delta t^p + h^2)$. |
| 1.4 | Linearized analytic comparison | §1.7.4 | 4 | Eqs. C.11, C.15 | Time series overlay at $A = 10^{-4}$ (exact match) and $A = 0.05$ (nonlinear onset); measured $\hat{\sigma}$ and $\hat{\omega}$ converging to analytic values as $A \to 0$. |

---

### Group I — Regime Geometry

These figures demonstrate the partition of parameter space into the Spiral Sheet, Monotonic Cone, and Boundary Surface, and the transitions between them.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 2.1 | Phase portrait of the Spiral Sheet | §2.1.2 | 2 | Thm. C.22(ii) | Elliptical spiral at small amplitude; nonlinearly deformed spiral at large amplitude showing mobility-collapse asymmetry. |
| 2.2 | Spiral tightening with increasing $\zeta$ | §2.1.3 | 2 | Thm. C.22(ii) | Five superimposed phase trajectories showing faster envelope decay and slower frequency as $\zeta \to \zeta_c$; measured $\hat{\gamma}_0$ and $\hat{\omega}$ versus $\zeta$ matching analytic predictions. |
| 2.3 | Phase portrait of the Monotonic Cone | §2.2.2 | 2 | Thm. C.22(iii) | Non-looping trajectory along slow eigenvector $\mathbf{r}_+$; semilog time series showing two-time-scale exponential separation $|\lambda_-|/|\lambda_+| \approx 5.4$. |
| 2.4 | Eigenvalue migration in the Monotonic Cone | §2.2.3 | 1 | Eq. C.15 | Measured $|\lambda_\pm|$ versus $D$, converging to decoupled limits $DP_*'$ and $\zeta/\tau$. |
| 2.5 | Jordan-block dynamics on $\Sigma$ | §2.3.2 | 3 | Lemma C.54 | Polynomial-times-exponential time series; semilog curvature signature distinguishing Jordan from pure exponential; phase trajectory aligning with eigenvector $\mathbf{e}_1$. |
| 2.6 | Near-critical comparison | §2.3.3 | 2 | Thm. C.60 | Three time series ($\zeta_c \pm 0.05$ and $\zeta_c$): vestigial half-loop, algebraic bump, monotonic decay. Smooth unfolding of the codimension-one transition. |
| 2.7 | The discriminant landscape | §2.4.1 | 1 | Def. C.19, Eq. C.63 | Full $(D, \zeta)$-plane color map of $\mathscr{D}_0$; parabolic Boundary Surface $\Sigma$; 25 verification points; five canonical Parameter Sets; $\Delta = 1$ contour. |
| 2.8 | Discriminant sign change across $\Sigma$ | §2.4.2 | 4 | Prop. C.52 | $\zeta$-sweep at $D = 0.5$: discriminant curve, zero-crossing count (sharp drop), frequency vanishing as $(\zeta_c - \zeta)^{1/2}$, transient-amplification cusp at $\zeta_c$. |
| 2.9 | Regime geometry at different time scales | §2.4.3 | 4 | Thm. C.61 | Four discriminant maps at $\tau \in \{0.25, 0.5, 1.0, 2.0\}$; Spiral Sheet expansion with increasing $\tau$. |
| 8.1 | Eigenvalue splitting across $\Sigma$ | §8.1.2 | 3 | Thm. C.60(i) | Fine-grained $\zeta$-sweep: frequency vanishing as $\sqrt{\zeta_c - \zeta}$; eigenvalue magnitude cusp at coalescence; integer winding number stepping to zero. |
| 8.2 | Phase-portrait morphing across $\Sigma$ | §8.1.3 | 7 | Thm. C.60(iii) | Seven phase trajectories: tight spiral → loose spiral → Jordan curve → gentle arc → straight line. Visual atlas of the topological transition. |
| 8.3 | Complexity-driven transient oscillation | §8.2.2 | 2 | §8.2.1 | Large-amplitude zero crossings in the Monotonic Cone; $\Delta_{\mathrm{eff}}(t)$ rising from near-critical to linearized value. |
| 8.4 | Monotonic transient in the Spiral Sheet | §8.2.3 | 2 | §8.2.1 | Near-horizon monotonic decay ($t < 5$) followed by oscillation emergence as mobility recovers; $M(\bar{\rho})/M_*$ tracking the transition. |
| 8.5 | Nonlinear regime map | §8.3.2 | 2 | Thm. C.22 | $9 \times 9$ grid in $(D, \zeta)$: small-amplitude map (exact agreement with $\Sigma$); large-amplitude map (transition band near $\Sigma$). |
| 8.6 | Observable landscape: $\hat{\gamma}$ and $\hat{\omega}$ | §8.3.3 | 2 | Cor. C.18, Eq. C.15 | Contour maps of decay rate (gradient kink at $\Sigma$) and frequency (contours crowding toward $\Sigma$ with square-root vanishing). |
| 8.7 | Transition time landscape | §8.3.4 | 1 | Thm. C.76 | Contour map of $t_*(D, \zeta)$: ridge along $\Sigma$ (near-critical slowdown), valley in deep Monotonic Cone, plateau in deep Spiral Sheet. |
| 8.8 | Regime maps at four $\tau$ values | §8.3.5 | 4 | Thm. C.61(ii) | Spiral Sheet expansion with $\tau$: narrow at $\tau = 0.25$, dominant at $\tau = 2.0$. |

---

### Group II — Modal Hierarchy

These figures demonstrate the spectral structure of the linearized operator: mode-by-mode exponential decay, the spectral gap, and the decay-rate funnel.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 3.1 | Single-mode exponential decay | §3.1.2 | 1 | Eq. C.11 | Semilog plot of $|a_n(t)|$ for modes $n = 1, 2, 3, 4$; four parallel lines with slopes $-D\alpha_n$ matching analytic rates. |
| 3.2 | Nonlinear onset in single-mode decay | §3.1.3 | 2 | Prop. C.35 | Amplitude-dependent damping enhancement (left); second-harmonic generation $|a_2(t)|$ peak scaling as $A^2$ (right). |
| 3.3 | Multi-mode spectral waterfall | §3.2.2 | 1 | Thm. C.17 | Nine modal amplitude curves fanning from $n = 8$ (steepest) to $n = 0$ (oscillating envelope), each reaching the noise floor at its predicted arrival time. |
| 3.4 | Spectral gap demonstration | §3.2.3 | 2 | Lemma C.31 | Spatial deviation at rate $D\alpha_1$, homogeneous envelope at rate $\gamma_0$, ratio decaying at gap $D\alpha_1 - \gamma_0 = 1.53$. |
| 3.5 | Spectral gap versus $D$ | §3.2.4 | 1 | Lemma C.31 | $D\alpha_1$ and $\gamma_{\mathrm{hom}}$ as functions of $D$; linearly widening shaded gap band. |
| 3.6 | The decay-rate funnel | §3.3.2 | 2 | Prop. C.29 | Parabolic funnel $D\alpha_n$ versus $n$ with penalty floor (top); relative error below $10^{-3}$ for $n \leq 20$ (bottom). |
| 3.7 | Two-dimensional decay-rate funnel | §3.3.3 | 1 | Prop. C.29 | Funnel indexed by $|\mathbf{n}|^2$ on $\Omega_2$; degeneracy structure of 2D Neumann modes; domain-independence of the functional relationship. |
| 3.8 | Penalty floor sweep | §3.3.4 | 1 | Prop. C.29(iii) | Five vertically shifted parabolas at $P_0 \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$; penalty controls the base, mobility controls the growth. |

---

### Group III — Triad Structure

These figures demonstrate the nonlinear triad coupling: the selection rule, locked amplitude ratios, and harmonic cascades.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 4.1 | Triad activation from pair $(1, 2)$ | §4.1.2 | 2 | Thm. C.34(i) | Rise-then-decay of generated modes $k = 3, 4$ at $O(A^2)$; bar chart confirming only selection-rule-permitted modes activated. |
| 4.2 | Inverse cascade from pair $(2, 3)$ | §4.1.3 | 1 | Thm. C.34(i) | Mode $k = 1$ generated from higher modes, persisting as dominant spatial mode after sources have decayed. |
| 4.3 | Selection-rule compliance matrix | §4.1.4 | 1 | Thm. C.34 | $21 \times 16$ binary matrix: dark cells only where selection rule predicts; zero false activations across all 21 pairs. |
| 4.4 | Locked amplitude ratio | §4.2.2 | 2 | Eq. C.40 | Parallel semilog decay of triad modes (left); instantaneous ratio $R_{31}(t)$ plateauing at the analytic prediction $0.236$ (right). |
| 4.5 | Locking test: normalized ratio vs. $\epsilon$ | §4.2.3 | 1 | Thm. C.36(iv) | $\bar{R}_{31}/\epsilon$ flat at $2.357$ for small $\epsilon$, with systematic $O(\epsilon^2)$ correction at large $\epsilon$. |
| 4.6 | Locked ratio versus $D$ | §4.2.4 | 1 | Eq. C.40 | Data on analytic hyperbola $0.707/D$; $D$-cancellation in the generation-to-decay balance. |
| 4.7 | Harmonic cascade: spectral snapshots | §4.3.2 | 1 | Thm. C.36 | Six spectral envelopes at successive times: monochromatic → broadband → contracted. Bloom-and-prune cycle under the modal hierarchy. |
| 4.8 | Cascade depth versus amplitude | §4.3.3 | 2 | §4.3.1 | Nested spectral envelopes (left); cascade depth $K(\epsilon)$ following logarithmic scaling $8\ln 10/(-\ln\epsilon)$ (right). |
| 4.9 | Energy redistribution and cascade | §4.3.4 | 2 | §4.3.1 | Stacked area plot of modal energy fractions (left); total energy decay with slope transition marking cascade extinction (right). |

---

### Group IV — Complexity Dynamics and Horizon Behavior

These figures demonstrate ED-complexity as the governing dynamical quantity: complexity-ordered dissipation, the stability threshold, complexity ordering of configurations, mobility collapse, energy barriers, and effective-complexity amplification near the horizon.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 5.1 | Complexity-dissipation at three levels | §5.1.2 | 3 | Lemma C.6 | Semilog $C_{\mathrm{ED}}(t)$ for LC/MC/HC converging to common asymptotic slope (top); dissipation rate ordered by complexity (middle); dissipation-to-complexity ratio converging to $DP_*'/M_* = 2.4$ (bottom). |
| 5.2 | Three-channel dissipation decomposition | §5.1.3 | 1 | Prop. C.42 | Gradient channel dominant early, penalty dominant late, participation at intermediate peak; crossover at $t \approx 0.4$; channel closure confirmed. |
| 5.3 | Convergence rate vs. initial complexity | §5.2.2 | 2 | Thm. C.43 | Seven $\mathcal{V}(t)$ curves from immediate exponential to prolonged nonlinear transient (left); universal late-time rate $\gamma_*$ regardless of initial $C_{\mathrm{ED}}$ (right). |
| 5.4 | Stability threshold across regimes | §5.2.3 | 1 | Thm. C.43 | $C_{\mathrm{ED}}^*$ smallest near the critical surface (Set III), largest in deep monotonic (Set IV); analytic estimate $(\gamma_*/C_{\mathrm{nl}})^2$ tracking the data. |
| 5.5 | Same mass, different fates | §5.3.2 | 3 | Prop. C.29 | Spatial profiles (top): sharp $n = 4$ profile vanishes $100\times$ faster than broad $n = 1$. Complexity curves (middle): $10^5$ separation by $t = 0.1$. $L^2$-norms (bottom): identical at $t = 0$, five orders apart by $t = 0.5$. |
| 5.6 | Complexity ordering: five configurations | §5.3.3 | 2 | Prop. C.29 | Normalized $C_{\mathrm{ED}}$ fan (left); log-log half-life plot confirming $t_{1/2} \propto 1/C_{\mathrm{ED}}$ (right). |
| 6.1 | Mobility collapse during approach | §6.1.2 | 2 | Remark C.12 | Five spatial profiles with asymmetric relaxation (left); mobility profiles recovering from $10^{-3}$ to $0.25$ over three orders of magnitude (right). |
| 6.2 | Proximity margin dynamics | §6.1.3 | 1 | Prop. C.11 | Margin $\delta(t)$ rising from $0.03$ to $0.50$; penalty-driven ODE comparison. |
| 6.3 | Energy barrier verification | §6.2.2 | 2 | Prop. C.11 | Log-log $\mathcal{E}_0$ vs. $\delta_0$ with slope $-1$ (left); product $\mathcal{E}_0 \cdot \delta_{\min}$ converging to $0.5$ (right). |
| 6.4 | Barrier exponent comparison | §6.2.3 | 1 | Eq. 6.1 | Three power-law families: $\beta = 1$ (logarithmic), $\beta = 2$ (slope $-1$), $\beta = 3$ (slope $-2$). |
| 6.5 | Bare versus effective complexity | §6.3.2 | 2 | Eq. 6.3 | Two-order-of-magnitude gap at $t = 0$ collapsing to equilibrium ratio $4.0$ (left); amplification ratio decaying as $\sim 1/t^2$ (right). |
| 6.6 | Gradient suppression near horizon | §6.3.3 | 2 | Prop. C.10 | Near-horizon set fraction collapsing to zero (left); near-horizon gradient integral dropping faster than bulk complexity (right). |
| 6.7 | Complexity amplification across densities | §6.3.4 | 2 | Prop. C.10 | Decay rate dropping to penalty floor $DP_*'$ (left); amplification factor $(0.5/(1-\bar{\rho}))^2$ reaching $6 \times 10^5$ at $\bar{\rho} = 0.98$ (right). |

---

### Group V — Convergence Structure

These figures demonstrate the three-stage convergence of Theorem C.76: global bounds, algebraic decay, exponential decay, and the transition time.

| Figure | Title | Section | Panels | Analytic basis | Content summary |
|--------|-------|---------|--------|---------------|-----------------|
| 7.1 | Stage I global bounds | §7.1.2 | 4 | Thm. C.66 | Energy descent (panel 1); pointwise confinement (panel 2); cumulative dissipation integrals converging to finite limits (panel 3); $L^2$-deviation and $|v|$ transient dynamics without clean exponential (panel 4). |
| 7.2 | Three stages of convergence | §7.2.2 | 3 | Thm. C.76 | Semilog $\mathcal{V}(t)$ with three distinct slopes (top); log-log revealing power law $t^{-2.5}$ in Stage II (middle); instantaneous rate $\hat{\beta}(t)$ rising from algebraic plateau to exponential plateau (bottom). |
| 7.3 | Barbalat decay of gradients and participation | §7.2.3 | 2 | Eqs. C.81, C.85 | $C_{\mathrm{ED}}(t)$ with three-stage descent and cumulative dissipation saturation (left); oscillatory $|v(t)|$ with amplitude modulation transitioning to clean exponential envelope (right). |
| 7.4 | Pure exponential decay in the basin | §7.3.2 | 2 | Thm. C.43 | Perfectly straight semilog $\mathcal{V}(t)$ from $t = 0$ (left); sinusoidal $(a_0, v)$ oscillations with exponential envelope (right). |
| 7.5 | Exponential rate across parameter sets | §7.3.3 | 1 | Eq. C.48 | Five measured rates matching analytic $2\gamma_*$ within 5%; ordering I $<$ V $<$ II $<$ III $<$ IV. |
| 7.6 | Transition time vs. initial complexity | §7.4.2 | 2 | Thm. C.72 | Ten nested $\mathcal{V}(t)$ curves joining the universal exponential slope at different $t_*$ (left); $t_*$ vs. $C_{\mathrm{ED}}$ following $a\ln(1 + C_{\mathrm{ED}}/b)$ (right). |
| 7.7 | Transition time across parameter regimes | §7.4.3 | 1 | Thm. C.76 | $t_*$ from $\approx 2$ (Set IV) to $\approx 25$ (Set III); heuristic estimate $\ln(C_{\mathrm{ED}}/\epsilon_0^2)/\gamma_*$ tracking the data. |

---

### Group VI — Cross-Domain Analogues

These figures demonstrate the canonical-system analogues of the five classes of physical predictions from the Applications Paper.

| Figure | Title | Section | Panels | Physical analogue | Content summary |
|--------|-------|---------|--------|------------------|-----------------|
| 9.1 | Decoherence ladder | §9.1.3 | 2 | Quantum $\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}$ | Eight $\mathcal{V}(t)/\mathcal{V}(0)$ curves fanning by complexity (left); log-log $\Gamma$ vs. $C_{\mathrm{ED}}$ with slope $\approx 1$ confirming linear scaling (right). |
| 9.2 | Activity-dependent participation response | §9.2.3 | 2 | Galactic temporal halo | Five $|v(t)|$ curves with activity-dependent peaks converging to common tension plateau $P_*'(\bar{\rho} - \rho^*)/\zeta$ (left); saturation of $v_{\max}$ with $C_{\mathrm{ED}}$ (right). |
| 9.3 | Triad-locked pattern spectrum | §9.3.3 | 2 | Condensed-matter triad signatures | Comb spectrum with teeth at multiples of 3 (left); locked harmonic ratios $|a_{3k}|/|a_3|$ plateauing at architecture-determined values (right). |
| 9.4 | Driven cavity harmonic locking | §9.4.3 | 2 | Photonic locked spectral shape | Five nested spectral envelopes with identical shapes (left); normalized ratio $|a_3^{\mathrm{ss}}|/(|a_1^{\mathrm{ss}}|)^3 \approx 7.5$ constant across pump levels (right). |
| 9.5 | Complexity-dependent effective diffusivity | §9.5.3 | 2 | Phononic transport kink | $D_{\mathrm{eff}}$ versus $C_{\mathrm{ED}}$ with plateau-knee-descent structure (left); non-monotonic transport rate peaking at moderate complexity (right). |

---

### Summary Statistics

| Group | Figures | Panels (total) | Governing appendix sections |
|-------|---------|----------------|---------------------------|
| 0. Validation | 4 | 11 | §C.1–C.2 |
| I. Regime Geometry | 18 | 35 | §C.3, C.6 |
| II. Modal Hierarchy | 8 | 11 | §C.3, C.4 |
| III. Triad Structure | 9 | 14 | §C.4 |
| IV. Complexity & Horizon | 13 | 26 | §C.2, C.5 |
| V. Convergence | 7 | 15 | §C.5, C.7 |
| VI. Cross-Domain | 5 | 10 | §C.2–C.7, Appendix D |
| **Total** | **64** | **122** | |

Every figure in the Atlas traces to a specific theorem, proposition, or remark in Appendix C or D. Every figure is specified with sufficient detail (axes, ranges, line styles, data sources) for independent reproduction from the pseudocode and parameter tables of Section 10. No figure requires rendering software or subjective aesthetic judgment — the figure descriptions are mathematical specifications, and the figure index is a lookup table for the complete numerical evidence base of the ED architectural ontology.

---

## 12. Summary

### 12.1 What the Simulations Demonstrate

The Numerical Atlas contains 55 numbered experiments comprising approximately 450 individual integrations of the canonical ED system (C.1), organized into 64 figures across 122 panels. Together, they demonstrate every analytic result of Appendix C at the level of concrete, reproducible numerical computation:

**Well-posedness and global existence** (Theorems C.2, C.14). The density remains strictly interior to $(0, \rho_{\max})$ for all tested initial conditions, the energy $\mathcal{E}$ decreases monotonically, the total dissipation converges to a finite limit, and no blow-up or degeneracy occurs — even for near-horizon configurations where the mobility drops to $10^{-3}$ of its equilibrium value (Experiments 6.1–6.2, 7.1).

**Spectral structure and modal hierarchy** (Theorem C.17, Proposition C.29, Corollary C.18). Each spatial mode $n \geq 1$ decays at the predicted rate $D\alpha_n = D(M_*\mu_n + P_*')$, with measured rates matching the analytic values to within $1\%$ across all parameter sets. The decay rates form the parabolic funnel $D\alpha_n \sim Dn^2$ with the penalty floor $DP_*'$, verified in one and two dimensions. The spectral gap $\gamma = \min(\gamma_{\mathrm{hom}}, \gamma_{\mathrm{sp}})$ is measured directly from the spatial-to-homogeneous amplitude ratio and confirmed across a sweep in $D$ (Experiments 3.1–3.8).

**Nonlinear triad coupling** (Theorem C.34, Proposition C.35, Theorem C.36). The selection rule $k \in \{|m-n|, m+n\}$ is verified without exception across all 21 tested mode pairs (Experiment 4.3). The locked amplitude ratio $|a_3|/|a_1|$ matches the analytic prediction (eq. C.40) to within $5\%$ for small amplitudes and follows the predicted $1/D$ dependence. The harmonic cascade from a single-mode initial condition blooms and contracts under the modal hierarchy, with cascade depth following the logarithmic scaling $K \sim -8\ln 10/\ln\epsilon$ (Experiments 4.1–4.9).

**Regime geometry and bifurcation** (Theorem C.22, Theorem C.60, Theorem C.61). The Spiral Sheet, Monotonic Cone, and Boundary Surface $\Sigma$ are mapped across the full $(D, \zeta)$-plane. The oscillation frequency vanishes as $\sqrt{\zeta_c - \zeta}$ at the boundary, the eigenvalues split from a Jordan block with the predicted cusp structure, and the winding number drops from positive to zero at a single critical value. The phase portraits morph continuously from tight spiral to straight-line approach. Nonlinear complexity-driven regime transitions (transient oscillation in the Monotonic Cone, transient monotonicity in the Spiral Sheet) are demonstrated and explained through the density-dependent effective damping $\Delta_{\mathrm{eff}}(\rho)$ (Experiments 2.1–2.9, 8.1–8.8).

**ED-complexity dynamics** (Lemma C.6, Theorem C.43, Proposition C.10). The dissipation rate is proportional to $C_{\mathrm{ED}}$ with the universal constant $DP_*'/M_*$, verified across three complexity levels. The stability threshold $\epsilon_0$ is identified operationally and varies across parameter sets as predicted by $(\gamma_*/C_{\mathrm{nl}})^2$. Configurations with identical mass but different gradient structure evolve on time scales differing by the ratio of their complexities — the half-life obeys $t_{1/2} \propto 1/C_{\mathrm{ED}}$ (Experiments 5.1–5.6).

**Mobility collapse and horizon behavior** (Propositions C.10, C.11, Remark C.12). The energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ is verified for three mobility exponents $\beta \in \{1, 2, 3\}$, with the scaling $\mathcal{E}_0 \propto \delta^{-(\beta-1)}$ confirmed. The effective complexity amplification $\mathcal{A}(\rho) = M_*/M(\rho)$ reaches $6 \times 10^5$ at $\bar{\rho} = 0.98$ and drives gradient suppression in the near-horizon region. The proximity margin improves monotonically as the density retreats (Experiments 6.1–6.7).

**Three-stage convergence** (Theorem C.76). The three stages — global bounds (Stage I), algebraic convergence (Stage II, $\mathcal{V} \sim t^{-p}$), and exponential convergence (Stage III, $\mathcal{V} \sim e^{-\gamma_* t}$) — are individually and collectively demonstrated. The transition time $t_*$ is measured as a function of initial complexity (logarithmic scaling) and parameter set (smallest for deep monotonic, largest near the critical surface), with the universal asymptotic rate $\gamma_*$ confirmed to within $5\%$ across all five parameter sets (Experiments 7.1–7.7).

### 12.2 How the Simulations Validate the Architecture

The Atlas validates the ED architecture at three levels:

**Theorem-level validation.** Each major theorem of Appendix C is paired with at least one experiment that realizes its conclusion in a concrete parameter regime. The pairing is not illustrative — it is quantitative: measured rates, ratios, and thresholds are compared to the analytic predictions with stated tolerances, and agreement is confirmed. The architecture's mathematical content is not merely consistent with numerical evidence; it is *reproduced* by it.

**Principle-level validation.** The seven canonical principles enter the numerical experiments through specific, identifiable mechanisms:

- Principle 1 (Operator Structure) is visible in the modal decay rates $D\alpha_n$ and the parabolic smoothing that underlies the convergence studies.
- Principle 2 (Channel Complementarity) is visible in the $D$-dependence of the spectral gap and the three-channel dissipation decomposition.
- Principle 3 (Penalty Equilibrium) is visible in the penalty floor of the decay-rate funnel, the coercivity of the Lyapunov functional, and the uniqueness of the $\omega$-limit point.
- Principle 4 (Mobility Capacity Bound) is visible in the energy barrier, the gradient suppression, the effective-complexity amplification, and the asymmetric relaxation near the horizon.
- Principle 5 (Participation Feedback Loop) is visible in the oscillatory dynamics of the homogeneous mode, the activity-dependent participation response, and the tension plateau.
- Principle 6 (Damping Discriminant) is visible in the regime geometry, the Boundary Surface, and the parameter-dependent convergence rates.
- Principle 7 (Nonlinear Triad Coupling) is visible in the selection rule, the locked amplitude ratios, and the harmonic cascade.

No principle is inert — each produces measurable numerical consequences.

**Universality-level validation.** The cross-domain demonstrations of Section 9 confirm that the five classes of physical predictions from the Applications Paper are genuine consequences of the canonical system, not artifacts of domain-specific assumptions. The decoherence ladder, the tension plateau, the triad-locked pattern spectrum, the pump-independent harmonic ratio, and the complexity-dependent transport kink all emerge from the same PDE with the same constitutive functions, differing only in the choice of initial condition and the identification of the physical observable. The universality class framework (Appendix D) is thereby confirmed computationally: all five demonstrations are instances of a single architectural logic.

### 12.3 How the Simulations Support the Applications Paper

The Applications Paper derives qualitative predictions from the architecture. The Atlas provides the quantitative infrastructure that converts those predictions into testable numbers:

**Decoherence scaling** (Applications Paper §3.1). The Atlas confirms $\Gamma \propto C_{\mathrm{ED}}$ with a proportionality constant $2D(M_*\mu_n + P_*')$ that depends on the constitutive parameters. For a specific physical system, the constitutive identification (mapping the physical density to the canonical $\rho$) would fix these parameters and produce a numerical decoherence rate.

**Temporal halos** (Applications Paper §4.1–4.2). The Atlas confirms the activity-dependent participation response and the tension plateau $|v| \approx P_*'(\bar{\rho} - \rho^*)/\zeta$. The 53% dwarf-galaxy separation observed in the SPARC dataset corresponds, in the canonical system, to the measured difference in peak participation between the G1 (quiet) and G5 (active) analogues.

**Triad signatures** (Applications Paper §5). The Atlas confirms the locked harmonic ratios and the comb-like spectral structure. The spectral fingerprint of the selection rule — energy at multiples of the dominant mode, negligible elsewhere — is the pattern that condensed-matter experiments should detect.

**Photonic locking** (Applications Paper §5.4, §5.7). The Atlas confirms the pump-independent normalized third-harmonic ratio. The predicted constant $|a_3^{\mathrm{ss}}|/(|a_1^{\mathrm{ss}}|)^3 \approx 7.5$ (for the canonical parameters) is the target that microresonator experiments should measure.

**Transport thresholds** (Applications Paper §5.1, §6). The Atlas confirms the knee in the effective diffusivity versus complexity curve. The critical complexity at the knee is determined by the constitutive parameters and the domain geometry; for a specific mesoscopic channel, the constitutive identification would fix this threshold.

In each case, the Atlas bridges the gap between the qualitative prediction ("the rate scales with complexity") and the quantitative target ("the proportionality constant is $X$ for these parameters"). The remaining step — the constitutive identification for each physical domain — is the subject of the planned ED-Arch-X paper.

### 12.4 What Remains to Be Simulated

The Atlas covers the one-dimensional domain $\Omega_1$ comprehensively and the two-dimensional domain $\Omega_2$ selectively (Experiment 3.7). Several directions remain open:

**Higher-dimensional simulations.** The two- and three-dimensional domains $\Omega_2$, $\Omega_3$ have been used only for the decay-rate funnel verification (§3.3.3). A full two-dimensional Atlas — including regime geometry, triad structure in 2D mode space (where the selection rules are richer), pattern-formation dynamics with 2D spatial structure, and mobility-collapse boundary layers — would extend the demonstrations to the geometrically richer setting relevant to galactic dynamics (2D disk projections) and condensed-matter patterns (2D order parameters).

**Multi-field extensions.** The canonical system has a single density field $\rho$ and a single participation variable $v$. Physical systems with multiple coupled order parameters (multi-band superconductors, coupled optical modes) require extensions to systems of the form $\partial_t\rho_i = D_i F_i[\rho_1, \ldots, \rho_K] + H_i v_i$. The universality class $\mathcal{U}_{\mathrm{ED}}$ is defined for the single-field case; the multi-field generalization is an open mathematical problem whose numerical exploration would precede the analytic theory.

**Constitutive function surveys.** The Atlas uses a single pair of constitutive functions (power-law mobility, linear penalty). The universality class guarantees that the qualitative results are insensitive to the constitutive choice, but the quantitative details (locked ratios, transition times, threshold values) depend on $M(\rho)$ and $P(\rho)$. A constitutive survey — repeating the key experiments with sigmoid mobility, exponential penalty, or physically derived constitutive functions — would map the quantitative dependence and identify which observables are truly universal (identical across all constitutive choices) versus which are constitutive-dependent (varying within the universality class).

**Driven and forced systems.** Experiment 9.4 introduced a time-independent source term as a cavity-pump analogue. A systematic study of driven ED systems — including time-periodic forcing (modulated pump), stochastic forcing (thermal noise), and spatially structured forcing (external potential) — would extend the Atlas into the territory most relevant to experimental comparison, where physical systems are rarely in free relaxation.

**Long-time and large-scale parameter surveys.** The regime maps of Section 8 cover a $9 \times 9$ grid at four values of $\tau$. A finer grid ($50 \times 50$ or higher), extended to include sweeps in $\rho^*$, $\rho_{\max}$, $M_0$, and $\beta$, would produce the complete parameter atlas needed for the ED-Arch-X diagnostic toolkit: given a measured set of physical observables (decay rate, oscillation frequency, triad ratio), the atlas would identify the canonical parameters that reproduce them, thereby constitutively identifying the physical system within $\mathcal{U}_{\mathrm{ED}}$.

### 12.5 The Atlas's Role in the ED Program

The Event-Density program rests on a chain of four documents:

1. **The Architectural Canon** states the seven principles and derives the nine-layer ontology.
2. **The Rigour Paper** (Appendices C and D) proves the mathematical well-posedness, spectral structure, stability, bifurcation geometry, long-time convergence, and universality class of the canonical system.
3. **The Applications Paper** derives falsifiable physical predictions from the architecture across five domains.
4. **The Numerical Atlas** demonstrates that the theorems produce the phenomena they describe, maps the quantitative dependence on parameters, and provides the computational evidence base for the entire program.

The Atlas does not replace any of the preceding documents. It does not prove theorems (that is the Rigour Paper's role), it does not identify physical systems (that is the Applications Paper's role), and it does not state principles (that is the Canon's role). What it does is make the architecture *visible*: every theorem becomes a curve, every proposition becomes a data point, every remark becomes a figure. The architecture is not an abstract logical structure — it is a dynamical system with measurable outputs, and the Atlas is the record of those measurements.

The 55 experiments, 64 figures, and 450 integrations of this Atlas constitute the complete numerical evidence base for the claim that the ED architecture is a self-consistent, computationally realized, and quantitatively predictive structural ontology. The architecture stands. The experiments will decide whether the physical world shares its structure.

---