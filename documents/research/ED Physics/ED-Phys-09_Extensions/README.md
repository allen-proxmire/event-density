# ED-Phys-09: Extensions to the Compositional Rule

Testing minimal, ED-consistent extensions to the canonical PDE to address missing physical capabilities.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-08 (canonical pipeline)
  -> ED-Phys-09 (Extensions)  <-- this module
    -> ED-Phys-10 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-09_Extensions.md` | Full analysis: missing physics, proposed extensions, simulation results, implications |
| `ed_phys_extensions.py` | Extension simulator: inertial (wave) and nonlocal kernel extensions |
| `results/extension_results.json` | All quantitative results (50+ experiments) |
| `results/2d_nonlocal_*.npy` | 2D density field snapshots |

## Key Findings

- **5 proposed extensions**, 2 selected and tested (inertial wave, nonlocal kernel)
- **No wave propagation detected** — canonical parameter regime is deeply overdamped
- **No inter-peak forces** — isotropic nonlocal smoothing produces diffusion, not forces
- **Inflation rate modifiable** — nonlocal coupling increases λ₁ by up to 14%
- **Horizons partially accessible** to nonlocal bypass (density transfer across M=0 regions)
- **Fundamental insight**: the wave sector requires not just new terms but a fundamentally different dissipation balance
