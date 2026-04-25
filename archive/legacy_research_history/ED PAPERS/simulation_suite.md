# Simulation Suite for the Event-Density Canon

**Computational Infrastructure for Reproducing the Numerical Atlas**

Allen Proxmire
March 2026

---

## 0. Overview

### 0.1 Purpose

The Simulation Suite is the implementation companion to the Numerical Atlas. Where the Atlas specifies *what* is computed — the 55 experiments, 64 figures, and 450 integrations that constitute the numerical evidence base of the ED architectural ontology — the Suite specifies *how* to compute it: the algorithms, data structures, workflow organization, testing protocols, and environment configurations required to reproduce every result independently.

The Suite has three purposes:

1. **Executable reproducibility.** The Numerical Atlas (Section 10) provides pseudocode for all simulations, parameter tables for all experiments, and convergence verification protocols. The Suite translates this pseudocode into implementation-ready specifications: module decompositions, interface contracts, data-flow diagrams, and testing harnesses. An implementor reading the Suite should be able to produce a working solver in their environment of choice — Python, Julia, or MATLAB — without consulting any additional source.

2. **Validation infrastructure.** The four validation tests of the Atlas (§1.7: convergence, energy dissipation, mass conservation, linearized comparison) are the gate through which every implementation must pass before its results are trusted. The Suite specifies these tests as formal acceptance criteria: inputs, expected outputs, tolerances, and pass/fail conditions. An implementation that passes all four tests is certified to reproduce the Atlas; one that fails any test is not.

3. **Extension framework.** The Atlas covers the canonical ED system with a single pair of constitutive functions on one- and two-dimensional domains. The Suite is designed to accommodate the extensions identified in Atlas §12.4: multi-field systems, alternative constitutive functions, driven and forced systems, and higher-dimensional domains. The module interfaces are defined at the level of the canonical system (C.1) but parameterized to accept arbitrary $M(\rho)$, $P(\rho)$, source terms $S(x, t)$, and domain dimensions.

The Suite does not contain executable code. It contains the complete mathematical and algorithmic specification from which executable code is produced. The distinction is deliberate: code is language-specific, version-dependent, and entangled with platform details; the Suite is language-independent, version-stable, and concerned only with the mathematical content.

### 0.2 Relationship to the Numerical Atlas and Appendix E

The three documents form a hierarchy of increasing specificity:

**Appendix E** (Numerical Methods, Rigour Paper) provides the top-level method specification: discretization schemes (finite-difference stencil, spectral method, semi-implicit time stepping), stability conditions (CFL constraints, nonlinear stability), parameter tables, the horizon detection algorithm, and the spectral analysis pipeline. Appendix E is written at the level of a journal methods section — sufficient for an expert in numerical PDE to reproduce the computations, but not sufficient for a non-specialist or for automated verification.

**The Numerical Atlas** (Sections 0–12) provides the experiment-level specification: the canonical PDE (§1.1), the spatial discretizations (§1.4), the time-stepping schemes (§1.5), the mobility-collapse handling (§1.6), the validation tests (§1.7), and the master pseudocode (§10.1). The Atlas specifies *what* each experiment computes, *what* observables are extracted, and *what* the expected results are. It provides pseudocode for both integration methods (Method A: finite-difference; Method B: spectral) and for the observable extraction pipeline.

**The Simulation Suite** (this document) provides the implementation-level specification: module architecture, interface contracts between components, data formats, testing harnesses, workflow orchestration, and environment-specific guidance. The Suite takes the Atlas pseudocode as given and specifies how to organize it into a maintainable, testable, extensible computational infrastructure.

The relationship is:

$$
\text{Appendix E} \xrightarrow{\text{method specification}} \text{Numerical Atlas} \xrightarrow{\text{experiment specification}} \text{Simulation Suite} \xrightarrow{\text{implementation specification}} \text{Executable code}.
$$

Each level adds detail without contradicting the level above. A result produced by an implementation following the Suite is, by construction, a result specified by the Atlas, which is, by construction, consistent with the methods of Appendix E.

### 0.3 Reproducibility Philosophy

The reproducibility standard of the Suite inherits and extends the five principles stated in Atlas §0.4:

**1. Complete specification.** Every algorithm is defined by its mathematical content — inputs, outputs, and the transformation between them — not by its implementation syntax. The specification is sufficient to produce a correct implementation in any language with the capabilities listed in §0.5. No parameter is implicit, no default is hidden, and no behavior is undefined.

**2. Convergence verification.** Every implementation must pass the four validation tests of Atlas §1.7 before any experiment results are reported. The Suite specifies these tests as automated acceptance criteria with machine-checkable pass/fail conditions. An implementation that produces results without passing the validation suite is not considered a reproduction of the Atlas.

**3. Implementation independence.** The Suite is designed so that implementations in Python, Julia, and MATLAB (or any other environment meeting the requirements of §0.5) produce identical results to within the convergence tolerances. "Identical" means: the same structural features (monotonic energy decay, correct regime classification, selection-rule compliance) and the same quantitative values (decay rates, frequencies, ratios) to within the stated tolerances. Bit-level reproducibility across environments is not required and not expected, because floating-point rounding depends on the platform.

**4. Separation of concerns.** The Suite separates the computational infrastructure into five independent modules: constitutive functions, spatial discretization, time stepping, observable extraction, and experiment orchestration. Each module has a defined interface, can be tested independently, and can be replaced without affecting the others. This separation ensures that a bug in one module does not silently corrupt the results of another, and that extensions (new constitutive functions, new domains, new observables) can be added without modifying existing code.

**5. Traceability.** Every output of the Suite is tagged with the experiment number (from the Atlas Master Experiment Table, §10.2.5), the parameter set, the initial condition, the resolution, and the method. Every figure-ready data file includes the Atlas figure number it corresponds to. The chain from raw output to published figure to analytic theorem is fully traceable.

A sixth principle, specific to the Suite, is added:

**6. Defensive computation.** The Suite specifies runtime checks at every stage where the ED system's structural properties could be violated by numerical error: positivity of the density ($\rho > 0$), sub-capacity bound ($\rho < \rho_{\max}$), monotonicity of the energy ($\mathcal{E}^{n+1} \leq \mathcal{E}^n + \text{tolerance}$), and finiteness of all computed quantities. A violation of any structural check halts the computation and reports the violation, rather than producing silently incorrect results. These checks are not optional optimizations; they are part of the specification.

### 0.4 Supported Environments

The Suite targets three computational environments, chosen for accessibility, ecosystem maturity, and complementary strengths:

**Python (NumPy/SciPy).** The primary reference environment. Python is chosen for its accessibility (the largest scientific-computing user base), its comprehensive numerical libraries (NumPy for array operations, SciPy for sparse linear algebra, FFT, and quadrature), and its ecosystem for data analysis and visualization. The finite-difference solver (Method A) uses SciPy's sparse tridiagonal/banded solvers. The spectral solver (Method B) uses SciPy's DCT-I implementation. The observable extraction uses NumPy's array operations.

**Julia (DifferentialEquations.jl, FFTW.jl).** The performance-critical environment. Julia is chosen for its compilation model (near-C performance without manual optimization), its native support for differential-equation solvers (DifferentialEquations.jl provides the ETD-RK4 scheme with adaptive time stepping), and its FFT infrastructure (FFTW.jl wraps the FFTW library for high-performance DCT). The Julia implementation is recommended for the large parameter sweeps (Experiments 8.5–8.8: $81$–$324$ integrations) and the long-time integrations (Experiments 7.1, 7.6: $T = 50$–$60$).

**MATLAB.** The verification environment. MATLAB is chosen for its ubiquity in engineering and physics departments, its built-in tridiagonal solver (the backslash operator), and its Signal Processing Toolbox (for DCT). The MATLAB implementation serves as an independent cross-check: if the Python and Julia implementations agree but the MATLAB implementation disagrees, the discrepancy is investigated; if all three agree, the result is considered validated.

No result in the Atlas or Suite depends on a feature specific to any one environment. The mathematical specification of each algorithm (Atlas §10.1) is the authoritative reference; the environment-specific guidance in the Suite is a convenience, not a constraint.

### 0.5 Minimum Capabilities

Any environment used to implement the Suite must provide:

| Capability | Purpose | Example implementations |
|-----------|---------|------------------------|
| Tridiagonal linear solver | Implicit time stepping (Method A) | Thomas algorithm; LAPACK `dgtsv` |
| Banded symmetric positive-definite solver | 2D implicit time stepping | LAPACK `dpbsv`; SciPy `solve_banded` |
| Type-I discrete cosine transform (DCT-I) | Spectral method (Method B) | FFTW `REDFT00`; SciPy `scipy.fft.dct` |
| Adaptive numerical quadrature | Density potential $\Phi(\rho)$ | Gauss–Kronrod; SciPy `quad` |
| Double-precision floating-point (IEEE 754) | All computations | Native in all target environments |
| Array/matrix operations | Pointwise constitutive evaluation | NumPy; Julia arrays; MATLAB matrices |

No GPU, parallel computing, or specialized hardware capability is required. The full Atlas ($\sim 450$ integrations) completes in $\sim 2$ hours on a single modern CPU core.

### 0.6 The Suite's Role in Validating the ED Architecture

The ED architecture claims that seven irreducible principles generate a complete structural ontology for a class of dynamical systems, and that this ontology produces falsifiable physical predictions across five domains. The validation chain for this claim is:

1. **Analytic validation** (Appendix C): the principles are shown to imply the ontology through rigorous proof.
2. **Numerical validation** (Numerical Atlas): the theorems are shown to produce the predicted phenomena through direct computation.
3. **Computational validation** (Simulation Suite): the computations are shown to be reproducible, convergent, and implementation-independent through formal verification.

The Suite occupies the third level. Its role is not to discover new results or to extend the architecture — those are the roles of the Atlas and the Applications Paper. Its role is to ensure that the numerical evidence base is *trustworthy*: that the 64 figures of the Atlas are not artifacts of a particular implementation, a particular compiler, or a particular set of floating-point rounding choices, but are genuine structural features of the canonical ED system that any correct implementation will reproduce.

The Suite's validation is complete when:

- At least two independent implementations (in different environments) pass all four validation tests of Atlas §1.7.
- The quantitative outputs of the two implementations agree to within the convergence tolerances stated in the Atlas (typically $1\%$–$5\%$ for decay rates, frequencies, and amplitude ratios).
- Every figure in the Atlas Figure Index (§11) is reproducible from the stored output of both implementations.

When these conditions are met, the numerical evidence base of the ED architecture is certified as reproducible, and the physical predictions of the Applications Paper rest on a foundation that is not only analytically rigorous (Appendix C) but computationally verified (Atlas + Suite).

---

## 1. Canonical System Specification

### 1.1 Canonical PDE Restatement

This subsection restates the canonical ED system in the form used by the simulation engine, defines all parameters and constitutive functions, identifies the constraints imposed by Principles 1–7, and specifies how the PDE is represented internally as a computable data structure. The notation is identical to Atlas §1.1 and Appendix C (§C.1.1–C.1.2); no new symbols are introduced.

---

#### 1.1.1 The Coupled PDE–ODE System

The canonical ED system is the coupled evolution equation

$$
\begin{cases}
\partial_t \rho = D\,F[\rho] + H\,v, \\[4pt]
\dot{v} = \dfrac{1}{\tau}\bigl(F[\rho] - \zeta\,v\bigr),
\end{cases}
$$

on a bounded spatial domain $\Omega \subset \mathbb{R}^d$ with Neumann boundary conditions $\partial_\nu\rho = 0$ on $\partial\Omega$. The density field $\rho(x, t) \in (0, \rho_{\max})$ is defined on $\overline{\Omega} \times [0, T]$ and the participation variable $v(t) \in \mathbb{R}$ is a scalar function of time alone.

The system has two components:

- **The density equation** (first line) is a quasilinear parabolic PDE. The density evolves under two channels: the direct channel $D\,F[\rho]$, which applies the nonlinear density operator $F$ directly to $\rho$, and the mediated channel $H\,v$, which injects the participation variable as a spatially uniform source.

- **The participation equation** (second line) is an ordinary differential equation. The participation variable integrates the spatially averaged operator output $F[\rho]$ with time constant $\tau$ and is damped at rate $\zeta/\tau$.

The coupling is bidirectional: the density feeds $F[\rho]$ into the participation equation, and the participation feeds $v$ into the density equation. This bidirectional coupling is the mathematical content of Principle 5 (Participation Feedback Loop).

---

#### 1.1.2 The Nonlinear Density Operator

The operator $F[\rho]$ is

$$
F[\rho] := M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho),
$$

where $M$ is the mobility function, $P$ is the penalty function, and the prime denotes differentiation with respect to $\rho$. The operator has three terms:

1. **Nonlinear diffusion**: $M(\rho)\,\nabla^2\rho$. A second-order elliptic operator with density-dependent coefficient. This is the spatial transport mechanism of Principle 1 (Operator Structure). Its strength is controlled by the mobility $M(\rho)$, which varies with the local density.

2. **Gradient-squared nonlinearity**: $M'(\rho)\,|\nabla\rho|^2$. A first-order nonlinear term, quadratic in the spatial gradient. This term is the source of all inter-modal energy transfer and is the mathematical content of Principle 7 (Nonlinear Triad Coupling). It vanishes identically at spatial equilibrium ($\nabla\rho = 0$) and at the linearized level (where it is second-order in the perturbation).

3. **Penalty restoring force**: $-P(\rho)$. A zero-order term that drives the density toward the equilibrium $\rho^*$ (where $P(\rho^*) = 0$). This is the mathematical content of Principle 3 (Penalty Equilibrium).

The operator $F[\rho]$ is evaluated pointwise in $x$ at each time step. Its computation requires the values of $\rho$, $\nabla\rho$, and $\nabla^2\rho$ at each spatial point, together with the constitutive functions $M(\rho)$, $M'(\rho)$, and $P(\rho)$.

---

#### 1.1.3 Canonical Parameters

The system is governed by six independent canonical parameters:

| Parameter | Symbol | Type | Range | Structural role |
|-----------|--------|------|-------|----------------|
| Direct-channel weight | $D$ | Scalar | $(0, 1)$ | Fraction of $F[\rho]$ applied directly to density |
| Mediated-channel weight | $H$ | Derived | $H = 1 - D$ | Fraction of participation fed back into density |
| Participation damping | $\zeta$ | Scalar | $(0, \infty)$ | Exponential decay rate of $v$ in the absence of driving |
| Participation time scale | $\tau$ | Scalar | $(0, \infty)$ | Integration time of the participation variable |
| Penalty equilibrium | $\rho^*$ | Scalar | $(0, \rho_{\max})$ | Unique zero of $P(\rho)$; the target density |
| Capacity bound | $\rho_{\max}$ | Scalar | $(\rho^*, \infty)$ | Maximum attainable density; mobility zero |

The parameter $H$ is not independent — it is determined by $D$ through the channel complementarity constraint $D + H = 1$ (Principle 2). The simulation engine stores $D$ as the independent parameter and computes $H = 1 - D$ at initialization. This ensures that the constraint is satisfied identically, not approximately.

**Derived parameters.** Several compound quantities appear frequently in the analysis and are precomputed at initialization:

| Derived quantity | Formula | Meaning |
|-----------------|---------|---------|
| $\Delta$ | $D + 2\zeta$ | Canonical damping parameter (Principle 6) |
| $M_*$ | $M(\rho^*)$ | Equilibrium mobility |
| $M_*'$ | $M'(\rho^*)$ | Mobility derivative at equilibrium |
| $P_*'$ | $P'(\rho^*)$ | Penalty derivative at equilibrium |
| $\alpha_n$ | $M_*\mu_n + P_*'$ | Modal decay coefficient for mode $n$ |
| $\gamma_0$ | $\frac{1}{2}(DP_*' + \zeta/\tau)$ | Homogeneous-mode decay rate |
| $\mathscr{D}_0$ | $(DP_*' - \zeta/\tau)^2 - 4HP_*'/\tau$ | Modal discriminant |
| $\omega$ | $\frac{1}{2}\sqrt{|\mathscr{D}_0|}$ (if $\mathscr{D}_0 < 0$) | Oscillation frequency |

These derived quantities are computed once from the canonical parameters and the constitutive functions and are stored alongside the primary parameters. They are never recomputed during the time-stepping loop.

---

#### 1.1.4 Constitutive Functions

The constitutive functions $M(\rho)$ and $P(\rho)$ encode the material-specific content of the ED system. The canonical principles constrain their qualitative properties but not their specific functional forms.

**Mobility $M(\rho)$.** The mobility is a smooth function on $[0, \rho_{\max}]$ satisfying:

- $M(\rho) > 0$ for $\rho \in [0, \rho_{\max})$ (Principle 1: the operator is non-degenerate in the interior).
- $M(\rho_{\max}) = 0$ (Principle 4: Mobility Capacity Bound).
- $M \in C^\infty([0, \rho_{\max}])$ (regularity assumption of §C.1.1).

The default choice is the power-law mobility:

$$
M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta, \qquad M_0 > 0, \quad \beta > 0.
$$

Its derivative is $M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta - 1}$.

The simulation engine represents $M$ as a callable function object with three evaluation modes:

- `M.value(ρ)` → $M(\rho)$
- `M.deriv(ρ)` → $M'(\rho)$
- `M.params()` → $(M_0, \beta, \rho_{\max})$

The separation of the constitutive function from the PDE solver is a design requirement (§0.3, Principle 4: separation of concerns). The solver never assumes the functional form of $M$; it calls the evaluation interface. This allows the constitutive function to be replaced (e.g., by a sigmoid mobility, a tabulated function, or a physically derived constitutive law) without modifying the solver.

**Penalty $P(\rho)$.** The penalty is a smooth function on $\mathbb{R}$ satisfying:

- $P(\rho^*) = 0$ (Principle 3: the equilibrium is a penalty zero).
- $P'(\rho) > 0$ for all $\rho$ (Principle 3: strict monotonicity).
- $P \in C^\infty(\mathbb{R})$ (regularity assumption of §C.1.1).

The default choice is the linear penalty:

$$
P(\rho) = P_0\,(\rho - \rho^*), \qquad P_0 > 0.
$$

Its derivative is $P'(\rho) = P_0$ (constant).

The simulation engine represents $P$ with the same callable interface:

- `P.value(ρ)` → $P(\rho)$
- `P.deriv(ρ)` → $P'(\rho)$
- `P.params()` → $(P_0, \rho^*)$

**Constitutive validation.** At initialization, the simulation engine verifies the constitutive constraints:

| Check | Condition | Failure mode |
|-------|-----------|-------------|
| Mobility positivity | $M(\rho^*) > 0$ | Fatal: equilibrium is degenerate |
| Mobility collapse | $M(\rho_{\max}) = 0$ (to within $10^{-14}$) | Fatal: Principle 4 violated |
| Penalty zero | $|P(\rho^*)| < 10^{-14}$ | Fatal: Principle 3 violated |
| Penalty monotonicity | $P'(\rho^*) > 0$ | Fatal: Principle 3 violated |
| Penalty monotonicity (sampled) | $P'(\rho) > 0$ at 100 uniformly spaced points in $[0, \rho_{\max}]$ | Warning: monotonicity may be violated away from $\rho^*$ |
| Smoothness | $M$, $M'$, $P$, $P'$ all finite at $\rho = \rho^*$ | Fatal: regularity violated |

A fatal check failure halts initialization with a diagnostic message. A warning allows the computation to proceed but logs the potential issue.

---

#### 1.1.5 Constraints from Principles 1–7

The seven canonical principles impose the following constraints on the system, each of which is enforced at a specific level of the simulation engine:

**Principle 1 (Operator Structure).** The operator $F[\rho]$ has the form $M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$. This is enforced by the operator evaluation module, which computes exactly these three terms and no others. The module does not accept additional terms (e.g., reaction terms, advection, higher-order diffusion) unless the system is explicitly extended (§0.1, extension framework).

**Principle 2 (Channel Complementarity).** The constraint $D + H = 1$ is enforced at initialization by computing $H = 1 - D$. The engine does not accept $D$ and $H$ as independent inputs. Any attempt to set $H \neq 1 - D$ is rejected with a diagnostic message.

**Principle 3 (Penalty Equilibrium).** The conditions $P(\rho^*) = 0$ and $P'(\rho^*) > 0$ are verified at initialization (§1.1.4, constitutive validation). The uniqueness of the equilibrium — that $\rho^*$ is the only zero of $P$ — is guaranteed by the strict monotonicity $P' > 0$ (which implies $P$ is injective, hence has at most one zero).

**Principle 4 (Mobility Capacity Bound).** The condition $M(\rho_{\max}) = 0$ is verified at initialization. At runtime, the mobility-collapse handling protocol (Atlas §1.6) monitors the proximity margin $\delta(t) = \rho_{\max} - \max_x\rho(x, t)$ and activates adaptive time-step reduction and positivity projection as needed. The energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ (Proposition C.11) is not explicitly enforced by the engine — it is a consequence of the constitutive functions and the PDE dynamics — but the runtime checks ensure that no grid value exceeds $\rho_{\max}$.

**Principle 5 (Participation Feedback Loop).** The bidirectional coupling between $\rho$ and $v$ is enforced by the system structure: the density equation receives $Hv$ and the participation equation receives $F[\rho]$. The engine does not allow the coupling to be disabled (setting $H = 0$ is permitted only by setting $D = 1$, which reduces the system to a single PDE without participation).

**Principle 6 (Damping Discriminant).** The canonical damping parameter $\Delta = D + 2\zeta$ and the modal discriminant $\mathscr{D}_0$ are computed at initialization and stored as derived parameters. The regime classification (oscillatory if $\mathscr{D}_0 < 0$, monotonic if $\mathscr{D}_0 > 0$, critical if $\mathscr{D}_0 = 0$) is logged but does not affect the numerical method — the same solver handles all regimes without branching.

**Principle 7 (Nonlinear Triad Coupling).** The gradient-squared term $M'(\rho)|\nabla\rho|^2$ is computed by the operator evaluation module as part of $F[\rho]$. No special treatment is applied to this term — it is evaluated pointwise alongside the diffusion and penalty terms. The triad structure (selection rule, locked ratios) emerges from the dynamics; it is not imposed by the engine.

---

#### 1.1.6 Internal Representation

The simulation engine represents the canonical system as a structured data object with the following fields:

**System state.** The instantaneous state of the system at time $t$ is the pair $(\boldsymbol{\rho}, v)$, where:

- $\boldsymbol{\rho}$ is the discrete density field — an array of floating-point values at the grid points. In one dimension with $N_{\mathrm{grid}}$ grid points: $\boldsymbol{\rho} = (\rho_0, \rho_1, \ldots, \rho_{N_{\mathrm{grid}}-1}) \in \mathbb{R}^{N_{\mathrm{grid}}}$. In two dimensions on an $N \times N$ grid: $\boldsymbol{\rho} \in \mathbb{R}^{N \times N}$. The storage layout is row-major (C-order) in Python and Julia, column-major in MATLAB; the mathematical content is identical.

- $v$ is the participation variable — a single floating-point scalar.

The state is advanced in time by the time-stepping module (Atlas §10.1.2 or §10.1.3). At each time step, the state is overwritten in place (no history is stored unless the observable extraction module requests it).

**Parameter record.** The canonical parameters are stored in an immutable record created at initialization:

```
RECORD CanonicalParams:
    D       : Float64          // direct-channel weight, ∈ (0, 1)
    H       : Float64          // = 1 − D, mediated-channel weight
    zeta    : Float64          // participation damping, > 0
    tau     : Float64          // participation time scale, > 0
    rho_star: Float64          // penalty equilibrium density
    rho_max : Float64          // capacity bound

    // Derived quantities (computed once at initialization)
    Delta   : Float64          // = D + 2ζ
    M_star  : Float64          // = M(ρ*)
    M_star_prime : Float64     // = M'(ρ*)
    P_star_prime : Float64     // = P'(ρ*)
    D0      : Float64          // = (D·P*' − ζ/τ)² − 4H·P*'/τ
    gamma_0 : Float64          // = (D·P*' + ζ/τ)/2
    omega   : Float64          // = √|D0|/2  if D0 < 0, else 0
    regime  : Enum {Oscillatory, Monotonic, Critical}
```

The record is immutable: once created, its fields cannot be modified during the simulation. This prevents accidental parameter drift during long integrations.

**Constitutive function record.** The constitutive functions are stored as a pair of callable objects:

```
RECORD Constitutive:
    M       : Function(ρ) → Float64     // mobility
    M_prime : Function(ρ) → Float64     // mobility derivative
    P       : Function(ρ) → Float64     // penalty
    P_prime : Function(ρ) → Float64     // penalty derivative

    // Constitutive parameters (for reporting and reproducibility)
    M_params : (M0: Float64, beta: Float64)
    P_params : (P0: Float64, rho_star: Float64)
```

The callable interface allows the solver to evaluate the constitutive functions at arbitrary density values without knowing their functional form. The constitutive parameters are stored separately for reproducibility (they appear in the output metadata).

**Operator evaluation.** The operator $F[\rho]$ is computed by a dedicated evaluation function that takes the discrete density field $\boldsymbol{\rho}$, the constitutive functions, and the spatial discretization (grid spacing $h$ or spectral eigenvalues $\mu_k$) as inputs and returns the discrete operator values $F_j$ at each grid point (Method A) or the spectral coefficients $\hat{F}_k$ (Method B):

```
FUNCTION Evaluate_F(ρ, constitutive, spatial_discretization) → F_values:

    // Step 1: Compute spatial derivatives
    Lap = spatial_discretization.laplacian(ρ)      // ∇²ρ
    Grad2 = spatial_discretization.grad_squared(ρ)  // |∇ρ|²

    // Step 2: Evaluate constitutive functions pointwise
    FOR each grid point j:
        M_j     = constitutive.M(ρ_j)
        M_prime_j = constitutive.M_prime(ρ_j)
        P_j     = constitutive.P(ρ_j)

    // Step 3: Assemble the operator
    FOR each grid point j:
        F_j = M_j · Lap_j + M_prime_j · Grad2_j − P_j

    RETURN F_values
```

This function is the computational core of the simulation engine. It is called once per time step (Method A) or once per Runge–Kutta substep (Method B). Its correctness is verified by the linearized comparison test (Atlas §1.7.4): at small amplitude, the operator output must match the linearized prediction $F[\rho^* + u] \approx M_*\nabla^2 u - P_*' u$ to within $O(A^2)$.

**Runtime invariant checks.** At each time step, the engine verifies:

| Check | Condition | Action on failure |
|-------|-----------|-------------------|
| Density positivity | $\min_j \rho_j > 0$ | Activate positivity projection (§1.6 of Atlas) |
| Sub-capacity | $\max_j \rho_j < \rho_{\max}$ | Activate adaptive time-step reduction (§1.6 of Atlas) |
| Finiteness | All $\rho_j$ and $v$ are finite (not NaN or Inf) | Halt with diagnostic |
| Energy monotonicity | $\mathcal{E}^{n+1} \leq \mathcal{E}^n + \text{tol}$ | Log warning; halt if violated by $> 10 \cdot \text{tol}$ |

The tolerance for the energy monotonicity check is $\text{tol} = 10\,\Delta t^p\,\mathcal{E}^n$, where $p$ is the temporal order of the scheme ($p = 1$ for implicit Euler, $p = 2$ for Crank–Nicolson, $p = 4$ for ETD-RK4). This allows for the truncation-error violation of strict monotonicity while catching genuine numerical instabilities.

These checks implement the defensive computation principle of §0.3. They add negligible computational cost (a single pass over the array per time step) and provide the runtime guarantee that the structural properties of the continuous PDE — positivity, sub-capacity, energy dissipation — are maintained at the discrete level.

---

### 1.2 Data Structures

This subsection specifies the data structures used by the simulation engine to represent the physical state, the computational grid, the discrete spatial operators, and the spectral decomposition. The structures are described at the logical level — field names, dimensions, element types, and access patterns — independently of any programming language. The mapping to specific array types in Python (NumPy `ndarray`), Julia (`Array{Float64}`), and MATLAB (double array) is straightforward and noted where the conventions differ.

---

#### 1.2.1 Density Field $\rho(x, t)$

The density field is the primary unknown of the system. At each time step $t_n$, the discrete density is stored as a $d$-dimensional array whose shape matches the spatial grid.

**One dimension ($d = 1$).** The density is a one-dimensional array of length $N_{\mathrm{grid}}$:

```
ρ : Array[Float64], shape = (N_grid,)
```

where $N_{\mathrm{grid}} = N + 2$ for Method A (interior points plus two boundary points) or $N_{\mathrm{grid}} = N$ for Method B (spectral coefficients; see §1.2.6). The element $\rho_j$ represents the density at grid point $x_j = jh$, where $h = L/(N+1)$ for Method A. The boundary points $\rho_0$ and $\rho_{N+1}$ carry the Neumann-enforced values (ghost-point reflection; see Atlas §1.4.1).

**Two dimensions ($d = 2$).** The density is a two-dimensional array:

```
ρ : Array[Float64], shape = (N_x, N_y)
```

where $N_x$ and $N_y$ are the grid dimensions (including boundary points) in each coordinate direction. For the standard square domain $\Omega_2 = [0, L]^2$ with uniform spacing, $N_x = N_y = N + 2$. The element $\rho_{i,j}$ represents the density at $(x_i, y_j) = (ih, jh)$.

**Three dimensions ($d = 3$).** The density is a three-dimensional array:

```
ρ : Array[Float64], shape = (N_x, N_y, N_z)
```

with the analogous interpretation. The three-dimensional case is used only for the dimension-independence verification (Atlas §3.3.3, Experiment 3.7 extended) and is not needed for the majority of the Atlas experiments.

**Storage convention.** The density array stores the *full* grid, including boundary points. This convention simplifies the stencil computation (the Laplacian and gradient operators can be applied uniformly to all points, with the boundary values providing the ghost-point data) at the cost of a small memory overhead (two extra points per dimension). The alternative — storing only interior points and applying boundary conditions as special cases — is equally valid but complicates the stencil logic.

**Temporal storage.** By default, only the current state $\boldsymbol{\rho}^n$ is stored. The time-stepping module overwrites $\boldsymbol{\rho}^n$ with $\boldsymbol{\rho}^{n+1}$ at each step. When the observable extraction module requires access to previous states (e.g., for computing $d\mathcal{E}/dt$ by finite differences), a single-step history buffer $\boldsymbol{\rho}^{n-1}$ is maintained. Extended time-series storage (all states from $t = 0$ to $t = T$) is managed by the experiment orchestration module, which selectively records the state at user-specified output times.

---

#### 1.2.2 Participation Variable $v(t)$

The participation variable is a single scalar:

```
v : Float64
```

It is stored alongside the density array but is not part of it — the density is a spatial field, the participation is a global (spatially constant) scalar. The ODE for $v$ involves the spatially averaged operator output $\bar{F} = N_{\mathrm{grid}}^{-1}\sum_j F_j$ (Method A) or the zero-mode coefficient $\hat{F}_0$ (Method B), but $v$ itself has no spatial index.

**Temporal storage.** Like the density, only the current value $v^n$ is stored by default, with a single-step history $v^{n-1}$ maintained when needed.

---

#### 1.2.3 Grid Representation

The spatial grid is represented as a structured record that encodes the domain geometry, the grid spacing, and the coordinate arrays. The grid is created once at initialization and is immutable during the simulation.

**One-dimensional grid:**

```
RECORD Grid1D:
    d       : Int = 1                    // spatial dimension
    L       : Float64                    // domain length
    N       : Int                        // number of interior points
    N_grid  : Int = N + 2               // total points including boundary
    h       : Float64 = L / (N + 1)     // uniform spacing
    x       : Array[Float64], shape = (N_grid,)   // coordinate array
                                         // x_j = j · h for j = 0, ..., N+1
```

**Two-dimensional grid:**

```
RECORD Grid2D:
    d       : Int = 2
    L_x, L_y : Float64                  // domain lengths
    N_x, N_y : Int                      // interior points per direction
    N_grid_x : Int = N_x + 2
    N_grid_y : Int = N_y + 2
    h_x     : Float64 = L_x / (N_x + 1)
    h_y     : Float64 = L_y / (N_y + 1)
    x       : Array[Float64], shape = (N_grid_x,)
    y       : Array[Float64], shape = (N_grid_y,)
```

For the standard square domain $\Omega_2 = [0,1]^2$, $L_x = L_y = 1$, $N_x = N_y = N$, and $h_x = h_y = h$.

**Three-dimensional grid:**

```
RECORD Grid3D:
    d       : Int = 3
    L_x, L_y, L_z : Float64
    N_x, N_y, N_z : Int
    N_grid_x, N_grid_y, N_grid_z : Int  // each = N_i + 2
    h_x, h_y, h_z : Float64
    x, y, z : Array[Float64]            // coordinate arrays
```

**Grid-to-index mapping.** In all dimensions, the mapping from a multi-index $(i_1, \ldots, i_d)$ to a position is $x_{i_k} = i_k \cdot h_k$ for each coordinate $k = 1, \ldots, d$. The boundary points are at $i_k = 0$ and $i_k = N_k + 1$. The interior points are at $i_k = 1, \ldots, N_k$.

---

#### 1.2.4 Discrete Spatial Operators — Laplacian

The discrete Laplacian $\nabla_h^2\boldsymbol{\rho}$ is stored as an array of the same shape as $\boldsymbol{\rho}$, computed by applying the finite-difference stencil (Atlas §1.4.1).

**One dimension.** The Laplacian array is:

```
Lap : Array[Float64], shape = (N_grid,)
```

with $\mathrm{Lap}_j = (\rho_{j-1} - 2\rho_j + \rho_{j+1})/h^2$ for interior points $j = 1, \ldots, N$, and modified boundary stencils at $j = 0$ and $j = N+1$ using ghost-point reflection (Atlas eq. 1.13). The computation is a single pass over the array, accessing three consecutive elements per point. No matrix is formed or stored — the Laplacian is applied stencil-wise.

The *implicit* Laplacian (used in the implicit and Crank–Nicolson time-stepping schemes) requires the matrix representation $\mathbf{L}_h \in \mathbb{R}^{N_{\mathrm{grid}} \times N_{\mathrm{grid}}}$, which is tridiagonal. This matrix is not stored explicitly as a dense array; it is stored in the banded format:

```
RECORD TridiagLaplacian:
    lower  : Array[Float64], shape = (N_grid - 1,)   // sub-diagonal
    diag   : Array[Float64], shape = (N_grid,)        // main diagonal
    upper  : Array[Float64], shape = (N_grid - 1,)    // super-diagonal
```

The entries are $\mathrm{lower}_j = 1/h^2$, $\mathrm{diag}_j = -2/h^2$, $\mathrm{upper}_j = 1/h^2$ for interior points, with the Neumann-modified boundary entries. The total storage is $3N_{\mathrm{grid}} - 2$ floating-point values — three orders of magnitude less than the dense matrix for typical $N_{\mathrm{grid}} = 514$.

**Two dimensions.** The Laplacian array is:

```
Lap : Array[Float64], shape = (N_grid_x, N_grid_y)
```

computed by the five-point stencil (Atlas eq. 1.17). The implicit matrix is banded (bandwidth $= N_{\mathrm{grid}_x}$) and stored in the banded format appropriate to the environment's sparse solver. In Python (SciPy), this is `scipy.sparse.diags`; in Julia, `Tridiagonal` does not apply (the 2D matrix is not tridiagonal), so a sparse CSC format is used; in MATLAB, the backslash operator accepts sparse matrices directly.

**Three dimensions.** The Laplacian array is three-dimensional. The implicit matrix is sparse with bandwidth $N_{\mathrm{grid}_x} \cdot N_{\mathrm{grid}_y}$. Only iterative solvers (conjugate gradient with incomplete Cholesky preconditioning) are practical for $N > 32$.

---

#### 1.2.5 Discrete Spatial Operators — Gradient and Gradient-Squared

The discrete gradient-squared $|\nabla_h\boldsymbol{\rho}|^2$ is stored as an array of the same shape as $\boldsymbol{\rho}$.

**One dimension:**

```
Grad2 : Array[Float64], shape = (N_grid,)
```

with $\mathrm{Grad2}_j = ((\rho_{j+1} - \rho_{j-1})/(2h))^2$ for interior points, and $\mathrm{Grad2}_0 = \mathrm{Grad2}_{N+1} = 0$ at the boundaries (Atlas eq. 1.15). The boundary values vanish identically by the Neumann condition.

**Two dimensions:**

```
Grad2 : Array[Float64], shape = (N_grid_x, N_grid_y)
```

with $\mathrm{Grad2}_{i,j} = ((\rho_{i+1,j} - \rho_{i-1,j})/(2h_x))^2 + ((\rho_{i,j+1} - \rho_{i,j-1})/(2h_y))^2$ (Atlas eq. 1.18). The gradient components along each axis are computed and squared separately, then summed. On boundaries, the ghost-point reflection ensures the vanishing of the normal gradient component.

**Intermediate gradient arrays.** When the individual gradient components $\partial\rho/\partial x_k$ are needed (e.g., for the effective-complexity observable $C_{\mathrm{ED}}^{\mathrm{eff}}$, which involves $|\nabla\rho|^2$ weighted by constitutive factors), the engine computes and stores the component arrays:

```
Grad_x : Array[Float64], shape = (same as ρ)   // (ρ_{j+1} − ρ_{j−1}) / (2h)
Grad_y : Array[Float64], shape = (same as ρ)   // (2D and 3D only)
Grad_z : Array[Float64], shape = (same as ρ)   // (3D only)
```

These are computed from the density array by centered differences and are discarded after the operator evaluation (they are not needed between time steps).

---

#### 1.2.6 Nonlinear Operator and Right-Hand Side

The full nonlinear operator $F[\boldsymbol{\rho}]$ and the right-hand side of the density equation are stored as arrays of the same shape as $\boldsymbol{\rho}$.

```
F_values : Array[Float64], shape = (same as ρ)
RHS      : Array[Float64], shape = (same as ρ)
```

The operator is assembled pointwise (§1.1.6):

$$
F_j = M(\rho_j)\cdot\mathrm{Lap}_j + M'(\rho_j)\cdot\mathrm{Grad2}_j - P(\rho_j).
$$

The right-hand side of the implicit system (Atlas eqs. 1.23, 1.27) is:

$$
\mathrm{RHS}_j = \rho_j + \Delta t\,\bigl[D\,M'(\rho_j)\cdot\mathrm{Grad2}_j - D\,P(\rho_j) + H\,v\bigr].
$$

Both arrays are workspace — computed at the beginning of each time step and consumed by the linear solver. They are overwritten at every step and need not be preserved.

**Constitutive evaluation buffers.** The pointwise constitutive evaluations $M(\rho_j)$, $M'(\rho_j)$, $P(\rho_j)$, $P'(\rho_j)$ are stored in temporary arrays of the same shape as $\boldsymbol{\rho}$:

```
M_vals      : Array[Float64], shape = (same as ρ)
M_prime_vals: Array[Float64], shape = (same as ρ)
P_vals      : Array[Float64], shape = (same as ρ)
P_prime_vals: Array[Float64], shape = (same as ρ)
```

These are computed once per time step (or once per Runge–Kutta substep) and reused across the operator evaluation and the implicit matrix assembly. The cost of evaluating the constitutive functions is typically negligible compared to the linear solve, but storing the results avoids redundant evaluation.

**Mobility-weighted Laplacian.** The implicit time-stepping matrix $\mathbf{I} - \Delta t\,D\,\operatorname{diag}(M(\boldsymbol{\rho}))\,\mathbf{L}_h$ requires the pointwise product of the mobility and the Laplacian stencil. In one dimension, this is a tridiagonal matrix whose entries vary along the diagonal:

```
RECORD MobilityWeightedTridiag:
    lower  : Array[Float64], shape = (N_grid - 1,)
    diag   : Array[Float64], shape = (N_grid,)
    upper  : Array[Float64], shape = (N_grid - 1,)
```

with entries $\mathrm{lower}_j = -\Delta t\,D\,M(\rho_j)/h^2$ (and similarly for the upper and diagonal entries, adjusted by the implicit/Crank–Nicolson coefficient). This matrix is rebuilt at every time step because $M(\rho_j)$ changes — the tridiagonal structure is preserved, but the entries are density-dependent.

---

#### 1.2.7 Spectral-Mode Storage (Method B)

For the spectral method, the density is represented in the Neumann cosine basis (Atlas §1.4.2, eq. 1.19). The spectral coefficients replace the physical-space grid values as the primary state representation.

**One dimension.** The spectral state is:

```
ρ_hat : Array[Float64], shape = (N_modes,)
```

where $N_{\mathrm{modes}} = N$ is the number of retained modes ($k = 0, 1, \ldots, N-1$). The coefficient $\hat{\rho}_k$ is the amplitude of the $k$-th Neumann eigenfunction $\phi_k(x) = c_k\cos(k\pi x/L)$, where $c_0 = 1/\sqrt{L}$ and $c_k = \sqrt{2/L}$ for $k \geq 1$. The physical density is reconstructed by the inverse DCT: $\rho_j = \sum_k \hat{\rho}_k\,\phi_k(x_j)$.

**Associated spectral arrays:**

```
RECORD SpectralData:
    rho_hat    : Array[Float64], shape = (N_modes,)   // modal amplitudes
    mu         : Array[Float64], shape = (N_modes,)   // eigenvalues μ_k = (kπ/L)²
    alpha      : Array[Float64], shape = (N_modes,)   // decay coefficients α_k = M*·μ_k + P*'
    c_linear   : Array[Float64], shape = (N_modes,)   // linear rates c_k = −D·M*·μ_k
    exp_factor : Array[Float64], shape = (N_modes,)   // e^{c_k·Δt} (precomputed)
    exp_half   : Array[Float64], shape = (N_modes,)   // e^{c_k·Δt/2} (precomputed)
    phi_weights: Array[Float64], shape = (3, N_modes,) // ETD-RK4 weight functions φ₃₁, φ₃₂, φ₃₃
```

The eigenvalues $\mu_k$, decay coefficients $\alpha_k$, linear rates $c_k$, and exponential factors are computed once at initialization (they depend only on the grid and the equilibrium constitutive values, not on the evolving state). The ETD-RK4 weight functions (Atlas §10.1.3) are also precomputed and stored, including the Taylor-series values for small $|c_k\Delta t|$ to avoid cancellation.

**Pseudospectral workspace.** The nonlinear terms are evaluated in physical space via the pseudospectral approach (Atlas §1.4.2). This requires a physical-space grid for the transform:

```
RECORD PseudospectralWorkspace:
    N_phys      : Int = 3 * N_modes / 2       // de-aliased physical grid (3/2 rule)
    rho_phys    : Array[Float64], shape = (N_phys,)    // density in physical space
    Lap_phys    : Array[Float64], shape = (N_phys,)    // Laplacian in physical space
    Grad_phys   : Array[Float64], shape = (N_phys,)    // gradient in physical space
    Grad2_phys  : Array[Float64], shape = (N_phys,)    // gradient-squared
    F_phys      : Array[Float64], shape = (N_phys,)    // nonlinear operator in physical space
    F_hat       : Array[Float64], shape = (N_modes,)   // operator in spectral space (truncated)
```

The physical grid has $3N/2$ points (the 3/2-rule for de-aliasing quadratic nonlinearities; Atlas §1.4.2). At each substep of the ETD-RK4 scheme, the spectral coefficients are transformed to the physical grid, the nonlinear terms are evaluated pointwise, and the result is transformed back and truncated to $N$ modes. The workspace arrays are overwritten at every substep.

**Two-dimensional spectral storage.** On $\Omega_2$, the spectral coefficients form a two-dimensional array:

```
rho_hat_2d : Array[Float64], shape = (N_modes_x, N_modes_y)
```

with eigenvalues $\mu_{k_1, k_2} = (k_1\pi/L_x)^2 + (k_2\pi/L_y)^2$. The 2D DCT is computed as a sequence of 1D DCTs along each axis (the tensor-product structure of the Neumann basis on a rectangular domain).

---

#### 1.2.8 Observable Storage

The observables extracted at each output time (Atlas §10.1.5) are stored in a structured record:

```
RECORD Observables:
    t          : Float64                    // current time
    energy     : Float64                    // E[ρ, v] (eq. C.3)
    C_ED       : Float64                    // ∫|∇ρ|² dx
    C_ED_eff   : Float64                    // ∫(P'/M)|∇ρ|² dx
    lyapunov   : Float64                    // V[u, w] (Definition C.39)
    rho_bar    : Float64                    // spatial mean of ρ
    a_0        : Float64                    // homogeneous-mode amplitude
    v          : Float64                    // participation variable
    delta      : Float64                    // proximity margin ρ_max − max(ρ)
    D_diff     : Float64                    // gradient dissipation channel
    D_pen      : Float64                    // penalty dissipation channel
    D_part     : Float64                    // participation dissipation channel
    modal_amps : Array[Float64], shape = (N_obs_modes,)  // |â_k| for k = 0, ..., N_obs−1
```

The field `N_obs_modes` is the number of modal amplitudes to track; it defaults to $\min(32, N_{\mathrm{modes}})$ but can be increased for experiments that require higher-mode monitoring (e.g., the cascade experiments of Atlas §4.3).

**Time-series storage.** The observables at all output times form a time series:

```
RECORD TimeSeries:
    n_steps    : Int                        // number of recorded time steps
    times      : Array[Float64], shape = (n_steps,)
    observables: Array[Observables], shape = (n_steps,)
```

The output times are a subset of the integration time steps, specified by the experiment: either every $k$-th step (for uniform sampling) or at a list of prescribed times (for snapshot-based experiments like Atlas §4.3.2, where specific time slices are needed). The time series is the primary output of every experiment and the input to the figure-generation pipeline (Atlas §11).

---

#### 1.2.9 Memory Layout and Performance Considerations

**Memory footprint.** The dominant memory cost is the density array and its associated workspace. For Method A in one dimension at $N_{\mathrm{grid}} = 514$ (the default $N = 512$):

| Array | Elements | Bytes (Float64) |
|-------|----------|-----------------|
| $\boldsymbol{\rho}$ (current) | 514 | 4,112 |
| $\boldsymbol{\rho}$ (history) | 514 | 4,112 |
| Lap, Grad2, F, RHS | $4 \times 514$ | 16,448 |
| $M$, $M'$, $P$, $P'$ buffers | $4 \times 514$ | 16,448 |
| Implicit tridiagonal | $3 \times 514$ | 12,336 |
| **Total (Method A, 1D)** | | **$\approx$ 53 KB** |

For Method B with $N_{\mathrm{modes}} = 128$:

| Array | Elements | Bytes |
|-------|----------|-------|
| $\hat{\boldsymbol{\rho}}$ (current) | 128 | 1,024 |
| Spectral arrays ($\mu$, $\alpha$, $c$, exp, weights) | $8 \times 128$ | 8,192 |
| Pseudospectral workspace ($N_{\mathrm{phys}} = 192$) | $6 \times 192$ | 9,216 |
| **Total (Method B, 1D)** | | **$\approx$ 18 KB** |

For Method A in two dimensions at $N = 64$ ($N_{\mathrm{grid}} = 66$ per direction):

| Array | Elements | Bytes |
|-------|----------|-------|
| $\boldsymbol{\rho}$ (current) | $66^2 = 4{,}356$ | 34,848 |
| Workspace arrays ($\times 8$) | $8 \times 4{,}356$ | 278,784 |
| Implicit banded matrix | $\sim 5 \times 4{,}356$ | 174,240 |
| **Total (Method A, 2D)** | | **$\approx$ 488 KB** |

All footprints are well within the $< 500$ MB limit stated in §0.5. Memory is not a constraint for any experiment in the Atlas.

**Access patterns.** The dominant computational operation is the stencil evaluation (Laplacian and gradient), which accesses the density array in a regular, stride-one pattern along each dimension. This pattern is cache-friendly in all environments when the array storage matches the access order:

- In Python (NumPy) and Julia: use row-major (C-order) storage for 1D arrays and the default (row-major in NumPy, column-major in Julia) for multi-dimensional arrays. The stencil loop should iterate over the fastest-varying index in the innermost loop.
- In MATLAB: arrays are column-major. The stencil loop should iterate over the first index in the innermost loop.

For the spectral method, the DCT is the dominant operation. All target environments provide FFT-based DCT implementations that are internally optimized for cache performance; no additional layout tuning is needed.

**Allocation discipline.** All workspace arrays (Lap, Grad2, F, RHS, constitutive buffers) are allocated once at initialization and reused at every time step. No dynamic allocation occurs inside the time-stepping loop. This eliminates garbage-collection overhead in Python and Julia and ensures predictable memory behavior for long integrations ($> 10^5$ steps).

---

### 1.3 Spatial Discretization

This subsection specifies the two spatial discretization methods used by the simulation engine: the finite-difference method (Method A) and the spectral method (Method B). Both are described in the Numerical Atlas (§1.4); the present section provides the implementation-level detail — the mathematical formulas, the properties that the implementation must preserve, the error characteristics, and the criteria for selecting one method over the other.

The notation follows Atlas §1.4 and Appendix C throughout. The domain is $\Omega = [0, L]^d$ with Neumann boundary conditions $\partial_\nu\rho = 0$ on $\partial\Omega$.

---

#### 1.3.1 Finite-Difference Discretization (Method A)

##### 1.3.1.1 Grid and Stencils in One Dimension

The domain $\Omega_1 = [0, L]$ is discretized on a uniform grid of $N_{\mathrm{grid}} = N + 2$ points (including the two boundary points) with spacing $h = L/(N+1)$ and coordinates $x_j = jh$ for $j = 0, 1, \ldots, N+1$.

**Discrete Laplacian.** The second-order central-difference approximation to $\nabla^2\rho$ at an interior point $j \in \{1, \ldots, N\}$ is

$$
(\nabla_h^2\rho)_j = \frac{\rho_{j-1} - 2\rho_j + \rho_{j+1}}{h^2}.
$$

At the boundary points, the Neumann condition $\partial_\nu\rho = 0$ is enforced by ghost-point reflection. The left boundary ($j = 0$) uses the reflected value $\rho_{-1} := \rho_1$, giving

$$
(\nabla_h^2\rho)_0 = \frac{2(\rho_1 - \rho_0)}{h^2}.
$$

The right boundary ($j = N+1$) uses $\rho_{N+2} := \rho_N$, giving

$$
(\nabla_h^2\rho)_{N+1} = \frac{2(\rho_N - \rho_{N+1})}{h^2}.
$$

The resulting discrete Laplacian $\nabla_h^2 : \mathbb{R}^{N_{\mathrm{grid}}} \to \mathbb{R}^{N_{\mathrm{grid}}}$ is a linear operator represented by the tridiagonal matrix $\mathbf{L}_h$ with the structure described in §1.2.4. It has the following properties that the implementation must preserve:

1. **Symmetry.** $\mathbf{L}_h$ is symmetric: $(\mathbf{L}_h)_{ij} = (\mathbf{L}_h)_{ji}$. This follows from the ghost-point construction and ensures that the discrete energy identity is structurally consistent with the continuous one (Lemma C.6).

2. **Negative semi-definiteness.** All eigenvalues of $\mathbf{L}_h$ are non-positive. The null space is one-dimensional, spanned by the constant vector $\mathbf{1} = (1, 1, \ldots, 1)^\top$. This is the discrete analogue of $\nabla^2 c = 0$ for a constant $c$, with $\int_\Omega\nabla^2\varphi\,dx = 0$ for Neumann conditions.

3. **Second-order accuracy.** $(\nabla_h^2\rho)_j = (\nabla^2\rho)(x_j) + O(h^2)$ for smooth $\rho$.

**Discrete gradient-squared.** The centered first-difference approximation to $|\nabla\rho|^2$ is

$$
(|\nabla_h\rho|^2)_j = \left(\frac{\rho_{j+1} - \rho_{j-1}}{2h}\right)^2
$$

for interior points $j \in \{1, \ldots, N\}$, and

$$
(|\nabla_h\rho|^2)_0 = 0, \qquad (|\nabla_h\rho|^2)_{N+1} = 0
$$

at the boundaries. The boundary values vanish identically because the Neumann condition $\partial_\nu\rho = 0$ implies $|\nabla\rho|^2 = (\partial_x\rho)^2 = 0$ at $x = 0$ and $x = L$. The discrete gradient-squared is non-negative everywhere and second-order accurate: $(|\nabla_h\rho|^2)_j = |\nabla\rho(x_j)|^2 + O(h^2)$.

**Discrete gradient components.** When the signed gradient $\partial_x\rho$ is needed (e.g., for the spectral analysis pipeline), the centered first difference is

$$
(\nabla_h\rho)_j = \frac{\rho_{j+1} - \rho_{j-1}}{2h},
$$

with $(\nabla_h\rho)_0 = 0$ and $(\nabla_h\rho)_{N+1} = 0$ by the Neumann condition.

**Discrete operator.** The full discrete nonlinear operator $F_h[\boldsymbol{\rho}]$ is assembled pointwise:

$$
F_h[\boldsymbol{\rho}]_j = M(\rho_j)\,(\nabla_h^2\rho)_j + M'(\rho_j)\,(|\nabla_h\rho|^2)_j - P(\rho_j)
$$

for $j = 0, 1, \ldots, N+1$. The evaluation requires three arrays (Laplacian, gradient-squared, and $F$-values) and two constitutive evaluations ($M$, $M'$, $P$) per grid point. The total cost is $O(N)$ per evaluation.

##### 1.3.1.2 Extension to Two Dimensions

On $\Omega_2 = [0, L_x] \times [0, L_y]$ with uniform spacing $h_x = L_x/(N_x+1)$, $h_y = L_y/(N_y+1)$:

**Discrete Laplacian (five-point stencil).**

$$
(\nabla_h^2\rho)_{i,j} = \frac{\rho_{i-1,j} + \rho_{i+1,j} - 2\rho_{i,j}}{h_x^2} + \frac{\rho_{i,j-1} + \rho_{i,j+1} - 2\rho_{i,j}}{h_y^2}
$$

for interior points $(i, j) \in \{1, \ldots, N_x\} \times \{1, \ldots, N_y\}$. The boundary stencils use ghost-point reflection along each edge independently: $\rho_{-1,j} := \rho_{1,j}$, $\rho_{N_x+2,j} := \rho_{N_x,j}$, and symmetrically in the $y$-direction. At corners, the reflection is applied in both directions.

The two-dimensional discrete Laplacian matrix has bandwidth $N_{\mathrm{grid}_x}$ and is stored in sparse format (§1.2.4). It retains the symmetry, negative semi-definiteness, and constant-vector null space of the one-dimensional case.

**Discrete gradient-squared (two-component sum).**

$$
(|\nabla_h\rho|^2)_{i,j} = \left(\frac{\rho_{i+1,j} - \rho_{i-1,j}}{2h_x}\right)^2 + \left(\frac{\rho_{i,j+1} - \rho_{i,j-1}}{2h_y}\right)^2.
$$

The boundary values along each edge vanish in the corresponding normal component. On the standard square domain with $h_x = h_y = h$, the stencil simplifies to a sum of two centered-difference squares.

##### 1.3.1.3 Extension to Three Dimensions

On $\Omega_3 = [0, L_x] \times [0, L_y] \times [0, L_z]$:

**Discrete Laplacian (seven-point stencil).**

$$
(\nabla_h^2\rho)_{i,j,k} = \frac{\rho_{i-1,j,k} + \rho_{i+1,j,k} - 2\rho_{i,j,k}}{h_x^2} + \frac{\rho_{i,j-1,k} + \rho_{i,j+1,k} - 2\rho_{i,j,k}}{h_y^2} + \frac{\rho_{i,j,k-1} + \rho_{i,j,k+1} - 2\rho_{i,j,k}}{h_z^2}.
$$

The three-dimensional Laplacian matrix has bandwidth $N_{\mathrm{grid}_x} \cdot N_{\mathrm{grid}_y}$. Direct solution is impractical for $N > 32$; iterative methods (conjugate gradient with incomplete Cholesky preconditioning) are used instead.

**Discrete gradient-squared (three-component sum).**

$$
(|\nabla_h\rho|^2)_{i,j,k} = \left(\frac{\rho_{i+1,j,k} - \rho_{i-1,j,k}}{2h_x}\right)^2 + \left(\frac{\rho_{i,j+1,k} - \rho_{i,j-1,k}}{2h_y}\right)^2 + \left(\frac{\rho_{i,j,k+1} - \rho_{i,j,k-1}}{2h_z}\right)^2.
$$

##### 1.3.1.4 Properties of the Finite-Difference Discretization

The following properties are structural — they must be verified by any implementation and are tested by the validation suite (Atlas §1.7):

| Property | Mathematical statement | Test |
|----------|----------------------|------|
| Symmetry of $\mathbf{L}_h$ | $\mathbf{L}_h = \mathbf{L}_h^\top$ | Verify $\|\mathbf{L}_h - \mathbf{L}_h^\top\| < 10^{-14}$ |
| Null space of $\mathbf{L}_h$ | $\mathbf{L}_h\mathbf{1} = \mathbf{0}$ | Verify $\|\mathbf{L}_h\mathbf{1}\|_\infty < 10^{-14}$ |
| Negative semi-definiteness | $\mathbf{x}^\top\mathbf{L}_h\mathbf{x} \leq 0$ for all $\mathbf{x}$ | Check sign of largest eigenvalue |
| Second-order accuracy | $\|\nabla_h^2 f - f''\|_\infty = O(h^2)$ for $f(x) = \cos(\pi x)$ | Verify convergence rate in §1.7.1 |
| Boundary consistency | $(|\nabla_h\rho|^2)_{\mathrm{boundary}} = 0$ | Verify identically zero at $j = 0, N+1$ |

These properties are not merely desirable — they are required for the discrete system to preserve the structural content of the continuous PDE. The symmetry of $\mathbf{L}_h$ ensures that the discrete energy identity has the correct sign structure. The null-space property ensures that the discrete mass equation is consistent with the continuous one ($\int_\Omega\nabla^2\rho\,dx = 0$ under Neumann conditions). The boundary consistency ensures that the discrete gradient-squared vanishes where the continuous one does.

---

#### 1.3.2 Spectral Discretization (Method B)

##### 1.3.2.1 The Neumann Eigenbasis

On the domain $\Omega_1 = [0, L]$, the Neumann Laplacian $-\nabla^2$ has the eigenfunctions

$$
\phi_k(x) = \begin{cases} \displaystyle\frac{1}{\sqrt{L}} & k = 0, \\[8pt] \displaystyle\sqrt{\frac{2}{L}}\,\cos\!\left(\frac{k\pi x}{L}\right) & k \geq 1, \end{cases}
$$

with eigenvalues

$$
\mu_k = \left(\frac{k\pi}{L}\right)^2, \qquad k = 0, 1, 2, \ldots
$$

The eigenfunctions satisfy $-\nabla^2\phi_k = \mu_k\phi_k$, $\partial_\nu\phi_k = 0$ on $\partial\Omega$, and the orthonormality relation $\langle\phi_m, \phi_n\rangle_{L^2(\Omega)} = \delta_{mn}$. The set $\{\phi_k\}_{k=0}^\infty$ forms a complete orthonormal basis for $L^2(\Omega)$.

The Neumann boundary condition is *built into the basis*: every function representable as $\rho(x) = \sum_k \hat{\rho}_k\phi_k(x)$ automatically satisfies $\partial_\nu\rho = 0$ at $x = 0$ and $x = L$ (since each $\phi_k$ does). This is the fundamental advantage of the spectral method for the ED system: the boundary condition is satisfied exactly, at every truncation level, with no ghost points or boundary stencils.

**Two-dimensional extension.** On $\Omega_2 = [0, L_x] \times [0, L_y]$, the eigenbasis is the tensor product $\{\phi_{k_1}(x)\,\phi_{k_2}(y)\}_{k_1, k_2 \geq 0}$ with eigenvalues $\mu_{k_1,k_2} = (k_1\pi/L_x)^2 + (k_2\pi/L_y)^2$. The two-dimensional DCT is computed as a sequence of one-dimensional DCTs along each axis.

##### 1.3.2.2 Spectral Representation of the Density

The density deviation $u(x,t) = \rho(x,t) - \rho^*$ is expanded in the truncated Neumann basis:

$$
u(x, t) = \sum_{k=0}^{N-1} \hat{u}_k(t)\,\phi_k(x),
$$

where $N$ is the number of retained modes and $\hat{u}_k(t) = \langle u(\cdot, t), \phi_k\rangle_{L^2}$ are the spectral coefficients. The full density is $\rho(x,t) = \rho^* + u(x,t)$, so $\hat{\rho}_k = \hat{u}_k$ for $k \geq 1$ and $\hat{\rho}_0 = \rho^*\sqrt{L} + \hat{u}_0$ (the mean density includes the equilibrium contribution).

The simulation engine stores the coefficients $\hat{u}_k$ (the deviation from equilibrium) as the primary spectral state, not the full $\hat{\rho}_k$. This choice has two advantages: the equilibrium is exactly $\hat{u}_k = 0$ for all $k$ (no residual from the constant $\rho^*$), and the convergence diagnostics ($\|\hat{u}\| \to 0$) are directly readable from the spectral state.

##### 1.3.2.3 Linear Operations in Spectral Space

The Laplacian acts diagonally on the spectral coefficients:

$$
\widehat{(\nabla^2 u)}_k = -\mu_k\,\hat{u}_k.
$$

This is exact — no approximation, no truncation error, no stencil. The linear part of the $\rho$-equation (the terms involving $M_*\nabla^2 u$ and $-P_*' u$ from the linearization at equilibrium) is therefore:

$$
\widehat{(\text{linear})}_k = -D\,\alpha_k\,\hat{u}_k, \qquad \alpha_k = M_*\mu_k + P_*'.
$$

Each mode $k$ decays independently at rate $D\alpha_k$ in the linearized system. The spectral method resolves this decay exactly (up to the time-stepping error), regardless of $N$, because the linear part requires no spatial approximation.

The gradient in spectral space is computed via the derivative of the cosine basis:

$$
\widehat{(\partial_x u)}_k = -\frac{k\pi}{L}\,\tilde{u}_k,
$$

where $\tilde{u}_k$ are the coefficients in the *sine* basis (the DCT of $u$ maps to the DST of $\partial_x u$, reflecting the derivative relationship $d\cos = -\sin$). The gradient operation maps cosine coefficients to sine coefficients:

$$
\partial_x\!\left[\sum_k \hat{u}_k\,\sqrt{\frac{2}{L}}\cos\frac{k\pi x}{L}\right] = -\sum_k \hat{u}_k\,\frac{k\pi}{L}\,\sqrt{\frac{2}{L}}\sin\frac{k\pi x}{L}.
$$

The gradient-squared $|\nabla u|^2 = (\partial_x u)^2$ is a pointwise product, which introduces mode coupling and is handled pseudospectrally (§1.3.2.4).

##### 1.3.2.4 Pseudospectral Evaluation of Nonlinear Terms

The nonlinear terms in $F[\rho]$ — specifically $M(\rho)\nabla^2\rho$, $M'(\rho)|\nabla\rho|^2$, and $P(\rho)$ — involve pointwise nonlinear functions of $\rho$ and cannot be computed in spectral space (where they would require convolution sums). Instead, they are evaluated in physical space via the pseudospectral approach:

**Step 1: Transform to physical space.** Compute $u(x_j)$ at $N_{\mathrm{phys}}$ uniformly spaced grid points via the inverse DCT (Type-I):

$$
u_j = \sum_{k=0}^{N-1} \hat{u}_k\,\phi_k(x_j), \qquad j = 0, 1, \ldots, N_{\mathrm{phys}} - 1.
$$

The physical density is $\rho_j = \rho^* + u_j$.

**Step 2: Compute spatial derivatives in spectral space, then transform.** The Laplacian $\nabla^2 u$ is computed spectrally ($\widehat{(\nabla^2 u)}_k = -\mu_k\hat{u}_k$) and then transformed to physical space by the same inverse DCT. The gradient $\partial_x u$ is computed via the cosine-to-sine derivative relation and transformed by the inverse DST. The gradient-squared is formed by squaring the physical-space gradient array pointwise.

**Step 3: Evaluate nonlinear terms pointwise.** At each physical-space grid point $j$:

$$
\mathcal{N}_j = \bigl[M(\rho_j) - M_*\bigr]\,(\nabla^2 u)_j + M'(\rho_j)\,|\nabla u_j|^2 - \bigl[P(\rho_j) - P(\rho^*) - P_*'\,u_j\bigr].
$$

This is the *nonlinear residual* — the part of $F[\rho]$ that is not captured by the linear operator $-\alpha_k\hat{u}_k$. It contains the density-dependence of the mobility ($M(\rho) - M_*$), the gradient-squared nonlinearity ($M'|\nabla u|^2$), and the nonlinear penalty ($P(\rho) - P_*' u$). The last term vanishes for the linear penalty $P(\rho) = P_0(\rho - \rho^*)$, but the formulation retains it for generality.

**Step 4: Transform back to spectral space.** The nonlinear residual $\mathcal{N}_j$ is transformed to spectral space via the forward DCT:

$$
\hat{\mathcal{N}}_k = \text{DCT}\{\mathcal{N}_j\}, \qquad k = 0, 1, \ldots, N - 1.
$$

Modes $k \geq N$ are discarded (truncation). The total right-hand side for mode $k$ in the spectral system is:

$$
\frac{d\hat{u}_k}{dt} = -D\,\alpha_k\,\hat{u}_k + D\,\hat{\mathcal{N}}_k + H\,v\,\delta_{k0}\,\sqrt{L},
$$

where the participation term $Hv$ contributes only to the $k = 0$ mode (since $v$ is spatially constant). The linear part $-D\alpha_k\hat{u}_k$ is integrated exactly by the ETD scheme; the nonlinear part $D\hat{\mathcal{N}}_k$ is treated explicitly within the Runge–Kutta substeps.

##### 1.3.2.5 De-Aliasing by the 3/2-Rule

The pointwise evaluation in Step 3 introduces aliasing: the product of two functions with bandwidth $N$ has bandwidth $2N$, and when sampled on an $N$-point grid, the modes $k \geq N$ are folded back into the resolved range $k < N$, corrupting the spectral coefficients.

The standard remedy is the **3/2-rule** (also called zero-padding): the physical-space evaluation is performed on a grid of $N_{\mathrm{phys}} = \lfloor 3N/2\rfloor$ points. The spectral coefficients are zero-padded from $N$ to $N_{\mathrm{phys}}$ modes before the inverse transform, the nonlinear evaluation is performed on the finer grid, and the forward transform yields $N_{\mathrm{phys}}$ modes, of which only the first $N$ are retained. This ensures that the *quadratic* products (gradient-squared, mobility times Laplacian) are alias-free: their spectral content up to mode $2N$ is fully resolved on the $3N/2$ grid and correctly projected onto the first $N$ modes.

For the ED system, the nonlinear terms are at most quadratic in the perturbation (the leading nonlinearity is $M'|\nabla u|^2$, which is quadratic in $\nabla u$). The 3/2-rule is therefore sufficient. For constitutive functions with higher-order polynomial structure (e.g., $M(\rho) = (\rho_{\max} - \rho)^3$ with $\beta = 3$), the aliasing from higher-order products may require a larger padding factor (2× instead of 3/2×); this is flagged by the constitutive validation (§1.1.4) when $\beta > 2$.

##### 1.3.2.6 Properties of the Spectral Discretization

| Property | Mathematical statement | Significance |
|----------|----------------------|--------------|
| Exact boundary conditions | $\partial_\nu\phi_k = 0$ for all $k$ | No ghost points needed; no boundary error |
| Exact linear operator | $\widehat{(\nabla^2 u)}_k = -\mu_k\hat{u}_k$ exactly | No spatial truncation error for linear terms |
| Spectral accuracy | Truncation error $\sim e^{-cN}$ for analytic $u$ | Exponentially fast convergence for smooth solutions |
| Orthonormality | $\langle\phi_m, \phi_n\rangle = \delta_{mn}$ | Energy-preserving transform; Parseval identity |
| Alias-free quadratic products | 3/2-rule ensures $O(h^{2N/3})$ aliasing error | Correct triad coupling to machine precision |
| Diagonal linear part | $\hat{u}_k$ modes decouple linearly | Enables ETD exact integration of stiff modes |

The spectral method's key advantage for the ED system is the combination of exact boundary conditions (Neumann built into the basis), exact linear operator (diagonal Laplacian), and spectral accuracy (exponential convergence for smooth solutions). Its disadvantage is the $O(N\log N)$ cost of the DCT at each substep and the complexity of the pseudospectral nonlinear evaluation. For the $N = 128$ modes used in the Atlas spectral experiments, the DCT cost is negligible.

---

#### 1.3.3 Method Selection Criteria

The two spatial discretization methods are complementary. The simulation engine selects (or the user specifies) the method according to the following criteria:

| Criterion | Method A (Finite Difference) | Method B (Spectral) |
|-----------|------------------------------|---------------------|
| **Primary use** | General-purpose integration | Modal analysis and spectral experiments |
| **Boundary conditions** | Neumann (ghost-point); extensible to Dirichlet, Robin | Neumann only (built into basis) |
| **Spatial accuracy** | Second-order ($O(h^2)$) | Spectral ($O(e^{-cN})$ for smooth $\rho$) |
| **Resolution needed for $1\%$ accuracy** | $N \sim 256$–$512$ | $N \sim 32$–$64$ |
| **Cost per time step** | $O(N)$ (tridiagonal solve) | $O(N\log N)$ (DCT + pseudospectral) |
| **Domain geometry** | Arbitrary rectangular; extensible to irregular | Rectangular only |
| **Spatial dimension** | 1D, 2D, 3D (with increasing cost) | 1D (standard); 2D (tensor-product) |
| **Near-horizon handling** | Direct (density-dependent stencil coefficients) | Requires care (constitutive evaluation on de-aliased grid) |
| **Modal amplitude extraction** | Requires post-hoc DCT of the grid solution | Native (spectral coefficients are the state) |
| **Triad coupling analysis** | Requires spectral post-processing | Native (coupling coefficients computed from spectral state) |
| **Implicit time stepping** | Natural (tridiagonal or banded linear system) | Not needed (ETD integrates linear part exactly) |

**Default recommendation.** Method A with Crank–Nicolson time stepping (Atlas §1.5.2) at $N = 512$ is the default for all experiments except those in the "spectral" category:

- **Use Method A** for: convergence studies (§1.7), regime geometry (§2), energy dissipation (§1.7.2), complexity dynamics (§5), horizon behavior (§6), three-stage convergence (§7), regime transitions (§8), and cross-domain demonstrations that do not require modal decomposition (§9.2, §9.5).

- **Use Method B** for: single-mode decay verification (§3.1), multi-mode spectral analysis (§3.2–§3.3), triad activation and selection-rule verification (§4.1), locked amplitude ratio measurement (§4.2), harmonic cascade tracking (§4.3), pattern spectrum analysis (§9.3), and driven-cavity harmonic locking (§9.4).

- **Use both** for: the validation tests (§1.7), where cross-method agreement is part of the acceptance criterion, and for any experiment where the result's independence from the spatial discretization must be confirmed.

**Cross-validation protocol.** For any experiment run with both methods, the acceptance criterion is:

$$
\frac{\|\boldsymbol{\rho}_A(t) - \boldsymbol{\rho}_B(t)\|_{L^2}}{\|\boldsymbol{\rho}_A(t) - \rho^*\|_{L^2}} < \epsilon_{\mathrm{cross}},
$$

where $\boldsymbol{\rho}_A$ is the Method A solution (interpolated to the spectral grid), $\boldsymbol{\rho}_B$ is the Method B solution, and $\epsilon_{\mathrm{cross}} = 10^{-3}$ is the default cross-validation tolerance. This ensures that the two methods agree to within $0.1\%$ in the relative $L^2$-norm at every output time. The tolerance is set above the individual truncation errors ($O(h^2)$ for Method A, $O(e^{-cN})$ for Method B at typical resolutions) but below the $1\%$ threshold used for comparing numerical results to analytic predictions.

---

### 1.4 Time Stepping

This subsection specifies the temporal integration methods used by the simulation engine. The density equation is a stiff parabolic PDE (the diffusion term $D\,M(\rho)\nabla^2\rho$ imposes a time-step restriction $\Delta t \lesssim h^2$ for explicit methods), while the participation equation is a non-stiff ODE (its eigenvalues are $O(1/\tau)$). The time-stepping strategy treats these two components differently to avoid unnecessarily restrictive time steps while maintaining accuracy.

The three schemes — implicit Euler, Crank–Nicolson, and ETD-RK4 — correspond to increasing levels of temporal accuracy ($O(\Delta t)$, $O(\Delta t^2)$, $O(\Delta t^4)$) and are paired with the two spatial methods: implicit Euler and Crank–Nicolson with Method A (finite-difference), ETD-RK4 with Method B (spectral). The notation follows Atlas §1.5 throughout.

---

#### 1.4.1 The Semi-Implicit Strategy for Method A

The canonical ED system couples a parabolic PDE (for $\rho$) with an ODE (for $v$). The PDE contains both a linear principal part ($D\,M(\rho)\nabla^2\rho$, second-order elliptic) and nonlinear lower-order terms ($D\,M'(\rho)|\nabla\rho|^2 - D\,P(\rho) + H\,v$). The semi-implicit strategy treats these two groups differently:

- **Implicit treatment of the linear diffusion.** The term $D\,M(\rho^n)\nabla^2\rho^{n+1}$ is evaluated at the new time level $t_{n+1}$, with the mobility coefficient frozen at the current level $t_n$. This produces a linear system for $\boldsymbol{\rho}^{n+1}$ at each time step. The implicit treatment removes the parabolic CFL restriction $\Delta t \lesssim h^2/(D\,M_{\max})$, which would otherwise limit the time step to $\sim 10^{-6}$ at $N = 512$.

- **Explicit treatment of the nonlinear terms.** The terms $D\,M'(\rho^n)|\nabla\rho^n|^2$, $-D\,P(\rho^n)$, and $H\,v^n$ are evaluated at the current time level $t_n$. These terms are of lower differential order (zero and one, versus two for the Laplacian) and do not generate the severe stiffness of the diffusion. Their explicit treatment avoids the nonlinear solve that a fully implicit scheme would require.

The semi-implicit split is justified by the parabolic structure of the ED system: the stiffness resides entirely in the principal part $M(\rho)\nabla^2\rho$, and the nonlinear terms are perturbative relative to it (they are bounded by the energy estimates of Appendix C.2). The split is exact in the linear regime (where $M(\rho) = M_*$ and the nonlinear terms vanish) and introduces an $O(\Delta t)$ splitting error in the nonlinear regime, which is of the same order as the time-stepping error for implicit Euler and subdominant for Crank–Nicolson.

##### 1.4.1.1 Implicit Euler Scheme

**Algorithmic flow.** At each time step $t_n \to t_{n+1} = t_n + \Delta t$:

1. **Evaluate the explicit terms.** Compute the pointwise constitutive values $M(\rho_j^n)$, $M'(\rho_j^n)$, $P(\rho_j^n)$; the discrete gradient-squared $(|\nabla_h\rho^n|^2)_j$; and assemble the explicit right-hand-side vector:

$$
\mathbf{R}_j = \rho_j^n + \Delta t\,\bigl[D\,M'(\rho_j^n)\,(|\nabla_h\rho^n|^2)_j - D\,P(\rho_j^n) + H\,v^n\bigr].
$$

2. **Assemble the implicit matrix.** Construct the tridiagonal (1D) or banded (2D) matrix:

$$
\mathbf{A} = \mathbf{I} - \Delta t\,D\,\operatorname{diag}(M(\rho_0^n), \ldots, M(\rho_{N+1}^n))\,\mathbf{L}_h.
$$

The matrix entries are density-dependent and must be recomputed at every time step. In one dimension, $\mathbf{A}$ is tridiagonal with entries:

$$
A_{j,j} = 1 + \frac{2\Delta t\,D\,M(\rho_j^n)}{h^2}, \qquad A_{j,j\pm 1} = -\frac{\Delta t\,D\,M(\rho_j^n)}{h^2},
$$

with Neumann-modified boundary rows (the $(0,0)$ and $(N+1, N+1)$ entries use the ghost-point stencil coefficients from §1.3.1.1).

3. **Solve the linear system.** Compute $\boldsymbol{\rho}^{n+1} = \mathbf{A}^{-1}\mathbf{R}$. In one dimension, this is a tridiagonal solve (Thomas algorithm, $O(N)$ operations). In two dimensions, this is a banded solve or sparse direct solve ($O(N^2)$ operations).

4. **Advance the participation variable.** Compute $v^{n+1}$ by the exponential integrator (see §1.4.3).

**Properties.**

| Property | Value |
|----------|-------|
| Temporal order of accuracy | 1 ($O(\Delta t)$) |
| Stability in the linear diffusion | Unconditional ($L^2$-stable for any $\Delta t > 0$) |
| Stability in the nonlinear terms | Conditional (CFL constraint, §1.4.5) |
| Linear systems per step | 1 |
| Cost per step (1D) | $O(N)$ |
| Cost per step (2D) | $O(N^2)$ |

**When to use.** Implicit Euler is the most robust scheme — it never fails for stable problems — but its first-order accuracy makes it inefficient for long-time integrations where quantitative precision is needed. It is recommended for: initial exploration of a new parameter regime, transient phases with rapidly changing density (e.g., the near-horizon experiments of Atlas §6, where the mobility varies by three orders of magnitude), and convergence studies where the first-order rate provides a baseline for comparison.

##### 1.4.1.2 Crank–Nicolson Scheme

**Algorithmic flow.** The same four steps as implicit Euler, with two modifications:

1. **Explicit terms.** Same as implicit Euler.

2. **Implicit matrix.** The diffusion is averaged between time levels, so the implicit matrix uses a half-weight:

$$
\mathbf{A}_{\mathrm{CN}} = \mathbf{I} - \frac{\Delta t\,D}{2}\,\operatorname{diag}(M(\boldsymbol{\rho}^n))\,\mathbf{L}_h.
$$

A second matrix is needed for the explicit diffusion contribution:

$$
\mathbf{B}_{\mathrm{CN}} = \mathbf{I} + \frac{\Delta t\,D}{2}\,\operatorname{diag}(M(\boldsymbol{\rho}^n))\,\mathbf{L}_h.
$$

3. **Right-hand side.** The right-hand-side vector becomes:

$$
\mathbf{R}_{\mathrm{CN}} = \mathbf{B}_{\mathrm{CN}}\,\boldsymbol{\rho}^n + \Delta t\,\bigl[D\,\mathbf{G}^n - D\,\mathbf{P}^n + H\,v^n\,\mathbf{1}\bigr],
$$

where the matrix-vector product $\mathbf{B}_{\mathrm{CN}}\boldsymbol{\rho}^n$ applies the explicit half of the diffusion.

4. **Solve.** $\boldsymbol{\rho}^{n+1} = \mathbf{A}_{\mathrm{CN}}^{-1}\,\mathbf{R}_{\mathrm{CN}}$.

**Properties.**

| Property | Value |
|----------|-------|
| Temporal order of accuracy | 2 ($O(\Delta t^2)$) for the diffusion; mixed 1/2 for the nonlinear terms |
| Stability in the linear diffusion | Unconditional |
| Stability in the nonlinear terms | Conditional (CFL, §1.4.5) |
| Linear systems per step | 1 (same structure as implicit Euler) |
| Cost per step | Same as implicit Euler |

**When to use.** Crank–Nicolson is the default scheme for Method A. It provides second-order accuracy in the diffusion (the dominant stiff term) at no additional cost per step compared to implicit Euler. The explicit nonlinear terms limit the overall accuracy to first-order in the far-from-equilibrium regime, but for the linearized regime (where $M'|\nabla\rho|^2$ is second-order in the perturbation), full second-order accuracy is achieved.

**Accuracy note.** The mixed first/second-order accuracy of the Crank–Nicolson scheme in the nonlinear regime is acceptable for the Atlas experiments because (a) the nonlinear terms are subdominant to the diffusion in the dissipation identity (Lemma C.6), so their $O(\Delta t)$ error contributes only a small fraction of the total error; and (b) the quantities of interest (decay rates, frequencies, amplitude ratios) are extracted from the late-time dynamics, where the solution is in or near the linearized regime and the scheme is genuinely second-order. If full second-order accuracy is needed in the nonlinear regime, the explicit terms can be evaluated at the half-step $t_{n+1/2}$ via Richardson extrapolation: compute $\mathbf{G}^{n+1/2} = 2\mathbf{G}^n - \mathbf{G}^{n-1}$ (linear extrapolation) and use this in the right-hand side.

---

#### 1.4.2 The ETD Strategy for Method B

The spectral discretization (§1.3.2) produces a system of ODEs for the modal amplitudes:

$$
\frac{d\hat{u}_k}{dt} = c_k\,\hat{u}_k + \hat{\mathcal{N}}_k(\hat{\mathbf{u}}, v), \qquad k = 0, 1, \ldots, N-1,
$$

where $c_k = -D\,M_*\,\mu_k$ is the linear decay rate of mode $k$ and $\hat{\mathcal{N}}_k$ is the nonlinear residual computed pseudospectrally (§1.3.2.4). This system is stiff: the linear rates span $c_0 = 0$ (the constant mode) to $c_{N-1} = -D\,M_*\,(N-1)^2\pi^2/L^2$ (the highest resolved mode), a range of $\sim 10^4$ for $N = 128$ at the default parameters. An explicit Runge–Kutta method would require $\Delta t \lesssim 1/|c_{N-1}|$, which is impractically small.

The **exponential time differencing** (ETD) strategy eliminates this stiffness by integrating the linear part exactly and treating only the nonlinear part explicitly:

**Variation-of-constants formulation.** The exact solution of the $k$-th mode equation over one time step is

$$
\hat{u}_k(t_n + \Delta t) = e^{c_k\Delta t}\,\hat{u}_k(t_n) + \int_0^{\Delta t} e^{c_k(\Delta t - s)}\,\hat{\mathcal{N}}_k(t_n + s)\,ds.
$$

The first term (the homogeneous solution) is computed exactly. The second term (the particular integral) requires approximating $\hat{\mathcal{N}}_k(t_n + s)$ over the interval $[0, \Delta t]$. The ETD-RK schemes approximate this integral by evaluating $\hat{\mathcal{N}}_k$ at specific substep points and combining the evaluations with precomputed weight functions.

##### 1.4.2.1 ETD-RK2 Scheme (Second Order)

The second-order ETD Runge–Kutta scheme evaluates the nonlinearity at two points: $t_n$ and $t_n + \Delta t$.

**Substep 1.** Evaluate the nonlinearity at the current state:

$$
\hat{\mathbf{a}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^n, v^n).
$$

**Substep 2.** Compute a preliminary full step using the variation-of-constants formula with $\hat{\mathcal{N}}$ held constant at $\hat{\mathbf{a}}$:

$$
\hat{\mathbf{u}}^{*} = e^{c_k\Delta t}\,\hat{u}_k^n + \varphi_1(c_k\Delta t)\,\Delta t\,\hat{a}_k, \qquad \text{for each } k,
$$

where $\varphi_1(z) = (e^z - 1)/z$ is the first ETD weight function.

**Substep 3.** Evaluate the nonlinearity at the preliminary state:

$$
\hat{\mathbf{b}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^{*}, v^{n+1}_{\mathrm{est}}),
$$

where $v^{n+1}_{\mathrm{est}}$ is the participation variable advanced by the exponential integrator (§1.4.3).

**Combination.** The second-order update is:

$$
\hat{u}_k^{n+1} = \hat{u}_k^{*} + \frac{\Delta t}{c_k\Delta t}\bigl[(\hat{b}_k - \hat{a}_k)(e^{c_k\Delta t} - 1 - c_k\Delta t)\bigr]/(c_k\Delta t).
$$

More precisely:

$$
\hat{u}_k^{n+1} = e^{c_k\Delta t}\,\hat{u}_k^n + \Delta t\bigl[\varphi_1(c_k\Delta t)\,\hat{a}_k + \varphi_2(c_k\Delta t)\,(\hat{b}_k - \hat{a}_k)\bigr],
$$

where $\varphi_2(z) = (e^z - 1 - z)/z^2$.

**Properties.** Second-order accuracy ($O(\Delta t^2)$). Two nonlinear evaluations per step (each requiring one forward and one inverse DCT). Unconditionally stable in the linear part. The scheme is sufficient for experiments where second-order temporal accuracy matches or exceeds the spatial accuracy.

##### 1.4.2.2 ETD-RK4 Scheme (Fourth Order)

The fourth-order Cox–Matthews ETD-RK4 scheme evaluates the nonlinearity at four points (analogous to the classical RK4 stages) and combines them with precomputed weight functions.

**Stage 1.** Evaluate at $t_n$:

$$
\hat{\mathbf{a}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^n, v^n).
$$

**Stage 2.** Advance to the half-step using $\hat{\mathbf{a}}$:

$$
\hat{u}_k^{(a)} = e^{c_k\Delta t/2}\,\hat{u}_k^n + \varphi_1(c_k\Delta t/2)\,\frac{\Delta t}{2}\,\hat{a}_k.
$$

Evaluate at $t_n + \Delta t/2$:

$$
\hat{\mathbf{b}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^{(a)}, v^{n+1/2}).
$$

**Stage 3.** Advance to the half-step using $\hat{\mathbf{b}}$:

$$
\hat{u}_k^{(b)} = e^{c_k\Delta t/2}\,\hat{u}_k^n + \varphi_1(c_k\Delta t/2)\,\frac{\Delta t}{2}\,\hat{b}_k.
$$

Evaluate at $t_n + \Delta t/2$:

$$
\hat{\mathbf{c}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^{(b)}, v^{n+1/2}).
$$

**Stage 4.** Advance to the full step using $\hat{\mathbf{c}}$, starting from the Stage 2 result:

$$
\hat{u}_k^{(c)} = e^{c_k\Delta t/2}\,\hat{u}_k^{(a)} + \varphi_1(c_k\Delta t/2)\,\frac{\Delta t}{2}\,(2\hat{c}_k - \hat{a}_k).
$$

Evaluate at $t_n + \Delta t$:

$$
\hat{\mathbf{d}} = \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}^{(c)}, v^{n+1}).
$$

**Combination.** The fourth-order update is:

$$
\hat{u}_k^{n+1} = e^{c_k\Delta t}\,\hat{u}_k^n + \Delta t\,\bigl[\hat{a}_k\,\phi_{31}(z_k) + 2(\hat{b}_k + \hat{c}_k)\,\phi_{32}(z_k) + \hat{d}_k\,\phi_{33}(z_k)\bigr],
$$

where $z_k = c_k\Delta t$ and the weight functions are:

$$
\phi_{31}(z) = \frac{-4 - z + e^z(4 - 3z + z^2)}{z^3},
$$

$$
\phi_{32}(z) = \frac{2 + z + e^z(-2 + z)}{z^3},
$$

$$
\phi_{33}(z) = \frac{-4 - 3z - z^2 + e^z(4 - z)}{z^3}.
$$

**Small-argument evaluation.** For $|z_k| < 10^{-2}$ (low-$k$ modes where $c_k\Delta t$ is small), the weight functions are evaluated via their Taylor series to avoid catastrophic cancellation in the $e^z - \text{polynomial}$ numerators:

$$
\phi_{31}(z) = \frac{1}{6} + \frac{z}{6} + \frac{z^2}{12} + O(z^3),
$$

$$
\phi_{32}(z) = \frac{1}{6} + \frac{z}{12} + \frac{z^2}{30} + O(z^3),
$$

$$
\phi_{33}(z) = \frac{1}{6} + \frac{z}{4} + \frac{z^2}{10} + O(z^3).
$$

The Taylor series is used for the first three terms when $|z| < 10^{-2}$ and for the first six terms when $|z| < 10^{-6}$.

**Properties.** Fourth-order accuracy ($O(\Delta t^4)$). Four nonlinear evaluations per step (each requiring one forward and one inverse DCT pair). Unconditionally stable in the linear part. The scheme is the default for all spectral-method experiments in the Atlas.

**Precomputation.** The exponential factors $e^{c_k\Delta t}$, $e^{c_k\Delta t/2}$, the $\varphi_1$ values, and the three weight functions $\phi_{31}$, $\phi_{32}$, $\phi_{33}$ depend only on $c_k$ and $\Delta t$, both of which are constant during the integration (the linear rates $c_k = -D\,M_*\,\mu_k$ are evaluated at equilibrium and do not change). They are computed once at initialization and stored in the `SpectralData` record (§1.2.7). This precomputation eliminates all exponential and division operations from the inner time-stepping loop, reducing the per-step cost to four pseudospectral evaluations plus array multiplications and additions.

---

#### 1.4.3 Participation Variable Integration

The participation equation $\dot{v} = \tau^{-1}(\bar{F} - \zeta\,v)$ is an ODE with two terms: a driving term $\bar{F}/\tau$ (the spatially averaged operator output) and a damping term $-\zeta v/\tau$. The damping introduces a time scale $\tau/\zeta$; if $\tau/\zeta \ll \Delta t$, an explicit Euler step would be unstable.

The simulation engine uses the **exact exponential integrator** for the participation variable in all schemes:

$$
v^{n+1} = v^n\,e^{-\zeta\Delta t/\tau} + \frac{\bar{F}^n}{\zeta}\,\bigl(1 - e^{-\zeta\Delta t/\tau}\bigr).
$$

This formula is the exact solution of $\dot{v} = \tau^{-1}(\bar{F} - \zeta v)$ with $\bar{F}$ held constant at $\bar{F}^n$ over the interval $[t_n, t_{n+1}]$. It is:

- **Unconditionally stable** for any $\Delta t > 0$ and any $\zeta, \tau > 0$.
- **Exact** when $\bar{F}$ is constant (which is the case in the linearized regime, where $\bar{F} = -P_*'\bar{u}$ is slowly varying).
- **First-order accurate** in $\Delta t$ when $\bar{F}$ varies in time (the error is $O(\Delta t\,|d\bar{F}/dt|)$).

The exponential integrator is used regardless of the density time-stepping scheme (implicit Euler, Crank–Nicolson, or ETD-RK4). It adds negligible cost (two exponential evaluations per step, which are precomputed as $e^{-\zeta\Delta t/\tau}$ and $(1 - e^{-\zeta\Delta t/\tau})/\zeta$ at initialization).

For the ETD-RK4 scheme, the participation variable is also needed at the half-step $t_n + \Delta t/2$ (for Stages 2 and 3). The half-step value is:

$$
v^{n+1/2} = v^n\,e^{-\zeta\Delta t/(2\tau)} + \frac{\bar{F}^n}{\zeta}\,\bigl(1 - e^{-\zeta\Delta t/(2\tau)}\bigr).
$$

The full-step value $v^{n+1}$ is then computed from $v^n$ (not from $v^{n+1/2}$) to avoid accumulation of half-step errors.

---

#### 1.4.4 Stiffness Analysis

The ED system has a well-defined stiffness structure that determines the time-stepping requirements:

**Source of stiffness.** The stiffness resides in the linear diffusion operator $D\,M(\rho)\nabla^2$, whose eigenvalues scale as $D\,M(\rho)\,\mu_k \sim D\,M(\rho)\,k^2\pi^2/L^2$. The stiffness ratio — the ratio of the largest to the smallest resolved eigenvalue — is:

$$
\text{Stiffness ratio} = \frac{D\,M_{\max}\,\mu_{N-1}}{D\,M_{\min}\,\mu_1} = \frac{M_{\max}}{M_{\min}}\cdot(N-1)^2,
$$

where $M_{\max} = \max_j M(\rho_j)$ and $M_{\min} = \min_j M(\rho_j)$. For the default parameters ($N = 512$, $M_* = 0.25$, density in $[0.1, 0.9]$): $M_{\max}/M_{\min} \approx 0.81/0.01 = 81$, so the stiffness ratio is $\sim 81 \times 511^2 \approx 2 \times 10^7$.

An explicit method would require $\Delta t \lesssim 2/|c_{N-1}| \sim 10^{-7}$ — impractically small for integrations to $T = 50$. The semi-implicit (Method A) and ETD (Method B) strategies both eliminate this restriction:

| Scheme | Stiffness handling | Effective time-step restriction |
|--------|-------------------|-------------------------------|
| Implicit Euler | Implicit diffusion | CFL from nonlinear terms only |
| Crank–Nicolson | Implicit diffusion | CFL from nonlinear terms only |
| ETD-RK2 | Exact linear integration | CFL from nonlinear variation only |
| ETD-RK4 | Exact linear integration | CFL from nonlinear variation only |
| Exponential integrator (participation) | Exact damping | None |

**Near-horizon stiffness.** When the density approaches $\rho_{\max}$, the mobility $M(\rho) \to 0$ and the diffusion coefficient degenerates. This *reduces* the stiffness of the diffusion (the eigenvalues shrink), but it creates a different numerical difficulty: the implicit matrix $\mathbf{I} - \Delta t\,D\,\mathbf{M}^n\,\mathbf{L}_h$ approaches the identity at high-density grid points, and the equation transitions from parabolic to essentially zero-order (penalty-dominated) at those points. The semi-implicit scheme handles this gracefully — the implicit matrix remains well-conditioned because the identity contribution dominates — but the *accuracy* degrades because the diffusion that the implicit treatment is designed to resolve has become negligible. This is acceptable: in the near-horizon regime, the dynamics are penalty-driven (§6.1 of the Atlas), and the time-step restriction comes from the explicit penalty term, not from the diffusion.

**Participation stiffness.** The participation equation has eigenvalue $-\zeta/\tau$. For Parameter Set V ($\zeta = 0.3$, $\tau = 0.5$), this gives $|\zeta/\tau| = 0.6$, which is mild. For hypothetical extreme parameters ($\zeta = 10$, $\tau = 0.01$), the eigenvalue would be $-1000$, creating stiffness. The exponential integrator handles this case exactly, regardless of $\Delta t$.

---

#### 1.4.5 Time-Step Selection Strategy

The time step $\Delta t$ is determined by the competition between accuracy requirements, stability requirements, and computational cost. The engine uses a two-phase strategy:

**Phase 1: Initial selection.** At initialization (before the first time step), the time step is set to the minimum of three constraints:

1. **CFL constraint for explicit nonlinear terms.** The explicit treatment of $M'(\rho)|\nabla\rho|^2$ and $P(\rho)$ introduces a stability restriction. The dominant explicit term is the gradient-squared nonlinearity, which has an effective advection speed $\sim D\,|M'(\rho)|\,|\nabla\rho|$. The CFL condition is:

$$
\Delta t_{\mathrm{CFL}} = C_{\mathrm{CFL}} \cdot \frac{h^2}{D\,\max_j|M'(\rho_j)|\cdot\max_j|(\nabla_h\rho)_j|\cdot h + D\,\max_j M(\rho_j)},
$$

with safety factor $C_{\mathrm{CFL}} = 0.5$. The denominator combines the nonlinear advection speed (first term) and the residual explicit diffusion (second term, which arises from the density-dependent variation of $M(\rho)$ around its frozen value $M(\rho^n)$ in the implicit matrix).

2. **ODE stability constraint.** When explicit Euler is used for the participation equation (rather than the exponential integrator):

$$
\Delta t_{\mathrm{ODE}} = \frac{2\tau}{\zeta}.
$$

This constraint is automatically satisfied when the exponential integrator is used (which is the default).

3. **User-specified maximum.** $\Delta t_{\mathrm{user}}$ is set by the experiment specification (Atlas §10.2.5).

The initial time step is $\Delta t = \min(\Delta t_{\mathrm{CFL}}, \Delta t_{\mathrm{ODE}}, \Delta t_{\mathrm{user}})$.

**Phase 2: Adaptive adjustment during integration.** The time step is held constant during the integration unless the mobility-collapse protocol (Atlas §1.6) is activated. When the proximity margin $\delta^n = \rho_{\max} - \max_j\rho_j^n$ drops below $\delta_{\mathrm{crit}} = 10^{-4}\rho_{\max}$, the time step is reduced by:

$$
\Delta t \leftarrow \Delta t \cdot \min\!\left(1,\;\frac{\delta^n}{\delta_{\mathrm{crit}}}\right).
$$

The time step is restored to its initial value once $\delta^n > 2\delta_{\mathrm{crit}}$. This adaptive reduction prevents the explicit terms from driving $\rho$ past $\rho_{\max}$ in a single step.

**No global adaptivity.** The engine does not use global error-based adaptivity (embedded Runge–Kutta pairs, Richardson extrapolation with step-size control, etc.). This is a deliberate choice: the Atlas experiments are designed with fixed time steps that satisfy the CFL constraint throughout the integration, and the convergence studies of §1.7.1 verify that the results are converged at the chosen resolution. Global adaptivity would add complexity without improving the Atlas results, and it would complicate the reproducibility standard (the output would depend on the adaptive tolerances). Implementations that wish to use adaptive time stepping for exploratory computations outside the Atlas are free to do so, but the Atlas results must be reproduced with fixed time steps.

**Time-step summary by scheme.**

| Scheme | Default $\Delta t$ | Restriction source | Adaptivity |
|--------|-------------------|-------------------|------------|
| Implicit Euler (Method A) | $5 \times 10^{-4}$ | CFL (nonlinear explicit terms) | Near-horizon only |
| Crank–Nicolson (Method A) | $5 \times 10^{-4}$ | CFL (nonlinear explicit terms) | Near-horizon only |
| ETD-RK4 (Method B) | $10^{-4}$ | Nonlinear variation rate | Near-horizon only |
| Exponential integrator ($v$) | Same as density | None (unconditionally stable) | None |

The ETD-RK4 default is smaller than the Method A default because the spectral experiments (modal analysis, triad coupling) require higher temporal accuracy to resolve the fast modal dynamics, not because of a stability limitation.

---

### 1.5 Boundary Conditions

The canonical ED system is posed on a bounded domain $\Omega \subset \mathbb{R}^d$ with Neumann (no-flux) boundary conditions:

$$
\partial_\nu\rho\big|_{\partial\Omega} = 0,
$$

where $\partial_\nu$ denotes the outward normal derivative on $\partial\Omega$. This is the boundary condition assumed throughout Appendix C (§C.1.1), the Numerical Atlas (§1.2), and all 55 experiments of the Atlas. The Neumann condition is not an arbitrary choice — it is the unique boundary condition consistent with the structural requirements of the ED architecture:

- **Principle 3** (Penalty Equilibrium) requires that $\rho^*$ is a spatially constant equilibrium. A spatially constant function satisfies $\partial_\nu\rho = 0$ on any domain, so Neumann conditions are the natural compatibility condition for constant equilibria.
- **Appendix C.2** (Global Existence) uses the Neumann condition in two essential places: the integration-by-parts identity $\int_\Omega P(\rho)\nabla^2\rho\,dx = -\int_\Omega P'(\rho)|\nabla\rho|^2\,dx$ (Lemma C.6, which eliminates the boundary term $\int_{\partial\Omega}P(\rho)\partial_\nu\rho\,dS = 0$), and the Poincaré–Wirtinger inequality $\|\rho - \bar{\rho}\|_{L^2}^2 \leq C_\Omega\|\nabla\rho\|_{L^2}^2$ (Proposition C.8, valid for functions with zero normal derivative on $\partial\Omega$).
- **Appendix C.3** (Eigenstructure) uses the Neumann eigenbasis $\{\varphi_n\}$ with $\partial_\nu\varphi_n = 0$, which is the foundation of the modal decomposition, the spectral gap, and the triad selection rule.
- **Appendix C.7** (Long-Time Behavior) uses $\int_\Omega\nabla^2\rho\,dx = 0$ (the divergence theorem with $\partial_\nu\rho = 0$) to derive the mass evolution equation and the Barbalat-lemma argument for gradient decay.

Replacing Neumann with Dirichlet, Robin, or periodic conditions would invalidate specific steps in these proofs (the boundary terms would not vanish, the eigenbasis would change, the Poincaré constant would differ). The simulation engine enforces Neumann conditions as the default and only supported boundary type for the canonical system.

---

#### 1.5.1 Ghost-Point Reflection (Method A)

The finite-difference method (§1.3.1) implements the Neumann condition through ghost-point reflection. The logic is as follows.

##### 1.5.1.1 The Ghost-Point Principle

The Neumann condition $\partial_\nu\rho = 0$ at a boundary point $x_b$ states that the density profile is symmetric about $x_b$ to first order:

$$
\rho(x_b - s) = \rho(x_b + s) + O(s^2) \qquad \text{for small } s > 0.
$$

In the discrete setting, this symmetry is enforced exactly by defining a ghost value at the fictitious grid point one step outside the domain:

$$
\rho_{\mathrm{ghost}} := \rho_{\mathrm{mirror}},
$$

where $\rho_{\mathrm{mirror}}$ is the grid value at the mirror point (one step inside the domain from $x_b$). This reflection ensures that the centered-difference approximation to $\partial_x\rho$ at $x_b$ is exactly zero:

$$
(\nabla_h\rho)_b = \frac{\rho_{\mathrm{mirror}} - \rho_{\mathrm{ghost}}}{2h} = \frac{\rho_{\mathrm{mirror}} - \rho_{\mathrm{mirror}}}{2h} = 0.
$$

##### 1.5.1.2 One-Dimensional Implementation

On $\Omega_1 = [0, L]$ with grid points $x_j = jh$, $j = 0, 1, \ldots, N+1$:

**Left boundary ($j = 0$, $x = 0$).** The ghost point is at $x_{-1} = -h$. The reflection is $\rho_{-1} := \rho_1$. The Laplacian stencil at $j = 0$ becomes:

$$
(\nabla_h^2\rho)_0 = \frac{\rho_{-1} - 2\rho_0 + \rho_1}{h^2} = \frac{\rho_1 - 2\rho_0 + \rho_1}{h^2} = \frac{2(\rho_1 - \rho_0)}{h^2}.
$$

The gradient at $j = 0$ is:

$$
(\nabla_h\rho)_0 = \frac{\rho_1 - \rho_{-1}}{2h} = \frac{\rho_1 - \rho_1}{2h} = 0.
$$

The gradient-squared at $j = 0$ is therefore $(|\nabla_h\rho|^2)_0 = 0$.

**Right boundary ($j = N+1$, $x = L$).** The ghost point is at $x_{N+2} = L + h$. The reflection is $\rho_{N+2} := \rho_N$. The Laplacian and gradient follow by symmetry:

$$
(\nabla_h^2\rho)_{N+1} = \frac{2(\rho_N - \rho_{N+1})}{h^2}, \qquad (\nabla_h\rho)_{N+1} = 0, \qquad (|\nabla_h\rho|^2)_{N+1} = 0.
$$

**Implementation logic.** The ghost-point reflection is not stored as additional array elements. Instead, the boundary stencils are implemented as special cases within the Laplacian and gradient evaluation routines:

- When computing $(\nabla_h^2\rho)_j$ for $j = 0$: use the formula $2(\rho_1 - \rho_0)/h^2$ directly, without accessing $\rho_{-1}$.
- When computing $(\nabla_h^2\rho)_j$ for $j = N+1$: use the formula $2(\rho_N - \rho_{N+1})/h^2$ directly, without accessing $\rho_{N+2}$.
- When computing $(|\nabla_h\rho|^2)_j$ for $j = 0$ or $j = N+1$: set the value to $0$ directly, without evaluating the stencil.

This avoids the need for ghost-point storage (the density array has exactly $N_{\mathrm{grid}} = N + 2$ elements, not $N + 4$) and eliminates the risk of ghost values becoming stale if the boundary update is accidentally omitted.

An alternative implementation stores the ghost values as the first and last elements of an extended array of size $N + 4$ and updates them by copying $\rho_1 \to \rho_{-1}$ and $\rho_N \to \rho_{N+2}$ at the beginning of each time step. This approach is equally correct but requires the discipline of updating the ghost values before every stencil evaluation. The Suite permits either approach; the structural tests of §1.3.1.4 verify the correctness regardless of the implementation strategy.

##### 1.5.1.3 Two-Dimensional Implementation

On $\Omega_2 = [0, L_x] \times [0, L_y]$ with grid points $(x_i, y_j)$, the Neumann condition applies on all four edges:

| Edge | Location | Ghost-point rule |
|------|----------|-----------------|
| Left ($i = 0$) | $x = 0$ | $\rho_{-1, j} := \rho_{1, j}$ for all $j$ |
| Right ($i = N_x + 1$) | $x = L_x$ | $\rho_{N_x+2, j} := \rho_{N_x, j}$ for all $j$ |
| Bottom ($j = 0$) | $y = 0$ | $\rho_{i, -1} := \rho_{i, 1}$ for all $i$ |
| Top ($j = N_y + 1$) | $y = L_y$ | $\rho_{i, N_y+2} := \rho_{i, N_y}$ for all $i$ |

**Corners.** At corner points (e.g., $(i, j) = (0, 0)$), the five-point Laplacian stencil requires $\rho_{-1, 0}$ and $\rho_{0, -1}$. These are obtained by applying the reflection in each direction independently:

$$
\rho_{-1, 0} = \rho_{1, 0}, \qquad \rho_{0, -1} = \rho_{0, 1}.
$$

The diagonal ghost point $\rho_{-1, -1}$ is not needed by the five-point stencil (it would be needed by a nine-point stencil, which the Suite does not use). The Laplacian at the corner $(0, 0)$ is:

$$
(\nabla_h^2\rho)_{0,0} = \frac{2(\rho_{1,0} - \rho_{0,0})}{h_x^2} + \frac{2(\rho_{0,1} - \rho_{0,0})}{h_y^2}.
$$

The gradient-squared at all boundary points has the normal component set to zero and the tangential component computed by the standard centered difference (the tangential derivative is not constrained by the Neumann condition). Explicitly, on the left edge ($i = 0$):

$$
(|\nabla_h\rho|^2)_{0, j} = 0 + \left(\frac{\rho_{0, j+1} - \rho_{0, j-1}}{2h_y}\right)^2.
$$

The normal component vanishes; the tangential component is computed normally. At corners, both components may be constrained (e.g., at $(0, 0)$, both the $x$- and $y$-normal derivatives vanish), giving $(|\nabla_h\rho|^2)_{0,0} = 0$.

##### 1.5.1.4 Three-Dimensional Implementation

The extension to $\Omega_3$ follows the same pattern: ghost-point reflection on each of the six faces, with edges and corners handled by applying reflections in each affected direction independently. The seven-point Laplacian stencil requires at most one ghost point per direction, so no diagonal ghost points are needed.

##### 1.5.1.5 Implicit Matrix Modification

The Neumann boundary conditions modify the implicit matrix $\mathbf{A} = \mathbf{I} - \Delta t\,D\,\operatorname{diag}(\mathbf{M})\,\mathbf{L}_h$ at the boundary rows. In one dimension:

**Row $j = 0$ (left boundary).** The ghost-point Laplacian $(\nabla_h^2\rho)_0 = 2(\rho_1 - \rho_0)/h^2$ corresponds to the matrix entries:

$$
(\mathbf{L}_h)_{0,0} = -\frac{2}{h^2}, \qquad (\mathbf{L}_h)_{0,1} = \frac{2}{h^2}, \qquad (\mathbf{L}_h)_{0,j} = 0 \text{ for } j \geq 2.
$$

The implicit matrix row becomes:

$$
A_{0,0} = 1 + \frac{2\Delta t\,D\,M(\rho_0)}{h^2}, \qquad A_{0,1} = -\frac{2\Delta t\,D\,M(\rho_0)}{h^2}.
$$

Note the factor of $2$ (compared to $1$ for interior rows). This asymmetry is a consequence of the ghost-point reflection and must be implemented correctly; an error here breaks the symmetry of $\mathbf{L}_h$ and corrupts the energy identity.

**Row $j = N+1$ (right boundary).** By symmetry:

$$
A_{N+1, N} = -\frac{2\Delta t\,D\,M(\rho_{N+1})}{h^2}, \qquad A_{N+1, N+1} = 1 + \frac{2\Delta t\,D\,M(\rho_{N+1})}{h^2}.
$$

**Verification.** The symmetry of the modified Laplacian $\mathbf{L}_h$ (with the factor-of-$2$ boundary entries) is verified by the structural test in §1.3.1.4: $\|\mathbf{L}_h - \mathbf{L}_h^\top\|_\infty < 10^{-14}$. If this test fails, the boundary implementation is incorrect.

---

#### 1.5.2 Spectral Boundary Handling (Method B)

The spectral method (§1.3.2) handles the Neumann boundary condition through the choice of basis functions. The mechanism is fundamentally different from ghost-point reflection: instead of modifying the stencil at the boundary, the boundary condition is encoded in the function space itself.

##### 1.5.2.1 Built-In Boundary Satisfaction

The Neumann eigenfunctions $\phi_k(x) = c_k\cos(k\pi x/L)$ satisfy $\partial_x\phi_k(0) = 0$ and $\partial_x\phi_k(L) = 0$ for every $k$:

$$
\phi_k'(x) = -c_k\,\frac{k\pi}{L}\sin\!\left(\frac{k\pi x}{L}\right), \qquad \phi_k'(0) = 0, \qquad \phi_k'(L) = -c_k\,\frac{k\pi}{L}\sin(k\pi) = 0.
$$

Any function in the span of $\{\phi_k\}$ — that is, any function representable as $\rho(x) = \sum_k\hat{\rho}_k\phi_k(x)$ — automatically satisfies the Neumann condition at both endpoints. The boundary condition is therefore *exactly* satisfied at every truncation level $N$, with no approximation error and no special boundary treatment.

This is the spectral method's primary advantage for the ED system: the boundary condition cannot be violated by numerical error, truncation, aliasing, or any other discretization artifact. The density field is, at every instant, a member of the Neumann function space.

##### 1.5.2.2 The Discrete Cosine Transform and Boundary Conditions

The forward DCT-I, which computes the spectral coefficients from the physical-space values, assumes that the input function satisfies the Neumann condition. Specifically, the DCT-I of a sequence $\{f_0, f_1, \ldots, f_{N-1}\}$ computes the coefficients in the expansion $f(x) = \sum_k\hat{f}_k\cos(k\pi x/L)$, where the cosine basis automatically imposes zero derivative at $x = 0$ and $x = L$.

If the physical-space values $\rho_j$ are obtained from a function that does *not* satisfy the Neumann condition (e.g., during initialization with a test function that has nonzero boundary gradient), the DCT will project the function onto the Neumann subspace, discarding the non-Neumann component. This is the correct behavior: the Neumann condition is enforced by the basis, not by the data.

**Consequence for initialization.** When the initial condition $\rho_0(x)$ is specified as a closed-form function (e.g., IC-C: a Gaussian), it may not exactly satisfy $\partial_x\rho_0(0) = 0$ and $\partial_x\rho_0(L) = 0$. The spectral method automatically projects $\rho_0$ onto the Neumann basis, which is equivalent to symmetrically extending the initial condition and retaining only the even (cosine) Fourier components. For the standard initial conditions of the Atlas (IC-A through IC-D), all are pure cosine functions and already satisfy the Neumann condition exactly, so no projection is needed.

##### 1.5.2.3 Pseudospectral Consistency

During the pseudospectral evaluation of nonlinear terms (§1.3.2.4), the density is transformed to physical space, the nonlinearity is evaluated pointwise, and the result is transformed back to spectral space. The physical-space grid points $x_j = jL/N_{\mathrm{phys}}$ include the endpoints $x_0 = 0$ and $x_{N_{\mathrm{phys}}-1} = L(1 - 1/N_{\mathrm{phys}})$ (for the standard DCT-I grid).

The nonlinear evaluation preserves the Neumann condition in the following sense: because the input $\rho(x_j)$ is a cosine expansion (even function about $x = 0$ and $x = L$), the nonlinear function $\mathcal{N}(\rho(x_j), \nabla^2\rho(x_j), |\nabla\rho(x_j)|^2)$ is also an even function about the endpoints (since even functions of even functions are even), and its DCT produces only cosine coefficients. The Neumann condition is therefore preserved through the pseudospectral evaluation without any explicit enforcement.

The gradient $\partial_x\rho$, computed as a sine expansion (§1.3.2.3), is an *odd* function about the endpoints. Its square $|\nabla\rho|^2 = (\partial_x\rho)^2$ is *even* (the square of an odd function is even), so it has a pure cosine expansion and is Neumann-compatible. The product $M'(\rho)\,|\nabla\rho|^2$ is even times even = even, also Neumann-compatible.

##### 1.5.2.4 Two-Dimensional Extension

On $\Omega_2 = [0, L_x] \times [0, L_y]$, the tensor-product basis $\phi_{k_1}(x)\,\phi_{k_2}(y) = c_{k_1}c_{k_2}\cos(k_1\pi x/L_x)\cos(k_2\pi y/L_y)$ satisfies $\partial_x\phi = 0$ at $x = 0, L_x$ and $\partial_y\phi = 0$ at $y = 0, L_y$ for every $(k_1, k_2)$. The 2D DCT (computed as sequential 1D DCTs along each axis) inherits the Neumann property in both directions. No special treatment is needed at corners.

---

#### 1.5.3 Consistency with Appendix C

The Neumann boundary condition enters the analytic theory at specific, identifiable points. The simulation engine must preserve the discrete analogues of these identities; failure to do so would invalidate the correspondence between the numerical results and the theorems they are intended to demonstrate.

##### 1.5.3.1 The Integration-by-Parts Identity

**Continuous form.** For smooth $\rho$ on $\Omega$ with $\partial_\nu\rho = 0$ on $\partial\Omega$:

$$
\int_\Omega P(\rho)\,\nabla^2\rho\,dx = -\int_\Omega P'(\rho)\,|\nabla\rho|^2\,dx.
$$

This identity is used in the proof of the energy dissipation bound (Lemma C.6). The boundary term $\int_{\partial\Omega}P(\rho)\,\partial_\nu\rho\,dS$ vanishes because $\partial_\nu\rho = 0$.

**Discrete form (Method A).** The discrete analogue is:

$$
h\sum_{j=0}^{N+1} P(\rho_j)\,(\nabla_h^2\rho)_j = -h\sum_{j=0}^{N+1} P'(\rho_j)\,(|\nabla_h\rho|^2)_j + O(h^2).
$$

This identity holds to second-order accuracy because both the discrete Laplacian and the discrete gradient-squared are second-order approximations, and the boundary terms cancel by the ghost-point construction ($(\nabla_h\rho)_0 = (\nabla_h\rho)_{N+1} = 0$). The identity is verified numerically as part of the energy dissipation test (Atlas §1.7.2): the discrete dissipation-identity residual must be $O(\Delta t^p + h^2)$.

**Discrete form (Method B).** In spectral space, the identity is exact: the Laplacian eigenvalues $-\mu_k$ and the $L^2$-inner products of the basis functions encode the integration by parts exactly (Parseval's identity). No approximation is involved.

##### 1.5.3.2 The Divergence-Theorem Identity

**Continuous form.** For the spatial mean:

$$
\frac{d}{dt}\int_\Omega\rho\,dx = \int_\Omega\partial_t\rho\,dx = D\int_\Omega F[\rho]\,dx + H\,v\,|\Omega|.
$$

The diffusion term $\int_\Omega M(\rho)\nabla^2\rho\,dx = \int_{\partial\Omega}M(\rho)\,\partial_\nu\rho\,dS = 0$ by the Neumann condition. Therefore $\int_\Omega F[\rho]\,dx = \int_\Omega(M'(\rho)|\nabla\rho|^2 - P(\rho))\,dx$, and the mass evolution is:

$$
\frac{d\bar{\rho}}{dt} = D\,\overline{M'(\rho)|\nabla\rho|^2 - P(\rho)} + H\,v.
$$

This identity is used in the mass conservation test (Atlas §1.7.3) and in the proof of the $\omega$-limit identification (Theorem C.70, Step 2).

**Discrete form.** The discrete divergence-theorem identity $h\sum_j(\nabla_h^2\rho)_j = 0$ must hold for any density array. This is guaranteed by the structure of $\mathbf{L}_h$: the column sums of $\mathbf{L}_h$ are all zero (equivalent to $\mathbf{1}^\top\mathbf{L}_h = \mathbf{0}^\top$, the left null-space property), which is in turn guaranteed by the ghost-point construction. The identity is verified by the null-space test in §1.3.1.4: $\|\mathbf{L}_h\mathbf{1}\|_\infty < 10^{-14}$.

##### 1.5.3.3 The Poincaré–Wirtinger Inequality

**Continuous form.** For $\rho \in H^1(\Omega)$ with $\partial_\nu\rho = 0$:

$$
\|\rho - \bar{\rho}\|_{L^2(\Omega)}^2 \leq C_\Omega\,\|\nabla\rho\|_{L^2(\Omega)}^2,
$$

where $C_\Omega = 1/\mu_1$ is the Poincaré constant (the reciprocal of the first nonzero Neumann eigenvalue). This inequality is used in Proposition C.8 (penalty-driven energy decay) and in the stability analysis (Theorem C.43).

**Discrete form.** The discrete Poincaré inequality $\|\boldsymbol{\rho} - \bar{\rho}\mathbf{1}\|^2 \leq C_h\,\|\nabla_h\boldsymbol{\rho}\|^2$ holds with a constant $C_h$ that converges to $C_\Omega = L^2/\pi^2$ as $h \to 0$. The discrete constant is $C_h = 1/\mu_1^h$, where $\mu_1^h = (2/h^2)(1 - \cos(\pi h/L))$ is the smallest nonzero eigenvalue of $-\mathbf{L}_h$. For $h \ll L$, $\mu_1^h \approx \mu_1(1 - \pi^2 h^2/(12L^2))$, so $C_h \approx C_\Omega(1 + O(h^2))$.

The discrete Poincaré constant is not used explicitly by the simulation engine, but it determines the effective spectral gap at finite resolution. Implementations that wish to compute the discrete spectral gap (e.g., for comparison with the analytic prediction of Corollary C.18) should use $\mu_1^h$ rather than $\mu_1$.

##### 1.5.3.4 Summary of Boundary-Dependent Identities

| Identity | Continuous form | Where used in Appendix C | Discrete preservation |
|----------|----------------|-------------------------|-----------------------|
| Integration by parts | $\int P\nabla^2\rho = -\int P'|\nabla\rho|^2$ | Lemma C.6 (energy dissipation) | Method A: $O(h^2)$. Method B: exact. |
| Divergence theorem | $\int\nabla^2\rho = 0$ | Theorem C.70 (mass, $\omega$-limit) | Method A: machine precision. Method B: exact. |
| Poincaré–Wirtinger | $\|\rho - \bar{\rho}\|^2 \leq C_\Omega\|\nabla\rho\|^2$ | Proposition C.8, Theorem C.43 | Method A: $C_h \to C_\Omega$ as $h \to 0$. Method B: exact. |
| Eigenfunction orthonormality | $\langle\varphi_m, \varphi_n\rangle = \delta_{mn}$ | Theorem C.17 (modal decomposition) | Method A: post-hoc DCT. Method B: exact. |
| Vanishing boundary gradient | $\partial_\nu\rho = 0$ on $\partial\Omega$ | Passim | Method A: ghost-point ($=0$ to machine precision). Method B: built into basis. |

The table confirms that every boundary-dependent identity from Appendix C is preserved by both discretization methods — exactly for Method B, to second-order accuracy (or machine precision for algebraic identities) for Method A. The simulation engine's boundary implementation is validated when all five identities in the table are confirmed by the corresponding structural tests.

---

### 1.6 Handling Mobility Collapse

The mobility function $M(\rho)$ vanishes at $\rho = \rho_{\max}$ (Principle 4). This vanishing is not a defect — it is an essential structural feature that creates the energy barrier (Proposition C.11), suppresses near-horizon gradients (Proposition C.10), and prevents the density from reaching the capacity bound (Theorem C.66(i)). But it presents a numerical challenge: as $\rho$ approaches $\rho_{\max}$ at any grid point, the diffusion coefficient $D\,M(\rho)$ approaches zero, and the equation transitions from uniformly parabolic to degenerate. The simulation engine must handle this transition without producing numerical artifacts, without violating the structural invariants of the PDE, and without masking the genuine physical content of the mobility collapse.

This subsection specifies the complete protocol for detecting, managing, and verifying the near-horizon dynamics. The protocol has four layers: proximity monitoring (§1.6.1), adaptive time-step control (§1.6.2), state projection (§1.6.3), and energy-barrier verification (§1.6.4). The layers are ordered by severity — each activates only when the previous layer's intervention is insufficient.

---

#### 1.6.1 Proximity Monitoring

At every time step, the engine computes the **proximity margin**:

$$
\delta^n := \rho_{\max} - \max_{j}\,\rho_j^n.
$$

This is the minimum distance between the current density field and the capacity bound, measured at the grid-point level. It is the single scalar diagnostic that governs all subsequent mobility-collapse interventions.

**Threshold levels.** The protocol defines three threshold levels:

| Level | Symbol | Default value | Meaning |
|-------|--------|--------------|---------|
| Normal | $\delta > \delta_{\mathrm{warn}}$ | $\delta_{\mathrm{warn}} = 0.01\,\rho_{\max}$ | No intervention; standard time stepping |
| Warning | $\delta_{\mathrm{crit}} < \delta \leq \delta_{\mathrm{warn}}$ | | Log diagnostic; no action |
| Critical | $\delta \leq \delta_{\mathrm{crit}}$ | $\delta_{\mathrm{crit}} = 10^{-4}\,\rho_{\max}$ | Activate adaptive time-step reduction |

The thresholds are expressed as fractions of $\rho_{\max}$ rather than absolute values, so they scale correctly when $\rho_{\max}$ is changed (e.g., in constitutive surveys).

**Monitoring cost.** Computing $\delta^n$ requires a single pass over the density array to find its maximum, followed by one subtraction. The cost is $O(N_{\mathrm{grid}})$ — negligible compared to the $O(N_{\mathrm{grid}})$ cost of the stencil evaluation or the $O(N_{\mathrm{grid}}\log N_{\mathrm{grid}})$ cost of the DCT. The monitoring is performed unconditionally at every time step, regardless of the current proximity level, because the density can approach $\rho_{\max}$ from any direction without warning (e.g., the mediated channel $Hv$ can inject density uniformly, pushing the peak closer to $\rho_{\max}$).

**Diagnostic logging.** When $\delta^n$ enters the warning zone ($\delta^n \leq \delta_{\mathrm{warn}}$), the engine records a diagnostic entry:

```
RECORD ProximityDiagnostic:
    time_step  : Int          // step number n
    time       : Float64      // current time t_n
    delta      : Float64      // proximity margin
    j_max      : Int          // grid index of maximum density
    rho_max_val: Float64      // value of max(ρ)
    M_min      : Float64      // M(max(ρ)), the minimum mobility
    energy     : Float64      // current energy E[ρ, v]
```

The diagnostic log is written to the output stream and is available for post-hoc analysis. It does not affect the computation.

---

#### 1.6.2 Adaptive Time-Step Reduction

When the proximity margin enters the critical zone ($\delta^n \leq \delta_{\mathrm{crit}}$), the time step is reduced to prevent the explicit nonlinear terms from driving $\rho$ past $\rho_{\max}$ in a single step.

**Reduction rule.** The time step is scaled by the ratio of the current margin to the critical threshold:

$$
\Delta t^{n+1} \leftarrow \Delta t_0 \cdot \min\!\left(1,\;\frac{\delta^n}{\delta_{\mathrm{crit}}}\right),
$$

where $\Delta t_0$ is the nominal time step (the initial value from §1.4.5). This rule has three properties:

1. **Proportionality.** The reduction is proportional to the margin. When $\delta^n = \delta_{\mathrm{crit}}$, the time step is unchanged. When $\delta^n = \delta_{\mathrm{crit}}/2$, the time step is halved. When $\delta^n = \delta_{\mathrm{crit}}/10$, the time step is reduced by a factor of 10. This ensures that the explicit step size scales with the available room before $\rho_{\max}$.

2. **Smoothness.** The reduction is a continuous function of $\delta^n$, so it does not introduce discontinuous jumps in the time step (which could excite spurious transients in the solution).

3. **Automatic recovery.** The reduction is relative to $\Delta t_0$, not to the previous $\Delta t^n$. When $\delta^n > \delta_{\mathrm{crit}}$, the time step immediately returns to $\Delta t_0$ (or the CFL-limited value, whichever is smaller). There is no hysteresis and no gradual ramp-up.

**Recovery with hysteresis band.** To prevent rapid oscillation of the time step when $\delta^n$ fluctuates near $\delta_{\mathrm{crit}}$, the recovery to $\Delta t_0$ is delayed until $\delta^n > 2\,\delta_{\mathrm{crit}}$. Between $\delta_{\mathrm{crit}}$ and $2\,\delta_{\mathrm{crit}}$, the time step remains at its reduced value. This introduces a narrow hysteresis band that smooths the transition.

**Interaction with the CFL constraint.** The adaptive reduction applies *after* the CFL constraint (§1.4.5): the effective time step is $\min(\Delta t_{\mathrm{CFL}}, \Delta t_{\mathrm{adaptive}})$. In practice, when $\delta^n$ is small, the CFL constraint may already produce a small time step (because $M'(\rho)$ grows as $\rho \to \rho_{\max}$ for sub-linear $\beta$, increasing the effective advection speed). The adaptive reduction provides an additional safety layer beyond the CFL.

**Maximum reduction factor.** The time step is never reduced below $\Delta t_{\min} = 10^{-8}$. If the adaptive rule would produce $\Delta t < \Delta t_{\min}$, the engine halts with a diagnostic message indicating that the density is too close to $\rho_{\max}$ for stable integration at the current resolution. This situation should not arise for initial conditions with finite energy (Proposition C.11 guarantees a positive margin $\delta > 0$), but it can occur if the initial condition is ill-posed (e.g., $\rho_0(x) > \rho_{\max}$ at some point) or if the resolution is insufficient to resolve the near-horizon boundary layer.

---

#### 1.6.3 State Projection

If, after the implicit solve and explicit update, any grid value violates the physical bounds, the engine applies a **projection** to restore the state to the admissible region $(0, \rho_{\max})$.

**Upper projection.** If $\rho_j^{n+1} \geq \rho_{\max}$ for any $j$:

$$
\rho_j^{n+1} \leftarrow \rho_{\max} - \delta_{\mathrm{floor}}, \qquad \delta_{\mathrm{floor}} = 10^{-12}.
$$

**Lower projection.** If $\rho_j^{n+1} \leq 0$ for any $j$:

$$
\rho_j^{n+1} \leftarrow \delta_{\mathrm{floor}}.
$$

**Post-projection actions.** After any projection:

1. **Energy recomputation.** The energy $\mathcal{E}[\boldsymbol{\rho}^{n+1}, v^{n+1}]$ is recomputed from the projected state. The projection modifies the density, which changes the energy; the recomputed value is the one recorded in the observable output.

2. **Diagnostic flag.** A projection event is logged:

```
RECORD ProjectionEvent:
    time_step   : Int
    time        : Float64
    n_upper     : Int        // number of grid points projected from above
    n_lower     : Int        // number of grid points projected from below
    max_violation : Float64  // max(ρ_j − ρ_max) or max(−ρ_j), before projection
    energy_before : Float64
    energy_after  : Float64
```

3. **Convergence flag.** If projection is activated at any time step during a converged run (one that has passed the convergence study of Atlas §1.7.1), the result is flagged as potentially compromised. The projection is a safety net, not a regularization; at converged resolutions, it should never be activated. If it is, the resolution is insufficient or the time step is too large.

**Structural interpretation.** The projection is *not* part of the ED dynamics. It is a numerical safeguard that prevents floating-point overflow (from evaluating $M(\rho)$ at $\rho > \rho_{\max}$, where $(\rho_{\max} - \rho)^\beta$ would be imaginary for non-integer $\beta$, or negative for even $\beta$). The analytic theory guarantees that $\rho(x, t) \in (0, \rho_{\max})$ for all time (Theorem C.2); the projection enforces this guarantee at the discrete level when the time-stepping error would violate it.

The projection introduces an $O(\delta_{\mathrm{floor}})$ perturbation to the density at the affected grid points. Since $\delta_{\mathrm{floor}} = 10^{-12}$ is far below the double-precision unit roundoff $\epsilon_{\mathrm{mach}} \approx 10^{-16}$ scaled by $\rho_{\max}$ (i.e., $\delta_{\mathrm{floor}} \gg \epsilon_{\mathrm{mach}}\rho_{\max} \approx 10^{-16}$ but $\delta_{\mathrm{floor}} \ll$ any physically meaningful density scale), the perturbation is negligible. The projection does not introduce a systematic bias because it is symmetric (both upper and lower bounds are enforced) and because the energy barrier ensures that $\rho$ spends negligible time near the bounds.

---

#### 1.6.4 Energy-Barrier Verification

The analytic energy barrier (Proposition C.11) states that the sublevel set $\{\mathcal{E} \leq E_0\}$ is contained in $\{\rho(x) \leq \rho_{\max} - \delta(E_0)\}$ for some $\delta(E_0) > 0$. This is the structural guarantee that the density cannot reach $\rho_{\max}$ when the energy is finite. The simulation engine verifies this guarantee at runtime.

**Barrier check.** At each time step (or at each output time, if per-step checking is too costly for the 2D/3D cases), the engine computes:

1. The current energy $\mathcal{E}^n$.
2. The current proximity margin $\delta^n$.
3. The barrier prediction: the value $\delta_{\mathrm{barrier}}(E_0)$ obtained by inverting the potential divergence.

For the canonical constitutive functions ($M(\rho) = M_0(\rho_{\max} - \rho)^\beta$, $P(\rho) = P_0(\rho - \rho^*)$) with $\beta = 2$:

$$
\Phi(\rho) = \int_{\rho^*}^{\rho}\frac{P_0(r - \rho^*)}{M_0(\rho_{\max} - r)^2}\,dr.
$$

For $\rho$ close to $\rho_{\max}$:

$$
\Phi(\rho) \approx \frac{P_0(\rho_{\max} - \rho^*)}{M_0(\rho_{\max} - \rho)}.
$$

The barrier prediction is obtained by requiring $|\Omega|\,\Phi(\rho_{\max} - \delta) \leq \mathcal{E}^n$:

$$
\delta_{\mathrm{barrier}} \approx \frac{P_0(\rho_{\max} - \rho^*)\,|\Omega|}{M_0\,\mathcal{E}^n}.
$$

For the default parameters ($P_0 = M_0 = 1$, $\rho_{\max} - \rho^* = 0.5$, $|\Omega| = 1$):

$$
\delta_{\mathrm{barrier}} \approx \frac{0.5}{\mathcal{E}^n}.
$$

**Verification condition.** The engine checks:

$$
\delta^n \geq \delta_{\mathrm{barrier}}(\mathcal{E}^n).
$$

If this condition is violated — the numerical proximity margin is smaller than the analytic barrier predicts — the engine logs a warning:

```
RECORD BarrierViolation:
    time_step     : Int
    time          : Float64
    delta_actual  : Float64
    delta_barrier : Float64
    energy        : Float64
    ratio         : Float64    // delta_actual / delta_barrier
```

A barrier violation does not halt the computation (the margin may still be large enough for stable integration), but it flags a potential inconsistency between the discrete and continuous dynamics. Possible causes include:

- **Insufficient spatial resolution.** The peak density may occur between grid points, and the grid-point maximum underestimates the true maximum. Increasing $N$ resolves this.
- **Insufficient temporal accuracy.** A large explicit step may overshoot the barrier. The adaptive time-step reduction (§1.6.2) should prevent this, but if the initial time step was too large, the first few steps may violate the barrier before the adaptation activates.
- **Energy computation error.** The trapezoidal-rule quadrature of $\Phi(\rho)$ may underestimate the energy when $\rho$ is close to $\rho_{\max}$ (where $\Phi$ diverges and the integrand varies rapidly). Increasing the quadrature order or using adaptive quadrature near $\rho_{\max}$ resolves this.

In all converged experiments of the Atlas, the barrier condition is satisfied at every time step with substantial margin ($\delta^n / \delta_{\mathrm{barrier}} > 2$ throughout).

---

#### 1.6.5 Implicit Matrix Conditioning Near the Horizon

As $\rho \to \rho_{\max}$ at grid point $j$, the mobility $M(\rho_j) \to 0$ and the corresponding diagonal entry of the implicit matrix approaches the identity:

$$
A_{jj} = 1 + \frac{2\Delta t\,D\,M(\rho_j)}{h^2} \to 1 \qquad \text{as } M(\rho_j) \to 0.
$$

Simultaneously, the off-diagonal entries approach zero: $A_{j,j\pm 1} \to 0$. The row of the implicit matrix at grid point $j$ becomes the $j$-th row of the identity matrix — the implicit solve at this point reduces to $\rho_j^{n+1} = R_j$ (the right-hand side directly).

This is physically correct: at $\rho = \rho_{\max}$, the diffusion is extinguished, and the density evolves by the penalty and participation terms alone (which are in the explicit right-hand side $R_j$). The implicit solve degenerates *gracefully* — the tridiagonal matrix becomes locally diagonal, the Thomas algorithm encounters no division by zero (because $A_{jj} \geq 1 > 0$), and the solution is well-defined.

**Condition number.** The condition number of the implicit matrix is

$$
\kappa(\mathbf{A}) = \frac{\max_j(1 + 2\Delta t\,D\,M(\rho_j)/h^2)}{\min_j(1 + 2\Delta t\,D\,M(\rho_j)/h^2)}.
$$

For the default parameters with $M(\rho_j)$ varying from $M_{\min} \approx 10^{-4}$ (near horizon) to $M_* = 0.25$ (at equilibrium):

$$
\kappa \approx \frac{1 + 2 \cdot 5 \times 10^{-4} \cdot 0.6 \cdot 0.25 / h^2}{1 + 2 \cdot 5 \times 10^{-4} \cdot 0.6 \cdot 10^{-4} / h^2}.
$$

At $h = 1/513$ ($N = 512$): the numerator is $\approx 1 + 78.9 \approx 79.9$ and the denominator is $\approx 1 + 0.032 \approx 1.032$, giving $\kappa \approx 77$. This is a mild condition number — the Thomas algorithm handles it without difficulty, and no preconditioning or iterative refinement is needed.

The condition number grows with $M_*/M_{\min}$ (the mobility contrast) and with $\Delta t/h^2$ (the implicit CFL number). For extreme near-horizon configurations ($M_{\min} < 10^{-8}$), the condition number can exceed $10^6$, at which point the Thomas algorithm's $O(N)$ cost is unchanged but its rounding-error accumulation may degrade the solution at the near-horizon grid points. In practice, this regime is never reached in the Atlas experiments because the energy barrier confines $\rho$ to $\rho_{\max} - \delta$ with $\delta > 0.01$ for all finite-energy initial conditions.

---

#### 1.6.6 Constitutive Evaluation at Near-Horizon Densities

The constitutive functions $M(\rho)$ and $M'(\rho)$ must be evaluated at grid points where $\rho$ is close to $\rho_{\max}$. For the power-law mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$:

- At $\rho = \rho_{\max} - 10^{-6}$: $M = M_0 \cdot 10^{-12}$ (for $\beta = 2$), which is a subnormal floating-point number. The computation $(\rho_{\max} - \rho)^\beta$ may underflow to zero.
- At $\rho = \rho_{\max}$: $M = 0$ exactly. The constitutive function is well-defined, but the subsequent computation $M(\rho)\nabla^2\rho$ is $0 \cdot \nabla^2\rho$, which is zero regardless of $\nabla^2\rho$ — even if $\nabla^2\rho$ is large.
- At $\rho > \rho_{\max}$: $(\rho_{\max} - \rho)^\beta$ is undefined for non-integer $\beta$ (negative base raised to a fractional power). This is the primary reason for the projection safeguard (§1.6.3).

**Safeguarded evaluation.** The constitutive evaluation module includes a guard for near-horizon densities:

1. Compute $\delta_j = \rho_{\max} - \rho_j$.
2. If $\delta_j > \delta_{\mathrm{safe}}$ (default: $\delta_{\mathrm{safe}} = 10^{-14}$): evaluate $M(\rho_j) = M_0\,\delta_j^\beta$ and $M'(\rho_j) = -\beta\,M_0\,\delta_j^{\beta-1}$ normally.
3. If $0 < \delta_j \leq \delta_{\mathrm{safe}}$: set $M(\rho_j) = M_0\,\delta_{\mathrm{safe}}^\beta$ and $M'(\rho_j) = -\beta\,M_0\,\delta_{\mathrm{safe}}^{\beta-1}$. This clamps the mobility at a small positive value rather than allowing it to underflow to zero.
4. If $\delta_j \leq 0$: this should never occur (the projection of §1.6.3 prevents it). If it does, halt with a fatal error.

The clamping threshold $\delta_{\mathrm{safe}} = 10^{-14}$ is chosen to be well below the projection floor $\delta_{\mathrm{floor}} = 10^{-12}$ (so the clamp is never activated when the projection is working correctly) but above the subnormal threshold $\sim 10^{-308}$ (so the evaluation does not produce denormalized numbers). In all converged Atlas experiments, the clamp is never activated — the energy barrier keeps $\delta_j > 0.01$.

**Derivative evaluation near $\beta = 1$.** For the mobility derivative $M'(\rho) = -\beta M_0(\rho_{\max} - \rho)^{\beta - 1}$, the exponent $\beta - 1$ is zero when $\beta = 1$ and negative when $\beta < 1$. At $\beta = 1$: $M'(\rho) = -M_0$ (constant), posing no difficulty. At $\beta < 1$ (not used in the Atlas, but permitted by the extension framework): $M'(\rho) \to -\infty$ as $\rho \to \rho_{\max}$, and the safeguarded evaluation clamps $\delta_j$ to $\delta_{\mathrm{safe}}$ to prevent overflow. At $\beta = 2$ (the default): $M'(\rho) = -2M_0(\rho_{\max} - \rho)$, which vanishes at $\rho_{\max}$ and is well-behaved everywhere.

---

#### 1.6.7 Protocol Summary

The complete mobility-collapse handling protocol, applied at each time step, is:

| Step | Action | Condition | Layer |
|------|--------|-----------|-------|
| 1 | Compute $\delta^n = \rho_{\max} - \max_j\rho_j^n$ | Always | Monitoring |
| 2 | Log diagnostic if $\delta^n \leq \delta_{\mathrm{warn}}$ | $\delta^n \leq 0.01\,\rho_{\max}$ | Monitoring |
| 3 | Reduce $\Delta t$ if $\delta^n \leq \delta_{\mathrm{crit}}$ | $\delta^n \leq 10^{-4}\,\rho_{\max}$ | Adaptive |
| 4 | Advance density (implicit solve + explicit step) | Always | Time stepping |
| 5 | Clamp constitutive evaluation if $\delta_j \leq \delta_{\mathrm{safe}}$ | Per grid point | Constitutive |
| 6 | Project $\rho_j^{n+1}$ if outside $(0, \rho_{\max})$ | Per grid point | Projection |
| 7 | Recompute energy if projection activated | After projection | Energy |
| 8 | Verify $\delta^{n+1} \geq \delta_{\mathrm{barrier}}(\mathcal{E}^{n+1})$ | At output times | Barrier |
| 9 | Restore $\Delta t$ if $\delta^{n+1} > 2\,\delta_{\mathrm{crit}}$ | After adaptive reduction | Recovery |

The protocol is ordered from least to most intrusive: monitoring (Step 1–2) is passive, adaptive reduction (Step 3) modifies the time step, constitutive clamping (Step 5) modifies the evaluation, projection (Step 6) modifies the state, and barrier verification (Step 8) checks the structural invariant. At converged resolutions with finite-energy initial conditions, only Steps 1, 4, and 8 are active — the remaining steps are safety nets that verify the analytic guarantees of Principle 4 at the discrete level.

---

### 1.7 Positivity Enforcement

The density field $\rho(x, t)$ of the canonical ED system is strictly positive for all time: $\rho(x, t) > 0$ for all $(x, t) \in \overline{\Omega} \times [0, \infty)$. This is proved in Theorem C.2 (local existence) by a comparison argument with the constant subsolution $\rho \equiv 0$: the penalty restoring force $P(\rho) < 0$ for $\rho < \rho^*$ provides a drift away from zero, and the maximum principle ensures that the density cannot reach zero in finite time. The global result (Theorem C.66(i)) strengthens this to a uniform lower bound: $\rho(x, t) \geq \delta > 0$ for all $t \geq 0$, where $\delta$ depends on the initial energy $\mathcal{E}_0$.

The numerical scheme does not automatically inherit this positivity. The semi-implicit Method A evaluates the penalty and gradient-squared terms explicitly, and a large time step or a steep gradient can produce a negative density at an isolated grid point. The spectral Method B represents $\rho$ as a truncated cosine series, which can take negative values (Gibbs-type oscillations near sharp features). Both methods require a positivity enforcement mechanism that detects and corrects negative densities without distorting the dynamics.

This subsection specifies the positivity enforcement protocol: the physical and mathematical basis for the constraint (§1.7.1), the detection and projection mechanism (§1.7.2), the energy-consistency requirement (§1.7.3), and the convergence criterion that determines when enforcement should never be triggered (§1.7.4).

---

#### 1.7.1 The Positivity Constraint

The density must satisfy two strict inequalities at every grid point and every time step:

$$
0 < \rho_j^n < \rho_{\max} \qquad \text{for all } j = 0, \ldots, N_{\mathrm{grid}} - 1 \text{ and all } n \geq 0.
$$

The upper bound ($\rho < \rho_{\max}$) is enforced by the mobility-collapse protocol (§1.6). The lower bound ($\rho > 0$) is the subject of this subsection.

The positivity constraint is not merely a numerical convenience. It is a physical requirement with three structural consequences:

1. **Constitutive well-definedness.** The mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ and penalty $P(\rho) = P_0(\rho - \rho^*)$ are defined for all real $\rho$, but the density potential $\Phi(\rho) = \int_{\rho^*}^{\rho}P(r)/M(r)\,dr$ diverges as $\rho \to 0^+$ (since $P(\rho) < 0$ for $\rho < \rho^*$ and $M(\rho) > 0$, the integral accumulates without bound). A negative density would place the system outside the domain of $\Phi$, making the energy functional $\mathcal{E}$ undefined.

2. **Physical interpretation.** In every physical domain where the ED architecture is applied (quantum wavefunction density, galactic mass distribution, condensed-matter order parameter), the density is intrinsically non-negative. A negative density is not a physical configuration.

3. **Analytic prerequisites.** The functional setting of §C.1.1 restricts the state to the admissible region $\mathcal{O} = \{(\rho, v) \in \mathcal{X} : 0 < \rho(x) < \rho_{\max}\}$. Every theorem in Appendix C assumes $\rho \in \mathcal{O}$. A numerical solution that exits $\mathcal{O}$ (even transiently) is outside the scope of the analytic theory.

---

#### 1.7.2 Detection and Projection

The positivity enforcement is applied immediately after the density update at each time step, before any observable extraction or diagnostic computation.

**Detection.** After the time-stepping module produces $\boldsymbol{\rho}^{n+1}$ (whether by the implicit solve of Method A or the ETD update of Method B), the engine scans the density array for violations:

$$
j_{\mathrm{neg}} := \{j : \rho_j^{n+1} \leq 0\}, \qquad j_{\mathrm{over}} := \{j : \rho_j^{n+1} \geq \rho_{\max}\}.
$$

The scan is a single pass over the array ($O(N_{\mathrm{grid}})$), performed simultaneously with the proximity monitoring of §1.6.1.

**Projection.** For each violating grid point:

- If $\rho_j^{n+1} \leq 0$: set $\rho_j^{n+1} \leftarrow \delta_{\mathrm{floor}}$, where $\delta_{\mathrm{floor}} = 10^{-12}$.
- If $\rho_j^{n+1} \geq \rho_{\max}$: set $\rho_j^{n+1} \leftarrow \rho_{\max} - \delta_{\mathrm{floor}}$.

The projection is applied pointwise and independently at each grid point. It is *not* a global operation (e.g., it does not rescale the entire density field to preserve mass); it is a local clamp that moves the offending grid values to the nearest admissible point.

**Projection record.** Every projection event is recorded in the diagnostic log:

```
RECORD PositivityEvent:
    time_step      : Int
    time           : Float64
    n_negative     : Int          // number of grid points with ρ ≤ 0
    n_overcap      : Int          // number of grid points with ρ ≥ ρ_max
    worst_negative : Float64      // min(ρ_j) before projection (most negative value)
    worst_overcap  : Float64      // max(ρ_j) − ρ_max before projection
    total_mass_change : Float64   // Σ_j (ρ_j_after − ρ_j_before) · h^d
```

The `total_mass_change` field records the spurious mass injected or removed by the projection. For a well-resolved computation, this quantity is zero (no projection triggered); for an under-resolved computation, it measures the magnitude of the numerical artifact.

---

#### 1.7.3 Energy Recomputation After Projection

The projection modifies the density array, which changes the energy $\mathcal{E}[\boldsymbol{\rho}, v]$ and the Lyapunov functional $\mathcal{V}[u, w]$. To maintain consistency between the recorded observables and the actual state, the engine recomputes both quantities after any projection:

1. Recompute the density potential $\Phi(\rho_j)$ at all affected grid points.
2. Recompute the energy $\mathcal{E}^{n+1} = h^d\sum_j\Phi(\rho_j^{n+1}) + (\tau H/2)(v^{n+1})^2$.
3. Recompute the ED-complexity $C_{\mathrm{ED}}^{n+1} = h^d\sum_j(|\nabla_h\rho^{n+1}|^2)_j$.
4. Recompute the Lyapunov functional $\mathcal{V}^{n+1}$.

The recomputation is performed only when the projection was activated (when $|j_{\mathrm{neg}}| + |j_{\mathrm{over}}| > 0$). The cost is $O(N_{\mathrm{grid}})$ — the same as a single observable extraction — and is negligible relative to the time-stepping cost.

**Energy monotonicity after projection.** The projection can either increase or decrease the energy, depending on the direction and location of the correction:

- Projecting a negative $\rho_j$ to $\delta_{\mathrm{floor}}$ increases $\rho_j$, which decreases $\Phi(\rho_j)$ (since $\Phi$ diverges to $+\infty$ as $\rho \to 0^+$ and decreases as $\rho$ moves away from $0$ toward $\rho^*$). The energy *decreases*.
- Projecting an over-capacity $\rho_j$ to $\rho_{\max} - \delta_{\mathrm{floor}}$ decreases $\rho_j$, which also decreases $\Phi(\rho_j)$ (since $\Phi$ diverges at $\rho_{\max}$ and decreases as $\rho$ moves away from $\rho_{\max}$ toward $\rho^*$). The energy *decreases*.

In both cases, the projection moves the density toward the interior of the admissible region, and the convexity of $\Phi$ (with its divergent barriers at both endpoints) ensures that the energy decreases. The projection therefore does not violate the energy-monotonicity invariant; it reinforces it. However, the amount of energy removed by the projection is a numerical artifact (it does not correspond to any physical dissipation channel), and it should be negligible — comparable to or smaller than the truncation error. This is verified by the convergence criterion in §1.7.4.

---

#### 1.7.4 The Convergence Criterion: When Projection Should Never Trigger

The positivity projection is a safety net, not a regularization. At converged spatial and temporal resolution, the discrete solution should remain strictly interior to $(0, \rho_{\max})$ without any projection, because the analytic solution does so (Theorem C.2, Theorem C.66(i)) and the discrete solution converges to the analytic solution as $h \to 0$ and $\Delta t \to 0$.

**Criterion.** An experiment is considered **positivity-converged** if:

$$
\text{No projection event occurs at any time step during the integration.}
$$

That is, $|j_{\mathrm{neg}}| = |j_{\mathrm{over}}| = 0$ for all $n = 0, 1, \ldots, N_{\mathrm{steps}}$.

This criterion is a binary pass/fail condition: either the projection was never activated (pass) or it was activated at least once (fail). It is stronger than the usual convergence criterion (which asks only that the solution is accurate to a specified tolerance) — it asks that the discrete solution respects the qualitative structure of the continuous solution (strict positivity and strict sub-capacity).

**Expected behavior across refinement levels.** For a well-posed initial condition with finite energy:

| Resolution | Typical behavior | Projection status |
|-----------|-----------------|-------------------|
| Coarse ($N = 32$, $\Delta t = 10^{-2}$) | Isolated negative values near steep gradients or near-horizon peaks | Projection activated sporadically |
| Moderate ($N = 128$, $\Delta t = 10^{-3}$) | Rare projection events, confined to the first few time steps of far-from-equilibrium initial conditions | Projection activated rarely |
| Fine ($N = 512$, $\Delta t = 5 \times 10^{-4}$) | No projection events | **Positivity-converged** |
| Very fine ($N = 1024$, $\Delta t = 10^{-4}$) | No projection events | **Positivity-converged** |

The transition from "projection activated" to "positivity-converged" occurs at a resolution that depends on the initial condition's complexity and proximity to the boundaries. For the standard initial conditions of the Atlas (IC-A through IC-D):

- **IC-A** ($A = 0.05$, single mode): positivity-converged at $N \geq 32$ (the density never approaches zero).
- **IC-B** ($N_m = 8$, multi-mode): positivity-converged at $N \geq 64$.
- **IC-C** ($A = 0.3$, localized Gaussian): positivity-converged at $N \geq 128$ (the Gaussian tails are close to $\rho^*$, not to zero).
- **IC-D** ($\delta = 0.05$, near-capacity): positivity-converged at $N \geq 256$ (the density is near $\rho_{\max}$, not near zero, so positivity is not the concern; the mobility-collapse protocol is the active safeguard).

All Atlas experiments use resolutions at or above these thresholds, so no projection events occur in any reported result. The positivity enforcement exists solely as a guard against implementation errors, under-resolved exploratory runs, and pathological initial conditions that place the density closer to zero than the standard ICs.

**Reporting requirement.** Every experiment output includes a field:

```
positivity_converged : Boolean   // true if no projection was triggered
```

An experiment whose output shows `positivity_converged = false` is not considered a valid reproduction of the Atlas. The resolution must be increased until the criterion is met.

---

#### 1.7.5 Interaction with the Spectral Method

The spectral method (Method B) represents the density as a truncated cosine series. Cosine series can produce negative values — the partial sum $\rho^* + \sum_{k=0}^{N-1}\hat{u}_k\phi_k(x)$ may drop below zero at some physical-space points, particularly near sharp features where the Gibbs phenomenon is active.

The positivity enforcement for Method B is applied in physical space after each pseudospectral evaluation:

1. Transform the spectral state $\hat{\mathbf{u}}$ to physical-space values $\rho_j = \rho^* + \sum_k\hat{u}_k\phi_k(x_j)$ on the $N_{\mathrm{phys}}$-point grid.
2. Check for violations: any $\rho_j \leq 0$ or $\rho_j \geq \rho_{\max}$.
3. If violations exist, project the physical-space values as in §1.7.2.
4. Transform the projected values back to spectral space via the forward DCT.
5. Replace $\hat{\mathbf{u}}$ with the projected spectral coefficients.

The back-transformation (Step 4) introduces a modification of the spectral state that is not a simple pointwise clamp — it redistributes the projection's effect across all modes. This is the correct behavior: the spectral state must be self-consistent (its inverse transform must produce the projected physical-space values), and the forward-inverse DCT pair ensures this.

The projection in physical space followed by re-transformation is equivalent to projecting the density onto the convex set $\{\rho : 0 < \rho_j < \rho_{\max} \text{ for all } j\}$ and then representing the projected function in the spectral basis. The energy of the projected state is computed from the projected spectral coefficients, not from the pre-projection state.

For the Atlas experiments, the spectral method is used at $N = 128$ modes with initial amplitudes $A \leq 0.2$ and equilibrium density $\rho^* = 0.5$ — the density deviation is at most $\pm 0.2$ from an equilibrium of $0.5$, so the density remains in $[0.3, 0.7]$ and positivity is never threatened. The spectral positivity enforcement is a precaution for future extensions (large-amplitude spectral computations, constitutive functions with $\rho^*$ close to zero) rather than a practical necessity for the current Atlas.

---

#### 1.7.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Constraint** | $0 < \rho_j^n < \rho_{\max}$ at every grid point and time step |
| **Detection** | Single-pass scan, simultaneous with proximity monitoring |
| **Lower projection** | $\rho_j \leftarrow \delta_{\mathrm{floor}} = 10^{-12}$ if $\rho_j \leq 0$ |
| **Upper projection** | $\rho_j \leftarrow \rho_{\max} - \delta_{\mathrm{floor}}$ if $\rho_j \geq \rho_{\max}$ |
| **Energy effect** | Projection decreases $\mathcal{E}$ (moves $\rho$ toward interior of $\Phi$-well) |
| **Energy recomputation** | Mandatory after any projection event |
| **Diagnostic** | `PositivityEvent` record logged; `positivity_converged` flag in output |
| **Convergence criterion** | No projection at any step = positivity-converged |
| **Expected at Atlas resolutions** | Never triggered (all IC-A through IC-D converged at $N \geq 256$) |
| **Spectral method** | Applied in physical space, then re-transformed to spectral space |
| **Structural role** | Safety net for implementation correctness, not a regularization |

The positivity enforcement is the simplest layer of the defensive computation framework (§0.3, Principle 6). It adds negligible computational cost, produces no artifacts at converged resolution, and provides the runtime guarantee that the discrete state remains in the admissible region $\mathcal{O}$ required by the analytic theory of Appendix C.

---

### 1.8 Stability Constraints

The time-stepping schemes of §1.4 are semi-implicit (Method A) or exponential-integrating (Method B): the stiff linear diffusion is handled implicitly or exactly, but the nonlinear terms are treated explicitly. The explicit treatment introduces conditional stability restrictions — the time step $\Delta t$ must be small enough that the explicit terms do not amplify perturbations faster than the implicit/exact treatment can suppress them. This subsection derives the stability constraints, analyzes the nonlinear mechanisms that can trigger instability, discusses the stability properties of the ETD schemes, and provides concrete time-step recommendations as functions of the grid spacing and canonical parameters.

---

#### 1.8.1 CFL Condition for the Explicit Nonlinear Terms

The explicit terms in the density equation are:

$$
\mathcal{E}_{\mathrm{explicit}} = D\,M'(\rho)\,|\nabla\rho|^2 - D\,P(\rho) + H\,v.
$$

Each contributes a distinct stability constraint.

##### 1.8.1.1 The Gradient-Squared Term

The term $D\,M'(\rho)\,|\nabla\rho|^2$ is the most restrictive. It has the character of a nonlinear advection: expanding $M'(\rho)|\nabla\rho|^2 = M'(\rho)\,(\partial_x\rho)^2$ and differentiating with respect to $\rho$ at a grid point, the effective "advection speed" seen by a perturbation $\delta\rho$ is

$$
a_{\mathrm{eff}} \sim D\,|M'(\rho)|\,|\nabla\rho|,
$$

which is the product of the mobility derivative and the local gradient magnitude. The CFL condition for a first-order explicit scheme with this advection speed on a grid with spacing $h$ is

$$
\Delta t \leq \frac{h}{a_{\mathrm{eff}}} = \frac{h}{D\,|M'(\rho)|\,|\nabla\rho|}.
$$

However, the gradient-squared term also has a diffusive character (it is second-order in spatial derivatives when $M'(\rho)\nabla\rho$ is viewed as a coefficient times $\nabla\rho$). The combined advection-diffusion CFL is

$$
\Delta t_{\mathrm{grad}} \leq \frac{C_{\mathrm{CFL}}\,h^2}{D\,\max_j|M'(\rho_j)|\,\max_j|(\nabla_h\rho)_j|\,h + D\,\max_j M(\rho_j)},
$$

where the denominator accounts for both the advective contribution ($|M'||\nabla\rho|h$, from the gradient-squared term) and the residual explicit diffusion ($M(\rho)$, from the density-dependent variation of the mobility around its frozen implicit value). The safety factor is $C_{\mathrm{CFL}} = 0.5$.

**Evaluation.** The CFL constraint is evaluated at the beginning of each time step using the current density $\boldsymbol{\rho}^n$. The quantities $\max_j|M'(\rho_j)|$, $\max_j|(\nabla_h\rho)_j|$, and $\max_j M(\rho_j)$ are computed during the constitutive evaluation and stencil computation that are already performed for the time step, so the CFL evaluation adds no additional array passes.

**Parameter dependence.** For the canonical constitutive functions at equilibrium ($\rho = \rho^*$, $\nabla\rho = 0$):

$$
\Delta t_{\mathrm{grad}}\big|_{\mathrm{equil}} = \frac{C_{\mathrm{CFL}}\,h^2}{D\,M_*} = \frac{0.5\,h^2}{D\,M_*}.
$$

At the default parameters ($D = 0.6$, $M_* = 0.25$, $h = 1/513$ for $N = 512$):

$$
\Delta t_{\mathrm{grad}}\big|_{\mathrm{equil}} = \frac{0.5 \cdot (1/513)^2}{0.6 \cdot 0.25} \approx \frac{0.5 \cdot 3.80 \times 10^{-6}}{0.15} \approx 1.27 \times 10^{-5}.
$$

This is well below the default $\Delta t = 5 \times 10^{-4}$, which means that the implicit treatment of the diffusion is *essential* — without it, the CFL would restrict the time step to $\sim 10^{-5}$, requiring $\sim 10^6$ steps for a $T = 10$ integration.

With the implicit treatment, the residual CFL comes only from the *nonlinear variation* of the mobility and the gradient-squared term. Near equilibrium ($\nabla\rho \approx 0$), the advective contribution $|M'||\nabla\rho|h$ vanishes, and the residual diffusion contribution $M(\rho) - M(\rho^n)$ (the difference between the true and frozen mobility) is $O(|\rho - \rho^n|) = O(\Delta t)$ — second order in the time step. The effective CFL near equilibrium is therefore $\Delta t_{\mathrm{grad}} \sim h^2/O(\Delta t) \sim \infty$ (no restriction), which is why the semi-implicit scheme permits large time steps in the linearized regime.

Away from equilibrium (large $|\nabla\rho|$), the advective contribution dominates, and the CFL becomes restrictive. The worst case is a steep gradient near the horizon, where $|M'(\rho)| = 2M_0(\rho_{\max} - \rho)$ can be large (for $\rho$ well below $\rho_{\max}$) and $|\nabla\rho|$ can be large (before the mobility-collapse gradient suppression takes effect). At the typical worst case for Atlas experiments ($|M'| \approx 1$, $|\nabla\rho| \approx 5$, $h = 1/513$):

$$
\Delta t_{\mathrm{grad}} \approx \frac{0.5 \cdot (1/513)^2}{0.6 \cdot 1.0 \cdot 5.0 \cdot (1/513) + 0.6 \cdot 0.25} \approx \frac{1.90 \times 10^{-6}}{5.85 \times 10^{-3} + 0.15} \approx 1.22 \times 10^{-5}.
$$

This is still below the default $\Delta t = 5 \times 10^{-4}$ by a factor of $\sim 40$. At the default $\Delta t$, the gradient-squared CFL is therefore *not* the binding constraint for typical Atlas experiments (the gradients are not steep enough). It becomes binding only for under-resolved computations or extreme initial conditions.

##### 1.8.1.2 The Penalty Term

The explicit penalty $-D\,P(\rho)$ acts as a zero-order reaction term. For the linear penalty $P(\rho) = P_0(\rho - \rho^*)$, the stability constraint is

$$
\Delta t_{\mathrm{pen}} \leq \frac{2}{D\,P_0}.
$$

At the default parameters ($D = 0.6$, $P_0 = 1.0$): $\Delta t_{\mathrm{pen}} \leq 3.33$. This is three orders of magnitude above the default $\Delta t = 5 \times 10^{-4}$, so the penalty is never the binding stability constraint.

For nonlinear penalties with $P'(\rho)$ varying across the domain, the local penalty stability requirement is $\Delta t \leq 2/(D\,\max_j P'(\rho_j))$, which is similarly non-restrictive for smooth penalties.

##### 1.8.1.3 The Participation Coupling

The term $H\,v$ is spatially constant and acts as a uniform source. It does not introduce a spatial stability constraint (no dependence on $h$). Its temporal stability is governed by the participation ODE: with explicit Euler, $\Delta t \leq 2\tau/\zeta$ (§1.4.5). With the exponential integrator (the default), there is no stability restriction on the participation.

##### 1.8.1.4 Combined CFL Condition

The effective CFL constraint is the minimum of the individual constraints:

$$
\Delta t_{\mathrm{CFL}} = \min\!\left(\Delta t_{\mathrm{grad}},\;\Delta t_{\mathrm{pen}},\;\Delta t_{\mathrm{part}}\right).
$$

In practice, $\Delta t_{\mathrm{pen}}$ and $\Delta t_{\mathrm{part}}$ are always much larger than $\Delta t_{\mathrm{grad}}$, so the binding constraint is the gradient-squared CFL:

$$
\Delta t_{\mathrm{CFL}} = \frac{C_{\mathrm{CFL}}\,h^2}{D\,\max_j|M'(\rho_j)|\,\max_j|(\nabla_h\rho)_j|\,h + D\,\max_j M(\rho_j)}.
$$

---

#### 1.8.2 Nonlinear Stability Limits

Beyond the linearized CFL analysis, the nonlinear structure of the ED system introduces three additional stability considerations that do not arise in standard von Neumann analysis.

##### 1.8.2.1 Mobility Positivity Constraint

The implicit matrix $\mathbf{A} = \mathbf{I} - \Delta t\,D\,\operatorname{diag}(M(\boldsymbol{\rho}^n))\,\mathbf{L}_h$ is positive definite only when $M(\rho_j^n) > 0$ at every grid point. If $M(\rho_j^n) = 0$ at some point $j$ (density at the capacity bound), the corresponding row of $\mathbf{A}$ reduces to the identity row, and the matrix remains non-singular — but the equation at that point is no longer parabolic, and the implicit scheme provides no diffusive stabilization there.

The mobility positivity is guaranteed by the energy barrier (Proposition C.11) and enforced by the mobility-collapse protocol (§1.6). The stability analysis assumes $M(\rho_j^n) \geq M_{\min} > 0$ at all grid points, where $M_{\min} = M(\rho_{\max} - \delta^n)$ depends on the current proximity margin $\delta^n$. The implicit scheme is stable as long as $M_{\min} > 0$; there is no additional time-step restriction from the mobility positivity.

##### 1.8.2.2 Energy Growth from the Cross-Coupling

The participation coupling $H\,v$ in the density equation injects energy into the density field (when $v$ and $\rho - \rho^*$ have the same sign). In the continuous system, this injection is bounded by the channel complementarity $D + H = 1$ and the participation damping $\zeta$: the energy identity (Lemma C.6) shows that the cross-coupling terms are controlled by Cauchy–Schwarz and Young's inequality. In the discrete system, the explicit treatment of $H\,v^n$ in the right-hand side means that the energy injection is computed at the *old* participation value $v^n$, not the *new* value $v^{n+1}$. This lag introduces a potential for transient energy growth if $v$ is oscillating rapidly (Parameter Set I: $\omega \approx 0.83$) and $\Delta t$ is comparable to the oscillation period $T_{\mathrm{osc}} = 2\pi/\omega \approx 7.6$.

The stability requirement is that $\Delta t$ be small enough to resolve the participation oscillation:

$$
\Delta t \ll T_{\mathrm{osc}} = \frac{2\pi}{\omega} = \frac{4\pi}{\sqrt{|\mathscr{D}_0|}}.
$$

At the default $\Delta t = 5 \times 10^{-4}$ and the worst-case $T_{\mathrm{osc}} \approx 3.2$ (Parameter Set V, $\omega \approx 1.25$): $\Delta t/T_{\mathrm{osc}} \approx 1.6 \times 10^{-4}$, which is negligible. The cross-coupling is never a binding stability constraint for the Atlas experiments.

For hypothetical parameter sets with very high oscillation frequency ($\omega \gg 1$, which requires $|\mathscr{D}_0| \gg 1$, hence $H P_*'/\tau \gg 1$), the cross-coupling could become restrictive. This regime is not encountered in the Atlas.

##### 1.8.2.3 Nonlinear Amplification in the Gradient-Squared Term

The gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$ is the source of inter-modal energy transfer (Principle 7). In the explicit scheme, this term can transfer energy from low modes (slowly decaying) to high modes (rapidly decaying) within a single time step. If the transfer rate exceeds the implicit diffusive decay rate of the receiving mode, the high mode can grow transiently.

The condition for stability against this nonlinear amplification is

$$
\Delta t\,D\,|M'(\rho)|\,|\nabla\rho|^2 \ll D\,M(\rho)\,\mu_k\,|a_k|
$$

for the highest resolved mode $k$. This is a *nonlinear* CFL condition: it depends on the amplitude of the solution, not just on the grid spacing. For the Atlas experiments (amplitudes $A \leq 0.4$), the nonlinear amplification is always subdominant to the linear CFL (§1.8.1.1). For very large amplitudes (approaching the mobility-collapse region), the adaptive time-step reduction (§1.6.2) provides the necessary control.

---

#### 1.8.3 ETD Stability Considerations

The ETD schemes (§1.4.2) integrate the linear part exactly and treat the nonlinear part explicitly within a Runge–Kutta framework. The stability properties differ qualitatively from the semi-implicit Method A.

##### 1.8.3.1 Linear Stability: Unconditional

The linear decay $\hat{u}_k^{n+1} = e^{c_k\Delta t}\hat{u}_k^n$ has $|e^{c_k\Delta t}| = e^{-D M_*\mu_k\Delta t} \leq 1$ for all $\Delta t > 0$ and all $k$ (since $c_k = -DM_*\mu_k \leq 0$). The linear part is therefore unconditionally stable — no time-step restriction arises from the stiff diffusion, regardless of the mode number $k$ or the grid resolution $N$.

This is the ETD method's defining advantage: it eliminates the stiffness-induced time-step restriction that would otherwise scale as $\Delta t \lesssim 1/(DM_*\mu_{N-1}) \sim L^2/(DM_*N^2\pi^2)$.

##### 1.8.3.2 Nonlinear Stability: Conditional

The nonlinear residual $\hat{\mathcal{N}}_k$ is treated explicitly within the RK substeps. The stability of the explicit treatment depends on the Lipschitz constant of $\hat{\mathcal{N}}$ as a function of the spectral state $\hat{\mathbf{u}}$:

$$
\|\hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}_1) - \hat{\boldsymbol{\mathcal{N}}}(\hat{\mathbf{u}}_2)\| \leq L_{\mathcal{N}}\,\|\hat{\mathbf{u}}_1 - \hat{\mathbf{u}}_2\|,
$$

where $L_{\mathcal{N}}$ is the local Lipschitz constant. The stability restriction is

$$
\Delta t \leq \frac{C_{\mathrm{RK}}}{L_{\mathcal{N}}},
$$

where $C_{\mathrm{RK}} \approx 2.78$ for RK4 (the radius of the RK4 absolute-stability region along the negative real axis). The Lipschitz constant $L_{\mathcal{N}}$ depends on the solution amplitude and the constitutive functions:

$$
L_{\mathcal{N}} \sim D\,|M_*'|\,\|\nabla\rho\|_{L^\infty}\,\|\nabla^2\rho\|_{L^\infty} + D\,|M_*''|\,\|\nabla\rho\|_{L^\infty}^2 + D\,|P_*''|\,\|\rho - \rho^*\|_{L^\infty}.
$$

For the linear penalty ($P'' = 0$) and the default constitutive functions near equilibrium ($\|\nabla\rho\| \sim A$, $\|\nabla^2\rho\| \sim A\mu_1$):

$$
L_{\mathcal{N}} \sim D\,|M_*'|\,A^2\,\mu_1 \approx 0.6 \cdot 1.0 \cdot A^2 \cdot 9.87 \approx 5.92\,A^2.
$$

At $A = 0.2$: $L_{\mathcal{N}} \approx 0.237$, giving $\Delta t \leq 2.78/0.237 \approx 11.7$. At $A = 0.05$: $L_{\mathcal{N}} \approx 0.0148$, giving $\Delta t \leq 188$. Both are far above the default $\Delta t = 10^{-4}$, confirming that the nonlinear CFL is not binding for the Atlas spectral experiments.

##### 1.8.3.3 Aliasing-Induced Instability

The pseudospectral evaluation (§1.3.2.4) with the 3/2-rule de-aliasing eliminates the leading-order aliasing error from quadratic products. However, higher-order products (e.g., $M(\rho)\nabla^2\rho$ when $M(\rho)$ has polynomial degree $> 1$) produce aliasing at order $> 2N/3$, which the 3/2-rule does not remove. This residual aliasing can introduce a slow energy transfer to the highest resolved modes, which the ETD scheme does not stabilize (the linear decay of high modes is real, not numerical dissipation, and it operates at the continuous rate $D\alpha_k$, not at an artificially enhanced rate).

For the canonical constitutive functions with $\beta = 2$, $M(\rho) = (\rho_{\max} - \rho)^2$ is a polynomial of degree $2$ in $\rho$. The product $M(\rho)\nabla^2\rho$ has polynomial degree $3$ in the perturbation (degree $2$ from $M$ times degree $1$ from $\nabla^2 u$), requiring a $2\times$ padding rule for exact de-aliasing. The 3/2-rule provides partial de-aliasing; the residual aliasing error is of order $(A/N)^3$, which is negligible for $A \leq 0.2$ and $N = 128$.

For constitutive functions with higher polynomial degree ($\beta > 2$) or non-polynomial structure, the 3/2-rule may be insufficient, and a $2\times$ or $5/2\times$ padding factor may be needed. The simulation engine accepts a configurable padding factor (default $3/2$) and logs a warning if the constitutive degree exceeds $2$.

---

#### 1.8.4 Recommended Time Steps

The following table provides recommended time steps as functions of the grid spacing $h$, the canonical parameters, and the initial condition amplitude. The recommendations are derived from the constraints of §§1.8.1–1.8.3 with a safety margin of $2\times$ below the theoretical stability limit.

##### 1.8.4.1 Method A (Finite Difference)

The binding constraint is the gradient-squared CFL (§1.8.1.1). The recommendation depends on whether the solution is near equilibrium or far from it.

**Near-equilibrium regime** ($\|\rho - \rho^*\|_{H^1} \ll 1$, $|\nabla\rho| \ll 1$):

The advective contribution to the CFL vanishes, and the residual constraint comes from the frozen-mobility variation:

$$
\Delta t_{\mathrm{rec}} = \frac{0.25\,h^2}{D\,M_*}.
$$

| $N$ | $h$ | $D = 0.3$ | $D = 0.6$ | $D = 0.9$ |
|-----|-----|-----------|-----------|-----------|
| 128 | $7.75 \times 10^{-3}$ | $2.0 \times 10^{-4}$ | $1.0 \times 10^{-4}$ | $6.7 \times 10^{-5}$ |
| 256 | $3.89 \times 10^{-3}$ | $5.0 \times 10^{-5}$ | $2.5 \times 10^{-5}$ | $1.7 \times 10^{-5}$ |
| 512 | $1.95 \times 10^{-3}$ | $1.3 \times 10^{-5}$ | $6.3 \times 10^{-6}$ | $4.2 \times 10^{-6}$ |

These values would be binding if the diffusion were treated explicitly. With implicit diffusion, the actual binding constraint near equilibrium is the *user-specified* default $\Delta t_{\mathrm{user}}$, because the CFL from the explicit nonlinear terms is effectively $\infty$ when $\nabla\rho \approx 0$. The default $\Delta t = 5 \times 10^{-4}$ is therefore safe in the near-equilibrium regime at all listed resolutions.

**Far-from-equilibrium regime** ($\|\nabla\rho\|_{L^\infty} \sim A/\sigma$ for a localized initial condition):

The advective contribution dominates. For IC-C with $A = 0.3$, $\sigma = 0.05$:

$$
|\nabla\rho|_{\max} \approx \frac{A}{\sigma} = 6.0, \qquad |M'|_{\max} \approx 2(\rho_{\max} - \rho^*) = 1.0.
$$

$$
\Delta t_{\mathrm{rec}} = \frac{0.25\,h^2}{D \cdot 1.0 \cdot 6.0 \cdot h + D \cdot 0.25}.
$$

| $N$ | $h$ | $D = 0.3$ | $D = 0.6$ |
|-----|-----|-----------|-----------|
| 256 | $3.89 \times 10^{-3}$ | $4.1 \times 10^{-5}$ | $2.1 \times 10^{-5}$ |
| 512 | $1.95 \times 10^{-3}$ | $1.2 \times 10^{-5}$ | $6.1 \times 10^{-6}$ |

These values are below the default $\Delta t = 5 \times 10^{-4}$ by factors of $10$–$80$. For far-from-equilibrium experiments (Atlas §6, §7.1), the CFL-selected time step is used instead of the default.

**General recommendation (Method A):**

$$
\boxed{\Delta t = \min\!\left(\Delta t_{\mathrm{user}},\;\frac{C_{\mathrm{CFL}}\,h^2}{D\,\|M'\|_\infty\,\|\nabla_h\rho\|_\infty\,h + D\,\|M\|_\infty}\right)}
$$

with $C_{\mathrm{CFL}} = 0.5$ and $\Delta t_{\mathrm{user}} = 5 \times 10^{-4}$ as the default maximum.

##### 1.8.4.2 Method B (Spectral / ETD)

The binding constraint is the nonlinear Lipschitz condition (§1.8.3.2). The recommendation is:

$$
\Delta t_{\mathrm{rec}} = \frac{1.0}{L_{\mathcal{N}}} = \frac{1.0}{D\,|M_*'|\,\|\nabla\rho\|_\infty\,\|\nabla^2\rho\|_\infty},
$$

with a safety factor of $1.0$ (approximately $C_{\mathrm{RK}}/2.78$). For the Atlas experiments ($A \leq 0.2$):

| $A$ | $L_{\mathcal{N}}$ (approx.) | $\Delta t_{\mathrm{rec}}$ |
|-----|-----|-----|
| $0.01$ | $6 \times 10^{-4}$ | $1700$ |
| $0.05$ | $0.015$ | $67$ |
| $0.1$ | $0.059$ | $17$ |
| $0.2$ | $0.237$ | $4.2$ |

All values are far above the default $\Delta t = 10^{-4}$. The ETD nonlinear CFL is never the binding constraint for the Atlas. The default $\Delta t = 10^{-4}$ is set by *accuracy* requirements (resolving the fast modal dynamics to $O(\Delta t^4) \sim 10^{-16}$ for the fourth-order ETD-RK4), not by stability.

**General recommendation (Method B):**

$$
\boxed{\Delta t = \min\!\left(\Delta t_{\mathrm{user}},\;\frac{C_{\mathrm{RK}}}{L_{\mathcal{N}}}\right)}
$$

with $C_{\mathrm{RK}} = 2.78$ and $\Delta t_{\mathrm{user}} = 10^{-4}$ as the default maximum.

---

#### 1.8.5 Stability Monitoring at Runtime

The stability constraints of §§1.8.1–1.8.3 are theoretical bounds. The simulation engine monitors stability empirically at runtime through two diagnostics:

**Energy monotonicity.** The energy $\mathcal{E}^{n+1}$ is compared to $\mathcal{E}^n$ at every time step. A violation $\mathcal{E}^{n+1} > \mathcal{E}^n + \text{tol}$ (where $\text{tol} = 10\,\Delta t^p\,\mathcal{E}^n$) indicates that the explicit terms are injecting energy faster than the implicit/exact treatment can dissipate it — a symptom of CFL violation. The engine logs a warning on the first violation and halts if the violation exceeds $10 \cdot \text{tol}$ (indicating gross instability).

**Spectral energy distribution.** For Method B, the engine monitors the energy in the highest resolved modes: $E_{\mathrm{tail}} = \sum_{k > 2N/3}|\hat{u}_k|^2$. A sustained growth of $E_{\mathrm{tail}}$ indicates aliasing-driven energy accumulation at the de-aliasing boundary, which is a symptom of insufficient padding or excessive amplitude. The engine logs a warning if $E_{\mathrm{tail}} > 10^{-6}\,E_{\mathrm{total}}$ (the tail energy exceeds $0.0001\%$ of the total).

Both diagnostics add $O(N)$ cost per step (a single pass for the energy, a partial sum for the spectral tail) and are enabled by default.

---

#### 1.8.6 Stability Summary

| Constraint | Source | Formula | Binding for Atlas? |
|-----------|--------|---------|-------------------|
| Gradient-squared CFL | $M'(\rho)|\nabla\rho|^2$ (explicit, Method A) | $\Delta t \leq C_{\mathrm{CFL}} h^2/(D|M'||\nabla\rho|h + DM)$ | Yes, for far-from-equilibrium ICs |
| Penalty CFL | $P(\rho)$ (explicit, Method A) | $\Delta t \leq 2/(DP_0)$ | No ($\Delta t_{\mathrm{pen}} \sim 3$) |
| Participation ODE | $v$ explicit Euler (if used) | $\Delta t \leq 2\tau/\zeta$ | No (exponential integrator used) |
| Cross-coupling | $Hv$ lag | $\Delta t \ll 2\pi/\omega$ | No ($\Delta t/T_{\mathrm{osc}} < 10^{-3}$) |
| Mobility positivity | $M(\rho_j) > 0$ required | Enforced by §1.6, not by $\Delta t$ | N/A |
| ETD linear | $e^{c_k\Delta t}$ factor | Unconditional | N/A |
| ETD nonlinear | $\hat{\mathcal{N}}$ Lipschitz (Method B) | $\Delta t \leq C_{\mathrm{RK}}/L_{\mathcal{N}}$ | No ($\Delta t_{\mathrm{rec}} \gg \Delta t_{\mathrm{user}}$) |
| Aliasing | Pseudospectral (Method B) | Controlled by 3/2-rule; $\beta \leq 2$ | No (monitored by $E_{\mathrm{tail}}$) |

The single binding stability constraint for the Atlas experiments is the gradient-squared CFL for Method A in the far-from-equilibrium regime. All other constraints are non-binding at the default time steps. The ETD scheme (Method B) has no binding stability constraint at the Atlas amplitudes and resolutions — its time step is set by accuracy, not stability.

---

## 2. Workflow

### 2.1 Initialization

Every experiment in the Atlas begins with an initialization phase that creates the computational infrastructure, loads the parameters, constructs the initial condition, allocates memory, precomputes all static quantities, and validates the configuration before the first time step. The initialization is deterministic — given the same experiment specification (from the Master Experiment Table, Atlas §10.2.5), the initialization produces an identical starting state in every environment.

This subsection specifies the initialization in the order it is executed: parameter loading and validation (§2.1.1), grid creation (§2.1.2), constitutive function construction (§2.1.3), initial condition evaluation (§2.1.4), memory allocation and precomputation (§2.1.5), and the final readiness check (§2.1.6).

---

#### 2.1.1 Parameter Loading and Validation

The first step of initialization is to load the canonical parameters and verify that they satisfy the structural constraints of Principles 1–7.

**Input.** The experiment specification provides:

- The parameter set identifier (I, II, III, IV, V, or Custom).
- Any parameter overrides (e.g., a sweep value of $\zeta$ that differs from the standard set).
- The constitutive type (default: power-law mobility with linear penalty) and its parameters ($M_0$, $\beta$, $P_0$).

**Parameter construction.** The engine constructs the `CanonicalParams` record (§1.1.6):

1. Load $D$, $\zeta$, $\tau$, $\rho^*$, $\rho_{\max}$ from the parameter set (Atlas §10.2.1) or from the override values.
2. Compute $H = 1 - D$.
3. Verify: $0 < D < 1$, $\zeta > 0$, $\tau > 0$, $0 < \rho^* < \rho_{\max}$.
4. Compute the derived quantities: $\Delta = D + 2\zeta$, and the constitutive-dependent quantities $M_* = M(\rho^*)$, $M_*' = M'(\rho^*)$, $P_*' = P'(\rho^*)$ (these require the constitutive functions, constructed in §2.1.3; the parameter record is completed after that step).
5. Compute the spectral quantities: $\mathscr{D}_0 = (DP_*' - \zeta/\tau)^2 - 4HP_*'/\tau$, $\gamma_0 = (DP_*' + \zeta/\tau)/2$, and $\omega = \sqrt{|\mathscr{D}_0|}/2$ if $\mathscr{D}_0 < 0$, else $\omega = 0$.
6. Classify the regime: Oscillatory if $\mathscr{D}_0 < 0$, Critical if $|\mathscr{D}_0| < 10^{-10}$, Monotonic if $\mathscr{D}_0 > 0$.
7. Freeze the record (mark as immutable).

**Validation checks.** The parameter validation is a sequence of assertions, each producing a fatal error if violated:

| Check | Condition | Error message |
|-------|-----------|--------------|
| Channel weight | $0 < D < 1$ | "D must be in (0, 1)" |
| Complementarity | $H = 1 - D > 0$ | "H must be positive" |
| Damping | $\zeta > 0$ | "Participation damping must be positive" |
| Time scale | $\tau > 0$ | "Participation time scale must be positive" |
| Equilibrium interior | $0 < \rho^* < \rho_{\max}$ | "Equilibrium must be interior to (0, ρ_max)" |
| Capacity bound | $\rho_{\max} > 0$ | "Capacity bound must be positive" |

These checks are performed before any computation and guarantee that the parameter record represents a well-posed ED system.

---

#### 2.1.2 Grid Creation

The second step constructs the spatial grid appropriate to the domain dimension and the chosen spatial method.

**Input.** The experiment specification provides:

- The spatial dimension $d \in \{1, 2, 3\}$.
- The number of interior grid points $N$ (or $N_x, N_y, N_z$ for anisotropic grids).
- The domain lengths $L$ (or $L_x, L_y, L_z$).
- The spatial method: `FD` (finite-difference, Method A) or `SPEC` (spectral, Method B).

**Grid construction for Method A.** The engine creates the `Grid1D`, `Grid2D`, or `Grid3D` record (§1.2.3):

1. Compute the grid spacing: $h = L/(N+1)$ (1D), or $h_x = L_x/(N_x + 1)$, $h_y = L_y/(N_y + 1)$ (2D).
2. Compute the total grid dimensions: $N_{\mathrm{grid}} = N + 2$ (1D), or $N_{\mathrm{grid}_x} = N_x + 2$, $N_{\mathrm{grid}_y} = N_y + 2$ (2D).
3. Compute the coordinate arrays: $x_j = jh$ for $j = 0, \ldots, N_{\mathrm{grid}} - 1$.
4. Freeze the grid record.

**Grid construction for Method B.** The engine creates the spectral grid:

1. Set the number of spectral modes: $N_{\mathrm{modes}} = N$.
2. Compute the eigenvalues: $\mu_k = (k\pi/L)^2$ for $k = 0, 1, \ldots, N_{\mathrm{modes}} - 1$.
3. Compute the de-aliased physical grid size: $N_{\mathrm{phys}} = \lfloor 3N/2\rfloor$.
4. Compute the physical-space coordinates: $x_j = jL/N_{\mathrm{phys}}$ for $j = 0, \ldots, N_{\mathrm{phys}} - 1$.
5. Freeze the spectral grid record.

**Validation checks.**

| Check | Condition | Error message |
|-------|-----------|--------------|
| Minimum resolution | $N \geq 8$ | "Grid too coarse for meaningful computation" |
| Positive domain | $L > 0$ (and $L_x, L_y, L_z > 0$) | "Domain length must be positive" |
| Even mode count (spectral) | $N_{\mathrm{modes}}$ is even | "Spectral mode count should be even for efficient DCT" |

The even-mode-count check for Method B is a recommendation (the DCT is most efficient for even $N$), not a hard requirement. Odd $N$ is accepted with a warning.

---

#### 2.1.3 Constitutive Function Construction

The third step creates the constitutive function objects $M(\rho)$ and $P(\rho)$ and validates them against the canonical constraints.

**Input.** The experiment specification provides:

- The constitutive type: `PowerLawLinear` (default), or a custom type.
- The constitutive parameters: $M_0$, $\beta$ (for $M$), $P_0$ (for $P$), and $\rho^*$, $\rho_{\max}$ (from the canonical parameters).

**Construction for the default type (`PowerLawLinear`).**

1. Define the mobility:
   - $M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta$
   - $M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta - 1}$

2. Define the penalty:
   - $P(\rho) = P_0\,(\rho - \rho^*)$
   - $P'(\rho) = P_0$

3. Package as the `Constitutive` record (§1.1.6) with the callable interface (`M.value`, `M.deriv`, `P.value`, `P.deriv`) and the stored parameters.

**Constitutive validation.** Apply the six checks of §1.1.4:

1. $M(\rho^*) > 0$: mobility positive at equilibrium.
2. $|M(\rho_{\max})| < 10^{-14}$: mobility vanishes at capacity bound.
3. $|P(\rho^*)| < 10^{-14}$: penalty vanishes at equilibrium.
4. $P'(\rho^*) > 0$: penalty strictly increasing at equilibrium.
5. $P'(\rho) > 0$ at 100 uniformly spaced sample points in $[0, \rho_{\max}]$: penalty monotonicity across the domain.
6. $M(\rho^*)$, $M'(\rho^*)$, $P'(\rho^*)$ all finite: regularity at equilibrium.

**Complete the parameter record.** After the constitutive functions are constructed, compute and store the derived quantities that depend on them: $M_* = M(\rho^*)$, $M_*' = M'(\rho^*)$, $P_*' = P'(\rho^*)$, and the spectral quantities $\mathscr{D}_0$, $\gamma_0$, $\omega$ (§2.1.1, Step 5).

---

#### 2.1.4 Initial Condition Evaluation

The fourth step evaluates the chosen initial condition on the grid and stores the result in the density array.

**Input.** The experiment specification provides:

- The IC type: `A`, `B`, `C`, `D`, `Homogeneous`, or `Custom`.
- The IC parameters (amplitude $A$, mode number $n$, width $\sigma$, center $x_0$, margin $\delta$, participation $v_0$, etc.).

**Evaluation for each standard IC type.**

**IC-A (Single-mode perturbation).**

For each grid point $j$:

$$
\rho_j = \rho^* + A\cos(n\pi x_j/L).
$$

Default: $A = 0.05$, $n = 1$, $v_0 = 0$.

The IC is evaluated on the Method A grid ($x_j = jh$) or the Method B physical-space grid ($x_j = jL/N_{\mathrm{phys}}$), whichever is active. For Method B, the spectral coefficients are computed directly: $\hat{u}_k = A/\sqrt{2/L}$ for $k = n$ and $\hat{u}_k = 0$ for $k \neq n$ (using the normalization of the Neumann eigenfunctions). This avoids the round-trip transform and is exact to machine precision.

**IC-B (Multi-mode perturbation).**

For each grid point $j$:

$$
\rho_j = \rho^* + \sum_{m=1}^{N_{\mathrm{modes}}} A_m\cos(m\pi x_j/L).
$$

Default: $A_m = 0.1/m^2$, $N_{\mathrm{modes}} = 8$, $v_0 = 0$.

For Method B, the spectral coefficients are set directly: $\hat{u}_k = A_k/\sqrt{2/L}$ for $k = 1, \ldots, N_{\mathrm{modes}}$ and $\hat{u}_k = 0$ otherwise.

**IC-C (Localized Gaussian perturbation).**

For each grid point $j$:

$$
\rho_j = \rho^* + A\exp\!\left(-\frac{(x_j - x_0)^2}{2\sigma^2}\right).
$$

Default: $A = 0.3$, $x_0 = L/2$, $\sigma = 0.05$, $v_0 = 0$.

The Gaussian is evaluated in physical space for both methods. For Method B, the spectral coefficients are obtained by applying the forward DCT to the physical-space values on the $N_{\mathrm{phys}}$-point grid, then truncating to $N_{\mathrm{modes}}$ modes. The Gaussian does not satisfy the Neumann condition exactly ($\partial_x\rho(0) \neq 0$ unless $x_0 = 0$ or the Gaussian tails are negligible at the boundary), but the DCT projection onto the Neumann basis automatically enforces it. For the default parameters ($x_0 = 0.5$, $\sigma = 0.05$), the Gaussian tails at $x = 0$ and $x = 1$ are $\exp(-50) \approx 10^{-22}$, so the Neumann violation is below machine precision.

**IC-D (Near-capacity perturbation).**

For each grid point $j$:

$$
\rho_j = \rho_{\max} - \delta + A\cos(\pi x_j/L).
$$

Default: $\delta = 0.05$, $A = 0.02$, $v_0 = 0$.

This IC places the density near $\rho_{\max}$. The constraint $|A| < \delta$ must be verified to ensure that $\rho_j < \rho_{\max}$ at all grid points; the engine checks $\max_j\rho_j < \rho_{\max}$ after evaluation and halts if violated.

**Homogeneous perturbation (for regime-geometry experiments).**

$$
\rho_j = \rho^* + A \qquad \text{(spatially constant)}, \qquad v_0 = v_{\mathrm{init}}.
$$

This IC has no spatial structure ($\nabla\rho = 0$, $C_{\mathrm{ED}} = 0$) and is used for the pure ODE dynamics of the homogeneous mode (Atlas §2.1–2.3).

**Custom IC.**

The experiment specification provides an explicit formula or a callable function $\rho_0(x)$ and a value $v_0$. The engine evaluates $\rho_0(x_j)$ at each grid point and sets $v = v_0$. For Method B, the forward DCT is applied to obtain the spectral coefficients.

**Post-evaluation checks.**

| Check | Condition | Action |
|-------|-----------|--------|
| Positivity | $\min_j\rho_j > 0$ | Fatal if violated; IC places density at or below zero |
| Sub-capacity | $\max_j\rho_j < \rho_{\max}$ | Fatal if violated; IC places density at or above capacity |
| Finite values | All $\rho_j$ and $v_0$ are finite | Fatal if NaN or Inf detected |
| Neumann compatibility (Method B) | $|(\nabla_h\rho)_0|$ and $|(\nabla_h\rho)_{N+1}|$ below $10^{-10}$ | Warning if the IC has significant boundary gradient |

---

#### 2.1.5 Memory Allocation and Precomputation

The fifth step allocates all workspace arrays and precomputes all quantities that remain constant during the integration.

**Memory allocation.** The following arrays are allocated once and reused at every time step:

*Method A workspace:*

| Array | Shape | Purpose |
|-------|-------|---------|
| $\boldsymbol{\rho}$ | $(N_{\mathrm{grid}},)$ or $(N_{\mathrm{grid}_x}, N_{\mathrm{grid}_y})$ | Current density state |
| $\boldsymbol{\rho}_{\mathrm{prev}}$ | Same as $\boldsymbol{\rho}$ | Previous-step density (for diagnostics) |
| $\mathbf{Lap}$ | Same as $\boldsymbol{\rho}$ | Discrete Laplacian values |
| $\mathbf{Grad2}$ | Same as $\boldsymbol{\rho}$ | Discrete gradient-squared values |
| $\mathbf{F}$ | Same as $\boldsymbol{\rho}$ | Operator values $F_h[\boldsymbol{\rho}]$ |
| $\mathbf{RHS}$ | Same as $\boldsymbol{\rho}$ | Right-hand side of implicit system |
| $\mathbf{M}_{\mathrm{vals}}$ | Same as $\boldsymbol{\rho}$ | Pointwise mobility $M(\rho_j)$ |
| $\mathbf{M}'_{\mathrm{vals}}$ | Same as $\boldsymbol{\rho}$ | Pointwise mobility derivative $M'(\rho_j)$ |
| $\mathbf{P}_{\mathrm{vals}}$ | Same as $\boldsymbol{\rho}$ | Pointwise penalty $P(\rho_j)$ |
| $\mathbf{P}'_{\mathrm{vals}}$ | Same as $\boldsymbol{\rho}$ | Pointwise penalty derivative $P'(\rho_j)$ |
| $\mathbf{A}_{\mathrm{lower}}$, $\mathbf{A}_{\mathrm{diag}}$, $\mathbf{A}_{\mathrm{upper}}$ | $(N_{\mathrm{grid}} - 1,)$, $(N_{\mathrm{grid}},)$, $(N_{\mathrm{grid}} - 1,)$ | Tridiagonal implicit matrix (1D) |

*Method B workspace:*

| Array | Shape | Purpose |
|-------|-------|---------|
| $\hat{\mathbf{u}}$ | $(N_{\mathrm{modes}},)$ | Current spectral state |
| $\hat{\mathbf{u}}_{\mathrm{prev}}$ | Same | Previous-step spectral state |
| $\boldsymbol{\mu}$ | $(N_{\mathrm{modes}},)$ | Neumann eigenvalues (precomputed) |
| $\boldsymbol{\alpha}$ | $(N_{\mathrm{modes}},)$ | Modal decay coefficients (precomputed) |
| $\mathbf{c}$ | $(N_{\mathrm{modes}},)$ | Linear rates $c_k = -DM_*\mu_k$ (precomputed) |
| $\mathbf{E}$, $\mathbf{E}_2$ | $(N_{\mathrm{modes}},)$ | Exponential factors $e^{c_k\Delta t}$, $e^{c_k\Delta t/2}$ (precomputed) |
| $\boldsymbol{\phi}_{31}$, $\boldsymbol{\phi}_{32}$, $\boldsymbol{\phi}_{33}$ | $(N_{\mathrm{modes}},)$ | ETD-RK4 weight functions (precomputed) |
| $\boldsymbol{\varphi}_1$, $\boldsymbol{\varphi}_{1h}$ | $(N_{\mathrm{modes}},)$ | $\varphi_1(c_k\Delta t)$, $\varphi_1(c_k\Delta t/2)$ (precomputed) |
| Pseudospectral workspace | $(6 \times N_{\mathrm{phys}},)$ | Physical-space buffers (§1.2.7) |
| $\hat{\mathbf{a}}$, $\hat{\mathbf{b}}$, $\hat{\mathbf{c}}_{\mathrm{rk}}$, $\hat{\mathbf{d}}$ | $(N_{\mathrm{modes}},)$ each | ETD-RK4 stage evaluations |

*Observable workspace:*

| Array | Shape | Purpose |
|-------|-------|---------|
| $\mathbf{obs}$ | `Observables` record | Current-step observables |
| $\mathbf{ts}$ | `TimeSeries` record | Accumulated time series |

All arrays are initialized to zero. The density array $\boldsymbol{\rho}$ (or $\hat{\mathbf{u}}$) is then overwritten with the initial condition from §2.1.4.

**Precomputation.** The following quantities are computed once and stored for the duration of the integration:

*Spectral quantities (Method B):*

1. Eigenvalues $\mu_k = (k\pi/L)^2$ for $k = 0, \ldots, N_{\mathrm{modes}} - 1$.
2. Decay coefficients $\alpha_k = M_*\mu_k + P_*'$.
3. Linear rates $c_k = -DM_*\mu_k$.
4. Exponential factors: $E_k = e^{c_k\Delta t}$, $E_{2,k} = e^{c_k\Delta t/2}$.
5. ETD weight functions $\phi_{31}(c_k\Delta t)$, $\phi_{32}(c_k\Delta t)$, $\phi_{33}(c_k\Delta t)$, using the Taylor-series evaluation for $|c_k\Delta t| < 10^{-2}$ (Atlas §10.1.3).
6. $\varphi_1$ values: $\varphi_1(c_k\Delta t) = (e^{c_k\Delta t} - 1)/(c_k\Delta t)$ and $\varphi_1(c_k\Delta t/2)$, with Taylor evaluation for small arguments.

*Participation integrator (both methods):*

7. Exponential decay factor: $e_v = e^{-\zeta\Delta t/\tau}$.
8. Driving coefficient: $f_v = (1 - e^{-\zeta\Delta t/\tau})/\zeta$.
9. Half-step variants: $e_{v,h} = e^{-\zeta\Delta t/(2\tau)}$, $f_{v,h} = (1 - e^{-\zeta\Delta t/(2\tau)})/\zeta$.

*Static derived quantities (both methods):*

10. Equilibrium constitutive values: $M_*$, $M_*'$, $P_*'$.
11. Equilibrium energy: $\mathcal{E}(\rho^*, 0) = 0$ (the potential $\Phi(\rho^*)= 0$ by construction).
12. Lyapunov coupling parameter: $\sigma = 0.01$ (or as specified).

All precomputed arrays depend on $\Delta t$ (through the exponential factors and weight functions). If the time step changes during the integration (§1.6.2, adaptive reduction), the affected precomputed quantities must be recomputed. The engine tracks whether $\Delta t$ has changed since the last precomputation and recomputes if necessary. The recomputation cost is $O(N_{\mathrm{modes}})$ — a single pass over the spectral arrays — and is negligible relative to the per-step cost.

---

#### 2.1.6 Readiness Check

The final step of initialization is a comprehensive readiness check that confirms the entire computational infrastructure is correctly assembled before the first time step.

**Checklist.**

| # | Check | Verified by |
|---|-------|-------------|
| 1 | Parameter record is complete and frozen | All derived quantities non-NaN |
| 2 | Grid record is complete and frozen | $h > 0$, $N_{\mathrm{grid}} > 0$, coordinates monotonically increasing |
| 3 | Constitutive functions pass all six validation checks | §2.1.3 |
| 4 | Initial condition is in the admissible region | $0 < \rho_j < \rho_{\max}$ for all $j$; $v_0$ finite |
| 5 | Initial energy is finite | $\mathcal{E}[\boldsymbol{\rho}^0, v_0] < \infty$ (computed by quadrature of $\Phi$) |
| 6 | Time step satisfies CFL | $\Delta t \leq \Delta t_{\mathrm{CFL}}$ (computed from the initial state) |
| 7 | Workspace arrays are allocated and zeroed | No null pointers; correct shapes |
| 8 | Precomputed quantities are finite | All $E_k$, $\phi_{3i}$, $\varphi_1$ values non-NaN, non-Inf |
| 9 | Discrete Laplacian satisfies structural tests | $\|\mathbf{L}_h\mathbf{1}\|_\infty < 10^{-14}$; symmetry (Method A only) |
| 10 | Observable record is initialized | $t = 0$; initial observables computed and stored |

If all ten checks pass, the engine transitions to the time-stepping phase (§2.2). If any check fails, the engine halts with a diagnostic message identifying the failed check, and no integration is performed.

**Initial observable computation.** As part of Check 10, the engine computes all observables (§1.1.6, `Extract_Observables`) at $t = 0$ from the initial state and stores them as the first entry of the time series. This provides the $t = 0$ reference values for the energy, complexity, Lyapunov functional, modal amplitudes, and dissipation channels. It also verifies that the observable extraction pipeline is functional before the integration begins.

**Initialization summary.** The complete initialization sequence is:

$$
\text{Parameters} \to \text{Grid} \to \text{Constitutive} \to \text{IC} \to \text{Allocation} \to \text{Precomputation} \to \text{Readiness} \to \text{Ready.}
$$

The sequence is strictly ordered: each step depends on the outputs of previous steps (the constitutive functions require the parameters; the IC evaluation requires the grid and the constitutive functions; the precomputation requires the constitutive values and the time step; the readiness check requires everything). No step can be parallelized with a preceding step, but the internal operations within each step (e.g., evaluating $\rho_0(x_j)$ at all grid points) are independently parallelizable.

---

### 2.2 Parameter Loading

Section 2.1.1 described the parameter loading step within the initialization sequence at the level of its logical position and validation checks. This subsection provides the full specification: the five canonical parameter sets stored by the engine, the override mechanism for parameter sweeps and custom experiments, the complete validation hierarchy, and the consistency checks that detect contradictions between parameter values before any computation is performed.

---

#### 2.2.1 The Five Canonical Parameter Sets

The simulation engine stores the five canonical parameter sets as named, immutable records. These are the parameter sets defined in Atlas §10.2.1, reproduced here with their full specifications for implementation reference.

**Set I — Deep Oscillatory.**

| Field | Value |
|-------|-------|
| $D$ | $0.3$ |
| $\zeta$ | $0.1$ |
| $\tau$ | $1.0$ |
| $\rho^*$ | $0.5$ |
| $\rho_{\max}$ | $1.0$ |
| $M_0$ | $1.0$ |
| $\beta$ | $2.0$ |
| $P_0$ | $1.0$ |

**Set II — Moderate Oscillatory.**

| Field | Value |
|-------|-------|
| $D$ | $0.6$ |
| $\zeta$ | $0.5$ |
| $\tau$ | $1.0$ |
| $\rho^*$ | $0.5$ |
| $\rho_{\max}$ | $1.0$ |
| $M_0$ | $1.0$ |
| $\beta$ | $2.0$ |
| $P_0$ | $1.0$ |

**Set III — Near-Critical.**

| Field | Value |
|-------|-------|
| $D$ | $0.8$ |
| $\zeta$ | $1.8$ |
| $\tau$ | $1.0$ |
| $\rho^*$ | $0.5$ |
| $\rho_{\max}$ | $1.0$ |
| $M_0$ | $1.0$ |
| $\beta$ | $2.0$ |
| $P_0$ | $1.0$ |

**Set IV — Deep Monotonic.**

| Field | Value |
|-------|-------|
| $D$ | $0.9$ |
| $\zeta$ | $5.0$ |
| $\tau$ | $1.0$ |
| $\rho^*$ | $0.5$ |
| $\rho_{\max}$ | $1.0$ |
| $M_0$ | $1.0$ |
| $\beta$ | $2.0$ |
| $P_0$ | $1.0$ |

**Set V — High Participation Coupling.**

| Field | Value |
|-------|-------|
| $D$ | $0.2$ |
| $\zeta$ | $0.3$ |
| $\tau$ | $0.5$ |
| $\rho^*$ | $0.5$ |
| $\rho_{\max}$ | $1.0$ |
| $M_0$ | $1.0$ |
| $\beta$ | $2.0$ |
| $P_0$ | $1.0$ |

The five sets share the same constitutive parameters ($M_0 = 1$, $\beta = 2$, $P_0 = 1$, $\rho^* = 0.5$, $\rho_{\max} = 1.0$) and differ only in the canonical dynamical parameters ($D$, $\zeta$, $\tau$). This design isolates the effect of the dynamical parameters from the constitutive form — every difference between sets is attributable to the channel partition, damping, and time scale, not to the mobility or penalty shape.

**Storage.** The five sets are stored as a dictionary (or equivalent associative container) keyed by the set name: `{"I": SetI, "II": SetII, "III": SetIII, "IV": SetIV, "V": SetV}`. Retrieval is by name: `params = LOAD_SET("II")` returns a copy of Set II. The stored sets are never modified; overrides produce new records (§2.2.2).

---

#### 2.2.2 User-Defined Overrides

Many Atlas experiments require parameter values that differ from the five canonical sets. These arise in three contexts:

1. **Parameter sweeps.** An experiment varies a single parameter (e.g., $\zeta$) across a range of values while holding all others fixed (e.g., Experiment 8.1: 41 values of $\zeta$ at fixed $D = 0.5$). Each sweep point requires a distinct parameter record.

2. **Critical-point experiments.** Experiments on or near the critical surface $\Sigma$ require parameter values computed from the critical condition $\mathscr{D}_0 = 0$ (e.g., Experiment 2.5: $\zeta_c = D + 2\sqrt{1-D}$), which do not coincide with any canonical set.

3. **Custom experiments.** Cross-domain demonstrations (Atlas §9) and constitutive surveys use parameter values chosen for specific physical analogies or constitutive variations.

**Override mechanism.** The engine supports overrides through a two-step process:

1. **Load a base set.** Start from one of the five canonical sets, or from a blank record with all fields set to `undefined`.

2. **Apply overrides.** For each parameter to be changed, set the new value explicitly. The override replaces the base value; unmodified parameters retain the base value.

The result is a new `CanonicalParams` record (a copy, not a mutation of the base set) with the overridden values and all derived quantities recomputed from the new primary values.

**Override rules.** The following rules govern the override process:

- **$H$ cannot be overridden directly.** It is always computed as $H = 1 - D$. If the user attempts to set $H$, the engine issues a warning and ignores the override (enforcing Principle 2).

- **Derived quantities cannot be overridden.** The fields $\Delta$, $M_*$, $M_*'$, $P_*'$, $\mathscr{D}_0$, $\gamma_0$, $\omega$, and `regime` are always computed from the primary parameters and the constitutive functions. They cannot be set manually.

- **Constitutive parameters can be overridden.** The values $M_0$, $\beta$, $P_0$ can be changed, producing a different constitutive function while retaining the canonical structure. The constitutive validation (§2.1.3) is reapplied after any constitutive override.

- **Multiple overrides are applied simultaneously.** If the experiment specifies overrides for both $D$ and $\zeta$ (e.g., a grid sweep across the $(D, \zeta)$-plane), both are applied before the derived quantities are computed. The order of override application does not matter (the derived quantities depend on the final primary values, not on the order in which they were set).

**Sweep construction.** For a parameter sweep, the engine generates a list of parameter records:

1. Load the base set.
2. For each sweep value $p_i$ of the swept parameter $p$:
   - Copy the base set.
   - Override $p$ with $p_i$.
   - Recompute derived quantities.
   - Store the record in the sweep list.

The sweep list is an ordered array of `CanonicalParams` records, one per sweep point. Each record is independent and self-contained — it carries all the information needed to run the corresponding experiment without reference to the base set or the other sweep points.

---

#### 2.2.3 Validation of Parameter Ranges

Every parameter record — whether loaded from a canonical set, produced by an override, or constructed for a sweep — is validated against the structural constraints before it is accepted. The validation is a hierarchy of three levels: range checks, constitutive checks, and consistency checks.

##### 2.2.3.1 Level 1: Range Checks (Primary Parameters)

These checks verify that each primary parameter falls within its structurally permitted range.

| Parameter | Permitted range | Boundary behavior | Check |
|-----------|----------------|-------------------|-------|
| $D$ | $(0, 1)$ | Open interval; $D = 0$ and $D = 1$ degenerate the system | $0 < D < 1$ |
| $\zeta$ | $(0, \infty)$ | Must be strictly positive | $\zeta > 0$ |
| $\tau$ | $(0, \infty)$ | Must be strictly positive | $\tau > 0$ |
| $\rho^*$ | $(0, \rho_{\max})$ | Must be interior to the density range | $0 < \rho^* < \rho_{\max}$ |
| $\rho_{\max}$ | $(0, \infty)$ | Must be positive | $\rho_{\max} > 0$ |
| $M_0$ | $(0, \infty)$ | Must be positive | $M_0 > 0$ |
| $\beta$ | $(0, \infty)$ | Must be positive; $\beta \geq 1$ recommended for smooth $M'$ | $\beta > 0$ |
| $P_0$ | $(0, \infty)$ | Must be positive (strict penalty monotonicity) | $P_0 > 0$ |

Each failed check produces a fatal error with a diagnostic message identifying the parameter, its value, and its permitted range. No computation proceeds until all range checks pass.

**Boundary warnings.** In addition to the hard range checks, the engine issues non-fatal warnings for parameter values that are technically permitted but numerically problematic:

| Condition | Warning |
|-----------|---------|
| $D < 0.01$ or $D > 0.99$ | "Extreme channel partition: $D$ near boundary of $(0,1)$" |
| $\zeta > 100$ | "Very large damping: participation equation may be stiff" |
| $\tau < 0.01$ | "Very small participation time scale: ODE may be stiff" |
| $\rho^* / \rho_{\max} < 0.01$ or $\rho^* / \rho_{\max} > 0.99$ | "Equilibrium near boundary of density range" |
| $\beta < 1$ | "Sub-linear mobility vanishing: $M'$ diverges at $\rho_{\max}$" |
| $\beta > 4$ | "High-order mobility vanishing: very soft barrier" |

##### 2.2.3.2 Level 2: Constitutive Checks

These checks verify that the constitutive functions satisfy the canonical constraints (§1.1.4, §2.1.3). They require the constitutive functions to be constructed, so they are performed after Level 1.

| Check | Condition | Level |
|-------|-----------|-------|
| Mobility at equilibrium | $M(\rho^*) > 0$ | Fatal |
| Mobility at capacity | $|M(\rho_{\max})| < 10^{-14}$ | Fatal |
| Penalty at equilibrium | $|P(\rho^*)| < 10^{-14}$ | Fatal |
| Penalty slope at equilibrium | $P'(\rho^*) > 0$ | Fatal |
| Penalty global monotonicity | $P'(\rho) > 0$ at 100 sample points in $[0, \rho_{\max}]$ | Warning |
| Regularity | $M(\rho^*)$, $M'(\rho^*)$, $P'(\rho^*)$ finite | Fatal |

##### 2.2.3.3 Level 3: Consistency Checks

These checks verify relationships between parameters that are not captured by individual range checks.

**Channel complementarity.** Verify that the stored $H$ equals $1 - D$ to machine precision:

$$
|H - (1 - D)| < 10^{-15}.
$$

This is a redundant check (the engine computes $H = 1 - D$), but it catches implementation errors where $H$ might be set independently.

**Equilibrium interiority.** Verify that $\rho^*$ is strictly interior to the density range with a margin sufficient for the constitutive functions to be well-behaved:

$$
\rho^* > \delta_{\mathrm{floor}} \qquad \text{and} \qquad \rho_{\max} - \rho^* > \delta_{\mathrm{floor}},
$$

where $\delta_{\mathrm{floor}} = 10^{-12}$. This prevents the equilibrium from being so close to $0$ or $\rho_{\max}$ that the energy potential $\Phi$ is nearly singular at $\rho^*$.

**Derived-quantity finiteness.** After computing all derived quantities, verify:

$$
|M_*| < \infty, \quad |M_*'| < \infty, \quad |P_*'| < \infty, \quad |\mathscr{D}_0| < \infty, \quad |\gamma_0| < \infty.
$$

A non-finite derived quantity indicates a pathological parameter combination (e.g., $\tau = 0$ would make $\zeta/\tau = \infty$).

**Spectral gap positivity.** Verify that the spectral gap is strictly positive:

$$
\gamma := \min\!\bigl(\gamma_{\mathrm{hom}},\; D\alpha_1\bigr) > 0,
$$

where $\gamma_{\mathrm{hom}} = \gamma_0$ in the oscillatory case and $\gamma_{\mathrm{hom}} = \gamma_0 - \frac{1}{2}\sqrt{\mathscr{D}_0}$ in the overdamped case (Lemma C.31). The spectral gap is positive for all parameter values satisfying the range checks (this is proved in Corollary C.18), so this check is a verification of the analytic result at the specific parameter values. A zero or negative spectral gap would indicate an error in the derived-quantity computation.

**Energy-barrier existence.** Verify that the density potential diverges at the capacity bound:

$$
\Phi(\rho_{\max} - 10^{-6}) > 10^3.
$$

This is a numerical spot-check of Proposition C.11. The threshold $10^3$ is arbitrary but ensures that the barrier is strong enough to confine the density at any energy level encountered in the Atlas experiments ($\mathcal{E}_0 \lesssim 100$ for the most extreme ICs).

---

#### 2.2.4 Parameter Record Finalization

After all three validation levels pass, the parameter record is finalized:

1. **Derived quantities are computed.** All fields of the `CanonicalParams` record (§1.1.6) are populated: the six primary parameters, the eight derived quantities, and the regime classification.

2. **The record is frozen.** The record is marked as immutable. Any subsequent attempt to modify a field raises a fatal error. This prevents accidental parameter drift during long integrations or parameter sweeps.

3. **The record is logged.** A complete printout of the parameter record (all primary and derived fields) is written to the diagnostic output. This printout is the authoritative record of the parameters used for the experiment and is included in the output metadata for reproducibility.

4. **The regime is reported.** The engine prints a one-line summary:

   - "Regime: Oscillatory (D₀ = −2.76, ω = 0.831, γ₀ = 0.200)" for Set I.
   - "Regime: Monotonic (D₀ = +16.41, λ₊ = −0.924, λ₋ = −4.976)" for Set IV.
   - "Regime: Critical (|D₀| = 2.0e−11, λ_c = −1.247)" for a critical-point experiment.

This summary provides immediate feedback on the dynamical character of the parameter set without requiring the user to compute $\mathscr{D}_0$ manually.

---

#### 2.2.5 Parameter Loading for Sweep Experiments

Sweep experiments (Atlas §§2.1.3, 2.2.3, 3.2.4, 4.2.3, 4.2.4, 5.2.2, 7.4.2, 8.1.2, 8.3.2–8.3.5) require an array of parameter records, one per sweep point. The loading process is:

1. **Specify the sweep.** The experiment provides:
   - The base set (e.g., "I" or "Custom").
   - The swept parameter name (e.g., "$\zeta$").
   - The sweep values (e.g., $\{0.05, 0.1, 0.2, 0.3, 0.5\}$ or a linspace/logspace specification).

2. **Generate the sweep array.** For each sweep value $p_i$:
   - Copy the base set.
   - Override the swept parameter: $\zeta \leftarrow p_i$.
   - Recompute all derived quantities.
   - Run the full three-level validation.
   - Store the validated, frozen record.

3. **Validate the sweep as a whole.** In addition to the per-record validation, the engine checks:
   - **Monotonicity of the swept parameter.** The sweep values are in strictly increasing order (to ensure reproducible ordering of the output).
   - **No duplicate values.** $|p_i - p_j| > 10^{-14}$ for all $i \neq j$.
   - **Regime transition detection.** If the discriminant $\mathscr{D}_0$ changes sign across the sweep (i.e., the sweep crosses the Boundary Surface $\Sigma$), the engine logs the approximate critical value $p_c$ by linear interpolation: $p_c \approx p_i + (p_{i+1} - p_i)\,|\mathscr{D}_0(p_i)|/(|\mathscr{D}_0(p_i)| + |\mathscr{D}_0(p_{i+1})|)$. This assists the user in identifying the transition point.

4. **Report the sweep summary.** The engine prints a table:

   | Point | $p$ value | $\mathscr{D}_0$ | Regime |
   |-------|-----------|------------------|--------|
   | 1 | $p_1$ | $\mathscr{D}_0(p_1)$ | Oscillatory/Monotonic |
   | 2 | $p_2$ | $\mathscr{D}_0(p_2)$ | ... |
   | ... | ... | ... | ... |

   If a regime transition is detected, the row containing the sign change is highlighted.

**Multi-parameter sweeps.** For grid sweeps across two parameters (e.g., the $(D, \zeta)$-plane of Experiment 8.5), the engine generates a two-dimensional array of parameter records by iterating over the outer product of the two sweep vectors. The per-record and sweep-level validations are applied to each record independently. The regime-transition detection is extended to identify the boundary curve $\Sigma$ across the grid by marking all adjacent pairs of grid points where $\mathscr{D}_0$ changes sign.

---

#### 2.2.6 Summary of the Parameter Loading Pipeline

| Stage | Input | Output | Failure mode |
|-------|-------|--------|-------------|
| Load base set | Set name or blank | Raw parameter values | Fatal if unknown set name |
| Apply overrides | Override list | Modified parameter values | Warning if $H$ overridden |
| Level 1 validation | Primary parameters | Range-checked values | Fatal if any range violated |
| Constitutive construction | $M_0$, $\beta$, $P_0$, $\rho^*$, $\rho_{\max}$ | Callable $M$, $M'$, $P$, $P'$ | Fatal if constitutive check fails |
| Level 2 validation | Constitutive functions | Constitutive-verified values | Fatal if monotonicity or regularity fails |
| Derived computation | All primary + constitutive | $\Delta$, $M_*$, $\mathscr{D}_0$, $\gamma_0$, $\omega$, regime | — |
| Level 3 validation | Full record | Consistency-verified record | Fatal if gap $\leq 0$ or barrier weak |
| Freeze and log | Verified record | Immutable `CanonicalParams` | — |

The pipeline is executed once per parameter record (once per experiment for single-point experiments, once per sweep point for sweeps). The total cost is negligible — dominated by the 100-point penalty monotonicity check in Level 2, which requires 100 constitutive evaluations ($\sim 10\,\mu$s). The validation is the price of the defensive computation principle (§0.3): it catches parameter errors before they propagate into hours of wasted integration time.

---

### 2.3 Time Loop Structure

After initialization (§2.1) completes and the readiness check passes, the simulation engine enters the time loop — the central computational phase that advances the state $(\boldsymbol{\rho}^n, v^n)$ from $t = 0$ to $t = T_{\mathrm{final}}$ one time step at a time. This subsection specifies the complete structure of the loop: the ordering of operations within each step (§2.3.1), the update sequence for the density and participation (§2.3.2), the diagnostic and observable sampling schedule (§2.3.3), and the criteria under which the loop terminates (§2.3.4).

---

#### 2.3.1 Main Loop Structure

The time loop iterates over a step counter $n = 0, 1, 2, \ldots$ until a stopping criterion is met. Each iteration advances the state from $(t_n, \boldsymbol{\rho}^n, v^n)$ to $(t_{n+1}, \boldsymbol{\rho}^{n+1}, v^{n+1})$ with $t_{n+1} = t_n + \Delta t^n$, where $\Delta t^n$ is the (possibly adaptive) time step at step $n$.

The operations within each iteration are executed in a fixed order. The order is not arbitrary — it reflects the dependency structure of the semi-implicit scheme and the defensive computation framework. The complete per-step sequence is:

**Phase 1: Pre-step diagnostics.**

1. **Proximity monitoring.** Compute $\delta^n = \rho_{\max} - \max_j\rho_j^n$ (§1.6.1). Log a diagnostic if $\delta^n \leq \delta_{\mathrm{warn}}$.

2. **Time-step adjustment.** If $\delta^n \leq \delta_{\mathrm{crit}}$: apply adaptive time-step reduction $\Delta t^n \leftarrow \Delta t_0 \cdot \delta^n/\delta_{\mathrm{crit}}$ (§1.6.2). If $\delta^n > 2\delta_{\mathrm{crit}}$ and the time step was previously reduced: restore $\Delta t^n \leftarrow \min(\Delta t_0, \Delta t_{\mathrm{CFL}})$. If the time step changes from the previous step, recompute the $\Delta t$-dependent precomputed quantities (exponential factors, ETD weight functions; §2.1.5).

3. **History storage.** If the observable extraction requires a previous-step state (e.g., for finite-difference computation of $d\mathcal{E}/dt$): copy $\boldsymbol{\rho}^n \to \boldsymbol{\rho}_{\mathrm{prev}}$ and $v^n \to v_{\mathrm{prev}}$.

**Phase 2: State update.**

4. **Density update.** Advance $\boldsymbol{\rho}^n \to \boldsymbol{\rho}^{n+1}$ using the chosen scheme (§2.3.2).

5. **Participation update.** Advance $v^n \to v^{n+1}$ using the exponential integrator (§2.3.2).

6. **Time advance.** Set $t_{n+1} = t_n + \Delta t^n$.

**Phase 3: Post-step safeguards.**

7. **Positivity enforcement.** Scan $\boldsymbol{\rho}^{n+1}$ for violations of $0 < \rho_j < \rho_{\max}$. Project if necessary (§1.7.2). Log any projection event.

8. **Finiteness check.** Verify that all $\rho_j^{n+1}$ and $v^{n+1}$ are finite (not NaN, not Inf). Halt with diagnostic if any non-finite value is detected.

9. **Energy recomputation (if projection occurred).** If Step 7 activated the projection, recompute $\mathcal{E}^{n+1}$ from the projected state (§1.7.3).

**Phase 4: Diagnostics and output.**

10. **Energy monotonicity check.** Compute $\mathcal{E}^{n+1}$ (if not already computed in Step 9). Compare to $\mathcal{E}^n$: if $\mathcal{E}^{n+1} > \mathcal{E}^n + \text{tol}$, log a warning; if $\mathcal{E}^{n+1} > \mathcal{E}^n + 10\cdot\text{tol}$, halt (§1.8.5).

11. **Observable sampling.** If the current step is a designated output step (§2.3.3): extract all observables from $(\boldsymbol{\rho}^{n+1}, v^{n+1})$ and append to the time series.

12. **Step counter and stopping check.** Increment $n \leftarrow n + 1$. Evaluate the stopping criteria (§2.3.4). If any criterion is met, exit the loop.

The loop then returns to Phase 1 for the next step.

---

#### 2.3.2 Update Order: Density Then Participation

The state update (Phase 2) advances the density and participation in a specific order that is consistent with the semi-implicit and ETD formulations.

##### 2.3.2.1 Method A: Semi-Implicit Update

The update within a single time step proceeds as:

**Step 4a: Evaluate constitutive functions.** Compute $M(\rho_j^n)$, $M'(\rho_j^n)$, $P(\rho_j^n)$ at all grid points. Store in the constitutive buffers (§1.2.6).

**Step 4b: Evaluate discrete spatial operators.** Compute the discrete Laplacian $(\nabla_h^2\boldsymbol{\rho}^n)$ and the discrete gradient-squared $(|\nabla_h\boldsymbol{\rho}^n|^2)$ from $\boldsymbol{\rho}^n$ using the stencils of §1.3.1.

**Step 4c: Evaluate the full discrete operator.** Assemble $F_h[\boldsymbol{\rho}^n]_j = M(\rho_j^n)(\nabla_h^2\rho^n)_j + M'(\rho_j^n)(|\nabla_h\rho^n|^2)_j - P(\rho_j^n)$ at all grid points.

**Step 4d: Compute the spatial average.** $\bar{F}^n = N_{\mathrm{grid}}^{-1}\sum_j F_h[\boldsymbol{\rho}^n]_j$. This scalar is needed for the participation update.

**Step 4e: Assemble the explicit right-hand side.** For implicit Euler:

$$
R_j = \rho_j^n + \Delta t\bigl[D\,M'(\rho_j^n)(|\nabla_h\rho^n|^2)_j - D\,P(\rho_j^n) + H\,v^n\bigr].
$$

For Crank–Nicolson: apply the explicit half of the diffusion as well (§1.4.1.2).

**Step 4f: Assemble and solve the implicit system.** Build the tridiagonal (1D) or banded (2D) matrix $\mathbf{A}$ with the density-dependent mobility coefficients. Solve $\mathbf{A}\boldsymbol{\rho}^{n+1} = \mathbf{R}$ by the Thomas algorithm (1D) or banded solver (2D).

**Step 5: Update participation.** Compute $v^{n+1}$ from $v^n$ and $\bar{F}^n$ using the exponential integrator:

$$
v^{n+1} = v^n\,e^{-\zeta\Delta t/\tau} + \frac{\bar{F}^n}{\zeta}(1 - e^{-\zeta\Delta t/\tau}).
$$

The participation update uses $\bar{F}^n$ (computed from $\boldsymbol{\rho}^n$, not $\boldsymbol{\rho}^{n+1}$). This is the explicit coupling direction: the participation sees the operator output at the *current* time level. The density sees the participation at the current level through $H\,v^n$ in the right-hand side. The coupling is therefore **symmetric in time level**: both $\rho$ and $v$ are updated using the other's value at time $t_n$, not at $t_{n+1}$. This avoids the need for an implicit coupling iteration.

##### 2.3.2.2 Method B: ETD-RK4 Update

The ETD-RK4 update (§1.4.2.2) interleaves density and participation substeps:

**Substep 1 (at $t_n$):** Evaluate $\hat{\mathcal{N}}(\hat{\mathbf{u}}^n, v^n)$ via the pseudospectral pipeline. This requires one inverse DCT ($\hat{\mathbf{u}} \to \boldsymbol{\rho}_{\mathrm{phys}}$), one spectral Laplacian ($-\mu_k\hat{u}_k \to$ physical space via inverse DCT), one spectral gradient ($\to$ physical space via inverse DST), pointwise nonlinear assembly, and one forward DCT ($\boldsymbol{\mathcal{N}}_{\mathrm{phys}} \to \hat{\boldsymbol{\mathcal{N}}}$). Store the result as $\hat{\mathbf{a}}$.

**Substep 2 (at $t_n + \Delta t/2$):** Advance the spectral state to the half-step using $\hat{\mathbf{a}}$. Advance $v$ to the half-step using the exponential integrator with $\bar{F}^n$. Evaluate $\hat{\mathcal{N}}(\hat{\mathbf{u}}^{(a)}, v^{n+1/2})$. Store as $\hat{\mathbf{b}}$.

**Substep 3 (at $t_n + \Delta t/2$):** Advance the spectral state to the half-step using $\hat{\mathbf{b}}$. Evaluate $\hat{\mathcal{N}}(\hat{\mathbf{u}}^{(b)}, v^{n+1/2})$. Store as $\hat{\mathbf{c}}$.

**Substep 4 (at $t_n + \Delta t$):** Advance the spectral state to the full step using $\hat{\mathbf{c}}$ (from the Stage 2 state). Advance $v$ to the full step from $v^n$ (not from $v^{n+1/2}$). Evaluate $\hat{\mathcal{N}}(\hat{\mathbf{u}}^{(c)}, v^{n+1})$. Store as $\hat{\mathbf{d}}$.

**Combination:** Combine $\hat{\mathbf{a}}$, $\hat{\mathbf{b}}$, $\hat{\mathbf{c}}$, $\hat{\mathbf{d}}$ with the precomputed weight functions $\phi_{31}$, $\phi_{32}$, $\phi_{33}$ to produce $\hat{\mathbf{u}}^{n+1}$. The final $v^{n+1}$ is the value computed in Substep 4.

The ETD-RK4 substeps require four pseudospectral evaluations per time step, each involving two DCT operations (forward and inverse). The total per-step cost is $8$ DCTs of size $N_{\mathrm{phys}}$, plus $O(N_{\mathrm{modes}})$ array operations for the exponential and weight-function multiplications.

##### 2.3.2.3 Why Density Before Participation

The ordering — density update first, then participation — is dictated by the semi-implicit structure:

1. The density equation contains the participation variable $v^n$ as an explicit source term. The participation equation contains the operator average $\bar{F}^n$ (computed from $\boldsymbol{\rho}^n$) as an explicit driving term. Both use the *current* time-level values of the other variable.

2. If the participation were updated first ($v^{n+1}$ computed from $\bar{F}^n$), and then the density were updated using $v^{n+1}$ instead of $v^n$, the scheme would become a Gauss–Seidel-type iteration with a different truncation error. This would not improve the order of accuracy (both approaches are first-order in the coupling) but would break the symmetry of the time-level treatment and could introduce a systematic bias in the oscillation frequency.

3. The ETD-RK4 scheme handles the coupling through its substep structure (§2.3.2.2), where the participation is advanced to intermediate time levels for use in the nonlinear evaluations. The final update order ($\hat{\mathbf{u}}^{n+1}$ then $v^{n+1}$) is imposed by the combination formula.

The ordering is a convention, not a mathematical necessity. The Atlas results are reproducible with either ordering (the difference is $O(\Delta t)$ in the coupling error, which is below the convergence tolerance). The convention density-then-participation is adopted for consistency across all experiments.

---

#### 2.3.3 Diagnostics and Observable Sampling

Not every time step produces output. The simulation engine distinguishes between **internal steps** (which advance the state but produce no external output) and **output steps** (which extract observables and append them to the time series). The sampling schedule determines which steps are output steps.

##### 2.3.3.1 Sampling Modes

The engine supports three sampling modes:

**Uniform sampling.** Output every $k_{\mathrm{out}}$-th step, where $k_{\mathrm{out}}$ is specified by the experiment. The output times are $t_{\mathrm{out}} = \{k_{\mathrm{out}}\Delta t,\; 2k_{\mathrm{out}}\Delta t,\; 3k_{\mathrm{out}}\Delta t,\; \ldots\}$. This is the default mode. The default output interval is $k_{\mathrm{out}} = 100$ (output every 100th step), giving $\sim 1000$ output points for a typical $T = 50$, $\Delta t = 5 \times 10^{-4}$ integration ($10^5$ steps total).

**Prescribed-time sampling.** Output at a user-specified list of times $\{t_1, t_2, \ldots, t_K\}$. At each internal step, the engine checks whether $t_{n+1}$ has crossed the next prescribed output time; if so, it records the output. This mode is used for snapshot experiments (e.g., Atlas §4.3.2: spectral snapshots at six specific times) where the output times do not coincide with a uniform grid.

When a prescribed output time $t_k$ falls between $t_n$ and $t_{n+1}$ ($t_n < t_k \leq t_{n+1}$), the engine records the state at $t_{n+1}$ (the nearest computed state) rather than interpolating. The temporal error introduced by this rounding is at most $\Delta t$, which is below the accuracy of the time-stepping scheme.

**Every-step sampling.** Output at every time step ($k_{\mathrm{out}} = 1$). This mode generates the most data and is used only for short integrations ($T \leq 1$) or for debugging. It is not recommended for production runs due to the large output volume ($\sim 10^5$ observable records for a typical integration).

##### 2.3.3.2 Per-Step Diagnostics (Always Computed)

Regardless of the sampling mode, the following diagnostics are computed at every internal step:

| Diagnostic | Computation | Cost |
|-----------|------------|------|
| Proximity margin $\delta^n$ | $\rho_{\max} - \max_j\rho_j$ | $O(N_{\mathrm{grid}})$ |
| Positivity check | $\min_j\rho_j > 0$ and $\max_j\rho_j < \rho_{\max}$ | $O(N_{\mathrm{grid}})$ (combined with above) |
| Finiteness check | All $\rho_j$ and $v$ finite | $O(N_{\mathrm{grid}})$ (combined with above) |
| Energy (for monotonicity check) | $\mathcal{E}[\boldsymbol{\rho}^{n+1}, v^{n+1}]$ | $O(N_{\mathrm{grid}})$ |

The energy computation requires the quadrature of $\Phi(\rho_j)$, which is $O(N_{\mathrm{grid}})$ (one constitutive evaluation per grid point plus a summation). The total per-step diagnostic cost is $O(N_{\mathrm{grid}})$ — the same order as a single stencil evaluation — and is included in the per-step cost budget.

##### 2.3.3.3 Output-Step Observables (Computed at Output Steps Only)

At each output step, the full observable set (§1.1.6, `Extract_Observables`) is computed:

| Observable | Computation | Cost |
|-----------|------------|------|
| Energy $\mathcal{E}$ | Quadrature of $\Phi(\rho)$ + participation term | $O(N_{\mathrm{grid}})$ |
| ED-complexity $C_{\mathrm{ED}}$ | Sum of $(|\nabla_h\rho|^2)_j$ | $O(N_{\mathrm{grid}})$ |
| Effective complexity $C_{\mathrm{ED}}^{\mathrm{eff}}$ | Sum of $P'(\rho_j)/M(\rho_j) \cdot (|\nabla_h\rho|^2)_j$ | $O(N_{\mathrm{grid}})$ |
| Lyapunov $\mathcal{V}$ | Quadratic form in $u$, $\nabla u$, $w$ | $O(N_{\mathrm{grid}})$ |
| Spatial mean $\bar{\rho}$ | Sum of $\rho_j$ | $O(N_{\mathrm{grid}})$ |
| Modal amplitudes $\hat{a}_k$ | Forward DCT of $\rho_j - \rho^*$ | $O(N_{\mathrm{grid}}\log N_{\mathrm{grid}})$ |
| Dissipation channels | Three separate sums | $O(N_{\mathrm{grid}})$ |
| Proximity margin $\delta$ | Already computed in diagnostics | $O(1)$ (cached) |

The dominant cost is the DCT for the modal amplitudes ($O(N\log N)$). For Method B, the modal amplitudes are the primary state representation and require no additional computation. The total output-step cost is $O(N_{\mathrm{grid}}\log N_{\mathrm{grid}})$ for Method A and $O(N_{\mathrm{grid}})$ for Method B.

##### 2.3.3.4 Diagnostic Counters

The engine maintains running counters that are updated at every step and reported at the end of the integration:

| Counter | Meaning |
|---------|---------|
| `n_steps` | Total number of time steps completed |
| `n_output` | Number of output steps recorded |
| `n_projection` | Number of positivity-projection events (§1.7) |
| `n_dt_reduction` | Number of adaptive time-step reductions (§1.6.2) |
| `n_energy_warning` | Number of energy-monotonicity warnings |
| `n_barrier_warning` | Number of energy-barrier violations (§1.6.4) |
| `wall_time` | Elapsed wall-clock time (seconds) |

These counters are printed in the post-integration summary (§2.3.4) and are included in the output metadata.

---

#### 2.3.4 Stopping Criteria

The time loop terminates when any of the following criteria is met:

##### 2.3.4.1 Normal Termination: Final Time Reached

$$
t_{n+1} \geq T_{\mathrm{final}}.
$$

This is the expected termination mode for every Atlas experiment. The integration runs from $t = 0$ to $t = T_{\mathrm{final}}$ and then stops. If the last time step would overshoot $T_{\mathrm{final}}$ (i.e., $t_n + \Delta t > T_{\mathrm{final}}$), the time step is shortened to $\Delta t_{\mathrm{last}} = T_{\mathrm{final}} - t_n$ so that the final state is exactly at $t = T_{\mathrm{final}}$. The $\Delta t$-dependent precomputed quantities are recomputed for this shortened step.

The final state $(\boldsymbol{\rho}^{N_{\mathrm{final}}}, v^{N_{\mathrm{final}}})$ at $t = T_{\mathrm{final}}$ is always recorded as an output step, regardless of the sampling schedule.

##### 2.3.4.2 Early Termination: Convergence Detected

For long-time integrations where the goal is convergence to equilibrium (e.g., Atlas §7), the engine can terminate early if the solution has converged to within a specified tolerance:

$$
\|\boldsymbol{\rho}^n - \rho^*\|_{L^2} + |v^n| < \epsilon_{\mathrm{conv}},
$$

where $\epsilon_{\mathrm{conv}}$ is an experiment-specified convergence tolerance (default: disabled, $\epsilon_{\mathrm{conv}} = 0$). When enabled, this criterion is evaluated at every output step (not at every internal step, to avoid the $O(N)$ cost of the $L^2$-norm computation at every step).

Early convergence termination is logged as a normal event, not a warning. The final state is recorded, and the time series is marked as converged.

##### 2.3.4.3 Abnormal Termination: Fatal Error

The loop terminates immediately if any of the following fatal conditions is detected:

| Condition | Detection point | Diagnostic |
|-----------|----------------|-----------|
| Non-finite density | Phase 3, Step 8 | "NaN or Inf detected in density array at step $n$" |
| Non-finite participation | Phase 3, Step 8 | "NaN or Inf detected in participation at step $n$" |
| Gross energy increase | Phase 4, Step 10 | "Energy increased by $> 10\cdot\text{tol}$ at step $n$" |
| Time step below minimum | Phase 1, Step 2 | "Time step $\Delta t < \Delta t_{\min} = 10^{-8}$ at step $n$" |
| Maximum step count exceeded | Phase 4, Step 12 | "Step count $n > N_{\max}$" |

The maximum step count $N_{\max}$ is a safeguard against infinite loops. Its default value is $N_{\max} = 10^8$ ($100$ million steps), which exceeds the requirement of any Atlas experiment by at least two orders of magnitude. It is triggered only by implementation errors (e.g., a time step that is accidentally set to zero) or by pathological parameter combinations.

An abnormal termination writes the diagnostic message, the current state, and the diagnostic counters to the output, then halts. The partial time series (up to the step before the failure) is retained for debugging.

##### 2.3.4.4 Post-Loop Summary

After the loop terminates (by any criterion), the engine produces a summary report:

```
REPORT Integration_Summary:
    termination_reason : Enum {FinalTime, Convergence, FatalError}
    n_steps            : Int
    n_output           : Int
    wall_time          : Float64 (seconds)
    final_time         : Float64
    final_energy       : Float64
    final_deviation    : Float64 (||ρ − ρ*||_L2)
    final_participation: Float64 (|v|)
    positivity_converged : Boolean
    n_projection       : Int
    n_dt_reduction     : Int
    n_energy_warning   : Int
    n_barrier_warning  : Int
    delta_min          : Float64 (minimum proximity margin over all steps)
    delta_final        : Float64 (proximity margin at final step)
```

The summary is written to the diagnostic output and stored in the experiment's output metadata. It provides a one-glance assessment of the integration's health: a normal termination with `positivity_converged = true`, `n_energy_warning = 0`, and `n_barrier_warning = 0` indicates a clean, fully validated integration. Any nonzero warning count or `positivity_converged = false` flags the result for review.

---

#### 2.3.5 Computational Cost Per Step

The per-step cost determines the total wall-clock time for the integration. For reference:

**Method A (Crank–Nicolson, 1D, $N = 512$):**

| Operation | Cost | Fraction |
|-----------|------|----------|
| Constitutive evaluation ($4 \times N_{\mathrm{grid}}$ calls) | $O(N)$ | $\sim 15\%$ |
| Stencil evaluation (Laplacian + gradient-squared) | $O(N)$ | $\sim 15\%$ |
| Operator assembly ($F_h$) | $O(N)$ | $\sim 10\%$ |
| RHS assembly | $O(N)$ | $\sim 5\%$ |
| Implicit matrix assembly | $O(N)$ | $\sim 5\%$ |
| Tridiagonal solve (Thomas algorithm) | $O(N)$ | $\sim 20\%$ |
| Participation update (exponential integrator) | $O(1)$ | $< 1\%$ |
| Diagnostics (proximity, positivity, energy) | $O(N)$ | $\sim 15\%$ |
| Observable extraction (at output steps only) | $O(N\log N)$ | $\sim 15\%$ (amortized) |

Total per step: $\sim 8N$ floating-point operations $\approx 4000$ flops at $N = 512$. At $\sim 10^9$ flops/sec (single-core): $\sim 4\,\mu$s per step, or $\sim 0.4$ seconds for $10^5$ steps ($T = 50$ at $\Delta t = 5 \times 10^{-4}$).

**Method B (ETD-RK4, 1D, $N_{\mathrm{modes}} = 128$):**

| Operation | Cost | Fraction |
|-----------|------|----------|
| 4 pseudospectral evaluations ($4 \times 2$ DCTs of size $192$) | $O(N\log N)$ | $\sim 60\%$ |
| 4 pointwise nonlinear assemblies | $O(N)$ | $\sim 15\%$ |
| Weight-function multiplications | $O(N)$ | $\sim 10\%$ |
| Participation updates (4 substeps) | $O(1)$ | $< 1\%$ |
| Diagnostics | $O(N)$ | $\sim 15\%$ |

Total per step: $\sim 8 \times 192 \times \log_2(192) \approx 12{,}000$ flops. At $\sim 10^9$ flops/sec: $\sim 12\,\mu$s per step, or $\sim 6$ seconds for $5 \times 10^5$ steps ($T = 50$ at $\Delta t = 10^{-4}$).

Both methods complete the full Atlas ($\sim 450$ integrations) in $\sim 2$ hours on a single core (§0.5).

---

### 2.4 Output Logging

Every experiment in the Atlas produces three categories of output: time-series data (the observables at each output step), spectral data (modal amplitudes and related quantities), and diagnostic data (runtime health information and structural-invariant checks). This subsection specifies the logical structure of each category, the metadata that accompanies every output, and the file naming conventions that ensure traceability from output to experiment to Atlas figure.

The output specification is format-agnostic — it defines the logical content (fields, types, dimensions) without prescribing a specific file format. Implementations may use CSV, HDF5, JSON, MATLAB `.mat`, NumPy `.npz`, Julia JLD2, or any other format that preserves the field names, types, and dimensions. The only requirement is that the format supports named fields (not positional columns) so that outputs remain interpretable when the field set is extended.

---

#### 2.4.1 Time-Series Logging

The time series is the primary output of every experiment. It records the full observable set (§1.1.6, §2.3.3.3) at each output step, forming a tabular dataset indexed by time.

##### 2.4.1.1 Record Structure

Each row of the time series corresponds to one output step and contains the fields of the `Observables` record (§1.2.8):

| Field | Type | Units | Description |
|-------|------|-------|-------------|
| `time` | Float64 | dimensionless | Current time $t$ |
| `energy` | Float64 | — | Total energy $\mathcal{E}[\rho, v]$ |
| `C_ED` | Float64 | — | ED-complexity $\int|\nabla\rho|^2\,dx$ |
| `C_ED_eff` | Float64 | — | Effective complexity $\int(P'/M)|\nabla\rho|^2\,dx$ |
| `lyapunov` | Float64 | — | Lyapunov functional $\mathcal{V}[u, w]$ |
| `rho_bar` | Float64 | — | Spatial mean $\bar{\rho} = L^{-d}\int\rho\,dx$ |
| `a_0` | Float64 | — | Homogeneous-mode amplitude $\bar{\rho} - \rho^*$ |
| `v` | Float64 | — | Participation variable |
| `delta` | Float64 | — | Proximity margin $\rho_{\max} - \max_j\rho_j$ |
| `D_diff` | Float64 | — | Gradient dissipation channel |
| `D_pen` | Float64 | — | Penalty dissipation channel |
| `D_part` | Float64 | — | Participation dissipation channel |

The time series has dimensions $(N_{\mathrm{output}} \times 12)$, where $N_{\mathrm{output}}$ is the number of recorded output steps (including the $t = 0$ initial record and the $t = T_{\mathrm{final}}$ terminal record).

##### 2.4.1.2 Writing Schedule

The time series is written incrementally: each output step appends one row. This ensures that partial results are available if the integration is interrupted or terminated abnormally. The engine does not buffer the entire time series in memory before writing — it flushes each row to the output stream as it is produced.

For long integrations with uniform sampling ($N_{\mathrm{output}} \sim 1000$ rows), the output volume per experiment is $\sim 1000 \times 12 \times 8\;\text{bytes} \approx 96$ KB (uncompressed). For every-step sampling ($N_{\mathrm{output}} \sim 10^5$), the volume is $\sim 10$ MB. The total output for the full Atlas ($\sim 450$ experiments at $\sim 1000$ rows each) is $\sim 45$ MB of time-series data.

---

#### 2.4.2 Spectral Logging

Experiments that require modal decomposition (Atlas §§3–4, §9.1, §9.3, §9.4) produce additional spectral output: the modal amplitudes $\hat{a}_k(t)$ at each output step.

##### 2.4.2.1 Record Structure

The spectral log is a separate dataset, parallel to the time series, with one row per output step:

| Field | Type | Shape | Description |
|-------|------|-------|-------------|
| `time` | Float64 | scalar | Current time (matches time-series `time`) |
| `modal_amps` | Float64 | $(N_{\mathrm{obs\_modes}},)$ | $|\hat{a}_k|$ for $k = 0, 1, \ldots, N_{\mathrm{obs\_modes}} - 1$ |
| `modal_phases` | Float64 | $(N_{\mathrm{obs\_modes}},)$ | $\arg(\hat{a}_k)$ (the sign of $\hat{a}_k$ for real coefficients) |
| `modal_energy` | Float64 | $(N_{\mathrm{obs\_modes}},)$ | $|\hat{a}_k|^2$ (modal energy per mode) |
| `total_modal_energy` | Float64 | scalar | $\sum_k|\hat{a}_k|^2$ |
| `spectral_centroid` | Float64 | scalar | $\sum_k k|\hat{a}_k|^2 / \sum_k|\hat{a}_k|^2$ |

The number of tracked modes $N_{\mathrm{obs\_modes}}$ defaults to $\min(32, N_{\mathrm{modes}})$ but is set to higher values for specific experiments:

| Experiment group | $N_{\mathrm{obs\_modes}}$ | Reason |
|-----------------|-------------------------|--------|
| Single-mode decay (§3.1) | $16$ | Monitor leakage to adjacent modes |
| Multi-mode waterfall (§3.2) | $32$ | Track all initialized modes plus harmonics |
| Triad experiments (§4) | $32$ | Track generation up to mode $16$ |
| Cascade experiments (§4.3) | $64$ | Track deep cascade |
| Pattern spectrum (§9.3) | $32$ | Track harmonic comb |

##### 2.4.2.2 Spectral Computation

For Method A: the spectral log requires a forward DCT of $\boldsymbol{\rho}^{n+1} - \rho^*$ at each output step. This is the dominant cost of the spectral logging — $O(N_{\mathrm{grid}}\log N_{\mathrm{grid}})$ per output step — and is performed only at output steps, not at internal steps.

For Method B: the spectral coefficients $\hat{u}_k$ are the primary state, so the spectral log is a direct copy of the state array truncated to $N_{\mathrm{obs\_modes}}$ elements. No DCT is needed; the cost is $O(N_{\mathrm{obs\_modes}})$.

##### 2.4.2.3 Spectral Snapshot Log

For experiments that require the full spatial profile at specific times (e.g., Atlas §6.1: five density profiles at prescribed time slices), the engine produces a **snapshot log**: the complete density array $\boldsymbol{\rho}$ at each prescribed snapshot time.

| Field | Type | Shape | Description |
|-------|------|-------|-------------|
| `time` | Float64 | scalar | Snapshot time |
| `rho` | Float64 | $(N_{\mathrm{grid}},)$ or $(N_x, N_y)$ | Full density array |
| `v` | Float64 | scalar | Participation variable |

Snapshots are written only at the prescribed times (typically 3–6 per experiment) and represent the highest-volume output per record (one full array per snapshot). The total volume is modest: $6 \times 514 \times 8 \approx 25$ KB per experiment for 1D snapshots.

---

#### 2.4.3 Diagnostic Logging

The diagnostic log records runtime health information that is not part of the scientific output but is essential for validating the computation and debugging failures.

##### 2.4.3.1 Event Log

The event log records discrete events that occurred during the integration:

| Event type | Fields | Trigger |
|-----------|--------|---------|
| `ProximityWarning` | step, time, $\delta$, $j_{\max}$, $\rho_{\max\_val}$, $M_{\min}$, $\mathcal{E}$ | $\delta \leq \delta_{\mathrm{warn}}$ |
| `TimestepReduction` | step, time, $\Delta t_{\mathrm{old}}$, $\Delta t_{\mathrm{new}}$, $\delta$ | §1.6.2 activated |
| `TimestepRestored` | step, time, $\Delta t_{\mathrm{restored}}$, $\delta$ | Recovery from adaptive reduction |
| `PositivityProjection` | step, time, $n_{\mathrm{neg}}$, $n_{\mathrm{over}}$, worst values, mass change | §1.7.2 activated |
| `EnergyWarning` | step, time, $\mathcal{E}^{n+1}$, $\mathcal{E}^n$, violation magnitude | $\mathcal{E}^{n+1} > \mathcal{E}^n + \text{tol}$ |
| `BarrierWarning` | step, time, $\delta_{\mathrm{actual}}$, $\delta_{\mathrm{barrier}}$, $\mathcal{E}$ | §1.6.4 condition violated |
| `FatalError` | step, time, error type, message | Any fatal condition |

The event log is append-only and is written as events occur. For a clean integration (no warnings, no projections), the event log is empty — its emptiness is itself a diagnostic result, confirming that the computation was uneventful.

##### 2.4.3.2 Summary Record

At the end of the integration, the engine writes the `Integration_Summary` record (§2.3.4.4):

| Field | Type | Description |
|-------|------|-------------|
| `termination_reason` | Enum | FinalTime, Convergence, or FatalError |
| `n_steps` | Int | Total steps completed |
| `n_output` | Int | Output steps recorded |
| `wall_time` | Float64 | Wall-clock seconds |
| `final_time` | Float64 | $t$ at termination |
| `final_energy` | Float64 | $\mathcal{E}$ at termination |
| `final_deviation` | Float64 | $\|\rho - \rho^*\|_{L^2}$ at termination |
| `final_participation` | Float64 | $|v|$ at termination |
| `positivity_converged` | Boolean | True if no projection occurred |
| `n_projection` | Int | Count of projection events |
| `n_dt_reduction` | Int | Count of adaptive time-step reductions |
| `n_energy_warning` | Int | Count of energy monotonicity warnings |
| `n_barrier_warning` | Int | Count of barrier violations |
| `delta_min` | Float64 | Minimum proximity margin over all steps |
| `delta_final` | Float64 | Proximity margin at final step |

The summary record is the first thing inspected when reviewing an experiment's output. A clean run has: `termination_reason = FinalTime`, `positivity_converged = true`, and all warning counts equal to zero.

---

#### 2.4.4 Metadata

Every output file (time series, spectral log, snapshot log, diagnostic log, summary) includes a metadata header that fully identifies the experiment and the computation.

##### 2.4.4.1 Metadata Fields

| Field | Type | Source | Example |
|-------|------|--------|---------|
| `experiment_id` | String | Master Table, §10.2.5 | "3.1" |
| `atlas_figure` | String | Figure Index, §11 | "3.1" |
| `parameter_set` | String | Set name or "Custom" | "II" |
| `D` | Float64 | CanonicalParams | 0.6 |
| `H` | Float64 | CanonicalParams | 0.4 |
| `zeta` | Float64 | CanonicalParams | 0.5 |
| `tau` | Float64 | CanonicalParams | 1.0 |
| `rho_star` | Float64 | CanonicalParams | 0.5 |
| `rho_max` | Float64 | CanonicalParams | 1.0 |
| `M0` | Float64 | Constitutive | 1.0 |
| `beta` | Float64 | Constitutive | 2.0 |
| `P0` | Float64 | Constitutive | 1.0 |
| `discriminant` | Float64 | Derived | $-1.59$ |
| `regime` | String | Derived | "Oscillatory" |
| `IC_type` | String | IC specification | "A" |
| `IC_amplitude` | Float64 | IC specification | 0.001 |
| `IC_v0` | Float64 | IC specification | 0.0 |
| `method` | String | Spatial method | "FD_CrankNicolson" |
| `N` | Int | Grid | 512 |
| `dt` | Float64 | Time step | $5 \times 10^{-4}$ |
| `T_final` | Float64 | Integration time | 5.0 |
| `output_interval` | Int | Sampling | 100 |
| `suite_version` | String | Implementation | "1.0.0" |
| `environment` | String | Runtime | "Python 3.11 / NumPy 1.24 / SciPy 1.11" |
| `timestamp` | String | Wall clock | "2026-03-26T14:30:00Z" |

The metadata is written at the beginning of the output file (as a header, a separate metadata section, or a companion `.meta` file, depending on the format). It is sufficient to reproduce the experiment: given the metadata, an implementor can reconstruct the parameter record, grid, initial condition, and integration settings without consulting the Atlas text.

##### 2.4.4.2 Reproducibility Hash

As an additional reproducibility safeguard, the metadata includes a deterministic hash of the experiment specification:

$$
\texttt{spec\_hash} = \text{SHA-256}(\texttt{parameter\_set} \| D \| \zeta \| \tau \| \rho^* \| \rho_{\max} \| M_0 \| \beta \| P_0 \| \text{IC\_type} \| A \| v_0 \| N \| \Delta t \| T)
$$

where $\|$ denotes concatenation of the string representations (to 15 decimal digits). Two outputs with the same `spec_hash` were produced from the same experiment specification; any difference in their numerical values is attributable to the implementation, the environment, or the floating-point rounding — not to the experiment design.

The hash does not include the `environment`, `timestamp`, or `suite_version` fields (which are implementation-specific and expected to differ between reproductions).

---

#### 2.4.5 File Naming Conventions

The output files are organized in a directory hierarchy that mirrors the Atlas structure. The naming conventions ensure that every file is traceable to its experiment and that no two experiments produce files with the same name.

##### 2.4.5.1 Directory Structure

```
output/
├── exp_1.1/                     # Experiment 1.1 (Convergence study)
│   ├── timeseries.{ext}         # Time-series log
│   ├── spectral.{ext}           # Spectral log (if applicable)
│   ├── snapshots.{ext}          # Snapshot log (if applicable)
│   ├── diagnostics.{ext}        # Diagnostic event log
│   ├── summary.{ext}            # Integration summary
│   └── metadata.{ext}           # Experiment metadata
├── exp_3.1/
│   ├── n1/                      # Sub-experiment: mode n = 1
│   │   ├── timeseries.{ext}
│   │   ├── spectral.{ext}
│   │   └── ...
│   ├── n2/                      # Sub-experiment: mode n = 2
│   │   └── ...
│   └── ...
├── exp_8.1/
│   ├── zeta_0.500/              # Sweep point: ζ = 0.500
│   │   └── ...
│   ├── zeta_0.561/              # Sweep point: ζ = 0.561
│   │   └── ...
│   └── ...
└── figures/                     # Figure-ready data (post-processed)
    ├── fig_3.1.{ext}
    ├── fig_4.3.{ext}
    └── ...
```

##### 2.4.5.2 Naming Rules

| Component | Convention | Example |
|-----------|-----------|---------|
| Experiment directory | `exp_{section}.{number}` | `exp_3.1`, `exp_8.5` |
| Sub-experiment directory | Swept parameter and value | `n1`, `zeta_0.500`, `A_0.050` |
| Output file | Descriptive name, no step numbers | `timeseries`, `spectral`, `summary` |
| File extension | Environment-dependent | `.csv`, `.h5`, `.npz`, `.mat`, `.jld2` |
| Figure-ready data | `fig_{section}.{number}` | `fig_3.1`, `fig_9.2` |
| Sweep-point value formatting | Fixed-width, 3 decimal places | `zeta_0.500`, `D_0.300` |

The fixed-width formatting of sweep-point values ensures correct lexicographic sorting of directories (so that `zeta_0.100` sorts before `zeta_1.000`, not after `zeta_0.500`).

##### 2.4.5.3 Figure-Ready Data

The `figures/` directory contains post-processed data files, one per Atlas figure, formatted for direct input to a plotting tool. Each file contains exactly the data specified in the figure description (§11 of the Atlas): the axis variables, the curve data, the reference lines, and the annotations. The figure-ready data is derived from the raw time-series and spectral logs by extraction and formatting — no additional computation is performed.

The figure-ready file includes a header that references the Atlas figure number, the source experiment(s), and the data columns:

```
# Figure 3.1: Single-mode exponential decay
# Source: Experiment 3.1, modes n = 1, 2, 3, 4
# Columns: time, |a_1|, |a_2|, |a_3|, |a_4|
# Reference slopes: -2.080, -6.522, -13.924, -24.287
```

---

#### 2.4.6 Output Volume Summary

| Output type | Per experiment | Full Atlas ($\sim 450$ experiments) |
|-------------|---------------|--------------------------------------|
| Time series | $\sim 100$ KB | $\sim 45$ MB |
| Spectral log | $\sim 200$ KB (when present) | $\sim 30$ MB |
| Snapshots | $\sim 25$ KB (when present) | $\sim 5$ MB |
| Diagnostics | $\sim 1$ KB (clean runs) | $\sim 0.5$ MB |
| Summary | $\sim 0.5$ KB | $\sim 0.2$ MB |
| Metadata | $\sim 1$ KB | $\sim 0.5$ MB |
| Figure-ready data | $\sim 10$ KB per figure | $\sim 0.6$ MB (64 figures) |
| **Total** | | **$\sim 82$ MB** |

The total output is well within the $\sim 5$ GB raw estimate of Atlas §10.3.3 (which assumed every-step sampling; the actual output with default $k_{\mathrm{out}} = 100$ is much smaller). The compressed output (gzip or similar) is $\sim 15$ MB.

---

### 2.5 Checkpointing

The longest Atlas integrations run to $T = 60$ with $\Delta t = 5 \times 10^{-4}$, requiring $1.2 \times 10^5$ time steps and taking approximately $50$ seconds of wall-clock time on a single core. At this scale, a power failure, system crash, or accidental process termination would lose at most one minute of computation — a minor inconvenience, not a catastrophic loss. Checkpointing is therefore not a critical requirement for the Atlas experiments.

It becomes essential, however, for two scenarios that the Suite is designed to support: parameter sweeps involving hundreds of independent integrations (Atlas §8.3: $81$–$324$ runs, total wall time $\sim 1$ hour), where a failure midway through the sweep should not require rerunning the completed portion; and future extensions involving longer integrations, higher resolution, or multi-dimensional domains, where individual runs may take hours rather than seconds. The checkpointing system is designed for both scenarios.

---

#### 2.5.1 Checkpoint Frequency

The engine writes a checkpoint at regular intervals during the integration, measured in wall-clock time rather than step count. This choice ensures that the checkpoint overhead is bounded as a fraction of the total computation time, regardless of the time-step size or the per-step cost.

**Default interval.** A checkpoint is written every $T_{\mathrm{ckpt}}$ seconds of wall-clock time, where $T_{\mathrm{ckpt}} = 300$ seconds (5 minutes) is the default. This means:

- For a $50$-second integration (typical single Atlas experiment): zero or one checkpoint is written. The overhead is negligible.
- For a $1$-hour sweep: approximately $12$ checkpoints are written. A failure at any point loses at most $5$ minutes of computation.
- For a hypothetical $10$-hour extended integration: approximately $120$ checkpoints, with the same $5$-minute maximum loss.

**Checkpoint also at output steps.** In addition to the wall-clock schedule, the engine writes a checkpoint at the first output step after each $T_{\mathrm{ckpt}}$ interval has elapsed. This ties the checkpoint to the output schedule, ensuring that the checkpointed state has valid observables and is at a "clean" time (an output time) rather than an arbitrary internal step. The logic is:

1. After each output step (§2.3.3), check whether $T_{\mathrm{ckpt}}$ seconds have elapsed since the last checkpoint.
2. If yes: write a checkpoint and reset the wall-clock timer.
3. If no: proceed without checkpointing.

This means the actual checkpoint interval is between $T_{\mathrm{ckpt}}$ and $T_{\mathrm{ckpt}} + (\text{time between output steps})$, which is at most $T_{\mathrm{ckpt}} + k_{\mathrm{out}} \cdot \Delta t \cdot (\text{wall time per step})$ — a negligible overshoot for the Atlas experiments.

**Mandatory checkpoints.** Regardless of the wall-clock schedule, a checkpoint is always written at:

- The first output step ($t = 0$ or the first prescribed output time).
- The final output step ($t = T_{\mathrm{final}}$).
- Immediately before any abnormal termination (§2.3.4.3).

The first and last checkpoints ensure that the integration can be verified from its endpoints. The pre-termination checkpoint preserves the state at the moment of failure for debugging.

---

#### 2.5.2 Checkpoint Contents

A checkpoint is a self-contained snapshot of the complete engine state, sufficient to restart the integration from the checkpointed step as if it had never been interrupted. It contains three groups of data: the dynamic state, the static configuration, and the accumulated output.

##### 2.5.2.1 Dynamic State

The dynamic state is the minimum information needed to advance the next time step:

| Field | Type | Description |
|-------|------|-------------|
| `step_n` | Int | Current step counter $n$ |
| `time` | Float64 | Current time $t_n$ |
| `rho` | Array[Float64] | Density array $\boldsymbol{\rho}^n$ (full grid) |
| `rho_prev` | Array[Float64] | Previous-step density $\boldsymbol{\rho}^{n-1}$ (if history is maintained) |
| `v` | Float64 | Participation variable $v^n$ |
| `v_prev` | Float64 | Previous-step participation $v^{n-1}$ |
| `dt_current` | Float64 | Current time step $\Delta t^n$ (may differ from $\Delta t_0$ if adaptive) |
| `energy_current` | Float64 | Current energy $\mathcal{E}^n$ (for monotonicity check at next step) |

For Method B, the density array is replaced by the spectral state:

| Field | Type | Description |
|-------|------|-------------|
| `u_hat` | Array[Float64] | Spectral coefficients $\hat{\mathbf{u}}^n$ |
| `u_hat_prev` | Array[Float64] | Previous-step spectral state |

The dynamic state is compact: for Method A at $N = 512$ in 1D, it is $2 \times 514 \times 8 + 4 \times 8 = 8{,}256$ bytes ($\sim 8$ KB). For Method B at $N = 128$, it is $2 \times 128 \times 8 + 4 \times 8 = 2{,}080$ bytes ($\sim 2$ KB).

##### 2.5.2.2 Static Configuration

The static configuration records everything needed to reconstruct the engine's internal state without re-running the initialization:

| Field | Type | Description |
|-------|------|-------------|
| `params` | CanonicalParams | Complete parameter record (§1.1.6), all primary and derived fields |
| `constitutive_type` | String | Constitutive function identifier (e.g., "PowerLawLinear") |
| `constitutive_params` | Record | $M_0$, $\beta$, $P_0$ |
| `grid` | Grid record | Dimension, $N$, $h$, $L$, coordinate arrays |
| `method` | String | "FD_ImplicitEuler", "FD_CrankNicolson", or "SPEC_ETDRK4" |
| `dt_nominal` | Float64 | Nominal time step $\Delta t_0$ (before adaptive adjustment) |
| `T_final` | Float64 | Target final time |
| `IC_type` | String | Initial condition identifier |
| `IC_params` | Record | IC-specific parameters ($A$, $n$, $\sigma$, $x_0$, $\delta$, $v_0$) |
| `output_mode` | String | "uniform", "prescribed", or "every_step" |
| `output_interval` | Int | $k_{\mathrm{out}}$ (for uniform mode) |
| `output_times` | Array[Float64] | Prescribed output times (for prescribed mode) |
| `spec_hash` | String | SHA-256 reproducibility hash (§2.4.4.2) |

The static configuration is identical across all checkpoints of the same integration (it does not change during the time loop). It is included in every checkpoint rather than stored once and referenced, because this makes each checkpoint fully self-contained — it can be read and used without access to any other file.

##### 2.5.2.3 Accumulated Output

The checkpoint stores the index of the last written output record, so that the restart can resume appending to the time series without duplication:

| Field | Type | Description |
|-------|------|-------------|
| `n_output_written` | Int | Number of output records already written to the time-series file |
| `n_spectral_written` | Int | Number of spectral records already written |
| `n_snapshot_written` | Int | Number of snapshots already written |
| `diagnostic_counters` | Record | Current values of all diagnostic counters (§2.3.3.4) |

The accumulated output data itself (the time-series rows, spectral log rows, etc.) is not stored in the checkpoint — it is in the output files, which are written incrementally (§2.4.1.2). The checkpoint stores only the bookkeeping needed to resume writing at the correct position.

---

#### 2.5.3 Restart Logic

A restart reconstructs the engine state from a checkpoint and resumes the integration as if it had never been interrupted. The restart must produce *identical* output from the restart point onward (to within floating-point rounding) as a continuous run would have produced.

##### 2.5.3.1 Restart Procedure

1. **Load the checkpoint.** Read the checkpoint file and extract the dynamic state, static configuration, and output bookkeeping.

2. **Verify the specification hash.** Compare the `spec_hash` in the checkpoint to the hash of the current experiment specification. If they differ, the checkpoint was produced by a different experiment, and the restart is rejected with a fatal error. This prevents accidental cross-contamination of results.

3. **Reconstruct the engine.** Using the static configuration, re-run the initialization sequence (§2.1) up to but not including the initial-condition evaluation (§2.1.4). Specifically:
   - Load the parameters (§2.2) from the checkpoint's `params` record.
   - Create the grid (§2.1.2) from the checkpoint's `grid` record.
   - Construct the constitutive functions (§2.1.3) from the checkpoint's constitutive type and parameters.
   - Allocate workspace (§2.1.5) and precompute static quantities.

4. **Restore the dynamic state.** Overwrite the density array with the checkpoint's `rho`, the participation variable with `v`, the step counter with `step_n`, and the current time with `time`. Restore the previous-step history (`rho_prev`, `v_prev`) and the adaptive time step (`dt_current`). Restore the current energy for the monotonicity check.

5. **Restore the output bookkeeping.** Set the output counters to the checkpoint's `n_output_written`, `n_spectral_written`, `n_snapshot_written`. Set the diagnostic counters to the checkpoint's values. Open the output files in append mode, positioned after the last written record.

6. **Recompute $\Delta t$-dependent quantities.** If the checkpointed `dt_current` differs from `dt_nominal` (adaptive reduction was active), recompute the exponential factors and ETD weight functions for the current time step.

7. **Verify consistency.** Compute the energy $\mathcal{E}$ from the restored state and compare to the checkpointed `energy_current`. If the relative difference exceeds $10^{-10}$, the checkpoint may be corrupted; issue a warning. (The threshold is above machine precision to allow for platform-dependent rounding in the energy quadrature.)

8. **Resume the time loop.** Enter the time loop (§2.3) at step $n + 1$, continuing from the restored state.

##### 2.5.3.2 Bitwise Reproducibility

The restart procedure aims for *identical* results to a continuous run, but does not guarantee bitwise reproducibility across platforms. The reasons are:

- **Floating-point rounding.** The order of floating-point operations may differ between a continuous run and a restart (e.g., the precomputation of exponential factors in Step 6 may produce slightly different values than the initial precomputation, due to intermediate rounding). The difference is at the level of machine precision ($\sim 10^{-16}$) and is not observable in any Atlas result.

- **Platform dependence.** The DCT, the tridiagonal solver, and the exponential function may produce different rounding in different environments (Python vs. Julia vs. MATLAB). Restarts within the same environment on the same hardware are expected to be bitwise identical; restarts across environments are expected to agree to within $10^{-12}$.

The engine does not attempt to guarantee bitwise reproducibility (which would require fixed-order arithmetic, platform-specific rounding modes, and deterministic library implementations). It guarantees *structural* reproducibility: the same structural features (regime classification, decay rates, amplitude ratios, convergence behavior) and the same quantitative values to within the convergence tolerances of the Atlas ($1\%$–$5\%$ for physical observables).

---

#### 2.5.4 Checkpoint File Format

The checkpoint is stored as a single file in a binary or structured format that supports named fields and heterogeneous types. The recommended formats are:

| Environment | Format | Extension | Library |
|-------------|--------|-----------|---------|
| Python | NumPy compressed archive | `.npz` | `numpy.savez` |
| Julia | JLD2 | `.jld2` | `JLD2.jl` |
| MATLAB | MAT-file v7.3 | `.mat` | `save` (HDF5-based) |

All three formats support named fields, arrays of arbitrary shape, and scalar values. The checkpoint file is self-describing (field names are stored in the file) and portable within its environment.

**File naming.** The checkpoint file is stored in the experiment's output directory:

```
output/exp_{id}/checkpoint_step_{n}.{ext}
```

where `{n}` is the step number (zero-padded to 8 digits) and `{ext}` is the format-specific extension. Only the most recent checkpoint is needed for restart; older checkpoints may be deleted to save space, or retained for debugging. The engine writes each new checkpoint to a temporary file and atomically renames it to the final name after the write completes, ensuring that a partially written checkpoint (due to a crash during the write) never overwrites a valid one.

**Checkpoint size.** For the typical Atlas experiment (Method A, 1D, $N = 512$):

| Component | Size |
|-----------|------|
| Dynamic state | $\sim 8$ KB |
| Static configuration | $\sim 2$ KB |
| Output bookkeeping | $\sim 0.1$ KB |
| Format overhead | $\sim 1$ KB |
| **Total** | **$\sim 11$ KB** |

For Method B ($N = 128$): $\sim 5$ KB. For 2D Method A ($N = 64$): $\sim 40$ KB. Checkpoint storage is negligible in all cases.

---

#### 2.5.5 Checkpointing for Sweep Experiments

Parameter sweeps (§2.2.5) involve many independent integrations. The checkpointing system handles sweeps at two levels:

**Integration-level checkpointing.** Each sweep point's integration produces its own checkpoints in its own sub-directory (`output/exp_{id}/zeta_0.500/checkpoint_step_{n}.{ext}`). The restart logic (§2.5.3) operates on individual integrations, not on the sweep as a whole.

**Sweep-level progress tracking.** The sweep orchestrator maintains a progress file that records which sweep points have completed:

```
output/exp_{id}/sweep_progress.{ext}
```

This file contains:

| Field | Type | Description |
|-------|------|-------------|
| `sweep_param` | String | Name of the swept parameter |
| `sweep_values` | Array[Float64] | All sweep values |
| `completed` | Array[Boolean] | True for each completed sweep point |
| `failed` | Array[Boolean] | True for each sweep point that terminated abnormally |

When the sweep is restarted after an interruption, the orchestrator reads the progress file and skips all completed sweep points, resuming only the incomplete ones. A sweep point is marked as completed only after its integration terminates normally and all output files are flushed. This ensures that a crash during a sweep point's integration does not mark it as complete.

The sweep-level progress file is updated atomically (write to temporary, then rename) after each sweep point completes.

---

#### 2.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Checkpoint frequency** | Every $T_{\mathrm{ckpt}} = 300$ seconds (wall clock), at output steps |
| **Mandatory checkpoints** | First step, final step, pre-termination |
| **Contents** | Dynamic state + static config + output bookkeeping |
| **Checkpoint size** | $\sim 5$–$40$ KB (negligible) |
| **Restart guarantee** | Structural reproducibility; identical within same platform |
| **Hash verification** | `spec_hash` match required; energy consistency check at restart |
| **Sweep support** | Per-integration checkpoints + sweep-level progress file |
| **Atomic writes** | Write to temp, then rename; no partial checkpoints |
| **Maximum data loss** | $\leq T_{\mathrm{ckpt}}$ seconds of computation ($\leq 5$ minutes at default) |

Checkpointing adds negligible overhead ($< 0.01\%$ of wall time for the Atlas experiments) and provides the resilience needed for long sweeps, extended integrations, and shared computing environments where process interruptions are common.

---

### 2.6 Error Handling

The defensive computation principle (§0.3, Principle 6) requires that the simulation engine detect every class of numerical error that could compromise the structural integrity of the output, respond with an appropriate action (warn, correct, or halt), and produce a diagnostic record that enables the user to identify the root cause. This subsection consolidates the error-detection mechanisms described in §§1.6–1.8 and §§2.3–2.5 into a unified error-handling framework: a classification of all detectable error conditions (§2.6.1), the detection logic for each (§2.6.2), the response hierarchy (§2.6.3), and the graceful termination protocol (§2.6.4).

The framework is designed around a single principle: **no silent corruption**. Every deviation from the expected behavior of the continuous PDE — a negative density, an energy increase, a non-finite value, a barrier violation — is detected, recorded, and acted upon. The engine never produces output that it has not verified against the structural invariants of the ED system.

---

#### 2.6.1 Error Classification

All detectable errors fall into four categories, ordered by severity:

**Level 0 — Informational.** A condition that is noteworthy but does not indicate any problem. No action is taken; the condition is logged for post-hoc analysis.

**Level 1 — Warning.** A condition that may indicate an emerging problem but does not yet compromise the output. The computation continues; the condition is logged and counted. Repeated or intensifying warnings may trigger escalation to Level 2.

**Level 2 — Corrective.** A condition that would compromise the output if left uncorrected. The engine applies a correction (adaptive time-step reduction, positivity projection) and logs the intervention. The corrected output is valid but may differ slightly from the unperturbed solution.

**Level 3 — Fatal.** A condition from which no recovery is possible. The engine halts immediately after writing a diagnostic record and a pre-termination checkpoint.

The complete error catalog:

| ID | Condition | Level | Detection point | Response |
|----|-----------|-------|----------------|----------|
| E01 | Proximity margin below warning threshold | 0 | Phase 1, Step 1 | Log `ProximityWarning` |
| E02 | Proximity margin below critical threshold | 2 | Phase 1, Step 2 | Adaptive $\Delta t$ reduction (§1.6.2) |
| E03 | Density $\leq 0$ at one or more grid points | 2 | Phase 3, Step 7 | Positivity projection (§1.7.2) |
| E04 | Density $\geq \rho_{\max}$ at one or more grid points | 2 | Phase 3, Step 7 | Upper projection (§1.6.3) |
| E05 | Energy increase above tolerance | 1 | Phase 4, Step 10 | Log `EnergyWarning` |
| E06 | Energy increase above $10\times$ tolerance | 3 | Phase 4, Step 10 | Halt |
| E07 | Non-finite density (NaN or Inf) | 3 | Phase 3, Step 8 | Halt |
| E08 | Non-finite participation (NaN or Inf) | 3 | Phase 3, Step 8 | Halt |
| E09 | Energy barrier condition violated | 1 | Phase 4 (at output steps) | Log `BarrierWarning` |
| E10 | Adaptive time step below minimum | 3 | Phase 1, Step 2 | Halt |
| E11 | Step count exceeds maximum | 3 | Phase 4, Step 12 | Halt |
| E12 | Constitutive evaluation produces non-finite value | 3 | Phase 2, Step 4a | Halt |
| E13 | Implicit solve fails (zero pivot or non-convergence) | 3 | Phase 2, Step 4f | Halt |
| E14 | Spectral tail energy exceeds threshold | 1 | Phase 4 (at output steps) | Log warning |
| E15 | Checkpoint write failure | 1 | Checkpoint write | Log warning; continue without checkpoint |

---

#### 2.6.2 Detection Logic

Each error condition is detected by a specific check at a specific point in the per-step sequence (§2.3.1). The checks are grouped by the phase in which they occur.

##### 2.6.2.1 Phase 1 Detections (Pre-Step)

**E01/E02: Proximity monitoring.** After computing $\delta^n = \rho_{\max} - \max_j\rho_j^n$:

- If $\delta^n \leq \delta_{\mathrm{warn}}$ and $\delta^n > \delta_{\mathrm{crit}}$: raise E01 (informational).
- If $\delta^n \leq \delta_{\mathrm{crit}}$: raise E02 (corrective).

**E10: Time-step minimum.** After the adaptive reduction of §1.6.2, if $\Delta t^n < \Delta t_{\min} = 10^{-8}$: raise E10 (fatal). This indicates that the density is so close to $\rho_{\max}$ that the adaptive reduction has shrunk the time step to an impractically small value — the energy barrier should have prevented this, so E10 typically indicates an implementation error or an ill-posed initial condition.

##### 2.6.2.2 Phase 2 Detections (State Update)

**E12: Constitutive non-finiteness.** During the pointwise evaluation of $M(\rho_j)$, $M'(\rho_j)$, $P(\rho_j)$: if any value is NaN or $\pm\infty$, raise E12 (fatal). This can occur if $\rho_j$ has drifted outside the domain of the constitutive function (e.g., $\rho_j > \rho_{\max}$ for non-integer $\beta$, producing $(\rho_{\max} - \rho_j)^\beta$ with a negative base). The safeguarded evaluation of §1.6.6 should prevent this; E12 catches the case where the safeguard is bypassed or incorrectly implemented.

**E13: Implicit solve failure.** During the tridiagonal (1D) or banded (2D) solve: if a zero pivot is encountered (the Thomas algorithm encounters $A_{jj} = 0$, which should never happen since $A_{jj} \geq 1$), or if an iterative solver (3D) fails to converge within the allotted iterations, raise E13 (fatal). This indicates a corrupted implicit matrix, which in turn indicates either a mobility that has become exactly zero (the energy barrier should prevent this) or a negative mobility (which is impossible for the canonical constitutive functions with $\rho \in (0, \rho_{\max})$).

##### 2.6.2.3 Phase 3 Detections (Post-Step Safeguards)

**E03/E04: Positivity and sub-capacity violations.** After the state update produces $\boldsymbol{\rho}^{n+1}$, scan for violations:

- If $\min_j\rho_j^{n+1} \leq 0$: raise E03 (corrective). Apply lower projection.
- If $\max_j\rho_j^{n+1} \geq \rho_{\max}$: raise E04 (corrective). Apply upper projection.

The scan is a single pass over the array, combined with the proximity monitoring for the next step. The cost is $O(N_{\mathrm{grid}})$.

**E07/E08: Non-finiteness.** During the same scan: if any $\rho_j^{n+1}$ is NaN or $\pm\infty$, raise E07 (fatal). If $v^{n+1}$ is NaN or $\pm\infty$, raise E08 (fatal). Non-finite values indicate a catastrophic numerical failure — typically an unstable explicit step (CFL violation) or a division by zero in the constitutive evaluation. No correction is possible; the state is corrupted beyond recovery.

The NaN/Inf check is performed before the positivity projection, because NaN values would not be caught by the comparison $\rho_j \leq 0$ (NaN comparisons return false in IEEE 754 arithmetic). The check uses the language-specific NaN/Inf detection function (`numpy.isfinite`, `isfinite` in Julia, `isfinite` in MATLAB).

##### 2.6.2.4 Phase 4 Detections (Diagnostics and Output)

**E05/E06: Energy monotonicity.** After computing $\mathcal{E}^{n+1}$:

- Compute the tolerance: $\text{tol} = 10\,\Delta t^p\,\mathcal{E}^n$, where $p$ is the temporal order.
- If $\mathcal{E}^{n+1} > \mathcal{E}^n + \text{tol}$: raise E05 (warning).
- If $\mathcal{E}^{n+1} > \mathcal{E}^n + 10\cdot\text{tol}$: raise E06 (fatal).

The tolerance is scaled by both $\Delta t^p$ (the expected truncation error) and $\mathcal{E}^n$ (the current energy scale). This ensures that the check is neither too sensitive at small $\mathcal{E}$ (where the truncation error is also small) nor too permissive at large $\mathcal{E}$.

The distinction between E05 (warning) and E06 (fatal) is the factor of $10$: a single energy increase of up to $10\cdot\text{tol}$ may be a transient artifact (e.g., from the interaction between the implicit and explicit terms at a step where the adaptive time reduction activates), but an increase exceeding $100\cdot\Delta t^p\,\mathcal{E}^n$ indicates a genuine instability that will grow without bound.

**E09: Energy barrier.** At each output step, after computing $\mathcal{E}^{n+1}$ and $\delta^{n+1}$:

- Compute $\delta_{\mathrm{barrier}} = P_0(\rho_{\max} - \rho^*)|\Omega|/(M_0\,\mathcal{E}^{n+1})$ (§1.6.4).
- If $\delta^{n+1} < \delta_{\mathrm{barrier}}$: raise E09 (warning).

The barrier check is performed only at output steps (not every internal step) to reduce the overhead of the energy quadrature. The check compares the *actual* proximity margin to the *analytic* lower bound; a violation indicates that the discrete dynamics is less confining than the continuous theory predicts, which may be caused by insufficient resolution or temporal accuracy.

**E11: Maximum step count.** After incrementing the step counter: if $n > N_{\max} = 10^8$, raise E11 (fatal). This is a safeguard against infinite loops caused by a time step that is accidentally zero or a final time that is unreachable.

**E14: Spectral tail energy (Method B only).** At each output step, compute $E_{\mathrm{tail}} = \sum_{k > 2N/3}|\hat{u}_k|^2$:

- If $E_{\mathrm{tail}} > 10^{-6}\sum_k|\hat{u}_k|^2$: raise E14 (warning).

This check detects aliasing-driven energy accumulation at the de-aliasing boundary (§1.8.3.3). A persistent E14 warning indicates that the spectral resolution is insufficient or that the de-aliasing padding factor is too small.

---

#### 2.6.3 Response Hierarchy

The four severity levels map to four response types:

**Level 0 (Informational).** The engine writes a log entry to the diagnostic event log (§2.4.3.1) and increments no counter. No modification to the state or the time step. The log entry includes the step number, time, and the condition's details. The user reviews informational events only if a higher-level event subsequently occurs and the informational events provide context.

**Level 1 (Warning).** The engine writes a log entry, increments the corresponding diagnostic counter (§2.3.3.4), and continues the integration unchanged. Warnings are reviewed post-hoc; they do not affect the computation in progress.

**Escalation rule.** If the same warning (same error ID) occurs at more than $100$ consecutive output steps, the engine escalates the warning to a Level 2 or Level 3 response:

| Warning ID | Escalation after 100 consecutive | Escalated response |
|-----------|----------------------------------|-------------------|
| E05 | Energy monotonicity persistently violated | Reduce $\Delta t$ by factor $2$ (Level 2) |
| E09 | Barrier persistently violated | Log severe warning; do not halt |
| E14 | Spectral tail persistently elevated | Increase de-aliasing padding to $2\times$ if possible (Level 2) |

The escalation is conservative — it modifies the computation only when the warning is persistent, not transient.

**Level 2 (Corrective).** The engine applies the specified correction (§§1.6.2, 1.6.3, 1.7.2), writes a log entry, increments the counter, and continues. The corrected state is the new starting point for the next step; the pre-correction state is not recoverable (except from the previous checkpoint).

**Correction budget.** Each corrective error type has a maximum number of allowed activations per integration:

| Error ID | Correction | Budget | Action when budget exhausted |
|----------|------------|--------|------------------------------|
| E02 | Adaptive $\Delta t$ reduction | Unlimited | — |
| E03 | Lower positivity projection | 1000 | Escalate to fatal |
| E04 | Upper capacity projection | 1000 | Escalate to fatal |

The budget of $1000$ projection events is generous — in a converged computation, the projection is never activated (§1.7.4). If $1000$ projections are reached, the computation is severely under-resolved, and continuing would produce unreliable output. The escalation to fatal halts the computation and reports the budget exhaustion.

**Level 3 (Fatal).** The engine executes the graceful termination protocol (§2.6.4).

---

#### 2.6.4 Graceful Termination

When a fatal error (Level 3) is detected, the engine does not simply crash. It executes a controlled shutdown that preserves as much information as possible for debugging.

**Termination sequence.**

1. **Log the fatal error.** Write a `FatalError` event to the diagnostic log with the error ID, the step number, the time, and a descriptive message. The message includes the specific values that triggered the error (e.g., "NaN detected in density at grid point $j = 247$, step $n = 84{,}312$, time $t = 42.156$").

2. **Write a pre-termination checkpoint.** Write a checkpoint containing the state *before* the failed step (the state at $t_n$, not the corrupted $t_{n+1}$). If the state at $t_n$ is also corrupted (e.g., E07 was raised at $t_n$ itself), write the most recent non-corrupted state from the history buffer or the most recent periodic checkpoint.

3. **Flush all output files.** Ensure that all time-series, spectral, and diagnostic records written before the failure are flushed to disk. The partial time series (up to the last clean output step before the failure) is valid and can be used for analysis.

4. **Write the integration summary.** Produce the `Integration_Summary` record (§2.3.4.4) with `termination_reason = FatalError` and the diagnostic counters reflecting all events up to the failure.

5. **Report to the user.** Print a summary to the console or standard error:

```
FATAL: [E07] Non-finite density detected.
  Step: 84312
  Time: 42.156
  Location: grid point j = 247
  Value: NaN
  Last clean output at: t = 42.100 (step 82000)
  Checkpoint written: output/exp_7.1/checkpoint_step_084312.npz
  Partial time series: 840 output records written (of expected ~1000)
  Suggested actions:
    - Reduce time step (current: 5.0e-04)
    - Increase resolution (current: N = 512)
    - Check initial condition for admissibility
```

6. **Exit with a nonzero return code.** The engine returns a nonzero exit code to the calling process, signaling that the integration did not complete normally. This is important for sweep orchestration (§2.5.5): the sweep orchestrator marks the sweep point as failed, not completed.

**Information preservation.** The termination sequence is designed to preserve the maximum amount of useful information:

- The **pre-termination checkpoint** allows the user to inspect the state at the moment of failure, diagnose the cause, and (after fixing the issue) restart from the last clean checkpoint.
- The **partial time series** provides all the output up to the failure, which may be sufficient for partial analysis (e.g., if the failure occurs at $t = 42$ in a $T = 50$ integration, the first $84\%$ of the output is valid).
- The **diagnostic log** provides the complete history of warnings and corrections leading up to the failure, which may reveal a pattern (e.g., a sequence of E05 warnings with increasing violation magnitude, indicating a growing instability that culminated in the E07 fatal).
- The **suggested actions** provide actionable guidance based on the error type, sparing the user from consulting the documentation for the most common remedies.

---

#### 2.6.5 Error Handling in Sweep Experiments

In a parameter sweep (§2.2.5, §2.5.5), a fatal error at one sweep point should not terminate the entire sweep. The sweep orchestrator handles errors as follows:

1. **Isolate the failure.** Each sweep point runs as an independent integration. A fatal error at sweep point $i$ terminates only that integration, not the orchestrator.

2. **Record the failure.** The orchestrator marks sweep point $i$ as `failed = true` in the progress file (§2.5.5) and records the error ID and message.

3. **Continue the sweep.** The orchestrator proceeds to sweep point $i + 1$ without delay.

4. **Report at sweep completion.** After all sweep points have been attempted, the orchestrator prints a summary:

```
Sweep completed: 79 of 81 points succeeded, 2 failed.
  Failed points:
    zeta = 0.012: [E10] Time step below minimum (proximity too close)
    zeta = 4.950: [E07] NaN in density (CFL violation at large gradient)
  Suggested: rerun failed points with reduced dt or increased N.
```

5. **Partial results are valid.** The $79$ successful sweep points produce valid output; the $2$ failed points produce partial output (up to the failure) and are flagged in the sweep results. Analyses that use the sweep data (e.g., regime maps, observable landscapes) can exclude the failed points or interpolate over them.

---

#### 2.6.6 Summary

| Principle | Implementation |
|-----------|---------------|
| **No silent corruption** | Every structural violation is detected and logged |
| **Proportional response** | Severity levels 0–3 with escalation rules |
| **Correct when possible** | Adaptive $\Delta t$, positivity projection, de-aliasing adjustment |
| **Halt when necessary** | NaN/Inf, gross energy violation, budget exhaustion |
| **Preserve information** | Pre-termination checkpoint, partial time series, diagnostic log |
| **Isolate failures** | Sweep points fail independently; sweep continues |
| **Guide the user** | Suggested actions printed with every fatal error |

The error-handling framework adds $< 1\%$ overhead to the per-step cost (the detection checks are combined with existing array scans) and provides the guarantee that every output file produced by the engine has been validated against the structural invariants of the ED system. An output file with `termination_reason = FinalTime`, `positivity_converged = true`, and all warning counts at zero represents a fully verified numerical solution of the canonical ED PDE.

---

### 2.7 Convergence Testing

The numerical results of the Atlas are credible only if they are *converged* — independent, to within stated tolerances, of the spatial resolution $N$ and the time step $\Delta t$. Convergence is not assumed; it is verified for every experiment by the methodology described in this subsection.

The convergence testing serves two purposes. First, it validates the implementation: an implementation that produces the correct convergence order (second-order in $h$ for Method A, spectral in $N$ for Method B, order $p$ in $\Delta t$ for each time-stepping scheme) is almost certainly correct, because the probability of an implementation error that preserves the convergence order is negligible. Second, it certifies the results: an experiment whose observables are converged at the reported resolution produces values that approximate the continuous PDE solution to within the stated tolerance.

The testing protocol corresponds to Atlas §1.7.1 (Experiment 1.1) and extends it to a general-purpose methodology applicable to any experiment in the Atlas.

---

#### 2.7.1 Resolution Doubling (Spatial Convergence)

Spatial convergence is verified by running the same experiment at successively refined grids and measuring the difference between solutions at adjacent refinement levels.

##### 2.7.1.1 Refinement Sequence

The standard refinement sequence for Method A in one dimension is:

$$
N \in \{N_0,\; 2N_0,\; 4N_0\},
$$

where $N_0$ is the coarsest resolution at which the experiment is expected to produce meaningful results. For the Atlas default ($N_0 = 128$), the sequence is $\{128, 256, 512\}$, corresponding to grid spacings $h \in \{7.75 \times 10^{-3},\; 3.89 \times 10^{-3},\; 1.95 \times 10^{-3}\}$.

For Method B, the refinement sequence is $N_{\mathrm{modes}} \in \{N_0, 2N_0, 4N_0\}$ with $N_0 = 32$, giving $\{32, 64, 128\}$.

At each refinement level, the time step is scaled to maintain the CFL ratio (§1.8.1): $\Delta t \propto h^2$ for Method A (so $\Delta t$ is reduced by a factor of $4$ at each refinement), or held fixed for Method B (where the CFL is not $h$-dependent). This ensures that the measured error reflects spatial discretization only, not temporal truncation.

##### 2.7.1.2 Error Metric

At the final time $T$, the spatial convergence error between refinement levels $N$ and $2N$ is:

$$
e_h(N) := \|\boldsymbol{\rho}_{N}(T) - \boldsymbol{\rho}_{2N}(T)\|_{L^2},
$$

where $\boldsymbol{\rho}_{N}$ denotes the discrete solution on the $N$-point grid and the two solutions are compared on the coarser grid (the finer solution is restricted to the coarse grid points by sampling at every other point, or by spectral truncation for Method B). The $L^2$-norm is computed by the trapezoidal rule:

$$
\|\mathbf{f}\|_{L^2}^2 = h\sum_{j=0}^{N_{\mathrm{grid}}-1} f_j^2.
$$

The convergence error $e_h$ is a single scalar summarizing the spatial accuracy at the given resolution. It is not the absolute error (which would require the exact solution), but the Richardson-extrapolation error — the difference between successive approximations, which converges to zero at the same rate as the absolute error.

##### 2.7.1.3 Observed Convergence Order

The observed spatial convergence order is computed from two successive error values:

$$
p_h = \log_2\!\left(\frac{e_h(N_0)}{e_h(2N_0)}\right).
$$

For Method A (second-order central differences): the expected order is $p_h = 2$. For Method B (spectral): the expected order is $p_h \gg 2$ for smooth solutions (exponential convergence appears as a very large $p_h$ in this finite-difference-of-logs formula; the more appropriate measure for spectral methods is the exponential decay of $e_h$ with $N$).

##### 2.7.1.4 Acceptance Criterion

The spatial discretization is accepted if:

1. **Order criterion.** The observed order $p_h$ is within $10\%$ of the theoretical order: $|p_h - 2| < 0.2$ for Method A. For Method B, the criterion is that $e_h(2N_0)/e_h(N_0) < 0.01$ (at least two orders of magnitude reduction per doubling — a proxy for spectral convergence).

2. **Magnitude criterion.** The convergence error at the finest resolution is below the experiment's accuracy requirement: $e_h(4N_0) < \epsilon_{\mathrm{spatial}}$, where $\epsilon_{\mathrm{spatial}}$ is the maximum permissible spatial error. The default is $\epsilon_{\mathrm{spatial}} = 10^{-4}$ for quantitative experiments (decay rates, amplitude ratios) and $\epsilon_{\mathrm{spatial}} = 10^{-2}$ for qualitative experiments (regime classification, zero-crossing counts).

Both criteria must be met. If the order criterion fails (the convergence rate is slower than expected), the implementation may contain a bug. If the magnitude criterion fails (the error is too large even at the finest resolution), the resolution must be increased.

---

#### 2.7.2 Time-Step Halving (Temporal Convergence)

Temporal convergence is verified by running the same experiment at successively halved time steps and measuring the difference.

##### 2.7.2.1 Refinement Sequence

The standard temporal refinement sequence is:

$$
\Delta t \in \{\Delta t_0,\; \Delta t_0/2,\; \Delta t_0/4\},
$$

where $\Delta t_0$ is the default time step for the experiment. All runs use the same spatial resolution $N$ (the finest from the spatial convergence study, §2.7.1), so the measured error reflects temporal discretization only.

##### 2.7.2.2 Error Metric

At the final time $T$, the temporal convergence error between time-step levels $\Delta t$ and $\Delta t/2$ is:

$$
e_{\Delta t}(\Delta t) := \|\boldsymbol{\rho}_{\Delta t}(T) - \boldsymbol{\rho}_{\Delta t/2}(T)\|_{L^2}.
$$

Both solutions are on the same spatial grid, so no interpolation or restriction is needed. The comparison is pointwise.

##### 2.7.2.3 Observed Convergence Order

$$
p_t = \log_2\!\left(\frac{e_{\Delta t}(\Delta t_0)}{e_{\Delta t}(\Delta t_0/2)}\right).
$$

Expected orders:

| Scheme | Expected $p_t$ |
|--------|----------------|
| Implicit Euler | $1$ |
| Crank–Nicolson (linear regime) | $2$ |
| Crank–Nicolson (nonlinear regime) | $1$–$2$ (mixed, see §1.4.1.2) |
| ETD-RK2 | $2$ |
| ETD-RK4 | $4$ |

The Crank–Nicolson scheme's mixed-order behavior in the nonlinear regime (§1.4.1.2, accuracy note) means that $p_t$ may lie between $1$ and $2$ for far-from-equilibrium experiments. This is expected and is not a convergence failure.

##### 2.7.2.4 Acceptance Criterion

1. **Order criterion.** $|p_t - p_{\mathrm{expected}}| < 0.3$ (within $30\%$ of the theoretical order). The wider tolerance relative to the spatial criterion reflects the mixed-order behavior of the semi-implicit scheme.

2. **Magnitude criterion.** $e_{\Delta t}(\Delta t_0/4) < \epsilon_{\mathrm{temporal}}$, where $\epsilon_{\mathrm{temporal}} = 10^{-4}$ (default). This ensures that the temporal error at the reported time step is negligible compared to the spatial error and the physical observables.

---

#### 2.7.3 Convergence Metrics for Physical Observables

The $L^2$-norm error metrics of §§2.7.1–2.7.2 measure the convergence of the *solution field* $\boldsymbol{\rho}(x, T)$. The Atlas experiments extract *scalar observables* (decay rates, frequencies, amplitude ratios, transition times) from the solution field, and these observables may converge at a different rate than the field itself (faster, if the observable is an integrated quantity; slower, if it depends on a pointwise feature like the maximum density).

The convergence of each scalar observable is tested independently.

##### 2.7.3.1 Observable Convergence Error

For a scalar observable $Q$ (e.g., the measured decay rate $\hat{\sigma}$, the oscillation frequency $\hat{\omega}$, the locked amplitude ratio $\bar{R}_{31}$):

$$
e_Q(N) := |Q_N - Q_{2N}|, \qquad e_Q(\Delta t) := |Q_{\Delta t} - Q_{\Delta t/2}|,
$$

where $Q_N$ denotes the observable extracted from the $N$-resolution run.

##### 2.7.3.2 Relative Observable Error

When the observable has a known analytic value $Q_{\mathrm{exact}}$ (e.g., $\hat{\sigma} = D\alpha_1$ from the linearized theory), the relative error is:

$$
\epsilon_Q := \frac{|Q_N - Q_{\mathrm{exact}}|}{|Q_{\mathrm{exact}}|}.
$$

This relative error should decrease with increasing resolution at the expected convergence order.

##### 2.7.3.3 Observable Acceptance Criteria

| Observable type | Acceptance threshold | Atlas experiments |
|----------------|---------------------|-------------------|
| Decay rate $\hat{\sigma}$ | $\epsilon_Q < 1\%$ | §§3.1, 3.2, 7.3, 7.5 |
| Oscillation frequency $\hat{\omega}$ | $\epsilon_Q < 1\%$ | §§2.1, 2.2, 8.1 |
| Locked amplitude ratio $\bar{R}_{31}$ | $\epsilon_Q < 5\%$ | §§4.2, 4.4, 4.5 |
| Transition time $t_*$ | $\epsilon_Q < 10\%$ | §§7.4, 7.6 |
| Regime classification | Exact agreement | §§2.4, 8.3, 8.5 |
| Zero-crossing count $N_{\mathrm{cross}}$ | Exact agreement | §§2.4, 8.1 |

The thresholds are chosen to match the precision of the analytic predictions: decay rates and frequencies are known to full precision from the eigenvalue formulas (C.15), so $1\%$ error is achievable and expected. Amplitude ratios involve the nonlinear coupling coefficients (C.40), which have $O(\epsilon^2)$ corrections, so $5\%$ is appropriate. Transition times depend on the nonlinear transient dynamics and are sensitive to the initial condition's spectral content, so $10\%$ is realistic. Regime classification and zero-crossing counts are topological invariants — they must be exact.

---

#### 2.7.4 The Four Validation Tests

The Atlas (§1.7) specifies four validation tests that every implementation must pass before any experiment results are trusted. These tests are the convergence-testing methodology applied to specific, well-characterized configurations. They constitute the **acceptance gate** for the implementation.

##### 2.7.4.1 Test 1: Spatial and Temporal Convergence (Atlas §1.7.1, Experiment 1.1)

**Configuration.** Parameter Set I, IC-A ($A = 0.05$), $T = 5.0$.

**Procedure.** Run the spatial refinement sequence (§2.7.1) at four levels ($N \in \{64, 128, 256, 512\}$ for Method A; $N \in \{16, 32, 64, 128\}$ for Method B) and the temporal refinement sequence (§2.7.2) at four levels ($\Delta t \in \{10^{-2}, 5 \times 10^{-3}, 2.5 \times 10^{-3}, 1.25 \times 10^{-3}\}$ for Method A; $\Delta t \in \{10^{-3}, 5 \times 10^{-4}, 2.5 \times 10^{-4}, 1.25 \times 10^{-4}\}$ for Method B).

**Pass criterion.** Spatial order within $10\%$ of theoretical ($p_h = 2.0 \pm 0.2$ for Method A; $e_h$ ratio $< 0.01$ for Method B). Temporal order within $30\%$ of theoretical ($p_t = 1.0 \pm 0.3$ for implicit Euler, $p_t = 2.0 \pm 0.6$ for Crank–Nicolson, $p_t = 4.0 \pm 1.2$ for ETD-RK4).

##### 2.7.4.2 Test 2: Energy Dissipation (Atlas §1.7.2, Experiment 1.2)

**Configuration.** Parameter Set I, IC-B ($N_m = 8$), $T = 50.0$, $N = 256$, Crank–Nicolson.

**Procedure.** Integrate and record $\mathcal{E}(t)$ at every output step. Compute the three dissipation channels $\mathcal{D}_{\mathrm{diff}}$, $\mathcal{D}_{\mathrm{pen}}$, $\mathcal{D}_{\mathrm{part}}$ and the discrete dissipation-identity residual $r^n = \mathcal{E}^{n+1} - \mathcal{E}^n + \Delta t(\mathcal{D}_{\mathrm{diff}}^n + \mathcal{D}_{\mathrm{pen}}^n + \mathcal{D}_{\mathrm{part}}^n)$.

**Pass criterion.** Energy monotonically non-increasing at every step (no E05 warnings). Dissipation-identity residual $|r^n| < 10\,\Delta t^2\,\mathcal{E}^n$ at every step (second-order closure for Crank–Nicolson).

##### 2.7.4.3 Test 3: Mass Conservation (Atlas §1.7.3, Experiment 1.3)

**Configuration.** Parameter Set IV, IC-A ($A = 0.05$), $T = 20.0$, $N = 256$, Crank–Nicolson.

**Procedure.** Track the discrete total mass $\mathcal{M}_h^n = h\sum_j\rho_j^n$ and the predicted mass rate $d\mathcal{M}/dt|_{\mathrm{pred}} = -Dh\sum_j P(\rho_j^n) + Hv^nL$. Compute the mass-rate residual $|d\mathcal{M}/dt|_{\mathrm{num}} - d\mathcal{M}/dt|_{\mathrm{pred}}|$.

**Pass criterion.** Mass-rate residual bounded by $O(\Delta t^2 + h^2)$ at every step. Total mass converges to $\rho^* L$ as $t \to \infty$.

##### 2.7.4.4 Test 4: Linearized Analytic Comparison (Atlas §1.7.4, Experiment 1.4)

**Configuration.** All five parameter sets (I–V), IC-A at $A = 10^{-4}$ (deep linearized regime), $T = 10.0$, $N = 256$.

**Procedure.** Compare the numerical solution to the analytic linearized solution: $u_1(t) = Ae^{-D\alpha_1 t}$ for the $n = 1$ spatial mode, and the $2 \times 2$ matrix exponential $e^{\mathbf{A}_0 t}(A, v_0)^\top$ for the homogeneous mode. Extract the measured decay rate $\hat{\sigma}$ and frequency $\hat{\omega}$ by fitting.

**Pass criterion.** At $A = 10^{-4}$: relative error in $\hat{\sigma}$ below $1\%$, and relative error in $\hat{\omega}$ below $1\%$ (for oscillatory parameter sets I, II, V). The pointwise error $\max_j|\rho_j^n - \rho_{\mathrm{lin}}(x_j, t_n)|$ is bounded by $O(\Delta t^p + h^2 + A^2)$ at every output time.

---

#### 2.7.5 Convergence Testing Workflow

The complete convergence-testing workflow, applied to a new implementation or to a new experiment, is:

**Step 1: Run the four validation tests.** These are non-negotiable prerequisites. If any test fails, the implementation is not ready for production use. Debug and repeat until all four pass.

**Step 2: Run the target experiment at the default resolution.** Record all observables.

**Step 3: Run the spatial refinement study.** Repeat the experiment at $N/2$ and $2N$ (or $N$ and $2N$ if the default is not the finest level). Compute $e_h$ and $p_h$.

**Step 4: Run the temporal refinement study.** Repeat the experiment at $\Delta t/2$ and $\Delta t/4$ (at the finest spatial resolution). Compute $e_{\Delta t}$ and $p_t$.

**Step 5: Compute observable convergence.** For each reported observable, compute $e_Q$ and $\epsilon_Q$ across the refinement levels. Verify that all acceptance criteria (§2.7.3.3) are met.

**Step 6: Report.** Record the convergence results in the experiment's metadata:

| Field | Value |
|-------|-------|
| `spatial_order` | Measured $p_h$ |
| `temporal_order` | Measured $p_t$ |
| `spatial_error_finest` | $e_h$ at finest $N$ |
| `temporal_error_finest` | $e_{\Delta t}$ at finest $\Delta t$ |
| `observable_errors` | Dictionary of $\epsilon_Q$ for each reported observable |
| `convergence_status` | "Passed" or "Failed" with details |

An experiment whose `convergence_status` is "Failed" is not included in the Atlas. The resolution or time step must be increased until convergence is achieved.

---

#### 2.7.6 When Convergence Testing Is Not Required

The full convergence study (Steps 2–5) is required for every experiment whose quantitative results are reported in the Atlas. It is not required for:

- **Qualitative demonstrations** where the result is a visual feature (e.g., the shape of a phase portrait, the presence or absence of oscillations) that is resolution-independent above a minimal threshold. These experiments require only the validation tests (Step 1) and a visual confirmation that the feature is present at the default resolution.

- **Parameter sweeps** where the same numerical method and resolution are used at every sweep point. In this case, the convergence study is performed at a representative subset of sweep points (e.g., three points spanning the parameter range), and the results are assumed to hold for the remaining points by continuity.

- **Repeat runs** of an experiment that has already been convergence-tested at the same resolution and time step. The convergence properties are resolution-dependent and scheme-dependent, not initial-condition-dependent (for smooth ICs in the same amplitude range).

The convergence testing is the most expensive part of the Atlas workflow (it requires $4$–$6$ additional integrations per experiment, at resolutions up to $4\times$ the default). The exemptions above reduce the total cost while maintaining the guarantee that every reported numerical value is converged.

---

## 3. Experiment Templates

This section provides a standardized template for specifying any experiment in the Atlas, followed by a complete worked example. Every experiment in the Master Experiment Table (Atlas §10.2.5) can be expressed as an instance of this template. The template ensures that experiment specifications are complete (no missing parameters), unambiguous (no implicit defaults that could differ between implementations), and traceable (every field maps to a specific component of the simulation engine).

---

### 3.1 Generic Experiment Template

The following template is the canonical specification format for any Atlas experiment. An experiment is fully defined when every field is filled; no external information is needed to reproduce it.

---

#### EXPERIMENT [ID]

**Atlas reference:** Section [§X.Y.Z], Experiment [X.Y]

---

##### 3.1.1 Purpose

*A one-to-three-sentence statement of what the experiment demonstrates, which theorem or proposition from Appendix C it targets, and what structural feature of the ED architecture it makes visible.*

**Demonstrates:** [Theorem/Proposition/Remark C.XX]

**Architectural feature:** [e.g., "Modal hierarchy," "Triad selection rule," "Three-stage convergence"]

---

##### 3.1.2 Required Parameters

**Parameter set:** [I / II / III / IV / V / Custom]

**Overrides** (if any):

| Parameter | Base value | Override value | Reason |
|-----------|-----------|----------------|--------|
| [name] | [from base set] | [new value] | [why the override is needed] |

**Derived quantities** (computed from the above):

| Quantity | Value |
|----------|-------|
| $H = 1 - D$ | [value] |
| $\Delta = D + 2\zeta$ | [value] |
| $M_* = M(\rho^*)$ | [value] |
| $M_*' = M'(\rho^*)$ | [value] |
| $P_*' = P'(\rho^*)$ | [value] |
| $\mathscr{D}_0$ | [value] |
| $\gamma_0$ | [value] |
| $\omega$ (if oscillatory) | [value] |
| Regime | [Oscillatory / Monotonic / Critical] |

**Constitutive functions:**

| Function | Form | Parameters |
|----------|------|-----------|
| $M(\rho)$ | $M_0(\rho_{\max} - \rho)^\beta$ | $M_0 = $ [value], $\beta = $ [value] |
| $P(\rho)$ | $P_0(\rho - \rho^*)$ | $P_0 = $ [value] |

---

##### 3.1.3 Initial Conditions

**IC type:** [A / B / C / D / Homogeneous / Custom]

**IC parameters:**

| Parameter | Value |
|-----------|-------|
| Amplitude $A$ | [value] |
| Mode number $n$ (IC-A) | [value] |
| Mode amplitudes $\{A_n\}$ (IC-B) | [list or formula] |
| Number of modes $N_{\mathrm{modes}}$ (IC-B) | [value] |
| Center $x_0$ (IC-C) | [value] |
| Width $\sigma$ (IC-C) | [value] |
| Margin $\delta$ (IC-D) | [value] |
| Initial participation $v_0$ | [value] |

**Initial complexity:** $C_{\mathrm{ED}}(0) = $ [value or formula]

**Admissibility verification:** $\min_j\rho_j(0) = $ [value] $> 0$; $\max_j\rho_j(0) = $ [value] $< \rho_{\max}$.

---

##### 3.1.4 Numerical Method

| Setting | Value |
|---------|-------|
| Spatial method | [FD (Method A) / Spectral (Method B)] |
| Time-stepping scheme | [Implicit Euler / Crank–Nicolson / ETD-RK4] |
| Spatial dimension $d$ | [1 / 2 / 3] |
| Domain | $\Omega = [0, L]^d$, $L = $ [value] |
| Grid points $N$ | [value] |
| Grid spacing $h$ | [value, or N/A for spectral] |
| Time step $\Delta t$ | [value] |
| Final time $T$ | [value] |
| CFL at initial condition | $\Delta t_{\mathrm{CFL}} = $ [value] (verify $\Delta t \leq \Delta t_{\mathrm{CFL}}$) |
| Output sampling | [Uniform, $k_{\mathrm{out}} = $ value / Prescribed times: list / Every step] |

---

##### 3.1.5 Expected Outputs

**Time-series observables** (recorded at each output step):

| Observable | Expected behavior | Analytic prediction |
|-----------|-------------------|---------------------|
| $\mathcal{E}(t)$ | [e.g., "Monotonically decreasing"] | [if available] |
| $C_{\mathrm{ED}}(t)$ | [e.g., "Exponential decay at rate $2D(\alpha_1 - P_*')$"] | [value] |
| $\mathcal{V}(t)$ | [e.g., "Exponential decay at rate $2\gamma_*$"] | [value] |
| $a_0(t)$ | [e.g., "Damped oscillation with frequency $\omega$"] | [value] |
| $v(t)$ | [e.g., "Oscillating with envelope $e^{-\gamma_0 t}$"] | [value] |

**Spectral observables** (if applicable):

| Observable | Expected behavior | Analytic prediction |
|-----------|-------------------|---------------------|
| $|a_n(t)|$ for mode $n$ | [e.g., "Exponential decay at rate $D\alpha_n$"] | [value] |
| Amplitude ratios | [e.g., "$|a_3|/|a_1| \to 0.236$"] | [value from eq. C.40] |

**Scalar summary quantities** (extracted post-integration):

| Quantity | Symbol | Expected value | Tolerance |
|----------|--------|---------------|-----------|
| Measured decay rate | $\hat{\sigma}$ | [value] | [e.g., $\pm 1\%$] |
| Measured frequency | $\hat{\omega}$ | [value] | [e.g., $\pm 1\%$] |
| Transition time | $t_*$ | [value or "N/A"] | [e.g., $\pm 10\%$] |
| Zero-crossing count | $N_{\mathrm{cross}}$ | [integer] | Exact |

---

##### 3.1.6 Figure Specification

**Atlas figure:** Figure [X.Y]

**Title:** *[Figure title from the Atlas]*

**Layout:** [Number of panels, arrangement]

**Panel descriptions:**

| Panel | Axes | Data | Reference overlays | Structural feature |
|-------|------|------|-------------------|-------------------|
| [1] | $x$: [variable, range]; $y$: [variable, range, scale] | [Curves to plot] | [Analytic lines, thresholds] | [What the panel demonstrates] |
| [2] | ... | ... | ... | ... |

**Figure-ready output file:** `figures/fig_[X.Y].{ext}`

**Columns in figure-ready file:**

| Column | Variable | Units |
|--------|----------|-------|
| 1 | [e.g., $t$] | dimensionless |
| 2 | [e.g., $|a_1(t)|$] | dimensionless |
| ... | ... | ... |

---

##### 3.1.7 Validation Criteria

**Structural checks** (must pass):

| Check | Criterion |
|-------|-----------|
| Positivity converged | No projection events during integration |
| Energy monotonicity | No E05 or E06 warnings |
| Clean termination | `termination_reason = FinalTime` |

**Quantitative checks** (must pass for the experiment to be accepted):

| Observable | Criterion | Method |
|-----------|-----------|--------|
| [e.g., $\hat{\sigma}$] | [e.g., "Within $1\%$ of $D\alpha_1 = 2.080$"] | [e.g., "Fit slope of $\ln|a_1|$ over $t \in [0.5, 4.5]$"] |
| [e.g., $\hat{\omega}$] | [e.g., "Within $1\%$ of $\omega = 0.831$"] | [e.g., "Zero-crossing intervals of $a_0(t)$"] |

**Convergence verification** (required / exempted):

| Study | Required? | Refinement levels | Acceptance |
|-------|-----------|-------------------|------------|
| Spatial | [Yes / No] | [e.g., $N \in \{128, 256, 512\}$] | [e.g., $p_h = 2.0 \pm 0.2$] |
| Temporal | [Yes / No] | [e.g., $\Delta t \in \{10^{-3}, 5 \times 10^{-4}, 2.5 \times 10^{-4}\}$] | [e.g., $p_t = 2.0 \pm 0.6$] |

---

### 3.2 Worked Example: Experiment 3.1 (Single-Mode Exponential Decay)

The following is the complete template instantiation for Experiment 3.1 of the Numerical Atlas (§3.1.2).

---

#### EXPERIMENT 3.1

**Atlas reference:** Section §3.1.2, Experiment 3.1

---

##### Purpose

Verify that each spatial mode $n \geq 1$ of the linearized ED system decays independently at the analytically predicted rate $D\alpha_n = D(M_*\mu_n + P_*')$, with no inter-mode energy transfer at small amplitude.

**Demonstrates:** Theorem C.17(i), equation C.11

**Architectural feature:** Modal hierarchy (Principle 1) — the spectral ordering of decay rates.

---

##### Required Parameters

**Parameter set:** II (Moderate Oscillatory)

**Overrides:** None.

**Derived quantities:**

| Quantity | Value |
|----------|-------|
| $H = 1 - D$ | $0.4$ |
| $\Delta = D + 2\zeta$ | $1.6$ |
| $M_* = M(0.5)$ | $0.25$ |
| $M_*' = M'(0.5)$ | $-1.0$ |
| $P_*' = P_0$ | $1.0$ |
| $\mathscr{D}_0$ | $-1.59$ |
| $\gamma_0$ | $0.55$ |
| $\omega$ | $0.630$ |
| Regime | Oscillatory |

**Constitutive functions:**

| Function | Form | Parameters |
|----------|------|-----------|
| $M(\rho)$ | $(\rho_{\max} - \rho)^2$ | $M_0 = 1.0$, $\beta = 2.0$ |
| $P(\rho)$ | $\rho - \rho^*$ | $P_0 = 1.0$ |

---

##### Initial Conditions

**IC type:** A (Single-mode perturbation)

**IC parameters (four sub-experiments, one per mode):**

| Sub-experiment | Mode $n$ | Amplitude $A$ | $v_0$ |
|---------------|----------|--------------|-------|
| 3.1a | $1$ | $10^{-3}$ | $0$ |
| 3.1b | $2$ | $10^{-3}$ | $0$ |
| 3.1c | $3$ | $10^{-3}$ | $0$ |
| 3.1d | $4$ | $10^{-3}$ | $0$ |

**Initial complexity (sub-experiment 3.1a):** $C_{\mathrm{ED}}(0) = A^2\mu_1/2 = 10^{-6} \cdot 9.870/2 = 4.93 \times 10^{-6}$.

**Admissibility:** $\min_j\rho_j(0) = 0.5 - 10^{-3} = 0.499 > 0$; $\max_j\rho_j(0) = 0.5 + 10^{-3} = 0.501 < 1.0$.

---

##### Numerical Method

| Setting | Value |
|---------|-------|
| Spatial method | Spectral (Method B) |
| Time-stepping scheme | ETD-RK4 |
| Spatial dimension | $1$ |
| Domain | $[0, 1]$, $L = 1$ |
| Spectral modes $N$ | $128$ |
| Time step $\Delta t$ | $10^{-4}$ |
| Final time $T$ | $5.0$ |
| CFL | Not binding (ETD unconditionally stable in linear part; $L_{\mathcal{N}} \approx 6 \times 10^{-6}$, $\Delta t_{\mathrm{rec}} \gg 1$) |
| Output sampling | Uniform, $k_{\mathrm{out}} = 50$ ($\sim 1000$ output points) |

---

##### Expected Outputs

**Time-series observables:**

| Observable | Expected behavior | Analytic prediction |
|-----------|-------------------|---------------------|
| $\mathcal{E}(t)$ | Monotonically decreasing | — |
| $C_{\mathrm{ED}}(t)$ | Exponential decay | $C_{\mathrm{ED}}(0)\,e^{-2D\alpha_n t}$ |

**Spectral observables (primary):**

| Sub-exp. | Mode | $\mu_n$ | $\alpha_n$ | $D\alpha_n$ | Expected $|a_n(t)|$ |
|----------|------|---------|-----------|------------|---------------------|
| 3.1a | $1$ | $9.870$ | $3.467$ | $2.080$ | $a_1(0)\,e^{-2.080\,t}$ |
| 3.1b | $2$ | $39.478$ | $10.870$ | $6.522$ | $a_2(0)\,e^{-6.522\,t}$ |
| 3.1c | $3$ | $88.826$ | $23.207$ | $13.924$ | $a_3(0)\,e^{-13.924\,t}$ |
| 3.1d | $4$ | $157.914$ | $40.478$ | $24.287$ | $a_4(0)\,e^{-24.287\,t}$ |

**Spectral purity check:** For each sub-experiment, $|a_m(t)| < 10^{-10}$ for all $m \neq n$ and all $t$ (no inter-mode leakage above machine-precision level).

**Scalar summary quantities:**

| Quantity | Symbol | Expected value | Tolerance |
|----------|--------|---------------|-----------|
| Decay rate (sub-exp. 3.1a) | $\hat{\sigma}_1$ | $2.080$ | $\pm 1\%$ |
| Decay rate (sub-exp. 3.1b) | $\hat{\sigma}_2$ | $6.522$ | $\pm 1\%$ |
| Decay rate (sub-exp. 3.1c) | $\hat{\sigma}_3$ | $13.924$ | $\pm 1\%$ |
| Decay rate (sub-exp. 3.1d) | $\hat{\sigma}_4$ | $24.287$ | $\pm 1\%$ |

---

##### Figure Specification

**Atlas figure:** Figure 3.1

**Title:** *Single-mode exponential decay*

**Layout:** Single panel, semilog-$y$

**Panel description:**

| Panel | Axes | Data | Reference overlays | Structural feature |
|-------|------|------|-------------------|-------------------|
| 1 | $x$: $t$, $[0, 5]$; $y$: $|a_n(t)|$, $[10^{-16}, 10^{-3}]$, log scale | Four curves: $|a_n(t)|$ for $n = 1, 2, 3, 4$ | Dashed lines with slopes $-D\alpha_n$ | Modal hierarchy: steeper slope = higher mode = faster decay |

**Figure-ready output file:** `figures/fig_3.1.csv`

**Columns:**

| Column | Variable |
|--------|----------|
| 1 | $t$ |
| 2 | $|a_1(t)|$ |
| 3 | $|a_2(t)|$ |
| 4 | $|a_3(t)|$ |
| 5 | $|a_4(t)|$ |

---

##### Validation Criteria

**Structural checks:**

| Check | Criterion |
|-------|-----------|
| Positivity converged | No projection events (amplitude $10^{-3}$ is deep in the admissible region) |
| Energy monotonicity | No warnings |
| Clean termination | `termination_reason = FinalTime` |

**Quantitative checks:**

| Observable | Criterion | Method |
|-----------|-----------|--------|
| $\hat{\sigma}_n$ for each $n$ | Within $1\%$ of $D\alpha_n$ | Fit slope of $\ln|a_n(t)|$ over $t \in [0.1, \min(4.0, t_{\mathrm{floor}}(n))]$ |
| Spectral purity | $\max_{m \neq n}|a_m(t)| < 10^{-10}$ for all $t$ | Monitor all modes $0$–$16$ at every output step |

**Convergence verification:**

| Study | Required? | Refinement levels | Acceptance |
|-------|-----------|-------------------|------------|
| Spatial | Yes | $N_{\mathrm{modes}} \in \{32, 64, 128\}$ | $e_h(64)/e_h(32) < 0.01$ (spectral convergence) |
| Temporal | Yes | $\Delta t \in \{4 \times 10^{-4}, 2 \times 10^{-4}, 10^{-4}\}$ | $p_t = 4.0 \pm 1.2$ (ETD-RK4) |

---

## 4. Parameter Surveys

### 4.1 Sweeping $D$, $\zeta$, $\tau$

The parameter surveys of the Numerical Atlas (§§2.4, 8.3) map the regime geometry, observable landscapes, and transition-time structure across the canonical parameter space. These surveys require hundreds of independent integrations — one per grid point in the $(D, \zeta)$-plane, repeated for each value of $\tau$ — and produce the regime maps (Figures 2.7–2.9, 8.5–8.8), the observable contour maps (Figure 8.6), and the transition-time landscape (Figure 8.7).

This subsection specifies the sweep infrastructure: the parameter ranges and grid construction (§4.1.1), the resolution and method settings (§4.1.2), the output structure for sweep data (§4.1.3), and the algorithms for generating regime maps and observable landscapes from the raw sweep output (§4.1.4).

---

#### 4.1.1 Sweep Ranges and Grid Construction

##### 4.1.1.1 One-Dimensional Sweeps

Several Atlas experiments sweep a single parameter while holding the others fixed:

| Experiment | Swept parameter | Base | Range | Points | Spacing |
|-----------|----------------|------|-------|--------|---------|
| 2.2 | $\zeta$ | Set I ($D = 0.3$) | $[0.05, 0.5]$ | $5$ | Selected values |
| 2.4 | $D$ | Set IV ($\zeta = 5.0$) | $[0.7, 0.95]$ | $5$ | Selected values |
| 3.5 | $D$ | Set II ($\zeta = 0.5$) | $[0.1, 0.9]$ | $9$ | Uniform, step $0.1$ |
| 4.5 | $\epsilon$ (amplitude) | Set I | $[0.02, 0.2]$ | $5$ | Selected values |
| 4.6 | $D$ | Set I base | $[0.1, 0.9]$ | $6$ | Selected values |
| 5.3 | $A$ (amplitude) | Set II | $[0.01, 0.4]$ | $7$ | Selected values |
| 7.6 | $A$ (amplitude) | Set I | $[0.005, 0.4]$ | $10$ | Selected values |
| 8.1 | $\zeta$ | Custom ($D = 0.5$) | $[0.5, 3.0]$ | $41$ | Uniform, step $\approx 0.061$ |

For one-dimensional sweeps, the parameter list is generated by one of two methods:

**Uniform spacing.** $p_i = p_{\min} + i \cdot (p_{\max} - p_{\min})/(N_{\mathrm{sweep}} - 1)$ for $i = 0, 1, \ldots, N_{\mathrm{sweep}} - 1$. This is the default for dense sweeps (Experiments 3.5, 8.1).

**Selected values.** An explicit list $\{p_1, p_2, \ldots, p_K\}$ chosen to sample specific regimes, thresholds, or transition points. This is used when the sweep spans a large dynamic range or when specific values have analytic significance (e.g., the critical $\zeta_c$).

For all one-dimensional sweeps, the parameter list is validated by the sweep-level checks of §2.2.5: monotonicity, uniqueness, and regime-transition detection.

##### 4.1.1.2 Two-Dimensional Sweeps: The $(D, \zeta)$-Grid

The regime maps (Atlas §§2.4, 8.3) require a two-dimensional sweep across the $(D, \zeta)$-plane. The standard grid is:

**Coarse grid** (Experiments 2.7, 8.5–8.7):

| Axis | Range | Points | Values |
|------|-------|--------|--------|
| $D$ | $[0.1, 0.9]$ | $9$ | $\{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9\}$ |
| $\zeta$ | $[0.1, 5.0]$ | $9$ | $\{0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0\}$ |
| **Total points** | | **81** | |

The $\zeta$-values are not uniformly spaced — they are denser at small $\zeta$ (where the Spiral Sheet is located and the regime transitions occur) and sparser at large $\zeta$ (where the dynamics are uniformly overdamped and vary slowly). This non-uniform spacing provides better resolution near the Boundary Surface $\Sigma$ without wasting grid points in the featureless deep Monotonic Cone.

**Fine grid** (optional, for higher-resolution regime maps):

| Axis | Range | Points | Spacing |
|------|-------|--------|---------|
| $D$ | $[0.05, 0.95]$ | $19$ | Uniform, step $\approx 0.0474$ |
| $\zeta$ | $[0.05, 5.0]$ | $25$ | Logarithmic: $\zeta_i = 0.05 \cdot (100)^{i/24}$ |
| **Total points** | | **475** | |

The logarithmic spacing in $\zeta$ places $\sim 60\%$ of the grid points in $[0.05, 1.0]$ (near the transition region) and $\sim 40\%$ in $[1.0, 5.0]$. The fine grid is used when the coarse grid's resolution is insufficient to resolve the Boundary Surface accurately (e.g., for determining $\zeta_c$ by interpolation).

**Grid construction.** For each grid point $(D_i, \zeta_j)$:

1. Load the base parameter set (default: all constitutive parameters from Set I, with $\tau = 1.0$).
2. Override $D \leftarrow D_i$ and $\zeta \leftarrow \zeta_j$.
3. Compute $H = 1 - D_i$ and all derived quantities.
4. Run the three-level validation (§2.2.3).
5. Store the validated parameter record in the 2D sweep array at position $(i, j)$.

The sweep array is a 2D grid of `CanonicalParams` records, indexed by $(i, j)$.

##### 4.1.1.3 Three-Dimensional Sweeps: The $(D, \zeta, \tau)$-Family

Experiment 8.8 extends the $(D, \zeta)$-grid to a family parameterized by $\tau$:

| Parameter | Values |
|-----------|--------|
| $\tau$ | $\{0.25, 0.5, 1.0, 2.0\}$ |
| $(D, \zeta)$ | The coarse $9 \times 9$ grid for each $\tau$ |
| **Total points** | $4 \times 81 = 324$ |

At each $\tau$ value, the entire $(D, \zeta)$-grid is constructed with that $\tau$, and the constitutive parameters are adjusted for the non-canonical normalization: $P_*' = P_0 = 1.0$ is held fixed, so $\tau P_*'$ varies across the family ($\tau P_*' \in \{0.25, 0.5, 1.0, 2.0\}$). The critical surface $\Sigma(\tau)$ shifts accordingly:

$$
\mathscr{D}_0(\tau) = \left(D P_*' - \frac{\zeta}{\tau}\right)^2 - \frac{4(1-D)P_*'}{\tau}.
$$

The analytic $\Sigma(\tau)$ is computed at each $\tau$ for comparison with the numerical regime classification.

---

#### 4.1.2 Resolution and Method Settings

All sweep integrations use the same numerical method and resolution, ensuring that differences between grid points are attributable to the parameter values alone, not to numerical artifacts.

**Standard sweep settings:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| Spatial method | FD, Crank–Nicolson (Method A) | General-purpose; no spectral analysis needed |
| Grid points $N$ | $512$ | Converged for all IC types at the default constitutive parameters |
| Time step $\Delta t$ | $5 \times 10^{-4}$ | Below CFL for all $(D, \zeta)$ in the sweep range |
| Final time $T$ | $30$ | Sufficient for Stage III convergence at all parameter values |
| IC (small-amplitude sweep) | IC-A, $A = 0.01$, $v_0 = 0.01$ | Linearized regime; regime classification from eigenvalue structure |
| IC (large-amplitude sweep) | IC-C, $A = 0.3$, $\sigma = 0.05$, $v_0 = 0.1$ | Nonlinear regime; tests complexity-driven regime modifications |
| Output sampling | Uniform, $k_{\mathrm{out}} = 100$ | $\sim 600$ output points per integration |

**CFL verification across the grid.** The CFL constraint (§1.8.1) depends on $D$, $M'(\rho)$, and $|\nabla\rho|$. The most restrictive CFL occurs at the grid point with the largest $D$ and the steepest initial gradient. For the small-amplitude IC ($A = 0.01$): $|\nabla\rho|_{\max} \approx A\pi \approx 0.031$, giving $\Delta t_{\mathrm{CFL}} \gg 5 \times 10^{-4}$ at all grid points. For the large-amplitude IC ($A = 0.3$, $\sigma = 0.05$): $|\nabla\rho|_{\max} \approx A/\sigma = 6$, and the worst-case CFL at $D = 0.9$ is $\Delta t_{\mathrm{CFL}} \approx 6 \times 10^{-6}$ — below the default $\Delta t$. For these grid points, the adaptive time-step reduction (§1.6.2) activates automatically during the initial transient and restores the nominal $\Delta t$ once the gradients have been smoothed.

**Parallelization.** The $81$ (or $324$, or $475$) integrations are independent — no integration depends on the results of any other. They can be distributed across multiple cores, each running a single integration to completion. The sweep orchestrator (§2.5.5) assigns sweep points to available cores, collects the results, and assembles the sweep output. No inter-process communication is needed during the integrations.

---

#### 4.1.3 Output Structure for Sweep Data

Each sweep produces a structured dataset indexed by the sweep coordinates $(D_i, \zeta_j)$ (or $(D_i, \zeta_j, \tau_k)$ for the three-parameter family). The dataset combines the per-integration scalar outputs into a grid-indexed array.

##### 4.1.3.1 Per-Point Output

For each grid point $(D_i, \zeta_j)$, the integration produces the full output described in §2.4 (time series, spectral log if applicable, diagnostics, summary). In addition, the sweep orchestrator extracts a set of **sweep scalars** — the quantities needed for the regime maps and observable landscapes:

| Scalar | Symbol | Extraction method |
|--------|--------|------------------|
| Discriminant | $\mathscr{D}_0(D_i, \zeta_j)$ | Computed analytically from parameters |
| Regime classification (analytic) | — | Sign of $\mathscr{D}_0$: $< 0$ → Oscillatory, $= 0$ → Critical, $> 0$ → Monotonic |
| Regime classification (numerical) | — | $N_{\mathrm{cross}} \geq 1$ → Oscillatory; $N_{\mathrm{cross}} = 0$ → Monotonic |
| Zero-crossing count | $N_{\mathrm{cross}}$ | Count sign changes of $a_0(t)$ in $[0, T]$ |
| Measured decay rate | $\hat{\gamma}$ | Fit slope of $\ln\mathcal{V}(t)$ over $[T/2, T]$ |
| Measured frequency | $\hat{\omega}$ | Mean of $\pi/(t_{k+1} - t_k)$ over consecutive zero crossings (if $N_{\mathrm{cross}} \geq 2$); $0$ otherwise |
| Transition time | $t_*$ | First time at which $\hat{\beta}(t) \geq 0.9 \cdot 2\gamma_*$ (§7.4) |
| Final deviation | $\|\rho(T) - \rho^*\|_{L^2}$ | $L^2$-norm at final time |
| Integration health | — | `positivity_converged`, warning counts |

##### 4.1.3.2 Grid-Indexed Arrays

The sweep scalars are assembled into grid-indexed arrays for post-processing:

| Array | Shape | Contents |
|-------|-------|----------|
| `D0_grid` | $(N_D, N_\zeta)$ | $\mathscr{D}_0(D_i, \zeta_j)$ |
| `regime_analytic` | $(N_D, N_\zeta)$ | Analytic regime classification (integer: $-1$, $0$, $+1$) |
| `regime_numerical` | $(N_D, N_\zeta)$ | Numerical regime classification (integer: $-1$, $0$, $+1$) |
| `N_cross` | $(N_D, N_\zeta)$ | Zero-crossing counts |
| `gamma_hat` | $(N_D, N_\zeta)$ | Measured decay rates |
| `omega_hat` | $(N_D, N_\zeta)$ | Measured frequencies ($0$ if monotonic) |
| `t_star` | $(N_D, N_\zeta)$ | Transition times |
| `deviation_final` | $(N_D, N_\zeta)$ | Final $L^2$-deviations |
| `health` | $(N_D, N_\zeta)$ | Boolean: all-clean integrations |

For the three-parameter family, the arrays gain a third index: shape $(N_D, N_\zeta, N_\tau)$.

##### 4.1.3.3 Directory Structure

The sweep output follows the naming conventions of §2.4.5:

```
output/exp_8.5/
├── sweep_grid.{ext}              # Grid coordinates: D_i, ζ_j arrays
├── sweep_scalars.{ext}           # All grid-indexed arrays above
├── sweep_progress.{ext}          # Completion status per grid point
├── D_0.100_zeta_0.100/           # Per-point output directory
│   ├── small_amp/
│   │   ├── timeseries.{ext}
│   │   ├── summary.{ext}
│   │   └── ...
│   └── large_amp/
│       ├── timeseries.{ext}
│       ├── summary.{ext}
│       └── ...
├── D_0.100_zeta_0.300/
│   └── ...
└── ...
```

The `sweep_grid.{ext}` file stores the coordinate arrays $(D_1, \ldots, D_{N_D})$ and $(\zeta_1, \ldots, \zeta_{N_\zeta})$ and the analytic discriminant $\mathscr{D}_0$ at every grid point. The `sweep_scalars.{ext}` file stores all the grid-indexed arrays. Both files include the experiment metadata (§2.4.4).

---

#### 4.1.4 Regime Map Generation

The regime maps (Figures 2.7, 8.5, 8.8) and observable landscapes (Figures 8.6, 8.7) are derived from the grid-indexed arrays by a post-processing pipeline that operates on the completed sweep data.

##### 4.1.4.1 Regime Classification Map

The regime map assigns a color (or symbol) to each grid point based on its regime classification:

1. **Analytic classification.** For each $(D_i, \zeta_j)$, the regime is determined by $\operatorname{sign}(\mathscr{D}_0)$:
   - $\mathscr{D}_0 < 0$: Oscillatory (blue circle).
   - $\mathscr{D}_0 = 0$ (within $|\mathscr{D}_0| < 10^{-10}$): Critical (diamond).
   - $\mathscr{D}_0 > 0$: Monotonic (red square).

2. **Numerical classification.** The same assignment, but based on the observed $N_{\mathrm{cross}}$:
   - $N_{\mathrm{cross}} \geq 1$: Oscillatory.
   - $N_{\mathrm{cross}} = 0$: Monotonic.

3. **Discrepancy detection.** Grid points where the analytic and numerical classifications disagree are marked with a special symbol (diamond overlay, as in Figure 8.5). These are the points in the nonlinear transition band (§8.2 of the Atlas).

##### 4.1.4.2 Boundary Surface Extraction

The Boundary Surface $\Sigma$ is extracted from the discriminant grid by identifying all adjacent pairs of grid points where $\mathscr{D}_0$ changes sign:

1. For each pair of horizontally adjacent grid points $((D_i, \zeta_j), (D_{i+1}, \zeta_j))$ with $\mathscr{D}_0(D_i, \zeta_j) \cdot \mathscr{D}_0(D_{i+1}, \zeta_j) < 0$: interpolate to find $D_c = D_i + (D_{i+1} - D_i)\,|\mathscr{D}_0(D_i)|/(|\mathscr{D}_0(D_i)| + |\mathscr{D}_0(D_{i+1})|)$.
2. Repeat for vertically adjacent pairs.
3. Connect the interpolated zero-crossing points into a piecewise-linear contour.

The resulting contour is the numerical approximation to $\Sigma$. It is compared to the analytic parabola $(D - \zeta)^2 = 4(1 - D)$ (in the canonical normalization $\tau P_*' = 1$) or the general formula (for non-canonical $\tau$).

##### 4.1.4.3 Observable Contour Maps

The decay rate $\hat{\gamma}(D, \zeta)$ and frequency $\hat{\omega}(D, \zeta)$ are interpolated from the grid values to produce smooth contour maps:

1. **Bilinear interpolation.** Between the $9 \times 9$ grid points, the observable values are estimated by bilinear interpolation on each grid cell. This produces a piecewise-bilinear surface over the $(D, \zeta)$-plane.

2. **Contour extraction.** Contour lines at specified levels (e.g., $\hat{\gamma} \in \{0.1, 0.2, 0.5, 1.0, 2.0, 3.0\}$, $\hat{\omega} \in \{0.2, 0.4, 0.6, 0.8, 1.0\}$) are extracted by the marching-squares algorithm applied to the bilinear surface.

3. **Analytic comparison.** The analytic contours (from the eigenvalue formulas C.15) are overlaid on the numerical contours. Agreement confirms the accuracy of both the integration and the observable extraction.

##### 4.1.4.4 Transition-Time Landscape

The transition time $t_*(D, \zeta)$ is interpolated and contoured using the same bilinear/marching-squares procedure. The key features to verify are:

- **Ridge along $\Sigma$.** The transition time peaks near the Boundary Surface, where the near-critical slowdown extends the algebraic phase (Stage II of Theorem C.76). The ridge position should coincide with the extracted $\Sigma$ contour.
- **Valley at large $D$, $\zeta$.** The transition time is minimal in the deep Monotonic Cone, where strong damping drives rapid convergence.
- **Plateau in the deep Spiral Sheet.** The transition time is moderate at small $D$, small $\zeta$, where the oscillatory participation channel provides efficient energy dissipation.

##### 4.1.4.5 Three-Parameter Visualization

For the $(D, \zeta, \tau)$-family (Experiment 8.8), the regime maps are presented as a panel array — one $(D, \zeta)$-map per $\tau$ value:

1. Generate the regime classification map (§4.1.4.1) at each $\tau$.
2. Extract the Boundary Surface $\Sigma(\tau)$ at each $\tau$.
3. Arrange the four maps in a $2 \times 2$ panel layout (Figure 8.8).
4. Optionally, overlay all four $\Sigma(\tau)$ curves on a single panel to show the systematic expansion of the Spiral Sheet with increasing $\tau$.

The structural prediction to verify: the Spiral Sheet expands as $\tau$ increases (the participation integration time favors oscillation), and the $\Delta = 1$ contour coincides with the inner boundary of the Spiral Sheet only at the canonical normalization $\tau P_*' = 1$ ($\tau = 1.0$ for the default $P_0 = 1.0$).

---

#### 4.1.5 Sweep Execution Summary

| Sweep | Experiment | Grid | Points | ICs per point | Total integrations | Estimated wall time (1 core) |
|-------|-----------|------|--------|--------------|-------------------|------------------------------|
| $\zeta$-sweep | 8.1 | $1 \times 41$ | $41$ | $1$ | $41$ | $\sim 3$ min |
| $(D, \zeta)$ coarse, small amp. | 8.5 (left) | $9 \times 9$ | $81$ | $1$ | $81$ | $\sim 7$ min |
| $(D, \zeta)$ coarse, large amp. | 8.5 (right) | $9 \times 9$ | $81$ | $1$ | $81$ | $\sim 7$ min |
| $(D, \zeta)$ observables | 8.6 | $9 \times 9$ | $81$ | $1$ | $81$ | $\sim 7$ min |
| $(D, \zeta)$ transition time | 8.7 | $9 \times 9$ | $81$ | $1$ | $81$ | $\sim 7$ min |
| $(D, \zeta, \tau)$ family | 8.8 | $9 \times 9 \times 4$ | $324$ | $1$ | $324$ | $\sim 27$ min |
| $(D, \zeta)$ fine (optional) | — | $19 \times 25$ | $475$ | $1$ | $475$ | $\sim 40$ min |
| **Total (standard)** | | | | | **$689$** | **$\sim 58$ min** |

The standard sweep program ($689$ integrations) completes in under one hour on a single core and under $5$ minutes on a $16$-core workstation with the sweep orchestrator distributing points across cores. The optional fine grid adds $40$ minutes (single core).

---

### 4.2 Sweeping Initial Complexity

The parameter sweeps of §4.1 vary the canonical parameters ($D$, $\zeta$, $\tau$) while holding the initial condition fixed. The complexity sweeps of this subsection do the opposite: the canonical parameters are held fixed, and the initial ED-complexity $C_{\mathrm{ED}}(0) = \int_\Omega|\nabla\rho_0|^2\,dx$ is varied systematically. These sweeps target the dependence of the dynamics on the *state* rather than on the *parameters* — the complexity-ordered decoherence (Atlas §5, §9.1), the stability threshold $\epsilon_0$ (Atlas §5.2), the transition time $t_*$ (Atlas §7.4), and the complexity-driven regime transitions (Atlas §8.2).

---

#### 4.2.1 Methods for Varying $C_{\mathrm{ED}}$

The ED-complexity depends on the spatial gradient content of the initial density field. For a fixed domain $\Omega = [0, L]$ and fixed equilibrium $\rho^*$, the complexity can be varied through three independent mechanisms:

##### 4.2.1.1 Amplitude Variation (Fixed Spatial Structure)

The simplest method: scale the perturbation amplitude $A$ while keeping the spatial profile fixed. For IC-A with mode $n$:

$$
\rho_0(x) = \rho^* + A\cos(n\pi x/L), \qquad C_{\mathrm{ED}}(0) = \frac{A^2\,n^2\pi^2}{2L}.
$$

The complexity scales as $A^2$. Varying $A$ over $[A_{\min}, A_{\max}]$ produces a complexity range $[A_{\min}^2 n^2\pi^2/(2L),\; A_{\max}^2 n^2\pi^2/(2L)]$.

**Advantages.** The spatial structure is identical at every sweep point (the same mode $n$, the same number of extrema, the same symmetry). Any difference in the dynamics is attributable to the amplitude alone. This isolates the role of $C_{\mathrm{ED}}$ in the nonlinear stability (Theorem C.43): smaller $A$ places the system inside the stability basin ($\|u_0\|_{H^1} < \epsilon_0$), larger $A$ places it outside.

**Limitations.** The $L^2$-norm $\|u_0\|_{L^2} = A/\sqrt{2}$ varies simultaneously with $C_{\mathrm{ED}}$. This means that both the gradient content and the mean deviation change, and the observed effects cannot be attributed to the gradients alone. For experiments requiring constant $L^2$-norm (e.g., the complexity-ordering demonstration of Atlas §5.3), the mode-variation method (§4.2.1.2) is used instead.

**Atlas experiments using this method:** 3.2 ($A$ sweep, mode $n = 1$), 4.5 ($\epsilon$ sweep for locked ratio), 5.3 ($A$ sweep for convergence rate vs. complexity), 7.6 ($A$ sweep for transition time).

| Experiment | $A$ values | $n$ | $C_{\mathrm{ED}}(0)$ range | Parameter set |
|-----------|-----------|-----|---------------------------|---------------|
| 3.2 | $\{10^{-4}, 10^{-3}, 10^{-2}, 0.05, 0.2\}$ | $1$ | $[4.9\times10^{-8},\; 0.197]$ | II |
| 4.5 | $\{0.02, 0.05, 0.1, 0.15, 0.2\}$ | $1$ | $[1.97\times10^{-3},\; 0.197]$ | I |
| 5.3 | $\{0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4\}$ | Gaussian | $[0.009,\; 14.18]$ | II |
| 7.6 | $\{0.005, \ldots, 0.4\}$ (10 values) | Gaussian | $[0.002,\; 14.18]$ | I |

##### 4.2.1.2 Mode Variation (Fixed Amplitude)

Vary the mode number $n$ while holding the amplitude $A$ constant. For IC-A:

$$
C_{\mathrm{ED}}(0) = \frac{A^2\,n^2\pi^2}{2L}.
$$

The complexity scales as $n^2$. This method keeps the $L^2$-norm $\|u_0\|_{L^2} = A/\sqrt{2}$ constant across the sweep — a critical requirement for the complexity-ordering experiments (Atlas §5.3, §9.1), which must demonstrate that systems with the same "mass" (same $L^2$-deviation) evolve on different time scales because of their different gradient content.

**Advantages.** The $L^2$-norm is identical at every sweep point. The total mass perturbation $\int_\Omega u_0\,dx = 0$ for all $n \geq 1$ (cosine modes have zero mean on $[0, L]$). Any difference in the dynamics is attributable to the spatial frequency — equivalently, to the gradient content — alone.

**Limitations.** The spatial structure changes qualitatively across the sweep (mode $1$ has one arch, mode $8$ has eight arches). The decay rate at each sweep point is dominated by the single initialized mode ($D\alpha_n$), so the "decoherence rate" varies as $D(M_*n^2\pi^2/L^2 + P_*')$ — a quadratic function of $n$, hence a linear function of $C_{\mathrm{ED}}(0)$ for fixed $A$. This linearity is the complexity-ordering prediction of the Applications Paper (§3.1).

**Atlas experiments using this method:** 5.5 (modes $n = 1, 4$), 5.6 (modes $n = 1, 2, 3, 4, 6$), 9.1 (modes $n = 1, 2, \ldots, 10$).

| Experiment | Mode values | $A$ | $C_{\mathrm{ED}}(0)$ range | Parameter set |
|-----------|------------|-----|---------------------------|---------------|
| 5.5 | $\{1, 4\}$ | $0.1$ | $[0.049,\; 0.790]$ | II |
| 5.6 | $\{1, 2, 3, 4, 6\}$ | $0.1$ | $[0.049,\; 1.776]$ | II |
| 9.1 | $\{1, 2, 3, 4, 5, 6, 8, 10\}$ | $0.05$ | $[0.012,\; 1.234]$ | II |

##### 4.2.1.3 Multi-Mode Superposition (Variable Spectral Breadth)

Vary the number of initialized modes while holding the per-mode amplitude fixed. For IC-B with $N_m$ modes and amplitudes $A_n$:

$$
C_{\mathrm{ED}}(0) = \sum_{n=1}^{N_m}\frac{A_n^2\,n^2\pi^2}{2L}.
$$

Increasing $N_m$ adds higher-frequency content, raising $C_{\mathrm{ED}}$ without changing the low-mode amplitudes. This method models the physical scenario where complexity increases through the addition of fine-scale structure (more spatial detail, more gradient content) rather than through the amplification of a single mode.

**Atlas experiments using this method:** 5.1 (LC/MC/HC configurations), 9.2 (galaxy analogues G1–G5).

| Experiment | Configuration | $N_m$ | $C_{\mathrm{ED}}(0)$ | Parameter set |
|-----------|--------------|-------|---------------------|---------------|
| 5.1 LC | $A\cos(\pi x)$ | $1$ | $1.97\times10^{-3}$ | II |
| 5.1 MC | $A(\cos\pi x + \cos 2\pi x + \cos 3\pi x)$ | $3$ | $2.76\times10^{-2}$ | II |
| 5.1 HC | $A\sum_{n=1}^{8}\cos n\pi x$ | $8$ | $0.402$ | II |

##### 4.2.1.4 Gaussian Width Variation

For IC-C, vary the width $\sigma$ while holding the amplitude $A$ and center $x_0$ fixed:

$$
C_{\mathrm{ED}}(0) \approx \frac{A^2\sqrt{\pi}}{2\sigma^3\sqrt{2}}.
$$

The complexity scales as $\sigma^{-3}$: narrower Gaussians have steeper gradients and exponentially higher complexity. This method produces a very large dynamic range in $C_{\mathrm{ED}}$ with modest changes in $\sigma$.

**Advantages.** The $L^2$-norm $\|u_0\|_{L^2} \approx A(\pi\sigma^2)^{1/4}$ varies slowly with $\sigma$ (as $\sigma^{1/2}$), while $C_{\mathrm{ED}}$ varies rapidly ($\sigma^{-3}$). This provides near-constant "mass" with highly variable gradient content — an effective proxy for the physical scenario where complexity varies at approximately fixed system size.

**Not currently used in the Atlas** (all Gaussian experiments fix $\sigma = 0.05$ and vary $A$), but included in the Suite as a supported complexity-sweep method for future extensions.

---

#### 4.2.2 Measuring Complexity

The ED-complexity $C_{\mathrm{ED}}[\rho] = \int_\Omega|\nabla\rho|^2\,dx$ is measured at every output step by the observable extraction pipeline (§1.1.6, §2.3.3.3). This subsection specifies the three distinct measurements used in the complexity sweeps.

##### 4.2.2.1 Initial Complexity $C_{\mathrm{ED}}(0)$

The initial complexity is computed at $t = 0$ from the initial condition, before any time stepping. It is the independent variable of the complexity sweep — the quantity that is varied across sweep points.

**Method A computation.** Using the discrete gradient (§1.3.1):

$$
C_{\mathrm{ED}}(0) = h\sum_{j=0}^{N_{\mathrm{grid}}-1}\left(\frac{\rho_{j+1}^0 - \rho_{j-1}^0}{2h}\right)^2.
$$

**Method B computation.** Using the spectral coefficients directly:

$$
C_{\mathrm{ED}}(0) = \sum_{k=1}^{N_{\mathrm{modes}}-1}\mu_k\,|\hat{u}_k(0)|^2.
$$

This formula follows from Parseval's identity: $\|\nabla u\|_{L^2}^2 = \sum_k\mu_k|\hat{u}_k|^2$ (since $\nabla\phi_k = -\sqrt{\mu_k}\,\psi_k$ where $\psi_k$ is the corresponding sine function, and $\|\nabla\phi_k\|_{L^2}^2 = \mu_k$).

**Analytic formula.** For the standard IC types, $C_{\mathrm{ED}}(0)$ is known in closed form (§4.2.1, tables above). The numerically computed value must agree with the analytic formula to within $O(h^2)$ (Method A) or machine precision (Method B). This agreement is verified at initialization as part of the readiness check (§2.1.6).

##### 4.2.2.2 Time-Dependent Complexity $C_{\mathrm{ED}}(t)$

The complexity is tracked as a function of time at every output step. It is a monotonically decreasing function for single-mode initial conditions (where $C_{\mathrm{ED}}(t) = C_{\mathrm{ED}}(0)\,e^{-2D(\alpha_n - P_*')t}$) and a non-monotonic function for multi-mode initial conditions (where the nonlinear triad can temporarily transfer energy into higher modes, transiently increasing the complexity before diffusion extinguishes it).

The time-dependent complexity is used to:

- Verify the dissipation bound (Lemma C.6): the dissipation rate $-d\mathcal{E}/dt$ is bounded below by $DP_*'/M_* \cdot C_{\mathrm{ED}}(t)$.
- Identify the transition time $t_*$ (§7.4): the time at which $C_{\mathrm{ED}}(t)$ drops below a threshold related to $\epsilon_0$.
- Track the three-stage convergence: $C_{\mathrm{ED}}(t)$ decreases through all three stages, with different rates in each.

##### 4.2.2.3 Effective Complexity $C_{\mathrm{ED}}^{\mathrm{eff}}(t)$

The effective (dissipation-weighted) complexity (§6.3 of the Atlas):

$$
C_{\mathrm{ED}}^{\mathrm{eff}}(t) = \int_\Omega\frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx.
$$

This is the quantity that directly controls the dissipation rate: $-d\mathcal{E}/dt \geq D\,C_{\mathrm{ED}}^{\mathrm{eff}}$. Near equilibrium, $C_{\mathrm{ED}}^{\mathrm{eff}} = (P_*'/M_*)\,C_{\mathrm{ED}} = 4\,C_{\mathrm{ED}}$ (the amplification factor is constant). Near the horizon, $C_{\mathrm{ED}}^{\mathrm{eff}} \gg C_{\mathrm{ED}}$ (the amplification diverges as $M(\rho) \to 0$).

The effective complexity is computed at output steps for experiments that probe the near-horizon dynamics (Atlas §6.3, §9.5). Its computation requires the pointwise constitutive values $P'(\rho_j)$ and $M(\rho_j)$, which are already available from the operator evaluation.

**Discrete computation (Method A):**

$$
C_{\mathrm{ED}}^{\mathrm{eff}} = h\sum_{j=0}^{N_{\mathrm{grid}}-1}\frac{P'(\rho_j)}{M(\rho_j)}\left(\frac{\rho_{j+1} - \rho_{j-1}}{2h}\right)^2.
$$

The safeguarded constitutive evaluation (§1.6.6) prevents division by zero at grid points near $\rho_{\max}$.

---

#### 4.2.3 Expected Transitions

The complexity sweeps reveal four structurally distinct transitions, each governed by a specific threshold in $C_{\mathrm{ED}}(0)$.

##### 4.2.3.1 Linearized-to-Nonlinear Transition

**Threshold.** $C_{\mathrm{ED}}(0) \sim \epsilon_{\mathrm{nl}}^2$, where $\epsilon_{\mathrm{nl}}$ is the amplitude at which the nonlinear terms ($M'(\rho)|\nabla\rho|^2$) become comparable to the linear terms ($M_*\nabla^2\rho - P_*' u$).

**Observable signature.** Below the threshold: measured decay rates match the linearized prediction $D\alpha_n$ to within $1\%$. Above the threshold: the decay rate deviates by $O(A^2)$, the nonlinear triad is activated, and the harmonic cascade (§4.3 of the Atlas) becomes visible in the spectral log. The amplitude-dependent frequency shift (lower frequency at larger amplitude) is also detectable.

**Typical value.** For the default constitutive functions, the nonlinear-to-linear crossover occurs at $A \sim 0.01$–$0.05$ (Atlas §3.1.3, Experiment 3.2), corresponding to $C_{\mathrm{ED}}(0) \sim 5 \times 10^{-4}$–$0.01$.

**Detection in the sweep.** Compare $\hat{\sigma}$ (measured) to $D\alpha_n$ (analytic) at each sweep point. The transition is the $C_{\mathrm{ED}}$ value at which $|\hat{\sigma} - D\alpha_n|/D\alpha_n$ first exceeds $1\%$.

##### 4.2.3.2 Stability Basin Boundary

**Threshold.** $C_{\mathrm{ED}}(0) \sim \epsilon_0^2$, where $\epsilon_0 = \gamma_*/C_{\mathrm{nl}}$ is the local stability radius of Theorem C.43.

**Observable signature.** Below the threshold: the Lyapunov functional $\mathcal{V}(t)$ decays exponentially from $t = 0$ at rate $\gamma_*$ (pure Stage III). Above the threshold: the Lyapunov functional shows a non-exponential transient (Stages I–II) before entering the exponential regime at a later time $t_*$. The transition time $t_*$ increases monotonically with $C_{\mathrm{ED}}(0)$ above the threshold and is zero below it.

**Typical value.** For Parameter Set II, $\epsilon_0^2 \sim 0.05$ (Atlas §5.2, Experiment 5.4). For Parameter Set III (near-critical), $\epsilon_0^2 \sim 0.03$. For Parameter Set IV (deep monotonic), $\epsilon_0^2 \sim 5$.

**Detection in the sweep.** Plot $t_*(C_{\mathrm{ED}}(0))$. The basin boundary is the $C_{\mathrm{ED}}$ value at which $t_*$ first exceeds zero (operationally, first exceeds $1.0$, the detection threshold of §5.2 in the Atlas).

##### 4.2.3.3 Complexity-Driven Regime Transition

**Threshold.** $C_{\mathrm{ED}}(0) \sim C_{\mathrm{ED}}^{\mathrm{regime}}$, the complexity at which the effective damping parameter $\Delta_{\mathrm{eff}}(\rho)$ crosses the critical value (§8.2 of the Atlas).

**Observable signature.** Below the threshold: the system exhibits the regime predicted by the linearized classification (oscillatory or monotonic, depending on $\mathscr{D}_0$). Above the threshold: the system exhibits a *different* transient regime — oscillatory transients in a nominally monotonic system (Experiment 8.3), or monotonic transients in a nominally oscillatory system near the horizon (Experiment 8.4). The transition is visible as a change in $N_{\mathrm{cross}}$ (the zero-crossing count of $a_0(t)$) between adjacent sweep points.

**Typical value.** For Parameter Set III ($\mathscr{D}_0 = 0.2$, weakly monotonic): $C_{\mathrm{ED}}^{\mathrm{regime}} \sim 1$–$5$ (the high-complexity initial condition pushes $\Delta_{\mathrm{eff}}$ below $1$). For Parameter Set I ($\mathscr{D}_0 = -2.76$, deep oscillatory): $C_{\mathrm{ED}}^{\mathrm{regime}}$ is very large (the system must be pushed nearly to the horizon to suppress the oscillation).

**Detection in the sweep.** Compare the numerical regime classification ($N_{\mathrm{cross}}$-based) to the analytic classification ($\mathscr{D}_0$-based) at each sweep point. The transition is the $C_{\mathrm{ED}}$ value at which the two classifications first disagree.

##### 4.2.3.4 Near-Horizon Complexity Amplification

**Threshold.** $C_{\mathrm{ED}}(0) \sim C_{\mathrm{ED}}^{\mathrm{horizon}}$, the complexity at which the initial density profile enters the near-horizon region ($\max_j\rho_j > \rho_{\max} - \delta_{\mathrm{warn}}$).

**Observable signature.** Below the threshold: $C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}} \approx P_*'/M_*$ (constant amplification, near-equilibrium regime). Above the threshold: $C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}} \gg P_*'/M_*$ (divergent amplification, near-horizon regime). The amplification factor $\mathcal{A} = C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}}$ increases with $C_{\mathrm{ED}}(0)$ and can reach $10^2$–$10^5$ for configurations with peak densities close to $\rho_{\max}$ (Atlas §6.3, Experiment 6.7).

The near-horizon amplification has two dynamical consequences:

1. **Enhanced dissipation.** The energy loss rate $-d\mathcal{E}/dt \geq D\,C_{\mathrm{ED}}^{\mathrm{eff}}$ is much larger than $D\,(P_*'/M_*)\,C_{\mathrm{ED}}$, so the gradient content is destroyed faster than the bare complexity suggests.
2. **Gradient suppression.** The near-horizon gradients are preferentially destroyed (Proposition C.10), so the effective complexity drops rapidly even as the bare complexity decreases more slowly.

**Typical value.** For IC-C with $\sigma = 0.05$: $\max_j\rho_j = \rho^* + A$, which enters the near-horizon region ($\rho > 0.99$) when $A > 0.49$. The corresponding $C_{\mathrm{ED}}(0) \approx 0.49^2 \cdot 88.6 \approx 21$. For IC-D: the near-horizon region is entered by construction at any $\delta < 0.01$.

**Detection in the sweep.** Plot the amplification ratio $C_{\mathrm{ED}}^{\mathrm{eff}}(0)/C_{\mathrm{ED}}(0)$ versus $C_{\mathrm{ED}}(0)$. The transition is the $C_{\mathrm{ED}}$ value at which the ratio first exceeds $2 \cdot P_*'/M_*$ (twice the equilibrium value, indicating significant near-horizon contribution).

---

#### 4.2.4 Sweep Output and Post-Processing

The complexity sweep produces a one-dimensional array of results indexed by the initial complexity. The output structure is:

| Array | Shape | Contents |
|-------|-------|----------|
| `C_ED_initial` | $(N_{\mathrm{sweep}},)$ | $C_{\mathrm{ED}}(0)$ at each sweep point |
| `A_values` | $(N_{\mathrm{sweep}},)$ | Amplitude (or mode number, or $\sigma$) at each point |
| `sigma_hat` | $(N_{\mathrm{sweep}},)$ | Measured decay rate |
| `omega_hat` | $(N_{\mathrm{sweep}},)$ | Measured frequency ($0$ if monotonic) |
| `t_star` | $(N_{\mathrm{sweep}},)$ | Transition time |
| `N_cross` | $(N_{\mathrm{sweep}},)$ | Zero-crossing count |
| `C_ED_eff_initial` | $(N_{\mathrm{sweep}},)$ | $C_{\mathrm{ED}}^{\mathrm{eff}}(0)$ |
| `amplification` | $(N_{\mathrm{sweep}},)$ | $C_{\mathrm{ED}}^{\mathrm{eff}}(0)/C_{\mathrm{ED}}(0)$ |
| `half_life` | $(N_{\mathrm{sweep}},)$ | Time at which $C_{\mathrm{ED}}(t) = C_{\mathrm{ED}}(0)/2$ |
| `lyapunov_rate` | $(N_{\mathrm{sweep}},)$ | Late-time $\hat{\beta} = -d\ln\mathcal{V}/dt$ |

**Post-processing.** The threshold values $C_{\mathrm{ED}}^{\mathrm{nl}}$, $\epsilon_0^2$, $C_{\mathrm{ED}}^{\mathrm{regime}}$, and $C_{\mathrm{ED}}^{\mathrm{horizon}}$ are identified from the sweep arrays by the detection criteria of §4.2.3. These thresholds are reported in the sweep summary and annotated on the figures (vertical dashed lines on the $C_{\mathrm{ED}}$-axis plots).

**Scaling verification.** The key predictions to verify from the sweep data are:

| Prediction | Expected scaling | Atlas figure | Verification |
|-----------|-----------------|-------------|-------------|
| Decoherence rate | $\Gamma \propto C_{\mathrm{ED}}$ | 9.1 (right) | Slope $\approx 1$ on log-log $\Gamma$ vs. $C_{\mathrm{ED}}$ |
| Half-life | $t_{1/2} \propto 1/C_{\mathrm{ED}}$ | 5.6 (right) | Slope $\approx -1$ on log-log $t_{1/2}$ vs. $C_{\mathrm{ED}}$ |
| Transition time | $t_* \sim \ln(C_{\mathrm{ED}}/\epsilon_0^2)$ | 7.6 (right) | Logarithmic growth on semilog-$x$ |
| Locked ratio | $\bar{R}_{31}/\epsilon = \text{const}$ | 4.5 | Flat line on $\bar{R}_{31}/\epsilon$ vs. $\epsilon$ |
| Amplification | $\mathcal{A} \propto (P_*'/M_*) \cdot M_*/M(\rho_{\max\text{-value}})$ | 6.7 (right) | Power-law growth $(0.5/(1-\bar{\rho}))^2$ |

Each scaling law is a structural consequence of the architecture (traced to a specific theorem in Appendix C) and is testable as a straight line (or logarithmic curve) on the appropriate axes. The sweep data either confirms the scaling (the data falls on the predicted curve) or refutes it (systematic deviation), with no free parameters.

---

### 4.3 Sweeping Constitutive Functions

The parameter sweeps of §4.1 and the complexity sweeps of §4.2 operate within a single pair of constitutive functions (the default power-law mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ and linear penalty $P(\rho) = P_0(\rho - \rho^*)$). The universality class $\mathcal{U}_{\mathrm{ED}}$ (Appendix D) guarantees that the *qualitative* structure of the dynamics — the regime geometry, the modal hierarchy, the triad selection rule, the three-stage convergence, the mobility-collapse barrier — is insensitive to the specific constitutive choice, provided Principles 1–7 are satisfied. The *quantitative* details — decay rates, locked amplitude ratios, threshold values, transition times — depend on the constitutive functions through the equilibrium values $M_*$, $M_*'$, $P_*'$ and their higher derivatives.

This subsection specifies the constitutive sweeps: systematic variations of $M(\rho)$ and $P(\rho)$ that test the universality claim numerically and map the quantitative dependence of the key observables on the constitutive form. These sweeps are not part of the current Atlas (which uses a single constitutive pair for all 55 experiments) but are specified here as the extension framework for the constitutive survey identified in Atlas §12.4.

---

#### 4.3.1 Varying the Mobility $M(\rho)$

The mobility function must satisfy three constraints (§1.1.4): $M(\rho) > 0$ for $\rho \in (0, \rho_{\max})$, $M(\rho_{\max}) = 0$, and $M \in C^\infty([0, \rho_{\max}])$. Within these constraints, the functional form is free. The sweep explores three families of mobility functions, each parameterized by a single scalar, holding $P(\rho)$ fixed at the default linear penalty.

##### 4.3.1.1 Power-Law Family: Varying the Collapse Exponent $\beta$

The default mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ is parameterized by the exponent $\beta > 0$, which controls the rate at which the mobility vanishes at $\rho_{\max}$.

**Sweep range:** $\beta \in \{0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0\}$ (seven values).

**Effect on the dynamics.** The exponent $\beta$ controls three quantities:

| Quantity | Dependence on $\beta$ | Physical meaning |
|----------|-----------------------|-----------------|
| $M_* = M(\rho^*) = M_0(0.5)^\beta$ | Decreases with $\beta$ | Equilibrium diffusivity |
| $M_*' = -\beta M_0(0.5)^{\beta-1}$ | Magnitude increases with $\beta$ | Nonlinear coupling strength |
| Energy barrier: $\Phi(\rho) \sim (\rho_{\max} - \rho)^{-(\beta-1)}$ | Stronger for larger $\beta$ | Confinement of $\rho < \rho_{\max}$ |

At $\beta = 0.5$ (sub-linear): the mobility vanishes slowly, $M'(\rho) \to -\infty$ as $\rho \to \rho_{\max}$ (the derivative diverges), and the energy barrier is logarithmic ($\Phi \sim \ln(1/(\rho_{\max} - \rho))$). The triad coupling $M'(\rho)|\nabla\rho|^2$ is enhanced near the horizon.

At $\beta = 4$ (super-quadratic): the mobility vanishes rapidly, $M'(\rho) \to 0$ as $\rho \to \rho_{\max}$ (the derivative vanishes with the mobility), and the energy barrier is strong ($\Phi \sim (\rho_{\max} - \rho)^{-3}$). The triad coupling is suppressed near the horizon.

**Quantities preserved across the sweep** (universality predictions):

- Regime classification: the sign of $\mathscr{D}_0 = (DM_*\mu_0/L^2 + DP_*' - \zeta/\tau)^2 - 4HP_*'/\tau$ depends on $M_*$, which changes with $\beta$, so the regime may change across the sweep. The existence of the Spiral Sheet and Monotonic Cone — and the codimension-one Boundary Surface between them — is predicted to be universal (present for every $\beta$), even though the location of $\Sigma$ in the $(D, \zeta)$-plane shifts.

- Three-stage convergence: the qualitative structure (global bounds → algebraic decay → exponential decay) is predicted to persist for all $\beta > 0$, with only the quantitative rates ($\gamma_*$, $\beta_{\mathrm{exp}}$, $t_*$) changing.

- Triad selection rule: $k \in \{|m-n|, m+n\}$ is a property of the cosine eigenbasis and the quadratic structure of $|\nabla\rho|^2$, independent of $M(\rho)$. The selection rule is predicted to hold identically for all $\beta$.

**Quantities that change across the sweep** (constitutive-dependent predictions):

- Modal decay rates: $D\alpha_n = D(M_*\mu_n + P_*')$ depends on $M_*$, hence on $\beta$.
- Locked amplitude ratio: $\bar{R}_{31}/\epsilon = |M_*'|\,|\Gamma_{12,3}|/(D(\alpha_3 - \alpha_1))$ depends on $M_*'$ and $M_*$, both $\beta$-dependent.
- Stability threshold: $\epsilon_0 = \gamma_*/C_{\mathrm{nl}}$ depends on the curvature of $M$ and $P$ near equilibrium.
- Energy barrier strength: determines the confinement margin $\delta(\mathcal{E}_0)$.

##### 4.3.1.2 Sigmoid Family

An alternative mobility that vanishes smoothly at $\rho_{\max}$ with a different functional form:

$$
M_{\mathrm{sig}}(\rho) = \frac{M_0}{1 + e^{\kappa(\rho - \rho_{\mathrm{mid}})}},
$$

where $\rho_{\mathrm{mid}} = (\rho^* + \rho_{\max})/2$ is the midpoint density and $\kappa > 0$ controls the steepness of the transition. This sigmoid does not vanish exactly at $\rho_{\max}$ — it approaches zero exponentially as $\rho \to \infty$ — so it must be modified to satisfy Principle 4 exactly:

$$
M_{\mathrm{sig,mod}}(\rho) = M_{\mathrm{sig}}(\rho) \cdot (\rho_{\max} - \rho)^\beta / (\rho_{\max} - \rho)^\beta\big|_{\mathrm{normalized}},
$$

or more simply, the product $M_{\mathrm{sig}}(\rho)\cdot(\rho_{\max} - \rho)$ is used, which vanishes linearly at $\rho_{\max}$ and has a sigmoid-shaped interior profile.

**Sweep range:** $\kappa \in \{5, 10, 20, 50, 100\}$ (five values), with $\beta = 1$ (linear vanishing at $\rho_{\max}$).

**Purpose.** The sigmoid family tests whether the qualitative features depend on the *shape* of the mobility interior (the transition from high to low mobility as $\rho$ approaches $\rho_{\max}$) or only on the *endpoint* behavior ($M(\rho_{\max}) = 0$, the rate of vanishing). The universality prediction is that the qualitative features are independent of the interior shape.

##### 4.3.1.3 Piecewise-Smooth Family

A mobility that is constant in the interior and collapses in a narrow boundary layer near $\rho_{\max}$:

$$
M_{\mathrm{pw}}(\rho) = \begin{cases} M_0 & \text{if } \rho \leq \rho_{\max} - \delta_M, \\ M_0\left(\frac{\rho_{\max} - \rho}{\delta_M}\right)^\beta & \text{if } \rho > \rho_{\max} - \delta_M, \end{cases}
$$

where $\delta_M > 0$ is the boundary-layer width. This function is $C^0$ at $\rho = \rho_{\max} - \delta_M$ (and $C^{\beta-1}$ for integer $\beta$). It separates the two roles of the mobility: uniform diffusion in the interior (controlled by $M_0$) and barrier formation near $\rho_{\max}$ (controlled by $\delta_M$ and $\beta$).

**Sweep range:** $\delta_M \in \{0.01, 0.05, 0.1, 0.2, 0.4\}$ (five values), with $\beta = 2$.

**Purpose.** This family tests the sensitivity of the dynamics to the width of the mobility-collapse region. The universality prediction is that the qualitative features are insensitive to $\delta_M$ (they persist even when the collapse region is a narrow boundary layer), while the quantitative near-horizon behavior (gradient suppression, effective complexity amplification) depends on $\delta_M$.

**Regularity note.** The piecewise-smooth mobility violates the $C^\infty$ regularity assumption of §C.1.1 at $\rho = \rho_{\max} - \delta_M$. The simulation engine accepts this (the constitutive validation checks $M_*$, $M_*'$, and sampled $P'$ at the equilibrium and at 100 interior points, but does not verify $C^\infty$ smoothness). The reduced regularity may affect the convergence order near the junction point; the convergence study (§2.7) must be applied to verify that the results are converged despite the reduced smoothness.

---

#### 4.3.2 Varying the Penalty $P(\rho)$

The penalty function must satisfy $P(\rho^*) = 0$, $P'(\rho) > 0$ for all $\rho$, and $P \in C^\infty(\mathbb{R})$. The sweep explores three families.

##### 4.3.2.1 Power-Law Penalty

$$
P_{\mathrm{pow}}(\rho) = P_0\,\operatorname{sign}(\rho - \rho^*)\,|\rho - \rho^*|^q, \qquad q > 0.
$$

For $q = 1$: the default linear penalty. For $q > 1$: a super-linear penalty that grows faster than linear away from equilibrium (stronger restoring force at large deviations, weaker at small deviations). For $q < 1$: a sub-linear penalty (weaker at large deviations, stronger at small deviations — effectively a sharper cusp at $\rho^*$).

**Sweep range:** $q \in \{0.5, 0.75, 1.0, 1.5, 2.0, 3.0\}$ (six values).

**Derivative:** $P'(\rho) = P_0\,q\,|\rho - \rho^*|^{q-1}$. For $q < 1$: $P'(\rho) \to \infty$ as $\rho \to \rho^*$ (the penalty is sharply peaked at equilibrium). For $q = 1$: $P'(\rho) = P_0$ (constant). For $q > 1$: $P'(\rho^*) = 0$ (the penalty slope vanishes at equilibrium), violating the strict positivity requirement $P'(\rho^*) > 0$.

**Constraint resolution for $q > 1$.** The condition $P'(\rho^*) > 0$ fails for $q > 1$ because $P'(\rho^*) = P_0 q \cdot 0^{q-1} = 0$. This means the super-linear penalty does *not* satisfy Principle 3 at the equilibrium. The penalty floor in the decay-rate funnel ($D\alpha_n \geq DP_*' = 0$) collapses, and the spectral gap may vanish (the homogeneous mode has zero penalty restoring force at $\rho^*$). This violation is structural — it removes the unique-equilibrium guarantee of Theorem C.70 (Step 3 requires $P' > 0$ at the equilibrium to identify $\rho_\infty = \rho^*$).

The sweep includes $q > 1$ values deliberately, to test the *necessity* of Principle 3: the universality claim predicts that the qualitative features persist only when $P'(\rho^*) > 0$, and that the $q > 1$ penalty produces qualitatively different dynamics (possible multiple equilibria, loss of the spectral gap, failure of the three-stage convergence). Observing this failure is a *confirmation* of the architecture — it shows that the principle is not merely sufficient but also necessary.

**Workaround for numerical testing.** For $q > 1$, the constitutive validation (§2.1.3) will flag $P'(\rho^*) = 0$ as a fatal error. The engine must be run with the penalty-slope check overridden (a special mode that logs the violation but does not halt). The override is indicated in the experiment metadata as `P_prime_override = true`.

##### 4.3.2.2 Nonlinear Monotone Penalty

$$
P_{\mathrm{nl}}(\rho) = P_0\,\tanh\!\left(\frac{\rho - \rho^*}{\rho_w}\right),
$$

where $\rho_w > 0$ is the width of the transition. This penalty is strictly monotone ($P' > 0$ everywhere), smooth, and bounded: $|P(\rho)| \leq P_0$ for all $\rho$. The derivative is $P'(\rho) = P_0/(\rho_w\,\cosh^2((\rho - \rho^*)/\rho_w))$, which peaks at $\rho^*$ (with value $P_0/\rho_w$) and decays exponentially away from $\rho^*$.

**Sweep range:** $\rho_w \in \{0.05, 0.1, 0.2, 0.5, 1.0\}$ (five values).

**Effect.** At small $\rho_w$: the penalty is nearly a step function (strong restoring near $\rho^*$, saturated away from it). The equilibrium value $P_*' = P_0/\rho_w$ is large, producing a high penalty floor in the decay-rate funnel and a small stability threshold $\epsilon_0$. At large $\rho_w$: the penalty is nearly linear (approaching the default $P(\rho) \approx (P_0/\rho_w)(\rho - \rho^*)$ for $|\rho - \rho^*| \ll \rho_w$). The equilibrium $P_*' = P_0/\rho_w$ is small.

**Purpose.** The tanh penalty tests whether the qualitative features depend on the global shape of $P$ (its behavior far from $\rho^*$) or only on the local properties ($P_*'$, $P_*''$). The universality prediction is that the qualitative features depend only on $P_*'$ (the local slope) and $P_*''$ (which enters the normal-form coefficient, eq. C.76); the global shape affects the far-from-equilibrium dynamics (Stages I and II) but not the spectral structure or the exponential decay of Stage III.

##### 4.3.2.3 Asymmetric Penalty

$$
P_{\mathrm{asym}}(\rho) = \begin{cases} P_0^-\,(\rho - \rho^*) & \text{if } \rho < \rho^*, \\ P_0^+\,(\rho - \rho^*) & \text{if } \rho \geq \rho^*, \end{cases}
$$

where $P_0^- > 0$ and $P_0^+ > 0$ may differ. This piecewise-linear penalty is monotone ($P' > 0$ everywhere) with a kink at $\rho^*$ where the slope changes from $P_0^-$ to $P_0^+$.

**Sweep range:** $(P_0^-, P_0^+) \in \{(1,1), (0.5, 1.5), (0.2, 1.8), (1.5, 0.5), (1.8, 0.2)\}$ (five values, including the symmetric default).

**Purpose.** The asymmetric penalty tests whether the architecture depends on the symmetry of the restoring force about $\rho^*$. Physical systems generically have asymmetric penalties (the energy cost of compression differs from the cost of rarefaction). The universality prediction is that the qualitative features persist for any monotone $P$ regardless of symmetry. The asymmetry introduces a nonzero $P_*''$ (computed as the distributional derivative at the kink), which enters the bifurcation normal form (Theorem C.58, eq. C.76) and may shift the locked amplitude ratios.

**Regularity note.** The kink at $\rho^*$ makes $P_{\mathrm{asym}}$ only $C^0$, not $C^\infty$. As with the piecewise-smooth mobility (§4.3.1.3), the reduced regularity may affect convergence near $\rho^*$. The convergence study must verify that the results are converged.

---

#### 4.3.3 Universality Checks

The constitutive sweeps produce a dataset in which the constitutive form varies while the canonical parameters ($D$, $\zeta$, $\tau$, $\rho^*$, $\rho_{\max}$) are held fixed. The universality claim (Appendix D, Theorem D.19) predicts which observables are invariant across the sweep and which vary. The checks are organized into three tiers.

##### 4.3.3.1 Tier 1: Qualitative Invariants (Must Be Identical)

These features are predicted to be present for *every* constitutive choice satisfying Principles 1–7:

| Feature | Check | Pass criterion |
|---------|-------|---------------|
| Unique equilibrium | $\rho(t) \to \rho^*$ as $t \to \infty$ | $\|\rho(T) - \rho^*\|_{L^2} < 10^{-3}$ at $T = 50$ |
| Strict positivity | $\rho(x, t) > 0$ for all $(x, t)$ | `positivity_converged = true` |
| Sub-capacity | $\rho(x, t) < \rho_{\max}$ for all $(x, t)$ | $\delta_{\min} > 0$ |
| Energy monotonicity | $\mathcal{E}(t)$ non-increasing | No E05 warnings |
| Regime geometry | Spiral Sheet and Monotonic Cone exist | Both oscillatory and monotonic classifications found across $(D, \zeta)$-plane |
| Modal hierarchy | $D\alpha_1 < D\alpha_2 < \cdots$ | Measured rates strictly ordered |
| Triad selection rule | $k \in \{|m-n|, m+n\}$ only | Selection-rule compliance matrix (Fig. 4.3 analogue) fully compliant |
| Three-stage convergence | Global → algebraic → exponential | $\hat{\beta}(t)$ transitions from low to $\gamma_*$ plateau |

If any Tier 1 check fails for a constitutive choice that satisfies Principles 1–7, the universality claim is falsified for that feature. If a Tier 1 check fails for a constitutive choice that violates a principle (e.g., $P'(\rho^*) = 0$ for the super-linear penalty), the failure is expected and confirms the principle's necessity.

##### 4.3.3.2 Tier 2: Quantitative Scaling Laws (Must Have Correct Functional Form)

These features are predicted to hold with the same functional form but possibly different numerical coefficients:

| Feature | Predicted form | Coefficient dependence | Check |
|---------|---------------|----------------------|-------|
| Decoherence scaling | $\Gamma \propto C_{\mathrm{ED}}$ | Proportionality constant $\propto D P_*'/M_*$ | Slope $= 1$ on log-log $\Gamma$ vs. $C_{\mathrm{ED}}$ |
| Half-life scaling | $t_{1/2} \propto 1/C_{\mathrm{ED}}$ | Coefficient $\propto M_*/(DP_*')$ | Slope $= -1$ on log-log |
| Locked ratio locking | $\bar{R}_{31}/\epsilon = \text{const}$ in $\epsilon$ | Constant $= |M_*'|\Gamma_{12,3}/(D\Delta\alpha)$ | Flat line on normalized ratio vs. $\epsilon$ |
| Barrier scaling | $\mathcal{E}_0 \propto \delta^{-(\beta-1)}$ | Exponent $= \beta - 1$ | Slope $= -(\beta-1)$ on log-log $\mathcal{E}$ vs. $\delta$ |
| Transition time | $t_* \sim \ln(C_{\mathrm{ED}}/\epsilon_0^2)/\gamma_*$ | $\gamma_*$ and $\epsilon_0$ depend on constitutive params | Logarithmic growth on semilog-$x$ |

At each constitutive sweep point, the scaling law is tested by running the corresponding complexity sweep (§4.2) and fitting the data to the predicted form. The *slope* (on the appropriate log-log or semilog axes) must match the predicted value to within $10\%$. The *intercept* (the numerical coefficient) is expected to vary with the constitutive parameters.

##### 4.3.3.3 Tier 3: Constitutive-Dependent Quantities (Expected to Vary)

These quantities are predicted to depend on the constitutive functions and should change systematically across the sweep:

| Quantity | Dependence | Direction across $\beta$-sweep |
|----------|-----------|-------------------------------|
| Equilibrium mobility $M_*$ | $M_0(0.5)^\beta$ | Decreases with $\beta$ |
| Modal decay rates $D\alpha_n$ | $D(M_*\mu_n + P_*')$ | Decrease with $\beta$ (through $M_*$) |
| Spectral gap $\gamma$ | $\min(\gamma_{\mathrm{hom}}, D\alpha_1)$ | Decreases with $\beta$ |
| Locked ratio coefficient | $|M_*'|/(D\,M_*\,\Delta\mu)$ | Non-monotone in $\beta$ |
| Stability threshold $\epsilon_0$ | $\gamma_*/C_{\mathrm{nl}}$ | Depends on curvature of $M$, $P$ near $\rho^*$ |
| Energy barrier margin $\delta(\mathcal{E}_0)$ | $\propto \mathcal{E}_0^{-1/(\beta-1)}$ | Tighter for larger $\beta$ at fixed $\mathcal{E}_0$ |

These quantities are measured at each sweep point and plotted against the constitutive parameter ($\beta$, $\kappa$, $\delta_M$, $q$, $\rho_w$, or $(P_0^-, P_0^+)$). The plots confirm that the quantities vary as predicted by the analytic formulas (which express them in terms of $M_*$, $M_*'$, $P_*'$, etc.) and that the variation is smooth and monotone where predicted.

---

#### 4.3.4 Sweep Execution

Each constitutive sweep point requires a full set of experiments to evaluate the three tiers:

| Experiment | Purpose | Integrations per constitutive point |
|-----------|---------|--------------------------------------|
| Single-mode decay (§3.1 analogue) | Measure $D\alpha_n$ for $n = 1, \ldots, 4$ | $4$ |
| Two-mode triad (§4.1 analogue) | Verify selection rule | $1$ |
| Locked ratio (§4.2 analogue) | Measure $\bar{R}_{31}$ at $3$ amplitudes | $3$ |
| Complexity ladder (§9.1 analogue) | Verify $\Gamma \propto C_{\mathrm{ED}}$ | $4$–$8$ |
| Three-stage convergence (§7.2 analogue) | Measure $t_*$ and $\gamma_*$ | $1$ |
| Barrier test (§6.2 analogue) | Measure $\delta(\mathcal{E}_0)$ at $3$ margins | $3$ |
| **Total per constitutive point** | | **$16$–$20$** |

For the $\beta$-sweep (seven values): $7 \times 18 \approx 126$ integrations. For the full constitutive survey (all six families, $\sim 33$ points): $33 \times 18 \approx 594$ integrations.

**Estimated wall time.** At $\sim 50$ seconds per integration (the Atlas average): $\sim 8$ hours on a single core for the full survey, or $\sim 30$ minutes on a $16$-core workstation. The constitutive survey is comparable in scale to the $(D, \zeta, \tau)$-parameter sweep of §4.1 and is well within the computational budget.

---

#### 4.3.5 Universality Verification Summary

The constitutive sweeps produce a table with the following structure:

| Constitutive family | Parameter | Tier 1 (qualitative) | Tier 2 (scaling laws) | Tier 3 (quantities) |
|--------------------|-----------|----------------------|----------------------|---------------------|
| Power-law, $\beta = 0.5$ | $\beta$ | All pass | All slopes correct | $M_*, D\alpha_n, \gamma$ vary as predicted |
| Power-law, $\beta = 1.0$ | $\beta$ | All pass | All slopes correct | ... |
| ... | ... | ... | ... | ... |
| Power-law penalty, $q = 2.0$ | $q$ | **Fails**: unique equilibrium not reached | N/A | $P_*' = 0$ at equilibrium |
| Power-law penalty, $q = 3.0$ | $q$ | **Fails**: unique equilibrium not reached | N/A | $P_*' = 0$ at equilibrium |
| Asymmetric, $(0.2, 1.8)$ | $(P_0^-, P_0^+)$ | All pass | All slopes correct | Asymmetric $P_*''$ shifts locked ratio |

The expected outcome is:

- **All Tier 1 checks pass** for every constitutive choice satisfying Principles 1–7 (i.e., all families except the super-linear penalty with $q > 1$).
- **All Tier 2 scaling laws hold** with the predicted slopes, confirming the functional form of the universality predictions.
- **Tier 3 quantities vary smoothly** with the constitutive parameter, matching the analytic dependence on $M_*$, $M_*'$, $P_*'$.
- **The super-linear penalty ($q > 1$) fails Tier 1**, confirming that $P'(\rho^*) > 0$ (Principle 3) is a *necessary* condition for the architectural ontology, not merely a convenient assumption.

This outcome would constitute the numerical verification of the universality class $\mathcal{U}_{\mathrm{ED}}$: the qualitative structure is invariant under constitutive perturbation (Theorem D.19), the quantitative dependence is captured by the equilibrium constitutive values (Theorems D.7–D.13), and the principles are individually necessary (each failure traces to a specific violated principle).

---

### 4.4 Sweeping Domain Size

The canonical ED system is posed on a bounded domain $\Omega = [0, L]^d$ with Neumann boundary conditions. The domain length $L$ enters the dynamics exclusively through the eigenvalues $\mu_n = (n\pi/L)^2$ of the Neumann Laplacian. Appendix D (Theorem D.7, Closure under domain changes) proves that the ED architecture is preserved under changes of $L$: the universality class $\mathcal{U}_{\mathrm{ED}}$ is closed under domain rescaling with Neumann boundary conditions. This subsection specifies the domain-size sweep that verifies this closure numerically and maps the quantitative dependence of the key observables on $L$.

---

#### 4.4.1 Scaling Invariance

##### 4.4.1.1 The Rescaling Transformation

Consider the canonical ED system on $\Omega = [0, L]$ and introduce the rescaled coordinate $\xi = x/L$, so $\xi \in [0, 1]$. The density in the rescaled coordinate is $\tilde{\rho}(\xi, t) = \rho(L\xi, t)$, and the spatial derivatives transform as $\partial_x = L^{-1}\partial_\xi$, $\nabla^2_x = L^{-2}\nabla^2_\xi$. The density equation becomes

$$
\partial_t\tilde{\rho} = D\bigl[M(\tilde{\rho})\,L^{-2}\nabla_\xi^2\tilde{\rho} + M'(\tilde{\rho})\,L^{-2}|\nabla_\xi\tilde{\rho}|^2 - P(\tilde{\rho})\bigr] + H\,v.
$$

This is the canonical system on the unit domain $[0, 1]$ with a modified effective mobility $\tilde{M}(\rho) = L^{-2}M(\rho)$. Equivalently, the rescaled system has the same constitutive functions but an effective diffusion coefficient $D_{\mathrm{eff}} = D/L^2$.

The rescaling does not change the penalty, the participation equation, or any of the canonical parameters except through the eigenvalue scaling. The architectural content — the seven principles, the regime geometry, the triad selection rule — is invariant under the rescaling. Only the *quantitative* time scales change: all diffusion-related rates are multiplied by $L^{-2}$.

##### 4.4.1.2 Eigenvalue Scaling

The Neumann eigenvalues on $\Omega = [0, L]$ are

$$
\mu_n(L) = \left(\frac{n\pi}{L}\right)^2 = \frac{\mu_n(1)}{L^2},
$$

where $\mu_n(1) = n^2\pi^2$ are the eigenvalues on the unit domain. All eigenvalue-dependent quantities scale accordingly:

| Quantity | Dependence on $L$ | Scaling |
|----------|--------------------|---------|
| Neumann eigenvalue $\mu_n$ | $n^2\pi^2/L^2$ | $\propto L^{-2}$ |
| Modal decay coefficient $\alpha_n$ | $M_*\mu_n + P_*' = M_*n^2\pi^2/L^2 + P_*'$ | Diffusive part $\propto L^{-2}$; penalty part constant |
| Spatial decay rate $D\alpha_n$ | $D(M_*n^2\pi^2/L^2 + P_*')$ | Approaches $DP_*'$ as $L \to \infty$ |
| Spectral gap $\gamma_{\mathrm{sp}} = D\alpha_1$ | $D(M_*\pi^2/L^2 + P_*')$ | Decreases toward $DP_*'$ as $L \to \infty$ |
| Homogeneous decay rate $\gamma_0$ | $\frac{1}{2}(DP_*' + \zeta/\tau)$ | Independent of $L$ |
| Oscillation frequency $\omega$ | $\frac{1}{2}\sqrt{|\mathscr{D}_0|}$ | Independent of $L$ |
| Discriminant $\mathscr{D}_0$ | $(DP_*' - \zeta/\tau)^2 - 4HP_*'/\tau$ | Independent of $L$ |
| Poincaré constant $C_\Omega$ | $L^2/\pi^2$ | $\propto L^2$ |
| ED-complexity $C_{\mathrm{ED}}$ (for mode $n$) | $A^2\mu_n/2 = A^2n^2\pi^2/(2L^2)$ ... on $[0,L]$: $A^2n^2\pi^2/(2L)$ | Depends on $L$ through both $\mu_n$ and the domain measure |

The critical observation is the *separation of scales*: the homogeneous-mode dynamics ($\gamma_0$, $\omega$, $\mathscr{D}_0$) are completely independent of $L$, while the spatial-mode dynamics ($D\alpha_n$ for $n \geq 1$) depend on $L$ through $\mu_n \propto L^{-2}$.

##### 4.4.1.3 Two Limiting Regimes

**Small domain ($L \to 0$).** The eigenvalues $\mu_n \to \infty$, making the spatial modes decay infinitely fast ($D\alpha_n \to \infty$). The spatial structure is extinguished instantaneously, and the dynamics reduce to the homogeneous-mode ODE $(a_0, v)$ governed by $\mathbf{A}_0$. The system is effectively zero-dimensional. The spectral gap $\gamma_{\mathrm{sp}} = D\alpha_1 \to \infty$, so the gap is always controlled by the homogeneous mode: $\gamma = \gamma_{\mathrm{hom}}$.

**Large domain ($L \to \infty$).** The eigenvalues $\mu_n \to 0$, and the spatial modes decay at rates approaching the penalty floor $D\alpha_n \to DP_*'$. The spectral gap $\gamma_{\mathrm{sp}} = D\alpha_1 \to DP_*'$, which may be smaller or larger than $\gamma_{\mathrm{hom}}$ depending on the parameters. The modal hierarchy becomes *compressed*: the decay rates $D\alpha_1, D\alpha_2, \ldots$ cluster near $DP_*'$, reducing the spectral separation between adjacent modes. In this limit, the three-stage convergence is dominated by the penalty (which is $L$-independent) rather than by diffusion.

The domain-size sweep maps the transition between these two regimes.

---

#### 4.4.2 Sweep Specification

##### 4.4.2.1 Sweep Range

$$
L \in \{0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0\}
$$

(seven values spanning two orders of magnitude). The default $L = 1.0$ is the reference point.

##### 4.4.2.2 Fixed Parameters

All canonical parameters are held at their Set II values ($D = 0.6$, $\zeta = 0.5$, $\tau = 1.0$, $\rho^* = 0.5$, $\rho_{\max} = 1.0$, $M_0 = 1.0$, $\beta = 2.0$, $P_0 = 1.0$). Only $L$ varies.

##### 4.4.2.3 Resolution Scaling

The spatial resolution must scale with $L$ to maintain a fixed number of grid points per unit length (constant physical resolution) or a fixed number of wavelengths resolved (constant spectral resolution). The two choices produce different grid sizes:

**Option A: Fixed grid-point density.** Set $N = \lceil N_{\mathrm{ref}} \cdot L/L_{\mathrm{ref}}\rceil$, where $N_{\mathrm{ref}} = 512$ at $L_{\mathrm{ref}} = 1.0$. This gives:

| $L$ | $N$ | $h = L/(N+1)$ |
|-----|-----|-----|
| $0.1$ | $51$ | $1.92 \times 10^{-3}$ |
| $0.2$ | $102$ | $1.94 \times 10^{-3}$ |
| $0.5$ | $256$ | $1.95 \times 10^{-3}$ |
| $1.0$ | $512$ | $1.95 \times 10^{-3}$ |
| $2.0$ | $1024$ | $1.95 \times 10^{-3}$ |
| $5.0$ | $2560$ | $1.95 \times 10^{-3}$ |
| $10.0$ | $5120$ | $1.95 \times 10^{-3}$ |

The grid spacing $h$ is approximately constant ($\approx 1.95 \times 10^{-3}$) across all $L$, so the spatial truncation error is uniform. The computational cost grows linearly with $L$ (more grid points for larger domains).

**Option B: Fixed mode count (spectral method).** Set $N_{\mathrm{modes}} = 128$ for all $L$. The eigenvalues $\mu_k = (k\pi/L)^2$ automatically adjust; higher $L$ resolves lower spatial frequencies. The physical-space grid has $N_{\mathrm{phys}} = 192$ points regardless of $L$.

The Suite uses Option A for Method A experiments and Option B for Method B experiments. The convergence study (§2.7) is run at $L = 1.0$ (the reference) and at $L = 0.1$ and $L = 10.0$ (the extremes) to verify that the spatial accuracy is uniform across the sweep.

##### 4.4.2.4 Initial Condition Scaling

The initial condition must be scaled with $L$ to produce a physically comparable perturbation at each domain size. Two choices are natural:

**Fixed spatial profile.** The perturbation occupies a fixed fraction of the domain:

$$
\rho_0(x) = \rho^* + A\cos(\pi x/L), \qquad v_0 = 0.
$$

This is IC-A with $n = 1$, which automatically scales with $L$ (one full cosine arch across the domain at every $L$). The initial complexity is

$$
C_{\mathrm{ED}}(0) = \frac{A^2\pi^2}{2L},
$$

which decreases with $L$ (larger domains with the same amplitude profile have lower gradient content per unit length, because the arch is wider and the slope is gentler).

**Fixed initial complexity.** Choose $A(L)$ so that $C_{\mathrm{ED}}(0)$ is the same at every $L$:

$$
A(L) = A_{\mathrm{ref}}\sqrt{L/L_{\mathrm{ref}}}.
$$

This keeps $C_{\mathrm{ED}}(0) = A_{\mathrm{ref}}^2\pi^2/(2L_{\mathrm{ref}})$ constant across the sweep. The amplitude increases with $L$, but the gradient $|\nabla\rho|_{\max} = A(L)\pi/L = A_{\mathrm{ref}}\pi/\sqrt{L\cdot L_{\mathrm{ref}}}$ decreases with $L$.

The Suite runs both variants: the fixed-profile sweep (to observe the $L$-dependence of $C_{\mathrm{ED}}$ at fixed profile) and the fixed-complexity sweep (to isolate the effect of $L$ on the dynamics at fixed gradient content). Default: $A_{\mathrm{ref}} = 0.05$ at $L_{\mathrm{ref}} = 1.0$.

##### 4.4.2.5 Time-Step Scaling

The CFL constraint scales as $\Delta t \propto h^2$, which is constant across the sweep for Option A (fixed $h$). The default $\Delta t = 5 \times 10^{-4}$ is used at all $L$ values.

For the ETD scheme (Option B), $\Delta t = 10^{-4}$ is used at all $L$ (the ETD scheme is unconditionally stable in the linear part, and the nonlinear CFL is $L$-independent for the fixed-complexity IC).

---

#### 4.4.3 Expected Effects

The domain-size sweep reveals how $L$ modulates the balance between diffusion and penalty in the ED dynamics. The effects are organized by the scaling regimes identified in §4.4.1.3.

##### 4.4.3.1 Effects on the Modal Hierarchy

**Decay rates.** The spatial decay rate of mode $n$ is $D\alpha_n(L) = D(M_*n^2\pi^2/L^2 + P_*')$. At $L = 0.1$: $D\alpha_1 = 0.6(0.25 \cdot 100\pi^2 + 1.0) \approx 148.8$ (very fast). At $L = 10.0$: $D\alpha_1 = 0.6(0.25 \cdot 0.01\pi^2 + 1.0) \approx 0.615$ (barely above the penalty floor $DP_*' = 0.6$).

**Spectral gap.** At $L = 0.1$: $\gamma_{\mathrm{sp}} = D\alpha_1 \approx 148.8 \gg \gamma_{\mathrm{hom}} = 0.55$, so $\gamma = \gamma_{\mathrm{hom}} = 0.55$. The gap is controlled by the homogeneous mode. At $L = 10.0$: $\gamma_{\mathrm{sp}} = D\alpha_1 \approx 0.615$, which is close to $\gamma_{\mathrm{hom}} = 0.55$. The gap $\gamma \approx 0.55$, but $D\alpha_1$ is only $12\%$ above it — the separation between spatial and homogeneous modes is thin.

**Modal compression.** The ratio $D\alpha_2/D\alpha_1 = (4M_*\pi^2/L^2 + P_*')/(M_*\pi^2/L^2 + P_*')$ depends on $L$. At $L = 1.0$: the ratio is $(4 \cdot 2.467 + 1)/(2.467 + 1) = 10.87/3.47 \approx 3.13$. At $L = 10.0$: the ratio is $(4 \cdot 0.0247 + 1)/(0.0247 + 1) = 1.099/1.025 \approx 1.07$. The hierarchy compresses: on large domains, adjacent modes have nearly identical decay rates, and the spectral gap between consecutive modes vanishes.

**Verification.** Measure $\hat{\sigma}_n$ for modes $n = 1, 2, 3$ at each $L$ by single-mode initialization (§3.1 analogue). Plot $D\alpha_n(L)$ versus $L$ on a log-log axis; the diffusive contribution should follow $L^{-2}$, with the penalty floor $DP_*'$ as a horizontal asymptote.

##### 4.4.3.2 Effects on the Regime Geometry

The regime classification is $L$-independent: $\mathscr{D}_0$ does not depend on $L$ (§4.4.1.2, table). The system is oscillatory or monotonic regardless of the domain size. The oscillation frequency $\omega$, the homogeneous decay rate $\gamma_0$, and the damping parameter $\Delta$ are all $L$-invariant.

**Verification.** Confirm that the measured $\hat{\omega}$ and the zero-crossing count $N_{\mathrm{cross}}$ are identical across all seven $L$ values (to within discretization tolerance). Any $L$-dependence in the regime classification would indicate a failure of the analytical prediction and would require investigation.

##### 4.4.3.3 Effects on the Three-Stage Convergence

**Stage I (global bounds).** The energy bound and the pointwise confinement are $L$-independent (they depend on $\mathcal{E}_0$ and the constitutive functions, not on $L$). The density potential $\Phi(\rho)$ is $L$-independent; the total energy $\mathcal{E} = \int_\Omega\Phi(\rho)\,dx + \frac{\tau H}{2}v^2$ scales with $|\Omega| = L^d$.

**Stage II (algebraic convergence).** The Barbalat decay of gradients $\|\nabla\rho\|_{L^2} \to 0$ proceeds at a rate that depends on $L$ through the dissipation integrand $P'/M \cdot |\nabla\rho|^2$. On large domains, the diffusive contribution to the dissipation is weakened ($M_*\mu_1 \ll P_*'$), and the gradient decay is driven primarily by the penalty. The algebraic phase may therefore be longer on large domains.

**Stage III (exponential convergence).** The exponential rate $\gamma_*$ (eq. C.48) depends on $L$ through $D\alpha_1 = D(M_*\pi^2/L^2 + P_*')$, which enters the spectral gap. On small domains, $\gamma_*$ is dominated by $\gamma_{\mathrm{hom}}$ (which is $L$-independent), so the exponential rate is $L$-independent. On large domains, $\gamma_*$ may be limited by the shrinking spectral gap $D\alpha_1 \to DP_*'$.

**Transition time $t_*$.** For the fixed-profile IC, the initial complexity $C_{\mathrm{ED}}(0) \propto L^{-1}$ decreases with $L$, so $t_*$ should decrease with $L$ (lower complexity enters the exponential basin faster). For the fixed-complexity IC, $C_{\mathrm{ED}}(0)$ is constant, and $t_*$ should increase with $L$ (the weaker diffusion on larger domains slows the complexity decay).

**Verification.** Measure $t_*$ at each $L$ for both IC variants. Plot $t_*(L)$ and compare to the predicted scalings.

##### 4.4.3.4 Effects on the Triad Coupling

The trilinear coupling coefficients $\Gamma_{mnk}$ (eq. C.26) are computed from the Neumann eigenfunctions, which scale with $L$. On $[0, L]$:

$$
\Gamma_{mnk}(L) = \int_0^L\nabla\varphi_m \cdot \nabla\varphi_n\;\varphi_k\,dx = \frac{mn\pi^2}{L^2}\cdot\frac{c_m c_n}{c_k}\cdot\frac{L}{2} = \frac{mn\pi^2}{2L}\cdot\frac{c_m c_n}{c_k},
$$

where $c_0 = 1/\sqrt{L}$ and $c_k = \sqrt{2/L}$ for $k \geq 1$. The coupling coefficients scale as $L^{-1}$ (for $k \geq 1$). The locked amplitude ratio (eq. C.40):

$$
\frac{|a_3|}{|a_1|} \sim \frac{|M_*'|\,|\Gamma_{12,3}|}{D(\alpha_3 - \alpha_1)}\,\epsilon = \frac{|M_*'|\,mn\pi^2/(2L) \cdot c_m c_n/c_k}{D\,M_*\,(9 - 1)\pi^2/L^2}\,\epsilon.
$$

After simplification (the $L$-dependent factors in numerator and denominator), the locked ratio is proportional to $L$:

$$
\frac{|a_3|}{|a_1|} \propto \frac{L}{D\,M_*} \cdot \epsilon.
$$

On larger domains, the locked ratio is *larger* (the triad coupling is stronger relative to the decay-rate difference, because the decay rates compress while the coupling coefficients decrease more slowly). This is the domain-size analogue of the $1/D$ dependence observed in Atlas §4.2.4: both reflect the balance between the generation rate and the differential decay.

**Verification.** Measure $\bar{R}_{31}$ at each $L$ by the locking test (§4.2 analogue). Plot $\bar{R}_{31}$ versus $L$; the predicted linear scaling should be confirmed.

##### 4.4.3.5 Effects on the Stability Threshold

The stability threshold $\epsilon_0$ (Theorem C.43) depends on $L$ through $\gamma_*$ and $C_{\mathrm{nl}}$. The Lyapunov rate $\gamma_*$ (eq. C.48) involves $D\alpha_1 \propto L^{-2}$, so on large domains ($L \gg 1$), $\gamma_*$ decreases and the stability basin shrinks: $\epsilon_0 \propto \gamma_* \propto L^{-2}$ in the regime where $D\alpha_1$ controls the gap. On small domains ($L \ll 1$), $\gamma_*$ is controlled by $\gamma_{\mathrm{hom}}$ (which is $L$-independent), and the stability basin is approximately $L$-independent.

**Verification.** Measure $\epsilon_0$ at each $L$ by the complexity-threshold experiment (§5.2 analogue). Plot $\epsilon_0(L)$; the predicted flattening at small $L$ and $L^{-2}$ decay at large $L$ should be confirmed.

---

#### 4.4.4 Output and Post-Processing

The domain-size sweep produces a one-dimensional array indexed by $L$:

| Array | Shape | Contents |
|-------|-------|----------|
| `L_values` | $(7,)$ | Domain lengths |
| `mu_1` | $(7,)$ | First eigenvalue $\pi^2/L^2$ |
| `D_alpha_1` | $(7,)$ | First spatial decay rate (analytic) |
| `sigma_hat_1` | $(7,)$ | Measured first-mode decay rate |
| `omega_hat` | $(7,)$ | Measured oscillation frequency |
| `N_cross` | $(7,)$ | Zero-crossing count |
| `t_star_fixed_profile` | $(7,)$ | Transition time (fixed profile IC) |
| `t_star_fixed_C_ED` | $(7,)$ | Transition time (fixed complexity IC) |
| `R31_hat` | $(7,)$ | Measured locked amplitude ratio |
| `epsilon_0_hat` | $(7,)$ | Measured stability threshold |
| `gamma_hat` | $(7,)$ | Measured late-time exponential rate |

**Key plots:**

| Plot | Axes | Expected feature |
|------|------|-----------------|
| $D\alpha_1$ vs. $L$ | Log-log | Slope $-2$ for $L < 1$, flattening to $DP_*'$ for $L > 1$ |
| $\hat{\omega}$ vs. $L$ | Linear-linear | Horizontal line (frequency $L$-independent) |
| $\bar{R}_{31}$ vs. $L$ | Log-log | Slope $+1$ (locked ratio $\propto L$) |
| $t_*$ (fixed profile) vs. $L$ | Semilog-$x$ | Decreasing (lower $C_{\mathrm{ED}}$ at larger $L$) |
| $t_*$ (fixed complexity) vs. $L$ | Semilog-$x$ | Increasing (weaker diffusion at larger $L$) |
| $\epsilon_0$ vs. $L$ | Log-log | Flat for $L < 1$; slope $-2$ for $L > 1$ |

Each plot tests a specific prediction of the rescaling invariance (§4.4.1) and the universality closure (Theorem D.7). Agreement confirms that the architecture is preserved under domain changes; disagreement at any sweep point identifies a failure of the scaling prediction that requires investigation.

---

#### 4.4.5 Sweep Execution

| Component | Integrations per $L$ | Total (7 values of $L$) |
|-----------|---------------------|------------------------|
| Single-mode decay ($n = 1, 2, 3$) | $3$ | $21$ |
| Homogeneous-mode dynamics | $1$ | $7$ |
| Locked ratio (3 amplitudes) | $3$ | $21$ |
| Transition time (fixed profile) | $1$ | $7$ |
| Transition time (fixed complexity) | $1$ | $7$ |
| Stability threshold (3 amplitudes) | $3$ | $21$ |
| **Total** | **$12$** | **$84$** |

Estimated wall time: $\sim 7$ minutes on a single core (most experiments are fast; the $L = 10$ runs at $N = 5120$ are the most expensive at $\sim 30$ seconds each). The domain-size sweep is modest in scale and completes well within the computational budget.

---

### 4.5 Parallelization Strategy

The Numerical Atlas requires approximately $1{,}800$ integrations in total: $450$ for the standard experiments (Atlas §10.2.5), $689$ for the parameter sweeps (§4.1.5), $84$ for the domain-size sweep (§4.4.5), and $594$ for the optional constitutive survey (§4.3.4). On a single core, the complete program takes approximately $4$ hours. This subsection specifies how to distribute these integrations across multiple cores to reduce the wall-clock time, without introducing any inter-process dependency or communication overhead.

---

#### 4.5.1 Embarrassingly Parallel Structure

Every integration in the Atlas is independent of every other integration. No experiment reads the output of a previous experiment as input; no sweep point depends on the results of an adjacent sweep point; no convergence study at one resolution requires the solution at another resolution to be available simultaneously. This independence is a consequence of the experiment design: each experiment is fully specified by its parameter record and initial condition (§3.1), and the only shared resource is the output directory (which is written, not read, during execution).

The parallelization is therefore **embarrassingly parallel** — the technical term for a workload that decomposes into fully independent tasks with no communication, synchronization, or data sharing between them. This is the simplest and most efficient form of parallelism: every core runs a complete, self-contained integration from initialization to termination, writes its output to a unique directory, and requires nothing from any other core.

The embarrassingly parallel structure holds at every level of the Atlas:

| Level | Tasks | Independence |
|-------|-------|-------------|
| Individual experiments | 55 numbered experiments | Each has its own parameter set, IC, and output directory |
| Sweep points | $81$–$475$ per sweep | Each point has its own $(D_i, \zeta_j)$ and output sub-directory |
| Convergence refinement levels | $3$–$4$ per study | Each level has its own $N$ or $\Delta t$; no level reads another's output |
| Sub-experiments | $4$–$8$ per experiment | E.g., modes $n = 1, 2, 3, 4$ in Experiment 3.1 |
| IC variants | $2$ per sweep point (small/large amplitude) | Independent ICs at the same parameter point |

The total task count — the number of independently executable integrations — is approximately $1{,}800$. Each task takes $10$–$60$ seconds on a single core (with a median of $\sim 8$ seconds for the standard experiments and $\sim 50$ seconds for the long-time integrations).

---

#### 4.5.2 Multiprocessing on a Single Workstation

The simplest parallel execution model distributes the tasks across the cores of a single multi-core workstation using the operating system's process-level parallelism.

##### 4.5.2.1 Task Queue Model

The sweep orchestrator (§2.5.5) maintains a **task queue** — an ordered list of all integrations to be performed. Each task is described by its experiment specification (parameter record, IC, resolution, method, output path). The orchestrator assigns tasks to available worker processes:

1. **Initialize the queue.** Load all experiment specifications from the Atlas Master Table and the sweep definitions. Assign each specification a unique task ID.

2. **Spawn worker processes.** Create $P$ worker processes, where $P$ is the number of available cores (or a user-specified maximum). Each worker runs in its own operating-system process with its own memory space.

3. **Dispatch loop.** While the queue is non-empty:
   - Wait for any worker to become idle (i.e., its previous task has completed).
   - Dequeue the next task from the queue.
   - Send the task specification to the idle worker.
   - The worker runs the full integration (initialization → time loop → output) and writes its results to the designated output directory.
   - Upon completion, the worker signals the orchestrator and returns to the idle pool.

4. **Collect results.** After all tasks are complete, the orchestrator assembles the sweep-level outputs (grid-indexed arrays, §4.1.3) from the per-task output files.

##### 4.5.2.2 Environment-Specific Implementation

**Python.** Use the `multiprocessing` module (standard library) or `concurrent.futures.ProcessPoolExecutor`. Each worker is a separate Python process (bypassing the GIL). The task specification is passed as a serializable dictionary. The worker imports the simulation engine, runs `Atlas_Experiment(spec)`, and returns the path to the output file.

**Julia.** Use `Distributed` (standard library) with `pmap` or `@distributed for`. Each worker is a separate Julia process. The task specification is a named tuple. The `@everywhere` macro ensures the simulation engine is loaded on all workers.

**MATLAB.** Use the Parallel Computing Toolbox with `parfor`. Each iteration of the `parfor` loop is an independent integration. The task specification is passed as a struct. MATLAB's `parfor` automatically distributes iterations across the available worker pool.

##### 4.5.2.3 Memory and I/O Considerations

**Memory.** Each worker requires $\sim 50$ KB of working memory for a 1D integration at $N = 512$ (§1.2.9) plus $\sim 100$ MB for the environment overhead (Python interpreter, NumPy arrays, etc.). On a 16-core workstation with 32 GB RAM: $16 \times 100$ MB $= 1.6$ GB, leaving $> 30$ GB free. Memory is never a bottleneck.

**I/O.** Each worker writes $\sim 100$–$300$ KB of output per task (§2.4.6). At $16$ workers completing tasks every $\sim 8$ seconds: $\sim 16 \times 300$ KB$/8$ s $= 600$ KB/s, which is negligible compared to any modern storage system ($> 100$ MB/s for spinning disk, $> 1$ GB/s for SSD). I/O contention is not a concern, even with all workers writing simultaneously, because each worker writes to a unique directory (no file-level contention).

**No shared state.** The workers share no mutable state. The parameter records are read-only; the output files are write-only; the task queue is managed by the orchestrator (which serializes access). This eliminates all race conditions, deadlocks, and consistency issues that arise in shared-memory parallelism.

---

#### 4.5.3 Cluster Execution

For users with access to a computing cluster (SLURM, PBS, SGE, or similar batch schedulers), the embarrassingly parallel structure maps naturally onto the cluster's job-array facility.

##### 4.5.3.1 Job Array Model

Each integration is submitted as a separate job (or as an element of a job array) to the cluster scheduler. The scheduler assigns jobs to available nodes; no inter-job communication is needed.

**Task-to-job mapping.** The orchestrator generates a task list file:

```
task_list.txt:
1  exp_1.1  SetI  IC_A  A=0.05  N=64   dt=1e-2  T=5   FD_IE
2  exp_1.1  SetI  IC_A  A=0.05  N=128  dt=5e-3  T=5   FD_IE
3  exp_1.1  SetI  IC_A  A=0.05  N=256  dt=2.5e-3  T=5  FD_IE
...
1800  exp_9.5  SetII  Custom  ...
```

Each line specifies one task. The job array submission uses the line number as the array index:

- **SLURM:** `sbatch --array=1-1800 run_task.sh` where `run_task.sh` reads line `$SLURM_ARRAY_TASK_ID` from `task_list.txt` and executes the corresponding integration.
- **PBS:** `qsub -t 1-1800 run_task.pbs` with analogous logic.

##### 4.5.3.2 Resource Requirements Per Job

| Resource | Requirement | Notes |
|----------|------------|-------|
| Cores | $1$ | Single-threaded integration |
| Memory | $256$ MB | Generous upper bound; actual usage $\sim 100$ MB |
| Wall time | $5$ minutes | Generous; median task takes $\sim 10$ seconds |
| Storage | $1$ MB per job | Output files |
| Network | None | No inter-job communication |

The minimal resource footprint means that the jobs can be scheduled on any available node, including preemptible/spot instances, without concern for memory or network requirements.

##### 4.5.3.3 Output Collection

After all jobs complete, the output files are distributed across the cluster's shared filesystem (one sub-directory per task). The sweep orchestrator's post-processing step (§4.1.4) reads these files and assembles the grid-indexed arrays. This collection step runs on a single node and takes $< 1$ minute (it reads $\sim 80$ MB of output across $\sim 1{,}800$ files).

##### 4.5.3.4 Fault Tolerance

On a cluster, individual jobs may fail due to node failures, walltime expiration, or transient I/O errors. The sweep progress file (§2.5.5) tracks which tasks have completed successfully. After the initial array completes, the orchestrator identifies failed tasks and resubmits them:

1. Read the progress file.
2. Collect the list of task IDs with `completed = false`.
3. Generate a reduced task list with only the failed tasks.
4. Submit a new job array for the failed tasks.
5. Repeat until all tasks are complete or a maximum retry count ($3$) is reached.

Tasks that fail after $3$ retries are flagged as permanently failed and excluded from the sweep results (§2.6.5).

---

#### 4.5.4 Scaling Analysis

The wall-clock time for the full Atlas program as a function of the number of available cores $P$:

$$
T_{\mathrm{wall}}(P) = \frac{T_{\mathrm{total}}}{P} + T_{\mathrm{overhead}},
$$

where $T_{\mathrm{total}} \approx 4$ hours is the total single-core computation time and $T_{\mathrm{overhead}}$ is the fixed overhead (orchestration, output collection, post-processing). The overhead is small: $T_{\mathrm{overhead}} \approx 2$ minutes for the orchestrator startup, task distribution, and sweep assembly.

| Cores $P$ | $T_{\mathrm{wall}}$ | Efficiency $T_{\mathrm{total}}/(P \cdot T_{\mathrm{wall}})$ |
|-----------|--------|-----------|
| $1$ | $\sim 4$ hours | $100\%$ |
| $4$ | $\sim 62$ min | $97\%$ |
| $16$ | $\sim 17$ min | $94\%$ |
| $64$ | $\sim 6$ min | $83\%$ |
| $256$ | $\sim 3$ min | $52\%$ |
| $1{,}800$ | $\sim 2.5$ min | $5\%$ |

The efficiency decreases at large $P$ because the tasks are not uniform in duration: the longest task ($\sim 60$ seconds for a long-time integration at high resolution) determines the minimum wall time regardless of $P$. At $P = 1{,}800$ (one core per task), the wall time is dominated by the single longest task ($\sim 60$ seconds) plus the overhead ($\sim 2$ minutes), giving $T_{\mathrm{wall}} \approx 2.5$ minutes — a speedup of $\sim 96\times$ over single-core, but with only $5\%$ efficiency (most cores are idle after finishing their short tasks).

The practical sweet spot is $P = 16$–$64$ cores, where the efficiency is $> 80\%$ and the wall time is $< 20$ minutes. This is achievable on a single workstation (16 cores) or a modest cluster allocation (64 cores).

---

#### 4.5.5 Load Balancing

The tasks in the Atlas are not uniform in duration. The distribution of per-task wall times is approximately:

| Duration range | Fraction of tasks | Examples |
|---------------|-------------------|---------|
| $< 5$ seconds | $\sim 40\%$ | Short-time experiments, small $N$, convergence sub-runs |
| $5$–$20$ seconds | $\sim 35\%$ | Standard experiments at default resolution |
| $20$–$60$ seconds | $\sim 20\%$ | Long-time integrations ($T = 50$–$60$), large $N$ ($> 1024$) |
| $> 60$ seconds | $\sim 5\%$ | 2D experiments, $L = 10$ domain-size sweep |

Naive static scheduling (assigning task $i$ to core $i \mod P$) would produce load imbalance: some cores would receive mostly short tasks and finish early, while others would receive the long tasks and delay completion.

**Dynamic scheduling.** The task-queue model (§4.5.2.1) provides natural load balancing: each core receives its next task only when it finishes its current one. Short tasks are dispatched quickly; long tasks are dispatched to whichever core is available. The queue ordering does not affect the total wall time (all tasks must complete regardless), but sorting the queue by *decreasing estimated duration* (longest tasks first) minimizes the idle time at the end of the sweep: the long tasks are dispatched first and occupy cores throughout the execution, while the short tasks fill the gaps near the end.

**Estimated duration.** The task duration can be estimated from the experiment specification without running the integration:

$$
\hat{T}_{\mathrm{task}} \approx \frac{T_{\mathrm{final}}}{\Delta t} \cdot c_{\mathrm{step}}(N, d, \text{method}),
$$

where $c_{\mathrm{step}}$ is the per-step cost from §2.3.5 ($\sim 4\,\mu$s for 1D Method A at $N = 512$, $\sim 12\,\mu$s for 1D Method B at $N = 128$). The orchestrator computes $\hat{T}_{\mathrm{task}}$ for each task during queue construction and sorts the queue in decreasing order.

---

#### 4.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Parallelism type** | Embarrassingly parallel (no communication, no shared state) |
| **Task granularity** | One integration per task ($\sim 1{,}800$ tasks total) |
| **Task duration** | $2$–$60$ seconds (median $\sim 8$ seconds) |
| **Workstation execution** | `multiprocessing` / `pmap` / `parfor`; task-queue dispatch |
| **Cluster execution** | Job array; $1$ core, $256$ MB, $5$ min per job |
| **Load balancing** | Dynamic dispatch with longest-first queue ordering |
| **Fault tolerance** | Sweep progress file; automatic resubmission of failed tasks |
| **Sweet-spot core count** | $16$–$64$ (efficiency $> 80\%$, wall time $< 20$ min) |
| **Full Atlas wall time at 16 cores** | $\sim 17$ minutes |

The parallelization requires no modification to the simulation engine itself — only the orchestrator (task queue, dispatch, progress tracking) is parallel-aware. Each worker runs the identical single-threaded engine that would be used for a single-core execution. This ensures that parallel execution produces identical results to sequential execution (the embarrassingly parallel structure guarantees this by construction) and that the parallelization can be validated by comparing any parallel-produced output to its single-core counterpart.

---

## 5. Observable Computation

### 5.1 Energy Functional

The total energy $\mathcal{E}[\rho, v]$ is the primary Lyapunov functional of the ED system (Appendix C.2, eq. C.3). Its monotonic decrease along solutions is the foundational structural property of the dynamics (Lemma C.6), and its value at each time step is the basis for the energy-monotonicity check (§1.8.5, §2.6.2.4), the energy-barrier verification (§1.6.4), and the three-channel dissipation decomposition (Atlas §5.1). This subsection specifies how the energy is computed, logged, and validated.

---

#### 5.1.1 Definition

The total energy is

$$
\mathcal{E}[\rho, v] = \int_\Omega \Phi(\rho(x))\,dx + \frac{\tau H}{2}\,v^2,
$$

where the density potential $\Phi : (0, \rho_{\max}) \to \mathbb{R}$ is

$$
\Phi(\rho) = \int_{\rho^*}^{\rho}\frac{P(r)}{M(r)}\,dr.
$$

The energy has two terms:

- **Potential energy** $\int_\Omega\Phi(\rho)\,dx$: the cost of the density configuration relative to the equilibrium $\rho^*$. It is non-negative (since $\Phi$ is minimized at $\rho^*$ with $\Phi(\rho^*) = 0$), strictly convex (since $\Phi''(\rho^*) = P_*'/M_* > 0$), and diverges at both boundaries ($\Phi(\rho) \to +\infty$ as $\rho \to 0^+$ or $\rho \to \rho_{\max}^-$; see Propositions C.11 and the analogous result at $\rho = 0$).

- **Kinetic energy** $\frac{\tau H}{2}v^2$: the cost of the participation deviation. It is a simple quadratic in $v$ with coefficient $\tau H/2$.

At the equilibrium $(\rho^*, 0)$: $\mathcal{E}[\rho^*, 0] = 0$ (since $\Phi(\rho^*) = 0$ and $v = 0$). The energy is strictly positive for any non-equilibrium state.

---

#### 5.1.2 Computation

The energy computation has two components: the density potential integral and the participation kinetic term.

##### 5.1.2.1 Density Potential: Pointwise Evaluation of $\Phi(\rho_j)$

At each grid point $j$, the potential $\Phi(\rho_j)$ is computed by evaluating the integral

$$
\Phi(\rho_j) = \int_{\rho^*}^{\rho_j}\frac{P(r)}{M(r)}\,dr.
$$

**For the default constitutive functions** ($M(\rho) = M_0(\rho_{\max} - \rho)^\beta$, $P(\rho) = P_0(\rho - \rho^*)$):

$$
\Phi(\rho) = \frac{P_0}{M_0}\int_{\rho^*}^{\rho}\frac{r - \rho^*}{(\rho_{\max} - r)^\beta}\,dr.
$$

At $\beta = 2$, this integral has a closed form:

$$
\Phi(\rho) = \frac{P_0}{M_0}\left[\frac{\rho_{\max} - \rho^*}{\rho_{\max} - \rho} - \ln\!\left(\frac{\rho_{\max} - \rho^*}{\rho_{\max} - \rho}\right) - 1\right].
$$

The derivation: substitute $s = \rho_{\max} - r$, expand $(r - \rho^*) = (\rho_{\max} - \rho^*) - s$, and integrate $\int s^{-2}[(\rho_{\max} - \rho^*) - s]\,ds = -(\rho_{\max} - \rho^*)/s + \ln s$, evaluated between the limits.

For the default parameters ($P_0 = M_0 = 1$, $\rho^* = 0.5$, $\rho_{\max} = 1.0$):

$$
\Phi(\rho) = \frac{0.5}{1.0 - \rho} - \ln\!\left(\frac{0.5}{1.0 - \rho}\right) - 1.
$$

**Verification.** $\Phi(0.5) = 0.5/0.5 - \ln(1) - 1 = 1 - 0 - 1 = 0$ ✓. $\Phi'(\rho) = P(\rho)/M(\rho) = (\rho - 0.5)/(1 - \rho)^2$. At $\rho = 0.5$: $\Phi'(0.5) = 0$ ✓. $\Phi''(0.5) = P_*'/M_* = 1/0.25 = 4 > 0$ ✓.

**For non-default constitutive functions** (arbitrary $M$ and $P$): the integral must be computed numerically at each grid point. The engine uses adaptive quadrature (§0.5, minimum capabilities) with absolute tolerance $10^{-12}$:

$$
\Phi(\rho_j) = \text{QUAD}\!\left(\frac{P(r)}{M(r)},\; \rho^*,\; \rho_j;\; \text{atol} = 10^{-12}\right).
$$

The quadrature is called once per grid point per output step (not per internal step — the energy is computed only at output steps and for the per-step monotonicity check).

**Precomputation for the default case.** When the closed-form $\Phi$ is available, the engine evaluates it directly (no quadrature). This is significantly faster: a single function evaluation versus an adaptive quadrature with $\sim 10$–$50$ function evaluations. The engine detects the default constitutive type at initialization (§2.1.3) and selects the closed-form path automatically. The generic quadrature path is used only for non-default constitutive functions.

**Near-boundary evaluation.** As $\rho_j \to \rho_{\max}$: $\Phi(\rho_j) \to +\infty$. The closed-form expression $\Phi(\rho) = 0.5/(1 - \rho) - \ln(0.5/(1 - \rho)) - 1$ is well-behaved numerically for all $\rho < \rho_{\max}$ (the divergence is a smooth $1/(1 - \rho)$ singularity, not an oscillatory or cancellation-prone expression). At $\rho_j = \rho_{\max} - \delta_{\mathrm{floor}} = 1.0 - 10^{-12}$: $\Phi \approx 0.5 \times 10^{12}$, which is representable in double precision (the maximum is $\sim 10^{308}$).

As $\rho_j \to 0^+$: $\Phi(\rho_j) \to +\infty$ as well (since $P(\rho) < 0$ for $\rho < \rho^*$ and $M(\rho) > 0$, the integral $\int_{\rho^*}^{\rho}P(r)/M(r)\,dr$ accumulates negative values, but $\Phi$ is defined as the unsigned integral from $\rho^*$ downward, which is positive). At $\rho_j = \delta_{\mathrm{floor}} = 10^{-12}$: $\Phi$ is large but finite and representable in double precision.

##### 5.1.2.2 Spatial Integration

The potential energy integral $\int_\Omega\Phi(\rho)\,dx$ is approximated by the trapezoidal rule on the grid:

**One dimension:**

$$
\int_0^L\Phi(\rho(x))\,dx \approx h\left[\frac{1}{2}\Phi(\rho_0) + \sum_{j=1}^{N}\Phi(\rho_j) + \frac{1}{2}\Phi(\rho_{N+1})\right].
$$

The trapezoidal rule is second-order accurate for smooth integrands ($O(h^2)$ error) and matches the second-order accuracy of the spatial discretization (Method A). For Method B, the spatial integration is computed in spectral space using Parseval's identity when possible, or by the trapezoidal rule on the $N_{\mathrm{phys}}$-point physical-space grid.

**Two dimensions:**

$$
\int_{\Omega_2}\Phi(\rho)\,dx\,dy \approx h_x h_y\sum_{i,j}\Phi(\rho_{i,j}),
$$

with the standard trapezoidal weights (half-weights at edges, quarter-weights at corners).

##### 5.1.2.3 Participation Kinetic Energy

The kinetic term is trivial:

$$
\mathcal{E}_{\mathrm{kin}} = \frac{\tau H}{2}\,v^2.
$$

This requires two multiplications and no spatial integration.

##### 5.1.2.4 Total Energy Assembly

The total energy is:

$$
\mathcal{E}^n = \mathcal{E}_{\mathrm{pot}}^n + \mathcal{E}_{\mathrm{kin}}^n,
$$

where $\mathcal{E}_{\mathrm{pot}}^n$ is the trapezoidal-rule approximation to $\int_\Omega\Phi(\rho^n)\,dx$ and $\mathcal{E}_{\mathrm{kin}}^n = (\tau H/2)(v^n)^2$.

**Cost.** The energy computation requires $N_{\mathrm{grid}}$ evaluations of $\Phi$ (one per grid point) and one summation. For the closed-form case: $O(N_{\mathrm{grid}})$ floating-point operations ($\sim 10$ operations per grid point for the evaluation of $0.5/(1 - \rho) - \ln(0.5/(1 - \rho)) - 1$). For the quadrature case: $O(N_{\mathrm{grid}} \times Q)$ operations, where $Q \sim 20$–$50$ is the number of quadrature evaluations per point.

---

#### 5.1.3 Logging

The energy is logged at two levels:

##### 5.1.3.1 Per-Step Energy (Monotonicity Check)

At every internal step $n$, the energy $\mathcal{E}^n$ is computed and compared to $\mathcal{E}^{n-1}$ for the monotonicity check (§2.6.2.4, E05/E06). This computation uses the current density array and participation variable and does not require the full observable extraction. The energy value is stored in a scalar variable `energy_current` (§2.5.2.1, dynamic state) and overwritten at each step. It is *not* written to the output file at every step (that would be every-step sampling, §2.3.3.1, which is not the default).

The per-step energy is used for:

- The monotonicity check: $\mathcal{E}^{n+1} \leq \mathcal{E}^n + \text{tol}$.
- The energy-barrier check (at output steps): $\delta^n \geq \delta_{\mathrm{barrier}}(\mathcal{E}^n)$.
- The post-projection recomputation (§1.7.3): if the positivity projection modifies the density, $\mathcal{E}^{n+1}$ is recomputed from the projected state.

##### 5.1.3.2 Output-Step Energy (Time-Series Record)

At each output step, the energy $\mathcal{E}^n$ is recorded in the `energy` field of the `Observables` record (§1.2.8) and appended to the time series (§2.4.1). This is the energy value that appears in the Atlas figures (e.g., Figure 1.2, top panel; Figure 7.1, panel 1).

The time-series energy record includes:

| Field | Value |
|-------|-------|
| `energy` | $\mathcal{E}^n$ (total) |
| `energy_potential` | $\mathcal{E}_{\mathrm{pot}}^n$ (density potential only) |
| `energy_kinetic` | $\mathcal{E}_{\mathrm{kin}}^n = \frac{\tau H}{2}(v^n)^2$ |

The split into potential and kinetic components enables the analysis of which component dominates the energy at each time — useful for the three-channel dissipation analysis (Atlas §5.1.3) and for identifying when the participation variable is the dominant energy reservoir (typically during the oscillatory transient of the homogeneous mode).

---

#### 5.1.4 Validation

The energy computation is validated by five checks, each targeting a different aspect of correctness.

##### 5.1.4.1 Equilibrium Value

**Check.** At $\rho = \rho^*$ (uniform) and $v = 0$:

$$
\mathcal{E}[\rho^*, 0] = \int_\Omega\Phi(\rho^*)\,dx + 0 = 0 \cdot |\Omega| = 0.
$$

**Test.** Initialize with $\rho_j = \rho^*$ for all $j$ and $v = 0$. Compute $\mathcal{E}$. Verify $|\mathcal{E}| < 10^{-14}$.

**Failure mode.** A nonzero equilibrium energy indicates an error in the $\Phi$ computation (e.g., incorrect integration limits, wrong constitutive function, or a constant offset in the potential).

##### 5.1.4.2 Quadratic Approximation Near Equilibrium

**Check.** For small perturbations $u = \rho - \rho^*$:

$$
\mathcal{E}[\rho^* + u, v] \approx \frac{1}{2}\frac{P_*'}{M_*}\int_\Omega u^2\,dx + \frac{\tau H}{2}v^2 + O(\|u\|^3).
$$

**Test.** Initialize with $\rho_j = \rho^* + \epsilon\cos(\pi x_j)$ for small $\epsilon = 10^{-4}$ and $v = 10^{-4}$. Compute $\mathcal{E}$ and compare to the quadratic prediction $\mathcal{E}_{\mathrm{quad}} = \frac{1}{2}(P_*'/M_*)\epsilon^2 L/2 + \frac{1}{2}\tau H\epsilon^2$. The relative error should be $O(\epsilon) < 10^{-3}$.

**Failure mode.** A relative error significantly above $O(\epsilon)$ indicates an error in the constitutive evaluation ($P_*'/M_*$ used in the quadratic approximation does not match the actual $\Phi''(\rho^*)$) or in the spatial integration (trapezoidal rule applied incorrectly).

##### 5.1.4.3 Monotonicity Under the Dynamics

**Check.** For a solution evolving under the canonical system, $\mathcal{E}(t)$ is non-increasing (Lemma C.6).

**Test.** This is Validation Test 2 (Atlas §1.7.2, Experiment 1.2). Integrate with a multi-mode IC for $T = 50$ and verify that $\mathcal{E}^{n+1} \leq \mathcal{E}^n + \text{tol}$ at every step.

**Failure mode.** A sustained energy increase indicates a CFL violation (§1.8), an incorrect implicit-matrix assembly (§1.4.1), or an error in the constitutive evaluation.

##### 5.1.4.4 Barrier Divergence

**Check.** $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}$.

**Test.** Evaluate $\Phi(\rho_{\max} - \delta)$ for $\delta \in \{0.1, 0.01, 0.001, 10^{-6}\}$. Verify that $\Phi$ increases monotonically and that $\Phi(\rho_{\max} - 10^{-6}) > 10^5$ (for the default parameters). Compare to the analytic asymptotic $\Phi \approx 0.5/\delta$.

**Failure mode.** A non-divergent $\Phi$ at $\rho_{\max}$ indicates an error in the closed-form expression or in the numerical quadrature (the integrand $P(r)/M(r)$ must diverge as $r \to \rho_{\max}$, and the quadrature must capture this divergence). A common error is evaluating the quadrature with insufficient resolution near the singular endpoint.

##### 5.1.4.5 Dissipation Identity Closure

**Check.** The discrete energy change per step should equal (to truncation-error accuracy) the sum of the three dissipation channels:

$$
\mathcal{E}^{n+1} - \mathcal{E}^n \approx -\Delta t\bigl(\mathcal{D}_{\mathrm{diff}}^n + \mathcal{D}_{\mathrm{pen}}^n + \mathcal{D}_{\mathrm{part}}^n\bigr),
$$

where the channels are defined in §5.1.3 of the Atlas and computed in the observable extraction (§1.1.6).

**Test.** This is part of Validation Test 2 (Atlas §1.7.2). The residual $r^n = \mathcal{E}^{n+1} - \mathcal{E}^n + \Delta t(\mathcal{D}_{\mathrm{diff}}^n + \mathcal{D}_{\mathrm{pen}}^n + \mathcal{D}_{\mathrm{part}}^n)$ should satisfy $|r^n| < 10\,\Delta t^p\,\mathcal{E}^n$, where $p$ is the temporal order of the scheme.

**Failure mode.** A large residual indicates either an error in the energy computation (§5.1.2), an error in the dissipation-channel computation (the three channels do not correctly decompose the energy derivative), or an inconsistency between the time-stepping scheme and the dissipation formula (e.g., using the Crank–Nicolson dissipation formula with the implicit Euler state update).

---

#### 5.1.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Definition** | $\mathcal{E} = \int_\Omega\Phi(\rho)\,dx + \frac{\tau H}{2}v^2$ with $\Phi(\rho) = \int_{\rho^*}^{\rho}P(r)/M(r)\,dr$ |
| **Computation (default)** | Closed-form $\Phi$ at each grid point + trapezoidal spatial integration |
| **Computation (general)** | Adaptive quadrature for $\Phi$ at each grid point + trapezoidal integration |
| **Cost** | $O(N_{\mathrm{grid}})$ (closed-form) or $O(N_{\mathrm{grid}} \times Q)$ (quadrature) per evaluation |
| **Logging frequency** | Every internal step (for monotonicity check); full record at output steps |
| **Output fields** | `energy`, `energy_potential`, `energy_kinetic` |
| **Equilibrium value** | $\mathcal{E}[\rho^*, 0] = 0$ (verified at initialization) |
| **Key property** | Monotonically non-increasing along solutions (Lemma C.6) |
| **Validation tests** | Equilibrium value, quadratic approximation, monotonicity, barrier divergence, dissipation closure |

The energy functional is the most frequently computed observable (once per internal step for the monotonicity check) and the most structurally significant (its monotonicity is the discrete analogue of the Lyapunov property that underlies the entire convergence theory of Appendix C). Its correct computation is a prerequisite for every other observable and every structural check in the simulation engine.

---

### 5.2 Dissipation Channels

The energy dissipation bound (Lemma C.6) and the linearized Lyapunov analysis (Proposition C.42, eq. C.45) decompose the total energy loss rate into three structurally distinct channels, each governed by a specific canonical principle. The decomposition is not merely an analytic convenience — it identifies the *mechanism* by which energy is removed from each configuration: spatial smoothing (diffusion), density relaxation (penalty), and participation damping. The simulation engine computes all three channels at every output step, enabling the dissipation-channel analysis of Atlas §5.1.3 (Figure 5.2) and the dissipation-identity closure test of Atlas §1.7.2 (Figure 1.2, bottom panel).

---

#### 5.2.1 The Three Channels

The total energy dissipation rate $-d\mathcal{E}/dt$ is decomposed near equilibrium (Proposition C.42) as:

$$
-\frac{d\mathcal{E}}{dt} \approx \mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}} + \text{cross terms},
$$

where the three channels are defined as follows.

##### 5.2.1.1 Gradient Dissipation $\mathcal{D}_{\mathrm{diff}}$

**Definition.**

$$
\mathcal{D}_{\mathrm{diff}} := D\,P_*'\,C_{\mathrm{ED}} = D\,P_*'\int_\Omega|\nabla\rho|^2\,dx.
$$

**Structural origin.** Principle 1 (Operator Structure) provides the diffusion $M(\rho)\nabla^2\rho$, which smooths spatial gradients. Principle 3 (Penalty Equilibrium) provides $P_*' > 0$, which ensures the gradient contribution is sign-definite. The product $D\,P_*'$ is the direct-channel penalty rate — the rate at which the direct channel converts spatial structure into energy loss.

**Physical meaning.** The gradient channel measures the rate at which spatial inhomogeneity is erased. High-gradient configurations (large $C_{\mathrm{ED}}$) dissipate faster through this channel. At equilibrium ($\nabla\rho = 0$): $\mathcal{D}_{\mathrm{diff}} = 0$.

**Regime dependence.** The gradient channel dominates at early times (when the initial condition has high spatial complexity, §5.1 of the Atlas) and at high mode numbers (since $C_{\mathrm{ED}} = \sum_n\mu_n|a_n|^2$ weights the high modes more heavily). It is the fastest dissipation channel for configurations with broad spectral content.

**Near-equilibrium approximation.** $\mathcal{D}_{\mathrm{diff}} = D\,P_*'\,C_{\mathrm{ED}}$ is the *leading-order* gradient dissipation, valid when $\rho \approx \rho^*$ so that $P'(\rho) \approx P_*'$ across the domain. The exact gradient dissipation from Lemma C.6 is $D\int_\Omega P'(\rho)|\nabla\rho|^2/M(\rho)\,dx$, which involves the density-dependent ratio $P'(\rho)/M(\rho)$ rather than the constant $P_*'$. The near-equilibrium formula underestimates the dissipation when $\rho$ is near $\rho_{\max}$ (where $P'/M \gg P_*'/M_*$, the effective-complexity amplification of §6.3 in the Atlas) and overestimates it when $\rho$ is near $0$ (where $P'/M < P_*'/M_*$).

##### 5.2.1.2 Penalty Dissipation $\mathcal{D}_{\mathrm{pen}}$

**Definition.**

$$
\mathcal{D}_{\mathrm{pen}} := \frac{D\,P_*'^{\,2}}{M_*}\int_\Omega(\rho - \rho^*)^2\,dx = \frac{D\,P_*'^{\,2}}{M_*}\,\|u\|_{L^2}^2.
$$

**Structural origin.** Principle 3 (Penalty Equilibrium) provides the penalty restoring force $-P(\rho)$, which drives $\rho$ toward $\rho^*$. The penalty dissipation is the rate at which the mean density deviation is reduced, independent of the spatial structure. The coefficient $D\,P_*'^2/M_*$ involves the square of the penalty slope, reflecting the fact that the penalty both creates the restoring force and sets the energy scale ($\Phi''(\rho^*) = P_*'/M_*$).

**Physical meaning.** The penalty channel measures the rate at which the density field relaxes toward its equilibrium value $\rho^*$ in the spatially averaged sense. It is active even for spatially uniform perturbations ($\nabla\rho = 0$, $C_{\mathrm{ED}} = 0$), where it is the *only* dissipation mechanism (aside from the participation channel).

**Regime dependence.** The penalty channel dominates at intermediate times (after the spatial gradients have been smoothed by the gradient channel but before the mean deviation has fully relaxed) and for low-complexity configurations (where $C_{\mathrm{ED}}$ is small and $\|u\|_{L^2}$ is the dominant deviation measure). In the linearized regime, the penalty channel and the gradient channel are related through the Poincaré–Wirtinger inequality: $\|u - \bar{u}\|_{L^2}^2 \leq C_\Omega\,C_{\mathrm{ED}}$, so the penalty dissipation bounds the gradient dissipation from below (up to a factor).

##### 5.2.1.3 Participation Dissipation $\mathcal{D}_{\mathrm{part}}$

**Definition.**

$$
\mathcal{D}_{\mathrm{part}} := H\,\zeta\,v^2.
$$

**Structural origin.** Principle 5 (Participation Feedback Loop) introduces the participation variable $v$ and its integration time $\tau$. The participation damping coefficient $\zeta$ (from the participation equation $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$) causes $v$ to decay exponentially in the absence of driving. The energy stored in the participation ($\frac{\tau H}{2}v^2$, the kinetic term in $\mathcal{E}$) is dissipated at rate $H\zeta v^2$.

**Physical meaning.** The participation channel measures the rate at which the feedback loop's accumulated operator output is damped. It is active whenever $v \neq 0$, regardless of the spatial structure of $\rho$. In the oscillatory regime (Spiral Sheet), the participation variable oscillates with a damped envelope, and $\mathcal{D}_{\mathrm{part}}$ oscillates correspondingly (peaking when $|v|$ is at its maximum in each cycle). In the monotonic regime, $\mathcal{D}_{\mathrm{part}}$ decays monotonically.

**Regime dependence.** The participation channel contributes throughout the dynamics but is most visible during the oscillatory transient of the homogeneous mode (Atlas §2.1, §7.2). Its relative importance increases with $H$ (stronger mediated channel) and with $\zeta$ (stronger damping per unit participation). For Parameter Set I ($H = 0.7$, $\zeta = 0.1$): $\mathcal{D}_{\mathrm{part}} = 0.07\,v^2$. For Parameter Set IV ($H = 0.1$, $\zeta = 5.0$): $\mathcal{D}_{\mathrm{part}} = 0.5\,v^2$. The per-unit-$v^2$ rate is seven times larger for Set IV, but the participation is typically smaller (the weak mediated channel generates less $v$).

---

#### 5.2.2 Discrete Computation

Each channel is computed from the discrete density array $\boldsymbol{\rho}^n$, the participation variable $v^n$, and the precomputed constitutive values.

##### 5.2.2.1 Gradient Dissipation

**Near-equilibrium formula (default):**

$$
\mathcal{D}_{\mathrm{diff}}^n = D\,P_*'\,C_{\mathrm{ED}}^n,
$$

where $C_{\mathrm{ED}}^n$ is the discrete ED-complexity computed by the trapezoidal rule on the gradient-squared array (§1.1.6):

$$
C_{\mathrm{ED}}^n = h\sum_{j=0}^{N_{\mathrm{grid}}-1}(|\nabla_h\rho^n|^2)_j.
$$

The gradient-squared values $(|\nabla_h\rho^n|^2)_j$ are already available from the operator evaluation (§2.3.2.1, Step 4b), so the computation of $C_{\mathrm{ED}}^n$ requires only a weighted summation — no additional array passes.

**Full formula (for near-horizon experiments):**

$$
\mathcal{D}_{\mathrm{diff,full}}^n = D\,h\sum_{j=0}^{N_{\mathrm{grid}}-1}\frac{P'(\rho_j^n)}{M(\rho_j^n)}\,(|\nabla_h\rho^n|^2)_j.
$$

This is the discrete approximation to $D\int_\Omega(P'(\rho)/M(\rho))|\nabla\rho|^2\,dx$, the full dissipation integrand from Lemma C.6. It requires the pointwise constitutive values $P'(\rho_j)$ and $M(\rho_j)$, which are available from the constitutive buffers (§1.2.6). The safeguarded evaluation (§1.6.6) prevents division by zero at near-horizon grid points.

**Selection rule.** The engine computes both formulas at every output step. The near-equilibrium formula is the default for logging (it is simpler and matches the Lyapunov analysis of Proposition C.42). The full formula is logged as $C_{\mathrm{ED}}^{\mathrm{eff}}$ (the effective complexity, §5.2 of the Atlas) and is used for the dissipation-identity closure test (§5.1.4.5) when the density is far from equilibrium.

##### 5.2.2.2 Penalty Dissipation

$$
\mathcal{D}_{\mathrm{pen}}^n = \frac{D\,P_*'^{\,2}}{M_*}\,h\sum_{j=0}^{N_{\mathrm{grid}}-1}(\rho_j^n - \rho^*)^2.
$$

This is the trapezoidal-rule approximation to $(D\,P_*'^2/M_*)\|u\|_{L^2}^2$. The deviation $u_j = \rho_j^n - \rho^*$ is computed by subtracting the scalar $\rho^*$ from each grid value — a single pass over the array.

**Full formula (for non-default constitutive functions):**

$$
\mathcal{D}_{\mathrm{pen,full}}^n = D\,h\sum_{j=0}^{N_{\mathrm{grid}}-1}\frac{P(\rho_j^n)^2}{M(\rho_j^n)}.
$$

This is the discrete approximation to $D\int_\Omega P(\rho)^2/M(\rho)\,dx$, which appears in the energy identity (eq. C.7) as the penalty-squared contribution. For the linear penalty ($P(\rho) = P_0(\rho - \rho^*)$), this reduces to $D\,P_0^2\sum_j(\rho_j - \rho^*)^2/M(\rho_j) \cdot h$, which differs from the near-equilibrium formula by the factor $M_*/M(\rho_j)$. The near-equilibrium formula uses $M_*$ (constant); the full formula uses $M(\rho_j)$ (density-dependent).

##### 5.2.2.3 Participation Dissipation

$$
\mathcal{D}_{\mathrm{part}}^n = H\,\zeta\,(v^n)^2.
$$

This is a scalar computation: two multiplications. No spatial integration is needed because $v$ is spatially constant.

##### 5.2.2.4 Cost Summary

| Channel | Arrays needed | Operations | Cost |
|---------|-------------|-----------|------|
| $\mathcal{D}_{\mathrm{diff}}$ (near-equil.) | $(|\nabla_h\rho|^2)_j$ (already computed) | $1$ weighted sum | $O(N_{\mathrm{grid}})$ |
| $\mathcal{D}_{\mathrm{diff,full}}$ | $(|\nabla_h\rho|^2)_j$, $P'(\rho_j)$, $M(\rho_j)$ | $1$ weighted sum with pointwise division | $O(N_{\mathrm{grid}})$ |
| $\mathcal{D}_{\mathrm{pen}}$ (near-equil.) | $(\rho_j - \rho^*)$ | $1$ squared sum | $O(N_{\mathrm{grid}})$ |
| $\mathcal{D}_{\mathrm{pen,full}}$ | $P(\rho_j)$, $M(\rho_j)$ | $1$ weighted sum with squaring and division | $O(N_{\mathrm{grid}})$ |
| $\mathcal{D}_{\mathrm{part}}$ | $v$ | $2$ multiplications | $O(1)$ |
| **Total (all channels)** | | | **$O(N_{\mathrm{grid}})$** |

The total cost of computing all three channels is $O(N_{\mathrm{grid}})$ per output step — the same order as a single stencil evaluation and negligible compared to the time-stepping cost.

---

#### 5.2.3 Logging

The three dissipation channels are recorded in the `Observables` record (§1.2.8) at each output step:

| Field | Value | Formula |
|-------|-------|---------|
| `D_diff` | $\mathcal{D}_{\mathrm{diff}}^n$ | $D\,P_*'\,C_{\mathrm{ED}}^n$ |
| `D_pen` | $\mathcal{D}_{\mathrm{pen}}^n$ | $(D\,P_*'^2/M_*)\,\|u^n\|_{L^2}^2$ |
| `D_part` | $\mathcal{D}_{\mathrm{part}}^n$ | $H\,\zeta\,(v^n)^2$ |

Additionally, the full formulas are logged as supplementary fields when the experiment involves near-horizon dynamics (Atlas §§5.1.3, 6.3):

| Field | Value |
|-------|-------|
| `D_diff_full` | $D\,h\sum_j(P'(\rho_j)/M(\rho_j))(|\nabla_h\rho|^2)_j$ |
| `D_pen_full` | $D\,h\sum_j P(\rho_j)^2/M(\rho_j)$ |

The supplementary fields are computed only when requested by the experiment specification (to avoid the additional constitutive evaluations for experiments where the near-equilibrium formulas suffice).

**Derived quantities.** The following derived quantities are computed from the logged channels and included in the time-series output:

| Derived field | Formula | Use |
|--------------|---------|-----|
| `D_total` | $\mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}}$ | Total dissipation rate (near-equilibrium) |
| `dissipation_residual` | $(\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t + \mathcal{D}_{\mathrm{total}}^n$ | Dissipation-identity closure residual |
| `frac_diff` | $\mathcal{D}_{\mathrm{diff}} / \mathcal{D}_{\mathrm{total}}$ | Gradient channel fraction |
| `frac_pen` | $\mathcal{D}_{\mathrm{pen}} / \mathcal{D}_{\mathrm{total}}$ | Penalty channel fraction |
| `frac_part` | $\mathcal{D}_{\mathrm{part}} / \mathcal{D}_{\mathrm{total}}$ | Participation channel fraction |

The three fractions sum to $1$ (by construction) and provide a normalized view of which channel dominates at each time. The crossover times (when one channel overtakes another) are identifiable from the fraction time series.

---

#### 5.2.4 Validation

The dissipation-channel computation is validated by three checks.

##### 5.2.4.1 Non-Negativity

Each channel is non-negative by construction:

- $\mathcal{D}_{\mathrm{diff}} = D\,P_*'\,C_{\mathrm{ED}} \geq 0$ because $D > 0$, $P_*' > 0$, $C_{\mathrm{ED}} \geq 0$.
- $\mathcal{D}_{\mathrm{pen}} = (D\,P_*'^2/M_*)\,\|u\|_{L^2}^2 \geq 0$ because all factors are positive.
- $\mathcal{D}_{\mathrm{part}} = H\,\zeta\,v^2 \geq 0$ because $H > 0$, $\zeta > 0$, $v^2 \geq 0$.

**Test.** At every output step, verify $\mathcal{D}_{\mathrm{diff}} \geq 0$, $\mathcal{D}_{\mathrm{pen}} \geq 0$, $\mathcal{D}_{\mathrm{part}} \geq 0$. A negative value indicates an implementation error (e.g., a sign flip in the gradient computation or a negative constitutive value).

##### 5.2.4.2 Equilibrium Values

At the equilibrium $(\rho^*, 0)$: all three channels are exactly zero.

- $\mathcal{D}_{\mathrm{diff}} = D\,P_*'\cdot 0 = 0$ (no gradients).
- $\mathcal{D}_{\mathrm{pen}} = (D\,P_*'^2/M_*)\cdot 0 = 0$ (no deviation).
- $\mathcal{D}_{\mathrm{part}} = H\,\zeta\cdot 0 = 0$ (no participation).

**Test.** Initialize with $\rho = \rho^*$, $v = 0$. Verify all three channels are below $10^{-14}$.

##### 5.2.4.3 Dissipation-Identity Closure

The sum of the three channels should approximate the negative energy rate:

$$
\mathcal{D}_{\mathrm{total}}^n \approx -\frac{\mathcal{E}^{n+1} - \mathcal{E}^n}{\Delta t}.
$$

The residual $r^n = (\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t + \mathcal{D}_{\mathrm{total}}^n$ includes:

- The truncation error of the time-stepping scheme ($O(\Delta t^p)$).
- The linearization error of the near-equilibrium channel formulas ($O(\|\rho - \rho^*\|^2)$).
- The cross-coupling terms between $\rho$ and $v$ that are not captured by the three-channel decomposition ($O(\|u\|\,|v|)$).

For the linearized regime ($\|u\| \ll 1$, $|v| \ll 1$): the residual is $O(\Delta t^p)$, dominated by the temporal truncation. For the nonlinear regime: the residual includes the $O(\|u\|^2)$ linearization error, which can be significant at early times when the perturbation is large.

**Test.** This is Validation Test 2 (Atlas §1.7.2). The acceptance criterion is $|r^n| < 10\,\Delta t^p\,\mathcal{E}^n$ at every output step. At late times (when the solution is in the linearized regime), the residual should decrease toward $O(\Delta t^p)$.

**Failure diagnosis.** If the residual is large:

| Residual pattern | Likely cause |
|-----------------|-------------|
| $r^n > 0$ consistently (channels overestimate dissipation) | Near-equilibrium formulas overcount; switch to full formulas |
| $r^n < 0$ consistently (channels underestimate dissipation) | Cross-coupling terms significant; density far from equilibrium |
| $r^n$ oscillates at frequency $\omega$ | Participation coupling not fully captured by the three channels |
| $|r^n|$ grows over time | Energy computation error or CFL instability |

The first two patterns are expected for far-from-equilibrium initial conditions and resolve as the solution enters the linearized regime. The third is expected for oscillatory parameter sets and reflects the phase relationship between $u$ and $v$ in the cross terms. The fourth is a genuine error requiring investigation.

---

#### 5.2.5 Structural Interpretation

The three channels correspond to the three dissipation mechanisms identified in the stability analysis (Proposition C.42, eq. C.45) and mapped to canonical principles in Remark C.77:

| Channel | Principle | Mechanism | Active when |
|---------|-----------|-----------|-------------|
| $\mathcal{D}_{\mathrm{diff}}$ | P1 (Operator Structure) + P3 (Penalty) | Diffusive smoothing of spatial gradients | $C_{\mathrm{ED}} > 0$ |
| $\mathcal{D}_{\mathrm{pen}}$ | P3 (Penalty Equilibrium) | Restoring force toward $\rho^*$ | $\|\rho - \rho^*\|_{L^2} > 0$ |
| $\mathcal{D}_{\mathrm{part}}$ | P5 (Participation Feedback) | Damping of the accumulated operator output | $|v| > 0$ |

The channels are not independent — they interact through the PDE–ODE coupling (the density feeds $F[\rho]$ into the participation, and the participation feeds $Hv$ back into the density). The cross terms, which are $O(\|u\|\,|v|)$, are positive or negative depending on the phase relationship between $u$ and $v$. In the oscillatory regime, the cross terms oscillate and average to zero over one cycle; in the monotonic regime, they are sign-definite and contribute to the total dissipation. The three-channel decomposition captures the leading-order structure; the cross terms are the $O(\|u\|\,|v|)$ correction.

The Atlas experiments demonstrate the temporal ordering of the channels (Atlas §5.1.3, Figure 5.2): gradient dissipation dominates at early times, penalty dissipation dominates at intermediate times, and participation dissipation oscillates throughout. The crossover time from gradient-dominated to penalty-dominated is a measurable quantity that depends on the initial complexity and the canonical parameters.

---

### 5.3 Modal Amplitudes

The spectral decomposition of the density field into the Neumann eigenbasis (Appendix C.4, eq. C.23) is the foundation of the modal hierarchy (Proposition C.29), the spectral gap (Lemma C.31), the triad selection rule (Theorem C.34), and the locked amplitude ratios (Proposition C.35). The simulation engine extracts the modal amplitudes at every output step, tracks their evolution over time, and derives scalar observables (decay rates, frequencies, amplitude ratios) from the time series. This subsection specifies the decomposition, the tracking infrastructure, and the decay-rate extraction methodology.

---

#### 5.3.1 Spectral Decomposition

##### 5.3.1.1 The Neumann Eigenbasis

The density deviation $u(x, t) = \rho(x, t) - \rho^*$ is expanded in the Neumann eigenbasis on $\Omega = [0, L]$:

$$
u(x, t) = \sum_{k=0}^{\infty}a_k(t)\,\varphi_k(x),
$$

where the eigenfunctions are

$$
\varphi_0(x) = \frac{1}{\sqrt{L}}, \qquad \varphi_k(x) = \sqrt{\frac{2}{L}}\,\cos\!\left(\frac{k\pi x}{L}\right) \quad (k \geq 1),
$$

and the modal amplitudes are the $L^2$-inner products

$$
a_k(t) = \langle u(\cdot, t),\, \varphi_k\rangle_{L^2(\Omega)} = \int_0^L u(x, t)\,\varphi_k(x)\,dx.
$$

The orthonormality $\langle\varphi_m, \varphi_n\rangle = \delta_{mn}$ ensures that the decomposition is unique and that Parseval's identity holds:

$$
\|u\|_{L^2}^2 = \sum_{k=0}^{\infty}|a_k|^2, \qquad C_{\mathrm{ED}} = \|\nabla u\|_{L^2}^2 = \sum_{k=1}^{\infty}\mu_k\,|a_k|^2.
$$

The mode $k = 0$ is the spatially uniform component: $a_0 = \sqrt{L}\,(\bar{\rho} - \rho^*)$, where $\bar{\rho} = L^{-1}\int_0^L\rho\,dx$ is the spatial mean. It couples to the participation variable $v$ through the $2 \times 2$ matrix $\mathbf{A}_0$ (eq. C.13). The modes $k \geq 1$ are the spatially structured components; each decays independently at rate $D\alpha_k = D(M_*\mu_k + P_*')$ in the linearized system (eq. C.11) and couples to other modes through the nonlinear triad (Theorem C.34) in the full system.

##### 5.3.1.2 Discrete Modal Amplitudes via the DCT

The discrete modal amplitudes are computed from the grid values $\boldsymbol{\rho}^n$ (or $\hat{\mathbf{u}}^n$ for Method B) by the forward discrete cosine transform (DCT-I).

**Method A (finite-difference grid).** The density deviation $u_j = \rho_j^n - \rho^*$ at the $N_{\mathrm{grid}}$ grid points is transformed to spectral space:

$$
\hat{a}_k = \text{DCT-I}\{u_j\}_{k}, \qquad k = 0, 1, \ldots, N_{\mathrm{grid}} - 1.
$$

The DCT-I computes the coefficients in the expansion $u(x) \approx \sum_k\hat{a}_k\varphi_k(x)$, where the $\varphi_k$ are evaluated at the grid points. The normalization convention must match the eigenbasis: $\hat{a}_0 = (1/\sqrt{L})\sum_j u_j\cdot(h/\sqrt{L}) \cdot (\text{weights})$, etc. The precise normalization depends on the DCT-I convention of the target environment:

| Environment | DCT-I convention | Normalization factor |
|-------------|-----------------|---------------------|
| Python (SciPy `dct(type=1)`) | $X_k = x_0 + (-1)^k x_{N-1} + 2\sum_{n=1}^{N-2}x_n\cos(k\pi n/(N-1))$ | Divide by $N_{\mathrm{grid}} - 1$ for orthonormality; adjust for $\varphi_k$ normalization |
| Julia (FFTW `REDFT00`) | Same as SciPy | Same |
| MATLAB (`dct` with `Type` parameter) | Built-in orthonormal convention | May require no additional normalization |

The engine applies the environment-specific normalization factor to produce the coefficients $a_k$ in the orthonormal Neumann basis. The correctness of the normalization is verified by the Parseval check (§5.3.4.1).

**Method B (spectral state).** The modal amplitudes are the primary state representation: $a_k = \hat{u}_k$ (no transform needed). The spectral log (§2.4.2) records the amplitudes directly from the state array. This is the fastest and most accurate path — no DCT rounding, no normalization ambiguity.

##### 5.3.1.3 Two-Dimensional Decomposition

On $\Omega_2 = [0, L_x] \times [0, L_y]$, the density deviation is expanded in the tensor-product basis $\varphi_{k_1}(x)\varphi_{k_2}(y)$:

$$
u(x, y, t) = \sum_{k_1, k_2 \geq 0}a_{k_1, k_2}(t)\,\varphi_{k_1}(x)\,\varphi_{k_2}(y).
$$

The 2D DCT is computed as sequential 1D DCTs along each axis. The resulting 2D array of coefficients $a_{k_1, k_2}$ is indexed by the mode pair $(k_1, k_2)$, with eigenvalue $\mu_{k_1, k_2} = (k_1\pi/L_x)^2 + (k_2\pi/L_y)^2$.

For the Atlas experiments on $\Omega_2$ (Experiment 3.7), the modal amplitudes are organized by the total eigenvalue $\mu = \mu_{k_1, k_2}$ rather than by the individual indices, because the decay rate $D\alpha = D(M_*\mu + P_*')$ depends only on $\mu$. Degenerate modes (different $(k_1, k_2)$ pairs with the same $\mu$) have the same decay rate and are grouped together.

---

#### 5.3.2 Modal Tracking

The engine tracks the modal amplitudes $\{a_k(t)\}$ over time, producing a time-indexed spectral dataset that is the basis for all spectral observables.

##### 5.3.2.1 Tracked Quantities Per Mode

At each output step $t_n$, the engine computes and records:

| Quantity | Symbol | Formula | Purpose |
|----------|--------|---------|---------|
| Modal amplitude | $a_k^n$ | $\langle u^n, \varphi_k\rangle$ (from DCT) | Primary spectral observable |
| Absolute amplitude | $|a_k^n|$ | $|a_k^n|$ | Semilog decay plots |
| Modal energy | $E_k^n$ | $|a_k^n|^2$ | Energy distribution, Parseval check |
| Weighted modal energy | $\mu_k E_k^n$ | $\mu_k|a_k^n|^2$ | Contribution to $C_{\mathrm{ED}}$ |
| Modal sign | $\operatorname{sign}(a_k^n)$ | $\pm 1$ | Zero-crossing detection |

##### 5.3.2.2 Number of Tracked Modes

The number of modes $N_{\mathrm{obs}}$ tracked at each output step is experiment-dependent (§2.4.2.1):

| Category | $N_{\mathrm{obs}}$ | Rationale |
|----------|---------------------|-----------|
| Default | $\min(32, N_{\mathrm{modes}})$ | Sufficient for most Atlas experiments |
| Triad experiments (§4) | $32$ | Track generation up to mode $16$ |
| Cascade experiments (§4.3) | $64$ | Track deep harmonic cascade |
| Convergence studies (§1.7) | $16$ | Only low modes needed for rate extraction |
| Pattern experiments (§9.3) | $32$ | Track harmonic comb |

Modes beyond $N_{\mathrm{obs}}$ are not tracked individually. Their aggregate contribution is monitored through two summary quantities:

- **Tail energy:** $E_{\mathrm{tail}} = \sum_{k > N_{\mathrm{obs}}}|a_k|^2$, computed as $\|u\|_{L^2}^2 - \sum_{k=0}^{N_{\mathrm{obs}}-1}|a_k|^2$ (using Parseval's identity to avoid computing the high-mode amplitudes explicitly).
- **Tail complexity:** $C_{\mathrm{tail}} = \sum_{k > N_{\mathrm{obs}}}\mu_k|a_k|^2$, computed as $C_{\mathrm{ED}} - \sum_{k=1}^{N_{\mathrm{obs}}-1}\mu_k|a_k|^2$.

These tail quantities verify that the tracked modes capture the dominant spectral content. For a well-resolved experiment, $E_{\mathrm{tail}}/\|u\|_{L^2}^2 < 10^{-6}$ (the tail carries less than $0.0001\%$ of the total energy).

##### 5.3.2.3 Spectral Purity Monitoring

For single-mode experiments (Atlas §3.1), the engine monitors **spectral purity** — the fraction of the total energy in modes other than the initialized mode:

$$
S_{\mathrm{purity}}^n = 1 - \frac{|a_{n_0}^n|^2}{\sum_k|a_k^n|^2},
$$

where $n_0$ is the initialized mode number. At $t = 0$: $S_{\mathrm{purity}} = 0$ (all energy in mode $n_0$). During the integration: $S_{\mathrm{purity}}$ increases as the nonlinear triad transfers energy to other modes. For small-amplitude experiments ($A = 10^{-3}$), $S_{\mathrm{purity}}$ should remain below $10^{-6}$ throughout (the triad transfer is $O(A^2)$ and the transferred energy is $O(A^4)$, far below the primary mode's $O(A^2)$).

A spectral purity violation ($S_{\mathrm{purity}} > 10^{-4}$ for a small-amplitude experiment) indicates either numerical aliasing (insufficient de-aliasing in Method B) or a CFL violation that has generated spurious high-frequency content (in Method A).

---

#### 5.3.3 Decay Rate Extraction

The primary scalar observable derived from the modal time series is the **measured decay rate** $\hat{\sigma}_k$ of each mode — the quantity that is compared to the analytic prediction $D\alpha_k$ (eq. C.11) to validate the modal hierarchy.

##### 5.3.3.1 Log-Linear Fitting

For a mode $k$ that decays exponentially ($|a_k(t)| = |a_k(0)|\,e^{-\sigma_k t}$), the decay rate is the slope of $\ln|a_k(t)|$ versus $t$. The measured rate $\hat{\sigma}_k$ is extracted by linear regression of $\ln|a_k(t)|$ over a fitting interval $[t_{\mathrm{start}}, t_{\mathrm{end}}]$:

$$
\hat{\sigma}_k = -\frac{\text{slope of least-squares fit of } \ln|a_k(t)| \text{ vs. } t}{1}.
$$

The fitting interval is chosen to exclude:

- **The initial transient** ($t < t_{\mathrm{start}}$): during the first few time steps, the discrete solution adjusts from the initial condition to the smooth parabolic trajectory. The transient duration is $t_{\mathrm{start}} \sim 5\Delta t$ for Method A (the implicit scheme's startup) and $t_{\mathrm{start}} \sim \Delta t$ for Method B (the ETD scheme has no startup transient).
- **The noise floor** ($t > t_{\mathrm{end}}$): once $|a_k(t)|$ drops below the noise level ($\sim 10^{-14}$ for double precision), the logarithm is dominated by rounding noise and the fit becomes unreliable. The end time is $t_{\mathrm{end}} = \min(T,\; t_{\mathrm{floor}}(k))$, where $t_{\mathrm{floor}}(k)$ is the time at which $|a_k|$ first drops below $10^{-10}$.

**Default fitting interval:**

$$
t_{\mathrm{start}} = 0.1, \qquad t_{\mathrm{end}} = \min\!\bigl(T - 0.5,\; t_{\mathrm{floor}}(k)\bigr).
$$

The interval $[0.1, t_{\mathrm{floor}}]$ captures the clean exponential decay phase, excluding both the startup and the noise floor.

##### 5.3.3.2 Fit Quality Assessment

The log-linear fit produces a slope $\hat{\sigma}_k$ and a coefficient of determination $R^2$:

$$
R^2 = 1 - \frac{\sum_n(\ln|a_k(t_n)| - (\alpha - \hat{\sigma}_k t_n))^2}{\sum_n(\ln|a_k(t_n)| - \overline{\ln|a_k|})^2},
$$

where $\alpha$ is the intercept. For a truly exponential decay: $R^2 \approx 1$ (perfect linear fit on the semilog scale). The acceptance criterion is:

$$
R^2 > 0.999.
$$

A fit with $R^2 < 0.999$ indicates that the decay is not purely exponential over the fitting interval, which may be caused by:

- **Nonlinear effects** ($A$ too large): the amplitude-dependent corrections modify the effective decay rate during the fit interval. Solution: reduce $A$ or narrow the fitting interval to the late-time phase.
- **Multi-mode contamination**: energy transferred from other modes (via the triad) contaminates mode $k$'s amplitude. Solution: increase the fitting interval's start time (to wait for the transferred energy to decay) or use a smaller initial amplitude.
- **Participation coupling** ($k = 0$ mode): the homogeneous mode is coupled to $v$ and may oscillate (in the Spiral Sheet). Its "decay rate" is the envelope rate $\gamma_0$, not a simple exponential. The fitting method must be adapted for oscillatory modes (§5.3.3.3).

##### 5.3.3.3 Decay Rate for Oscillatory Modes

The homogeneous mode ($k = 0$) in the oscillatory regime (Parameter Sets I, II, V) has the form:

$$
a_0(t) = C\,e^{-\gamma_0 t}\cos(\omega t + \phi),
$$

where $\gamma_0$ is the envelope decay rate and $\omega$ is the oscillation frequency. The log-linear fit of $\ln|a_0(t)|$ would produce a noisy line (because $|a_0|$ oscillates between local maxima and zero crossings). Two extraction methods are used:

**Envelope fitting.** Identify the local maxima of $|a_0(t)|$ (the peaks of the oscillation envelope). Fit $\ln(\text{peak amplitude})$ versus the peak times by linear regression. The slope is $-\hat{\gamma}_0$.

The local maxima are identified by the condition $|a_0(t_{n-1})| < |a_0(t_n)| > |a_0(t_{n+1})|$ on the sampled time series. For well-resolved oscillations ($\Delta t_{\mathrm{out}} \ll T_{\mathrm{osc}} = 2\pi/\omega$), this detects every peak.

**Zero-crossing frequency.** The oscillation frequency $\hat{\omega}$ is extracted from the zero crossings of $a_0(t)$. A zero crossing at time $t_{\mathrm{zc}}$ is detected when $a_0(t_n)\cdot a_0(t_{n+1}) < 0$; the crossing time is interpolated linearly: $t_{\mathrm{zc}} = t_n + \Delta t_{\mathrm{out}}\cdot|a_0(t_n)|/(|a_0(t_n)| + |a_0(t_{n+1})|)$. The half-period is $T_{1/2} = t_{\mathrm{zc},i+1} - t_{\mathrm{zc},i}$ (between consecutive crossings of the same sign), and the frequency is $\hat{\omega} = \pi/T_{1/2}$.

The measured frequency is averaged over all detected half-periods in the fitting interval to produce a single estimate $\hat{\omega}$. The standard deviation of the individual $T_{1/2}$ values provides an uncertainty estimate.

##### 5.3.3.4 Amplitude Ratio Extraction

For triad experiments (Atlas §4.2), the locked amplitude ratio $R_{31} = |a_3|/|a_1|$ is extracted from the time series of $|a_1(t)|$ and $|a_3(t)|$:

$$
R_{31}(t) = \frac{|a_3(t)|}{|a_1(t)|}.
$$

The quasi-steady value $\bar{R}_{31}$ is the time-average of $R_{31}(t)$ over the quasi-steady interval $[t_{\mathrm{onset}}, t_{\mathrm{end}}]$, where:

- $t_{\mathrm{onset}}$ is the time at which $|a_3(t)|$ first exceeds $10^{-6}$ (mode 3 has been generated by the triad).
- $t_{\mathrm{end}}$ is the time at which $|a_1(t)|$ drops below $10^{-6}$ (the source mode has decayed to the noise floor).

The standard deviation of $R_{31}(t)$ over the quasi-steady interval provides the uncertainty. For a well-locked triad, the standard deviation is $< 5\%$ of $\bar{R}_{31}$.

---

#### 5.3.4 Validation

##### 5.3.4.1 Parseval Check

The discrete Parseval identity must hold at every output step:

$$
\left|\;\|u^n\|_{L^2}^2 - \sum_{k=0}^{N_{\mathrm{obs}}-1}|a_k^n|^2 - E_{\mathrm{tail}}^n\;\right| < 10^{-10}\,\|u^n\|_{L^2}^2.
$$

The left-hand side is zero by construction (since $E_{\mathrm{tail}}$ is defined as the difference), so this check verifies that the DCT normalization is correct and that no energy is lost or gained in the transform.

For Method B (where the spectral coefficients are the state): the check reduces to $|\|u\|_{L^2}^2 - \sum_k|\hat{u}_k|^2| < 10^{-14}\|u\|_{L^2}^2$, which should hold to machine precision.

For Method A (where the DCT is applied post-hoc): the check verifies the DCT normalization. A failure indicates an incorrect normalization factor (§5.3.1.2, environment-specific table).

##### 5.3.4.2 Decay Rate Accuracy

For single-mode experiments at small amplitude ($A = 10^{-3}$, Atlas §3.1), the measured decay rate must match the analytic prediction:

$$
\frac{|\hat{\sigma}_k - D\alpha_k|}{D\alpha_k} < 0.01 \qquad (1\% \text{ tolerance}).
$$

This is the acceptance criterion of Validation Test 4 (Atlas §1.7.4). A failure indicates either an error in the time-stepping scheme (the mode is not decaying at the correct rate) or an error in the spectral decomposition (the DCT is assigning the wrong amplitude to mode $k$).

##### 5.3.4.3 Frequency Accuracy

For oscillatory parameter sets at small amplitude, the measured frequency must match the analytic prediction:

$$
\frac{|\hat{\omega} - \omega|}{|\omega|} < 0.01 \qquad (1\% \text{ tolerance}),
$$

where $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ is the analytic frequency from eq. C.15.

##### 5.3.4.4 Selection-Rule Compliance

For triad experiments (Atlas §4.1.4, Experiment 4.3), the modal amplitudes at modes not predicted by the selection rule must remain below the detection threshold:

$$
|a_k(t)| < 10^{-5} \qquad \text{for all } k \notin \{|m-n|, m+n, 2m, 2n, 0\},
$$

at every output step. A violation indicates aliasing (insufficient de-aliasing in Method B) or a numerical artifact in the nonlinear evaluation (Method A).

---

#### 5.3.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Basis** | Neumann eigenfunctions $\varphi_k(x) = c_k\cos(k\pi x/L)$ |
| **Transform** | DCT-I (Method A, post-hoc) or direct state access (Method B) |
| **Tracked modes** | $N_{\mathrm{obs}} = 16$–$64$ (experiment-dependent) |
| **Per-mode quantities** | $a_k$, $|a_k|$, $|a_k|^2$, $\mu_k|a_k|^2$, $\operatorname{sign}(a_k)$ |
| **Tail monitoring** | $E_{\mathrm{tail}}$ and $C_{\mathrm{tail}}$ via Parseval subtraction |
| **Purity monitoring** | $S_{\mathrm{purity}}$ for single-mode experiments |
| **Decay rate extraction** | Log-linear fit over $[t_{\mathrm{start}}, t_{\mathrm{end}}]$; $R^2 > 0.999$ |
| **Oscillatory mode extraction** | Envelope fitting (peaks) + zero-crossing frequency |
| **Amplitude ratio extraction** | Time-average of $R_{31}(t)$ over quasi-steady interval |
| **Key validation** | Parseval check, $1\%$ rate accuracy, $1\%$ frequency accuracy, selection-rule compliance |

The modal amplitudes are the most information-rich observable: from a single time series of $\{a_k(t)\}_{k=0}^{N_{\mathrm{obs}}}$, the engine extracts decay rates, frequencies, amplitude ratios, spectral purity, energy distribution, complexity, and triad-coupling verification. The spectral decomposition is the lens through which the architectural predictions of Appendix C become quantitatively testable.

---

### 5.4 Triad Coefficients

The nonlinear triad coupling (Principle 7) is encoded in the trilinear coupling coefficients $\Gamma_{mnk}$ (Appendix C.4, eq. C.26), which determine which pairs of modes $(m, n)$ transfer energy to which target mode $k$, at what rate, and with what amplitude ratio. The simulation engine computes these coefficients analytically, tracks the activation of triad-predicted modes during integration, and validates the selection rule (Theorem C.34) by comparing the observed spectral content to the predicted content. This subsection specifies all three components.

---

#### 5.4.1 Computing $\Gamma_{mnk}$

##### 5.4.1.1 Definition

The trilinear coupling coefficient is (eq. C.26):

$$
\Gamma_{mnk} := \int_\Omega \nabla\varphi_m(x) \cdot \nabla\varphi_n(x)\;\varphi_k(x)\,dx,
$$

where $\{\varphi_k\}$ are the Neumann eigenfunctions. This integral measures the strength of the interaction by which modes $m$ and $n$ (through the gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$) generate spectral content in mode $k$.

The coefficient has the following properties (Proposition C.33):

- **Symmetry in the source pair:** $\Gamma_{mnk} = \Gamma_{nmk}$.
- **Vanishing for the zero mode:** $\Gamma_{0nk} = \Gamma_{m0k} = 0$ for all $n, k$ (because $\nabla\varphi_0 = 0$).
- **Self-interaction:** $\Gamma_{nnk} = \int_\Omega|\nabla\varphi_n|^2\varphi_k\,dx \geq 0$ for $k = 0$.

##### 5.4.1.2 Closed-Form Evaluation on $\Omega_1 = [0, L]$

On the one-dimensional domain with Neumann eigenfunctions $\varphi_k(x) = c_k\cos(k\pi x/L)$ (where $c_0 = 1/\sqrt{L}$, $c_k = \sqrt{2/L}$ for $k \geq 1$), the coupling coefficients have the closed-form expressions of Theorem C.34.

The gradients are $\nabla\varphi_k(x) = -c_k(k\pi/L)\sin(k\pi x/L)$ for $k \geq 1$ and $\nabla\varphi_0 = 0$. The integral becomes:

$$
\Gamma_{mnk} = c_m c_n c_k\,\frac{mn\pi^2}{L^2}\int_0^L\sin\!\left(\frac{m\pi x}{L}\right)\sin\!\left(\frac{n\pi x}{L}\right)\cos\!\left(\frac{k\pi x}{L}\right)dx.
$$

The product-to-sum identity $\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)]$ reduces the integrand to a sum of cosine terms, and the orthogonality of cosines on $[0, L]$ selects the nonzero contributions.

**Result (Theorem C.34).** For $m, n \geq 1$:

$$
\Gamma_{mnk} \neq 0 \quad \Longleftrightarrow \quad k \in \{|m - n|,\; m + n\} \cup \{0 \text{ if } m = n\}.
$$

The explicit values are:

**Case $m \neq n$, $k = m + n \geq 1$:**

$$
\Gamma_{mn,m+n} = \frac{mn\pi^2}{L^2}\cdot\frac{c_m\,c_n}{c_{m+n}}\cdot\frac{L}{2} = \frac{mn\pi^2}{2L}\cdot\frac{c_m c_n}{c_{m+n}}.
$$

For $m, n \geq 1$ and $m + n \geq 1$ (always satisfied): $c_m = c_n = c_{m+n} = \sqrt{2/L}$, giving:

$$
\Gamma_{mn,m+n} = \frac{mn\pi^2}{2L}\cdot\frac{(\sqrt{2/L})^2}{\sqrt{2/L}} = \frac{mn\pi^2}{2L}\cdot\sqrt{\frac{2}{L}} = \frac{mn\pi^2\sqrt{2}}{2L^{3/2}}.
$$

**Case $m \neq n$, $k = |m - n| \geq 1$:**

$$
\Gamma_{mn,|m-n|} = \frac{mn\pi^2\sqrt{2}}{2L^{3/2}}.
$$

(Same magnitude as the sum-mode coefficient.)

**Case $m = n$, $k = 2m$:**

$$
\Gamma_{mm,2m} = \frac{m^2\pi^2}{L^2}\cdot\frac{c_m^2}{c_{2m}}\cdot\frac{L}{2} = \frac{m^2\pi^2}{2L}\cdot\frac{2/L}{\sqrt{2/L}} = \frac{m^2\pi^2\sqrt{2}}{2L^{3/2}}.
$$

**Case $m = n$, $k = 0$:**

$$
\Gamma_{mm,0} = \frac{m^2\pi^2}{L^2}\cdot\frac{c_m^2}{c_0}\cdot\frac{L}{2} = \frac{m^2\pi^2}{2L}\cdot\frac{2/L}{1/\sqrt{L}} = \frac{m^2\pi^2}{L^{3/2}}.
$$

**All other $k$:** $\Gamma_{mnk} = 0$.

##### 5.4.1.3 Precomputation and Storage

The coefficients $\Gamma_{mnk}$ depend only on the domain $\Omega$ and the mode indices $(m, n, k)$ — they are independent of the density, the canonical parameters, and the time. They are computed once at initialization and stored in a lookup structure.

**Storage structure.** Because the selection rule restricts the nonzero coefficients to $k \in \{|m-n|, m+n, 0\}$, the storage is sparse. For each source pair $(m, n)$ with $1 \leq m \leq n \leq N_{\mathrm{obs}}$, the engine stores at most three nonzero coefficients:

| Source pair | Target modes | Stored values |
|-----------|-------------|---------------|
| $(m, n)$ with $m < n$ | $k = n - m$, $k = m + n$ | $\Gamma_{mn,n-m}$, $\Gamma_{mn,m+n}$ |
| $(m, m)$ | $k = 0$, $k = 2m$ | $\Gamma_{mm,0}$, $\Gamma_{mm,2m}$ |

The total number of stored values is $\leq 2\binom{N_{\mathrm{obs}}}{2} + 2N_{\mathrm{obs}} = N_{\mathrm{obs}}(N_{\mathrm{obs}} + 1)$. At $N_{\mathrm{obs}} = 32$: $\leq 1056$ values ($\sim 8$ KB). At $N_{\mathrm{obs}} = 64$: $\leq 4160$ values ($\sim 33$ KB). The storage is negligible.

**Lookup interface.** The stored coefficients are accessed by a function:

$$
\texttt{Gamma}(m, n, k) \to \begin{cases} \Gamma_{mnk} & \text{if } k \in \{|m-n|, m+n\} \text{ or } (m = n, k = 0), \\ 0 & \text{otherwise}. \end{cases}
$$

The lookup is $O(1)$ (a direct table access indexed by the pair $(m, n)$ and the target type: sum, difference, or zero).

##### 5.4.1.4 Numerical Verification of the Closed Form

For the first few mode triples, the closed-form coefficients are verified against direct numerical quadrature of the defining integral (using adaptive quadrature with tolerance $10^{-12}$). This verification is performed once at initialization:

| Triple $(m, n, k)$ | Closed-form value | Quadrature value | Agreement |
|-------------------|------------------|-----------------|-----------|
| $(1, 1, 0)$ | $\pi^2/L^{3/2}$ | (computed) | $< 10^{-12}$ |
| $(1, 1, 2)$ | $\pi^2\sqrt{2}/(2L^{3/2})$ | (computed) | $< 10^{-12}$ |
| $(1, 2, 1)$ | $2\pi^2\sqrt{2}/(2L^{3/2})$ | (computed) | $< 10^{-12}$ |
| $(1, 2, 3)$ | $2\pi^2\sqrt{2}/(2L^{3/2})$ | (computed) | $< 10^{-12}$ |
| $(2, 3, 1)$ | $6\pi^2\sqrt{2}/(2L^{3/2})$ | (computed) | $< 10^{-12}$ |
| $(1, 1, 1)$ | $0$ (by selection rule) | (computed) | $< 10^{-14}$ |
| $(1, 2, 2)$ | $0$ (by selection rule) | (computed) | $< 10^{-14}$ |

The last two rows verify that coefficients predicted to vanish by the selection rule are indeed zero to machine precision. A nonzero value would indicate an error in the closed-form derivation or in the eigenbasis normalization.

##### 5.4.1.5 Two-Dimensional Coefficients

On $\Omega_2 = [0, L_x] \times [0, L_y]$, the coupling coefficients involve the tensor-product eigenfunctions $\varphi_{\mathbf{k}}(\mathbf{x}) = \varphi_{k_1}(x)\varphi_{k_2}(y)$:

$$
\Gamma_{\mathbf{m}\mathbf{n}\mathbf{k}} = \int_{\Omega_2}\nabla\varphi_{\mathbf{m}} \cdot \nabla\varphi_{\mathbf{n}}\;\varphi_{\mathbf{k}}\,dx\,dy.
$$

The gradient is $\nabla\varphi_{\mathbf{k}} = (\partial_x\varphi_{k_1}\cdot\varphi_{k_2},\;\varphi_{k_1}\cdot\partial_y\varphi_{k_2})$, so the dot product $\nabla\varphi_{\mathbf{m}}\cdot\nabla\varphi_{\mathbf{n}}$ separates into $x$- and $y$-contributions:

$$
\nabla\varphi_{\mathbf{m}}\cdot\nabla\varphi_{\mathbf{n}} = (\partial_x\varphi_{m_1})(\partial_x\varphi_{n_1})\varphi_{m_2}\varphi_{n_2} + \varphi_{m_1}\varphi_{n_1}(\partial_y\varphi_{m_2})(\partial_y\varphi_{n_2}).
$$

Each term factors into a product of 1D integrals, so the 2D coefficient is a sum of products of 1D coefficients and overlap integrals. The selection rules become richer: the mode triple $(\mathbf{m}, \mathbf{n}, \mathbf{k})$ has a nonzero coefficient when the 1D selection rules are satisfied in *each* coordinate independently, producing sum and difference combinations in each axis.

The 2D coefficients are computed by the product formula and stored in a sparse lookup indexed by the mode pairs $(\mathbf{m}, \mathbf{n})$. The Atlas uses 2D coefficients only for Experiment 3.7 (the 2D decay-rate funnel), where the triad structure is not the primary focus; the full 2D triad analysis is deferred to future extensions.

---

#### 5.4.2 Tracking Triad Activation

The simulation engine detects triad activation — the generation of spectral content in a mode $k$ that was initially at zero amplitude — by monitoring the modal amplitudes $\{a_k(t)\}$ at each output step.

##### 5.4.2.1 Activation Detection

A mode $k$ is classified as **activated** at time $t$ if:

$$
|a_k(t)| > \theta_{\mathrm{act}},
$$

where $\theta_{\mathrm{act}}$ is the activation threshold. The default is $\theta_{\mathrm{act}} = 10^{-5}$, chosen to lie between the second-order generation level ($O(A^2) \sim 10^{-3}$ for $A = 0.05$) and the third-order level ($O(A^3) \sim 10^{-4}$), ensuring that only the leading nonlinear products are counted as activated (§4.1.4 of the Atlas).

The activation status of each mode is a binary flag, updated at every output step. The first time a mode transitions from inactive ($|a_k| \leq \theta_{\mathrm{act}}$) to active ($|a_k| > \theta_{\mathrm{act}}$), the **activation time** $t_{\mathrm{act}}(k)$ is recorded.

##### 5.4.2.2 Activation Map

For a given integration with source modes $m$ and $n$, the activation map is the set of all activated target modes:

$$
\mathcal{A}(m, n) := \{k : |a_k(t)| > \theta_{\mathrm{act}} \text{ for some } t \in [0, T]\}.
$$

The selection rule predicts:

$$
\mathcal{A}_{\mathrm{pred}}(m, n) = \{|m - n|,\; m + n\} \cup \{0, 2m\} \cup \{0, 2n\},
$$

where the second and third sets arise from the self-interactions $m \otimes m$ and $n \otimes n$. The compliance check (§5.4.3) compares $\mathcal{A}(m, n)$ to $\mathcal{A}_{\mathrm{pred}}(m, n)$.

##### 5.4.2.3 Peak Amplitude and Timing

For each activated mode $k \in \mathcal{A}(m, n)$, the engine records:

| Quantity | Symbol | Definition |
|----------|--------|-----------|
| Peak amplitude | $a_k^{\max}$ | $\max_t|a_k(t)|$ |
| Peak time | $t_k^{\max}$ | $\arg\max_t|a_k(t)|$ |
| Activation time | $t_{\mathrm{act}}(k)$ | First $t$ with $|a_k| > \theta_{\mathrm{act}}$ |
| Late-time decay rate | $\hat{\sigma}_k$ | From log-linear fit after the peak (§5.3.3.1) |

The peak amplitude $a_k^{\max}$ is compared to the predicted scaling: for the sum mode $k = m + n$ generated at second order, $a_k^{\max} \sim |D\,M_*'\,\Gamma_{mn,m+n}|\,|a_m(0)\,a_n(0)|/D\alpha_k$ (the balance between the generation rate and the target-mode decay rate).

The late-time decay rate $\hat{\sigma}_k$ is compared to $D\alpha_k$: after the source modes have decayed and the generation has ceased, the target mode decays at its own rate $D\alpha_k$. Agreement confirms that the generated mode is a genuine eigenmode of the linearized operator, not a numerical artifact.

---

#### 5.4.3 Selection-Rule Validation

The selection rule (Theorem C.34) is the defining structural prediction of Principle 7: it specifies *exactly* which modes interact and which do not. The validation tests this prediction by exhaustive comparison across all tested mode pairs.

##### 5.4.3.1 Per-Pair Compliance Test

For each source pair $(m, n)$ in the experiment (Atlas §4.1.4 tests all 21 pairs with $1 \leq m \leq n \leq 6$), the engine evaluates:

**True positives.** Modes in $\mathcal{A}_{\mathrm{pred}}(m, n)$ that are also in $\mathcal{A}(m, n)$: predicted and observed. These confirm the selection rule.

**False negatives.** Modes in $\mathcal{A}_{\mathrm{pred}}(m, n)$ that are *not* in $\mathcal{A}(m, n)$: predicted but not observed. This can occur if the predicted mode's peak amplitude is below $\theta_{\mathrm{act}}$ (e.g., the mode $k = 0$ correction, which has amplitude $O(A^2/\sqrt{L})$ and may fall below $10^{-5}$ for small $A$). A false negative is not a selection-rule violation — it means the interaction exists but is too weak to detect at the given amplitude. The engine logs these as "below threshold" rather than as failures.

**False positives.** Modes *not* in $\mathcal{A}_{\mathrm{pred}}(m, n)$ that are in $\mathcal{A}(m, n)$: observed but not predicted. These are genuine selection-rule violations. A false positive indicates that mode $k$ has acquired amplitude $> \theta_{\mathrm{act}}$ through a mechanism not predicted by Theorem C.34.

**Pass criterion.** The per-pair test passes if and only if there are zero false positives:

$$
\mathcal{A}(m, n) \subseteq \mathcal{A}_{\mathrm{pred}}(m, n) \cup \mathcal{A}_{\mathrm{higher}}(m, n),
$$

where $\mathcal{A}_{\mathrm{higher}}(m, n)$ is the set of modes that can be generated at third or higher order (e.g., $k = m + 2n$ from the cascade $m \otimes n \to m + n$, then $(m + n) \otimes n \to m + 2n$). The higher-order modes are permitted as long as their peak amplitude is $O(A^3)$ or smaller — consistent with the third-order generation pathway.

In practice, the threshold $\theta_{\mathrm{act}} = 10^{-5}$ is set between $O(A^2)$ and $O(A^3)$ for $A = 0.03$ (the amplitude used in Experiment 4.3), so the higher-order modes fall below the threshold and are not activated. The test then reduces to: no mode outside $\mathcal{A}_{\mathrm{pred}}(m, n)$ exceeds $10^{-5}$.

##### 5.4.3.2 Compliance Matrix

The per-pair results are assembled into the **compliance matrix** (Atlas §4.1.4, Figure 4.3): a $K_{\mathrm{pairs}} \times N_{\mathrm{obs}}$ binary matrix where:

- Row $(m, n)$ corresponds to source pair $(m, n)$.
- Column $k$ corresponds to target mode $k$.
- Entry $(m,n,k) = 1$ (dark/filled) if mode $k$ was activated ($|a_k| > \theta_{\mathrm{act}}$ at some $t$).
- Entry $(m,n,k) = 0$ (light/empty) if mode $k$ was never activated.

The selection-rule prediction is overlaid as a symbol in each cell: a circle if $k \in \mathcal{A}_{\mathrm{pred}}(m, n)$, a cross otherwise.

**Global pass criterion.** The selection rule is validated if:

$$
\text{Every filled cell has a circle, and no cross-marked cell is filled.}
$$

Equivalently: the compliance matrix has no false positives. The Atlas reports (Experiment 4.3) state that this criterion is met for all 21 pairs tested.

##### 5.4.3.3 Quantitative Compliance: Generation Rate Comparison

Beyond the binary selection rule (which modes are activated), the engine compares the *magnitude* of the generated amplitudes to the predicted values from Proposition C.35:

**Predicted peak amplitude (sum mode $k = m + n$):**

$$
a_{m+n}^{\max,\mathrm{pred}} \approx \frac{|D\,M_*'\,\Gamma_{mn,m+n}|\,|a_m(0)|\,|a_n(0)|}{D\alpha_{m+n}}.
$$

This formula estimates the peak as the balance between the generation rate ($\propto |M_*'|\,|\Gamma|\,|a_m|\,|a_n|$) and the decay rate ($D\alpha_{m+n}$), reached at $t \approx 1/(D\alpha_{m+n})$.

**Comparison.** The engine computes the ratio $a_k^{\max}/a_k^{\max,\mathrm{pred}}$ for each activated mode. For $A \leq 0.05$ (weakly nonlinear regime): the ratio should be $1.0 \pm 0.2$ (within $20\%$, accounting for the $O(A^2)$ corrections to the linear decay rates). For $A > 0.1$ (moderately nonlinear): the ratio may deviate by up to $50\%$ due to the amplitude-dependent modifications of the source-mode decay rates and the higher-order cascade contributions.

The quantitative comparison is logged in the triad output record:

| Field | Type | Contents |
|-------|------|----------|
| `source_pair` | (Int, Int) | $(m, n)$ |
| `target_mode` | Int | $k$ |
| `Gamma_mnk` | Float64 | Precomputed coupling coefficient |
| `peak_amp_measured` | Float64 | $a_k^{\max}$ from the integration |
| `peak_amp_predicted` | Float64 | From the generation-decay balance formula |
| `ratio` | Float64 | Measured/predicted |
| `activation_time` | Float64 | $t_{\mathrm{act}}(k)$ |
| `peak_time` | Float64 | $t_k^{\max}$ |
| `decay_rate` | Float64 | $\hat{\sigma}_k$ (late-time) |
| `decay_rate_predicted` | Float64 | $D\alpha_k$ |

---

#### 5.4.4 Summary

| Aspect | Specification |
|--------|--------------|
| **Definition** | $\Gamma_{mnk} = \int_\Omega\nabla\varphi_m\cdot\nabla\varphi_n\;\varphi_k\,dx$ |
| **Selection rule** | $\Gamma_{mnk} \neq 0$ iff $k \in \{|m-n|, m+n\}$ (or $k = 0$ for $m = n$) |
| **Closed form (1D)** | $\Gamma_{mn,m+n} = mn\pi^2\sqrt{2}/(2L^{3/2})$ for $m \neq n$, $m,n \geq 1$ |
| **Storage** | Sparse: $\leq N_{\mathrm{obs}}(N_{\mathrm{obs}}+1)$ values; $O(1)$ lookup |
| **Precomputation** | Once at initialization; verified against numerical quadrature |
| **Activation detection** | $|a_k(t)| > \theta_{\mathrm{act}} = 10^{-5}$ |
| **Compliance matrix** | $K_{\mathrm{pairs}} \times N_{\mathrm{obs}}$ binary matrix; pass = zero false positives |
| **Quantitative check** | Peak-amplitude ratio (measured/predicted) within $20\%$ at $A \leq 0.05$ |
| **2D extension** | Product of 1D coefficients; richer selection rules |

The triad coefficients connect the architectural claim (Principle 7: the nonlinear term $M'(\rho)|\nabla\rho|^2$ generates specific inter-modal couplings) to a quantitatively testable prediction (the compliance matrix has no false positives, and the generated amplitudes match the coupling-coefficient formulas). The validation is exhaustive — every pair, every target mode, every amplitude — and binary: the selection rule either holds or it does not.

---

### 5.5 ED-Complexity $C_{\mathrm{ED}}$

The ED-complexity $C_{\mathrm{ED}}[\rho] = \int_\Omega|\nabla\rho|^2\,dx$ is the scalar measure that ranks configurations by their spatial gradient content and, through the dissipation bound (Lemma C.6), governs the rate at which the system loses energy. It is not merely a diagnostic — it is the bridge quantity between the mathematical architecture and the physical predictions of the Applications Paper (§1.4): decoherence rates, transport thresholds, and halo formation all scale with $C_{\mathrm{ED}}$, not with mass or size. The simulation engine computes $C_{\mathrm{ED}}$ at every output step, tracks its evolution over the full integration, and uses it in three diagnostic roles: as a dissipation-rate predictor, as a stability-basin indicator, and as the independent variable for the complexity sweeps of §4.2.

---

#### 5.5.1 Computation

The ED-complexity is the $L^2$-norm squared of the density gradient:

$$
C_{\mathrm{ED}}[\rho] = \int_\Omega|\nabla\rho(x)|^2\,dx = \|\nabla\rho\|_{L^2(\Omega)}^2.
$$

Since $\rho = \rho^* + u$ and $\nabla\rho^* = 0$, this is equivalently $C_{\mathrm{ED}} = \|\nabla u\|_{L^2}^2$.

##### 5.5.1.1 Method A: Finite-Difference Computation

The discrete gradient-squared array $(|\nabla_h\rho|^2)_j$ is computed during the operator evaluation (§2.3.2.1, Step 4b) and is available in the workspace at every time step. The ED-complexity is the trapezoidal-rule integral of this array:

**One dimension:**

$$
C_{\mathrm{ED}}^n = h\left[\frac{1}{2}(|\nabla_h\rho^n|^2)_0 + \sum_{j=1}^{N}(|\nabla_h\rho^n|^2)_j + \frac{1}{2}(|\nabla_h\rho^n|^2)_{N+1}\right].
$$

Since $(|\nabla_h\rho|^2)_0 = (|\nabla_h\rho|^2)_{N+1} = 0$ by the Neumann boundary condition (§1.3.1.1), the formula simplifies to:

$$
C_{\mathrm{ED}}^n = h\sum_{j=1}^{N}(|\nabla_h\rho^n|^2)_j.
$$

This is a single weighted summation over the interior grid points — $O(N)$ operations, using the array already computed for the operator evaluation.

**Two dimensions:**

$$
C_{\mathrm{ED}}^n = h_x h_y\sum_{i,j}(|\nabla_h\rho^n|^2)_{i,j},
$$

with the standard trapezoidal weights at the boundaries. The gradient-squared on the 2D grid is the sum of the two centered-difference components (§1.3.1.2).

**Accuracy.** The discrete $C_{\mathrm{ED}}$ approximates the continuous value to $O(h^2)$, matching the second-order accuracy of the spatial discretization. For smooth solutions, the error is typically $< 0.1\%$ at $N = 512$.

##### 5.5.1.2 Method B: Spectral Computation via Parseval

In spectral space, the ED-complexity is computed exactly (no spatial approximation) using the Parseval identity:

$$
C_{\mathrm{ED}}^n = \sum_{k=1}^{N_{\mathrm{modes}}-1}\mu_k\,|\hat{u}_k^n|^2,
$$

where $\mu_k = (k\pi/L)^2$ and $\hat{u}_k^n$ are the spectral coefficients of the density deviation. The $k = 0$ mode is excluded because $\nabla\varphi_0 = 0$ (the constant mode has no gradient content).

This formula is exact for the truncated spectral representation — it computes the gradient norm of the $N$-mode approximation with no quadrature error. The only error source is the spectral truncation: the unresolved modes $k \geq N$ contribute $C_{\mathrm{ED,tail}} = \sum_{k \geq N}\mu_k|\hat{u}_k|^2$, which is exponentially small for smooth solutions ($|\hat{u}_k| \sim e^{-ck}$, so $C_{\mathrm{ED,tail}} \sim N^2 e^{-2cN}$).

The spectral computation requires $N_{\mathrm{modes}} - 1$ multiplications and one summation — $O(N)$ operations. No transform is needed (the spectral coefficients are the primary state).

##### 5.5.1.3 Effective Complexity

The effective (dissipation-weighted) complexity (§6.3 of the Atlas) is:

$$
C_{\mathrm{ED}}^{\mathrm{eff}}[\rho] = \int_\Omega\frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx.
$$

**Method A:**

$$
C_{\mathrm{ED,eff}}^n = h\sum_{j=1}^{N}\frac{P'(\rho_j^n)}{M(\rho_j^n)}\,(|\nabla_h\rho^n|^2)_j.
$$

The constitutive values $P'(\rho_j)$ and $M(\rho_j)$ are available from the constitutive buffers (§1.2.6). The safeguarded evaluation (§1.6.6) prevents division by zero at near-horizon grid points.

**Method B:** The effective complexity cannot be computed in spectral space (the pointwise ratio $P'/M$ is density-dependent and does not diagonalize in the eigenbasis). It is computed pseudospectrally: transform $\hat{u}$ to physical space, evaluate $P'(\rho_j)/M(\rho_j) \cdot (|\nabla\rho_j|^2)$ pointwise, and integrate by the trapezoidal rule. This requires one inverse DCT plus one forward pass — $O(N\log N + N)$ operations.

**Amplification ratio.** The ratio $\mathcal{A}^n = C_{\mathrm{ED,eff}}^n / C_{\mathrm{ED}}^n$ is the instantaneous amplification factor. Near equilibrium: $\mathcal{A} \approx P_*'/M_* = 4.0$ (for the default parameters). Near the horizon: $\mathcal{A} \gg 1$ (the amplification diverges as $M(\rho) \to 0$, §6.3 of the Atlas).

---

#### 5.5.2 Temporal Evolution

The ED-complexity is tracked at every output step, producing a time series $\{C_{\mathrm{ED}}(t_n)\}_{n=0}^{N_{\mathrm{output}}}$ that is the basis for the complexity dynamics analysis of Atlas §5.

##### 5.5.2.1 Expected Behavior

The time evolution of $C_{\mathrm{ED}}(t)$ reflects the three stages of convergence (Theorem C.76):

**Stage I (Global bounds, $t \in [0, T_I]$).** $C_{\mathrm{ED}}$ may be non-monotone. The nonlinear triad (Principle 7) can transiently transfer energy into high modes, temporarily increasing $C_{\mathrm{ED}}$ (because $C_{\mathrm{ED}} = \sum\mu_k|a_k|^2$ weights the high modes more heavily). This transient increase is bounded: the energy monotonicity ($\mathcal{E}$ non-increasing) and the Poincaré inequality constrain $C_{\mathrm{ED}}$ to remain within $O(\mathcal{E}_0)$. The non-monotone phase, if present, is brief — it occurs during the harmonic cascade (Atlas §4.3) and resolves once the high modes are damped.

**Stage II (Algebraic convergence, $t \in [T_I, t_*]$).** $C_{\mathrm{ED}}$ decreases monotonically. The finite dissipation integral $\int_0^\infty C_{\mathrm{ED}}(t)\,dt < \infty$ (eq. C.81, via the bound $P'/M \geq c_\delta > 0$) and the Barbalat lemma give $C_{\mathrm{ED}}(t) \to 0$ (eq. C.85). The rate of decrease is algebraic — not exponential — for far-from-equilibrium initial data.

**Stage III (Exponential convergence, $t > t_*$).** $C_{\mathrm{ED}}$ decreases exponentially. The dominant contribution is from the surviving fundamental mode: $C_{\mathrm{ED}}(t) \approx \mu_1|a_1(t)|^2 \sim \mu_1|a_1(0)|^2 e^{-2D\alpha_1 t}$, giving an exponential decay rate of $2D\alpha_1$ for the complexity (twice the amplitude rate, because $C_{\mathrm{ED}} \propto |a_1|^2$).

**Single-mode special case.** For a single-mode initial condition $\rho_0 = \rho^* + A\cos(n\pi x/L)$, the complexity is exactly $C_{\mathrm{ED}}(t) = A^2\mu_n e^{-2D\alpha_n t}/2$ in the linearized regime — purely exponential from $t = 0$, with no Stages I or II.

##### 5.5.2.2 Derived Time-Series Quantities

From the $C_{\mathrm{ED}}(t)$ time series, the engine computes and logs:

| Quantity | Symbol | Formula | Purpose |
|----------|--------|---------|---------|
| Complexity decay rate | $\hat{\sigma}_{C}$ | Slope of $\ln C_{\mathrm{ED}}(t)$ over $[t_*, T]$ | Compare to $2D\alpha_1$ (linearized prediction) |
| Complexity half-life | $t_{1/2}^{C}$ | First $t$ with $C_{\mathrm{ED}}(t) = C_{\mathrm{ED}}(0)/2$ | Complexity-ordering observable (Atlas §5.3) |
| Dissipation predictor | $\hat{\mathcal{D}}_{\mathrm{pred}}$ | $D\,(P_*'/M_*)\,C_{\mathrm{ED}}(t)$ | Compare to $-d\mathcal{E}/dt$ (Lemma C.6 verification) |
| Complexity at $t_*$ | $C_{\mathrm{ED}}(t_*)$ | Interpolated from time series | Compare to $\epsilon_0^2$ (stability-basin boundary) |
| Peak complexity (if non-monotone) | $C_{\mathrm{ED}}^{\max}$ | $\max_t C_{\mathrm{ED}}(t)$ | Cascade amplitude diagnostic |
| Effective amplification | $\mathcal{A}(t)$ | $C_{\mathrm{ED}}^{\mathrm{eff}}(t)/C_{\mathrm{ED}}(t)$ | Near-horizon diagnostic (Atlas §6.3) |

##### 5.5.2.3 Spectral Decomposition of Complexity

The ED-complexity can be decomposed into per-mode contributions:

$$
C_{\mathrm{ED}}(t) = \sum_{k=1}^{N_{\mathrm{obs}}}\mu_k|a_k(t)|^2 + C_{\mathrm{tail}}(t),
$$

where $C_{\mathrm{tail}} = C_{\mathrm{ED}} - \sum_{k=1}^{N_{\mathrm{obs}}}\mu_k|a_k|^2$ is the unresolved tail contribution. The per-mode contributions $\mu_k|a_k|^2$ are already computed in the modal tracking (§5.3.2.1).

The spectral decomposition reveals which modes dominate the complexity at each time:

- At $t = 0$ (multi-mode IC): the complexity is distributed across the initialized modes, with high modes contributing disproportionately (because of the $\mu_k$ weighting).
- During the cascade phase: the complexity may temporarily shift to higher modes as the triad generates harmonics.
- At late times: the complexity is dominated by the fundamental mode ($k = 1$), which decays slowest.

The **spectral centroid of complexity** is

$$
\bar{k}_C(t) = \frac{\sum_k k\,\mu_k|a_k|^2}{\sum_k\mu_k|a_k|^2},
$$

which measures the "average mode number" weighted by complexity contribution. For a single-mode IC with mode $n$: $\bar{k}_C = n$ (constant). For a multi-mode IC: $\bar{k}_C$ starts high (the high modes contribute more to $C_{\mathrm{ED}}$ per unit energy) and decreases over time as the high modes decay faster, converging to $\bar{k}_C = 1$ when only the fundamental survives. The decrease of $\bar{k}_C$ over time is the spectral signature of the modal hierarchy: complexity is funneled from high to low mode numbers by the differential decay rates.

---

#### 5.5.3 Diagnostic Roles

The ED-complexity serves three distinct diagnostic roles in the simulation engine, beyond its recording as a time-series observable.

##### 5.5.3.1 Dissipation-Rate Predictor

The dissipation bound (Lemma C.6) states that the energy loss rate is bounded below by a multiple of $C_{\mathrm{ED}}$:

$$
-\frac{d\mathcal{E}}{dt} \geq D\,\frac{P_*'}{M_*}\,C_{\mathrm{ED}}(t) + O(\|\rho - \rho^*\|_{L^\infty}\,C_{\mathrm{ED}}).
$$

The leading term $D\,P_*'/M_*\cdot C_{\mathrm{ED}}$ provides a lower bound on the instantaneous dissipation rate. The engine computes this bound at every output step and records it alongside the actual dissipation rate $-(\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t$. The ratio

$$
\eta_{\mathrm{diss}}(t) = \frac{-d\mathcal{E}/dt}{D\,(P_*'/M_*)\,C_{\mathrm{ED}}(t)}
$$

should be $\geq 1$ (the actual dissipation exceeds the complexity-based lower bound) for all $t$. Near equilibrium: $\eta_{\mathrm{diss}} \to 1 + O(\|u\|)$ (the bound becomes tight). Far from equilibrium: $\eta_{\mathrm{diss}} > 1$ (the penalty and participation channels contribute additional dissipation beyond the gradient channel alone).

A violation $\eta_{\mathrm{diss}} < 1$ would indicate an error in the energy computation or the $C_{\mathrm{ED}}$ computation (one is inconsistent with the other). The engine logs a warning if $\eta_{\mathrm{diss}} < 0.9$ at any output step (the $0.9$ threshold allows for the $O(\Delta t^p)$ truncation error in the discrete energy rate).

##### 5.5.3.2 Stability-Basin Indicator

The stability threshold $\epsilon_0$ (Theorem C.43) is defined in terms of $\|u\|_{H^s} + |w|$. The $H^1$-component of this norm includes $\|\nabla u\|_{L^2}^2 = C_{\mathrm{ED}}$, so the condition $\|u\|_{H^1}^2 + |w|^2 < \epsilon_0^2$ includes $C_{\mathrm{ED}} < \epsilon_0^2 - \|u\|_{L^2}^2 - |w|^2$.

The engine tracks the **basin-entry indicator**:

$$
\mathcal{B}(t) = \frac{\|u(t)\|_{H^1}^2 + |v(t)|^2}{\epsilon_0^2},
$$

where $\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + C_{\mathrm{ED}}$ and $\epsilon_0$ is computed from the canonical parameters at initialization (§2.1.1, using the formula $\epsilon_0 = \gamma_*/C_{\mathrm{nl}}$ with $\gamma_*$ from eq. C.48 and $C_{\mathrm{nl}}$ estimated from the constitutive curvature). The transition time $t_*$ (§7.4 of the Atlas) is the first time at which $\mathcal{B}(t) < 1$.

For $\mathcal{B}(t) > 1$: the solution is outside the exponential basin (Stages I–II). For $\mathcal{B}(t) < 1$: the solution is inside the basin (Stage III), and the Lyapunov functional decays exponentially. The crossing of $\mathcal{B} = 1$ is the dynamical event that defines $t_*$.

The engine records $\mathcal{B}(t)$ at every output step and flags the crossing in the diagnostic log. For experiments that target the three-stage convergence (Atlas §7), the basin-entry time $t_*$ is the primary scalar observable.

##### 5.5.3.3 Complexity-Ordering Diagnostic

The complexity sweeps of §4.2 compare systems with different initial $C_{\mathrm{ED}}$ to verify the prediction that complexity orders the dynamical behavior. The engine provides a convenience function that, given two time series from different sweep points, computes the **ordering verification**:

- **Decay-rate ordering:** Is $\hat{\sigma}_{C}^{(1)} < \hat{\sigma}_{C}^{(2)}$ whenever $C_{\mathrm{ED}}^{(1)}(0) < C_{\mathrm{ED}}^{(2)}(0)$? (Higher initial complexity should produce faster complexity decay.)
- **Half-life ordering:** Is $t_{1/2}^{(1)} > t_{1/2}^{(2)}$ whenever $C_{\mathrm{ED}}^{(1)}(0) < C_{\mathrm{ED}}^{(2)}(0)$? (Lower initial complexity should produce longer half-life.)
- **Dissipation-rate ordering:** Is $(-d\mathcal{E}/dt)^{(1)} < (-d\mathcal{E}/dt)^{(2)}$ at $t = 0$ whenever $C_{\mathrm{ED}}^{(1)}(0) < C_{\mathrm{ED}}^{(2)}(0)$? (Higher initial complexity should produce faster initial dissipation.)

All three orderings should hold for any pair of sweep points that differ only in $C_{\mathrm{ED}}(0)$ (same parameters, same mode structure, different amplitude or mode number). A violation of any ordering would challenge the complexity-ordering principle — the claim that $C_{\mathrm{ED}}$, not mass or size, determines the dynamical fate.

---

#### 5.5.4 Logging

The ED-complexity and its derived quantities are recorded at two levels:

**Output-step record** (in the `Observables` record, §1.2.8):

| Field | Value |
|-------|-------|
| `C_ED` | $C_{\mathrm{ED}}^n = \|\nabla u^n\|_{L^2}^2$ |
| `C_ED_eff` | $C_{\mathrm{ED,eff}}^n = \int(P'/M)|\nabla\rho^n|^2\,dx$ |

**Derived fields** (computed from the above and other observables):

| Field | Formula |
|-------|---------|
| `amplification` | $C_{\mathrm{ED,eff}}^n / C_{\mathrm{ED}}^n$ |
| `diss_predictor` | $D\,(P_*'/M_*)\,C_{\mathrm{ED}}^n$ |
| `diss_ratio` | $(-d\mathcal{E}/dt) / (D\,(P_*'/M_*)\,C_{\mathrm{ED}}^n)$ |
| `basin_indicator` | $(\|u^n\|_{L^2}^2 + C_{\mathrm{ED}}^n + |v^n|^2)/\epsilon_0^2$ |
| `spectral_centroid_C` | $\sum_k k\mu_k|a_k|^2 / \sum_k\mu_k|a_k|^2$ |

**Post-integration summary** (in the experiment's output metadata):

| Field | Value |
|-------|-------|
| `C_ED_initial` | $C_{\mathrm{ED}}(0)$ |
| `C_ED_final` | $C_{\mathrm{ED}}(T)$ |
| `C_ED_half_life` | $t_{1/2}^C$ (or "N/A" if $C_{\mathrm{ED}}$ did not halve during $[0, T]$) |
| `C_ED_decay_rate` | $\hat{\sigma}_C$ (late-time slope) |
| `C_ED_peak` | $\max_t C_{\mathrm{ED}}(t)$ (if non-monotone) |
| `basin_entry_time` | $t_*$ (first $t$ with $\mathcal{B} < 1$; "N/A" if always inside or never entered) |

---

#### 5.5.5 Validation

##### 5.5.5.1 Parseval Consistency

For Method B, the spectral computation $C_{\mathrm{ED}} = \sum\mu_k|\hat{u}_k|^2$ and the physical-space computation $C_{\mathrm{ED}} = h\sum(|\nabla_h\rho|^2)_j$ (applied to the pseudospectral grid) must agree to machine precision:

$$
\left|\sum_{k=1}^{N-1}\mu_k|\hat{u}_k|^2 - h\sum_j(|\nabla_h\rho|^2)_j\right| < 10^{-12}\,\sum_{k=1}^{N-1}\mu_k|\hat{u}_k|^2.
$$

For Method A, this check is not applicable (no spectral state is available), but the spatial computation is verified by the convergence study (§2.7.1): the discrete $C_{\mathrm{ED}}$ converges to the continuous value at $O(h^2)$.

##### 5.5.5.2 Analytic Value at $t = 0$

For the standard initial conditions with known $C_{\mathrm{ED}}(0)$ (§4.2.1, tables):

$$
|C_{\mathrm{ED}}^{\mathrm{computed}}(0) - C_{\mathrm{ED}}^{\mathrm{analytic}}(0)| < 10^{-6}\,C_{\mathrm{ED}}^{\mathrm{analytic}}(0).
$$

The tolerance $10^{-6}$ accounts for the $O(h^2)$ spatial discretization error at $N = 512$ ($h^2 \approx 3.8 \times 10^{-6}$). For Method B: the tolerance tightens to $10^{-12}$ (spectral accuracy).

##### 5.5.5.3 Dissipation Bound Compliance

At every output step:

$$
\eta_{\mathrm{diss}}(t) = \frac{-(\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t}{D\,(P_*'/M_*)\,C_{\mathrm{ED}}^n} \geq 0.9.
$$

The threshold $0.9$ (rather than $1.0$) allows for the truncation error in the discrete energy rate. A persistent violation ($\eta_{\mathrm{diss}} < 0.9$ for more than $10$ consecutive output steps) indicates a systematic inconsistency between the energy and complexity computations.

##### 5.5.5.4 Single-Mode Decay Rate

For a single-mode initial condition at small amplitude ($A = 10^{-3}$, mode $n$):

$$
\left|\hat{\sigma}_C - 2D\alpha_n\right| / (2D\alpha_n) < 0.01,
$$

where $\hat{\sigma}_C$ is the measured complexity decay rate (from the log-linear fit of $C_{\mathrm{ED}}(t)$) and $2D\alpha_n$ is the predicted rate (twice the amplitude rate, because $C_{\mathrm{ED}} \propto |a_n|^2$). This is equivalent to the modal decay-rate check of §5.3.4.2 but applied to the aggregate complexity rather than the individual modal amplitude.

---

#### 5.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Definition** | $C_{\mathrm{ED}} = \int_\Omega|\nabla\rho|^2\,dx = \|\nabla u\|_{L^2}^2$ |
| **Method A computation** | Trapezoidal rule on $(|\nabla_h\rho|^2)_j$; $O(N)$ |
| **Method B computation** | Parseval: $\sum\mu_k|\hat{u}_k|^2$; $O(N)$, exact for truncated basis |
| **Effective complexity** | $C_{\mathrm{ED}}^{\mathrm{eff}} = \int(P'/M)|\nabla\rho|^2\,dx$; pseudospectral for Method B |
| **Temporal behavior** | Non-monotone (Stage I cascade), monotone decreasing (Stage II), exponential (Stage III) |
| **Diagnostic: dissipation predictor** | $D(P_*'/M_*)C_{\mathrm{ED}}$ lower-bounds $-d\mathcal{E}/dt$ |
| **Diagnostic: basin indicator** | $\mathcal{B} = (\|u\|_{H^1}^2 + |v|^2)/\epsilon_0^2$; crossing $\mathcal{B} = 1$ defines $t_*$ |
| **Diagnostic: ordering** | Higher $C_{\mathrm{ED}}(0) \Rightarrow$ faster decay, shorter half-life, higher dissipation |
| **Key validation** | Parseval consistency, analytic IC value, dissipation bound, single-mode rate |

ED-complexity is the unifying observable of the ED architecture. It connects the mathematical infrastructure (the dissipation bound, the stability threshold, the modal hierarchy) to the physical predictions (complexity-ordered decoherence, transport thresholds, halo formation) through a single, computable scalar. Every experiment in the Atlas measures it; every physical prediction of the Applications Paper is expressed in terms of it.

---

### 5.6 Convergence Rate $\sigma$

The convergence rate — the exponential decay rate at which the solution approaches the equilibrium $(\rho^*, 0)$ — is the single scalar that distills the long-time dynamics of the ED system into a testable number. The analytic theory provides two rates: the spectral gap $\gamma$ (Corollary C.18, Lemma C.31), which governs the linearized semigroup decay, and the Lyapunov rate $\gamma_*$ (eq. C.48), which governs the nonlinear stability. The simulation engine extracts a measured rate $\hat{\sigma}$ from the numerical solution and compares it to both analytic predictions. This subsection specifies the extraction methodology, the fitting procedures, and the validation protocol.

---

#### 5.6.1 Definitions: What Is Being Measured

The ED system has multiple decay rates, each associated with a different norm and a different component of the solution. The simulation engine extracts four distinct rates, corresponding to the four observables most directly connected to the analytic theory.

##### 5.6.1.1 Modal Decay Rate $\hat{\sigma}_k$

**Definition.** The rate at which the amplitude of spatial mode $k$ decreases:

$$
|a_k(t)| \sim C_k\,e^{-\hat{\sigma}_k t} \qquad \text{for } t \gg 0.
$$

**Analytic prediction.** For $k \geq 1$: $\hat{\sigma}_k = D\alpha_k = D(M_*\mu_k + P_*')$ (eq. C.11). For $k = 0$ (homogeneous mode): $\hat{\sigma}_0 = \gamma_0 = \frac{1}{2}(DP_*' + \zeta/\tau)$ in the oscillatory regime, or $\hat{\sigma}_0 = \gamma_0 - \frac{1}{2}\sqrt{\mathscr{D}_0}$ (the slow eigenvalue) in the overdamped regime.

**When to use.** Modal decay rates are the primary observables for the modal hierarchy (Atlas §3), the spectral gap (Atlas §3.2), and the linearized comparison (Atlas §1.7.4). They are extracted from single-mode or few-mode experiments at small amplitude.

##### 5.6.1.2 Lyapunov Decay Rate $\hat{\sigma}_{\mathcal{V}}$

**Definition.** The rate at which the Lyapunov functional $\mathcal{V}[u, w]$ (Definition C.39) decreases:

$$
\mathcal{V}(t) \sim C_\mathcal{V}\,e^{-\hat{\sigma}_{\mathcal{V}} t} \qquad \text{for } t > t_*.
$$

**Analytic prediction.** $\hat{\sigma}_{\mathcal{V}} = \gamma_*$ (eq. C.48), the Lyapunov rate from the nonlinear stability theorem (Theorem C.43). Since $\mathcal{V}$ is a quadratic functional of $(u, w)$, the rate $\hat{\sigma}_{\mathcal{V}}$ corresponds to twice the amplitude rate: $\hat{\sigma}_{\mathcal{V}} = 2\gamma$ in the linearized regime (where $\gamma$ is the spectral gap).

**When to use.** The Lyapunov rate is the primary observable for the three-stage convergence (Atlas §7) and the stability threshold (Atlas §5.2). It is extracted from the late-time phase of integrations that begin far from equilibrium.

##### 5.6.1.3 Envelope Decay Rate $\hat{\gamma}_0$

**Definition.** For oscillatory parameter sets (Spiral Sheet), the homogeneous mode oscillates with a decaying envelope:

$$
|a_0(t)| \leq C_0\,e^{-\hat{\gamma}_0 t}.
$$

The envelope rate $\hat{\gamma}_0$ is the decay rate of the oscillation peaks, not the instantaneous rate (which oscillates between positive and negative values as $a_0$ passes through zero).

**Analytic prediction.** $\hat{\gamma}_0 = \gamma_0 = \frac{1}{2}(DP_*' + \zeta/\tau)$ (the real part of the complex eigenvalues $\lambda_\pm$).

**When to use.** The envelope rate is the primary observable for the regime geometry (Atlas §2.1) and the regime transitions (Atlas §8.1). It is extracted by peak fitting (§5.3.3.3).

##### 5.6.1.4 Instantaneous Rate $\hat{\beta}(t)$

**Definition.** The time-dependent rate at which the Lyapunov functional decreases at time $t$:

$$
\hat{\beta}(t) = -\frac{d\ln\mathcal{V}}{dt} = -\frac{1}{\mathcal{V}}\frac{d\mathcal{V}}{dt}.
$$

This is not a constant — it varies as the solution traverses the three stages of convergence. At early times (Stage I): $\hat{\beta}$ is large (the fast spatial modes contribute strong dissipation). At intermediate times (Stage II): $\hat{\beta}$ settles to a lower value (the algebraic-phase rate). At late times (Stage III): $\hat{\beta}$ converges to the asymptotic rate $\gamma_*$.

**Analytic prediction.** $\hat{\beta}(t) \to \gamma_*$ as $t \to \infty$ (Theorem C.72). The approach may be monotonic (in the Monotonic Cone) or oscillatory (in the Spiral Sheet, where $\hat{\beta}$ oscillates around $\gamma_*$ with decreasing amplitude).

**When to use.** The instantaneous rate is the primary observable for identifying the transition time $t_*$ (Atlas §7.4): $t_*$ is the first time at which $\hat{\beta}(t)$ reaches $90\%$ of its asymptotic value.

---

#### 5.6.2 Extraction Methods

Each rate requires a specific fitting procedure, matched to the character of the underlying signal.

##### 5.6.2.1 Log-Linear Fitting for $\hat{\sigma}_k$ and $\hat{\sigma}_{\mathcal{V}}$

For a quantity $Q(t)$ that decays exponentially ($Q(t) = Q_0 e^{-\sigma t}$), the decay rate is the negative slope of $\ln Q(t)$ versus $t$. The fitting procedure is:

1. **Select the fitting interval** $[t_a, t_b]$.
   - For $\hat{\sigma}_k$: $t_a = 0.1$ (skip startup transient), $t_b = \min(T - 0.5,\; t_{\mathrm{floor}}(k))$ where $t_{\mathrm{floor}}$ is the time $|a_k|$ drops below $10^{-10}$.
   - For $\hat{\sigma}_{\mathcal{V}}$: $t_a = t_* + 1$ (begin well inside the exponential basin), $t_b = T$ (use all available late-time data).

2. **Extract the data.** Collect $\{(t_n, \ln Q(t_n))\}$ at all output steps within $[t_a, t_b]$.

3. **Perform least-squares regression.** Fit $\ln Q = \alpha - \sigma t$ (a straight line on the semilog plot) by minimizing $\sum_n(\ln Q(t_n) - \alpha + \sigma t_n)^2$ over $(\alpha, \sigma)$.

4. **Extract the rate.** The fitted slope is $\hat{\sigma} = \sigma$ (positive, since $Q$ is decreasing).

5. **Assess the fit quality.** Compute $R^2$. Accept if $R^2 > 0.999$ (§5.3.3.2).

6. **Compute the uncertainty.** The standard error of the slope is

$$
\delta\hat{\sigma} = \sqrt{\frac{\sum_n(\ln Q_n - \alpha + \hat{\sigma} t_n)^2}{(N_{\mathrm{fit}} - 2)\sum_n(t_n - \bar{t})^2}},
$$

where $N_{\mathrm{fit}}$ is the number of data points and $\bar{t}$ is their mean. This provides an error bar on $\hat{\sigma}$.

##### 5.6.2.2 Envelope Fitting for $\hat{\gamma}_0$

For oscillatory modes (§5.3.3.3):

1. **Detect peaks.** Identify the local maxima of $|a_0(t)|$: times $t_p^{(i)}$ where $|a_0(t_{n-1})| < |a_0(t_n)| > |a_0(t_{n+1})|$. The peak amplitudes are $A_p^{(i)} = |a_0(t_p^{(i)})|$.

2. **Fit the envelope.** Apply the log-linear fitting procedure (§5.6.2.1) to the peak sequence $\{(t_p^{(i)}, \ln A_p^{(i)})\}$. The fitted slope is $\hat{\gamma}_0$.

3. **Quality check.** Require at least $4$ detected peaks in the fitting interval (to ensure a robust fit). Require $R^2 > 0.99$ (the tolerance is relaxed relative to §5.6.2.1 because the peak detection introduces timing jitter of $O(\Delta t_{\mathrm{out}})$).

##### 5.6.2.3 Instantaneous Rate via Finite Differences for $\hat{\beta}(t)$

The instantaneous rate $\hat{\beta}(t) = -d\ln\mathcal{V}/dt$ is computed by centered finite differences on the time series:

$$
\hat{\beta}(t_n) = -\frac{\ln\mathcal{V}(t_{n+1}) - \ln\mathcal{V}(t_{n-1})}{t_{n+1} - t_{n-1}}.
$$

The centered difference avoids the half-step offset of the forward or backward difference and is second-order accurate in the output interval $\Delta t_{\mathrm{out}} = k_{\mathrm{out}}\Delta t$.

At the first and last output steps, one-sided differences are used:

$$
\hat{\beta}(t_0) = -\frac{\ln\mathcal{V}(t_1) - \ln\mathcal{V}(t_0)}{t_1 - t_0}, \qquad \hat{\beta}(t_{N_{\mathrm{out}}}) = -\frac{\ln\mathcal{V}(t_{N_{\mathrm{out}}}) - \ln\mathcal{V}(t_{N_{\mathrm{out}}-1})}{t_{N_{\mathrm{out}}} - t_{N_{\mathrm{out}}-1}}.
$$

**Smoothing.** The raw $\hat{\beta}(t)$ may oscillate (especially in the Spiral Sheet, where $\mathcal{V}$ has an oscillatory component superimposed on the exponential decay). For the transition-time extraction, the engine applies a running average over a window of width $T_{\mathrm{smooth}} = 2\pi/\omega$ (one oscillation period) to smooth out the oscillatory fluctuations:

$$
\hat{\beta}_{\mathrm{smooth}}(t_n) = \frac{1}{|\mathcal{W}_n|}\sum_{j \in \mathcal{W}_n}\hat{\beta}(t_j),
$$

where $\mathcal{W}_n = \{j : |t_j - t_n| \leq T_{\mathrm{smooth}}/2\}$ is the set of output steps within the smoothing window. For monotonic parameter sets ($\omega = 0$): no smoothing is needed ($T_{\mathrm{smooth}} = 0$, the raw $\hat{\beta}$ is used directly).

##### 5.6.2.4 Asymptotic Rate Extraction

The asymptotic (late-time) convergence rate $\hat{\sigma}_\infty$ is the limit of $\hat{\beta}(t)$ as $t \to T$. It is computed as the time-average of the smoothed instantaneous rate over the final portion of the integration:

$$
\hat{\sigma}_\infty = \frac{1}{T - t_{\mathrm{avg}}}\int_{t_{\mathrm{avg}}}^{T}\hat{\beta}_{\mathrm{smooth}}(t)\,dt \approx \frac{1}{|\mathcal{W}_{\mathrm{avg}}|}\sum_{n \in \mathcal{W}_{\mathrm{avg}}}\hat{\beta}_{\mathrm{smooth}}(t_n),
$$

where $t_{\mathrm{avg}} = T - 5$ is the start of the averaging window (the last $5$ time units). The standard deviation over the averaging window provides the uncertainty:

$$
\delta\hat{\sigma}_\infty = \sqrt{\frac{1}{|\mathcal{W}_{\mathrm{avg}}|}\sum_{n \in \mathcal{W}_{\mathrm{avg}}}(\hat{\beta}_{\mathrm{smooth}}(t_n) - \hat{\sigma}_\infty)^2}.
$$

For a cleanly converged run (the solution is well inside the exponential basin by $t = T - 5$): $\delta\hat{\sigma}_\infty < 0.01\,\hat{\sigma}_\infty$ (the rate is constant to within $1\%$ over the averaging window).

---

#### 5.6.3 Validation Against Appendix C

The extracted rates are compared to the analytic predictions of Appendix C at three levels: individual eigenvalues, the spectral gap, and the Lyapunov rate.

##### 5.6.3.1 Individual Eigenvalue Comparison

For each spatial mode $k = 1, 2, \ldots$ at small amplitude ($A = 10^{-3}$):

$$
\frac{|\hat{\sigma}_k - D\alpha_k|}{D\alpha_k} < 0.01.
$$

The predicted values $D\alpha_k = D(M_*\mu_k + P_*')$ are computed from the precomputed parameter record (§1.1.3). This is Validation Test 4 (Atlas §1.7.4, Experiment 1.4).

For the homogeneous mode at small amplitude:

- **Oscillatory regime:** $|\hat{\gamma}_0 - \gamma_0|/\gamma_0 < 0.01$ and $|\hat{\omega} - \omega|/\omega < 0.01$.
- **Overdamped regime:** $|\hat{\sigma}_0 - |\lambda_+||/|\lambda_+| < 0.01$, where $\lambda_+ = -\gamma_0 + \frac{1}{2}\sqrt{\mathscr{D}_0}$ is the slow eigenvalue (eq. C.15).
- **Critical regime:** the measured rate should approach $\gamma_0$ with an algebraic correction from the Jordan block — the $R^2$ of the log-linear fit may be below $0.999$ (the decay is not purely exponential), and the measured rate may differ from $\gamma_0$ by up to $10\%$ due to the polynomial prefactor $(1 + c_2 t)$.

##### 5.6.3.2 Spectral Gap Comparison

The spectral gap $\gamma = \min(\gamma_{\mathrm{hom}}, \gamma_{\mathrm{sp}})$ (Lemma C.31) is compared to the measured slowest rate:

$$
\hat{\gamma} = \min(\hat{\sigma}_0, \hat{\sigma}_1),
$$

where $\hat{\sigma}_0$ is the homogeneous-mode rate (§5.6.1.1 or §5.6.1.3) and $\hat{\sigma}_1$ is the first spatial-mode rate (§5.6.1.1). The comparison is:

$$
\frac{|\hat{\gamma} - \gamma|}{\gamma} < 0.02.
$$

The $2\%$ tolerance (wider than the $1\%$ per-mode tolerance) allows for the interaction between the homogeneous and first spatial modes, which at finite amplitude produces a small correction to both rates.

The spectral gap determines the dominant time scale of the linearized dynamics: the slowest-decaying component (whichever of mode $0$ or mode $1$ has the smaller rate) persists longest and dominates the late-time solution. The comparison confirms that the engine correctly identifies which mode controls the spectral gap.

**Gap classification check.** The engine verifies that the analytic gap classification matches the numerical observation:

| Analytic classification | Condition | Numerical check |
|------------------------|-----------|-----------------|
| Gap controlled by homogeneous mode | $\gamma_{\mathrm{hom}} < \gamma_{\mathrm{sp}}$ | $\hat{\sigma}_0 < \hat{\sigma}_1$ |
| Gap controlled by spatial mode | $\gamma_{\mathrm{hom}} > \gamma_{\mathrm{sp}}$ | $\hat{\sigma}_0 > \hat{\sigma}_1$ |
| Gap marginally controlled | $|\gamma_{\mathrm{hom}} - \gamma_{\mathrm{sp}}| < 0.05\gamma$ | Either ordering permitted |

For all five canonical parameter sets, $\gamma_{\mathrm{hom}} < \gamma_{\mathrm{sp}}$ (the homogeneous mode is always the slowest; see the table in Atlas §7.3.3). The gap classification check confirms this.

##### 5.6.3.3 Lyapunov Rate Comparison

The asymptotic Lyapunov rate $\hat{\sigma}_\infty$ (§5.6.2.4) is compared to the predicted rate $\gamma_*$ (eq. C.48):

$$
\frac{|\hat{\sigma}_\infty - \gamma_*|}{\gamma_*} < 0.05.
$$

The $5\%$ tolerance is wider than the eigenvalue tolerances because the Lyapunov rate $\gamma_*$ is a *constructed* quantity (it depends on the choice of the coupling parameter $\sigma$ in the Lyapunov functional and on the coercivity constants $c_\pm$), not a spectral quantity. The measured $\hat{\sigma}_\infty$ may differ from the theoretical $\gamma_*$ by the gap between the Lyapunov bound and the actual decay rate, which is non-negative but may be nonzero.

In practice, the measured asymptotic rate is close to $2\gamma = 2\min(\gamma_{\mathrm{hom}}, \gamma_{\mathrm{sp}})$ (twice the spectral gap), which is the rate at which $\mathcal{V} \propto \|u\|_{H^1}^2 + |v|^2$ decays when the solution is dominated by the slowest mode. The Lyapunov rate $\gamma_*$ from eq. C.48 is a *lower bound* on the actual rate; the measured rate may exceed it.

##### 5.6.3.4 Cross-Parameter-Set Comparison

The five canonical parameter sets have different predicted rates. The engine verifies that the ordering of the measured rates matches the predicted ordering:

| Predicted ordering (from Atlas §7.3.3) | Check |
|----------------------------------------|-------|
| $\hat{\sigma}_\infty^{\mathrm{I}} < \hat{\sigma}_\infty^{\mathrm{V}} < \hat{\sigma}_\infty^{\mathrm{II}} < \hat{\sigma}_\infty^{\mathrm{III}} < \hat{\sigma}_\infty^{\mathrm{IV}}$ | All five inequalities hold |

This ordering reflects the increasing total damping from Set I (smallest $D$ and $\zeta$) to Set IV (largest $D$ and $\zeta$). The ordering check is a single comparison across five scalar values; it does not require per-mode analysis and serves as a quick sanity check that the parameter dependence is qualitatively correct.

---

#### 5.6.4 Logging

The convergence-rate observables are recorded in the experiment's output:

**Per-mode rates** (in the spectral log, §2.4.2):

| Field | Value |
|-------|-------|
| `sigma_k` | Array of $\hat{\sigma}_k$ for $k = 0, 1, \ldots, N_{\mathrm{obs}} - 1$ |
| `sigma_k_predicted` | Array of $D\alpha_k$ (analytic) |
| `sigma_k_error` | Array of $|\hat{\sigma}_k - D\alpha_k|/D\alpha_k$ (relative error) |
| `sigma_k_R2` | Array of fit $R^2$ values |

**Envelope rate** (for oscillatory parameter sets):

| Field | Value |
|-------|-------|
| `gamma_0_hat` | $\hat{\gamma}_0$ (envelope decay rate) |
| `gamma_0_predicted` | $\gamma_0 = \frac{1}{2}(DP_*' + \zeta/\tau)$ |
| `omega_hat` | $\hat{\omega}$ (oscillation frequency) |
| `omega_predicted` | $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ |
| `n_peaks` | Number of detected peaks used in the envelope fit |

**Lyapunov and instantaneous rates** (in the time-series output):

| Field | Value |
|-------|-------|
| `beta_instantaneous` | $\hat{\beta}(t_n)$ at each output step |
| `beta_smoothed` | $\hat{\beta}_{\mathrm{smooth}}(t_n)$ (after running average) |
| `sigma_asymptotic` | $\hat{\sigma}_\infty$ (late-time average) |
| `sigma_asymptotic_std` | $\delta\hat{\sigma}_\infty$ (uncertainty) |
| `gamma_star_predicted` | $\gamma_*$ from eq. C.48 |

**Summary fields** (in the experiment metadata):

| Field | Value |
|-------|-------|
| `spectral_gap_measured` | $\hat{\gamma} = \min(\hat{\sigma}_0, \hat{\sigma}_1)$ |
| `spectral_gap_predicted` | $\gamma$ from Lemma C.31 |
| `gap_controller` | "homogeneous" or "spatial" (which mode sets the gap) |
| `rate_ordering_pass` | Boolean (true if the ordering check §5.6.3.4 passes) |

---

#### 5.6.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Four rates measured** | $\hat{\sigma}_k$ (per-mode), $\hat{\sigma}_{\mathcal{V}}$ (Lyapunov), $\hat{\gamma}_0$ (envelope), $\hat{\beta}(t)$ (instantaneous) |
| **Primary fitting method** | Log-linear regression on $\ln Q(t)$ vs. $t$ over $[t_a, t_b]$ |
| **Envelope fitting** | Peak detection + log-linear fit of peak amplitudes |
| **Instantaneous rate** | Centered finite difference of $\ln\mathcal{V}$, with running-average smoothing |
| **Asymptotic rate** | Time-average of $\hat{\beta}_{\mathrm{smooth}}$ over $[T-5, T]$ |
| **Analytic targets** | $D\alpha_k$ (eq. C.11), $\gamma_0$ (eq. C.15), $\gamma$ (Lemma C.31), $\gamma_*$ (eq. C.48) |
| **Per-mode tolerance** | $1\%$ relative error |
| **Gap tolerance** | $2\%$ relative error |
| **Lyapunov rate tolerance** | $5\%$ relative error |
| **Ordering check** | I $<$ V $<$ II $<$ III $<$ IV (five inequalities) |

The convergence rate is the observable that most directly tests the spectral theory of Appendix C. The modal rates test the eigenvalue computation (Theorem C.17). The spectral gap tests the gap lemma (Lemma C.31). The Lyapunov rate tests the stability theorem (Theorem C.43). The instantaneous rate tests the three-stage convergence (Theorem C.76). Each rate is extracted by a specific, reproducible fitting procedure with stated tolerances and quality criteria, ensuring that the comparison between numerics and theory is quantitative, not qualitative.

---

### 5.7 Horizon Proximity

The horizon — the capacity bound $\rho_{\max}$ where the mobility vanishes ($M(\rho_{\max}) = 0$, Principle 4) — is the structural boundary of the ED density space. The analytic theory guarantees that the density never reaches it (Theorem C.2, Theorem C.66(i)), but the *distance* to the horizon is a dynamically meaningful quantity: it determines the local diffusivity, the effective complexity amplification, the gradient suppression rate, and the energy barrier strength. The simulation engine measures this distance continuously, detects when the solution approaches the barrier, and logs the proximity history for post-hoc analysis of the near-horizon dynamics (Atlas §6).

---

#### 5.7.1 Measuring Distance to $\rho_{\max}$

The distance to the horizon is measured by three complementary quantities, each capturing a different aspect of the proximity.

##### 5.7.1.1 Proximity Margin $\delta(t)$

The **proximity margin** is the minimum distance between the current density field and the capacity bound:

$$
\delta(t) := \rho_{\max} - \max_{x \in \overline{\Omega}}\rho(x, t).
$$

In the discrete setting:

$$
\delta^n = \rho_{\max} - \max_j\,\rho_j^n.
$$

This is a single scalar computed by a maximum-scan over the density array — $O(N_{\mathrm{grid}})$ operations, performed at every time step as part of the proximity monitoring (§1.6.1, §2.3.1 Phase 1).

**Interpretation.** $\delta > 0$ means the density is strictly below $\rho_{\max}$ everywhere (the horizon is not reached). $\delta = 0$ would mean the density has reached $\rho_{\max}$ at some point (the horizon is contacted) — this is forbidden by the analytic theory and by the mobility-collapse protocol (§1.6). The proximity margin is the *tightest* measure of horizon distance: it reports the closest approach of any grid point.

**Location of the closest approach.** The engine also records the grid index $j_{\max}$ where the maximum density occurs:

$$
j_{\max}^n = \arg\max_j\,\rho_j^n.
$$

This identifies the spatial location of the closest approach — useful for diagnosing whether the proximity is due to a global density increase (the mean $\bar{\rho}$ is close to $\rho_{\max}$) or a localized peak (a single grid point is close while the rest of the density is far below).

##### 5.7.1.2 Minimum Mobility $M_{\min}(t)$

The minimum mobility across the domain:

$$
M_{\min}(t) := \min_{x \in \overline{\Omega}} M(\rho(x, t)) = M(\rho_{\max} - \delta(t)).
$$

For the power-law mobility: $M_{\min} = M_0\,\delta^\beta$. This is the diffusion coefficient at the closest-approach point — the value that determines whether the equation is effectively parabolic ($M_{\min} \gg 0$) or effectively degenerate ($M_{\min} \approx 0$) at the most critical grid point.

**Discrete computation.** $M_{\min}^n = M(\max_j\rho_j^n) = M(\rho_{\max} - \delta^n)$. This requires one constitutive evaluation at the maximum density — a single function call, $O(1)$ cost.

**Threshold levels.** The minimum mobility provides a more physically meaningful threshold than the proximity margin alone:

| $M_{\min}/M_*$ | Interpretation |
|----------------|---------------|
| $> 0.5$ | Well away from the horizon; uniform parabolicity |
| $0.1$–$0.5$ | Approaching the horizon; noticeable mobility reduction |
| $0.01$–$0.1$ | Near-horizon region; diffusion significantly suppressed |
| $< 0.01$ | Deep near-horizon; effectively degenerate |

For the default parameters ($M_* = 0.25$, $\beta = 2$): $M_{\min}/M_* = (\delta/0.5)^2$. The threshold $M_{\min}/M_* = 0.01$ corresponds to $\delta = 0.05$ — a $5\%$ margin from $\rho_{\max}$.

##### 5.7.1.3 Energy-Barrier Distance $\delta_{\mathrm{barrier}}(t)$

The analytic barrier prediction (Proposition C.11): the minimum margin consistent with the current energy level:

$$
\delta_{\mathrm{barrier}}(t) := \frac{P_0\,(\rho_{\max} - \rho^*)\,|\Omega|}{M_0\,\mathcal{E}(t)}.
$$

This is the *theoretical* minimum distance to the horizon, derived from the energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$. The actual margin $\delta(t)$ must satisfy $\delta(t) \geq \delta_{\mathrm{barrier}}(t)$; a violation indicates an inconsistency between the energy and proximity computations (§1.6.4).

**Discrete computation.** $\delta_{\mathrm{barrier}}^n = P_0(\rho_{\max} - \rho^*)|\Omega|/(M_0\,\mathcal{E}^n)$. This requires the current energy $\mathcal{E}^n$ (already computed for the monotonicity check, §5.1) and the precomputed constants $P_0$, $\rho_{\max} - \rho^*$, $|\Omega|$, $M_0$ — a single division, $O(1)$ cost.

**Barrier ratio.** The ratio $\delta(t)/\delta_{\mathrm{barrier}}(t)$ measures how much headroom the solution has above the theoretical minimum. For a solution relaxing toward equilibrium: $\delta(t)$ increases (the density retreats from the horizon) while $\delta_{\mathrm{barrier}}(t)$ decreases (the energy decreases, making the barrier weaker), so the ratio grows over time. A ratio close to $1$ indicates that the solution is near the theoretical limit; a ratio $\gg 1$ indicates ample headroom.

---

#### 5.7.2 Detecting Barrier Approach

The proximity monitoring system (§1.6.1) classifies the current state into three zones based on the proximity margin $\delta^n$. This subsection specifies the detection logic and the information recorded at each transition between zones.

##### 5.7.2.1 Zone Classification

| Zone | Condition | Status | Action |
|------|-----------|--------|--------|
| **Normal** | $\delta^n > \delta_{\mathrm{warn}} = 0.01\,\rho_{\max}$ | Far from the horizon | None |
| **Warning** | $\delta_{\mathrm{crit}} < \delta^n \leq \delta_{\mathrm{warn}}$ | Approaching the horizon | Log diagnostic |
| **Critical** | $\delta^n \leq \delta_{\mathrm{crit}} = 10^{-4}\,\rho_{\max}$ | At the horizon boundary layer | Adaptive $\Delta t$ reduction |

The zone transitions are detected by comparing $\delta^n$ to the thresholds at each time step. The transitions are:

- **Normal → Warning** ($\delta^n$ crosses below $\delta_{\mathrm{warn}}$): the density field has entered the near-horizon region. This may be expected (IC-D experiments deliberately start near the horizon) or unexpected (a far-from-equilibrium transient has pushed a density peak toward $\rho_{\max}$).

- **Warning → Critical** ($\delta^n$ crosses below $\delta_{\mathrm{crit}}$): the density is very close to $\rho_{\max}$. The adaptive time-step reduction (§1.6.2) activates.

- **Critical → Warning** ($\delta^n$ rises above $2\delta_{\mathrm{crit}}$): the density has retreated from the critical zone. The adaptive time-step reduction is deactivated (with hysteresis, §1.6.2).

- **Warning → Normal** ($\delta^n$ rises above $\delta_{\mathrm{warn}}$): the density has fully retreated from the near-horizon region.

Each transition is logged as a diagnostic event (§2.4.3.1).

##### 5.7.2.2 Approach Rate

When the solution is in the Warning or Critical zone, the engine computes the **approach rate** — the time derivative of the proximity margin:

$$
\dot{\delta}^n = \frac{\delta^{n+1} - \delta^{n-1}}{2\Delta t}.
$$

A negative $\dot{\delta}$ means the solution is moving *toward* the horizon (the margin is decreasing). A positive $\dot{\delta}$ means the solution is retreating. The approach rate provides early warning: a large negative $\dot{\delta}$ in the Warning zone suggests that the solution will enter the Critical zone within $\sim \delta/|\dot{\delta}|$ time units.

The engine does not extrapolate or predict the future margin — it only records the current rate. The adaptive time-step reduction (§1.6.2) responds to the *current* margin, not to the predicted future margin, ensuring that the response is causal and non-anticipatory.

##### 5.7.2.3 Spatial Extent of the Near-Horizon Region

For experiments that probe the near-horizon dynamics (Atlas §6.3, Experiment 6.6), the engine measures the **near-horizon set fraction**:

$$
f_\eta(t) := \frac{|\{x \in \Omega : \rho(x, t) > \rho_{\max} - \eta\}|}{|\Omega|},
$$

for a fixed threshold $\eta > 0$ (default: $\eta = 0.1$). In the discrete setting:

$$
f_\eta^n = \frac{\#\{j : \rho_j^n > \rho_{\max} - \eta\}}{N_{\mathrm{grid}}}.
$$

This measures what fraction of the domain is in the near-horizon region. For IC-D (near-capacity initialization): $f_\eta(0) \approx 1$ (the entire domain is near $\rho_{\max}$). As the density retreats: $f_\eta(t)$ decreases monotonically, reaching $0$ when no grid point exceeds $\rho_{\max} - \eta$.

The near-horizon gradient integral $G_\eta(t) = \int_{\Omega_\eta}|\nabla\rho|^2\,dx$ (Proposition C.10) is computed alongside $f_\eta$:

$$
G_\eta^n = h\sum_{j : \rho_j^n > \rho_{\max} - \eta}(|\nabla_h\rho^n|^2)_j.
$$

This measures the gradient content *within* the near-horizon region. Proposition C.10 predicts $G_\eta \leq M(\rho_{\max} - \eta)\,\mathcal{E}_0/(D\,P'(\rho_{\max} - \eta))$ — the gradient suppression bound. The engine verifies this bound at every output step when the experiment involves near-horizon dynamics.

---

#### 5.7.3 Logging

The horizon-proximity observables are recorded at two levels.

##### 5.7.3.1 Per-Step Diagnostics (Always Recorded)

At every internal time step, the following are computed and stored in the running diagnostic state:

| Quantity | Symbol | Cost |
|----------|--------|------|
| Proximity margin | $\delta^n$ | $O(N_{\mathrm{grid}})$ |
| Location of maximum | $j_{\max}^n$ | Same pass as $\delta^n$ |
| Current zone | Normal / Warning / Critical | Comparison |

These are also used by the mobility-collapse protocol (§1.6) and the positivity enforcement (§1.7). They are not written to the output file at every step unless the experiment specifies every-step sampling.

##### 5.7.3.2 Output-Step Record (At Output Steps)

At each output step, the following are recorded in the `Observables` record:

| Field | Value |
|-------|-------|
| `delta` | $\delta^n = \rho_{\max} - \max_j\rho_j^n$ |
| `j_max` | Grid index of maximum density |
| `rho_max_val` | $\max_j\rho_j^n$ (the maximum density value) |
| `M_min` | $M(\max_j\rho_j^n)$ (minimum mobility) |
| `M_min_ratio` | $M_{\min}/M_*$ (mobility ratio) |
| `delta_barrier` | $P_0(\rho_{\max} - \rho^*)|\Omega|/(M_0\mathcal{E}^n)$ |
| `barrier_ratio` | $\delta^n/\delta_{\mathrm{barrier}}^n$ |

For near-horizon experiments (when the experiment specification requests extended proximity logging):

| Field | Value |
|-------|-------|
| `f_eta` | Near-horizon set fraction $f_\eta^n$ |
| `G_eta` | Near-horizon gradient integral $G_\eta^n$ |
| `G_eta_bound` | Proposition C.10 bound: $M(\rho_{\max} - \eta)\mathcal{E}_0/(DP'(\rho_{\max} - \eta))$ |
| `delta_dot` | Approach rate $\dot{\delta}^n$ |
| `amplification` | $C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}}$ (from §5.5.1.3) |

##### 5.7.3.3 Diagnostic Events

The following events are written to the diagnostic log (§2.4.3.1) when they occur:

| Event | Trigger | Fields logged |
|-------|---------|--------------|
| `ProximityWarning` | $\delta^n \leq \delta_{\mathrm{warn}}$ (first time or re-entry) | $n$, $t$, $\delta$, $j_{\max}$, $\rho_{\max\_val}$, $M_{\min}$, $\mathcal{E}$ |
| `ProximityCritical` | $\delta^n \leq \delta_{\mathrm{crit}}$ | Same fields + $\Delta t_{\mathrm{new}}$ |
| `ProximityRecovery` | $\delta^n > 2\delta_{\mathrm{crit}}$ after a Critical event | $n$, $t$, $\delta$, $\Delta t_{\mathrm{restored}}$ |
| `ProximityNormal` | $\delta^n > \delta_{\mathrm{warn}}$ after a Warning event | $n$, $t$, $\delta$ |
| `BarrierViolation` | $\delta^n < \delta_{\mathrm{barrier}}^n$ | $n$, $t$, $\delta$, $\delta_{\mathrm{barrier}}$, $\mathcal{E}$, ratio |

##### 5.7.3.4 Post-Integration Summary

The horizon-proximity history is summarized in the integration summary (§2.3.4.4):

| Field | Value |
|-------|-------|
| `delta_min` | $\min_n\delta^n$ (closest approach over the entire integration) |
| `delta_min_time` | Time of the closest approach |
| `delta_min_location` | Grid index of the closest approach |
| `delta_final` | $\delta^{N_{\mathrm{final}}}$ (margin at the final time) |
| `M_min_overall` | $\min_n M_{\min}^n$ (minimum mobility over the entire integration) |
| `time_in_warning` | Total time spent in the Warning zone |
| `time_in_critical` | Total time spent in the Critical zone |
| `n_barrier_violations` | Number of barrier-violation events |
| `barrier_ratio_min` | $\min_n(\delta^n/\delta_{\mathrm{barrier}}^n)$ (tightest barrier compliance) |

The summary provides a one-glance assessment of the near-horizon behavior: a run with `delta_min > 0.01`, `time_in_critical = 0`, and `n_barrier_violations = 0` had no significant near-horizon dynamics. A run with `delta_min = 0.001` and `time_in_critical > 0` experienced a significant near-horizon excursion that activated the adaptive time-step reduction.

---

#### 5.7.4 Validation

##### 5.7.4.1 Barrier Compliance

At every output step where the barrier is computed:

$$
\delta^n \geq \delta_{\mathrm{barrier}}^n.
$$

This is the discrete analogue of Proposition C.11. A violation ($\delta < \delta_{\mathrm{barrier}}$) is logged as a `BarrierViolation` event (§5.7.3.3) and triggers the diagnostic analysis described in §1.6.4.

In all converged Atlas experiments, the barrier compliance holds with substantial margin: $\delta/\delta_{\mathrm{barrier}} > 2$ throughout. The margin increases over time as the density retreats and the energy decreases.

##### 5.7.4.2 Monotonic Margin Improvement

For solutions evolving under the canonical dynamics from an admissible initial condition, Proposition C.73 (Horizon persistence) predicts that the margin improves asymptotically:

$$
\delta(t) \to \rho_{\max} - \rho^* = 0.5 \qquad \text{as } t \to \infty.
$$

The engine verifies:

- $\delta(T) > \delta(0)$ for experiments that start near the horizon (IC-D): the margin has increased over the integration.
- $\delta(T) \approx \rho_{\max} - \rho^*$ for long integrations ($T > 20$): the margin has converged to its equilibrium value.

A failure ($\delta(T) < \delta(0)$ for a near-horizon IC) would indicate that the density is drifting *toward* the horizon rather than away from it — contradicting the analytic theory. This would be a serious structural failure, likely caused by an error in the penalty implementation (the penalty should drive $\rho$ toward $\rho^*$, away from $\rho_{\max}$).

##### 5.7.4.3 Gradient Suppression Bound

For experiments with extended proximity logging (near-horizon experiments):

$$
G_\eta^n \leq \frac{M(\rho_{\max} - \eta)}{P'(\rho_{\max} - \eta)}\,\frac{\mathcal{E}_0}{D} \qquad \text{for all } n.
$$

This is the discrete analogue of Proposition C.10. The bound is evaluated at every output step using the initial energy $\mathcal{E}_0$ (the bound uses the initial energy, not the current energy, because the dissipation integral $\int_0^t\int P'|\nabla\rho|^2/M\,dx\,ds \leq \mathcal{E}_0/D$ is cumulative from $t = 0$).

The bound is conservative — the actual $G_\eta$ is typically well below it, because the amplified dissipation in the near-horizon region destroys the gradients rapidly (§6.3 of the Atlas). Verification of the bound confirms that the gradient-suppression mechanism is operating correctly at the discrete level.

##### 5.7.4.4 Mobility Recovery

For near-horizon experiments that run to sufficient final time ($T > 15$):

$$
M_{\min}(T)/M_* > 0.9.
$$

This verifies Proposition C.74 (Asymptotic mobility recovery): the diffusion coefficient returns to its equilibrium value as $\rho \to \rho^*$. The $0.9$ threshold allows for residual deviations of $\|\rho - \rho^*\|_{L^\infty} \leq 0.05$ (which gives $M(\rho)/M_* = ((0.5 - 0.05)/0.5)^2 = 0.81$ at the default parameters — just below $0.9$, so the threshold accommodates slightly slower convergence).

---

#### 5.7.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Primary measure** | Proximity margin $\delta = \rho_{\max} - \max_j\rho_j$; $O(N_{\mathrm{grid}})$ per step |
| **Complementary measures** | Minimum mobility $M_{\min}$; barrier distance $\delta_{\mathrm{barrier}}$; near-horizon set fraction $f_\eta$ |
| **Zone system** | Normal ($\delta > 0.01\rho_{\max}$), Warning, Critical ($\delta \leq 10^{-4}\rho_{\max}$) |
| **Approach rate** | $\dot{\delta}$ by centered finite difference; computed in Warning/Critical zones |
| **Logging** | Per-step: $\delta$, $j_{\max}$, zone. Output-step: $\delta$, $M_{\min}$, $\delta_{\mathrm{barrier}}$, barrier ratio, $f_\eta$, $G_\eta$ |
| **Diagnostic events** | ProximityWarning, ProximityCritical, ProximityRecovery, ProximityNormal, BarrierViolation |
| **Post-integration summary** | $\delta_{\min}$, time in zones, barrier violations, mobility recovery |
| **Key validations** | Barrier compliance ($\delta \geq \delta_{\mathrm{barrier}}$), margin improvement ($\delta(T) > \delta(0)$), gradient suppression ($G_\eta \leq$ bound), mobility recovery ($M_{\min}(T)/M_* > 0.9$) |

The horizon proximity observables transform Principle 4 from an abstract structural constraint ($M(\rho_{\max}) = 0$) into a set of measurable, time-resolved quantities: the distance to the barrier, the local diffusivity, the gradient suppression, and the approach dynamics. Together with the energy barrier (§5.1) and the effective complexity amplification (§5.5), they provide the complete numerical picture of the near-horizon behavior predicted by Propositions C.10, C.11, C.73, and C.74.

---

## 6. Data Formats

### 6.1 Time Series Format

The time series is the primary data product of every experiment. It records the full observable set (§§5.1–5.7) at each output step, forming a tabular dataset that is the input to all post-processing, figure generation, and validation analysis. This subsection specifies the logical structure of the time-series file — the field definitions, their types and units, the ordering conventions, and the metadata that makes the file self-describing and independently reproducible.

---

#### 6.1.1 File Structure

The time-series file is a rectangular table: each row corresponds to one output step, and each column corresponds to one observable field. The table is ordered chronologically (row $0$ is $t = 0$; row $N_{\mathrm{output}} - 1$ is $t = T_{\mathrm{final}}$).

**Logical layout:**

```
Row 0:    t₀,   E₀,   C_ED₀,   V₀,   ...
Row 1:    t₁,   E₁,   C_ED₁,   V₁,   ...
  ⋮
Row N:    tₙ,   Eₙ,   C_EDₙ,   Vₙ,   ...
```

**Physical format.** The table is stored in one of the supported formats (§2.4):

| Format | Extension | Library | Row/column access |
|--------|-----------|---------|------------------|
| CSV | `.csv` | Any text reader | Column-by-header-name |
| NumPy compressed | `.npz` | `numpy.load` | Field-by-key |
| HDF5 | `.h5` | `h5py` / `HDF5.jl` / MATLAB `h5read` | Dataset-by-name |
| MATLAB | `.mat` | `scipy.io.loadmat` / MATLAB `load` | Variable-by-name |

The CSV format stores the table as a header line (field names, comma-separated) followed by one data line per row. The binary formats (NPZ, HDF5, MAT) store each column as a named array of length $N_{\mathrm{output}}$, preserving full double-precision accuracy.

**Mandatory requirement.** Regardless of the physical format, the file must satisfy:

1. **Named fields.** Every column is identified by a unique string name (not by its positional index). This ensures that adding new fields in future versions does not break existing readers.
2. **Self-describing.** The file includes its own metadata (§6.1.4) — a reader can determine the experiment, parameter set, and observable definitions without consulting an external document.
3. **Chronologically ordered.** Rows are in strictly increasing time order: $t_0 < t_1 < \cdots < t_{N-1}$.

---

#### 6.1.2 Field Definitions

The time-series file contains three groups of fields: the time index, the primary observables, and the derived quantities.

##### 6.1.2.1 Time Index

| # | Field name | Type | Description |
|---|-----------|------|-------------|
| 1 | `time` | Float64 | Current time $t_n$ |
| 2 | `step` | Int64 | Internal step counter $n$ at this output step |

The `step` field records the actual integration step number (not the output-step index). It enables cross-referencing with the diagnostic log, where events are indexed by step number.

##### 6.1.2.2 Primary Observables

These fields are computed directly from the state $(\boldsymbol{\rho}^n, v^n)$ and the constitutive functions at each output step. Each is defined in a specific subsection of §5.

| # | Field name | Type | Definition | Reference |
|---|-----------|------|-----------|-----------|
| 3 | `energy` | Float64 | $\mathcal{E}[\rho^n, v^n]$ | §5.1 |
| 4 | `energy_potential` | Float64 | $\int_\Omega\Phi(\rho^n)\,dx$ | §5.1.2.2 |
| 5 | `energy_kinetic` | Float64 | $\frac{\tau H}{2}(v^n)^2$ | §5.1.2.3 |
| 6 | `C_ED` | Float64 | $\int_\Omega|\nabla\rho^n|^2\,dx$ | §5.5 |
| 7 | `C_ED_eff` | Float64 | $\int_\Omega(P'/M)|\nabla\rho^n|^2\,dx$ | §5.5.1.3 |
| 8 | `lyapunov` | Float64 | $\mathcal{V}[u^n, w^n]$ (Definition C.39) | §5.1 |
| 9 | `rho_bar` | Float64 | $L^{-d}\int_\Omega\rho^n\,dx$ | §5.3 |
| 10 | `a_0` | Float64 | $\bar{\rho}^n - \rho^*$ (homogeneous-mode amplitude) | §5.3 |
| 11 | `v` | Float64 | Participation variable $v^n$ | §1.1 |
| 12 | `delta` | Float64 | $\rho_{\max} - \max_j\rho_j^n$ (proximity margin) | §5.7 |
| 13 | `M_min` | Float64 | $M(\max_j\rho_j^n)$ (minimum mobility) | §5.7 |
| 14 | `D_diff` | Float64 | $D\,P_*'\,C_{\mathrm{ED}}^n$ (gradient dissipation) | §5.2 |
| 15 | `D_pen` | Float64 | $(D\,P_*'^2/M_*)\,\|u^n\|_{L^2}^2$ (penalty dissipation) | §5.2 |
| 16 | `D_part` | Float64 | $H\,\zeta\,(v^n)^2$ (participation dissipation) | §5.2 |

##### 6.1.2.3 Derived Quantities

These fields are computed from the primary observables and/or from the previous output step. They are included for convenience and to ensure that the derivation is performed consistently (the same formula, applied to the same data, in every implementation).

| # | Field name | Type | Definition | Reference |
|---|-----------|------|-----------|-----------|
| 17 | `D_total` | Float64 | $\mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}}$ | §5.2.3 |
| 18 | `dE_dt` | Float64 | $(\mathcal{E}^{n} - \mathcal{E}^{n-1})/(t_n - t_{n-1})$ | §5.1.3 |
| 19 | `dissipation_residual` | Float64 | $d\mathcal{E}/dt + \mathcal{D}_{\mathrm{total}}$ | §5.2.3 |
| 20 | `beta_instantaneous` | Float64 | $-d\ln\mathcal{V}/dt$ (centered FD) | §5.6.2.3 |
| 21 | `amplification` | Float64 | $C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}}$ | §5.5.1.3 |
| 22 | `delta_barrier` | Float64 | $P_0(\rho_{\max} - \rho^*)|\Omega|/(M_0\mathcal{E}^n)$ | §5.7.1.3 |
| 23 | `barrier_ratio` | Float64 | $\delta^n/\delta_{\mathrm{barrier}}^n$ | §5.7.1.3 |
| 24 | `basin_indicator` | Float64 | $(\|u^n\|_{H^1}^2 + |v^n|^2)/\epsilon_0^2$ | §5.5.3.2 |

**First-row handling.** The fields `dE_dt`, `dissipation_residual`, and `beta_instantaneous` require data from the previous output step. At row $0$ ($t = 0$): these fields are set to NaN (not-a-number) to indicate that they are undefined. Subsequent rows use the formulas above with the previous row's data.

**Total column count.** The standard time-series file has $24$ columns. Experiments that request extended logging (§2.4.2, §5.7.3.2) add up to $5$ additional columns:

| # | Field name | Condition | Definition |
|---|-----------|-----------|-----------|
| 25 | `f_eta` | Extended proximity logging | Near-horizon set fraction |
| 26 | `G_eta` | Extended proximity logging | Near-horizon gradient integral |
| 27 | `D_diff_full` | Extended dissipation logging | Full gradient dissipation $D\int(P'/M)|\nabla\rho|^2\,dx$ |
| 28 | `D_pen_full` | Extended dissipation logging | Full penalty dissipation $D\int P^2/M\,dx$ |
| 29 | `spectral_centroid_C` | Extended spectral logging | $\sum k\mu_k|a_k|^2/\sum\mu_k|a_k|^2$ |

Extended columns are present only when the experiment specification requests them; otherwise, they are omitted (not filled with zeros or NaN).

---

#### 6.1.3 Units and Conventions

The canonical ED system is dimensionless — all quantities are expressed in the natural units of the PDE, with no physical dimension attached. The time-series file inherits this dimensionlessness.

| Convention | Specification |
|-----------|--------------|
| **Units** | All fields are dimensionless. No SI, CGS, or other physical unit system is used. |
| **Floating-point format** | IEEE 754 double precision (64-bit). All values are stored with full precision ($\sim 15$ significant digits). |
| **CSV numeric format** | Scientific notation with $15$ significant digits: e.g., `1.234567890123456e-04`. This preserves the full double-precision content in text form. |
| **NaN convention** | `NaN` (text) or IEEE 754 NaN (binary) for undefined values (first-row derivatives, §6.1.2.3). |
| **Sign convention for rates** | Dissipation channels $\mathcal{D}_{\mathrm{diff}}$, $\mathcal{D}_{\mathrm{pen}}$, $\mathcal{D}_{\mathrm{part}}$ are *positive* (they represent energy *removal*). The energy rate $d\mathcal{E}/dt$ is *negative* for a dissipating system. The instantaneous rate $\hat{\beta}$ is *positive* (it is $-d\ln\mathcal{V}/dt$, so positive means $\mathcal{V}$ is decreasing). |
| **Time convention** | Time starts at $t = 0$ and increases. The first row has `time = 0.0`; the last row has `time = T_final` (exactly, after the last-step shortening of §2.3.4.1). |

---

#### 6.1.4 Metadata

Every time-series file includes a metadata block that fully identifies the experiment and the computational setup. The metadata is stored as:

- **CSV:** Comment lines at the top of the file, prefixed by `#`.
- **NPZ:** A separate key `metadata` containing a dictionary.
- **HDF5:** Attributes on the root group.
- **MAT:** A struct variable `metadata` alongside the data arrays.

##### 6.1.4.1 Metadata Fields

The metadata fields are those defined in §2.4.4.1 (25 fields). For quick reference, the fields most relevant to interpreting the time series are:

| Field | Example | Purpose |
|-------|---------|---------|
| `experiment_id` | `"3.1"` | Which Atlas experiment produced this file |
| `atlas_figure` | `"3.1"` | Which Atlas figure this file supports |
| `parameter_set` | `"II"` | Which canonical parameter set was used |
| `D`, `zeta`, `tau` | `0.6`, `0.5`, `1.0` | Canonical parameters (for quick reference) |
| `discriminant` | `-1.59` | Modal discriminant $\mathscr{D}_0$ |
| `regime` | `"Oscillatory"` | Regime classification |
| `IC_type` | `"A"` | Initial condition type |
| `IC_amplitude` | `0.001` | Perturbation amplitude |
| `method` | `"SPEC_ETDRK4"` | Spatial method and time-stepping scheme |
| `N` | `128` | Grid points or spectral modes |
| `dt` | `1e-04` | Time step |
| `T_final` | `5.0` | Integration time |
| `n_output` | `1000` | Number of output rows in the file |
| `spec_hash` | `"a3b4c5..."` | SHA-256 reproducibility hash |

##### 6.1.4.2 Field Description Block

In addition to the experiment metadata, the file includes a field description block that documents each column:

```
# FIELD DESCRIPTIONS:
# time          : Current time t
# step          : Internal step counter
# energy        : Total energy E[rho, v] = int Phi(rho) dx + (tau H / 2) v^2
# energy_potential : Potential energy int Phi(rho) dx
# energy_kinetic : Kinetic energy (tau H / 2) v^2
# C_ED          : ED-complexity int |grad rho|^2 dx
# ...
```

This block is included in the CSV header comments and in the HDF5/NPZ/MAT metadata. It ensures that the file is interpretable without consulting the Suite documentation — the field names, formulas, and physical meanings are embedded in the file itself.

---

#### 6.1.5 Example

A minimal CSV time-series file for Experiment 3.1a (single-mode $n = 1$ decay, Parameter Set II, Method B, $N = 128$, $\Delta t = 10^{-4}$, $T = 5$, $k_{\mathrm{out}} = 50$):

```
# ED Simulation Suite - Time Series Output
# experiment_id: 3.1a
# atlas_figure: 3.1
# parameter_set: II
# D: 0.6, H: 0.4, zeta: 0.5, tau: 1.0
# rho_star: 0.5, rho_max: 1.0
# M0: 1.0, beta: 2.0, P0: 1.0
# discriminant: -1.59
# regime: Oscillatory
# IC_type: A, IC_amplitude: 1.0e-03, IC_mode: 1, IC_v0: 0.0
# method: SPEC_ETDRK4
# N: 128, dt: 1.0e-04, T_final: 5.0
# output_interval: 50
# n_output: 1001
# spec_hash: 7f3a2b...
#
# FIELD DESCRIPTIONS:
# time            : Current time t
# step            : Internal step counter
# energy          : Total energy E[rho, v]
# energy_potential: Potential energy
# energy_kinetic  : Kinetic energy (tau H / 2) v^2
# C_ED            : ED-complexity
# C_ED_eff        : Effective complexity
# lyapunov        : Lyapunov functional V[u, w]
# rho_bar         : Spatial mean density
# a_0             : Homogeneous mode amplitude
# v               : Participation variable
# delta           : Proximity margin
# M_min           : Minimum mobility
# D_diff          : Gradient dissipation channel
# D_pen           : Penalty dissipation channel
# D_part          : Participation dissipation channel
# D_total         : Total dissipation
# dE_dt           : Energy rate of change
# dissipation_residual : Dissipation identity residual
# beta_instantaneous   : Instantaneous Lyapunov rate
# amplification   : C_ED_eff / C_ED
# delta_barrier   : Energy barrier distance
# barrier_ratio   : delta / delta_barrier
# basin_indicator : (||u||_H1^2 + |v|^2) / epsilon_0^2
#
time,step,energy,energy_potential,energy_kinetic,C_ED,C_ED_eff,...
0.000000000000000e+00,0,9.869604401089358e-07,9.869604401089358e-07,0.0,...
5.000000000000000e-03,50,9.766505638498113e-07,...
...
5.000000000000000e+00,50000,1.234567890123456e-16,...
```

The file has $1001$ data rows (including $t = 0$ and $t = 5$) and $24$ data columns. The header block ($30$+ lines) provides complete metadata and field descriptions. A reader can load the file, identify every column by name, and reproduce the experiment from the metadata alone.

---

#### 6.1.6 Reading and Integrity Verification

When a time-series file is read for post-processing or figure generation, the engine performs the following integrity checks:

| Check | Condition | Action on failure |
|-------|-----------|-------------------|
| Header present | Metadata block parseable | Reject file |
| Field names match | All 24 standard fields present (by name) | Reject if any missing |
| Row count | `n_output` in metadata equals actual row count | Warning |
| Time monotonicity | $t_0 < t_1 < \cdots < t_{N-1}$ | Reject |
| First time | $t_0 = 0.0$ (to within $10^{-14}$) | Warning |
| Last time | $t_{N-1} = T_{\mathrm{final}}$ (to within $\Delta t$) | Warning |
| Energy non-negative | $\mathcal{E}^n \geq 0$ for all $n$ | Warning (possible corruption) |
| Spec hash | Matches the hash of the current experiment specification | Warning if mismatch (file may be from a different run) |

These checks ensure that the file is valid, complete, and correctly associated with the experiment. A file that passes all checks is accepted for analysis; a file that fails a "Reject" check is not processed.

---

#### 6.1.7 Summary

| Aspect | Specification |
|--------|--------------|
| **Structure** | Rectangular table: $N_{\mathrm{output}}$ rows × $24$–$29$ columns |
| **Row ordering** | Chronological ($t_0 < t_1 < \cdots$) |
| **Column identification** | By name (not by position) |
| **Standard fields** | 2 index + 14 primary + 8 derived = 24 |
| **Extended fields** | Up to 5 additional (experiment-dependent) |
| **Precision** | IEEE 754 double (64-bit); CSV: 15 significant digits |
| **Units** | All dimensionless |
| **Metadata** | 25+ fields identifying experiment, parameters, IC, method, resolution |
| **Field descriptions** | Embedded in the file (self-describing) |
| **Integrity checks** | 8 checks on read (header, fields, row count, time order, hash) |
| **Typical size** | $\sim 100$ KB per experiment (1000 rows × 24 columns × 8 bytes) |

The time-series format is the data contract between the simulation engine and all downstream consumers (post-processing scripts, figure generators, validation tests, cross-implementation comparisons). Every consumer reads the same named fields from the same self-describing file; no positional assumptions, no implicit conventions, and no external lookups are needed.

---

### 6.2 Spectral Data Format

The spectral data file records the modal amplitudes $\{a_k(t)\}$ and related per-mode quantities at each output step. It is produced alongside the time-series file for experiments that require spectral analysis (Atlas §§3–4, §9.1, §9.3, §9.4) and provides the raw data for decay-rate extraction (§5.6), triad-coupling verification (§5.4), and the spectral figures of the Atlas (Figures 3.1–3.8, 4.1–4.9, 9.1, 9.3, 9.4).

The spectral data file is separate from the time-series file because it has a different shape: the time series has a fixed number of scalar columns ($24$–$29$), while the spectral data has a variable number of per-mode columns ($N_{\mathrm{obs}}$ modes, each with multiple quantities). Merging them into a single table would produce an unwieldy file with $\sim 100$ columns; separating them keeps each file focused and manageable.

---

#### 6.2.1 Modal Amplitude Arrays

##### 6.2.1.1 Primary Array: Modal Amplitudes $a_k(t)$

The core content of the spectral file is the array of signed modal amplitudes at each output step:

$$
\mathbf{A} \in \mathbb{R}^{N_{\mathrm{output}} \times N_{\mathrm{obs}}},
$$

where $N_{\mathrm{output}}$ is the number of output steps and $N_{\mathrm{obs}}$ is the number of tracked modes. The entry $\mathbf{A}[n, k]$ is the amplitude $a_k(t_n)$ — the coefficient of the $k$-th Neumann eigenfunction $\varphi_k$ in the expansion of $u(x, t_n) = \rho(x, t_n) - \rho^*$.

The amplitudes are *signed* — they carry the phase information needed for zero-crossing detection (§5.3.3.3) and for verifying the triad generation direction (the sign of the generated mode depends on $\operatorname{sign}(M_*')$ and the signs of the source amplitudes).

**Index convention.** The mode index $k$ runs from $0$ to $N_{\mathrm{obs}} - 1$:

- $k = 0$: the spatially uniform (homogeneous) mode. $a_0 = \sqrt{L}\,(\bar{\rho} - \rho^*)$.
- $k = 1, 2, \ldots, N_{\mathrm{obs}} - 1$: the spatial modes. $a_k = \langle u, \varphi_k\rangle_{L^2}$.

The $k = 0$ mode is always included (it is the homogeneous mode that couples to the participation variable). The number of spatial modes tracked is $N_{\mathrm{obs}} - 1$.

##### 6.2.1.2 Derived Arrays

In addition to the signed amplitudes, the spectral file stores the following per-mode derived quantities, each as an $N_{\mathrm{output}} \times N_{\mathrm{obs}}$ array:

| Array name | Symbol | Formula | Purpose |
|-----------|--------|---------|---------|
| `abs_amp` | $|a_k(t)|$ | $|\mathbf{A}[n, k]|$ | Semilog decay plots; peak detection |
| `modal_energy` | $E_k(t)$ | $|a_k(t)|^2$ | Energy distribution; Parseval check |
| `modal_complexity` | $\mu_k E_k(t)$ | $\mu_k|a_k(t)|^2$ | Contribution to $C_{\mathrm{ED}}$; spectral centroid |

These arrays are redundant (they are deterministic functions of $\mathbf{A}$ and the eigenvalues $\mu_k$), but storing them avoids recomputation during post-processing and ensures that all consumers use the same formulas.

##### 6.2.1.3 Scalar Summary Quantities Per Output Step

Each output step also has scalar quantities derived from the full mode array:

| Field name | Symbol | Formula | Purpose |
|-----------|--------|---------|---------|
| `total_modal_energy` | $E_{\mathrm{total}}(t)$ | $\sum_{k=0}^{N_{\mathrm{obs}}-1}|a_k|^2$ | Parseval check against $\|u\|_{L^2}^2$ |
| `tail_energy` | $E_{\mathrm{tail}}(t)$ | $\|u\|_{L^2}^2 - E_{\mathrm{total}}$ | Unresolved-mode contribution |
| `total_modal_complexity` | $C_{\mathrm{modal}}(t)$ | $\sum_{k=1}^{N_{\mathrm{obs}}-1}\mu_k|a_k|^2$ | Resolved portion of $C_{\mathrm{ED}}$ |
| `tail_complexity` | $C_{\mathrm{tail}}(t)$ | $C_{\mathrm{ED}} - C_{\mathrm{modal}}$ | Unresolved-mode contribution to $C_{\mathrm{ED}}$ |
| `spectral_centroid` | $\bar{k}(t)$ | $\sum_k k|a_k|^2 / \sum_k|a_k|^2$ | Mean mode number (energy-weighted) |
| `spectral_centroid_C` | $\bar{k}_C(t)$ | $\sum_k k\mu_k|a_k|^2 / \sum_k\mu_k|a_k|^2$ | Mean mode number (complexity-weighted) |
| `spectral_purity` | $S(t)$ | $1 - |a_{n_0}|^2/E_{\mathrm{total}}$ | Fraction of energy outside initialized mode (§5.3.2.3) |

The scalar summaries are stored as a separate $N_{\mathrm{output}} \times 7$ array (or as seven named columns) alongside the per-mode arrays.

---

#### 6.2.2 Frequency Indexing

##### 6.2.2.1 Mode-to-Eigenvalue Mapping

The mode index $k$ maps to a physical eigenvalue $\mu_k$ and an eigenfrequency through the Neumann spectrum:

$$
\mu_k = \left(\frac{k\pi}{L}\right)^2, \qquad k = 0, 1, 2, \ldots
$$

The spectral file stores the eigenvalue array as a one-dimensional vector of length $N_{\mathrm{obs}}$:

| Array name | Shape | Contents |
|-----------|-------|----------|
| `mode_index` | $(N_{\mathrm{obs}},)$ | $\{0, 1, 2, \ldots, N_{\mathrm{obs}} - 1\}$ |
| `eigenvalue` | $(N_{\mathrm{obs}},)$ | $\{\mu_0 = 0,\; \mu_1 = (\pi/L)^2,\; \mu_2 = (2\pi/L)^2,\; \ldots\}$ |
| `decay_coeff` | $(N_{\mathrm{obs}},)$ | $\{\alpha_0 = P_*',\; \alpha_1 = M_*\mu_1 + P_*',\; \ldots\}$ |
| `decay_rate` | $(N_{\mathrm{obs}},)$ | $\{D\alpha_0 = DP_*',\; D\alpha_1,\; \ldots\}$ |

These arrays are constant (they depend only on $L$, $M_*$, $P_*'$, and $D$, all of which are fixed during the integration) and are stored once, not repeated at each output step.

The eigenvalue array enables the consumer to convert between mode index $k$ (an integer) and the physical eigenvalue $\mu_k$ (a real number) without recomputing the formula. The decay-rate array provides the analytic prediction against which the measured rates $\hat{\sigma}_k$ (§5.6) are compared.

##### 6.2.2.2 Two-Dimensional Mode Indexing

For 2D experiments on $\Omega_2 = [0, L_x] \times [0, L_y]$, the mode index is a pair $(k_1, k_2)$ with eigenvalue $\mu_{k_1, k_2} = (k_1\pi/L_x)^2 + (k_2\pi/L_y)^2$. The spectral file stores the 2D amplitudes as a three-dimensional array:

$$
\mathbf{A}_{\mathrm{2D}} \in \mathbb{R}^{N_{\mathrm{output}} \times N_{\mathrm{obs},x} \times N_{\mathrm{obs},y}},
$$

where $N_{\mathrm{obs},x}$ and $N_{\mathrm{obs},y}$ are the number of tracked modes in each direction. The eigenvalue array is also two-dimensional:

$$
\boldsymbol{\mu}_{\mathrm{2D}} \in \mathbb{R}^{N_{\mathrm{obs},x} \times N_{\mathrm{obs},y}}.
$$

For the Atlas 2D experiments (Experiment 3.7), the modes are tracked up to $|\mathbf{k}|^2 = k_1^2 + k_2^2 \leq 25$ (a quarter-circle of radius $5$ in mode space), with $N_{\mathrm{obs},x} = N_{\mathrm{obs},y} = 6$ (modes $0$–$5$ in each direction). The 2D spectral file is produced only for experiments that explicitly request it.

##### 6.2.2.3 Wavenumber Convention

The engine uses the **physical wavenumber** convention: the wavenumber of mode $k$ is $\kappa_k = k\pi/L$ (in units of inverse length), so the eigenvalue is $\mu_k = \kappa_k^2$. The spectral file stores the wavenumber array alongside the eigenvalue array:

| Array name | Shape | Contents |
|-----------|-------|----------|
| `wavenumber` | $(N_{\mathrm{obs}},)$ | $\{0,\; \pi/L,\; 2\pi/L,\; \ldots\}$ |

This enables plots with the wavenumber on the horizontal axis (the standard convention in spectral analysis) without requiring the consumer to know $L$.

---

#### 6.2.3 Storage Conventions

##### 6.2.3.1 Array Layout

The spectral file contains the following named arrays:

| Array | Shape | Type | Varies with time? |
|-------|-------|------|-------------------|
| `time` | $(N_{\mathrm{output}},)$ | Float64 | Indexing |
| `step` | $(N_{\mathrm{output}},)$ | Int64 | Indexing |
| `amplitudes` | $(N_{\mathrm{output}}, N_{\mathrm{obs}})$ | Float64 | Yes |
| `abs_amplitudes` | $(N_{\mathrm{output}}, N_{\mathrm{obs}})$ | Float64 | Yes |
| `modal_energy` | $(N_{\mathrm{output}}, N_{\mathrm{obs}})$ | Float64 | Yes |
| `modal_complexity` | $(N_{\mathrm{output}}, N_{\mathrm{obs}})$ | Float64 | Yes |
| `scalars` | $(N_{\mathrm{output}}, 7)$ | Float64 | Yes |
| `mode_index` | $(N_{\mathrm{obs}},)$ | Int64 | No (static) |
| `eigenvalue` | $(N_{\mathrm{obs}},)$ | Float64 | No (static) |
| `decay_coeff` | $(N_{\mathrm{obs}},)$ | Float64 | No (static) |
| `decay_rate` | $(N_{\mathrm{obs}},)$ | Float64 | No (static) |
| `wavenumber` | $(N_{\mathrm{obs}},)$ | Float64 | No (static) |

The time-varying arrays (rows indexed by output step, columns indexed by mode) and the static arrays (indexed by mode only) are stored in the same file but are clearly distinguished by their dimensionality.

##### 6.2.3.2 File Naming

The spectral file is stored in the experiment's output directory:

```
output/exp_{id}/spectral.{ext}
```

or, for sub-experiments:

```
output/exp_{id}/n1/spectral.{ext}
output/exp_{id}/n2/spectral.{ext}
```

The file extension matches the chosen format (`.npz`, `.h5`, `.mat`). For CSV format, the 2D amplitude array is flattened into columns named `a_0`, `a_1`, ..., `a_{N_obs-1}` (one column per mode), and the static arrays are stored in a separate CSV file `spectral_meta.csv`.

##### 6.2.3.3 Compression

The spectral data is compressible because adjacent time steps have similar amplitude patterns (the amplitudes change slowly between output steps). For binary formats:

- **NPZ:** `numpy.savez_compressed` applies zlib compression. Typical compression ratio: $3$–$5\times$ (the Float64 arrays have correlated entries).
- **HDF5:** gzip or LZF chunk compression. Chunking by output step (one chunk per row) enables efficient row-wise access.
- **MAT:** v7.3 (HDF5-based) with built-in compression.

For CSV: no compression is applied (the text format is already space-inefficient; external gzip is recommended for archival).

##### 6.2.3.4 Typical File Sizes

| Experiment type | $N_{\mathrm{output}}$ | $N_{\mathrm{obs}}$ | Arrays | Uncompressed | Compressed |
|----------------|----------------------|---------------------|--------|-------------|------------|
| Standard (§3.1) | $1000$ | $16$ | $4 \times 1000 \times 16$ | $512$ KB | $\sim 150$ KB |
| Triad (§4.1) | $1000$ | $32$ | $4 \times 1000 \times 32$ | $1.0$ MB | $\sim 300$ KB |
| Cascade (§4.3) | $1000$ | $64$ | $4 \times 1000 \times 64$ | $2.0$ MB | $\sim 600$ KB |
| Pattern (§9.3) | $500$ | $32$ | $4 \times 500 \times 32$ | $512$ KB | $\sim 150$ KB |

The total spectral output for all spectral experiments in the Atlas ($\sim 25$ experiments): $\sim 15$ MB uncompressed, $\sim 5$ MB compressed.

---

#### 6.2.4 Metadata

The spectral file includes the same experiment metadata as the time-series file (§6.1.4), plus spectral-specific metadata:

| Field | Value | Purpose |
|-------|-------|---------|
| `N_obs` | Integer ($16$–$64$) | Number of tracked modes |
| `L` | Float64 | Domain length (needed for eigenvalue computation) |
| `M_star` | Float64 | Equilibrium mobility |
| `P_star_prime` | Float64 | Penalty derivative at equilibrium |
| `eigenvalue_formula` | String: `"(k*pi/L)^2"` | How eigenvalues are computed |
| `decay_rate_formula` | String: `"D*(M_star*mu_k + P_star_prime)"` | How predicted rates are computed |
| `normalization` | String: `"orthonormal_neumann"` | DCT normalization convention |
| `IC_mode` | Integer or list | Which mode(s) were initialized (for purity check) |
| `threshold_act` | Float64 ($10^{-5}$) | Activation threshold for triad detection |

The `normalization` field documents which DCT normalization convention was used to produce the amplitudes. This is critical for cross-implementation comparison: two implementations using different DCT conventions would produce amplitude arrays that differ by a constant factor, and the normalization field enables the consumer to detect and correct this discrepancy.

---

#### 6.2.5 Relationship to the Time-Series File

The spectral file and the time-series file are parallel: they share the same `time` and `step` arrays (identical values, identical ordering). A consumer can join the two files on the `time` column to produce a combined dataset with both scalar observables and per-mode amplitudes.

The relationship is:

| Time-series field | Spectral equivalent |
|------------------|---------------------|
| `a_0` | `amplitudes[:, 0]` (the $k = 0$ column) |
| `C_ED` | $\sum_{k=1}^{N_{\mathrm{obs}}-1}\texttt{modal\_complexity[:, k]}$ + `tail_complexity` |
| `rho_bar` | $\rho^* + \texttt{amplitudes[:, 0]} / \sqrt{L}$ |

These relationships serve as consistency checks: the `a_0` field in the time series must match the first column of the spectral amplitude array to machine precision. A discrepancy indicates a bug in either the time-series or the spectral extraction pipeline.

---

#### 6.2.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Core content** | Signed modal amplitudes $a_k(t)$: $N_{\mathrm{output}} \times N_{\mathrm{obs}}$ array |
| **Derived arrays** | $|a_k|$, $|a_k|^2$, $\mu_k|a_k|^2$: same shape |
| **Per-step scalars** | 7 quantities: total/tail energy, total/tail complexity, 2 centroids, purity |
| **Static arrays** | Mode index, eigenvalue, decay coefficient, decay rate, wavenumber |
| **Index convention** | $k = 0$ (homogeneous), $k = 1, \ldots, N_{\mathrm{obs}}-1$ (spatial) |
| **2D extension** | 3D amplitude array indexed by $(n, k_1, k_2)$ |
| **File naming** | `spectral.{ext}` in the experiment directory |
| **Typical size** | $0.5$–$2$ MB uncompressed per experiment |
| **Metadata** | Experiment metadata + spectral-specific fields ($N_{\mathrm{obs}}$, normalization, formulas) |
| **Consistency with time series** | `time`/`step` arrays identical; `a_0` cross-checked |

The spectral data file is the per-mode companion to the per-step time series. Together, they provide the complete numerical record of every experiment: the time series captures the aggregate dynamics (energy, complexity, dissipation, proximity), and the spectral file captures the mode-resolved dynamics (individual amplitudes, decay rates, triad interactions, cascade structure). Every figure in the Atlas that involves modal information (Figures 3.1–3.8, 4.1–4.9, 9.1, 9.3, 9.4) is generated from the spectral data file.

---

### 6.3 Figure Data Format

The Numerical Atlas specifies 64 figures across 122 panels (§11 of the Atlas). Each figure is described textually — axes, data curves, reference overlays, structural features — but is not rendered. The **figure data files** bridge the gap between the raw simulation output (time-series and spectral files) and the figure descriptions: they contain exactly the data needed to produce each figure, extracted and formatted so that a plotting tool can generate the figure directly without further computation.

The figure data format is the final output of the Suite's data pipeline:

$$
\text{Integration} \to \text{Time series + Spectral file} \to \text{Post-processing} \to \text{Figure data file} \to \text{Rendering.}
$$

The rendering step (the actual plotting) is outside the scope of the Suite — it depends on the user's visualization tool (Matplotlib, Plots.jl, MATLAB, gnuplot, etc.). The figure data format is tool-agnostic: it provides labeled numerical arrays that any plotting tool can consume.

---

#### 6.3.1 Storage Structure

##### 6.3.1.1 One File Per Figure

Each Atlas figure has a single corresponding figure data file:

```
output/figures/fig_{section}.{number}.{ext}
```

Examples: `fig_3.1.csv`, `fig_5.2.h5`, `fig_8.7.npz`.

For figures with sub-panels that draw data from different experiments (e.g., Figure 8.5: two panels, small-amplitude and large-amplitude regime maps from different integration sets), the file contains all panels' data, distinguished by panel-specific prefixes or nested groups.

##### 6.3.1.2 Internal Organization

Each figure data file contains:

1. **A header block** (metadata and column descriptions).
2. **One or more data tables**, one per curve or data series in the figure.
3. **Reference data** (analytic predictions, threshold lines, etc.).

**CSV layout.** For CSV files, the data tables are concatenated vertically, separated by blank lines and section headers:

```
# Figure 3.1: Single-mode exponential decay
# Source: Experiment 3.1, modes n = 1, 2, 3, 4
# Panel: 1 (single panel, semilog-y)
#
# CURVE 1: Mode n = 1
# columns: time, abs_a1
time,abs_a1
0.000e+00,7.071e-04
5.000e-03,7.000e-04
...

# CURVE 2: Mode n = 2
# columns: time, abs_a2
time,abs_a2
0.000e+00,7.071e-04
5.000e-03,6.846e-04
...

# REFERENCE 1: Analytic slope for n = 1
# columns: time, ref_a1
# formula: 7.071e-04 * exp(-2.080 * time)
time,ref_a1
0.0,7.071e-04
5.0,2.265e-08
```

**Binary layout (NPZ/HDF5/MAT).** For binary files, each curve and reference is a named array:

| Key | Shape | Contents |
|-----|-------|----------|
| `curve_1_time` | $(N_1,)$ | Time values for curve 1 |
| `curve_1_abs_a1` | $(N_1,)$ | $|a_1(t)|$ values |
| `curve_2_time` | $(N_2,)$ | Time values for curve 2 |
| `curve_2_abs_a2` | $(N_2,)$ | $|a_2(t)|$ values |
| `ref_1_time` | $(2,)$ | Endpoints for reference line 1 |
| `ref_1_abs_a1` | $(2,)$ | Endpoint values |
| ... | ... | ... |

The curves may have different lengths (e.g., mode $n = 4$ reaches the noise floor before mode $n = 1$ and has fewer data points). The binary format handles this naturally (each array has its own length); the CSV format uses separate sections.

---

#### 6.3.2 Referencing

##### 6.3.2.1 Figure-to-Experiment Mapping

Each figure data file records which experiment(s) produced the underlying data:

| Metadata field | Value | Purpose |
|---------------|-------|---------|
| `atlas_figure` | `"3.1"` | The Atlas figure number |
| `atlas_section` | `"3.1.2"` | The Atlas section containing the figure description |
| `figure_title` | `"Single-mode exponential decay"` | The title from the Atlas |
| `source_experiments` | `["3.1a", "3.1b", "3.1c", "3.1d"]` | List of experiment IDs |
| `source_files` | `["exp_3.1/n1/timeseries.csv", ...]` | Paths to the raw data files |
| `panel_count` | `1` | Number of panels |
| `panel_layout` | `"1x1"` | Panel arrangement |

The `source_experiments` and `source_files` fields establish the provenance chain: from the figure data file, the reader can trace back to the raw simulation output, and from there to the experiment specification and parameter record. This chain is the traceability requirement of §0.3 (Principle 5).

##### 6.3.2.2 Curve-to-Source Mapping

Each curve in the figure data file is annotated with its data source:

| Annotation | Value | Purpose |
|-----------|-------|---------|
| `curve_id` | `"mode_n1"` | Unique identifier within the figure |
| `source_experiment` | `"3.1a"` | Which experiment |
| `source_file` | `"exp_3.1/n1/spectral.csv"` | Which raw data file |
| `source_field` | `"abs_amplitudes[:, 1]"` | Which field/column in the raw file |
| `extraction` | `"direct"` or `"fit"` or `"derived"` | How the data was obtained |
| `description` | `"|a_1(t)| from Experiment 3.1a"` | Human-readable label |

The `extraction` field distinguishes three types of figure data:

- **Direct:** The curve is a column (or slice) of the raw time-series or spectral file, with no transformation. Example: $|a_1(t)|$ is directly the `abs_amplitudes[:, 1]` column of the spectral file.
- **Fit:** The curve is derived from a fitting procedure applied to the raw data. Example: the reference line with slope $-D\alpha_1$ is computed from the analytic formula, not extracted from the data.
- **Derived:** The curve is computed from multiple raw-data columns or from multiple experiments. Example: the spectral-gap ratio $\|\rho - \bar{\rho}\|_{L^2}/|a_0(t)|$ (Figure 3.4, right panel) is the quotient of two time-series fields.

##### 6.3.2.3 Reference Overlays

Analytic reference curves (dashed lines, threshold markers, etc.) are stored alongside the data curves with a `type` annotation:

| Annotation | Value | Meaning |
|-----------|-------|---------|
| `type` | `"data"` | Numerical data from the integration |
| `type` | `"analytic"` | Analytic prediction (computed from parameters, not from data) |
| `type` | `"threshold"` | A fixed threshold value (horizontal or vertical line) |
| `type` | `"fit"` | A fitted curve (e.g., a regression line through the data) |

The distinction between `data` and `analytic` is critical for the Atlas's purpose: the figures demonstrate that the *data* matches the *analytic predictions*. A figure data file that mixes the two without labeling them would obscure the comparison.

---

#### 6.3.3 Reproducibility Requirements

The figure data format is the terminal point of the reproducibility chain. A figure is considered reproducible if an independent implementation can produce a figure data file whose numerical content matches the original to within stated tolerances.

##### 6.3.3.1 Deterministic Extraction

The extraction of figure data from raw simulation output must be deterministic: given the same raw files and the same extraction procedure, the figure data file is identical (bitwise, for direct extractions; to within fitting tolerance, for fit-based extractions). The extraction procedure is specified in the figure data file's metadata:

| Field | Value | Purpose |
|-------|-------|---------|
| `extraction_procedure` | Free-text description | How each curve was extracted from the raw data |

Example for Figure 3.1:

```
extraction_procedure: >
  For each mode n = 1, 2, 3, 4:
    1. Load spectral file exp_3.1/n{n}/spectral.{ext}
    2. Extract column abs_amplitudes[:, n]
    3. Extract column time[:]
    4. Truncate at t_floor: discard rows where abs_amplitudes[:, n] < 1e-14
    5. Store as curve_{n} with columns (time, abs_a{n})
  For each reference line:
    1. Compute D_alpha_n = D * (M_star * mu_n + P_star_prime)
    2. Compute two endpoints: (0, a_n(0)) and (T, a_n(0) * exp(-D_alpha_n * T))
    3. Store as ref_{n} with columns (time, ref_a{n})
```

This free-text procedure is human-readable and unambiguous. An independent implementor can follow the steps to reproduce the figure data from the raw files.

##### 6.3.3.2 Tolerance for Numerical Curves

Two figure data files (from independent implementations) are considered **matching** if, for each data curve:

$$
\max_i\left|\frac{y_i^{(1)} - y_i^{(2)}}{|y_i^{(1)}| + \epsilon_{\mathrm{abs}}}\right| < \epsilon_{\mathrm{fig}},
$$

where $y_i^{(1)}$ and $y_i^{(2)}$ are the $i$-th data values from the two implementations, $\epsilon_{\mathrm{abs}} = 10^{-12}$ prevents division by zero for values near zero, and $\epsilon_{\mathrm{fig}} = 10^{-3}$ ($0.1\%$ relative tolerance) is the default figure-data matching tolerance.

The $0.1\%$ tolerance is tighter than the $1\%$–$5\%$ tolerances used for the physical observables (decay rates, amplitude ratios) because the figure data is derived from converged integrations at high resolution, where the implementation-to-implementation variation is dominated by floating-point rounding ($\sim 10^{-12}$), not by truncation error. The $0.1\%$ tolerance provides a meaningful test of implementation agreement while allowing for platform-dependent rounding.

##### 6.3.3.3 Tolerance for Analytic Reference Curves

Analytic reference curves are computed from the parameter record and do not depend on the integration. Two implementations must produce identical analytic references to machine precision:

$$
\max_i|y_i^{(1)} - y_i^{(2)}| < 10^{-12}.
$$

A discrepancy in the analytic references indicates a disagreement in the parameter values or the analytic formulas — a more serious issue than a discrepancy in the numerical data.

##### 6.3.3.4 Figure Registry

The Suite maintains a **figure registry** — a table listing every Atlas figure with its source experiments, extraction procedure, and expected visual features:

| Figure | Source experiments | Extraction type | Key visual feature |
|--------|-------------------|----------------|-------------------|
| 1.1 | 1.1 (4 resolutions) | Derived (error vs. $h$) | Convergence slopes 2, 2, exponential |
| 1.2 | 1.2 | Direct (energy, channels) | Monotonic $\mathcal{E}$; channel crossover |
| 3.1 | 3.1a–d | Direct (modal amplitudes) | Four parallel semilog lines |
| 4.3 | 4.3 (21 pairs) | Derived (compliance matrix) | No false positives |
| 5.5 | 5.5 (2 profiles) | Direct + derived | Sharp profile vanishes $100\times$ faster |
| 8.5 | 8.5 ($81 \times 2$ runs) | Derived (regime map) | Blue/red classification matches $\Sigma$ |
| ... | ... | ... | ... |

The registry serves as the lookup table for the figure-generation pipeline: given a figure number, the pipeline consults the registry to determine which experiments to load, which extraction to apply, and which visual features to verify in the output.

---

#### 6.3.4 Post-Processing Pipeline

The figure data files are generated by a post-processing pipeline that runs after all integrations are complete. The pipeline is a sequence of deterministic operations:

1. **Load the figure registry.** Identify all 64 figures and their source experiments.

2. **For each figure:**
   - **Load the raw data.** Read the time-series and/or spectral files from the source experiments.
   - **Apply the extraction procedure.** Extract the data curves, compute derived quantities, and generate analytic references.
   - **Write the figure data file.** Store the extracted curves, references, and metadata in the figure data format.
   - **Verify the visual features.** Run automated checks for the key visual features (e.g., "four parallel semilog lines" → check that the four fitted slopes differ by $< 5\%$ from the analytic rates; "no false positives" → check the compliance matrix for zero non-predicted activations).

3. **Generate the figure summary.** Produce a table listing all 64 figures with their verification status (pass/fail for each key visual feature).

The pipeline is deterministic and reproducible: given the same raw data files, it produces identical figure data files. The automated verification in Step 2d is not a substitute for visual inspection (some features, like "the spiral is visibly deformed," are difficult to automate), but it catches the most common failures (wrong slopes, missing curves, incorrect normalization).

---

#### 6.3.5 Summary

| Aspect | Specification |
|--------|--------------|
| **One file per figure** | `output/figures/fig_{section}.{number}.{ext}` |
| **Content** | Data curves + analytic references + metadata |
| **Curve annotation** | Source experiment, source file, source field, extraction type, description |
| **Reference annotation** | Type (data / analytic / threshold / fit) |
| **Provenance** | Figure → experiment → raw data → parameter record (fully traceable) |
| **Extraction procedure** | Documented in the file metadata (human-readable, step-by-step) |
| **Numerical tolerance** | $0.1\%$ relative for data curves; machine precision for analytic references |
| **Figure registry** | 64-entry table mapping every Atlas figure to its sources, extraction, and key features |
| **Post-processing pipeline** | Load → extract → write → verify (deterministic, automated) |
| **Visual feature verification** | Automated checks for slopes, compliance, orderings; supplements visual inspection |

The figure data format closes the loop between computation and publication. Every curve in every Atlas figure is traceable to a specific field in a specific raw data file, extracted by a documented procedure, and verifiable against a stated tolerance. An independent implementor who produces matching figure data files has, by construction, reproduced the entire numerical content of the Numerical Atlas.

---

### 6.4 Metadata Schema

Every output file produced by the simulation engine — time series, spectral data, snapshots, diagnostics, figure data, checkpoints — carries a metadata block that identifies the experiment, the parameters, and the computational environment. The metadata schema is the formal specification of this block: the field names, their types, their permitted values, and which fields are required versus optional. A file that conforms to the schema is self-describing; a reader can determine what was computed, with what parameters, on what platform, without consulting any external document.

---

#### 6.4.1 Schema Overview

The metadata schema has three groups, reflecting three levels of identification:

| Group | Question answered | Fields | Where defined |
|-------|------------------|--------|---------------|
| **Run metadata** | *What* was computed? | Experiment ID, IC, method, resolution, timing | §6.4.2 |
| **Parameter metadata** | *With what* parameters? | Canonical parameters, constitutive functions, derived quantities | §6.4.3 |
| **Environment metadata** | *On what* platform? | Language, libraries, hardware, timestamps | §6.4.4 |

All three groups are required in every output file. The schema is the same across all file types (time series, spectral, figure data, etc.); specific file types may add type-specific fields (e.g., `N_obs` in the spectral file, §6.2.4) but never omit schema fields.

---

#### 6.4.2 Run Metadata

The run metadata identifies the specific computation that produced the file: which experiment, which initial condition, which numerical method, and which resolution and timing parameters were used.

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `experiment_id` | String | Yes | Atlas experiment number | `"3.1a"` |
| `atlas_section` | String | Yes | Atlas section reference | `"3.1.2"` |
| `atlas_figure` | String | No | Atlas figure this file supports | `"3.1"` |
| `IC_type` | String | Yes | Initial condition type | `"A"` |
| `IC_amplitude` | Float64 | Yes | Perturbation amplitude $A$ | `1.0e-03` |
| `IC_mode` | Int or List | No | Mode number(s) for IC-A/B | `1` |
| `IC_sigma` | Float64 | No | Gaussian width for IC-C | `0.05` |
| `IC_x0` | Float64 | No | Gaussian center for IC-C | `0.5` |
| `IC_delta` | Float64 | No | Margin for IC-D | `0.05` |
| `IC_v0` | Float64 | Yes | Initial participation | `0.0` |
| `method` | String | Yes | Spatial method + time-stepping scheme | `"FD_CrankNicolson"` |
| `dimension` | Int | Yes | Spatial dimension $d$ | `1` |
| `domain_L` | Float64 or List | Yes | Domain length(s) | `1.0` |
| `N` | Int or List | Yes | Grid points or spectral modes | `512` |
| `h` | Float64 or List | No | Grid spacing (Method A only) | `1.949e-03` |
| `dt` | Float64 | Yes | Nominal time step $\Delta t_0$ | `5.0e-04` |
| `T_final` | Float64 | Yes | Final integration time | `5.0` |
| `output_mode` | String | Yes | Sampling mode | `"uniform"` |
| `output_interval` | Int | No | $k_{\mathrm{out}}$ (uniform mode) | `50` |
| `output_times` | List[Float64] | No | Prescribed times (prescribed mode) | `[0.01, 0.1, ...]` |
| `n_output` | Int | Yes | Number of output records produced | `1001` |
| `n_steps` | Int | Yes | Total integration steps completed | `50000` |

**Permitted values for `method`:**

| Value | Meaning |
|-------|---------|
| `"FD_ImplicitEuler"` | Method A, implicit Euler (§1.4.1.1) |
| `"FD_CrankNicolson"` | Method A, Crank–Nicolson (§1.4.1.2) |
| `"SPEC_ETDRK2"` | Method B, ETD-RK2 (§1.4.2.1) |
| `"SPEC_ETDRK4"` | Method B, ETD-RK4 (§1.4.2.2) |

**Permitted values for `IC_type`:**

| Value | Meaning |
|-------|---------|
| `"A"` | Single-mode cosine (§2.1.4) |
| `"B"` | Multi-mode superposition (§2.1.4) |
| `"C"` | Localized Gaussian (§2.1.4) |
| `"D"` | Near-capacity (§2.1.4) |
| `"Homogeneous"` | Spatially constant (§2.1.4) |
| `"Custom"` | User-defined (formula stored in `IC_formula` field) |
| `"Driven"` | Driven system with source term (§9.4 of Atlas) |

---

#### 6.4.3 Parameter Metadata

The parameter metadata records the canonical parameters, the constitutive functions, and all derived quantities needed to interpret the results and to reproduce the experiment.

##### 6.4.3.1 Canonical Parameters

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `parameter_set` | String | Yes | Set name or `"Custom"` | `"II"` |
| `D` | Float64 | Yes | Direct-channel weight | `0.6` |
| `H` | Float64 | Yes | Mediated-channel weight ($= 1 - D$) | `0.4` |
| `zeta` | Float64 | Yes | Participation damping | `0.5` |
| `tau` | Float64 | Yes | Participation time scale | `1.0` |
| `rho_star` | Float64 | Yes | Penalty equilibrium density | `0.5` |
| `rho_max` | Float64 | Yes | Capacity bound | `1.0` |

##### 6.4.3.2 Constitutive Parameters

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `constitutive_type` | String | Yes | Constitutive family name | `"PowerLawLinear"` |
| `M0` | Float64 | Yes | Mobility amplitude | `1.0` |
| `beta` | Float64 | Yes | Mobility collapse exponent | `2.0` |
| `P0` | Float64 | Yes | Penalty slope | `1.0` |
| `M_formula` | String | No | Mobility function formula | `"M0 * (rho_max - rho)^beta"` |
| `P_formula` | String | No | Penalty function formula | `"P0 * (rho - rho_star)"` |

The formula fields are human-readable strings included for documentation. They are not parsed or evaluated by the engine; they are informational only. For non-default constitutive types (§4.3), the formulas are essential for reproducibility (the `constitutive_type` name alone may not uniquely identify the function).

##### 6.4.3.3 Derived Quantities

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `Delta` | Float64 | Yes | $D + 2\zeta$ | `1.6` |
| `M_star` | Float64 | Yes | $M(\rho^*)$ | `0.25` |
| `M_star_prime` | Float64 | Yes | $M'(\rho^*)$ | `-1.0` |
| `P_star_prime` | Float64 | Yes | $P'(\rho^*)$ | `1.0` |
| `discriminant` | Float64 | Yes | $\mathscr{D}_0$ | `-1.59` |
| `gamma_0` | Float64 | Yes | $(DP_*' + \zeta/\tau)/2$ | `0.55` |
| `omega` | Float64 | Yes | $\sqrt{|\mathscr{D}_0|}/2$ (or $0$ if monotonic) | `0.630` |
| `regime` | String | Yes | `"Oscillatory"`, `"Monotonic"`, or `"Critical"` | `"Oscillatory"` |
| `alpha_1` | Float64 | Yes | $M_*\mu_1 + P_*'$ (first modal decay coefficient) | `3.467` |
| `D_alpha_1` | Float64 | Yes | $D\alpha_1$ (first spatial decay rate) | `2.080` |
| `spectral_gap` | Float64 | Yes | $\gamma = \min(\gamma_{\mathrm{hom}}, D\alpha_1)$ | `0.55` |
| `epsilon_0` | Float64 | No | Stability threshold (estimated) | `0.22` |

The derived quantities are *computed* from the canonical and constitutive parameters (not user-specified). Including them in the metadata serves two purposes: (1) the reader can verify the derivation by recomputing from the primary parameters and checking agreement; (2) the reader can access the derived values directly without implementing the derivation formulas.

---

#### 6.4.4 Environment Metadata

The environment metadata records the computational platform on which the integration was performed. This information is not needed to reproduce the experiment (the experiment is fully specified by the run and parameter metadata), but it is essential for diagnosing discrepancies between independent implementations and for certifying the computational provenance.

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `suite_version` | String | Yes | Simulation Suite version | `"1.0.0"` |
| `engine_version` | String | Yes | Simulation engine version | `"1.0.0"` |
| `language` | String | Yes | Implementation language | `"Python"` |
| `language_version` | String | Yes | Language version | `"3.11.5"` |
| `os` | String | Yes | Operating system | `"Linux 6.1"` |
| `architecture` | String | Yes | CPU architecture | `"x86_64"` |
| `numpy_version` | String | No | NumPy version (Python only) | `"1.24.3"` |
| `scipy_version` | String | No | SciPy version (Python only) | `"1.11.2"` |
| `fftw_version` | String | No | FFTW version (Julia only) | `"3.3.10"` |
| `matlab_version` | String | No | MATLAB version | `"R2023a"` |
| `timestamp_start` | String (ISO 8601) | Yes | Integration start time | `"2026-03-26T14:30:00Z"` |
| `timestamp_end` | String (ISO 8601) | Yes | Integration end time | `"2026-03-26T14:30:48Z"` |
| `wall_time_seconds` | Float64 | Yes | Wall-clock duration | `48.3` |
| `hostname` | String | No | Machine hostname | `"compute-node-07"` |
| `cpu_model` | String | No | CPU model | `"Intel Xeon E5-2680 v4"` |
| `n_cores_used` | Int | No | Cores used for this integration | `1` |

**Version fields.** The `suite_version` and `engine_version` fields distinguish the specification (the Suite document) from the implementation (the code that realizes it). A change in the Suite version (e.g., adding a new observable) changes the specification; a change in the engine version (e.g., fixing a bug in the tridiagonal solver) changes the implementation. Both are recorded so that the reader knows exactly which specification and which implementation produced the data.

**Library version fields.** The NumPy, SciPy, FFTW, and MATLAB version fields are environment-specific and are present only for the corresponding language. They are critical for diagnosing floating-point discrepancies: a change in the FFTW version, for instance, can change the DCT rounding behavior and produce $O(10^{-15})$ differences in the spectral coefficients.

---

#### 6.4.5 The Reproducibility Hash

The metadata schema includes a single field that cryptographically summarizes the experiment specification:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec_hash` | String (64 hex chars) | Yes | SHA-256 of the experiment specification |

The hash is computed from the concatenation of the run and parameter metadata fields (in a fixed, documented order), excluding the environment metadata (which is platform-dependent and expected to differ between reproductions):

$$
\texttt{spec\_hash} = \text{SHA-256}\bigl(\texttt{D} \| \texttt{H} \| \texttt{zeta} \| \texttt{tau} \| \texttt{rho\_star} \| \texttt{rho\_max} \| \texttt{M0} \| \texttt{beta} \| \texttt{P0} \| \texttt{IC\_type} \| \texttt{IC\_amplitude} \| \texttt{IC\_v0} \| \texttt{method} \| \texttt{N} \| \texttt{dt} \| \texttt{T\_final}\bigr),
$$

where $\|$ denotes concatenation of the string representations (each value formatted to 15 decimal digits for Float64, or as-is for strings and integers). The hash is deterministic: the same experiment specification always produces the same hash, regardless of the environment.

**Usage.** The `spec_hash` serves three purposes:

1. **Matching.** Two output files with the same `spec_hash` were produced from the same experiment specification. Any difference in their numerical content is attributable to the implementation or environment, not to the specification.

2. **Integrity.** If the reader recomputes the hash from the metadata fields and it does not match the stored `spec_hash`, the metadata may have been corrupted or tampered with.

3. **Checkpoint validation.** The restart logic (§2.5.3) compares the checkpoint's `spec_hash` to the current experiment's hash; a mismatch rejects the checkpoint.

---

#### 6.4.6 Schema Validation

When a file is read (by the post-processing pipeline, the figure generator, or an external consumer), the metadata is validated against the schema:

| Check | Condition | Severity |
|-------|-----------|----------|
| All required fields present | Every field marked "Required" in §§6.4.2–6.4.4 has a non-null value | Fatal (reject file) |
| Type correctness | Each field has the declared type (Float64, Int, String, etc.) | Fatal |
| Range validity | Canonical parameters satisfy §2.2.3 Level 1 checks ($0 < D < 1$, $\zeta > 0$, etc.) | Warning |
| Complementarity | $|H - (1 - D)| < 10^{-15}$ | Warning |
| Derived consistency | $|\Delta - (D + 2\zeta)| < 10^{-12}$ | Warning |
| Discriminant consistency | $|\mathscr{D}_0 - ((DP_*' - \zeta/\tau)^2 - 4HP_*'/\tau)| < 10^{-10}$ | Warning |
| Regime consistency | `regime` matches $\operatorname{sign}(\mathscr{D}_0)$ | Warning |
| Hash integrity | Recomputed hash matches stored `spec_hash` | Warning |
| Version present | `suite_version` and `engine_version` are non-empty | Warning |
| Timestamp valid | `timestamp_start` and `timestamp_end` parse as ISO 8601 | Warning |

Fatal checks prevent corrupted or incomplete files from entering the analysis pipeline. Warning checks flag potential issues (metadata inconsistency, version mismatch) without blocking the analysis — the reader may choose to accept the file despite warnings if the discrepancy is understood and benign.

---

#### 6.4.7 Storage Format

The metadata is stored differently in each file format:

| Format | Storage mechanism | Access |
|--------|------------------|--------|
| **CSV** | Comment lines at the top, prefixed by `#`. Each field on its own line: `# field_name: value` | Parsed by reading lines starting with `#` |
| **NPZ** | A dedicated key `"metadata"` containing a serialized dictionary (via `numpy.savez`) | `data["metadata"].item()` returns the dict |
| **HDF5** | Attributes on the root group (`/`). Each field is an attribute: `f.attrs["D"] = 0.6` | `f.attrs["D"]` returns the value |
| **MAT** | A struct variable `metadata` containing one field per schema entry | `data.metadata.D` returns the value |

The CSV storage is the most verbose (a 40-line header for the full schema) but the most portable (any text editor can read it). The binary formats are compact but require a library to read.

---

#### 6.4.8 Summary

| Aspect | Specification |
|--------|--------------|
| **Three groups** | Run (what), Parameter (with what), Environment (on what) |
| **Run fields** | 22 fields: experiment ID, IC, method, resolution, timing |
| **Parameter fields** | 19 fields: 7 canonical + 6 constitutive + 12 derived |
| **Environment fields** | 16 fields: versions, OS, architecture, timestamps, hardware |
| **Reproducibility hash** | SHA-256 of run + parameter fields (excludes environment) |
| **Schema validation** | 10 checks on read (fatal for missing/mistyped fields; warning for inconsistencies) |
| **Total fields** | 58 (including the hash) |
| **Storage** | CSV comments / NPZ dict / HDF5 attributes / MAT struct |

The metadata schema is the identity card of every output file. It answers three questions — what was computed, with what parameters, on what platform — completely and unambiguously. A file conforming to the schema carries its full provenance: an independent reader can reproduce the experiment, verify the derived quantities, and diagnose any discrepancy, using nothing but the information in the metadata block itself.

---

### 6.5 Versioning

The Simulation Suite and its implementations evolve over time — bugs are fixed, new observables are added, constitutive families are extended, and the post-processing pipeline gains new figure types. The versioning system ensures that every output file is tagged with the exact specification and implementation that produced it, that older files remain interpretable by newer readers, and that breaking changes are communicated clearly.

---

#### 6.5.1 Version Numbers

The versioning system uses two independent version numbers, recorded in every output file (§6.4.4):

##### 6.5.1.1 Suite Version (`suite_version`)

The **Suite version** identifies the version of this specification document — the Simulation Suite itself. It governs:

- The metadata schema (§6.4): which fields exist, their types, and their semantics.
- The data formats (§§6.1–6.3): the structure of the time-series, spectral, and figure data files.
- The observable definitions (§5): the formulas used to compute each observable.
- The experiment templates (§3): the structure of experiment specifications.
- The validation criteria (§2.7): the acceptance thresholds for convergence tests.

A change to any of these specification-level elements increments the Suite version. The current version is **1.0.0**.

##### 6.5.1.2 Engine Version (`engine_version`)

The **Engine version** identifies the version of a specific implementation of the Suite — the executable code that performs the integrations. Different implementations (Python, Julia, MATLAB) have their own independent engine versions. The engine version governs:

- The algorithms: the specific implementation of the time-stepping schemes, spatial discretizations, and observable extraction routines.
- The bug fixes: corrections to implementation errors that do not change the specification.
- The performance optimizations: changes to the computational strategy that do not affect the output (e.g., parallelization improvements, memory layout changes).

A change to any implementation-level element increments the engine version. The engine version is implementation-specific and starts at **1.0.0** for each implementation.

##### 6.5.1.3 Relationship

The two versions are independent but related:

- A single Suite version may have multiple engine versions (different implementations, or successive bug-fix releases of the same implementation).
- A single engine version implements exactly one Suite version (the engine is built to a specific specification).
- The engine's metadata records both versions, so the reader always knows which specification was targeted and which implementation was used.

---

#### 6.5.2 Semantic Versioning

Both the Suite version and the engine version follow **semantic versioning** (SemVer): a three-part version number `MAJOR.MINOR.PATCH` with specific rules for when each part is incremented.

##### 6.5.2.1 Version Format

$$
\texttt{MAJOR.MINOR.PATCH}
$$

- **MAJOR** ($X$.0.0): Incremented for breaking changes that are not backward-compatible. A reader or implementation built for Suite $X$ cannot, in general, correctly process files from Suite $X+1$ (or vice versa) without modification.
- **MINOR** ($X$.$Y$.0): Incremented for backward-compatible additions. A reader built for Suite $X.Y$ can correctly process files from Suite $X.Y'$ for any $Y' \leq Y$ (older files are readable by newer readers).
- **PATCH** ($X$.$Y$.$Z$): Incremented for backward-compatible corrections that do not change the specification's content (typo fixes, clarifications, editorial improvements).

##### 6.5.2.2 Suite Version Increment Rules

| Change type | Example | Version increment |
|------------|---------|-------------------|
| New required metadata field | Adding `epsilon_0` to the schema | MINOR (older files lack the field; reader fills with default or "unknown") |
| New optional metadata field | Adding `cpu_model` | MINOR |
| New observable in time series | Adding field #25 `spectral_centroid_C` | MINOR (older files have 24 columns; reader ignores the missing field) |
| Changed observable formula | Redefining `D_diff` to use full $P'/M$ instead of $P_*'$ | MAJOR (the same field name now means something different) |
| New IC type | Adding `IC_type = "Driven"` | MINOR |
| Changed validation threshold | Changing decay-rate tolerance from $1\%$ to $0.5\%$ | MINOR (stricter threshold; older results may no longer pass) |
| Removed field | Dropping `energy_kinetic` from the time series | MAJOR (older readers expect the field) |
| New experiment in the Atlas | Adding Experiment 9.6 | MINOR (no existing data is affected) |
| Rewritten §5.6 (convergence rate extraction) | Different fitting interval or smoothing method | MAJOR (changes the extracted values) |
| Typo correction in the text | Fixing a formula typo that does not affect implementations | PATCH |

##### 6.5.2.3 Engine Version Increment Rules

| Change type | Example | Version increment |
|------------|---------|-------------------|
| Bug fix (changes output) | Correcting an off-by-one in the Neumann boundary stencil | MINOR (the output changes, but the specification was already correct) |
| Bug fix (no output change) | Fixing a memory leak that did not affect computed values | PATCH |
| Performance optimization | Replacing the tridiagonal solver with a faster implementation | PATCH (no output change) |
| New feature | Adding support for 3D domains | MINOR |
| Suite version upgrade | Implementing a new observable required by Suite 1.1.0 | MINOR (the engine now targets Suite 1.1.0) |
| Algorithmic change | Switching from Thomas algorithm to LU factorization | PATCH (if output is identical) or MINOR (if output changes at rounding level) |

---

#### 6.5.3 Compatibility Guarantees

The versioning system provides three levels of compatibility guarantee.

##### 6.5.3.1 Forward Compatibility (Older Reader, Newer File)

A reader built for Suite version $X.Y$ can process a file produced by Suite version $X.Y'$ with $Y' \geq Y$ (a file from the same or a newer minor version) under the following conditions:

- **New optional fields are ignored.** If the file contains metadata fields or data columns that the reader does not recognize (because they were added in a newer minor version), the reader skips them without error.
- **New required fields are filled with defaults.** If the reader requires a field that the file does not contain (because the file was produced by an older minor version — the reverse of the typical forward-compatibility scenario), the reader fills the missing field with a documented default value or with `"unknown"`.

Forward compatibility across MAJOR versions is not guaranteed. A file from Suite $2.0.0$ may have a different schema, different field semantics, or a different file structure that a Suite $1.x$ reader cannot interpret.

##### 6.5.3.2 Backward Compatibility (Newer Reader, Older File)

A reader built for Suite version $X.Y$ can process a file produced by Suite version $X.Y'$ with $Y' \leq Y$ (a file from the same or an older minor version):

- **Missing optional fields are filled with defaults.** Fields added in versions $Y' + 1$ through $Y$ are filled with `"unknown"` or a computed default (e.g., `spectral_gap` can be recomputed from $D$, $\alpha_1$, and $\gamma_0$ if the field is missing).
- **All required fields from the older version are present.** No field is removed within a major version, so the older file always has the fields the newer reader expects (at the older version's specification level).

Backward compatibility across MAJOR versions is provided on a best-effort basis. The reader may attempt to read a Suite $1.x$ file when running Suite $2.x$, but success is not guaranteed.

##### 6.5.3.3 Cross-Implementation Compatibility

Files produced by different implementations (Python, Julia, MATLAB) at the same Suite version are interchangeable:

- The metadata schema is identical (the same field names, types, and semantics).
- The data arrays contain the same fields in the same order with the same semantics.
- The numerical values agree to within the convergence tolerances (§2.7) — not bitwise, but structurally.

The `spec_hash` (§6.4.5) provides the definitive compatibility check: two files with the same `spec_hash` were produced from the same experiment specification, regardless of the implementation. Their numerical content should match to within $\epsilon_{\mathrm{fig}} = 10^{-3}$ for data curves (§6.3.3.2).

---

#### 6.5.4 Version History

The version history is maintained as a change log that documents every version increment with the date, the change description, and the compatibility impact.

**Suite version history:**

| Version | Date | Change | Impact |
|---------|------|--------|--------|
| 1.0.0 | 2026-03 | Initial release | Baseline |

**Engine version history** (per implementation):

| Implementation | Version | Date | Change | Impact |
|---------------|---------|------|--------|--------|
| Python | 1.0.0 | 2026-03 | Initial release | Baseline |
| Julia | 1.0.0 | 2026-03 | Initial release | Baseline |
| MATLAB | 1.0.0 | 2026-03 | Initial release | Baseline |

Future changes are appended to this table. Each entry includes a compatibility annotation: "backward-compatible" (MINOR/PATCH) or "breaking" (MAJOR).

---

#### 6.5.5 Version Checking at Runtime

The simulation engine performs version checks at two points during execution.

##### 6.5.5.1 At Initialization

The engine verifies that its `engine_version` targets the current `suite_version`:

- If the engine targets a Suite version *newer* than the current Suite specification (e.g., engine targets Suite 1.2.0 but the specification is 1.1.0): warning ("Engine targets a newer Suite version than this specification; some features may not be documented").
- If the engine targets a Suite version *older* than the current Suite specification: warning ("Engine targets an older Suite version; some new features may not be available").
- If the MAJOR versions differ: fatal error ("Incompatible Suite version").

##### 6.5.5.2 At Checkpoint Restart

The restart logic (§2.5.3) compares the checkpoint's `suite_version` and `engine_version` to the current values:

- Same Suite MAJOR and engine MAJOR: proceed (compatible).
- Different Suite MINOR or engine MINOR: proceed with warning ("Minor version mismatch; output may differ at rounding level").
- Different Suite MAJOR or engine MAJOR: fatal error ("Cannot restart from an incompatible checkpoint").

The `spec_hash` check (§2.5.3, Step 2) provides an additional safeguard: even if the versions match, a `spec_hash` mismatch rejects the checkpoint (the experiment specification has changed despite the version match, which should not happen in a correctly versioned system).

---

#### 6.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Two version numbers** | `suite_version` (specification) and `engine_version` (implementation) |
| **Format** | Semantic versioning: `MAJOR.MINOR.PATCH` |
| **MAJOR increment** | Breaking changes (schema changes, formula redefinitions, field removals) |
| **MINOR increment** | Backward-compatible additions (new fields, new observables, new IC types) |
| **PATCH increment** | Corrections with no content change (typos, clarifications, performance) |
| **Forward compatibility** | Within same MAJOR: newer files readable by older readers (unknown fields ignored) |
| **Backward compatibility** | Within same MAJOR: older files readable by newer readers (missing fields defaulted) |
| **Cross-implementation** | Same Suite version → same schema, same semantics, same `spec_hash` |
| **Runtime checks** | At initialization (version targeting) and at restart (version + hash match) |
| **Current version** | Suite 1.0.0, Engine 1.0.0 (all implementations) |

The versioning system ensures that the reproducibility guarantee of the Suite extends across time: a file produced today can be read, interpreted, and compared against a file produced years from now, as long as the MAJOR version has not changed. The version numbers, stored in every file's metadata (§6.4.4), are the temporal anchors that bind each output to the specification that defined it and the implementation that computed it.

---

## 7. Reproducibility Guarantees

### 7.1 Random Seed Control

The canonical ED system (C.1) is deterministic: given an initial condition $(\rho_0, v_0)$ and the canonical parameters, the solution is uniquely determined for all time (Theorem C.2). The simulation engine inherits this determinism — the numerical solution at every time step is a deterministic function of the initial condition, the parameters, the discretization, and the time-stepping scheme. No random number generator is invoked during any standard integration.

This subsection specifies why randomness could nevertheless enter the computation, how it is controlled when it does, and what reproducibility guarantees the engine provides.

---

#### 7.1.1 Sources of Potential Non-Determinism

Although the core integration is deterministic, several scenarios can introduce non-determinism into the computation or its environment.

##### 7.1.1.1 Stochastic Initial Conditions

Some future extensions of the Atlas may require stochastic initial conditions — density fields with random spatial structure, used to test the robustness of the architectural predictions against initial-condition variability. These are not part of the current Atlas (all 55 experiments use deterministic ICs: cosines, Gaussians, or explicit formulas), but the Suite specification supports them.

**Example.** A random multi-mode initial condition:

$$
\rho_0(x) = \rho^* + \sum_{n=1}^{N_m}A_n\cos(n\pi x/L), \qquad A_n \sim \mathcal{N}(0, \sigma_n^2),
$$

where the amplitudes $A_n$ are drawn from independent Gaussian distributions. The resulting density field is different for each draw, and the integration outcome depends on the specific realization.

##### 7.1.1.2 Stochastic Forcing

The driven-system extension (Atlas §9.4, §12.4) may include stochastic forcing terms $S(x, t)$ that model thermal noise or environmental fluctuations. The forcing introduces randomness at every time step, making the solution a stochastic process rather than a deterministic trajectory.

##### 7.1.1.3 Parallel Execution Order

When the sweep orchestrator (§4.5) distributes tasks across multiple cores, the order in which tasks complete is non-deterministic (it depends on the operating system's scheduling, the load on each core, and the wall-clock duration of each task). This does not affect the numerical content of any individual task (each task is deterministic), but it affects the order in which results are written to the sweep output files and the order in which the progress file is updated.

##### 7.1.1.4 Floating-Point Non-Associativity

IEEE 754 floating-point arithmetic is not associative: $(a + b) + c \neq a + (b + c)$ in general, due to rounding. If the order of summation in a reduction operation (e.g., the spatial integral $h\sum_j\Phi(\rho_j)$) depends on the runtime environment (thread scheduling, vectorization width, library internals), the result may differ by $O(\epsilon_{\mathrm{mach}})$ between runs on the same machine. This is not randomness in the mathematical sense, but it produces non-reproducibility at the bit level.

---

#### 7.1.2 Seed Setting

When randomness is used (§7.1.1.1 or §7.1.1.2), the engine controls it through a **global random seed** — a single integer that initializes the pseudorandom number generator (PRNG) at the start of the computation.

##### 7.1.2.1 Seed Specification

The seed is specified in the experiment specification as an optional field:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `random_seed` | Int64 | `None` | PRNG seed. If `None`, no PRNG is used (deterministic mode). |

When `random_seed` is specified (non-`None`):

1. The PRNG is initialized with the given seed at the start of initialization (§2.1), before any random draws.
2. All random draws (IC amplitudes, stochastic forcing samples) are drawn sequentially from the seeded PRNG.
3. The seed is recorded in the metadata (§6.4.2) as a new field `random_seed`.
4. The `spec_hash` (§6.4.5) includes the seed, so that two runs with different seeds produce different hashes.

When `random_seed` is `None` (the default for all current Atlas experiments):

1. No PRNG is initialized.
2. Any attempt to draw a random number raises a fatal error ("Random draw requested but no seed was specified").
3. The `random_seed` field in the metadata is set to `"none"` (a string, not a null value, to distinguish from "not recorded").

##### 7.1.2.2 Environment-Specific PRNG

The PRNG implementation is environment-specific:

| Environment | PRNG | Seed interface |
|-------------|------|---------------|
| Python | NumPy's `default_rng(seed)` (PCG64) | `rng = numpy.random.default_rng(seed)` |
| Julia | `Random.seed!(seed)` (Xoshiro256++) | `Random.seed!(seed)` |
| MATLAB | `rng(seed, 'twister')` (Mersenne Twister) | `rng(seed, 'twister')` |

The PRNG algorithms differ across environments, so the same seed produces *different* random sequences in different environments. This is acceptable: the seed guarantees reproducibility *within* an environment (running the same seed on the same environment twice produces identical results), not *across* environments (the sequences are algorithm-dependent).

Cross-environment reproducibility for stochastic experiments requires specifying the random amplitudes explicitly (as a stored array) rather than regenerating them from a seed. The Suite supports this through the `IC_type = "Custom"` mechanism (§2.1.4): the user provides the amplitudes as an explicit list in the experiment specification, bypassing the PRNG entirely.

---

#### 7.1.3 Deterministic Runs

The vast majority of Atlas experiments — all 55 standard experiments and all parameter sweeps — are deterministic: no PRNG is used, no stochastic forcing is applied, and the output is a deterministic function of the experiment specification.

##### 7.1.3.1 Conditions for Determinism

A run is deterministic if and only if:

1. `random_seed = None` (no PRNG initialized).
2. No stochastic forcing term is specified.
3. The initial condition is deterministic (IC types A, B, C, D, Homogeneous, or Custom with explicit values).

When all three conditions hold, the numerical output depends only on:

- The canonical parameters ($D$, $\zeta$, $\tau$, $\rho^*$, $\rho_{\max}$, $M_0$, $\beta$, $P_0$).
- The initial condition parameters ($A$, $n$, $\sigma$, $x_0$, $\delta$, $v_0$).
- The numerical method and resolution ($N$, $\Delta t$, scheme).
- The floating-point arithmetic of the platform (rounding behavior).

The first three groups are recorded in the metadata and captured by the `spec_hash`. The fourth group is platform-dependent and is the sole source of non-reproducibility in deterministic runs.

##### 7.1.3.2 Platform-Dependent Reproducibility

Within the same platform (same hardware, same OS, same compiler, same library versions): a deterministic run produces bitwise-identical output every time. This is because:

- The computation is sequential (single-threaded within each task, §4.5).
- The order of floating-point operations is fixed by the algorithm specification (§§1.3–1.4).
- No PRNG is invoked.
- The input (parameters + IC) is identical.

Across platforms (different hardware, different OS, or different library versions): a deterministic run produces output that agrees to within $O(\epsilon_{\mathrm{mach}}) \sim 10^{-15}$ per operation, accumulating to $O(N_{\mathrm{steps}} \cdot \epsilon_{\mathrm{mach}}) \sim 10^{-10}$ over a full integration. This is far below any observable tolerance ($1\%$–$5\%$) and is structurally invisible — no Atlas figure, no decay rate, and no amplitude ratio is affected by this level of variation.

The platform-dependent variation arises from:

- Different rounding modes in the IEEE 754 implementation (all platforms use round-to-nearest-even, but the intermediate precision of fused multiply-add operations may differ).
- Different summation orders in library functions (e.g., NumPy's `sum` may use pairwise summation while Julia's `sum` may use sequential summation, producing different rounding).
- Different DCT implementations (FFTW vs. SciPy's internal FFT vs. MATLAB's FFT, each with different butterfly orderings and twiddle-factor computations).

These differences are normal and expected. They do not constitute a reproducibility failure.

---

#### 7.1.4 Reproducibility Guarantees

The Suite provides three tiers of reproducibility guarantee, each with a specific scope and tolerance.

##### 7.1.4.1 Tier 1: Bitwise Reproducibility (Same Platform, Same Run)

**Scope.** Same implementation, same hardware, same OS, same library versions, same experiment specification.

**Guarantee.** The output is bitwise identical across runs. Every floating-point value in the time-series, spectral, and figure data files is identical bit-for-bit.

**Mechanism.** The computation is deterministic and sequential. No source of non-determinism is present (no PRNG, no parallel scheduling, no non-deterministic library calls).

**Verification.** Compute the SHA-256 hash of the entire output file. Two runs on the same platform with the same `spec_hash` should produce identical file hashes.

##### 7.1.4.2 Tier 2: Numerical Reproducibility (Same Implementation, Different Platform)

**Scope.** Same implementation (e.g., Python), different hardware or OS.

**Guarantee.** The output agrees to within $O(N_{\mathrm{steps}} \cdot \epsilon_{\mathrm{mach}})$ — typically $< 10^{-10}$ in absolute terms. All structural features (regime classification, zero-crossing counts, decay-rate signs) are identical. All quantitative observables (decay rates, frequencies, amplitude ratios) agree to within $0.001\%$.

**Mechanism.** The algorithm is identical; only the floating-point rounding differs.

**Verification.** Compare the time-series files field-by-field: $\max_n|Q_n^{(1)} - Q_n^{(2)}|/(|Q_n^{(1)}| + 10^{-12}) < 10^{-8}$ for each observable $Q$.

##### 7.1.4.3 Tier 3: Structural Reproducibility (Different Implementation)

**Scope.** Different implementations (e.g., Python vs. Julia vs. MATLAB) at the same Suite version.

**Guarantee.** The output agrees to within the convergence tolerances of §2.7: $1\%$–$5\%$ for physical observables, $0.1\%$ for figure data curves, exact agreement for qualitative features (regime classification, zero-crossing counts, selection-rule compliance). All four validation tests (§2.7.4) pass.

**Mechanism.** The specification (this document) is the same; the implementations differ in the algorithms' low-level details (library calls, DCT implementations, solver routines). The convergence testing (§2.7) ensures that the discretization error dominates the implementation-dependent variation.

**Verification.** Compare the extracted scalar observables ($\hat{\sigma}_k$, $\hat{\omega}$, $\bar{R}_{31}$, $t_*$) across implementations. All must agree within the acceptance criteria of §2.7.3.3.

---

#### 7.1.5 Metadata for Reproducibility

All reproducibility-relevant information is captured in the metadata schema (§6.4):

| Reproducibility tier | Key metadata fields |
|---------------------|---------------------|
| Tier 1 (bitwise) | `spec_hash`, `engine_version`, `language_version`, `numpy_version` (etc.), `hostname`, `timestamp` |
| Tier 2 (numerical) | `spec_hash`, `engine_version`, `language` |
| Tier 3 (structural) | `spec_hash`, `suite_version` |

The `spec_hash` is the universal reproducibility key: two files with the same `spec_hash` are guaranteed to be from the same experiment, regardless of the platform or implementation. The additional fields narrow the scope: at Tier 1, the full environment specification (down to the library version and hostname) is needed to guarantee bitwise identity; at Tier 3, only the Suite version is needed to guarantee structural agreement.

---

#### 7.1.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Core system** | Deterministic (no randomness in the canonical ED PDE) |
| **PRNG usage** | Only for stochastic ICs or forcing (future extensions); controlled by `random_seed` |
| **Default mode** | `random_seed = None`; any random draw is a fatal error |
| **Within-environment seed** | Deterministic sequence from the seed; bitwise reproducible |
| **Cross-environment seed** | Different PRNG algorithms; same seed ≠ same sequence |
| **Cross-environment ICs** | Use explicit amplitude lists (`IC_type = "Custom"`) for cross-environment reproducibility |
| **Tier 1 (bitwise)** | Same platform, same run → identical output (bit-for-bit) |
| **Tier 2 (numerical)** | Same implementation, different platform → agreement $< 10^{-10}$ |
| **Tier 3 (structural)** | Different implementation → agreement within $1\%$–$5\%$ tolerances |
| **Key metadata** | `spec_hash` (universal), `engine_version` (Tier 2), full environment (Tier 1) |

The reproducibility guarantees are not aspirational — they are testable consequences of the Suite's design. Tier 1 is verified by file-hash comparison. Tier 2 is verified by field-by-field numerical comparison. Tier 3 is verified by the four validation tests and the observable acceptance criteria. Every output file carries sufficient metadata to determine which tier of reproducibility applies and to perform the corresponding verification.

---

### 7.2 Environment Capture

The environment metadata (§6.4.4) records the computational platform on which each integration was performed. This subsection specifies *what* is captured, *how* it is collected, and *why* each piece of information matters for reproducibility diagnostics. The environment capture is performed automatically at initialization (§2.1) and requires no user input.

---

#### 7.2.1 Operating System

The operating system determines the floating-point behavior of the standard library functions, the memory alignment of arrays, the default thread model, and the file-system semantics. Two integrations on different operating systems may produce Tier-2 differences (§7.1.4.2) due to differences in the math library's implementation of transcendental functions ($\exp$, $\ln$, $\cos$, $\sin$).

##### 7.2.1.1 Captured Fields

| Field | Source | Example |
|-------|--------|---------|
| `os` | OS name and version | `"Linux 6.1.0"`, `"macOS 14.2"`, `"Windows 11 23H2"` |
| `os_kernel` | Kernel identification string | `"6.1.0-22-generic"` |
| `architecture` | CPU instruction set architecture | `"x86_64"`, `"aarch64"` |

##### 7.2.1.2 Collection Method

| Environment | Method |
|-------------|--------|
| Python | `platform.system()`, `platform.release()`, `platform.machine()` |
| Julia | `Sys.KERNEL`, `Sys.MACHINE`, `Sys.ARCH` |
| MATLAB | `computer`, `version('-release')` |

##### 7.2.1.3 Diagnostic Relevance

The OS fields are the first checkpoint when diagnosing a Tier-2 discrepancy between two runs of the same implementation. If the OS or architecture differs, the transcendental-function rounding may differ, producing $O(\epsilon_{\mathrm{mach}})$ per-call variations that accumulate over $\sim 10^5$ steps. The OS fields identify this as the likely cause and distinguish it from an implementation bug.

The architecture field is particularly relevant for ARM versus x86 comparisons: ARM processors may use different fused-multiply-add behavior (FMA is mandatory on ARMv8, optional on x86), which can change the rounding of products that appear in the constitutive evaluations and the stencil computations.

---

#### 7.2.2 Library Versions

The numerical libraries used by the engine — the linear-algebra solvers, the FFT implementations, and the quadrature routines — are the components most likely to produce Tier-2 differences across platforms. A version change in any of these libraries can alter the internal algorithm (e.g., switching from a radix-2 to a split-radix FFT), the rounding behavior (e.g., using FMA in a new version where the old version did not), or the thread model (e.g., enabling multi-threaded BLAS by default).

##### 7.2.2.1 Captured Fields by Environment

**Python:**

| Field | Source | Example |
|-------|--------|---------|
| `python_version` | `sys.version` | `"3.11.5"` |
| `numpy_version` | `numpy.__version__` | `"1.24.3"` |
| `scipy_version` | `scipy.__version__` | `"1.11.2"` |
| `numpy_blas` | `numpy.show_config()` (BLAS library) | `"openblas 0.3.23"` |
| `numpy_lapack` | `numpy.show_config()` (LAPACK library) | `"openblas 0.3.23"` |

**Julia:**

| Field | Source | Example |
|-------|--------|---------|
| `julia_version` | `VERSION` | `"1.9.3"` |
| `fftw_version` | `FFTW.version` | `"3.3.10"` |
| `diffeq_version` | `Pkg.status("DifferentialEquations")` | `"7.10.0"` |
| `blas_vendor` | `LinearAlgebra.BLAS.vendor()` | `"openblas64"` |

**MATLAB:**

| Field | Source | Example |
|-------|--------|---------|
| `matlab_version` | `version` | `"9.14.0 (R2023a)"` |
| `matlab_toolboxes` | `ver` (relevant toolboxes) | `"Signal Processing 9.2"` |

##### 7.2.2.2 Diagnostic Relevance

The library version fields enable precise diagnosis of Tier-2 discrepancies:

| Scenario | Diagnostic path |
|----------|----------------|
| Two Python runs disagree at $O(10^{-14})$ | Check `numpy_version` and `numpy_blas`. If the BLAS library differs (e.g., OpenBLAS vs. MKL), the tridiagonal solver may round differently. |
| Python and Julia runs disagree at $O(10^{-12})$ | Expected: different PRNG algorithms, different DCT implementations (SciPy vs. FFTW), different summation orders. Confirm both pass the four validation tests. |
| Two runs on the same machine disagree | Check `numpy_version`: a NumPy upgrade between runs may have changed the `dct` implementation. |
| Spectral coefficients differ at $O(10^{-15})$ | Check `fftw_version` or `scipy_version`: the FFT butterfly ordering may have changed. |

The BLAS vendor is captured because many numerical libraries delegate to BLAS internally (e.g., SciPy's tridiagonal solver may call LAPACK's `dgtsv`, which in turn calls BLAS routines). The BLAS vendor (OpenBLAS, MKL, ATLAS, Apple Accelerate) determines the low-level implementation of these routines and is the most common source of platform-dependent rounding differences.

---

#### 7.2.3 Hardware Information

The hardware on which the integration runs affects the floating-point behavior through the CPU's instruction set (FMA support, SIMD width), the cache hierarchy (which affects the summation order of vectorized loops), and the memory bandwidth (which affects performance but not correctness).

##### 7.2.3.1 Captured Fields

| Field | Source | Example | Relevance |
|-------|--------|---------|-----------|
| `hostname` | Machine name | `"compute-07"` | Identifies the specific machine |
| `cpu_model` | CPU model string | `"Intel Xeon E5-2680 v4"` | Identifies the instruction set and FMA support |
| `cpu_cores` | Total physical cores | `28` | Context for parallelization |
| `n_cores_used` | Cores used for this run | `1` | Confirms single-threaded execution |
| `ram_gb` | Total RAM in GB | `128` | Confirms memory sufficiency |
| `fma_support` | FMA instruction available | `true` | Affects rounding of $a \times b + c$ operations |

##### 7.2.3.2 Collection Method

| Environment | Method |
|-------------|--------|
| Python | `platform.processor()`, `os.cpu_count()`, `psutil.virtual_memory().total` (if `psutil` available) |
| Julia | `Sys.CPU_NAME`, `Sys.CPU_THREADS`, `Sys.total_memory()` |
| MATLAB | `feature('numcores')`, `memory` (Windows), `system('sysctl -n hw.memsize')` (macOS) |

Some fields (e.g., `cpu_model`, `ram_gb`, `fma_support`) may not be available on all platforms. The engine collects them on a best-effort basis: if a field cannot be determined, it is recorded as `"unknown"` rather than omitted. The metadata schema (§6.4) accepts `"unknown"` as a valid value for optional environment fields.

##### 7.2.3.3 FMA and Its Impact

The fused multiply-add (FMA) instruction computes $a \times b + c$ in a single operation with a single rounding, rather than the two-operation sequence $(a \times b) + c$ with two roundings. This changes the rounding of every expression of the form $a \times b + c$, which includes:

- The stencil evaluation: $\rho_{j-1} - 2\rho_j + \rho_{j+1}$ involves a multiply-add.
- The constitutive evaluation: $M_0 \times (\rho_{\max} - \rho)^\beta$ involves exponentiation followed by multiplication.
- The tridiagonal solve: the Thomas algorithm's forward and backward sweeps involve multiply-adds at every step.

The impact is $O(\epsilon_{\mathrm{mach}})$ per operation — invisible to the user but detectable by bit-level comparison. The `fma_support` field enables the diagnostician to predict whether two runs on different hardware will agree at the bit level (they will if both have the same FMA support and the compiler generates the same FMA usage) or only at the $O(\epsilon_{\mathrm{mach}})$ level (they will if the FMA support or usage differs).

---

#### 7.2.4 Timestamps

The timestamps record when the integration was performed, providing the temporal context for the output.

| Field | Format | Source | Example |
|-------|--------|--------|---------|
| `timestamp_start` | ISO 8601 with timezone | Captured at the start of initialization | `"2026-03-26T14:30:00-04:00"` |
| `timestamp_end` | ISO 8601 with timezone | Captured after the post-loop summary is written | `"2026-03-26T14:30:48-04:00"` |
| `wall_time_seconds` | Float64 (seconds) | `timestamp_end - timestamp_start` | `48.3` |

The timestamps serve two purposes:

1. **Provenance.** They establish *when* the data was produced, enabling the user to correlate the output with a specific software environment (which may have changed between runs due to library updates or system patches).

2. **Performance monitoring.** The `wall_time_seconds` field enables comparison of execution times across implementations and hardware, which is useful for the performance analysis of §4.5 (parallelization) and for detecting anomalous slowdowns that may indicate a computational issue (e.g., excessive adaptive time-step reduction, disk I/O contention, or memory swapping).

---

#### 7.2.5 Environment Snapshot Utility

The environment capture is implemented as a utility function that is called once at initialization and returns the complete environment record:

```
FUNCTION Capture_Environment() → EnvironmentRecord:

    COLLECT os, os_kernel, architecture from platform API
    COLLECT language, language_version from runtime
    COLLECT library versions from package metadata
    COLLECT hostname, cpu_model, cpu_cores, ram_gb from system API
    DETECT fma_support from CPU feature flags (best-effort)
    RECORD timestamp_start = current time in ISO 8601

    RETURN EnvironmentRecord with all collected fields
    (fields that could not be determined are set to "unknown")
```

The utility is called exactly once per integration (not per time step, not per output step). Its output is stored in the `CanonicalParams`-adjacent metadata structure and written to every output file produced by the integration.

The utility does not modify any system state — it only reads. It does not require elevated privileges, network access, or user interaction. On systems where certain information is restricted (e.g., `hostname` on a shared cluster with anonymized node names), the restricted fields are recorded as `"restricted"` rather than causing an error.

---

#### 7.2.6 Summary

| Category | Fields captured | Purpose |
|----------|----------------|---------|
| **Operating system** | OS name/version, kernel, architecture | Diagnose transcendental-function and FMA rounding differences |
| **Language and libraries** | Language version, NumPy/SciPy/FFTW/MATLAB versions, BLAS vendor | Diagnose DCT, solver, and summation-order differences |
| **Hardware** | Hostname, CPU model, core count, RAM, FMA support | Identify the machine; predict FMA-related rounding |
| **Timestamps** | Start/end in ISO 8601, wall time in seconds | Provenance and performance monitoring |
| **Collection** | Automatic at initialization; best-effort for unavailable fields | No user input required |

The environment capture is the most detailed level of the metadata hierarchy. The run metadata (§6.4.2) tells you *what* was computed. The parameter metadata (§6.4.3) tells you *with what* parameters. The environment metadata tells you *on what* machine, *with what* software, *at what* time — the complete context needed to reproduce the computation at Tier 1 (bitwise) fidelity, or to diagnose why two runs at Tier 2 or Tier 3 disagree.

---

### 7.3 Parameter Manifest

The metadata schema (§6.4) embeds the parameter record into every output file, ensuring that each file is self-describing. The **parameter manifest** complements this per-file metadata with a single, authoritative document that lists *all* parameter values used across the *entire* Atlas — every experiment, every sweep point, every convergence sub-run — in a unified format. The manifest is the master reference for reproducing the Atlas as a whole.

---

#### 7.3.1 Purpose

The parameter manifest serves three roles:

1. **Single source of truth.** The five canonical parameter sets (§2.2.1), the sweep ranges (§§4.1–4.4), the initial-condition parameters, and the numerical settings are specified in many places throughout the Atlas and Suite. The manifest consolidates them into a single file that an implementor can load to configure every experiment, eliminating the need to extract parameters from the narrative text.

2. **Cross-file consistency check.** Each output file embeds its own parameter metadata (§6.4.3). The manifest provides the reference against which these per-file values are verified: if an output file's `D` value disagrees with the manifest's `D` for the same `experiment_id`, the file is flagged as inconsistent.

3. **Sweep orchestration input.** The sweep orchestrator (§2.5.5, §4.5) reads the manifest to determine which experiments to run, at which parameter values, and in which order. The manifest is the machine-readable input to the orchestrator, replacing the human-readable tables of Atlas §10.2.5.

---

#### 7.3.2 Manifest Structure

The manifest is a structured file containing one record per integration (one row per task in the parallelization framework of §4.5). Each record specifies the complete input to the `Atlas_Experiment` procedure (Atlas §10.1.1): the parameters, the initial condition, the numerical method, and the output configuration.

##### 7.3.2.1 File Format

The manifest is stored as:

- **CSV:** One header line (field names) followed by one data line per integration. Suitable for human inspection and for import into spreadsheet tools.
- **JSON:** An array of objects, one per integration. Suitable for programmatic access and for nested fields (e.g., IC parameters as a sub-object).
- **HDF5/NPZ/MAT:** A table dataset with named columns. Suitable for efficient binary access in the corresponding environment.

The CSV format is the reference format (the one guaranteed to be readable by all environments). The binary formats are convenience exports.

##### 7.3.2.2 Record Layout

Each record contains the following field groups, in order:

**Group A: Identification.**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `task_id` | Int | Unique task identifier (1, 2, ..., $N_{\mathrm{tasks}}$) | `42` |
| `experiment_id` | String | Atlas experiment number | `"3.1a"` |
| `atlas_section` | String | Atlas section reference | `"3.1.2"` |
| `sweep_id` | String | Sweep name (if part of a sweep; else `"none"`) | `"zeta_sweep"` |
| `sweep_index` | Int | Position within the sweep (0-based; $-1$ if not a sweep) | `7` |

**Group B: Canonical parameters.**

| Field | Type | Description |
|-------|------|-------------|
| `parameter_set` | String | Set name or `"Custom"` |
| `D` | Float64 | Direct-channel weight |
| `zeta` | Float64 | Participation damping |
| `tau` | Float64 | Participation time scale |
| `rho_star` | Float64 | Penalty equilibrium |
| `rho_max` | Float64 | Capacity bound |

**Group C: Constitutive parameters.**

| Field | Type | Description |
|-------|------|-------------|
| `constitutive_type` | String | Constitutive family |
| `M0` | Float64 | Mobility amplitude |
| `beta` | Float64 | Mobility collapse exponent |
| `P0` | Float64 | Penalty slope |

**Group D: Initial condition.**

| Field | Type | Description |
|-------|------|-------------|
| `IC_type` | String | IC type (A/B/C/D/Homogeneous/Custom/Driven) |
| `IC_amplitude` | Float64 | Perturbation amplitude $A$ |
| `IC_mode` | String | Mode number(s) (e.g., `"1"`, `"1,2,3"`, `"N/A"`) |
| `IC_sigma` | Float64 | Gaussian width ($-1$ if N/A) |
| `IC_x0` | Float64 | Gaussian center ($-1$ if N/A) |
| `IC_delta` | Float64 | Near-capacity margin ($-1$ if N/A) |
| `IC_v0` | Float64 | Initial participation |
| `IC_formula` | String | Custom IC formula (empty if standard type) |

**Group E: Numerical settings.**

| Field | Type | Description |
|-------|------|-------------|
| `method` | String | `"FD_CrankNicolson"`, `"SPEC_ETDRK4"`, etc. |
| `dimension` | Int | Spatial dimension $d$ |
| `domain_L` | Float64 | Domain length |
| `N` | Int | Grid points or spectral modes |
| `dt` | Float64 | Nominal time step $\Delta t_0$ |
| `T_final` | Float64 | Final integration time |
| `output_mode` | String | `"uniform"`, `"prescribed"`, `"every_step"` |
| `output_interval` | Int | $k_{\mathrm{out}}$ (for uniform mode; $-1$ otherwise) |

**Group F: Derived quantities (precomputed).**

| Field | Type | Description |
|-------|------|-------------|
| `H` | Float64 | $1 - D$ |
| `Delta` | Float64 | $D + 2\zeta$ |
| `discriminant` | Float64 | $\mathscr{D}_0$ |
| `regime` | String | `"Oscillatory"` / `"Monotonic"` / `"Critical"` |
| `gamma_0` | Float64 | $(DP_*' + \zeta/\tau)/2$ |
| `D_alpha_1` | Float64 | $D(M_*\mu_1 + P_*')$ |
| `spec_hash` | String | SHA-256 of Groups B–E |

The total number of fields per record is **37**. The manifest for the full Atlas ($\sim 1{,}800$ integrations) has $\sim 1{,}800$ rows and occupies $\sim 500$ KB in CSV format.

---

#### 7.3.3 Required Fields

Every field in the manifest record is **required** — no field may be null, empty, or omitted. Fields that do not apply to a specific experiment are filled with sentinel values:

| Condition | Sentinel value | Fields affected |
|-----------|---------------|----------------|
| Not part of a sweep | `sweep_id = "none"`, `sweep_index = -1` | Group A |
| IC parameter not applicable | $-1$ (numeric) or `"N/A"` (string) | `IC_sigma`, `IC_x0`, `IC_delta`, `IC_mode` |
| No custom formula | `IC_formula = ""` (empty string) | Group D |
| Output not uniform | `output_interval = -1` | Group E |

The sentinel values are documented and unambiguous — they cannot be confused with valid parameter values (no physical parameter is $-1$; no IC type is `"N/A"`).

---

#### 7.3.4 Validation

The manifest is validated at two stages: at construction (when the manifest is first generated) and at consumption (when the orchestrator or a reader loads it).

##### 7.3.4.1 Construction-Time Validation

When the manifest is generated (either manually from the Atlas tables or automatically by the experiment-specification tool), each record undergoes the full three-level parameter validation of §2.2.3:

1. **Level 1 (Range checks):** $0 < D < 1$, $\zeta > 0$, $\tau > 0$, etc.
2. **Level 2 (Constitutive checks):** $M(\rho^*) > 0$, $|M(\rho_{\max})| < 10^{-14}$, $|P(\rho^*)| < 10^{-14}$, $P'(\rho^*) > 0$.
3. **Level 3 (Consistency checks):** $|H - (1 - D)| < 10^{-15}$, $|\Delta - (D + 2\zeta)| < 10^{-12}$, discriminant consistency, spectral gap positivity.

Additionally, manifest-level checks are applied:

| Check | Condition | Severity |
|-------|-----------|----------|
| Unique `task_id` | No two records share the same `task_id` | Fatal |
| Unique `experiment_id` + `sweep_index` | No two records share the same ($\texttt{experiment\_id}$, $\texttt{sweep\_index}$) pair | Fatal |
| Consistent `spec_hash` | The hash recomputed from Groups B–E matches the stored `spec_hash` | Fatal |
| Sweep ordering | Within each `sweep_id`, records are ordered by `sweep_index` (0, 1, 2, ...) | Warning |
| Sweep completeness | Within each `sweep_id`, `sweep_index` runs from 0 to $N_{\mathrm{sweep}} - 1$ without gaps | Warning |
| Regime consistency | `regime` matches $\operatorname{sign}(\mathscr{D}_0)$ | Warning |

A manifest that fails any fatal check is rejected. A manifest with warnings is accepted but the warnings are logged.

##### 7.3.4.2 Consumption-Time Validation

When the orchestrator loads the manifest to run the Atlas, it re-validates every record (repeating the construction-time checks) and additionally verifies:

| Check | Condition | Severity |
|-------|-----------|----------|
| Method supported | `method` is one of the four permitted values (§6.4.2) | Fatal |
| IC type supported | `IC_type` is one of the seven permitted values (§6.4.2) | Fatal |
| Resolution positive | $N > 0$, $\Delta t > 0$, $T_{\mathrm{final}} > 0$ | Fatal |
| CFL feasibility | $\Delta t \leq \Delta t_{\mathrm{CFL}}$ at the initial condition (estimated from the parameters) | Warning |
| Output directory available | The output path `output/exp_{experiment_id}/` can be created | Fatal |

The consumption-time validation ensures that the manifest is not only internally consistent but also executable — the specified experiments can actually be run on the current system.

##### 7.3.4.3 Post-Run Cross-Validation

After all integrations are complete, the manifest is cross-validated against the per-file metadata:

For each record $r$ in the manifest and its corresponding output file $f$:

$$
\text{For each field } F \in \{D, \zeta, \tau, \rho^*, \rho_{\max}, M_0, \beta, P_0, N, \Delta t, T_{\mathrm{final}}\}:
$$

$$
|r.F - f.F| < 10^{-14} \cdot \max(|r.F|, 1).
$$

A discrepancy indicates that the output file was produced with different parameters than the manifest specifies — a serious error that invalidates the output. This check catches bugs in the orchestrator (e.g., passing the wrong parameter record to a worker), file-system errors (e.g., an output file written to the wrong directory), and manual errors (e.g., editing the manifest after the runs were completed).

The `spec_hash` provides a fast shortcut: if $r.\texttt{spec\_hash} = f.\texttt{spec\_hash}$, the field-by-field comparison can be skipped (the hash already guarantees agreement). The field-by-field check is performed only when the hashes disagree, to diagnose which field is discrepant.

---

#### 7.3.5 Manifest Generation

The manifest is generated from three sources:

1. **The Master Experiment Table** (Atlas §10.2.5): provides the experiment IDs, parameter sets, IC types, methods, resolutions, and time steps for all 55 standard experiments.

2. **The sweep definitions** (§§4.1–4.4): provide the parameter ranges, sweep grids, and per-point overrides for all parameter, complexity, constitutive, and domain-size sweeps.

3. **The convergence study specifications** (§2.7.4): provide the refinement levels for the four validation tests and any experiment-specific convergence studies.

The generation procedure is:

1. For each experiment in the Master Table: create one record (or one record per sub-experiment, e.g., modes $n = 1, 2, 3, 4$ for Experiment 3.1).
2. For each sweep: create one record per sweep point, using the base set and overrides (§2.2.5).
3. For each convergence study: create one record per refinement level.
4. Assign sequential `task_id` values: $1, 2, \ldots, N_{\mathrm{tasks}}$.
5. Compute the derived quantities (Group F) for every record.
6. Compute the `spec_hash` for every record.
7. Run the construction-time validation (§7.3.4.1).
8. Write the manifest file.

The generation is deterministic: the same Atlas specification produces the same manifest. The `task_id` assignment is by the order of generation (experiments first, then sweeps, then convergence studies), which is documented and fixed.

---

#### 7.3.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Purpose** | Single source of truth for all Atlas parameters; orchestrator input; cross-file consistency reference |
| **Scope** | One record per integration ($\sim 1{,}800$ records for the full Atlas) |
| **Record size** | 37 fields across 6 groups (identification, canonical, constitutive, IC, numerical, derived) |
| **Required fields** | All 37 (sentinels for inapplicable fields; no nulls) |
| **File format** | CSV (reference), JSON, HDF5/NPZ/MAT (convenience) |
| **File size** | $\sim 500$ KB (CSV, full Atlas) |
| **Construction validation** | Per-record: 3-level parameter checks. Manifest-level: uniqueness, hash, sweep ordering |
| **Consumption validation** | Method/IC support, resolution positivity, CFL feasibility, output-directory access |
| **Post-run cross-validation** | Per-field comparison between manifest and output-file metadata ($< 10^{-14}$ tolerance) |
| **Generation** | Deterministic from Atlas tables + sweep definitions + convergence specs |

The parameter manifest is the machine-readable specification of the entire Numerical Atlas. It replaces the human-readable tables of Atlas §10.2 with a structured, validated, hash-protected dataset that can be loaded directly by the orchestrator, used to configure every integration, and verified against every output file. An implementor who receives the manifest and the Suite specification can reproduce the Atlas without consulting the Atlas text — the manifest contains every numerical value needed to run every experiment.

---

### 7.4 Run Manifest

The parameter manifest (§7.3) specifies what *should* be computed. The **run manifest** records what *was* computed — the actual execution history of the Atlas, one record per completed (or attempted) integration, annotated with timestamps, exit status, output file locations, and diagnostic summaries. The parameter manifest is written before the integrations begin; the run manifest is written as the integrations complete.

---

#### 7.4.1 Purpose

The run manifest serves three roles:

1. **Execution log.** It is the authoritative record of which tasks were executed, when, in what order, and with what outcome. For the $\sim 1{,}800$ integrations of the full Atlas, the run manifest answers: "Did task $k$ run? Did it succeed? How long did it take? Where are the output files?"

2. **Provenance bridge.** It connects the *specification* (the parameter manifest, §7.3) to the *output* (the time-series, spectral, and figure data files, §§6.1–6.3). Each record in the run manifest links a `task_id` (from the parameter manifest) to a set of output file paths (in the output directory). This link is the final step in the traceability chain: Atlas figure → figure data file → raw output file → run manifest record → parameter manifest record → experiment specification.

3. **Sweep progress tracker.** For parameter sweeps (§4.5), the run manifest is the persistent record of which sweep points have completed, which have failed, and which remain. After an interruption, the orchestrator reads the run manifest to determine which tasks to rerun (§2.5.5).

---

#### 7.4.2 Record Structure

Each record in the run manifest corresponds to one task (one integration) and contains the following fields:

##### 7.4.2.1 Task Identification

| Field | Type | Description | Source |
|-------|------|-------------|--------|
| `task_id` | Int | Unique task identifier (matches the parameter manifest) | Parameter manifest |
| `experiment_id` | String | Atlas experiment number | Parameter manifest |
| `spec_hash` | String | SHA-256 of the experiment specification | Parameter manifest |

These three fields link the run record to the corresponding parameter-manifest record. The `spec_hash` provides a cryptographic check: if the run manifest's `spec_hash` matches the parameter manifest's `spec_hash` for the same `task_id`, the task was run with the correct parameters.

##### 7.4.2.2 Timestamps

| Field | Type | Description |
|-------|------|-------------|
| `timestamp_queued` | String (ISO 8601) | Time the task was placed in the queue |
| `timestamp_started` | String (ISO 8601) | Time the worker began initialization |
| `timestamp_ended` | String (ISO 8601) | Time the worker completed (normally or abnormally) |
| `wall_time_seconds` | Float64 | $\texttt{timestamp\_ended} - \texttt{timestamp\_started}$ in seconds |
| `init_time_seconds` | Float64 | Time spent in initialization (§2.1) |
| `loop_time_seconds` | Float64 | Time spent in the time loop (§2.3) |
| `output_time_seconds` | Float64 | Time spent writing output files (§2.4) |

The three sub-timings (`init_time`, `loop_time`, `output_time`) sum to approximately `wall_time_seconds` (the difference is overhead from the orchestrator dispatch and the post-loop summary). They enable performance profiling: a task whose `init_time` dominates may have a slow constitutive-validation or precomputation step; a task whose `output_time` dominates may be I/O-bound.

The `timestamp_queued` field records when the orchestrator placed the task in the queue, which may differ from `timestamp_started` if the task waited for an available worker. The difference $\texttt{timestamp\_started} - \texttt{timestamp\_queued}$ is the queue wait time — relevant for diagnosing load-balancing issues in parallel sweeps (§4.5.5).

##### 7.4.2.3 Execution Status

| Field | Type | Description |
|-------|------|-------------|
| `status` | String | `"completed"`, `"failed"`, or `"pending"` |
| `termination_reason` | String | `"FinalTime"`, `"Convergence"`, `"FatalError"`, or `"N/A"` (if pending) |
| `error_id` | String | Error code if failed (e.g., `"E07"`); `"none"` if completed |
| `error_message` | String | Diagnostic message if failed; empty if completed |

The `status` field has three values:

- **`"completed"`**: The integration ran to $T_{\mathrm{final}}$ (or to an early convergence criterion) and terminated normally. All output files are present and valid.
- **`"failed"`**: The integration terminated abnormally due to a fatal error (§2.6.4). Partial output files may be present; the `error_id` and `error_message` identify the failure.
- **`"pending"`**: The task has not yet been executed (it is in the queue or has not been attempted). This status appears in the run manifest during a sweep that is in progress or after an interruption.

##### 7.4.2.4 Integration Summary

| Field | Type | Description |
|-------|------|-------------|
| `n_steps` | Int | Total time steps completed |
| `n_output` | Int | Output records written |
| `n_projection` | Int | Positivity-projection events |
| `n_dt_reduction` | Int | Adaptive time-step reductions |
| `n_energy_warning` | Int | Energy-monotonicity warnings |
| `n_barrier_warning` | Int | Energy-barrier violations |
| `positivity_converged` | Boolean | True if no projection occurred |
| `delta_min` | Float64 | Minimum proximity margin |
| `final_energy` | Float64 | $\mathcal{E}$ at termination |
| `final_deviation` | Float64 | $\|\rho(T) - \rho^*\|_{L^2}$ at termination |

These fields are copied from the `Integration_Summary` record (§2.3.4.4) after the integration completes. For failed tasks, they reflect the state at the moment of failure (not at $T_{\mathrm{final}}$).

##### 7.4.2.5 Output References

| Field | Type | Description |
|-------|------|-------------|
| `output_dir` | String | Path to the output directory for this task |
| `timeseries_file` | String | Path to the time-series file (relative to `output_dir`) |
| `spectral_file` | String | Path to the spectral file (`""` if not produced) |
| `snapshot_file` | String | Path to the snapshot file (`""` if not produced) |
| `diagnostics_file` | String | Path to the diagnostic event log |
| `summary_file` | String | Path to the integration summary |
| `checkpoint_file` | String | Path to the most recent checkpoint (`""` if none) |

The output references are relative paths (relative to the root output directory), not absolute paths. This ensures that the manifest remains valid if the output directory is moved or copied to a different location.

##### 7.4.2.6 Environment Reference

| Field | Type | Description |
|-------|------|-------------|
| `worker_id` | Int | Identifier of the worker process that executed this task |
| `hostname` | String | Machine hostname where the task ran |
| `engine_version` | String | Engine version used for this task |

These fields link the run record to the environment metadata in the output files. In a parallel sweep, different tasks may run on different workers (possibly on different machines in a cluster); the `worker_id` and `hostname` identify which worker executed each task.

---

#### 7.4.3 File Location and Format

The run manifest is stored at the top level of the output directory:

```
output/run_manifest.{ext}
```

The format matches the parameter manifest: CSV (reference), JSON, or binary. The CSV format has one header line followed by one data line per task, with the total field count of **32** fields per record.

The run manifest is written incrementally: each record is appended as the corresponding task completes. This ensures that partial progress is preserved if the orchestrator is interrupted. The appending is atomic (write to a temporary file, then rename; see §2.5 for the atomic-write protocol) to prevent corruption from concurrent writes in parallel sweeps.

For parallel sweeps with multiple workers, the orchestrator serializes the manifest writes: only the orchestrator process (not the worker processes) writes to the manifest. Each worker reports its completion to the orchestrator, which appends the record. This eliminates the risk of concurrent-write corruption.

---

#### 7.4.4 Timestamps and Temporal Ordering

The run manifest records three timestamps per task, enabling a complete temporal reconstruction of the Atlas execution.

**Execution timeline for a single task:**

$$
t_{\mathrm{queued}} \;\leq\; t_{\mathrm{started}} \;\leq\; t_{\mathrm{ended}}.
$$

**Execution timeline for a sweep:**

The tasks in a sweep are executed in an order determined by the orchestrator's dispatch strategy (§4.5.5: longest-first queue ordering) and the availability of workers. The run manifest's records are ordered by `task_id` (which follows the parameter-manifest order), not by execution order. The execution order can be reconstructed from the `timestamp_started` values: sorting the records by `timestamp_started` gives the chronological execution order.

**Gantt-chart reconstruction.** The three timestamps per task ($t_{\mathrm{queued}}$, $t_{\mathrm{started}}$, $t_{\mathrm{ended}}$) and the `worker_id` enable a Gantt-chart reconstruction of the sweep execution: each worker's timeline shows the sequence of tasks it executed, with idle gaps between them. This visualization is useful for diagnosing load-balancing issues (§4.5.5) and for estimating the speedup from additional workers.

---

#### 7.4.5 Validation

The run manifest is validated at two stages.

##### 7.4.5.1 Per-Record Validation (At Write Time)

When a record is appended to the manifest:

| Check | Condition | Severity |
|-------|-----------|----------|
| `task_id` matches parameter manifest | $\exists$ record in param manifest with same `task_id` | Fatal |
| `spec_hash` matches | Run record's `spec_hash` = param manifest's `spec_hash` for same `task_id` | Fatal |
| Status valid | `status` $\in$ {`"completed"`, `"failed"`, `"pending"`} | Fatal |
| Timestamps ordered | $t_{\mathrm{queued}} \leq t_{\mathrm{started}} \leq t_{\mathrm{ended}}$ | Warning |
| Wall time positive | `wall_time_seconds` $> 0$ | Warning |
| Output files exist | All referenced files exist on disk (for completed tasks) | Warning |

##### 7.4.5.2 Post-Sweep Validation (After All Tasks Complete)

| Check | Condition | Severity |
|-------|-----------|----------|
| Completeness | Every `task_id` in the parameter manifest has a record in the run manifest | Warning if any `"pending"` remain |
| No duplicates | No `task_id` appears more than once | Fatal |
| Success rate | $N_{\mathrm{completed}} / N_{\mathrm{total}} > 0.95$ ($> 95\%$ success) | Warning if below |
| File consistency | For every completed task: output-file metadata matches run-manifest fields | Warning if mismatch |

The completeness check identifies tasks that were never executed (still `"pending"` after the sweep finished) — these may have been lost due to an orchestrator crash or a queue error. The success-rate check provides a high-level assessment: a sweep with $> 5\%$ failures likely has a systematic issue (CFL violation at certain parameter values, insufficient resolution, etc.) rather than isolated transient errors.

---

#### 7.4.6 Relationship to Other Manifests and Logs

The run manifest occupies a specific position in the Suite's data hierarchy:

| Document | When written | Content | Scope |
|----------|-------------|---------|-------|
| **Parameter manifest** (§7.3) | Before execution | What should be computed | All tasks (specification) |
| **Run manifest** (§7.4) | During/after execution | What was computed | All tasks (execution history) |
| **Per-file metadata** (§6.4) | During execution | Parameters + environment for one task | One task (embedded in output) |
| **Diagnostic log** (§2.4.3) | During execution | Runtime events for one task | One task (health record) |
| **Sweep progress** (§2.5.5) | During execution | Completion status per sweep point | One sweep (checkpoint) |

The run manifest subsumes the sweep progress file: it contains the same completion-status information plus the timestamps, diagnostic summaries, and output references that the progress file lacks. After the sweep is complete, the progress file can be discarded — the run manifest is the authoritative record.

The run manifest and the per-file metadata are complementary: the run manifest provides the global view (all tasks in one table), and the per-file metadata provides the local view (one task in full detail). A discrepancy between them (e.g., the run manifest says `status = "completed"` but the output file's `termination_reason = "FatalError"`) indicates a serious error in the orchestrator's status tracking.

---

#### 7.4.7 Summary

| Aspect | Specification |
|--------|--------------|
| **Purpose** | Execution history of the Atlas; provenance bridge; sweep progress tracker |
| **Scope** | One record per task ($\sim 1{,}800$ records for the full Atlas) |
| **Record size** | 32 fields: identification (3), timestamps (7), status (4), summary (10), output refs (7), environment ref (3) |
| **File location** | `output/run_manifest.{ext}` |
| **Writing mode** | Incremental (appended as tasks complete); atomic writes |
| **Parallel safety** | Orchestrator serializes writes; workers report to orchestrator |
| **Temporal reconstruction** | Three timestamps per task enable Gantt-chart visualization |
| **Per-record validation** | task_id match, spec_hash match, status valid, timestamps ordered, files exist |
| **Post-sweep validation** | Completeness, no duplicates, success rate $> 95\%$, file consistency |
| **Relationship** | Bridges parameter manifest (specification) to output files (data) |

The run manifest completes the reproducibility documentation: the parameter manifest says what should have been computed, the run manifest says what was computed, the per-file metadata says how it was computed, and the output files contain the results. Together, these four layers provide a complete, machine-verifiable record of the entire Numerical Atlas — from specification to execution to output — with no undocumented gaps.

---

### 7.5 Output Manifest

The parameter manifest (§7.3) indexes tasks by specification. The run manifest (§7.4) indexes tasks by execution. The **output manifest** indexes the outputs by *content* — it catalogs every file produced by the Atlas, classifies it by type, links it to its source task and its destination figure, and provides the checksums needed to verify file integrity. The output manifest is the final document in the reproducibility chain: it answers the question "What files exist, what do they contain, and are they intact?"

---

#### 7.5.1 Purpose

The output manifest serves four roles:

1. **File inventory.** It lists every file in the `output/` directory tree with its path, type, size, and creation time. An implementor receiving a copy of the Atlas output can verify that all expected files are present and that none have been corrupted or truncated.

2. **Figure-to-data mapping.** For each of the 64 Atlas figures, it records which figure data file contains the plot-ready data and which raw data files were used to produce it. This mapping is the machine-readable version of the figure registry (§6.3.3.4).

3. **Data-to-task mapping.** For each raw data file (time series, spectral, snapshot), it records the `task_id` of the integration that produced it. This completes the bidirectional link: from any output file, the reader can trace back to the task, the parameters, and the specification; from any specification, the reader can trace forward to the output files.

4. **Integrity verification.** For each file, it stores a content hash (SHA-256 of the file contents) that can be checked at any time to detect corruption, truncation, or accidental modification.

---

#### 7.5.2 Record Structure

The output manifest contains one record per file. The total number of records is approximately:

| File type | Count | Source |
|-----------|-------|--------|
| Time-series files | $\sim 1{,}800$ | One per completed task |
| Spectral files | $\sim 200$ | Tasks with spectral logging |
| Snapshot files | $\sim 30$ | Tasks with spatial-profile snapshots |
| Diagnostic logs | $\sim 1{,}800$ | One per task (may be empty) |
| Summary files | $\sim 1{,}800$ | One per completed task |
| Checkpoint files | $\sim 100$ | Most recent per long task |
| Figure data files | $64$ | One per Atlas figure |
| Manifests | $3$ | Parameter, run, output manifests |
| **Total** | **$\sim 5{,}800$** | |

Each record contains:

##### 7.5.2.1 File Identification

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `file_id` | Int | Unique file identifier (sequential) | `1247` |
| `file_path` | String | Path relative to `output/` root | `"exp_3.1/n1/timeseries.csv"` |
| `file_type` | String | Classification | `"timeseries"` |
| `file_format` | String | Storage format | `"csv"` |

**Permitted values for `file_type`:**

| Value | Description |
|-------|-------------|
| `"timeseries"` | Time-series observable log (§6.1) |
| `"spectral"` | Spectral modal-amplitude log (§6.2) |
| `"snapshot"` | Spatial density profiles at prescribed times |
| `"diagnostics"` | Diagnostic event log (§2.4.3) |
| `"summary"` | Integration summary (§2.3.4.4) |
| `"checkpoint"` | Checkpoint file (§2.5) |
| `"figure_data"` | Figure-ready extracted data (§6.3) |
| `"manifest"` | One of the three manifests (parameter, run, output) |
| `"metadata"` | Standalone metadata file (if separate from data) |
| `"sweep_scalars"` | Sweep-level grid-indexed arrays (§4.1.3) |

##### 7.5.2.2 Provenance

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `task_id` | Int | Source task ($-1$ for non-task files like manifests or figure data) | `42` |
| `experiment_id` | String | Source experiment | `"3.1a"` |
| `spec_hash` | String | Spec hash of the source task (`""` for non-task files) | `"7f3a2b..."` |

For figure data files, the `task_id` field is $-1$ (figure data is derived from multiple tasks). The source tasks are recorded in the figure-reference fields (§7.5.2.4).

##### 7.5.2.3 File Properties

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `size_bytes` | Int | File size in bytes | `102400` |
| `n_rows` | Int | Number of data rows ($-1$ for non-tabular files) | `1001` |
| `n_columns` | Int | Number of data columns ($-1$ for non-tabular files) | `24` |
| `created` | String (ISO 8601) | File creation timestamp | `"2026-03-26T14:30:48Z"` |
| `content_hash` | String | SHA-256 of the file contents | `"a1b2c3..."` |

The `content_hash` is computed over the entire file contents (including headers, metadata, and data). It is the definitive integrity check: if the hash of a file on disk matches the manifest's `content_hash`, the file has not been modified since the manifest was written.

##### 7.5.2.4 Figure References

For figure data files (`file_type = "figure_data"`), additional fields link the file to the Atlas figure it supports:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `atlas_figure` | String | Atlas figure number | `"3.1"` |
| `atlas_section` | String | Atlas section of the figure description | `"3.1.2"` |
| `figure_title` | String | Figure title from the Atlas | `"Single-mode exponential decay"` |
| `source_task_ids` | List[Int] | Task IDs that produced the underlying data | `[37, 38, 39, 40]` |
| `source_files` | List[String] | Paths to the raw data files used | `["exp_3.1/n1/spectral.csv", ...]` |
| `panel_count` | Int | Number of panels in the figure | `1` |
| `n_curves` | Int | Number of data curves in the file | `4` |
| `n_references` | Int | Number of analytic reference curves | `4` |

For non-figure files, these fields are absent (not filled with sentinels — the fields are simply not present in the record, which is permitted because the output manifest uses a typed schema where figure-reference fields are optional).

##### 7.5.2.5 Data References (for raw data files)

For time-series and spectral files, additional fields describe the data content:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `time_range` | (Float64, Float64) | $(t_{\mathrm{first}}, t_{\mathrm{last}})$ | `(0.0, 5.0)` |
| `energy_range` | (Float64, Float64) | $(\min\mathcal{E}, \max\mathcal{E})$ | `(1.2e-16, 9.9e-07)` |
| `delta_min` | Float64 | Minimum proximity margin in the file | `0.498` |
| `positivity_converged` | Boolean | No projection events | `true` |

These summary fields enable quick filtering: a consumer looking for "all tasks that approached the horizon" can scan the `delta_min` field without opening each file.

---

#### 7.5.3 Figure-to-Data Mapping

The output manifest provides a complete, machine-readable mapping from every Atlas figure to its data. The mapping has two levels:

##### 7.5.3.1 Figure → Figure Data File

For each of the 64 Atlas figures:

$$
\text{Figure } F \;\xrightarrow{\texttt{atlas\_figure}}\; \text{Figure data file } \texttt{figures/fig\_}F\texttt{.\{ext\}}.
$$

The output manifest record for the figure data file contains the `atlas_figure` field, enabling lookup by figure number. The figure data file itself contains the curve data, reference overlays, and extraction metadata (§6.3).

##### 7.5.3.2 Figure Data File → Raw Data Files

The figure data file's `source_files` field (§7.5.2.4) lists the raw data files from which the figure data was extracted. Each raw data file is itself an entry in the output manifest, with its own `task_id`, `experiment_id`, and `content_hash`.

$$
\text{Figure data file} \;\xrightarrow{\texttt{source\_files}}\; \{\text{Raw files}\} \;\xrightarrow{\texttt{task\_id}}\; \{\text{Tasks}\} \;\xrightarrow{\texttt{spec\_hash}}\; \{\text{Specifications}\}.
$$

This two-level mapping enables the complete provenance query: "Figure 4.3 was generated from `figures/fig_4.3.csv`, which was extracted from 21 spectral files in `exp_4.3/pair_*/spectral.csv`, each produced by a specific task in the parameter manifest, each with a verified `spec_hash`."

##### 7.5.3.3 Reverse Mapping: Data File → Figures

The output manifest also supports the reverse query: "Which figures use data from task $k$?" This is answered by scanning the `source_task_ids` field of all figure-data records:

$$
\text{Task } k \;\xrightarrow{\text{scan}}\; \{F : k \in F.\texttt{source\_task\_ids}\}.
$$

This reverse mapping is useful for impact analysis: if a task's output is found to be incorrect (e.g., due to a bug fix that changes the results), the reverse mapping identifies which figures are affected and must be regenerated.

---

#### 7.5.4 Integrity Verification

The output manifest enables two levels of integrity verification.

##### 7.5.4.1 File-Level Integrity

For each file listed in the manifest:

1. Verify the file exists at the specified path.
2. Verify the file size matches `size_bytes`.
3. Compute SHA-256 of the file contents.
4. Compare to the manifest's `content_hash`.

If the hash matches: the file is intact. If the hash does not match: the file has been modified, corrupted, or replaced since the manifest was written. The mismatch is reported with the file path, the expected hash, and the computed hash.

The full integrity check (all $\sim 5{,}800$ files) requires reading every file and computing its hash. At typical storage speeds ($\sim 500$ MB/s): the $\sim 80$ MB of total output can be verified in $< 1$ second.

##### 7.5.4.2 Completeness Check

The output manifest is cross-referenced against the run manifest (§7.4):

- For every task with `status = "completed"` in the run manifest: verify that the expected output files (timeseries, spectral if applicable, diagnostics, summary) exist in the output manifest.
- For every figure in the Atlas figure index (§11 of the Atlas, 64 figures): verify that a figure data file exists in the output manifest.

A missing file indicates either a failed file write (disk full, I/O error) or an incomplete post-processing step (the figure-generation pipeline, §6.3.4, was not run for that figure).

---

#### 7.5.5 File Location and Generation

The output manifest is stored at the top level of the output directory:

```
output/output_manifest.{ext}
```

It is generated as the final step of the Atlas workflow, after all integrations are complete and the figure data files have been produced:

1. **Scan the output directory.** Recursively enumerate all files in `output/`.
2. **Classify each file** by its path and extension (using the naming conventions of §2.4.5).
3. **Link to tasks.** For each raw data file, extract the `task_id` from the file's embedded metadata or from the directory path.
4. **Link to figures.** For each figure data file, extract the `atlas_figure` and `source_files` from the file's metadata.
5. **Compute content hashes.** SHA-256 of every file.
6. **Extract summary fields.** For time-series and spectral files, read the time range, energy range, and diagnostic flags from the file's content.
7. **Assemble the manifest.** Write all records to the output manifest file.
8. **Self-inclusion.** Add the output manifest itself as the final record (with `file_type = "manifest"` and `content_hash` computed over the manifest's content excluding the self-referencing record — a standard bootstrapping technique).

The generation is deterministic: given the same output directory, the same output manifest is produced (modulo the self-referencing hash, which is computed last).

---

#### 7.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Purpose** | File inventory, figure-to-data mapping, data-to-task mapping, integrity verification |
| **Scope** | One record per file ($\sim 5{,}800$ records for the full Atlas) |
| **Record fields** | Identification (4), provenance (3), properties (5), figure refs (8, optional), data refs (4, optional) |
| **File location** | `output/output_manifest.{ext}` |
| **Content hash** | SHA-256 per file; enables corruption/modification detection |
| **Figure mapping** | Two-level: figure → figure data file → raw data files → tasks → specifications |
| **Reverse mapping** | Task → affected figures (via `source_task_ids` scan) |
| **Integrity check** | File existence + size + SHA-256 hash match; $< 1$ second for the full Atlas |
| **Completeness check** | Cross-reference against run manifest (all completed tasks have files) and figure index (all 64 figures have data) |
| **Generation** | Post-processing step: scan → classify → link → hash → assemble |

The output manifest is the inventory of the Atlas's computational output. Combined with the parameter manifest (what was specified), the run manifest (what was executed), and the per-file metadata (how each file was produced), it provides a four-layer documentation system in which every numerical value in every Atlas figure is traceable, verifiable, and reproducible — from the `spec_hash` in the parameter manifest, through the `task_id` in the run manifest, to the `content_hash` in the output manifest, and finally to the specific curve in the specific figure data file that appears in the published Atlas.

---

## 8. Validation Tests

### 8.1 Linear Regime Validation

The linear regime — the neighborhood of the equilibrium $(\rho^*, 0)$ where the nonlinear terms are negligible — is the only regime where the ED system has a complete analytic solution. The linearized eigenvalues (Theorem C.17), the modal decay rates (eq. C.11), the oscillation frequency (eq. C.15), and the spectral gap (Corollary C.18) are all known exactly. Comparing the numerical solution to these exact predictions is the most stringent test of the simulation engine: any error in the spatial discretization, the time-stepping scheme, the constitutive evaluation, or the boundary implementation will manifest as a discrepancy between the measured and predicted rates.

This section specifies the linear regime validation as a formal acceptance test: the configuration, the procedure, the analytic targets, the comparison metrics, and the pass/fail criteria. It corresponds to Validation Test 4 of the Atlas (§1.7.4, Experiment 1.4).

---

#### 8.1.1 Configuration

The linear regime is accessed by initializing the system with a small perturbation about the equilibrium:

**Spatial modes ($n \geq 1$).** IC-A with a single mode:

$$
\rho_0(x) = \rho^* + A\cos(n\pi x/L), \qquad v_0 = 0,
$$

at amplitude $A = 10^{-4}$. This amplitude is small enough that the nonlinear terms $M'(\rho)|\nabla\rho|^2$ are $O(A^2) = O(10^{-8})$ — eight orders of magnitude below the linear terms $M_*\nabla^2 u - P_*' u$, which are $O(A)$. The linearized approximation is therefore accurate to $O(10^{-4})$ relative error over the entire integration.

**Homogeneous mode ($n = 0$).** A spatially constant perturbation with nonzero participation:

$$
\rho_0(x) = \rho^* + A, \qquad v_0 = A,
$$

at $A = 10^{-4}$. This initializes the $2 \times 2$ homogeneous-mode system (eq. C.13) with both $a_0$ and $v$ at $O(10^{-4})$. The nonlinear correction is $O(A^2)$ (from the penalty curvature $P''$ and the mobility variation $M(\rho) - M_*$).

**Parameter sets.** The test is run for all five canonical parameter sets (I–V), exercising both the oscillatory regime (I, II, V: complex eigenvalues) and the monotonic regime (III, IV: real eigenvalues).

**Numerical settings.** The test is run at the default resolution ($N = 512$ for Method A, $N = 128$ for Method B) with the default time step. The integration time is $T = 10.0$ — long enough for the mode amplitude to decrease by several orders of magnitude, providing a clean exponential-decay interval for rate extraction.

---

#### 8.1.2 Analytic Targets

The linearized ED system has exact solutions that serve as the comparison targets.

##### 8.1.2.1 Spatial Mode $n \geq 1$

The amplitude of mode $n$ evolves as (eq. C.11):

$$
a_n(t) = a_n(0)\,e^{-D\alpha_n\,t},
$$

where $\alpha_n = M_*\mu_n + P_*'$ and $\mu_n = (n\pi/L)^2$. The participation variable remains $v(t) = 0$ (mode $n$ does not couple to $v$; Remark C.16).

**Target quantities:**

| Quantity | Formula | Set II value ($n = 1$) |
|----------|---------|----------------------|
| Decay rate | $\sigma_n = D\alpha_n = D(M_*\mu_n + P_*')$ | $2.080$ |
| Half-life | $t_{1/2} = \ln 2/\sigma_n$ | $0.333$ |
| Amplitude at $T = 10$ | $|a_n(10)| = A\,e^{-\sigma_n \cdot 10}$ | $A \cdot e^{-20.8} \approx 9.2 \times 10^{-10}\,A$ |

##### 8.1.2.2 Homogeneous Mode ($n = 0$)

The homogeneous mode evolves according to the $2 \times 2$ matrix exponential (eq. C.13):

$$
\begin{pmatrix}a_0(t)\\v(t)\end{pmatrix} = e^{\mathbf{A}_0 t}\begin{pmatrix}a_0(0)\\v_0\end{pmatrix},
$$

where $\mathbf{A}_0$ has eigenvalues $\lambda_\pm$ (eq. C.15).

**Oscillatory case ($\mathscr{D}_0 < 0$).** The eigenvalues are $\lambda_\pm = -\gamma_0 \pm i\omega$, and the solution is:

$$
a_0(t) = e^{-\gamma_0 t}\bigl[c_1\cos(\omega t) + c_2\sin(\omega t)\bigr],
$$

where $c_1$, $c_2$ are determined by the initial data.

**Target quantities (oscillatory):**

| Quantity | Formula | Set I value |
|----------|---------|-------------|
| Envelope rate | $\gamma_0 = \frac{1}{2}(DP_*' + \zeta/\tau)$ | $0.200$ |
| Frequency | $\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}$ | $0.831$ |
| Period | $T_{\mathrm{osc}} = 2\pi/\omega$ | $7.56$ |

**Overdamped case ($\mathscr{D}_0 > 0$).** The eigenvalues are $\lambda_+ > \lambda_- < 0$ (both real, negative), and the solution is:

$$
a_0(t) = c_+\,e^{\lambda_+ t} + c_-\,e^{\lambda_- t},
$$

where $c_\pm$ are determined by the initial data and the eigenvectors $\mathbf{r}_\pm$.

**Target quantities (overdamped):**

| Quantity | Formula | Set IV value |
|----------|---------|-------------|
| Slow rate | $|\lambda_+| = \gamma_0 - \frac{1}{2}\sqrt{\mathscr{D}_0}$ | $0.924$ |
| Fast rate | $|\lambda_-| = \gamma_0 + \frac{1}{2}\sqrt{\mathscr{D}_0}$ | $4.976$ |
| Rate ratio | $|\lambda_-|/|\lambda_+|$ | $5.39$ |

##### 8.1.2.3 Spectral Gap

The spectral gap is the minimum decay rate across all modes:

$$
\gamma = \min(\gamma_{\mathrm{hom}},\; D\alpha_1),
$$

where $\gamma_{\mathrm{hom}} = |\operatorname{Re}(\lambda_+)|$ is the decay rate of the slowest homogeneous eigenvalue. The test verifies that the measured slowest rate matches $\gamma$.

| Parameter set | $\gamma_{\mathrm{hom}}$ | $D\alpha_1$ | $\gamma$ | Gap controller |
|--------------|----------------------|------------|---------|---------------|
| I | $0.200$ | $1.040$ | $0.200$ | Homogeneous |
| II | $0.550$ | $2.080$ | $0.550$ | Homogeneous |
| III | $0.818$ | $4.160$ | $0.818$ | Homogeneous |
| IV | $0.924$ | $4.680$ | $0.924$ | Homogeneous |
| V | $0.500$ | $1.040$ | $0.500$ | Homogeneous |

For all five sets, the spectral gap is controlled by the homogeneous mode ($\gamma_{\mathrm{hom}} < D\alpha_1$).

---

#### 8.1.3 Validation Procedure

The validation is a sequence of four sub-tests, each targeting a specific analytic prediction.

##### 8.1.3.1 Sub-Test A: Spatial-Mode Decay Rates

**For each parameter set (I–V) and each mode $n \in \{1, 2, 3, 4\}$:**

1. Initialize with IC-A at $A = 10^{-4}$, $v_0 = 0$.
2. Integrate to $T = 10.0$.
3. Extract the modal amplitude $|a_n(t)|$ from the spectral log (§6.2).
4. Fit $\ln|a_n(t)|$ vs. $t$ over $[0.1, \min(9.5, t_{\mathrm{floor}})]$ by least-squares regression (§5.6.2.1).
5. Obtain the measured rate $\hat{\sigma}_n$ and the fit quality $R^2$.
6. Compute the analytic rate $\sigma_n = D\alpha_n$.
7. Compute the relative error $\epsilon_n = |\hat{\sigma}_n - \sigma_n|/\sigma_n$.

**Total sub-experiments:** $5 \times 4 = 20$.

##### 8.1.3.2 Sub-Test B: Spectral Purity

**For each sub-experiment of Sub-Test A:**

1. At every output step, record the maximum amplitude of any non-initialized mode: $S_{\mathrm{leak}} = \max_{k \neq n}|a_k(t)|$.
2. Record the maximum over all output steps: $S_{\mathrm{leak}}^{\max} = \max_t S_{\mathrm{leak}}(t)$.

**Purpose:** Verify that the initialized mode does not leak energy into other modes. At $A = 10^{-4}$, the triad coupling generates $O(A^2) = O(10^{-8})$ in the daughter modes. With $|a_n(0)| \sim A/\sqrt{2} \sim 7 \times 10^{-5}$, the leakage should be $< 10^{-10}$.

##### 8.1.3.3 Sub-Test C: Homogeneous-Mode Dynamics

**For each parameter set (I–V):**

1. Initialize with spatially constant perturbation: $\rho_0 = \rho^* + 10^{-4}$, $v_0 = 10^{-4}$.
2. Integrate to $T = 10.0$.
3. Extract $a_0(t)$ and $v(t)$ from the time-series log (§6.1).
4. **For oscillatory sets (I, II, V):**
   - Extract the envelope rate $\hat{\gamma}_0$ by peak fitting (§5.6.2.2).
   - Extract the frequency $\hat{\omega}$ by zero-crossing analysis (§5.6.2.3).
   - Compute relative errors $\epsilon_\gamma = |\hat{\gamma}_0 - \gamma_0|/\gamma_0$ and $\epsilon_\omega = |\hat{\omega} - \omega|/\omega$.
5. **For monotonic sets (III, IV):**
   - Extract the slow rate $\hat{\sigma}_{\mathrm{slow}}$ by fitting $\ln|a_0(t)|$ over $[2, 9]$ (after the fast mode has decayed).
   - Compute the relative error $\epsilon_{\mathrm{slow}} = |\hat{\sigma}_{\mathrm{slow}} - |\lambda_+||/|\lambda_+|$.

**Total sub-experiments:** $5$.

##### 8.1.3.4 Sub-Test D: Pointwise Solution Comparison

**For each parameter set and each mode ($n = 1$ spatial, $n = 0$ homogeneous):**

1. Compute the analytic solution $\rho_{\mathrm{lin}}(x_j, t_n)$ at every grid point and every output step, using the eigenvalue formulas (eqs. C.11 and C.15).
2. Compute the pointwise error: $e_j^n = |\rho_j^n - \rho_{\mathrm{lin}}(x_j, t_n)|$.
3. Compute the maximum pointwise error: $e_{\max} = \max_{j, n} e_j^n$.
4. Compute the expected error bound: $e_{\mathrm{bound}} = C(\Delta t^p + h^2 + A^2)$, where $p$ is the temporal order and $C$ is a modest constant ($C \sim 10$).

**Purpose:** Verify that the numerical solution converges to the analytic solution with the correct combined order. The $\Delta t^p$ term is the temporal error, $h^2$ is the spatial error (Method A), and $A^2$ is the linearization error. At $A = 10^{-4}$: $A^2 = 10^{-8}$, which is the dominant error source (the discretization errors are smaller at the default resolution). At $A = 10^{-6}$ (an optional ultra-small-amplitude test): the discretization errors dominate, and the convergence order is directly measurable.

---

#### 8.1.4 Pass/Fail Criteria

Each sub-test has explicit, machine-checkable pass/fail criteria.

##### 8.1.4.1 Sub-Test A: Spatial Decay Rates

| Criterion | Condition | Applies to |
|-----------|-----------|-----------|
| Rate accuracy | $\epsilon_n < 0.01$ ($1\%$ relative error) | All 20 sub-experiments |
| Fit quality | $R^2 > 0.999$ | All 20 sub-experiments |
| Rate ordering | $\hat{\sigma}_1 < \hat{\sigma}_2 < \hat{\sigma}_3 < \hat{\sigma}_4$ | Each parameter set |

**Pass:** All three criteria met for all 20 sub-experiments.
**Fail:** Any sub-experiment violates any criterion.

##### 8.1.4.2 Sub-Test B: Spectral Purity

| Criterion | Condition |
|-----------|-----------|
| Leakage bound | $S_{\mathrm{leak}}^{\max} < 10^{-10}$ for all 20 sub-experiments |

**Pass:** All 20 sub-experiments satisfy the bound.
**Fail:** Any sub-experiment violates the bound.

##### 8.1.4.3 Sub-Test C: Homogeneous Mode

| Criterion | Condition | Applies to |
|-----------|-----------|-----------|
| Envelope rate accuracy (oscillatory) | $\epsilon_\gamma < 0.01$ | Sets I, II, V |
| Frequency accuracy (oscillatory) | $\epsilon_\omega < 0.01$ | Sets I, II, V |
| Slow rate accuracy (monotonic) | $\epsilon_{\mathrm{slow}} < 0.01$ | Sets III, IV |
| Number of detected peaks (oscillatory) | $N_{\mathrm{peaks}} \geq 4$ | Sets I, II, V |

**Pass:** All criteria met for all 5 parameter sets.
**Fail:** Any parameter set violates any applicable criterion.

##### 8.1.4.4 Sub-Test D: Pointwise Comparison

| Criterion | Condition |
|-----------|-----------|
| Maximum error | $e_{\max} < 10 \cdot (\Delta t^p + h^2 + A^2)$ |

The factor of $10$ accommodates the accumulation of per-step errors over $\sim 10^5$ steps. At the default resolution ($\Delta t = 5 \times 10^{-4}$, $h \approx 2 \times 10^{-3}$, $A = 10^{-4}$): $e_{\mathrm{bound}} \approx 10 \cdot (2.5 \times 10^{-7} + 4 \times 10^{-6} + 10^{-8}) \approx 4.3 \times 10^{-5}$, so the maximum pointwise error should be $< 4.3 \times 10^{-5}$.

**Pass:** All 10 sub-experiments ($5$ parameter sets $\times$ $2$ modes) satisfy the bound.
**Fail:** Any sub-experiment violates the bound.

---

#### 8.1.5 Failure Diagnosis

When the linear regime validation fails, the failure pattern identifies the likely cause:

| Failure pattern | Likely cause | Diagnostic action |
|----------------|-------------|-------------------|
| $\epsilon_n > 0.01$ for all $n$ at all sets | Systematic error in the time-stepping scheme | Check the implicit-matrix assembly; verify boundary stencil |
| $\epsilon_n > 0.01$ for high $n$ only | Spatial discretization error | Check the Laplacian stencil; verify ghost-point reflection |
| $R^2 < 0.999$ for oscillatory sets | Frequency error or fitting-interval issue | Check the $v$-update formula; extend the fitting interval |
| $S_{\mathrm{leak}}^{\max} > 10^{-10}$ | Aliasing or nonlinear contamination | Check de-aliasing (Method B); reduce $A$ to $10^{-6}$ |
| $\epsilon_\gamma > 0.01$ but $\epsilon_\omega < 0.01$ | Damping-rate error, frequency correct | Check the participation-damping coefficient $\zeta$ in the $v$-equation |
| $\epsilon_\omega > 0.01$ but $\epsilon_\gamma < 0.01$ | Frequency error, damping correct | Check the off-diagonal coupling $H$ in the density equation |
| $e_{\max}$ exceeds bound for $n = 0$ only | Error in the homogeneous-mode ODE | Check the $v$-update (exponential integrator); verify $\bar{F}$ computation |
| $e_{\max}$ exceeds bound for all modes | Combined spatial + temporal error | Run the convergence study (§2.7) to isolate spatial from temporal |

The diagnosis table is exhaustive for the most common error types. An error that does not match any pattern requires deeper investigation (e.g., printing the intermediate arrays at each step to identify the first step at which the error appears).

---

#### 8.1.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Amplitude** | $A = 10^{-4}$ (nonlinear terms $O(10^{-8})$, linearization accurate to $O(10^{-4})$) |
| **Parameter sets** | All five (I–V): oscillatory and monotonic |
| **Spatial modes** | $n = 1, 2, 3, 4$ per set (20 spatial-mode sub-experiments) |
| **Homogeneous mode** | $a_0 = v_0 = 10^{-4}$ per set (5 homogeneous sub-experiments) |
| **Analytic targets** | $D\alpha_n$ (spatial rates), $\gamma_0$ and $\omega$ (oscillatory), $|\lambda_\pm|$ (monotonic) |
| **Rate tolerance** | $1\%$ relative error |
| **Fit quality** | $R^2 > 0.999$ |
| **Spectral purity** | Leakage $< 10^{-10}$ |
| **Pointwise error** | $< 10(\Delta t^p + h^2 + A^2)$ |
| **Total sub-experiments** | 25 (20 spatial + 5 homogeneous) |
| **Failure diagnosis** | Eight-pattern table mapping failure signatures to causes |

The linear regime validation is the most decisive test of the simulation engine. A correct implementation passes all four sub-tests at all five parameter sets; an implementation with any error in the spatial discretization, time stepping, boundary conditions, constitutive evaluation, or participation-variable integration fails at least one sub-test. The failure pattern then identifies the specific error, enabling targeted debugging. An implementation that passes this test has demonstrated that it correctly solves the linearized ED system — and, by the convergence theory of §2.7, that it correctly solves the full nonlinear system to within the discretization error.

---

### 8.2 Nonlinear Regime Validation

The linear regime validation (§8.1) verifies the engine against exact analytic solutions at small amplitude. The nonlinear regime validation verifies the engine against the *structural* predictions of Appendix C at finite amplitude — predictions that hold for any solution of the canonical system, not just for small perturbations. These predictions do not specify the exact solution (no closed-form exists for the nonlinear system), but they specify *qualitative and quantitative properties* that the solution must satisfy: energy monotonicity, positivity, the triad selection rule, the locked amplitude ratio, the three-stage convergence structure, and the mobility-collapse barrier. A correct implementation exhibits all of these properties; an incorrect implementation violates at least one.

This section specifies the nonlinear validation as a suite of six sub-tests, each targeting a specific Appendix C result at finite amplitude.

---

#### 8.2.1 Configuration

The nonlinear regime is accessed by initializing the system at amplitudes large enough for the nonlinear terms to be significant:

**Standard nonlinear IC.** IC-C (localized Gaussian) at $A = 0.3$, $\sigma = 0.05$, $x_0 = L/2$:

$$
\rho_0(x) = \rho^* + 0.3\,\exp\!\left(-\frac{(x - 0.5)^2}{2(0.05)^2}\right), \qquad v_0 = 0.
$$

This places the peak density at $\rho^* + 0.3 = 0.8$ (well above equilibrium, approaching the near-horizon region), produces $C_{\mathrm{ED}}(0) \approx 7.97$ (high complexity), and activates all the nonlinear mechanisms: the mobility variation $M(\rho) - M_*$, the gradient-squared coupling $M'(\rho)|\nabla\rho|^2$, the nonlinear penalty curvature $P(\rho) - P_*' u$, and the participation feedback.

**Near-horizon IC.** IC-D at $\delta = 0.05$, $A = 0.02$:

$$
\rho_0(x) = 0.95 + 0.02\cos(\pi x), \qquad v_0 = 0.
$$

Peak density $0.97$ — within $3\%$ of $\rho_{\max}$. Used specifically for the mobility-collapse sub-test (§8.2.7).

**Triad IC.** IC-A with two modes:

$$
\rho_0(x) = \rho^* + 0.05\cos(\pi x) + 0.05\cos(2\pi x), \qquad v_0 = 0.
$$

Moderate amplitude ($A = 0.05$), two-mode superposition. Used for the triad sub-test (§8.2.5).

**Parameter set.** Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$) is used for all sub-tests unless noted. Set I is chosen because its oscillatory character, strong participation coupling ($H = 0.7$), and moderate damping make it the most sensitive to nonlinear effects — errors in the nonlinear terms are most visible when the participation coupling is strong.

**Resolution.** $N = 512$ (Method A, Crank–Nicolson) and $N = 128$ (Method B, ETD-RK4) for cross-validation.

---

#### 8.2.2 Sub-Test E: Energy Monotonicity (Lemma C.6)

**Appendix C prediction.** The total energy $\mathcal{E}[\rho, v]$ is monotonically non-increasing along solutions: $d\mathcal{E}/dt \leq 0$ for all $t \geq 0$ (Lemma C.6, Proposition C.5).

**Procedure.**

1. Initialize with the standard nonlinear IC ($A = 0.3$).
2. Integrate to $T = 30.0$.
3. At every internal time step, verify $\mathcal{E}^{n+1} \leq \mathcal{E}^n + \text{tol}$, where $\text{tol} = 10\,\Delta t^p\,\mathcal{E}^n$.

**Pass criterion.** Zero energy-monotonicity violations (no E05 or E06 events in the diagnostic log) across the entire integration.

**What this tests.** Energy monotonicity is a global structural property that depends on the correct implementation of *all* terms in the PDE: the implicit diffusion (which provides the leading dissipation), the explicit nonlinear terms (which must not inject spurious energy), the participation coupling (which exchanges energy between $\rho$ and $v$ but must not create it), and the boundary conditions (which must not permit energy flux through the boundary). A violation at any time step indicates that one of these mechanisms is incorrectly implemented.

**Relationship to §8.1.** The linear validation (§8.1) also checks energy monotonicity, but at $A = 10^{-4}$, the nonlinear terms are negligible — the energy decreases simply because the linear diffusion dominates. At $A = 0.3$, the nonlinear terms contribute significantly to the energy dynamics, and the monotonicity property is a nontrivial constraint.

---

#### 8.2.3 Sub-Test F: Positivity and Sub-Capacity (Theorems C.2, C.66)

**Appendix C prediction.** The density satisfies $0 < \rho(x, t) < \rho_{\max}$ for all $(x, t)$ (Theorem C.2, local; Theorem C.66(i), global uniform bound).

**Procedure.**

1. Initialize with the standard nonlinear IC.
2. Integrate to $T = 30.0$.
3. At every time step, verify $\min_j\rho_j > 0$ and $\max_j\rho_j < \rho_{\max}$.
4. Record the positivity-convergence flag (`positivity_converged = true` if no projection events).

**Pass criterion.** `positivity_converged = true` — no positivity or sub-capacity projection was triggered during the entire integration.

**What this tests.** At $A = 0.3$ with $\rho^* = 0.5$, the density ranges from $\sim 0.5$ (far from the Gaussian) to $\sim 0.8$ (at the Gaussian peak) — well within $(0, 1)$. The explicit nonlinear terms could, in principle, produce a negative density at an isolated grid point if the CFL is violated or the stencil is incorrect. The positivity test at finite amplitude is more stringent than at $A = 10^{-4}$ because the gradients are steeper and the explicit terms are larger.

**Extended test.** Repeat with the near-horizon IC ($\delta = 0.05$). The peak density is $0.97$ — much closer to $\rho_{\max}$ — and the sub-capacity constraint is under greater stress. The positivity-convergence flag must still be `true`.

---

#### 8.2.4 Sub-Test G: Dissipation-Channel Closure (Proposition C.42)

**Appendix C prediction.** The energy loss rate is decomposed into three non-negative channels whose sum approximates $-d\mathcal{E}/dt$ (Proposition C.42, eq. C.45).

**Procedure.**

1. Initialize with the standard nonlinear IC.
2. Integrate to $T = 30.0$.
3. At every output step, compute the three dissipation channels $\mathcal{D}_{\mathrm{diff}}$, $\mathcal{D}_{\mathrm{pen}}$, $\mathcal{D}_{\mathrm{part}}$ (§5.2) and the dissipation-identity residual $r^n = (\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t + \mathcal{D}_{\mathrm{total}}^n$.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Channel non-negativity | $\mathcal{D}_{\mathrm{diff}}^n \geq 0$, $\mathcal{D}_{\mathrm{pen}}^n \geq 0$, $\mathcal{D}_{\mathrm{part}}^n \geq 0$ at every output step |
| Residual bound (late time) | $|r^n| < 10\,\Delta t^2\,\mathcal{E}^n$ for $t > 10$ (when the solution is in the linearized regime) |
| Residual bound (early time) | $|r^n| < 0.1\,\mathcal{D}_{\mathrm{total}}^n$ for $t < 10$ ($10\%$ closure during the nonlinear transient) |
| Channel crossover | $\mathcal{D}_{\mathrm{diff}} > \mathcal{D}_{\mathrm{pen}}$ at $t = 0$ and $\mathcal{D}_{\mathrm{diff}} < \mathcal{D}_{\mathrm{pen}}$ at $t = T$ (the gradient channel dominates early; the penalty channel dominates late) |

**What this tests.** The dissipation-channel decomposition depends on the correct computation of $C_{\mathrm{ED}}$, $\|u\|_{L^2}^2$, and $v^2$, and on the consistency between the energy computation (§5.1) and the channel formulas (§5.2). The early-time residual bound ($10\%$) is looser than the late-time bound because the near-equilibrium channel formulas ($\mathcal{D}_{\mathrm{diff}} = DP_*' C_{\mathrm{ED}}$, etc.) are approximations that include $O(\|u\|^2)$ linearization error, which is significant at $A = 0.3$. The late-time bound ($O(\Delta t^2)$) is tight because the solution has entered the linearized regime by $t = 10$.

The channel-crossover criterion is a qualitative structural prediction: the gradient channel must dominate initially (when the Gaussian has steep slopes) and the penalty channel must dominate eventually (when the density deviation is spatially smooth but still nonzero). This crossover is a consequence of the modal hierarchy — the spatial modes decay faster than the homogeneous mode — and its occurrence at finite amplitude validates the hierarchy at the nonlinear level.

---

#### 8.2.5 Sub-Test H: Triad Selection Rule (Theorem C.34)

**Appendix C prediction.** The nonlinear term $M'(\rho)|\nabla\rho|^2$ transfers energy between modes according to the selection rule $k \in \{|m - n|, m + n\}$ (Theorem C.34). No other modes are activated at leading order.

**Procedure.**

1. Initialize with the triad IC: modes $m = 1$ and $n = 2$ at $A = 0.05$.
2. Integrate to $T = 5.0$.
3. Extract modal amplitudes $|a_k(t)|$ for $k = 0, 1, \ldots, 15$ from the spectral log.
4. Classify each mode $k$ as "activated" if $\max_t|a_k(t)| > 10^{-5}$ (the activation threshold, §5.4.2.1).
5. Compute the predicted activation set: $\mathcal{A}_{\mathrm{pred}} = \{0, 1, 2, 3, 4\}$ (from $1 \otimes 1 \to \{0, 2\}$, $2 \otimes 2 \to \{0, 4\}$, $1 \otimes 2 \to \{1, 3\}$).
6. Compare the observed activation set $\mathcal{A}_{\mathrm{obs}}$ to the predicted set.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| No false positives | $\mathcal{A}_{\mathrm{obs}} \subseteq \mathcal{A}_{\mathrm{pred}}$ (no unpredicted mode exceeds $10^{-5}$) |
| Sum-mode generation | $|a_3|$ reaches $O(A^2) \sim 10^{-3}$ (the $1 \otimes 2 \to 3$ channel is active) |
| Target-mode decay | After the generation phase, $|a_3|$ decays at rate $\approx D\alpha_3$ ($\pm 10\%$) |

**What this tests.** The selection rule is a consequence of the cosine-basis product formula and the structure of the $M'(\rho)|\nabla\rho|^2$ term. A false positive (a mode outside $\mathcal{A}_{\mathrm{pred}}$ activated above $10^{-5}$) indicates either aliasing (insufficient de-aliasing in Method B), a stencil error (the discrete gradient-squared does not correctly approximate $|\nabla\rho|^2$), or a bug in the constitutive evaluation (incorrect $M'(\rho)$).

---

#### 8.2.6 Sub-Test I: Locked Amplitude Ratio (Proposition C.35)

**Appendix C prediction.** The ratio $|a_3|/|a_1|$ reaches a quasi-steady value that is proportional to $\epsilon$ (the perturbation amplitude) and independent of time during the quasi-steady phase (Proposition C.35, eq. C.40).

**Procedure.**

1. Initialize with IC-A at mode $n = 1$, amplitude $\epsilon = 0.1$, $v_0 = 0$.
2. Integrate to $T = 8.0$.
3. Extract $|a_1(t)|$ and $|a_3(t)|$ from the spectral log.
4. Compute the instantaneous ratio $R_{31}(t) = |a_3(t)|/|a_1(t)|$.
5. Identify the quasi-steady interval $[t_{\mathrm{onset}}, t_{\mathrm{end}}]$ (§5.3.3.4).
6. Compute the quasi-steady mean $\bar{R}_{31}$ and its standard deviation $\delta R$.
7. Compute the analytic prediction: $\bar{R}_{31}^{\mathrm{pred}} = |M_*'|\,|\Gamma_{12,3}|/(D(\alpha_3 - \alpha_1)) \cdot \epsilon$ (eq. C.40).

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Ratio accuracy | $|\bar{R}_{31} - \bar{R}_{31}^{\mathrm{pred}}|/\bar{R}_{31}^{\mathrm{pred}} < 0.10$ ($10\%$ tolerance) |
| Plateau stability | $\delta R / \bar{R}_{31} < 0.10$ (standard deviation $< 10\%$ of the mean) |
| Quasi-steady duration | $t_{\mathrm{end}} - t_{\mathrm{onset}} > 1.0$ (the plateau persists for at least $1$ time unit) |

**What this tests.** The locked ratio is a nonlinear prediction that combines three elements: the triad-coupling coefficient $\Gamma_{12,3}$ (from the eigenbasis geometry), the differential decay rate $D(\alpha_3 - \alpha_1)$ (from the modal hierarchy), and the generation rate $D|M_*'|\epsilon$ (from the constitutive function). A $10\%$ accuracy in the ratio implies that all three elements are correctly implemented to within a few percent each. The plateau stability criterion verifies that the ratio is genuinely locked (constant in time) rather than drifting — a drift would indicate that the generation-decay balance is not achieved, possibly because the decay rates are incorrect or the nonlinear coupling is mis-evaluated.

The $10\%$ tolerance is wider than the $1\%$ linear-regime tolerance (§8.1.4) because the locked ratio involves the nonlinear coupling at finite amplitude, where $O(\epsilon^2)$ corrections are non-negligible at $\epsilon = 0.1$.

---

#### 8.2.7 Sub-Test J: Mobility-Collapse Barrier (Propositions C.10, C.11)

**Appendix C prediction.** The density remains strictly below $\rho_{\max}$ with a margin $\delta \geq \delta_{\mathrm{barrier}}(\mathcal{E}_0) > 0$ determined by the energy barrier (Proposition C.11). The near-horizon gradients are suppressed by the amplified dissipation (Proposition C.10). The margin improves over time as the density retreats from the horizon (Proposition C.73).

**Procedure.**

1. Initialize with the near-horizon IC ($\delta = 0.05$, $A = 0.02$).
2. Integrate to $T = 20.0$.
3. Track the proximity margin $\delta(t)$, the barrier prediction $\delta_{\mathrm{barrier}}(t)$, and the amplification ratio $\mathcal{A}(t) = C_{\mathrm{ED}}^{\mathrm{eff}}/C_{\mathrm{ED}}$ at every output step.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Barrier compliance | $\delta(t) \geq \delta_{\mathrm{barrier}}(t)$ at every output step |
| Margin improvement | $\delta(T) > \delta(0)$ (the density has retreated from the horizon) |
| Mobility recovery | $M_{\min}(T)/M_* > 0.5$ (the diffusion has substantially recovered) |
| Amplification at $t = 0$ | $\mathcal{A}(0) > 10$ (the near-horizon amplification is active) |
| Amplification at $t = T$ | $\mathcal{A}(T) < 2\,P_*'/M_*$ (the amplification has subsided to near-equilibrium levels) |
| Positivity | `positivity_converged = true` |

**What this tests.** The near-horizon sub-test exercises the mobility-collapse handling (§1.6) at the level of the PDE dynamics, not just the numerical safeguards. The barrier compliance verifies Proposition C.11. The margin improvement verifies Proposition C.73. The amplification checks verify the effective-complexity mechanism of §6.3 of the Atlas. A failure of the barrier compliance indicates that the energy computation or the barrier formula is incorrect. A failure of the margin improvement indicates that the penalty is not driving $\rho$ toward $\rho^*$ — possibly because the penalty evaluation is wrong or the mobility collapse is preventing the diffusive transport that would spread the density.

---

#### 8.2.8 Overall Nonlinear Validation

**Pass criterion.** The nonlinear regime validation passes if and only if all six sub-tests (E through J) pass.

**Relationship to the linear validation.** The linear validation (§8.1) and the nonlinear validation (§8.2) are complementary:

| Property | Linear test (§8.1) | Nonlinear test (§8.2) |
|----------|--------------------|-----------------------|
| Amplitude | $A = 10^{-4}$ | $A = 0.05$–$0.3$ |
| Analytic reference | Exact eigenvalue formulas | Structural inequalities and qualitative predictions |
| Rate accuracy | $1\%$ relative | $10\%$ (for the locked ratio); exact (for structural properties) |
| Mechanisms tested | Linear diffusion, penalty, participation | Nonlinear coupling, mobility variation, gradient-squared term, energy barrier |
| Failure type detected | Discretization errors, boundary errors | Nonlinear-term errors, constitutive errors, CFL violations |

An implementation must pass both validations before it is accepted for production use. The linear validation certifies the *infrastructure* (stencils, solvers, eigenbasis); the nonlinear validation certifies the *architecture* (the structural properties that make the ED system a realization of Principles 1–7).

---

#### 8.2.9 Summary

| Sub-test | Appendix C target | IC | Key criterion | Tolerance |
|---------|-------------------|-----|--------------|-----------|
| E | Energy monotonicity (Lemma C.6) | Gaussian $A = 0.3$ | Zero E05/E06 events | Exact |
| F | Positivity (Theorems C.2, C.66) | Gaussian + near-horizon | `positivity_converged = true` | Exact |
| G | Dissipation closure (Prop. C.42) | Gaussian $A = 0.3$ | Channels non-negative; residual bounded; crossover observed | $10\%$ early, $O(\Delta t^2)$ late |
| H | Selection rule (Theorem C.34) | Two-mode $A = 0.05$ | Zero false positives | Exact (structural) |
| I | Locked ratio (Prop. C.35) | Single-mode $\epsilon = 0.1$ | $|\bar{R}_{31} - \bar{R}_{31}^{\mathrm{pred}}|/\bar{R}_{31}^{\mathrm{pred}} < 0.10$ | $10\%$ |
| J | Mobility barrier (Props. C.10, C.11) | Near-horizon $\delta = 0.05$ | Barrier compliance; margin improvement; amplification | Exact (structural) |

The nonlinear validation tests the simulation engine against the six structural predictions of Appendix C that have no linear-regime analogue: energy monotonicity at finite amplitude, positivity under nonlinear dynamics, dissipation-channel structure, the triad selection rule, the locked amplitude ratio, and the mobility-collapse barrier. Together with the linear validation (§8.1), these twelve sub-tests (A–J) constitute the complete acceptance gate for the simulation engine. An implementation that passes all twelve has demonstrated correct behavior across both regimes, all five parameter sets, and every structural prediction of the ED architecture.

---

### 8.3 Triad Selection Rule Validation

The triad selection rule (Theorem C.34) is the spectral fingerprint of Principle 7: it specifies that the nonlinear term $M'(\rho)|\nabla\rho|^2$ transfers energy from source modes $(m, n)$ to target modes $k \in \{|m - n|, m + n\}$ and to no others. Sub-Test H (§8.2.5) verifies the rule for a single source pair. This section extends the verification to a comprehensive, exhaustive test: all source pairs in a defined range, all possible target modes, with quantitative comparison of the measured generation rates to the analytic coupling coefficients $\Gamma_{mnk}$.

This section corresponds to Atlas Experiment 4.3 (§4.1.4) and provides the full specification for the compliance matrix (Atlas Figure 4.3).

---

#### 8.3.1 Test Design

##### 8.3.1.1 Source Pairs

The test exhaustively covers all distinct source pairs $(m, n)$ with $1 \leq m \leq n \leq N_{\mathrm{test}}$, where $N_{\mathrm{test}} = 6$ is the maximum source mode. The total number of pairs is $\binom{6}{2} + 6 = 15 + 6 = 21$ (15 cross-pairs plus 6 self-pairs).

| # | Pair $(m, n)$ | Sum $m + n$ | Difference $|m - n|$ | Self-interaction products |
|---|-------------|------------|---------------------|--------------------------|
| 1 | $(1, 1)$ | $2$ | $0$ | $\{0, 2\}$ |
| 2 | $(1, 2)$ | $3$ | $1$ | $\{0, 2\}$, $\{0, 4\}$ |
| 3 | $(1, 3)$ | $4$ | $2$ | $\{0, 2\}$, $\{0, 6\}$ |
| 4 | $(1, 4)$ | $5$ | $3$ | $\{0, 2\}$, $\{0, 8\}$ |
| 5 | $(1, 5)$ | $6$ | $4$ | $\{0, 2\}$, $\{0, 10\}$ |
| 6 | $(1, 6)$ | $7$ | $5$ | $\{0, 2\}$, $\{0, 12\}$ |
| 7 | $(2, 2)$ | $4$ | $0$ | $\{0, 4\}$ |
| 8 | $(2, 3)$ | $5$ | $1$ | $\{0, 4\}$, $\{0, 6\}$ |
| 9 | $(2, 4)$ | $6$ | $2$ | $\{0, 4\}$, $\{0, 8\}$ |
| 10 | $(2, 5)$ | $7$ | $3$ | $\{0, 4\}$, $\{0, 10\}$ |
| 11 | $(2, 6)$ | $8$ | $4$ | $\{0, 4\}$, $\{0, 12\}$ |
| 12 | $(3, 3)$ | $6$ | $0$ | $\{0, 6\}$ |
| 13 | $(3, 4)$ | $7$ | $1$ | $\{0, 6\}$, $\{0, 8\}$ |
| 14 | $(3, 5)$ | $8$ | $2$ | $\{0, 6\}$, $\{0, 10\}$ |
| 15 | $(3, 6)$ | $9$ | $3$ | $\{0, 6\}$, $\{0, 12\}$ |
| 16 | $(4, 4)$ | $8$ | $0$ | $\{0, 8\}$ |
| 17 | $(4, 5)$ | $9$ | $1$ | $\{0, 8\}$, $\{0, 10\}$ |
| 18 | $(4, 6)$ | $10$ | $2$ | $\{0, 8\}$, $\{0, 12\}$ |
| 19 | $(5, 5)$ | $10$ | $0$ | $\{0, 10\}$ |
| 20 | $(5, 6)$ | $11$ | $1$ | $\{0, 10\}$, $\{0, 12\}$ |
| 21 | $(6, 6)$ | $12$ | $0$ | $\{0, 12\}$ |

##### 8.3.1.2 Predicted Activation Set

For each pair $(m, n)$, the predicted activation set includes the cross-interaction products and the self-interaction products:

$$
\mathcal{A}_{\mathrm{pred}}(m, n) = \{|m - n|,\; m + n\} \cup \{0, 2m\} \cup \{0, 2n\}.
$$

For $m = n$ (self-pairs): $\mathcal{A}_{\mathrm{pred}}(m, m) = \{0, 2m\}$ (the cross-interaction gives $|m - m| = 0$ and $m + m = 2m$, which coincide with the self-interaction products).

For $m \neq n$: $\mathcal{A}_{\mathrm{pred}}$ has up to $5$ distinct elements: $\{0, |m - n|, 2m, m + n, 2n\}$ (when all are distinct). Some may coincide (e.g., for $(1, 2)$: $|m - n| = 1 = m$, $2m = 2 = n$, giving $\mathcal{A}_{\mathrm{pred}} = \{0, 1, 2, 3, 4\}$).

##### 8.3.1.3 Target Mode Range

The monitored target modes are $k = 0, 1, \ldots, N_{\mathrm{obs}} - 1$ with $N_{\mathrm{obs}} = 16$. This range is sufficient to capture all predicted targets (the largest is $2 \cdot 6 = 12$) and to provide a margin for detecting any unpredicted activation up to $k = 15$.

##### 8.3.1.4 Initial Condition and Parameters

Each pair is tested independently with a two-mode initial condition:

$$
\rho_0(x) = \rho^* + A\cos(m\pi x/L) + A\cos(n\pi x/L), \qquad v_0 = 0,
$$

at amplitude $A = 0.03$. This amplitude is chosen so that:

- The second-order generation level $O(A^2) = O(9 \times 10^{-4})$ is well above the activation threshold $\theta_{\mathrm{act}} = 10^{-5}$.
- The third-order level $O(A^3) = O(2.7 \times 10^{-5})$ is close to but below $\theta_{\mathrm{act}}$, so third-order products are not counted as activated.

Parameter Set I ($D = 0.3$, $\zeta = 0.1$, $\tau = 1.0$) is used. Method B (spectral, ETD-RK4) with $N = 128$ modes and $\Delta t = 10^{-4}$. Integration time $T = 2.0$ (sufficient for the generated modes to peak and begin decaying).

---

#### 8.3.2 Testing the Sum Mode $m + n$

##### 8.3.2.1 Generation Mechanism

The sum mode $k = m + n$ is generated by the cross-interaction of modes $m$ and $n$ through the gradient-squared nonlinearity:

$$
M'(\rho)\,|\nabla\rho|^2 \;\supset\; M_*'\,(\nabla\varphi_m)(\nabla\varphi_n)\,a_m\,a_n + \ldots
$$

Projecting onto $\varphi_{m+n}$ via the trilinear coefficient $\Gamma_{mn,m+n}$ (§5.4.1.2) gives the generation rate:

$$
\dot{a}_{m+n}\big|_{\mathrm{gen}} = D\,M_*'\,\Gamma_{mn,m+n}\,a_m\,a_n + O(a^3).
$$

The sum mode rises from zero (it is not initialized), reaches a peak amplitude set by the balance between the generation rate and the target-mode decay rate $D\alpha_{m+n}$, and then decays at rate $D\alpha_{m+n}$ once the source modes have diminished.

##### 8.3.2.2 Measurement

For each pair $(m, n)$ with $m \neq n$:

1. Extract $|a_{m+n}(t)|$ from the spectral log.
2. Verify activation: $\max_t|a_{m+n}(t)| > \theta_{\mathrm{act}} = 10^{-5}$.
3. Record the peak amplitude $a_{m+n}^{\max}$ and peak time $t_{m+n}^{\max}$.
4. Compute the predicted peak amplitude:

$$
a_{m+n}^{\max,\mathrm{pred}} \approx \frac{|D\,M_*'\,\Gamma_{mn,m+n}|\,|a_m(0)|\,|a_n(0)|}{D\alpha_{m+n}}.
$$

5. Compute the amplitude ratio: $r = a_{m+n}^{\max}/a_{m+n}^{\max,\mathrm{pred}}$.

##### 8.3.2.3 Expected Results

The sum mode is activated for every pair with $m \neq n$ (the coupling coefficient $\Gamma_{mn,m+n} \neq 0$ by Theorem C.34). The peak amplitude scales as $A^2$ (second-order in the source amplitude). The amplitude ratio $r$ should be $1.0 \pm 0.3$ (within $30\%$; the tolerance is wide because the peak-amplitude formula is a leading-order estimate that neglects the time dependence of the source amplitudes and the contribution from higher-order pathways).

---

#### 8.3.3 Testing the Difference Mode $|m - n|$

##### 8.3.3.1 Generation Mechanism

The difference mode $k = |m - n|$ is generated by the same cross-interaction, but with the cosine-product formula selecting the difference frequency:

$$
\cos(m\pi x/L)\cos(n\pi x/L) = \tfrac{1}{2}\cos((m-n)\pi x/L) + \tfrac{1}{2}\cos((m+n)\pi x/L).
$$

The gradient-squared term contains both the sum and difference products, so the difference mode is generated simultaneously with the sum mode, at the same order ($O(A^2)$), with a coupling coefficient $\Gamma_{mn,|m-n|}$ that has the same magnitude as $\Gamma_{mn,m+n}$ (§5.4.1.2: both equal $mn\pi^2\sqrt{2}/(2L^{3/2})$).

##### 8.3.3.2 Measurement

For each pair $(m, n)$ with $m \neq n$ and $|m - n| \geq 1$:

1. Extract $|a_{|m-n|}(t)|$ from the spectral log.
2. Verify activation: $\max_t|a_{|m-n|}(t)| > \theta_{\mathrm{act}}$.
3. Record the peak amplitude and peak time.
4. Compute the predicted peak amplitude using $\Gamma_{mn,|m-n|}$ and $D\alpha_{|m-n|}$.

##### 8.3.3.3 Special Cases

**$|m - n| = 0$ (self-pair).** For self-pairs ($m = n$), the "difference mode" is $k = 0$ (the homogeneous mode). This is always in the predicted set $\mathcal{A}_{\mathrm{pred}}$ and is generated at rate $\Gamma_{mm,0} = m^2\pi^2/L^{3/2}$ (§5.4.1.2).

**$|m - n| = m$ or $|m - n| = n$.** For some pairs (e.g., $(1, 2)$: $|m - n| = 1 = m$), the difference mode coincides with one of the initialized modes. In this case, the "generation" manifests as an amplitude correction to the existing mode (a nonlinear frequency shift or amplitude modification) rather than as the creation of a new mode from zero. The activation criterion is automatically satisfied (the mode was already initialized). The measurement instead extracts the amplitude correction: $\delta a_m = |a_m(t)| - |a_m(0)|e^{-D\alpha_m t}$ (the deviation from the linearized decay).

---

#### 8.3.4 Measuring $\Gamma_{mnk}$ from the Simulation

The trilinear coupling coefficients $\Gamma_{mnk}$ are precomputed analytically (§5.4.1.2) and stored for comparison. They can also be *measured* from the simulation data, providing an independent check on both the analytic formula and the numerical implementation.

##### 8.3.4.1 Extraction from Initial Growth Rate

At $t = 0$, the generated mode $k$ has zero amplitude ($a_k(0) = 0$) and its initial growth rate is entirely due to the nonlinear generation:

$$
\dot{a}_k(0) = D\,M_*'\,\Gamma_{mnk}\,a_m(0)\,a_n(0).
$$

The numerically measured initial growth rate is:

$$
\hat{\dot{a}}_k = \frac{a_k(\Delta t_{\mathrm{out}}) - a_k(0)}{\Delta t_{\mathrm{out}}} = \frac{a_k(\Delta t_{\mathrm{out}})}{\Delta t_{\mathrm{out}}},
$$

where $\Delta t_{\mathrm{out}} = k_{\mathrm{out}}\Delta t$ is the first output interval (the earliest time at which the spectral data is available). The measured coupling coefficient is:

$$
\hat{\Gamma}_{mnk} = \frac{\hat{\dot{a}}_k}{D\,M_*'\,a_m(0)\,a_n(0)}.
$$

This extraction is accurate when $\Delta t_{\mathrm{out}}$ is small enough that the linear decay of mode $k$ has not yet significantly reduced its amplitude from the generated value (i.e., $D\alpha_k\Delta t_{\mathrm{out}} \ll 1$). At $\Delta t_{\mathrm{out}} = 50 \cdot 10^{-4} = 5 \times 10^{-3}$ and $D\alpha_k \lesssim 50$ (for $k \leq 12$): $D\alpha_k\Delta t_{\mathrm{out}} \lesssim 0.25$ — marginal. For higher accuracy, the initial growth rate can be extracted from the first $3$–$5$ output steps by fitting $a_k(t)$ to the model $a_k(t) = Ct(1 - D\alpha_k t/2 + \ldots)$ (the leading terms of the variation-of-constants solution), but the simpler single-step formula suffices for a $30\%$-level comparison.

##### 8.3.4.2 Extraction from Peak Amplitude

An alternative extraction uses the peak amplitude and peak time:

$$
a_k^{\max} \approx \frac{|D\,M_*'\,\hat{\Gamma}_{mnk}|\,|a_m(0)|\,|a_n(0)|}{D\alpha_k},
$$

which gives:

$$
\hat{\Gamma}_{mnk} = \frac{a_k^{\max}\,D\alpha_k}{|D\,M_*'|\,|a_m(0)|\,|a_n(0)|}.
$$

This formula is less sensitive to the output time resolution (the peak amplitude is a global feature, not a local derivative) but more sensitive to the higher-order corrections (the peak amplitude includes contributions from the cascade $m \otimes n \to k$, then $m \otimes k \to \ldots$, etc.). It is accurate to $\sim 30\%$ at $A = 0.03$.

##### 8.3.4.3 Comparison to Analytic Values

For each activated target mode $k$ in each pair $(m, n)$, the engine computes:

$$
\epsilon_\Gamma = \frac{|\hat{\Gamma}_{mnk} - \Gamma_{mnk}|}{|\Gamma_{mnk}|},
$$

where $\Gamma_{mnk}$ is the precomputed analytic value (§5.4.1.2) and $\hat{\Gamma}_{mnk}$ is the numerically measured value (from §8.3.4.1 or §8.3.4.2).

**Acceptance criterion:** $\epsilon_\Gamma < 0.30$ ($30\%$ tolerance). The wide tolerance reflects the $O(A)$ corrections to the leading-order generation formula and the finite output time resolution. At smaller amplitudes ($A = 0.01$), the tolerance tightens to $< 0.10$ because the higher-order corrections are proportionally smaller.

---

#### 8.3.5 The Compliance Matrix

The results of the 21-pair test are assembled into the compliance matrix: a $21 \times 16$ binary array where entry $(i, k)$ indicates whether target mode $k$ was activated (peak amplitude $> \theta_{\mathrm{act}}$) by source pair $i$.

##### 8.3.5.1 Matrix Construction

For each pair $i = 1, \ldots, 21$ and each target mode $k = 0, 1, \ldots, 15$:

$$
C_{ik} = \begin{cases}1 & \text{if } \max_t|a_k(t)| > \theta_{\mathrm{act}} \text{ in the integration for pair } i,\\0 & \text{otherwise.}\end{cases}
$$

##### 8.3.5.2 Annotation

Each cell is annotated with the selection-rule prediction:

$$
P_{ik} = \begin{cases}1 & \text{if } k \in \mathcal{A}_{\mathrm{pred}}(m_i, n_i),\\0 & \text{otherwise.}\end{cases}
$$

##### 8.3.5.3 Classification

Each cell falls into one of four categories:

| $C_{ik}$ | $P_{ik}$ | Category | Meaning |
|----------|----------|----------|---------|
| $1$ | $1$ | **True positive** | Predicted and observed. Selection rule confirmed. |
| $0$ | $1$ | **False negative** | Predicted but not observed. The coupling exists but the amplitude is below $\theta_{\mathrm{act}}$. Not a selection-rule violation. |
| $1$ | $0$ | **False positive** | Observed but not predicted. A mode was activated that the selection rule forbids. A selection-rule violation. |
| $0$ | $0$ | **True negative** | Neither predicted nor observed. The selection rule correctly predicts absence. |

##### 8.3.5.4 Pass Criterion

The selection rule is validated if and only if:

$$
\sum_{i,k}C_{ik}(1 - P_{ik}) = 0.
$$

That is, **zero false positives** across the entire matrix. Every activated mode must be in the predicted set.

False negatives are permitted (some predicted modes may not reach the activation threshold at $A = 0.03$ — notably the $k = 0$ mean correction, which has amplitude $O(A^2/\sqrt{L})$ and may be below $10^{-5}$ for $L = 1$). The number of false negatives is logged but does not affect the pass/fail status.

---

#### 8.3.6 Quantitative Results Record

For each pair and each activated target mode, the engine records the quantitative comparison:

| Field | Type | Contents |
|-------|------|----------|
| `pair_index` | Int | Pair number $i$ (1–21) |
| `m` | Int | Source mode $m$ |
| `n` | Int | Source mode $n$ |
| `k` | Int | Target mode $k$ |
| `predicted` | Boolean | $P_{ik}$ |
| `activated` | Boolean | $C_{ik}$ |
| `peak_amplitude` | Float64 | $\max_t|a_k(t)|$ |
| `peak_time` | Float64 | $\arg\max_t|a_k(t)|$ |
| `Gamma_analytic` | Float64 | $\Gamma_{mnk}$ (precomputed) |
| `Gamma_measured` | Float64 | $\hat{\Gamma}_{mnk}$ (from peak amplitude) |
| `Gamma_error` | Float64 | $\epsilon_\Gamma = |\hat{\Gamma} - \Gamma|/|\Gamma|$ |
| `decay_rate_measured` | Float64 | $\hat{\sigma}_k$ (late-time decay of the generated mode) |
| `decay_rate_predicted` | Float64 | $D\alpha_k$ |
| `decay_rate_error` | Float64 | $|\hat{\sigma}_k - D\alpha_k|/D\alpha_k$ |

This record is stored in the triad output file alongside the compliance matrix. The total number of records is $21 \times 16 = 336$, of which approximately $21 \times 4 \approx 84$ have `activated = true` (each pair activates $\sim 4$ target modes on average).

---

#### 8.3.7 Extended Tests

Beyond the standard 21-pair test, the engine supports two extended tests:

##### 8.3.7.1 Amplitude Scaling Test

For a single pair (e.g., $(1, 2)$), repeat the test at five amplitudes $A \in \{0.01, 0.02, 0.03, 0.05, 0.08\}$. At each amplitude, measure the peak amplitude of the sum mode ($k = 3$). The predicted scaling is $a_3^{\max} \propto A^2$ (second-order in $A$). A log-log plot of $a_3^{\max}$ versus $A$ should have slope $2.0 \pm 0.2$.

**Purpose.** This test verifies the *order* of the nonlinear generation, not just its presence. A slope significantly different from $2$ would indicate that the gradient-squared term is incorrectly implemented (e.g., a missing factor in $M'(\rho)$, or an incorrect stencil for $|\nabla\rho|^2$).

##### 8.3.7.2 High-Mode Pair Test

Extend the source-pair range to $N_{\mathrm{test}} = 10$ (55 pairs). This tests the selection rule for higher modes ($m + n$ up to $20$) and verifies that the coupling coefficients scale correctly with $m$ and $n$ (the predicted scaling $\Gamma_{mn,m+n} \propto mn$ is verified by plotting $\hat{\Gamma}/(mn)$ versus $m + n$ and checking for a flat line).

**Purpose.** High-mode pairs have faster decay rates and smaller coupling coefficients (relative to $D\alpha_k$), so the signal-to-noise ratio of the measurement decreases. This test establishes the mode range over which the triad measurement is reliable at the given amplitude and resolution.

---

#### 8.3.8 Summary

| Aspect | Specification |
|--------|--------------|
| **Source pairs** | All 21 pairs with $1 \leq m \leq n \leq 6$ |
| **Target modes** | $k = 0, 1, \ldots, 15$ (16 modes monitored) |
| **Amplitude** | $A = 0.03$ (second-order products above $\theta_{\mathrm{act}}$; third-order below) |
| **Activation threshold** | $\theta_{\mathrm{act}} = 10^{-5}$ |
| **Compliance matrix** | $21 \times 16$ binary array; pass = zero false positives |
| **Coupling measurement** | $\hat{\Gamma}_{mnk}$ from peak amplitude; accuracy $\sim 30\%$ at $A = 0.03$ |
| **Sum-mode test** | Activation verified; peak amplitude compared to $\Gamma_{mn,m+n}$ prediction |
| **Difference-mode test** | Activation verified; special handling for $|m-n| = 0$ and $|m-n| = m$ or $n$ |
| **Amplitude scaling** | $a_k^{\max} \propto A^2$ verified at $5$ amplitudes; slope $2.0 \pm 0.2$ |
| **Total integrations** | $21$ (standard) + $5$ (scaling) + $55$ (extended, optional) |

The triad selection rule validation is the most exhaustive structural test in the Suite. It verifies a combinatorial prediction — that exactly the modes satisfying $k \in \{|m - n|, m + n\}$ are activated, and no others — across 21 source pairs and 16 target modes, producing a $336$-cell compliance matrix with a zero-false-positive pass criterion. The quantitative coupling measurement ($\hat{\Gamma}_{mnk}$ versus $\Gamma_{mnk}$) and the amplitude-scaling test ($a_k^{\max} \propto A^2$) provide additional verification that the nonlinear term $M'(\rho)|\nabla\rho|^2$ is correctly discretized, correctly evaluated, and correctly coupled to the modal dynamics. A false positive anywhere in the matrix would falsify the selection rule for the implementation — and, if confirmed at converged resolution, would challenge Theorem C.34 itself.

---

### 8.4 Horizon Barrier Validation

Principle 4 (Mobility Capacity Bound) states that $M(\rho_{\max}) = 0$, creating an energy barrier that prevents the density from reaching $\rho_{\max}$. Propositions C.10 and C.11 establish the two consequences — gradient suppression in the near-horizon region and the divergence of the energy potential $\Phi(\rho)$ as $\rho \to \rho_{\max}$ — and Theorem C.66(i) guarantees a uniform margin $\delta > 0$ for all time. This section specifies the validation tests that verify these predictions numerically: the barrier's existence and scaling (§8.4.1), the gradient suppression (§8.4.2), the monotonic margin improvement (§8.4.3), and the mobility recovery (§8.4.4). Together, these four sub-tests constitute the definitive numerical test of Principle 4.

---

#### 8.4.1 Sub-Test K: Energy Barrier Scaling (Proposition C.11)

**Prediction.** The density potential $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}^-$, with the asymptotic behavior (for the canonical constitutive functions with $\beta = 2$):

$$
\Phi(\rho) \approx \frac{P_0(\rho_{\max} - \rho^*)}{M_0(\rho_{\max} - \rho)} = \frac{0.5}{\rho_{\max} - \rho}.
$$

The sublevel set $\{\mathcal{E} \leq E_0\}$ is therefore confined to $\{\rho \leq \rho_{\max} - \delta(E_0)\}$ with:

$$
\delta(E_0) \geq \frac{P_0(\rho_{\max} - \rho^*)|\Omega|}{M_0\,E_0} = \frac{0.5}{E_0}.
$$

**Procedure.**

1. Construct seven near-horizon initial conditions at decreasing margins $\delta_0 \in \{0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005\}$:

$$
\rho_0(x) = \rho_{\max} - \delta_0 + \frac{\delta_0}{2}\cos(\pi x), \qquad v_0 = 0.
$$

The peak density is $\rho_{\max} - \delta_0/2$ (within $\delta_0/2$ of $\rho_{\max}$).

2. For each, compute the initial energy $\mathcal{E}_0$ by the trapezoidal rule of $\Phi(\rho_0)$ (§5.1.2).

3. Compute the analytic barrier prediction $\delta_{\mathrm{barrier}} = 0.5/\mathcal{E}_0$.

4. Integrate to $T = 1.0$ (long enough for the density to begin relaxing but not to reach equilibrium).

5. Record $\delta_{\min} = \min_t\delta(t)$ (the closest approach to $\rho_{\max}$ during the integration).

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Barrier compliance | $\delta_{\min} \geq \delta_{\mathrm{barrier}}$ for all seven ICs |
| Energy scaling | $\mathcal{E}_0 \propto \delta_0^{-1}$ (slope $-1$ on log-log plot of $\mathcal{E}_0$ vs. $\delta_0$) within $10\%$ for $\delta_0 \leq 0.1$ |
| No contact | $\delta_{\min} > 0$ for all seven ICs (the density never reaches $\rho_{\max}$) |
| Positivity | `positivity_converged = true` for all seven |

**Quantitative check.** The product $\mathcal{E}_0 \cdot \delta_{\min}$ should be approximately constant (equal to $0.5|\Omega| = 0.5$ in the asymptotic regime). Verify:

$$
\frac{\max_i(\mathcal{E}_{0,i}\cdot\delta_{\min,i}) - \min_i(\mathcal{E}_{0,i}\cdot\delta_{\min,i})}{\text{mean}_i(\mathcal{E}_{0,i}\cdot\delta_{\min,i})} < 0.3
$$

for the four smallest $\delta_0$ values (where the asymptotic formula is most accurate).

**Extended test: exponent sweep.** Repeat the barrier test for three mobility exponents $\beta \in \{1, 2, 3\}$ at three margins $\delta_0 \in \{0.1, 0.01, 0.001\}$. The predicted scaling is $\mathcal{E}_0 \propto \delta_0^{-(\beta - 1)}$ for $\beta > 1$ and $\mathcal{E}_0 \propto \ln(1/\delta_0)$ for $\beta = 1$.

| $\beta$ | Predicted $\mathcal{E}_0$ scaling | Log-log slope | Acceptance |
|---------|----------------------------------|---------------|-----------|
| $1$ | $\sim \ln(1/\delta_0)$ | Curved (sub-linear) | $\mathcal{E}_0(\delta_0 = 0.01) > \mathcal{E}_0(\delta_0 = 0.1) > 0$ |
| $2$ | $\sim 1/\delta_0$ | $-1$ | Slope $= -1.0 \pm 0.1$ |
| $3$ | $\sim 1/\delta_0^2$ | $-2$ | Slope $= -2.0 \pm 0.2$ |

This extended test verifies that the barrier strength depends on $\beta$ as predicted by the asymptotics of $\Phi$ (Atlas §6.2, eq. 6.1), confirming that the implementation correctly evaluates the density potential for different mobility exponents.

---

#### 8.4.2 Sub-Test L: Gradient Suppression (Proposition C.10)

**Prediction.** In the near-horizon region $\Omega_\eta(t) = \{x : \rho(x,t) > \rho_{\max} - \eta\}$, the gradient integral is bounded:

$$
\int_{\Omega_\eta(t)}|\nabla\rho|^2\,dx \leq \frac{M(\rho_{\max} - \eta)}{P'(\rho_{\max} - \eta)}\cdot\frac{\mathcal{E}_0}{D}.
$$

For the default constitutive functions with $\eta = 0.1$:

$$
G_\eta^{\mathrm{bound}} = \frac{(0.1)^2}{1.0}\cdot\frac{\mathcal{E}_0}{0.3} = \frac{0.01\,\mathcal{E}_0}{0.3} \approx 0.033\,\mathcal{E}_0.
$$

**Procedure.**

1. Initialize with IC-D at $\delta_0 = 0.05$, $A = 0.02$, $v_0 = 0$. Use Parameter Set I. Integrate to $T = 3.0$ at $N = 1024$.

2. At every output step, compute:
   - The near-horizon set fraction $f_\eta(t) = \#\{j : \rho_j > \rho_{\max} - \eta\}/N_{\mathrm{grid}}$ with $\eta = 0.1$.
   - The near-horizon gradient integral $G_\eta(t) = h\sum_{j : \rho_j > \rho_{\max} - \eta}(|\nabla_h\rho|^2)_j$.
   - The Proposition C.10 bound $G_\eta^{\mathrm{bound}} = M(\rho_{\max} - \eta)\,\mathcal{E}_0/(D\,P'(\rho_{\max} - \eta))$.

3. Track $f_\eta(t)$ and $G_\eta(t)$ as time series.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Bound compliance | $G_\eta(t) \leq G_\eta^{\mathrm{bound}}$ at every output step where $f_\eta > 0$ |
| Set shrinkage | $f_\eta(T) < f_\eta(0)$ (the near-horizon region has contracted) |
| Gradient decay | $G_\eta(T) < 0.01 \cdot G_\eta(0)$ (the near-horizon gradient content has been reduced by $> 99\%$) |
| Faster-than-bulk decay | The decay rate of $G_\eta(t)$ exceeds the decay rate of $C_{\mathrm{ED}}(t)$ during the near-horizon phase ($t < 1.0$) |

**What this tests.** The gradient suppression is the kinetic mechanism of Principle 4: the vanishing mobility prevents the formation and maintenance of spatial gradients near $\rho_{\max}$. The bound compliance verifies Proposition C.10. The faster-than-bulk decay verifies the amplified effective complexity (§6.3 of the Atlas): near-horizon gradients are destroyed faster than interior gradients because the dissipation integrand $P'/M \cdot |\nabla\rho|^2$ is amplified by $1/M(\rho) \to \infty$.

---

#### 8.4.3 Sub-Test M: Monotonic Margin Improvement (Proposition C.73)

**Prediction.** The proximity margin $\delta(t)$ improves monotonically as $t \to \infty$, converging to $\rho_{\max} - \rho^* = 0.5$:

$$
\delta(t) \to \rho_{\max} - \rho^* \qquad \text{as } t \to \infty.
$$

More strongly: the density at every grid point converges to $\rho^*$ (Theorem C.70, Theorem C.72), so $\max_j\rho_j \to \rho^*$ and $\delta(t) \to \rho_{\max} - \rho^* = 0.5$.

**Procedure.**

1. Initialize with IC-D at $\delta_0 = 0.05$, $A = 0.02$, $v_0 = 0$. Integrate to $T = 20.0$ at $N = 1024$.

2. Record $\delta(t)$ at every output step.

3. Compute the margin at the final time: $\delta(T)$.

4. Check for monotonicity: after the initial transient ($t > 0.5$), verify $\delta(t_{n+1}) \geq \delta(t_n) - \text{tol}$ at every consecutive pair of output steps, where $\text{tol} = 10^{-6}$ accounts for the temporal discretization error.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Final margin improvement | $\delta(T) > \delta(0)$ |
| Convergence toward equilibrium | $\delta(T) > 0.4$ (the margin has recovered at least $80\%$ of the way from $\delta_0 = 0.05$ to the equilibrium value $0.5$) |
| Near-monotonicity | No output step with $\delta(t_{n+1}) < \delta(t_n) - 10^{-6}$ for $t > 0.5$ |
| Equilibrium agreement | $|\delta(T) - (\rho_{\max} - \rho^*)| < 0.1$ (within $20\%$ of the equilibrium margin) |

**What this tests.** The margin improvement verifies that the penalty term $-P(\rho)$ is correctly driving the density away from $\rho_{\max}$ toward $\rho^*$, even in the near-horizon region where the diffusion is suppressed. A failure (the margin decreasing or stagnating) would indicate that the penalty is incorrectly implemented (wrong sign, wrong magnitude) or that a numerical artifact (e.g., the explicit nonlinear terms injecting spurious density toward $\rho_{\max}$) is counteracting the penalty.

The near-monotonicity criterion allows for small transient decreases (during the first few time steps, the explicit terms may produce a slight overshoot before the implicit diffusion and the adaptive time-step reduction take effect), but requires that the trend is consistently upward after the initial transient.

---

#### 8.4.4 Sub-Test N: Mobility Recovery (Proposition C.74)

**Prediction.** As the density converges to $\rho^*$, the mobility recovers uniformly:

$$
M(\rho(x, t)) \to M(\rho^*) = M_* \qquad \text{uniformly in } x \text{ as } t \to \infty.
$$

Equivalently, $M_{\min}(t)/M_* \to 1$.

**Procedure.**

1. Use the same integration as Sub-Test M ($T = 20.0$, IC-D at $\delta_0 = 0.05$).

2. At every output step, record $M_{\min}(t)/M_*$ (§5.7.1.2).

3. Record the recovery trajectory: the time series $M_{\min}(t)/M_*$ from its initial value to its final value.

**Pass criteria.**

| Criterion | Condition |
|-----------|-----------|
| Initial suppression | $M_{\min}(0)/M_* < 0.05$ (the mobility is initially suppressed by $> 95\%$) |
| Final recovery | $M_{\min}(T)/M_* > 0.9$ (the mobility has recovered to $> 90\%$ of equilibrium) |
| Monotonic recovery | $M_{\min}(t)$ is non-decreasing for $t > 0.5$ (after the initial transient) |
| Consistent with margin | $M_{\min}(t) = M_0(\delta(t))^\beta$ to within $10^{-12}$ at every output step (the mobility is consistent with the proximity margin) |

**What this tests.** The mobility recovery is the functional consequence of the margin improvement: as $\delta(t)$ grows, $M(\rho_{\max} - \delta) = M_0\delta^\beta$ grows, and the equation recovers its parabolic character. The consistency check ($M_{\min} = M_0\delta^\beta$) verifies that the constitutive evaluation and the proximity monitoring are using the same density values — a discrepancy would indicate a stale-data bug (the mobility being evaluated at a previous time step's density).

The initial suppression criterion ($M_{\min}(0)/M_* < 0.05$) confirms that the IC-D configuration is genuinely near the horizon — the test is meaningless if the density is not close enough to $\rho_{\max}$ to suppress the mobility significantly.

---

#### 8.4.5 Overall Horizon Barrier Validation

**Pass criterion.** The horizon barrier validation passes if and only if all four sub-tests (K through N) pass.

**Relationship to the nonlinear validation.** Sub-Test J (§8.2.7) tested the mobility-collapse barrier at the level of a single IC at a single $\delta_0$. The horizon barrier validation (§8.4) extends this to a systematic study: the barrier scaling across seven margins (Sub-Test K), the gradient suppression mechanism (Sub-Test L), the margin dynamics (Sub-Test M), and the mobility recovery (Sub-Test N). The four sub-tests together provide a complete verification of Principle 4 at the numerical level.

**Numerical requirements.** Sub-Tests L, M, and N use $N = 1024$ (higher resolution than the default $N = 512$) because the near-horizon dynamics involve steep gradients and narrow boundary layers that require finer spatial resolution. Sub-Test K uses the default resolution at most margins but may require $N = 1024$ at the smallest margin ($\delta_0 = 0.005$) to resolve the near-horizon boundary layer.

---

#### 8.4.6 Summary

| Sub-test | Appendix C target | IC | Key criterion | Tolerance |
|---------|-------------------|-----|--------------|-----------|
| K | Energy barrier scaling (Prop. C.11) | 7 margins ($\delta_0$: $0.3$ to $0.005$) | $\delta_{\min} \geq \delta_{\mathrm{barrier}}$; $\mathcal{E}_0 \propto \delta_0^{-1}$ | Exact (barrier); $10\%$ (slope) |
| L | Gradient suppression (Prop. C.10) | IC-D, $\delta_0 = 0.05$ | $G_\eta \leq G_\eta^{\mathrm{bound}}$; $G_\eta$ decays faster than $C_{\mathrm{ED}}$ | Exact (bound) |
| M | Margin improvement (Prop. C.73) | IC-D, $\delta_0 = 0.05$, $T = 20$ | $\delta(T) > \delta(0)$; $\delta(T) > 0.4$; near-monotone | $10^{-6}$ (monotonicity) |
| N | Mobility recovery (Prop. C.74) | Same as M | $M_{\min}(0)/M_* < 0.05$; $M_{\min}(T)/M_* > 0.9$ | Exact (consistency) |

The horizon barrier validation tests the four predictions of Principle 4 that are unique to the ED architecture: no other PDE framework requires $M(\rho_{\max}) = 0$, no other framework produces the energy-barrier scaling $\mathcal{E} \propto \delta^{-(\beta-1)}$, no other framework predicts gradient suppression in the high-density region, and no other framework guarantees monotonic margin improvement toward $\rho_{\max} - \rho^*$. These are structural predictions — they hold for every solution, at every amplitude, for every constitutive function satisfying Principle 4. Their numerical verification confirms that the simulation engine correctly implements the mobility collapse and that the discrete dynamics preserves the continuous system's structural barrier.

---

### 8.5 Three-Stage Convergence Validation

Theorem C.76 (Three-Stage Convergence) is the synthesis of the entire long-time theory of Appendix C: every global solution of the ED system converges to the unique equilibrium $(\rho^*, 0)$ through three structurally distinct stages — global bounds (Stage I, §C.2), algebraic convergence (Stage II, §C.7.1–C.7.4), and exponential convergence (Stage III, §C.5, C.7.5). The three stages are connected by the transition time $t_*$ — the time at which the solution enters the local stability basin — and each stage is governed by a different subset of the canonical principles.

This section specifies the validation tests that verify the three-stage structure numerically: the detection of each stage (§8.5.1), the measurement of the transition time (§8.5.2), and the quantitative comparison to the analytic predictions of Theorem C.76 (§8.5.3). These tests correspond to Atlas §7 (Experiments 7.1–7.7).

---

#### 8.5.1 Detecting the Three Stages

Each stage has a distinctive signature in the Lyapunov functional $\mathcal{V}(t)$ and the instantaneous rate $\hat{\beta}(t) = -d\ln\mathcal{V}/dt$ (§5.6.1.4). The engine detects the stages by analyzing these two time series.

##### 8.5.1.1 Stage I: Global Bounds

**Signature.** During Stage I, the solution is far from equilibrium and the nonlinear terms are comparable to the linear terms. The Lyapunov functional decreases, but not at a constant rate — the instantaneous rate $\hat{\beta}(t)$ is large and rapidly decreasing (the fast spatial modes are being extinguished, removing the high-$C_{\mathrm{ED}}$ content).

**Detection criteria.**

| Observable | Stage I behavior |
|-----------|-----------------|
| $\mathcal{V}(t)$ | Decreasing; steep descent on semilog plot |
| $\hat{\beta}(t)$ | Large ($\hat{\beta} > 2\gamma_*$) and decreasing |
| $C_{\mathrm{ED}}(t)$ | Rapidly decreasing (high modes decaying at $D\alpha_n \gg \gamma_*$) |
| $\mathcal{B}(t)$ | $> 1$ (outside the exponential basin) |

**Stage I end.** Stage I ends when the fast transient is over — operationally, when $\hat{\beta}(t)$ first drops below $3\gamma_*$ (no longer dominated by the fast spatial modes). This transition is gradual, not sharp; the criterion $\hat{\beta} < 3\gamma_*$ is a convention, chosen because $3\gamma_*$ is well above the Stage III plateau ($\gamma_*$) and well below the initial peak ($\hat{\beta}(0) \sim 10\gamma_*$ for the Gaussian IC at $A = 0.3$).

##### 8.5.1.2 Stage II: Algebraic Convergence

**Signature.** During Stage II, the spatial modes have been extinguished and only the homogeneous mode $(a_0, v)$ remains. The solution is still outside the exponential basin ($\mathcal{B}(t) > 1$) because the homogeneous-mode amplitude has not yet decayed sufficiently. The Lyapunov functional decreases at a rate that is approximately algebraic ($\mathcal{V} \sim t^{-p}$ for some $p > 0$), which appears as a straight line on a log-log plot.

**Detection criteria.**

| Observable | Stage II behavior |
|-----------|------------------|
| $\mathcal{V}(t)$ | Decreasing; approximately straight on log-log |
| $\hat{\beta}(t)$ | Approximately constant, below $\gamma_*$ (the algebraic rate is slower than the exponential rate) |
| $C_{\mathrm{ED}}(t)$ | Small and slowly decreasing (only the fundamental mode contributes) |
| $\mathcal{B}(t)$ | $> 1$ but decreasing toward $1$ |

**Stage II characterization.** The algebraic exponent $p$ is extracted by fitting $\ln\mathcal{V}$ versus $\ln t$ over the Stage II interval $[t_I, t_*]$ (where $t_I$ is the end of Stage I). The fit is:

$$
\ln\mathcal{V} = c_0 - p\,\ln t, \qquad p = -\frac{d\ln\mathcal{V}}{d\ln t}.
$$

The algebraic exponent $p$ depends on the initial condition and the parameter set; it is not a universal constant. For the standard Gaussian IC ($A = 0.3$) at Parameter Set I: $p \approx 2$–$3$ (Atlas §7.2.2).

**Stage II end.** Stage II ends at the transition time $t_*$ (§8.5.2), when the solution enters the exponential basin.

##### 8.5.1.3 Stage III: Exponential Convergence

**Signature.** During Stage III, the solution is inside the exponential basin ($\mathcal{B}(t) < 1$) and the Lyapunov functional decays exponentially: $\mathcal{V}(t) \sim Ce^{-\gamma_* t}$, which appears as a straight line on a semilog plot with slope $-\gamma_*$.

**Detection criteria.**

| Observable | Stage III behavior |
|-----------|-------------------|
| $\mathcal{V}(t)$ | Decreasing; straight line on semilog (constant slope $-\gamma_*$) |
| $\hat{\beta}(t)$ | Approximately constant at $\gamma_*$ (the Lyapunov rate) |
| $C_{\mathrm{ED}}(t)$ | Exponentially decreasing at rate $\approx 2D\alpha_1$ |
| $\mathcal{B}(t)$ | $< 1$ and decreasing |

**Stage III characterization.** The exponential rate is extracted by fitting $\ln\mathcal{V}$ versus $t$ over $[t_* + 1, T]$ (well inside the basin). The measured rate $\hat{\sigma}_\infty$ is compared to $\gamma_*$ (§5.6.3.3).

##### 8.5.1.4 Stage Detection Algorithm

The engine detects the three stages automatically from the $\hat{\beta}(t)$ time series using the following algorithm:

```
PROCEDURE Detect_Stages(beta_smooth, gamma_star, B):

    // Stage I: fast transient
    t_I = first time t where beta_smooth(t) < 3 * gamma_star

    // Stage III: exponential basin
    t_star = first time t >= t_I where B(t) < 1.0
    IF t_star not found: t_star = T  (never entered basin; Stage III absent)

    // Verify Stage III rate
    IF t_star < T - 5:
        sigma_inf = mean(beta_smooth[t_star+1 : T])
        stage_III_detected = (|sigma_inf - gamma_star| / gamma_star < 0.1)
    ELSE:
        stage_III_detected = false

    // Stage II: the interval between Stage I end and Stage III start
    stage_II_present = (t_star - t_I > 1.0)

    RETURN (t_I, t_star, stage_II_present, stage_III_detected, sigma_inf)
```

The algorithm returns the Stage I end time ($t_I$), the transition time ($t_*$), whether Stage II is present (it may be absent if the initial amplitude is small enough that the solution enters the basin immediately), whether Stage III is detected (it may be absent if $T$ is too short), and the measured asymptotic rate.

---

#### 8.5.2 Measuring $t_*$

The transition time $t_*$ is the central observable of the three-stage convergence. It separates Stage II from Stage III and determines the duration of the nonlinear transient.

##### 8.5.2.1 Primary Definition

$$
t_* := \inf\{t \geq 0 : \mathcal{B}(t) < 1\},
$$

where $\mathcal{B}(t) = (\|u(t)\|_{H^1}^2 + |v(t)|^2)/\epsilon_0^2$ is the basin indicator (§5.5.3.2). The transition time is the first time the solution enters the exponential-stability basin of Theorem C.43.

**Discrete implementation.** The basin indicator is computed at every output step. The transition time is the output time at which $\mathcal{B}$ first drops below $1$:

$$
t_* = t_{n_*}, \qquad n_* = \min\{n : \mathcal{B}(t_n) < 1\}.
$$

If $\mathcal{B}(t_0) < 1$ (the initial condition is already inside the basin): $t_* = 0$. If $\mathcal{B}(t_n) \geq 1$ for all $n$ (the basin is never entered during $[0, T]$): $t_* = T$ and Stage III is flagged as absent.

##### 8.5.2.2 Alternative Definition (Rate-Based)

When $\epsilon_0$ is not precisely known (it depends on the nonlinear Lipschitz constant $C_{\mathrm{nl}}$, which is estimated rather than computed exactly), an alternative definition uses the instantaneous rate:

$$
t_*^{\mathrm{rate}} := \inf\{t \geq t_I : \hat{\beta}_{\mathrm{smooth}}(t) \geq 0.9\,\gamma_*\}.
$$

This defines the transition as the time at which the smoothed Lyapunov decay rate reaches $90\%$ of its asymptotic value. The $90\%$ threshold is conventional — it balances sensitivity (detecting the transition early) against robustness (avoiding premature detection from a transient fluctuation in $\hat{\beta}$).

The two definitions ($t_*$ from $\mathcal{B}$ and $t_*^{\mathrm{rate}}$ from $\hat{\beta}$) should agree to within $\sim 1$–$2$ time units. A large discrepancy indicates that $\epsilon_0$ is incorrectly estimated (the basin boundary does not coincide with the rate transition).

##### 8.5.2.3 Dependence on Initial Complexity

Theorem C.76 predicts that $t_*$ depends on the initial data through the initial energy $\mathcal{E}_0$ (equivalently, through $C_{\mathrm{ED}}(0)$ for high-complexity ICs). The validation tests this dependence by measuring $t_*$ at multiple amplitudes (Atlas §7.4, Experiment 7.6):

**Procedure.** Initialize with IC-C at amplitudes $A \in \{0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.35, 0.4\}$ ($10$ values). Integrate each to $T = 60.0$. Measure $t_*$ (both definitions) and $C_{\mathrm{ED}}(0)$ at each amplitude.

**Expected scaling.** For $C_{\mathrm{ED}}(0) < \epsilon_0^2$: $t_* \approx 0$ (already inside the basin). For $C_{\mathrm{ED}}(0) > \epsilon_0^2$: $t_*$ increases, approximately as $t_* \sim c\ln(C_{\mathrm{ED}}(0)/\epsilon_0^2)$ for moderate complexities. The logarithmic scaling reflects the exponential decay of the spatial modes during Stage I: it takes $\sim \ln(C_{\mathrm{ED}}/\epsilon_0^2)/(2D\alpha_1)$ time units for the complexity to decay from $C_{\mathrm{ED}}(0)$ to $\epsilon_0^2$.

##### 8.5.2.4 Dependence on Parameter Set

Theorem C.76 also predicts that $t_*$ depends on the canonical parameters through $\gamma_*$ and $\epsilon_0$ — both of which vary across parameter sets. The validation tests this by measuring $t_*$ at a fixed amplitude ($A = 0.2$) across all five parameter sets (Atlas §7.4, Experiment 7.7).

**Expected ordering.** Set IV (largest $\gamma_*$, largest $\epsilon_0$) → smallest $t_*$. Set III (smallest $\gamma_*$ near the critical surface) → largest $t_*$. The ordering should be: $t_*^{\mathrm{IV}} < t_*^{\mathrm{II}} < t_*^{\mathrm{V}} < t_*^{\mathrm{I}} < t_*^{\mathrm{III}}$.

---

#### 8.5.3 Validating Theorem C.76

The validation of Theorem C.76 consists of five checks, each targeting a specific clause of the theorem.

##### 8.5.3.1 Check 1: Stage I — Global Bounds (Theorem C.66)

**Prediction.** The energy $\mathcal{E}(t)$ is bounded above by $C(\mathcal{E}_0)$, the density remains in $(\delta, \rho_{\max} - \delta)$, and the total dissipation is finite.

**Verification.** Using the standard nonlinear IC ($A = 0.3$, $T = 50$):

| Criterion | Condition |
|-----------|-----------|
| Energy bounded | $\mathcal{E}(t) \leq \mathcal{E}(0)$ for all $t$ (energy is non-increasing) |
| Density confined | $\delta_{\min} > 0$ (density never reaches $\rho_{\max}$) |
| Dissipation finite | $\sum_n\Delta t\,\mathcal{D}_{\mathrm{total}}^n < \infty$ (the cumulative dissipation converges) |

The cumulative dissipation is computed as $\mathcal{D}_{\mathrm{cum}}(T) = \Delta t_{\mathrm{out}}\sum_{n=0}^{N_{\mathrm{out}}-1}\mathcal{D}_{\mathrm{total}}^n$ (trapezoidal sum over output steps). The finiteness is verified by checking that $\mathcal{D}_{\mathrm{cum}}(T)$ has converged to within $1\%$: $|\mathcal{D}_{\mathrm{cum}}(T) - \mathcal{D}_{\mathrm{cum}}(T/2)|/\mathcal{D}_{\mathrm{cum}}(T) < 0.01$.

##### 8.5.3.2 Check 2: Stage II — Convergence to Equilibrium (Theorem C.70)

**Prediction.** $\|\rho(t) - \rho^*\|_{H^1} + |v(t)| \to 0$ as $t \to \infty$, and the $\omega$-limit set is $\{(\rho^*, 0)\}$.

**Verification.**

| Criterion | Condition |
|-----------|-----------|
| $L^2$-convergence | $\|\rho(T) - \rho^*\|_{L^2} < 10^{-3}$ at $T = 50$ |
| Participation convergence | $|v(T)| < 10^{-3}$ at $T = 50$ |
| Gradient convergence | $C_{\mathrm{ED}}(T) < 10^{-6}$ at $T = 50$ |
| Unique $\omega$-limit | The solution approaches $\rho^*$ from the correct direction (the density at every grid point converges to $\rho^*$, not to any other value) |

The "unique $\omega$-limit" check verifies Step 3 of Theorem C.70 (Principle 3): the penalty's strict monotonicity $P' > 0$ ensures that $\rho^*$ is the only possible limit. This is checked by verifying $\max_j|\rho_j(T) - \rho^*| < 10^{-3}$ — the density has converged pointwise, not just in the $L^2$-norm.

##### 8.5.3.3 Check 3: Stage III — Exponential Decay (Theorem C.72)

**Prediction.** For $t \geq t_*$, $\mathcal{V}(t) \leq C\mathcal{V}(t_*)\,e^{-\gamma_*(t - t_*)}$.

**Verification.**

| Criterion | Condition |
|-----------|-----------|
| Rate accuracy | $|\hat{\sigma}_\infty - \gamma_*|/\gamma_* < 0.05$ (asymptotic Lyapunov rate within $5\%$ of predicted) |
| Exponential fit quality | $R^2 > 0.999$ for the log-linear fit of $\mathcal{V}(t)$ over $[t_* + 1, T]$ |
| Basin containment | $\mathcal{B}(t) < 1$ for all $t > t_*$ (once inside the basin, the solution stays inside) |

The basin-containment check verifies that the solution does not leave the exponential basin after entering it. Theorem C.43 guarantees this (the Lyapunov functional is monotonically decreasing inside the basin, and the basin is a sublevel set of $\mathcal{V}$), but a numerical violation could occur if the time-stepping error causes a transient increase in $\mathcal{V}$ that pushes $\mathcal{B}$ above $1$.

##### 8.5.3.4 Check 4: Stage Connectivity

**Prediction.** Stage I provides the uniform bounds needed for Stage II (compactness); Stage II provides the convergence needed for Stage III (eventual entry into the basin).

**Verification.** This check verifies the logical chain:

| Criterion | Condition |
|-----------|-----------|
| Stages are sequential | $t_I < t_*$ (Stage I ends before Stage III begins) |
| Stage II is non-empty (for high-amplitude ICs) | $t_* - t_I > 1.0$ for $A = 0.3$ |
| Stage II may be empty (for low-amplitude ICs) | $t_* = 0$ for $A = 0.01$ (the solution starts inside the basin) |
| Transition is smooth | $\hat{\beta}(t)$ has no discontinuity at $t_*$ (the rate transitions smoothly from the Stage II value to the Stage III value) |

The smoothness check is verified by examining the derivative $d\hat{\beta}/dt$ at $t_*$: it should be bounded (no jump). A discontinuity in $\hat{\beta}$ at $t_*$ would indicate a numerical artifact (e.g., a sudden change in $\Delta t$ from the adaptive scheme that causes a step in $\mathcal{V}$).

##### 8.5.3.5 Check 5: Universal Asymptotic Rate

**Prediction.** The late-time exponential rate $\hat{\sigma}_\infty$ is the same regardless of the initial condition — all solutions converge at rate $\gamma_*$ once inside the basin (Theorem C.43 provides a universal rate for the local stability).

**Verification.** Compare $\hat{\sigma}_\infty$ across the ten amplitudes of §8.5.2.3:

$$
\frac{\max_i\hat{\sigma}_{\infty,i} - \min_i\hat{\sigma}_{\infty,i}}{\text{mean}_i\hat{\sigma}_{\infty,i}} < 0.05.
$$

All ten values should agree to within $5\%$ — the asymptotic rate is amplitude-independent. The transition time $t_*$ varies (it increases with $C_{\mathrm{ED}}(0)$), but the eventual rate does not.

---

#### 8.5.4 Pass/Fail Criteria

The three-stage convergence validation passes if and only if all five checks pass.

| Check | Tests | Pass condition |
|-------|-------|----------------|
| 1 (Stage I bounds) | Energy bounded; density confined; dissipation finite | All three conditions |
| 2 (Stage II convergence) | $L^2$, participation, gradient, unique $\omega$-limit | All four below $10^{-3}$ ($10^{-6}$ for $C_{\mathrm{ED}}$) |
| 3 (Stage III exponential) | Rate $< 5\%$ of $\gamma_*$; $R^2 > 0.999$; basin containment | All three conditions |
| 4 (Stage connectivity) | Sequential stages; smooth transition; non-empty Stage II at high amplitude; empty at low | All applicable conditions |
| 5 (Universal rate) | Ten-amplitude spread $< 5\%$ | Spread condition |

**Total integrations.** Check 1–4: $1$ integration at $A = 0.3$, $T = 50$. Check 5 (and §8.5.2.3): $10$ integrations at $A = 0.005$–$0.4$, $T = 60$. Parameter-set comparison (§8.5.2.4): $5$ integrations at $A = 0.2$, $T = 60$. Total: $16$ integrations.

---

#### 8.5.5 Failure Diagnosis

| Failure | Likely cause | Diagnostic |
|---------|-------------|-----------|
| Energy not bounded (Check 1 fails) | CFL violation or implicit-matrix error | Run energy dissipation test (§8.2.2); check $\Delta t$ |
| Density not converging to $\rho^*$ (Check 2 fails) | Penalty evaluation error; wrong $\rho^*$ | Check $P(\rho^*) = 0$; verify constitutive functions |
| Convergence to wrong limit (unique $\omega$-limit fails) | Penalty has multiple zeros ($P' \leq 0$ somewhere) | Check $P'(\rho)$ across $[0, \rho_{\max}]$; verify Principle 3 |
| Exponential rate wrong (Check 3 fails) | Incorrect spectral gap or Lyapunov rate | Run linear validation (§8.1); compare measured $\gamma$ to analytic |
| Solution leaves basin after entering (basin containment fails) | $\epsilon_0$ overestimated; time step too large | Reduce $\Delta t$; recalculate $\epsilon_0$ with tighter $C_{\mathrm{nl}}$ |
| No Stage II detected at $A = 0.3$ (Check 4 fails) | $\epsilon_0$ too large (basin encompasses the IC) | Check $\epsilon_0$; this is not necessarily an error — it means the local stability is very strong |
| Asymptotic rate varies with amplitude (Check 5 fails) | Nonlinear corrections persist to late time | Increase $T$; verify that $\mathcal{B}(T) \ll 1$ for all amplitudes |
| $t_*$ ordering wrong across parameter sets | Incorrect $\gamma_*$ or $\epsilon_0$ at one set | Run linear validation at the failing parameter set |

---

#### 8.5.6 Summary

| Aspect | Specification |
|--------|--------------|
| **Theorem tested** | C.76 (Three-Stage Convergence) |
| **Stages detected** | I (fast transient, $\hat{\beta} > 3\gamma_*$), II (algebraic, $\hat{\beta} < \gamma_*$, $\mathcal{B} > 1$), III (exponential, $\hat{\beta} \approx \gamma_*$, $\mathcal{B} < 1$) |
| **Transition time $t_*$** | Primary: $\inf\{t : \mathcal{B}(t) < 1\}$. Alternative: $\inf\{t : \hat{\beta}_{\mathrm{smooth}} \geq 0.9\gamma_*\}$ |
| **$t_*$ dependence on $C_{\mathrm{ED}}$** | $t_* \sim c\ln(C_{\mathrm{ED}}/\epsilon_0^2)$; measured at 10 amplitudes |
| **$t_*$ ordering across sets** | IV $<$ II $<$ V $<$ I $<$ III |
| **Five checks** | Stage I bounds, Stage II convergence, Stage III exponential, connectivity, universal rate |
| **Rate tolerance** | $5\%$ relative for $\hat{\sigma}_\infty$ vs. $\gamma_*$ |
| **Universal-rate spread** | $< 5\%$ across 10 amplitudes |
| **Total integrations** | $16$ ($1 + 10 + 5$) |
| **Failure diagnosis** | Eight-pattern table |

The three-stage convergence validation is the most comprehensive dynamical test in the Suite. It verifies Theorem C.76 — the synthesis of the entire long-time theory — by detecting each stage in the numerical solution, measuring the transition time between them, confirming the universal exponential rate, and verifying the dependence on the initial complexity and the canonical parameters. An implementation that passes this test has demonstrated that it correctly reproduces the global-to-local-to-exponential convergence structure that is the dynamical realization of the ED architectural ontology.

---

## 9. Implementation Notes

### 9.1 Python Implementation Notes

Python with NumPy and SciPy is the primary reference environment for the Simulation Suite (§0.4). This section provides environment-specific guidance for implementing the Suite in Python: the recommended library versions and functions, the performance patterns that avoid Python's overhead, and the memory layout conventions that ensure correct and efficient array operations.

---

#### 9.1.1 Recommended Libraries

The Python implementation requires three packages beyond the standard library:

| Package | Minimum version | Purpose | Key functions used |
|---------|----------------|---------|-------------------|
| **NumPy** | 1.24+ | Array operations, linear algebra basics | `ndarray`, `dot`, `sum`, `max`, `min`, `exp`, `log`, `cos`, `sin` |
| **SciPy** | 1.11+ | Sparse linear algebra, DCT, quadrature | `solve_banded`, `dct`, `quad`, `sparse` |
| **hashlib** | (stdlib) | SHA-256 for `spec_hash` and `content_hash` | `sha256` |

Optional packages that improve convenience but are not required:

| Package | Purpose | Used for |
|---------|---------|----------|
| **h5py** | HDF5 file I/O | Output in `.h5` format (§6.1.1) |
| **psutil** | System information | Environment capture: RAM, CPU model (§7.2) |
| **tqdm** | Progress bars | Sweep orchestration display (§4.5) |

**Version sensitivity.** NumPy 1.24 introduced `numpy.random.default_rng` (PCG64) as the recommended PRNG interface (§7.1.2.2). SciPy 1.11 uses the `scipy.fft` module (replacing the deprecated `scipy.fftpack`) for the DCT. Older versions may produce different DCT normalization conventions; the Suite requires the `scipy.fft.dct` interface with explicit `type=1` and `norm=None` parameters.

---

#### 9.1.2 Library Function Mapping

The Suite's pseudocode operations (§§1.3–1.5, §10.1 of the Atlas) map to specific NumPy/SciPy functions:

##### 9.1.2.1 Array Operations

| Suite operation | NumPy equivalent | Notes |
|----------------|-----------------|-------|
| Create array of zeros | `numpy.zeros(shape, dtype=numpy.float64)` | Always specify `dtype=float64` explicitly |
| Pointwise multiply | `a * b` (element-wise) | Both `a` and `b` must be the same shape |
| Pointwise divide | `a / b` | Division by zero raises warning; use safeguarded evaluation (§1.6.6) |
| Sum over array | `numpy.sum(a)` | Uses pairwise summation (more accurate than sequential) |
| Maximum of array | `numpy.max(a)` | Returns scalar; for index use `numpy.argmax(a)` |
| Dot product | `numpy.dot(a, b)` | For 1D arrays; equivalent to `sum(a * b)` |

##### 9.1.2.2 Tridiagonal Solver (Method A)

The implicit time step (§1.4.1) requires solving a tridiagonal system $\mathbf{A}\boldsymbol{\rho}^{n+1} = \mathbf{R}$ at each step. The recommended SciPy function is `scipy.linalg.solve_banded`:

- **Input format.** The tridiagonal matrix is stored in banded format: a $(3, N_{\mathrm{grid}})$ array where row 0 is the upper diagonal (padded with a leading zero), row 1 is the main diagonal, and row 2 is the lower diagonal (padded with a trailing zero).
- **Call.** `rho_new = scipy.linalg.solve_banded((1, 1), A_banded, rhs)`.
- **Cost.** $O(N_{\mathrm{grid}})$ — equivalent to the Thomas algorithm.
- **Positive definiteness.** The implicit matrix is symmetric positive definite (§1.4.1.1); `solve_banded` does not exploit this (it uses LU factorization, not Cholesky). For marginal performance improvement, use `scipy.linalg.solveh_banded` (which assumes Hermitian positive-definite and uses Cholesky), storing only the upper triangle.

**Caution.** SciPy's `solve_banded` modifies the input arrays in place (it overwrites `A_banded` and `rhs` during the solve). If the original values are needed later (e.g., for the Crank–Nicolson scheme, which uses the same matrix for the explicit half), copies must be made before the call.

##### 9.1.2.3 Discrete Cosine Transform (Method B)

The spectral method requires the Type-I DCT. The recommended function is `scipy.fft.dct`:

- **Forward transform.** `rho_hat = scipy.fft.dct(rho_phys, type=1, norm=None)`.
- **Inverse transform.** `rho_phys = scipy.fft.idct(rho_hat, type=1, norm=None)`.
- **Normalization.** With `norm=None`, the DCT-I is unnormalized: the forward transform computes $X_k = x_0 + (-1)^k x_{N-1} + 2\sum_{n=1}^{N-2}x_n\cos(\pi kn/(N-1))$, and the inverse divides by $2(N-1)$. The Suite's eigenbasis normalization (§5.3.1.2) requires an additional factor to produce the orthonormal coefficients $a_k$.

**Normalization factor.** To convert from SciPy's DCT output to the Suite's orthonormal Neumann coefficients:

$$
a_k = \frac{X_k}{N_{\mathrm{phys}} - 1} \cdot \begin{cases} 1/\sqrt{L} & k = 0, \\ \sqrt{2/(L(N_{\mathrm{phys}} - 1))} & 1 \leq k \leq N_{\mathrm{phys}} - 2, \\ 1/\sqrt{L(N_{\mathrm{phys}} - 1)} & k = N_{\mathrm{phys}} - 1. \end{cases}
$$

The precise factors depend on the DCT-I endpoint conventions. The correctness of the normalization is verified by the Parseval check (§5.3.4.1): $\sum_k|a_k|^2 = \|u\|_{L^2}^2$ to within $10^{-12}$.

##### 9.1.2.4 Adaptive Quadrature

The density potential $\Phi(\rho) = \int_{\rho^*}^{\rho}P(r)/M(r)\,dr$ (§5.1.2.1) is computed by `scipy.integrate.quad`:

- **Call.** `phi, error = scipy.integrate.quad(lambda r: P(r)/M(r), rho_star, rho_j, epsabs=1e-12)`.
- **Near-boundary handling.** When $\rho_j$ is close to $\rho_{\max}$, the integrand $P(r)/M(r)$ diverges. The `quad` function handles integrable singularities automatically (it uses adaptive subdivision near the singularity). For the canonical constitutive functions with $\beta = 2$: the closed-form expression (§5.1.2.1) should be used instead of quadrature, bypassing this issue entirely.

---

#### 9.1.3 Performance Tips

Python's interpreted execution model introduces overhead for operations that are fast in compiled languages (loop iterations, function calls, conditional branches). The following patterns minimize this overhead for the ED simulation engine.

##### 9.1.3.1 Vectorize All Grid Operations

Every operation that touches the density array must be vectorized — expressed as a NumPy array operation rather than a Python `for` loop. The performance difference is typically $100\times$–$1000\times$.

**Example: constitutive evaluation.** Instead of:

```
# SLOW: Python loop
for j in range(N_grid):
    M_vals[j] = M0 * (rho_max - rho[j])**beta
```

Use:

```
# FAST: Vectorized
M_vals = M0 * (rho_max - rho)**beta
```

The vectorized form computes all $N_{\mathrm{grid}}$ values in a single C-level loop inside NumPy, with no Python interpreter overhead per element.

**Critical operations to vectorize:**

| Operation | Vectorized form |
|-----------|----------------|
| Constitutive evaluation | `M_vals = M0 * (rho_max - rho)**beta` |
| Laplacian stencil | `Lap[1:-1] = (rho[:-2] - 2*rho[1:-1] + rho[2:]) / h**2` |
| Gradient-squared | `grad = (rho[2:] - rho[:-2]) / (2*h); Grad2[1:-1] = grad**2` |
| Operator assembly | `F = M_vals * Lap + Mp_vals * Grad2 - P_vals` |
| Energy quadrature | `E_pot = h * numpy.sum(Phi_vals)` |
| Complexity | `C_ED = h * numpy.sum(Grad2[1:-1])` |

##### 9.1.3.2 Avoid Repeated Memory Allocation

Allocate all workspace arrays once at initialization (§2.1.5) and reuse them at every time step. NumPy's array creation (`numpy.zeros`, `numpy.empty`) involves a memory allocation and a C-level `memset`; repeating this at every step adds $\sim 1\,\mu$s per array per step, which accumulates to $\sim 10$ ms over $10^4$ steps for $10$ workspace arrays.

**Pattern.** Store workspace arrays as attributes of the engine object (or as module-level variables) and overwrite their contents in place:

```
# At initialization:
self.Lap = numpy.zeros(N_grid)
self.Grad2 = numpy.zeros(N_grid)
self.F_vals = numpy.zeros(N_grid)

# At each time step:
self.Lap[1:-1] = (rho[:-2] - 2*rho[1:-1] + rho[2:]) / h2
# (overwrites Lap in place; no new allocation)
```

##### 9.1.3.3 Precompute Constants

All quantities that are constant during the integration (§2.1.5) should be computed once and stored:

| Quantity | Compute once | Reuse at every step |
|----------|-------------|---------------------|
| $h^2$ | `h2 = h**2` | Used in Laplacian stencil |
| $2h$ | `two_h = 2*h` | Used in gradient stencil |
| $e^{-\zeta\Delta t/\tau}$ | `ev = numpy.exp(-zeta*dt/tau)` | Used in participation update |
| $(1 - e^{-\zeta\Delta t/\tau})/\zeta$ | `fv = (1 - ev)/zeta` | Used in participation update |
| $\Delta t\,D/h^2$ | `dtD_h2 = dt*D/h2` | Used in implicit-matrix entries |

Recomputing these at every step would add $\sim 10$ transcendental-function evaluations ($\exp$, division) per step — negligible individually but avoidable.

##### 9.1.3.4 Use In-Place Operations Where Possible

NumPy supports in-place operations via the `out` parameter or the `+=`, `*=` operators:

```
# Out-of-place (creates a new array):
result = a + b

# In-place (modifies a):
numpy.add(a, b, out=a)
# or equivalently:
a += b
```

In-place operations avoid the allocation of a temporary array. For the ED engine, the most impactful in-place operations are in the RHS assembly (§1.4.1.1, Step 4e), where multiple terms are accumulated into the `RHS` array.

##### 9.1.3.5 Single-Threaded NumPy

By default, NumPy may use multi-threaded BLAS (OpenBLAS, MKL) for matrix operations. For the ED engine, the matrices are small ($N_{\mathrm{grid}} \leq 5120$) and the operations are tridiagonal solves, not dense matrix multiplications. Multi-threading adds overhead (thread creation, synchronization) without benefit at these sizes.

**Recommendation.** Set the environment variable `OMP_NUM_THREADS=1` (or `MKL_NUM_THREADS=1` for MKL) before launching the Python process. This forces single-threaded BLAS and eliminates the threading overhead. The parallelization is handled at the task level (§4.5), not at the array-operation level.

---

#### 9.1.4 Memory Layout

##### 9.1.4.1 Array Order

NumPy arrays default to C-order (row-major) memory layout. For the ED engine:

- **1D arrays** (density, Laplacian, gradient-squared, etc.): contiguous in memory by construction (1D arrays have only one layout).
- **2D arrays** (density on $\Omega_2$): stored in C-order (row-major), so `rho[i, j]` and `rho[i, j+1]` are adjacent in memory. The stencil loops should iterate over $j$ (the column index, second axis) in the innermost loop to achieve stride-one access.

The 2D Laplacian stencil (§1.3.1.2) accesses `rho[i-1,j]`, `rho[i+1,j]`, `rho[i,j-1]`, `rho[i,j+1]`. In C-order, the $j$-adjacent accesses are stride-one (fast) and the $i$-adjacent accesses are stride-$N_y$ (slow). The stencil is therefore most efficient when vectorized along $j$ (the fast axis):

```
# Vectorized 2D Laplacian (fast j-axis):
Lap[1:-1, 1:-1] = (
    (rho[:-2, 1:-1] + rho[2:, 1:-1] - 2*rho[1:-1, 1:-1]) / hx2
  + (rho[1:-1, :-2] + rho[1:-1, 2:] - 2*rho[1:-1, 1:-1]) / hy2
)
```

This vectorized form processes the entire interior grid in a single NumPy operation, with C-level loops that access memory in the optimal order.

##### 9.1.4.2 Data Type

All floating-point arrays use `numpy.float64` (IEEE 754 double precision). This is the default for NumPy and matches the Suite's precision requirement (§0.5). Using `float32` would halve the memory but reduce the precision to $\sim 7$ digits, which is insufficient for the $10^{-10}$-level agreement needed for Tier 2 reproducibility (§7.1.4.2).

Integer arrays (step counters, mode indices) use `numpy.int64` to avoid overflow for long integrations ($> 10^5$ steps) and large mode counts.

##### 9.1.4.3 Avoiding Copies

NumPy slicing returns *views* (references to the same memory), not copies. This is efficient (no data movement) but dangerous (modifying a view modifies the original):

```
# This is a VIEW (no copy):
interior = rho[1:-1]  # shares memory with rho

# Modifying interior ALSO modifies rho:
interior[:] = 0  # rho[1:-1] is now zero
```

The ED engine uses views intentionally for read-only access (extracting the interior points for the stencil) and explicit copies (`rho.copy()`) for write access (the history buffer `rho_prev = rho.copy()` in §2.3.1, Phase 1, Step 3).

---

#### 9.1.5 Output I/O

##### 9.1.5.1 CSV Output

The time-series CSV is written incrementally using Python's built-in `open` and `write`:

```
# At initialization:
f = open(filepath, 'w')
f.write(header_string)  # metadata + field names

# At each output step:
f.write(','.join(f'{v:.15e}' for v in obs_values) + '\n')
f.flush()  # ensure data is on disk
```

The `flush()` call after each row ensures that partial results survive a crash (§2.4.1.2).

##### 9.1.5.2 NPZ Output

For binary output, use `numpy.savez_compressed`:

```
numpy.savez_compressed(filepath,
    time=time_array,
    energy=energy_array,
    C_ED=C_ED_array,
    ...,
    metadata=metadata_dict)
```

The NPZ file is written in a single call at the end of the integration (or at each checkpoint). It does not support incremental writing; the arrays are accumulated in memory during the integration and written once.

##### 9.1.5.3 HDF5 Output

For HDF5, use `h5py`:

```
with h5py.File(filepath, 'w') as f:
    f.create_dataset('time', data=time_array)
    f.create_dataset('energy', data=energy_array, compression='gzip')
    f.attrs['D'] = 0.6
    f.attrs['experiment_id'] = '3.1a'
```

HDF5 supports incremental writing via resizable datasets, enabling the same row-by-row append pattern as CSV but in binary form.

---

#### 9.1.6 Summary

| Aspect | Recommendation |
|--------|---------------|
| **NumPy version** | $\geq 1.24$ |
| **SciPy version** | $\geq 1.11$ |
| **Tridiagonal solver** | `scipy.linalg.solve_banded((1,1), ...)` |
| **DCT** | `scipy.fft.dct(type=1, norm=None)` with manual normalization |
| **Quadrature** | `scipy.integrate.quad` with `epsabs=1e-12`; closed form preferred |
| **Vectorization** | All grid operations via NumPy array expressions; no Python `for` loops over grid points |
| **Memory** | Pre-allocate all workspace at initialization; reuse via in-place operations |
| **Threading** | `OMP_NUM_THREADS=1`; parallelism at the task level only |
| **Array dtype** | `numpy.float64` throughout |
| **2D layout** | C-order (row-major); vectorize along the fast (last) axis |
| **Output** | CSV (incremental, `flush` per row); NPZ (single write); HDF5 (incremental with `h5py`) |

The Python implementation is the reference: all other implementations (Julia, MATLAB) are validated against it. The performance optimizations above ensure that the Python implementation is fast enough ($\sim 4\,\mu$s per step at $N = 512$ in 1D) to complete the full Atlas in $\sim 4$ hours on a single core, meeting the computational budget of §0.5.

---

### 9.2 Julia Implementation Notes

Julia is the performance-critical environment for the Simulation Suite (§0.4). Its compilation model (just-in-time compilation to native machine code) eliminates the interpreter overhead that limits Python, allowing the time-stepping loop to run at near-C speed without sacrificing the high-level expressiveness needed for the Suite's modular architecture. The Julia implementation is recommended for the large parameter sweeps (§4.1: $324$–$689$ integrations), the long-time integrations (Atlas §7: $T = 50$–$60$), and the high-resolution near-horizon experiments (Atlas §6: $N = 1024$–$5120$).

---

#### 9.2.1 Recommended Packages

The Julia implementation requires the following packages:

| Package | Version | Purpose | Key functions |
|---------|---------|---------|---------------|
| **LinearAlgebra** | (stdlib) | Tridiagonal solve, norms | `Tridiagonal`, `ldiv!`, `norm` |
| **FFTW** | $\geq 0.3.0$ | DCT via the FFTW library | `FFTW.r2r`, `FFTW.REDFT00` |
| **Random** | (stdlib) | PRNG seeding | `seed!`, `randn` |
| **SHA** | (stdlib) | SHA-256 hashing | `sha256` |
| **Printf** | (stdlib) | Formatted output for CSV | `@sprintf` |

Optional packages for extended functionality:

| Package | Purpose | Used for |
|---------|---------|----------|
| **DifferentialEquations.jl** | ODE/PDE solvers | Alternative time-stepping backend; ETD schemes |
| **HDF5.jl** | HDF5 file I/O | Output in `.h5` format |
| **JLD2.jl** | Julia-native binary I/O | Checkpoints (§2.5) |
| **Distributed** | Multi-process parallelism | Sweep orchestration (§4.5) |

**FFTW configuration.** FFTW must be configured with the `REDFT00` transform type for the DCT-I. The first call to `FFTW.r2r` with a given array size triggers FFTW's planner, which measures the optimal algorithm for that size and caches the plan. Subsequent calls reuse the plan at no planning cost. For the Suite, the plan is created during initialization (§2.1.5) and stored for reuse throughout the time-stepping loop:

```
plan = FFTW.plan_r2r(workspace_array, FFTW.REDFT00)
```

The plan is specific to the array size $N_{\mathrm{phys}}$; if the size changes (e.g., between the spectral grid and the de-aliased physical grid), separate plans are needed for each size.

---

#### 9.2.2 Type Stability

Julia's performance depends critically on **type stability**: every variable and every function return value must have a type that the compiler can infer at compile time, without inspecting the runtime values. Type-unstable code forces the compiler to generate dynamic dispatch (boxing, unboxing, method lookup), which is $10\times$–$100\times$ slower than type-stable code.

##### 9.2.2.1 Critical Type-Stability Requirements

The following components of the engine must be type-stable:

**Constitutive functions.** The mobility $M(\rho)$ and penalty $P(\rho)$ must return `Float64` for any `Float64` input. If the constitutive functions are implemented as closures or anonymous functions, they must be wrapped in a type-stable container (a `struct` with concrete field types, not an abstract `Function` field):

```
# TYPE-STABLE: struct with concrete function types
struct PowerLawMobility
    M0::Float64
    beta::Float64
    rho_max::Float64
end

(m::PowerLawMobility)(rho) = m.M0 * (m.rho_max - rho)^m.beta
```

Storing the constitutive function as `Function` (the abstract type) or `Any` would destroy type stability in every function that calls it.

**Parameter record.** The `CanonicalParams` struct must have concrete field types (all `Float64`, `Int64`, or `String`), not abstract types (`Real`, `Number`, `Any`):

```
struct CanonicalParams
    D::Float64
    H::Float64
    zeta::Float64
    tau::Float64
    rho_star::Float64
    rho_max::Float64
    # ... all Float64
end
```

**The time-stepping loop.** Every variable inside the loop body (`Lap`, `Grad2`, `F_vals`, `rho_new`, etc.) must have a type known at compile time. This is automatic if the workspace arrays are pre-allocated as `Vector{Float64}` and the constitutive functions are type-stable.

##### 9.2.2.2 Diagnosing Type Instability

Julia provides the `@code_warntype` macro to detect type instabilities:

```
@code_warntype time_step!(state, params, workspace)
```

Any variable highlighted in red (type `Any` or a union type) indicates a type instability. The engine must be developed with `@code_warntype` checks on every performance-critical function (the time-step function, the operator evaluation, the constitutive evaluation, the tridiagonal solve wrapper). No red highlights are permitted in these functions.

---

#### 9.2.3 Performance Tuning

##### 9.2.3.1 In-Place Operations

Julia supports in-place modification of arrays through functions ending in `!` (by convention). The time-stepping loop should use exclusively in-place operations to avoid allocation:

| Operation | Allocating (slow) | In-place (fast) |
|-----------|-------------------|-----------------|
| Array addition | `c = a .+ b` | `c .= a .+ b` (broadcast assignment) |
| Array multiply | `c = a .* b` | `@. c = a * b` (fused broadcast) |
| Tridiagonal solve | `x = A \ b` | `ldiv!(x, factorize(A), b)` |
| DCT | `y = plan * x` | `mul!(y, plan, x)` |
| Constitutive eval | `M_vals = M.(rho)` | `M_vals .= M.(rho)` or `map!(M, M_vals, rho)` |

The `@.` macro applies broadcast fusion: `@. c = a * b + d` computes the entire expression in a single pass without intermediate temporaries.

##### 9.2.3.2 The `@inbounds` and `@simd` Annotations

For inner loops that are known to be within bounds (e.g., the stencil evaluation, where the loop range excludes the boundary points):

```
@inbounds @simd for j in 2:N-1
    Lap[j] = (rho[j-1] - 2*rho[j] + rho[j+1]) / h2
end
```

`@inbounds` disables array bounds checking (which adds $\sim 1$ ns per access — significant in a tight loop). `@simd` enables SIMD vectorization of the loop body (processing 2–4 elements per instruction on modern CPUs). Together, they can improve the stencil loop performance by $2\times$–$4\times$ compared to a standard loop.

**Safety note.** `@inbounds` is used only for loops whose bounds have been verified to be safe (the stencil loop's range $2:N-1$ never accesses out-of-bounds indices). Using `@inbounds` on an incorrectly bounded loop produces silent memory corruption — the most dangerous kind of bug. The engine uses `@inbounds` only in the stencil functions, which are individually tested by the structural checks of §1.3.1.4.

##### 9.2.3.3 Pre-Allocated Tridiagonal System

Julia's `LinearAlgebra.Tridiagonal` type stores the three diagonals (lower, main, upper) as separate vectors and provides optimized $O(N)$ factorization and solve:

```
# At initialization:
A = Tridiagonal(lower, diag, upper)

# At each time step:
# Update diag, lower, upper in place with new mobility values
diag .= 1.0 .+ 2*dtD .* M_vals ./ h2
lower .= -dtD .* M_vals[1:end-1] ./ h2
upper .= -dtD .* M_vals[2:end] ./ h2
# (Neumann boundary modifications)
ldiv!(rho_new, lu!(A), rhs)
```

The `lu!` function performs the LU factorization in place (overwriting the `Tridiagonal` object), and `ldiv!` solves the system in place (overwriting `rho_new`). No temporary arrays are allocated during the solve.

**Caution.** `lu!` modifies the `Tridiagonal` object destructively. If the original diagonals are needed after the solve (e.g., for the Crank–Nicolson explicit half), they must be saved before calling `lu!`.

##### 9.2.3.4 FFTW Plan Reuse

The FFTW plan (§9.2.1) is the most expensive object to create ($\sim 1$ ms for $N = 192$) and the cheapest to reuse ($\sim 1\,\mu$s per transform). The plan must be created once and stored:

```
# At initialization:
fft_plan = FFTW.plan_r2r(buffer, FFTW.REDFT00; flags=FFTW.MEASURE)

# At each substep of ETD-RK4:
mul!(rho_hat, fft_plan, rho_phys)        # forward DCT
ldiv!(rho_phys, fft_plan, rho_hat)       # inverse DCT
```

The `FFTW.MEASURE` flag tells FFTW to measure the performance of several algorithms and select the fastest, rather than using a heuristic guess (`FFTW.ESTIMATE`). The measurement adds $\sim 100$ ms to the initialization but produces a plan that is $\sim 2\times$ faster than the estimate-based plan for the $N = 192$ de-aliased grid.

##### 9.2.3.5 Avoiding Global Variables

Julia's compiler cannot infer the type of global variables (because they can be reassigned to any type at any time). All parameters, workspace arrays, and constitutive functions must be passed as function arguments or stored in typed structs — never as module-level global variables.

The recommended pattern is a single `SimulationState` struct that holds all mutable state:

```
mutable struct SimulationState
    rho::Vector{Float64}
    v::Float64
    t::Float64
    n::Int64
    # workspace arrays...
end
```

The time-stepping function takes this struct as its first argument:

```
function time_step!(state::SimulationState, params::CanonicalParams, ...)
    # all operations on state.rho, state.v, etc.
end
```

This pattern ensures type stability (the compiler knows the types of all fields) and avoids global-variable overhead.

---

#### 9.2.4 Memory Layout

##### 9.2.4.1 Column-Major Order

Julia arrays are **column-major** (Fortran-order): `A[i, j]` and `A[i+1, j]` are adjacent in memory, while `A[i, j]` and `A[i, j+1]` are separated by $N_x$ elements. This is the opposite of Python's C-order.

For the 2D stencil on $\Omega_2$: the innermost loop should iterate over the *first* index $i$ (the column, the fast axis in Julia):

```
@inbounds for j in 2:Ny-1
    @simd for i in 2:Nx-1
        Lap[i,j] = (rho[i-1,j] + rho[i+1,j] - 2*rho[i,j]) / hx2 +
                   (rho[i,j-1] + rho[i,j+1] - 2*rho[i,j]) / hy2
    end
end
```

The `i` loop (innermost, SIMD-annotated) accesses `rho[i-1,j]`, `rho[i,j]`, `rho[i+1,j]` — stride-one in memory. The `j` loop (outermost) steps across columns.

##### 9.2.4.2 Contiguous Subarrays

Julia's `@view` macro creates a view (reference, no copy) of a subarray. Views of contiguous memory regions (e.g., `@view rho[2:N-1]` for a 1D array) are as fast as the original array. Views of non-contiguous regions (e.g., `@view rho[1:2:end]` for every other element) involve strided access and are slower.

For the ED engine, all array accesses are contiguous (the stencil accesses consecutive elements), so views are appropriate and efficient. The engine uses `@view` for read-only access to subarrays (e.g., extracting the interior points for the stencil) and direct indexing for write access (overwriting workspace arrays in place).

---

#### 9.2.5 Parallelization

Julia's `Distributed` module provides multi-process parallelism for the sweep orchestrator (§4.5):

```
using Distributed
addprocs(16)  # spawn 16 worker processes

@everywhere include("ed_engine.jl")  # load engine on all workers

results = pmap(task_specs) do spec
    run_experiment(spec)  # each worker runs one experiment
end
```

The `pmap` function distributes the task list across workers with dynamic load balancing (each worker receives its next task upon completion of the previous one, §4.5.5). No shared mutable state is passed between workers; each worker operates on its own copy of the engine and writes to its own output files.

For cluster execution (§4.5.3): Julia's `ClusterManagers.jl` package provides interfaces to SLURM, PBS, and SGE schedulers, enabling `addprocs` to spawn workers on remote cluster nodes transparently.

---

#### 9.2.6 Expected Performance

| Operation | Python (NumPy) | Julia | Speedup |
|-----------|----------------|-------|---------|
| Constitutive evaluation ($N = 512$) | $\sim 2\,\mu$s | $\sim 0.3\,\mu$s | $\sim 7\times$ |
| Laplacian stencil ($N = 512$) | $\sim 1\,\mu$s | $\sim 0.2\,\mu$s | $\sim 5\times$ |
| Tridiagonal solve ($N = 512$) | $\sim 3\,\mu$s | $\sim 0.5\,\mu$s | $\sim 6\times$ |
| DCT ($N = 192$) | $\sim 5\,\mu$s | $\sim 2\,\mu$s | $\sim 2.5\times$ |
| Full time step (Method A, $N = 512$) | $\sim 10\,\mu$s | $\sim 2\,\mu$s | $\sim 5\times$ |
| Full Atlas ($\sim 1{,}800$ integrations) | $\sim 4$ hours | $\sim 50$ min | $\sim 5\times$ |

The $5\times$ speedup over Python comes primarily from the elimination of interpreter overhead in the constitutive evaluation and the stencil computation (where Julia's compiled loops are $5$–$7\times$ faster than NumPy's vectorized operations). The DCT speedup is smaller ($2.5\times$) because both implementations call the same FFTW library; the Julia advantage is in the surrounding overhead (function-call dispatch, array bookkeeping).

The Julia implementation is recommended whenever wall-clock time is a constraint: the full Atlas completes in under an hour (versus $4$ hours in Python), and the large parameter sweeps complete in minutes (versus tens of minutes in Python).

---

#### 9.2.7 Summary

| Aspect | Recommendation |
|--------|---------------|
| **Julia version** | $\geq 1.9$ |
| **FFT library** | FFTW.jl with `REDFT00`; plan with `FFTW.MEASURE` |
| **Tridiagonal solve** | `Tridiagonal` + `lu!` + `ldiv!` (all in-place) |
| **Type stability** | All structs with concrete types; no `Any` or `Function` fields; verify with `@code_warntype` |
| **In-place operations** | `.=` broadcast assignment; `@.` fused broadcast; `mul!`, `ldiv!` |
| **Loop annotations** | `@inbounds @simd` on verified inner loops |
| **Memory layout** | Column-major; innermost loop over first index for 2D stencils |
| **No globals** | All state in typed structs; passed as function arguments |
| **Parallelism** | `Distributed` + `pmap` for sweep orchestration |
| **Expected performance** | $\sim 2\,\mu$s per step (Method A, $N = 512$); $\sim 50$ min for the full Atlas |

The Julia implementation provides the best single-core performance of the three supported environments. Its compilation model eliminates the vectorization requirement of Python (explicit `for` loops in Julia are as fast as NumPy's vectorized operations), enabling a more natural coding style that closely follows the Suite's pseudocode. The type-stability discipline is the main development-time cost: every struct and every function must be checked for type stability, and any regression must be caught immediately (a single type-unstable function can degrade the entire loop by $10\times$).

---

### 9.3 MATLAB Implementation Notes

MATLAB is the verification environment for the Simulation Suite (§0.4). Its role is not to provide the fastest or the most flexible implementation, but to serve as an independent cross-check: if the Python and Julia implementations agree but the MATLAB implementation disagrees, the discrepancy is investigated; if all three agree, the result is certified as implementation-independent. MATLAB's ubiquity in engineering and physics departments, its matrix-centric programming model, and its integrated visualization make it well-suited for this verification role.

---

#### 9.3.1 Matrix Operations

MATLAB's core strength is matrix and array computation. The ED engine maps naturally onto MATLAB's array operations because every grid-level computation — the stencil evaluation, the constitutive evaluation, the operator assembly, the observable extraction — is an element-wise or matrix operation on the density array.

##### 9.3.1.1 Density as a Column Vector

The density array $\boldsymbol{\rho}$ is stored as a column vector of length $N_{\mathrm{grid}}$:

```
rho = zeros(N_grid, 1);   % Column vector, double precision
```

MATLAB's default numeric type is `double` (IEEE 754 Float64), matching the Suite's precision requirement. No explicit type annotation is needed.

All workspace arrays (Laplacian, gradient-squared, operator values, RHS) are column vectors of the same size:

```
Lap    = zeros(N_grid, 1);
Grad2  = zeros(N_grid, 1);
F_vals = zeros(N_grid, 1);
RHS    = zeros(N_grid, 1);
```

##### 9.3.1.2 Vectorized Stencil Computation

The Laplacian stencil (§1.3.1.1) is computed using MATLAB's colon indexing:

```
% Interior points (j = 2 to N_grid-1):
Lap(2:end-1) = (rho(1:end-2) - 2*rho(2:end-1) + rho(3:end)) / h^2;

% Neumann boundary (j = 1, left):
Lap(1) = 2*(rho(2) - rho(1)) / h^2;

% Neumann boundary (j = N_grid, right):
Lap(end) = 2*(rho(end-1) - rho(end)) / h^2;
```

The gradient-squared:

```
Grad2(2:end-1) = ((rho(3:end) - rho(1:end-2)) / (2*h)).^2;
Grad2(1)   = 0;
Grad2(end) = 0;
```

The operator assembly:

```
F_vals = M_vals .* Lap + Mp_vals .* Grad2 - P_vals;
```

The `.*` operator is element-wise multiplication; `.^` is element-wise power. These are MATLAB's analogues of NumPy's vectorized operations and achieve comparable performance (both call optimized C/Fortran routines internally).

##### 9.3.1.3 Constitutive Evaluation

The constitutive functions are evaluated element-wise on the density vector:

```
M_vals  = M0 * (rho_max - rho).^beta;
Mp_vals = -beta * M0 * (rho_max - rho).^(beta - 1);
P_vals  = P0 * (rho - rho_star);
```

For the default constitutive functions ($\beta = 2$): `(rho_max - rho).^2` is a single vectorized operation with no loop overhead.

##### 9.3.1.4 Two-Dimensional Arrays

On $\Omega_2$, the density is stored as a 2D matrix:

```
rho = zeros(Nx_grid, Ny_grid);   % Nx_grid x Ny_grid matrix
```

MATLAB uses **column-major** order (same as Julia, opposite of Python): `rho(i, j)` and `rho(i+1, j)` are adjacent in memory. The 2D Laplacian stencil is vectorized using MATLAB's matrix indexing:

```
Lap(2:end-1, 2:end-1) = ...
    (rho(1:end-2, 2:end-1) + rho(3:end, 2:end-1) - 2*rho(2:end-1, 2:end-1)) / hx^2 + ...
    (rho(2:end-1, 1:end-2) + rho(2:end-1, 3:end) - 2*rho(2:end-1, 2:end-1)) / hy^2;
```

The column-major layout means the $i$-index (first index) is the fast axis, so the stencil accesses along $i$ are stride-one.

---

#### 9.3.2 Solver Choices

##### 9.3.2.1 Tridiagonal Solver (1D, Method A)

MATLAB's backslash operator `\` is the recommended solver for the implicit system:

```
rho_new = A \ RHS;
```

When `A` is a tridiagonal matrix (constructed as a `sparse` matrix or a full matrix with tridiagonal structure), the backslash operator automatically detects the tridiagonal structure and uses the Thomas algorithm — $O(N)$ operations, identical to SciPy's `solve_banded` and Julia's `Tridiagonal` solver.

**Sparse construction.** The implicit matrix is best constructed as a sparse matrix:

```
% Main diagonal:
d_main = 1 + 2*dt*D*M_vals/h^2;
% Off-diagonals:
d_upper = -dt*D*M_vals(1:end-1)/h^2;
d_lower = -dt*D*M_vals(2:end)/h^2;

% Neumann boundary modifications:
d_main(1)   = 1 + 2*dt*D*M_vals(1)/h^2;
d_upper(1)  = -2*dt*D*M_vals(1)/h^2;
d_main(end) = 1 + 2*dt*D*M_vals(end)/h^2;
d_lower(end) = -2*dt*D*M_vals(end)/h^2;

A = spdiags([d_lower, d_main, d_upper], [-1, 0, 1], N_grid, N_grid);
```

The `spdiags` function creates a sparse matrix from diagonal vectors. The backslash operator on a sparse tridiagonal matrix calls LAPACK's `dgtsv` (the Thomas algorithm) — confirmed by checking `spparms('spumoni', 1)` for diagnostic output.

**Full-matrix alternative.** For small $N_{\mathrm{grid}}$ ($< 100$), the sparse overhead may exceed the benefit. In that case, a full (dense) matrix and the standard backslash are acceptable:

```
A = diag(d_main) + diag(d_upper, 1) + diag(d_lower, -1);
rho_new = A \ RHS;
```

The backslash on a full matrix uses LU factorization ($O(N^3)$), which is wasteful for tridiagonal systems but acceptable at small $N$.

##### 9.3.2.2 Banded Solver (2D, Method A)

For the 2D implicit system, the matrix has bandwidth $N_x$ and is stored as a sparse matrix. The backslash operator selects an appropriate direct solver (typically UMFPACK for general sparse, or a banded solver if the structure is detected). For $N = 64$ per direction: the system has $\sim 4{,}000$ unknowns and the sparse solve takes $\sim 1$ ms — adequate for the Atlas 2D experiments.

##### 9.3.2.3 DCT (Method B)

MATLAB provides a built-in `dct` function in the Signal Processing Toolbox. However, this function computes the DCT-II (the standard "DCT"), not the DCT-I required by the Suite's Neumann eigenbasis. The DCT-I must be computed via the FFT:

```
% DCT-I of a vector x of length N:
% Extend x to length 2*(N-1) by mirroring:
x_ext = [x; flipud(x(2:end-1))];
X = real(fft(x_ext));
dct1_result = X(1:N);
```

This exploits the relationship between the DCT-I and the DFT of the symmetrically extended sequence. The cost is $O(N\log N)$ (one FFT of length $2(N-1)$).

**Normalization.** The FFT-based DCT-I produces unnormalized output (analogous to SciPy's `norm=None`). The same normalization factors as §9.1.2.3 apply, adjusted for MATLAB's $1$-based indexing.

**Alternative: FFTW MEX interface.** For higher performance, FFTW can be called from MATLAB via a MEX interface (e.g., the `fftw_mex` package), which provides direct access to the `REDFT00` transform. This avoids the mirroring overhead and matches the Julia/FFTW interface exactly.

##### 9.3.2.4 Adaptive Quadrature

MATLAB's `integral` function provides adaptive quadrature:

```
phi_j = integral(@(r) P(r)./M(r), rho_star, rho_j, 'AbsTol', 1e-12);
```

For the default constitutive functions: the closed-form expression (§5.1.2.1) is used instead, evaluated as:

```
phi_j = 0.5 ./ (rho_max - rho_j) - log(0.5 ./ (rho_max - rho_j)) - 1;
```

This vectorized expression computes $\Phi(\rho_j)$ at all grid points simultaneously.

---

#### 9.3.3 Visualization Tools

MATLAB's integrated plotting capabilities make it the most convenient environment for generating the Atlas figures. While the Suite specifies figure data files (§6.3) rather than rendered figures, MATLAB can produce publication-quality plots directly from the simulation output for rapid visual inspection during development and debugging.

##### 9.3.3.1 Time-Series Plots

The standard semilog-$y$ energy plot (Atlas Figure 1.2, top panel):

```
semilogy(time, energy, 'LineWidth', 1.5);
xlabel('t'); ylabel('\mathcal{E}(t)');
title('Energy dissipation');
```

The dissipation-channel comparison (Atlas Figure 5.2):

```
semilogy(time, D_diff, 'b-', time, D_pen, 'r-', time, D_part, 'g-');
legend('Gradient', 'Penalty', 'Participation');
```

##### 9.3.3.2 Phase Portraits

The $(a_0, v)$ phase portrait (Atlas Figure 2.1):

```
plot(a_0, v, 'b-', 'LineWidth', 1);
hold on; plot(a_0(1), v(1), 'ko', 'MarkerFaceColor', 'k');
xlabel('a_0'); ylabel('v');
```

##### 9.3.3.3 Spectral Bar Charts

The spectral snapshot (Atlas Figure 4.7):

```
bar(0:N_obs-1, abs_amps(time_index, :));
set(gca, 'YScale', 'log');
xlabel('Mode k'); ylabel('|a_k|');
```

##### 9.3.3.4 Contour Maps

The regime map (Atlas Figure 2.7):

```
contourf(D_grid, zeta_grid, D0_grid);
hold on;
% Plot the Boundary Surface Sigma:
fimplicit(@(D, z) (D - z).^2 - 4*(1-D), [0 1 0 5], 'k-', 'LineWidth', 2);
colorbar; xlabel('D'); ylabel('\zeta');
```

The visualization is not part of the Suite's reproducibility chain (the figure data files are the reproducible output; the plots are for inspection only). However, MATLAB's ability to produce these plots in a few lines makes it the fastest path from simulation to visual verification during the development cycle.

---

#### 9.3.4 MATLAB-Specific Considerations

##### 9.3.4.1 1-Based Indexing

MATLAB arrays are 1-based: the first element is `rho(1)`, not `rho(0)`. The Suite's 0-based mode index ($k = 0, 1, \ldots$) must be mapped to MATLAB's 1-based indexing:

| Suite convention | MATLAB equivalent |
|-----------------|-------------------|
| Mode $k = 0$ | `a(1)` |
| Mode $k = n$ | `a(n+1)` |
| Grid point $j = 0$ | `rho(1)` |
| Grid point $j = N+1$ | `rho(N_grid)` |

This offset must be applied consistently throughout the implementation. A common error is to use `rho(j)` where `rho(j+1)` is needed, producing a one-element shift in the stencil and corrupting the boundary conditions.

##### 9.3.4.2 Structs for Parameter Records

MATLAB's `struct` type provides named fields:

```
params = struct('D', 0.6, 'H', 0.4, 'zeta', 0.5, 'tau', 1.0, ...
                'rho_star', 0.5, 'rho_max', 1.0);
```

Unlike Julia's typed structs, MATLAB structs do not enforce field types — any field can hold any value. The validation checks (§2.2.3) must be performed explicitly (MATLAB does not provide compile-time type safety).

##### 9.3.4.3 Function Handles for Constitutive Functions

The constitutive functions are represented as function handles:

```
M  = @(rho) M0 * (rho_max - rho).^beta;
Mp = @(rho) -beta * M0 * (rho_max - rho).^(beta - 1);
P  = @(rho) P0 * (rho - rho_star);
```

Function handles support element-wise operations on vectors (via `.*` and `.^`), so `M(rho)` evaluates the mobility at all grid points simultaneously.

##### 9.3.4.4 No Native Parallelism in Base MATLAB

The `parfor` loop (from the Parallel Computing Toolbox) is required for sweep parallelization (§4.5). Without the Toolbox, sweeps must be executed sequentially using a standard `for` loop. The sequential execution is slower ($\sim 4$ hours for the full Atlas) but produces identical results.

```
% With Parallel Computing Toolbox:
parfor i = 1:n_tasks
    results{i} = run_experiment(task_specs{i});
end

% Without (sequential fallback):
for i = 1:n_tasks
    results{i} = run_experiment(task_specs{i});
end
```

##### 9.3.4.5 File I/O

MATLAB's native `.mat` format (v7.3, HDF5-based) is the recommended output format:

```
save(filepath, 'time', 'energy', 'C_ED', 'metadata', '-v7.3');
```

The `-v7.3` flag produces an HDF5-based file that is readable by Python (`scipy.io.loadmat` or `h5py`), Julia (`MAT.jl` or `HDF5.jl`), and MATLAB itself. This cross-environment readability is essential for the Suite's cross-implementation comparison.

CSV output is also supported:

```
writematrix([time, energy, C_ED, ...], filepath);
```

The `writematrix` function (R2019a+) writes numeric arrays to CSV with full double-precision digits. For older MATLAB versions, `dlmwrite` provides equivalent functionality.

---

#### 9.3.5 Expected Performance

| Operation | MATLAB | Python (NumPy) | Julia |
|-----------|--------|----------------|-------|
| Constitutive evaluation ($N = 512$) | $\sim 3\,\mu$s | $\sim 2\,\mu$s | $\sim 0.3\,\mu$s |
| Laplacian stencil ($N = 512$) | $\sim 2\,\mu$s | $\sim 1\,\mu$s | $\sim 0.2\,\mu$s |
| Tridiagonal solve ($N = 512$) | $\sim 2\,\mu$s | $\sim 3\,\mu$s | $\sim 0.5\,\mu$s |
| Full time step (Method A, $N = 512$) | $\sim 12\,\mu$s | $\sim 10\,\mu$s | $\sim 2\,\mu$s |
| Full Atlas ($\sim 1{,}800$ integrations) | $\sim 5$ hours | $\sim 4$ hours | $\sim 50$ min |

MATLAB is the slowest of the three environments by a modest margin ($\sim 20\%$ slower than Python for most operations). The overhead comes from MATLAB's JIT compilation model, which is less aggressive than Julia's and less optimized for element-wise array operations than NumPy's C-level vectorized routines. The tridiagonal solve is the exception: MATLAB's backslash operator calls the same LAPACK routines as SciPy and is comparably fast.

The $\sim 5$-hour wall time for the full Atlas is within the computational budget of §0.5 ($< 1$ day on a single core). For the verification role (running a subset of experiments for cross-checking), the MATLAB implementation typically needs only $\sim 30$ minutes ($\sim 100$ selected experiments).

---

#### 9.3.6 Summary

| Aspect | Recommendation |
|--------|---------------|
| **MATLAB version** | $\geq$ R2023a |
| **Required toolboxes** | Signal Processing (for DCT reference); Parallel Computing (for `parfor`, optional) |
| **Density storage** | Column vector `zeros(N_grid, 1)` |
| **Tridiagonal solver** | `spdiags` + backslash (`\`) on sparse matrix |
| **DCT-I** | FFT of symmetrically extended sequence; or FFTW MEX for higher performance |
| **Quadrature** | `integral` with `AbsTol = 1e-12`; closed form preferred |
| **Constitutive functions** | Function handles with element-wise operators (`.*`, `.^`) |
| **Indexing** | 1-based; mode $k$ is `a(k+1)`; grid point $j$ is `rho(j+1)` |
| **Output format** | `.mat` v7.3 (HDF5-based, cross-environment readable) |
| **Visualization** | `semilogy`, `plot`, `bar`, `contourf` for rapid visual inspection |
| **Parallelism** | `parfor` (Parallel Computing Toolbox) or sequential `for` |
| **Performance** | $\sim 12\,\mu$s per step; $\sim 5$ hours for the full Atlas |
| **Primary role** | Independent cross-check against Python and Julia |

The MATLAB implementation completes the three-environment verification framework. Its matrix-centric programming model produces clean, readable code that closely mirrors the mathematical formulas of the Suite. Its integrated visualization enables rapid visual inspection of every Atlas figure directly from the simulation output. Its cross-environment `.mat` file format enables seamless data exchange with the Python and Julia implementations. As the third independent implementation, it provides the final confirmation that the Atlas results are not artifacts of any single environment — they are structural properties of the canonical ED system.

---

### 9.4 Performance Tuning

The preceding sections (§§9.1–9.3) provided environment-specific optimization guidance. This section provides **cross-environment** performance principles: strategies that improve performance in every implementation regardless of the language, organized around the three pillars of numerical computing performance — vectorization, caching, and parallelization.

The guiding constraint is that performance optimizations must not compromise correctness or reproducibility. Every optimization described here preserves the numerical output to within the Tier 2 guarantee (§7.1.4.2: $< 10^{-10}$ difference from the unoptimized implementation on the same platform). Optimizations that would change the output (e.g., reduced-precision arithmetic, approximate constitutive evaluation) are not permitted.

---

#### 9.4.1 Vectorization

Vectorization is the replacement of scalar loops (one element at a time) with array operations (all elements in a single instruction or a single library call). It is the single most important optimization for the ED engine because the time-stepping loop is dominated by element-wise operations on the density array — constitutive evaluation, stencil application, operator assembly — each of which touches every grid point.

##### 9.4.1.1 The Vectorization Principle

Every operation that processes the density array $\boldsymbol{\rho}$ must be expressed as an array-level operation:

| Scalar form (slow) | Vectorized form (fast) | Speedup |
|--------------------|----------------------|---------|
| `for j: Lap[j] = (rho[j-1] - 2*rho[j] + rho[j+1])/h2` | `Lap[1:-1] = (rho[:-2] - 2*rho[1:-1] + rho[2:])/h2` | $50\times$–$200\times$ (Python) |
| `for j: M[j] = M0*(rho_max - rho[j])^beta` | `M = M0*(rho_max - rho).^beta` | $100\times$–$500\times$ (Python) |
| `for j: F[j] = M[j]*Lap[j] + Mp[j]*G2[j] - P[j]` | `F = M.*Lap + Mp.*G2 - P` | $50\times$–$200\times$ (Python) |
| `sum = 0; for j: sum += f[j]` | `sum(f)` | $20\times$–$50\times$ (Python) |

The speedup factors are Python-specific (the scalar loop incurs Python interpreter overhead per element). In Julia, the speedup from vectorization is $1\times$–$2\times$ (compiled loops are already fast); in MATLAB, it is $10\times$–$50\times$ (MATLAB's JIT is faster than Python's interpreter but slower than Julia's compiler).

The vectorization applies to:

- **Constitutive evaluation** (§2.3.2.1, Step 4a): all $N_{\mathrm{grid}}$ values of $M(\rho_j)$, $M'(\rho_j)$, $P(\rho_j)$ in a single array expression.
- **Stencil computation** (Step 4b): the Laplacian and gradient-squared via sliced array operations.
- **Operator assembly** (Step 4c): the pointwise combination $F = M\cdot\mathrm{Lap} + M'\cdot\mathrm{Grad2} - P$.
- **RHS assembly** (Step 4e): the explicit right-hand side for the implicit system.
- **Observable extraction** (§5): all spatial integrals ($\mathcal{E}$, $C_{\mathrm{ED}}$, $\|u\|_{L^2}^2$, dissipation channels) via `sum` of vectorized expressions.

##### 9.4.1.2 Fused Operations

When multiple element-wise operations are applied sequentially, the intermediate arrays can be eliminated by fusing the operations into a single pass:

| Unfused (3 passes over memory) | Fused (1 pass) |
|-------------------------------|----------------|
| `temp1 = M .* Lap;` | Julia: `@. F = M * Lap + Mp * G2 - P` |
| `temp2 = Mp .* G2;` | Python: `numpy.add(numpy.multiply(M, Lap, out=F), numpy.multiply(Mp, G2, out=temp), out=F); numpy.subtract(F, P, out=F)` |
| `F = temp1 + temp2 - P;` | MATLAB: `F = M.*Lap + Mp.*G2 - P;` (MATLAB fuses internally for simple expressions) |

Fusion reduces the number of memory passes from 3 (one per intermediate array) to 1 (one combined pass). For $N = 512$ ($\sim 4$ KB of data per array): the arrays fit in L1 cache ($\sim 32$ KB), so the memory-bandwidth saving is modest. For $N = 5120$ ($\sim 40$ KB per array) or 2D at $N = 64$ ($\sim 34$ KB per array): the arrays spill to L2 cache, and fusion provides a $\sim 2\times$ speedup.

Julia's `@.` macro provides automatic fusion. Python requires manual use of the `out` parameter or the `numexpr` library. MATLAB fuses simple element-wise expressions internally but not complex ones.

---

#### 9.4.2 Caching

Caching exploits the reuse of computed values across time steps or across operations within a single time step. The ED engine has three levels of caching opportunity.

##### 9.4.2.1 Precomputation (Cross-Step Caching)

Quantities that are constant across all time steps are computed once at initialization and stored (§2.1.5):

| Quantity | Computed at initialization | Reused at every step |
|----------|--------------------------|---------------------|
| $h^2$, $2h$, $\Delta t\,D/h^2$ | Scalar arithmetic | Stencil and RHS assembly |
| $e^{-\zeta\Delta t/\tau}$, $(1 - e^{-\zeta\Delta t/\tau})/\zeta$ | `exp`, division | Participation update |
| ETD weight functions $\phi_{31}(c_k\Delta t)$, etc. | $O(N)$ evaluations | Every ETD substep |
| Neumann eigenvalues $\mu_k$ | $O(N)$ evaluations | Spectral operations |
| FFTW plan | $O(N\log N)$ planning | Every DCT call |

The precomputation saves $\sim 10$–$50$ operations per step (the transcendental functions `exp`, `log`, `cos` that would otherwise be called every step). For the ETD scheme, the savings are more substantial: the weight functions involve complex expressions with `exp` and polynomial divisions (§1.4.2.2) that cost $\sim 5\,\mu$s per mode if evaluated every substep but $0$ per substep when precomputed.

**Recomputation trigger.** If the time step changes (§1.6.2, adaptive reduction), the $\Delta t$-dependent precomputed quantities must be recomputed. The engine tracks whether $\Delta t$ has changed since the last precomputation and recomputes only when necessary. The recomputation cost is $O(N)$ — one pass over the spectral arrays — and occurs only during near-horizon excursions (a few steps per integration, if any).

##### 9.4.2.2 Within-Step Reuse

Some arrays computed during the density update are also needed for the observable extraction, and can be reused without recomputation:

| Array | Computed during update | Reused for observables |
|-------|----------------------|----------------------|
| $M(\rho_j)$ | Constitutive evaluation (Step 4a) | $C_{\mathrm{ED}}^{\mathrm{eff}}$ (§5.5.1.3); $M_{\min}$ (§5.7.1.2) |
| $|\nabla_h\rho|^2$ | Gradient-squared (Step 4b) | $C_{\mathrm{ED}}$ (§5.5); $G_\eta$ (§5.7.2.3) |
| $P(\rho_j)$ | Constitutive evaluation (Step 4a) | $\mathcal{D}_{\mathrm{pen}}$ (§5.2) |
| $F_h[\rho]$ | Operator assembly (Step 4c) | $\bar{F}$ for participation update (Step 4d) |

The reuse is implemented by storing these arrays in workspace buffers (§1.2.6) that persist from the update phase to the observable-extraction phase within the same time step. No recomputation is needed.

At output steps (when full observables are extracted): the constitutive values, gradient-squared, and operator values are all available from the immediately preceding update. The observable extraction adds only the energy quadrature ($\Phi(\rho_j)$ evaluation and summation) and the spectral decomposition (DCT, for spectral experiments) — no stencil or constitutive recomputation.

##### 9.4.2.3 Cache-Friendly Memory Access

The CPU's cache hierarchy ($\sim 32$ KB L1, $\sim 256$ KB L2, $\sim 8$ MB L3) determines how fast the processor can access array data. The stencil computation accesses three consecutive elements ($\rho_{j-1}$, $\rho_j$, $\rho_{j+1}$) per iteration; if these elements are in L1 cache, the access takes $\sim 1$ ns; if they are in main memory, the access takes $\sim 50$ ns.

For the 1D engine at $N = 512$: the density array is $\sim 4$ KB, which fits entirely in L1. The stencil computation is cache-optimal regardless of access pattern.

For the 2D engine at $N = 64$ per direction: the density array is $\sim 34$ KB, which spills from L1 but fits in L2. The stencil's $j$-adjacent accesses (stride $N_x = 66$ elements $= 528$ bytes) are not cache-optimal — they skip $\sim 500$ bytes between accesses, potentially causing L1 misses. The mitigation is to iterate over the fast axis (first index in Julia/MATLAB, last index in Python) in the innermost loop, ensuring that the stride-one accesses (which are the majority) are cache-optimal.

For the 3D engine or $N > 256$ per direction in 2D: the array exceeds L2 and cache optimization becomes important. The recommended approach is **tiling**: processing the array in blocks that fit in L2 ($\sim 256$ KB $\approx 32{,}000$ elements), so that each block is loaded once and fully processed before moving to the next. Tiling is relevant only for the extended experiments (Atlas §12.4) and is not needed for the current Atlas.

---

#### 9.4.3 Parallelization

The parallelization strategy (§4.5) distributes independent tasks across multiple cores. This section summarizes the cross-environment principles.

##### 9.4.3.1 Task-Level Parallelism (the Only Level Used)

The ED engine uses parallelism exclusively at the task level: each integration is a self-contained, single-threaded computation, and multiple integrations run simultaneously on different cores. No parallelism is used within a single integration (no multi-threaded stencil evaluation, no parallel tridiagonal solve, no concurrent DCT).

This single-level strategy is optimal for the Atlas workload because:

- **The tasks are small.** Each integration takes $2$–$60$ seconds. The overhead of spawning and synchronizing threads within a task ($\sim 10$–$100\,\mu$s per thread operation) would consume a significant fraction of the task's wall time at these durations.
- **The arrays are small.** At $N = 512$ in 1D, the density array is $4$ KB — too small to benefit from multi-threaded array operations (the thread-creation overhead exceeds the computation time). Multi-threaded BLAS is beneficial only for arrays $> 1$ MB.
- **The tasks are plentiful.** With $\sim 1{,}800$ tasks, there is more than enough parallelism to saturate any reasonable number of cores ($\leq 64$) without needing intra-task parallelism.

##### 9.4.3.2 Threading Configuration

To prevent the numerical libraries from spawning their own threads (which would compete with the task-level parallelism for CPU resources), the engine configures single-threaded execution:

| Environment | Configuration |
|-------------|--------------|
| Python | `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1` (environment variables, set before import) |
| Julia | `BLAS.set_num_threads(1)`, `FFTW.set_num_threads(1)` |
| MATLAB | `maxNumCompThreads(1)` (deprecated but functional), or `feature('numThreads', 1)` |

These settings ensure that each worker process uses exactly one CPU core, maximizing the efficiency of the task-level distribution.

##### 9.4.3.3 I/O Parallelism

When multiple workers write output simultaneously, the storage system may become a bottleneck if all workers write to the same physical disk. Mitigations:

- **Unique output directories.** Each task writes to its own sub-directory (§2.4.5.1). No two workers write to the same file.
- **Buffered writes.** Output is buffered in memory (the time-series rows accumulate in a list) and flushed periodically (every $\sim 100$ rows or at every checkpoint). This reduces the number of disk writes from $\sim 1{,}000$ per task (one per output step) to $\sim 10$ per task (one per flush).
- **SSD storage.** Solid-state drives handle parallel random writes much better than spinning disks ($> 100{,}000$ IOPS for SSD vs. $\sim 200$ IOPS for HDD). On an SSD, $16$ workers writing simultaneously produce no measurable I/O contention.

##### 9.4.3.4 Scaling Beyond One Node

For cluster execution (§4.5.3): each node runs a batch of tasks, and the tasks are distributed across nodes by the job scheduler. No inter-node communication is needed (embarrassingly parallel). The only shared resource is the filesystem (where the output is written). On a shared filesystem (NFS, Lustre, GPFS): the I/O mitigations above (unique directories, buffered writes) apply. On a local-disk filesystem: each node writes to its local storage, and the output is collected post-hoc.

---

#### 9.4.4 Profiling and Bottleneck Identification

Before applying performance optimizations, the engine should be profiled to identify the actual bottleneck. The expected bottleneck depends on the method and the resolution:

| Method | Resolution | Expected bottleneck | Fraction of step time |
|--------|-----------|--------------------|-----------------------|
| A (FD), 1D, $N = 512$ | Low | Tridiagonal solve | $\sim 30\%$ |
| A (FD), 1D, $N = 512$ | — | Constitutive evaluation | $\sim 25\%$ |
| A (FD), 2D, $N = 64$ | Medium | Sparse matrix solve | $\sim 50\%$ |
| B (Spectral), 1D, $N = 128$ | Low | DCT (4 per step) | $\sim 60\%$ |
| Any method, at output steps | — | Energy quadrature ($\Phi(\rho)$) | $\sim 40\%$ of output-step time |

**Profiling tools.**

| Environment | Tool |
|-------------|------|
| Python | `cProfile` (function-level), `line_profiler` (line-level) |
| Julia | `@time`, `@btime` (BenchmarkTools.jl), `Profile.@profile` |
| MATLAB | `profile on/off/viewer` (built-in profiler) |

The profiling should be run on a representative experiment (e.g., Experiment 3.1 at the default resolution) and the results should identify which function consumes the most wall time. Optimizations should target only the identified bottleneck — optimizing a function that consumes $5\%$ of the step time can improve the total by at most $5\%$, regardless of how much faster the function becomes.

---

#### 9.4.5 Performance Budget

The target per-step performance for each method and environment:

| Method | $N$ | Python target | Julia target | MATLAB target |
|--------|-----|--------------|-------------|---------------|
| A (FD), 1D | $512$ | $\leq 10\,\mu$s | $\leq 2\,\mu$s | $\leq 12\,\mu$s |
| A (FD), 2D | $64^2$ | $\leq 200\,\mu$s | $\leq 40\,\mu$s | $\leq 250\,\mu$s |
| B (Spectral), 1D | $128$ | $\leq 20\,\mu$s | $\leq 5\,\mu$s | $\leq 25\,\mu$s |

An implementation that exceeds these targets by more than $2\times$ should be profiled and optimized. An implementation that meets these targets is "fast enough" — further optimization would not meaningfully reduce the Atlas completion time (which is dominated by the number of tasks, not the per-step speed).

The full Atlas at the target performance:

| Environment | Per-step | Steps (total) | Integration time | Overhead | Total |
|-------------|----------|--------------|-----------------|----------|-------|
| Python | $10\,\mu$s | $\sim 9 \times 10^7$ | $\sim 900$ s | $\sim 200$ s | $\sim 18$ min (16 cores) |
| Julia | $2\,\mu$s | $\sim 9 \times 10^7$ | $\sim 180$ s | $\sim 100$ s | $\sim 5$ min (16 cores) |
| MATLAB | $12\,\mu$s | $\sim 9 \times 10^7$ | $\sim 1080$ s | $\sim 200$ s | $\sim 21$ min (16 cores) |

All three environments complete the full Atlas in under $30$ minutes on a $16$-core workstation — well within the computational budget.

---

#### 9.4.6 Summary

| Principle | Strategy | Where applied | Impact |
|-----------|---------|---------------|--------|
| **Vectorization** | Array operations instead of scalar loops | Constitutive eval, stencils, operator assembly, observables | $50\times$–$500\times$ in Python; $2\times$ in Julia; $10\times$–$50\times$ in MATLAB |
| **Fusion** | Combine multiple passes into one | Operator assembly (`@.` in Julia, `out=` in NumPy) | $\sim 2\times$ at large $N$ or 2D |
| **Precomputation** | Compute constants once at init | $h^2$, exponential factors, ETD weights, FFTW plans | Saves $\sim 50$ transcendental evals/step |
| **Within-step reuse** | Share workspace arrays across phases | Constitutive buffers, gradient-squared, operator values | Eliminates redundant evaluation at output steps |
| **Cache-friendly access** | Stride-one innermost loop | 2D stencils (fast axis innermost) | $\sim 2\times$ at large $N$ in 2D |
| **Task-level parallelism** | One task per core, no intra-task threading | Sweep orchestration | Linear speedup to $\sim 64$ cores |
| **Single-threaded libraries** | Disable BLAS/FFTW threading | Environment variables at startup | Prevents thread contention in task-parallel execution |
| **Buffered I/O** | Batch output writes | Time-series flushing | Reduces disk operations by $\sim 100\times$ |

The performance optimization hierarchy is: vectorization first (the largest single factor), then caching (eliminating redundant computation), then parallelization (distributing the workload). Each level builds on the previous — there is no benefit to parallelizing a non-vectorized implementation (it would run slowly on every core), and no benefit to caching values that are not reused (they would be computed once either way). The hierarchy is the same in every environment; only the specific syntax differs.

---

### 9.5 Memory Considerations

The ED simulation engine has a modest memory footprint — the standard 1D experiments at $N = 512$ require $\sim 50$ KB of working memory, and the largest 2D experiments at $N = 64$ per direction require $\sim 500$ KB (§1.2.9). Even with $16$ parallel workers, each carrying $\sim 100$ MB of environment overhead (the Python interpreter, NumPy, SciPy), the total memory usage is $\sim 2$ GB — a small fraction of a modern workstation's $16$–$128$ GB RAM. Memory is not a constraint for the current Atlas.

This section addresses memory considerations for three scenarios: the standard Atlas (§9.5.1), the extended Atlas with large domains (§9.5.2), and the output accumulation during long sweeps (§9.5.3).

---

#### 9.5.1 Memory Footprint of the Standard Engine

The engine's memory is partitioned into four categories: the state arrays, the workspace arrays, the precomputed constants, and the output buffers.

##### 9.5.1.1 Detailed Footprint by Method

**Method A (Finite Difference, 1D, $N = 512$, $N_{\mathrm{grid}} = 514$):**

| Category | Arrays | Elements | Bytes |
|----------|--------|----------|-------|
| State | $\boldsymbol{\rho}$, $\boldsymbol{\rho}_{\mathrm{prev}}$, $v$, $v_{\mathrm{prev}}$ | $2 \times 514 + 2$ | $8{,}240$ |
| Workspace | Lap, Grad2, F, RHS, $M$, $M'$, $P$, $P'$ | $8 \times 514$ | $32{,}896$ |
| Implicit matrix | lower, diag, upper | $3 \times 514$ | $12{,}336$ |
| Precomputed | $h^2$, $e_v$, $f_v$, params (~20 scalars) | $20$ | $160$ |
| Output buffer | Current observables (24 fields) | $24$ | $192$ |
| **Subtotal (engine)** | | | **$53{,}824$ ($\sim 53$ KB)** |

**Method B (Spectral, 1D, $N_{\mathrm{modes}} = 128$, $N_{\mathrm{phys}} = 192$):**

| Category | Arrays | Elements | Bytes |
|----------|--------|----------|-------|
| State | $\hat{\mathbf{u}}$, $\hat{\mathbf{u}}_{\mathrm{prev}}$, $v$, $v_{\mathrm{prev}}$ | $2 \times 128 + 2$ | $2{,}064$ |
| Spectral arrays | $\mu$, $\alpha$, $c$, $E$, $E_2$, $\varphi_1$, $\varphi_{1h}$, $\phi_{31}$, $\phi_{32}$, $\phi_{33}$ | $10 \times 128$ | $10{,}240$ |
| Pseudospectral | 6 physical-space buffers | $6 \times 192$ | $9{,}216$ |
| ETD stages | $\hat{\mathbf{a}}$, $\hat{\mathbf{b}}$, $\hat{\mathbf{c}}$, $\hat{\mathbf{d}}$ | $4 \times 128$ | $4{,}096$ |
| FFTW plan | Internal plan data | $\sim 2{,}000$ | $\sim 2{,}000$ |
| **Subtotal (engine)** | | | **$\sim 28$ KB** |

**Method A (Finite Difference, 2D, $N = 64$ per direction, $N_{\mathrm{grid}} = 66^2 = 4{,}356$):**

| Category | Arrays | Elements | Bytes |
|----------|--------|----------|-------|
| State | $\boldsymbol{\rho}$, $\boldsymbol{\rho}_{\mathrm{prev}}$ | $2 \times 4{,}356$ | $69{,}696$ |
| Workspace | 8 arrays | $8 \times 4{,}356$ | $278{,}784$ |
| Sparse matrix | $\sim 5$ diagonals of the banded system | $\sim 5 \times 4{,}356$ | $174{,}240$ |
| **Subtotal (engine)** | | | **$\sim 510$ KB** |

##### 9.5.1.2 Environment Overhead

The engine memory is dwarfed by the language runtime:

| Environment | Runtime overhead | Typical total per worker |
|-------------|-----------------|------------------------|
| Python (NumPy, SciPy loaded) | $\sim 80$–$120$ MB | $\sim 100$ MB |
| Julia (base + packages loaded) | $\sim 150$–$250$ MB | $\sim 200$ MB |
| MATLAB (base, no toolboxes) | $\sim 500$–$800$ MB | $\sim 600$ MB |

The environment overhead is fixed (it does not grow with $N$) and is paid once per worker process. For $16$ parallel workers: $\sim 1.6$ GB (Python), $\sim 3.2$ GB (Julia), $\sim 10$ GB (MATLAB). All fit comfortably in $16$–$32$ GB RAM.

##### 9.5.1.3 The 500 MB Budget

The Suite specifies a $500$ MB maximum working-memory requirement per worker (§0.5). The standard engine uses $< 1$ MB of working memory (engine arrays only, excluding environment overhead), so the budget is satisfied with a margin of $> 500\times$ for 1D and $> 1000\times$ for the engine-only footprint. The environment overhead is not counted toward the $500$ MB budget (it is a fixed per-process cost, not a per-problem cost).

---

#### 9.5.2 Array Reuse

The engine's memory efficiency relies on the pre-allocation and reuse strategy of §2.1.5: all workspace arrays are allocated once at initialization and overwritten at every time step. This subsection specifies the reuse discipline in detail.

##### 9.5.2.1 The No-Allocation Rule

Inside the time-stepping loop (§2.3), no new arrays are allocated. Every array that appears in the loop body is a pre-allocated workspace. The rule applies to:

- **Intermediate results.** The Laplacian, gradient-squared, constitutive values, and operator values are computed into pre-allocated buffers (`Lap`, `Grad2`, `M_vals`, `F_vals`), not into newly created arrays.
- **Solver inputs and outputs.** The RHS vector and the solution vector are pre-allocated; the solver writes into the pre-allocated output array (in-place solve).
- **Observable extraction.** The observables are computed into scalar variables or into pre-allocated summary arrays, not into new containers.

The no-allocation rule is enforced by:

- **Python:** Using the `out` parameter of NumPy operations (§9.1.3.4) or the `[:]` slice assignment (e.g., `Lap[:] = ...` assigns into the existing array; `Lap = ...` would create a new array and reassign the name).
- **Julia:** Using `.=` broadcast assignment (§9.2.3.1) and `!`-suffixed in-place functions.
- **MATLAB:** Assigning into pre-existing variables (MATLAB's copy-on-write semantics ensure that `Lap(2:end-1) = ...` modifies in place when no other reference to `Lap` exists).

##### 9.5.2.2 Lifetime of Workspace Arrays

Each workspace array has a specific lifetime within the time-step:

| Array | Written by | Read by | Lifetime |
|-------|-----------|---------|----------|
| `M_vals` | Constitutive eval (Step 4a) | Operator assembly (Step 4c), implicit matrix (Step 4f), observables | Steps 4a through output |
| `Lap` | Stencil (Step 4b) | Operator assembly (Step 4c) | Steps 4b–4c only |
| `Grad2` | Stencil (Step 4b) | Operator (Step 4c), $C_{\mathrm{ED}}$ (output) | Steps 4b through output |
| `F_vals` | Operator (Step 4c) | Spatial average (Step 4d) | Steps 4c–4d only |
| `RHS` | RHS assembly (Step 4e) | Implicit solve (Step 4f) | Steps 4e–4f only |

Arrays with non-overlapping lifetimes *could* share the same memory (aliasing). For example, `F_vals` and `RHS` are never live simultaneously — `F_vals` is consumed in Step 4d, and `RHS` is produced in Step 4e. They could use the same underlying buffer.

**Recommendation.** The Suite does *not* require aliasing (it complicates debugging and provides negligible memory savings at the $\sim 50$ KB level). Each workspace array is a separate allocation. Aliasing is permitted for large-domain extensions (§9.5.3) where the memory savings are material.

##### 9.5.2.3 Output Buffer Management

The time-series output (§2.4.1) accumulates $N_{\mathrm{output}}$ rows of $24$ scalar fields. At the default output interval ($k_{\mathrm{out}} = 100$) and $T = 50$: $N_{\mathrm{output}} \approx 1{,}000$ rows, consuming $1{,}000 \times 24 \times 8 = 192$ KB.

The spectral output (§2.4.2) accumulates $N_{\mathrm{output}}$ rows of $N_{\mathrm{obs}}$ modal amplitudes (plus derived arrays). At $N_{\mathrm{obs}} = 32$: $1{,}000 \times (4 \times 32 + 7) \times 8 \approx 1.1$ MB.

These accumulation buffers grow linearly with $N_{\mathrm{output}}$. For the standard Atlas experiments ($N_{\mathrm{output}} \leq 1{,}200$): the buffers are small ($< 2$ MB total). For every-step sampling ($N_{\mathrm{output}} \sim 10^5$): the buffers grow to $\sim 200$ MB (time series) or $\sim 110$ MB (spectral) — still within the $500$ MB budget but approaching the limit.

**Incremental writing.** To avoid accumulating the entire time series in memory, the engine flushes the output buffers to disk periodically (§2.4.1.2). The buffer holds the most recent batch of rows ($\sim 100$ rows between flushes), not the entire history. After flushing, the buffer's memory is reused for the next batch.

For the NPZ format (which writes in a single call): the entire time series must be accumulated in memory before writing. The engine preallocates the output arrays at their full size ($N_{\mathrm{output}} \times 24$ for the time series) during initialization, based on $N_{\mathrm{output}} = \lceil T/(\Delta t \cdot k_{\mathrm{out}})\rceil$. This preallocation is included in the initialization memory budget.

---

#### 9.5.3 Large-Domain Strategies

The current Atlas uses 1D domains up to $N = 5{,}120$ (the $L = 10$ domain-size sweep, §4.4) and 2D domains at $N = 64$ per direction. Future extensions (Atlas §12.4) may require:

- 2D domains at $N = 256$ per direction ($N_{\mathrm{grid}} \approx 66{,}000$; arrays $\sim 500$ KB each; workspace $\sim 4$ MB).
- 3D domains at $N = 32$ per direction ($N_{\mathrm{grid}} \approx 36{,}000$; arrays $\sim 280$ KB; workspace $\sim 2.5$ MB; but the sparse matrix is large: bandwidth $\sim 34^2 = 1{,}156$, storage $\sim 40$ MB).
- Long-time 1D integrations at $N = 512$ with every-step output ($N_{\mathrm{output}} \sim 10^6$; output buffer $\sim 200$ MB).

These scenarios remain within the $500$ MB engine budget but approach it. The following strategies extend the memory efficiency.

##### 9.5.3.1 Sparse Matrix Storage for 2D and 3D

The implicit matrix for 2D ($N = 256$) has $\sim 66{,}000$ rows with $5$ nonzeros per row (the five-point stencil): $\sim 330{,}000$ nonzeros, stored in CSC (compressed sparse column) format as three arrays (row indices, column pointers, values) totaling $\sim 330{,}000 \times 12 \approx 4$ MB. This is manageable.

For 3D ($N = 32$): the seven-point stencil has $\sim 36{,}000$ rows with $7$ nonzeros per row: $\sim 250{,}000$ nonzeros, $\sim 3$ MB in CSC. However, the sparse factorization (LU or Cholesky) produces fill-in that can expand the storage to $\sim 10$–$50$ MB depending on the ordering. Using an iterative solver (conjugate gradient with incomplete Cholesky preconditioning) avoids the factorization fill-in entirely — the preconditioner is $\sim 3$ MB and the solver workspace is $\sim 5$ vectors ($\sim 1.5$ MB). Total: $\sim 5$ MB.

**Recommendation for 3D.** Use iterative CG with IC(0) preconditioning for the 3D implicit system. The convergence is fast ($\sim 5$–$10$ iterations per step, because the implicit matrix is well-conditioned — §1.6.5, $\kappa \sim 80$), and the memory is linear in $N_{\mathrm{grid}}$.

##### 9.5.3.2 Out-of-Core Output for Long Integrations

For integrations producing $> 10^6$ output steps (e.g., every-step sampling over $T = 50$ at $\Delta t = 5 \times 10^{-4}$), the output buffer exceeds $200$ MB if accumulated in memory. The incremental-writing strategy (§9.5.2.3) avoids this by flushing to disk every $\sim 100$–$1{,}000$ rows, keeping the in-memory buffer at $\sim 1$ MB regardless of the total output size.

For the NPZ format (single-write): the engine can fall back to the HDF5 format with incremental writes (`h5py` resizable datasets in Python, `HDF5.jl` in Julia, HDF5-based `.mat` in MATLAB). This eliminates the need to accumulate the full output in memory.

##### 9.5.3.3 Array Aliasing for Memory-Critical Applications

When the workspace memory exceeds $\sim 50$ MB (2D at $N > 128$ or 3D at $N > 32$), the engine may alias workspace arrays that have non-overlapping lifetimes (§9.5.2.2):

| Alias group | Arrays | Condition |
|-------------|--------|-----------|
| Group 1 | `F_vals` and `RHS` | `F_vals` consumed before `RHS` produced |
| Group 2 | `Lap` and `RHS` | `Lap` consumed in Step 4c; `RHS` produced in Step 4e |
| Group 3 | `P_vals` and output temp | `P_vals` consumed by operator; output computed after the update |

Each alias group shares a single memory buffer, reducing the workspace from $8 \times N_{\mathrm{grid}}$ arrays to $\sim 5 \times N_{\mathrm{grid}}$ arrays (a $37.5\%$ reduction). At $N_{\mathrm{grid}} = 66{,}000$ (2D, $N = 256$): the saving is $\sim 3 \times 66{,}000 \times 8 = 1.6$ MB — modest in absolute terms but meaningful when the total workspace is $\sim 4$ MB.

**Caution.** Aliasing must be documented and tested: a change to the step ordering (e.g., moving the observable extraction to before the RHS assembly) would invalidate the lifetime analysis and produce silent data corruption. The aliased arrays must be annotated with their alias group in the source code, and any modification to the step ordering must re-verify the lifetime analysis.

##### 9.5.3.4 Memory Scaling Summary

| Configuration | Engine memory | Environment + engine | Fits in 500 MB? |
|--------------|--------------|---------------------|-----------------|
| 1D, $N = 512$ | $53$ KB | $\sim 100$ MB | ✓ (by $5000\times$) |
| 1D, $N = 5{,}120$ | $530$ KB | $\sim 101$ MB | ✓ (by $500\times$) |
| 2D, $N = 64$ | $510$ KB | $\sim 101$ MB | ✓ (by $500\times$) |
| 2D, $N = 256$ | $4$ MB | $\sim 104$ MB | ✓ (by $5\times$) |
| 3D, $N = 32$ (iterative) | $5$ MB | $\sim 105$ MB | ✓ (by $5\times$) |
| 3D, $N = 64$ (iterative) | $\sim 40$ MB | $\sim 140$ MB | ✓ (by $3.5\times$) |
| 3D, $N = 128$ (iterative) | $\sim 300$ MB | $\sim 400$ MB | ✓ (marginal) |
| 3D, $N = 256$ (iterative) | $\sim 2.4$ GB | $\sim 2.5$ GB | ✗ (exceeds budget) |

The $500$ MB budget is sufficient for all current Atlas experiments and for the planned extensions up to 3D at $N = 128$. Beyond $N = 128$ in 3D, the memory budget must be revisited (either by increasing the per-worker allocation or by implementing domain decomposition, which is outside the scope of the current Suite).

---

#### 9.5.4 Summary

| Aspect | Specification |
|--------|--------------|
| **Standard 1D footprint** | $\sim 53$ KB engine; $\sim 100$ MB total per worker |
| **Standard 2D footprint** | $\sim 510$ KB engine; $\sim 101$ MB total per worker |
| **Memory budget** | $500$ MB per worker (engine only, excluding runtime overhead) |
| **No-allocation rule** | No `new` or `malloc` inside the time-stepping loop |
| **Array reuse** | Pre-allocated workspace; overwritten every step |
| **Output buffering** | Incremental flush to disk; in-memory buffer $\sim 1$ MB |
| **Sparse matrices (2D/3D)** | CSC format; iterative CG+IC(0) for 3D |
| **Array aliasing** | Permitted for memory-critical applications; non-overlapping lifetimes documented |
| **Scaling limit** | 3D at $N = 128$ ($\sim 300$ MB engine) is the upper limit of the current budget |

Memory is the least constraining resource for the ED simulation engine. The standard Atlas fits $5{,}000\times$ within the budget; the planned extensions fit with a comfortable margin; and the pathological case (3D at $N = 256$) is the only scenario that exceeds the budget — and it is far beyond the current Atlas scope. The primary memory discipline is not conservation but *predictability*: the no-allocation rule ensures that the memory usage is constant throughout the integration (no garbage-collection pauses, no heap fragmentation, no out-of-memory surprises during long runs), which is more valuable for reliability than the absolute footprint is for capacity.

---

## 10. Future Extensions

### 10.1 GPU Acceleration

The current Suite specifies CPU-only execution: single-threaded integrations distributed across CPU cores by the task-level parallelism of §4.5. This section assesses the suitability of GPU acceleration for the ED simulation engine, identifies the scenarios where GPUs provide meaningful speedup, estimates the expected performance gains, and describes the libraries that would enable a GPU implementation. GPU acceleration is not part of the current Suite specification — it is a planned extension for future versions that target large-domain or high-throughput applications.

---

#### 10.1.1 GPU Suitability Assessment

GPU acceleration is effective when a computation has two properties: **massive parallelism** (thousands of independent operations that can execute simultaneously) and **regular memory access** (stride-one or broadcast patterns that exploit the GPU's wide memory bus). The ED engine's operations are assessed against these criteria.

##### 10.1.1.1 Operations That Are GPU-Suitable

| Operation | Parallelism | Memory pattern | GPU suitability |
|-----------|------------|----------------|----------------|
| Constitutive evaluation | $N_{\mathrm{grid}}$ independent pointwise evaluations | Stride-one read and write | **Excellent.** Each grid point is independent; the operation maps directly to one GPU thread per point. |
| Stencil evaluation (Laplacian, gradient-squared) | $N_{\mathrm{grid}}$ stencil applications, each accessing $3$–$7$ neighbors | Stride-one with short-range neighbor access | **Good.** Standard GPU stencil pattern; high arithmetic intensity for the five-point and seven-point stencils. |
| Operator assembly ($F = M\cdot\mathrm{Lap} + M'\cdot\mathrm{Grad2} - P$) | $N_{\mathrm{grid}}$ independent fused multiply-adds | Stride-one | **Excellent.** Fused element-wise operations are the GPU's strongest pattern. |
| Spatial reductions ($\sum_j f_j$ for energy, $C_{\mathrm{ED}}$, etc.) | Parallel reduction tree | Global read, hierarchical combine | **Good.** Well-optimized GPU reduction kernels are standard. |
| DCT (Method B) | FFT-based ($O(N\log N)$) | Butterfly access pattern | **Good.** cuFFT (NVIDIA) provides highly optimized FFT/DCT. |

##### 10.1.1.2 Operations That Are GPU-Unsuitable

| Operation | Parallelism | Memory pattern | GPU suitability |
|-----------|------------|----------------|----------------|
| Tridiagonal solve | Sequential (Thomas algorithm is inherently serial) | Stride-one but with data dependency $j \to j+1$ | **Poor.** The Thomas algorithm cannot be parallelized in its standard form. Parallel tridiagonal solvers (cyclic reduction, PCR) exist but have higher constant factors. |
| Participation ODE ($v$ update) | Single scalar operation | N/A (one value) | **Poor.** One operation cannot utilize the GPU; the $v$ update should remain on the CPU. |
| Adaptive time-step control | Sequential logic (compare $\delta$ to thresholds, adjust $\Delta t$) | N/A | **Poor.** Control flow, not computation. CPU only. |
| Diagnostic checks (positivity, finiteness) | Parallel scan/reduction | Global read | **Acceptable.** Can be fused with the constitutive evaluation kernel. |
| Output I/O | Sequential file writes | N/A | **Poor.** I/O is CPU-bound. |

##### 10.1.1.3 The Bottleneck Analysis

For Method A at $N = 512$ (1D): the tridiagonal solve takes $\sim 30\%$ of the step time (§9.4.4). Since the solve is GPU-unsuitable, the maximum theoretical speedup from GPU acceleration of the remaining $70\%$ is $1/(0.30 + 0.70/S_{\mathrm{GPU}})$, where $S_{\mathrm{GPU}}$ is the GPU speedup on the GPU-suitable operations. Even at $S_{\mathrm{GPU}} = 100\times$: the overall speedup is $1/(0.30 + 0.007) \approx 3.3\times$ — limited by the serial solve (Amdahl's law).

For Method A at $N = 5{,}120$ (1D) or $N = 256$ per direction (2D): the tridiagonal/banded solve still dominates, but the stencil and constitutive evaluations become more expensive (proportional to $N_{\mathrm{grid}}$). The solve fraction decreases to $\sim 15\%$–$20\%$, and the overall GPU speedup improves to $\sim 5\times$–$8\times$.

For Method B at $N = 128$ (1D): the DCT takes $\sim 60\%$ of the step time. The GPU-accelerated cuFFT can provide $\sim 10\times$–$50\times$ speedup on the DCT at $N = 192$ (the de-aliased grid), giving an overall speedup of $1/(0.40 + 0.60/S_{\mathrm{DCT}}) \approx 2\times$–$2.4\times$.

For Method B at $N = 1{,}024$ or higher: the DCT dominates ($\sim 80\%$ of the step), and cuFFT's advantage grows with $N$ ($\sim 50\times$–$100\times$ at $N = 4{,}096$). The overall speedup approaches $5\times$–$10\times$.

**Conclusion.** GPU acceleration provides a meaningful speedup ($> 3\times$) only for large problems: 1D at $N > 2{,}000$, 2D at $N > 64$ per direction, or spectral at $N > 512$ modes. For the standard Atlas experiments ($N = 512$ in 1D, $N = 128$ spectral): the GPU speedup is marginal ($< 3\times$), and the task-level CPU parallelism (§4.5) is more efficient (it scales linearly with cores and has zero serial bottleneck).

---

#### 10.1.2 Expected Speedups

The following estimates assume an NVIDIA GPU (A100 or equivalent, $\sim 10{,}000$ CUDA cores, $\sim 2$ TB/s memory bandwidth) and a modern CPU (Intel/AMD, $\sim 4$ GHz, $\sim 50$ GB/s memory bandwidth).

##### 10.1.2.1 Per-Operation Speedup

| Operation | CPU time ($N = 5{,}120$, 1D) | GPU time (estimated) | Speedup |
|-----------|------------------------------|---------------------|---------|
| Constitutive eval ($N$ pointwise) | $\sim 20\,\mu$s | $\sim 0.5\,\mu$s | $40\times$ |
| Laplacian stencil ($N$ points) | $\sim 10\,\mu$s | $\sim 0.3\,\mu$s | $30\times$ |
| Operator assembly (fused, $N$ points) | $\sim 15\,\mu$s | $\sim 0.3\,\mu$s | $50\times$ |
| Tridiagonal solve ($N$ points) | $\sim 15\,\mu$s | $\sim 10\,\mu$s (PCR) | $1.5\times$ |
| Spatial reduction (sum, $N$ values) | $\sim 2\,\mu$s | $\sim 0.5\,\mu$s | $4\times$ |
| DCT ($N = 7{,}680$ de-aliased) | $\sim 100\,\mu$s | $\sim 3\,\mu$s (cuFFT) | $30\times$ |

##### 10.1.2.2 Per-Step Speedup (Method A, 1D)

| $N$ | CPU step time | GPU step time (est.) | Speedup |
|-----|--------------|---------------------|---------|
| $512$ | $\sim 10\,\mu$s | $\sim 12\,\mu$s (kernel launch overhead dominates) | $< 1\times$ (GPU slower) |
| $2{,}048$ | $\sim 40\,\mu$s | $\sim 15\,\mu$s | $\sim 2.7\times$ |
| $5{,}120$ | $\sim 100\,\mu$s | $\sim 20\,\mu$s | $\sim 5\times$ |
| $10{,}240$ | $\sim 200\,\mu$s | $\sim 25\,\mu$s | $\sim 8\times$ |

The GPU is *slower* than the CPU at $N = 512$ because the kernel launch overhead ($\sim 5$–$10\,\mu$s per kernel) exceeds the computation time. At $N = 2{,}048$: the computation begins to amortize the launch overhead, and the GPU becomes beneficial. At $N = 10{,}240$: the GPU provides $8\times$ speedup.

##### 10.1.2.3 Per-Step Speedup (Method A, 2D)

| $N$ per direction | $N_{\mathrm{grid}}$ | CPU step time | GPU step time (est.) | Speedup |
|-------------------|---------------------|--------------|---------------------|---------|
| $64$ | $4{,}356$ | $\sim 200\,\mu$s | $\sim 50\,\mu$s | $\sim 4\times$ |
| $128$ | $16{,}900$ | $\sim 1$ ms | $\sim 80\,\mu$s | $\sim 12\times$ |
| $256$ | $66{,}564$ | $\sim 5$ ms | $\sim 200\,\mu$s | $\sim 25\times$ |

The 2D case benefits strongly from GPU acceleration because the grid size is large enough to utilize the GPU's parallelism, and the sparse banded solve (the CPU bottleneck) can be replaced by a GPU-accelerated iterative solver (CG with a GPU-parallel preconditioner).

##### 10.1.2.4 Sweep-Level Speedup

An alternative to per-step GPU acceleration is **batch GPU execution**: running many independent integrations simultaneously on a single GPU, each as a separate stream. This exploits the GPU's parallelism at the task level rather than the grid level.

At $N = 512$ (1D): each integration uses $\sim 50$ KB of GPU memory. A GPU with $40$ GB memory can hold $\sim 800{,}000$ simultaneous integrations — far more than the Atlas requires. The challenge is the kernel launch overhead: $800{,}000$ simultaneous kernels would saturate the GPU's scheduler. A practical batch size is $\sim 1{,}000$–$10{,}000$ integrations, each processed in lockstep (all integrations advance one step simultaneously).

The batch approach is effective for the parameter sweeps (§4.1): the $81$–$689$ sweep points can be batched into a single GPU pass, with each GPU thread block processing one sweep point. The expected speedup is $\sim 100\times$–$500\times$ compared to sequential CPU execution (all sweep points processed in the time of one).

---

#### 10.1.3 Libraries

The GPU acceleration would be implemented through environment-specific GPU libraries:

##### 10.1.3.1 Python

| Library | Purpose | Notes |
|---------|---------|-------|
| **CuPy** | Drop-in NumPy replacement for NVIDIA GPUs | Array operations (`cupy.ndarray`) with the same API as NumPy. Stencils, constitutive evaluations, and reductions transfer transparently. |
| **cuFFT** (via CuPy) | GPU-accelerated FFT/DCT | `cupy.fft.fft` calls cuFFT internally. DCT-I requires the same symmetric-extension trick as the CPU (§9.3.2.3). |
| **cuSPARSE** (via SciPy/CuPy) | GPU-accelerated sparse solvers | Tridiagonal and banded solves via `cusparse<t>gtsv2`. |
| **Numba CUDA** | Custom GPU kernels | For fused stencil-constitutive kernels that cannot be expressed as CuPy array operations. |

##### 10.1.3.2 Julia

| Library | Purpose | Notes |
|---------|---------|-------|
| **CUDA.jl** | Julia interface to NVIDIA GPUs | `CuArray` type with broadcast support. The existing Julia engine code (with `@.` broadcasts) transfers to GPU with minimal changes: replace `Array` with `CuArray`. |
| **cuFFT** (via CUDA.jl) | GPU FFT | `CUFFT.plan_fft` and related functions. |
| **CUSOLVER** (via CUDA.jl) | GPU sparse/dense solvers | Tridiagonal solve via `CUSOLVER.gtsv2`. |

##### 10.1.3.3 MATLAB

| Library | Purpose | Notes |
|---------|---------|-------|
| **Parallel Computing Toolbox** (GPU) | MATLAB GPU arrays | `gpuArray(rho)` transfers data to GPU; element-wise operations and reductions execute on GPU transparently. |
| **cuFFT** (via MATLAB) | GPU FFT | `fft(gpuArray(x))` calls cuFFT automatically. |

##### 10.1.3.4 Cross-Environment Considerations

- **Double precision.** The Suite requires IEEE 754 double precision (§0.5). All GPU libraries listed above support double precision, but the performance is typically $2\times$ lower than single precision on consumer GPUs (which have fewer FP64 units). Data-center GPUs (A100, H100) provide full-speed FP64.
- **Reproducibility.** GPU floating-point arithmetic may not be bitwise-reproducible across GPU generations (different architectures may use different FMA behavior, different reduction tree depths, etc.). The Suite's Tier 2 guarantee (§7.1.4.2: agreement to $< 10^{-10}$) is expected to hold; Tier 1 (bitwise) is not guaranteed across GPU architectures.
- **Validation.** A GPU implementation must pass all validation tests (§§8.1–8.5) at the same tolerances as the CPU implementation. The validation is performed on the GPU output (not by comparing GPU to CPU); the GPU is treated as an independent implementation, not as an accelerator for the CPU implementation.

---

#### 10.1.4 Recommendation

| Scenario | Recommendation | Rationale |
|----------|---------------|-----------|
| Standard Atlas (1D, $N = 512$) | **CPU only.** No GPU. | GPU is slower due to kernel launch overhead. Task-level CPU parallelism is optimal. |
| Large 1D ($N > 2{,}000$) | **GPU optional.** $3\times$–$8\times$ speedup. | Useful for the domain-size sweep at $L = 10$ ($N = 5{,}120$). |
| 2D at $N > 64$ | **GPU recommended.** $4\times$–$25\times$ speedup. | The 2D extensions (Atlas §12.4) benefit strongly. |
| 3D at $N > 32$ | **GPU strongly recommended.** $10\times$–$50\times$ estimated. | The 3D extensions are impractical on CPU at $N > 64$. |
| Batch sweeps ($> 100$ points) | **GPU recommended (batch mode).** $100\times$+ speedup. | All sweep points processed simultaneously. |
| Standard Atlas reproduction | **CPU required.** GPU optional for cross-check. | The Suite's validation and reproducibility are CPU-based. GPU results are supplementary. |

The GPU extension does not replace the CPU implementation — it supplements it for large-domain and high-throughput scenarios. The CPU implementation remains the reference for all validation tests, reproducibility guarantees, and cross-implementation comparisons. A GPU implementation that passes all validation tests at the stated tolerances is accepted as a valid fourth environment alongside Python, Julia, and MATLAB.

---

#### 10.1.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Current status** | CPU only; GPU is a planned extension |
| **GPU-suitable operations** | Constitutive eval, stencils, operator assembly, DCT, reductions ($30\times$–$50\times$ per-operation) |
| **GPU-unsuitable operations** | Tridiagonal solve ($1.5\times$), participation ODE, adaptive control, I/O |
| **Crossover point** | $N \gtrsim 2{,}000$ (1D) or $N \gtrsim 64$ per direction (2D) |
| **Standard Atlas speedup** | $< 1\times$ at $N = 512$ (GPU slower due to launch overhead) |
| **Large-domain speedup** | $5\times$–$25\times$ at $N = 5{,}120$ (1D) or $N = 256$ (2D) |
| **Batch sweep speedup** | $100\times$+ (all sweep points processed simultaneously) |
| **Libraries** | CuPy/Numba (Python), CUDA.jl (Julia), gpuArray (MATLAB) |
| **Precision** | FP64 required; data-center GPUs recommended |
| **Reproducibility** | Tier 2 expected ($< 10^{-10}$); Tier 1 not guaranteed across architectures |
| **Validation** | Same tests, same tolerances as CPU |

GPU acceleration is the most impactful extension for scaling the ED simulation engine beyond the current Atlas. It transforms the 2D and 3D extensions from "feasible but slow" ($\sim$ hours per experiment on CPU) to "fast" ($\sim$ minutes per experiment on GPU), and it enables batch sweep processing that would reduce the parameter-survey wall time from minutes to seconds. The extension is designed to be additive — it does not modify the CPU engine, the data formats, or the validation framework — and it is validated by the same twelve sub-tests (A–N) that certify the CPU implementations.

---

### 10.2 Adaptive Mesh Refinement

The current Suite uses uniform spatial grids: the grid spacing $h$ is constant across the entire domain $\Omega$ (§1.3.1). This is efficient when the solution is spatially smooth or when the features of interest are distributed uniformly. It is inefficient when the solution develops localized structure — steep gradients, narrow boundary layers, or sharp transitions — that requires fine resolution in one region while the remainder of the domain is smooth and could be resolved with a much coarser grid.

The ED system generates exactly this type of localized structure in two scenarios: the near-horizon boundary layer (§6 of the Atlas), where the density gradient is steep near $\rho_{\max}$ but smooth elsewhere, and the localized Gaussian IC (IC-C, §2.1.4), where the initial gradient is concentrated near $x_0 = L/2$ and decays rapidly away from it. Adaptive mesh refinement (AMR) would place fine grid points where the gradients are large and coarse grid points where the solution is smooth, reducing the total grid count while maintaining accuracy.

This section describes the design considerations for an AMR extension to the Suite: the refinement criteria (§10.2.1), the error indicators (§10.2.2), and the challenges that must be resolved before AMR can be incorporated (§10.2.3). AMR is not part of the current Suite specification; it is a planned extension for future versions targeting 2D and 3D domains where uniform grids become prohibitively expensive.

---

#### 10.2.1 Refinement Criteria

The AMR system must decide, at each time step (or at regular refinement intervals), which regions of the domain need finer resolution and which can tolerate coarser resolution. The decision is based on refinement criteria — local conditions that, when exceeded, trigger the insertion of additional grid points.

##### 10.2.1.1 Gradient-Based Criterion

The most natural criterion for the ED system is the local gradient magnitude:

$$
|\nabla_h\rho(x_j)| > \theta_{\mathrm{grad}},
$$

where $\theta_{\mathrm{grad}}$ is a user-specified threshold. Grid points where the gradient exceeds the threshold are flagged for refinement; grid points where the gradient is well below the threshold are candidates for coarsening.

**Connection to the architecture.** The gradient magnitude is directly proportional to the local ED-complexity density $|\nabla\rho|^2$. Regions with high gradient contribute disproportionately to $C_{\mathrm{ED}}$ and to the dissipation rate (Lemma C.6). Refining these regions ensures that the dominant dissipation channel — the gradient channel $\mathcal{D}_{\mathrm{diff}} = DP_*'C_{\mathrm{ED}}$ — is accurately resolved, which is essential for the energy monotonicity and the dissipation-identity closure.

**Threshold selection.** The threshold $\theta_{\mathrm{grad}}$ controls the trade-off between accuracy and grid count. A small threshold (aggressive refinement) produces more grid points and higher accuracy; a large threshold (conservative refinement) produces fewer grid points and lower accuracy. The default is:

$$
\theta_{\mathrm{grad}} = 0.1 \cdot \frac{\rho_{\max} - \rho^*}{L},
$$

which flags regions where the density changes by more than $10\%$ of its dynamic range per domain length — a moderate criterion that captures the near-horizon boundary layer and the Gaussian peak but does not refine the smooth interior.

##### 10.2.1.2 Curvature-Based Criterion

The second-derivative (curvature) criterion refines regions where the solution has high spatial curvature, which is where the finite-difference truncation error is largest:

$$
|\nabla_h^2\rho(x_j)| > \theta_{\mathrm{curv}}.
$$

This criterion is complementary to the gradient criterion: a steep but linear profile (large $|\nabla\rho|$ but small $|\nabla^2\rho|$) is well-resolved by a coarse grid with an appropriate slope; a narrow peak or a sharp kink (large $|\nabla^2\rho|$) requires fine resolution regardless of the gradient magnitude.

**Connection to the architecture.** The Laplacian $\nabla^2\rho$ is the principal part of the operator $F[\rho]$. The truncation error of the finite-difference Laplacian is $O(h^2|\nabla^4\rho|)$, which is proportional to the fourth derivative. The curvature $|\nabla^2\rho|$ is a proxy for the fourth derivative (by the Sobolev interpolation inequality, $\|\nabla^4\rho\|_{L^2} \leq C\|\nabla^2\rho\|_{H^2}$), making it a practical error indicator.

##### 10.2.1.3 Mobility-Based Criterion

A criterion specific to the ED system: refine regions where the mobility is small (near the horizon):

$$
M(\rho(x_j)) < \theta_M \cdot M_*,
$$

where $\theta_M$ is a fraction of the equilibrium mobility (default: $\theta_M = 0.1$). This criterion ensures that the near-horizon boundary layer — where the equation transitions from parabolic to degenerate — is always well-resolved, even if the local gradient is not yet large (the gradient may be suppressed by the vanishing mobility before it can grow large).

**Connection to the architecture.** The mobility-based criterion directly targets Principle 4 (Mobility Capacity Bound). The near-horizon region is where the effective complexity amplification $\mathcal{A}(\rho) = P'/M$ diverges (§6.3 of the Atlas), and accurate resolution of this region is essential for verifying Propositions C.10 and C.11.

##### 10.2.1.4 Combined Criterion

The refinement decision uses the logical OR of the three criteria: a grid point is flagged for refinement if *any* of the three conditions is met:

$$
\text{Refine at } x_j \quad \text{if} \quad |\nabla_h\rho_j| > \theta_{\mathrm{grad}} \;\;\text{OR}\;\; |\nabla_h^2\rho_j| > \theta_{\mathrm{curv}} \;\;\text{OR}\;\; M(\rho_j) < \theta_M M_*.
$$

The coarsening decision uses the logical AND of the negations: a grid point is a candidate for coarsening only if *all* three criteria are far from their thresholds:

$$
\text{Coarsen at } x_j \quad \text{if} \quad |\nabla_h\rho_j| < 0.1\,\theta_{\mathrm{grad}} \;\;\text{AND}\;\; |\nabla_h^2\rho_j| < 0.1\,\theta_{\mathrm{curv}} \;\;\text{AND}\;\; M(\rho_j) > 2\theta_M M_*.
$$

The factor-of-$10$ hysteresis between refinement and coarsening thresholds prevents rapid oscillation of the grid (a point refined at one step and coarsened at the next).

---

#### 10.2.2 Error Indicators

The refinement criteria of §10.2.1 are heuristic — they are based on properties of the solution (gradients, curvature, mobility) rather than on a direct estimate of the discretization error. A more rigorous approach uses **a posteriori error indicators** that estimate the local truncation error from the computed solution.

##### 10.2.2.1 Richardson-Based Error Indicator

The local truncation error of the second-order finite-difference scheme is $O(h^2)$. At each grid point, the error can be estimated by computing the solution on two grids — the current grid with spacing $h$ and a coarsened grid with spacing $2h$ — and comparing them:

$$
\epsilon_j^{\mathrm{Rich}} \approx \frac{|\rho_j^{(h)} - \rho_j^{(2h)}|}{2^p - 1},
$$

where $p = 2$ is the convergence order and $\rho_j^{(2h)}$ is the solution on the coarser grid, estimated by averaging adjacent fine-grid values:

$$
\rho_j^{(2h)} \approx \frac{1}{2}(\rho_{j-1}^{(h)} + \rho_{j+1}^{(h)}).
$$

The Richardson indicator provides a quantitative error estimate (in the same units as $\rho$) without requiring an analytic solution or a reference computation.

**Cost.** The indicator is computed from the existing fine-grid solution — no additional integration is needed. The cost is $O(N_{\mathrm{grid}})$ per evaluation (one pass over the array).

##### 10.2.2.2 Gradient-Jump Error Indicator

At the interface between refined and coarsened regions (where the grid spacing changes), the gradient may be discontinuous. The magnitude of this discontinuity is an error indicator:

$$
\epsilon_j^{\mathrm{jump}} = |(\nabla_h\rho)_{j+1/2} - (\nabla_h\rho)_{j-1/2}|,
$$

where the half-indices denote the gradient evaluated on each side of a grid-spacing transition. This indicator is specific to AMR grids (it is zero on uniform grids) and flags regions where the refinement level transition introduces a spurious error.

##### 10.2.2.3 Energy-Based Error Indicator

The energy dissipation identity (Lemma C.6) provides a global error indicator: the discrete dissipation residual $r^n = (\mathcal{E}^{n+1} - \mathcal{E}^n)/\Delta t + \mathcal{D}_{\mathrm{total}}^n$ (§5.2.3) should be $O(h^2 + \Delta t^p)$. A residual that exceeds this bound indicates that the discretization error is larger than expected — possibly because the solution has developed structure that the current grid cannot resolve.

The energy-based indicator is global (one scalar for the entire domain), not local (one value per grid point). It signals that refinement is needed somewhere but does not identify where. It is used as a trigger for the local indicators: when $|r^n|$ exceeds a threshold, the local gradient and curvature indicators are evaluated to identify the regions that need refinement.

---

#### 10.2.3 Challenges

AMR introduces several complications that do not arise with uniform grids. Each must be resolved before an AMR implementation can pass the Suite's validation tests.

##### 10.2.3.1 Neumann Boundary Conditions on Adaptive Grids

The ghost-point reflection (§1.5.1) is designed for uniform grids: the ghost value $\rho_{-1} := \rho_1$ assumes that the grid spacing is the same on both sides of the boundary. On an adaptive grid with non-uniform spacing, the ghost-point formula must be generalized to account for the local spacing:

$$
\rho_{\mathrm{ghost}} = \rho_{\mathrm{mirror}} + O(h_{\mathrm{local}}^2),
$$

where $h_{\mathrm{local}}$ is the spacing at the boundary. The Neumann condition $\partial_\nu\rho = 0$ must be enforced to the same order as the interior stencil ($O(h^2)$), which requires a modified ghost-point formula that accounts for the non-uniform spacing.

##### 10.2.3.2 Conservation on Non-Uniform Grids

The discrete divergence-theorem identity $\sum_j(\nabla_h^2\rho)_j = 0$ (§1.5.3.2) guarantees that the total mass evolves correctly. On a non-uniform grid, the Laplacian stencil must be modified to preserve this identity — the standard central-difference stencil with variable spacing does not automatically satisfy $\sum_j(\nabla_h^2\rho)_j = 0$ unless the weights are carefully chosen. A conservative discretization (one that preserves the integral identities on non-uniform grids) is required.

##### 10.2.3.3 Implicit Solver on Non-Uniform Grids

The tridiagonal structure of the 1D implicit matrix (§1.4.1) is preserved on non-uniform grids (the stencil still accesses only $j-1$, $j$, $j+1$), but the matrix entries become spacing-dependent:

$$
A_{j,j} = 1 + \Delta t\,D\,M(\rho_j)\left(\frac{1}{h_{j-1/2}\,\bar{h}_j} + \frac{1}{h_{j+1/2}\,\bar{h}_j}\right),
$$

where $h_{j\pm 1/2}$ are the half-spacings and $\bar{h}_j = (h_{j-1/2} + h_{j+1/2})/2$ is the control-volume width. The Thomas algorithm still applies (the matrix is tridiagonal), but the entries are non-uniform and must be recomputed whenever the grid changes.

In 2D and 3D, the sparse matrix structure on a non-uniform grid is more complex (the bandwidth may vary with refinement level), requiring an adaptive sparse-matrix assembly at each refinement event.

##### 10.2.3.4 Spectral Method Incompatibility

The spectral method (Method B) is fundamentally incompatible with AMR: the Neumann eigenbasis $\{\varphi_k(x)\}$ is defined on a uniform grid, and the DCT assumes equispaced samples. On a non-uniform grid, the eigenbasis is no longer a set of cosines, and the DCT cannot be used. AMR is therefore restricted to Method A (finite-difference).

The spectral observables (modal amplitudes, triad coefficients) can still be computed from an AMR solution by interpolating the solution onto a uniform grid and applying the DCT. The interpolation introduces an $O(h_{\mathrm{interp}}^p)$ error, where $h_{\mathrm{interp}}$ is the spacing of the interpolation grid and $p$ is the interpolation order. For spectral analysis, the interpolation grid should be at least as fine as the finest AMR level.

##### 10.2.3.5 Energy Monotonicity Preservation

The energy dissipation (Lemma C.6) is proved for the continuous PDE, not for any particular discretization. On a uniform grid with the standard stencil, the discrete energy is monotonically non-increasing (verified by Validation Test 2, §8.2.2). On a non-uniform grid with a modified stencil, the monotonicity must be re-verified — the modified stencil may introduce a discretization error that temporarily violates the energy inequality.

The challenge is that grid changes (refinement or coarsening) modify the solution by interpolation or restriction, which can change the energy. The energy change from a refinement event must be bounded and accounted for in the dissipation identity — otherwise, the energy-monotonicity check (§2.6.2.4) will produce false violations every time the grid changes.

**Approach.** After each refinement event, recompute the energy from the refined solution and accept the new value as the baseline for subsequent monotonicity checks. The energy change from the refinement is logged as a diagnostic event (not an error), and the dissipation-identity residual is evaluated only between refinement events (not across them).

##### 10.2.3.6 Reproducibility Across Refinement Histories

Two runs of the same experiment with different refinement histories (e.g., slightly different threshold parameters, or different evaluation frequencies for the refinement criteria) may produce different grids at intermediate times, leading to different solutions. The solutions should converge to the same result as the refinement becomes finer (this is the convergence guarantee of the AMR scheme), but at any fixed refinement level, the results may differ.

This is a Tier 3 reproducibility issue (§7.1.4.3): the refinement history is part of the "implementation" rather than the "specification," so different AMR implementations may produce different intermediate results while agreeing on the converged solution. The `spec_hash` (§6.4.5) would need to be extended to include the AMR parameters (thresholds, refinement frequency, maximum levels) to distinguish runs with different AMR configurations.

##### 10.2.3.7 Validation Test Adaptation

The current validation tests (§§8.1–8.5) assume a uniform grid. On an AMR grid:

- **The linear regime validation** (§8.1) can be performed on a uniform grid at the finest AMR level (equivalent to a uniform fine grid with no adaptivity). This verifies the engine's core algorithms without the complication of adaptivity.
- **The nonlinear validation** (§8.2) must be run on the actual AMR grid to verify that the adaptivity does not introduce artifacts (energy violations, positivity failures, false triad activations).
- **The convergence study** (§2.7) must be modified: instead of refining $N$ uniformly, the AMR parameters are tightened (lower thresholds, more refinement levels), and convergence is measured as the AMR tolerance decreases.

---

#### 10.2.4 Estimated Benefit

The benefit of AMR depends on how localized the solution's features are. For the ED system:

| Scenario | Uniform grid $N$ | AMR grid (estimated) | Saving |
|---------|-----------------|---------------------|--------|
| 1D, Gaussian IC ($\sigma = 0.05$, $L = 1$) | $512$ | $\sim 100$ (fine near peak, coarse elsewhere) | $5\times$ |
| 1D, near-horizon ($\delta = 0.01$) | $1{,}024$ | $\sim 200$ (fine near $\rho_{\max}$ region, coarse elsewhere) | $5\times$ |
| 2D, localized perturbation | $256^2 = 65{,}536$ | $\sim 5{,}000$ (fine in one corner, coarse elsewhere) | $13\times$ |
| 2D, uniform perturbation (IC-A) | $256^2 = 65{,}536$ | $\sim 65{,}536$ (no benefit; the feature is global) | $1\times$ |
| 3D, localized perturbation | $128^3 = 2{,}097{,}152$ | $\sim 50{,}000$ (fine in one octant) | $42\times$ |

The savings are most dramatic in 3D, where the ratio of the localized-feature volume to the total domain volume is smallest. In 1D with smooth initial conditions (IC-A, IC-B), the solution is globally smooth and AMR provides little or no benefit.

---

#### 10.2.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Current status** | Uniform grids only; AMR is a planned extension |
| **Refinement criteria** | Gradient, curvature, and mobility (combined with OR logic) |
| **Error indicators** | Richardson (local, quantitative), gradient jump (interface), energy residual (global trigger) |
| **Key challenges** | Neumann BCs on non-uniform grids, conservation, implicit solver adaptation, spectral incompatibility, energy monotonicity across refinements, reproducibility |
| **Method restriction** | AMR applies to Method A only; Method B requires uniform grids |
| **Estimated saving** | $5\times$ (1D localized), $13\times$ (2D localized), $42\times$ (3D localized); $1\times$ for globally smooth solutions |
| **Validation** | Linear tests on uniform fine grid; nonlinear tests on AMR grid; convergence by AMR-tolerance refinement |

AMR is the most impactful extension for reducing the computational cost of 2D and 3D experiments where the solution has localized features. Its implementation requires resolving the six challenges of §10.2.3 — each of which involves a nontrivial modification to the engine's spatial discretization, implicit solver, or validation framework. The extension is designed to be additive: the uniform-grid engine is unmodified, and the AMR layer wraps it with a grid-management system that refines and coarsens the grid while delegating the actual time stepping to the existing stencil and solver infrastructure.

---

### 10.3 Higher-Order Schemes

The current Suite uses second-order spatial discretization (Method A, §1.3.1) and first-to-fourth-order temporal discretization (implicit Euler through ETD-RK4, §1.4). The spectral method (Method B, §1.3.2) achieves exponential spatial accuracy for smooth solutions but is limited to rectangular domains with Neumann conditions. This section assesses the benefits and tradeoffs of upgrading to higher-order finite-difference schemes, compares their accuracy-cost characteristics to the spectral method, and identifies the scenarios where the upgrade is justified.

---

#### 10.3.1 Higher-Order Finite Differences

##### 10.3.1.1 Fourth-Order Laplacian Stencil

The standard second-order Laplacian stencil (§1.3.1.1) uses three points per dimension:

$$
(\nabla_h^2\rho)_j^{(2)} = \frac{\rho_{j-1} - 2\rho_j + \rho_{j+1}}{h^2} + O(h^2).
$$

The fourth-order stencil uses five points:

$$
(\nabla_h^2\rho)_j^{(4)} = \frac{-\rho_{j-2} + 16\rho_{j-1} - 30\rho_j + 16\rho_{j+1} - \rho_{j+2}}{12h^2} + O(h^4).
$$

The truncation error is $O(h^4)$ instead of $O(h^2)$: at the same grid spacing $h$, the fourth-order stencil is $h^2/h^4 = 1/h^2$ times more accurate. Equivalently, to achieve the same accuracy as the second-order stencil at $N$ points, the fourth-order stencil needs only $\sim N^{1/2}$ points — a substantial reduction for large $N$.

**Cost.** The five-point stencil accesses two additional neighbors per grid point (5 instead of 3). The per-point cost increases by $\sim 70\%$ (from 3 additions + 1 multiplication to 5 additions + 4 multiplications). The total cost per stencil evaluation is $O(N)$ with a larger constant.

##### 10.3.1.2 Fourth-Order Gradient Stencil

The second-order gradient approximation:

$$
(\nabla_h\rho)_j^{(2)} = \frac{\rho_{j+1} - \rho_{j-1}}{2h} + O(h^2).
$$

The fourth-order gradient approximation:

$$
(\nabla_h\rho)_j^{(4)} = \frac{-\rho_{j+2} + 8\rho_{j+1} - 8\rho_{j-1} + \rho_{j-2}}{12h} + O(h^4).
$$

The gradient-squared $|\nabla_h\rho|^2 = ((\nabla_h\rho)^{(4)})^2$ is then sixth-order accurate in $\rho$ (the square of a fourth-order quantity is accurate to at least fourth order in the truncation sense, though the formal order of $|\nabla\rho|^2$ as a composite approximation is fourth).

##### 10.3.1.3 Sixth-Order and Beyond

Sixth-order stencils use seven points per dimension:

$$
(\nabla_h^2\rho)_j^{(6)} = \frac{2\rho_{j-3} - 27\rho_{j-2} + 270\rho_{j-1} - 490\rho_j + 270\rho_{j+1} - 27\rho_{j+2} + 2\rho_{j+3}}{180h^2} + O(h^6).
$$

Each additional order of accuracy adds one point to the stencil width. The stencil coefficients grow in magnitude (the leading coefficient is $490/180 \approx 2.7$ for the sixth-order stencil versus $30/12 = 2.5$ for fourth-order and $2$ for second-order), which can amplify rounding errors.

Beyond sixth order, the stencil coefficients become large and alternating in sign, making the approximation sensitive to rounding noise at low $N$. In practice, sixth-order is the highest useful order for finite-difference stencils; beyond that, spectral methods are more effective.

##### 10.3.1.4 Boundary Treatment

The higher-order stencils require more ghost points for the Neumann boundary condition:

| Order | Stencil width | Ghost points needed (per boundary) |
|-------|-------------|-----------------------------------|
| 2nd | 3 | 1 |
| 4th | 5 | 2 |
| 6th | 7 | 3 |

The ghost-point values are determined by the Neumann condition $\partial_\nu\rho = 0$ and its derivatives. For the second-order scheme, a single reflection $\rho_{-1} = \rho_1$ suffices. For the fourth-order scheme, two conditions are needed:

$$
\rho_{-1} = \rho_1, \qquad \rho_{-2} = \rho_2.
$$

These conditions enforce $\partial_x\rho(0) = 0$ and $\partial_x^3\rho(0) = 0$ (the odd derivatives vanish at the boundary, consistent with the even symmetry imposed by the Neumann condition). For sixth-order: three conditions ($\rho_{-k} = \rho_k$ for $k = 1, 2, 3$).

The symmetry-based ghost-point construction preserves the structural properties of §1.5.3 (the discrete divergence theorem, the Parseval identity) to the order of the stencil.

##### 10.3.1.5 Implicit Matrix Structure

The fourth-order implicit matrix $\mathbf{I} - \Delta t\,D\,\mathbf{M}^n\,\mathbf{L}_h^{(4)}$ is pentadiagonal (bandwidth 2) instead of tridiagonal (bandwidth 1). The Thomas algorithm does not apply; a banded solver with bandwidth 2 is needed. The cost is $O(N)$ per solve (same asymptotic order as tridiagonal) but with a larger constant ($\sim 3\times$ the tridiagonal cost for bandwidth 2).

In 2D, the bandwidth of the implicit matrix increases from $N_x$ (five-point stencil) to $2N_x$ (nine-point stencil for the fourth-order 2D Laplacian), increasing the sparse-solve cost correspondingly.

---

#### 10.3.2 Spectral Accuracy Comparison

The spectral method (Method B) provides exponential accuracy for smooth solutions: the truncation error decreases as $O(e^{-cN})$ for analytic solutions, where $c$ depends on the analyticity strip of the solution in the complex plane. This is faster than any polynomial order ($O(h^p) = O(N^{-p})$).

##### 10.3.2.1 Accuracy Versus Resolution

| Method | Truncation error | $N$ for $10^{-6}$ accuracy | $N$ for $10^{-12}$ accuracy |
|--------|-----------------|---------------------------|----------------------------|
| 2nd-order FD | $O(h^2) = O(N^{-2})$ | $\sim 1{,}000$ | $\sim 10^6$ (impractical) |
| 4th-order FD | $O(h^4) = O(N^{-4})$ | $\sim 32$ | $\sim 1{,}000$ |
| 6th-order FD | $O(h^6) = O(N^{-6})$ | $\sim 10$ | $\sim 100$ |
| Spectral | $O(e^{-cN})$ | $\sim 16$ | $\sim 32$ |

For the ED system's smooth solutions (the canonical constitutive functions are $C^\infty$, and the Neumann boundary conditions are compatible with the cosine eigenbasis): the spectral method achieves machine-precision accuracy at $N = 64$–$128$ modes, while the second-order FD method requires $N = 512$–$1{,}024$ for $\sim 10^{-6}$ accuracy.

The fourth-order FD method narrows the gap substantially: $N = 32$ fourth-order points achieve comparable accuracy to $N = 1{,}000$ second-order points. For the Atlas experiments, where $10^{-4}$–$10^{-6}$ accuracy suffices, fourth-order FD at $N = 64$–$128$ would match the current second-order FD at $N = 512$.

##### 10.3.2.2 Cost Versus Accuracy

The relevant metric is the computational cost to achieve a given accuracy level:

| Method | Cost per step | $N$ for $10^{-6}$ | Total cost for $10^{-6}$ |
|--------|-------------|-------------------|--------------------------|
| 2nd-order FD | $\sim 8N$ flops | $1{,}000$ | $\sim 8{,}000$ flops |
| 4th-order FD | $\sim 15N$ flops | $32$ | $\sim 480$ flops |
| Spectral (ETD-RK4) | $\sim 40N\log N$ flops | $16$ | $\sim 2{,}600$ flops |

At the $10^{-6}$ accuracy level: fourth-order FD is the most efficient (lowest total flop count). The spectral method is less efficient than fourth-order FD in total flops (due to the $N\log N$ cost of the DCT) but provides higher accuracy per point.

At the $10^{-12}$ accuracy level: the spectral method is dramatically more efficient (32 points versus $1{,}000$ for fourth-order FD). For experiments requiring high-precision spectral analysis (triad coefficients, locked amplitude ratios), the spectral method is irreplaceable.

---

#### 10.3.3 Tradeoffs

##### 10.3.3.1 Accuracy Versus Complexity

| Aspect | 2nd-order FD | 4th-order FD | 6th-order FD | Spectral |
|--------|-------------|-------------|-------------|---------|
| Implementation complexity | Low | Moderate | High | High |
| Stencil width | 3 | 5 | 7 | Global ($N$ points) |
| Ghost points per boundary | 1 | 2 | 3 | 0 (built into basis) |
| Implicit matrix bandwidth | 1 (tridiagonal) | 2 (pentadiagonal) | 3 (heptadiagonal) | 0 (ETD, no implicit matrix) |
| Boundary domain restriction | None (any Neumann domain) | None | None | Rectangular only |
| AMR compatibility | Yes | Yes (wider stencil) | Marginal (very wide stencil) | No (§10.2.3.4) |
| Near-horizon handling | Direct | Direct | Direct | Requires care (Gibbs) |
| Code changes from current Suite | None (current default) | Stencil + solver + boundary | Major (stencil + solver + boundary + validation) | None (current Method B) |

##### 10.3.3.2 When Higher Order Is Justified

The upgrade from second-order to fourth-order FD is justified when:

1. **The accuracy requirement exceeds $O(h^2)$ at the available resolution.** If the experiment requires $10^{-6}$ accuracy and the maximum affordable $N$ is $128$ (e.g., in 2D or 3D where $N^d$ grid points are needed): second-order FD at $N = 128$ gives $O(h^2) = O(N^{-2}) \approx 6 \times 10^{-5}$ — one order of magnitude short. Fourth-order FD at $N = 128$ gives $O(h^4) \approx 4 \times 10^{-9}$ — far exceeding the requirement.

2. **The temporal accuracy matches.** There is no benefit to a fourth-order spatial scheme paired with a first-order time scheme (implicit Euler): the temporal error $O(\Delta t)$ dominates regardless of the spatial accuracy. Fourth-order spatial should be paired with at least second-order temporal (Crank–Nicolson) or fourth-order (a Runge–Kutta IMEX scheme or ETD-RK4).

3. **The solution is smooth.** Higher-order FD methods gain their advantage from the assumption that the solution has bounded higher derivatives ($\partial^{p+2}\rho$ must exist and be bounded for order-$p$ accuracy). Near the mobility-collapse boundary ($\rho \to \rho_{\max}$), the solution may develop steep gradients where the higher derivatives are large, reducing the effective order. In these regions, AMR (§10.2) or the spectral method's exponential convergence is more effective than higher-order FD.

##### 10.3.3.3 When Higher Order Is Not Justified

The upgrade is *not* justified when:

1. **The current accuracy is sufficient.** The Atlas experiments at $N = 512$ with second-order FD achieve $1\%$ accuracy in decay rates and $5\%$ in amplitude ratios (§2.7.3.3). If these tolerances are acceptable, the upgrade provides no benefit to the scientific conclusions.

2. **The time step is the bottleneck.** If the experiment is limited by the CFL constraint (§1.8.1) rather than by the spatial accuracy, reducing $N$ (which the higher-order scheme enables) also reduces $h$ and tightens the CFL. The time-step saving may offset the spatial-point saving, producing no net speedup.

3. **The problem is 1D.** In 1D, the cost of the second-order scheme at $N = 512$ is $\sim 10\,\mu$s per step — already negligible. Reducing $N$ to $128$ with a fourth-order scheme saves $\sim 7\,\mu$s per step, which is immaterial for the Atlas's wall time.

##### 10.3.3.4 The Recommended Upgrade Path

For the current Atlas: **no upgrade is needed.** The second-order FD (Method A) and spectral (Method B) methods are sufficient for all 55 experiments at the stated tolerances.

For the 2D extensions (Atlas §12.4): **fourth-order FD is recommended.** At $N = 128$ per direction ($N_{\mathrm{grid}} = 16{,}900$): second-order gives $O(h^2) \approx 6 \times 10^{-5}$; fourth-order gives $O(h^4) \approx 4 \times 10^{-9}$. The fourth-order scheme achieves the same accuracy as the second-order scheme at $N = 1{,}024$ per direction ($N_{\mathrm{grid}} = 1{,}052{,}676$) — a $62\times$ reduction in grid points, which translates to a $\sim 60\times$ reduction in memory and a $\sim 60\times$ reduction in per-step cost.

For the 3D extensions: **fourth-order FD is strongly recommended.** The same analysis in 3D gives a $\sim 250\times$ reduction in grid points (from $N = 512$ per direction to $N = 32$ per direction at the same accuracy level). This makes 3D simulations feasible on a single workstation instead of requiring a cluster.

---

#### 10.3.4 Implementation Effort

| Component | Change required for 4th-order FD |
|-----------|--------------------------------|
| Stencil functions | Replace 3-point with 5-point formulas; add second ghost point |
| Implicit matrix | Replace tridiagonal with pentadiagonal; replace Thomas with banded solver |
| Boundary treatment | Two ghost points per boundary; verify Neumann to 4th order |
| CFL condition | Recompute with wider stencil (the CFL constant changes) |
| Convergence tests (§2.7) | Verify 4th-order convergence rate ($p_h = 4.0 \pm 0.4$) |
| Validation tests (§8) | All twelve sub-tests (A–N) must pass at the same tolerances |
| Observable extraction | No change (the observables are computed from the grid values, not from the stencil) |
| Spectral analysis | No change (the DCT is applied to the grid values, independent of the stencil order) |
| Data formats | No change (the time-series and spectral files have the same structure) |
| Metadata | Add `spatial_order` field to the schema (§6.4) |

The implementation effort is moderate: the stencil and solver changes are localized (§1.3 and §1.4 only), and the rest of the engine (§§2–8) is unchanged. The validation effort is the dominant cost — all twelve sub-tests must be re-run and re-verified at the new order.

---

#### 10.3.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Current spatial order** | 2nd (Method A), spectral (Method B) |
| **Proposed upgrade** | 4th-order FD for Method A; spectral unchanged |
| **Stencil** | 5-point ($-1, 16, -30, 16, -1$)/($12h^2$) |
| **Implicit matrix** | Pentadiagonal (bandwidth 2); banded solver |
| **Accuracy gain** | $O(h^4)$ vs. $O(h^2)$: same accuracy at $\sim N^{1/2}$ points |
| **Cost per point** | $\sim 1.7\times$ higher (5-point vs. 3-point stencil + banded vs. tridiagonal solver) |
| **Net cost at same accuracy** | $\sim 35\times$–$250\times$ lower in 2D/3D (fewer grid points needed) |
| **Justified for** | 2D at $N > 64$; 3D at any $N$; high-accuracy 1D studies |
| **Not justified for** | Standard 1D Atlas; experiments limited by temporal accuracy |
| **Spectral comparison** | 4th-order FD is more efficient at moderate accuracy ($10^{-6}$); spectral is superior at high accuracy ($10^{-12}$) |
| **Implementation effort** | Moderate (stencil + solver + boundary + validation); rest of engine unchanged |

Higher-order finite differences are the natural upgrade path for scaling the ED simulation engine to 2D and 3D domains. They provide a multiplicative reduction in grid count ($\sim N^{p/2}$ for order $p$) that compounds in higher dimensions ($\sim N^{dp/2}$ total), making the upgrade most valuable precisely where the computational cost is highest. The upgrade is self-contained (it modifies only the spatial discretization module), is validated by the same tests as the current engine, and is transparent to all downstream consumers (the data formats, observables, and figure specifications are unchanged).

---

### 10.4 Multi-Domain Coupling

The canonical ED system is posed on a single, connected spatial domain $\Omega$ with Neumann boundary conditions (§1.5). All Atlas experiments operate on this single domain. The **multi-domain coupling** extension partitions a large or geometrically complex problem into multiple subdomains, each solved independently, with interface conditions that couple the subdomains into a globally consistent solution. This extension addresses two distinct use cases: computational domain decomposition (§10.4.3.1), where a single physical domain is split for parallel efficiency, and physical multi-region coupling (§10.4.3.2), where distinct physical regions with different constitutive properties are joined.

Multi-domain coupling is not part of the current Suite specification. It is a planned extension for scenarios that exceed the single-domain framework: very large 2D/3D domains that do not fit in a single worker's memory, multi-material systems where the constitutive functions differ between regions, and multi-scale problems where different regions require different resolutions.

---

#### 10.4.1 Domain Decomposition

Domain decomposition splits a single domain $\Omega$ into $K$ non-overlapping subdomains $\Omega_1, \Omega_2, \ldots, \Omega_K$ with $\Omega = \bigcup_k\Omega_k$ and $\Omega_i \cap \Omega_j = \emptyset$ for $i \neq j$. Each subdomain is solved by a separate worker, and the subdomains are coupled through interface conditions that ensure the global solution is continuous and smooth across the subdomain boundaries.

##### 10.4.1.1 Partitioning Strategy

For the rectangular domains of the Suite ($\Omega = [0, L]^d$), the natural decomposition is a Cartesian partition:

**1D:** Split $[0, L]$ into $K$ intervals $[x_{k-1}, x_k]$, $k = 1, \ldots, K$, with $x_0 = 0$ and $x_K = L$.

**2D:** Split $[0, L_x] \times [0, L_y]$ into a $K_x \times K_y$ grid of rectangular subdomains.

**3D:** Split into a $K_x \times K_y \times K_z$ grid.

Each subdomain has $N_k$ interior grid points (approximately $N_{\mathrm{total}}/K$ for a uniform partition). The partition is defined at initialization and does not change during the integration (static decomposition). Dynamic repartitioning (load balancing during the integration) is a further extension beyond the scope of this section.

##### 10.4.1.2 Ghost Zones

Each subdomain maintains a layer of **ghost zones** along its internal boundaries — grid points that overlap with the neighboring subdomain and are updated by receiving data from the neighbor at each time step (or at each coupling synchronization point).

The ghost-zone width depends on the stencil width:

| Stencil order | Stencil width | Ghost zones needed |
|--------------|-------------|-------------------|
| 2nd | 3 | 1 |
| 4th | 5 | 2 |
| 6th | 7 | 3 |

The ghost zones are in addition to the Neumann ghost points at the *external* boundaries (the original boundaries of $\Omega$). Internal boundaries between subdomains use *continuity* ghost zones (receiving data from the neighbor), not *reflection* ghost zones (the Neumann condition does not apply at internal boundaries).

##### 10.4.1.3 Communication Pattern

At each synchronization point (typically once per time step), each subdomain sends its boundary values to its neighbors and receives the neighbor's boundary values into its ghost zones:

**1D, $K$ subdomains:** Subdomain $k$ sends $\rho_{x_k}$ (its right boundary value) to subdomain $k+1$ and $\rho_{x_{k-1}}$ (its left boundary value) to subdomain $k-1$. It receives $\rho_{x_k}$ from subdomain $k+1$ (to fill its right ghost zone) and $\rho_{x_{k-1}}$ from subdomain $k-1$ (to fill its left ghost zone). The communication volume is $2$ scalar values per boundary per step — negligible.

**2D, $K_x \times K_y$ subdomains:** Each subdomain exchanges boundary strips (1D arrays of length $N_y/K_y$) with its four neighbors. The communication volume is $4 \times N_y/K_y$ values per step per subdomain.

**3D:** Each subdomain exchanges boundary planes with its six neighbors. The communication volume is $6 \times (N_y/K_y)(N_z/K_z)$ values per step per subdomain.

The communication is nearest-neighbor only (each subdomain communicates with at most $2d$ neighbors in $d$ dimensions). This pattern is compatible with distributed-memory parallelism (MPI) and with shared-memory parallelism (each subdomain is a thread with shared access to the ghost-zone arrays).

---

#### 10.4.2 Interface Conditions

The interface conditions specify how the solution is coupled across subdomain boundaries. The conditions must ensure that the global solution is:

1. **Continuous:** $\rho$ has no jumps at the interface.
2. **Smooth:** $\nabla\rho$ is continuous at the interface (to the order of the stencil).
3. **Conservative:** The total mass $\int_\Omega\rho\,dx$ is preserved by the coupling (no mass is created or destroyed at the interface).

##### 10.4.2.1 Continuity of Density

The simplest interface condition is **direct injection**: the ghost-zone value at the interface is set equal to the neighboring subdomain's boundary value:

$$
\rho_{\mathrm{ghost},k}^{\mathrm{right}} := \rho_{\mathrm{boundary},k+1}^{\mathrm{left}}.
$$

This ensures pointwise continuity of $\rho$ at the interface. The condition is applied after each subdomain completes its time step (or at each synchronization point).

##### 10.4.2.2 Continuity of Flux

Continuity of the density alone is not sufficient for a conservative scheme. The *flux* — the diffusive transport across the interface — must also be continuous:

$$
M(\rho)\,\partial_\nu\rho\big|_{\mathrm{right\;of\;interface}} = M(\rho)\,\partial_\nu\rho\big|_{\mathrm{left\;of\;interface}}.
$$

This condition is automatically satisfied if the ghost zones are wide enough for the stencil to compute the gradient accurately at the interface. For the second-order stencil (one ghost zone): the gradient at the boundary point $x_k$ is computed from $\rho_{x_k - h}$, $\rho_{x_k}$, $\rho_{x_k + h}$, where $\rho_{x_k + h}$ is the ghost value received from subdomain $k+1$. If the ghost value is the exact boundary value of subdomain $k+1$, the gradient is accurate to $O(h^2)$ — the same order as the interior stencil — and the flux is continuous to $O(h^2)$.

For higher-order stencils (more ghost zones): the flux continuity extends to $O(h^p)$, where $p$ is the stencil order.

##### 10.4.2.3 Conservation Check

The global mass evolution (§1.5.3.2) is:

$$
\frac{d}{dt}\int_\Omega\rho\,dx = -D\int_\Omega P(\rho)\,dx + H\,v\,|\Omega|.
$$

On a decomposed domain: $\int_\Omega\rho\,dx = \sum_k\int_{\Omega_k}\rho\,dx$. If the subdomain integrals use consistent quadrature weights at the interfaces (each interface grid point is counted once, not twice), the global integral is preserved. The engine verifies this by computing the global mass at each output step and checking the mass-rate residual (Validation Test 3, §8.1 adapted for the decomposed domain).

##### 10.4.2.4 Participation Variable Coupling

The participation variable $v(t)$ is spatially constant — it has the same value everywhere in $\Omega$. On a decomposed domain, each subdomain maintains its own copy of $v$, and all copies must agree. The coupling is:

1. Each subdomain computes its local spatial average $\bar{F}_k = |\Omega_k|^{-1}\int_{\Omega_k}F[\rho]\,dx$.
2. The global average is $\bar{F} = |\Omega|^{-1}\sum_k|\Omega_k|\bar{F}_k$.
3. The participation update $v^{n+1} = v^n e^{-\zeta\Delta t/\tau} + \bar{F}/\zeta\,(1 - e^{-\zeta\Delta t/\tau})$ is applied identically on all subdomains using the same $\bar{F}$.

The global average computation (Step 2) requires a global reduction (an all-reduce in MPI terminology): each subdomain contributes its $|\Omega_k|\bar{F}_k$ to a global sum. The communication volume is $1$ scalar value per subdomain per step — negligible.

---

#### 10.4.3 Use Cases

##### 10.4.3.1 Computational Domain Decomposition

**Scenario.** A single physical domain that is too large for a single worker's memory or too expensive for a single worker's computation time.

**Example.** A 3D simulation at $N = 128$ per direction: $N_{\mathrm{grid}} \approx 2 \times 10^6$ grid points, $\sim 300$ MB engine memory (§9.5.3.4). Decomposed into $K = 8$ subdomains ($2 \times 2 \times 2$ partition): each subdomain has $\sim 250{,}000$ grid points, $\sim 40$ MB engine memory — well within the $500$ MB budget.

**Benefits.** Memory: each worker holds $1/K$ of the total data. Time: each worker computes $1/K$ of the total grid in the stencil, constitutive, and operator evaluations. The speedup is $\sim K$ (linear in the number of subdomains) minus the communication overhead.

**Communication cost.** For the 3D example at $K = 8$: each subdomain exchanges $6$ boundary planes of $\sim 64 \times 64 = 4{,}096$ values, totaling $\sim 200$ KB per step. At $\sim 10\,\mu$s per KB on a shared-memory system: $\sim 2$ ms per step. The computation per subdomain per step is $\sim 5$ ms (at $\sim 200\,\mu$s per step for $250{,}000$ points, adjusted for the implicit solver). The communication fraction is $\sim 30\%$ — acceptable but not negligible. The scalability is limited to $K \sim 16$–$32$ subdomains before communication dominates.

##### 10.4.3.2 Physical Multi-Region Coupling

**Scenario.** A domain with spatially varying constitutive properties — different regions have different mobility or penalty functions, modeling different materials or different physical phases.

**Example.** A 1D domain $[0, 2L]$ composed of two regions: $[0, L]$ with mobility $M_1(\rho)$ (a "bulk" material) and $[L, 2L]$ with mobility $M_2(\rho)$ (a "surface" material). The two regions share the same density field $\rho(x, t)$ and the same participation variable $v(t)$, but the constitutive functions differ.

This scenario is not covered by the current Suite (which assumes a single pair of constitutive functions on the entire domain). The multi-domain extension handles it naturally: each subdomain has its own constitutive function record, and the interface conditions ensure that $\rho$ and $M(\rho)\partial_\nu\rho$ are continuous at the material boundary.

**Architectural significance.** The universality class $\mathcal{U}_{\mathrm{ED}}$ (Appendix D) is defined for systems satisfying Principles 1–7. A multi-region system satisfies the principles on each subdomain separately, but the global system may have interfaces where the constitutive functions are discontinuous. The interface conditions of §10.4.2 ensure that the global solution is well-posed (continuous density, continuous flux), but the interface itself — a discontinuity in $M(\rho)$ — is a new structural element not present in the single-domain theory. The behavior of the ED system at constitutive interfaces (e.g., reflection, transmission, or refraction of density waves) is an open question that multi-domain simulations can explore.

##### 10.4.3.3 Multi-Scale Coupling

**Scenario.** A domain with regions that require vastly different spatial resolutions — a fine-scale region (narrow boundary layer, sharp interface) embedded in a coarse-scale background.

**Example.** A 2D domain with a near-horizon region ($\rho \approx \rho_{\max}$) occupying $1\%$ of the domain area but requiring $10\times$ finer resolution than the remainder. A uniform grid resolving the boundary layer at $h_{\mathrm{fine}}$ would require $(10L/h_{\mathrm{fine}})^2$ points; a multi-domain approach with a fine-resolution subdomain covering the $1\%$ boundary-layer region and a coarse-resolution subdomain covering the $99\%$ background requires $\sim (L/(10h_{\mathrm{fine}}))^2 + (L/h_{\mathrm{fine}})^2 = 0.01(10L/h_{\mathrm{fine}})^2 + (L/h_{\mathrm{fine}})^2$ — a $\sim 50\times$ reduction in total grid points compared to the uniform fine grid.

The multi-scale coupling is a combination of domain decomposition (§10.4.3.1) and non-uniform resolution. The interface between the fine and coarse subdomains requires interpolation (coarse to fine) and restriction (fine to coarse) operators that maintain the conservation and continuity conditions of §10.4.2.

This use case overlaps with AMR (§10.2) but is architecturally different: AMR dynamically adjusts the resolution within a single domain, while multi-domain coupling statically assigns different resolutions to different subdomains. AMR is more flexible (the refinement adapts to the evolving solution); multi-domain is simpler (the decomposition is fixed at initialization) and more amenable to distributed-memory parallelism (each subdomain is a self-contained unit with well-defined communication interfaces).

---

#### 10.4.4 Challenges

##### 10.4.4.1 Synchronization Overhead

The subdomain coupling requires synchronization at each time step (or at each coupling interval). On shared-memory systems: the synchronization is a barrier (all workers must reach the synchronization point before any can proceed). On distributed-memory systems: the synchronization involves message passing (MPI send/receive). Both add latency that scales with the number of subdomains and limits the strong scaling.

**Mitigation.** Overlap communication with computation: while one subdomain is waiting for its ghost values, it can compute the interior stencil (which does not depend on the ghost values). The ghost values are needed only for the boundary stencil, which is a small fraction of the total computation.

##### 10.4.4.2 Implicit Solver Coupling

The implicit time step (§1.4.1) solves a global linear system $\mathbf{A}\boldsymbol{\rho}^{n+1} = \mathbf{R}$. On a decomposed domain, the global system is block-structured: each subdomain contributes a diagonal block (the local implicit matrix), and the interface coupling contributes off-diagonal entries. Two approaches:

**Block Jacobi (explicit coupling).** Each subdomain solves its local system independently using the ghost values from the previous step. The coupling is lagged by one step ($O(\Delta t)$ error). This is the simplest approach and preserves the single-domain solver infrastructure; it is equivalent to an explicit treatment of the interface flux.

**Schwarz iteration (implicit coupling).** The subdomains iterate within each time step: solve locally, exchange ghost values, solve again, exchange again, repeat until convergence. This eliminates the lag error but requires multiple solves per step (typically $2$–$5$ iterations for convergence). The cost is $2\times$–$5\times$ higher than the block Jacobi approach but provides $O(\Delta t^p)$ accuracy at the interface (matching the interior).

For the ED system: the block Jacobi approach is recommended for initial development. The $O(\Delta t)$ coupling error is the same order as the explicit nonlinear terms and does not degrade the overall accuracy of the semi-implicit scheme.

##### 10.4.4.3 Spectral Analysis on Decomposed Domains

The spectral decomposition (§5.3) requires the global density field — the DCT is a global operation that cannot be applied to individual subdomains. On a decomposed domain, the spectral analysis must first assemble the global field (by collecting all subdomain data onto a single worker), then apply the DCT. This assembly is an all-gather communication with volume $N_{\mathrm{total}}$ values — potentially large for 3D domains.

The assembly is needed only at output steps (not at every time step), so the cost is amortized over $k_{\mathrm{out}}$ steps. For $k_{\mathrm{out}} = 100$ and $N_{\mathrm{total}} = 2 \times 10^6$: the assembly volume is $\sim 16$ MB per output step, occurring $\sim 1{,}000$ times per experiment — $\sim 16$ GB total I/O, which is manageable on modern interconnects.

---

#### 10.4.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Current status** | Single domain only; multi-domain is a planned extension |
| **Decomposition** | Cartesian partition into $K$ non-overlapping subdomains |
| **Ghost zones** | $1$–$3$ layers per internal boundary (stencil-dependent) |
| **Interface conditions** | Density continuity (direct injection), flux continuity (ghost-zone stencil), conservation (consistent quadrature), participation coupling (global all-reduce) |
| **Communication** | Nearest-neighbor exchange per step; $1$ scalar all-reduce for $v$ |
| **Use case 1** | Computational domain decomposition (memory/time reduction; $\sim K\times$ speedup) |
| **Use case 2** | Physical multi-region coupling (different $M$, $P$ in different regions) |
| **Use case 3** | Multi-scale coupling (fine/coarse resolution in different regions; $\sim 50\times$ grid reduction) |
| **Key challenges** | Synchronization overhead, implicit solver coupling, global spectral assembly |
| **Recommended solver coupling** | Block Jacobi (explicit, simple, $O(\Delta t)$ interface error) for initial development |

Multi-domain coupling is the extension that enables the ED simulation engine to scale beyond a single worker's memory and beyond a single domain's constitutive description. It is architecturally distinct from both task-level parallelism (§4.5, which runs independent integrations) and AMR (§10.2, which adapts the resolution within a single domain): domain decomposition splits a *single* integration across multiple workers that must communicate, producing a globally consistent solution from locally computed pieces. The extension requires new infrastructure (ghost-zone management, interface conditions, global reductions) that is absent from the current single-domain engine, but the core algorithms (stencils, solvers, constitutive evaluation, observable extraction) are reused without modification on each subdomain.

---

### 10.5 Stochastic Perturbations

The canonical ED system (C.1) is deterministic: the density operator $F[\rho]$, the participation coupling $Hv$, and the constitutive functions $M(\rho)$, $P(\rho)$ contain no random elements. Every solution is uniquely determined by its initial condition and parameters (Theorem C.2). This determinism is a structural feature of the architecture — the seven canonical principles make no reference to randomness — and it is essential for the analytic theory (the uniqueness, stability, and convergence results of Appendices C.2–C.7 all assume a deterministic PDE).

Physical systems, however, are subject to noise: thermal fluctuations, environmental disturbances, measurement uncertainties, and quantum indeterminacy. The **stochastic perturbation** extension adds controlled noise to the canonical system to model these effects and to probe the robustness of the architectural predictions against random disturbances. This section specifies the noise models (§10.5.1), the resulting stochastic PDE variants (§10.5.2), and the expected effects on the ED dynamics (§10.5.3).

Stochastic perturbations are not part of the current Suite specification. They are a planned extension for future versions targeting the experimental comparison program (Applications Paper §9), where the physical systems are inevitably noisy and the predictions must be robust against noise.

---

#### 10.5.1 Noise Models

Three noise models are defined, each representing a different physical source of randomness and a different mathematical structure.

##### 10.5.1.1 Additive Spatiotemporal White Noise

The simplest noise model adds a Gaussian white-noise field to the density equation:

$$
\partial_t\rho = D\,F[\rho] + H\,v + \sigma_\rho\,\dot{W}(x, t),
$$

where $\dot{W}(x, t)$ is a spatiotemporal white-noise field (the formal time derivative of a cylindrical Wiener process) and $\sigma_\rho > 0$ is the noise intensity. In the Itô interpretation:

$$
d\rho = \bigl(D\,F[\rho] + H\,v\bigr)\,dt + \sigma_\rho\,dW(x, t),
$$

where $dW(x, t)$ is the increment of a $Q$-Wiener process with covariance operator $Q$.

**Physical interpretation.** Additive white noise models thermal fluctuations in the density field — random agitation that is independent of the current state. It is the standard model for Langevin-type dynamics and is appropriate when the noise source is external (environmental) rather than internal (state-dependent).

**Spatial correlation.** True spatiotemporal white noise has zero spatial correlation length — each point $x$ receives an independent noise increment at each time $dt$. On a discrete grid, this produces independent random values at each grid point. For physical applications, the noise should have a finite correlation length $\ell > 0$: the noise at nearby points is correlated, modeling the fact that physical fluctuations have a characteristic scale. The correlated noise is:

$$
\sigma_\rho\,\dot{W}_\ell(x, t) = \sigma_\rho\int_\Omega G_\ell(x - y)\,\dot{W}(y, t)\,dy,
$$

where $G_\ell$ is a spatial kernel with width $\ell$ (e.g., a Gaussian $G_\ell(z) = (2\pi\ell^2)^{-d/2}\exp(-|z|^2/(2\ell^2))$). At $\ell \to 0$: the correlated noise approaches white noise. At $\ell \to L$: the noise becomes spatially uniform (affecting only the homogeneous mode).

**Discrete implementation.** At each time step, generate a random increment:

$$
\Delta W_j^n = \sqrt{\Delta t}\,\xi_j^n, \qquad \xi_j^n \sim \mathcal{N}(0, 1) \text{ i.i.d.},
$$

and add $\sigma_\rho\,\Delta W_j^n/h^{d/2}$ to the density at each grid point (the $h^{-d/2}$ factor normalizes the discrete noise to match the continuous white-noise covariance). For correlated noise: apply the kernel $G_\ell$ by convolution (efficiently computed via the DCT for the Neumann eigenbasis).

##### 10.5.1.2 Multiplicative Noise (State-Dependent)

The noise intensity depends on the current density:

$$
\partial_t\rho = D\,F[\rho] + H\,v + \sigma_\rho\,g(\rho)\,\dot{W}(x, t),
$$

where $g(\rho)$ is a state-dependent noise coefficient. Two physically motivated choices:

**Density-proportional noise:** $g(\rho) = \rho$. The fluctuations scale with the local density — denser regions are noisier. This models Poisson-type fluctuations in particle systems.

**Mobility-proportional noise:** $g(\rho) = \sqrt{M(\rho)}$. The fluctuations scale with the square root of the mobility — the noise is generated by the same transport mechanism that drives the diffusion. This is the fluctuation-dissipation relation: the noise and the dissipation are linked by the mobility, consistent with the Langevin equation for overdamped dynamics.

The mobility-proportional choice is the most architecturally natural: it vanishes at $\rho = \rho_{\max}$ (where $M = 0$), so the noise respects the mobility-collapse barrier — the horizon is "quiet" as well as "frozen." This is a structural prediction: near-horizon configurations experience reduced fluctuations because the transport mechanism that generates them has been extinguished.

**Discrete implementation.** At each time step:

$$
\rho_j^{n+1} = \rho_j^{n+1,\mathrm{det}} + \sigma_\rho\,g(\rho_j^n)\,\frac{\sqrt{\Delta t}}{h^{d/2}}\,\xi_j^n,
$$

where $\rho_j^{n+1,\mathrm{det}}$ is the deterministic update from the implicit/ETD step and $\xi_j^n \sim \mathcal{N}(0, 1)$.

The Itô versus Stratonovich interpretation matters for multiplicative noise. The Suite uses the **Itô** convention (the noise coefficient $g(\rho)$ is evaluated at the pre-step value $\rho^n$, not at $\rho^{n+1}$ or at a midpoint), which is consistent with the explicit treatment of the nonlinear terms in the semi-implicit scheme.

##### 10.5.1.3 Participation Noise

Noise in the participation equation models fluctuations in the feedback mechanism:

$$
\dot{v} = \frac{1}{\tau}\bigl(F[\rho] - \zeta\,v\bigr) + \sigma_v\,\dot{\eta}(t),
$$

where $\dot{\eta}(t)$ is a scalar white-noise process and $\sigma_v > 0$ is the participation noise intensity. This models random perturbations to the integration of the operator output — fluctuations in the "attention" or "participation" of the feedback loop.

**Discrete implementation.** The participation update (§1.4.3) is modified to:

$$
v^{n+1} = v^n e^{-\zeta\Delta t/\tau} + \frac{\bar{F}^n}{\zeta}(1 - e^{-\zeta\Delta t/\tau}) + \sigma_v\sqrt{\frac{\tau}{2\zeta}(1 - e^{-2\zeta\Delta t/\tau})}\,\eta^n,
$$

where $\eta^n \sim \mathcal{N}(0, 1)$ and the noise coefficient is the exact variance of the Ornstein–Uhlenbeck process with damping $\zeta/\tau$ driven by white noise of intensity $\sigma_v$.

---

#### 10.5.2 Stochastic PDE Variants

The noise models of §10.5.1 produce three variants of the canonical system, each with a different mathematical structure and different analytic properties.

##### 10.5.2.1 SPDE with Additive Noise

$$
\begin{cases}
d\rho = \bigl(D\,F[\rho] + H\,v\bigr)\,dt + \sigma_\rho\,dW(x, t), \\
dv = \tau^{-1}(F[\rho] - \zeta\,v)\,dt.
\end{cases}
$$

This is a semilinear stochastic parabolic equation. The noise is additive (independent of $\rho$) and drives the density continuously. The well-posedness theory (existence, uniqueness, regularity) for this class of SPDEs is well-established (Da Prato and Zabczyk, 1992) and requires the noise covariance operator $Q$ to satisfy a trace-class condition: $\operatorname{tr}(Q) < \infty$ (equivalently, the correlated noise with $\ell > 0$ is trace-class; the uncorrelated white noise with $\ell = 0$ is not trace-class in $d \geq 1$ and requires regularization).

##### 10.5.2.2 SPDE with Multiplicative Noise

$$
\begin{cases}
d\rho = \bigl(D\,F[\rho] + H\,v\bigr)\,dt + \sigma_\rho\,g(\rho)\,dW(x, t), \\
dv = \tau^{-1}(F[\rho] - \zeta\,v)\,dt.
\end{cases}
$$

The noise coefficient $g(\rho)$ couples the noise to the state. The well-posedness is more delicate: the Lipschitz continuity of $g$ (required for existence and uniqueness) must be verified for each choice. For $g(\rho) = \rho$: Lipschitz, but the noise can drive $\rho$ negative (violating positivity). For $g(\rho) = \sqrt{M(\rho)}$: Hölder continuous (not Lipschitz at $\rho_{\max}$ where $M = 0$), requiring a separate argument for uniqueness near the boundary.

##### 10.5.2.3 Coupled Density-Participation Noise

$$
\begin{cases}
d\rho = \bigl(D\,F[\rho] + H\,v\bigr)\,dt + \sigma_\rho\,g(\rho)\,dW(x, t), \\
dv = \tau^{-1}(F[\rho] - \zeta\,v)\,dt + \sigma_v\,d\eta(t).
\end{cases}
$$

Both the density and the participation are noisy. The two noise sources $W$ and $\eta$ are independent (they model different physical mechanisms). The participation noise $\sigma_v d\eta$ feeds back into the density through the $Hv$ coupling, so even if $\sigma_\rho = 0$, the density is affected by the participation noise (albeit filtered through the participation ODE's damping).

---

#### 10.5.3 Expected Effects

The stochastic perturbations modify the deterministic ED dynamics in several structurally significant ways.

##### 10.5.3.1 Equilibrium Fluctuations

In the deterministic system, the equilibrium $(\rho^*, 0)$ is a fixed point: once reached (or approached exponentially), the solution remains there forever. With noise, the equilibrium becomes a **fluctuating steady state**: the solution oscillates randomly around $(\rho^*, 0)$ with an amplitude proportional to the noise intensity.

**Stationary variance (additive noise).** For small $\sigma_\rho$, the linearized SPDE has a Gaussian stationary distribution with variance:

$$
\operatorname{Var}(\hat{u}_k) \approx \frac{\sigma_\rho^2\,q_k}{2D\alpha_k},
$$

where $q_k = \langle Q\varphi_k, \varphi_k\rangle$ is the noise power in mode $k$ and $D\alpha_k$ is the modal decay rate. The variance is inversely proportional to the decay rate: slow modes (low $k$) fluctuate more than fast modes (high $k$). The total density variance is $\sum_k\operatorname{Var}(\hat{u}_k)$, dominated by the slowest mode ($k = 1$ or $k = 0$, depending on the spectral gap).

**Architectural prediction.** The fluctuation spectrum $\operatorname{Var}(\hat{u}_k) \propto 1/D\alpha_k$ is determined by the modal hierarchy (Proposition C.29) — the same hierarchy that governs the deterministic decay. The noise does not create a new spectral structure; it populates the existing eigenmodes at amplitudes set by the balance between the noise input and the dissipative output. This is the stochastic analogue of the dissipation-generation balance in the triad coupling (§4.2 of the Atlas): the noise generates spectral content, and the diffusion removes it, with the steady-state amplitude set by their ratio.

##### 10.5.3.2 Noise-Induced Transitions

At finite noise intensity, the stochastic system can explore regions of state space that the deterministic system never visits. Two architecturally significant transitions are possible:

**Noise-induced regime switching.** If the noise drives the effective damping parameter $\Delta_{\mathrm{eff}}(\rho)$ (§8.2 of the Atlas) across the critical value $1$, the system can exhibit stochastic switching between oscillatory and monotonic behavior — even at parameter values that are deterministically in one regime. The switching rate depends on the noise intensity and the distance from the critical surface $\Sigma$: near $\Sigma$, the switching is frequent (the barrier between regimes is low); far from $\Sigma$, it is exponentially rare (Kramers-type escape rate).

**Noise-induced positivity violation.** Additive noise with $g(\rho) = 1$ does not respect the positivity constraint: a large negative noise increment can drive $\rho$ below zero. The probability of this event decreases exponentially with the distance from zero: $P(\rho < 0) \sim \exp(-\rho^{*2}/(2\sigma_\rho^2\Delta t/h^d))$, which is negligible for $\sigma_\rho \ll \rho^*\sqrt{h^d/\Delta t}$. The mobility-proportional noise ($g = \sqrt{M}$) avoids this problem — the noise vanishes at both $\rho = 0$ (where $M$ is typically positive but finite) and $\rho = \rho_{\max}$ (where $M = 0$), providing a state-dependent regularization that respects the admissible region.

##### 10.5.3.3 Robustness of Architectural Predictions

The central question for the stochastic extension is: **do the architectural predictions of the Applications Paper survive the addition of noise?** The expected answer, based on the structural stability of the universality class (Appendix D, Theorem D.19), is yes — the qualitative predictions are robust — with the following caveats:

| Prediction | Deterministic | Stochastic modification |
|-----------|--------------|------------------------|
| Unique equilibrium $(\rho^*, 0)$ | Exact fixed point | Fluctuating steady state; mean $= (\rho^*, 0)$ |
| Energy monotonicity | $d\mathcal{E}/dt \leq 0$ always | $d\mathcal{E}/dt \leq 0$ on average; positive fluctuations possible |
| Three-stage convergence | Global → algebraic → exponential | Same three stages, with noise floor in Stage III |
| Decoherence scaling $\Gamma \propto C_{\mathrm{ED}}$ | Exact proportionality | Proportionality preserved on average; fluctuations around the scaling line |
| Locked amplitude ratio | Constant ratio in quasi-steady state | Ratio fluctuates; mean preserved; variance $\propto \sigma^2$ |
| Triad selection rule | Exact ($k \in \{|m-n|, m+n\}$) | Noise populates all modes; rule holds for the *excess* above the noise floor |
| Mobility-collapse barrier | $\rho < \rho_{\max}$ always | $\rho < \rho_{\max}$ in probability (for $g = \sqrt{M}$; possible violation for $g = 1$) |

The key insight is that the noise **populates** the existing architectural structure (eigenmodes, triad channels, dissipation channels) without **creating** new structure. The selection rule remains valid for the nonlinearly generated content; the noise adds a background level in all modes. The locked ratio is maintained for the coherent (deterministic) component of the triad; the noise adds incoherent fluctuations that average to zero. The three-stage convergence proceeds to a noise floor (instead of to zero), but the three stages and their transition times remain identifiable.

##### 10.5.3.4 Noise as a Probe

Beyond testing robustness, noise can be used as a *diagnostic probe* of the architecture:

**Fluctuation spectroscopy.** The stationary variance $\operatorname{Var}(\hat{u}_k) \propto 1/D\alpha_k$ directly measures the modal decay rates without requiring a transient experiment. By measuring the noise-driven fluctuation spectrum, an experimentalist can extract the modal hierarchy from a system at steady state — which is the typical condition of physical systems in the laboratory.

**Response function.** The system's response to a sudden noise pulse (a single large $\Delta W$ at $t = 0$, followed by zero noise) traces the same relaxation trajectory as the deterministic initial-condition problem. The response function is the Green's function of the linearized operator, whose poles are the eigenvalues $\lambda_k$ — directly measurable from the response time series.

**Critical slowing down.** Near the critical surface $\Sigma$, the slowest eigenvalue approaches zero (the near-critical slowdown of Atlas §8.1). The fluctuation spectrum reflects this: the variance of the homogeneous mode diverges as $1/|\operatorname{Re}(\lambda_+)| \to \infty$ at $\Sigma$. The noise-driven fluctuation amplitude is a direct probe of the distance to the critical surface.

---

#### 10.5.4 Implementation Requirements

| Requirement | Specification |
|-------------|--------------|
| PRNG | Seeded, deterministic within environment (§7.1.2) |
| Noise parameters | $\sigma_\rho$, $\sigma_v$, $\ell$ (correlation length), $g$ (noise coefficient type) — stored in metadata |
| Random seed | Required (§7.1.2.1); recorded in `spec_hash` |
| Itô convention | Noise coefficient evaluated at pre-step density $\rho^n$ |
| Positivity enforcement | Projection (§1.7) required; frequency increases with $\sigma_\rho$ |
| Energy monotonicity | Not expected to hold per-step; checked on average (time-averaged $d\mathcal{E}/dt \leq 0$) |
| Ensemble averaging | Multiple runs at the same parameters with different seeds; statistics computed post-hoc |
| Output | Standard time-series format (§6.1) with additional fields `sigma_rho`, `sigma_v`, `noise_type` in metadata |

The stochastic extension reuses the entire deterministic engine (§§1–9) and adds only the noise injection (one array operation per step) and the PRNG infrastructure (§7.1.2). The validation tests (§8) are adapted: the per-step energy monotonicity check is relaxed to an ensemble-average check, the positivity convergence criterion accepts occasional projections (at a rate proportional to $\sigma_\rho^2$), and the decay rates are measured from ensemble-averaged time series rather than from single trajectories.

---

#### 10.5.5 Summary

| Aspect | Specification |
|--------|--------------|
| **Current status** | Deterministic only; stochastic is a planned extension |
| **Noise model 1** | Additive spatiotemporal (white or correlated); $\sigma_\rho\,dW(x,t)$ |
| **Noise model 2** | Multiplicative (state-dependent); $\sigma_\rho\,g(\rho)\,dW$; $g = \rho$ or $g = \sqrt{M}$ |
| **Noise model 3** | Participation noise; $\sigma_v\,d\eta(t)$ |
| **Preferred model** | Mobility-proportional ($g = \sqrt{M}$): respects the horizon barrier and the fluctuation-dissipation relation |
| **Equilibrium effect** | Fixed point → fluctuating steady state with $\operatorname{Var}(\hat{u}_k) \propto 1/D\alpha_k$ |
| **Architectural robustness** | Qualitative predictions survive; noise populates but does not create structure |
| **Diagnostic value** | Fluctuation spectroscopy, response functions, critical-slowing-down probes |
| **Implementation** | One array operation per step + PRNG; rest of the engine unchanged |
| **Ensemble statistics** | Multiple seeded runs; post-hoc averaging |

The stochastic extension transforms the ED simulation engine from a deterministic PDE solver into a stochastic PDE solver, opening three new avenues: robustness testing (do the architectural predictions survive noise?), physical realism (do the noisy solutions match experimental systems that are inevitably fluctuating?), and diagnostic probing (can the architecture's spectral structure be measured from the noise-driven steady state?). The extension is minimal in implementation (one additional term per step) but profound in its implications: it is the bridge between the idealized deterministic architecture of Appendix C and the noisy physical world of the Applications Paper.

---