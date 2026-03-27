# ED-SIM v1 Invariant Map

One-page reference for all 16 invariant families, their inputs, outputs, dependencies, and expected verdicts.

## Invariant Families

| # | Family | Script | Input | Output Dir | Key Metric | Expected Verdict |
|---|--------|--------|-------|------------|------------|-----------------|
| 1 | Low-Mode Collapse | `invariant_low_mode_collapse.py` | `modal_amplitudes` | `low_mode_collapse/` | m_k^* for k=0..5 | INVARIANT |
| 2 | Mode-Energy Ratios | `invariant_mode_energy_ratios.py` | `modal_amplitudes` | `mode_energy_ratios/` | R_k^* = E_k/E_total | INVARIANT |
| 3 | Modal Ratios | `invariant_modal_ratios.py` | `modal_amplitudes` | `modal_ratios/` | R_k = \|a_{k+1}\|/\|a_k\| | INVARIANT |
| 4 | Spectral Entropy | `invariant_spectral_entropy.py` | `modal_amplitudes` | `spectral_entropy/` | H^* (Shannon) | INVARIANT |
| 5 | Spectral Complexity | `invariant_spectral_complexity.py` | `modal_amplitudes` | `spectral_complexity/` | H_q^* (Renyi, q=0..4) | INVARIANT |
| 6 | Dissipation Partitions | `invariant_dissipation_partitions.py` | `D_grad, D_pen, D_part` | `dissipation_partitions/` | R_grad^*, R_pen^*, R_part^* | INVARIANT |
| 7 | Energy-Entropy Geometry | `invariant_energy_entropy_geometry.py` | `E_total, modal_amplitudes` | `energy_entropy_geometry/` | (E^*, H^*) | INVARIANT |
| 8 | Broadband Cascade | `invariant_broadband_cascade.py` | `modal_amplitudes` | `broadband_cascade/` | R_b^* (log-binned) | INVARIANT |
| 9 | Convergence Stability | `invariant_convergence_stability.py` | `E_total, D_total` | `convergence_stability/` | Stage-III slope | INVARIANT |
| 10 | Modal Correlations | `invariant_modal_correlations.py` | `modal_amplitudes` | `modal_correlations/` | mean corr, spectral radius | WEAKLY INVARIANT |
| 11 | Modal Overlap | `invariant_modal_overlap.py` | `modal_amplitudes` | `modal_overlap/` | O_k^* | INVARIANT |
| 12 | Phase Dynamics | `invariant_modal_phase_dynamics.py` | `modal_amplitudes` (complex) | `modal_phase_dynamics/` | phase coherence | WEAKLY INVARIANT |
| 13 | Phase-Amplitude Coupling | `invariant_phase_amplitude_coupling.py` | `modal_amplitudes` (complex) | `phase_amplitude_coupling/` | PAC_k | WEAKLY INVARIANT |
| 14 | Triad Balance | `invariant_triad_balance.py` | `modal_amplitudes` | `triad_balance/` | T_ijk^* | INVARIANT |
| 15 | Lyapunov Spectrum | `invariant_lyapunov_spectrum.py` | `modal_amplitudes` | `lyapunov_spectrum/` | n_positive, D_KY | INVARIANT |
| 16 | Attractor Manifold | `invariant_attractor_manifold.py` | `modal_amplitudes` | `attractor_manifold/` | D_eff, spectral gap | INVARIANT |

## Meta-Analyses

| # | Analysis | Script | Input | Key Metric |
|---|----------|--------|-------|------------|
| M1 | Parameter Universality | `invariant_parameter_universality.py` | All invariant JSONs | U score |
| M2 | Cross-Consistency | `invariant_cross_consistency.py` | All invariant JSONs | C score |
| M3 | Embedding Map | `invariant_embedding_map.py` | Universality vectors | Cluster radius |

## Dependency Graph

```
regime_volume_3d.py
    │
    ├── invariant_low_mode_collapse.py ────────┐
    ├── invariant_mode_energy_ratios.py ───────┤
    ├── invariant_modal_ratios.py ─────────────┤
    ├── invariant_spectral_entropy.py ─────────┤
    ├── invariant_spectral_complexity.py ──────┤
    ├── invariant_dissipation_partitions.py ───┤
    ├── invariant_energy_entropy_geometry.py ──┤
    ├── invariant_broadband_cascade.py ────────┤
    ├── invariant_convergence_stability.py ────┤
    ├── invariant_modal_correlations.py ───────┤
    ├── invariant_modal_overlap.py ────────────┤
    ├── invariant_modal_phase_dynamics.py ─────┤
    ├── invariant_phase_amplitude_coupling.py ─┤
    ├── invariant_triad_balance.py ────────────┤
    ├── invariant_lyapunov_spectrum.py ────────┤
    └── invariant_attractor_manifold.py ───────┤
                                               │
    ┌──────────────────────────────────────────┘
    │
    ├── invariant_parameter_universality.py
    ├── invariant_cross_consistency.py
    └── invariant_embedding_map.py
                │
                ├── generate_global_atlas_report.py
                └── generate_master_index_and_certificate.py
```

## Verdict Definitions

| Verdict | Criterion | Meaning |
|---------|-----------|---------|
| INVARIANT | CV < 5% | The quantity is constant across all tested regimes |
| WEAKLY INVARIANT | CV < 15% | The quantity varies modestly but retains qualitative structure |
| NOT INVARIANT | CV >= 15% | The quantity depends significantly on parameters |

## Per-Family Figures

Each invariant script produces three standard figures:

- **(A) Evolution**: time series of the invariant for a representative run
- **(B) Attractor Profile**: the invariant's attractor value across all runs
- **(C) Convergence Heatmap**: which (D, A, Nm) points converged

## Data Requirements

All invariant scripts require:
- Completed regime volume runs in `output/runs/regime_D*_A*_Nm*/`
- Each run must have `time_series.npz` with `modal_amplitudes` field
- Each run must have `metadata.json` with `D`, `A`, `Nm` fields

Families 6, 7, 9 additionally require `D_grad`, `D_pen`, `D_part`, `D_total`, `E_total` fields.

Families 12, 13 require complex-valued `modal_amplitudes` (with phase information).
