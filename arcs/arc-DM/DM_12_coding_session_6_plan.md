# DM.12 — Coding Session 6 Plan: `run_full_sample.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — thirteenth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 6 and followed without further design decisions.
**Predecessor:** DM.11 (Session 5 plan — `run_single_galaxy.py`).
**Target file:** `ed-lab/simulations/edsim/dm/run_full_sample.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py`
**Session goal:** End-to-end multi-galaxy orchestration. After this session, the SPARC sample can be processed and a real DM.5 verdict produced, subject to validation gates (Session 7 / DM.13).

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Note on session scope.** This is the largest single module in the DM arc — it folds together what DM.3 originally specified as three separate analysis scripts (`fit_activity_parameters.py`, `compute_residuals.py`, `btfr_analysis.py`) plus the parallelized run loop. The session budget is correspondingly larger: 5–6 hours of implementation plus 2 hours of testing. If the session must be split, the natural break is between the per-galaxy execution layer and the global-fit / RC-detection analysis layer.

**Prerequisite:** DM.7–DM.11 must be fully landed before starting Session 6. The orchestrator depends on the entire pipeline being functional.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("Multi-galaxy orchestration: SPARC ingestion, stratified sample selection, per-galaxy execution, global parameter fit, universality test, BTFR analysis, refutation-condition detection"), authorship, and references to DM.2 §1 (six-stage pipeline at sample level), DM.3 §1.1.7 and §1.2.1–§1.2.3 (public APIs), DM.4 §3–§5 (sample selection, fitting, BTFR), and DM.5-TEMPLATE (verdict architecture).

Imports:
- `numpy as np`, `pandas as pd`, `scipy.optimize.minimize`, `scipy.odr`, `scipy.stats.spearmanr`
- `from joblib import Parallel, delayed`
- `from dataclasses import dataclass, field`
- `from typing import Optional, Callable, Literal`
- `from pathlib import Path`
- From sibling modules: `from .run_single_galaxy import SparcGalaxy, SingleGalaxyResult, run_single_galaxy`

### 1.2 Unit conventions

**Inherited from DM.7–DM.11. Not renegotiated.**

All inner-pipeline computation in galactic-natural units (kpc, km/s, M☉, Gyr). SPARC tabulated values are already in compatible units (kpc, km/s, M☉/L☉) and are loaded directly without conversion. BTFR analysis uses log M_b/M☉ and log v_∞/(km/s) for slope/intercept fitting.

### 1.3 Dataclass — `SampleConfig`

**Definition.** Frozen dataclass holding the configuration of one full-sample run.

`@dataclass(frozen=True)`
- `sparc_table_1_path: Path` — path to SPARC structural-parameter CSV.
- `sparc_table_2_path: Path` — path to SPARC rotation-curve CSV.
- `quality_cut: int = 2` — drop galaxies with quality flag > 2.
- `inclination_min_deg: float = 30.0` — drop galaxies with i < 30°.
- `distance_uncertainty_max: float = 0.30` — drop galaxies with > 30% distance uncertainty.
- `D_T: float` — penalty-channel diffusivity.
- `lam: float` — relaxation rate.
- `tier: int = 3` — Tier-1, 2, or 3 self-consistency mode.
- `kappa_act_init: float` — initial guess for κ_act in the global fit.
- `alpha_init: float = 0.5` — initial guess for α.
- `optimizer_max_evals: int = 50` — Nelder-Mead evaluation cap.
- `optimizer_tol: float = 1e-4` — function tolerance.
- `n_jobs: int = -1` — joblib parallelism (-1 means all cores).
- `output_dir: Path` — directory for output artifacts.
- `seed: int = 42` — RNG seed for fold splits.

### 1.4 Dataclass — `SampleResult`

**Definition.** Frozen dataclass holding the output of one full-sample run.

