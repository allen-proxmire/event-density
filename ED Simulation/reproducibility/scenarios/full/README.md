# Full Reproducibility Scenario

## Purpose

Runs the complete ED-SIM v1 pipeline: all 64 regime volume runs, all 16 invariant families, all 3 meta-analyses, the global atlas report, and the ED Consistency Certificate.

## Expected Runtime

30–120 minutes depending on hardware (single-core). 5–20 minutes on a 16-core workstation.

## Expected Outputs

- `output/runs/regime_D*_A*_Nm*/` — 64 simulation runs
- `output/figures/invariants/*/` — 16 invariant figure directories
- `output/atlas/ED_Attractor_Invariant_Atlas_Report.*` — atlas report
- `output/atlas/MASTER_INDEX.txt` — master index
- `output/atlas/ED_Consistency_Certificate.txt` — final certificate

## Usage

```bash
python reproducibility/scenarios/full/run.py
```

## When to Use

- Full validation of the ED-SIM pipeline
- Generating publication-ready outputs
- Preparing the Atlas for submission
