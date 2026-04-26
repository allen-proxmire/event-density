# DM.4 — Execution Protocol for the SPARC Confrontation

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — fifth memo
**Status:** Execution protocol committed. This memo specifies the build sequence, validation protocol, proof-of-concept run, 30-galaxy fit, BTFR extraction, and full-sample run. It does **not** report results — those are DM.5.
**Predecessor:** DM.3 (implementation plan).
**Successor:** DM.5 (full-sample execution + verdict).
**Target:** `ed-lab/simulations/edsim/dm/`, `ed-lab/analysis/scripts/dm2_sparc/`, `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`.

---

## 1. Implementation order

Eight modules built in dependency order. Each step has explicit "ready to proceed" criteria. Skipping a step or merging steps voids the gate guarantees.

### Step 1 — `disk_geometry.py`

**Implement.** `baryonic_velocity(R, v_gas, v_disk, v_bulge)` — quadrature sum of SPARC component velocities. `baryonic_potential_grid(R_grid, z_grid, R_sparc, v_bar_sparc)` — in-plane potential by integration of v²_bar / R, off-plane by analytic exponential-disk Bessel form parametrized by R_d.

**Test.** Unit tests on a synthetic exponential disk with known (M_d, R_d). Verify v_bar(R) reproduces the analytic exponential-disk curve to 0.1% at five reference radii. Verify Φ_bar matches the closed-form disk potential at z = 0.

**Ready to proceed.** Both unit tests pass.

### Step 2 — `activity_source.py`

**Implement.** `shear_squared(R, v)`, `vorticity_squared(R, v)`, `activity_index(R, v, alpha)`, `activity_source_3d(R_grid, z_grid, A_R, kappa_act, h_disk)`.

**Test.** On a constant-velocity input v(R) = 200 km/s, verify shear_squared = 0 (within numerical-derivative noise) and vorticity_squared = (200 km/s / R)². On a synthetic v(R) = R/(R + R_d), verify dv/dR matches the analytic derivative within 1% at SPARC sampling density.

**Ready to proceed.** Tests pass; shear and vorticity behave as expected on synthetic curves.

### Step 3 — `pde_solver.py`

**Implement.** `ScreenedPoissonSolver` class with cylindrical-Laplacian stencil per DM.3 §2.2. SOR iteration with ω = 1.7. Convergence by max relative change < 10⁻⁶. Pole regularization at R = 0.

**Test.** Standalone test: source = δ-function at origin (regularized as a thin Gaussian). Solve. Compare to analytic Yukawa T(r) = exp(−r/L)/(4π D_T r). Pass if max relative error < 5% over r ∈ [10 kpc, 500 kpc]. (This is the validation Test 1 below; the gate here is functional, not yet the production validation.)

**Ready to proceed.** Solver converges in < 5000 iterations on the validation grid; analytic comparison passes within 5%.

### Step 4 — `boundary_conditions.py`

**Implement.** `BoundaryConditions` dataclass with `inner_R`, `outer_R`, `inner_z`, `outer_z` modes. Outer-R Yukawa-far Dirichlet: `T(R_max, z) = M_S exp(−r/L) / (4π D_T r)` with M_S = ∫ S d³x and r = √(R_max² + z²). Inner-z Neumann via ghost-cell mirror.

**Test.** With BCs in place, re-run the point-source test. Verify the boundary at R_max is not a reflection source — the field at R_max−ΔR should match the analytic Yukawa to better than 0.5%.

**Ready to proceed.** Boundary tests pass; no spurious reflection visible in the field plot.

### Step 5 — `validation_tests.py`

**Implement.** `test_point_source`, `test_uniform_source`, `test_isothermal_source`, `run_all`. Each returns a dict with `pass`, `rel_err`, and arrays for diagnosis.

**Test.** This *is* the test layer. Run all three on the production grid (300 R × 30 z, R_max = 5 Mpc, h_disk = 0.3 kpc).

