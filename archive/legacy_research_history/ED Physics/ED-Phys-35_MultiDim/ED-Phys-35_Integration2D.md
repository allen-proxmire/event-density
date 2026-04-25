# ED-Phys-35: 2D Integration into the ED-SIM Ecosystem

**Package:** `edsim2d/`
**Atlas run:** 4 scenarios, 33 output files, validated

---

## 1. Package Structure

```
ED Physics/ED-Phys-35_MultiDim/
  edsim_solver_2d.py       # Core PDE solver (ETD-RK4, CN-ADI)
  invariants_2d.py         # 2D invariant atlas (25 functions)
  visualization_2d.py      # Visualization suite (21 functions)
  edsim2d/
    __init__.py            # Package entry point; re-exports all public API
    runner_2d.py           # RunConfig2D, TimeSeries2D, run_experiment_2d()
    experiments_2d.py      # Scenarios A2D-D2D, run_atlas_2d()
    output/
      runs/                # Per-run data (metadata.json, time_series.npz, final_state.npz)
      figures/             # Per-scenario figure sets
      atlas/               # atlas_2d_report.json
```

The flat modules (`edsim_solver_2d.py`, `invariants_2d.py`, `visualization_2d.py`) remain importable standalone. The `edsim2d/` package wraps them with experiment orchestration.

## 2. Architecture Mapping (1D -> 2D)

| 1D Component | 2D Component | Role |
|---|---|---|
| `EDParameters` | `EDParameters2D` | Physics + grid config |
| `edsim_core.py` | `edsim_solver_2d.py` | PDE solver, time steppers |
| `edsim_diagnostics.py` | `invariants_2d.py` | Observable extraction |
| `edsim_runner.RunConfig` | `runner_2d.RunConfig2D` | Run specification |
| `edsim_runner.TimeSeries` | `runner_2d.TimeSeries2D` | Time-series storage |
| `edsim_runner.run_simulation()` | `runner_2d.run_experiment_2d()` | Main integration loop |
| `edsim_runner.run_batch()` | `runner_2d.run_batch_2d()` | Batch execution |
| `regime_volume_3d.py` | `experiments_2d.run_atlas_2d()` | Atlas generation |
| `edsim_initial_conditions.py` | `edsim_solver_2d.initialize_state_2d()` | IC generation |
| `ed_phys_visualization.py` | `visualization_2d.py` | Plotting |

## 3. Output Conventions

### Per-Run Directory (`output/runs/{run_id}/`)

| File | Format | Content |
|---|---|---|
| `metadata.json` | JSON | All parameters, IC name, wall time, violation counts, termination reason |
| `time_series.npz` | Compressed NPZ | t, v, E_total, E_potential, E_kinetic, D_gradient, D_penalty, D_participation, D_total, C_ED, mass, spectral_entropy, rho_max_local, rho_min_local, horizon_margin, modal_amplitudes (Nt, Kx, Ky) |
| `final_state.npz` | Compressed NPZ | rho (Nx, Ny), v (scalar), t (scalar) |

### Per-Scenario Figures (`output/figures/{scenario}/`)

| File | Content |
|---|---|
| `field_quad.png` | Density heatmap, contours, gradient, gradient magnitude |
| `time_series.png` | Energy, mass, participation, F_bar vs time |
| `evolution.png` | Multi-frame density snapshots |
| `invariants.png` | 6-panel invariant dashboard |
| `geometry.png` | Hessian, filamentarity, curvature |
| `horizon.png` | (D2D only) Proximity field + mask |

### Atlas Report (`output/atlas/atlas_2d_report.json`)

Per-scenario summary with: status, wall_time, E_ratio, mass change, spectral entropy, ED complexity, spectral/geometric anisotropy, filamentarity, horizon proximity, dissipation ratios, violation counts.

## 4. Experiment Scenarios

### A2D: Isotropic Relaxation

