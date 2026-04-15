# Minimal Reproducibility Scenario

## Purpose

The smallest possible end-to-end test of the ED-SIM v1 pipeline. Runs a single regime-volume point, computes one invariant (low-mode collapse), and validates the output.

## Expected Runtime

< 2 minutes on any modern machine.

## Expected Outputs

- `output/runs/regime_D0.1_A0.01_Nm5/` — one simulation run
- `output/figures/invariants/low_mode_collapse/` — one set of figures
- `output/atlas/environment_check.json` — environment report

## Usage

```bash
python reproducibility/scenarios/minimal/run.py
```

## When to Use

- First-time setup verification
- CI/CD smoke tests
- Quick sanity check after code changes
