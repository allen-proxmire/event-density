# DM.11 — Coding Session 5 Plan: `run_single_galaxy.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — twelfth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 5 and followed without further design decisions.
**Predecessor:** DM.10 (Session 4 plan — `boundary_conditions.py`).
**Target file:** `ed-lab/simulations/edsim/dm/run_single_galaxy.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py`
**Session goal:** End-to-end pipeline for one galaxy. After this session, NGC 3198 is runnable in principle (subject to the validation gate, which is Step 7 / DM.13 in this revised numbering).

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Note on session ordering.** DM.4's original ordering had `validation_tests.py` (Step 5) before `run_single_galaxy.py` (Step 6). DM.11 reverses this: implement the end-to-end pipeline first so the analytic-validation suite (Test 1: point-source Yukawa; Test 2: uniform-source flat T; Test 3: isothermal-source flat curve) can be assembled as integration tests *of the full pipeline* in Session 6. Each module's own test file (DM.7–DM.10) already exercises its component logic. The DM.4 §2 validation suite gates SPARC runs and is more meaningfully expressed as integration tests of `run_single_galaxy`.

**Prerequisite:** DM.7, DM.8, DM.9, and DM.10 must be fully landed before starting Session 5. The pipeline depends on all four prior modules.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("End-to-end pipeline for one SPARC galaxy: load → grid → activity → source → PDE solve → predicted rotation curve → residuals"), an authorship line, and references to DM.2 §1 (six-stage pipeline), DM.3 §1.1.6 (public API), DM.4 §3 (NGC 3198 spec), and DM.6 §4.2 (Reading B mapping).

Imports:
- `numpy as np`
- `from dataclasses import dataclass, field`
- `from typing import Optional`
- From sibling modules: `from .disk_geometry import baryonic_velocity, baryonic_potential_inplane`
- `from .activity_source import activity_index, activity_source_3d`
- `from .pde_solver import CylindricalGrid, ScreenedPoissonSolver`
- `from .boundary_conditions import BoundaryConditions`

### 1.2 Unit conventions

**Inherited from DM.7–DM.10. Not renegotiated.**

Galactic-natural units throughout the inner loop:
- Lengths: kpc.
- Velocities: km/s.
- Masses: M☉.
- Time: Gyr.
- Potentials: (km/s)² = 10⁶ m²/s².
- D_T: kpc²/Gyr.
- λ: 1/Gyr.

The pipeline accepts SPARC inputs in their native units (also kpc, km/s, M☉) and produces outputs in the same.

### 1.3 Reading B sign convention

DM.1 §4.1 named Reading B as "T as gravitational potential directly: Φ_T = γ T". In practice, the sign convention must produce Φ_T < 0 (attractive gravitational well) given T > 0 from a positive source. The committed convention is:

> **Φ_T(R, z) = − γ · T(R, z),    γ = D_T / κ_act > 0**

The negative sign ensures Φ_T < 0 where T > 0 (source-driven temporal-tension halo behaves gravitationally). The self-consistency relation γ · κ_act = D_T from DM.1 §4.2 still holds in magnitude.

The total potential at z = 0 is:

> Φ_total(R, 0) = Φ_baryon(R, 0) + Φ_T(R, 0)
>               = Φ_baryon(R, 0) − γ · T(R, 0)

The predicted rotation velocity at z = 0 follows from circular-orbit equilibrium:

> v_pred²(R) = R · ∂Φ_total / ∂R |_{z=0}
>            = v_baryon²(R) − R · γ · ∂T / ∂R |_{z=0}
>            = v_baryon²(R) + R · γ · |∂T/∂R| |_{z=0}    (since T decays outward)

If v_pred² turns out negative (e.g., due to numerical error or unphysical input), the function returns NaN at that point and flags the galaxy.

### 1.4 Dataclass — `SparcGalaxy`

**Definition.** Frozen dataclass holding the input data for one galaxy.

