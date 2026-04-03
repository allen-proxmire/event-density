# ED-Sim-02: ED-Poisson Halo Atlas

## Purpose

Systematic exploration of how the ED mobility parameters (alpha, beta) and velocity dispersion sigma_v determine halo core structure. Tests whether core-widening is robust or fine-tuned, and whether the spiral-galaxy challenge has a solution.

## Key Results

**800 parameter sets** across alpha in [0, 1], beta in [1, 3], sigma_v in [10, 150] km/s.

- **470 sets** produce dwarf-like cores (1-5 kpc)
- Core widening factor ranges from **2.6x to 9.3x** relative to isothermal
- Widening **increases with beta** (stronger degeneracy = wider core)
- Widening is **weakly dependent on alpha**
- Core radius **scales approximately linearly with sigma_v**

## The Core-Widening Mechanism

The ED mobility M(rho) = rho^alpha * (rho_max - rho)^beta caps the maximum density at a value below rho_max where the mobility becomes too small to maintain the isothermal gradient. This caps the central density and forces the core to widen to accommodate the same enclosed mass.

For the canonical ED (alpha=0, beta=2): widening ~ 3-4x, matching the synthesis paper result.

## How to Reproduce

```bash
python data/ED-Sim-02-Halo-Atlas/scripts/run_halo_atlas_v2.py
```

## Files

```
data/ED-Sim-02-Halo-Atlas/
    scripts/run_halo_atlas_v2.py
    results/halo_scan.csv (800 rows)
    results/final_summary.json
    results/final_summary.md
    figures/widening_map_sv30.png
    figures/widening_map_sv100.png
    figures/core_vs_sigma.png
    figures/representative_profiles/rotation_curves.png
```
