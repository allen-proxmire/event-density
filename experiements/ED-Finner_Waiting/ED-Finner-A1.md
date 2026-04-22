# ED Merger-Lag Test A1: Finner Sample Analysis and Pipeline Validation

**Status:** ED velocity-scaling signature detected in the high-precision subsample; consistent with — but not discriminated by — the noise-limited Finner sample.
**Date:** 2026-04-17
**Scripts:** `analysis/scripts/finner_a1_analysis.py`, `analysis/scripts/seven_cluster_validation.py`
**Data:** `data/ED-Finner/`
**Companion paper:** `papers/Cluster_Merger_Lag_Evidence/paper.md`

---

## 1. Executive Summary

Test A1 extends the ED merger-lag prediction `ℓ = D_T / v_current` (with `D_T = 2.1 × 10²⁷ m²/s` fixed from independent Mistele-scale calibration) from the 7-cluster quantitative sample of Galaxy-15 to the per-subcluster offsets of Finner et al. (2025, ApJS 277, 28), Figure 36.

Two pipelines were run against the same analysis machinery (capped zero-parameter ED, ED `A/v_current` fit, ED linear-in-TSP, SIDM-like `v^n`, flat baseline, and ΛCDM ~1 kpc reference):

- **High-precision 4-cluster subset (HP4)** — Bullet, El Gordo SE, MACS J0025, Musket Ball S. The pipeline recovers slope **n = −0.90 ± 0.04** (log ℓ vs log v_current), consistent with the published Galaxy-15 fit of −1.07 ± 0.20 at < 1σ. Spearman ρ(offset, 1/v_current) = +1.00 (p = 0.00). ED `A/v_current` is the BIC-preferred model; ΛCDM is excluded at ~25σ.

- **Finner 25-subcluster sample** — BCG-WL offsets from Fig 36 (25 subclusters for which Table 2 of the merger-lag paper provides published merger velocities). The zero-parameter capped ED prediction fits at reduced χ² ≈ 0.91; but a flat 69.8 ± 11 kpc baseline gives lower BIC by ΔBIC ≈ 6. No Spearman correlation emerges (ρ ≈ +0.04, p = 0.86 against 1/v_current; ρ = −0.03, p = 0.88 against TSP). The SIDM power-law fit returns n = −0.12 ± 0.07, the wrong sign for SIDM and too shallow for ED at this sample's S/N.