`@dataclass(frozen=True)`
- `galaxy_id: str`
- `distance_Mpc: float`
- `inclination_deg: float`
- `M_baryon: float` — total baryonic mass in M☉ (M_star + 1.4 M_HI from SPARC).
- `R_d: float` — disk scale length in kpc.
- `T_type: int` — morphological type (SPARC convention).
- `SB_disk: float` — disk surface brightness.
- `quality_flag: int` — SPARC quality flag (1, 2, or 3).
- `R_obs: np.ndarray` — observed radii in kpc.
- `v_obs: np.ndarray` — observed rotation velocities in km/s.
- `sigma_v: np.ndarray` — observation uncertainties in km/s.
- `v_gas: np.ndarray` — gas component in km/s.
- `v_disk: np.ndarray` — disk component in km/s.
- `v_bulge: np.ndarray` — bulge component in km/s (zeros if no bulge).

**Validation.** `__post_init__` checks that all velocity arrays have the same shape as R_obs; that R_obs is monotonically increasing; that distance, mass, and R_d are positive.

**Note.** A separate utility (deferred to a follow-up `sparc_io.py` module) loads `SparcGalaxy` instances from SPARC tables. Session 5 does not load real data; tests construct synthetic `SparcGalaxy` instances directly.

### 1.5 Dataclass — `SingleGalaxyResult`

**Definition.** Frozen dataclass holding the output of one galaxy run.

`@dataclass(frozen=True)`
- `galaxy_id: str`
- `R_obs: np.ndarray` — copy of input R_obs for downstream convenience.
- `v_obs: np.ndarray` — copy of input v_obs.
- `sigma_v: np.ndarray` — copy of input σ_v.
- `v_pred: np.ndarray` — predicted rotation velocity at R_obs.
- `delta_v: np.ndarray` — v_pred − v_obs.
- `chi2: float` — total χ² over the SPARC R-grid.
- `chi2_red: float` — reduced χ² (χ² / N_points).
- `T_field: np.ndarray` — full T(R_sim, z_sim) on the simulation grid (HDF5-compressible later).
- `R_sim: np.ndarray` — simulation R-grid.
- `z_sim: np.ndarray` — simulation z-grid.
- `tier_used: int` — 1, 2, or 3.
- `outer_iterations: int` — number of outer self-consistency iterations (1 for Tier 1, 1 for Tier 2, ≤ 50 for Tier 3).
- `converged: bool` — True if outer loop converged within tolerance.
- `damping_triggered: bool` — True if damping was activated.

### 1.6 Helper function — `build_simulation_grid`

**Signature.**
`build_simulation_grid(R_outer_sparc: float, R_max_grid: float = 5000.0, n_log: int = 200, n_lin: int = 100, n_z: int = 30, z_max: float = 1.5) -> CylindricalGrid`

**Behavior.** Constructs the simulation grid per DM.4 §5.1 spec (revised in DM.9 §1.3 to 300 R × 30 z).

R-grid: log-spaced from 0.01 kpc to max(50, R_outer_sparc + 5) kpc with `n_log` cells, then linearly spaced from that point to R_max_grid with `n_lin` cells. Total: 300 cells by default.

z-grid: uniform from 0 to z_max kpc with `n_z` cells. (Mid-plane symmetry; z is non-negative.)

**Returns.** `CylindricalGrid` object.

**Validation.** R_outer_sparc > 0; z_max > 0.

### 1.7 Helper function — `compute_v_pred_at_sparc_radii`

**Signature.**
`compute_v_pred_at_sparc_radii(T_field: np.ndarray, grid: CylindricalGrid, gamma: float, v_baryon_sparc: np.ndarray, R_sparc: np.ndarray) -> np.ndarray`

**Behavior.** Implements the Reading B mapping per §1.3.

1. Extract T(R, z=0) — the j=0 column of T_field (which is shape (n_R, n_z)).
2. Compute dT/dR at z=0 using `np.gradient(T_at_z0, grid.R)`.
3. Interpolate dT/dR at z=0 from the simulation R-grid to the SPARC R-grid (cubic spline, no extrapolation).
4. Compute v_T²(R_sparc) = R_sparc · γ · (−dT/dR_sparc).
5. v_pred²(R_sparc) = v_baryon_sparc² + v_T²(R_sparc).
6. v_pred(R_sparc) = sqrt(v_pred²) where v_pred² ≥ 0; NaN where v_pred² < 0 (flagged).

**Returns.** v_pred array of length len(R_sparc) in km/s.

**Validation.** T_field shape matches grid; R_sparc within grid.R range.

### 1.8 Helper function — `compute_chi2`

**Signature.**
`compute_chi2(v_pred: np.ndarray, v_obs: np.ndarray, sigma_v: np.ndarray, ignore_nan: bool = True) -> tuple[float, float]`

