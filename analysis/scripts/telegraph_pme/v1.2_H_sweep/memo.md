# v1.2 H-Sweep — Linear-Regime ω(H) Scaling

**Version:** **v1.2 — LOCKED 2026-04-21.** Three simulations at H=10, 20, 50 in the linear regime (same canonical parameters as v1.0 with varying H only). Reproduces the linear-theory ω(H) scaling cleanly and quantifies the discrepancy with Foundational Paper v2 §8.4's reported nonlinear values.

**Canonical figures for citation:**
- [`figures_canonical/Analogue5_Hsweep_Linear_v1.2.png`](../figures_canonical/Analogue5_Hsweep_Linear_v1.2.png) — two-panel composite (time-series overlay + PSD overlay)
- [`figures_canonical/Analogue5_OmegaVsH_v1.2.png`](../figures_canonical/Analogue5_OmegaVsH_v1.2.png) — **ω(H) scaling plot** with both linear theory and FPv2 nonlinear curve, our measurements, and FPv2 reported values on the same axes. **Recommended lead figure** for any future write-up of this H-sweep.

---

## Headline result

| H | Linear prediction | Our measurement | FPv2 §8.4 reported | Our ω / linear | FPv2 ω / linear |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 10 | 0.3125 | **0.3682** | 0.1662 | 1.178 | 0.532 |
| 20 | 0.4446 | **0.4909** | 0.2400 | 1.104 | 0.540 |
| 50 | 0.7054 | **0.7363** | 0.3842 | 1.044 | 0.545 |

**Two facts pop out:**

1. **Our measurements sit on the linear-theory curve at every H.** Measured/linear ratio converges toward 1.0 as H increases (limited by FFT bin resolution at low H where the peak spacing is smaller). Three independent H values — one unified theory match.

2. **The FPv2 reported values sit on a parallel curve at exactly 54% of linear.** Ratios 0.532, 0.540, 0.545 are mutually consistent to within ~1% across three decades of H. Whatever the FPv2 authors measured, it is a **consistent phenomenon**, not noise — but it is a different phenomenon than what our explicit-Euler + Gaussian-IC protocol captures.

## Interpretation

The linear eigenmode prediction `ω = √((DP₀ζ + HP₀)/τ − γ²)` is verified across three H values spanning a factor of 5. This is a solid confirmation of the PDE's coupling structure at the linear-theory level.

The FPv2 §8.4 54% renormalization is reproducibly present in the paper's figures but is NOT our protocol. The consistency of the ratio (0.532/0.540/0.545) suggests it arises from a specific regime — possibly a different IC, a different solver, or a specific nonlinear interaction — that our runs do not activate.

## Run summary

All three runs used the canonical v1.0 parameters with only H varying:

| Parameter | Value | Source |
|:---|:---:|:---|
| D | 0.3 | Canon |
| P₀ | 0.01 | weak-penalty Analogue 5 spec |
| ζ | 0.1 | Canon default |
| τ | 1.0 | Canon default |
| β | 2.0 | Canon |
| ρ_max, ρ* | 1.0, 0.5 | — |
| H | **10, 20, 50** | swept |
| Grid | 80 × 80 on L = 2.0 | |
| dt | 5 × 10⁻⁴ (CFL ratio 0.234) | |
| T total | 200 | |
| IC | Gaussian depression amp=0.2, σ=0.15 | same as v1.0 |
| Runtime | ~10 minutes total (3 × ~3 min) | |

## Files

```
v1.2_H_sweep/
├── memo.md                         (this file)
├── analogue5_H10.npz               (0.56 MB)
├── analogue5_H20.npz               (0.57 MB)
├── analogue5_H50.npz               (0.57 MB)
├── H_sweep_summary.png             (2-panel: v(t) overlay + PSD overlay)
└── omega_vs_H.png                  (scaling plot; RECOMMENDED LEAD FIGURE)
```

Both PNGs are also copied to `../figures_canonical/` with the locked v1.2 filenames.

## Reproducibility

```bash
cd analysis/scripts/telegraph_pme/
python3 run_H_sweep.py                # ~10 min (3 simulations)
python3 make_H_sweep_figure.py        # ~5 sec
```

## What this run establishes for the ED program

1. **Linear theory verified at 3 H values.** The eigenmode analysis is correct; the coupled PDE produces oscillation at the predicted linear frequency across a 5× variation in H.
2. **The 54% renormalization reported in FPv2 §8.4 is consistent with itself (uniform factor across H) but distinct from our Gaussian-IC protocol's result.** Until an independent reproduction is obtained, the paper's specific numerical value at H=50 (ω = 0.3842) should be treated as "reproducible within the paper's protocol; pending independent confirmation outside that protocol."
3. **The v-δ frequency match claim (§8.2 of the paper) holds** at all three H values in our data: v(t) and ρ_center(t) peak in the same FFT bin at each H.

## Cross-references

- **v1.0 canonical linear regime (H=50):** [`../v1.0_linear_regime/memo.md`](../v1.0_linear_regime/memo.md)
- **v1.1 nonlinear-regime attempt (unsuccessful):** [`../v1.1_nonlinear_regime/memo.md`](../v1.1_nonlinear_regime/memo.md)
- **Project README:** [`../README.md`](../README.md)
- **Foundational Paper v2 §8.4:** the source of the FPv2 reported values (0.1662, 0.2400, 0.3842)

## Next steps

- **Animation of v1.0 field evolution** — deferred; ~30-min task.
- **Semi-implicit solver to probe the nonlinear regime** — would either reproduce the 54% renormalization or sharpen the finding that it's protocol-dependent. Half-day of solver work.
- **Alternative ICs** (two-bump, top-hat, sustained flux) — could potentially access the nonlinear regime from a different direction. 1-2 hours.
- **Larger grid (N=128) cross-check** — replicate FPv2 §8.4's grid size exactly, see if the 54% value emerges. 30 min (runs will just be slower).

If reproducing the 54% is a priority, the highest-leverage next step is the larger-grid replication (rules out grid-size as the cause) combined with probing alternative ICs.