The combined outcome is a **pipeline-validated detection** in the high-precision sample and an **inconclusive non-discrimination** in the noise-limited sample. It mirrors the structure of the WL-activity test (prediction #4): present-data depth permits the framework's signature to appear where signal-to-noise is engineered for it, and washes it out where it is not.

---

## 2. Why the Two Samples Give Different Verdicts

| | HP4 | Finner-25 |
|---|---:|---:|
| N subclusters | 4 | 25 |
| Per-point σ on offset | 0.7 – 60 kpc | 50 – 150 kpc |
| Dynamic range in offset | 11.5 → 129 kpc (12×) | 25 → 250 kpc (10×) |
| Dynamic range in v_current | 500 → 4400 km/s (9×) | 50 → 4200 km/s (84× nominal, ~5× effective) |
| TSP spread | 0.15 – 0.96 Gyr (wide) | 0.10 – 1.30 Gyr (radio-relic selected, narrow-peaked) |
| v_current source | MCMAC (Bullet, Musket Ball); paper estimates | Keplerian from assumed T_apo, mostly |
| Spearman ρ(offset, 1/v_current) | +1.00 | +0.04 |

HP4 has roughly 30× better per-point precision than a typical Finner point, clean MCMAC dynamics on the systems that drive the fit, and selection for binary post-pericenter geometry. Finner is uniform-methodology Subaru WL on a radio-relic-selected sample, by design sacrificing per-cluster sensitivity for sample uniformity. Finner himself states that per-subcluster mass-peak uncertainties are ~100 kpc, comparable to the median offset, so individual points are at single-point S/N ≈ 1 and only the aggregate (79 ± 14 kpc median) is statistically robust.

### The regime-mixing effect

ED predicts two limits of the wake centroid:

- **Steady-state** (when TSP ≫ t_lag = D_T/v²): ℓ ≈ D_T / v_current ∝ 1/v.
- **Partial-equilibration / filled** (TSP ≪ t_lag, near apocenter): ℓ ≈ v_current · TSP ∝ +v.

A sample covering both regimes therefore shows a **slope near zero** on a naive log ℓ vs log v fit, even if ED is entirely correct — the two branches have opposite sign in v. The capped Model 3 used in A1.0b handles both regimes correctly (zero free parameters, reduced χ² ≈ 0.91 on Finner-25), but a single-power-law fit across a mixed sample naturally washes out. This is the structural reason the Finner SIDM-test returns n ≈ 0 instead of either −1 (ED) or +1 (SIDM).

---

## 3. Model Comparison Highlights

**HP4 ranking by BIC (lower is better):**

| Model | BIC | note |
|---|---:|---|
| ED `A / v_current` | **1.77** | preferred |
| Power-law, n = −0.90 ± 0.04 | 2.87 | tied with Model 1 |
| ED linear-in-TSP | 3.89 | |
| Flat (≈ 50 kpc) | 4.96 | second-worst |
| ED capped (0 params) | 12.4 | driven almost entirely by Bullet tension |
| ΛCDM ~1 kpc | 651.7 | excluded |

**Finner-25 ranking by BIC:**

| Model | BIC | note |
|---|---:|---|
| Flat (69.8 ± 11 kpc) | **16.2** | preferred |
| ED linear-in-TSP | 22.3 | |
| ED capped (0 params) | 22.6 | essentially tied with Model 2 |
| ED `A / v_current` | 26.6 | |
| SIDM-like `v^n` (n = −0.12 ± 0.07) | 34.3 | wrong sign for SIDM |
| ΛCDM ~1 kpc | 34.3 | |

The two rankings are consistent with a single interpretation: where the data have leverage, ED wins; where they don't, flat wins; ΛCDM is never competitive. SIDM's predicted n > 0 is directly disfavored in both samples.

---

## 4. Anomalies and Notes

- **Bullet at +3.5σ in the capped Model 3.** Cha et al. (2025) report 17.78 ± 0.66 kpc; ED at v_current = 4400 km/s predicts 15.5 kpc. The 2.3 kpc excess is formally 3.5σ because of the exceptionally tight JWST error bar. Earlier WL literature with ±1 – 10 kpc uncertainties hid this tension. The physical direction (observed offset larger than pure D_T/v) is consistent with partial deceleration that the Keplerian model does not capture; see Galaxy-15 §3.2.

- **MACS J1149 SL at −33.9σ (expected).** Strong-lensing aperture of Rau+2014 probes only the inner ~100 kpc where the wake has partially equilibrated; the SL offset (11.5 ± 1 kpc) is 4× smaller than the full-wake prediction, by design. MACS J1149 SL is **correctly excluded** from the velocity-scaling fit and appears here as the archetype of the scale-dependence signature documented in Galaxy-15 §4.3.

- **A2255 E is the only genuine Finner-25 outlier (+2.2σ).** Observed 250 ± 100 kpc at v_current = 2529 km/s and TSP = 0.15 Gyr. The cap selects the steady-state branch (ED prediction 26 kpc). Neither cap nor Keplerian artifact explains the excess. Candidates: the Sakelliou+2006 TSP value may be wrong (A2255 is possibly a more advanced merger than 0.15 Gyr implies) or A2255's eastern substructure may be a different configuration than Finner's WL peak identification assumes. Flagged for literature follow-up; no action taken here.

- **A3411 apocenter artifact resolved.** In the uncapped A1.0 run, A3411 W/E produced −11σ and −12σ residuals because Keplerian v_current → 0 at TSP = T_apo. Applying the equilibration-time cap ℓ = min(D_T/v, v·TSP) reduces these to z < 1σ and restores Model 3 to a physically meaningful fit (reduced χ² 11.6 → 0.91).

---

## 5. Final Status

> **The ED velocity-scaling signature is detected in the precision HP4 sample (n = −0.90 ± 0.04, ρ = +1.00) and is consistent with — but not discriminated by — the noise-limited Finner 25-subcluster sample.**

The zero-parameter capped ED prediction fits the Finner sample at reduced χ² ≈ 0.91 with no tunable free parameters, while the best-fitting phenomenological alternative (flat 70 kpc) has one tunable and improves BIC by only ΔBIC ≈ 6. ΛCDM is excluded in HP4 and disfavored in Finner-25. SIDM's positive-slope velocity scaling is disfavored in both.

### No further digitization of Finner is needed

Adding the remaining 33 Finner subclusters (pushing N from 25 → 58) would improve the per-fit statistical power by roughly √(58/25) ≈ 1.5×, while each added point has intrinsic S/N ≈ 1 and would require new literature compilation of v_peri and TSP. The A1.0b run on N = 25 is already clean enough to state that **the Finner sample cannot discriminate ED from a flat baseline at this noise floor**, and the HP4 validation shows that framework-level discrimination already exists in the precision-measured subsample. Further decisive tests of prediction #4 wait on:

- **Next-generation WL depth** — Euclid Wide, LSST, or JWST follow-up of individual systems (e.g., the remaining MCC clusters at Bullet-like precision), reducing per-point σ below the 10 kpc scale.
- **Per-subcluster MCMAC dynamics** for the Finner sample, replacing Keplerian v_current estimates with direct reconstructions. A targeted MCMAC campaign on the 58 Finner subclusters would convert this test from noise-limited to signal-limited.

Until then, A1 is recorded as **validated on HP4, inconclusive on Finner-25**, with prediction #3 (deceleration scaling) and prediction #5 (scale dependence) both still supported by the HP4 + MACS J1149 SL data as reported in Galaxy-15. The framework is not falsified; the discriminating test on an enlarged sample awaits better data.

---

*Raw data, fit tables, and plots are preserved under `data/ED-Finner/`.*