**Ready to proceed.** All three production-grid tests pass at the tolerances in §2 below. **This is the hard gate.** No SPARC galaxy is run until this gate clears.

### Step 6 — `run_single_galaxy.py`

**Implement.** `SingleGalaxyResult` dataclass; `run_single_galaxy()` orchestrates Stages 1–6 of the DM.2 pipeline. Tier-3 self-consistency loop with damping per DM.3 §2.6.

**Test.** Run on NGC 3198 with κ_act at the dimensional anchor (§3.2 below). Verify the loop converges (no oscillation, max 50 outer iterations). Check that output v_pred(R) is finite, positive, and monotonically reasonable across the SPARC R range.

**Ready to proceed.** NGC 3198 runs to completion, returns a valid result object, and passes the proof-of-concept criteria in §3.

### Step 7 — `fit_activity_parameters.py`

**Implement.** Global Nelder-Mead optimizer over (log κ_act, α). Cross-validation with 5-fold split stratified by log M_b. Per-galaxy κ_act distribution computation for the universality test.

**Test.** Run the optimizer on a 5-galaxy sub-stratification first to verify convergence behavior. Step up to the 30-galaxy fit (§4 below) when 5-galaxy convergence is clean.

**Ready to proceed.** 30-galaxy fit converges with R_cv ∈ [0.9, 1.5] (universality not yet certain at this stage but global fit is well-conditioned).

### Step 8 — `run_full_sample.py`

**Implement.** Parallelized full-sample loop using `joblib.Parallel`. Diagnostic logging per galaxy. Aggregate output to CSV/JSON/HDF5 per DM.3 §5.7.

**Test.** Smoke test on 10 galaxies serial, verify output formats. Then run full ~150 with `n_jobs = -1`.

**Ready to proceed.** Full sample completes within the runtime budget (§6); all output artifacts written; no per-galaxy convergence failures > 5% of sample.

---

## 2. Validation protocol — executable

The validation gate is hard. All three tests below must pass before any SPARC galaxy is run.

### Test 1 — Point source → Yukawa

**Setup.**
- Source: regularized δ at origin, S(R, z) = M_test · exp(−r²/2σ²) / ((2π)^(3/2) σ³), σ = 0.5 kpc, M_test = 10¹⁰ M☉ (numerical scale chosen to give a non-trivial T magnitude).
- Boundary: Dirichlet T = 0 at R_max, z_max.
- Solve.

**Expected.** T(r) = M_test exp(−r/L) / (4π D_T r) for r ≫ σ, where L = 1 Mpc.

**Tolerance.** max |T_computed − T_analytic| / |T_analytic| < 5% over r ∈ [10 kpc, 500 kpc].

**Pass.** Tolerance met.
**Fail.** Tolerance violated. Diagnose: solver not converged → tighten tolerance to 10⁻⁷; grid too coarse → refine R-resolution; wrong stencil → re-derive cylindrical Laplacian.

### Test 2 — Uniform source → zero curvature

**Setup.**
- Source: S(R, z) = S_0 = 10⁻³⁵ kg s⁻¹ m⁻³ (a small constant, units chosen for dimensional consistency with [S]).
- Boundary: Dirichlet T = S_0 / λ at R_max, z_max (the analytic uniform solution; this is a special-case BC).
- Solve.

**Expected.** T = S_0 / λ everywhere (zero ∇²T solution; sourceless except for the constant input).

**Tolerance.** max |∇T| / (S_0 / λ) per cell-width < 1%.

**Pass.** Tolerance met across the central 90% of the grid (boundary cells excluded).
**Fail.** Indicates either incorrect Laplacian discretization or BC mismatch. Diagnose Laplacian first.

### Test 3 — Isothermal 1/r² source → flat curve

