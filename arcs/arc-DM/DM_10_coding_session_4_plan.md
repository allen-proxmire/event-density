# DM.10 — Coding Session 4 Plan: `boundary_conditions.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — eleventh memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 4 and followed without further design decisions.
**Predecessor:** DM.9 (Session 3 plan — `pde_solver.py`).
**Target file:** `ed-lab/simulations/edsim/dm/boundary_conditions.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py`
**Session goal:** Step 4 of the DM.4 implementation sequence complete. After this session, Step 5 (`validation_tests.py`) is unblocked.

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Prerequisite:** DM.7, DM.8, and DM.9 must be fully landed before starting Session 4. The boundary-conditions module factors out logic that DM.9 implemented inline; without DM.9 in place, there is nothing to factor.

**Note on session character.** Session 4 is partly a refactor: the boundary-condition logic that DM.9 placed inline in `pde_solver.py` is extracted into a reusable module. The session also adds two new modes (outer-R Neumann fallback for debugging; explicit far-z Dirichlet utility) that did not exist in DM.9. After Session 4, `pde_solver.py` is refactored to delegate to the new module.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("Boundary-condition modes and applications for the screened-Poisson solver"), an authorship line, and references to DM.3 §1.1.4 (public API), DM.4 §2.4 (BC specifications), and DM.9 §1.9 (where the BCs first appeared inline).

Imports: `numpy as np`, `from dataclasses import dataclass, field`, `from typing import Literal, Callable, Optional`. Import `CylindricalGrid` and `yukawa_green` from `pde_solver`:

> `from .pde_solver import CylindricalGrid, yukawa_green`

