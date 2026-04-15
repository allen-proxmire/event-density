# ED-Phys-14: Oscillatory Participation with Restoring Penalty

Combines hyperbolic time evolution (ED-Phys-13) with the symmetric restoring penalty (ED-Phys-12) to test whether ED supports oscillatory participation channels around a maintained equilibrium.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-13 (canonical pipeline + penalty + hyperbolic)
  -> ED-Phys-14 (Oscillatory Participation)  <-- this module
    -> ED-Phys-15 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-14_Oscillator.md` | Full analysis: combined formulation, linear theory, 6 experiments, ontological implications |
| `ed_phys_oscillator.py` | Simulator with hyperbolic+symmetric mode, 6 experiment blocks |
| `results/oscillator_results.json` | All quantitative results |
| `results/2d_*.npy` | 2D density field snapshots |

## Key Findings

- **True equilibrium maintained.** rho_mean = rho_star to machine precision in all runs. Zero drain. First module with non-dissipative background dynamics.
- **Oscillation at ALL wavelengths.** Unlike ED-Phys-13 (short-wave only), the symmetric penalty enables oscillation from lambda=8 to lambda=512 (the full grid). The ED-Phys-13 scale hierarchy is completely eliminated.
- **85 oscillation cycles** achieved (R2, mode n=32, 100K steps). Damping ratio 0.030-0.049 — long-lived but not sustained.
- **Period matches linear theory to <1%.** Measured periods agree with T = 2*pi*sqrt(tau/K_eff) after correcting for the rho_std factor-of-2 (|cos(wt)| oscillates at 2w).
- **Zero positivity clips** in all 1D and 2D runs. The symmetric penalty keeps density near rho_star, eliminating the positivity-floor artifact from ED-Phys-13.
- **Perfect restoring recovery** from 0.5*rho_star and 1.5*rho_star with classical underdamped overshoot and ringing.
- **2D works cleanly** for small/moderate perturbations (radial: 1 oscillation, directional: 9 oscillations). Large random perturbations show density growth from nonlinear penalty asymmetry.
- **rho_star defines a "participation equilibrium layer"** — a density where participation is self-sustaining, with oscillatory restoration of perturbations.
