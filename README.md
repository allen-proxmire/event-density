# Event Density

**A structural ontology for physics.**

Event Density (ED) is a foundational framework built on a minimal set of
primitives — events, becoming, gradients, and flow — from which physical
dynamics emerge without assuming spacetime, geometry, fields, or curvature.
A single canonical PDE, governed by seven irreducible structural principles,
generates cosmological behavior, quantum-classical boundaries, galactic
dynamics, and condensed-matter phenomena as architectural consequences of
density evolution.

This repository contains the complete ED research program: the
Architectural Canon, the Rigour Paper, the Applications Paper, the
ED-SIM numerical pipeline, and all supporting theory, interpretations,
experiments, and validation.

---

## Core Papers

### The Architectural Canon of the Unified ED Framework
Defines the seven structural principles (P1–P7) that uniquely characterize
the ED architecture. Each principle is irreducible: removing any one
collapses the ontology. The Canon is the axiomatic foundation of the
entire program.

### The Unified Cosmological Equation of Event Density
Derives the ED cosmological dynamics from the canonical operator and
demonstrates how ED reproduces inflation-like smoothing, structure
formation, expansion, and late-time flattening — without geometry.

### Event Density Canon Foundations (Rigour Paper)
Places the Architectural Canon on rigorous mathematical footing. Includes
Appendices C (PDE well-posedness, spectral analysis, stability, bifurcation,
long-time behavior) and D (universality class and closure theorems).

### Physical Applications of the Event Density Architecture
Derives nineteen falsifiable predictions across five physical domains —
quantum mechanics, galactic dynamics, condensed matter, photonics, and
phononics — from the architectural principles. One prediction (dwarf galaxy
rotation curves) has been tested and confirmed.

### The ED Monograph
A unified mathematical treatment integrating the Canon, Rigour Paper,
Applications Paper, Invariant Atlas, and Simulation Suite into a single
self-contained account. Available as both Markdown and LaTeX (Overleaf-ready).

All core papers are collected in `ED PAPERS/`.

---

## Repository Structure

```
Event Density/
├── ED Architecture/     Structural anatomy: 12 layered documents
├── ED PAPERS/           Core papers, appendices, and monograph
├── ED Physics/          UCE, cosmological modules, physical consequences
├── ED Interpretations/  31 domain interpretations + 12 foundational essays
├── ED Experiments/      Open Note, experiment program, SPARC test
├── ED Simulation/       ED-SIM v1: full numerical pipeline
└── ED Validation/       P1–P7 reproducible test outputs
```

### ED Architecture
Twelve progressive documents developing the internal structure of the ED
equation — from the canonical three-channel PDE through motifs, laws,
geometry, field theory, energetics, causality, information, symmetry, and
invariants to the irreducible Architectural Canon.

### ED PAPERS
The publication-grade deliverables of the program: the Architectural Canon,
the Unified Cosmological Equation, the Canon Foundations (Rigour Paper)
with ten appendices (proofs, PDE analysis, universality, numerical methods,
glossary), the Applications Paper, the Numerical Atlas, the Simulation
Suite specification, and the Monograph.

### ED Physics
Ten modules deriving the physical consequences of the canonical PDE: the
update rule, the simulator, cosmological timeline, physical analogues,
parameter sweeps, emergent phenomena, analytical theory, documentation,
extensions, and multi-field generalizations.

### ED Interpretations
Forty-three documents exploring ED across physics: twelve foundational
essays (architecture of the universe, galactic curvature, temporal tension,
spacetime emergence) and thirty-one domain-specific interpretations covering
superconductivity, entanglement, spin, the quantum-classical boundary,
magnetism, the double-slit experiment, the Higgs boson, neutrinos,
gravitational waves, baryogenesis, photonics, quantum information,
topological effects, microresonators, Casimir self-assembly, chiral phonons,
Josephson junctions, black-hole scattering, weak lensing, tunneling,
gamma rays, and photons.

### ED Experiments
The experimental program: the Open Note defining all falsifiable predictions,
the experiment expansion framework, quantum-classical FAQs, and the
completed SPARC-based temporal tension test (dwarf galaxy rotation curves).

### ED Simulation
The ED-SIM v1 numerical pipeline — a complete, reproducible simulation
engine implementing the canonical PDE with:
- The core solver (`edsim_core.py`, `edsim_runner.py`)
- Sixteen invariant families probing the attractor from independent angles
- Three meta-analyses (universality, cross-consistency, embedding collapse)
- The Invariant Atlas and global architectural verdict
- The ED Architecture Certificate
- A full reproducibility suite (`reproducibility/`)

### ED Validation
Self-contained test scripts reproducing each architectural principle:
- P1 — Modal Funnel
- P2 — D/H Complementarity
- P3 — Manifold Collapse
- P4 — Horizon Formation
- P6 — Damping Discriminant
- P7 — Nonlinear Triad Coupling

Each test regenerates its own outputs. No precomputed data is required.

---

## The Seven Principles

