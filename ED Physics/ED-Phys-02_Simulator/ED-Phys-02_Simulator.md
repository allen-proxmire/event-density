# ED-Phys-02: Minimal ED Universe Simulator — Specification

## Canonical Lineage

This simulator implements **only** the update rule derived in ED-Phys-01, which itself draws exclusively from:

| Source | What It Provides |
|--------|-----------------|
| ED-5 | ED system axioms (E, C, rho), non-negativity, compositionality |
| ED-12 | General compositional rule, three penalty terms, coarse-grained dynamics |
| ED-12.5 | Nonlinear diffusion form, mobility M(rho), Friedmann analogue |
| ED-Phys-01 | Discretized update rule, finite-difference operators, CFL stability |

No other ED sources (ED-Sim, ED-Interpretations, ED-Physical-Computation) are used.

---

## 1. Architecture

```
ed_phys_config.py        Parameters and presets
ed_phys_lattice.py       Lattice construction and initial conditions
ed_phys_operators.py     Finite-difference gradient operators and mobility
ed_phys_engine.py        Core simulation loop (the update rule)
ed_phys_diagnostics.py   Observable extraction, phase identification, summary
ed_phys_visualization.py Plotting hooks (1D line plots, 2D heatmaps, time series)
ed_phys_run.py           CLI entry point
```

### Data Flow

```
EDParams ──> create_initial_condition() ──> rho_0
                                              |
                                              v
                            simulate(params, rho_0) ──> SimulationResult
                                              |
                                 ┌────────────┼────────────┐
                                 v            v            v
                           rho_final     history     rho_snapshots
                                 |            |
                                 v            v
                         plot_*_triple   plot_time_series
                                          identify_phases
                                            summary
```

---

## 2. The Update Rule

Implemented exactly as derived in ED-Phys-01 Section 7.5:

```
rho_{t+1}(x) = rho_t(x) + eta * [
    M(rho) * Lap(rho)                           ... mobility-weighted diffusion
  + M'(rho) * |grad(rho)|^2                     ... nonlinear gradient correction
  - alpha * gamma_exp * max(rho, eps)^(gamma_exp - 1)   ... relational penalty
]
```

followed by positivity enforcement: `rho = max(rho, 0)`.

### Term Implementations

| Term | Function | File | ED-Phys-01 Section |
|------|----------|------|--------------------|
| Lap(rho) | `discrete_laplacian()` | `ed_phys_operators.py` | 7.2 |
| \|grad(rho)\|^2 | `discrete_grad_squared()` | `ed_phys_operators.py` | 7.2 |
| M(rho) | `mobility()` | `ed_phys_operators.py` | 7.3 |
| M'(rho) | `mobility_derivative()` | `ed_phys_operators.py` | 7.4 |
| Relational penalty | inline in `simulate()` | `ed_phys_engine.py` | 5.1, 7.5 |

### Boundary Conditions

| Type | Implementation |
|------|---------------|
| Periodic (default) | `np.pad(rho, 1, mode='wrap')` |
| Reflecting | `np.pad(rho, 1, mode='reflect')` |
| Absorbing | `np.pad(rho, 1, constant_values=rho_min)` |

---

## 3. Update Loop Pseudocode

```
FOR t = 0 TO n_steps - 1:

    1. Pad rho with ghost cells (boundary condition)
    2. Compute Laplacian:
         lap_i = (rho_{i+1} - 2*rho_i + rho_{i-1}) / dx^2       [1D]
         lap_{ij} = (rho_{i+1,j} + rho_{i-1,j} + rho_{i,j+1}
                   + rho_{i,j-1} - 4*rho_{ij}) / dx^2            [2D]

    3. Compute gradient squared:
         |grad rho|^2_i = ((rho_{i+1} - rho_{i-1}) / (2*dx))^2   [1D]
         [analogous for 2D with both partial derivatives]

    4. Compute mobility:
         M_i = M_0 * max(0, 1 - rho_i/rho_max)^n_mob

    5. Compute mobility derivative:
         M'_i = -M_0 * (n_mob/rho_max) * max(0, 1 - rho_i/rho_max)^(n_mob-1)

    6. Compute relational penalty:
         rel_i = alpha * gamma_exp * max(rho_i, eps)^(gamma_exp - 1)

    7. Assemble RHS:
         drho_i = M_i * lap_i + M'_i * |grad rho|^2_i - rel_i

    8. Update:
         rho_i = rho_i + eta * drho_i

    9. Enforce positivity:
         rho_i = max(rho_i, 0)

    10. Record diagnostics every record_interval steps
    11. Check early-stopping condition (if configured)
```

---

## 4. Parameter Definitions and Defaults

### Physics Parameters

