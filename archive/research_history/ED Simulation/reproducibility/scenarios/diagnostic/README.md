# Diagnostic Scenario

## Purpose

Runs only consistency checks against existing data. Does not launch any new simulations or invariant analyses.

## Expected Runtime

< 30 seconds.

## Checks

1. **Environment** — Python version, required packages, optional packages
2. **Data Integrity** — Run directories, NPZ validity, metadata completeness
3. **Output Validation** — Invariant JSONs, atlas report, certificate

## Usage

```bash
python reproducibility/scenarios/diagnostic/run.py
```

## When to Use

- Debugging a failed pipeline run
- Checking data after a transfer or migration
- Verifying that existing outputs are intact
