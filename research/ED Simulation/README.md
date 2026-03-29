# ED Simulation

The computational engine of the Event Density research program.

> **TL;DR:** Run `python reproducibility/run_all.py` from this directory
> to execute the full pipeline. Outputs go to `output/` (runs, figures,
> atlas, certificate). To run only the simulation:
> `python experiments/regime_volume_3d.py`. New contributors: start with
> `reproducibility/docs/onboarding.md`.

ED-SIM v1 is a complete, reproducible numerical pipeline that solves the
canonical ED partial differential equation across a systematic parameter
space, computes sixteen families of attractor invariants, performs three
meta-analyses, and generates a global architectural verdict encoded in an
ED Architecture Certificate. The entire pipeline — from raw PDE
integration through invariant extraction to certificate generation — runs
from a single command and produces all figures, data, and deliverables
of the ED-SIM-01 paper and the ED Monograph.

---

## Role in the ED Program

The Architecture defines the seven principles. The Rigour Paper proves
them. The Validation tests confirm them individually. ED-SIM answers the
comprehensive question: *do the principles hold together, across the full
parameter space, as a single coherent architecture?*

The answer is the Invariant Atlas — sixteen families of structural
quantities computed across sixty-four parameter regimes — and the ED
Architecture Certificate, which encodes the global consistency verdict.
ED-SIM is the bridge between the analytic theory of Appendix C and the
physical predictions of the Applications Paper: if the certificate reads
PASS, the architecture is self-consistent, and the predictions that follow
from it are structurally well-founded.

ED-SIM is the successor to ED-Phys (in `ED Physics/`). Where ED-Phys
explored the physics of the ED equation with a lattice-based simulator,
ED-SIM provides rigorous numerical infrastructure (spectral methods,
Crank–Nicolson, ETD-RK4), formal invariant extraction, and a
publication-grade reproducibility framework.

---

## Directory Structure

```
ED Simulation/
│
├── edsim_core.py                  Core PDE solver
├── edsim_parameters.py            Canonical parameter sets
├── edsim_diagnostics.py           Observable extraction
├── edsim_initial_conditions.py    Initial condition generators
├── edsim_runner.py                Integration loop and output
│
├── experiments/                   PDE experiments and invariant scripts
│   ├── three_stage_convergence.py
│   ├── modal_hierarchy.py
│   ├── triad_coupling.py
│   ├── triad_cascade.py
│   ├── broadband_cascade.py
│   ├── overlap_cascade.py
│   ├── low_mode_attractor.py
│   ├── parameter_sweep.py
│   ├── regime_map_2d.py
│   ├── regime_volume_3d.py        64-point (D, A, Nm) regime map
│   ├── invariant_*.py             23 invariant extraction scripts
│   ├── generate_global_atlas_report.py
│   └── generate_master_index_and_certificate.py
│
├── analyze_*.py                   9 post-processing and figure scripts
│
├── generate_certificate_figure.py Certificate renderer (matplotlib)
│
├── reproducibility/               Full pipeline orchestration
│   ├── run_all.py                 One-command reproducibility pipeline
│   ├── checks/                    Environment + data integrity
│   ├── scenarios/                 Minimal, full, diagnostic
│   ├── docs/                      Architecture, onboarding, invariant map
│   ├── validation/                Output verification
│   ├── examples/                  Sample outputs
│   └── figures/                   Reference figures
│
├── output/
│   ├── runs/                      Per-experiment run directories
│   ├── figures/                   All generated PNGs (300 dpi)
│   ├── logs/                      Execution logs
│   └── atlas/                     Atlas report, certificate, master index
│
├── manifests/
│   ├── parameter_manifest.json    Complete parameter specification
│   └── run_manifest.json          Execution record
│
├── ed_monograph.md                Monograph source (Markdown)
├── ed_monograph.tex               Monograph source (LaTeX, Overleaf-ready)
├── ed_references.bib              Bibliography (BibLaTeX)
├── ED-SIM-01.md                   ED-SIM-01 paper
├── ED-SIM-public_narrative_package.md  Public-facing narrative
└── certificate_design_spec.md     Certificate figure specification
```

---

## The Pipeline

ED-SIM operates in five layers, each reading the outputs of the layer
below:

| Layer | Components | Output |
|-------|-----------|--------|
| 1. Solver | `edsim_core.py`, `edsim_runner.py` | `time_series.npz`, `metadata.json` per run |
| 2. Experiments | 10 experiment scripts in `experiments/` | 64+ run directories in `output/runs/` |
| 3. Invariants | 23 invariant scripts in `experiments/` | Summary JSONs, figures in `output/figures/` |
| 4. Meta-analyses | Universality, cross-consistency, embedding | Synthesis JSONs |
| 5. Synthesis | Atlas report, master index, certificate | `output/atlas/` deliverables |

