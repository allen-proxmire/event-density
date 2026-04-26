# DM.8 — Coding Session 2 Plan: `activity_source.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — ninth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 2 and followed without further design decisions.
**Predecessor:** DM.7 (Session 1 plan — `disk_geometry.py`).
**Target file:** `ed-lab/simulations/edsim/dm/activity_source.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_activity_source.py`
**Session goal:** Step 2 of the DM.4 implementation sequence complete. After this session, Step 3 (`pde_solver.py`) is unblocked.

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Prerequisite:** DM.7 Session 1 must be fully complete (its §5 checklist satisfied) before starting Session 2. The DM.8 unit conventions and edge-case philosophy match DM.7; if DM.7 is not landed, the foundations are not yet in place.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("Activity-density source term construction for the DM-arc PDE: shear, vorticity, composite activity index, and 3D source-field assembly"), an authorship line, and references to DM.1 (the structural argument), DM.3 §1.1.2 (the public API), and DM.6 §4.2 (Session 1 prereq).

Imports: `numpy as np`, `scipy.interpolate.CubicSpline`. No other dependencies for this module.

### 1.2 Unit conventions

**Inherited from DM.7 §1.2 — not renegotiated.**

- Lengths: kpc.
- Velocities: km/s.
- **Velocity gradients (dv/dR):** km/s per kpc.
- **Shear² and vorticity²:** (km/s / kpc)² = (km/s/kpc)². This is the natural unit for both quantities; do *not* convert to SI inverse-second-squared inside this module. Conversion happens at the source-coupling stage if needed.
- **Activity index A(R):** (km/s/kpc)². Same unit as shear² and vorticity².
- **Coupling κ_act:** units chosen at the framework level so that S = κ_act · A · ρ_geom has the right dimensions for the PDE source. Treat κ_act as a black-box scalar inside this module; do not enforce a particular unit.
- **Disk thickness h_disk:** kpc.
- **Source field S(R, z):** units of κ_act × (km/s/kpc)² × (1/kpc). The PDE solver consumes whatever units this returns; consistency is enforced by the κ_act fit, not by this module.

### 1.3 Function 1 — `shear_squared`

**Signature.**
`shear_squared(R: np.ndarray, v: np.ndarray, smooth: bool = False) -> np.ndarray`

**Behavior.** Returns (dv/dR)² at every R-grid point.

**Numerical method.** Use `numpy.gradient(v, R)` for the derivative. This applies second-order centered differences on the interior with second-order accurate one-sided differences at the endpoints; it correctly handles non-uniform spacing by passing R as the second argument.

**Smoothing.** If `smooth=True`, apply a 3-point box filter to dv/dR before squaring (mitigates SPARC sampling noise). Default is `smooth=False` so that test outputs are unambiguous; production use of the function may pass `smooth=True`.

**Validation.** Require R and v to have matching shape and length ≥ 2. Require R strictly monotonically increasing.

**Edge cases.**
- Length-2 input: forward/backward differences only; no centered. Function still returns shape (2,) with one shear value used for both endpoints (a numerical compromise — flag in docstring).
- NaN propagation: NaN in v leads to NaN in adjacent shear values. Documented behavior.

**Docstring.** State inputs (R kpc, v km/s, smooth bool), output ((km/s/kpc)², same shape as inputs), method (`numpy.gradient` with non-uniform spacing), and the smoothing option's effect.

### 1.4 Function 2 — `vorticity_squared`

**Signature.**
`vorticity_squared(R: np.ndarray, v: np.ndarray) -> np.ndarray`

**Behavior.** Returns (v/R)² at every R-grid point.

**Regularization at R = 0.** If any R[i] == 0, the value at that point is set to (dv/dR|_{R=0})², where the derivative is computed from the forward difference (v[1] − v[0]) / (R[1] − R[0]). This is the physical limit for v(0) = 0 in axisymmetric rotation: ω = v/R → dv/dR as R → 0.

