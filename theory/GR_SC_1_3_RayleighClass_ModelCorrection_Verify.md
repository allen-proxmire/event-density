# GR-SC 1.3 — Rayleigh-Class Model Correction Verification (F3-verify)

**Status:** Pre-registration + execution-ready. Confirms or
refines the F3 Student-t ν ≈ 30 fit via maximum-likelihood
estimation on the raw pooled `T_motif` sample from F2's
multi-seed run. No new evolution on the lattice; this driver
re-generates the F2 fields deterministically (inheriting the
F2 evolution pipeline) and emits an MLE-refined ν estimate plus
a tightened model band.
**Parents:**
- `theory/GR_SC_1_3_RayleighClass_ModelCorrection.md` §3.1 +
  §4.5 (F3 summary-statistic fit ν ≈ 30; ±10 range from
  10-seed Gaussianity-ratio sampling; F3-verify pre-registered
  as the MLE-refinement follow-up).
- `theory/ED_SC_3_4_sigma1_MultiSeed.md` + execution (F2
  multi-seed run; raw T_motif values regenerated here via the
  same IC-amplitude calibration + 40-snapshot pooling per seed).
- `theory/GR_SC_1_3_RayleighClass_Predictions.md` §5.4 + §8.2
  (current model band ±1.61 % from F3 summary-statistic ν
  envelope; F3-verify output will replace it if the MLE-derived
  band differs).
- `theory/GR_SC_1_5_HorizonKappa_MotifStatistics.md` (tenth-
  pass Rayleigh scaling `κ ∝ |N̂'|·σ_T(effective)/(2√2)`; F3's
  Student-t correction factor `√((ν−2)/ν)` is applied through
  this scaling).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post F2 + F3 consolidation).

---

## 1. Purpose

F3 derived a Student-t ν ≈ 30 best-fit for the `T_motif`
distribution at the canonical operating point, using the
**summary statistic** `⟨σ₁_std⟩ / ⟨σ₁_IQR_proxy⟩ = 1.023`
(multi-seed F2 aggregate) mapped through the analytical
Student-t R(ν) table. This fit is correct in principle but has
two limitations:

- **ν is pinned via two summary statistics only** (the mean σ₁_std
  and the mean σ₁_IQR_proxy across 10 seeds). A direct MLE fit
  on the raw pooled `T_motif` sample uses the full distribution
  shape, not just two moments. The raw MLE is therefore
  statistically more powerful and produces a tighter ν estimate.
- **ν uncertainty was propagated via a 10-seed Gaussianity-ratio
  sampling envelope `[20, 50]`**, giving a ±1.61 % model band on
  κ. The MLE log-likelihood curvature at ν_fit gives a direct
  Fisher-information-based Δν that is typically sharper than
  the sampling envelope, potentially tightening the model band
  further.

F3-verify addresses both limitations by:

1. Regenerating the raw pooled `T_motif` sample (re-running
   the F2 evolution pipeline; the F2 summary JSON did not
   persist the raw `T_motif` values).
2. Running MLE Student-t fit on the ~850-motif pool.
3. Computing Δν from the log-likelihood Hessian curvature at
   ν_fit.
4. Re-emitting the κ correction factor, model band, and
   downstream-citation values.

**No new lattice physics is executed** — the evolution under
canonical parameters is deterministic given seeds, and the
driver regenerates the same fields that F2 used.

This memo is pre-registration plus execution-ready. The driver
is `analysis/scripts/ed_sc_3_4_sigma1_model_verify.py`.

---

## 2. Inputs

- **Raw pooled `T_motif` sample**, regenerated via re-running
  the F2 evolution pipeline:
  - 10 canonical F2 seeds `{11, 22, 33, 44, 55, 66, 77, 88, 99,
    111}`.
  - Per-seed IC-amplitude calibration pre-pass to target
    ξ = 1.7575 lu.
  - 40-snapshot motif extraction per seed at
    `(α_filt = 0.25, N_req = 4, L_ray = 1.08·ξ_measured)`.
  - All `T_motif = λ_neg + λ_pos` values pooled across
    snapshots and seeds — expected sample size ≈ 850.
- **Student-t PDF:**

      f(t | ν, μ, σ) = Γ((ν+1)/2) / (√(νπ)·Γ(ν/2)·σ)
                     · (1 + ((t − μ)/σ)²/ν)^(−(ν+1)/2)

  with `ν > 2` (for finite variance), `μ` location, `σ` scale.
  The κ scaling uses the scale parameter `σ_t = σ · √((ν−2)/ν)`
  (relation between Student-t scale and the Rayleigh-relevant
  second-moment-derived standard deviation).