**Setup.**
- Source: S(R, z) = S_0 / R² for R ∈ [1 kpc, 50 kpc] in the disk plane (z ∈ [−h_disk, h_disk]); zero outside.
- S_0 chosen to give v_T ≈ 150 km/s (typical galactic flat-curve value).
- Solve.

**Expected.** T(R) ≈ −(S_0 / D_T) · ln(R) + const for R ∈ [5 kpc, 30 kpc]. Compute v_T(R) = √(R · ∂Φ_T/∂R) under Reading B with γ such that γ · κ_act = D_T.

**Tolerance.** |dv_T/dR| < 2 km/s/kpc over R ∈ [5 kpc, 30 kpc] (i.e., the curve is flat to better than ~13% across the range).

**Pass.** Tolerance met.
**Fail.** This is the most diagnostic test. If Tests 1 and 2 pass but Test 3 fails, the Reading B mapping or the κ_act normalization is incorrect. Diagnose by computing T(R) and verifying logarithmic shape before Φ_T conversion.

### Validation gate

> **All three tests must pass on the production grid (300 R × 30 z, R_max = 5 Mpc, h_disk = 0.3 kpc) before any SPARC galaxy is run. The gate is enforced as the first cell of `05_dm2_sparc_fits.ipynb` and the first call in every script in `analysis/scripts/dm2_sparc/`. If any test fails, the pipeline raises and exits.**

---

## 3. NGC 3198 proof-of-concept

NGC 3198 is the canonical well-studied SPARC galaxy. SPARC properties: distance ≈ 13.8 Mpc, stellar mass ≈ 4 × 10¹⁰ M☉, gas mass ≈ 10¹⁰ M☉, total baryonic mass M_b ≈ 5 × 10¹⁰ M☉, R_d ≈ 3.0 kpc, v_flat ≈ 150 km/s, observed range R ∈ [0.7, 38] kpc, quality Q = 1.

### 3.1 Preprocessing

- Load NGC 3198 from SPARC tables 1 and 2.
- Construct v_bar(R) = √(v_gas² + v_disk² + v_bulge²) on the SPARC R-grid.
- Identify R_min = 0.7 kpc, R_max,sparc = 38 kpc.
- Build simulation grid: log-spaced in R from 0.01 kpc to 50 kpc (200 cells), linear from 50 kpc to 5 Mpc (100 cells); z from 0 to 1.5 kpc, 30 cells. Total 300 × 30 = 9000 cells.
- Set h_disk = 0.3 kpc (default).
- Build ρ_geom(R, z) = sech²(z/h_disk) / (2 h_disk).

### 3.2 Tier-3 settings

- Initial guess: v_pred = v_bar.
- Activity construction: A(R) = 0.5 · |dv_pred/dR|² + 0.5 · (v_pred/R)² (α = 0.5 default).
- κ_act initialization: dimensional anchor κ_act,0 = D_T / (R_d · v_flat²) ≈ 2.1 × 10²⁷ / (3 × 10¹⁹ · (1.5 × 10⁵)²) ≈ 3 × 10⁻³ in mks units (this is the order-of-magnitude scale; final value is fitted, not committed).
- Outer-loop convergence: max |v_pred,n+1 − v_pred,n| < 1 km/s across all SPARC radii.
- Outer-loop max: 50 iterations.
- Damping: enable if residual stops decreasing for 3 consecutive iterations.

### 3.3 Expected runtime

- Inner SOR solve: ~10–30 s per outer iteration on a single CPU core.
- Outer iterations to convergence: 5–15.
- **Per-galaxy total: 1–8 minutes.**

### 3.4 Expected qualitative shape

For NGC 3198 with κ_act,0 of the right order:

- Inner disk (R < R_d): rising rotation curve dominated by baryons.
- Transition (R d < R < 5 R_d): contribution of v_T begins to flatten the curve.
- Outer (R > 5 R_d): v_pred ≈ v_flat, with small residual curvature from the imperfect match between the assumed activity profile and the converged self-consistent solution.
- Asymptotic value: v_pred(R = 30 kpc) ≈ 130–170 km/s (factor-of-1.2 acceptable bracket around the observed 150 km/s, since κ_act is at dimensional anchor not fit).

