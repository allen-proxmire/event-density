# ED-SIM-02: An Architectural Lab for Entropic Dynamics

![Tests](https://github.com/allen/edsim/actions/workflows/tests.yml/badge.svg)
![Certify](https://github.com/allen/edsim/actions/workflows/certify.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![Version](https://img.shields.io/badge/version-0.1.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

ED-SIM-02 is a modular simulation platform for the Event Density PDE, a nonlinear parabolic system with degenerate mobility, penalty relaxation, and global participation coupling. It solves the canonical ED equation in 2D, 3D, and 4D, computes a full invariant atlas at each time step, and provides a reproducible pipeline for verifying the nine architectural laws established in the ED-Phys series. The platform is designed for scientific exploration, not production computation: clarity and correctness take precedence over raw performance.

---

## Quick Start

### Install

```bash
cd "Event Density"
pip install -e .
```

Dependencies: NumPy, SciPy, Matplotlib. Optional: pytest (for tests).

### Run the tests

```bash
pytest edsim/tests/ -v
```

112 tests covering core numerics, invariants, and architectural laws.

### Run the reproducibility pipeline

```bash
python -m edsim.reproducibility.run_all
```

Nine phases checking Laws 1-6, dimensional scaling, morphology, and topology. Takes about 6 seconds.

### Run a single scenario

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series

scenario = get_scenario("A_2d_cosine")
params, ts = run_atlas(scenario)
summary = summarize_time_series(ts)

print(f"Energy ratio:  {summary['energy_ratio']:.4f}")
print(f"R_grad mean:   {summary['R_grad_mean']:.4f}")
print(f"xi growth:     {summary['xi_ratio']:.2f}x")
```

---

## Core Ideas

- **The PDE.** ED-SIM-02 solves a coupled system: a density field rho(x,t) evolving under nonlinear diffusion with degenerate mobility M(rho), a penalty P(rho) driving rho toward equilibrium, and a global participation variable v(t) providing non-local feedback.

- **Nine architectural laws.** The ED framework predicts specific qualitative and quantitative behaviours: a unique attractor, energy monotonicity, exponential modal decay, factorial complexity dilution with dimension, gradient-dissipation dominance, topological conservation, horizon formation, morphological hierarchy, and sheet-filament oscillation. The simulation platform tests each of these.

- **Full invariant atlas.** At every output snapshot, the platform computes: Lyapunov energy, ED-complexity, mass, spectral entropy, modal hierarchy, morphology fractions (blob/sheet/filament/pancake), dissipation channel ratios (R_grad/R_pen/R_part), correlation length, structure functions, Euler characteristic, and Betti numbers.

- **Dimensions 2 through 4.** The same API serves d=2, 3, and 4. Dimension-specific optimisations (explicit stencils for 2D/3D/4D) are encapsulated inside the operator module; the user-facing interface is dimension-agnostic.

- **Two integrators.** Implicit Euler (FD, all dimensions) and ETD-RK4 (spectral, 2D only). Selected via `method="implicit_euler"` or `method="etdrk4"`.

---

## Repository Layout

```
edsim/
  core/              Parameters, operators, integrators, boundary, spectral
  invariants/        Energy, spectral, morphology, dissipation, correlation, topology
  experiments/       Scenarios, sweeps, atlas runner
  reproducibility/   9-phase pipeline, certificate
  tests/             112 pytest tests (unit + science)

docs/                Architecture, usage, API overview
examples/            Lab tour notebook
```

---

## What You Can Do

**Run named scenarios.** Six predefined experiments (A-F) covering 2D/3D/4D, cosine/random/Gaussian ICs, moderate and high amplitudes.

**Sweep parameters.** Vary any EDParameters field (D, P0, beta, ...) or IC parameter (A, Nm, sigma) across a range and collect full invariant time series for each.

**Inspect the atlas.** Every TimeSeries object contains time-indexed arrays of all invariants. Plot energy decay, spectral concentration, morphology evolution, dissipation partition, correlation growth, and topological conservation directly from the returned data.

**Validate laws.** The reproducibility pipeline checks Laws 1-6 and dimensional scaling in a single command, producing a structured certificate with pass/fail status and quantitative details.

---

## Status

### Implemented

- Solver: 2D/3D/4D FD implicit Euler; 2D spectral ETD-RK4
- Invariants: energy, complexity, mass, spectral entropy, modal hierarchy, morphology (blob/sheet/filament/pancake), dissipation channels, correlation length, structure functions, Euler characteristic, Betti numbers
- Experiments: 6 scenarios, 1D/2D parameter sweeps, atlas runner with summary extraction
- Reproducibility: 9-phase pipeline, structured certificate
- Tests: 112 pytest tests (3s)

### Out of Scope (This Version)

- Large-scale performance (no GPU, no parallel sweeps)
- Spectral integrators for d > 2
- Full persistent homology (Betti numbers are approximate for d >= 3)
- Visualization module (users use matplotlib directly)
- Crank-Nicolson / ADI integrator (skeleton only)
- Checkpoint save/load and HDF5 export (skeleton only)