- **Rayleigh scaling + F3 correction factor** (from GR-SC 1.5 +
  GR-SC 1.3-ModelCorrection):

      κ(ξ) / |N̂'| = σ₁_std · √((ν−2)/ν) / (2√2).

---

## 3. Tasks

### 3.1 MLE Student-t fit

Minimise the negative log-likelihood

    −log L(ν, μ, σ | T_data)
      = −Σᵢ log f(Tᵢ | ν, μ, σ).

over `ν ∈ (2, ∞)`, `μ ∈ ℝ`, `σ > 0`. Implementation: `scipy.stats.t.fit`
returns the MLE `(ν_fit, μ_fit, σ_fit)` via Nelder-Mead or L-BFGS-B
optimisation. As a consistency check, also fit with a custom
objective (scipy.optimize.minimize) and report both.

**Expected outcome based on F3:** ν_fit somewhere in `[15, 50]`
with central value near 30. If ν_fit < 15, the Student-t
assumption becomes questionable (Rayleigh-shape preservation
from F3 §3.4 breaks down) and the Student-t correction factor
may need revision.

### 3.2 ν confidence interval via Hessian

At the MLE optimum, the Fisher information matrix `I(θ)` is the
Hessian of the negative log-likelihood:

    I_ij = −∂² log L / ∂θ_i ∂θ_j   evaluated at θ_fit.

The ν marginal standard error is:

    σ_ν = √((I⁻¹)_{νν}).

Implementation: numerical Hessian via finite differences
(scipy.optimize compute_jacobian) or closed-form Student-t
Fisher information for ν. The **68 % confidence interval** on ν
is `ν_fit ± σ_ν`.

Expected: σ_ν ≈ 2 at ν_fit = 30 with N ≈ 850 samples (the
Fisher information for Student-t ν scales as N × g(ν)/ν² with
g(ν) an O(1) function; N = 850 should pin ν to ±2 for a range
near 30).

### 3.3 Corrected κ scale factor and model band

Using ν_fit and σ_ν:

    scale_factor(ν_fit) = √((ν_fit − 2) / ν_fit).

Central κ correction:

    κ_MLE(ξ_canonical) / |N̂'| = 0.001828 · scale_factor(ν_fit).

Model band from the ν_fit ± σ_ν envelope:

    scale_factor(ν_fit − σ_ν) to scale_factor(ν_fit + σ_ν)
    → κ_model_band_MLE / |N̂'|.

Relative model band:

    ±δκ_model / |κ_MLE| = ±( scale_factor(ν_fit + σ_ν)
                           − scale_factor(ν_fit − σ_ν) ) / 2 / scale_factor(ν_fit).

### 3.4 Comparison to F3 summary-statistic fit

Record:

- `ν_F3_summary = 30` (F3 best fit).
- `ν_F3_envelope = [20, 50]` (F3 10-seed sampling envelope).
- `κ_F3 / |N̂'| = 0.001766` (F3 central).
- `model_band_F3 = ±1.61 %` (F3 band).
- `ν_MLE = ν_fit` (this memo).
- `σ_ν_MLE` (this memo).
- `κ_MLE / |N̂'|` (this memo).
- `model_band_MLE` (this memo).
- **tightening factor = 1.61 % / model_band_MLE** (expected
  ≥ 1, i.e. MLE is at least as tight as summary-statistic).
- Whether ν_MLE is within the F3 envelope `[20, 50]` (expected
  yes).

### 3.5 Student-t assumption validation

Compute the Kolmogorov–Smirnov statistic between the empirical
`T_motif` CDF and the fitted Student-t CDF:

    D_KS = max_t |F_empirical(t) − F_Student-t(t | ν_fit, μ_fit, σ_fit)|.

Report p-value. **Pass criterion (pre-registered): p > 0.05.**
If `p ≤ 0.05` at N = 850, the Student-t family does not fit the
data adequately and F3's correction factor structure requires
revision (e.g. generalised-Gaussian or other family).

---

## 4. Outputs

### 4.1 `sigma1_model_verify_table.csv` (1 row)

    nu_fit, nu_sigma, mu_fit, sigma_fit, N_pooled,
    scale_factor, kappa_central_MLE, kappa_model_band_MLE_rel,
    KS_stat, KS_pvalue, tightening_factor_vs_F3

### 4.2 `sigma1_model_verify_summary.json`

