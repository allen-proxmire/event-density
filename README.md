# Event Density

**A single PDE that produces exponential decay, porous-medium fronts, and telegraph oscillation — tested against 10 materials and 61 orders of magnitude in length.**

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/ED_FrontDoor/ED_minimal_demo.ipynb)


## What This Is

Event Density (ED) derives a nonlinear PDE from seven axioms. The PDE has three channels:

- **Mobility** — degenerate diffusion that shuts off at a packing limit, producing sharp fronts
- **Penalty** — relaxation toward equilibrium, producing exponential decay
- **Participation** — global coupling that produces telegraph oscillation at finite speed

These three channels, acting together, reproduce structural features of known physics across five regimes: quantum mechanics, condensed matter, fluid dynamics, galaxy dynamics, and cosmology.

The framework is implemented in a simulation engine (ED-SIM-02) with 148 Python source files, 112 automated tests, and a 9-phase reproducibility pipeline. Everything in this repository is executable and reproducible.

---

## What ED Gets Right

### Condensed matter: 10-material universality

The ED mobility law predicts that diffusion in crowded systems follows:

```
D(phi) = D0 * M0 * (1 - phi/phi_max)^beta
```

This has been tested against 10 chemically distinct materials:

| Material | Type | beta | R² |
|----------|------|------|-----|
| Hard-sphere colloids | Colloid | 1.69 | 0.995 |
| Sucrose-water | Molecular | 2.49 | 0.987 |
| BSA protein | Protein | 2.12 | 0.986 |
| Lysozyme | Protein | 1.36 | 0.998 |
| PMMA colloids | Colloid | 1.81 | 0.994 |
| Ludox silica | Charged colloid | 1.41 | 0.999 |
| PEG-water | Polymer | 1.30 | 0.996 |
| Dextran | Polysaccharide | 1.46 | 0.993 |
| Casein micelles | Bio-colloid | 1.79 | 0.998 |
| Glycerol-water | Small molecule | 1.74 | 0.999 |

**All 10 fit with R² > 0.986.** The mean exponent is beta = 1.72 +/- 0.37. The functional form is universal across colloids, proteins, polymers, polysaccharides, and small molecules. No material has been found that breaks the law.

### Galaxy dynamics: rotation curves and the BTFR

Coupled to gravity (ED-Poisson), the PDE produces:
- Naturally cored dark matter halos (matching observations, unlike NFW cusps)
- The baryonic Tully-Fisher relation with the observed exponent 1/4
- Flat rotation curves extending to 1 Mpc (consistent with weak-lensing data)

### Structural analogues: six for six

Six structural analogues test the three channels against known physics:

1. RC/Debye decay (penalty) — machine-precision match
2. Barenblatt/PME spreading (mobility) — 1-11% error
3. Stefan horizon formation (mobility + penalty) — 2.5% error
4. Telegraph-modulated horizons (all channels) — correct negative result
5. Telegraph-modulated PME (mobility + participation) — 0.03-4% error
6. Temporal tension (all channels) — emergent pair interaction discovered

### Architecture: mathematically proven

- Uniqueness: the seven axioms produce exactly one PDE (proven in ED-Math-01)
- Well-posedness: solutions exist and are unique in 1D/2D/3D
- Nine architectural laws: verified numerically across 2D, 3D, and 4D

### The nine architectural laws

1. **Unique attractor** — The coupled (rho, v) system converges to rho = rho*, v = 0 for all initial conditions. *(partial)*
2. **Monotone energy decay** — The Lyapunov functional E[rho] is non-increasing: dE/dt <= 0. *(derived)*
3. **Spectral concentration** — Spectral entropy decreases as energy concentrates into low-k modes. *(empirical)*
4. **Factorial complexity dilution** — Initial ED-complexity scales as C^(1)/d! with spatial dimension d. *(partial)*
5. **Gradient-dissipation dominance** — The gradient dissipation channel R_grad increases with d, approaching 1 asymptotically. *(derived)*
6. **Topological conservation** — The Euler characteristic of excursion sets is constant in time. *(partial)*
7. **Horizon formation** — Degenerate mobility creates free boundaries when amplitude exceeds a d-dependent threshold. *(empirical)*
8. **Morphological hierarchy** — In d >= 2, Hessian eigenvalues produce stratified morphology (filaments dominate in 3D). *(empirical)*
9. **Sheet-filament oscillation** — In d >= 3, morphology fractions oscillate between sheets and filaments during transients. *(empirical)*

Formal definitions and programmatic verification: `edsim/math/laws.py`

---

## What ED Gets Wrong

### Cosmology: provisionally falsified as a standalone model

The ED PDE, without a gravitational sector, cannot reproduce the observed cosmic expansion history. The penalty channel relaxes too fast (homogeneous limit) or the dilution coupling is incorrectly balanced (spatial limit). Pure ED telegraph cosmology is provisionally falsified.