**Behavior.** Returns (χ², χ²_red) where:
- χ² = Σ_i [(v_pred(R_i) − v_obs(R_i)) / σ_v(R_i)]²
- χ²_red = χ² / N_valid

If `ignore_nan=True`, NaN values in v_pred are excluded from the sum (and N_valid reduced accordingly).

**Validation.** All three input arrays must be the same length.

### 1.9 Main function — `run_single_galaxy`

**Signature.**
`run_single_galaxy(galaxy: SparcGalaxy, kappa_act: float, alpha: float, D_T: float, lam: float, tier: int = 3, tol: float = 1.0, max_outer_iter: int = 50, damping_threshold: int = 3, verbose: bool = False) -> SingleGalaxyResult`

**Behavior.** Orchestrates the six-stage pipeline.

**Stage 1 — Setup.**
- Compute v_baryon_sparc = baryonic_velocity(galaxy.R_obs, v_gas, v_disk, v_bulge).
- Build the simulation grid: `grid = build_simulation_grid(galaxy.R_obs.max())`.
- Compute γ = D_T / κ_act.
- L = √(D_T / λ).
- Build BoundaryConditions with defaults.
- Construct ScreenedPoissonSolver: `solver = ScreenedPoissonSolver(grid, D_T, lam, bc=bc)`.

**Stage 2 — Tier-1 / initial pass.**
- Use v_init = v_baryon_sparc as the initial velocity for activity construction.
- Compute A(R_sparc) = activity_index(galaxy.R_obs, v_init, alpha).
- Build source: `S = activity_source_3d(grid.R, grid.z, galaxy.R_obs, A, kappa_act, h_disk=0.3)`.
- Solve: `result = solver.solve(S, ..., tol=1e-6, max_iter=5000)`.
- Compute v_pred from T = result['T'] using `compute_v_pred_at_sparc_radii`.

**If `tier == 1`:** record outer_iterations = 1 and proceed to Stage 5.

**Stage 3 — Tier-2 / single iteration on activity.**
- Replace v_init with v_pred from Tier 1.
- Repeat A construction, source build, PDE solve, v_pred extraction.

**If `tier == 2`:** record outer_iterations = 1 (Stage 3 is a single update; the iteration counter measures self-consistency loops in Tier 3 only) and proceed to Stage 5.

**Stage 4 — Tier-3 / fixed-point iteration.**
- Initialize v_pred_prev = v_pred from Tier 1's first solve.
- For n in 1..max_outer_iter:
  - Compute A_n = activity_index(galaxy.R_obs, v_pred_prev, alpha).
  - Build source S_n, solve, extract v_pred_n.
  - Check convergence: max |v_pred_n − v_pred_prev| over R_sparc < tol (default 1.0 km/s).
  - If converged: record outer_iterations = n, break.
  - Damping: if max-residual fails to decrease for `damping_threshold` consecutive iterations, replace v_pred_n with 0.5 (v_pred_n + v_pred_prev) and set damping_triggered = True.
  - Update v_pred_prev = v_pred_n.

**Stage 5 — Compute residuals and χ².**
- delta_v = v_pred − v_obs.
- (chi2, chi2_red) = compute_chi2(v_pred, v_obs, sigma_v).

**Stage 6 — Build SingleGalaxyResult.**
- Populate all fields per §1.5.

**Returns.** `SingleGalaxyResult`.

**Verbose mode.** If True, print per-outer-iteration max-residual and final χ²_red.

**Robustness.** If the inner solver (`solver.solve`) returns `converged=False`, do not raise — record outer_iterations as the iteration count when the failure occurred and converged=False on the result. The caller (Step 8 / DM.13) decides how to handle non-converging galaxies.

### 1.10 Inclination correction

SPARC v_obs is already inclination-corrected in the released tables (the listed v_obs is the deprojected rotation velocity). No additional inclination correction is applied in this module.

The `inclination_deg` field of `SparcGalaxy` is preserved for downstream filtering (DM.4 §5.1: drop galaxies with i < 30° because deprojection becomes unreliable). Filtering is done in `run_full_sample.py` (Step 8 / DM.13), not here.

### 1.11 Distance scaling

SPARC R_obs and M_baryon both scale with distance (R ∝ D, M ∝ D²). The released SPARC tables are at the assumed SPARC distance for each galaxy. No additional distance scaling is applied in this module; if a future analysis needs to test distance sensitivity, that's a separate utility.

