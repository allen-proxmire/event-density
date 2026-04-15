# Getting Started

This page gets you from a fresh `git clone` to running the canonical Event Density demo and reproducing each of the three flagship results, all in under 10 minutes.

---

## 1. Install

### Requirements

- Python 3.10 or newer
- `numpy`, `scipy`, `matplotlib`, `scikit-learn` (all in `requirements.txt`)

### Local install

```bash
git clone https://github.com/Allen-Proxmire/Event-Density.git
cd Event-Density
pip install -r requirements.txt
```

Verify the install:

```bash
python -c "import numpy, scipy, matplotlib; print('OK')"
```

### Run the test suite (optional, recommended)

```bash
pip install pytest
pytest edsim/tests/ -q
```

Expected: **112 passed in ~5 seconds.** If any test fails, please open an issue with the failure output.

### Run the certify pipeline (optional)

```bash
python -m edsim certify
```

Expected: **9/9 phases pass.**

---

## 2. Run the canonical demo

The fastest path to seeing ED in action is the minimal demo notebook.

### Colab (zero setup)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/ED_FrontDoor/ED_minimal_demo.ipynb)

Click the badge, then `Runtime → Run all`. Total runtime: under 3 minutes.

### Local

```bash
jupyter notebook ED_FrontDoor/ED_minimal_demo.ipynb
```

### Expected output

The notebook runs the canonical 2D ED simulation with default parameters and prints / plots:

- A density field evolving from a cosine perturbation toward equilibrium.
- The penalty channel reproducing exponential (RC / Debye) decay at **0.00% error**.
- The participation channel reproducing telegraph oscillation at **0.00% error**.
- All nine architectural laws verified against the simulation.
- A monotone energy-decay curve with dissipation channels summing exactly to 1.

If you see all of the above, the install is correct and you can proceed to the reproduction notebooks.

---

## 3. Reproduce the three flagship results

Each flagship result has a dedicated notebook in `analysis/notebooks/`. They are independent of each other — you can run them in any order.

### Notebook 02 — Three Channels in Isolation

```bash
jupyter notebook analysis/notebooks/02_three_channels.ipynb
```

**What it does.** Integrates the canonical ED PDE in 1D with each constitutive channel exercised in isolation:

1. **Penalty channel only** (mobility = 0, no participation): exponential decay toward equilibrium. Compared to the analytic solution `ρ(t) = ρ* + (ρ₀ − ρ*) e^(−P₀ t)`.
2. **Mobility channel only** (penalty = 0): degenerate diffusion with M(ρ) = (ρ_max − ρ)^β. Shows compact-support spreading characteristic of the porous-medium equation.
3. **Participation channel only** (decoupled ODE): damped oscillation `τv̈ + ζv̇ + v = 0` with telegraph envelope.

**Expected output.** Three plots showing each channel's signature behaviour, with quantitative comparison to the closed-form analytic solution. Total runtime: ~10 seconds.

### Notebook 03 — Galaxy-15 Merger Lag

```bash
jupyter notebook analysis/notebooks/03_galaxy15_lag.ipynb
```

**What it does.** Reproduces the two key plots of Galaxy-15 (the cluster merger-lag paper):

1. **Velocity-scaling test:** plots observed lensing-BCG offset `ℓ` versus current subcluster velocity `v_current` for the four high-precision clusters (Bullet, El Gordo, MACS J0025, Musket Ball). Performs a power-law fit and prints the slope.
2. **Deceleration test:** plots `ℓ` versus time since pericenter for the seven-cluster sample, overlaid with the ED prediction (monotonic growth) and the SIDM prediction (peak-and-decay).

**Expected output.** Two plots and the printed power-law slope `n = −1.07 ± 0.20` (ED predicts n = −1). Total runtime: ~5 seconds. The plots match Figures 5 and 6 of `papers/galaxy-15/ED-Data-Galaxy-15_First_Evidence_For_Merger_Lag.pdf`.

### Notebook 04 — UDM Mobility Fits

```bash
jupyter notebook analysis/notebooks/04_udm_mobility.ipynb
```

**What it does.** Reproduces the universal-mobility fit `D(c) = D₀(1 − c/c_max)^β` for representative materials from the UDM dataset. Performs nonlinear least-squares fitting on the canonical functional form and prints fitted exponents.

**Expected output.** A composite plot of D(c) versus c/c_max for several materials with overlaid fits, plus a printed table of fitted (β, D₀, R²) per material. Mean β ≈ 1.7, all R² > 0.98. Total runtime: ~3 seconds.

---

## 4. What to read after running

1. **[RESULTS.md](RESULTS.md)** — the unification narrative tying all three results to the single canonical PDE.
2. **[`papers/foundational/`](papers/foundational/)** — the axiomatic derivation.
3. **[`papers/UDM/`](papers/UDM/)** and **[`papers/galaxy-15/`](papers/galaxy-15/)** — the two recent flagship empirical papers.
4. **[ED_FrontDoor/ED_Falsifiable_Prediction.md](ED_FrontDoor/ED_Falsifiable_Prediction.md)** — the strongest currently-untested ED prediction, with an observational protocol you can execute.

---

## 5. Troubleshooting

### `ModuleNotFoundError: No module named 'numpy'`

`pip install -r requirements.txt` did not run successfully. Try:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### `pytest: command not found` or `No module named pytest`

Pytest is optional and not in `requirements.txt`. Install separately:

```bash
pip install pytest
```

### Tests fail on a fresh clone

Open an issue with: your Python version (`python --version`), your platform (`uname -a` or Windows version), and the full output of `pytest edsim/tests/ -v` for at least one failing test. The 112-test suite is checked in CI on every push and is expected to pass on Linux, macOS, and Windows with Python 3.10+.

### Colab notebook errors out

Most often caused by Colab's pre-installed numpy/scipy versions. Add a setup cell at the top:

```python
!pip install --quiet --upgrade numpy scipy matplotlib
```

then `Runtime → Restart runtime → Run all`.

### "Cannot find `papers/galaxy-15/`"

You're on an older clone. Pull the latest:

```bash
git pull origin main
```

The repository was reorganised in early 2026; the old top-level PDFs were moved into `papers/<paper-name>/` subfolders.

### Reproduction notebook outputs differ from the paper

Some notebooks intentionally use a small, fast subset of the full data (so they run in seconds, not minutes). The qualitative behaviour and headline numbers should match within a few percent. If you see a qualitative mismatch (e.g., wrong sign, order-of-magnitude error), please open an issue.

---

## 6. Where to go next

- **Reproduce a falsifiable prediction** — see [`ED_FrontDoor/ED_Falsifiable_Prediction.md`](ED_FrontDoor/ED_Falsifiable_Prediction.md). The strongest currently-untested ED prediction (activity-dependent rotation velocities) can be tested *today* with existing SPARC + GALEX data.
- **Read the canonical PDE derivation** — [`papers/foundational/`](papers/foundational/).
- **Understand the cross-regime atlas** — [`papers/ED-Dimensional-Master_The_Unified_Atlas.md`](papers/ED-Dimensional-Master_The_Unified_Atlas.md).
- **Contribute** — see [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports, new analogues, new test cases, and documentation improvements are all welcome.
