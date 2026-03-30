# ED-PHYS-07: Energy, Entropy, and Lyapunov Structure

## Purpose

ED-PHYS-07 tests the energy and entropy structure of the ED PDE:
which functionals are monotone, whether ED is a gradient flow, and
what dissipation inequalities hold.

## Candidate Functionals

| Functional | Formula | H=0 monotone? |
|------------|---------|---------------|
| E_Lyapunov | integral Phi(rho) dV | **Yes (decreasing)** |
| E_gradient | integral |grad rho|^2 dV | **Yes (decreasing)** |
| E_penalty | integral (rho - rho*)^2 dV | **Yes (decreasing)** |
| I_Fisher | integral |grad rho|^2 / rho dV | **Yes (decreasing)** |
| F_free | E_Lyap + kappa * E_grad | **Yes (decreasing)** |
| S_Boltzmann | -integral rho log rho dV | **Yes (increasing)** |
| E_participation | v^2/2 | No |

## Key Findings

1. **Five functionals are monotone decreasing** for H=0, confirming
   the dissipative structure of the ED PDE.

2. **Boltzmann entropy increases** (diffusion increases disorder),
   but is NOT a Lyapunov functional because it is not monotone for
   all initial conditions.

3. **ED is NOT a gradient flow** of E_Lyapunov. The gradient-flow
   operator div(M grad(P/M)) differs from the ED operator
   div(M grad rho) - P by ~995%.

4. For H > 0, the participation coupling can break monotonicity of
   E_Lyapunov by injecting energy into the density field.

## How to Run

```python
from edsim.phys import run_full_energy_study

study = run_full_energy_study(d=2, N=64, H_pos=0.5)
print(study.report)
```

## Gradient-Flow Structure

The H=0 PDE can be written as rho_t = D div(M grad rho) - D P.
The gradient flow of E_Lyapunov would be rho_t = D div(M grad(P/M)).
These are NOT the same because:

    div(M grad rho) != div(M grad(P/M))

The difference is O(|grad rho|^2) from the nonlinear mobility.
ED is dissipative (dE/dt <= 0) but NOT a gradient flow.
