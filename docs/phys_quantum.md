# ED-PHYS-05: Quantum-Like Regime Tests

## Purpose

ED-PHYS-05 tests whether the ED PDE, in a high-mobility, low-penalty,
strong-participation regime, produces any transport signatures that
structurally resemble quantum mechanics.

## The Quantum-Like Regime

| Parameter | Value | Role |
|-----------|-------|------|
| M0 | 4.0 | High mobility (4x canonical) |
| P0 | 0.05 | Very weak penalty |
| H | 3.0 | Strong participation (20x canonical) |
| zeta | 0.05 | Low damping |
| D_eff | 0.30 | Fast diffusion |
| Telegraph Q | 5.95 | High-quality oscillation |
| Mobility variation | 36% | Strong nonlinear effect at A=0.1 |

## Three Tested Signatures

### 1. Anomalous Spreading

The density-dependent mobility M(rho) = M0*(rho_max - rho)^beta makes the
effective diffusivity vary across the profile: the peak (high density) has
lower mobility than the tails.  This can produce:

- **Non-Gaussian profiles** (excess kurtosis != 0)
- **Anomalous variance scaling** (<x^2> ~ t^alpha with alpha != 1)

Result: Non-Gaussian profiles detected (kurtosis ~ -1.6).  Variance scaling
is affected by finite-domain effects; longer domains needed for clean
power-law extraction.

### 2. Double-Bump Interference

Two identical bumps are evolved simultaneously and compared to the linear
superposition of two individually evolved bumps.  Any discrepancy measures
nonlinear coupling in the overlap region.

Result: Large overlap error (~98%) detected.  The nonlinear mobility creates
strong coupling between the two bumps that cannot be decomposed as a
linear sum — a classical analogue of wave-function interference.

### 3. Oscillatory Envelope

With strong participation coupling (Q ~ 6), the mean density oscillates
via the telegraph mechanism, creating an oscillatory modulation of the
spreading profile.

Result: Requires T >> period (~16) to observe multiple oscillations.
At shorter times the effect is sub-threshold.

## How to Run

```python
from edsim.phys import run_full_quantum_study

study = run_full_quantum_study(d=2, N=64, T=3.0)
print(study.report)
```

For cleaner oscillatory envelope results, use T >= 30 with dt=1e-3.

## Interpretation

These signatures are **structural analogies**, not quantum mechanics.
The mechanisms are entirely classical:

- Non-Gaussian spreading: density-dependent diffusion (porous-medium effect)
- Nonlinear superposition: state-dependent mobility coupling
- Oscillatory modulation: telegraph-type global feedback

ED has no Planck constant, no superposition principle, no entanglement,
and no measurement problem.
