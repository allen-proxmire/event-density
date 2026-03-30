# ED-PHYS-02: Wave and Dispersion Limits of Event Density

## Purpose

ED-PHYS-02 tests whether the canonical ED PDE can exhibit wave-like or
dispersive behaviour in any parameter regime.  The answer is nuanced:

- **Spatial propagation:** No.  The ED PDE is parabolic (diffusive).
  All spatial modes decay exponentially.  There is no group velocity.
- **Temporal oscillation:** Yes.  The coupled (rho, v) system produces
  damped telegraph-like oscillations of the spatially uniform (k=0)
  density component when the participation coupling H is strong enough.

## The Wave/Telegraph Regime

The coupled (rho, v) system linearised about (rho_star, 0) yields a
second-order telegraph equation for the spatially uniform perturbation:

$$A_0'' + 2\gamma\,A_0' + \omega_0^2\,A_0 = 0$$

where

$$\gamma = \frac{D\,P_0 + \zeta/\tau}{2}, \qquad
  \omega_0^2 = \frac{D\,P_0\,\zeta + H\,P_0}{\tau}.$$

The system is **underdamped** (oscillatory) when $\omega_0^2 > \gamma^2$,
which requires sufficiently strong participation coupling H:

$$H > \frac{(D\,P_0 - \zeta/\tau)^2\,\tau}{4\,P_0}.$$

For canonical parameters with H = 2.0, zeta = 0.05:
gamma = 0.175, omega_osc = 1.409, period = 4.46, Q = 4.02.

## Experiments

### Experiment 1: Uniform Perturbation Oscillation

A spatially uniform offset rho = rho_star + A is evolved.  The Laplacian
vanishes, leaving only the penalty and participation coupling.  The
domain-averaged density oscillates with the predicted telegraph frequency.

### Experiment 2: Spatial Mode Decay

Individual cosine modes cos(k pi x / L) are evolved with H = 0 to
isolate the pure diffusive decay.  The decay rate is

$$\sigma_k = D\,(M^*\,\mu_k + P_0)$$

which scales as k^2 (diffusive).  There is no oscillation for k >= 1.

### Experiment 3: Wave Packet

A localised oscillatory packet is evolved to test for propagation.
The centroid does not shift (no group velocity); the packet spreads
diffusively and decays.

## How omega(k) Is Extracted

For k = 0: the oscillation frequency is extracted from zero-crossing
intervals of the domain-averaged perturbation A(t) = <rho>(t) - rho_star.
The damping rate is extracted from the Hilbert-transform envelope.

For k >= 1: no frequency exists.  Instead, a decay rate sigma(k) is
fitted from the exponential decrease of the modal amplitude |A_k(t)|.

## Results (2D, N=32, H=2.0)

| Quantity | Fitted | Predicted | Error |
|----------|--------|-----------|-------|
| gamma (k=0) | 0.158 | 0.175 | 9.9% |
| omega (k=0) | 1.408 | 1.409 | 0.0% |
| sigma (k=1) | 1.040 | 1.040 | 0.1% |
| sigma (k=2) | 3.248 | 3.261 | 0.4% |
| sigma (k=3) | 6.907 | 6.962 | 0.8% |

## How to Run

```python
from edsim.phys import run_full_wave_study

study = run_full_wave_study(d=2, N=32, T_osc=15.0, H=2.0)
print(study.report)
```

## How to Interpret Results

**Telegraph match:** If gamma and omega errors are both < 30%, the
telegraph model describes the k=0 oscillation well.

**No wave propagation:** If centroid shift < domain size / 100 and
decay rates scale as k^2, there is no wave-like behaviour.

**ED is parabolic:** The fundamental character of the PDE is diffusive.
The participation coupling adds a global memory (telegraph-like
oscillation) but does not change the local parabolic structure.
