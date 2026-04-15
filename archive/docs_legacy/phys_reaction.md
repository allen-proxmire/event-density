# ED-PHYS-03: Reaction/Source Limit of Event Density

## Purpose

ED-PHYS-03 tests whether the canonical ED PDE, in the strong-penalty regime
with zero participation, behaves as a linear reaction (source/sink) equation.

## The Reaction Regime

For a spatially uniform field, the Laplacian vanishes and the ED PDE reduces to

$$\frac{d\delta}{dt} = -D\,P_0\,\delta, \qquad \delta = \rho - \rho^*,$$

which is pure exponential relaxation with rate $\lambda_{\mathrm{eff}} = D\,P_0$.

The reaction regime uses strong P0 and H = 0:

| Parameter | Value | Role |
|-----------|-------|------|
| D | 0.3 | Diffusion weight |
| P0 | 2.0 | Strong penalty |
| H | 0.0 | No participation |
| lambda_eff | 0.60 | Effective reaction rate |
| e-folding time | 1.67 | 1/lambda |
| Crossover k_c | 0.90 | Reaction-diffusion boundary |

Modes with $k < k_c$ are reaction-dominated; modes with $k > k_c$ are
diffusion-dominated.

## Experiments

### Experiment 1: Uniform Decay

$\rho(x,0) = \rho^* + A$ with $A > 0$.  The field decays exponentially
toward $\rho^*$ at rate $\lambda = D P_0$.

### Experiment 2: Uniform Growth

$\rho(x,0) = \rho^* + A$ with $A < 0$.  The field grows toward $\rho^*$
at the same rate.  "Growth" means increasing $\rho$, not instability —
ED always relaxes toward equilibrium.

### Experiment 3: Localised Source

A Gaussian bump decays (reaction) and spreads (diffusion) simultaneously.
The peak amplitude decays at a combined rate that exceeds the pure
reaction rate because diffusion also removes the peak.

## How lambda_eff Is Extracted

A linear fit of $\ln|\delta(t)|$ vs $t$ gives the slope $-\lambda_{\mathrm{eff}}$.

## Results (2D, N=64, P0=2.0, H=0.0)

| Diagnostic | Value | Predicted | Error |
|------------|-------|-----------|-------|
| lambda (decay) | 0.59982 | 0.60000 | 0.03% |
| lambda (growth) | 0.59982 | 0.60000 | 0.03% |
| Asymmetry | 0.00% | 0% | — |
| R^2 | 1.000 | 1 | — |
| L2 error | 5.8e-13 | 0 | machine precision |

## How to Run

```python
from edsim.phys import run_full_reaction_study

study = run_full_reaction_study(d=2, N=64, T=8.0, P0=2.0)
print(study.report)
```

## How to Interpret Results

**Success** means:
- lambda relative error < 5%
- R^2 > 0.99
- Decay/growth asymmetry < 5%

**Physical interpretation:** The ED penalty P(rho) = P0(rho - rho_star)
acts as a linear restoring force — the ED analogue of a chemical reaction
term, a radiative cooling rate, or an entropic sink.  Unlike nonlinear
reaction kinetics (logistic, bistable), the ED penalty is strictly linear
and produces pure exponential relaxation with no thresholds, no hysteresis,
and no pattern formation.
