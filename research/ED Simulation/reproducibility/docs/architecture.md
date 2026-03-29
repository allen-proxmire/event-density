# ED-SIM v1 Architecture

## Overview

ED-SIM v1 is the computational engine for the Event Density Architectural Canon. It implements the canonical PDE system derived in the Rigour Paper (Appendix C), solves it numerically across a three-dimensional parameter space (D, A, Nm), and computes sixteen families of attractor invariants that characterize the structural properties of the ED architecture.

## Pipeline Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: Canonical PDE Solver                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ edsim    │  │ edsim    │  │ edsim    │  │ edsim    │   │
│  │ core     │  │ params   │  │ ICs      │  │ diag     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                       │                                     │
│                  edsim_runner                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│  Layer 2: Experiments                                        │
│  ┌──────────────────┐  ┌──────────────────┐                 │
│  │ regime_volume_3d │  │ broadband_cascade│                 │
│  │ three_stage_conv │  │ low_mode_attract │                 │
│  │ modal_hierarchy  │  │ parameter_sweep  │                 │
│  │ triad_cascade    │  │ overlap_cascade  │                 │
│  └──────────────────┘  └──────────────────┘                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│  Layer 3: Invariant Analyses (20 core + 3 meta in Layer 4)   │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐              │
│  │ low_mode   │ │ mode_ratio │ │ renyi      │  ...         │
│  │ triad_bal  │ │ dissip_pt  │ │ lyapunov   │              │
│  │ manifold   │ │ phase_dyn  │ │ PAC        │              │
│  └────────────┘ └────────────┘ └────────────┘              │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│  Layer 4: Meta-Analyses                                      │
│  ┌──────────────────────┐                                    │
│  │ parameter_universality│ → U score                         │
│  │ cross_consistency     │ → C score                         │
│  │ embedding_map         │ → cluster radius                  │
│  └──────────────────────┘                                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│  Layer 5: Synthesis                                          │
│  ┌──────────────────────────────────────────┐               │
│  │ Global Atlas Report                       │               │
│  │ Master Index                              │               │
│  │ ED Consistency Certificate                │               │
│  └──────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────┘
```

## How Invariants Fit Together

Each invariant family captures one aspect of the attractor:

| Family | What it measures | Architectural connection |
|--------|-----------------|------------------------|
| Low-mode collapse | Which modes survive long-time | Principle 3 (unique equilibrium) |
| Mode-energy ratios | Energy distribution across modes | Modal hierarchy (Prop. C.29) |
| Modal ratios | Inter-mode amplitude structure | Spectral gap (Lemma C.31) |
| Spectral entropy | Disorder of the mode distribution | Complexity (§5.5 of Suite) |
| Renyi entropies | Multi-scale entropy family | Generalised complexity |
| Dissipation partitions | Channel balance at equilibrium | Three-channel structure (Thm. C.43) |
| Energy-entropy geometry | (E, H) attractor point | Global energy landscape |
| Broadband cascade | Bin-energy distribution | Triad cascade (Thm. C.34) |
| Convergence stability | Three-stage decay structure | Theorem C.76 |
| Modal correlations | Inter-mode energy coupling | Triad network |
| Modal overlap | Nearest-neighbour mode coupling | Local spectral structure |
| Phase dynamics | Phase coherence and drift | Oscillatory regime (Δ < 1) |
| Phase-amplitude coupling | Phase-amplitude interactions | Nonlinear feedback |
| Triad balance | Triad closure relations | Selection rule (Thm. C.34) |
| Lyapunov spectrum | Dynamical stability | Principle 3 (attractor) |
| Attractor manifold | Effective dimension | Universality (Appendix D) |

The three meta-analyses synthesize the families:

- **Universality** asks: do all (D, A, Nm) regimes produce the same invariants?
- **Cross-consistency** asks: do the invariants agree with each other?
- **Embedding** asks: do the runs cluster or scatter in invariant space?

## Data Flow

```
regime_volume_3d.py
    → output/runs/regime_D*_A*_Nm*/
        → time_series.npz, metadata.json

invariant_*.py
    → reads time_series.npz
    → writes figures + summary JSON

meta-analysis scripts
    → reads summary JSONs
    → writes synthesis figures + JSONs

generate_global_atlas_report.py
    → reads all JSONs
    → writes atlas report

generate_master_index_and_certificate.py
    → reads atlas report
    → writes MASTER_INDEX.txt + Certificate
```

## Key Design Principles

1. **No shared state**: each script reads files, computes, writes files. No database, no daemon.
2. **Streaming computation**: invariants are computed one triad / one mode at a time to bound memory.
3. **Defensive computation**: every step checks positivity, capacity, energy monotonicity.
4. **Reproducibility by construction**: seeded PRNG, versioned formats, environment capture.
5. **Graceful degradation**: missing data → SKIPPED, not crash.

---

See the [reproducibility README](../README.md), the [ED Simulation README](../../README.md), or the [root README](../../../README.md) for project navigation.
