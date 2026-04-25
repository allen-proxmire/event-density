# ED-PHYS-10: Master Interpretation and Synthesis

## Purpose

ED-PHYS-10 integrates all results from PHYS-01 through PHYS-09 into a
single coherent scientific interpretation of the Event Density PDE.

## The Nine Experiments

| # | Experiment | Key Result |
|---|-----------|------------|
| 01 | Diffusion | D_eff = D M_star (7.5%) |
| 02 | Wave | Telegraph oscillation (k=0), no spatial waves |
| 03 | Reaction | lambda = D P0 (0.03%) |
| 04 | Pattern | No instability — all sigma_k < 0 |
| 05 | Quantum-like | Non-Gaussian spreading, nonlinear superposition |
| 06 | Phase diagram | 5 phases, telegraph dominates (69%) |
| 07 | Energy | 5 Lyapunov functionals, NOT gradient flow |
| 08 | Interpretation | Population density strongest match (8/10) |
| 09 | Cosmology | 5 structural analogues confirmed |

## ED's Identity

**Mathematical:** Quasilinear degenerate parabolic PDE with monostable
penalty and global scalar feedback.

**Physical:** Density-dependent transport with carrying capacity,
relaxation toward equilibrium, and global environmental feedback.

**Universality class:** Degenerate parabolic reaction-diffusion with
global feedback.  Nearest relative: porous-medium equation.  Strongest
physical match: population/agent density models (8/10).

## What ED Is Not

| Claim | Why not |
|-------|---------|
| Quantum | Classical, dissipative, no Planck constant |
| Hydrodynamic | Scalar density, no velocity field |
| Thermodynamic | Not entropy-maximising, not detailed-balance |
| Variational | NOT a gradient flow (995% residual) |
| Relativistic | No metric, no curvature, no gravity |

## Structural Analogues

| Target | Mechanism | Quality |
|--------|-----------|---------|
| Cosmological expansion | Penalty decay | Strong |
| Causal horizons | Degenerate mobility | Strong |
| Cosmic web | Hessian morphology | Moderate |
| Quantum spreading | Nonlinear mobility | Weak |
| Telegraph | Participation coupling | Strong |

## How to Run

```python
from edsim.phys.master_interpretation import build_master_report

report = build_master_report()
print(report)
```

## Significance

The ED PHYS programme demonstrates that a single PDE — with three
constitutive functions and seven axioms — can be rigorously decomposed
into diffusion, reaction, and telegraph channels, quantitatively compared
to eight physical domains, and shown to produce structural analogues of
cosmological phenomena.  The framework is complete, reproducible, and
falsifiable.
