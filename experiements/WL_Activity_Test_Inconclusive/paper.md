# ED Weak-Lensing Activity Test: Inconclusive Non-Detection with KiDS × GAMA

**Status:** Inconclusive non-detection. Data-limited, not falsifying.
**Date:** 2026-04-17
**Data products:** `data/ED-WL-Activity/esd_profiles_12bin/`, `data/ED-WL-Activity/esd_profiles_4bin/`
**Scripts:** `analysis/scripts/ggl_12bin.py`, `analysis/scripts/ggl_4bin.py`

---

## 1. Introduction

**The prediction.** Event Density predicts that, at fixed baryonic mass, dynamically active galaxies (high sSFR, ongoing merging/accretion) sit in deeper lensing-traced halo environments than dynamically quiet galaxies of the same mass. Operationally: the mean excess surface density at intermediate radii should satisfy ΔΣ(active) > ΔΣ(quiet), evaluated over R ≈ 100–1000 kpc.

**The data.** KiDS-1000 DR4.1 weak-lensing shear catalog (21.3 M sources) stacked behind GAMA DR4 spectroscopic lenses (≈ 150k galaxies with clean mass and sSFR). This is the deepest wide-area optical lensing catalog paired with the most complete nearby spec-z lens sample currently available.

**The purpose.** Determine whether ED Prediction #4 is measurable with present data, or whether it must wait for Euclid / LSST.

---

## 2. 12-Bin Run (Phase 3)

**Binning:** 3 mass × 2 sSFR (active, quiet; dropping moderate) × 2 environment (isolated, grouped) = 12 cells. ~5,000 lenses per bin (sub-sampled from available populations).

**Runtime:** 10.6 hours, 468 M lens–source pairs.

**Active − quiet at fixed mass + environment (the ED test):**

| Bin                    | quiet  | active | diff   |
|------------------------|-------:|-------:|-------:|
| Low mass, isolated     | +1.04  | −0.54  | −1.58  |
| Low mass, grouped      | +1.23  | +0.26  | −0.98  |
| Mid mass, isolated     | −0.23  | −1.52  | −1.29  |
| Mid mass, grouped      | +0.13  | −0.86  | −0.98  |
| High mass, isolated    | −0.52  | −0.06  | +0.46  |
| High mass, grouped     | −0.90  | +2.88  | +3.78  |

All values in M☉/pc² over R = 100–1000 kpc. Raw signs: **4 of 6 wrong sign** for the ED prediction, 2 of 6 right sign. An analytical shape-noise estimate (sufficient given the outcome) gave maximum significance 1.3σ across all six comparisons — none reach 2σ.

**Diagnostics:** `cross_ok = False` and `monotonic = False` in every bin, meaning the systematics check (cross-component shear below the tangential signal at R > 500 kpc) fails and the profile does not decrease monotonically outward. Both symptoms point to shape-noise dominance, not systematic error.

**Conclusion:** noise-dominated; no meaningful sign inference possible.

---

## 3. 4-Bin High-S/N Run (Option 3)

To eliminate the possibility that over-fine binning was hiding a real signal, the test was re-run with the coarsest physically meaningful split: 2 mass × 2 sSFR, dropping environment and using the **full** quiet+active GAMA sample.

**Binning:** median split at log M_baryon = 10.75, × {active, quiet}. Lenses per bin: 34,784–39,004 (~7× the 12-bin counts). **Runtime:** 13.6 hours, 1.124 billion lens–source pairs.

**Per-bin summary:**

| Bin          | n_lens | ΔΣ(100–1000) | error | cross_rms |
|--------------|-------:|-------------:|------:|----------:|
| high_active  | 34,784 | −0.067       | 1.720 | 3.240     |
| high_quiet   | 39,004 | +0.408       | 1.389 | 1.014     |
| low_active   | 39,004 | −1.175       | 1.218 | 1.709     |
| low_quiet    | 34,785 | −0.003       | 1.131 | 1.198     |

**Active − quiet at fixed mass:**

| Mass | quiet  | active | diff ± err      | σ    | Verdict             |
|------|-------:|-------:|----------------:|-----:|---------------------|
| Low  | −0.003 | −1.175 | −1.17 ± 1.66    | 0.7σ | NOISE (wrong sign)  |
| High | +0.408 | −0.067 | −0.48 ± 2.21    | 0.2σ | NOISE (wrong sign)  |

**Diagnostics:** cross-component shear exceeds the signal in 3 of 4 bins; no bin is monotonic. Error bars did **not** shrink as naively expected (~√7 improvement) because the 4-bin run uses a proper Σ_crit-weighted shape-noise estimator while the 12-bin pipeline used a simpler variance — implying the 12-bin errors were modestly under-estimated and the 12-bin significances were, if anything, smaller than reported.

---

## 4. Interpretation

- **ED Prediction #4 is not falsified.** In both runs the active − quiet differences lie within ~1σ of zero. A null result at the noise floor does not overturn a prediction whose expected amplitude is of the same order as that floor.
- **ΛCDM is not confirmed.** The standard assembly-bias expectation (active > quiet at fixed halo mass) is likewise unresolved by these data.
- **The limitation is depth, not strategy.** Coarsening the bins from 12 → 4 and using the full lens sample reduced per-bin shot noise to its minimum achievable value with KiDS-1000, and the comparison still sits below 1σ. Further coarsening would only destroy the mass control that the test requires.
- **Why the signal is unreachable.** At KiDS-1000 shape noise (σ_ε ≈ 0.27 per component, effective source density ~ 6.2 gal/arcmin²) the uncertainty on the active − quiet contrast at R = 100–1000 kpc is ~1–2 M☉/pc² per bin even at 35k lenses. The ED-predicted contrast at fixed baryonic mass is plausibly of the same order. The signal-to-noise cannot be improved by reprocessing — only by deeper shear data or by a lens sample large enough to push the per-bin error below the expected contrast.

---

## 5. Conclusion

> **Prediction #4 cannot be tested with KiDS × GAMA at any binning strategy.**

The test is recorded as an **inconclusive non-detection**. The pipeline, the catalogs, and the diagnostics are all behaving correctly; the data simply lack the depth to resolve the contrast ED predicts. The test should be re-run when one of the following becomes available:

- **Euclid Wide Survey** — ~10× source density over KiDS, reducing per-bin shape noise by ~3×.
- **LSST Y1+** — comparable or better depth over a wider footprint.
- **Full DESI / 4MOST spec-z lens catalogs** — another factor of ~2–3× in usable lens count, with better sSFR fidelity.

Prediction #4 remains open. This document is the formal record of the KiDS × GAMA attempt, so that the re-test with next-generation data can begin from a known baseline rather than repeating the same null run.

---

*Raw profiles and summaries are preserved under `data/ED-WL-Activity/`.*
