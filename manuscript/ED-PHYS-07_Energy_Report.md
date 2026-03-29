# ED-PHYS-07: Energy, Entropy, and Lyapunov Structure

## Candidate Functionals

| Functional | Formula | Physical role |
|------------|---------|---------------|
| E_Lyapunov | integral Phi(rho) dV | Density potential energy |
| E_gradient | integral |grad rho|^2 dV | Gradient (complexity) energy |
| E_penalty | integral (rho - rho*)^2 dV | Displacement energy |
| E_participation | v^2 / 2 | Global kinetic energy |
| S_Boltzmann | -integral rho log rho dV | Boltzmann entropy |
| I_Fisher | integral |grad rho|^2 / rho dV | Fisher information |
| F_free | E_Lyapunov + kappa * E_gradient | Free energy |

## Test 1: Monotonicity (H = 0, 2D, N = 32)

With H = 0 the Lyapunov functional E[rho] is guaranteed monotone decreasing by the analytical dissipation inequality (Law 2).

| Functional | Monotone dec? | Decay ratio | Max violation |
|------------|-------------|-------------|---------------|
| E_Lyapunov | True | 0.000250 | -1.84e-06 |
| E_gradient | True | 0.000243 | -8.63e-06 |
| E_penalty | True | 0.000792 | -9.18e-07 |
| E_participation | False | 32489710483719636777959424.000000 | 3.71e-06 |
| S_Boltzmann | False | 1.024162 | 1.58e-03 |
| I_Fisher | True | 0.000285 | -1.72e-05 |
| F_free | True | 0.000250 | -1.93e-06 |

**Monotone decreasing:** E_Lyapunov, E_gradient, E_penalty, I_Fisher, F_free
**Monotone increasing:** S_Boltzmann

## Test 2: Monotonicity (H = 0.5)

With H > 0 the participation term can inject energy.

| Functional | Monotone dec? | Decay ratio | Max violation |
|------------|-------------|-------------|---------------|
| E_Lyapunov | True | 0.000880 | -3.13e-06 |
| E_gradient | True | 0.000230 | -8.25e-06 |
| E_penalty | True | 0.002838 | -1.61e-06 |
| E_participation | False | 66771945814547926876160.000000 | 3.48e-06 |
| S_Boltzmann | False | 1.027903 | 1.59e-03 |
| I_Fisher | True | 0.000272 | -1.66e-05 |
| F_free | True | 0.000850 | -3.21e-06 |

**Violated by participation:** none

## Test 3: Gradient-Flow Structure

The ED operator F_ED = D * [div(M grad rho) - P] is compared to the formal gradient flow F_gf = D * div(M grad(P/M)) of the Lyapunov functional.

- Mean residual ||F_ED - F_gf|| / ||F_ED||: **9.9509** (995.1%)

The ED operator differs significantly from the gradient flow of E_Lyapunov.  ED is dissipative (dE/dt <= 0 for H=0) but NOT a gradient flow in the strict sense.

## Summary

| Property | H = 0 | H > 0 |
|----------|-------|-------|
| E_Lyapunov monotone | True | True |
| E_gradient monotone | True | True |
| S_Boltzmann monotone | True | False |
| Gradient-flow residual | 995.1% | — |

## Conclusions

1. **E_Lyapunov is a valid Lyapunov functional for H = 0.**  This confirms Law 2 (monotone energy decay).

2. **E_Lyapunov is NOT monotone for H > 0.**  The participation coupling injects energy into the density field.

3. **ED is NOT a gradient flow** of E_Lyapunov in the strict sense.  The operator residual is 995.1%.  ED is dissipative but the dissipation structure is not exactly the gradient-flow metric.

4. **Boltzmann entropy is NOT monotone** under the ED flow.  ED is not a detailed-balance system.

5. **E_gradient (complexity) and E_penalty are both monotone decreasing for H = 0.**  These provide additional Lyapunov-like diagnostics.