| Parameter | Symbol | Default | Role | Constraint |
|-----------|--------|---------|------|-----------|
| Relational coupling | alpha | 0.1 | Concave competition strength | > 0 |
| Concavity exponent | gamma_exp | 0.5 | f(rho) = rho^gamma_exp | (0, 1) |
| Bare mobility | M_0 | 1.0 | Maximum diffusion rate | > 0 |
| Saturation density | rho_max | 100.0 | Horizon / ceiling density | > 0 |
| Mobility exponent | n_mob | 2 | Saturation sharpness | >= 1 |
| Boundary coupling | gamma_b | 0.0 | Boundary penalty strength | >= 0 |

### Numerical Parameters

| Parameter | Symbol | Default | Role |
|-----------|--------|---------|------|
| Grid size | N | 256 (1D), 128 (2D) | Lattice resolution |
| Grid spacing | dx | 1.0 | Normalized spacing |
| Timestep | eta | auto (10% CFL) | Evolution rate |
| CFL safety | cfl_safety | 0.1 | Fraction of stability limit |
| Density floor | eps | 1e-10 | Prevents rho^(gamma-1) divergence |
| Steps | n_steps | 10000 | Total simulation steps |
| Record interval | record_interval | 100 | Diagnostic sampling frequency |

### Auto-Timestep Computation

From ED-Phys-01 Section 8.3:

```
eta = cfl_safety * min(
    dx^2 / (2 * D * M_0),                    ... diffusion CFL
    eps^(1 - gamma_exp) / (alpha * gamma_exp) ... relational bound
)
```

where D = number of spatial dimensions (1 or 2).

---

## 5. Diagnostics

Recorded every `record_interval` steps (ED-Phys-01 Section 9):

| Observable | Definition | Physical Analogue |
|-----------|-----------|-------------------|
| rho_total | Sum of rho over all sites | Total "becoming" |
| rho_mean | Mean rho | Global density (Friedmann rho) |
| rho_max | Maximum rho | Peak intensity |
| rho_min | Minimum rho | Background level |
| grad_mean | Mean \|grad rho\| | Inhomogeneity measure G(t) |
| grad_max | Max \|grad rho\| | Sharpest gradient |
| grad_energy | Sum of \|grad rho\|^2 | Total gradient penalty cost |
| thinning_rate | Change in rho_total since last record | Expansion rate proxy |
| n_basins | Count of local minima | Structure / void count |
| scale_factor_proxy | 1 / grad_mean | ED scale factor a(t) |

---

## 6. Stability and Stiffness

### Sources of Stiffness (ED-Phys-01 Section 13.1)

1. **Relational term divergence:** The term rho^(gamma_exp - 1) diverges as rho -> 0.
   - Mitigation: density floor eps = 1e-10
   - The CFL bound includes eps^(1-gamma_exp) / (alpha * gamma_exp)

2. **Mobility contrast:** When some cells are near rho_max (M -> 0) and others are at low rho (M -> M_0), effective diffusion rates span orders of magnitude.
   - Mitigation: conservative CFL safety factor (10%)
   - Future option: semi-implicit integration (implicit diffusion, explicit relational)

3. **Scale separation:** During inflation, gradients decay exponentially while mean density changes slowly. This timescale separation can cause numerical drift.
   - Mitigation: small timestep; monitor thinning_rate for anomalous behavior

### Positivity

The explicit Euler scheme does not automatically preserve rho >= 0. Post-update clamping `rho = max(rho, 0)` is applied at every step (ED-Phys-01 Section 8.4).

### Saturation

If rho > rho_max, mobility becomes zero (via the max(0,...) clamp in the mobility function). This prevents unbounded density growth and provides a natural self-limiting mechanism corresponding to horizon formation.

---

## 7. Expected Qualitative Behaviors

The four cosmological phases predicted by ED-12 and formalized in ED-Phys-01 Section 10:

### Phase 1: Inflation (Gradient Smoothing)
- **When:** Early time, starting from noisy initial conditions
- **Mechanism:** M(rho) * Lap(rho) dominates; diffusion smooths gradients
- **Observable signature:** grad_mean decays exponentially; scale_factor_proxy grows exponentially
- **Duration:** Continues until gradients become small enough that diffusion weakens relative to relational term

### Phase 2: Structure Formation
- **When:** After inflation, when gradients are small but nonzero
- **Mechanism:** Relational penalty -alpha * gamma_exp * rho^(gamma_exp - 1) amplifies overdensities via concave instability; sublinear saturation prevents runaway
- **Observable signature:** n_basins initially increases as structures seed, then decreases as structures merge; rho_max may increase; rho range widens
- **Sensitivity:** Depends critically on alpha/M_0 ratio and gamma_exp

### Phase 3: Global Thinning (Expansion)
- **When:** After structures form, on longer timescales
- **Mechanism:** Net diffusive outflow from high-density pockets; rho_mean decreases as "becoming" spreads
- **Observable signature:** rho_mean monotonically decreasing; thinning_rate negative; scale_factor_proxy continues growing
- **Dynamics:** d(rho_mean)/dt ~ -lambda_2 * G^2 (from ED-12)

