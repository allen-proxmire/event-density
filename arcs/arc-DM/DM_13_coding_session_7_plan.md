# DM.13 — Coding Session 7 Plan: `validation_tests.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — fourteenth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 7 and followed without further design decisions.
**Predecessor:** DM.12 (Session 6 plan — `run_full_sample.py`).
**Target file:** `ed-lab/simulations/edsim/dm/validation_tests.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_validation_tests.py`
**Session goal:** Implement the analytic-validation suite that gates SPARC runs per DM.4 §2. After this session, DM.4 Gate 2 is unblocked: the SPARC pipeline can run if and only if the production-grid validation suite passes.

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Prerequisite:** DM.7–DM.12 must be fully landed. The validation suite tests the full pipeline (`pde_solver` for Tests 1–2, plus `run_single_galaxy` for Test 3 and the integration test).

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("Analytic validation suite for the DM screened-Poisson solver and full pipeline. Three production-grid tests gate any SPARC run per DM.4 §2."), authorship, and references to DM.0 §3 (Yukawa Green's function), DM.1 §3.1 (isothermal flat-curve derivation), DM.4 §2 (validation gate specification), and DM.11 (full-pipeline integration).

Imports:
- `numpy as np`, `from typing import Optional`, `from dataclasses import dataclass`
- From sibling modules: `from .pde_solver import CylindricalGrid, ScreenedPoissonSolver, yukawa_green`
- `from .boundary_conditions import BoundaryConditions`
- `from .activity_source import activity_source_3d`
- `from .run_single_galaxy import SparcGalaxy, run_single_galaxy`

### 1.2 Unit conventions

**Inherited from DM.7–DM.12. Not renegotiated.**

All tests run on the production grid in galactic-natural units. The solver inputs (D_T, λ) at production values per DM.9 §1.2.

### 1.3 Tolerance constants

Defined as module-level constants for clarity and centralized adjustment:

- `TOL_POINT_SOURCE_REL = 0.005` — 0.5% relative error tolerance on Yukawa shape (Test 1; tighter than DM.4 §2.1's 5% to discriminate solver quality at production-grid resolution).
- `TOL_UNIFORM_SOURCE_REL = 0.01` — 1% gradient tolerance on uniform-source field (Test 2, matches DM.4 §2.2).
- `TOL_ISOTHERMAL_DV_DR = 2.0` — 2 km/s/kpc maximum |dv/dr| over [5, 30] kpc (Test 3, matches DM.4 §2.3).
- `R_RANGE_POINT_SOURCE = (10.0, 500.0)` — kpc range for Test 1 evaluation.
- `Z_TOL_BOUNDARY_CELLS = 2` — number of boundary cells excluded from Test 2's gradient check.

### 1.4 Dataclass — `ValidationResult`

**Definition.** Frozen dataclass per analytic test.

`@dataclass(frozen=True)`
- `test_name: str` — "point_source", "uniform_source", "isothermal_source", or "grid_refinement", "pipeline_integration".
- `passed: bool` — True if tolerance met.
- `metric_value: float` — the measured quantity (max relative error, max gradient, etc.).
- `tolerance: float` — the threshold compared against.
- `expected_array: np.ndarray` — the analytic reference values.
- `computed_array: np.ndarray` — the solver output.
- `details: dict` — free-form diagnostic info (iterations, wall-time, etc.).

### 1.5 Function — `make_production_grid`

**Signature.**
`make_production_grid(R_max_kpc: float = 5000.0, n_R_log: int = 200, n_R_lin: int = 100, n_z: int = 30, z_max_kpc: float = 1.5) -> CylindricalGrid`

**Behavior.** Constructs the production grid per DM.4 §5.1 (300 R × 30 z, log-linear hybrid).

**Note.** This duplicates `build_simulation_grid` from `run_single_galaxy.py` but is callable without a SparcGalaxy. Refactor target: extract a shared helper to `pde_solver.py` or a new `_grid_factory.py`. For Session 7, keep the duplication and add a TODO.

### 1.6 Function — `test_point_source`

**Signature.**
`test_point_source(grid: Optional[CylindricalGrid] = None, D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT, M_test: float = 1.0e10, sigma_kpc: float = 0.5) -> ValidationResult`

**Behavior.** Implements DM.4 §2.1 / DM.9 Test 2 at the validation-suite level.

**Setup.**
- Grid: production grid if not provided.
- Source: regularized δ at origin — Gaussian with σ = sigma_kpc and total mass M_test:
  S(R, z) = M_test · exp(−r² / (2 σ²)) / ((2π)^(3/2) σ³)
  with r = √(R² + z²).
- BoundaryConditions: defaults (Yukawa-far at outer R, Dirichlet zero at outer z, mirror at z=0, pole-regularized at inner R).
- Solve: `solver.solve(source, ..., tol=1e-7, max_iter=10000)`.

**Comparison.**
- L = √(D_T / λ) ≈ 1000 kpc.
- For each (R[i], z[j]) with r_ij = √(R[i]² + z[j]²) ∈ R_RANGE_POINT_SOURCE:
  T_analytic(r_ij) = M_test · exp(−r_ij / L) / (4π · D_T · r_ij).
- Compute max relative error: max |T_computed − T_analytic| / |T_analytic|.

**Pass criterion.** max_rel_err < TOL_POINT_SOURCE_REL (0.5%).

**Returns.** ValidationResult with metric_value = max_rel_err, expected_array = T_analytic on the grid, computed_array = T_computed.

**Diagnostic info.** iterations to convergence, wall-time, BC values at outer R column, max-error location (R, z).

### 1.7 Function — `test_uniform_source`

**Signature.**
`test_uniform_source(grid: Optional[CylindricalGrid] = None, D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT, S_uniform: float = 1.0e-35) -> ValidationResult`

**Behavior.** Implements DM.4 §2.2 / DM.9 §1.6 expectation.

**Setup.**
- Grid: production.
- Source: S(R, z) = S_uniform everywhere (constant array).
- BoundaryConditions: special-case for this test — outer-R and outer-z must use Dirichlet at the analytic uniform value T = S_uniform / λ. Override the default Yukawa-far / Dirichlet-zero with this value. (The default BCs would fight the uniform interior solution.)

**Comparison.**
- Expected: T(R, z) = S_uniform / λ everywhere.
- Compute T_uniform = S_uniform / λ.
- For each interior cell (excluding Z_TOL_BOUNDARY_CELLS layers from each boundary):
  Compute |∇T|_cell = max(|T[i+1, j] − T[i, j]|, |T[i, j+1] − T[i, j]|) / cell-spacing.
- max gradient relative to T_uniform: max |∇T| · cell_size / T_uniform.

**Pass criterion.** max relative gradient < TOL_UNIFORM_SOURCE_REL (1%).

**Returns.** ValidationResult.

**Note.** This test verifies that the discretization recovers the trivial constant solution when the BCs are consistent with it. A failure here indicates a discretization bug (sign error in the Laplacian, wrong stencil normalization, etc.).

### 1.8 Function — `test_isothermal_source`

**Signature.**
`test_isothermal_source(grid: Optional[CylindricalGrid] = None, D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT, R_inner_kpc: float = 1.0, R_outer_kpc: float = 50.0, S_amplitude: float = 1.0) -> ValidationResult`

**Behavior.** Implements DM.4 §2.3 / DM.1 §3.1 expectation. The most diagnostic of the three.

**Setup.**
- Grid: production.
- Source: S(R, z) = S_amplitude / R² for R ∈ [R_inner_kpc, R_outer_kpc] in the disk plane, with disk geometry sech²(z / 0.3) / 0.6 vertical structure (matching DM.8 §1.6 default). Zero outside the active region.
- BoundaryConditions: defaults.
- Solve.
- Compute v_T(R) at z = 0 under Reading B per DM.11 §1.3:
  γ = D_T / κ_act_effective, where κ_act_effective is chosen so that the predicted v_T amplitude matches a target value (e.g., 150 km/s).
  Specifically: choose S_amplitude so that γ · S_amplitude / D_T = (150 km/s)² (the DM.1 self-consistency relation).
  v_T²(R) = R · γ · |dT/dR|_{z=0}.

**Comparison.**
- Expected: v_T(R) ≈ 150 km/s flat over R ∈ [5, 30] kpc.
- Compute |dv_T/dR| over R ∈ [5, 30] kpc using `np.gradient(v_T, grid.R)`.
- Take max |dv_T/dR| in the range.

**Pass criterion.** max |dv_T/dR| < TOL_ISOTHERMAL_DV_DR (2 km/s/kpc).

**Returns.** ValidationResult with computed_array = v_T(R) over the production R grid.

**Why this is the most diagnostic test.** Tests 1 and 2 verify the solver's discretization. Test 3 verifies that the full mapping from source to v_T (the Reading B sign convention, the gradient extraction, the unit consistency) reproduces the structural argument from DM.1. If Tests 1 and 2 pass but Test 3 fails, the bug is in the Reading B mapping or the activity-source convention, not in the solver.

### 1.9 Function — `test_grid_refinement`

**Signature.**
`test_grid_refinement(D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT) -> ValidationResult`

**Behavior.** Verifies that solution accuracy improves under grid refinement (i.e., second-order convergence is approximately observed).

**Setup.** Run `test_point_source` on three grids:
- Coarse: 150 R × 15 z (half production resolution).
- Medium: 300 R × 30 z (production).
- Fine: 600 R × 60 z (double production).

**Comparison.** Compute max relative error for each. Ratio coarse/medium and medium/fine.

**Pass criterion.** Each ratio < 0.5 (i.e., refinement halves the error or better — consistent with second-order accuracy).

**Returns.** ValidationResult with details containing the three error values.

**Caveat.** The non-uniform R-grid means second-order convergence is approximate. A factor-of-2 reduction is the practical target; strict O((dR)²) is not asserted.

### 1.10 Function — `test_pipeline_integration`

**Signature.**
`test_pipeline_integration(D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT) -> ValidationResult`

**Behavior.** End-to-end test through `run_single_galaxy` per the DM.11 integration-test spec.

**Setup.** Construct a synthetic `SparcGalaxy` whose v_obs is a perfectly flat 150 km/s curve over R ∈ [1, 30] kpc. Set v_baryon = 0 (zero baryonic contribution; v_obs comes entirely from temporal tension).

Strictly, v_baryon = 0 violates SparcGalaxy's structural assumption. Mitigate by setting v_disk to a tiny nonzero value (1 km/s) so v_baryon is nominally nonzero but contributes negligibly. Document this synthetic-galaxy convention in the test docstring.

- κ_act, α at the dimensional anchor.
- Tier-1 (no self-consistency loop, single solve).

**Comparison.** Run `run_single_galaxy`. The returned v_pred(R) should approximate flat 150 km/s.

**Pass criterion.** max |v_pred(R) − 150| over R ∈ [5, 25] kpc < 30 km/s.

**Returns.** ValidationResult with computed_array = v_pred over the SPARC R grid.

**Why this test exists.** Tests 1–3 test the solver and Reading B in isolation. Test 5 verifies they integrate correctly through `run_single_galaxy` — including the activity-source construction from v(R), the SparcGalaxy → grid pipeline, the χ² computation, and the result-dataclass packaging. A pass here is the final clearance for SPARC runs.

### 1.11 Function — `run_validation_suite`

**Signature.**
`run_validation_suite(grid: Optional[CylindricalGrid] = None, D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT, verbose: bool = True) -> dict`

**Behavior.** Runs all five tests sequentially. Returns a summary dict.

**Returns.**
- `all_passed: bool` — True only if all five pass.
- `results: list[ValidationResult]` — per-test results.
- `gate_status: str` — "PASS" or "FAIL with details".
- `wall_time_seconds: float`.

**Side effect.** If `verbose=True`, prints a one-line summary per test and a final gate verdict.

**Use case.** This is the function called as the first cell of `05_dm2_sparc_fits.ipynb` and the first call in `run_full_sample.py`. The SPARC pipeline does not run unless `all_passed = True`.

### 1.12 Function — `assert_validation_passed`

**Signature.**
`assert_validation_passed(grid: Optional[CylindricalGrid] = None, D_T: float = D_T_DEFAULT, lam: float = LAMBDA_DEFAULT) -> None`

**Behavior.** Calls `run_validation_suite` and raises `RuntimeError` with diagnostic info if `all_passed` is False. Returns None on pass.

**Use case.** Hard-gate enforcement. Called at the entry of any SPARC-touching script. The exception message includes which tests failed and their metric values, so the analyst can diagnose immediately.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_validation_tests.py`. These are tests *of the validation suite* — they verify that the suite correctly identifies pass and fail conditions on synthetic inputs.

Six tests, each isolating one structural property.

### 2.1 Test 1 — Point source passes on production grid

**Purpose.** Verify the Yukawa-shape test passes when the solver is correct.

**Inputs.** Production grid, D_T and λ at default.

**Expected.** `test_point_source` returns `passed=True`, `metric_value < TOL_POINT_SOURCE_REL`.

**Tolerance.** Pass criterion is the test's own pass criterion.

### 2.2 Test 2 — Uniform source passes on production grid

**Purpose.** Verify the uniform-source test passes when the solver is correct.

**Inputs.** Production grid, D_T and λ at default.

**Expected.** `test_uniform_source` returns `passed=True`, `metric_value < TOL_UNIFORM_SOURCE_REL`.

### 2.3 Test 3 — Isothermal source passes on production grid

**Purpose.** Verify the flat-curve test passes when the solver and Reading B mapping are correct.

**Inputs.** Production grid, D_T and λ at default.

**Expected.** `test_isothermal_source` returns `passed=True`, `metric_value < TOL_ISOTHERMAL_DV_DR`.

### 2.4 Test 4 — Grid refinement test produces decreasing error

**Purpose.** Verify second-order convergence is observed.

**Inputs.** Default D_T, λ.

**Expected.** `test_grid_refinement` returns `passed=True`. Both ratios (coarse/medium, medium/fine) < 0.5.

**Note.** This test runs three full PDE solves on different grids; runtime ~5 minutes total. Mark with `@pytest.mark.slow`.

### 2.5 Test 5 — Pipeline integration passes

**Purpose.** Verify the full pipeline reproduces a flat curve from a synthetic flat-input galaxy.

**Inputs.** Default D_T, λ.

**Expected.** `test_pipeline_integration` returns `passed=True`, `metric_value < 30` km/s.

**Note.** Runtime ~3 minutes (one full Tier-1 solve through `run_single_galaxy`). Mark with `@pytest.mark.slow`.

### 2.6 Test 6 — `run_validation_suite` correctly aggregates

**Purpose.** Verify the suite-level aggregator returns correct `all_passed` and `gate_status`.

**Inputs.** Default.

**Expected.**
- `result["all_passed"] == True`.
- `result["gate_status"] == "PASS"`.
- `len(result["results"]) == 5`.
- All five individual results have `passed == True`.
- `assert_validation_passed()` returns None (does not raise).

**Tolerance.** Logical correctness.

**Additional case.** Modify a tolerance constant temporarily to force a failure (e.g., set TOL_ISOTHERMAL_DV_DR to 0.001 — an unreachable threshold). Verify `all_passed = False`, `gate_status` includes "FAIL", `assert_validation_passed()` raises `RuntimeError`. Reset tolerance after the test.

---

## 3. Two-hour implementation plan

### 3.1 Hour 0:00 — 0:10 — Setup

- Verify DM.7–DM.12 are landed: full test suite passes.
- Create empty file `ed-lab/simulations/edsim/dm/validation_tests.py`.
- Add module docstring and imports per §1.1.
- Define tolerance constants per §1.3.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:10 — 0:25 — `ValidationResult` dataclass and `make_production_grid`

- Define `ValidationResult` per §1.4.
- Implement `make_production_grid` per §1.5.
- Smoke test: construct ValidationResult; build production grid; verify shapes.

**Checkpoint.** Both available.

### 3.3 Hour 0:25 — 1:00 — `test_point_source`

- Implement per §1.6.
- Includes Gaussian source construction, solver call, Yukawa-analytic comparison, max-relative-error computation, ValidationResult packaging.
- Smoke test: run on production grid, verify it returns a ValidationResult with sensible numbers (the Yukawa-shape test should pass at ~0.1% relative error if the solver is correct).

**Checkpoint.** Test 1 produces a passing ValidationResult.

### 3.4 Hour 1:00 — 1:25 — `test_uniform_source`

- Implement per §1.7.
- Includes uniform-source construction, BC override (set outer-R and outer-z to S_uniform / λ), solver call, gradient-metric computation, ValidationResult packaging.
- Smoke test: verify pass on production grid.

**Checkpoint.** Test 2 produces a passing ValidationResult.

### 3.5 Hour 1:25 — 1:55 — `test_isothermal_source`

This is the most diagnostic test; budget extra time.

- Implement per §1.8.
- Includes 1/R² source on the active disk, sech² vertical structure, solver call, Reading B mapping (γ = D_T / κ_act_effective), v_T(R) computation, |dv_T/dR| metric.
- The S_amplitude → κ_act_effective relation is the trickiest bookkeeping; lay it out explicitly in a comment block.
- Smoke test: verify pass.

**Checkpoint.** Test 3 produces a passing ValidationResult (the most rigorous structural verification).

### 3.6 Hour 1:55 — 2:00 — Buffer

End of two-hour implementation block. Tests 4 and 5, the suite aggregator, and the formal-test suite extend into hours 2–3.

---

## 4. Hours 2–4 — Additional tests, suite aggregator, debug

### 4.1 Hour 2:00 — 2:30 — `test_grid_refinement` and `test_pipeline_integration`

- Implement `test_grid_refinement` per §1.9 — three sub-runs of `test_point_source` at different resolutions.
- Implement `test_pipeline_integration` per §1.10 — synthetic flat-curve SparcGalaxy through `run_single_galaxy`.
- Smoke test each individually.

### 4.2 Hour 2:30 — 2:50 — `run_validation_suite` and `assert_validation_passed`

- Implement per §1.11 and §1.12.
- Smoke test: call the suite end-to-end. Verify all five results aggregate correctly.

### 4.3 Hour 2:50 — 3:30 — Write tests and run

- Create `ed-lab/simulations/edsim/dm/tests/test_validation_tests.py`.
- Write the six tests per §2.1–§2.6.
- Mark Tests 4 and 5 with `@pytest.mark.slow`.
- Run `pytest ed-lab/simulations/edsim/dm/tests/test_validation_tests.py -v -m "not slow"`.
- Run slow tests separately: `pytest -v -m slow`.

### 4.4 Hour 3:30 — 4:00 — Debug, document, commit

- Likely failures and resolutions:
  - **Test 1 fails at 0.5% but passes at 5%.** The 0.5% is tighter than DM.4's 5% baseline. If 5% passes, the solver is acceptable for the original DM.4 gate; tighten to 0.5% only if production-grid resolution genuinely supports it. If 0.5% is unattainable, document and relax to DM.4's original 5%.
  - **Test 3 fails the flat-curve criterion.** Diagnosis: Reading B sign convention (DM.11 §1.3); if v_T comes out negative or NaN, the sign is wrong. Fix and re-test.
  - **Test 5 (pipeline integration) fails.** Diagnosis: the synthetic v_baryon = 1 km/s convention may not be carrying through cleanly. Mitigation: try v_baryon = 10 km/s (still negligible) and see if the pipeline accepts it.

- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 7 complete. validation_tests.py implemented; 5/5 validation tests pass; DM.4 Validation Gate UNBLOCKED.`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/validation_tests.py
  git add ed-lab/simulations/edsim/dm/tests/test_validation_tests.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add validation_tests.py — DM Step 7 complete, Validation Gate unblocked"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/simulations/edsim/dm/validation_tests.py` exists with `ValidationResult` dataclass, `make_production_grid`, and seven test/aggregator functions per §1.4–§1.12.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_validation_tests.py` exists with six tests.
- [ ] All non-slow tests pass under `pytest -m "not slow"`.
- [ ] Slow tests (Tests 4, 5) run at least once and pass.
- [ ] All DM.7–DM.12 tests still pass.
- [ ] All public functions and dataclasses have complete docstrings.
- [ ] The module imports cleanly with no warnings.
- [ ] No TODO comments remain except those explicitly deferred (grid-factory consolidation; analytic boundary closed-form for Test 2).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to run log noting **DM.4 Validation Gate is now unblocked**.
- [ ] Commit landed.
- [ ] Push to origin successful.
- [ ] **DM.4 Gate 2 status verified: production-grid validation passes.**

If any item is unchecked, the session is incomplete. Do not advance to NGC 3198 (DM.4 Gate 3) until the §5 checklist is fully satisfied **and** `run_validation_suite()` returns `all_passed = True` on the production grid.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 7:

- **The reproducibility notebook `05_dm2_sparc_fits.ipynb`.** Session 8 task.
- **NGC 3198 actual proof-of-concept run.** That is DM.4 Gate 3, executed after Session 7 lands.
- **30-galaxy global fit.** DM.4 Gate 4.
- **Full-sample SPARC run.** Compute session, post-DM.4 gates.
- **Refactoring the duplicated grid factory.** Tagged TODO; address in a follow-up cleanup session.
- **Adding Tests 4–5 stratification or alternative metrics.** Six tests per the spec; expanding is a future enhancement.
- **Optimizing the validation suite for speed.** Acceptable runtime is up to 10 minutes; no optimization needed yet.

If during the session a tempting deviation surfaces, record it in a TODO and move on.

---

## 7. Risk inventory for Session 7

Three things most likely to consume more time than expected:

1. **Test 1 tolerance tightening.** The 0.5% threshold is tighter than DM.4 §2.1's 5% baseline. If the solver achieves only 1–2% on the production grid, tightening to 0.5% requires either grid refinement or solver-tolerance tightening. Mitigation: relax to 5% and document; the DM.4 gate still passes. Expected resolution: 15–30 minutes.

2. **Test 2 BC override interaction.** The uniform-source test requires Dirichlet at outer R and outer z set to T = S_uniform / λ — overriding the default Yukawa-far. The override mechanism may not be cleanly exposed in `BoundaryConditions`. Mitigation: pass the override values directly to `solver.solve` rather than through the BC config. Expected resolution: 15–30 minutes.

3. **Test 3 Reading B amplitude calibration.** The S_amplitude must be chosen so that the predicted v_T comes out at ~150 km/s (the target flat-curve amplitude). The dimensional bookkeeping (κ_act_effective = D_T / γ; γ chosen for self-consistency) is fiddly. Mitigation: write out the full chain in comments; smoke-test on a coarse grid first. Expected resolution: 30–60 minutes.

If the session runs over budget, do not skip writing tests or commit. The completion checklist is the gate.

---

## 8. Cross-checks against earlier memos

The implementation must respect five structural constraints:

1. **Yukawa Green's function for point source** (DM.0 §3, DM.9 §1.5): T(r) = exp(−r/L) / (4π D_T r). Verified by Test 1.

2. **Screened-Poisson uniform solution** (DM.9 §1.6 implicit): T = S/λ when ∇²T = 0. Verified by Test 2.

3. **DM.1 isothermal flat-curve derivation** (DM.1 §3.1): S ∝ 1/R² ⇒ T ∝ ln(R) ⇒ v_T flat under Reading B. Verified by Test 3.

4. **Reading B sign convention** (DM.11 §1.3): Φ_T = −γ T with γ = D_T / κ_act > 0. Critical for Test 3 sign correctness.

5. **DM.4 Gate 2 tolerances** (DM.4 §2.1–§2.3): 5% / 1% / 2 km/s/kpc. The validation suite uses 0.5% / 1% / 2 km/s/kpc — the first is tighter, the latter two match DM.4. The DM.4 gate passes if the suite passes; the suite is a more discriminating discrimination tool.

---

## End-of-turn summary

**What got done this turn:** the Session 7 coding plan is fully scoped. The validation suite has a `ValidationResult` dataclass, three core analytic tests (point source, uniform source, isothermal source), one grid-refinement test, one pipeline-integration test, an aggregator, and an assert wrapper for hard-gate enforcement. Six tests exercise the suite's pass/fail logic. Tolerances are explicit (0.5%, 1%, 2 km/s/kpc).

**What did not get done:** no Python code has been written. The DM.13 memo is a session plan, not the session itself.

**What this means for the program:** after Session 7, all eight modules of the DM pipeline are implemented. **DM.4 Gate 2 (the validation gate) is unblocked** when the suite passes on the production grid. The next gate is NGC 3198 (DM.4 Gate 3), which is a compute task, not a coding task.

**Decision after this session:** the question is whether to begin compute work (NGC 3198 single-galaxy run) or implement the reproducibility notebook (Session 8 / DM.14). Either is appropriate after Session 7 lands.

---

## Recommended Next Step

After confirming DM.7 through DM.12 are all fully landed (their §5 checklists satisfied), begin DM.13 Session 7: in `ed-lab/simulations/edsim/dm/`, create `validation_tests.py` and `tests/test_validation_tests.py`, then implement the components in the order specified in DM.13 §3.2–§3.5 (`ValidationResult` dataclass and `make_production_grid` → `test_point_source` → `test_uniform_source` → `test_isothermal_source` → `test_grid_refinement` and `test_pipeline_integration` → `run_validation_suite` and `assert_validation_passed`), following the unit conventions in §1.2 and the tolerance constants in §1.3. After all components are implemented, run the full validation suite on the production grid via `run_validation_suite()`; if `all_passed = True`, log "DM.4 Validation Gate UNBLOCKED" in the run log and proceed to Session 8 (reproducibility notebook) or to the NGC 3198 compute task. If the suite does not pass, halt and diagnose — no SPARC galaxy is run until validation clears.