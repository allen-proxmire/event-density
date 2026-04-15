# Reproducing the Foundations Paper

This document explains how to regenerate every figure, table, and result in:

> **Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues**

The paper source files are in `documents/manuscript/foundational_paper/`:
- `ED_Foundational_Paper.md` — Markdown source
- `ED_Foundational_Paper.tex` — LaTeX source (Overleaf-ready)

---

## Section-to-Module Mapping

| Paper section | Module | Key function |
|---------------|--------|-------------|
| Section 4 (Analogue 1: RC/Debye) | `edsim.phys.analogues.rc_debye` | `run_rc_debye_experiment()` |
| Section 5 (Analogue 2: Barenblatt) | `edsim.phys.analogues.barenblatt` | `run_barenblatt_experiment()` |
| Section 6 (Analogue 3: Horizon) | `edsim.phys.analogues.horizon` | `run_horizon_experiment()` |
| Section 7 (Analogue 4: Telegraph horizon) | `edsim.phys.analogues.telegraph_horizon` | `run_telegraph_horizon_experiment()` |
| Section 8 (Analogue 5: Telegraph PME) | `edsim.phys.analogues.telegraph_pme` | `run_telegraph_pme_experiment()` |
| Section 9 (Analogue 6: Temporal tension) | `edsim.phys.analogues.temporal_tension` | `run_temporal_tension_experiment()` |
| Section 10 (Synthesis tables) | All of the above | `summarize_time_series()` |

---

## Reproducing Individual Tables

### Table 3 (Analogue 1 results)

```python
from edsim.phys.analogues.rc_debye import run_rc_debye_experiment

result = run_rc_debye_experiment()

# lambda (H=0)
print(f"lambda predicted: 0.300000")
print(f"lambda measured:  {result.lambda_measured:.6f}")
print(f"error: {result.lambda_error_pct:.2f}%")

# telegraph omega at various H
for h_res in result.telegraph_results:
    print(f"H={h_res.H}: omega_pred={h_res.omega_pred:.4f}, "
          f"omega_meas={h_res.omega_meas:.4f}")
```

### Table 5 (Analogue 2 results)

```python
from edsim.phys.analogues.barenblatt import run_barenblatt_experiment

result = run_barenblatt_experiment()
for r in result.runs:
    print(f"beta={r.beta}: alpha_R_pred={r.alpha_R_pred:.4f}, "
          f"alpha_R_meas={r.alpha_R_measured:.4f}, "
          f"error={r.alpha_R_error_pct:.1f}%")
```

### Table 6 (Analogue 3 results)

```python
from edsim.phys.analogues.horizon import run_horizon_experiment

result = run_horizon_experiment()
print(f"A_c predicted: {result.A_c_predicted:.3f}")
print(f"A_c measured:  {result.A_c_measured:.3f}")
```

### Table 7 (Analogue 5 results)

```python
from edsim.phys.analogues.telegraph_pme import run_telegraph_pme_experiment

result = run_telegraph_pme_experiment()
for r in result.runs:
    print(f"H={r.H}: omega_pred={r.omega_pred:.4f}, "
          f"omega_v={r.omega_v:.4f}, omega_delta={r.omega_delta:.4f}")
```

### Tables 8-9 (Analogue 6 results)

```python
from edsim.phys.analogues.temporal_tension import run_temporal_tension_experiment

result = run_temporal_tension_experiment()
for r in result.baseline_runs:
    print(f"d={r.d}: drift={r.drift_rate:+.3f}")
for r in result.telegraph_runs:
    print(f"H={r.H}, d={r.d}: drift={r.drift_rate:+.3f}")
```

---

## Regenerating All Reports

Run each analogue's full experiment function. These return report strings:

```python
from edsim.phys.analogues.rc_debye import run_full_rc_experiment
from edsim.phys.analogues.barenblatt import run_full_barenblatt_experiment
from edsim.phys.analogues.telegraph_horizon import run_full_telegraph_horizon_experiment
from edsim.phys.analogues.telegraph_pme import run_full_telegraph_pme_experiment
from edsim.phys.analogues.temporal_tension import run_full_tension_experiment

for name, runner in [
    ("RC/Debye", run_full_rc_experiment),
    ("Barenblatt", run_full_barenblatt_experiment),
    ("Telegraph Horizon", run_full_telegraph_horizon_experiment),
    ("Telegraph PME", run_full_telegraph_pme_experiment),
    ("Temporal Tension", run_full_tension_experiment),
]:
    report = runner()
    print(f"{name}: done ({len(report)} chars)")
```

---

## Running the Reproducibility Pipeline

The ED-SIM-02 reproducibility pipeline validates the core solver and invariant engine:

```bash
python -m edsim certify
```

Expected output: 9/9 phases pass.

---

## Running the Full Test Suite

```bash
pytest edsim/tests/ -v
```

Expected output: 112 tests pass.

---

## Building the LaTeX Paper

The `.tex` file compiles directly in Overleaf or locally:

```bash
cd documents/manuscript/foundational_paper/
pdflatex ED_Foundational_Paper.tex
pdflatex ED_Foundational_Paper.tex  # second pass for TOC
```

No external bibliography files are needed (uses `thebibliography`).

---

## Numerical Accuracy Notes

| Analogue | Key quantity | Expected accuracy |
|----------|-------------|-------------------|
| 1 (RC) | lambda = D * P0 | Machine precision (0.00%) |
| 1 (RLC) | omega, gamma | Machine precision (0.00%) |
| 2 (Barenblatt) | alpha_R | 1-11% (resolution-dependent) |
| 3 (Horizon) | A_c | 2.5% |
| 4 (Telegraph horizon) | Oscillation absent | Qualitative (negative result) |
| 5 (Telegraph PME) | omega scaling | 0.03-4% |
| 6 (Temporal tension) | Drift rates | 5-10% (simulation-dependent) |

Results may vary slightly depending on grid resolution, time step, and platform. The qualitative conclusions (presence/absence of features, scaling directions) are robust.
