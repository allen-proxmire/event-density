# ED-SC 3.4-σ₁ — σ₁ Calibration within r_diag = 1

**Status:** Pre-registration + execution-ready. Opens the σ₁
calibration scan on the same operating grid as ED-SC 3.4 (S2
calibration) but measuring the spread of the Hessian-trace
distribution instead of the spread of the eigenvalue-ratio
distribution. No falsifier verdict; pure calibration for
downstream GR-SC 1.3+ / 1.8 use.
**Parents:**
- `theory/ED_SC_3_4_XiCalibration.md` (S2 calibration blueprint;
  this memo inherits its ξ-control method, seed, cadence, grid,
  and r_diag guardrail unchanged).
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5
  (authoritative table; row for `κ` marked **awaits ED-SC 3.4-σ₁
  scan** — this memo is that scan).
- `theory/GR_SC_1_5_HorizonKappa_MotifStatistics.md` (tenth-pass
  arc; Rayleigh-class surface-gravity `κ` scales as `|N̂'|σ_1/
  (2√2)`; pooled-R2 `κ/(|μ₁|σ_1) = 0.52 ± 0.05`).
- `theory/GR_SC_1_8_EIT_Extremal_ErrorBudget.md` (integration
  memo; clearance target `σ₁/κ_M^det < 0.036` needs σ₁ calibrated).
- `theory/ED_SC_3_3_10_ArcClosure.md` §3 (four-clause final
  invariance statement; r_diag = 1 canonical window).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (ensemble-only
  caveat; inherited for σ₁ with the same ~25 % per-realisation
  spread assumption pending empirical verification).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness;
  verdict taxonomy; r_diag window guardrail).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post GR-SC 1.0 / 1.0a / 1.1 / 1.2 consolidation).

---

## 1. Purpose

ED-SC 3.4 calibrated `S2(ξ) = −0.322 + 1.396·ξ` over 9 points in
`ξ ∈ [1.60, 1.95]` and produced the ensemble-pool Quadratic-class
inputs that GR-SC 1.2 consumed for the `C²` and `det G`
quantitative predictions. The **remaining single-point curvature
invariant** on the GR-SC 1.0 §5 authoritative table is the
Rayleigh-class surface gravity `κ`, whose tenth-pass scaling

    κ_pooled / (|μ₁| · σ₁) = 0.52 ± 0.05

requires **σ₁(ξ)** — the spread of the Hessian-trace distribution
at admitted motifs — calibrated across the canonical r_diag = 1
window.

ED-SC 3.4-σ₁ executes that calibration. The scan mirrors ED-SC
3.4 exactly (same ξ grid, same fixed seed, same IC-amplitude
ξ-control, same 40-snapshot pooling, same filter geometry) but
measures σ₁ instead of S2. After this memo closes:

- GR-SC 1.3 (Rayleigh-class predictions) can be opened as the
  third quantitative prediction layer, analogous to GR-SC 1.1
  and 1.2 but on σ₁ instead of S1 or S2.
- GR-SC 1.8's EIT-Extremal `σ₁/κ_M^det < 0.036` clearance target
  becomes numerically actionable.

This is a **calibration**, not a falsifier. The distributional
claim is characterised at each ξ point; no cross-ξ invariance
verdict is pre-registered.

---

## 2. Operating point

Identical to ED-SC 3.4 §2 to maximise cross-comparability between
the S2 and σ₁ calibrations:

- **Filter:** `α_filt = 0.25`, `N_req = 4` (canonical, fixed).
- **Hinge:** `L_ray = 1.08 · ξ_measured` per ξ point (canonical
  continuous hinge).
- **ξ window:** `ξ ∈ [1.60, 1.95] lu` (r_diag = 1 canonical
  domain per ED-SC 3.3.10 clause c).
- **ξ grid:** `{1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.93,
  1.95}` — 9 points matching ED-SC 3.4.
- **Snapshot cadence:** burn-in 100, snap every 10, **40
  snapshots per ξ**.
- **Fixed seed:** `77` (reproducibility; matches ED-SC 3.4 /
  ED-SC 3.3.8a).