### Phase 4: Heat Death (Asymptotic Flatness)
- **When:** Very late time
- **Mechanism:** All gradients effectively vanished; relational penalty sets the floor
- **Observable signature:** rho_mean and grad_mean both approximately constant; n_basins stable; scale_factor_proxy very large or infinite
- **Character:** Near-uniform low-density state with minimal evolution

### Phase Identification

The `identify_phases()` function uses heuristic rules on the diagnostic time series:
- Inflation: grad_mean decreasing rapidly, n_basins not growing
- Structure formation: n_basins increasing
- Thinning: rho_mean decreasing, n_basins stable
- Heat death: both rho_mean and grad_mean approximately constant

These heuristics are approximate and may classify transitional periods ambiguously. More sophisticated phase detection (e.g., fitting exponential decay to grad_mean) is deferred to ED-Phys-03.

---

## 8. Initial Conditions

Three modes are supported:

| Mode | Description | Use Case |
|------|-----------|----------|
| `uniform_noise` | rho_mean + small Gaussian noise | Default cosmological IC (ED-Phys-01 Sec 13.3) |
| `localized_gradient` | Uniform background + single Gaussian bump | Perturbation growth study |
| `random` | rho_mean + large random perturbations | Structure formation stress test |

Default: `uniform_noise` with rho_mean = 50.0, noise_amplitude = 0.1

---

## 9. Visualization Hooks

All plotting functions are defined but do NOT auto-generate images. Call explicitly when needed.

### 1D Hooks
- `plot_1d_density(rho)` — line plot of rho(x)
- `plot_1d_gradient(rho, dx)` — line plot of |grad rho|(x)
- `plot_1d_curvature(rho, dx)` — line plot of Lap(rho)(x)
- `plot_1d_triple(rho, dx)` — three-panel combined plot

### 2D Hooks
- `plot_2d_density(rho)` — heatmap of rho(x,y)
- `plot_2d_gradient(rho, dx)` — heatmap of |grad rho|
- `plot_2d_horizon_candidates(rho, rho_max)` — heatmap of near-saturation cells
- `plot_2d_triple(rho, rho_max, dx)` — three-panel combined

### Time Series
- `plot_time_series(result)` — six-panel diagnostic history (rho_mean, grad_mean, scale_factor, n_basins, grad_energy, thinning_rate)

---

## 10. CLI Usage

```bash
# Default 1D cosmological run
python ed_phys_run.py

# 2D run, larger grid, more steps
python ed_phys_run.py --dim 2 --N 64 --n_steps 50000

# Custom physics
python ed_phys_run.py --alpha 0.2 --gamma_exp 0.3 --M_0 2.0

# Different initial conditions
python ed_phys_run.py --ic_mode localized_gradient --rho_mean 80 --noise 0.5

# Save results
python ed_phys_run.py --save_npz results.npz --snapshot_interval 1000

# Aggressive timestep (faster but less stable)
python ed_phys_run.py --cfl_safety 0.4 --n_steps 100000

# Early stopping when gradients vanish
python ed_phys_run.py --early_stop 0.001
```

---

## 11. File Manifest

| File | Lines | Purpose |
|------|-------|---------|
| `ed_phys_config.py` | ~120 | Parameter dataclass, validation, CFL computation, presets |
| `ed_phys_lattice.py` | ~80 | Initial condition generation (3 modes) |
| `ed_phys_operators.py` | ~140 | Laplacian, gradient, mobility operators with boundary padding |
| `ed_phys_engine.py` | ~170 | Core simulation loop, basin counting, SimulationResult |
| `ed_phys_diagnostics.py` | ~150 | Time series extraction, phase ID, summary text |
| `ed_phys_visualization.py` | ~200 | Plotting hooks (1D, 2D, time series) |
| `ed_phys_run.py` | ~155 | CLI entry point with argparse |

---

## 12. Dependencies

- **Required:** `numpy` (all numerical computation)
- **Optional:** `matplotlib` (visualization hooks only; simulator runs without it)
- **Python:** 3.10+ (uses `X | None` type hints)

---

## 13. Open Items for Downstream Modules

| Decision | Deferred To | Notes |
|----------|------------|-------|
| Semi-implicit integration | ED-Phys-05 (if stability limits parameter sweeps) | Explicit Euler sufficient for initial exploration |
| Adaptive timestepping | ED-Phys-05 | May be needed for extreme parameter regimes |
| Boundary penalty form h(u) | ED-Phys-06 (if horizon phenomena studied) | Currently gamma_b = 0 (periodic BCs) |
| Higher-order stencils | ED-Phys-07 | Current 2nd-order stencils match ED-Phys-01 spec |
| GPU acceleration | Not planned | NumPy is sufficient for N <= 512 |