This creates a one-way dependency: `boundary_conditions` imports from `pde_solver`, not vice versa. The refactor at the end of the session inverts the dependency: `pde_solver` will import from `boundary_conditions`. To avoid a circular import, move `CylindricalGrid` and `yukawa_green` either to a new `_grid.py` or accept that `pde_solver` becomes the upstream module for both (preferred: keep `CylindricalGrid` in `pde_solver`, do not import it back into `pde_solver` from `boundary_conditions`; instead, `pde_solver`'s `solve` method takes a BC-config object as input).

### 1.2 Unit conventions

**Inherited from DM.7 §1.2, DM.8 §1.2, and DM.9 §1.2 — not renegotiated.**

- Lengths: kpc.
- D_T: kpc²/Gyr (galactic-natural units).
- λ: 1/Gyr.
- L: kpc.
- T: solver-internal units (whatever `pde_solver` returns).
- Source: solver-internal units (whatever `activity_source_3d` returns).

The BC module performs no unit conversions; it consumes whatever the solver and source produce.

### 1.3 Dataclass — `BoundaryConditions`

**Definition.** Frozen dataclass with four string fields naming the BC mode at each side of the grid.

`@dataclass(frozen=True)`
- `inner_R: Literal["neumann_zero", "pole_regularized"] = "pole_regularized"` — at R = R_min (or R = 0 if axis is on-grid). Default: `pole_regularized` for grids with R[0] = 0; `neumann_zero` for grids with R[0] > 0 (use `pole_regularized` for both as it reduces to Neumann when R[0] > 0).
- `outer_R: Literal["yukawa_far", "neumann_zero", "dirichlet_zero"] = "yukawa_far"` — at R = R_max. Default: `yukawa_far` (the production choice). `neumann_zero` is a debugging fallback; `dirichlet_zero` is for testing isolated configurations.
- `inner_z: Literal["neumann_zero"] = "neumann_zero"` — at z = 0. Mid-plane symmetry by ghost-cell mirror. Only one mode supported.
- `outer_z: Literal["dirichlet_zero", "neumann_zero"] = "dirichlet_zero"` — at z = z_max. Default: `dirichlet_zero`.

**Validation.** `__post_init__` checks string values against the Literal options; raises `ValueError` with allowed-values list on bad input.

**Method 1.** `is_dirichlet_outer_R(self) -> bool` — returns True if `outer_R == "yukawa_far"` or `outer_R == "dirichlet_zero"`.

**Method 2.** `is_dirichlet_outer_z(self) -> bool` — returns True if `outer_z == "dirichlet_zero"`.

**Docstring.** State that this is a configuration object naming BC modes; actual application is done by module-level functions.

### 1.4 Function — `compute_outer_R_dirichlet`

**Signature.**
`compute_outer_R_dirichlet(bc: BoundaryConditions, grid: CylindricalGrid, source: np.ndarray, D_T: float, L: float) -> np.ndarray`

**Behavior.** Returns a 1-D array of length `grid.n_z` giving the Dirichlet T values at R = R_max for each z[j].

For `bc.outer_R == "yukawa_far"`:
- Compute `source_total = ∫∫ source(R, z) · 2π R · dR · dz` via trapezoidal integration on the grid.
- For each j, compute r_j = √(R[n_R-1]² + z[j]²).
- Return T[n_R-1, j] = `yukawa_green(r_j, L, D_T, source_total)`.

For `bc.outer_R == "dirichlet_zero"`:
- Return zeros of length n_z.

For `bc.outer_R == "neumann_zero"`:
- Raise `NotImplementedError`. Neumann at outer R requires stencil modification, not value enforcement; the function returns nothing and the caller (solver) handles it via `modify_stencil_outer_R` instead.

**Validation.** Source shape must match (n_R, n_z). D_T > 0, L > 0.

**Docstring.** State that this returns Dirichlet values for outer-R BC; that Neumann mode raises and is handled separately; reference to `yukawa_green` and DM.0 §3.

### 1.5 Function — `compute_outer_z_dirichlet`

**Signature.**
`compute_outer_z_dirichlet(bc: BoundaryConditions, grid: CylindricalGrid) -> np.ndarray`

**Behavior.** Returns a 1-D array of length `grid.n_R` giving the Dirichlet T values at z = z_max for each R[i].

For `bc.outer_z == "dirichlet_zero"`:
- Return zeros of length n_R.

For `bc.outer_z == "neumann_zero"`:
- Raise `NotImplementedError` (handled via stencil modification).

**Docstring.** Same structure as §1.4.

### 1.6 Function — `apply_dirichlet`

**Signature.**
`apply_dirichlet(T: np.ndarray, bc: BoundaryConditions, dirichlet_R: np.ndarray, dirichlet_z: np.ndarray) -> np.ndarray`

**Behavior.** Modifies T in place to enforce Dirichlet boundary values at the outer R and outer z faces.

- If `bc.is_dirichlet_outer_R()`: T[n_R-1, :] = dirichlet_R.
- If `bc.is_dirichlet_outer_z()`: T[:, n_z-1] = dirichlet_z.

The four corner values are set by either path (the order does not matter as long as both are applied).

**Returns.** The modified T array (also modified in place; return is for chainability).

**Validation.** T shape must match (n_R, n_z). dirichlet_R length n_z, dirichlet_z length n_R.

**Docstring.** State that this enforces Dirichlet values; called once at solve setup and after each sweep (to be safe). Neumann boundaries are not touched here.

### 1.7 Function — `modify_stencil_for_neumann`

**Signature.**
`modify_stencil_for_neumann(stencil: dict, bc: BoundaryConditions, grid: CylindricalGrid, L: float) -> dict`

**Behavior.** Takes a dict containing the precomputed stencil coefficient arrays (a_E, a_W, a_N, a_S, a_C) from `pde_solver` and modifies them in-place to enforce Neumann BCs via ghost-cell mirroring at the appropriate sides.

For `bc.inner_R == "pole_regularized"` and grid.R[0] == 0:
- Apply pole regularization per DM.9 §1.7: a_E[0, :] = 4 / dR_forward(0)²; a_W[0, :] = 0; a_C[0, :] adjusted.

For `bc.inner_R == "pole_regularized"` and grid.R[0] > 0:
- Apply Neumann mirror: a_W[0, :] = 0; a_E[0, :] doubled (from mirror); a_C[0, :] adjusted.

For `bc.inner_z == "neumann_zero"` (always, the only supported mode):
- At j = 0: a_S[:, 0] = 0; a_N[:, 0] doubled (from mirror); a_C[:, 0] adjusted to a_E + a_W + 2·(1/dz²) + 1/L².

For `bc.outer_R == "neumann_zero"` (debugging fallback):
- At i = n_R - 1: a_E[n_R-1, :] = 0; a_W[n_R-1, :] doubled; a_C[n_R-1, :] adjusted.

For `bc.outer_z == "neumann_zero"` (alternative outer-z mode):
- At j = n_z - 1: a_N[:, n_z-1] = 0; a_S[:, n_z-1] doubled; a_C[:, n_z-1] adjusted.

**Returns.** The modified stencil dict.

**Validation.** Stencil must contain keys `a_E`, `a_W`, `a_N`, `a_S`, `a_C`, each of shape (n_R, n_z).

**Docstring.** State that this modifies the stencil for Neumann mirror conditions; called once at solver setup; references DM.9 §1.7 and §1.8.

### 1.8 Function — `apply_all_boundaries`

**Signature.**
`apply_all_boundaries(T: np.ndarray, bc: BoundaryConditions, grid: CylindricalGrid, source: np.ndarray, D_T: float, L: float) -> dict`

**Behavior.** Convenience wrapper that:
- Calls `compute_outer_R_dirichlet` to get the R-side Dirichlet values.
- Calls `compute_outer_z_dirichlet` to get the z-side Dirichlet values.
- Calls `apply_dirichlet` to set them on T.
- Returns a dict with keys `dirichlet_R` (the array for outer R), `dirichlet_z` (the array for outer z), and `T` (the modified field).

**Returns.** Dict for diagnosis; T is also modified in place.

**Use case.** Called once at solver setup. After each SOR sweep, only `apply_dirichlet` needs to be re-called using the cached dirichlet_R and dirichlet_z arrays (since they don't change unless the source changes).

**Docstring.** State this is the high-level entry point that ties Dirichlet computation and application together.

### 1.9 Refactor of `pde_solver.py`

After implementing the boundary_conditions module, refactor `pde_solver.py`:

- `ScreenedPoissonSolver.__init__` now accepts `bc: BoundaryConditions = None`. If None, default to `BoundaryConditions()` (which gives the production defaults).
- `ScreenedPoissonSolver.solve` now calls `apply_all_boundaries(T, self.bc, self.grid, source, self.D_T, self.L)` at the start to compute and apply Dirichlet values.
- Stencil construction (also at __init__) calls `modify_stencil_for_neumann(stencil, self.bc, self.grid, self.L)` to apply Neumann modifications.
- The Dirichlet rows (last R column, last z row) are skipped in the SOR sweep (they're fixed values).

This refactor is mechanical given §1.6 and §1.7. Most of DM.9's inline BC logic is deleted and replaced with delegation to `boundary_conditions` functions.

**Test compatibility.** After the refactor, all six DM.9 `test_pde_solver.py` tests must still pass. The refactor changes implementation but not behavior.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py`. Use `pytest`, plain assertions, `pytest.approx`.

Six tests, each isolating one BC behavior.

### 2.1 Test 1 — Yukawa Dirichlet for synthetic point source

**Purpose.** Verify `compute_outer_R_dirichlet` returns the correct Yukawa values at R = R_max.

**Inputs.**
- Grid: R = np.linspace(0.1, 100, 50) kpc, z = np.linspace(0, 10, 11) kpc.
- Source: a delta-like Gaussian at origin; M_test = 1.0 in solver units.
- bc: BoundaryConditions(outer_R="yukawa_far").
- D_T = 1.0, L = 50.0 (so screening matters at R_max = 100).

**Expected.** For each j, the returned dirichlet_R[j] should equal yukawa_green(r_j, L, D_T, source_total) where r_j = √(100² + z[j]²) and source_total ≈ 1.0 (the integral of the Gaussian).

**Tolerance.** Relative error < 0.5% per j, after accounting for the trapezoidal integration of source_total (which has its own integration error).

### 2.2 Test 2 — Mid-plane Neumann via ghost-cell mirror

**Purpose.** Verify that `modify_stencil_for_neumann` correctly modifies the j=0 row to enforce ∂T/∂z = 0.

**Inputs.**
- Grid: simple uniform R-grid R = np.linspace(0.5, 10, 20), z = np.linspace(0, 5, 11).
- bc: BoundaryConditions() with default inner_z = "neumann_zero".
- A pre-built stencil dict with a_E, a_W, a_N, a_S, a_C all = 1 (placeholder values).

**Expected.** After `modify_stencil_for_neumann`:
- a_S[:, 0] == 0 (south side absorbed into ghost mirror).
- a_N[:, 0] == 2 * (1/dz²) where dz = z[1] - z[0] = 0.5. So a_N[:, 0] should be exactly 2 / 0.25 = 8.0 if the stencil convention is per DM.9 §1.10.

Note: this test is sensitive to exactly how a_N was originally computed. The placeholder a_N = 1 above is a stand-in; in practice, the stencil's a_N for uniform z would be 1/dz². The check is that the modification correctly doubles whatever value was there at j=0.

**Tolerance.** Exact equality (no floating-point arithmetic involved in the modification — just multiplication by 2 and zeroing).

### 2.3 Test 3 — Far-z Dirichlet T = 0

**Purpose.** Verify `compute_outer_z_dirichlet` returns zeros for the default mode.

**Inputs.**
- Grid: any with n_R = 30.
- bc: BoundaryConditions() with default outer_z = "dirichlet_zero".

**Expected.** Returned array of length 30, all zeros.

**Tolerance.** Exact equality.

**Additional assertion.** With outer_z = "neumann_zero", the function raises NotImplementedError.

### 2.4 Test 4 — Interaction with CylindricalGrid

**Purpose.** Verify `apply_all_boundaries` correctly integrates with a real grid and source.

**Inputs.**
- Grid: production-spec subset (R log-spaced [0.5, 30] kpc with 50 cells; z linear [0, 1.5] kpc with 30 cells).
- Source: thin-disk Gaussian peaked at R = 3 kpc, z = 0; total integrated source = 1.0.
- bc: BoundaryConditions() defaults.
- D_T, L at production values (D_T from §1.2 default, L = 1000 kpc).
- Initial T = zeros.

**Expected.**
- After `apply_all_boundaries`, T has nonzero values along the i = n_R-1 column and zeros along the j = n_z-1 row (both as per BC).
- The values along i = n_R-1 are the Yukawa-far prediction; specifically, for R_max = 30 kpc and L = 1000 kpc, exp(-30/1000) ≈ 0.97, so the values should be close to (1 / (4π D_T r)) × 0.97 with r ≈ 30 kpc.
- T[i, n_z-1] = 0 for all i.

**Tolerance.** Relative error < 1% on the outer R column; exact zeros on the outer z row.

### 2.5 Test 5 — Stability under grid refinement

**Purpose.** Verify Dirichlet BC values converge as the R-grid is refined (i.e., source_total integration error decreases).

**Inputs.** Same source and BCs as Test 4, on three grid resolutions:
- Coarse: 25 R cells × 15 z cells.
- Medium: 50 R cells × 30 z cells.
- Fine: 100 R cells × 60 z cells.

**Expected.** The source_total integrals are coarse_total, medium_total, fine_total. Each should converge toward the analytic value (1.0 for a normalized Gaussian source).

**Tolerance.**
- |coarse_total - 1.0| > |medium_total - 1.0| > |fine_total - 1.0|.
- |fine_total - 1.0| / |coarse_total - 1.0| < 0.3 (factor of 3+ improvement).

### 2.6 Test 6 — Apply to known analytic solution

**Purpose.** Verify that applying BCs to a field that already satisfies them is a no-op.

**Inputs.**
- Grid: R = np.linspace(0.5, 100, 50), z = np.linspace(0, 10, 11).
- D_T = 1.0, L = 50.0.
- Source: zero everywhere except a small region at origin (a "synthetic point source" with normalized total = 1.0).
- Initial T: the analytic Yukawa T(R, z) = exp(-r/L) / (4π D_T r), with r = √(R² + z²). Set this on the entire grid.
- bc: BoundaryConditions() defaults.

**Expected.** After `apply_dirichlet`, the values at i = n_R-1 should equal what was already there (the analytic Yukawa at R_max), and the values at j = n_z-1 should be set to zero.

The analytic Yukawa at z = z_max = 10 kpc, R = 100 kpc gives r ≈ 100.5 kpc, so T ≈ exp(-2.01) / (4π × 1 × 100.5) ≈ 0.1342 / 1263 ≈ 1.06 × 10⁻⁴ — nonzero! The Dirichlet zero at z_max thus *changes* the field there.

This is intended behavior: the framework's BC at z_max = 10 kpc is approximately wrong for a Yukawa with L = 50 kpc, since z_max / L = 0.2 — the field hasn't decayed by z_max. In production, z_max ~ 5 h_disk = 1.5 kpc, much smaller than L = 1000 kpc, so the field is essentially zero at z_max anyway.

**Tolerance.**
- The Yukawa-far values at i = n_R-1 should equal the pre-existing analytic Yukawa values (within trapezoidal-integration error of the source_total — well below 1% for a normalized source).
- T[:, n_z-1] is set to exact zeros, regardless of what was there before.

---

## 3. Two-hour implementation plan

### 3.1 Hour 0:00 — 0:10 — Setup

- Verify DM.7, DM.8, DM.9 are landed: `pytest ed-lab/simulations/edsim/dm/tests/` passes cleanly.
- Create empty file `ed-lab/simulations/edsim/dm/boundary_conditions.py`.
- Add module docstring per §1.1.
- Add imports.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:10 — 0:25 — `BoundaryConditions` dataclass

- Define the frozen dataclass per §1.3.
- Implement validation in `__post_init__`.
- Implement `is_dirichlet_outer_R` and `is_dirichlet_outer_z` methods.
- Smoke test: construct with defaults, with each non-default option, verify validation catches bad strings.

**Checkpoint.** Dataclass instantiates and validates correctly.

### 3.3 Hour 0:25 — 0:55 — Dirichlet computation functions

- Implement `compute_outer_R_dirichlet` per §1.4. The trapezoidal source integral is the meaty part — use `numpy.trapz` or `scipy.integrate.trapezoid` over R and z, with the 2π R Jacobian factor.
- Implement `compute_outer_z_dirichlet` per §1.5 — trivial (returns zeros for the default mode).
- Smoke test: synthetic Gaussian source on a small grid, verify source_total ≈ Gaussian's known integral.

**Checkpoint.** Outer-R Dirichlet values match analytic expectation for a Gaussian source.

### 3.4 Hour 0:55 — 1:25 — `apply_dirichlet` and `apply_all_boundaries`

- Implement `apply_dirichlet` per §1.6.
- Implement `apply_all_boundaries` per §1.8.
- Smoke test: build a small grid, source, BC; call `apply_all_boundaries`; verify T has correct values at outer-R column and outer-z row.

**Checkpoint.** Dirichlet application works end-to-end.

### 3.5 Hour 1:25 — 1:55 — `modify_stencil_for_neumann`

- Implement per §1.7.
- Handle each of the four sides (inner_R, inner_z, outer_R debug, outer_z alt) with the appropriate stencil modifications.
- Smoke test: build a placeholder stencil dict with a_E, a_W, a_N, a_S, a_C all = 1, apply default BCs; verify a_S[:, 0] = 0 and a_N[:, 0] = 2.

**Checkpoint.** Stencil modification is correct.

### 3.6 Hour 1:55 — 2:00 — Buffer / cleanup

- Re-read each function's docstring for completeness.
- Remove any debug prints.
- Run `python -c "from ed_lab.simulations.edsim.dm import boundary_conditions"` (path adjusted).

End of two-hour implementation block.

---

## 4. Hours 2–4 — Tests, refactor, debug

### 4.1 Hour 2:00 — 2:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py`.
- Write the six tests per §2.1–§2.6.

### 4.2 Hour 2:30 — 3:30 — Refactor `pde_solver.py`

This is a real refactor of the working DM.9 module. Approach with care.

- In `ScreenedPoissonSolver.__init__`, accept a `bc: BoundaryConditions = None` parameter (default to `BoundaryConditions()` if None).
- Replace inline stencil-modification code (DM.9 §1.7 and §1.8 logic) with calls to `modify_stencil_for_neumann`.
- In `ScreenedPoissonSolver.solve`, replace inline Dirichlet computation with `compute_outer_R_dirichlet` and `compute_outer_z_dirichlet` calls; replace inline value enforcement with `apply_dirichlet`.
- Verify the refactor by re-running the DM.9 test suite: `pytest ed-lab/simulations/edsim/dm/tests/test_pde_solver.py -v`. **All six DM.9 tests must still pass after the refactor.** This is the strongest sign that the refactor is correct.

If any DM.9 test fails after the refactor, halt and diagnose — the refactor introduced a behavioral change. Common issues:
- The `apply_dirichlet` is overwriting values during iteration that should remain free.
- The stencil modification has a wrong sign or factor at one of the BC sides.
- The default `BoundaryConditions()` doesn't match what DM.9 had inline (verify each default).

### 4.3 Hour 3:30 — 4:00 — Run boundary_conditions tests, debug, commit

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py -v`.
- Run `pytest ed-lab/simulations/edsim/dm/tests/` (all tests).
- Verify all DM.7, DM.8, DM.9, and DM.10 tests pass.
- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 4 complete. boundary_conditions.py implemented; pde_solver.py refactored to delegate; all tests pass (5 + 7 + 6 + 6 = 24 total).`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/boundary_conditions.py
  git add ed-lab/simulations/edsim/dm/pde_solver.py
  git add ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add boundary_conditions.py and refactor pde_solver — DM Step 4 complete"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/simulations/edsim/dm/boundary_conditions.py` exists with the dataclass and five functions per §1.3–§1.8.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_boundary_conditions.py` exists with six tests.
- [ ] `ed-lab/simulations/edsim/dm/pde_solver.py` refactored to delegate BC handling to `boundary_conditions`.
- [ ] All DM.10 tests pass.
- [ ] All DM.9 tests still pass after the refactor.
- [ ] All DM.7 and DM.8 tests still pass (sanity check that nothing leaked).
- [ ] All public dataclasses, methods, and functions have complete docstrings.
- [ ] Modules import cleanly with no warnings.
- [ ] No TODO comments remain except those explicitly deferred (red-black ordering, multigrid migration, stencil JIT).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to run log.
- [ ] Commit landed with message `Add boundary_conditions.py and refactor pde_solver — DM Step 4 complete`.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not move to Step 5 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 4:

- `validation_tests.py` (Step 5). The DM.4 §2 production-grid validation suite uses the BC module but is its own module.
- Any actual SPARC galaxy run. No SPARC data is loaded in Session 4.
- The full Tier-3 self-consistency loop. The solver is stateless; the loop lives in Step 6.
- Adding new BC modes beyond what is specified (e.g., mixed Robin BCs, periodic). The four sides have committed mode lists in §1.3; expanding them is a future-arc decision.
- Optimization of the Yukawa-far computation. Trapezoidal integration is fine; vectorized or analytic forms are premature.
- Refactoring the SOR loop itself. Only the BC handling is refactored; the inner solve algorithm is unchanged.

If during the session a tempting deviation surfaces, record it in a TODO comment and move on.

---

## 7. Risk inventory for Session 4

Three things most likely to consume more time than expected:

1. **Refactor regression in DM.9 tests.** The most likely failure mode is that the refactor breaks one of the six DM.9 tests. Diagnosis: bisect by reverting the refactor and re-running; identify which BC-handling change caused the failure. Expected resolution: 30–60 minutes if it bites.

2. **Source-total integration error.** The `compute_outer_R_dirichlet` Yukawa-far computation depends on a trapezoidal integral of the source. For coarse grids or sources with sharp features (e.g., delta-like point sources), the integral can be off by several percent, corrupting the BC values. Use `scipy.integrate.trapezoid` and verify on a known integrable source. Expected resolution: 15–30 minutes.

3. **Stencil-modification index errors.** The four sides each have specific (i, j) ranges to modify, and getting the slicing wrong (e.g., `a_S[:, 0]` vs. `a_S[0, :]`) is a classic mistake. Test 2 catches the mid-plane case directly. Expected resolution: 10–20 minutes.

If the session runs over budget, do not skip writing tests or commit. The completion checklist is the gate.

---

## 8. Cross-checks against earlier memos

The implementation must respect three structural constraints established earlier:

1. **Yukawa Green's function form** (DM.0 §3, DM.9 §1.5). The far-R BC is the Yukawa formula; verified by Test 1.

2. **Mid-plane symmetry by ghost-cell mirror** (DM.4 §2.4, DM.9 §1.8). Stencil modification doubles a_N at j=0 and zeros a_S; verified by Test 2.

3. **No-source-flux outer boundaries** (DM.4 §2.4). The default outer_z = "dirichlet_zero" and outer_R = "yukawa_far" both ensure the field is well-behaved at the truncation radii.

---

## End-of-turn summary

**What got done this turn:** the Session 4 coding plan is fully scoped. The boundary-conditions module's API is specified — a `BoundaryConditions` config dataclass plus five module-level functions for computing and applying Dirichlet values and modifying Neumann stencils. The refactor of `pde_solver.py` to delegate to this module is part of the session, with the regression test being the DM.9 test suite still passing. Six tests have explicit inputs, expected outputs, and tolerances. The two-hour implementation plan and the two-hour test/refactor/commit block are sequenced.

**What did not get done:** no Python code has been written. The DM.10 memo is a session plan, not the session itself.

**What this means for the program:** the arc has continued past `pde_solver.py` to `boundary_conditions.py` — the BC abstraction layer. After Session 4, four of eight modules will be complete. The validation gate (Step 5) is unblocked.

**Decision after this session:** Step 5 (`validation_tests.py`) per DM.3 §1.1.5, scoped in DM.11 (a future coding-session-5 plan) when Session 4 lands. Step 5 is the production validation suite that gates SPARC runs from beginning.

---

## Recommended Next Step

After confirming DM.7, DM.8, and DM.9 are all fully landed (their §5 checklists satisfied), begin DM.10 Session 4: in `ed-lab/simulations/edsim/dm/`, create `boundary_conditions.py` and `tests/test_boundary_conditions.py`, then implement the components in the order specified in DM.10 §3.2–§3.5 (`BoundaryConditions` dataclass → Dirichlet computation functions → `apply_dirichlet` and `apply_all_boundaries` → `modify_stencil_for_neumann`), following the unit conventions in §1.2 and the BC specifications in each subsection. After implementation, refactor `pde_solver.py` per §1.9 to delegate BC handling to the new module, and verify all DM.9 tests still pass. Stop and run the full test suite per §4.3 only after refactor; do not attempt Step 5 until the §5 session-complete checklist is fully satisfied.