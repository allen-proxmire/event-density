# Observable Sweep — Results

**Program:** Determinability-boundary bits-measurement — robustness phase, axis 2 (observable)
**Status:** Complete. **Verdict: Δ is observable-dependent; the ~1 bit was an artifact. Factorization (M2 ≈ 0) is observable-invariant.**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `examples/observable_sweep.py`; `analysis/observables.py`; `analysis/delta.py` (KSG dispatch)
**Related:** `Phase_ObservableSweep_Implementation.md`; `SizeSweep_Results.md`

---

## The result (S=64, N=400, KSG, k=5)

| Observable | Kind | M1 (within) | M2 (across) | Δ |
|---|---|---|---|---|
| `summed_rho` | scalar | +0.983 | +0.000 | **+0.983** |
| `half_vectors` | vector | +0.977 | +0.035 | **+0.942** |
| `subregion_rho` | scalar | +0.198 | +0.033 | **+0.165** |
| `gradient_rho` | vector | +0.356 | +0.000 | **+0.356** |

**Cross-observable Δ range: [0.165, 0.983], spread = 0.818 bits.** Within each observable, Δ is KSG-stable (k=3,5,7 spreads ≤ 0.076 bits) — so the variation is real, not estimator noise. M2 ≈ 0 for every observable.

## What it means

- **Δ is observable-dependent.** Read the same states globally (summed ρ) → ~1 bit; through a local window → 0.17 bits; through the gradient → 0.36 bits. The "~1 bit" from the size sweep was the information content of `summed_rho`, **not** an intrinsic ED quantity. There is no single scalar "Δ for ED."
- **Factorization is observable-invariant.** M2 ≈ 0 for all four observables — because genuine independence gives zero mutual information between *any* functions of the two sides. This is the robust core.
- **Why this is expected, in hindsight.** Independence is observable-invariant; *strength* of dependence is observable-relative. So the zero (across) is invariant and the magnitude (within) is not — exactly the pattern observed.

## The honest bottom line for the whole Δ program

| Statement | Status |
|---|---|
| Across the boundary, shared info = 0 | **Robust** — to size, estimator, and observable. The genuine finding. |
| Within a region, determination is positive | **Robust** — nonzero under every observable. |
| Within-region determination = ~1 bit | **Artifact** — that value is `summed_rho`-specific; ranges 0.17–0.98 across observables. |
| A single intrinsic "Δ for ED" exists | **Falsified** — within-region magnitude is observable-relative. |

The determinability boundary is characterized by its **perfect, observable-independent severance** (M2 = 0), not by a single bits-lost number. That severance — invariant across every dial we have turned (scale, estimator, observable) — is the measurement program's solid result. The scalar "Δ" is not.

## Artifacts

`examples/sweep_output/observable_sweep.json` (gitignored; regenerate via `python examples/observable_sweep.py`).

---

*End of observable-sweep results. Δ varies 0.17–0.98 bits across observables — observable-dependent, not intrinsic. M2 ≈ 0 holds for every observable: the boundary's perfect severance is the robust, observable-invariant finding; a single scalar Δ for ED is not.*
