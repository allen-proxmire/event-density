# API Overview

High-level reference for the key classes and functions in ED-SIM-02. For detailed signatures and docstrings, see the source code directly.

---

## Core

### `edsim.core.parameters.EDParameters`

Frozen dataclass specifying all simulation parameters: dimension, grid, constitutive constants, numerical settings. Central configuration object for the entire platform.

```python
from edsim.core.parameters import EDParameters
params = EDParameters(d=2, N=(32, 32), L=(1.0, 1.0), D=0.3, dt=5e-4, T=0.5)
```

### `edsim.core.constitutive`

Pure functions for the ED constitutive law.

| Function | Description |
|----------|------------|
| `mobility(rho, params)` | M(rho) = M0 * (rho_max - rho)^beta |
| `mobility_deriv(rho, params)` | M'(rho) |
| `penalty(rho, params)` | P(rho) = P0 * (rho - rho_star) |
| `enforce_bounds(rho, params)` | Clip rho to [0, rho_max] |

### `edsim.core.operators`

Spatial operators for the ED PDE.

| Function | Description |
|----------|------------|
| `operator_F_split_fd(rho, params, v)` | Returns (F_local, F_total) for any d |
| `laplacian_fd_2d(rho, dx)` | 5-point FD Laplacian |
| `laplacian_fd_3d(rho, dx)` | 7-point FD Laplacian |
| `laplacian_fd_4d(rho, dx)` | 9-point FD Laplacian |

### `edsim.core.integrators.base.get_integrator`

Factory that returns the appropriate integrator for `params.method`.

```python
from edsim.core.integrators.base import get_integrator
integrator = get_integrator(params)
state = integrator.setup(params)
rho_new, v_new, state = integrator.step(rho, v, t, params, state)
```

---

## Invariants

### `edsim.invariants.atlas.compute_atlas`

Compute the full invariant atlas for a single snapshot.

```python
from edsim.invariants.atlas import compute_atlas
atlas = compute_atlas(rho, v, params)
# atlas["energy"], atlas["complexity"], atlas["spectral_entropy"], ...
```

### Individual invariant modules

| Module | Key functions |
|--------|--------------|
| `edsim.invariants.energy` | `lyapunov_energy`, `ed_complexity`, `total_mass` |
| `edsim.invariants.spectral` | `spectral_entropy`, `modal_hierarchy`, `spectral_anisotropy` |
| `edsim.invariants.morphology` | `hessian_eigenvalues`, `morphology_fractions` |
| `edsim.invariants.dissipation` | `dissipation_channels` |
| `edsim.invariants.correlation` | `correlation_length`, `structure_function_2` |
| `edsim.invariants.topology` | `euler_characteristic`, `betti_numbers` |

---

## Experiments

### `edsim.experiments.scenarios.Scenario`

A named, reproducible experiment specification.

```python
from edsim.experiments.scenarios import get_scenario, get_scenarios
scenario = get_scenario("A_2d_cosine")
config = scenario.make_config()   # returns RunConfig
```

Available scenarios: `A_2d_cosine`, `B_3d_cosine`, `C_4d_cosine`, `D_2d_random`, `E_2d_high_amplitude`, `F_3d_gaussian`.

### `edsim.experiments.runner.run_simulation`

Execute a simulation and return a `TimeSeries` with full invariant tracking.

```python
from edsim.experiments.runner import RunConfig, run_simulation
ts = run_simulation(config)
```

### `edsim.experiments.atlas.run_atlas`

Run a scenario with optional parameter modification.

```python
from edsim.experiments.atlas import run_atlas, summarize_time_series
params, ts = run_atlas(scenario)
summary = summarize_time_series(ts)
```

### `edsim.experiments.sweeps.run_sweep`

1D parameter sweep over a named field.

```python
from edsim.experiments.sweeps import run_sweep
results = run_sweep(scenario, vary="D", values=[0.1, 0.3, 0.5])
```

---

## Reproducibility

### `edsim.reproducibility.pipeline.run_pipeline`

Run the full 9-phase validation pipeline.

```python
from edsim.reproducibility.pipeline import run_pipeline
cert = run_pipeline()
print(cert.summary())
```

### `edsim.reproducibility.certificate.ReproducibilityCertificate`

Structured validation result with `phases`, `all_passed`, `failed_names`, `to_dict()`, and `summary()`.

### CLI

```bash
python -m edsim.reproducibility.run_all
```