### 1.12 Missing SPARC fields

If a SPARC galaxy lacks a bulge (most do), `v_bulge` is zeros. The pipeline handles this transparently via `baryonic_velocity` accepting zero arrays.

If a galaxy has missing distance, M_baryon, or R_d (rare but possible for low-quality entries), the SPARC ingestion utility (out of Session 5 scope) flags these. Within `run_single_galaxy`, no missing-field handling is needed beyond standard validation.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py`. Use `pytest`, plain assertions, `pytest.approx`. Synthetic `SparcGalaxy` instances are constructed in test fixtures.

Six tests, each isolating one structural property.

### 2.1 Test 1 — Synthetic galaxy with known v_pred (analytic limit)

**Purpose.** Verify the full pipeline reproduces a known analytic result in a limiting case.

**Setup.** Construct a synthetic galaxy with v_baryon = 0 everywhere (zero baryons; not physical but a clean test). Force v_pred to come entirely from temporal tension. Set the activity profile to be such that the resulting T is a known function (e.g., a Gaussian source giving a known Yukawa convolution).

**Inputs.**
- Galaxy: synthetic with R_obs = np.linspace(1, 30, 30) kpc, v_obs = some baseline (used for χ² but not the test pass criterion), v_gas = v_disk = v_bulge = zeros. Distance = 10 Mpc, M_baryon = 10⁹ M☉ (small but nonzero so validation passes), R_d = 3 kpc, inclination = 60°.
- κ_act = 1.0 in arbitrary units, α = 0.5.
- D_T, λ at production values.
- Tier = 1.

**Expected.** v_pred is the pure-temporal-tension contribution, with shape determined by the activity profile derived from v_obs (since v_baryon = 0). For the synthetic case with constant v_obs = 100 km/s, A(R) = α · 0 + (1−α) · (100/R)² (since shear is zero for constant v_obs and vorticity is the dominant term). The resulting T should be approximately logarithmic, giving v_pred(R) approximately constant — but the value depends on how the analytic limit traces through the numerics.

Rather than predicting an exact value, the test verifies:
- v_pred(R) is finite, positive, and within an order of magnitude of v_obs.
- v_pred(R) varies less than 50% across R (i.e., approximately flat — the structural prediction).

**Tolerance.**
- All v_pred values finite and positive.
- max(v_pred)/min(v_pred) < 1.5 across R ∈ [5, 25] kpc.

This is a weak test; its purpose is "the pipeline runs end-to-end and produces sensible output," not "the numerical answer is exact."

### 2.2 Test 2 — Correct grid construction

**Purpose.** Verify `build_simulation_grid` produces a grid satisfying the design spec.

**Inputs.**
- R_outer_sparc = 30 kpc.

**Expected.**
- grid.R[0] ≈ 0.01 kpc (innermost log cell).
- grid.R[-1] ≈ 5000 kpc (outermost linear cell).
- grid.n_R = 300.
- grid.n_z = 30.
- grid.z[0] = 0.
- grid.z[-1] = 1.5 kpc.
- grid.R is monotonically strictly increasing.
- The transition between log and linear regions occurs at ~50 kpc (R[200] ≈ 50).

**Tolerance.** Exact for n_R, n_z, z[0], z[-1]. ±5% for the log-to-linear transition radius.

### 2.3 Test 3 — Correct activity computation in Stage 2

**Purpose.** Verify Stage 2 of `run_single_galaxy` correctly invokes `activity_index` with the right v_init.

**Inputs.** Mock galaxy with v_obs = 200 km/s constant, v_baryon also constant 200 (synthetic). Tier = 1.

**Expected.** A(R) = 0.5 · (dv_bar/dR)² + 0.5 · (v_bar/R)² = 0 + 0.5 · (200/R)² for constant v_bar. The check is internal: verify that the source `S` passed to the solver is consistent with this A(R). Use a debug hook (return source array as part of result) or trace the call.

**Tolerance.** Per-radius source value matches direct activity_index computation to within 1%.

**Implementation note.** This test may require exposing the source S in the result dataclass for debugging, or factoring the Stage-2 logic into a helper function tested in isolation. Either is fine; the latter is cleaner.

### 2.4 Test 4 — Correct PDE call integration

**Purpose.** Verify that the PDE solver is invoked with correctly constructed inputs and returns a sensible T field.

**Inputs.** Mock galaxy with thin-disk activity. Tier = 1.

**Expected.**
- `solver.solve` is called once.
- The returned T field has shape (n_R_sim, n_z_sim) = (300, 30).
- T[0, 0] > 0 (positive midplane on-axis value, from positive activity source).
- T at the outermost R cell matches the Yukawa-far BC (verified by Test 4 of DM.10).

**Tolerance.** T[0, 0] > 0; T shape correct; T at outer R matches BC within 1%.

### 2.5 Test 5 — Correct v_pred extraction (Reading B)

**Purpose.** Verify `compute_v_pred_at_sparc_radii` correctly applies the Reading B mapping.

**Inputs.**
- Mock T_field of shape (300, 30) with a known analytic form: T(R, z=0) = A · ln(R / R_max) for R in some range, zero elsewhere. (This corresponds to the DM.1 analytic flat-curve limit.)
- v_baryon_sparc = zeros (so v_pred² = v_T² alone).
- R_sparc in the active range.
- γ chosen so that the predicted v_T is a known constant.

**Expected.** v_pred(R) ≈ √(R · γ · A / R) = √(γ · A) — constant across R_sparc.

**Tolerance.** Relative spread of v_pred across R_sparc < 5% (numerical-derivative noise from `np.gradient` plus interpolation).

### 2.6 Test 6 — NGC 3198 synthetic mock

**Purpose.** End-to-end pipeline test on a galaxy with NGC 3198–like parameters. No real SPARC data is loaded; the SparcGalaxy is constructed synthetically.

**Inputs.**
- galaxy_id = "NGC3198_mock"
- distance_Mpc = 13.8, inclination_deg = 71, M_baryon = 5e10, R_d = 3.0, T_type = 5, SB_disk = 1e8, quality_flag = 1.
- R_obs = np.linspace(0.7, 38, 40) kpc.
- v_obs = synthetic flat-ish curve: 50 + 100 · (1 − exp(−R / 3)) km/s, capping near v ≈ 150 at R = 38 kpc.
- σ_v = 5 km/s constant.
- v_gas, v_disk constructed to give v_baryon ≈ 110 km/s at R = 5 kpc, falling to ≈ 60 km/s at R = 38 kpc (Keplerian-like). v_bulge = zeros.
- κ_act at the dimensional anchor from DM.4 §3.2.
- α = 0.5.
- D_T, λ at production values.
- Tier = 3, max_outer_iter = 50.

**Expected.**
- The pipeline runs to completion without crashing.
- v_pred is finite and positive at all R_obs.
- v_pred at R = 25 kpc is in the range [80, 200] km/s (sensible order of magnitude; exact value depends on κ_act tuning).
- Tier-3 outer loop converges in < 50 iterations.
- chi2_red < 100 (not necessarily < 1; the mock κ_act is not fitted).

**Tolerance.**
- All assertions above hold.
- Wall time < 10 minutes.

---

## 3. Two-hour implementation plan

### 3.1 Hour 0:00 — 0:10 — Setup

- Verify DM.7–DM.10 are landed: `pytest ed-lab/simulations/edsim/dm/tests/` passes cleanly.
- Create empty file `ed-lab/simulations/edsim/dm/run_single_galaxy.py`.
- Add module docstring and imports per §1.1.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:10 — 0:30 — Dataclasses

- Define `SparcGalaxy` per §1.4 with validation.
- Define `SingleGalaxyResult` per §1.5.
- Smoke test: construct each with synthetic data, verify validation catches bad inputs.

**Checkpoint.** Dataclasses instantiate and validate correctly.

### 3.3 Hour 0:30 — 0:50 — Helper functions

- Implement `build_simulation_grid` per §1.6.
- Implement `compute_chi2` per §1.8.
- Implement `compute_v_pred_at_sparc_radii` per §1.7 — this includes the gradient computation, sign convention, and interpolation.
- Smoke-test each in REPL.

**Checkpoint.** All three helpers behave as expected on synthetic inputs.

### 3.4 Hour 0:50 — 1:30 — `run_single_galaxy` Stages 1, 2, 5, 6 (Tier-1 path)

- Implement Stage 1 (setup): grid, γ, BC, solver.
- Implement Stage 2 (initial activity + PDE solve + v_pred): one solver call, one v_pred extraction.
- Skip Stage 3 and Stage 4 for now (Tier-1 only).
- Implement Stage 5 (residuals and χ²).
- Implement Stage 6 (build result).
- Smoke test on a synthetic galaxy with Tier = 1.

**Checkpoint.** Tier-1 path runs end-to-end on synthetic input.

### 3.5 Hour 1:30 — 1:50 — Stages 3 and 4 (Tier-2 and Tier-3)

- Implement Stage 3 (Tier-2 single update on activity).
- Implement Stage 4 (Tier-3 fixed-point loop with damping).
- Smoke test Tier-3 on the same synthetic galaxy; verify convergence.

**Checkpoint.** All three tiers run; Tier-3 converges within a few iterations on a clean synthetic input.

### 3.6 Hour 1:50 — 2:00 — Buffer

- Re-read each function's docstring.
- Remove debug prints.
- Verify imports are minimal.

End of two-hour implementation block.

---

## 4. Hours 2–4 — Tests and debugging

### 4.1 Hour 2:00 — 2:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py`.
- Write the six tests per §2.1–§2.6.
- For Test 6 (NGC 3198 mock), construct the synthetic SparcGalaxy in a fixture.

