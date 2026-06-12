# Robustness Sweep — Results (Δ vs Size, and the Estimator Check)

**Program:** Determinability-boundary bits-measurement — robustness phase, axis 1 (size)
**Status:** Complete. **Key finding: the *structure* is robust; the *value* is not (yet).**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/examples/size_sweep.py`; bin-resolution check inline
**Related:** `Delta_Results.md`; `Phase_Delta_Implementation.md`; measurement plan §7–§8

---

## Summary

The robustness sweep ran in two stages — a histogram pass that exposed a problem, and a KSG pass that resolved it.

1. **Factorization is scale- and estimator-robust.** Across-boundary MI (M2) is ≈ 0 at *every* size (8–256 nodes per stratum) and *every* estimator tested. The boundary severs cleanly regardless of scale or measurement choice. This is the strongest statement in the study.
2. **The histogram estimator was unreliable for the within-stratum number.** With 2-bin histograms, Δ "converged" to ~0.92 — but varying the bin count alone swung it 0.46–0.99 bits. That convergence was an estimator artifact, not a property of the substrate.
3. **A binning-free (KSG) estimator resolves it.** Stable under its own knob (k≥3 → ~1.05 bits, vs the histogram's 0.46–0.99 across bins), and across a 16× size range it gives **Δ ≈ 1.0 bit** (mean 1.006, N=400), scattering as finite-N noise around 1.0 with no trend.

**Conclusion (current honest position):** Across the boundary, shared information is zero — robust to scale and estimator. Within a region, determination is worth about **one bit** — now robust to *scale and estimator*, but **not yet** tested against topology, observable, or dynamics. The earlier 0.09 and 0.92 were estimator-specific; ~1 bit is the size- and estimator-robust value. Whether ~1 bit is intrinsic to ED or a property of the chosen observable (summed ρ) is the next question.

---

## Size sweep (2-bin estimator)

```
   S        M1        M2        M3      Delta    M2~0?   nat%
   8    +0.0920   -0.0025   -0.0010   +0.0945    True   100%
  16    +0.9156   -0.0036   -0.0033   +0.9192    True   100%
  32    +0.9156   -0.0033   -0.0025   +0.9189    True   100%
  64    +0.9156   +0.0010   -0.0010   +0.9146    True   100%
 128    +0.9156   +0.0010   +0.0010   +0.9146    True   100%
```

(N = 200 per size, all runs terminated naturally at a fixed point.)

At 2 bins, M1 jumps from 0.09 (S=8) to 0.92 (S≥16) and then sits flat. The flatness *looked* like convergence — but see below.

## Bin-resolution check (S = 32, the same ensemble)

```
 bins   ceiling      M1        M2      Delta
   2      1.00    +0.916   -0.003   +0.919
   3      1.58    +0.462   -0.004   +0.466
   4      2.00    +0.933   -0.021   +0.954
   6      2.58    +0.952   +0.010   +0.943
   8      3.00    +0.959   -0.032   +0.991
```

M1 does not converge as resolution increases — it is jagged (0.46–0.99) and non-monotone. A well-behaved MI estimate would rise smoothly toward a stable limit as bins increase. This jaggedness is the signature of an **estimator failing on a near-deterministic relationship**: the two halves of a stratum are so tightly coupled (the same propagation front fills both) that their mutual information is near-saturated, and a coarse histogram on a continuous, nearly-deterministic pair gives a value that depends on where the bin edges happen to fall.

Meanwhile M2 stays ≈ 0 at every bin count — because genuine independence is *easy* to estimate (there is no relationship for the binning to mis-resolve).

---

## What this means

- **The boundary result is real and robust.** M2 ≈ 0 across all sizes and all binnings is the strongest, most estimator-independent statement in the whole study: across the determinability boundary, there is no shared information, full stop. Scale does not weaken it.
- **The within-stratum determination is near-total, but its exact bit-value is ill-posed under this estimator.** For S ≥ 16, the two halves of a region are almost perfectly mutually determined — M1 sits near the binning ceiling at every resolution. That qualitative fact (near-total within-region determinability) is robust. The precise number is not: the histogram estimator cannot pin it down for a near-deterministic continuous pair at N = 200.
- **The earlier 0.09 and the sweep's 0.92 are both estimator-specific.** 0.09 was S=8 at 2 bins; 0.92 was S≥16 at 2 bins. Neither is an intrinsic Δ. The honest position is the one stated from the start, now sharpened: the *value* is configuration- and estimator-dependent; the *structure* (within ≫ across = 0) is what holds.

This is the robustness program working as intended. It tested whether the headline number survives changing things that shouldn't matter — and found that, for the magnitude, it does not. That is a more valuable outcome than a falsely tidy convergence: it tells us precisely what to fix before any Δ value can be trusted.

---

## Resolution — the KSG (binning-free) estimator

The histogram failure was diagnosed as estimator saturation on a near-deterministic pair. We implemented the standard fix — a **Kraskov–Stögbauer–Grassberger (KSG) k-nearest-neighbour estimator** (`analysis/entropy.py:mutual_information_ksg`), which does not discretize — and re-ran the sweep. Two checks:

**(a) The KSG estimator is stable under *its own* knob (k), at S=32:**

```
 k= 2   Delta=+1.194
 k= 3   Delta=+1.045
 k= 5   Delta=+1.066
 k= 7   Delta=+1.058
 k=10   Delta=+1.047
