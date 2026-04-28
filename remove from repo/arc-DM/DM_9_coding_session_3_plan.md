# DM.9 — Coding Session 3 Plan: `pde_solver.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — tenth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of Session 3 and followed without further design decisions.
**Predecessor:** DM.8 (Session 2 plan — `activity_source.py`).
**Target file:** `ed-lab/simulations/edsim/dm/pde_solver.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_pde_solver.py`
**Session goal:** Step 3 of the DM.4 implementation sequence complete. After this session, Step 4 (`boundary_conditions.py`) is unblocked.

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

**Prerequisite:** DM.7 (Session 1) and DM.8 (Session 2) must be fully landed before starting Session 3. The screened-Poisson solver depends only on the cylindrical-grid geometry, but the testing strategy uses the activity-source pipeline downstream. If either prior session is not complete, halt and finish before beginning Session 3.

**Note on scope.** Session 3 is the hardest module in the DM arc. It implements the cylindrical screened-Poisson solver — the physics core. Budget for the full 3.5–5 hours specified in DM.6 §5.1 plus a one-hour debugging buffer. This is the session most likely to discover issues in the discretization or boundary handling.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("2D axisymmetric screened-Poisson solver for the Event Density penalty-channel PDE"), an authorship line, and references to DM.0 §3 (Yukawa Green's function), DM.3 §1.1.1 (public API), DM.3 §2.1–§2.4 (numerical methods), and DM.4 §2.4 (boundary conditions).

Imports: `numpy as np`, `dataclasses.dataclass`, `typing.Optional, Callable`. No SciPy required for SOR; SciPy may be imported in test code only.

### 1.2 Unit conventions

**Inherited from DM.7 §1.2 and DM.8 §1.2 — not renegotiated.**

- Lengths: kpc.
- Temporal-tension field T: [κ_act] · (km/s/kpc)² · (1/kpc) · t_H ≈ whatever the solver returns; consumed downstream by Reading-B mapping.
- Source S: [κ_act] · (km/s/kpc)² / kpc, matching `activity_source_3d` output.
- D_T: kpc² / Gyr (galactic-time-natural units; equivalent to 2.1 × 10²⁷ m²/s after conversion).
- λ: 1/Gyr (galactic-time-natural; equivalent to 1/t_H).
- L = √(D_T/λ) ≈ 1000 kpc = 1 Mpc.

The solver works in these natural galactic units throughout. Conversion to/from mks happens only at the data-input boundary (`run_single_galaxy.py`, Step 6) and at the framework-coupling boundary (`fit_activity_parameters.py`, Step 7).

**Define module constants:**
- `D_T_DEFAULT_GAL_UNITS` = (D_T value in kpc²/Gyr; analyst computes from 2.1 × 10²⁷ m²/s).
- `LAMBDA_DEFAULT_GAL_UNITS` = (1/13.8 Gyr⁻¹ = 0.0725 Gyr⁻¹).
- `L_DEFAULT_KPC` = √(D_T_DEFAULT / LAMBDA_DEFAULT) ≈ 1000.

These are defaults; the solver accepts D_T, λ as constructor inputs and does not assume defaults.

### 1.3 Class — `CylindricalGrid`

**Definition.** Frozen dataclass with three fields:

`@dataclass(frozen=True)`
- `R: np.ndarray` — 1-D array of cell-center R values in kpc, monotonically strictly increasing, R[0] >= 0.
- `z: np.ndarray` — 1-D array of cell-center z values in kpc, monotonically strictly increasing, z[0] >= 0 (mid-plane symmetry assumed; the solver computes only the upper half).
- `validate(self)` method called in `__post_init__` to enforce monotonicity and non-negativity.

**Derived properties (computed on demand):**
- `dR_forward(self, i)` → R[i+1] - R[i] (returns full array if no i passed).
- `dR_backward(self, i)` → R[i] - R[i-1].
- `dR_avg(self, i)` → (dR_forward + dR_backward) / 2.
- `R_face_plus(self, i)` → (R[i] + R[i+1]) / 2.
- `R_face_minus(self, i)` → (R[i-1] + R[i]) / 2.
- `dz` → uniform z-spacing (validated to be uniform; raise if not).
- `n_R` → len(R), `n_z` → len(z).

**Note.** z-grid is required to be uniform for simplicity. R-grid is non-uniform (log-linear hybrid for production).

### 1.4 Class — `ScreenedPoissonSolver`

**Constructor signature.**
`ScreenedPoissonSolver(grid: CylindricalGrid, D_T: float, lam: float, omega: float = 1.7)`

**State.**
- Grid (stored).
- D_T, λ stored.
- L = √(D_T/λ) computed and stored.
- ω relaxation parameter (default 1.7, configurable).
- Pre-computed stencil coefficients per (i, j) — cached on construction since they depend only on the grid and (D_T, λ), not on the source.

**Public method 1.** `solve(source, bc_far_R, tol=1e-6, max_iter=5000, verbose=False) -> dict`

**Inputs.**
- `source: np.ndarray` of shape (n_R, n_z) — the source S(R, z) on the grid, in source units (DM.8).
- `bc_far_R: Callable[[float, float], float] | np.ndarray` — either a function returning T(R_max, z) for any z, or a precomputed 1-D array of length n_z giving Dirichlet values at R_max. The Yukawa-far BC computes this from the source's total integral.
- `tol`: convergence tolerance on max relative change between iterations.
- `max_iter`: maximum iterations.
- `verbose`: if True, print residual every 100 iterations.

**Output.** Dictionary with:
- `T`: np.ndarray of shape (n_R, n_z), the converged temporal-tension field.
- `iterations`: int, number of iterations to converge.
- `final_residual`: float, max relative change at the last iteration.
- `converged`: bool, True if final_residual < tol within max_iter.

**Side effect on non-convergence.** If `converged` is False, the solver returns the partial result with the boolean flag rather than raising. The caller (Step 6, `run_single_galaxy.py`) decides how to handle non-convergence. This keeps the solver pure.

**Public method 2.** `apply_laplacian(T) -> np.ndarray`

**Behavior.** Returns the discrete cylindrical Laplacian ∇²T on the grid for an arbitrary T field. Used in tests and validation; not used internally by `solve`. Dimension: 1/kpc² applied to T.

### 1.5 Module-level function — `yukawa_green`

**Signature.** `yukawa_green(r: np.ndarray | float, L: float, D_T: float, source_total: float = 1.0) -> np.ndarray | float`

**Behavior.** Returns G(r) = source_total · exp(−r/L) / (4π D_T r). Used by `solve()` to construct the Yukawa-far BC and by validation Test 1.

**Validation.** r > 0; raise on r == 0 or r < 0.

### 1.6 Numerical method — discrete cylindrical Laplacian on non-uniform R

The PDE is ∇²T − T/L² = −S/D_T. The discrete operator at interior point (i, j) — with i indexing R and j indexing z — is:

> [a_E T(i+1, j) + a_W T(i−1, j) + a_N T(i, j+1) + a_S T(i, j−1) − a_C T(i, j)] = −S(i, j) / D_T

where:

- a_E = R_{i+1/2} / (R_i · dR_avg(i) · dR_forward(i))
- a_W = R_{i−1/2} / (R_i · dR_avg(i) · dR_backward(i))
- a_N = 1 / dz²
- a_S = 1 / dz²
- a_C = a_E + a_W + a_N + a_S + 1/L²

**This is the conservative discretization.** It preserves the divergence form of the cylindrical Laplacian on a non-uniform grid. Reference: Patankar (1980) §4.6 for the conservative finite-volume derivation.

### 1.7 Pole regularization at R = 0

If R[0] = 0 (the axis is on-grid), the (1/R) ∂_R(R ∂_R T) term is singular. Apply L'Hôpital:

> lim_{R→0} (1/R) ∂_R(R ∂_R T) = 2 ∂²T/∂R² |_{R=0}

Using a mirror condition (∂T/∂R|_0 = 0 by axisymmetry), the discrete form at i=0 is:

> a_E_pole · T(1, j) − a_C_pole · T(0, j) + a_N · T(0, j+1) + a_S · T(0, j−1) = −S(0, j) / D_T

where:

- a_E_pole = 4 / dR_forward(0)²
- a_W_pole = 0 (mirror suppresses W contribution)
- a_C_pole = a_E_pole + a_N + a_S + 1/L²

**Note.** If R[0] > 0 (axis not on grid; the production R-grid starts at R = 0.01 kpc per DM.4 §5.1), pole regularization is not needed because R[0] is small but nonzero. The standard interior stencil applies. Always validate which case is in effect.

### 1.8 Mid-plane symmetry at z = 0

The grid stores only z ≥ 0 (DM.4 §5.1). At j = 0, apply Neumann BC ∂T/∂z |_0 = 0 via ghost-cell mirror: T(i, j=−1) ≡ T(i, j=1). This modifies the j=0 stencil:

> a_N at j=0 = 2 / dz²
> a_S at j=0 = 0 (mirror absorbed into a_N)

The interior stencil is unchanged for j > 0.

### 1.9 Boundary conditions

**Inner R = 0 (or R_min):** handled by pole regularization (§1.7) or by the standard interior stencil if R_min > 0.

**Outer R = R_max:** Dirichlet from the Yukawa-far form. Before iteration begins, compute:

> source_total = ∫∫ source(R, z) · 2π R · dR · dz over the grid (numerical integration via trapezoidal rule).

For each j, set:

> T(n_R − 1, j) = source_total · exp(−r_{n_R−1, j} / L) / (4π · D_T · r_{n_R−1, j}),

where r_{n_R−1, j} = √(R[n_R−1]² + z[j]²). This row is fixed throughout iteration.

**Inner z = 0:** ghost-cell mirror (§1.8); not a fixed row.

**Outer z = z_max:** Dirichlet T = 0. The j = n_z − 1 row is fixed throughout iteration.

### 1.10 SOR update rule

For each interior point (i, j) (excluding fixed-row boundaries):

> T_new(i, j) = [a_E T(i+1, j) + a_W T(i−1, j) + a_N T(i, j+1) + a_S T(i, j−1) + S(i, j) / D_T] / a_C
>
> T(i, j) ← (1 − ω) T(i, j) + ω · T_new(i, j)

Use Gauss-Seidel ordering: update in place, with later cells in the sweep using already-updated earlier cells.

**Sweep order.** Iterate over (i, j) in row-major order: outer loop over i = 0 to n_R − 1, inner loop over j = 0 to n_z − 1. At i = 0, use pole-regularized stencil. At j = 0, use mirror-modified stencil. Skip (n_R − 1, *) and (*, n_z − 1) — those are Dirichlet-fixed.

**Optional red-black ordering.** For better parallelism and faster convergence, color cells red/black by (i + j) % 2 and update reds in one pass, blacks in another. For Session 3, simple row-major is acceptable; red-black is a follow-up optimization.

### 1.11 Convergence criterion

After each full sweep, compute:

> max_change = max |T_new(i, j) − T_old(i, j)| / max(|T_new(i, j)|, ε)

over all interior cells, where ε = 10⁻¹² (avoid division by zero where T is near zero).

Convergence: max_change < tol (default 10⁻⁶).

If max_iter reached without convergence, return with `converged=False` and the partial T.

### 1.12 Outer-loop self-consistency hooks

Session 3 implements only the inner SOR solve. The Tier-3 self-consistency loop (DM.4 §3.2) — where the activity-source A is recomputed from v_pred(R) and the PDE is re-solved — lives in `run_single_galaxy.py` (Step 6). The solver's API is designed to support this without modification: each `solve()` call is independent, takes a fresh source, and returns a fresh T. The outer loop in Step 6 calls `solve()` repeatedly with updated source until the v_pred fixed point is reached.

**No outer-loop code is written in Session 3.** The hooks exist by virtue of the API being functional and stateless across `solve()` calls.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_pde_solver.py`. Use `pytest` conventions, `pytest.approx`, and `numpy.testing.assert_allclose`.

Six tests, each isolating one structural property.

### 2.1 Test 1 — Laplacian operator on analytic function

**Purpose.** Verify `apply_laplacian` returns the correct ∇²T for a function whose Laplacian is known analytically.

**Inputs.**
- Grid: R = np.linspace(0.5, 10, 50) kpc (uniform, simple), z = np.linspace(0, 5, 25) kpc.
- Test function: T(R, z) = R² + z².
- Analytic ∇²T = (1/R) ∂_R(R · 2R) + ∂²_z(z²) = (1/R)(4R) + 2 = 4 + 2 = 6.

**Expected.** Discrete ∇²T ≈ 6 at every interior point.

**Tolerance.** Relative error < 5% at interior points (excluding outer 2 cells in R and z to avoid boundary artifacts).

### 2.2 Test 2 — SOR convergence on Newtonian Poisson (point source)

**Purpose.** Verify SOR converges to the correct Newtonian (un-screened) potential when the screening term is turned off.

**Inputs.**
- Grid: R = np.linspace(0.1, 200, 100) kpc, z = np.linspace(0, 50, 25) kpc.
- D_T = 1.0 (arbitrary units; what matters is dimensional consistency).
- λ = 1e-30 (effectively zero — pure Poisson limit; L → ∞).
- Source: regularized point source at origin, S(R, z) = M_test · exp(−r²/2σ²) / ((2π)^(3/2) σ³) with σ = 0.5 kpc, M_test = 1.0.
- Yukawa-far BC computed with L = √(D_T/λ); for the very small λ, L is enormous and the BC is effectively the Newtonian 1/(4π D_T r) at R_max.

**Expected.** Converged T(r) ≈ 1/(4π D_T r) for r > 5 kpc (well outside the Gaussian source).

**Tolerance.**
- max relative error < 5% over r ∈ [10 kpc, 100 kpc].
- iterations < 10000.

### 2.3 Test 3 — Yukawa boundary condition correctness

**Purpose.** Verify that the Yukawa-far Dirichlet BC produces the correct asymptotic field at R_max.

**Inputs.**
- Grid: R = np.linspace(0.5, 1000, 200) kpc (extends to L = 1000 kpc), z = np.linspace(0, 50, 20) kpc.
- D_T, λ at production values: D_T = D_T_DEFAULT_GAL_UNITS, λ = LAMBDA_DEFAULT_GAL_UNITS, L = 1000 kpc.
- Source: regularized point source at origin (as Test 2), M_test = 1.0.
- Solve to convergence.

**Expected.** At every grid point on the second-to-last R column (i = n_R − 2), T value matches the analytic Yukawa T_analytic(R[n_R − 2], z) = M_test · exp(−r/L) / (4π D_T r).

**Tolerance.** Relative error < 0.5% at every (n_R − 2, j).

### 2.4 Test 4 — Stability under grid refinement

**Purpose.** Verify the solver converges under successive grid refinement (i.e., the discretization error decreases).

**Inputs.** Repeat Test 2 (Newtonian Poisson, point source) on three grids:
- Coarse: 50 R × 12 z.
- Medium: 100 R × 25 z.
- Fine: 200 R × 50 z.

**Expected.** The L_∞ norm of the difference between coarse and analytic, medium and analytic, and fine and analytic should decrease with grid refinement, approximately as O((dR)²) for the second-order stencil.

**Tolerance.**
- ε_coarse > ε_medium > ε_fine.
- ε_medium / ε_coarse ∈ [0.1, 0.5] (factor of 2–10 improvement; not strict O(dR²) due to non-uniform grid effects).
- ε_fine / ε_medium ∈ [0.1, 0.5].

### 2.5 Test 5 — Non-uniform R-grid

**Purpose.** Verify the conservative discretization handles a log-linear hybrid grid as planned for production.

**Inputs.**
- Grid: production-spec — log-spaced in [0.01 kpc, 50 kpc] with 200 cells, linear in [50 kpc, 5000 kpc] with 100 cells; z linear from 0 to 1.5 kpc with 30 cells.
- D_T, λ at production values.
- Source: thin-disk activity source mimicking a SPARC galaxy (use `activity_source_3d` from DM.8 with synthetic v(R) = 200 · (1 − exp(−R/3)) km/s on a 25-point R_act grid; κ_act = 1; h_disk = 0.3).
- Solve to convergence.

**Expected.** T(R, z) is finite, positive at z = 0 (since the source is positive), monotonically decaying away from the disk, and approximately matches the analytic Yukawa at R = 4000 kpc (well into the screened regime).

**Tolerance.**
- max iterations < 5000.
- T(R, 0) > 0 for R inside the active region, < ε for R = 4000 kpc (where source = 0 and field decayed).
- T at second-to-last R column matches Yukawa-far BC computed from the same source's total integral, within 1%.

### 2.6 Test 6 — R = 0 pole regularization

**Purpose.** Verify the solver handles a grid that includes the axis (R[0] = 0) without divergence.

**Inputs.**
- Grid: R = np.concatenate([[0.0], np.linspace(0.5, 50, 100)]) kpc — first cell on the axis.
- z = np.linspace(0, 5, 20) kpc.
- D_T, λ at production values.
- Source: smooth Gaussian centered at origin (R = 0, z = 0), σ = 1 kpc.
- Solve to convergence.

**Expected.** T(0, j) is finite for all j (no NaN, no Inf). T is approximately Yukawa-shaped, peaking at the origin and decaying outward.

**Tolerance.**
- T(0, 0) finite and positive.
- max iterations < 5000.
- T(0, j) − T(1, j) is small (axis and first off-axis cell have similar values for a regular source); specifically |T(0, 0) − T(1, 0)| / T(0, 0) < 0.05 (5% — the source is smooth at the axis so T is smooth too).

---

## 3. Two-hour implementation plan

Session 3 is the longest and hardest of the coding sessions. The "two-hour implementation plan" covers the core SOR loop and Laplacian; tests and debug come in hours 2–4.

### 3.1 Hour 0:00 — 0:15 — Setup

- Verify DM.7 and DM.8 are landed: `pytest ed-lab/simulations/edsim/dm/tests/` should pass cleanly.
- Create empty file `ed-lab/simulations/edsim/dm/pde_solver.py`.
- Add module docstring per §1.1.
- Add imports: `numpy as np`, `from dataclasses import dataclass`, `from typing import Optional, Callable`.
- Add module constants per §1.2.

**Checkpoint.** File imports cleanly.

### 3.2 Hour 0:15 — 0:35 — `CylindricalGrid` dataclass

- Define the frozen dataclass per §1.3.
- Implement validation in `__post_init__`.
- Implement derived methods (`dR_forward`, `dR_backward`, `dR_avg`, `R_face_plus`, `R_face_minus`, `dz`, `n_R`, `n_z`).
- Smoke test: construct a small grid, verify validation catches non-monotonic R, verify derived properties give correct values.

**Checkpoint.** Grid object instantiates cleanly, validation works.

### 3.3 Hour 0:35 — 1:15 — `apply_laplacian` method

This is the discrete cylindrical Laplacian, and it is the heart of the solver.

- Define the method on `ScreenedPoissonSolver`.
- Implement the stencil per §1.6 for interior points.
- Implement pole regularization per §1.7 if R[0] == 0.
- Implement mid-plane symmetry per §1.8 at j = 0.
- Outer boundary z = z_max: Dirichlet 0 — values at j = n_z − 1 contribute zero to neighbors' updates.
- Outer R = R_max: Dirichlet from BC; for `apply_laplacian`, just use the supplied T values (the method computes Laplacian, not the solve).

**Smoke test.** Use T(R, z) = R² + z²; verify ∇²T ≈ 6 at interior points. This is Test 1 done as a smoke test before formal testing.

**Checkpoint.** Laplacian operator returns 6 for the analytic test function within 5%.

### 3.4 Hour 1:15 — 1:45 — `solve` method

- Pre-compute stencil coefficients (a_E, a_W, a_N, a_S, a_C) for every (i, j) once on construction or at start of solve. Store as 2D arrays.
- Compute Yukawa-far BC values (1-D array of length n_z) before iteration.
- Compute mid-plane Neumann modification at j = 0.
- Implement the SOR loop: for each iteration, sweep through interior cells, apply update rule per §1.10, track max_change.
- Test convergence per §1.11; break if converged or max_iter reached.
- Return dict per §1.4.

**Smoke test.** Run on a tiny grid (10 × 5) with a uniform source; verify the field is approximately T_uniform = S/λ.

**Checkpoint.** Solver runs without crashing, returns a finite T field.

### 3.5 Hour 1:45 — 2:00 — `yukawa_green` function and final wiring

- Implement `yukawa_green(r, L, D_T, source_total)` per §1.5.
- Wire it into `solve()` for the Yukawa-far BC.
- Re-run the smoke test to confirm BC application doesn't break convergence.

**Checkpoint.** Module is functionally complete; smoke tests pass.

End of two-hour implementation block. Stop, take a break, then move to formal testing.

---

## 4. Hours 2–4 — Tests and debugging

### 4.1 Hour 2:00 — 2:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_pde_solver.py`.
- Write the six tests per §2.1–§2.6.
- For Test 1, the analytic Laplacian is the simplest reference.
- For Tests 2–4, the analytic Newtonian-Poisson reference is the workhorse.

### 4.2 Hour 2:30 — 3:30 — Run and debug

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_pde_solver.py -v`.
- This is the session most likely to have failures on first run. Common issues:
  - **Test 1 (Laplacian):** sign error in the stencil; off-by-one in the R_face_plus / R_face_minus indexing; wrong dR_avg definition.
  - **Test 2 (Newtonian Poisson):** the regularized point source's total integral must match the BC source_total. If the BC source_total is wrong, the far-field doesn't anchor correctly.
  - **Test 3 (Yukawa BC):** verify yukawa_green sign convention and units. Common bug: missing factor of 4π or incorrect L vs L².
  - **Test 6 (pole):** if T(0, 0) is NaN or Inf, the pole regularization is broken — most likely a wrong factor in the 4/dR² formula.
- Debug each failure individually. Do not modify the spec; modify the implementation.

### 4.3 Hour 3:30 — 4:00 — Documentation, lint, commit

- Verify all classes and methods have complete docstrings.
- Run lint if configured.
- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 3 complete. pde_solver.py implemented; 6/6 tests pass.`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/pde_solver.py
  git add ed-lab/simulations/edsim/dm/tests/test_pde_solver.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add pde_solver.py and tests — DM Step 3 complete"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/simulations/edsim/dm/pde_solver.py` exists with `CylindricalGrid`, `ScreenedPoissonSolver`, and `yukawa_green`.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_pde_solver.py` exists with six tests.
- [ ] All six tests pass under `pytest`.
- [ ] All public methods, classes, and functions have complete docstrings.
- [ ] The module imports cleanly with no warnings.
- [ ] No TODO comments remain except those explicitly deferred (red-black ordering, multigrid migration — both in scope only if SOR is too slow at the 30-galaxy stage).
- [ ] No `print` debug statements remain.
- [ ] One-line entry added to `ed-lab/arcs/arc-DM/run_log.md`.
- [ ] Commit landed with message `Add pde_solver.py and tests — DM Step 3 complete`.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not move to Step 4 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 3:

- `boundary_conditions.py`. Although Session 3 implements Yukawa-far and mid-plane-mirror inline, the dedicated boundary-conditions module (Step 4) factors these into reusable modes. Do not anticipate Step 4's API in Session 3.
- `validation_tests.py` (Step 5). The DM.4 §2 production-grid validation suite uses this solver but is its own module.
- Any actual SPARC galaxy run. No SPARC data is loaded in Session 3.
- The full Tier-3 self-consistency loop. The solver is stateless across `solve()` calls; the loop lives in Step 6.
- Multigrid implementation. Default is SOR; multigrid is a follow-up only if SOR proves too slow at the 30-galaxy stage.
- Red-black ordering. Default is row-major; red-black is a follow-up.
- Any vectorized or JIT-compiled (Numba) optimization. Profile first; optimize only if needed.

If during the session a tempting deviation surfaces, record it in a TODO comment and move on.

---

## 7. Risk inventory for Session 3

This is the highest-risk module in the arc. Three things most likely to consume more time than expected:

1. **Stencil sign or indexing errors.** The conservative cylindrical Laplacian on a non-uniform grid has six terms (a_E, a_W, a_N, a_S, a_C, source) and many places to make a mistake. Test 1 (analytic Laplacian) is specifically designed to catch these. If Test 1 fails, the bug is here. Expected resolution time if it bites: 30–90 minutes.

2. **Yukawa-far BC normalization.** The source_total integral must match the analytic 1/(4π D_T r) prefactor. A factor of 2π or 4π error in either the integral or the BC formula produces wrong far-field values. Test 3 catches this. Expected resolution time: 20–40 minutes.

3. **SOR convergence stall.** ω = 1.7 is typical for 2D Laplacian on a rectangular grid. For non-uniform R-grid with Dirichlet/Neumann mixed BCs, optimal ω may be different. If iterations fail to converge or oscillate, try ω in [1.5, 1.9] in increments of 0.05. Expected resolution time: 30–60 minutes if ω tuning is needed.

If the session runs over 5 hours, do not skip writing tests or commit. The completion checklist is the gate. If a test fails persistently, commit the partial work with the failure documented and resume in a follow-up session.

---

## 8. Cross-checks against earlier memos

The implementation must respect three structural constraints from earlier in the arc:

1. **Yukawa Green's function for point source** (DM.0 §3): T(r) ∝ exp(−r/L) / (4π D_T r). Verified by Tests 2 and 3.

2. **Screening length L = √(D_T/λ) ≈ 1 Mpc** (DM.0 §2). Verified implicitly in production grid extending to 5 Mpc.

3. **Conservative form of the cylindrical Laplacian** (DM.4 §2.2). Required because the non-conservative form does not preserve the divergence theorem on a non-uniform grid. The conservative discretization (Patankar §4.6) is the choice committed in §1.6.

---

## End-of-turn summary

**What got done this turn:** the Session 3 coding plan is fully scoped. Every class and method signature, unit convention, validation rule, stencil coefficient, boundary-condition treatment, and convergence criterion is specified. Six tests have explicit inputs, expected outputs, and tolerances. The two-hour implementation plan and the two-hour test/debug block are sequenced. Anti-scope-creep guardrails name what is forbidden. The session-complete checklist gates progress to Step 4.

**What did not get done:** no Python code has been written. The DM.9 memo is a session plan, not the session itself.

**What this means for the program:** the arc has continued past `activity_source.py` to `pde_solver.py` — the physics core. After Session 3, three of eight modules will be complete. The validation gate (Step 5) will be unblocked once Step 4 (`boundary_conditions.py`) is added.

**Decision after this session:** Step 4 (`boundary_conditions.py`) per DM.3 §1.1.4, scoped in DM.10 (a future coding-session-4 plan) when Session 3 lands. Session 4 will factor the Yukawa-far and mid-plane-mirror logic from this module into a reusable BC-mode dataclass.

---

## Recommended Next Step

After confirming DM.7 (Session 1) and DM.8 (Session 2) are fully landed (their §5 checklists satisfied), begin DM.9 Session 3: in `ed-lab/simulations/edsim/dm/`, create `pde_solver.py` and `tests/test_pde_solver.py`, then implement the components in the order specified in DM.9 §3.2–§3.5 (`CylindricalGrid` dataclass → `apply_laplacian` method → `solve` method → `yukawa_green` function), following the unit conventions in §1.2, the discretization in §1.6, the pole regularization in §1.7, the mid-plane symmetry in §1.8, the boundary conditions in §1.9, and the SOR rule in §1.10. Stop and run the test suite per §4.2 only after all four components are implemented; do not attempt Step 4 until the §5 session-complete checklist is fully satisfied.