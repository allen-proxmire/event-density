# analysis/

Unified figure generation for the ED-SIM pipeline.

## Scripts in This Directory

- `generate_all_figures.py` — Master figure pipeline. Produces all nine
  monograph figures from the regime-volume runs.

## Per-Experiment Analysis Scripts

The nine `analyze_*.py` scripts live in the parent directory (`ED Simulation/`),
not here. Each corresponds to a specific experiment and produces figures
for that experiment only:

    analyze_three_stage_I.py
    analyze_modal_hierarchy.py
    analyze_triad_cascade.py
    analyze_overlap_cascade.py
    analyze_broadband_cascade.py
    analyze_low_mode_attractor.py
    analyze_parameter_sweep.py
    analyze_regime_map_2d.py
    analyze_regime_volume_3d.py

## When to Use Which

There are two figure-generation paths. They are complementary, not
redundant:

| Script | Purpose | Output |
|--------|---------|--------|
| `generate_all_figures.py` | **Publication.** Produces the 9 monograph figures (energy-entropy, Lyapunov, regime maps, etc.) from the full regime-volume data. This is what `run_all.py` and `make figures` call. | `output/figures/*.png` |
| `analyze_*.py` (9 scripts) | **Diagnostics.** Each produces per-experiment figures (modal funnels, triad cascades, attractor portraits, etc.) for a single experiment. Use these when debugging or exploring a specific run. | `output/figures/<experiment>/*.png` |

To generate all publication figures at once, use `generate_all_figures.py`
from this directory. To generate diagnostic figures for a single
experiment, use the corresponding `analyze_*.py` from the parent
directory.

---

See the [ED Simulation README](../README.md) for the full pipeline overview,
or the [root README](../../README.md) for the complete project structure.