### 3.5 Pass / fail

**Pass criteria.**
- **Shape:** |v_pred(R) − v_obs(R)| < 30 km/s for all R in [5 kpc, 25 kpc].
- **Convergence:** outer loop converges in < 50 iterations with no oscillatory divergence.
- **No solver pathology:** no NaNs, no negative T outside the active region, no unphysical features.

**Fail criteria.**
- Any of the above pass criteria violated.
- v_pred(R) shape qualitatively wrong (e.g., still falls Keplerian-like at large R, indicating Reading B is not being applied correctly, or T-to-Φ mapping has wrong sign).

**On failure: HALT and diagnose.** Do not scale up to 30-galaxy or full-sample runs until the proof of concept is clean. Diagnostic order:
1. Verify Test 3 (isothermal → flat) passed on the production grid.
2. Print T(R) profile for NGC 3198. Verify it shows the expected log-then-Yukawa shape.
3. Verify Reading B coupling sign and magnitude (γ · κ_act = D_T).
4. Verify the activity-source convolution with disk geometry is correct.

---

## 4. 30-galaxy global fit

### 4.1 Sample selection

Stratified across the SPARC mass range. Five mass bins, six galaxies per bin, prioritizing quality Q = 1 and well-determined distances:

| Mass bin (log M_b/M☉) | N | Selection priority |
|---|---|---|
| 7.0–8.0 | 6 | Dwarf irregulars (DDO, NGC dwarfs) |
| 8.0–9.0 | 6 | Late-type dwarfs |
| 9.0–10.0 | 6 | Late-type spirals (Sd, Sm) |
| 10.0–10.5 | 6 | LSB and intermediate spirals |
| 10.5–11.0 | 6 | High-mass spirals (Sa, Sb, Sc) |

Ensure morphological diversity within each bin (where possible) and exclude galaxies with Q > 1, distance method "indirect", or inclination < 30°.

### 4.2 Nelder-Mead initialization

- Initial guess: (log κ_act, α) = (log κ_act,0, 0.5), where κ_act,0 is the dimensional anchor from §3.2.
- Bounds: log κ_act ∈ [log κ_act,0 − 2, log κ_act,0 + 2] (factor-of-100 each side), α ∈ [0, 1].
- Objective: total χ² = Σ_g χ²_g across the 30-galaxy subset.
- Convergence: function tolerance 10⁻⁴, max evaluations 50.

### 4.3 Cross-validation

5-fold split stratified by log M_b (each fold has a representative sample across mass bins).

For each fold k:
- Fit (κ_act, α) on the training 80% (24 galaxies).
- Compute χ² on the held-out 20% (6 galaxies) with no re-fit.

Metric: R_cv = mean(χ²_test) / mean(χ²_train) across folds.

### 4.4 Universality test

After the global fit converges, re-fit κ_act per galaxy with α held at the global value (single-parameter fit). Output: κ_act,g for each of 30 galaxies.

