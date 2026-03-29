# experiments/

This directory contains all executable scripts for the ED-SIM pipeline,
organized into four of the five architectural layers defined in the
pipeline (see `reproducibility/docs/architecture.md`). Layer 1 (the
core PDE solver) lives in the parent directory as `edsim_*.py`. This
directory contains Layers 2-5. Scripts within each layer share a naming
convention and a common input/output contract.

---

## Layer 2 -- Experiments (PDE Runners)

These scripts initialize the canonical ED PDE with specific initial
conditions and parameters, run the solver, and write `time_series.npz`
and `metadata.json` to `output/runs/`.

| Script | Purpose |
|--------|---------|
| `three_stage_convergence.py` | Three-stage convergence (low/medium/high complexity) |
| `modal_hierarchy.py` | Single-mode decay, multi-mode superposition, spectral gap |
| `triad_coupling.py` | Triad selection rule verification |
| `triad_cascade.py` | Multi-triad energy transfer from two-mode ICs |
| `broadband_cascade.py` | Dense-block initializations (modes 1-30) |
| `overlap_cascade.py` | Overlapping triad networks with shared modes |
| `low_mode_attractor.py` | Long-time attractor convergence from diverse ICs |
| `parameter_sweep.py` | Single-parameter sweep of D |
| `regime_map_2d.py` | (D, A) regime classification |
| `regime_volume_3d.py` | Full 64-point (D, A, Nm) parameter grid |

---

## Layer 3 -- Invariants (Attractor Analysis)

These scripts load completed runs from `output/runs/`, compute a
specific structural invariant over the attractor window, and save
summary JSONs and figures to `output/figures/invariants/`.

Each script follows the same pattern: discover runs, load data, compute
invariant, fit convergence, produce three standard figures, save JSON
summary. Use `invariant_spectral_entropy.py` as the canonical example.

| Script | Invariant family |
|--------|-----------------|
| `invariant_low_mode_collapse.py` | Late-time modal amplitudes |
| `invariant_mode_energy_ratios.py` | Spectral energy distribution |
| `invariant_modal_ratios.py` | Adjacent-mode amplitude ratios |
| `invariant_spectral_entropy.py` | Shannon entropy of the spectrum |
| `invariant_spectral_complexity.py` | Renyi entropies at six orders |
| `invariant_dissipation_partitions.py` | Three-channel dissipation balance |
| `invariant_energy_entropy_geometry.py` | (E*, H*) attractor point |
| `invariant_broadband_cascade.py` | Log-binned energy distribution |
| `invariant_convergence_stability.py` | Three-stage decay rates |
| `invariant_modal_correlations.py` | Cross-mode energy correlations |
| `invariant_modal_overlap.py` | Nearest-neighbour energy coupling |
| `invariant_modal_phase_dynamics.py` | Phase coherence and triad closure |
| `invariant_phase_amplitude_coupling.py` | Phase-amplitude decoupling |
| `invariant_triad_balance.py` | Nonlinear triad balance |
| `invariant_lyapunov_spectrum.py` | Lyapunov exponents and D_KY |
| `invariant_attractor_manifold.py` | PCA effective dimension |
| `invariant_dissipation_geometry.py` | Energy-dissipation trajectory |
| `invariant_geometric_norms.py` | Weighted spectral norms |
| `invariant_return_map.py` | Dominant-mode return map |
| `invariant_perturbed_attractor_stability.py` | Perturbation recovery rate |

---

## Layer 4 -- Meta-Analyses

These scripts operate on the outputs of all Layer 3 invariants. They
aggregate invariant summaries across runs and produce global synthesis
metrics (universality score U, consistency score C, embedding collapse).

They use the `invariant_` prefix for consistency with the discovery
pattern, but they are architecturally distinct from Layer 3 and must
run after all Layer 3 scripts have completed.

| Script | Meta-analysis |
|--------|--------------|
| `invariant_parameter_universality.py` | Universality score U from pairwise distances |
| `invariant_cross_consistency.py` | Consistency score C from cross-family correlations |
| `invariant_embedding_map.py` | PCA/t-SNE/UMAP embedding and cluster collapse |

---

## Layer 5 -- Synthesis

These scripts read the global atlas data and produce the final
deliverables: the atlas report, the master index, and the text
certificate.

| Script | Output |
|--------|--------|
| `generate_global_atlas_report.py` | `output/atlas/ED_Attractor_Invariant_Atlas_Report.json` |
| `generate_master_index_and_certificate.py` | `output/atlas/MASTER_INDEX.txt`, `ED_Consistency_Certificate.txt` |

---

## Execution Order

The layers must execute in order (2 -> 3 -> 4 -> 5) because each
layer reads the outputs of the previous. Within each layer, scripts
are independent and can run in any order (or in parallel).

The canonical execution order is defined in `reproducibility/run_all.py`.

---

See the [ED Simulation README](../README.md) for the full pipeline overview,
or the [root README](../../README.md) for the complete project structure.
