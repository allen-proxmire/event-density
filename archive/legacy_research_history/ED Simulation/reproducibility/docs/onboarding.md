# ED-SIM v1 Onboarding Guide

## Welcome

This guide walks you through running the ED-SIM v1 reproducibility suite for the first time.

## Prerequisites

- Python >= 3.10
- `pip install numpy scipy matplotlib`
- The ED Simulation repository cloned locally

## Step 1: Verify Your Environment

```bash
cd "ED Simulation"
python reproducibility/checks/check_environment.py
```

You should see all required packages marked `[PASS]`. Optional packages are nice-to-have but not required.

## Step 2: Run the Minimal Scenario

Start with the smallest test to make sure everything works:

```bash
python reproducibility/scenarios/minimal/run.py
```

This runs one simulation, one invariant, and one validation. Takes < 2 minutes.

## Step 3: Run the Full Pipeline

If the minimal scenario passes:

```bash
python reproducibility/run_all.py
```

This runs all 64 regime-volume simulations, all 16 invariant analyses, the meta-analyses, and generates the ED Consistency Certificate.

Expected time: approximately 2-4 hours on a single core for the full
64-point sweep. Faster hardware or fewer parameter points will reduce this.

## Step 4: Review Outputs

After the pipeline completes:

```
output/
    atlas/
        ED_Consistency_Certificate.txt   ← The final verdict
        MASTER_INDEX.txt                 ← Index of all outputs
        ED_Attractor_Invariant_Atlas_Report.txt
    figures/
        invariants/
            low_mode_collapse/           ← Figures for each family
            mode_energy_ratios/
            ...
    runs/
        regime_D0.05_A0.005_Nm5/         ← Raw simulation data
        ...
```

## Step 5: Interpret the Certificate

Open `output/atlas/ED_Consistency_Certificate.txt`. The key items:

- **Final verdict**: PASS / PARTIAL / FAIL
- **Universality score U**: how similar invariants are across regimes (U > 0.9 = good)
- **Consistency score C**: how well invariants agree with each other (C > 0.8 = good)
- **Stability**: number of positive Lyapunov exponents (should be 0 for a stable attractor)

## How to Add a New Invariant

Use `invariant_spectral_entropy.py` as the canonical example pattern.

1. Create `experiments/invariant_my_new_quantity.py` following its structure.
2. The script must:
   - Discover runs via `glob("output/runs/regime_D*_A*_Nm*")`
   - Skip inadmissible runs: `if meta.get("inadmissible", False): continue`
   - Compute the invariant for each run
   - Save figures to `output/figures/invariants/my_new_quantity/`
   - Save a summary JSON (see Required Output Format below)
   - Print a summary table with CV and verdict
3. Add the script to `PHASE_4_INVARIANTS` in `reproducibility/run_all.py`.
4. Add the family to `FAMILY_META` in `generate_master_index_and_certificate.py`.
5. Run the pipeline and check the certificate.

### Required Output Format

Each invariant script must save a summary JSON with the following
structure. The `generate_global_atlas_report.py` and the meta-analysis
scripts depend on this contract.

**Required fields** (note: `n_runs` is the number of admissible runs
processed, which may be fewer than the 64 total if some are inadmissible):

```json
{
  "family": "my_new_quantity",
  "n_runs": 48,
  "n_converged": 45,
  "frac_converged": 0.9375,
  "global_stats": {
    "mean": 0.1234,
    "std": 0.0056,
    "min": 0.1102,
    "max": 0.1389,
    "CV": 0.0454,
    "verdict": "INVARIANT"
  },
  "per_run": [
    {
      "D": 0.05, "A": 0.005, "Nm": 10,
      "value": 0.1198,
      "sigma": 0.0312,
      "R2": 0.987,
      "converged": true
    }
  ]
}
```

**Required fields explained:**
- `family`: string identifier matching the script name (without `invariant_` prefix)
- `n_runs`: number of admissible runs processed
- `n_converged`: number of runs where the invariant converged (R^2 > 0.95)
- `frac_converged`: `n_converged / n_runs`
- `global_stats.mean/std/min/max`: statistics of the invariant value across runs
- `global_stats.CV`: coefficient of variation (`std / mean`)
- `global_stats.verdict`: one of `"INVARIANT"` (CV < 5%), `"WEAKLY INVARIANT"` (CV < 15%), `"NOT INVARIANT"` (CV >= 15%)
- `per_run`: array of per-run results with parameters, value, convergence rate, and flag

**Optional fields:**
- `description`: human-readable description of the invariant
- `theorem_ref`: reference to the Appendix C theorem being tested
- `figures`: list of generated figure filenames

---

## How to Add a New Experiment

1. Create `experiments/my_experiment.py` in the experiments directory.
   Follow the naming convention: lowercase, underscores, descriptive.
2. The script must:
   - Import from the core solver: `from edsim_parameters import ...`,
     `from edsim_runner import ...`, `from edsim_core import ...`
   - Use `sys.path.insert(0, parent_dir)` to resolve imports
     (see any existing experiment for the pattern).
   - Save outputs to `output/runs/<experiment_name>/` with
     `time_series.npz` and `metadata.json`.
