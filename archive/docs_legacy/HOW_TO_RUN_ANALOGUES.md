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
- A `run_full_*_experiment()` function running the full experiment and returning a report string.

---

## Analogue 1: RC / Debye Relaxation (Penalty Channel)

**Channels:** Penalty only (H = 0, uniform field).

```python
from edsim.phys.analogues.rc_debye import predict_rc, run_full_rc_experiment

# Analytical prediction
pred = predict_rc(D=0.3, P0=1.0, H=0.0)
print(f"lambda = {pred.lam}, tau_ED = {pred.tau_ed}")

# Full experiment (H=0 decay + H>0 telegraph + amplitude independence)
report = run_full_rc_experiment()
print(report)
```

**Expected output:** lambda = 0.300000, error = 0.00%.

**Falsification check:** lambda must equal D * P0 exactly. Amplitude independence must hold (CV = 0). Telegraph omega must match at all H.

---

## Analogue 2: Barenblatt / PME (Mobility Channel)

**Channels:** Mobility only (P0 ~ 0, H = 0).

```python
from edsim.phys.analogues.barenblatt import predict_barenblatt, run_full_barenblatt_experiment

# Analytical prediction
pred = predict_barenblatt(beta=1.0)
print(f"m = {pred.m}, alpha_R = {pred.alpha_R}")

# Full experiment (beta=1,2,3 sweep)
report = run_full_barenblatt_experiment()
print(report)
```

**Expected output:** beta=1: alpha_R = 0.2496 (1.1% error). Compact support confirmed.

**Falsification check:** Front must propagate at finite speed. No Gaussian tails. Exponent must match m = beta + 1.

---

## Analogue 3: Stefan / Horizon Dynamics (Mobility + Penalty)

**Channels:** Mobility + Penalty (H = 0, large-amplitude bump).

```python
from edsim.phys.analogues.horizon import predict_horizon, run_horizon_experiment

# Analytical prediction
pred = predict_horizon()
print(f"rho_crit = {pred.rho_crit}, A_c = {pred.A_c}")

# Full experiment (amplitude sweep)
result = run_horizon_experiment()
print(f"A_c measured: {result.A_c_measured}")
```

**Expected output:** A_c predicted = 0.400, measured = 0.410 (2.5% error). Horizon retreats monotonically.

**Falsification check:** No horizon for A <= 0.40. Horizon must form for A >= 0.42. Lifetime must increase with A.

---

## Analogue 4: Telegraph-Modulated Horizons (All Channels)

**Channels:** All three (large-amplitude bump + H > 0).

```python
from edsim.phys.analogues.telegraph_horizon import run_full_telegraph_horizon_experiment

# Full experiment
report = run_full_telegraph_horizon_experiment()
print(report)
```

**Expected output:** Oscillation NOT detected. This is the negative result (architectural limit).

**Falsification check:** If oscillation IS detected, the structural constraint analysis is wrong.

---

## Analogue 5: Telegraph-Modulated PME (Mobility + Participation)

**Channels:** Mobility + tiny Penalty (P0 = 0.01) + Participation.

```python
from edsim.phys.analogues.telegraph_pme import predict_telegraph_pme, run_full_telegraph_pme_experiment

# Analytical prediction
pred = predict_telegraph_pme(H=50.0, P0=0.01)
print(f"omega_pred = {pred.omega}")

# Full experiment (H sweep)
report = run_full_telegraph_pme_experiment()
print(report)
```

**Expected output:** omega scales as H^0.52. v-delta frequency match: 0.03%.

**Falsification check:** No oscillation at H = 0. Frequency must track H. v and delta must oscillate at the same frequency.

---

## Analogue 6: Temporal Tension (All Channels)

**Channels:** All three (two peaks, H sweep, d sweep).

```python
from edsim.phys.analogues.temporal_tension import run_full_tension_experiment

# Full experiment
report = run_full_tension_experiment()
print(report)
```

**Expected output:** Baseline repulsion at H = 0 (drift > 0). Telegraph-modulated attraction at H = 2. Oscillatory approach/recession at H = 5.

**Falsification check:** Drift must be positive at H = 0. Drift must correlate with v(t) at H > 0. Drift must decay with distance.

---

## Run All Analogues at Once

```python
from edsim.phys.analogues.rc_debye import run_full_rc_experiment
from edsim.phys.analogues.barenblatt import run_full_barenblatt_experiment
from edsim.phys.analogues.horizon import run_horizon_experiment
from edsim.phys.analogues.telegraph_horizon import run_full_telegraph_horizon_experiment
from edsim.phys.analogues.telegraph_pme import run_full_telegraph_pme_experiment
from edsim.phys.analogues.temporal_tension import run_full_tension_experiment

runners = [
    ("RC/Debye", run_full_rc_experiment),
    ("Barenblatt", run_full_barenblatt_experiment),
    ("Horizon", lambda: run_horizon_experiment()),
    ("Telegraph Horizon", run_full_telegraph_horizon_experiment),
    ("Telegraph PME", run_full_telegraph_pme_experiment),
    ("Temporal Tension", run_full_tension_experiment),
]
for name, runner in runners:
    result = runner()
    print(f"{name}: done")
```

---

## Verifying Results

Each analogue has explicit falsification criteria. To verify:

1. **Run the experiment** and check that the measured values match the predictions within the stated tolerances.
2. **Run the control** (set the relevant channel parameter to zero) and check that the feature disappears.
3. **Sweep the parameter** and check that the feature scales as predicted.

If any of these checks fails, the analogue is falsified. Report the failure.
