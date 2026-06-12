# Phase Bits / Observable Sweep — The Decisive Test

**Program:** Determinability-boundary bits-measurement — robustness phase, axis 2 (observable)
**Document:** Observable-sweep implementation and result
**Status:** **Implemented, run — and it falsifies the intrinsic-Δ hypothesis.** Δ is observable-dependent; factorization is observable-invariant.
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `SizeSweep_Results.md` (the ~1-bit result this tests); `analysis/observables.py`, `analysis/delta.py`; `ObservableSweep_Results.md`

---

## 1. Purpose

The size sweep, with a binning-free (KSG) estimator, found Δ ≈ 1.0 bit stable across a 16× size range. That left one sharp question, and this phase answers it: **is ~1 bit an intrinsic property of the ED architecture, or an artifact of the specific observable (summed ρ) we happened to read out?**

This is the decisive test. We measure Δ under four genuinely different readouts of the same final states. The logic is falsification:

- If Δ stays ~1.0 ± 0.1 bit across observables → ~1 bit is likely **intrinsic** to ED.
- If Δ varies widely across observables → ~1 bit was an **observable artifact**, and there is no single "Δ for ED."

In either case, across-boundary MI (M2) must remain ≈ 0 — factorization should not care what you measure.

---

## 2. Observables

Four readouts of a region's final state, deliberately spanning global/local and level/derivative (`analysis/observables.py`):

| Key | Observable | Kind | What it reads |
|---|---|---|---|
| **A** | `summed_rho` | scalar | total commitment density over the region (the baseline) |
| **B** | `half_vectors` | vector | per-node ρ vector (full resolution; high-dimensional MI) |
| **C** | `subregion_rho` | scalar | ρ over a contiguous 4-node window only (local; discards most of the region) |
| **D** | `gradient_rho` | vector | discrete gradient of ρ along the region (a derivative readout) |

Each supports M1 (within-stratum, between two halves), M2 (across-boundary), and M3 (shuffle null). Vector observables are handled natively by KSG (max-norm k-NN over the feature dimensions).

---

## 3. Code

- **`analysis/observables.py`** — `get_summed_rho`, `get_half_vectors`, `get_subregion_rho`, `get_gradient_rho`, plus an `OBSERVABLES` registry tagging each scalar/vector.
- **`analysis/delta.py`** — `_mi_bits` now dispatches on `estimator` ("ksg" | "hist"); `compute_M1/M2/M3/compute_all` thread `estimator` and `k`. Shuffle control shuffles along the sample axis (so vector features keep their structure). The histogram default is preserved, so earlier callers are unaffected.
- **`examples/observable_sweep.py`** — fixes S=64, N=400, builds one ensemble of runs, and re-measures Δ for every observable at k∈{3,5,7} (KSG-knob stability), reporting the cross-observable spread.

All MI is computed with the KSG estimator (the size sweep showed histogram MI is unreliable here). k is swept to confirm each observable's Δ is KSG-stable, not estimator noise.

---

## 4. Sweep protocol

- **Size** fixed at S = 64 (midpoint of the size-stable region).
- **Ensemble** N = 400 independent runs (independent per-stratum seeds).
- **For each observable:** build the (A, B, A_left, A_right) feature arrays, compute M1/M2/M3/Δ at k = 3, 5, 7, record the k-spread, report Δ at k = 5.
- **Assess** the cross-observable Δ spread and whether M2 ≈ 0 throughout.

---

## 5. Result

Executed; recorded output (Δ at k = 5):

```
   observable    kind   k       M1       M2       M3    Delta
  summed_rho   scalar   5   +0.983   +0.000   +0.059   +0.983
  half_vectors vector   5   +0.977   +0.035   +0.000   +0.942
  subregion_rho scalar  5   +0.198   +0.033   +0.004   +0.165
  gradient_rho vector   5   +0.356   +0.000   +0.000   +0.356

  Delta (k=5) by observable:
        summed_rho:  +0.983 bits
      half_vectors:  +0.942 bits
     subregion_rho:  +0.165 bits
      gradient_rho:  +0.356 bits

  cross-observable Delta range : [+0.165, +0.983]  spread = 0.818 bits
  M2 ~ 0 for all observables   : True
  VERDICT: VARIES across observables -> Delta is observable-DEPENDENT
```

