# Event Density

### A candidate unifying ontology for physical law.

**Event Density (ED) is a single PDE — derived from four primitives and seven axioms — whose structural consequences reproduce known physics without importing it.**

No fitting. No tuning. No borrowed equations. Three constitutive channels produce exponential decay, porous-medium diffusion, and telegraph oscillation as mathematical identities. Nine architectural laws hold across all parameter values and spatial dimensions 1 through 4. The framework spans 61 orders of magnitude in length scale, from quantum to cosmological.

This repository is not a paper. It is a verification platform. Clone it, run it, and see for yourself.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/ED_FrontDoor/ED_minimal_demo.ipynb)

---

## Start Here

The fastest path to understanding ED is to run the minimal demo:

**[ED_FrontDoor/](ED_FrontDoor/)** contains everything you need:

| File | What it does |
|------|-------------|
| **[ED_minimal_demo.ipynb](ED_FrontDoor/ED_minimal_demo.ipynb)** | Run the full ED pipeline in under 3 minutes (Colab or local) |
| [ED_What_It_Does_1pager.md](ED_FrontDoor/ED_What_It_Does_1pager.md) | One-page overview for researchers |
| [ED_Falsifiable_Prediction.md](ED_FrontDoor/ED_Falsifiable_Prediction.md) | The strongest testable prediction, with observational protocol |
| [ED_Targeted_Hooks.md](ED_FrontDoor/ED_Targeted_Hooks.md) | Audience-specific entry points |
| [ED_3min_demo_script.md](ED_FrontDoor/ED_3min_demo_script.md) | Timestamped script for a video walkthrough |

**The ask is simple: run the notebook. Tell me what you see.**

---

## What ED Is

ED starts with a question: *What are the minimal primitives from which physically recognisable structure arises?*

The answer is four objects:

| Primitive | Symbol | Role |
|-----------|--------|------|
| **Density** | rho(x,t) | Bounded scalar field — the state variable |
| **Mobility** | M(rho) = M0(rho_max - rho)^beta | Degenerate diffusion that vanishes at capacity, creating free boundaries |
| **Penalty** | P(rho) = P0(rho - rho*) | Monostable restoring force driving toward a unique equilibrium |
| **Participation** | v(t) | Global feedback variable creating non-local oscillatory dynamics |

Seven structural axioms — locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency — constrain these four primitives into a **unique** canonical PDE. The derivation is not a postulate; the axioms eliminate all alternatives.

The PDE decomposes into three independently testable channels: **mobility** (nonlinear diffusion), **penalty** (exponential relaxation), and **participation** (telegraph oscillation).

**What makes ED different from traditional models:** ED is not fitted to data. It does not import the laws it reproduces. The structural correspondences between ED channels and known physics are built into the constitutive architecture. They hold for *all* parameter values, without tuning.

---

## What ED Does

### Structural Analogues: The Channels Reproduce Known Physics

Each channel, when isolated, reduces to a known physical equation — not approximately, but exactly:

| Channel | Isolated behaviour | Physical correspondence | Accuracy |
|---------|--------------------|------------------------|----------|
| Penalty | Exponential decay | RC-circuit / Debye relaxation | **0.00% error** |
| Mobility | Self-similar spreading | Porous-medium equation (Barenblatt) | **1.1% error** |
| Participation | Damped oscillation | Telegraph / RLC circuit | **0.00% error** |

Nine structural analogues (six in 2D, three in 3D) test these channels and their combinations. Five produce quantitative matches. One produces a scientifically informative negative result. One discovers an emergent pair interaction not predicted by any individual channel.

### Empirical Results

