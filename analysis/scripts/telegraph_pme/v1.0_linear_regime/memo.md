# Telegraph-Modulated PME — First Visualization of Foundational Paper v2 Analogue 5

**Version:** **v1.0 — LOCKED 2026-04-21.** Canonical linear-regime run. Any subsequent improvements become v1.0.1 / v1.1 / v1.2 in separate folders; this memo and its figures are frozen for citation.

**Canonical figure for citation:** [`figures_canonical/Analogue5_Linear_H50_v1.0.png`](../figures_canonical/Analogue5_Linear_H50_v1.0.png) (locked copy of `summary.png` in this folder).

**Date:** 2026-04-21. **Run:** `analogue5_H50.npz`. **Status:** first-pass reproduction in the linear regime. Nonlinear regime (v1.1) and H-sweep (v1.2) handled in sibling folders.

---

## What was run

The canonical ED PDE in the uniform-mode limit (2D, Neumann BC, coupled `(ρ, v)` system):

$$\partial_t \rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H\,v$$
$$\dot v = \tfrac{1}{\tau}\bigl(\bar F[\rho] - \zeta v\bigr)$$

with canonical Analogue 5 parameters:

| Parameter | Value |
|:---|:---:|
| `D` | 0.3 |
| `P₀` | 0.01 (weak penalty) |
| `H` | 50.0 (strong participation coupling) |
| `ζ` | 0.1 |
| `τ` | 1.0 |
| `β` | 2.0 (canonical mobility exponent) |
| `ρ_max` | 1.0 |
| `ρ*` | 0.5 |

| Simulation | Value |
|:---|:---:|
| Grid | 80 × 80 |
| Domain side | L = 2.0 |
| Total time | T = 200 |
| dt | 5 × 10⁻⁴ |
| Scheme | Explicit Euler with 5-point Laplacian, Neumann BC via mirror padding |
| CFL ratio (worst-case) | 0.234 (stable) |
| Initial condition | Gaussian depression, amplitude 0.2, σ = 0.15 |
| Runtime | ≈ 1 min 50 s on single-core numpy |

Output: `analogue5_H50.npz` (0.57 MB) with `v(t)`, `⟨ρ⟩(t)`, `ρ_center(t)`, `F̄(t)` at 0.025-unit cadence, plus 800 field snapshots at 0.25-unit cadence.

## Linearized prediction for this parameter set

From the 2D template eigenmode analysis:

$$\gamma = \tfrac{1}{2}(DP_0 + \zeta/\tau) = 0.0515$$
$$\omega_0^2 = \tfrac{1}{\tau}(DP_0\zeta + HP_0) = 0.5003$$
$$\omega = \sqrt{\omega_0^2 - \gamma^2} = 0.7054,\quad T = 8.91,\quad Q = \omega/(2\gamma) = 6.85$$

## Measured

| Quantity | Predicted | Measured | Notes |
|:---|:---:|:---:|:---|
| ω_v (participation peak) | 0.7054 | **0.7363** | 4.4% above linear prediction; within FFT bin resolution (Δω ≈ 0.123) |
| ω_δ (central density peak) | 0.7054 | **0.7363** | **identical bin to ω_v** |
| v–δ frequency match | exact (identity) | **0.000%** | limited by FFT bin width, not by data |
| γ (decay rate) | 0.0515 | ~0.05 | estimated from envelope falloff; amplitude at t=100 matches 0.006× prediction within order of magnitude |
| 3rd-harmonic amplitude ratio | 3–6% (ED nonlinear prediction) | **0.079%** | far below band — we are in the **linear** regime |

## Interpretation

**The coupling works as predicted by linear theory.** The uniform-mode eigenmode analysis gives `ω = 0.7054`; the simulation produces a clean damped oscillation in `v(t)` and `⟨ρ⟩(t)` with measured `ω = 0.7363`, and both series peak in the same FFT bin — satisfying the v–δ frequency-match claim of Analogue 5 to within the bin resolution of this run.

**The 3rd-harmonic prediction is not verified in this run** because the amplitude is too small (max |v| ≈ 9 × 10⁻⁵). The ED prediction of 3–6% triad-coupling content is for the **nonlinear** regime — the same regime the Foundational Paper v2 §8 describes with the 54% frequency renormalization. This run sits well inside the linear regime (amplitude < 1% of ρ_max), so only the linear dynamics are exercised.

**The PME spreading completes well before the oscillation damps.** Visible in `field_snapshots.png`: at t=40 (≈4.5 oscillation periods) the field is already essentially uniform, and the remaining 160 time units of dynamics are pure uniform-mode oscillation with no visible spatial structure. The "telegraph-modulated PME spreading" that Analogue 5 names as the distinctive phenomenon requires the spreading and the oscillation to occur on comparable timescales — not the regime we hit here.

## Figures

| File | Content |
|:---|:---|
| `field_snapshots.png` | ρ* − ρ at six times from t=0 to t=200. Clear depression at t=0; uniform by t=40. |
| `time_series.png` | v(t), ρ_center(t), ⟨ρ⟩(t), F̄(t) as stacked panels. ~12 visible damped oscillations in v(t). |
| `psd.png` | Welch PSD of v(t) and ρ_center(t) with peaks overlaid; linear prediction marked. |
| `harmonic.png` | Zoom on fundamental + 3× harmonic band on v(t) PSD. |
| `summary.png` | 4-panel composite: initial/mid/late field snapshots, time series (v and ⟨ρ⟩), PSD, parameters + measurements box. **Use this figure as the publication-quality single image.** |

