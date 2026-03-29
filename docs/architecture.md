# Architecture

ED-SIM-02 is organised in five layers, each with a single responsibility. Data flows downward (orchestration calls analysis calls core) and results flow upward.

---

## Layers

### 1. Core Numerics (`edsim/core/`)

The bottom layer. Contains everything needed to advance the density field rho and participation variable v by one time step.

| Module | Responsibility |
|--------|---------------|
| `parameters.py` | `EDParameters` frozen dataclass. Single source of truth for all physical and numerical settings. |
| `constitutive.py` | Mobility M(rho), penalty P(rho), enforce_bounds. Pure functions, no state. |
| `operators.py` | FD Laplacian, gradient-squared, and the full density operator F[rho] for 2D/3D/4D. Dimension-specific stencils dispatch automatically. |
| `boundary.py` | Ghost-cell padding and stripping for Neumann, periodic, and Dirichlet BCs. |
| `spectral.py` | SpectralState (precomputed eigenvalues and ETD coefficients), DCT forward/inverse transforms. |
| `integrators/` | Implicit Euler (FD, all dimensions) and ETD-RK4 (spectral, 2D). Selected via `get_integrator(params)` factory. |
| `participation.py` | Exact exponential integration of the v ODE, spatial averaging. |

### 2. Invariants (`edsim/invariants/`)

Computes the full ED invariant atlas from a density snapshot. Each invariant family is a separate module; the `atlas.py` module calls them all and merges the results.

| Module | Invariants |
|--------|-----------|
| `energy.py` | Lyapunov energy E, ED-complexity C, total mass M |
| `spectral.py` | Spectral entropy H, modal hierarchy, anisotropy, radial spectrum |
| `morphology.py` | Hessian eigenvalues, morphology fractions (blob/sheet/filament/pancake) |
| `dissipation.py` | Dissipation channel ratios R_grad, R_pen, R_part |
| `correlation.py` | Correlation length xi, structure function S_2(r), autocorrelation |
| `topology.py` | Euler characteristic chi, Betti numbers, connected components |
| `atlas.py` | `compute_atlas(rho, v, params)` -- calls all of the above |

### 3. Experiments (`edsim/experiments/`)

Orchestrates simulations: defines what to run and collects results.

| Module | Responsibility |
|--------|---------------|
| `scenarios.py` | Six named Scenario objects (A-F) with predefined parameters and ICs. `get_scenario(name)` lookup. |
| `runner.py` | `RunConfig`, `TimeSeries`, `run_simulation()`. The main entry point for executing a simulation with full invariant tracking. |
| `sweeps.py` | `run_sweep()` for 1D parameter sweeps, `run_grid_sweep()` for 2D sweeps, `run_batch()` for multiple configs. |
| `atlas.py` | `run_atlas()` for single instrumented runs, `summarize_time_series()` for compact result extraction. |

### 4. Reproducibility (`edsim/reproducibility/`)

Validates the implementation against the nine architectural laws.

| Module | Responsibility |
|--------|---------------|
| `pipeline.py` | Nine phase functions, each running a scenario and checking specific laws. `run_pipeline()` orchestrates all phases. |
| `certificate.py` | `LawCheck` and `ReproducibilityCertificate` dataclasses. Structured, serialisable validation output. |
| `run_all.py` | CLI entry point. Prints a formatted report with pass/fail status. |

### 5. Tests (`edsim/tests/`)

112 pytest tests organised by module. Shared fixtures in `conftest.py` provide small-grid parameters and standard ICs for fast execution.

---

## Dimensions and Methods

| Dimension | Implicit Euler (FD) | ETD-RK4 (Spectral) |
|-----------|--------------------|--------------------|
| d = 2 | Supported | Supported |
| d = 3 | Supported | Not yet |
| d = 4 | Supported | Not yet |

The implicit Euler integrator uses a fixed-point (Picard) iteration with the full nonlinear FD operator. It is unconditionally stable but first-order in time.

The ETD-RK4 integrator treats the linear part (M_star * Laplacian + P0) exactly via matrix exponentials in DCT space, and integrates the nonlinear remainder with a four-stage explicit RK scheme. It is fourth-order in time but currently restricted to 2D Neumann problems.

Both integrators couple the participation variable v via exact exponential integration of its ODE at each step.

---

## Design Principles

**Laws drive architecture drive code.** The nine architectural laws (ED-Phys-40) define what the simulation must produce. The invariant atlas is the measurement instrument. The tests verify that the laws hold numerically.

**Dimension-agnostic where possible.** The user writes `EDParameters(d=3, N=(16,16,16), ...)` and calls `run_simulation(config)`. Dimension dispatch happens inside the operator and integrator modules, not at the API level.

**Small, composable modules.** Each module has a single responsibility and a defined interface. The operator module does not know about invariants. The invariant module does not know about time integration. This makes it straightforward to replace or extend any component.

**Zero hidden state.** Every function is pure or nearly pure. The `SpectralState` is immutable. The integrator's `step()` takes state in and returns state out. There are no global variables, no singletons, no module-level caches.

**Deterministic reproducibility.** Every simulation is fully determined by its `EDParameters` and `RunConfig`. Random seeds are explicit. The reproducibility pipeline produces a structured certificate that captures platform info, phase results, and quantitative details.