### 4.2 Hour 2:30 — 3:30 — Run and debug

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py -v`.
- Likely failures and resolutions:
  - **Sign convention error in v_pred extraction (Test 5).** v_pred² comes out negative. Diagnosis: missing minus sign in §1.3 formula. Fix: Φ_T = −γ T (negative coupling).
  - **Interpolation out-of-range error (Test 5).** R_sparc extends beyond simulation R-grid. Mitigation: ensure `build_simulation_grid` covers the SPARC range. The R[200] ≈ 50 kpc transition handles galaxies up to ~30–40 kpc.
  - **Tier-3 oscillation on NGC 3198 mock (Test 6).** The damping in Stage 4 should kick in. If it doesn't, verify the damping_threshold logic: the residual must fail to decrease for 3 consecutive iterations to trigger damping.
  - **Solver non-convergence on NGC 3198 mock.** Inner solver returns converged=False. Diagnosis: SOR ω might need tuning, or the source has a feature that's hard for SOR. Mitigation: increase max_iter to 10000; if still failing, halt and diagnose.

### 4.3 Hour 3:30 — 4:00 — Documentation, lint, commit

- Verify all dataclasses, helpers, and the main function have complete docstrings.
- Run lint if configured.
- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 5 complete. run_single_galaxy.py implemented; 6/6 tests pass.`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/run_single_galaxy.py
  git add ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add run_single_galaxy.py and tests — DM Step 5 complete"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/simulations/edsim/dm/run_single_galaxy.py` exists with two dataclasses, three helper functions, and the main `run_single_galaxy` function.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_run_single_galaxy.py` exists with six tests.
