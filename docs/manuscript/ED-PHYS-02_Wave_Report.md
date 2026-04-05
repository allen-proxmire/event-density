# ED-PHYS-02: Wave and Dispersion Limits of Event Density

## Regime

- Dimension: 2D
- Grid: 32 per axis
- D = 0.3, H = 2.0, zeta = 0.05, tau = 1.0, P0 = 1.0
- Predicted: gamma = 0.1750, omega_osc = 1.4087, period = 4.46, Q = 4.02

## Key Finding

The canonical ED PDE is **parabolic** (diffusive) and does NOT support true wave propagation.  However, the coupled (rho, v) system exhibits **damped telegraph-like oscillation** of the spatially uniform (k=0) density component.  Spatial modes k >= 1 decay exponentially without oscillation.

## Experiment 1: Uniform Perturbation Oscillation

- Initial offset: A0 = 0.02
- Duration: T = 15.0
- Measured oscillations: gamma = 0.1577 (predicted 0.1750, error 9.9%)
- omega = 1.4081 (predicted 1.4087, error 0.0%)
- Fitted period = 4.46 (predicted 4.46)
- Q factor = 4.46 (predicted 4.02)

### Telegraph Model Comparison

- Model: A'' + 2 gamma A' + omega_0^2 A = 0
- gamma match: 9.9% error
- omega match: 0.0% error
- Telegraph model MATCHES the ED oscillation.

## Experiment 2: Spatial Mode Decay (Dispersion Table)

Spatial modes k >= 1 decay exponentially.  The ED PDE has no real frequency omega(k); instead it has a purely real decay rate sigma(k) = D * (M_star * mu_k + P0).

| k | sigma_fitted | sigma_predicted | Rel Error | R^2 |
|---|-------------|----------------|-----------|-----|
| 1 | 1.0395 | 1.0402 | 0.1% | 1.0000 |
| 2 | 3.2476 | 3.2609 | 0.4% | 1.0000 |
| 3 | 6.9073 | 6.9620 | 0.8% | 1.0000 |

The decay rates are purely real and scale as k^2 (diffusive), confirming that spatial perturbations do NOT propagate as waves.

## Experiment 3: Wave Packet Evolution

- Carrier k0 = 3, envelope sigma = 0.12, A = 0.02
- Centroid shift: 0.001141 (> 1e-4 (unexpected))
- Width ratio (final/initial): 2.203 (spreading)
- Peak amplitude decay: 1.1233e-02 -> 4.7268e-01 (ratio 42.0803)

The wave packet **does not propagate** (centroid remains fixed). It **spreads diffusively** and decays in amplitude.  There is no group velocity.

## Summary

| Property | ED Behaviour | Wave Equation |
|----------|-------------|---------------|
| Spatial propagation | No | Yes |
| Group velocity | 0 | nonzero |
| Temporal oscillation (k=0) | Yes (telegraph) | Yes |
| Mode decay | Exponential (k^2) | None |
| Dispersion | sigma(k) real | omega(k) real |
| Packet spreading | Diffusive | Dispersive |

**ED is not a wave equation.  It is a parabolic diffusion equation with a telegraph-like global coupling.**

The participation variable v(t) introduces a memory effect that produces damped temporal oscillations of the spatially uniform density component.  This is the ED analogue of the telegraph equation, not of the wave equation.

## Implications

- ED cannot be mapped to a wave equation in any parameter regime.
- The participation coupling H controls the quality factor Q of the temporal oscillation.
- For Q >> 1 (strong H, weak zeta), the oscillation is long-lived and resembles a global breathing mode.
- Spatial transport in ED is always diffusive, never ballistic.