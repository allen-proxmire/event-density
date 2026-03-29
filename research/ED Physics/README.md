# ED Physics

The computational physics pipeline of the Event Density framework.

This folder contains ED-Phys: a thirty-four-module simulation and analysis
pipeline that derives, implements, and verifies the physical dynamics of
the ED canonical PDE entirely from the ED ontology. No physics is imported
from outside the framework. Every equation, parameter, and prediction flows
from the single compositional rule and its continuum limit.

---

## Role in the ED Program

The ED Architecture defines the seven structural principles. The Rigour
Paper proves them mathematically. ED-Phys answers the physical question:
*what dynamics does the canonical PDE actually produce?*

Starting from the ED system triple (E, C, rho) and the five foundational
axioms, ED-Phys derives the update rule, implements a modular simulator,
runs the canonical cosmological experiments, maps the parameter space,
identifies emergent phenomena, and develops the analytical theory — all in
a strict derivation chain with no external imports. The pipeline
demonstrates that ED reproduces inflation-like smoothing, structure
formation, horizon dynamics, and late-time flattening as generic
consequences of the compositional rule.

ED-Phys is the precursor to ED-SIM (in `ED Simulation/`). Where ED-Phys
explores the physics of the ED equation, ED-SIM provides the rigorous
numerical infrastructure, the sixteen-family invariant atlas, and the
architectural consistency certificate.

---

## Pipeline Architecture

The thirty-four modules fall into five groups: core derivation (01–08),
extensions and variants (09–19), robustness and stress testing (20–28),
global analysis (29–33), and unified verification (34).

### Core Pipeline (01–08)

The first eight modules form a strict derivation chain. Each depends on
the outputs of the previous.

| Module | Title | Content |
|--------|-------|---------|
| 01 | Update Rule | Derivation of the canonical PDE from the compositional rule. Discretization, stability analysis, and the finite-difference scheme. |
| 02 | Simulator | Modular Python implementation: lattice engine, operators, diagnostics, configuration. |
| 03 | Cosmological Timeline | Three baseline experiments (1D inflation, 1D structure formation, 2D cosmology) producing the four-epoch timeline: inflation, residual gradients, structure formation, heat death. |
| 04 | Physical Analogues | Eight mappings from ED quantities to standard physics: density to matter, gradients to forces, mobility to transport, penalty to restoring potential. |
| 05 | Parameter Sweeps | 135 simulations across three sweep dimensions. Phase diagrams and regime classification. |
| 06 | Emergent Phenomena | Phenomena not put in by hand: spontaneous structure, horizon formation, oscillator death, pattern selection. |
| 07 | Analytical Theory | Scaling laws, eigenvalue analysis, stability conditions. Eight quantitative scaling laws validated against 200+ simulations. |
| 08 | Documentation | Master Document (full pipeline synthesis), Public Summary, and module index. |

### Extensions and Variants (09–19)

Modules exploring modifications and generalizations of the canonical PDE.

| Module | Title | Content |
|--------|-------|---------|
| 09 | Extensions | Beyond the canonical single-field system: boundary variations, source terms, higher dimensions. |
| 10 | Multi-Field | Coupled density fields: multi-species dynamics, cross-field interactions. |
| 11 | Non-Dissipative | Removing dissipation: what survives when the Lyapunov structure is broken. |
| 12 | Penalty | Penalty function variations: linear, quadratic, saturating, non-monotone. |
| 13 | Hyperbolic | Replacing parabolic diffusion with wave-like propagation: the hyperbolic ED variant. |
| 14 | Oscillator | The homogeneous ED oscillator: the ODE subsystem governing the participation variable. |
| 15 | Symmetric Denominator | Symmetric mobility functions and their effect on horizon geometry. |
| 16 | Coupled Oscillators | Multiple participation variables with inter-channel coupling. |
| 17 | Oscillator Cosmology | The oscillator subsystem applied to cosmological dynamics. |
| 18 | Hybrid Cosmology | Mixed parabolic-hyperbolic systems combining diffusive and wave-like sectors. |
| 19 | Unified Cosmology | The full unified cosmological equation integrating all sectors. |

### Robustness and Stress Testing (20–28)