---

## Core Solver

The solver implements the canonical ED PDE:

- **Spatial discretization:** Finite difference (Method A) or spectral
  Neumann eigenbasis (Method B) with 3/2-rule dealiasing.
- **Time stepping:** Crank–Nicolson (default), implicit Euler, or ETD-RK4.
- **Stability controls:** Positivity enforcement, sub-capacity monitoring,
  energy monotonicity check, mass conservation, mobility positivity.
- **Default parameters:** N = 768 grid points, dt = 3.125 × 10⁻⁵,
  Crank–Nicolson method.

---

## Experiments

Ten experiment scripts explore the canonical PDE dynamics:

| Experiment | Script | Purpose |
|-----------|--------|---------|
| Three-stage convergence | `three_stage_convergence.py` | Validates the global → algebraic → exponential decay structure (Theorem C.76). |
| Modal hierarchy | `modal_hierarchy.py` | Single-mode decay, multi-mode superposition, spectral gap. |
| Triad coupling | `triad_coupling.py` | Selection rule verification: modes m, n → \|m−n\|, m+n. |
| Triad cascade | `triad_cascade.py` | Multi-triad energy transfer and cascade dynamics. |
| Broadband cascade | `broadband_cascade.py` | Dense-block initializations (modes 1–30) and network collapse. |
| Overlap cascade | `overlap_cascade.py` | Overlapping triad networks and shared-mode dynamics. |
| Low-mode attractor | `low_mode_attractor.py` | Long-time attractor convergence from diverse initial conditions. |
| Parameter sweep | `parameter_sweep.py` | Single-parameter sweeps of D with broadband ICs. |
| Regime map 2D | `regime_map_2d.py` | (D, A) regime classification with discriminant computation. |
| Regime volume 3D | `regime_volume_3d.py` | The full 64-point (D, A, Nm) parameter grid. |

---

## Invariant Families

Twenty-three invariant scripts extract sixteen families of structural
quantities from the regime-volume runs:

| # | Family | Script | Key invariant |
|---|--------|--------|---------------|
| 1 | Low-mode collapse | `invariant_low_mode_collapse.py` | m_k* attractor profile |
| 2 | Mode-energy ratios | `invariant_mode_energy_ratios.py` | R_k* spectral fingerprint |
| 3 | Spectral complexity | `invariant_spectral_complexity.py` | H_q* Rényi entropy family |
| 4 | Dissipation partitions | `invariant_dissipation_partitions.py` | R_grad*, R_pen*, R_part* |
| 5 | Energy–entropy geometry | `invariant_energy_entropy_geometry.py` | (E*, H*) attractor point |
| 6 | Broadband cascade | `invariant_broadband_cascade.py` | R_b* bin-energy profile |
| 7 | Convergence stability | `invariant_convergence_stability.py` | σ_III Stage-III rate |
| 8 | Modal correlations | `invariant_modal_correlations.py` | Mean off-diagonal correlation |
| 9 | Modal overlap | `invariant_modal_overlap.py` | O_k* neighbour profile |
| 10 | Phase dynamics | `invariant_modal_phase_dynamics.py` | Phase coherence, triad closure |
| 11 | Phase–amplitude coupling | `invariant_phase_amplitude_coupling.py` | ρ_k self-PAC |
| 12 | Lyapunov spectrum | `invariant_lyapunov_spectrum.py` | λ_i, D_KY |
| 13 | Attractor manifold | `invariant_attractor_manifold.py` | D_eff, spectral gap |
| 14 | Perturbed stability | `invariant_perturbed_attractor_stability.py` | σ_ε recovery rate |
| 15 | Parameter universality | `invariant_parameter_universality.py` | U score |
| 16 | Cross-consistency | `invariant_cross_consistency.py` | C score |

Additional scripts compute supporting invariants: modal ratios, geometric
norms, spectral entropy, dissipation geometry, return maps, and the
embedding map.

---

## Analysis Scripts

Nine post-processing scripts generate publication-quality figures:

| Script | Figures |
|--------|---------|
| `analyze_three_stage_I.py` | Energy decay, complexity decay, dissipation channels, modal amplitudes |
| `analyze_modal_hierarchy.py` | Single-mode decay, modal funnel, triad activation, dissipation |
| `analyze_triad_cascade.py` | Triad-generated modes, parent/child annotations |
| `analyze_overlap_cascade.py` | Overlapping triad networks, cascade detail panels |
| `analyze_broadband_cascade.py` | Modal collapse, network density, cross-IC comparison |
| `analyze_low_mode_attractor.py` | Return maps, phase portraits, convergence rates |
| `analyze_parameter_sweep.py` | Modal funnels by D, decay-rate vs D, regime map |
| `analyze_regime_map_2d.py` | 2D regime map, decay-rate surface, representative funnels |
| `analyze_regime_volume_3d.py` | 3D regime scatter, slices, decay-rate tensor |

