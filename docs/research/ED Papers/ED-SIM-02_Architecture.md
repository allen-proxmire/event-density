# ED-SIM-02: The Event Density Simulation Platform (v2 Architecture)

---

# 0. Purpose and Scope

ED-SIM-02 is the second-generation simulation platform for the Event Density framework. It replaces the v1 system (ED-SIM-01), which grew organically across ED-Phys-01 through ED-Phys-35, with a unified, modular architecture aligned to the nine architectural laws and four dimensional laws established in ED-Phys-40.

The platform has four goals.

**Goal 1. Modular, extensible solver architecture for 1D–4D.** The v1 system separates 1D into `ED Simulation/` and 2D/3D into `ED Physics/ED-Phys-35_MultiDim/`, with incompatible APIs and duplicated logic. ED-SIM-02 unifies all dimensions behind a single interface while preserving dimension-specific optimisation.

**Goal 2. Implement the constitutive structure of ED-Phys-40.** The canonical PDE, mobility, penalty, and participation coupling are encoded as first-class objects with validated parameter ranges and derived-quantity computation. The nine architectural laws are verifiable through the invariant engine.

**Goal 3. Reproducible pipeline for all ED invariants.** The full invariant atlas — Lyapunov energy, ED-complexity, dissipation channels, spectral entropy, morphology fractions, Euler characteristic, and all auxiliary diagnostics — is computed through a single pipeline that produces deterministic, versioned output.

**Goal 4. Clean API, test suite, and experiment harness.** Every public function has a defined signature, every module has unit tests, and every experiment is a reproducible script that consumes the API.

ED-SIM-02 supersedes ED-SIM-01 by:

- Consolidating 1D/2D/3D/4D solvers under a single package.
- Extracting the constitutive functions, boundary conditions, and time integrators into independent modules.
- Aligning the invariant engine with the ED-Phys-40 invariant atlas.
- Adding a 4D solver (from ED-Phys-39).
- Providing a unified experiment harness with batch execution and atlas generation.

---

# I. System Overview

---

## I.1 High-Level Architecture