3. Optionally create a matching `analyze_<experiment>.py` at the root
   of `ED Simulation/` for per-experiment diagnostic figures.
4. Add the script to `PHASE_3_RUNS` in `reproducibility/run_all.py`
   if it should run as part of the full pipeline.

---

## How to Add a New Figure

There are two figure paths:

**Publication figures** (for the monograph):
- Edit `analysis/generate_all_figures.py`.
- Add a new function following the pattern of the existing `figure_*`
  functions.
- The figure is saved to `output/figures/` and called by `make figures`
  and `run_all.py` Phase 9.

**Diagnostic figures** (for per-experiment debugging):
- Create or edit `analyze_<experiment>.py` at the root of
  `ED Simulation/`.
- Each script loads runs for its specific experiment and saves figures
  to `output/figures/<experiment>/`.
- These scripts are not called by the pipeline; run them manually.

See `analysis/README.md` for more detail on the distinction.

---

## How to Add a New Meta-Analysis

Meta-analyses (Layer 4) operate on the outputs of all Layer 3 invariant
scripts. They aggregate invariant summaries across runs into global
synthesis metrics.

1. Create `experiments/invariant_my_meta.py` in the experiments directory.
   Use the `invariant_` prefix for consistency with the discovery pattern.
2. Add a 4-line Layer 4 comment block at the top of the file (see the
   existing meta-analysis scripts for the template).
3. The script must:
   - Load summary JSONs produced by Layer 3 invariant scripts
   - Compute a global synthesis metric (e.g., a score, a distance matrix)
   - Save a summary JSON and figures following the same contract as Layer 3
4. Register the script in `PHASE_5_META` (not `PHASE_4_INVARIANTS`) in
   `reproducibility/run_all.py`.
5. See the three existing meta-analyses for the canonical pattern:
   `invariant_parameter_universality.py`, `invariant_cross_consistency.py`,
   `invariant_embedding_map.py`.

---

## Run Output Schema

Every experiment script must produce two files per run: `time_series.npz`
and `metadata.json`. The invariant scripts depend on these fields.

### time_series.npz

| Key | Shape | Description |
|-----|-------|-------------|
| `t` | `(n_steps,)` | Time array |
| `v` | `(n_steps,)` | Participation variable |
| `E_total` | `(n_steps,)` | Total energy |
| `E_potential` | `(n_steps,)` | Potential energy |
| `E_kinetic` | `(n_steps,)` | Kinetic energy |
| `D_gradient` | `(n_steps,)` | Gradient dissipation channel |
| `D_penalty` | `(n_steps,)` | Penalty dissipation channel |
| `D_participation` | `(n_steps,)` | Participation dissipation channel |
| `D_total` | `(n_steps,)` | Total dissipation |
| `C_ED` | `(n_steps,)` | Bare ED-complexity |
| `C_ED_eff` | `(n_steps,)` | Effective ED-complexity |
| `mass` | `(n_steps,)` | Total mass |
| `margin` | `(n_steps,)` | Proximity to horizon (rho_max - max(rho)) |
| `M_min` | `(n_steps,)` | Minimum mobility |
| `rho_max_local` | `(n_steps,)` | Local maximum density |
| `modal_amplitudes` | `(n_steps, N_obs)` | Modal coefficients in the Neumann eigenbasis |

### metadata.json

| Field | Type | Description |
|-------|------|-------------|
| `run_id` | string | Unique run identifier |
| `D` | float | Direct-channel weight |
| `A_per_mode` | float | Amplitude per seeded mode |
| `Nm` | int | Number of seeded modes |
| `seeded_modes` | list[int] | Which modes were seeded |
| `zeta` | float | Participation damping rate |
| `tau` | float | Participation time scale |
| `rho_star` | float | Equilibrium density |
| `rho_max` | float | Capacity bound |
| `N` | int | Grid points |
| `dt` | float | Time step |
| `T` | float | Final time |
| `method` | string | Time-stepping method |
| `inadmissible` | bool | True if the run violated positivity or capacity |
| `effective_regime` | string | Regime classification (oscillatory/overdamped/critical/inadmissible) |
| `discriminant_Delta` | float | Discriminant value |
| `termination_reason` | string | FinalTime / Converged / NaN_detected |
| `wall_time_s` | float | Wall-clock time in seconds |
| `source` | string | Pipeline identifier (e.g., "edsim-v1") |

### Sample files

See `reproducibility/examples/sample_metadata.json` for a complete
metadata example, and `reproducibility/examples/sample_invariant.json`
for a complete invariant output example.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: numpy` | `pip install numpy` |
| `No regime_D* runs found` | Run `python experiments/regime_volume_3d.py` first |
| `TIMEOUT` on invariant | Reduce the parameter grid or increase the timeout in `run_all.py` |
| Figures look empty | Check that the runs completed (`metadata.json` -> `termination_reason: FinalTime`) |
| Certificate says FAIL | Check which invariants failed in the atlas report |

---

## Getting Help

The architecture document (`reproducibility/docs/architecture.md`) explains how the pipeline fits together. The invariant map (`reproducibility/docs/invariant_map.md`) lists all 16 families with their inputs and outputs.

---

See the [reproducibility README](../README.md), the [ED Simulation README](../../README.md), or the [root README](../../../README.md) for project navigation.
