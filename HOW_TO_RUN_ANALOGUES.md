# How to Run the Six Structural Analogues

This document provides step-by-step instructions for running each of the six structural analogues described in the Foundational Paper.

---

## Prerequisites

```bash
pip install -e .
pytest edsim/tests/ -q   # 112 passed
```

All analogues live in `edsim/phys/analogues/`. Each module provides:
- A `predict_*()` function returning the analytical prediction.
- A `run_*_experiment()` function running the full experiment.
- A `build_*_report()` function generating the Markdown report.

Reports are saved to `documents/manuscript/`.

---

## Analogue 1: RC / Debye Relaxation (Penalty Channel)

**Channels:** Penalty only (H = 0, uniform field).

```python
from edsim.phys.analogues.rc_debye import (
    predict_rc, run_rc_debye_experiment, build_rc_debye_report
)

# Analytical prediction
pred = predict_rc(D=0.3, P0=1.0, H=0.0)
print(f"lambda = {pred.lam}, tau_ED = {pred.tau_ed}")

# Full experiment (H=0 decay + H>0 telegraph + amplitude independence)
result = run_rc_debye_experiment()
print(f"lambda error: {result.lambda_error_pct}%")

# Generate report
report = build_rc_debye_report()
with open("documents/manuscript/ED-Analogue-01_RC_Debye_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** lambda = 0.300000, error = 0.00%.

**Falsification check:** lambda must equal D * P0 exactly. Amplitude independence must hold (CV = 0). Telegraph omega must match at all H.

---

## Analogue 2: Barenblatt / PME (Mobility Channel)

**Channels:** Mobility only (P0 ~ 0, H = 0).

```python
from edsim.phys.analogues.barenblatt import (
    predict_barenblatt, run_barenblatt_experiment, build_barenblatt_report
)

# Analytical prediction
pred = predict_barenblatt(beta=1.0)
print(f"m = {pred.m}, alpha_R = {pred.alpha_R}")

# Full experiment (beta=1,2,3 sweep)
result = run_barenblatt_experiment()
for r in result.runs:
    print(f"beta={r.beta}: alpha_R measured={r.alpha_R_measured:.4f}, "
          f"error={r.alpha_R_error_pct:.1f}%")