| Domain | Result |
|--------|--------|
| **Condensed matter** | Mobility law fits 10 materials (colloids, proteins, polymers) with R-squared > 0.986. Functional form is universal. |
| **Dwarf galaxies** | Rotation curves match Burkert profiles to 99.6% via degenerate mobility (no dark matter halo). |
| **Spiral galaxies** | NGC 3198 fit at 1.9 km/s RMS with temporal-tension channel. |
| **Weak lensing** | Flat velocity signal at 100-1000 kpc, where both NFW and Burkert fail. Consistent with Mistele et al. (2024). |
| **Tully-Fisher** | Baryonic TF exponent = 1/4 (matching free fit to 0.2 sigma; rejecting LCDM's 1/3 at >3 sigma). |

### The Falsifiable Prediction

**ED predicts that galaxies with higher star-formation activity will have systematically higher rotation velocities at fixed baryonic mass (30-70 km/s shift).** Neither MOND nor LCDM predicts this. Testable now with existing SPARC + GALEX data.

Full details: [ED_FrontDoor/ED_Falsifiable_Prediction.md](ED_FrontDoor/ED_Falsifiable_Prediction.md)

---

## Why ED Is a ToE Candidate

ED is not yet a Theory of Everything. It is a candidate — a constitutive architecture whose structural reach is broad enough to warrant the comparison:

1. **Architectural universality.** The same PDE, with the same constitutive functions, produces dynamics corresponding to known physics across five regimes (quantum, condensed matter, fluid, galactic, cosmological) and 61 orders of magnitude in length scale.

2. **Emergent classical analogues.** The three channels reproduce exponential decay, porous-medium diffusion, and telegraph oscillation without being designed to do so. These are foundational mechanisms of classical physics, emerging from constitutive structure alone.

3. **Parameter-free structure.** The structural correspondences hold for all parameter values. The penalty channel IS exponential decay for any D, P0. The mobility channel IS porous-medium diffusion for any M0, beta. The correspondences are architectural, not parametric.

4. **Nine dimensional laws.** The system obeys nine architectural laws that hold across all tested spatial dimensions (1-4), including monotone energy decay, spectral concentration, topological conservation, and morphological hierarchy.

5. **Falsifiable predictions.** ED makes specific, quantitative, testable predictions that differ from both MOND and LCDM. It can be wrong, and it tells you how to check.

6. **Known limits.** ED does not derive general relativity, quantum mechanics, or the Standard Model. Its horizons are transient, not permanent. Its cosmology is provisionally falsified as a standalone model. These limits are documented, tested, and scientifically informative.

---

## How to Verify ED Yourself

### Run the minimal demo (3 minutes)

Click the Colab badge at the top of this page, or:

```bash
git clone https://github.com/Allen-Proxmire/Event-Density.git
cd Event-Density
pip install -r requirements.txt
jupyter notebook ED_FrontDoor/ED_minimal_demo.ipynb
```

### Run the full test suite

```bash
pip install -e .
pytest edsim/tests/ -v          # 112 tests
python -m edsim certify          # 9-phase reproducibility pipeline
```

### Reproduce the structural analogues

```python
from edsim.phys.analogues.rc_debye import run_full_rc_experiment
from edsim.phys.analogues.barenblatt import run_full_barenblatt_experiment

print(run_full_rc_experiment())       # Penalty channel = RC decay
print(run_full_barenblatt_experiment())  # Mobility channel = PME
```

### Verify the nine architectural laws

```python
from edsim import EDParameters, RunConfig, run_simulation
from edsim.math.laws import verify_all_laws

params = EDParameters(d=2, L=(1.0, 1.0), N=(64, 64))
config = RunConfig(params=params)
ts = run_simulation(config)
results = verify_all_laws(ts, params)
for r in results:
    print(f"Law {r['law']}: {r['name']} — {'PASS' if r['passed'] else 'FAIL'}")
```

---

## Repository Structure

```
Event-Density/
|
|-- ED_FrontDoor/           <-- START HERE
|   |-- ED_minimal_demo.ipynb       Colab-ready demo notebook
|   |-- ED_What_It_Does_1pager.md   One-page overview
|   |-- ED_Falsifiable_Prediction.md  Testable prediction
|   |-- ED_Targeted_Hooks.md        Audience-specific entry points
|   +-- ED_3min_demo_script.md      Video walkthrough script
|
|-- edsim/                  The simulation engine (ED-SIM-02)
|   |-- core/               PDE operators, integrators, boundary conditions
|   |-- math/               Nine architectural laws, formal derivations
|   |-- phys/               Physics regime modules and structural analogues
|   |-- invariants/         Energy, spectral, morphology, topology, correlation
|   |-- experiments/        Scenarios, parameter sweeps, atlas generation
|   |-- reproducibility/    9-phase validation pipeline
|   |-- tests/              112 automated tests
|   |-- units/              Physical constants and dimensional mapping
|   |-- visualization/      Field plots, spectra, animations
|   +-- comparison/         Cross-framework analysis
|
|-- data/                   Empirical datasets (galactic rotation, SFR, SPARC)
|
|-- docs/                   Papers, manuscripts, and technical documentation
|   |-- manuscript/         Foundational paper and analogue reports
|   |-- research/           Research notes across 10 series
|   |-- WHAT_IS_ED.md       Conceptual overview
|   |-- CORE_PAPERS.md      Reading order for canonical papers
|   |-- KEY_FINDINGS_TAKEAWAYS.md   Summary of all results
|   |-- RESULTS_OVERVIEW.md Condensed empirical results
|   +-- HOW_TO_RUN_ANALOGUES.md     Reproduction guide
|
|-- outputs/                Simulation results (regenerate locally)
|
|-- CONTRIBUTING.md         How to contribute
|-- LICENSE                 MIT
|-- pyproject.toml          Package configuration
+-- requirements.txt        Dependencies (numpy, scipy, matplotlib)
```

---

## Papers and Documentation

### Reading order

| # | Paper | What it establishes |
|---|-------|---------------------|
| 1 | [Foundational Paper](docs/manuscript/foundational_paper/) | Axiomatic derivation, six structural analogues, falsification framework |
| 2 | [Dimensional Atlas](docs/research/ED%20PAPERS/) | Five-regime mapping across 61 orders of magnitude |
| 3 | [Mathematical Foundations](docs/math.md) | Uniqueness proof, well-posedness, formal law statements |
| 4 | [Synthesis Paper](docs/research/ED%20PAPERS/) | Cross-regime integration and architectural completeness |

### Key documents

- [What Is ED?](docs/WHAT_IS_ED.md) — Conceptual overview for non-specialists
- [Key Findings](docs/KEY_FINDINGS_TAKEAWAYS.md) — Complete summary of what ED has demonstrated
- [Results Overview](docs/RESULTS_OVERVIEW.md) — Condensed empirical results table
- [How to Run Analogues](docs/HOW_TO_RUN_ANALOGUES.md) — Step-by-step reproduction guide
- [Reproducing the Foundations Paper](docs/REPRODUCING_FOUNDATIONS_PAPER.md) — Section-by-section guide

---

## Key Numbers

| Quantity | Value |
|----------|-------|
| Structural analogues | 9 (6 in 2D, 3 in 3D) |
| RC/Debye match | 0.00% error |
| Telegraph match | 0.00% error |
| Materials tested | 10 (all R-squared > 0.986) |
| Automated tests | 112 |
| Reproducibility phases | 9/9 pass |
| Architectural laws | 9 (verified in dimensions 1-4) |
| BTFR exponent | 1/4 (predicted and observed) |
| Length scales spanned | 61 orders of magnitude |
| Lyapunov functionals | 5 simultaneous (not a gradient flow) |

---

## What ED Does Not Claim

ED does not derive general relativity, quantum mechanics, or the Standard Model. It does not contain gauge fields, fermions, or superposition. Its horizons are transient, not permanent. Its cosmology is provisionally falsified as a standalone model.

These limits are not concealed. They are tested, documented, and published in this repository.

ED claims that a minimal constitutive architecture — without fitting, without tuning, and without importing the laws it reproduces — can generate the mathematical structures that underlie much of classical and continuum physics. Whether this architectural sufficiency reflects something deep about the logical structure of physical law is a question this repository invites you to investigate.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on bug fixes, new analogues, new invariants, documentation, and performance improvements.

## Contact

**Allen Proxmire** — Creator of the Event Density framework

- Repository: [github.com/Allen-Proxmire/Event-Density](https://github.com/Allen-Proxmire/Event-Density)
- To propose experiments, test predictions, or collaborate: open an issue on this repository.

## License

MIT
