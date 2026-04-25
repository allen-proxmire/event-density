# ED-PHYS-01: ED as an Effective Diffusion Equation

## Purpose

ED-PHYS-01 is the first physics experiment in the Event Density programme.
It tests whether the canonical ED PDE, in a suitable parameter regime,
behaves like the linear heat (diffusion) equation with a well-defined
effective diffusion coefficient.

## The Diffusion Regime

The canonical ED operator is

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho).$$

When the perturbation $\delta\rho = \rho - \rho^*$ is small, the mobility
is approximately constant $M(\rho) \approx M^* = M_0(\rho_{\max} - \rho^*)^\beta$,
the gradient-coupling term $M'|\nabla\rho|^2$ is $O(\delta\rho^2)$, and the
penalty $P(\rho) = P_0\,\delta\rho$ is a slow linear decay.

If we additionally set $P_0 \ll D M^* \pi^2/L^2$ (weak penalty) and $H = 0$
(no participation), the PDE reduces to

$$\partial_t\rho \approx D\,M^*\,\nabla^2\rho = D_{\mathrm{eff}}\,\nabla^2\rho.$$

This is the heat equation with effective diffusion coefficient
$D_{\mathrm{eff}} = D \cdot M^*$.

The `edsim.phys.diffusion_regime` module constructs this regime with
canonical defaults:

| Parameter | Value | Role |
|-----------|-------|------|
| D | 0.3 | Diffusion weight |
| M0 | 1.0 | Mobility prefactor |
| beta | 2.0 | Mobility exponent |
| rho_star | 0.5 | Equilibrium density |
| rho_max | 1.0 | Capacity bound |
| P0 | **0.01** | Weak penalty |
| H | **0.0** | No participation |
| M_star | 0.25 | M(rho_star) = 0.5^2 |
| D_eff | **0.075** | D * M_star |

## Experiments

### Experiment 1: Gaussian Spread

A Gaussian bump $\rho(x,0) = \rho^* + A\,\exp(-|x-x_c|^2/2\sigma_0^2)$
is centred in the domain and evolved. The heat equation predicts:

- Variance: $\langle x^2\rangle(t) = \sigma_0^2 + 2\,d\,D_{\mathrm{eff}}\,t$
- Peak: $A(t) = A_0\,(\sigma_0/\sigma(t))^d$ with $\sigma(t)^2 = \sigma_0^2 + 2D_{\mathrm{eff}}t$

### Experiment 2: Step Relaxation

A smoothed step $\rho(x,0) = \rho^* + \delta\,\tanh((x - L/2)/w)$ is
evolved. The heat equation predicts an error-function profile at later times:

$$\rho(x,t) = \rho^* + \delta\,\mathrm{erf}\!\left(\frac{x - L/2}{\sqrt{2w^2 + 4D_{\mathrm{eff}}t}}\right).$$

## How D_eff Is Extracted

A linear least-squares fit of $\langle x^2\rangle(t)$ vs $t$ from the
Gaussian experiment gives slope $= 2\,d\,D_{\mathrm{eff}}$, from which
$D_{\mathrm{eff}}$ is extracted. The goodness of fit is measured by $R^2$.

## Results (Canonical 2D, N=64)

| Quantity | Value |
|----------|-------|
| Fitted D_eff | 0.0694 |
| Predicted D_eff | 0.0750 |
| Relative error | 7.5% |
| Variance R^2 | 0.998 |
| Gaussian mean L2 error | 3.9e-02 |
| Step mean L2 error | 1.8e-02 |

The fitted value is 7.5% below the prediction, consistent with the
$O(A^2)$ mobility correction and the weak-penalty drift.

## How to Run

```python
from edsim.phys import run_full_diffusion_study

study = run_full_diffusion_study(d=2, N=64, T=0.3)
print(study.report)
```

## Interpreting Success and Failure

**Success** means:
- D_eff relative error < 15%
- Variance fit R^2 > 0.95
- Step mean L2 error < 0.2

**Failure** indicates that nonlinear terms (mobility variation, penalty
drift, or boundary reflections) are too large for the diffusion
approximation to hold. This can occur with:
- Large amplitude A (mobility strongly nonlinear)
- Large P0 (penalty dominates diffusion)
- Long integration time (boundary reflections accumulate)
- Small domain relative to the Gaussian width (finite-size effects)
