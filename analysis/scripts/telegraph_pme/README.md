# Telegraph-Modulated PME Visualization Project

**Purpose.** First quantitative visualizations of the telegraph-modulated Porous Medium Equation (the coupled mobility + participation dynamics) reported in Foundational Paper v2 Analogue 5. Produces standalone (numpy-only) 2D PDE simulations and publication-quality figures for inclusion in future ED papers and the orientation doc.

**Canonical reference:** Foundational Paper v2 §8 — the telegraph-modulated PME section reporting 0.03% v–δ frequency match and 54% frequency renormalization at H=50 in the nonlinear regime.

---

## Canonical figure (foundational — lock-in)

**`figures_canonical/Analogue5_Linear_H50_v1.0.png`** — the primary publication-quality composite showing:

- 2D field evolution (initial / mid / late snapshots)
- Participation variable `v(t)` + domain-averaged density `⟨ρ⟩(t)` time series with phase-locked oscillation
- Power spectral density showing matched peaks for both series aligned with linear-theory prediction
- Measurement summary table

**This is the first-in-repo visualization** of the Analogue-5 coupling structure in the linear regime. Lock date: **2026-04-21**. Cited by: (pending) future Foundational Paper v2 revision, orientation doc §5.7 cross-reference.

## Runs

| Version | Regime | H | Amplitude | Solver(s) | Folder | Status | Primary figure |
|:---|:---|:---:|:---:|:---|:---|:---|:---|
| **v1.0** | **Linear** | 50 | 0.2 | explicit Euler (Neumann) | `v1.0_linear_regime/` | **✓ Canonical lock-in** | `Analogue5_Linear_H50_v1.0.png` |
| **v1.1** | **Attempted nonlinear** | 50 | 0.4 → 0.45 | explicit Euler (Neumann) | `v1.1_nonlinear_regime/` | **✓ Locked (honest finding)** | `Analogue5_Nonlinear_Attempt_H50_v1.1.png` |
| **v1.2** | **H-sweep (linear)** | 10, 20, 50 | 0.2 | explicit Euler (Neumann) | `v1.2_H_sweep/` | **✓ Locked** | `Analogue5_OmegaVsH_v1.2.png` |
| **v1.3** | **Solver-independence test** | 10, 20, 50 | 0.2, 0.45 | **Spectral ETDRK2 + MOL-BDF (periodic)** | `v1.3_solver_independence/` | **✓ LOCKED — Scenario A confirmed** | `Analogue5_SolverIndependence_v1.3.png` |
| **v1.4** | **Root-cause bug diagnosis** | 10, 20, 50 | 0.01–0.4 | `telegraph_pme.py` orig vs patched | `v1.4_bug_diagnosis/` | **✓ LOCKED — bug identified + patched** | (text-only; see memo) |

## File layout

```
telegraph_pme/
├── README.md                       (this file — project index)
├── ed_solver_2d.py                 (standalone solver; numpy only)
├── make_figures.py                 (figure generator; takes npz → PNGs)
├── figures_canonical/              (versioned figures for citation)
│   └── Analogue5_Linear_H50_v1.0.png
├── v1.0_linear_regime/             (CANONICAL LINEAR-REGIME RUN)
│   ├── memo.md                     (detailed writeup + reproducibility)
│   ├── analogue5_H50.npz           (simulation output)
│   ├── summary.png, time_series.png, psd.png, field_snapshots.png, harmonic.png
├── v1.1_nonlinear_regime/          (pending — nonlinear renormalization + 3rd harmonic)
└── v1.2_H_sweep/                   (pending — ω(H) scaling)
```

## Reproducibility

Each run folder contains:
1. An `npz` with the saved simulation state (v, ⟨ρ⟩, ρ_center, F̄ time series + field snapshots at coarser cadence).
2. A memo.md with parameters, linear prediction, measured values, and interpretation.
3. Generated figures.

To re-run the canonical v1.0 linear-regime simulation:

```bash
cd analysis/scripts/telegraph_pme/
python3 ed_solver_2d.py          # ~2 min, writes analogue5_H50.npz at top level
python3 make_figures.py          # ~10 sec, writes PNGs at top level
# then move outputs into the appropriate v*_* folder
```

Dependencies: `numpy`, `scipy`, `matplotlib`. No ED-specific package imports.

## Canonical parameters (applies to all runs unless specified)

| Parameter | Value | Source |
|:---|:---:|:---|
| D | 0.3 | Canon P2 |
| β | 2.0 | Canon P7 |
| ρ_max | 1.0 | — |
| ρ* | 0.5 | — |
| ζ | 0.1 | Canon default |
| τ | 1.0 | Canon default |
| P₀ (weak) | 0.01 | Analogue 5 specifies weak penalty |
| H (canonical) | 50 | strongest coupling in Foundational Paper v2 §8 |

## Key results summary

