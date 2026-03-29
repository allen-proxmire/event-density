# Event Density

**A structural ontology for physics.**

![Tests](https://github.com/allen/edsim/actions/workflows/tests.yml/badge.svg)
![Certify](https://github.com/allen/edsim/actions/workflows/certify.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![Version](https://img.shields.io/badge/version-0.1.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Event Density (ED) is a foundational framework built on a minimal set of
primitives -- events, becoming, gradients, and flow -- from which physical
dynamics emerge without assuming spacetime, geometry, fields, or curvature.
A single canonical PDE, governed by nine irreducible structural principles,
generates cosmological behaviour, quantum-classical boundaries, galactic
dynamics, and condensed-matter phenomena as architectural consequences of
density evolution.

This repository contains both the **complete ED research programme** (40
physics papers, 31 interpretations, 12 architecture documents) and
**ED-SIM-02**, the second-generation simulation platform that implements,
tests, and demonstrates the ED architecture in 2D, 3D, and 4D.

---

## Quick Start (ED-SIM-02)

```bash
pip install -e .
pytest edsim/tests/ -v          # 112 tests, ~3s
python -m edsim certify          # 9-phase reproducibility pipeline, ~7s
python -m edsim run A_2d_cosine  # run a scenario
```

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series

params, ts = run_atlas(get_scenario("A_2d_cosine"))
summary = summarize_time_series(ts)
print(f"Energy ratio: {summary['energy_ratio']:.4f}")
```

See [edsim/README.md](edsim/README.md) for the full ED-SIM-02 documentation.

---

## Repository Layout

```
Event Density/
    edsim/                  ED-SIM-02 simulation platform (Python package)
        core/               Parameters, operators, integrators, boundary, spectral
        invariants/         Energy, spectral, morphology, dissipation, correlation, topology
        experiments/        Scenarios, sweeps, atlas runner
        reproducibility/    9-phase validation pipeline
        visualization/      Field, invariant, morphology, animation plots
        manuscript/         Auto-generated manuscript + figures
        performance/        Optional Numba/JAX acceleration
        ci/                 CI/CD configuration
        tests/              112 pytest tests (unit + science)
        README.md           ED-SIM-02 documentation

    docs/                   Usage guide, architecture, API reference, performance
    examples/               Lab tour + visual gallery notebooks
    manuscript/             Generated manuscript + figures

    research/               Complete ED research archive
        ED Architecture/    12 layered structural documents
        ED PAPERS/          Core papers, appendices, monograph
        ED Physics/         ED-Phys 01-40: PDE to architectural synthesis
        ED Interpretations/ 31 domain interpretations + 12 essays
        ED Experiments/     Experiment programme, SPARC test
        ED Simulation/      ED-SIM v1 + v2 architecture document
        ED Validation/      P1-P7 reproducibility outputs
        README.md           Archive guide
        archive_index.md    Folder index with file counts and dates

    pyproject.toml          PEP 621 package metadata
    CHANGELOG.md            Semantic versioning changelog
    CONTRIBUTING.md         Contribution guidelines
    requirements.txt        Dependencies
    .github/workflows/      CI/CD: tests, certify, docs
```

---

## Core Ideas

**The PDE.** ED evolves a density field under nonlinear diffusion with
degenerate mobility, a penalty driving the field toward equilibrium, and a
global participation variable providing non-local feedback.

**Nine architectural laws.** Unique attractor, energy monotonicity,
exponential modal decay, factorial complexity dilution, gradient-dissipation
dominance, topological conservation, horizon formation, morphological
hierarchy, and sheet-filament oscillation.

**Full invariant atlas.** At every time step: Lyapunov energy,
ED-complexity, mass, spectral entropy, modal hierarchy, morphology fractions
(blob/sheet/filament/pancake), dissipation channels, correlation length,
structure functions, Euler characteristic, and Betti numbers.

**Dimensions 2-4.** A single API serves d=2, 3, and 4. Two integrators:
implicit Euler (all dimensions) and ETD-RK4 (2D spectral).

---

## Research Archive

All foundational materials are preserved in `research/`. See
[research/README.md](research/README.md) for navigation and
[research/archive_index.md](research/archive_index.md) for the full index.

Key entry points:

- **ED-Phys-40** (`research/ED Physics/ED-Phys-40_Synthesis/`): Architectural synthesis of the full ED-Phys series.
- **ED-Phys-38** (`research/ED Physics/ED-Phys-38_CrossFramework/`): Quantitative comparison to PME, AC, CH, and other PDEs.
- **ED-Phys-39** (`research/ED Physics/ED-Phys-39_HigherDim/`): 4D extension and asymptotic laws.
- **ED-SIM-02 Architecture** (`research/ED Simulation/ED-SIM-02/`): Design document for the simulation platform.

---

## Status

**ED-SIM-02 v0.1.0** (current):
- Solver: 2D/3D/4D implicit Euler + 2D ETD-RK4
- Invariants: 12 families, computed at every snapshot
- Experiments: 6 scenarios, parameter sweeps, atlas runner
- Reproducibility: 9-phase pipeline, structured certificate
- Tests: 112 pytest tests (3s)
- CLI: `edsim info | run | sweep | certify`
- Visualization: fields, invariants, morphology, animations
- Performance: optional Numba/JAX acceleration
- CI/CD: GitHub Actions for tests, certification, docs