**What survives:** The synchronization mechanism (local expansion rates coordinating into a coherent global signal) is robust and universal. Three roadmap options are documented: ED-Poisson coupling, alternative scale-factor identification, or hybrid ED-LCDM.

Full details: `documents/research/ED Cosmology/ED-Cosmo-06/`

---

## The Open Test

The most important prediction that has not yet been measured:

**In a FRAP experiment on concentrated BSA protein, the recovery front should expand as R(t) ~ t^0.16, not the Fickian t^0.50.**

This is a zero-free-parameter prediction. The exponent 0.16 is computed from the independently measured beta = 2.12 and the spatial dimension d = 2. A standard confocal microscope with FRAP capability can test this in one afternoon.

The prediction, the synthetic validation, and a complete experimental protocol are documented in:
- `documents/research/ED Physics/ED-Phys-10/` (experiment design)
- `documents/research/ED Physics/ED-Phys-11/` (synthetic validation)
- `documents/research/ED Physics/ED-Phys-12/` (collaboration protocol)
- `outputs/ED-Phys-11/` (simulation results confirming the pipeline works)

If you have access to a confocal microscope and would like to run this test, everything you need is in `documents/research/ED Collaboration/FRAP-Collab-Kit/`.

---

## Reproduce Everything

### Install

```bash
git clone https://github.com/allen-proxmire/event-density.git
cd event-density
pip install -e .
```

### Run the tests

```bash
pytest edsim/tests/ -v          # 112 tests
python -m edsim certify          # 9-phase reproducibility pipeline
```

### Run the analogues

```python
from edsim.phys.analogues.rc_debye import run_full_rc_experiment
from edsim.phys.analogues.barenblatt import run_full_barenblatt_experiment
from edsim.phys.analogues.telegraph_pme import run_full_telegraph_pme_experiment

print(run_full_rc_experiment())
print(run_full_barenblatt_experiment())
print(run_full_telegraph_pme_experiment())
```

### Run a simulation

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series

scenario = get_scenario("A_2d_cosine")
params, ts = run_atlas(scenario)
summary = summarize_time_series(ts)
print(f"Energy ratio: {summary['energy_ratio']:.4f}")
```

---

## Repository Structure

```
event-density/
    edsim/                  148 Python files — the simulation engine
        core/               PDE operators, integrators, boundary conditions
        invariants/         Energy, spectral, morphology, topology, correlation
        experiments/        Scenarios, sweeps, atlas generation
        reproducibility/    9-phase validation pipeline
        phys/analogues/     Six structural analogues
        units/              Physical constants and dimensional mapping
        tests/              112 automated tests

    documents/
        manuscript/         Foundational Paper (Markdown + LaTeX)
        research/           142 research notes across 8 series:
            ED PAPERS/          Core papers (Foundations, Atlas, Math, Synthesis)
            ED Physics/         ED-Phys-01 through 13
            ED Data/            ED-Data-01 through 08 (10-material universality)
            ED Cosmology/       ED-Cosmo-01 through 06
            ED Collaboration/   FRAP experiment collaboration kit

    outputs/                Simulation results (not committed; regenerate locally)
```

---

## Reading Order

Start here:

1. **[What Is ED?](WHAT_IS_ED.md)** — conceptual overview for non-specialists
2. **[Core Papers](CORE_PAPERS.md)** — the four canonical papers in reading order
3. **[How to Run the Analogues](HOW_TO_RUN_ANALOGUES.md)** — reproduce every result
4. **[Reproducing the Foundations Paper](REPRODUCING_FOUNDATIONS_PAPER.md)** — section-by-section reproduction guide

---

## Key Numbers

| Quantity | Value | Source |
|----------|-------|--------|
| Materials tested | 10 | ED-Data-06/07 |
| Mean mobility exponent | 1.72 +/- 0.37 | 10-material fit |
| Best-fit R² (worst material) | 0.986 | BSA protein |
| Best-fit R² (best material) | 0.999 | Ludox silica |
| Automated tests | 112 | `edsim/tests/` |
| Reproducibility phases | 9/9 pass | `python -m edsim certify` |
| Structural analogues | 5 quantitative + 1 negative | Foundational Paper |
| BTFR exponent | 1/4 (predicted and observed) | ED-Data-Galaxy series |
| FRAP exponent (predicted) | 0.160 +/- 0.009 | ED-Phys-10 |
| Dimensional regimes | 5 (quantum to cosmological) | ED-Dimensional series |
| Length scales spanned | 61 orders of magnitude | ED-Dimensional Master Atlas |
| Cosmology status | Provisionally falsified (standalone) | ED-Cosmo-06 |

---

## License

MIT

## Author

Allen Proxmire
