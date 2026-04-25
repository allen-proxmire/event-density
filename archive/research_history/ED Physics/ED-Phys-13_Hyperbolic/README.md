# ED-Phys-13: Hyperbolic Participation with Regularized Penalty

Testing whether oscillatory participation channels are possible when the low-density singularity is removed (soft-floor penalty) and the time sector is promoted to a hyperbolic form.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-12 (canonical pipeline + penalty redesign)
  -> ED-Phys-13 (Hyperbolic + Soft-Floor)  <-- this module
    -> ED-Phys-14 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-13_Hyperbolic.md` | Full analysis: formulation, stability theory, 8 experiments, architectural findings |
| `ed_phys_hyperbolic.py` | Simulator with parabolic/hyperbolic modes, soft-floor penalty, 8 experiment blocks |
| `results/hyperbolic_results.json` | All quantitative results |
| `results/2d_*.npy` | 2D density field snapshots |

## Key Findings

- **Soft-floor removes ED-Phys-11 instability.** The bounded penalty (P_max = 0.071 at rho=0) eliminates the runaway feedback loop. All 4 parameter regimes are unconditionally stable through 50K steps.
- **Oscillatory dynamics confirmed at short wavelengths.** Single-mode tests (k=0.196, k=0.393) show 21-43 oscillation cycles in density, with period scaling matching linear theory to within 4%.
- **Velocity drain constraint:** zeta must be ~1 to match parabolic drain rate. The damping coefficient is not a free parameter.
- **Long-wavelength modes remain overdamped.** Modes with lambda > ~60 sites are always overdamped regardless of tau. The canonical ED structures (basins, peaks) operate in this regime.
- **Scale hierarchy:** sub-structural scales oscillate, structural scales diffuse. This parallels the phonon/heat-conduction distinction in condensed matter.
- **2D hyperbolic is numerically problematic.** The positivity floor breaks conservation by asymmetrically clipping velocity-driven oscillations.
- **Recommendation:** Combine hyperbolic dynamics with symmetric penalty (ED-Phys-12) for sustained oscillation around a nonzero equilibrium.