For R[i] > 0 but very small (R[i] < 1e-3 kpc, say), no special regularization — the direct (v/R)² is well-defined since v is presumed continuous and v(0) = 0.

**Validation.** Require R and v matching shape, length ≥ 1, R non-negative, R monotonic non-decreasing. (Allow R[0] = 0 since some grids may include the axis.)

**Edge cases.**
- Single-point input: return shape (1,) with the direct (v/R)² value (or the regularized derivative if R == 0).
- NaN in v at any point propagates to vorticity² at that point.
- Negative v values: physics convention is non-negative v in axisymmetric rotation curves, but the function squares so this is benign. No validation error.

**Docstring.** State inputs (R kpc, v km/s), output ((km/s/kpc)², same shape as inputs), method (direct division with R=0 forward-difference regularization), and the physical limit.

### 1.5 Function 3 — `activity_index`

**Signature.**
`activity_index(R: np.ndarray, v: np.ndarray, alpha: float = 0.5, smooth: bool = False) -> np.ndarray`

**Behavior.** Returns A(R) = α · shear² + (1 − α) · vorticity² where shear² and vorticity² are computed from `shear_squared` and `vorticity_squared`.

**Composition.** Linear combination only. No cross-terms, no nonlinearities.

**Validation.** Require α ∈ [0, 1]. Raise `ValueError` otherwise. R, v requirements inherited from underlying functions.

**Edge cases.** Inherit from `shear_squared` and `vorticity_squared`. NaN propagation: NaN in either component yields NaN in A.

**Docstring.** State inputs (R kpc, v km/s, alpha dimensionless ∈ [0, 1], smooth optional), output ((km/s/kpc)², same shape as inputs), and the linear combination formula. Note that α is a free parameter to be fit globally (DM.4 §1).

### 1.6 Function 4 — `activity_source_3d`

**Signature.**
`activity_source_3d(R_sim: np.ndarray, z_sim: np.ndarray, R_act: np.ndarray, A_act: np.ndarray, kappa_act: float, h_disk: float = 0.3) -> np.ndarray`

**Behavior.** Returns S(R, z) of shape (len(R_sim), len(z_sim)).

The activity index A(R) is computed on the input grid R_act (which is typically the SPARC R-grid for a galaxy). It is interpolated to the simulation grid R_sim, then multiplied by κ_act and the vertical sech² profile.

The output is:

> S(R_sim[i], z_sim[j]) = κ_act · A_interp(R_sim[i]) · sech²(z_sim[j] / h_disk) / (2 h_disk)

with A_interp obtained by cubic-spline interpolation of A_act on R_act, evaluated at R_sim. Outside [R_act.min(), R_act.max()], A_interp returns 0 (no activity outside the observed disk).

**Numerical.**
- Interpolation: `scipy.interpolate.CubicSpline` with `bc_type='natural'` and `extrapolate=False`. Outside-domain returns NaN; explicitly replace NaN with 0 after interpolation.
- Vertical profile: `1 / (np.cosh(z_sim / h_disk)**2 * 2 * h_disk)`. Note `np.cosh` is fine for z up to ~10 h_disk; beyond that the function approaches zero correctly via cosh's exponential growth.

**Validation.** Require R_sim and z_sim 1-D arrays. Require R_act and A_act matching length ≥ 2 (cubic spline requires this). Require κ_act > 0 (sign convention: activity sources tension positively). Require h_disk > 0.

**Edge cases.**
- z_sim contains 0: at z=0, sech²(0)/(2h_disk) = 1/(2 h_disk). The vertical profile peaks on the midplane.
- A_act all zeros (quiescent galaxy): S returns all zeros.
- R_sim extends well beyond R_act.max(): the field is zero in that exterior region, which is the correct boundary behavior for the PDE solver downstream.

**Docstring.** State inputs (kpc, kpc, kpc, (km/s/kpc)², κ_act units arbitrary, kpc), output (2-D array shape (len(R_sim), len(z_sim))), interpolation method, and the vertical-profile form. Note that h_disk = 0.3 kpc default is the DM.4 nuisance parameter.