## What we learned versus the Foundational Paper v2 claim

| Claim | Status in this run |
|:---|:---|
| Coupled (ρ, v) PDE produces telegraph oscillation at a well-defined frequency | **Confirmed.** |
| v(t) and ⟨ρ⟩(t) oscillate at matched frequency | **Confirmed within FFT bin resolution** (0.000% = both in same bin). |
| Measured ω matches linearized eigenmode prediction | **Confirmed** (0.7363 vs 0.7054, 4.4% error, within bin resolution). |
| Measured ω = 0.3842 (54% of linear) at H=50 — nonlinear renormalization | **Not reproduced.** We got the linear value (0.7363) because our amplitude is too small. The nonlinear renormalization requires either larger amplitude than our explicit solver supports or a different parameter regime. |
| Third-harmonic content 3–6% | **Not reproduced.** Got 0.079%. Linear regime has no triad coupling signature. |

## What's needed to reach the nonlinear regime

The Foundational Paper v2 Analogue 5 reported measurements with the bump driven far from equilibrium (large amplitude near the capacity bound). To reach that regime with the current explicit solver, the bump amplitude would exceed the CFL-stable regime on this grid. Options for a follow-up run:

1. **Implicit / semi-implicit solver.** Crank–Nicolson or IMEX with treatment of the nonlinear diffusion would lift the CFL constraint and allow larger amplitude at the current grid. Effort: ~half a day.
2. **Smaller D (e.g. D = 0.1).** Relaxes CFL by factor of 3. Would allow amp = 0.35 on the current grid. Doesn't change the physics, just the effective timescale.
3. **Finer grid with adaptive timestep.** Use scipy's `solve_ivp` with LSODA/BDF; slower wall-clock but no stability worries. ~1 hour.
4. **H-sweep at fixed linear regime.** Stay in linear amplitude but run at H = 10, 20, 50 to show ω_linear(H) scaling. Easier; demonstrates the H-dependence directly from the linear theory with no nonlinear issues. This reproduces Analogue 5's table structure at the linear level.

Option 4 is the cheapest next step and gives a clean "figure set showing ω_v(H) matches linear prediction across three H values" result. Option 1 is the canonical path to match Analogue 5's specific reported numbers (0.1662, 0.2400, 0.3842 at H=10, 20, 50).

## Reproducibility

Everything under `analysis/scripts/telegraph_pme/`:

```
telegraph_pme/
├── ed_solver_2d.py        # the 2D PDE solver; standalone, numpy-only
├── make_figures.py        # generates all 5 figures from analogue5_H50.npz
├── analogue5_H50.npz      # simulation output (v_hist, rho_snap, etc.)
├── field_snapshots.png
├── time_series.png
├── psd.png
├── harmonic.png
├── summary.png
└── memo.md                # this file
```

To re-run from scratch:

```bash
cd analysis/scripts/telegraph_pme/
python3 ed_solver_2d.py    # ~2 min
python3 make_figures.py    # ~10 sec
```

Dependencies: numpy, scipy, matplotlib. No ED-specific imports — the solver is self-contained so this script can be shared with anyone.

## Lines of follow-up work

1. **H-sweep (easy):** run at H=10, 20, 50 with otherwise identical parameters. Produce a combined figure showing ω_v(H) matches linear prediction for three points. 1-hour task.
2. **Nonlinear-regime reproduction (medium):** implement semi-implicit solver or switch to `solve_ivp` with LSODA. Push amplitude to 0.4+. Recover the 54% ω renormalization and the 3–6% 3rd-harmonic content. Half-day task.
3. **Cross-check with edsim (medium):** confirm the results here match what the repo's `edsim/` package produces for the same parameters. Bridges this standalone solver to the canonical package. 1–2 hour task.
4. **Animation (nice-to-have):** render the field evolution as an mp4/gif. Makes the phenomenon visible without needing to read static snapshots. ~30-min task with `matplotlib.animation`.

## Connection to the wider ED program

This run is the **first visualization** in the repo of the telegraph–PME coupling structure that Foundational Paper v2 Analogue 5 reported numerically. The original paper lists the 0.03% v–δ frequency match across multiple H values as one of the cleanest tests of the PDE's coupling structure; the ED-RLC-Analogue memo derives the same coupling in the spatially-uniform limit as a textbook RLC circuit. This simulation sits at the intersection: it confirms the uniform-mode eigenmode structure in a 2D spatial setting where the PME diffusion is active, bridging the purely-spatial mobility channel (Analogue 2, Barenblatt) and the purely-temporal participation channel (Analogue 1, RC/RLC).

The figure set belongs in the eventual Foundational Paper v2 revision or in a standalone note showing the coupled-channel dynamics. The nonlinear-regime follow-up (option 2 above) would close the gap to the specific numerical claim (54% frequency renormalization) that the paper's v2 reports but never visualized.
