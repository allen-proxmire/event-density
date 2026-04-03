# ED-Sim-01: Temporal-Tension Parameter Survey

## Purpose

Systematic parameter-space exploration of the steady-state temporal-tension PDE to determine whether the flat-velocity prediction (V_flat to 1 Mpc) is generic or requires fine-tuning.

## Key Result

**The tension length l_T >> 1 Mpc is necessary but not sufficient.** In 3D spherical symmetry, the Green's function decays as (1/r)*exp(-r/l_T), so T(r) is never flat for a compact source regardless of l_T. Flat V_temp requires either an extended source (sigma > 1 Mpc) or a mechanism beyond the steady-state spherical PDE.

| Source width | Flatness (30-1000 kpc) |
|---|---|
| 5 kpc (galaxy core) | 258% — not flat |
| 200 kpc (galaxy group) | 42% — marginal |
| 1000 kpc (Mpc-scale) | 6.8% — approximately flat |
| 2000 kpc (filament) | 2.7% — flat |

## How to Reproduce

```bash
python data/ED-Sim-01-Temporal-Tension/scripts/run_tension_survey.py
```

## How This Relates to the Synthesis

Section 5 of the synthesis assumed T(r) ~ constant for r << l_T. This is correct in 1D but not in 3D, where geometric dilution (1/r) dominates. ED-Sim-01 identifies this as the most important open theoretical question in the galaxy programme.

## Files

```
data/ED-Sim-01-Temporal-Tension/
    scripts/run_tension_survey.py
    results/parameter_scan.csv (4800 rows)
    results/final_summary.md
    results/final_summary.json
    figures/flatness_map_{gaussian,exponential,tophat}.png
    figures/lengthscale_map.png
    figures/sigma_sensitivity.png
```
