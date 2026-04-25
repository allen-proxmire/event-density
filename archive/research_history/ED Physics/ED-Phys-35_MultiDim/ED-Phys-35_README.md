# ED-Phys-35: 2D/3D Event Density Extension

Multi-dimensional extension of the canonical ED PDE, implementing solvers,
invariants, visualization, and scientific exploration in 2D and 3D.

## Quick Start

```bash
# Run the full reproducibility pipeline (quick mode, ~20s)
cd "ED Physics/ED-Phys-35_MultiDim"
python reproducibility/run_all_2d3d.py --quick

# Run a 2D simulation
python -c "
from edsim_solver_2d import *
p = EDParameters2D(Nx=64, Ny=64, dt=5e-4, T=1.0, method='etdrk4')
res = run_simulation_2d(p, perturbation='gaussian', amplitude=0.05)
"

# Run a 3D simulation
python -c "
from edsim_solver_3d import *
p = EDParameters3D(Nx=32, Ny=32, Nz=32, dt=1e-3, T=0.5, method='etdrk4')
res = run_simulation_3d(p, perturbation='cosine', amplitude=0.03)
"

# Run the 2D atlas (4 scenarios with figures)
python -m edsim2d.experiments_2d -N 64 -T 1.0

# Generate synthesis figures
python generate_final_figures.py
```

## Requirements

- Python >= 3.10
- NumPy >= 1.21
- SciPy >= 1.7
- Matplotlib >= 3.5

## Directory Structure

```
ED-Phys-35_MultiDim/
  edsim_solver_2d.py          # 2D PDE solver (ETD-RK4 + CN-ADI)
  edsim_solver_3d.py          # 3D PDE solver (ETD-RK4 + CN-ADI)
  invariants_2d.py            # 2D invariant atlas (23 invariants)
  invariants_3d.py            # 3D invariant atlas (23 invariants)
  visualization_2d.py         # 2D visualization suite (21 functions)
  visualization_3d.py         # 3D visualization suite (18 functions)
  edsim2d/                    # Integrated experiment package
    __init__.py
    runner_2d.py              # RunConfig2D, TimeSeries2D, run_experiment_2d
    experiments_2d.py         # Scenarios A2D-D2D, run_atlas_2d
    output/                   # Generated data, figures, reports
  reproducibility/
    run_all_2d3d.py           # 8-phase reproducibility pipeline
  phase3_validation.py        # Phase 3: 2D validation suite
  phase7_exploration.py       # Phase 7: 2D scientific exploration
  phase11_exploration_3d.py   # Phase 11: 3D scientific exploration
  generate_final_figures.py   # Phase 12: Synthesis figures
  test_*.py                   # Unit tests (151 total)
```

## Documentation

| File | Content |
|------|---------|
| `ED-Phys-35_Architecture.md` | Phase 1: Mathematical specification |
| `ED-Phys-35_Phase3_ValidationReport.md` | Phase 3: Convergence, stability, energy |
| `ED-Phys-35_Invariants2D.md` | Phase 4: 2D invariant definitions |
| `ED-Phys-35_Visualization2D.md` | Phase 5: 2D visualization API |
| `ED-Phys-35_Integration2D.md` | Phase 6: ED-SIM integration |
| `ED-Phys-35_2D_ScientificFindings.md` | Phase 7: 2D scientific results |
| `ED-Phys-35_3D_SolverArchitecture.md` | Phase 8: 3D solver design |
| `ED-Phys-35_Invariants3D.md` | Phase 9: 3D invariant definitions |
| `ED-Phys-35_Visualization3D.md` | Phase 10: 3D visualization API |
| `ED-Phys-35_3D_ScientificFindings.md` | Phase 11: 3D scientific results |
| `ED-Phys-35_Final_2D3D_Report.md` | Phase 12: Unified final report |

## Key Scientific Results

### Four Dimensional Laws

1. **Complexity Dilution:** $C^{(d)} = C^{(1)} / d!$ (2% agreement)
2. **Gradient Dominance:** $R_\text{grad}$ increases 0.72 -> 0.83 -> 0.88 across 1D/2D/3D
3. **Horizon Elevation:** Higher dimensions require larger amplitudes for horizon formation
4. **Topological Conservation:** $d\chi/dt = 0$ (Euler characteristic is constant)

### Architectural Invariant

R_grad = 0.89 with CV = 2% across 20 3D runs — the most stable invariant in any dimension of the ED system.

## Test Coverage

| Module | Tests | Status |
|--------|-------|--------|
| 2D solver | 33 | PASS |
| 3D solver | 14 | PASS |
| 2D invariants | 33 | PASS |
| 3D invariants | 32 | PASS |
| 2D visualization | 21 | PASS |
| 3D visualization | 18 | PASS |
| **Total** | **151** | **ALL PASS** |

## Reproducibility Pipeline

```bash
python reproducibility/run_all_2d3d.py          # Full run (~2 min)
python reproducibility/run_all_2d3d.py --quick   # Quick run (~20 sec)
```

8 phases: environment -> 2D solver -> 3D solver -> 2D invariants -> 3D invariants -> 2D atlas -> 3D demo -> figures. Produces `pipeline_report.json` with timestamps and verdicts.