`@dataclass(frozen=True)`
- `n_galaxies: int`
- `kappa_act_fit: float`
- `kappa_act_fit_uncertainty: float` — bootstrap or Hessian-based 1σ.
- `alpha_fit: float`
- `alpha_fit_uncertainty: float`
- `chi2_total: float`
- `chi2_red_distribution: np.ndarray` — per-galaxy χ²_red.
- `r_cv: float` — cross-validation ratio.
- `r_cv_per_fold: list[float]` — per-fold ratios.
- `kappa_act_per_galaxy: np.ndarray` — per-galaxy fitted κ_act with α held global.
- `kappa_act_universality_sigma_over_mean: float`
- `kappa_act_correlations: dict[str, tuple[float, float]]` — Spearman (ρ, p) for each of {log_M_b, T_type, log_SB, log_sSFR}.
- `btfr_slope: float`
- `btfr_slope_sigma: float`
- `btfr_scatter: float` — RMS scatter in log v_∞ at fixed log M_b.
- `btfr_offset: float` — predicted log v_∞ at log M_b = 10, minus empirical 2.15.
- `rc_1_fired: bool`
- `rc_2_fired: bool`
- `rc_3_fired: bool`
- `verdict: Literal["PASS", "PARTIAL_universality", "PARTIAL_BTFR", "FAIL"]`
- `per_galaxy_results: list[SingleGalaxyResult]` — full results for downstream analysis.
- `failed_galaxies: list[str]` — IDs of galaxies that failed to converge or returned NaN.

### 1.5 Function — `load_sparc_catalog`

**Signature.**
`load_sparc_catalog(table1_path: Path, table2_path: Path) -> list[SparcGalaxy]`

**Behavior.** Reads the SPARC tables and returns a list of `SparcGalaxy` objects.

**Implementation.**
- Parse Table 1 (structural parameters) and Table 2 (rotation curves) using pandas.
- Group Table 2 rows by galaxy ID.
- For each galaxy, extract the structural parameters from Table 1 and the per-radius arrays from Table 2.
- Compute M_baryon = M_star + 1.4 · M_HI (helium correction); use Υ_3.6 = 0.5 if M_star is not directly tabulated.
- Construct one SparcGalaxy per galaxy.

**Validation.** If a galaxy is missing fields needed for SparcGalaxy construction, log a warning and skip. Return only successfully constructed galaxies.