**Universality criteria (must hold for RC #2 to clear):**
- σ(log κ_act,g) / mean(log κ_act,g) < 0.13 (≈ ±30% spread).
- Spearman |ρ| < 0.3 against each of {log M_b, T-type, log SB_disk, log sSFR}.

**Violation of either is RC #2.** The framework's parsimony claim — "form forced, value inherited (singular)" — fails if κ_act varies systematically across galaxies. This does *not* mean ED is refuted; it means the activity-source mechanism is incomplete and missing structure.

### 4.5 30-galaxy gate

Proceed to full-sample run only if:
- Global Nelder-Mead converges within 50 evaluations.
- R_cv ∈ [0.9, 1.5].
- No catastrophic per-galaxy fit failures (> 5 of 30 with χ²_red > 100).

If R_cv > 1.5 or per-galaxy failures > 5, the global fit is unstable. Do not run full sample; first diagnose what the 30-galaxy fit is telling us (likely κ_act variation or shape mismatch).

---

## 5. BTFR extraction

### 5.1 v_∞ extraction

For each galaxy with predicted v_pred(R) on the SPARC R-grid:

- **Definition.** v_∞,g = median(v_pred(R)) over R ∈ [R_outer/2, R_outer], where R_outer is the outermost SPARC radius for galaxy g.
- This matches the standard SPARC operational definition of v_flat.

**Why median.** Robust to noise and to mild non-flatness in v_pred at the outer edge.

### 5.2 M_b computation

For each galaxy, M_b = M_star + M_gas, where:

- M_star from SPARC L_3.6 with stellar mass-to-light Υ_3.6 = 0.5 (standard SPARC convention).
- M_gas = 1.4 · M_HI (helium correction; SPARC convention).
- Both extracted from SPARC table 1.

Distance uncertainty propagation: M_b ∝ D², so σ(log M_b) = 2 σ(log D) / ln 10. Use SPARC's tabulated distance methods to weight; prefer Cepheid/TRGB distances over flow-field.

### 5.3 Slope and scatter

Fit log v_∞,g vs. log M_b,g across all galaxies in the analysis sample (full sample after DM.5).

- Method: linear regression with errors-in-both-variables (orthogonal distance regression, `scipy.odr`), using σ(log v_∞) propagated from σ_v residuals and σ(log M_b) from distance.
- Report: slope ± 1σ, intercept, RMS scatter in log v_∞ at fixed M_b.

### 5.4 RC #3

> **Refutation condition #3:** fitted slope ∉ [3.5, 4.5] at > 3σ.

Empirical BTFR slope from McGaugh et al. is ≈ 4.0 ± 0.1. The acceptable bracket [3.5, 4.5] is generous to allow for the conditional nature of DM.1's BTFR derivation (which inherits the disk-scaling relation). A slope outside [3.5, 4.5] at > 3σ refutes the conditional argument.

A slope inside [3.5, 4.5] is RC #3 cleared. A slope inside [3.9, 4.1] would be a strong positive — quantitative agreement with empirical MOND/SPARC BTFR.

### 5.5 BTFR offset diagnostic

Per DM.3 §6 risk #4: a correct slope can mask an offset. Add an offset diagnostic.

- Predicted intercept at log M_b = 10: log v_∞,pred.
- Empirical intercept at log M_b = 10: log v_∞,emp ≈ 2.15 (i.e., v_∞ ≈ 140 km/s for M_b = 10¹⁰ M☉; from SPARC).
- Difference Δ_offset = log v_∞,pred − log v_∞,emp.

Report Δ_offset alongside slope. A correct slope with |Δ_offset| > 0.1 (factor of 1.25) is a warning, not a refutation, but it indicates κ_act is fit to a non-universal target.

---

## 6. Full-sample run protocol

### 6.1 Sample

After Q ≤ 2 cut, distance-uncertainty cut, inclination cut: ~150 galaxies.

### 6.2 Runtime

- Per galaxy at Tier 3: 3 minutes (mean estimate from §3.3 for typical galaxies; outliers may take up to 10 minutes).
- Full sample serial: ~7.5 hours.
- Full sample with 8 parallel cores: ~1 hour.

### 6.3 Logging

For each galaxy:
- Galaxy ID, M_b, T-type, R_d, distance.
- Solver iterations to convergence (inner and outer).
- Final χ², χ²_red, max residual.
- Wall-time.
- Any flags (convergence failure, NaN encountered, oscillation damping triggered).

Logs written to `dm2_run_log.json` with one record per galaxy. Catastrophic failures recorded but do not halt the run.

### 6.4 Output formats

Per DM.3 §5.7:
- `dm2_global_fit_results.json` — fitted parameters and CV statistics.
- `dm2_per_galaxy.csv` — one row per galaxy with all summary metrics.
- `dm2_residuals.csv` — per-radius residuals.
- `dm2_btfr.json` — BTFR slope, scatter, intercept, offset diagnostic, RC #3 verdict.
- `dm2_T_fields.h5` — full T(R, z) for each galaxy (compressed HDF5).
- `dm2_run_log.json` — execution diagnostics.
- `dm2_verdict.md` — narrative summary memo (becomes DM.5).

### 6.5 Diagnostic plots

Generated after the full-sample run completes:

1. **Per-galaxy v_pred vs. v_obs.** Grid of small panels, one per galaxy. ~150 panels in 12 × 13 layout.
2. **Aggregate residual histogram.** Distribution of Δv at each radial bin across the sample.
3. **χ²_red distribution.** Histogram across the sample.
4. **κ_act,g distribution.** Histogram + scatter against M_b, T-type, SB, sSFR (universality test).
5. **BTFR plot.** log v_∞ vs. log M_b across the sample, with fitted slope and scatter.
6. **Stratified residuals.** ⟨Δv(r)⟩ per radial bin, conditioned on each of mass / morphology / SB / activity.

### 6.6 RC #1 detection

After residual computation and stratification:

> **Refutation condition #1:** median |⟨Δv(r)⟩| > 20 km/s in any radial bin within any stratification, across more than 30% of the sample. Or the χ²_red distribution is multimodal at significant level (Hartigan dip test p < 0.01).

Trigger detection is automatic in `compute_residuals.py`. RC #1 firing implies the activity-source PDE has systematic shape failures even with universal parameters — a hard refutation.

### 6.7 Failure-mode triage

If the full sample returns one of the partial verdicts:

- **PARTIAL — universality failure (RC #2 fires alone):** examine which property κ_act correlates with. A clean correlation (e.g., κ_act ∝ sSFR^γ) is structurally informative — it suggests an additional physical ingredient (e.g., explicit SFR coupling to the activity coupling itself). DM.6 would target this.
- **PARTIAL — BTFR failure (RC #3 fires alone):** test whether the disk relation R_d ∝ √M_b holds for the SPARC subsample used. If it does, BTFR is genuinely missing — possibly because the activity-source mechanism doesn't deliver the right v_∞ scaling. DM.6 would re-examine the conditional derivation.
- **FAIL (RC #1 fires):** the activity-source PDE is structurally insufficient for galactic rotation curves. DM.6 returns to the V₁ + acoustic-metric channel.

---

## 7. Decision points and stop conditions

The DM.4 protocol has four decision points. At each, the next stage runs only if the previous gate clears.

| Stage | Gate | If clear | If fail |
|---|---|---|---|
| 1 — Implementation Steps 1–4 | Unit tests pass | Proceed to validation suite | Diagnose, fix, retest |
| 2 — Validation Tests 1–3 | All three pass at production tolerances | Proceed to NGC 3198 | **HALT.** Do not run any galaxy until validation is clean. |
| 3 — NGC 3198 proof-of-concept | Pass criteria in §3.5 | Proceed to 30-galaxy fit | **HALT.** Diagnose qualitative failure before scaling. |
| 4 — 30-galaxy fit | Convergence + R_cv ∈ [0.9, 1.5] | Proceed to full sample | Diagnose, possibly re-scope |

The discipline is: a failure at any gate is a finding, not a setback. Failure at validation means the solver has a bug. Failure at NGC 3198 means the physics is wrong (DM.1 may need revision). Failure at 30-galaxy fit means κ_act is non-universal (RC #2) and DM.5 should examine that finding directly rather than scaling up to 150 galaxies that will inherit the same failure.

---

## 8. What DM.4 produces

### 8.1 Code artifacts

- 8 Python modules in `ed-lab/simulations/edsim/dm/` (totaling ~1500 lines).
- 3 analysis scripts in `ed-lab/analysis/scripts/dm2_sparc/` (totaling ~400 lines).
- 1 reproducibility notebook `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`.
- A test suite under `ed-lab/simulations/edsim/dm/tests/`.

### 8.2 Validation evidence

Documented pass of all three analytic tests on the production grid. This evidence is committed to the repository alongside the code.

### 8.3 NGC 3198 result

A documented result for one canonical galaxy with:
- v_pred(R) plotted against v_obs(R).
- Tier 3 convergence trace.
- χ², χ²_red.
- T(R, z) field visualization.

This is the smallest empirical artifact that establishes the pipeline works end-to-end.

### 8.4 30-galaxy fit

Fitted (κ_act, α) with cross-validation statistics. Per-galaxy κ_act distribution. Universality verdict (clear / RC #2).

### 8.5 What DM.4 does not produce

- The full-sample verdict (DM.5).
- Resolution of the open structural questions (κ_act from primitives, Reading B vs. C).
- A simulation of cluster-scale physics (already done in the merger-lag paper).
- Non-axisymmetric corrections.

---

## Recommended Next Step

**DM.5 — full-sample execution and verdict memo.**

The protocol is committed. Implementation order is fixed. Validation gates are concrete. Proof-of-concept criteria are quantitative. The 30-galaxy intermediate gate gives an early universality signal. The full-sample run produces the four-way verdict (PASS / PARTIAL-univ / PARTIAL-BTFR / FAIL).

DM.5 is the verdict memo: the analyst runs the protocol exactly as specified in DM.4, captures the outputs, and writes a memo reporting which verdict was returned along with diagnostic detail. DM.5 is structurally simpler than DM.4 (no design decisions remain) but operationally larger (it includes the actual computational work).

The alternative branches the user named are not appropriate at this stage:

- **Parameter-sensitivity analysis** is folded into DM.5 (cross-validation, stratified residuals, κ_act dispersion). It does not stand alone.
- **Branching to V₁ + acoustic-metric channel** is the right move *only if* DM.5 returns FAIL after validation passes and NGC 3198 / 30-galaxy gates clear. Speculative branching before the test is premature.

DM.5 is the smallest executable unit that produces the verdict the arc has been driving toward. After DM.5, the framework either has its galactic-scale claim or it doesn't, and the next decision branches are determined by that outcome.

---

## End-of-turn summary

**What got done.** The execution protocol is fully specified. Build sequence has eight steps with explicit gates. Validation has three tests with quantitative tolerances (5%, 1%, 2 km/s/kpc). NGC 3198 proof-of-concept has runtime estimates and pass criteria (|Δv| < 30 km/s, no oscillation). 30-galaxy fit has stratified sample, Nelder-Mead initialization, cross-validation, and the universality test. BTFR extraction has v_∞ definition, M_b computation, slope+scatter, and RC #3 quantification. Full-sample run has runtime budget, logging, output formats, diagnostic plots, and RC #1 detection.

**What did not get done.** Implementation. No code has been written.

**What this means for the program.** The DM arc has advanced from "structural plausibility" (DM.1) through "design committed" (DM.2), "implementation specified" (DM.3), to "execution protocol committed" (DM.4). The next memo (DM.5) reports results.

**Operational ask.** ~3 days of implementation effort (matched against DM.3 estimate). ~50 hours single-CPU compute envelope (with parallelization, ~1 hour wall-time). Standard scientific Python stack only.

**Verdict architecture.** Full-sample run returns one of {PASS, PARTIAL-univ, PARTIAL-BTFR, FAIL}. DM.5 reports which and provides the diagnostic detail. DM.6 onward is determined by the verdict.

**Stop conditions.** Validation gate, proof-of-concept gate, 30-galaxy gate, full-sample gate. A failure at any gate halts forward progress and triggers diagnosis. A pass at all gates produces the framework's first quantitative empirical claim at galactic equilibrium scales.
