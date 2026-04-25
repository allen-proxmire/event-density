# ED-Phys-11: Non-Dissipative and Strong-Coupling Regimes

Testing whether aggressive (non-perturbative) extensions can access wave-like, strong-force, or anisotropic dynamics beyond the canonical overdamped regime.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-10 (canonical pipeline + extensions + multi-field)
  -> ED-Phys-11 (Non-Dissipative)  <-- this module
    -> ED-Phys-12 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-11_NonDissipative.md` | Full analysis: targets, 3 extensions, 45 experiments, classifications, implications |
| `ed_phys_nondissipative.py` | Three extension simulators (hyperbolic, strong GMF, directional) |
| `results/nondissipative_results.json` | All quantitative results (45 experiments) |
| `results/2d_*.npy` | 2D density and phi field snapshots |

## Key Findings

Three aggressive extensions tested against quantitative targets:

| Extension | Target | Result | Classification |
|-----------|--------|--------|---------------|
| **A: Hyperbolic** (low tau, low zeta) | Waves, oscillations | Runaway density depletion | **UNSTABLE** |
| **B: Strong GMF** (kappa*lambda up to 25) | Inter-peak forces | All runs blow up | **UNSTABLE** |
| **C: Directional** (anisotropic phi) | Anisotropy | **grad_aniso = 0.25 (4:1 bias)** | **MARGINAL (achieved)** |

- **Waves remain inaccessible** -- the rho^(gamma-1) penalty singularity creates runaway depletion when amplified by 1/tau
- **Strong forces remain inaccessible** -- quadratic feedback (force ~ kappa*lambda*rho^2) creates unconditional instability
- **Anisotropy achieved** -- directional phi diffusion + gradient source produces sustained 4:1 gradient directional bias
- **Fundamental insight**: the ED compositional rule produces an intrinsically dissipative system; wave physics requires a new ontological layer
