# ED-Phys-06: Emergent Phenomena

Targeted high-resolution simulations searching for emergent behavior in the ED cosmological simulator.

## Pipeline Position

```
ED-Phys-01 (Update Rule)
  -> ED-Phys-02 (Simulator)
    -> ED-Phys-03 (Cosmological Timeline)
      -> ED-Phys-04 (Physical Analogues)
        -> ED-Phys-05 (Parameter Sweeps)
          -> ED-Phys-06 (Emergent Phenomena)  <-- this module
            -> ED-Phys-07 (Analytical Theory)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-06_EmergentPhenomena.md` | Full analysis document |
| `ed_phys_emergent.py` | Experiment code: custom ICs, enhanced diagnostics, full suite |
| `results/emergent_phenomena_results.json` | All quantitative results (60+ experiments) |
| `results/2d_filament_g*.npy` | 2D density field snapshots |

## Key Findings

- **6 confirmed phenomena**: peak persistence, basin merging, horizons, mode preservation, Lap=0 dynamics, smooth inflation crossover
- **5 absent phenomena**: traveling waves, oscillons, long-range peak interaction, filaments, sharp bifurcations
- **Fundamental result**: the ED PDE is parabolic (diffusive), producing no wave-like behavior