- `method`, simulator-of-record string, F2-parent artefact.
- F2 inputs regeneration diagnostics (per-seed ξ_measured,
  N_pool per seed, total N_pooled).
- **MLE fit block:**
  - `nu_fit`, `nu_sigma`, `mu_fit`, `sigma_fit`, `N_pooled`.
  - Optimisation details (optimiser used, iteration count,
    convergence criterion, final log-likelihood).
  - Hessian-derived full 3×3 parameter covariance (for audit).
- **κ correction block:**
  - `scale_factor_MLE = √((ν_fit−2)/ν_fit)`.
  - `kappa_central_MLE = 0.001828 · scale_factor_MLE`.
  - Model-band envelope from ν_fit ± σ_ν:
    `[scale_factor_lo, scale_factor_hi]` and the corresponding
    κ range.
  - `model_band_rel_MLE` (relative half-width, %).
- **Comparison to F3 summary-statistic fit:**
  - `nu_F3_summary`, `nu_F3_envelope`,
    `model_band_F3 = 0.0161`.
  - `tightening_factor = 0.0161 / model_band_rel_MLE`.
  - Boolean `nu_in_F3_envelope = (20 ≤ nu_fit ≤ 50)`.
- **KS test block:**
  - `KS_stat`, `KS_pvalue`.
  - Pass boolean `student_t_fit_valid = (pvalue > 0.05)`.
- **Downstream update block** (for the consolidation patch
  pass):
  - Updated κ central.
  - Updated model band.
  - Updated GR-SC 1.8 clearance threshold
    (`|N̂'| ≳ 27.78 / (0.35355 · scale_factor_MLE)`).
  - Updated pooled-R2 ratio `|N̂'|/|μ₁| = 0.52 /
    (0.35355 · scale_factor_MLE)`.
- `wall_seconds_total`.

Artefacts live under `outputs/ed_sc_3_4_sigma1/` alongside the
other σ₁-related outputs.

---

## 5. Deliverables

- **Verified `ν_fit ± σ_ν`** from MLE on raw pooled data
  (sharper than F3's summary-statistic `ν ≈ 30 ± 10`).
- **Corrected κ model band** from the MLE Hessian curvature,
  replacing F3's ±1.61 % (sampling-envelope-based).
- **Student-t family validity statement** from the KS test —
  if `p > 0.05`, Student-t remains the canonical fit; if
  `p ≤ 0.05`, a revised family choice is required and the F3
  correction factor structure needs re-derivation.
- **Updated uncertainty hierarchy** if the model band changes
  significantly.

**Expected outcomes (pre-registered):**

- `ν_fit ≈ 30 ± 2`, consistent with F3 summary-statistic fit.
- Model band tightens from ±1.61 % to ≈ ±0.5–1.0 % (N = 850
  samples pin ν more tightly than 10-seed sampling of the
  Gaussianity ratio).
- KS `p > 0.05` validating Student-t as the correct family.
- κ central shifts from 0.001766 by at most ~0.3 % (within
  the MLE σ_ν envelope), well inside the current calibration
  band ±2.4 %.
- Uncertainty hierarchy unchanged: per-real (±9.9 %) > ensemble
  (±8 %) > calibration (±2.4 %) > model (now even smaller).

**Alternative outcomes (pre-registered):**

- If `ν_fit` substantially outside `[20, 50]`: GR-SC
  1.3-ModelCorrection's ν-envelope assumption is refuted;
  recalculate central and band with the new ν.
- If KS `p ≤ 0.05`: Student-t family fails; open F3-alt memo
  to test generalised-Gaussian or stretched-exponential.
- If ν_fit < 10: Rayleigh-shape preservation breaks down
  (F3 §3.4 caveat); open a non-Rayleigh κ derivation.

The driver emits all three outcomes transparently; memo
integration will choose the branch based on the actual results.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F3-verify as the
  MLE-refined Student-t fit on the raw pooled `T_motif` sample
  from the F2 multi-seed run. Pre-registers the three-task
  pipeline (MLE fit, Hessian-based ν uncertainty, KS
  goodness-of-fit), the expected-outcome bands (ν_fit ≈ 30 ± 2,
  model band ≈ ±0.5–1.0 %, KS p > 0.05), and the alternative
  outcomes that would trigger further memo work. Driver:
  `analysis/scripts/ed_sc_3_4_sigma1_model_verify.py`.
  Regenerates F2 fields deterministically (no new physics);
  MLE computation is instantaneous post-field-regeneration.
  No GR-SC 1.3-Predictions patching in this memo —
  consolidation is deferred to a subsequent pass after F3-verify
  execution.