### 1.7 Module-level constants

None required. h_disk has a default value at the function-signature level. κ_act is always supplied externally.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_activity_source.py`. Use `pytest` conventions, plain assertions, `pytest.approx` for floating-point.

Seven tests, each isolating one structural property.

### 2.1 Test 1 — Shear of flat rotation curve

**Purpose.** Verify `shear_squared` returns ~0 for a flat curve.

**Inputs.**
- R = np.linspace(1, 30, 30) kpc (uniform)
- v = 200 * np.ones(30) km/s

**Expected.** shear_squared = 0 at all points.

**Tolerance.** max value < 10⁻⁶ (km/s/kpc)² (numerical-derivative noise).

### 2.2 Test 2 — Vorticity of solid-body rotation

**Purpose.** Verify `vorticity_squared` recovers the constant ω² for v = ω₀ R.

**Inputs.**
- R = np.linspace(1, 10, 10) kpc
- v = 10 * R (so v = 10 km/s at R = 1; ω₀ = 10 km/s/kpc)

**Expected.** vorticity_squared = 100 (km/s/kpc)² at all points.

**Tolerance.** Relative error < 1%.

**Additional assertion.** Calling `shear_squared` on the same input gives 100 as well (since dv/dR = 10 = ω₀ for solid-body). So in this case shear² and vorticity² are equal, which is correct physics for solid-body rotation.

### 2.3 Test 3 — Composite A(R) for mixed profile

**Purpose.** Verify `activity_index` correctly combines shear² and vorticity² across α values.

**Inputs.**
- R = np.array([1, 2, 5, 10, 20]) kpc
- v = 100 + 5 * R km/s (linear rising; dv/dR = 5)
- shear² = 25 (km/s/kpc)² at all points
- v/R = (100 + 5R)/R = 100/R + 5
- vorticity²: at R=1: 105² = 11025; at R=10: 15² = 225; at R=20: 10² = 100

**Expected.** For each α ∈ {0.0, 0.5, 1.0}, verify A(R) = α · 25 + (1 − α) · vort²(R) at every point.
- α = 0: A = vort²
- α = 1: A = 25 everywhere
- α = 0.5: A = 12.5 + 0.5 · vort²

**Tolerance.** Relative error < 1% for all three α values at all five R values.

**Additional assertion.** α = 1.5 raises `ValueError`; α = -0.1 raises `ValueError`.

### 2.4 Test 4 — Regularization at R = 0

**Purpose.** Verify `vorticity_squared` handles R = 0 by limiting v/R → dv/dR.

**Inputs.**
- R = np.array([0.0, 0.1, 1.0, 10.0]) kpc
- v = 50 * R km/s (so v = 0 at R = 0, ω₀ = 50)

**Expected.** vorticity_squared = 2500 (km/s/kpc)² at all four points. At R = 0, the function uses the forward-difference regularization: (v[1] - v[0]) / (R[1] - R[0]) = 5 / 0.1 = 50, squared = 2500.

**Tolerance.** Relative error < 1% per point.

### 2.5 Test 5 — Large-R 1/R² tail for flat curve

**Purpose.** Verify `vorticity_squared` correctly produces 1/R² scaling at large R for an asymptotically flat curve.

**Inputs.**
- R = np.array([5, 10, 20, 30, 50]) kpc
- v = 200 * np.ones(5) km/s

**Expected.** vorticity² = (200/R)². At R = 30: (200/30)² = 44.44 (km/s/kpc)². At R = 50: (200/50)² = 16 (km/s/kpc)².

**Tolerance.** Relative error < 1% at each R.

**Additional assertion.** vort²[i+1] / vort²[i] = (R[i] / R[i+1])² to within 1%, confirming the 1/R² scaling.

### 2.6 Test 6 — Non-uniform R-grid

**Purpose.** Verify shear² and vorticity² correctly handle log-spaced or otherwise non-uniform R-grids.

**Inputs.**
- R = np.logspace(np.log10(0.1), np.log10(50), 50) kpc (log-spaced, 50 points)
- v = 200 * (1 - np.exp(-R / 3)) km/s (rising-then-flattening exponential approach)

**Expected.** Analytic dv/dR = (200/3) * exp(-R/3); shear² is the square of this. Compare numerical shear² to analytic at every point.

**Tolerance.** Relative error < 5% at each point. (Log-grid numerical derivatives are noisier than uniform-grid; 5% is generous.)

**Additional assertion.** vort²(R) = (v(R)/R)² matches direct evaluation to < 1%.

### 2.7 Test 7 — `activity_source_3d` vertical structure and integration

**Purpose.** Verify the 3D source field has correct vertical profile and correct vertical integral.

**Inputs.**
- R_sim = np.linspace(0.5, 30, 100) kpc
- z_sim = np.linspace(0, 1.5, 30) kpc
- R_act = np.linspace(1, 25, 25) kpc
- A_act = 100 * np.ones(25) (uniform A across the active disk)
- κ_act = 1.0 (test uses unit coupling for simplicity)
- h_disk = 0.3 kpc

**Expected.**
- At R = 5 kpc, z = 0: S = 1.0 · 100 · 1 / (2 · 0.3) = 166.67 (in the unit system).
- At R = 5 kpc, z = h_disk = 0.3: S = S(z=0) · sech²(1) / 1 = 166.67 · (1 / cosh(1)²) = 166.67 · 0.4200 ≈ 70.0.
- At R = 50 kpc (outside R_act range), z = 0: S = 0 (extrapolation returns 0).
- Vertical integral at R = 5: ∫₀^{1.5} S(5, z) dz ≈ κ_act · A_act · tanh(1.5/0.3) / 2 — tanh(5) ≈ 0.99991, so the integral approaches κ_act · A_act / 2 (factor of 1/2 because z range is [0, z_max], not [-z_max, z_max]; full-range integral would be κ_act · A_act).

**Tolerance.**
- z = 0 midplane value: relative error < 1%.
- z = h_disk value: relative error < 1%.
- Outside-domain zero: absolute error < 10⁻¹⁰.
- Vertical integral: relative error < 2% (numerical-integration tolerance on coarse z-grid).

---

## 3. Two-hour implementation plan

### 3.1 Hour 0:00 — 0:10 — Setup

- Verify DM.7 (`disk_geometry.py` and tests) is fully landed: `pytest ed-lab/simulations/edsim/dm/tests/` should pass cleanly. If anything fails, halt and fix DM.7 first.
- Create empty file `ed-lab/simulations/edsim/dm/activity_source.py`.
- Add module docstring per §1.1.
- Add imports: `numpy as np`, `from scipy.interpolate import CubicSpline`.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:10 — 0:35 — `shear_squared`

- Write the function signature per §1.3.
- Compute `dv_dR = np.gradient(v, R)`.
- Optionally apply 3-point box filter if `smooth=True` (use `numpy.convolve` with `[1/3, 1/3, 1/3]` kernel; handle endpoints).
- Square.
- Add input validation (shape match, monotonic R).
- Write the docstring.
- Smoke test in REPL: pass flat curve, verify ~0; pass linear curve, verify constant.

**Checkpoint.** Function defined, smoke tests behave correctly.

### 3.3 Hour 0:35 — 0:55 — `vorticity_squared`

- Write the function signature per §1.4.
- Direct computation: `omega_sq = (v / R) ** 2` with care for R == 0.
- Implement R = 0 regularization: detect R[i] == 0, compute forward-difference dv/dR there, replace.
- Add input validation.
- Write the docstring.
- Smoke test: solid-body rotation v = 10R returns 100 everywhere.

**Checkpoint.** Function defined, smoke test passes including R=0 case.

### 3.4 Hour 0:55 — 1:15 — `activity_index`

- Write the function signature per §1.5.
- Validate α ∈ [0, 1].
- Call `shear_squared(R, v, smooth=smooth)` and `vorticity_squared(R, v)`.
- Combine: `A = alpha * shear_sq + (1 - alpha) * vort_sq`.
- Write the docstring.
- Smoke test: verify α=0 gives pure vorticity, α=1 gives pure shear, α=0.5 gives the average.

**Checkpoint.** Function defined, three α values give expected mixtures.

### 3.5 Hour 1:15 — 1:50 — `activity_source_3d`

- Write the function signature per §1.6.
- Construct cubic spline: `spline = CubicSpline(R_act, A_act, bc_type='natural', extrapolate=False)`.
- Evaluate on R_sim: `A_interp = spline(R_sim)`. Replace NaN with 0: `A_interp = np.nan_to_num(A_interp, nan=0.0)`.
- Build 2D source: `S = kappa_act * A_interp[:, None] * (1 / (np.cosh(z_sim / h_disk)**2 * 2 * h_disk))[None, :]`.
- Add input validation.
- Write the docstring.
- Smoke test: uniform A_act of 100, query at R_sim = 5 kpc, z = 0, h_disk = 0.3, κ_act = 1; expect S ≈ 166.67.

**Checkpoint.** Function defined, smoke test gives expected midplane value.

### 3.6 Hour 1:50 — 2:00 — Buffer / cleanup

- Re-read each function's docstring for completeness.
- Ensure no `print` debug statements remain.
- Verify imports are minimal (only what's used).

End of two-hour implementation block. Stop, take a break, then move to testing.

---

## 4. Hours 2–3 — Tests and debugging

### 4.1 Hour 2:00 — 2:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_activity_source.py`.
- Write the seven tests per §2.1–§2.7.
- For Test 7, compute the expected values by hand or in a REPL before writing the test.