- **Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility` with canonical parameters
  unchanged.
- **ξ-control method:** IC-amplitude calibration pre-pass +
  interpolant + one bisection refinement if |miss| > 1 % —
  verbatim from ED-SC 3.4 / ED-SC 3.3.8a.

---

## 3. Measurement definition

**σ₁ target statistic.** For each admitted motif, the
eigenvalues of the 2D field-space Hessian at the saddle
(`λ_neg`, `λ_pos`) are already computed by the motif filter
pipeline; their ratio becomes `S1 = r*`. Their **trace**

    T_motif ≡ λ_neg + λ_pos

is the Hessian-trace diagnostic. Pooled across all admitted
motifs from the 40-snapshot trajectory at a given ξ point, the
distribution of `T_motif` is Trace-Gaussian-class per the tenth-
pass arc (rigidly zero median; Gaussian shape; scale set by
`|μ₁|·σ_2²`·k). Its **spread** is the σ₁ calibration target:

    σ₁(ξ) ≡ std{ T_motif : motif ∈ pool(ξ) }

with a standard-deviation definition. The driver also records
the IQR-based proxy `IQR(T_motif) / 1.349` for cross-check (the
1.349 factor converts a Gaussian IQR to a standard deviation;
discrepancies flag non-Gaussianity).

**Bootstrap CI.** 4000 resamples on the pool of `T_motif`
values per ξ point; 16–84 band reported for σ₁.

**Per-snapshot diagnostic.** At each of the 40 snapshots,
record `N_snap` (admitted motif count) and the per-snapshot
`std(T_motif)` where N_snap ≥ 4 (below which std is unstable).
Deviations from stationarity show up as large-amplitude per-
snapshot fluctuations in σ₁.

**Shell-histogram cross-check.** Record the endpoint shell
histogram at each ξ point (same convention as ED-SC 3.3.7 /
3.3.8a) to verify that r_diag = 1 is held throughout — a silent
Class-2 excursion would bias σ₁ without a visible signal in the
target quantity itself.

---

## 4. Protocol

Per ξ point (9 total):

1. **Calibrate** IC amplitude `w` via the ED-SC 3.3.8a pre-pass
   interpolant (re-run the 9-point w sweep on seed 77 if no
   prior interpolant is cached; expected wall time ~6 s).
2. **Evolve** seed 77 with `rng.uniform(0.5 − w, 0.5 + w)` for
   `fr.STEPS = 500` timesteps under canonical parameters.
3. **Extract 40 snapshots** at burn-in 100, snap every 10.
4. **Measure** `ξ_measured = mean(xi_halfdecay(snapshot_k))` and
   apply the one-bisection-refinement rule if miss > 1 %.
5. **Compute** `L_ray = 1.08 · ξ_measured`.
6. **Guard:** hard-fail if `L_ray` intersects Window A or B;
   flag out-of-scope if `r_diag_measured ≠ 1` (expected to be
   True throughout the canonical grid; defensive).
7. **Collect motifs** at each snapshot under `(α_filt = 0.25,
   N_req = 4, L_ray)`; for each admitted motif record
   `T_motif = λ_neg + λ_pos` and the endpoint shell radii.
   Pool `T_motif` values across the 40 snapshots.
8. **Compute:**
   - `N_pool` — total admitted motif count across 40 snapshots.
   - `σ₁_std` — standard deviation of the pooled `T_motif`
     distribution.
   - `σ₁_IQR_proxy` — `IQR(T_motif) / 1.349` (Gaussian
     equivalent).
   - `median(T_motif)` — sanity check for the Trace-Gaussian-
     class rigid-zero prediction.
   - Bootstrap 16–84 band on `σ₁_std` (4000 resamples).
   - Per-snapshot `N_snap[k]`, `std(T_motif)_snap[k]` (if
     N_snap ≥ 4).
   - Endpoint shell histogram (r_diag cross-check).

After all 9 points:

- **OLS fit** `σ₁(ξ) = a + b·ξ` on the central σ₁_std values.
  Report slope `b`, intercept `a`, RMS residual, R².
- **ξ-dependence interpretation** in the summary JSON, analogous
  to ED-SC 3.4 §6 for S2: near-flat vs monotone trend.
- **Rigid-zero check:** pool-level `median(T_motif)` across all
  9 points should be statistically consistent with zero (a
  positive finding for the tenth-pass-arc Trace-Gaussian-class
  rigid identity).

---

## 5. Outputs and deliverables

**Per scan point**, emitted into `outputs/ed_sc_3_4_sigma1/`:

Per-point rows in `sigma1_calibration_table.csv`:

    xi_target, xi_measured, miss_frac, w_used, refined,
    L_ray, r_diag, out_of_scope,
    N_pool,
    median_T, median_T_CI_lo, median_T_CI_hi,
    sigma1_std, sigma1_std_CI_lo, sigma1_std_CI_hi,
    sigma1_IQR_proxy,
    N_per_snap_mean,
    shell_dominant, shell_entropy_bits

**Master aggregate** `sigma1_calibration_summary.json`:

- `method` string citing the simulator of record.
- Canonical parameters, canonical seed, canonical filter
  geometry, snapshot schedule.
- `xi_targets`, `xi_ref_index` (4, for ξ = 1.80).
- `resonance_windows_excluded`.
- `calibration_prepass` (w grid + measured ξ + interpolant audit
  trail).
- `scan_points[]` — full per-point payload (all columns above
  plus per-snapshot arrays).
- `derived_summary`:
  - `sigma1_vs_xi_fit` — OLS `{slope, intercept, RMS_residual,
    R_squared, residuals[]}`.
  - `sigma1_flat_check` — total variation fraction vs |σ₁_mean|;
    boolean `near_flat_prior_020` under the ED-SC 3.0 rev. 3
    size-corrected 20 % envelope.
  - `sigma1_trend_direction` — sign of the OLS slope.
  - `rigid_zero_check` — pool-level median(T_motif) across all
    points + whether consistent with 0 at 16–84 band.
  - `n_in_scope_points`, `n_out_of_scope_points`.
  - `r_diag_excursions[]` (should be empty).

**Downstream deliverables** for GR-SC consumption (analogous to
the GR-SC 1.2 three-component bands):

- **Central σ₁(ξ_canonical)** at canonical `ξ = 1.7575 lu` via
  interpolation on the fit.
- **Calibration CI** — bootstrap 16–84 at nearest grid point or
  RMS residual 0.xxx between points.
- **Ensemble CI** — per-point bootstrap CI at nearest grid
  point.
- **Per-realisation ±25 % band** — inherited from ED-SC 3.3.9
  pending empirical characterisation in a follow-up that
  multi-seeds σ₁ (out of scope for this memo).

---

## 6. ξ-positioning guidance for downstream GR-SC

Once executed, σ₁(ξ) enters GR-SC predictions via the same
three-tier guidance as GR-SC 1.2 for S2:

- **Ensemble predictions** — use the calibration CI band.
- **Intermediate-ensemble predictions** — use the ensemble-pool
  CI band.
- **Single-realisation predictions** — use the ±25 %
  per-realisation band (pending empirical verification that
  ED-SC 3.3.9's S2-spread estimate transfers to σ₁).

The **Rayleigh-class κ** scales as `|N̂'|·σ₁/(2√2)` per GR-SC
1.5 (tenth-pass). At canonical ξ, the quantitative κ prediction
is therefore:

    κ_central(ξ_canonical) = |N̂'| · σ₁(ξ_canonical) / (2√2)
    κ_band_lower = |N̂'| · σ₁_lower / (2√2)
    κ_band_upper = |N̂'| · σ₁_upper / (2√2)