All figures are saved as 300 dpi PNGs with no interactive display.

---

## Synthesis and Certificate

The final pipeline stages produce the global deliverables:

| Script | Output |
|--------|--------|
| `generate_global_atlas_report.py` | `ED_Attractor_Invariant_Atlas_Report.json` and `.txt` |
| `generate_master_index_and_certificate.py` | `MASTER_INDEX.txt`, `ED_Consistency_Certificate.txt`, certificate figure |
| `generate_certificate_figure.py` | `ED_Architecture_Certificate.png` and `.pdf` |

The certificate encodes five global diagnostics: universality (U),
cross-consistency (C), stability (Lyapunov spectrum, D_KY, D_eff),
embedding collapse (cluster radius), and perturbation recovery
(ε-independence CV). The verdict is PASS, PARTIAL, or FAIL.

---

## Monograph and Paper Sources

| File | Purpose |
|------|---------|
| `ed_monograph.md` | Full monograph source in Markdown (6 parts, 24 chapters, appendices). |
| `ed_monograph.tex` | Complete LaTeX conversion (1,398 lines, Overleaf-ready, `book` class). |
| `ed_references.bib` | BibLaTeX bibliography (12 entries). |
| `ED-SIM-01.md` | The ED-SIM-01 paper. |
| `ED-SIM-public_narrative_package.md` | Public-facing narrative: executive summary, website copy, press kit, explainer script. |
| `certificate_design_spec.md` | Full design specification for the certificate figure. |

---

## Running ED-SIM

### Full reproducibility pipeline (one command)
```
cd "ED Simulation/reproducibility"
python run_all.py
```
This produces all runs, invariants, meta-analyses, figures, atlas report,
and certificate.

### Single experiment
```
cd "ED Simulation"
python experiments/regime_volume_3d.py
```

### Single analysis
```
python analyze_three_stage_I.py
```

### Certificate generation
```
python generate_certificate_figure.py --verdict PASS
```

---

## Parameter Grid

The default 3D regime sweep:

| Parameter | Values | Count |
|-----------|--------|-------|
| D | 0.05, 0.1, 0.2, 0.5 | 4 |
| A | 0.005, 0.01, 0.02, 0.05 | 4 |
| N_m | 5, 10, 20, 30 | 4 |
| **Total** | | **64** |

Each run integrates the canonical PDE from a broadband eigenmode IC
(modes 1 through N_m, equal amplitude A) to T = 20 using Crank–Nicolson
at N = 768, dt = 3.125 × 10⁻⁵.

---

## Requirements

- Python 3.10+
- NumPy, SciPy, Matplotlib
- Optional: scikit-learn (embedding analyses), umap-learn (UMAP embedding)

No external data is required. All runs and outputs are self-contained.

---

## Connection to Other Folders

| Folder | Relationship |
|--------|-------------|
| **ED Architecture** | ED-Arch-12 defines the seven principles that ED-SIM verifies across the parameter space. ED-Arch-06 (Energetics) and ED-Arch-10 (Invariants) motivate the invariant families. |
| **ED PAPERS** | The Simulation Suite specification, Numerical Atlas, and Applications Paper are in `ED PAPERS/`. The Monograph source files are here. Appendix C provides the theorems that every invariant tests. |
| **ED Physics** | ED-Phys is the precursor pipeline. ED-SIM replaces its lattice simulator with spectral methods, formal invariant extraction, and the reproducibility framework. |
| **ED Experiments** | The architectural signatures confirmed by ED-SIM underpin the nineteen predictions in the Open Note and the Applications Paper. |
| **ED Validation** | The six principle tests validate P1–P7 individually. ED-SIM confirms they hold together across 64 parameter regimes. |
| **ED Interpretations** | The domain interpretations invoke structural behaviors (modal hierarchy, triad coupling, three-stage convergence) that ED-SIM quantifies. |

---

## Glossary

For definitions of technical terms (attractor, capacity, discriminant,
horizon, manifold, modal hierarchy, triad, etc.), see the glossary in
`ED PAPERS/ED_Canon Foundation Appendices/glossary.md`.

---

## Citation

Proxmire, Allen T., *Event Density Ontology*, 2026