- **IC:** `rho_star + 0.05 cos(pi x) cos(pi y)`
- **Physics:** Set I (D=0.3, zeta=0.1)
- **Tests:** Energy monotone decay, spectral entropy low (single-mode dominance), anisotropy ~ 0

| Metric | Observed |
|---|---|
| E_ratio | 0.43 |
| A_spec | 0.000 |
| Filamentarity | 0.46 |
| Violations | 0 |

### B2D: Filament Formation

- **IC:** `rho_star + 0.08 cos(pi x)` (y-invariant)
- **Physics:** Set I
- **Tests:** Perfect filamentarity (F=1), spectral anisotropy = 1, y-uniformity preserved

| Metric | Observed |
|---|---|
| E_ratio | 0.68 |
| A_spec | 1.000 |
| Filamentarity | 1.000 |
| A_geom | 1.000 |

### C2D: Anisotropic Collapse

- **IC:** Multi-mode: `0.04 cos(pi x) + 0.015 cos(pi y) + 0.01 cos(2pi x) cos(pi y)`
- **Physics:** Set II (D=0.6, zeta=0.5)
- **Tests:** Anisotropic spectral structure, mode coupling, saddle-point formation

| Metric | Observed |
|---|---|
| E_ratio | 0.42 |
| A_spec | 0.74 |
| Filamentarity | 0.64 |
| Spectral entropy | 0.50 |

### D2D: Horizon Emergence

- **IC:** `rho_star + 0.4 exp(-r^2/0.02)` (large-amplitude Gaussian)
- **Physics:** Set IV (D=0.9, zeta=5.0)
- **Tests:** Horizon proximity -> 1, mobility collapse, capacity violations expected

| Metric | Observed |
|---|---|
| H_prox_max | 1.000 |
| Capacity violations | 7104 |
| A_spec | 0.000 (radially symmetric) |

## 5. API Quick Reference

### Run a single experiment
```python
from edsim2d.runner_2d import RunConfig2D, run_experiment_2d
from edsim_solver_2d import EDParameters2D

params = EDParameters2D(Nx=64, Ny=64, dt=5e-4, T=1.0, method='etdrk4')
config = RunConfig2D(params, ic_name='gaussian', ic_kwargs={'amplitude': 0.05},
                     run_id='my_experiment')
result = run_experiment_2d(config, verbose=True, save=True)
```

### Run all four scenarios
```python
from edsim2d.experiments_2d import run_atlas_2d
atlas = run_atlas_2d(N=64, T=1.0, dt=5e-4, method='etdrk4')
```

### Compute invariants on an arbitrary field
```python
from edsim2d import compute_invariants_2d, EDParameters2D
inv = compute_invariants_2d(rho, v, F_bar, params)
```

### Generate visualizations
```python
from visualization_2d import plot_field_quad, plot_invariants_2d
fig = plot_field_quad(rho, params, savepath='field.png')
fig = plot_invariants_2d(inv, params, savepath='dashboard.png')
```

### Command-line atlas
```bash
python -m edsim2d.experiments_2d -N 64 -T 1.0 --dt 5e-4
python -m edsim2d.experiments_2d --scenario A2D -N 128
```

## 6. Reproducibility Pipeline Integration

The 2D system integrates into the 1D pipeline as an optional extension phase. The atlas JSON report format is compatible with the existing aggregation tools.

| Phase | 1D | 2D |
|---|---|---|
| Initialization | `load_ic()` | `initialize_state_2d()` |
| Solver | `step()` | `step_2d()` |
| Diagnostics | `diagnostic_snapshot()` | `diagnostic_snapshot_2d()` |
| Invariants | 16 experiment scripts | `compute_invariants_2d()` |
| Visualization | `ed_phys_visualization.py` | `visualization_2d.py` |
| Atlas | `regime_volume_3d.py` | `experiments_2d.run_atlas_2d()` |
| Certificate | `generate_certificate_figure.py` | `atlas_2d_report.json` |
