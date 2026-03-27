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

Expected time: 30–120 minutes on a single core.

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

1. Create `experiments/invariant_my_new_quantity.py` following the pattern of existing scripts.
2. The script must:
   - Discover runs via `glob("output/runs/regime_D*_A*_Nm*")`
   - Compute the invariant for each run
   - Save figures to `output/figures/invariants/my_new_quantity/`
   - Save a summary JSON
   - Print a summary table with CV and verdict
3. Add the script to `PHASE_4_INVARIANTS` in `reproducibility/run_all.py`.
4. Add the family to `FAMILY_META` in `generate_master_index_and_certificate.py`.
5. Run the pipeline and check the certificate.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: numpy` | `pip install numpy` |
| `No regime_D* runs found` | Run `python experiments/regime_volume_3d.py` first |
| `TIMEOUT` on invariant | Reduce the parameter grid or increase the timeout in `run_all.py` |
| Figures look empty | Check that the runs completed (`metadata.json` → `termination_reason: FinalTime`) |
| Certificate says FAIL | Check which invariants failed in the atlas report |

## Getting Help

The architecture document (`reproducibility/docs/architecture.md`) explains how the pipeline fits together. The invariant map (`reproducibility/docs/invariant_map.md`) lists all 16 families with their inputs and outputs.
