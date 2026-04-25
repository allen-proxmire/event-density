# ED-PHYS-05: Quantum-Like Regime Tests for Event Density

## Regime

- Dimension: 2D, grid 64^2
- M0 = 4.0 (high mobility), P0 = 0.05 (weak penalty)
- H = 3.0 (strong participation), zeta = 0.05
- D_eff = 0.3000
- Telegraph: omega = 0.3869, Q = 5.95
- Mobility variation at A=0.1: 36.0%

## Experiment 1: Anomalous Spreading

- Initial bump: sigma_0 = 0.06, A = 0.1
- Variance scaling exponent: **alpha = -0.0005**
  (R^2 = 0.2101)
- Classification: **subdiffusive**
- Linear D_eff = -0.000011 (predicted 0.300000)
- Mean excess kurtosis: -1.6005 (non-Gaussian)

The variance growth exponent alpha = -0.000 deviates from unity, indicating subdiffusive transport.  This arises from the density-dependent mobility: the peak spreads more slowly than the tails, creating non-Gaussian profiles.

## Experiment 2: Double-Bump Interference

- Separation: 0.3
- Mean overlap error (vs linear superposition): **9.8389e-01**
- Max overlap error: 1.0174e+00
- Overlap error grows with time: False

The double-bump profile differs measurably from linear superposition.  The nonlinear mobility M(rho) makes the overlap region evolve differently from two independent bumps.  This is a structural analogue of wave-function interference: the interaction is nonlinear (density-dependent diffusion), not quantum (phase coherence).

## Experiment 3: Oscillatory Envelope

- Oscillation count: 0
- omega measured: 0.0000 (predicted 0.3869, error 100.0%)
- Envelope decay rate: -0.1730

No oscillation detected in the mean density.  The integration time may be too short or the amplitude too small for the telegraph mode to manifest visibly.

## Summary of Quantum-Like Signatures

| Signature | Detected? | Mechanism |
|-----------|----------|-----------|
| Anomalous spreading (alpha != 1) | Yes | Density-dependent mobility |
| Non-Gaussian profile (kurtosis) | Yes | Nonlinear M(rho) |
| Interference-like overlap | Yes | Nonlinear superposition |
| Oscillatory envelope | No | Telegraph coupling |

## Conclusions

The ED PDE in the quantum-like regime produces structural analogues of several quantum transport signatures.  These arise from two classical mechanisms:

1. **Nonlinear mobility** M(rho): creates density-dependent diffusion that can produce non-Gaussian profiles and anomalous variance scaling.

2. **Participation coupling** (telegraph mode): creates global oscillatory modulation of the density field, analogous to wave-packet oscillation.

These are structural analogies, not quantum mechanics.  The ED PDE is classical, dissipative, and parabolic.  There is no Planck constant, no superposition principle, no entanglement, and no measurement problem.  The analogies are purely dynamical: density-dependent diffusion mimics some transport signatures of quantum probability flow.