```

For k≥3 the value clusters tightly at ~1.05 bits — versus the histogram's 0.46–0.99 swing across bins. The gross estimator-dependence is resolved: KSG does not drift the way binning did.

**(b) KSG size sweep (N=400, k=3), across a 16× size range:**

```
   S        M1        M2        M3    Delta=M1-M3
  16    +0.996    +0.007    +0.020    +0.976
  32    +1.067    +0.034    +0.051    +1.016
  64    +0.926    +0.004    +0.015    +0.911
 128    +1.086    +0.000    +0.000    +1.086
 256    +1.041    +0.000    +0.000    +1.041
```

**Δ ≈ 1.0 bit** for every size S ≥ 16 (mean 1.006, range [0.911, 1.086], spread 0.175 with no monotone trend — scatter around a stable ~1.0, consistent with finite-N noise). M2 sits at the KSG floor (≈ M3), so factorization holds throughout.

### What the KSG result establishes — and what it does not

**Established (real progress):**
- The estimator problem is fixed. Under a binning-free estimator that is stable to its own parameter, **Δ does not wander — it settles at ≈ 1.0 bit** across a 16× size range. The earlier 0.09 (S=8, 2-bin) and 0.92 (S≥16, 2-bin) were both estimator artifacts; the size- and estimator-robust value is ~1 bit.
- Across the boundary, M2 ≈ M3 ≈ 0 at every size — factorization remains the most robust statement in the study.
- Interpretation: within a region, the two halves share about **one bit** of determination (roughly one yes/no question's worth), and the boundary erases all of it.

**Not yet established (honest caveats):**
- **Only the size axis is closed.** Δ ≈ 1 bit is robust to *size* and *estimator*. It has **not** been tested against topology (still chains), the observable (still summed ρ), the Σ coefficients, or the reach profile. The value could still be specific to "summed-ρ on a chain."
- **The round ~1 bit warrants suspicion.** The summary statistic (total ρ) is dominated by one near-binary feature — essentially *how far the front swept the region* — which by itself carries about a bit. So ~1 bit may partly reflect the *observable's* own information content, not a deep ED constant. A richer observable is needed to tell these apart.

**Bounded claim (current honest position):**

> Across the determinability boundary, shared information is zero — robust to scale and estimator. Within a region, determination is worth about **one bit**, robust to scale and estimator but **not yet** tested against topology, observable, or dynamics. Whether ~1 bit is an intrinsic ED quantity or a property of this observable is the next question.

## Next steps

1. **Vary the observable** (off the saturated summed-ρ): sub-regions, rates, orientation-based or per-node quantities — does Δ stay ~1 bit, or was 1 bit the observable's own content?
2. **Vary topology and reach profile**: trees, grids, graded vs. hard decoupling, multiple strata — does Δ ≈ 1 bit persist, or does it depend on structure (a scaling law)?
3. **Vary the Σ coefficients**: is Δ robust to the rule's tuning?

If Δ ≈ 1 bit survives those, it is a candidate *intrinsic* quantity of the ED architecture. If it moves lawfully, that dependence is itself the finding. If it scatters, the honest conclusion is that Δ is observable-defined, not intrinsic.

---

## Artifacts

`Bits/examples/sweep_output/` — `size_sweep.json` (per-size M1/M2/M3/Δ), `size_sweep.png` (Δ, M1, M2 vs size). (Gitignored as regenerable; `python examples/size_sweep.py` reproduces them.)

---

*End of size-sweep results. Factorization is scale- and estimator-robust (M2 ≈ 0 always). The within-stratum value is near-saturated and estimator-dependent (0.46–0.99 across binnings), so the precise Δ magnitude is not yet trustworthy. The robust finding is structural — within ≫ across = 0 — not numerical. A binning-free estimator and a non-saturated observable are the next steps toward a real Δ value.*