### 4.2 Hour 2:30 — 3:00 — Run and debug

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_activity_source.py -v`.
- Most likely failures:
  - **Test 1 (flat shear):** `np.gradient` may return very small but non-zero values (~1e-14). Tolerance < 10⁻⁶ accommodates this; if it fails, the issue is more severe and worth diagnosing.
  - **Test 4 (R=0 regularization):** off-by-one indexing in the forward-difference. Common bug; fix the indexing.
  - **Test 7 (activity_source_3d):** cubic-spline extrapolation behavior. If the test fails because outside-domain returns non-zero, verify the `extrapolate=False` flag and `np.nan_to_num` step are both applied.
- Debug each failure individually. Do not modify the spec; modify the implementation.

### 4.3 Hour 3:00 — 3:30 — Documentation, lint, commit

- Verify all four functions have complete docstrings.
- Run lint if configured.
- Run `python -c "from ed_lab.simulations.edsim.dm import activity_source"` (path adjusted to repo layout) and verify no warnings.
- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 2 complete. activity_source.py implemented; 7/7 tests pass.`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/activity_source.py
  git add ed-lab/simulations/edsim/dm/tests/test_activity_source.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add activity_source.py and tests — DM Step 2 complete"
  git push
  ```

---

## 5. Session-complete checklist

The session is complete if and only if all of the following are true:

- [ ] `ed-lab/simulations/edsim/dm/activity_source.py` exists with four functions implemented.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_activity_source.py` exists with seven tests.
- [ ] All seven tests pass under `pytest`.
- [ ] All four functions have complete docstrings (Args, Returns, References).
- [ ] The module imports cleanly with no warnings.
- [ ] No TODO comments remain except those explicitly deferred (smoothing optimization, environmental coupling — neither in scope for Session 2).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to `ed-lab/arcs/arc-DM/run_log.md`.
- [ ] Commit landed with message `Add activity_source.py and tests — DM Step 2 complete`.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not move to Step 3 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 2 and must not be attempted:

- `pde_solver.py`, `boundary_conditions.py`, or any other module beyond `activity_source.py`.
- Loading actual SPARC data. SPARC ingestion is Session 1.5 (parallel-track, optional, can happen any time before Session 6).
- The validation suite or any actual PDE solving.
- Vectorization or caching of the `CubicSpline` evaluation across galaxies. Premature optimization; profile first.
- A self-consistent activity-source loop (Tier 3 of DM.4 §3). That requires the full pipeline.
- Environmental-coupling extensions (DM.6 partial-universality branch).
- Smoothing-kernel tuning beyond the simple 3-point box filter.

If during the session a tempting deviation surfaces, record it in a TODO comment and move on.

---

## 7. Risk inventory for Session 2

Three things most likely to consume more time than expected:

1. **`numpy.gradient` non-uniform-grid behavior.** `np.gradient(v, R)` correctly handles non-uniform R if R is passed as the second argument. If the analyst passes a scalar dx instead, the function silently uses uniform spacing and Test 6 will fail. Expected resolution: 5–10 minutes if it bites.

2. **`CubicSpline` extrapolation.** The default `extrapolate=True` returns interpolated values outside the data range, which is wrong for activity-source (no activity outside the observed disk). The fix is `extrapolate=False` plus `np.nan_to_num`. Expected resolution: 5 minutes.