# Generate report
report = build_barenblatt_report()
with open("documents/manuscript/ED-Analogue-02_Barenblatt_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** beta=1: alpha_R = 0.2496 (1.1% error). Compact support confirmed.

**Falsification check:** Front must propagate at finite speed. No Gaussian tails. Exponent must match m = beta + 1.

---

## Analogue 3: Stefan / Horizon Dynamics (Mobility + Penalty)

**Channels:** Mobility + Penalty (H = 0, large-amplitude bump).

```python
from edsim.phys.analogues.horizon import (
    predict_horizon, run_horizon_experiment, build_horizon_report
)

# Analytical prediction
pred = predict_horizon()
print(f"rho_crit = {pred.rho_crit}, A_c = {pred.A_c}")

# Full experiment (amplitude sweep)
result = run_horizon_experiment()
print(f"A_c measured: {result.A_c_measured}")

# Generate report
report = build_horizon_report()
with open("documents/manuscript/ED-Analogue-03_Horizon_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** A_c predicted = 0.400, measured = 0.410 (2.5% error). Horizon retreats monotonically.

**Falsification check:** No horizon for A <= 0.40. Horizon must form for A >= 0.42. Lifetime must increase with A.

---

## Analogue 4: Telegraph-Modulated Horizons (All Channels)

**Channels:** All three (large-amplitude bump + H > 0).

```python
from edsim.phys.analogues.telegraph_horizon import (
    run_telegraph_horizon_experiment, build_telegraph_horizon_report
)

# Full experiment
result = run_telegraph_horizon_experiment()
print(f"Oscillation detected: {result.oscillation_detected}")

# Generate report
report = build_telegraph_horizon_report()
with open("documents/manuscript/ED-Analogue-04_TelegraphHorizon_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** Oscillation NOT detected. This is the negative result (architectural limit).

**Falsification check:** If oscillation IS detected, the structural constraint analysis is wrong.

---

## Analogue 5: Telegraph-Modulated PME (Mobility + Participation)

**Channels:** Mobility + tiny Penalty (P0 = 0.01) + Participation.

```python
from edsim.phys.analogues.telegraph_pme import (
    predict_telegraph_pme, run_telegraph_pme_experiment,
    build_telegraph_pme_report
)

# Analytical prediction
pred = predict_telegraph_pme(H=50.0, P0=0.01)
print(f"omega_pred = {pred.omega}")

# Full experiment (H sweep)
result = run_telegraph_pme_experiment()
for r in result.runs:
    print(f"H={r.H}: omega_v={r.omega_v:.4f}, omega_delta={r.omega_delta:.4f}")

# Generate report
report = build_telegraph_pme_report()
with open("documents/manuscript/ED-Analogue-05_TelegraphPME_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** omega scales as H^0.52. v-delta frequency match: 0.03%.

**Falsification check:** No oscillation at H = 0. Frequency must track H. v and delta must oscillate at the same frequency.

---

## Analogue 6: Temporal Tension (All Channels)

**Channels:** All three (two peaks, H sweep, d sweep).

```python
from edsim.phys.analogues.temporal_tension import (
    run_temporal_tension_experiment, build_temporal_tension_report
)

# Full experiment
result = run_temporal_tension_experiment()
for r in result.baseline_runs:
    print(f"d={r.d}: drift={r.drift_rate:+.3f}")

# Generate report
report = build_temporal_tension_report()
with open("documents/manuscript/ED-Analogue-06_TemporalTension_Report.md", "w") as f:
    f.write(report)
```

**Expected output:** Baseline repulsion at H = 0 (drift > 0). Telegraph-modulated attraction at H = 2. Oscillatory approach/recession at H = 5.

**Falsification check:** Drift must be positive at H = 0. Drift must correlate with v(t) at H > 0. Drift must decay with distance.

---

## Run All Analogues at Once

```python
from edsim.phys.analogues import rc_debye, barenblatt, horizon
from edsim.phys.analogues import telegraph_horizon, telegraph_pme, temporal_tension

modules = [rc_debye, barenblatt, horizon, telegraph_horizon, telegraph_pme, temporal_tension]
for mod in modules:
    report = mod.build_report() if hasattr(mod, 'build_report') else "N/A"
    print(f"{mod.__name__}: done")
```

---

## Regenerate All Reports

```bash
python -c "
from edsim.phys.analogues.rc_debye import build_rc_debye_report
from edsim.phys.analogues.barenblatt import build_barenblatt_report
from edsim.phys.analogues.horizon import build_horizon_report
from edsim.phys.analogues.telegraph_horizon import build_telegraph_horizon_report
from edsim.phys.analogues.telegraph_pme import build_telegraph_pme_report
from edsim.phys.analogues.temporal_tension import build_temporal_tension_report

reports = {
    'ED-Analogue-01_RC_Debye_Report.md': build_rc_debye_report,
    'ED-Analogue-02_Barenblatt_Report.md': build_barenblatt_report,
    'ED-Analogue-03_Horizon_Report.md': build_horizon_report,
    'ED-Analogue-04_TelegraphHorizon_Report.md': build_telegraph_horizon_report,
    'ED-Analogue-05_TelegraphPME_Report.md': build_telegraph_pme_report,
    'ED-Analogue-06_TemporalTension_Report.md': build_temporal_tension_report,
}
for fname, builder in reports.items():
    with open(f'documents/manuscript/{fname}', 'w') as f:
        f.write(builder())
    print(f'  {fname}: written')
"
```

---

## Verifying Results

Each analogue has explicit falsification criteria. To verify:

1. **Run the experiment** and check that the measured values match the predictions within the stated tolerances.
2. **Run the control** (set the relevant channel parameter to zero) and check that the feature disappears.
3. **Sweep the parameter** and check that the feature scales as predicted.

If any of these checks fails, the analogue is falsified. Report the failure.
