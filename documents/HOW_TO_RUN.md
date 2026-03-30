# How to Run the Experiments

## Prerequisites

```bash
# Python 3.10+
pip install numpy scipy matplotlib pillow

# Verify
python -c "import numpy; import scipy; print('OK')"
```

The ED-SIM-02 solver is in `edsim/`. No external dependencies beyond NumPy and SciPy.

---

## Run the Full Test Suite

```bash
pytest edsim/tests/ -v
# Expected: 112 tests pass
```

## Run the Reproducibility Pipeline

```bash
python -m edsim certify
# Expected: 9/9 phases pass
```

---

## Reproduce the Foundational Paper

Each analogue has a corresponding module with a single entry point:

```python
from edsim.phys.analogues.rc_debye import run_rc_debye_experiment
from edsim.phys.analogues.barenblatt import run_barenblatt_experiment
from edsim.phys.analogues.horizon import run_horizon_experiment
from edsim.phys.analogues.telegraph_horizon import run_telegraph_horizon_experiment
from edsim.phys.analogues.telegraph_pme import run_telegraph_pme_experiment
from edsim.phys.analogues.temporal_tension import run_temporal_tension_experiment

# Example: Analogue 1 (RC/Debye decay)
result = run_rc_debye_experiment()
print(f"lambda predicted: 0.300000")
print(f"lambda measured:  {result.lambda_measured:.6f}")
```

Full instructions: [`REPRODUCING_FOUNDATIONS_PAPER.md`](../REPRODUCING_FOUNDATIONS_PAPER.md)

---

## Reproduce the Condensed-Matter Fits

The three-material universality test (ED-Data-01 through 11):

```python
import numpy as np
from scipy.optimize import curve_fit

# Hard-sphere colloid D(phi) data
phi = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30,
                0.35, 0.40, 0.45, 0.50, 0.54, 0.57])
D   = np.array([1.000, 0.84, 0.72, 0.60, 0.47, 0.36, 0.26,
                0.17, 0.10, 0.050, 0.020, 0.005, 0.001])

def D_ED(phi, phi_max, beta):
    return np.clip(1.0 - phi / phi_max, 1e-12, 1.0) ** beta

popt, _ = curve_fit(D_ED, phi, D, p0=[0.58, 1.9],
                     bounds=([0.5, 0.5], [0.7, 5.0]))
print(f"phi_max = {popt[0]:.3f}, beta = {popt[1]:.3f}")
# Expected: phi_max ~ 0.53, beta ~ 1.60, R² > 0.999
```

---

## Reproduce the Galaxy Halo Fits

The dwarf-galaxy ED–Poisson halo (ED-Data-Galaxy-05, 06):

```python
from edsim.core.parameters import EDParameters
from edsim.units import galactic_scales

params = EDParameters(d=3, L=(1.0, 1.0, 1.0), N=(64, 64, 64))
sc = galactic_scales(params)
print(f"L0 = {sc.L0:.4e} m  (1 kpc)")
print(f"T0 = {sc.T0:.4e} s")
```

The full ED–Poisson solver and dwarf-galaxy comparison are described in:
[`research/ED PAPERS/ED-Data-Galaxy-05_ED_Poisson_Coupled_Halos.md`](research/ED%20PAPERS/ED-Data-Galaxy-05_ED_Poisson_Coupled_Halos.md)

---

## Reproduce the BTFR Fit

```python
import numpy as np
from scipy.optimize import curve_fit

# Mistele et al. (2024) BTFR data
Mb = 10**np.array([10.10, 10.66, 10.96, 11.29])  # Msun
V  = np.array([137.3, 182.1, 204.7, 260.2])       # km/s

def quarter_power(M, A):
    return A * M**0.25

popt, _ = curve_fit(quarter_power, Mb, V)
print(f"A = {popt[0]:.4f}")
print(f"V = {popt[0]:.4f} * Mb^(1/4)")
# Expected: A ~ 0.389, RMS ~ 5.9 km/s
```

---

## Reproduce the Weak-Lensing Comparison

The full pipeline is described in:
[`research/ED PAPERS/ED-Data-Galaxy-10_Fit_to_Mistele_Weak_Lensing_Data.md`](research/ED%20PAPERS/ED-Data-Galaxy-10_Fit_to_Mistele_Weak_Lensing_Data.md)

---

## Build the LaTeX Papers

The synthesis paper and the foundational paper both compile with pdflatex:

```bash
cd manuscript/foundational_paper/
pdflatex ED_Foundational_Paper.tex
pdflatex ED_Foundational_Paper.tex  # second pass for TOC

cd ../research/ED\ PAPERS/
pdflatex ED-Final_Synthesis_EventDensity_Physics.tex
pdflatex ED-Final_Synthesis_EventDensity_Physics.tex
```

No external bibliography files needed.

---

## Expected Numerical Accuracy

| Analogue | Key quantity | Expected accuracy |
|:---------|:-----------|:-----------------|
| RC/Debye | λ = D·P₀ | Machine precision (0.00%) |
| Barenblatt | α_R | 1–11% (resolution-dependent) |
| Horizon | A_c | 2.5% |
| Telegraph PME | ω scaling | 0.03–4% |
| Temporal tension | Drift rates | 5–10% |
| Condensed-matter β | Mean across 3 materials | 2.00 ± 0.29 |
| BTFR exponent | n = 1/(V ∝ M^n) | 0.246 ± 0.025 |