3. **R = 0 regularization indexing.** The forward-difference computation requires `R[1] - R[0]` and `v[1] - v[0]`. An off-by-one or wrong-direction-of-difference is the most common bug. Test 4 catches it. Expected resolution: 10–15 minutes.

If the session runs long, do not skip writing tests or commit. The completion checklist is the gate.

---

## 8. Cross-checks against DM.1 and DM.4

The implementation must respect three structural constraints established earlier in the arc:

1. **A(R) ∝ 1/R² for asymptotically flat curves** (DM.1 §3.1). Test 5 confirms this for the vorticity contribution. The shear contribution for a perfectly flat curve is zero; in real galaxies it is nonzero but typically smaller than vorticity at outer radii.

2. **Universal α across the SPARC sample** (DM.4 §1). The function accepts α as input but is silent on its value. Fitting is downstream (`fit_activity_parameters.py`, Step 7).

3. **Source units consistent with the PDE** (DM.0 §3 dimensional analysis). The function does not enforce dimensional consistency; it returns S in units that are [κ_act] × (km/s/kpc)² × (1/kpc). Whatever units κ_act has chosen, S inherits. The PDE solver consumes whatever this returns; consistency is a system-level invariant maintained by the κ_act fit.

---

## End-of-turn summary

**What got done this turn:** the Session 2 coding plan is fully scoped. Every function signature, unit convention, validation rule, edge case, and regularization strategy is specified. Seven tests have explicit inputs, expected outputs, and tolerances. The two-hour implementation plan and one-hour test/commit block are sequenced. Anti-scope-creep guardrails name what is forbidden in the session. The session-complete checklist gates progress to Step 3.

**What did not get done:** no Python code has been written. The DM.8 memo is a session plan, not the session itself. The plan presupposes a future coding session in which the analyst executes per these specifications.

**What this means for the program:** the arc has continued past `disk_geometry.py` to `activity_source.py`. After Session 2, two of eight modules will be complete. Step 3 (`pde_solver.py`) — the physics core — is the next dependency.

**Decision after this session:** Step 3 (`pde_solver.py`) per DM.3 §1.1.1, scoped in DM.9 (a future coding-session-3 plan) when Session 2 lands.

---

## Recommended Next Step

After confirming DM.7 Session 1 is fully landed (the §5 checklist of DM.7 satisfied), begin DM.8 Session 2: in `ed-lab/simulations/edsim/dm/`, create `activity_source.py` and `tests/test_activity_source.py`, then implement the four functions in the order specified in DM.8 §3.2–§3.5 (`shear_squared` → `vorticity_squared` → `activity_index` → `activity_source_3d`), following the unit conventions in §1.2 and the validation rules in each subsection. Stop and run the test suite per §4.2 only after all four functions are implemented; do not attempt Step 3 until the §5 session-complete checklist is fully satisfied.