The ED-SIM-02 platform is composed of nine modules arranged in three tiers: core computation, analysis, and orchestration.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     ORCHESTRATION TIER                              │
│                                                                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │   Experiment      │  │  Reproducibility  │  │    CLI / API     │  │
│  │   Harness         │  │  Suite            │  │    Interface     │  │
│  └───────┬──────────┘  └───────┬──────────┘  └───────┬──────────┘  │
├──────────┼─────────────────────┼─────────────────────┼──────────────┤
│          │        ANALYSIS TIER                      │              │
│          │                                           │              │
│  ┌───────▼──────────┐  ┌──────────────────┐  ┌──────▼───────────┐  │
│  │   Invariant       │  │   Visualization   │  │    Export /      │  │
│  │   Engine          │  │   Engine          │  │    Serialization │  │
│  └───────┬──────────┘  └───────┬──────────┘  └───────┬──────────┘  │
├──────────┼─────────────────────┼─────────────────────┼──────────────┤
│          │         CORE TIER                         │              │
│          │                                           │              │
│  ┌───────▼──────────┐  ┌──────────────────┐  ┌──────▼───────────┐  │
│  │   Operator        │  │   Time            │  │   Boundary       │  │
│  │   Module          │  │   Integrator      │  │   Module         │  │
│  │                   │  │                   │  │                   │  │
│  │ ┌───────────────┐ │  │ ┌───────────────┐ │  │ ┌───────────────┐ │  │
│  │ │ Constitutive  │ │  │ │ ETD-RK4       │ │  │ │ Neumann       │ │  │
│  │ │ Functions     │ │  │ │ Crank-Nicolson│ │  │ │ Periodic      │ │  │
│  │ │ (M, P, v)    │ │  │ │ Implicit Euler│ │  │ │ Dirichlet     │ │  │
│  │ └───────────────┘ │  │ └───────────────┘ │  │ └───────────────┘ │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    Participation Module                       │   │
│  │              v(t) dynamics, global coupling                   │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**Core Tier.** The operator module computes $F[\rho]$ for any dimension $d \in \{1,2,3,4\}$. The time integrator advances $\rho$ and $v$ forward. The boundary module enforces spatial boundary conditions. The participation module evolves the global variable $v(t)$. The constitutive functions ($M$, $M'$, $P$) are injected into the operator module as callable objects.

**Analysis Tier.** The invariant engine computes the full ED invariant atlas from a solver state. The visualization engine renders fields, spectra, morphology, and diagnostics. The export module serialises results to JSON, NPZ, and HDF5.

**Orchestration Tier.** The experiment harness defines and runs simulation scenarios. The reproducibility suite runs the full pipeline and generates consistency certificates. The CLI/API interface provides programmatic and command-line access.

Data flows downward (orchestration calls analysis calls core) and results flow upward (core returns states, analysis returns invariants, orchestration returns reports).

---

## I.2 Design Principles

Six principles govern the ED-SIM-02 architecture.

**Modularity.** Each module has a single responsibility and a defined interface. The operator module does not know about time integration. The time integrator does not know about invariants. Modules communicate through typed state dictionaries, not global variables.

**Extensibility.** New dimensions ($d = 5, 6, \ldots$), new constitutive functions, new time integrators, and new invariants can be added without modifying existing code. Extension points are defined by abstract interfaces (Python protocols) rather than concrete inheritance.

**Dimensional generality.** A single API serves $d = 1$ through $d = 4$. Dimension-specific optimisations (1D tridiagonal solvers, 2D/3D ADI splitting, 4D tensor-product transforms) are encapsulated inside the operator and integrator modules. The user-facing API is dimension-agnostic: `run_simulation(params, ic)` works for any $d$.

**Deterministic reproducibility.** Every simulation is fully determined by its parameter set and initial condition. Random seeds are explicit. Floating-point operations use a fixed order of evaluation. Output files include a metadata block with the full parameter set, software version, and platform information.

**Separation of concerns.** Physics (constitutive functions, PDE structure) is separated from numerics (discretisation, time stepping) which is separated from analysis (invariants, visualisation) which is separated from orchestration (experiments, reproducibility). No layer reaches into another's internals.

**Zero hidden state.** No module maintains mutable state between calls except through explicitly passed state dictionaries. The spectral precomputation (`SpectralState`) is immutable after construction. The solver is a pure function: `state_new = step(state_old, params)`.

---

## I.3 Folder Structure

```
edsim/                              # Top-level package
├── __init__.py                     # Package metadata, version
├── core/                           # Core tier
│   ├── __init__.py
│   ├── parameters.py               # EDParameters (all dimensions)
│   ├── constitutive.py             # M(rho), M'(rho), P(rho), Phi(rho)
│   ├── operators.py                # F[rho] computation (1D–4D)
│   ├── participation.py            # v(t) dynamics
│   ├── boundary.py                 # BC enforcement (Neumann, periodic, Dirichlet)
│   ├── integrators/
│   │   ├── __init__.py
│   │   ├── etdrk4.py              # Spectral ETD-RK4 (1D–4D)
│   │   ├── crank_nicolson.py      # FD Crank-Nicolson / ADI (1D–4D)
│   │   ├── implicit_euler.py      # FD Implicit Euler (1D–4D)
│   │   └── base.py                # Integrator protocol
│   └── spectral.py                # SpectralState, DCT/DFT utilities
│
├── invariants/                     # Analysis tier: invariant engine
│   ├── __init__.py
│   ├── energy.py                   # Lyapunov functional, mass, complexity
│   ├── spectral.py                 # Spectral entropy, modal hierarchy
│   ├── dissipation.py              # Dissipation channels, R_grad
│   ├── morphology.py               # Hessian eigenvalues, morphology fractions
│   ├── topology.py                 # Euler characteristic, Betti numbers
│   ├── correlation.py              # Correlation lengths, structure functions
│   └── atlas.py                    # Full invariant atlas computation
│
├── visualization/                  # Analysis tier: visualization
│   ├── __init__.py
│   ├── fields.py                   # Heatmaps, contours, slices, isosurfaces
│   ├── spectra.py                  # Power spectra, radial spectra, anisotropy
│   ├── geometry.py                 # Hessian maps, curvature, morphology
│   ├── horizons.py                 # Horizon masks, proximity fields
│   ├── time_series.py              # Invariant evolution plots
│   └── style.py                    # ED-SIM style conventions
│
├── io/                             # Analysis tier: serialization
│   ├── __init__.py
│   ├── export.py                   # JSON, NPZ, HDF5 export
│   ├── metadata.py                 # Run metadata generation
│   └── checkpoints.py             # Checkpoint save/load
│
├── experiments/                    # Orchestration tier
│   ├── __init__.py
│   ├── scenarios.py                # Scenario definitions (A–D per dimension)
│   ├── sweeps.py                   # Parameter sweeps
│   ├── atlas.py                    # Atlas generation
│   └── runner.py                   # RunConfig, TimeSeries, run_simulation()
│
├── reproducibility/                # Orchestration tier
│   ├── __init__.py
│   ├── pipeline.py                 # Full reproducibility pipeline
│   ├── certificate.py              # Consistency certificate generation
│   └── run_all.py                  # Entry point
│
└── tests/                          # Test suite
    ├── test_parameters.py
    ├── test_constitutive.py
    ├── test_operators.py
    ├── test_integrators.py
    ├── test_boundary.py
    ├── test_invariants.py
    ├── test_morphology.py
    ├── test_topology.py
    ├── test_roundtrip.py           # Serialize → deserialize identity
    ├── test_dimensional_laws.py    # Nine laws verification
    └── conftest.py                 # Shared fixtures
```

The `edsim/` package is self-contained. It has no external dependencies beyond NumPy, SciPy, and Matplotlib. Optional dependencies (scikit-image for isosurfaces, h5py for HDF5) are imported lazily.

---

# II. Core Modules

---

## II.1 Parameters

The `EDParameters` dataclass holds the complete specification of an ED simulation.

```python
@dataclass(frozen=True)
class EDParameters:
    # Dimension
    d: int                          # Spatial dimension (1, 2, 3, 4)

    # Domain
    L: tuple[float, ...]            # Domain size per axis (length d)
    N: tuple[int, ...]              # Grid points per axis (length d)

    # Constitutive
    D: float = 0.3                  # Diffusion weight
    H: float = 0.15                 # Participation coupling
    zeta: float = 0.1               # Participation damping
    tau: float = 1.0                # Participation timescale
    rho_star: float = 0.5           # Penalty equilibrium
    rho_max: float = 1.0            # Capacity bound
    M0: float = 1.0                 # Mobility prefactor
    beta: float = 2.0               # Mobility exponent
    P0: float = 1.0                 # Penalty slope

    # Numerical
    dt: float = 1e-4                # Time step
    T: float = 1.0                  # Final time
    method: str = "etdrk4"          # Integrator: etdrk4, crank_nicolson, implicit_euler
    bc: str = "neumann"             # Boundary: neumann, periodic, dirichlet
    k_out: int = 100                # Output every k_out steps

    # Reproducibility
    seed: int = 42                  # RNG seed for stochastic ICs
```

Key design decisions:

- **Frozen.** Parameters are immutable after construction. This prevents accidental mutation during a run and enables hashing for cache keys.
- **Tuple axes.** Domain size `L` and grid count `N` are tuples of length `d`, supporting anisotropic grids.
- **Defaults.** All constitutive parameters default to the canonical values from ED-Phys-40.
- **Validation.** A `__post_init__` method checks `d in {1,2,3,4}`, `len(L) == len(N) == d`, `0 < rho_star < rho_max`, `beta > 0`, `M0 > 0`, `P0 > 0`, `dt > 0`.

Derived quantities are computed as cached properties:

```python
@property
def M_star(self) -> float:
    return self.M0 * (self.rho_max - self.rho_star) ** self.beta

@property
def R_grad_predicted(self) -> float:
    return self.d * np.pi**2 / (self.d * np.pi**2 + self.P0**2 / self.M_star)

@property
def total_grid_points(self) -> int:
    return int(np.prod(self.N))
```

---

## II.2 Constitutive Functions

The constitutive module provides the mobility, penalty, and density potential as standalone functions.

```python
def mobility(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """M(rho) = M0 * (rho_max - rho)^beta. Clipped to [0, inf)."""

def mobility_deriv(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """M'(rho) = -beta * M0 * (rho_max - rho)^(beta-1)."""

def penalty(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """P(rho) = P0 * (rho - rho_star)."""

def density_potential(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Phi(rho) = integral of P(s)/M(s) ds from rho_star to rho."""
```

Each function is vectorised over NumPy arrays of any shape. The functions are pure: they read from `params` and return new arrays without side effects. Custom constitutive functions can be injected by subclassing `EDParameters` and overriding a `constitutive` attribute, but the default implementation covers all cases in the ED-Phys series.

---

## II.3 Operator Module

The operator module computes $F[\rho] = \nabla\!\cdot\!(M(\rho)\nabla\rho) - P(\rho)$ for any dimension. It provides two implementations: finite-difference (FD) and spectral (DCT/DFT).

### FD Implementation

```python
def laplacian_fd(rho: np.ndarray, dx: tuple, bc: str) -> np.ndarray:
    """d-dimensional Laplacian using 2nd-order central differences.
    Dispatches to optimised 1D/2D/3D/4D kernels by rho.ndim."""

def grad_squared_fd(rho: np.ndarray, dx: tuple, bc: str) -> np.ndarray:
    """|nabla rho|^2 using 2nd-order central differences."""

def operator_F_fd(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """F[rho] = M(rho)*laplacian + M'(rho)*|grad|^2 - P(rho). FD version."""
```

The FD stencils are:

| Dimension | Laplacian stencil | Points | Ghost cells |
|-----------|------------------|--------|-------------|
| 1D | 3-point | $[-1, 2, -1]/dx^2$ | 1 per side |
| 2D | 5-point | Cross stencil | 1 per side per axis |
| 3D | 7-point | Cross stencil | 1 per side per axis |
| 4D | 9-point | Cross stencil | 1 per side per axis |

Boundary conditions are enforced through ghost cells (Neumann: mirror; periodic: wrap; Dirichlet: fixed value). The ghost cells are filled before each operator evaluation and discarded afterward.

### Spectral Implementation

```python
def laplacian_spectral(rho_hat: np.ndarray, eigenvalues: np.ndarray) -> np.ndarray:
    """Spectral Laplacian: multiply by -mu_k in transform space."""

def operator_F_spectral(rho: np.ndarray, rho_hat: np.ndarray,
                         params: EDParameters, sstate: SpectralState) -> np.ndarray:
    """F[rho] via hybrid spectral/physical: linear terms in spectral,
    nonlinear terms in physical space."""
```

The spectral method uses the Type-I DCT for Neumann boundaries and the DFT for periodic boundaries. The Laplacian is diagonal in the transform basis: $\widehat{\nabla^2\rho}_\mathbf{k} = -\mu_\mathbf{k}\,\hat{\rho}_\mathbf{k}$. Nonlinear terms ($M(\rho)\nabla^2\rho$, $M'(\rho)|\nabla\rho|^2$) are computed in physical space and transformed back.

---

## II.4 Participation Module

The participation variable $v(t)$ evolves according to

$$\dot{v} = \frac{1}{\tau}(\bar{F} - \zeta\,v),$$

where $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^d\!x$.

```python
def advance_v(v: float, F_avg: float, params: EDParameters) -> float:
    """One-step exact integration of the participation ODE.
    Uses the exact solution: v(t+dt) = v(t)*exp(-zeta*dt/tau) + (F_avg/zeta)*(1 - exp(-zeta*dt/tau))."""

def spatial_average(F: np.ndarray, dx: tuple) -> float:
    """Domain-averaged operator: sum(F * prod(dx)) / prod(L)."""
```

The participation ODE is integrated exactly (exponential decay plus constant forcing) at each time step, avoiding the need for a separate ODE integrator.

---

## II.5 Boundary Module

```python
def apply_bc(rho: np.ndarray, bc: str, d: int) -> np.ndarray:
    """Apply boundary conditions by filling ghost cells.

    bc = "neumann":  mirror reflection at boundaries.
    bc = "periodic": wrap-around at boundaries.
    bc = "dirichlet": fixed value (rho_star) at boundaries.
    """

def strip_ghost(rho: np.ndarray, d: int) -> np.ndarray:
    """Remove ghost cells from a padded array."""
```

Ghost cells are the universal boundary mechanism. The operator module always works on padded arrays; the boundary module fills the padding before each evaluation. This keeps boundary logic out of the operator stencils.

---

## II.6 Time Integrators

All integrators implement a common protocol:

```python
class Integrator(Protocol):
    def step(self, rho: np.ndarray, v: float, t: float,
             params: EDParameters, state: Any) -> tuple[np.ndarray, float, Any]:
        """Advance (rho, v) by one time step dt.
        Returns (rho_new, v_new, state_new)."""
```

### ETD-RK4 (Spectral)

The primary integrator. The linear part $L = D\,M^*\nabla^2 - D\,P_0$ is integrated exactly using matrix exponentials computed from the Laplacian eigenvalues. The nonlinear remainder $N[\rho] = D\,(M(\rho) - M^*)\nabla^2\rho + D\,M'(\rho)|\nabla\rho|^2 - D\,(P(\rho) - P_0\rho) + H\,v$ is integrated with a four-stage explicit Runge-Kutta scheme in the exponential-time-differencing framework.

Precomputed quantities (stored in `SpectralState`):

| Quantity | Symbol | Shape |
|----------|--------|-------|
| Eigenvalues | $\mu_\mathbf{k}$ | $(N_1, \ldots, N_d)$ |
| Linear operator | $\lambda_\mathbf{k} = -D(M^*\mu_\mathbf{k} + P_0)$ | $(N_1, \ldots, N_d)$ |
| $e^{\lambda\,dt}$ | `E` | $(N_1, \ldots, N_d)$ |
| $e^{\lambda\,dt/2}$ | `E2` | $(N_1, \ldots, N_d)$ |
| ETD coefficients | `f1, f2, f3` | $(N_1, \ldots, N_d)$ |

The ETD coefficients are computed via contour integrals (Kassam-Trefethen) to avoid numerical cancellation near $\lambda = 0$.

### Crank-Nicolson / ADI (FD)

The secondary integrator. In 1D, Crank-Nicolson produces a tridiagonal system solved by Thomas' algorithm. In 2D/3D/4D, the alternating-direction implicit (ADI) splitting decomposes the $d$-dimensional implicit step into $d$ sequential 1D tridiagonal solves, one per axis.

Each ADI sub-step:

$$\frac{\rho^{n+1/d,i} - \rho^{n+(i-1)/d}}{\Delta t/d} = \frac{1}{2}\bigl(L_i[\rho^{n+1/d,i}] + L_i[\rho^{n+(i-1)/d}]\bigr) + N_{\mathrm{explicit}},$$

where $L_i$ is the diffusion operator along axis $i$ and $N_{\mathrm{explicit}}$ collects the nonlinear terms evaluated at the previous sub-step.

### Implicit Euler (FD)

A fallback integrator for stiff regimes. Fully implicit, first-order in time, unconditionally stable. Uses Newton iteration for the nonlinear system at each step. Expensive but robust.

---

## II.7 Spectral Utilities

The `SpectralState` class precomputes all dimension-specific spectral data at construction time.

```python
@dataclass(frozen=True)
class SpectralState:
    d: int                          # Dimension
    N: tuple[int, ...]              # Grid points per axis
    eigenvalues: np.ndarray         # mu_k array, shape N
    linear_op: np.ndarray           # lambda_k = -D*(M_star*mu_k + P0)
    E: np.ndarray                   # exp(lambda*dt)
    E2: np.ndarray                  # exp(lambda*dt/2)
    f1: np.ndarray                  # ETD coefficient 1
    f2: np.ndarray                  # ETD coefficient 2
    f3: np.ndarray                  # ETD coefficient 3
```

Transform functions:

```python
def forward_transform(rho: np.ndarray, bc: str) -> np.ndarray:
    """DCT-I (Neumann) or FFT (periodic), d-dimensional."""

def inverse_transform(rho_hat: np.ndarray, bc: str) -> np.ndarray:
    """Inverse DCT-I or IFFT, d-dimensional."""
```

The transforms use `scipy.fft.dctn` / `scipy.fft.idctn` (type I, orthonormal) for Neumann boundaries and `numpy.fft.fftn` / `numpy.fft.ifftn` for periodic boundaries. All transforms operate along all $d$ axes simultaneously.

---

# III. Invariant Engine

---

## III.1 Architecture

The invariant engine computes the full ED invariant atlas from a solver state. It is organised by invariant family, with each family implemented as a standalone module.

```
compute_atlas(rho, v, params) -> dict
    ├── compute_energy(rho, params)         -> {E, mass, complexity}
    ├── compute_spectral(rho, params)       -> {entropy, modal_hierarchy, anisotropy}
    ├── compute_dissipation(rho, v, params) -> {R_grad, R_pen, R_part, total_rate}
    ├── compute_morphology(rho, params)     -> {fractions, dominant_type, eigenvalue_stats}
    ├── compute_topology(rho, params)       -> {chi, betti_numbers}
    └── compute_correlation(rho, params)    -> {xi, structure_functions}
```

Each `compute_*` function accepts a density array `rho` (of shape `N`), optionally the participation variable `v`, and the parameter set `params`. Each returns a dictionary of named invariants. The top-level `compute_atlas` calls all families and merges the results.

---

## III.2 Energy Invariants

```python
def lyapunov_energy(rho: np.ndarray, params: EDParameters) -> float:
    """E[rho] = integral of Phi(rho) over Omega."""

def total_mass(rho: np.ndarray, dx: tuple) -> float:
    """M = integral of rho over Omega."""

def ed_complexity(rho: np.ndarray, dx: tuple) -> float:
    """C = integral of |grad rho|^2 over Omega."""
```

The energy and mass are integrated using the composite trapezoidal rule (exact for the Neumann eigenbasis). The complexity uses central-difference gradients.

---

## III.3 Spectral Invariants

```python
def spectral_entropy(rho: np.ndarray, params: EDParameters) -> float:
    """H = -sum(p_k * ln(p_k)) where p_k = |rho_hat_k|^2 / sum."""

def modal_hierarchy(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Sorted modal amplitudes |rho_hat_k|, descending."""

def spectral_anisotropy(rho: np.ndarray, params: EDParameters) -> dict:
    """Inertia tensor of the power spectrum. Returns eigenvalues and eigenvectors."""

def radial_spectrum(rho: np.ndarray, params: EDParameters) -> tuple[np.ndarray, np.ndarray]:
    """Radially averaged power spectrum P(k) vs k."""
```

All spectral invariants operate on the DCT/DFT transform of $\rho$. The spectral anisotropy is the inertia tensor $I_{ij} = \sum_\mathbf{k} k_i k_j |\hat{\rho}_\mathbf{k}|^2 / \sum_\mathbf{k} |\hat{\rho}_\mathbf{k}|^2$, whose eigenvalues measure directional energy concentration (sphere = isotropic, ellipsoid = anisotropic).

---

## III.4 Dissipation Invariants

```python
def dissipation_channels(rho: np.ndarray, v: float, params: EDParameters) -> dict:
    """Decompose dE/dt into gradient, penalty, and participation channels.
    Returns {R_grad, R_pen, R_part, total_rate}."""
```

The decomposition follows ED-Phys-40:

$$R_{\mathrm{grad}} = \frac{\int M|\nabla\rho|^2\,d^d\!x}{\int M|\nabla\rho|^2\,d^d\!x + \int P^2/M\,d^d\!x + |H\,v\,\bar{\Phi'}|},$$

with analogous expressions for $R_{\mathrm{pen}}$ and $R_{\mathrm{part}}$. All integrals are computed numerically using the composite trapezoidal rule.

---

## III.5 Morphology Invariants

```python
def hessian_eigenvalues(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute Hessian eigenvalues at each grid point.
    Returns array of shape (*N, d), sorted descending."""

def morphology_fractions(eigenvalues: np.ndarray) -> dict:
    """Classify each point into morphological type and return volume fractions.
    Types: blob (d=1), {sheet, blob} (d=2), {filament, sheet, blob} (d=3),
    {filament, sheet, pancake, blob} (d=4)."""
```

The Hessian $\partial^2\rho/\partial x_i\partial x_j$ is computed using central differences. The eigenvalues are obtained via `numpy.linalg.eigvalsh` (symmetric eigenvalue decomposition) at each grid point. Classification follows the ED-Phys-35/39 definitions based on eigenvalue ratios.

---

## III.6 Topology Invariants

```python
def euler_characteristic(rho: np.ndarray, threshold: float, dx: tuple) -> int:
    """Euler characteristic of the excursion set {rho >= threshold}.
    Uses cubical complex computation for d <= 3, voxel-based for d = 4."""

def betti_numbers(rho: np.ndarray, threshold: float, dx: tuple) -> list[int]:
    """Betti numbers beta_0, ..., beta_{d-1} of the excursion set.
    Requires optional dependency: gudhi or dionysus."""
```

For $d \leq 3$, the Euler characteristic is computed directly from the binary mask using the cubical-complex formula. For $d = 4$, a voxel-counting approach computes $\chi = V - E + F - C + H$ (vertices minus edges plus faces minus cubes plus hypercubes). The full Betti number computation requires a persistent homology library (optional dependency).

---

## III.7 Correlation Invariants

```python
def correlation_length(rho: np.ndarray, params: EDParameters) -> float:
    """Correlation length xi = sqrt(sum(r^2 * C(r)) / sum(C(r))),
    where C(r) is the radially averaged autocorrelation."""

def structure_function(rho: np.ndarray, p: int, dx: tuple) -> tuple[np.ndarray, np.ndarray]:
    """p-th order structure function S_p(r) = <|rho(x+r) - rho(x)|^p>."""
```

The autocorrelation is computed via the Wiener-Khinchin theorem (inverse transform of the power spectrum). The structure functions are computed by direct spatial averaging over separation vectors.

---

# IV. Visualization Engine

---

## IV.1 Field Visualizations

| Function | Dimensions | Output |
|----------|-----------|--------|
| `plot_field_1d(rho, params)` | 1D | Line plot of $\rho(x)$ |
| `plot_field_heatmap(rho, params)` | 2D | Colour heatmap of $\rho(x,y)$ |
| `plot_field_contour(rho, params)` | 2D | Contour lines with level labels |
| `plot_field_quiver(rho, params)` | 2D | Quiver plot of $\nabla\rho$ |
| `plot_field_slices(rho, params)` | 3D, 4D | Orthogonal slice triplet/quartet |
| `plot_field_isosurface(rho, params, level)` | 3D | Marching-cubes isosurface |

All field visualizations accept a `fig_kw` dictionary for figure size, DPI, and colourmap customisation. The default colourmap is `viridis` for density and `RdBu_r` for signed quantities.

## IV.2 Spectral Visualizations

| Function | Dimensions | Output |
|----------|-----------|--------|
| `plot_spectrum_1d(rho, params)` | 1D | Log-log amplitude spectrum |
| `plot_spectrum_2d(rho, params)` | 2D | 2D amplitude map + radial profile |
| `plot_spectrum_radial(rho, params)` | All | Radially averaged $P(k)$ vs $k$ |
| `plot_anisotropy_ellipse(rho, params)` | 2D | Inertia-tensor ellipse |
| `plot_anisotropy_ellipsoid(rho, params)` | 3D, 4D | Inertia-tensor ellipsoid (3D projection) |

## IV.3 Diagnostic Visualizations

| Function | Input | Output |
|----------|-------|--------|
| `plot_invariants(series, params)` | TimeSeries | Multi-panel time evolution (energy, mass, complexity, entropy, $R_{\mathrm{grad}}$) |
| `plot_morphology_evolution(series, params)` | TimeSeries | Stacked area plot of morphology fractions vs time |
| `plot_dissipation_partition(series, params)` | TimeSeries | $R_{\mathrm{grad}}, R_{\mathrm{pen}}, R_{\mathrm{part}}$ vs time |

---

# V. Experiment Harness

---

## V.1 RunConfig and TimeSeries

```python
@dataclass
class RunConfig:
    params: EDParameters
    ic_type: str                    # "cosine", "random", "gaussian", "custom"
    ic_kwargs: dict                 # IC-specific arguments (A, Nm, sigma, etc.)
    output_dir: str                 # Output directory
    save_checkpoints: bool = True
    checkpoint_interval: int = 1000

@dataclass
class TimeSeries:
    times: list[float]
    states: list[np.ndarray]        # rho snapshots
    v_history: list[float]
    invariants: list[dict]          # atlas at each output step
```

## V.2 Unified Run Interface

```python
def run_simulation(config: RunConfig) -> TimeSeries:
    """Execute a single ED simulation.

    1. Construct grid and initial condition from config.
    2. Initialise integrator (spectral or FD based on config.params.method).
    3. Time-step loop:
       a. Advance (rho, v) by one dt.
       b. Enforce bounds [0, rho_max].
       c. Every k_out steps: compute atlas, store snapshot.
    4. Return TimeSeries.
    """
```

The function is dimension-agnostic. The dimension is read from `config.params.d` and dispatched internally. The user never writes dimension-specific code.

## V.3 Batch and Sweep Interface

```python
def run_batch(configs: list[RunConfig], parallel: bool = True) -> list[TimeSeries]:
    """Run multiple simulations. If parallel=True, use multiprocessing."""

def run_sweep(base_params: EDParameters, sweep_param: str,
              sweep_values: list, ic_type: str, ic_kwargs: dict) -> list[TimeSeries]:
    """Parameter sweep: vary one parameter, hold others fixed."""
```

## V.4 Predefined Scenarios

Each dimension has a standard set of test scenarios:

| Scenario | Description | Key parameters |
|----------|-------------|----------------|
| **A** (Relaxation) | Isotropic cosine IC, moderate amplitude | $A = 0.03$, $N_m = 2$ |
| **B** (Filament) | Anisotropic IC favouring one axis | $A_x = 0.05$, $A_y = 0.01$ |
| **C** (Collapse) | High amplitude, near-capacity | $A = 0.08$, $N_m = 3$ |
| **D** (Horizon) | IC tuned for horizon formation | $A = 0.15$, $N_m = 2$ |

Each scenario is a function returning a `RunConfig`:

```python
def scenario_A(d: int, N: int = 64) -> RunConfig: ...
def scenario_B(d: int, N: int = 64) -> RunConfig: ...
def scenario_C(d: int, N: int = 64) -> RunConfig: ...
def scenario_D(d: int, N: int = 64) -> RunConfig: ...
```

## V.5 Atlas Generation

```python
def run_atlas(d: int, N: int = 64,
              D_values: list = [0.1, 0.3, 0.5],
              A_values: list = [0.01, 0.03, 0.05],
              Nm_values: list = [2, 3, 4]) -> dict:
    """Full invariant atlas: sweep (D, A, Nm), compute all invariants,
    return structured results dict."""
```

The atlas generation replicates the ED-Phys-35 atlas pipeline in a single function call.

---

# VI. Reproducibility Suite

---

## VI.1 Pipeline

The reproducibility pipeline executes a sequence of phases that verify the entire ED-SIM-02 system.

```
Phase 1: Environment check
    - Python version, NumPy/SciPy versions, platform info
    - Write environment.json

Phase 2: Parameter validation
    - Verify canonical parameters produce expected derived quantities
    - Verify R_grad formula matches numerical computation

Phase 3: Solver validation (per dimension)
    - Spatial convergence (N = 32, 64, 128)
    - Temporal convergence (dt halving)
    - Mass conservation (machine precision)
    - Energy monotonicity
    - Bounds preservation

Phase 4: Integrator cross-validation
    - ETD-RK4 vs Crank-Nicolson agreement (L2 < 1e-4)
    - ETD-RK4 vs Implicit Euler agreement (L2 < 1e-3)

Phase 5: Invariant validation
    - Known-field tests (constant, cosine, Gaussian)
    - Cross-dimension regression (2D y-invariant == 1D)

Phase 6: Dimensional law verification
    - Factorial complexity: C^(d)/C^(1) vs 1/d! for d = 1,2,3
    - Gradient dominance: R_grad vs formula for d = 1,2,3
    - Topological conservation: chi(t) = const for d = 1,2,3

Phase 7: Atlas generation
    - Run standard scenarios A-D for d = 1,2,3
    - Compute full invariant atlas

Phase 8: Consistency certificate
    - Hash all output files
    - Compare to reference hashes (if available)
    - Write certificate.json

Phase 9: Summary
    - Generate human-readable report
    - List any failures or warnings
```

## VI.2 Consistency Certificate

```python
@dataclass
class Certificate:
    timestamp: str
    platform: str
    python_version: str
    numpy_version: str
    scipy_version: str
    edsim_version: str
    phases_passed: list[int]
    phases_failed: list[int]
    output_hashes: dict[str, str]   # filename -> SHA256
    warnings: list[str]
```

The certificate is a JSON file that uniquely identifies a reproducibility run. Two runs on different machines with identical parameters should produce identical certificates (up to platform-dependent floating-point rounding, which is tracked in the warnings).

## VI.3 Entry Point

```bash
python -m edsim.reproducibility.run_all [--quick] [--dimensions 1 2 3] [--output-dir ./results]
```

The `--quick` flag skips convergence studies and atlas generation, running only the validation phases. The `--dimensions` flag selects which dimensions to validate.

---

# VII. Testing Strategy

---

## VII.1 Test Categories

| Category | Module | Tests |
|----------|--------|-------|
| **Unit** | `test_parameters.py` | Parameter validation, derived quantities, immutability |
| **Unit** | `test_constitutive.py` | $M$, $M'$, $P$ values at known points; edge cases ($\rho = 0$, $\rho_{\max}$) |
| **Unit** | `test_operators.py` | Laplacian of known functions (cosines); $F[\rho^*] = 0$; FD vs spectral agreement |
| **Unit** | `test_boundary.py` | Ghost-cell symmetry (Neumann); wraparound (periodic); fixed values (Dirichlet) |
| **Integration** | `test_integrators.py` | ETD-RK4 vs CN on the same IC; convergence order; mass/energy conservation |
| **Integration** | `test_invariants.py` | Known-field invariants (constant → $C = 0$, $H = 0$); cross-dimension consistency |
| **Integration** | `test_morphology.py` | Sphere → blob; plane → sheet; line → filament |
| **Integration** | `test_topology.py` | $\chi$ of known shapes (sphere, torus); $d\chi/dt = 0$ over short runs |
| **Regression** | `test_roundtrip.py` | Serialize → deserialize → compare to original |
| **Science** | `test_dimensional_laws.py` | Nine laws at $d = 1, 2, 3$ within specified tolerances |

## VII.2 Test Infrastructure

Tests use `pytest` with fixtures defined in `conftest.py`:

```python
@pytest.fixture(params=[1, 2, 3])
def params_small(request):
    """Small-grid EDParameters for fast testing."""
    d = request.param
    N = (16,) * d
    L = (1.0,) * d
    return EDParameters(d=d, N=N, L=L, dt=1e-3, T=0.01)

@pytest.fixture
def cosine_ic(params_small):
    """Standard cosine initial condition on the test grid."""
    ...
```

The `params=[1, 2, 3]` parametrisation ensures every test runs in all dimensions automatically. The 4D tests are gated behind a `--include-4d` flag to keep the default test suite fast.

## VII.3 Performance Benchmarks

| Benchmark | Metric | Target |
|-----------|--------|--------|
| 2D step (ETD-RK4, $N = 128$) | Wall time per step | $< 5$ ms |
| 3D step (ETD-RK4, $N = 64$) | Wall time per step | $< 50$ ms |
| 4D step (ETD-RK4, $N = 32$) | Wall time per step | $< 200$ ms |
| Full atlas ($d = 2$, 27 runs) | Total wall time | $< 10$ min |
| Invariant computation ($d = 3$, $N = 64$) | Per-snapshot | $< 1$ s |

Benchmarks are tracked by the CI suite (if configured) but are not hard test failures.

---

# VIII. Migration from v1

---

## VIII.1 Mapping v1 Modules to v2

| v1 Location | v1 Module | v2 Location |
|-------------|-----------|-------------|
| `ED Simulation/edsim_core.py` | 1D solver | `edsim/core/operators.py` + `edsim/core/integrators/` |
| `ED Simulation/edsim_parameters.py` | 1D parameters | `edsim/core/parameters.py` |
| `ED Simulation/edsim_diagnostics.py` | 1D diagnostics | `edsim/invariants/` |
| `ED Simulation/edsim_runner.py` | 1D runner | `edsim/experiments/runner.py` |
| `ED-Phys-35/edsim_solver_2d.py` | 2D solver | `edsim/core/operators.py` + `edsim/core/integrators/` |
| `ED-Phys-35/edsim_solver_3d.py` | 3D solver | `edsim/core/operators.py` + `edsim/core/integrators/` |
| `ED-Phys-35/invariants_2d.py` | 2D invariants | `edsim/invariants/` |
| `ED-Phys-35/invariants_3d.py` | 3D invariants | `edsim/invariants/` |
| `ED-Phys-35/visualization_2d.py` | 2D plots | `edsim/visualization/` |
| `ED-Phys-35/visualization_3d.py` | 3D plots | `edsim/visualization/` |
| `ED-Phys-35/edsim2d/` | 2D package | `edsim/experiments/` |
| `ED Simulation/reproducibility/` | 1D repro | `edsim/reproducibility/` |
| `ED-Phys-35/reproducibility/` | 2D/3D repro | `edsim/reproducibility/` |

## VIII.2 Breaking Changes

| v1 API | v2 API | Reason |
|--------|--------|--------|
| `EDParameters2D`, `EDParameters3D` | `EDParameters(d=2)`, `EDParameters(d=3)` | Unified parameter class |
| `step_etdrk4_2d(rho, v, ...)` | `integrator.step(rho, v, ...)` | Protocol-based dispatch |
| `run_simulation_2d(params, ...)` | `run_simulation(config)` | Unified run interface |
| `compute_invariants_2d(state)` | `compute_atlas(rho, v, params)` | Unified invariant API |

## VIII.3 Backward Compatibility

The v1 modules remain in their original locations and are not modified. The v2 package `edsim/` is a new, independent package that can coexist with the v1 files. A thin compatibility layer in `edsim/compat/` provides v1-style function signatures that delegate to v2 internals:

```python
# edsim/compat/v1.py
from edsim.experiments.runner import run_simulation

def run_simulation_2d(params, ic, **kwargs):
    """v1-compatible wrapper."""
    config = _convert_v1_params_to_config(params, ic, d=2, **kwargs)
    return run_simulation(config)
```

---

# IX. Closing Summary

ED-SIM-02 provides a unified simulation platform for the Event Density framework across dimensions $d = 1$ through $d = 4$. The architecture is organised in three tiers (core, analysis, orchestration) with nine modules connected by typed interfaces and a zero-hidden-state discipline.

The core tier implements the canonical ED PDE with pluggable constitutive functions, three time integrators (ETD-RK4, Crank-Nicolson/ADI, implicit Euler), and three boundary condition types (Neumann, periodic, Dirichlet). The analysis tier computes the full invariant atlas (energy, spectral, dissipation, morphology, topology, correlation) and renders visualisations. The orchestration tier provides a unified run interface, batch execution, parameter sweeps, atlas generation, and a nine-phase reproducibility pipeline with consistency certificates.

The platform is:

- **Dimension-general:** a single API serves $d = 1, 2, 3, 4$.
- **Modular:** each module has a single responsibility and a defined interface.
- **Reproducible:** every run is fully specified by its `RunConfig` and verified by the reproducibility suite.
- **Extensible:** new dimensions, constitutive functions, integrators, and invariants can be added without modifying existing code.
- **Testable:** every module has unit tests; every law has a science test.

ED-SIM-02 is the implementation counterpart to ED-Phys-40. Where ED-Phys-40 defines the architecture of Event Density as a mathematical theory, ED-SIM-02 defines it as a computational platform.