Systematic verification that the architectural signatures survive
perturbation, parameter variation, and extreme conditions.

| Module | Title | Content |
|--------|-------|---------|
| 20 | Oscillator Death | Conditions under which oscillatory behavior collapses to monotonic decay. |
| 21 | Amplitude Sweep | Response to amplitude variation across the full dynamic range. |
| 22 | Horizon D-Sweep | Horizon behavior under diffusion-coefficient variation. |
| 23 | 2D Oscillatory | Oscillatory dynamics in two spatial dimensions. |
| 24 | Triad Map 2D | Two-dimensional triad coupling structure and mode interactions. |
| 25 | Penalty Robustness | Architectural stability under penalty function perturbation. |
| 26 | Mobility Robustness | Architectural stability under mobility function perturbation. |
| 27 | Participation Robustness | Architectural stability under participation parameter variation. |
| 28 | Stress Test | Combined extreme-parameter runs testing the limits of the architecture. |

### Global Analysis (29–33)

Modules mapping the global structure of the ED dynamical system.

| Module | Title | Content |
|--------|-------|---------|
| 29 | Attractor Map | Global attractor structure across the parameter space. |
| 30 | Stability Manifold | The manifold of stable equilibria and its geometry. |
| 31 | Parameter Geometry | Geometric structure of the parameter space: regime boundaries, critical surfaces, degeneracies. |
| 32 | Global Phase Portrait | The full phase portrait of the ED system across all regimes. |
| 33 | Global Dynamical Atlas | Unified atlas combining attractor maps, stability manifolds, and phase portraits. |

### Unified Verification (34)

| Module | Title | Content |
|--------|-------|---------|
| 34 | Unified Verification Run | End-to-end verification: runs all modules, checks all outputs, confirms all scaling laws and architectural signatures in a single pass. |

---

## Principal Results

| Domain | Key finding |
|--------|------------|
| Cosmology | A four-epoch timeline (inflation → residual gradients → structure formation → heat death) emerges generically from uniform-noise initial conditions. |
| Inflation | Exponential gradient decay with analytically predicted rate, R² > 0.99 across all tested parameters. |
| Structure | Overdensity peaks persist indefinitely via concave penalty saturation — proto-matter concentrations. |
| Horizons | Causal horizons form where M(ρ) → 0; stable on simulation timescales. |
| Scaling laws | Eight quantitative scaling laws derived analytically and validated against 200+ simulations. |
| Universality | Five universality classes identified covering all confirmed dynamical regimes. |
| Robustness | All architectural signatures survive penalty, mobility, and participation perturbation (modules 25–28). |

---

## Running the Pipeline

Each module has its own Python scripts and results directory and can be
run independently. However, modules 01-08 form a logical derivation chain
(each builds on concepts from the previous), so new users should run them
in order. Modules 09-34 can be run in any order. To run a single module:

```
cd "ED Physics/ED-Phys-05_ParameterSweeps"
python ed_phys_sweep.py
```

To run the full unified verification:

```
cd "ED Physics/ED-Phys-34_UnifiedVerificationRun"
python ed_phys_unifiedverify.py
```

---

## Connection to Other Folders

| Folder | Relationship |
|--------|-------------|
| **ED Architecture** | Provides the seven principles (P1–P7) that ED-Phys implements and verifies dynamically. |
| **ED PAPERS** | The Unified Cosmological Equation paper formalizes the cosmological results of modules 03, 17–19. The Rigour Paper (Appendix C) provides the analytic theory that module 07 validates numerically. |
| **ED Simulation** | ED-SIM v1 is the successor pipeline. It uses a more rigorous numerical framework (spectral methods, Crank–Nicolson, ETD-RK4) and computes the sixteen-family invariant atlas. ED-Phys established the physical results; ED-SIM places them on reproducible, publication-grade footing. |
| **ED Experiments** | The physical predictions confirmed by ED-Phys (horizon formation, four-epoch timeline, scaling laws) underpin the falsifiable predictions in the Open Note and the Applications Paper. |
| **ED Validation** | The principle tests (P1–P7) validate the same architectural signatures that ED-Phys explores dynamically. |

---

## Citation

Proxmire, Allen T., *Event Density Ontology*, 2026
