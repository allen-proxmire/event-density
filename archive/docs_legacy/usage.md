# Usage Guide

This document explains how to set up, run, and inspect ED-SIM-02 simulations.

---

## 1. Constructing Parameters

Every simulation is specified by an `EDParameters` object. It is a frozen (immutable) dataclass that holds all physical and numerical settings.

```python
from edsim.core.parameters import EDParameters

params = EDParameters(
    d=2,                        # spatial dimension
    N=(32, 32),                 # grid points per axis
    L=(1.0, 1.0),              # domain size per axis
    D=0.3,                      # diffusion weight
    H=0.15,                     # participation coupling
    zeta=0.1,                   # participation damping
    tau=1.0,                    # participation timescale
    rho_star=0.5,               # penalty equilibrium
    rho_max=1.0,                # capacity bound
    M0=1.0,                     # mobility prefactor
    beta=2.0,                   # mobility exponent
    P0=1.0,                     # penalty slope
    dt=5e-4,                    # time step
    T=0.5,                      # final time
    k_out=100,                  # output every k_out steps
    method="implicit_euler",    # integrator: "implicit_euler" or "etdrk4" (2D only)
    bc="neumann",               # boundary conditions
    seed=42,                    # RNG seed
)
```

Useful derived quantities:

```python
params.dx                  # grid spacing per axis
params.M_star              # mobility at equilibrium
params.R_grad_predicted    # predicted gradient-dissipation ratio
params.total_grid_points   # total grid count
params.n_steps             # total time steps
```

To create a modified copy (the object is frozen, so you cannot assign fields directly):

```python
from edsim.experiments.scenarios import _replace_params
params_fast = _replace_params(params, D=0.5, T=1.0)
```

---

## 2. Running a Simulation

The simplest path is through `RunConfig` and `run_simulation`:

```python
from edsim.experiments.runner import RunConfig, run_simulation

config = RunConfig(
    params=params,
    ic_type="cosine",           # "cosine", "random", "gaussian", or "custom"
    ic_kwargs={"A": 0.03, "Nm": 2},
)

ts = run_simulation(config)
```

The returned `TimeSeries` object contains everything:

```python
ts.times                   # list of snapshot times
ts.fields                  # list of rho arrays (one per snapshot)
ts.v_history               # participation variable at each snapshot
ts.energy                  # Lyapunov energy E[rho]
ts.complexity              # ED-complexity C[rho]
ts.mass                    # total mass M[rho]
ts.spectral_entropy        # spectral entropy H
ts.modal_hierarchy         # sorted modal amplitudes
ts.morphology_fractions    # {blob, sheet, filament, pancake} dicts
ts.R_grad, ts.R_pen, ts.R_part   # dissipation channel fractions
ts.correlation_length      # correlation length xi
ts.structure_r, ts.structure_S2   # structure function S_2(r)
ts.euler_characteristic    # Euler characteristic chi
ts.betti_numbers           # [beta_0, beta_1, ...]
```

---

## 3. Using Predefined Scenarios

ED-SIM-02 ships with six named scenarios:

```python
from edsim.experiments.scenarios import get_scenarios

for name, sc in get_scenarios().items():
    print(f"{name}: {sc.description[:60]}...")
```

To run a scenario with the atlas runner:

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series

scenario = get_scenario("A_2d_cosine")
params, ts = run_atlas(scenario)
summary = summarize_time_series(ts)
```

The summary dict gives you quick access to initial/final values of all invariants.

---

## 4. Parameter Sweeps

Vary a single parameter across a range:

```python
from edsim.experiments.sweeps import run_sweep

results = run_sweep(scenario, vary="D", values=[0.1, 0.3, 0.5])

for sr in results:
    print(f"{sr.label}: E_final={sr.series.energy[-1]:.4e}")
```

Vary an IC parameter by prefixing with `ic_`:

```python
results = run_sweep(scenario, vary="ic_A", values=[0.01, 0.03, 0.05])
```

---

## 5. Plotting Results

ED-SIM-02 does not include a built-in visualization module. Use matplotlib directly:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].semilogy(ts.times, ts.energy)
axes[0].set_xlabel("t")
axes[0].set_ylabel("E[rho]")
axes[0].set_title("Lyapunov Energy")

axes[1].semilogy(ts.times, ts.complexity)
axes[1].set_xlabel("t")
axes[1].set_ylabel("C[rho]")
axes[1].set_title("ED-Complexity")

axes[2].plot(ts.times, ts.spectral_entropy)
axes[2].set_xlabel("t")
axes[2].set_ylabel("H")
axes[2].set_title("Spectral Entropy")

plt.tight_layout()
plt.show()
```

For morphology evolution:

```python
blobs = [m["blob"] for m in ts.morphology_fractions]
sheets = [m["sheet"] for m in ts.morphology_fractions]

plt.stackplot(ts.times, blobs, sheets, labels=["blob", "sheet"])
plt.xlabel("t")
plt.ylabel("fraction")
plt.legend()
plt.title("Morphology Evolution")
plt.show()
```

---

## 6. Reproducibility Pipeline

Run all nine validation phases:

```python
from edsim.reproducibility.pipeline import run_pipeline

cert = run_pipeline()
print(cert.summary())
```

Or from the command line:

```bash
python -m edsim.reproducibility.run_all
```