**Note on data location.** SPARC files are assumed to live in `ed-lab/data/SPARC/` (canonical location). If they are not present, the function raises `FileNotFoundError` with a clear message pointing to the SPARC download URL (http://astroweb.cwru.edu/SPARC/).

**TODO comment.** The full SPARC ingestion utility (with edge-case handling for galaxies with mass-decomposition issues, distance method weighting, etc.) is deferred to a dedicated `sparc_io.py` module. For Session 6, this in-module loader is sufficient.

### 1.6 Function — `apply_quality_cuts`

**Signature.**
`apply_quality_cuts(galaxies: list[SparcGalaxy], config: SampleConfig) -> list[SparcGalaxy]`

**Behavior.** Filters the catalog per DM.4 §5.1.

**Cuts applied (in order):**
1. Quality flag ≤ `config.quality_cut`.
2. Inclination ≥ `config.inclination_min_deg`.
3. Distance uncertainty ≤ `config.distance_uncertainty_max` (requires distance method metadata in SparcGalaxy; if not available, skip this cut with a warning).
4. R_obs has at least 5 measured radii (avoid single-point fits).
5. v_obs > 0 at all measured radii (avoid pathological data).

**Returns.** Filtered list. Logs the count dropped at each step for diagnostic purposes.

### 1.7 Function — `select_stratified_subset`

**Signature.**
`select_stratified_subset(galaxies: list[SparcGalaxy], n_per_bin: int = 6, n_bins: int = 5, seed: int = 42) -> list[SparcGalaxy]`

**Behavior.** Constructs the 30-galaxy stratified subset for the global fit per DM.4 §4.1.

**Stratification.**
- 5 mass bins by log M_b: [7.0, 8.0], [8.0, 9.0], [9.0, 10.0], [10.0, 10.5], [10.5, 11.0].
- Within each bin, sort by quality flag (prefer Q = 1) and sample size (prefer galaxies with more SPARC data points).
- Pick `n_per_bin` galaxies per bin; if a bin has fewer than n_per_bin galaxies meeting criteria, take all and log a warning.
- Use `seed` for reproducible random selection within ties.

**Returns.** List of up to `n_per_bin × n_bins` = 30 galaxies. May be smaller if some bins are sparsely populated.

### 1.8 Function — `run_galaxy_with_kwargs`

**Signature.**
`run_galaxy_with_kwargs(galaxy: SparcGalaxy, kappa_act: float, alpha: float, D_T: float, lam: float, tier: int) -> SingleGalaxyResult`

**Behavior.** Thin wrapper around `run_single_galaxy` for use with `joblib.Parallel`. Catches all exceptions and returns a sentinel "failed" `SingleGalaxyResult` with NaN values and the galaxy ID, so a single bad galaxy doesn't crash the parallel run.

**Returns.** A SingleGalaxyResult, possibly a failed-sentinel.

### 1.9 Function — `run_sample`

**Signature.**
`run_sample(galaxies: list[SparcGalaxy], kappa_act: float, alpha: float, D_T: float, lam: float, tier: int = 3, n_jobs: int = -1) -> list[SingleGalaxyResult]`

**Behavior.** Runs `run_galaxy_with_kwargs` across the sample using `joblib.Parallel`.

**Implementation.**
- For `n_jobs == 1`: serial loop (useful for debugging).
- For `n_jobs == -1` or > 1: `Parallel(n_jobs=n_jobs)(delayed(run_galaxy_with_kwargs)(g, ...) for g in galaxies)`.

**Returns.** List of results in the same order as the input galaxies.

### 1.10 Function — `compute_total_chi2`

**Signature.**
`compute_total_chi2(results: list[SingleGalaxyResult]) -> float`

**Behavior.** Returns sum of per-galaxy χ² (not reduced) across the sample. NaN-skipping: failed galaxies contribute zero.

### 1.11 Function — `global_fit`

**Signature.**
`global_fit(galaxies: list[SparcGalaxy], config: SampleConfig) -> dict`

**Behavior.** Performs the Nelder-Mead optimization over (log κ_act, α) per DM.4 §4.2.

**Objective function.** Closure:
- Takes (log_kappa_act, alpha) as input.
- Calls `run_sample(galaxies, exp(log_kappa_act), alpha, D_T, lam, tier, n_jobs)`.
- Returns `compute_total_chi2(results)`.

**Optimizer call.**
- `scipy.optimize.minimize(method='Nelder-Mead', x0=[log(kappa_act_init), alpha_init], options={'fatol': optimizer_tol, 'maxiter': optimizer_max_evals})`.
- Bounds enforced via penalty: if α ∉ [0, 1], return χ² = 1e10.

**Returns.** Dict with:
- `kappa_act_fit`: exp(log_kappa_act at minimum).
- `alpha_fit`: α at minimum.
- `chi2_total_at_min`: final χ².
- `n_evaluations`: number of objective-function calls.
- `convergence_message`: optimizer.message.

**Cost note.** Each evaluation runs `run_sample` (the entire 30-galaxy fit). With Tier-3 ~3 min per galaxy and 8-core parallelism, one evaluation takes ~12 minutes. 30 evaluations take ~6 hours. This is the longest single computation in the entire DM arc.

**Mitigation.** During development and initial testing, use Tier-1 (single solve per galaxy, ~30 sec each) and a 5-galaxy subset. Promote to Tier-3 + 30-galaxy only after the optimizer is verified to converge correctly on the simpler problem.

### 1.12 Function — `cross_validate`

**Signature.**
`cross_validate(galaxies: list[SparcGalaxy], config: SampleConfig, n_folds: int = 5) -> dict`

**Behavior.** Performs k-fold cross-validation per DM.4 §4.3.

**Implementation.**
1. Stratify the sample into `n_folds` folds by log M_b.
2. For each fold k:
   - Training set: 4 folds (80%).
   - Test set: 1 fold (20%).
   - Run `global_fit` on training set; get (κ_act, α).
   - Compute χ² on test set with no re-fitting (single `run_sample` call).
3. Return r_cv = mean(chi2_test) / mean(chi2_train), plus per-fold details.

**Cost.** 5 × global_fit ≈ 30 hours at Tier-3 + 30-galaxy. Mitigate by reducing the inner-fit subset and/or using Tier-1 for cross-validation only.

**Returns.** Dict with `r_cv`, `r_cv_per_fold`, fitted parameters per fold.

### 1.13 Function — `compute_kappa_per_galaxy`

**Signature.**
`compute_kappa_per_galaxy(galaxies: list[SparcGalaxy], alpha_global: float, D_T: float, lam: float, tier: int = 3) -> np.ndarray`

**Behavior.** For each galaxy, refit κ_act with α held at `alpha_global`. Returns an array of per-galaxy κ_act values per DM.4 §4.4.

**Per-galaxy fit.** 1-D Nelder-Mead in log κ_act on the single-galaxy χ². Initial guess at the global κ_act_fit.

### 1.14 Function — `test_universality`

**Signature.**
`test_universality(kappa_per_galaxy: np.ndarray, galaxy_properties: dict[str, np.ndarray]) -> dict`

**Behavior.** Applies the universality test per DM.4 §4.4.

**Inputs.** Array of per-galaxy κ_act values; dict mapping property names to arrays (`log_M_b`, `T_type`, `log_SB_disk`, `log_sSFR`).

**Computes:**
- σ(log κ_act) / mean(log κ_act).
- Spearman ρ and p-value for κ_act vs. each property.

**RC #2 verdict.** Fires if σ/mean > 0.13 OR any |ρ| > 0.3.

**Returns.** Dict with `sigma_over_mean`, `correlations` (dict of property → (ρ, p)), `rc_2_fired` (bool).

### 1.15 Function — `compute_btfr`

**Signature.**
`compute_btfr(galaxies: list[SparcGalaxy], results: list[SingleGalaxyResult]) -> dict`

**Behavior.** Computes BTFR per DM.4 §5.

**Steps:**
1. For each galaxy with non-failed result: v_∞ = median(v_pred over outer half of R_obs).
2. M_b = galaxy.M_baryon.
3. Compute log v_∞ and log M_b for the sample.
4. Linear regression with errors-in-both-variables (`scipy.odr`):
   - σ(log v_∞) propagated from σ_v residuals.
   - σ(log M_b) ≈ 2 σ(log D) / ln 10 (distance-uncertainty-dominated).
5. Compute slope, slope σ, intercept, scatter (RMS in log v_∞ at fixed M_b).
6. Compute Δ_offset = predicted log v_∞ at log M_b = 10, minus empirical 2.15.
7. RC #3: fires if slope ∉ [3.5, 4.5] at > 3σ.

**Returns.** Dict with `slope`, `slope_sigma`, `intercept`, `scatter`, `offset`, `rc_3_fired`.

### 1.16 Function — `detect_rc1`

**Signature.**
`detect_rc1(results: list[SingleGalaxyResult], radial_bins: list[tuple[float, float]] = None) -> dict`

**Behavior.** Detects systematic-shape failure per DM.4 §6.6.

**Steps:**
1. Default radial bins: 5 logarithmic bins from 1 kpc to 30 kpc.
2. For each bin, collect Δv values across all galaxies whose R_obs intersects the bin.
3. Compute median |⟨Δv⟩| in each bin.
4. RC #1 condition: median |⟨Δv⟩| > 20 km/s in any bin within any stratification, across > 30% of the sample. (For Session 6, do an unstratified version first; stratification by mass/morphology is a downstream analysis.)
5. Hartigan dip test on the χ²_red distribution; multimodal if p < 0.01.

**Returns.** Dict with `median_dv_per_bin`, `rc_1_fired_radial`, `chi2_red_dip_pvalue`, `rc_1_fired_multimodal`, `rc_1_fired` (OR of the two).

### 1.17 Function — `assign_verdict`

**Signature.**
`assign_verdict(rc_1_fired: bool, rc_2_fired: bool, rc_3_fired: bool) -> str`

**Behavior.** Implements the verdict-assignment rule from DM.5-TEMPLATE §6.2.

**Rules (mechanical):**
- If `rc_1_fired`: return "FAIL".
- Elif `rc_2_fired and rc_3_fired`: return "FAIL" (joint failure of universality and BTFR).
- Elif `rc_2_fired`: return "PARTIAL_universality".
- Elif `rc_3_fired`: return "PARTIAL_BTFR".
- Else: return "PASS".

### 1.18 Function — `run_full_dm_analysis`

**Signature.**
`run_full_dm_analysis(config: SampleConfig) -> SampleResult`

**Behavior.** The top-level orchestrator. Calls each function above in sequence:
1. Load SPARC catalog.
2. Apply quality cuts.
3. Select stratified subset (or use full sample, depending on context).
4. Global fit → (κ_act, α).
5. Run sample at the global fit.
6. Compute per-galaxy κ_act with α held global.
7. Test universality → RC #2.
8. BTFR analysis → RC #3.
9. Detect RC #1.
10. Assign verdict.
11. Build and return SampleResult.

**Returns.** SampleResult.

**Output side effects.** Writes all artifacts to `config.output_dir` per DM.5-TEMPLATE §8.1: `dm2_global_fit_results.json`, `dm2_per_galaxy.csv`, `dm2_residuals.csv`, `dm2_btfr.json`, `dm2_T_fields.h5`, `dm2_run_log.json`.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py`. Use `pytest`, plain assertions, `pytest.approx`. All tests use synthetic data unless noted.

Six tests, each isolating one structural property.

### 2.1 Test 1 — Stratified sample selection

**Purpose.** Verify `select_stratified_subset` produces the right counts per mass bin.

**Inputs.** A synthetic catalog of 200 SparcGalaxy instances with M_baryon distributed uniformly in log space [10⁷, 10¹¹] M☉.

**Expected.**
- Output length = 30 (5 bins × 6 galaxies).
- Each bin contains 6 galaxies.
- Bin assignments are correct (no galaxies misplaced).

**Tolerance.** Exact for all counts and bin assignments.

### 2.2 Test 2 — Global-fit convergence on synthetic data

**Purpose.** Verify `global_fit` finds a known optimum on synthetic data.

**Inputs.**
- Construct 5 synthetic galaxies whose v_obs has been generated from a forward simulation with known (κ_act_true = 1.0, α_true = 0.5).
- Initial guess: (κ_act_init = 0.5, α_init = 0.3) — off from the true value by factor of 2.
- Use Tier-1 (no self-consistency) for speed.
- Optimizer max_evals = 30.

**Expected.** Optimizer recovers (κ_act, α) within 10% of the true values.

**Tolerance.** |κ_act_fit − 1.0| / 1.0 < 0.1; |α_fit − 0.5| < 0.05.

**Implementation note.** This test runs the actual SOR solver and Nelder-Mead optimizer, so it's an integration test. Expected runtime: 5–15 minutes. Mark with `@pytest.mark.slow` so it can be skipped during routine development testing.

### 2.3 Test 3 — Universality detection

**Purpose.** Verify `test_universality` fires RC #2 when κ_act varies systematically.

**Inputs.**
- Synthetic per-galaxy κ_act array of length 30 with σ/mean = 0.5 (well above the 0.13 threshold).
- Synthetic galaxy properties (log M_b spanning [7, 11]).
- Inject a correlation: κ_act = 0.5 + 0.1 · log_M_b.

**Expected.**
- σ/mean > 0.13 → RC #2 fires.
- Spearman ρ between κ_act and log_M_b > 0.3.
- Verdict: `rc_2_fired = True`.

**Tolerance.** Logical correctness; specific σ/mean and ρ values are not asserted to high precision.

**Additional case.** Run with synthetic κ_act = constant (no variation, no correlation). Verify RC #2 does not fire.

### 2.4 Test 4 — BTFR extraction

**Purpose.** Verify `compute_btfr` recovers a known slope.

**Inputs.**
- Synthetic results with v_∞ values constructed to satisfy log v_∞ = 0.25 · log M_b + 0.0 (slope 4 in v_∞⁴ vs. M_b, since v_∞ ∝ M_b^0.25).
- 20 galaxies spanning M_b ∈ [10⁸, 10¹¹] M☉.
- σ_v injected as small random noise.

**Expected.** Fitted slope = 4.0 ± 0.2; verdict `rc_3_fired = False`.

**Tolerance.** |slope - 4.0| < 0.3.

**Additional case.** Inject slope = 3.0 (outside [3.5, 4.5]); verify `rc_3_fired = True`.

### 2.5 Test 5 — RC detection logic (verdict assignment)

**Purpose.** Verify `assign_verdict` correctly maps (rc_1, rc_2, rc_3) to verdict strings.

**Inputs.** Each of the 8 combinations of (rc_1_fired, rc_2_fired, rc_3_fired).

**Expected:**

| rc_1 | rc_2 | rc_3 | verdict |
|---|---|---|---|
| F | F | F | PASS |
| F | T | F | PARTIAL_universality |
| F | F | T | PARTIAL_BTFR |
| F | T | T | FAIL |
| T | F | F | FAIL |
| T | T | F | FAIL |
| T | F | T | FAIL |
| T | T | T | FAIL |

**Tolerance.** Exact string match.

### 2.6 Test 6 — Parallel vs. serial execution gives same result

**Purpose.** Verify `run_sample` produces identical results in parallel and serial modes.

**Inputs.** 5 synthetic galaxies (small enough that parallel overhead doesn't dominate).

**Expected.** For each galaxy, the SingleGalaxyResult from `run_sample(n_jobs=1)` and `run_sample(n_jobs=-1)` should be bit-identical (same v_pred, same χ², etc.).

**Tolerance.** `numpy.testing.assert_allclose(rtol=1e-12, atol=1e-12)` on all numerical fields.

**Caveat.** If joblib is not installed in the test environment, mark the test with `@pytest.mark.skipif`.

---

## 3. Two-hour implementation plan

This session has the largest scope of any in the DM arc. The two-hour block covers the orchestrator skeleton; the analysis layer (fit, universality, BTFR, RC detection) extends into hours 2–4.

### 3.1 Hour 0:00 — 0:10 — Setup

- Verify DM.7–DM.11 are landed: `pytest ed-lab/simulations/edsim/dm/tests/` passes cleanly.
- Create empty file `ed-lab/simulations/edsim/dm/run_full_sample.py`.
- Add module docstring and imports per §1.1.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:10 — 0:30 — Dataclasses

- Define `SampleConfig` per §1.3 with validation.
- Define `SampleResult` per §1.4.
- Smoke test: construct each with synthetic data.

**Checkpoint.** Dataclasses instantiate.

### 3.3 Hour 0:30 — 0:55 — SPARC ingestion and quality cuts

- Implement `load_sparc_catalog` per §1.5 (in-module loader; full sparc_io.py is a TODO).
- Implement `apply_quality_cuts` per §1.6.
- Implement `select_stratified_subset` per §1.7.
- Smoke test on a synthetic mock catalog.

**Checkpoint.** A 200-galaxy synthetic catalog reduces to a 30-galaxy stratified subset correctly.

### 3.4 Hour 0:55 — 1:25 — Per-galaxy run wrappers

- Implement `run_galaxy_with_kwargs` per §1.8 with exception handling.
- Implement `run_sample` per §1.9 using `joblib.Parallel`.
- Implement `compute_total_chi2` per §1.10.
- Smoke test: run 3 synthetic galaxies in parallel; verify shapes.

**Checkpoint.** Parallel run works, exception handling catches failures.

### 3.5 Hour 1:25 — 1:50 — Global fit core

- Implement `global_fit` per §1.11.
- Smoke test on the 5-synthetic-galaxy setup from Test 2 (do not run full optimization yet — just verify the closure structure works and one objective-function call succeeds).

**Checkpoint.** Optimizer can be invoked; one objective evaluation completes.

### 3.6 Hour 1:50 — 2:00 — Buffer

End of two-hour implementation block. The remaining functions (cross_validate, kappa_per_galaxy, universality, BTFR, RC1, verdict, top-level analysis) extend into hours 2–4.

---

## 4. Hours 2–4 — Analysis layer + tests + debug

### 4.1 Hour 2:00 — 2:45 — Analysis-layer functions

- Implement `cross_validate` per §1.12.
- Implement `compute_kappa_per_galaxy` per §1.13.
- Implement `test_universality` per §1.14.
- Implement `compute_btfr` per §1.15 (uses `scipy.odr`).
- Implement `detect_rc1` per §1.16.
- Implement `assign_verdict` per §1.17.

### 4.2 Hour 2:45 — 3:00 — Top-level orchestrator

- Implement `run_full_dm_analysis` per §1.18 (chain together everything).
- Smoke test: run on a synthetic 10-galaxy mini-sample with Tier-1.

### 4.3 Hour 3:00 — 3:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py`.
- Write the six tests per §2.1–§2.6.
- Mark Test 2 (global-fit convergence) with `@pytest.mark.slow` so it can be excluded from default test runs.

### 4.4 Hour 3:30 — 4:30 — Run and debug

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py -v -m "not slow"`.
- Run the slow tests separately: `pytest ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py -v -m slow`.
- Likely failures and resolutions:
  - **Test 2 (global fit) doesn't converge.** Diagnosis: optimizer initial guess too far from optimum. Mitigation: tighten initial guess; or relax tolerance.
  - **Test 6 (parallel vs serial) gives different results.** Diagnosis: joblib-induced numerical non-determinism (rare). Mitigation: set joblib backend to 'loky' explicitly; use single-thread BLAS during the test.
  - **`scipy.odr` failure on near-degenerate input (Test 4).** Diagnosis: degeneracy in synthetic data. Mitigation: add small random noise.

### 4.5 Hour 4:30 — 5:00 — Documentation, lint, commit

- Verify all functions and dataclasses have complete docstrings.
- Run lint if configured.
- Update run log.
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/run_full_sample.py
  git add ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add run_full_sample.py and tests — DM Step 6 complete"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/simulations/edsim/dm/run_full_sample.py` exists with two dataclasses and ~13 functions per §1.3–§1.18.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_run_full_sample.py` exists with six tests.
- [ ] All non-slow tests pass under `pytest -m "not slow"`.
- [ ] At least Test 2 (slow) has been run at least once, even if just to manually confirm it converges.
- [ ] All DM.7–DM.11 tests still pass.
- [ ] All public dataclasses and functions have complete docstrings.
- [ ] The module imports cleanly.
- [ ] No TODO comments remain except those explicitly deferred (sparc_io.py for full SPARC parsing edge cases; HDF5 output formatting if not yet implemented).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to run log.
- [ ] Commit landed.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not advance to Session 7 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 6:

- **Real SPARC ingestion edge-case handling.** The in-module loader covers the standard case. A robust `sparc_io.py` with handling of unusual mass decompositions, missing distances, etc., is a separate utility.
- **HDF5 output for T-fields.** Defer to a follow-up if not natively supported by `h5py`. CSV/JSON outputs are sufficient for Session 6's deliverable.
- **The reproducibility notebook `05_dm2_sparc_fits.ipynb`.** Session 7 task.
- **The validation-tests.py module (Step 7 in DM.4 ordering, deferred to Session 7).**
- **Performance optimization** of the global fit beyond using parallelism. The 6-hour Tier-3 fit is acceptable for Session 6; multigrid migration of the inner solver is a follow-up only if needed.
- **Stratified-residual analysis for RC #1.** The default `detect_rc1` is unstratified. Mass/morphology stratification is a downstream analysis (in compute_residuals.py if it is split out, or as a follow-up).
- **The DM.5 (real, not template) verdict memo writing.** That comes after the actual full-sample run completes, which requires a real compute session, not just code.

If during the session a tempting deviation surfaces, record it in a TODO and move on.

---

## 7. Risk inventory for Session 6

Four things most likely to consume more time than expected:

1. **Global-fit objective non-convergence (Test 2).** Nelder-Mead can stall if the objective is very noisy or the initial guess is poor. Mitigation: tighten initial guess using a coarse pre-search; relax max_evals if necessary; verify the objective is monotonic in a 1-D scan around the true optimum. Expected resolution: 30–60 minutes.

2. **Parallel-execution determinism (Test 6).** joblib + numpy + multi-threaded BLAS can produce small numerical non-determinism. Mitigation: set OMP_NUM_THREADS=1 for the test, or compare with looser tolerances. Expected resolution: 15–30 minutes.

3. **SPARC table format ambiguity.** SPARC tables are well-documented but column orderings and missing-value conventions can vary. Mitigation: load a single galaxy interactively first; verify the dataframe columns match expectations; document any deviations. Expected resolution: 30–60 minutes.

4. **Cross-validation cost.** A single CV run at Tier-3 + 30-galaxy is 30 hours. For Session 6 testing, use Tier-1 + 5-galaxy. Document explicitly that the production cross-validation requires a separate compute session. Expected resolution: 10 minutes (just a documentation note, but reminder to not actually run the production CV during Session 6).

If the session runs over budget, do not skip writing tests or commit. The completion checklist is the gate.

---

## 8. Cross-checks against earlier memos

The implementation must respect six structural constraints from earlier memos:

1. **Universal (κ_act, α) hard rule** (DM.4 §2). The global fit uses one (κ_act, α) for the entire sample; per-galaxy variation only enters the universality test.

2. **Stratified subset of 30 galaxies** (DM.4 §4.1). Five mass bins × six galaxies per bin.

3. **Nelder-Mead with bounds** (DM.4 §4.2). Initial (log κ_act, 0.5); function tolerance 1e-4; max 50 evaluations.

4. **5-fold cross-validation stratified by log M_b** (DM.4 §4.3). R_cv ∈ [0.9, 1.5] for universality consistency.

5. **BTFR slope test against [3.5, 4.5]** (DM.4 §5). RC #3 fires outside this range at >3σ.

6. **Verdict assignment rule** (DM.5-TEMPLATE §6.2). Mechanically applied per §1.17.

---

## End-of-turn summary

**What got done this turn:** the Session 6 coding plan is fully scoped. Two dataclasses (`SampleConfig`, `SampleResult`) and ~13 functions covering SPARC ingestion, quality cuts, stratified selection, parallel execution, global fitting, cross-validation, per-galaxy κ_act extraction, universality testing, BTFR analysis, RC #1 detection, verdict assignment, and top-level orchestration. Six tests (one slow) cover the analysis layer end-to-end.

**What did not get done:** no Python code has been written. The DM.12 memo is a session plan, not the session itself.

**What this means for the program:** after Session 6, the entire DM pipeline is implemented. Six of eight modules are complete (DM.7–DM.12). The remaining work is the validation-tests integration suite (Session 7 / DM.13), the reproducibility notebook (Session 7 or 8), and then actual execution against real SPARC data — which is a compute session, not a coding session.

**Decision after this session:** Session 7 (DM.13) implements the validation-tests integration suite — analytic test cases (point source → Yukawa, uniform → flat T, isothermal → flat curve) expressed as integration tests through the full `run_single_galaxy` pipeline, gating real SPARC runs.

---

## Recommended Next Step

After confirming DM.7, DM.8, DM.9, DM.10, and DM.11 are all fully landed (their §5 checklists satisfied), begin DM.12 Session 6: in `ed-lab/simulations/edsim/dm/`, create `run_full_sample.py` and `tests/test_run_full_sample.py`, then implement the components in the order specified in DM.12 §3.2–§3.5 then §4.1–§4.2 (`SampleConfig` and `SampleResult` dataclasses → SPARC ingestion + quality cuts + stratified selection → parallel run wrappers + total-χ² → global-fit core → analysis-layer functions → top-level orchestrator), following the unit conventions in §1.2 and the verdict architecture in §1.17. Stop and run the test suite per §4.4 only after all components are implemented; do not attempt Session 7 until the §5 session-complete checklist is fully satisfied.