### v1.0 Linear Regime (H=50, amp=0.2)

| Quantity | Linear prediction | Measured |
|:---|:---:|:---:|
| ω | 0.7054 | 0.7363 (within FFT bin) |
| T (period) | 8.91 | ~8.5 |
| γ (damping) | 0.0515 | ~0.05 |
| v–δ frequency match | exact | 0.000% (same FFT bin) |
| 3rd-harmonic ratio | n/a (linear) | 0.079% |

**Status:** linear theory confirmed to FFT-bin resolution. Nonlinear regime (where the 54% ω renormalization and 3-6% 3rd-harmonic content appear) requires follow-up runs at higher amplitude — see v1.1 below.

## Status (2026-04-21)

All four versions locked in a single session.

- **v1.0 linear canonical:** linear theory confirmed to FFT-bin resolution at H=50 (explicit Euler + Neumann BC).
- **v1.1 nonlinear attempt (honest finding):** FPv2 §8.4's reported 54% renormalization at H=50 **does not reproduce** under explicit-Euler + Neumann + Gaussian IC, even at amp=0.45.
- **v1.2 H-sweep:** three H values (10, 20, 50) all land on the linear-theory ω(H) curve to within ~4-18%.
- **v1.3 solver-independence (DECISIVE):** two independent solvers (spectral ETDRK2 + MOL-BDF), periodic BC, both regimes, same 3 H values = 12 runs. **In all 9 reliable runs (6 linear-regime both solvers + 3 BDF nonlinear-regime), ω/ω_linear = 1.01 ± 0.04.** The FPv2 54% value is NOT reproduced. **Scenario A confirmed: FPv2 §8.4's renormalization is solver-specific, not a physical property of the ED PDE.** Combined with v1.0/v1.1/v1.2, this gives three independent numerical methods all agreeing with linear theory.
- **v1.3 architectural follow-through ([`v1.3_solver_independence/architectural_followthrough.md`](v1.3_solver_independence/architectural_followthrough.md)):** modular document with four copy-paste-ready parts — (1) full "Numerical Independence Result" section for FPv2 §8.4 inclusion, (2) drop-in correction block replacing the 54% quantitative paragraph, (3) repo Next-Steps list, (4) three versions of publication-ready summary paragraph for abstracts / figure captions / orientation doc. Use when propagating the correction upstream.
- **v1.4 root-cause diagnosis (2026-04-22):** the 54% renormalization traced to a single-line bug in `edsim/phys/analogues/telegraph_pme.py:162` — `F_avg = spatial_average(params.D * F_local, dx)` inserts a spurious factor of `D` into the participation ODE's forcing. The eigenmode implied by the buggy code is `ω_coded = √(DP₀(H+ζ)/τ − γ²)`, asymptoting to `√D · ω_linear ≈ 0.548 · ω_linear` and matching all three FPv2-reported values (0.1662, 0.2400, 0.3842) to 4-significant-figure precision. Patching the line to `F_avg = spatial_average(F_local, dx)` restores `ω_measured ≈ ω_linear`. **Upgrades v1.3's "solver-specific" conclusion from general to definitive**: specific line, specific file, one-character patch. See [`v1.4_bug_diagnosis/memo.md`](v1.4_bug_diagnosis/memo.md).

## Deferred (not session-critical)

- **Animation of v1.0 field evolution** (mp4/gif from the snapshot stack). ~30 min task with `matplotlib.animation.FuncAnimation`. Valuable for presentation purposes; not needed for the locked canonical figures.
- **Semi-implicit solver for v1.3** (Crank–Nicolson or IMEX on the variable-coefficient Laplacian) to push amp > 0.45 and test whether the FPv2 54% value emerges in the high-amplitude regime our explicit solver can't reach. Half-day of work.
- **Alternative IC probe for v1.4** (two-bump, top-hat, sustained flux). Could access the FPv2 regime from a different direction. 1-2 hours.
- **N=128 grid cross-check** to replicate FPv2 §8.4's resolution exactly. ~30 min (3× slower runs).

## Cross-references

- Foundational Paper v2 §8 (Analogue 5) — the original numerical claim.
- [`docs/ED-Orientation.md`](../../../docs/ED-Orientation.md) §5.7 — six-structural-analogues table.
- [`theory/Architectural_Canon.md`](../../../theory/Architectural_Canon.md) — Canon principles P1–P7.
- [`experiements/ED-RLC-Analogue_InProcess/memo.md`](../../../experiements/ED-RLC-Analogue_InProcess/memo.md) — the spatially-uniform-limit reduction (RLC-circuit isomorphism) that the v1.0 run's uniform-mode oscillation validates in a 2D PDE setting.

---

*This project exists to produce the first in-repo figures of the coupled-channel telegraph-PME structure. Each version is locked once generated; improvements create new versions rather than overwriting. The canonical figure stays identified by filename forever.*