- [ ] All six tests pass under `pytest`.
- [ ] All DM.7, DM.8, DM.9, and DM.10 tests still pass.
- [ ] All public dataclasses, helpers, and main function have complete docstrings.
- [ ] The module imports cleanly with no warnings.
- [ ] No TODO comments remain except those explicitly deferred (sparc_io.py for real SPARC ingestion; performance optimization of Tier-3 loop; non-axisymmetric corrections).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to run log.
- [ ] Commit landed with message `Add run_single_galaxy.py and tests — DM Step 5 complete`.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not advance to Session 6 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 5:

- **`sparc_io.py` — real SPARC data ingestion.** Tests use synthetic SparcGalaxy instances. Real SPARC ingestion is a separate utility.
- **`fit_activity_parameters.py` — global fit across galaxies.** Step 7 / DM.13 task.
- **`run_full_sample.py` — parallelized sample run.** Step 8 / DM.14 task.
- **The notebook `05_dm2_sparc_fits.ipynb`.** All eight modules must be in place first.
- **Performance optimization of the Tier-3 loop.** Acceptable runtime on the NGC 3198 mock is up to 10 minutes; if the production target of 3 minutes per galaxy is exceeded, optimization is a follow-up session.
- **Non-axisymmetric corrections.** The pipeline is axisymmetric; bars, warps, lopsidedness are out of scope.
- **Cluster-scale extension.** The merger-lag paper handles clusters; this pipeline is galactic.