Per-observable KSG-knob stability (k = 3,5,7) was tight throughout — k-spreads of 0.076 / 0.060 / 0.059 / 0.014 bits — so the cross-observable variation is **real, not estimator noise.**

---

## 6. Verdict against the acceptance criteria

| Criterion | Outcome |
|---|---|
| Δ ~ 1.0 ± 0.1 across all observables → intrinsic | **FAILED** — Δ ranges 0.165 → 0.983, spread 0.818 bits |
| Δ varies widely → observable-dependent artifact | **CONFIRMED** |
| M2 ≈ 0 for all observables | **HELD** — M2 at the KSG floor for every observable |

**The ~1 bit was an artifact of `summed_rho`.** It is not an intrinsic property of the ED architecture. Read the same states a different way and the within-region determinability is 0.17 bits (a local window), 0.36 bits (the gradient), or ~0.95 bits (global level / full vector). There is **no single "Δ for ED"** — the magnitude of within-region determinability is relative to the observable.

---

## 7. Interpretation — what *is* invariant

The result is not a failure of the program; it is a clarification, and a sharp one.

**Independence is observable-invariant; dependence is observable-relative.** This is a basic but decisive fact of information theory. If two regions are genuinely independent, the mutual information between *any* function of one and *any* function of the other is zero — which is exactly why **M2 ≈ 0 for every observable**. But if two regions are dependent, *how much* information they share depends on what you measure — which is exactly why **M1 (and Δ) varies across observables**.

Therefore the determinability boundary's defining, intrinsic property is the **zero**: across the boundary, every observable agrees that shared information vanishes. That severance is observable-invariant, scale-invariant, and estimator-invariant — the genuine, robust finding. The *within*-region "amount of determinability," by contrast, is not a single number; it is a property of the question you ask, not of the architecture alone.

**Consequence for the Factor Skyline parallel.** This refines the parallel honestly. FS's parity barrier has a defined scalar (escape density ≈ 0.265) within its own framework. The clean ED analogue is **not** a scalar bits-lost figure — that quantity is observable-relative — but the **qualitative invariant**: perfect, observable-independent severance across the determinability boundary (M2 = 0). The two systems still share the *structural* motif (a finite-reach boundary past which determination fails); they do not share a single comparable number, and this sweep is what establishes that, rather than assuming it.

---

## 8. What this settles, and what remains

**Settled:**
- ~1 bit is **not** intrinsic; it was the information content of `summed_rho`.
- The robust, observable-invariant statement is **M2 = 0** — perfect severance across the boundary.
- There is no single scalar "Δ for ED" via this approach; within-region determinability is observable-relative.

**Still open (lower priority now):**
- Topology and reach-profile sweeps remain unrun, but the observable result already shows a single intrinsic Δ value is not on the table, so these would refine the *structure*, not rescue a scalar.
- A principled, observable-independent characterization of the boundary (e.g. whether the *set* of within-region MIs has an invariant feature, or whether channel-capacity rather than a single-observable MI is the right object) is the genuinely interesting direction — but it is a reformulation, not a parameter sweep.

---

## 9. Deliverables

- **`analysis/observables.py`** — the four observables + registry.
- **`analysis/delta.py`** — estimator dispatch (KSG/hist), vector-safe shuffle.
- **`examples/observable_sweep.py`** — the sweep (S=64, N=400, k∈{3,5,7}).
- **`ObservableSweep_Results.md`** — recorded run and assessment.
- **`Phase_ObservableSweep_Implementation.md`** — this document.

Artifacts: `examples/sweep_output/observable_sweep.json` (gitignored; regenerable via `python examples/observable_sweep.py`).

---

*End of observable sweep. The decisive test ran and falsified the intrinsic-Δ hypothesis: Δ varies 0.17–0.98 bits across observables (spread 0.82), KSG-stable within each, so the ~1 bit was an artifact of summed-ρ. What survives is the zero — M2 ≈ 0 for every observable — the observable-invariant severance that genuinely characterizes the determinability boundary.*