| Principle | Name | Statement |
|-----------|------|-----------|
| P1 | Operator Structure | The density operator has exactly three terms: mobility-weighted diffusion, gradient-squared nonlinearity, and penalty reaction. |
| P2 | Channel Complementarity | The evolution is a weighted sum of a direct channel and a participation channel, with weights summing to unity. |
| P3 | Penalty Equilibrium | The penalty vanishes at a unique equilibrium density and is strictly restoring. |
| P4 | Mobility Capacity Bound | The mobility vanishes at the capacity bound, creating an impassable horizon. |
| P5 | Participation Feedback | A participation variable integrates the spatial average of the operator and feeds it back into the evolution. |
| P6 | Damping Discriminant | A discriminant classifies the dynamics as oscillatory, critical, or monotonic. |
| P7 | Nonlinear Triad Coupling | The gradient-squared term generates inter-modal coupling with the selection rule: modes m and n produce modes \|m-n\| and m+n. |

### The Sixteen Invariants

The seven principles generate structural predictions about the long-time
behavior of the canonical PDE. The ED-SIM pipeline verifies these
predictions by computing sixteen families of attractor invariants across
sixty-four parameter regimes. Each invariant probes the attractor from an
independent angle — spectral, dynamical, topological, or statistical —
and its constancy across regimes confirms that the predicted behavior is
architectural, not parameter-dependent.

**Spectral invariants** characterize the shape of the attractor in mode space:

| # | Invariant | What it measures | Principle tested |
|---|-----------|-----------------|-----------------|
| 1 | Low-Mode Collapse | Late-time modal amplitudes m_k* → 0 | P3 (unique attractor) |
| 2 | Mode-Energy Ratios | Spectral energy distribution R_k* | P1, P7 (modal hierarchy) |
| 3 | Modal Ratios | Adjacent-mode amplitude ratios | P1 (operator structure) |
| 4 | Spectral Entropy | Shannon entropy of the energy spectrum | P1, P7 (spectral shape) |
| 5 | Spectral Complexity | Rényi entropies H_q* at six orders | P1, P7 (multi-scale structure) |
| 8 | Broadband Cascade | Log-binned energy distribution R_b* | P7 (triad-driven cascade) |
| 11 | Modal Overlap | Nearest-neighbour energy coupling O_k* | P1, P7 (local spectral structure) |

**Dynamical invariants** characterize the temporal approach to equilibrium:

| # | Invariant | What it measures | Principle tested |
|---|-----------|-----------------|-----------------|
| 9 | Convergence Stability | Three-stage decay rates (σ_III) | P3 (global attractor) |
| 12 | Phase Dynamics | Phase coherence and triad closure | P5, P7 (feedback + coupling) |
| 13 | Phase–Amplitude Coupling | Decoupling of phase and amplitude at equilibrium | P3 (point attractor) |
| 14 | Triad Balance | Nonlinear balance T_ijk* = a_i·a_j − λ·a_k | P7 (selection rule) |

**Topological invariants** characterize the geometry of the attractor:

| # | Invariant | What it measures | Principle tested |
|---|-----------|-----------------|-----------------|
| 15 | Lyapunov Spectrum | Stability exponents λ_i and Kaplan–Yorke dimension | P3 (all λ_i ≤ 0, D_KY ≈ 0) |
| 16 | Attractor Manifold | PCA effective dimension and spectral gap | P3, P4 (point attractor) |

**Statistical invariants** characterize macroscopic structure and cross-regime consistency:

| # | Invariant | What it measures | Principle tested |
|---|-----------|-----------------|-----------------|
| 6 | Dissipation Partitions | Channel balance R_grad*, R_pen*, R_part* | P2 (complementarity) |
| 7 | Energy–Entropy Geometry | Attractor point (E*, H*) in the energy–entropy plane | P3, P2 (universal endpoint) |
| 10 | Modal Correlations | Cross-mode energy correlations and spectral radius | P7 (triad connectivity) |

An invariant is classified as **INVARIANT** (CV < 5%), **WEAKLY INVARIANT**
(CV < 15%), or **NOT INVARIANT** (CV ≥ 15%) based on its coefficient of
variation across all admissible runs. Three meta-analyses — parameter
universality (U), cross-invariant consistency (C), and embedding
collapse — synthesize the sixteen families into a global verdict encoded
in the ED Architecture Certificate.

---

## What ED Provides

- A non-geometric ontology for physical law
- A canonical PDE that generates cosmology from density evolution
- Seven irreducible principles with a rigorous mathematical foundation
- Nineteen falsifiable predictions across five physical domains
- A reproducible computational pipeline (ED-SIM v1) with an Invariant Atlas
- A structural consistency certificate verified across 64 parameter regimes

---

## Quick Start

**Run a principle test:**
```
cd "ED Validation/P4_horizon_formation"
python run_test.py
```

**Run the full ED-SIM pipeline:**
```
cd "ED Simulation/reproducibility"
python run_all.py
```

**Read the monograph:**
```
ED PAPERS/The ED Monograph.pdf
```

---

## Requirements

- Python 3.10+
- NumPy, SciPy, Matplotlib
- Optional: scikit-learn (for embedding analyses), umap-learn

No external data is required. All tests and simulations are self-contained.

---

## Contact

ED is an active research program. Researchers interested in mathematical
physics, architectural frameworks, ontology, or computational verification
are invited to engage with the work.

---

## Citation

Proxmire, Allen T., *Event Density Ontology*, 2026

[![DOI](https://zenodo.org/badge/1124778234.svg)](https://doi.org/10.5281/zenodo.18090236)