If during the session a tempting deviation surfaces, record it in a TODO and move on.

---

## 7. Risk inventory for Session 5

Three things most likely to consume more time than expected:

1. **Reading B sign convention.** §1.3 commits to Φ_T = −γ T (negative coupling). If the analyst implements Φ_T = +γ T by mistake, v_pred² comes out as v_baryon² minus the temporal-tension contribution — the curve falls instead of flattening. Test 5 catches this directly. Expected resolution: 10–20 minutes.

2. **Tier-3 outer-loop convergence behavior.** The damping logic activates only when the residual fails to decrease for 3 consecutive iterations. For galaxies with v_baryon ≪ v_obs, the activity source can drive large changes between iterations and trigger oscillation. The damping factor of 0.5 is a heuristic; if oscillation persists, try damping factor 0.3 or 0.7. Expected resolution: 30–60 minutes if it bites.

3. **Numerical derivative noise on the SPARC R-grid.** `np.gradient` on a ~30-point R-grid produces noisy dT/dR values, especially at the inner and outer ends. The cubic-spline interpolation from sim grid to SPARC grid mitigates this somewhat. If Test 5 fails by more than a few percent, consider switching to a higher-order finite-difference (e.g., 5-point stencil). Expected resolution: 20–40 minutes.

If the session runs over budget, do not skip writing tests or commit. The completion checklist is the gate.

---

## 8. Cross-checks against earlier memos

The implementation must respect four structural constraints established earlier:

1. **Reading B mapping** (DM.1 §4.1, refined in §1.3 above): Φ_T = −γ T with γ = D_T / κ_act. This is the load-bearing structural commitment of the DM arc; a sign error here invalidates the entire activity-source mechanism.

2. **Tier-3 self-consistency** (DM.4 §3.2): the activity index is built from v_pred (not v_baryon) at convergence. Until convergence, the iteration depends on initial conditions and damping behavior.

3. **SPARC R-grid for output** (DM.4 §6.1): v_pred is reported at R_obs (the SPARC grid), not on the simulation grid. Interpolation happens via `compute_v_pred_at_sparc_radii`.

4. **Universal (κ_act, α) across galaxies** (DM.4 §1): the function accepts these as inputs. The hard rule that they are *globally fitted* is enforced at the next-level-up, in `fit_activity_parameters.py` (Step 7).

---

## End-of-turn summary

**What got done this turn:** the Session 5 coding plan is fully scoped. The end-to-end pipeline has six stages, two dataclasses, three helper functions, and one main entry point. The Reading B sign convention is committed (Φ_T = −γ T). Tier handling (1, 2, 3) is specified with damping logic. Six tests have explicit inputs, expected outputs, and tolerances. The two-hour implementation plan and the two-hour test/debug block are sequenced.

**What did not get done:** no Python code has been written. The DM.11 memo is a session plan, not the session itself.

**What this means for the program:** after Session 5, five of eight modules will be complete. The pipeline runs end-to-end on synthetic data. Real SPARC ingestion, validation suite as integration tests, parameter fitting, and full-sample execution remain.

**Decision after this session:** Step 6 (next memo, DM.12) — the validation suite as integration tests of the pipeline. This is a slight reordering from DM.4: instead of validation_tests.py being a separate gate before any galaxy runs, the analytic-validation cases (point source, uniform source, isothermal source) are run as integration tests through `run_single_galaxy` (with synthetic SparcGalaxy instances representing each test case). The DM.4 §2 tolerances still apply.

---

## Recommended Next Step

After confirming DM.7, DM.8, DM.9, and DM.10 are all fully landed (their §5 checklists satisfied), begin DM.11 Session 5: in `ed-lab/simulations/edsim/dm/`, create `run_single_galaxy.py` and `tests/test_run_single_galaxy.py`, then implement the components in the order specified in DM.11 §3.2–§3.5 (`SparcGalaxy` and `SingleGalaxyResult` dataclasses → `build_simulation_grid`, `compute_chi2`, `compute_v_pred_at_sparc_radii` helpers → `run_single_galaxy` Tier-1 path → `run_single_galaxy` Tier-2 and Tier-3 paths), following the unit conventions in §1.2 and the Reading B sign convention in §1.3. Stop and run the test suite per §4.2 only after all components are implemented; do not attempt Session 6 until the §5 session-complete checklist is fully satisfied.