with `|N̂'|` a kinematic calibration constant from GR-SC 1.5 and
the σ₁ bands drawn from the three-tier structure above. This
populates the `κ` row of GR-SC 1.0 §5 and unlocks a new memo
GR-SC 1.3 analogous to 1.1 / 1.2.

**GR-SC 1.8 EIT-Extremal clearance.** The engineering
falsification-clearance target `σ₁ / κ_M^det < 0.036` (2σ) from
GR-SC 1.8 §6 becomes numerically evaluable at the canonical
operating point once σ₁(ξ_canonical) has a central value and a
band. The ratio `σ₁ / κ_M^det` can then be quoted per-ξ across
the scan, giving GR-SC 1.8 a clearance-vs-ξ curve.

---

## 7. Verdict taxonomy

No falsifier verdict — this is a calibration memo. **Diagnostic
checks** pre-registered per §4:

- `rigid_zero_check` passes iff pool-level `median(T_motif)` at
  every ξ point has 16–84 CI containing zero. **Positive
  confirmation** of the tenth-pass-arc Trace-Gaussian-class
  rigid identity at the ED-SC motif-filter level.
- `r_diag_excursions` should be empty list — all 9 points inside
  the r_diag = 1 window at their measured ξ values.
- `sigma1_IQR_proxy` vs `sigma1_std` discrepancy < 10 % at each
  point — empirical Gaussianity check on `T_motif`
  distribution. Large discrepancy flags non-Gaussian tails and
  requires a revised scaling rule before σ₁ feeds into κ.

Failure on any diagnostic check is recorded in the summary but
does not block downstream integration; the flag is surfaced to
the GR-SC 1.3 scoping memo to decide interpretation.

---

## 8. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.4-σ₁ as the
  σ₁ calibration inside the r_diag = 1 canonical window. Mirrors
  ED-SC 3.4 structure exactly (same 9-point ξ grid, fixed seed
  77, 40-snapshot cadence, IC-amplitude ξ-control) but measures
  the spread of the Hessian-trace distribution `T_motif =
  λ_neg + λ_pos` across admitted motifs instead of the IQR of
  the eigenvalue-ratio distribution. Emits central σ₁(ξ), OLS
  fit, three-component uncertainty bands for downstream GR-SC
  1.3 and 1.8 consumption, plus three diagnostic checks
  (Trace-Gaussian rigid-zero median, r_diag window, Gaussian
  shape via std vs IQR comparison). Driver (next turn):
  `analysis/scripts/ed_sc_3_4_sigma1_calibration.py`. No
  numerics.
