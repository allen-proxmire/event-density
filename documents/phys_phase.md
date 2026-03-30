# ED-PHYS-06: Global Phase Diagram

## Purpose

ED-PHYS-06 maps the qualitative behaviour of the ED PDE across the
three-parameter space (M0, P0, H) and identifies five distinct dynamical
phases.

## The Three Control Parameters

| Parameter | Role | Range tested |
|-----------|------|-------------|
| M0 | Mobility prefactor (diffusion strength) | 0.5 - 4.0 |
| P0 | Penalty slope (reaction strength) | 0.05 - 3.0 |
| H | Participation coupling (telegraph strength) | 0.0 - 5.0 |

## The Five Phases

**Diffusion** (14%): M_star pi^2 / P0 >= 5, H = 0. The Laplacian
dominates; the field spreads like the heat equation.

**Reaction** (3%): M_star pi^2 / P0 < 1, H = 0. The penalty dominates;
the field relaxes exponentially toward rho_star.

**Telegraph** (69%): Q >= 1 (any H > 0 at most P0 values). The
participation coupling creates damped oscillation of the mean density.

**Transient** (8%): Moderate ratio, H = 0. Diffusion and reaction
compete; rich transient morphology.

**Quantum-like** (6%): M0 >= 2, P0 <= 0.1, H >= 1. Strong nonlinear
mobility + oscillatory envelope.

## Phase Boundaries

**Diffusion-reaction:** R = D * M_star * pi^2 / (D * P0). R > 5:
diffusion. R < 1: reaction. 1 < R < 5: transient.

**Telegraph:** Q = omega_osc / (2 gamma) >= 1. For most P0, even
H = 0.5 exceeds this threshold.

**Quantum-like:** Joint condition on M0, P0, H simultaneously.

## How to Run

```python
from edsim.phys import run_full_phase_study

study = run_full_phase_study(n_validate=8)
print(study.report)
```

## Key Finding

The telegraph phase dominates the parameter space (69%) because the
threshold for underdamped oscillation is low.  The diffusion and
reaction phases occupy the H = 0 hyperplane.  The quantum-like phase
is a narrow corner requiring all three conditions simultaneously.
