# ED-Phys-10: Multi-Field ED and Coupled Dynamics

Testing whether a second scalar field with gradient-mediated force coupling can produce waves, inter-peak forces, anisotropy, and horizon penetration.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-09 (canonical pipeline + extensions)
  -> ED-Phys-10 (Multi-Field)  <-- this module
    -> ED-Phys-11 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-10_MultiField.md` | Full analysis: architecture, formulation, 38 experiments, results, scaling laws |
| `ed_phys_multifield.py` | Multi-field simulator with Gradient-Mediated Force (GMF) coupling |
| `results/multifield_results.json` | All quantitative results (38 experiments) |
| `results/2d_multifield_*.npy` | 2D density field snapshots |

## Key Findings

- **Gradient-Mediated Force** selected from 5 candidate coupling architectures
- **No wave propagation** — both fields remain parabolic (diffusive, not wave-like)
- **No inter-peak attraction** — force exists (scales as 3.1*kappa*lambda) but is ~100x too weak to move peaks
- **No anisotropy** — directional phi gradient has zero measurable effect on rho symmetry
- **Horizon penetration confirmed** — phi crosses M(rho)=0 regions via independent diffusion
- **Inflation retardation** — coupling reduces lambda_1 by up to 12% (scales as -48*kappa*lambda)
- **Fundamental insight**: canonical parameter regime is dissipation-dominated; non-dissipative physics requires either hyperbolic field equations or non-perturbative coupling strengths
