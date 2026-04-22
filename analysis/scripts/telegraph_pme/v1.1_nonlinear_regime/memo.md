# v1.1 Nonlinear-Regime Attempt — Honest Finding

**Version:** **v1.1 — LOCKED 2026-04-21.** Attempted nonlinear-regime reproduction. **The attempt did NOT reach the nonlinear regime that Foundational Paper v2 §8 reports.** This memo documents what was tried, what was measured, and what the discrepancy means.

**Canonical figure for citation:** [`figures_canonical/Analogue5_Nonlinear_Attempt_H50_v1.1.png`](../figures_canonical/Analogue5_Nonlinear_Attempt_H50_v1.1.png).

---

## TL;DR

Under the Foundational Paper v2 §8 canonical parameters (D=0.3, P₀=0.01, H=50), with initial-condition amplitudes ranging from 0.2 (linear, v1.0) through 0.4 and 0.45 (intended nonlinear), the **measured oscillation frequency always matches the linearized eigenmode prediction ω ≈ 0.7054** (within the 0.12 rad/s FFT bin resolution of this run).

The Foundational Paper v2 reports ω = 0.3842 at H=50 — a **54% renormalization** of the linear value — as a robust nonlinear feature. **That 54% renormalization does not reproduce in our simulations at any IC amplitude we have tried.**

This is a **real discrepancy** that needs either (a) new information about the paper's IC protocol, (b) a semi-implicit solver run at amplitudes above our CFL limit, or (c) reconsideration of the paper's reported measurement.

## What was run

Two attempts, both failed to leave the linear regime:

### v1.1a — amp = 0.4, σ = 0.2

Same as v1.0 except amplitude doubled. CFL still stable (M_max at center = 0.81 vs 0.49 in v1.0).

| Measurement | Value | vs v1.0 |
|:---|:---:|:---:|
| Max \|v(t)\| | 3.3 × 10⁻⁴ | 3.7× larger |
| ω_v peak (FFT) | 0.7363 | **identical bin** |
| ω_δ peak (FFT) | 0.7363 | **identical bin** |
| Peak of ⟨ρ⟩ − ρ* | 3.3 × 10⁻³ | 3.7× larger |
| 3rd-harmonic ratio | 0.049% | slightly smaller |

### v1.1b — amp = 0.45, σ = 0.3 (wider bump)

Widened the Gaussian to sustain spatial structure longer. CFL marginal but stable.

| Measurement | Value | vs v1.0 |
|:---|:---:|:---:|
| Max \|v(t)\| | 8.1 × 10⁻⁴ | **9× larger** |
| ω_v peak (FFT) | 0.7363 | **identical bin** |
| ρ_center range during run | [0.051, 0.545] | large excursion |
| ⟨ρ⟩ range | [0.438, 0.551] | 11% domain-level variation |
| 3rd-harmonic ratio | 0.077% | basically same |

**Figure in this folder is the v1.1b run (wide-bump), as the more aggressive attempt.**

## Why the nonlinearity doesn't appear

Diagnosis from the time-series data:

1. **The bump equilibrates in ~20-40 time units** due to PME spreading + penalty relaxation. After that, the field is nearly uniform at ρ ≈ ρ*.
2. **During the oscillation phase** (t > 40), the uniform-mode density deviation from ρ* is tiny (max ~8 × 10⁻³). So the mobility `M(ρ) = (ρ_max − ρ)^2` is essentially constant during each oscillation cycle, varying only by ~3%.
3. **The nonlinear renormalization requires M(ρ) to vary significantly across the oscillation.** That requires either:
   - A sustained large spatial gradient (which bump-IC loses via spreading)
   - A large uniform-mode oscillation amplitude (which the linear theory's γ = 0.0515 damping prevents from growing)

Both paths are blocked in the Gaussian-bump IC protocol at any amplitude the explicit solver can handle.

## What the Foundational Paper v2 must have done differently

Candidate explanations for the 54% renormalization reported in §8:

1. **Different initial condition.** A sustained non-equilibrium state — e.g., two-peak IC, top-hat profile, or continuously-forced boundary — could keep M(ρ) varying over the oscillation timescale. The paper text describes "Gaussian IC" but this is not the only possibility.
2. **Different solver.** A semi-implicit or fully-implicit scheme could handle amp → 0.48 (very close to the capacity bound), where M varies by >100% during oscillation. Our explicit Euler is CFL-limited to amp ≤ 0.45 approximately.
3. **Measurement artifact.** If the paper measured ω by some method sensitive to the initial transient rather than the sustained oscillation tail, the PME spreading phase (which is fast and has energy at frequencies much lower than ω_linear) could contribute a spurious peak at ~0.38 rad/s. We do NOT see evidence of this in our data — the sustained tail has a clean peak at 0.7363.
4. **Parameter mismatch.** The paper uses N=128 (vs our N=80) and L not specified. If L is smaller than our L=2, the bump spreading would be different. Not a likely explanation for a 54% frequency shift.

Without access to the original Foundational Paper v2 solver code or a more detailed methods section, we cannot discriminate among these four. **For the purposes of the repo's empirical record, we report the linear-regime result as canonical (v1.0) and flag v1.1 as an attempted-but-not-successful nonlinear reproduction.**

## Implications for the ED program

**This does not falsify Analogue 5.** The core coupling structure (v and ρ_center oscillating at matched frequency) is cleanly reproduced in v1.0 and v1.1. What's not reproduced is the specific numerical value (0.3842) that the paper reports for H=50.

**The LINEAR prediction ω = 0.7054 is cleanly verified in our sims.** That is itself a verification of the PDE's coupling structure at the linear-theory level. The paper's 54% value is a nonlinear finding that deserves independent reproduction before being treated as canon.

**Recommendation:** flag Foundational Paper v2 Analogue 5 §8.4 as "linear prediction verified, nonlinear renormalization pending independent confirmation" in the next revision of the paper.

## Reproducibility

```
v1.1_nonlinear_regime/
├── memo.md                                (this file)
├── analogue5_H50_nonlinear_wide.npz       (v1.1b simulation output; amp=0.45, sigma=0.3)
├── summary.png                            (copied to figures_canonical/Analogue5_Nonlinear_Attempt_H50_v1.1.png)
├── field_snapshots.png
├── time_series.png
├── psd.png
└── harmonic.png
```

Re-run:
```bash
cd analysis/scripts/telegraph_pme/
python3 run_nonlinear.py          # ~2 min
python3 make_figures_v11.py       # ~10 sec
```

## Cross-references

- **v1.0 canonical (linear regime):** [`../v1.0_linear_regime/memo.md`](../v1.0_linear_regime/memo.md)
- **Project README:** [`../README.md`](../README.md)
- **Foundational Paper v2 §8** (the source of the 54% renormalization claim): `Desktop/ED Important Papers/ED_Foundational_Paper_v2.md` §8.4
- **Next steps for the canonical confirmation:** implement semi-implicit PME step (Crank-Nicolson with variable-coefficient Laplacian, or IMEX with method-of-lines + scipy LSODA) to push amp → 0.48. That's a half-day of solver work and is deferred until v1.2 (H-sweep) lands.
