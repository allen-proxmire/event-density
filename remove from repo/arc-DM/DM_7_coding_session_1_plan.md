# DM.7 — Coding Session 1 Plan: `disk_geometry.py`

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — eighth memo
**Status:** Coding-session plan committed. This memo is read by the analyst at the start of the coding session and followed without further design decisions.
**Predecessor:** DM.6 (branch selection — Branch A, begin implementation).
**Target file:** `ed-lab/simulations/edsim/dm/disk_geometry.py`
**Target tests:** `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py`
**Session goal:** Step 1 of the DM.4 implementation sequence complete. After this session, Step 2 (`activity_source.py`) is unblocked.

This memo contains no Python code. It specifies what the code must do, in what units, with what tolerances, in what order. Implementation is the analyst's task.

---

## 1. Module specification

### 1.1 File header

The file begins with a module-level docstring stating purpose ("Baryonic potential and velocity utilities for DM-arc simulations"), an authorship line, and a reference to DM.3 §1.1.3 and DM.6 §4.2. Imports: `numpy as np`, `scipy.integrate.quad`, `scipy.special.j0`. No other dependencies are required for this module.

### 1.2 Unit conventions

Fixed once for the entire DM submodule and not negotiated again:

- Lengths: kpc.
- Velocities: km/s.
- Masses: M☉.
- Potentials: (km/s)² = 10⁶ m²/s².
- Surface densities: M☉/kpc².

The gravitational constant in these units is **G ≈ 4.30091 × 10⁻⁶ kpc · (km/s)² / M☉**. Define this as a module-level constant `G_KPC_KMS_MSUN` and reuse. Do not redefine in functions.

### 1.3 Function 1 — `baryonic_velocity`

**Signature.**
`baryonic_velocity(R: np.ndarray, v_gas: np.ndarray, v_disk: np.ndarray, v_bulge: np.ndarray | None = None) -> np.ndarray`

**Behavior.** Returns v_bar(R) where v_bar² = v_gas² + v_disk² + v_bulge². If `v_bulge` is None, treat as zeros. R is passed through for shape validation but does not enter the computation.

**Numerical.** Pure quadrature. No interpolation. No integration.

**Validation.** Raise `ValueError` if input arrays do not all have the same shape. Raise `ValueError` if any of v_gas, v_disk, v_bulge contains negative values (SPARC convention is non-negative components).

**Edge cases.** NaN entries propagate. Empty arrays return empty arrays. Length-1 arrays return length-1 arrays. The function does not interpolate or extrapolate.

**Docstring.** State inputs (units kpc, km/s, km/s, km/s; v_bulge optional), output (km/s, same shape as inputs), the formula (v_bar² = v_gas² + v_disk² + v_bulge²), and a one-line reference to SPARC convention.

### 1.4 Function 2 — `baryonic_potential_inplane`

**Signature.**
`baryonic_potential_inplane(R: np.ndarray, v_bar: np.ndarray) -> np.ndarray`

**Behavior.** Returns Φ_bar(R) at z = 0 from the radial-equilibrium relation v²_bar = R · dΦ/dR. Solving for Φ:

Φ(R) = − ∫_R^{R_max} (v²_bar(R') / R') dR'

The integration convention sets Φ(R_max) = 0. Φ at smaller R is more negative.

**Numerical.** Trapezoidal integration on the input R grid (no resampling). Use `scipy.integrate.cumulative_trapezoid` or equivalent. Return the antiderivative shifted so that the last element is zero.

**Validation.** Require R strictly increasing. Raise `ValueError` if R has duplicates or is not monotonic. Require R[0] > 0 (no R = 0 input — singular at the axis).

**Edge cases.** Single-point arrays return zero. NaN entries in v_bar propagate downstream of the NaN.

**Docstring.** State inputs (R in kpc, v_bar in km/s), output (Φ in (km/s)², same shape as R, Φ(R_max) = 0 by convention), method (trapezoidal antiderivative), and the radial-equilibrium relation.

### 1.5 Function 3 — `exponential_disk_potential`

**Signature.**
`exponential_disk_potential(R_grid: np.ndarray, z_grid: np.ndarray, M_disk: float, R_d: float) -> np.ndarray`

**Behavior.** Returns the analytic gravitational potential of a razor-thin exponential disk at every grid point (R_grid[i], z_grid[j]) for i in 0..len(R_grid)-1, j in 0..len(z_grid)-1.

The exponential disk has surface density Σ(R) = Σ_0 exp(−R/R_d) with Σ_0 = M_disk / (2π R_d²).

The potential follows Binney & Tremaine §2.6.1 (eq. 2.169 in the 2008 edition):

Φ(R, z) = − G Σ_0 R_d · 2π · ∫_0^∞ J_0(k R) · exp(−k |z|) · (1 + (k R_d)²)^(−3/2) · dk · R_d

The bracketed integrand is the standard Hankel-transform form. Use `scipy.integrate.quad` over k from 0 to k_max, with k_max = 50 / R_d (practical convergence; sensitivity-test in §3 below).

**Numerical.**
- Bessel function: `scipy.special.j0`.
- Integration: `scipy.integrate.quad` per (R, z) point. This is slow if done naively (one quad call per grid point); for a 300 × 30 grid that's 9000 quad calls. For the first session, this is acceptable. Optimization (caching across z for fixed R, or vectorized Hankel transforms via `scipy.special.j0` on a precomputed k-grid) is a follow-up.
- Tolerance: `quad` defaults are fine; add `epsabs=1e-8, epsrel=1e-6, limit=200` to suppress occasional convergence warnings.

**Validation.** Raise `ValueError` if M_disk ≤ 0 or R_d ≤ 0. R_grid and z_grid must be 1-D arrays.

**Edge cases.**
- R = 0: J_0(0) = 1, integral converges. The function returns the on-axis potential correctly.
- z = 0: integrand simplifies; same general code path applies.
- Very large R (R ≫ R_d): potential approaches Keplerian −G M_disk / √(R² + z²). Verify in Test 5 below.

**Docstring.** State inputs (kpc, kpc, M☉, kpc), output (2-D array of shape (len(R_grid), len(z_grid)) in (km/s)²), the surface-density form, the Bessel-integral form, and a citation to Binney & Tremaine §2.6.1.

### 1.6 Function 4 — `baryonic_potential_grid`

**Signature.**
`baryonic_potential_grid(R_grid: np.ndarray, z_grid: np.ndarray, R_sparc: np.ndarray, v_bar_sparc: np.ndarray, R_d_fit: float, M_b: float) -> np.ndarray`

**Behavior.** Returns the combined baryonic potential Φ_bar(R, z) on the simulation grid. For Session 1, the implementation is the analytic exponential-disk form using the supplied (M_b, R_d_fit). The R_sparc / v_bar_sparc arrays are accepted in the signature for forward compatibility but are not used in the computation (they will be used in Session 1.5 for `R_d_fit` fitting; for now, R_d_fit is required as input).

**Numerical.** Single call to `exponential_disk_potential(R_grid, z_grid, M_b, R_d_fit)` and return.

**Validation.** Raise `NotImplementedError` if `R_d_fit is None` with a message: *"Auto-fitting of R_d from v_bar_sparc deferred to Session 1.5. Pass R_d_fit explicitly for Session 1."*

**Bulge contribution.** Deferred. Add a TODO comment in the function body: *"TODO (Session 1.5): add bulge potential via Hernquist or Plummer form."*

**Gas contribution.** Deferred. Same TODO.

**Docstring.** State that this is the Session-1 wrapper around `exponential_disk_potential` and that bulge/gas contributions and R_d auto-fitting are deferred.

---

## 2. Test specification

Tests live in `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py`. Use `pytest` conventions (`test_` prefix on functions, plain assertions). The test file imports `numpy`, `pytest`, and the four module functions.

### 2.1 Test 1 — Quadrature sum

**Purpose.** Verify `baryonic_velocity` computes the quadrature sum correctly.

**Inputs.**
- v_gas = [10, 20, 30] km/s
- v_disk = [40, 30, 20] km/s
- v_bulge = [0, 10, 20] km/s
- R = [1, 2, 3] kpc (passed for shape but not used)

**Expected output.**
- v_bar = [√(100 + 1600 + 0), √(400 + 900 + 100), √(900 + 400 + 400)] = [41.231, 37.417, 41.231] km/s

**Tolerance.** Relative error < 10⁻⁶ per element.

**Additional assertions.**
- Calling with `v_bulge = None` and v_bulge = [0, 0, 0] gives identical results to within 10⁻¹² km/s.
- Calling with mismatched shapes raises `ValueError`.
- Calling with negative v_disk raises `ValueError`.

### 2.2 Test 2 — In-plane potential of constant-velocity curve

**Purpose.** Verify `baryonic_potential_inplane` integrates correctly for an analytically known case.

**Inputs.**
- R = [1, 2, 5, 10, 20] kpc
- v_bar = [100, 100, 100, 100, 100] km/s (constant)

**Expected output.** For v constant = v_0, dΦ/dR = v_0² / R, so Φ(R) = v_0² · ln(R) + const. With Φ(R_max = 20) = 0 by convention:
- Φ(R) = v_0² · (ln R − ln 20) = 10000 · ln(R / 20)
- Expected Φ = [10000 · ln(0.05), 10000 · ln(0.1), 10000 · ln(0.25), 10000 · ln(0.5), 0]
- Numerical: ≈ [−29957, −23026, −13863, −6931, 0] (km/s)²

**Tolerance.** Trapezoidal integration on a sparse R-grid is not exact for ln. Tolerance: 5% relative on the slope (Φ[i+1] − Φ[i]) / (ln R[i+1] − ln R[i]) compared to v_0² = 10000.

**Additional assertions.**
- Φ is monotonically increasing in R.
- Φ at the largest R is exactly 0 (within 10⁻¹⁰ floating-point tolerance).

### 2.3 Test 3 — Exponential disk potential at z = 0, reference points

**Purpose.** Verify `exponential_disk_potential` matches the known closed-form midplane potential.

**Inputs.**
- M_disk = 5 × 10¹⁰ M☉
- R_d = 3 kpc
- R_grid = [0.1, 1, 3, 10, 30] kpc
- z_grid = [0] kpc

**Expected output.** The midplane potential of a razor-thin exponential disk has the closed-form expression involving modified Bessel functions I_n and K_n (Binney & Tremaine §2.6.1, eq. 2.165):

Φ(R, 0) = − π G Σ_0 R · [I_0(y) K_1(y) − I_1(y) K_0(y)],   where y = R / (2 R_d)

This is the analytic comparison target. Compute reference values using `scipy.special.iv` and `scipy.special.kv` (or `i0e`, `k0e`, etc., for numerical stability at large argument).

For the inputs above:
- y = [1/60, 1/6, 1/2, 5/3, 5]
- The reference Φ values can be computed in a separate utility before the test or precomputed to a table.

**Tolerance.** Relative error < 1% per point. (Expect ~0.1% achievable with default `quad` settings; tolerance of 1% allows margin.)

**Additional assertions.**
- Φ at all five points is negative.
- Φ becomes more negative as R decreases (closer to disk center).

### 2.4 Test 4 — Off-plane monotonicity

**Purpose.** Verify the potential decreases (becomes less negative) as |z| increases at fixed R.

**Inputs.**
- M_disk = 5 × 10¹⁰ M☉, R_d = 3 kpc
- R_grid = [5] kpc
- z_grid = [0, 0.5, 1, 2, 5] kpc

**Expected.** Φ(5, z) is monotonically increasing (less negative) in z. No quantitative tolerance for Session 1.

**Assertion.** `np.all(np.diff(Phi[0, :]) > 0)` is True.

### 2.5 Test 5 — Asymptotic Keplerian falloff

**Purpose.** Verify `exponential_disk_potential` reproduces the point-mass limit at large radius.

**Inputs.**
- M_disk = 5 × 10¹⁰ M☉, R_d = 3 kpc
- R_grid = [50, 100, 200, 500] kpc
- z_grid = [0] kpc

**Expected.** For R ≫ R_d, Φ → −G M_disk / R.
- Reference values: Φ_kep = −G_KPC_KMS_MSUN · 5e10 / R_grid.

**Tolerance.**
- 5% relative error at R = 100 kpc.
- 1% relative error at R = 500 kpc.

### 2.6 Test infrastructure

- Use `pytest.approx` for floating-point comparisons where convenient.
- Use parametrize-style tests if the analyst is comfortable with `pytest.mark.parametrize`; otherwise write five separate `def test_*` functions.
- Save reference Bessel values for Test 3 in the test file itself as a `REFERENCE_PHI_TEST3 = {...}` dict.

---

## 3. Two-hour implementation plan

The first two hours of the session are dedicated to writing the four functions. Tests come in the third hour.

### 3.1 Hour 0:00 — 0:15 — Setup

- Verify the working directory is `ed-lab/`. Check git status to confirm clean tree.
- Create directory `ed-lab/simulations/edsim/dm/` with empty `__init__.py`.
- Create directory `ed-lab/simulations/edsim/dm/tests/` with empty `__init__.py`.
- Create empty file `ed-lab/simulations/edsim/dm/disk_geometry.py`. Add module docstring per §1.1.
- Add imports: `numpy as np`, `scipy.integrate.quad`, `scipy.special.j0`, `scipy.special.iv`, `scipy.special.kv` (the last two for the test reference, but importing here is fine).
- Define `G_KPC_KMS_MSUN = 4.30091e-6` as a module constant with a comment naming the units.

**Checkpoint.** `python -c "import ed_lab.simulations.edsim.dm.disk_geometry"` succeeds (or whatever the actual import path turns out to be — verify against repo layout). The file imports cleanly even though it has no functions yet.

### 3.2 Hour 0:15 — 0:35 — `baryonic_velocity`

- Write the function signature per §1.3.
- Implement the quadrature sum.
- Add input validation (shape match, non-negative components).
- Handle `v_bulge is None` case.
- Write the docstring.
- Quick smoke test in a Python REPL: pass simple synthetic arrays and verify a sensible v_bar comes out.

**Checkpoint.** Function defined, imports clean, smoke test passes.

### 3.3 Hour 0:35 — 1:10 — `baryonic_potential_inplane`

- Write the function signature per §1.4.
- Implement the trapezoidal antiderivative using `scipy.integrate.cumulative_trapezoid` (note: with `initial=0` to keep array length).
- Apply the convention shift so Φ(R_max) = 0.
- Add input validation (monotonic R, R[0] > 0).
- Write the docstring.
- Smoke test: pass R = np.linspace(1, 20, 50), v = constant 100. Verify the output is a sensible logarithmic-looking curve.

**Checkpoint.** Function defined, smoke test gives expected logarithmic shape.

### 3.4 Hour 1:10 — 1:50 — `exponential_disk_potential`

This is the hardest function in the session. Budget the most time here.

- Write the signature per §1.5.
- Implement a helper function for the Bessel integrand (function of k for fixed R, z).
- Implement the outer loop over (R_grid, z_grid). For each (R, z), call `quad` on the integrand from 0 to k_max = 50/R_d.
- Multiply by the prefactor − G_KPC_KMS_MSUN · Σ_0 · R_d · 2π. Verify the dimensions work out: G [kpc·(km/s)²/M☉] · Σ_0 [M☉/kpc²] · R_d [kpc] = (km/s)². Good.
- Add input validation (positive M_disk, R_d).
- Write the docstring.
- Smoke test: run on R = [3] kpc, z = [0]; verify the result is a finite negative number around the right order of magnitude (a few × 10⁴ (km/s)² for the canonical inputs).

**Checkpoint.** Function defined; smoke test returns finite, negative, sensible-magnitude potential.

### 3.5 Hour 1:50 — 2:00 — `baryonic_potential_grid`

- Write the signature per §1.6.
- Validate `R_d_fit is not None`; raise `NotImplementedError` otherwise.
- Single call to `exponential_disk_potential` and return.
- Add the TODO comments for bulge, gas, and R_d-fitting.
- Write the docstring noting Session-1 limitations.

**Checkpoint.** Function defined; the file has all four functions; module imports cleanly.

End of two-hour implementation block. Stop, take a break, then move to testing in hours 2–3.

---

## 4. Hours 2–3 — Tests and debugging

### 4.1 Hour 2:00 — 2:30 — Write tests

- Create `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py`.
- Write the five tests per §2.1–§2.5.
- For Test 3, compute the reference Bessel values once (use a Python REPL or a one-off script) and hardcode them in the test file as a dict.

### 4.2 Hour 2:30 — 3:00 — Run and debug

- Run `pytest ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py -v`.
- Expected: all five tests pass on the first run if the implementation matches the spec. Realistic: 1–2 tests fail on first run, usually due to:
  - Sign error in the potential (check the convention: more negative = deeper well; Test 3 reference values are all negative).
  - Off-by-one in the integration convention (Φ(R_max) = 0 means the *last* element is zero).
  - Trapezoidal sparseness (Test 2 may need a denser R-grid; if 5 points fails, try 50).
  - `quad` convergence warning (suppressible with `quad` parameters per §1.5).
- Debug each failure individually. Do not modify the spec — modify the implementation to match the spec.

### 4.3 Hours 3:00 — 3:30 — Documentation, lint, commit

- Verify all four functions have complete docstrings.
- Run `python -c "import ed_lab.simulations.edsim.dm.disk_geometry"` from the repo root to confirm clean import.
- Run any local linters (black, ruff) if configured in the repo.
- Update or create `ed-lab/arcs/arc-DM/run_log.md` with a single line: `2026-MM-DD: Step 1 complete. disk_geometry.py implemented; 5/5 tests pass.`
- Commit:

  ```
  git add ed-lab/simulations/edsim/dm/disk_geometry.py
  git add ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py
  git add ed-lab/simulations/edsim/dm/__init__.py
  git add ed-lab/simulations/edsim/dm/tests/__init__.py
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add disk_geometry.py and tests — DM Step 1 complete"
  ```

- Push to origin.

---

## 5. Session-complete checklist

The session is complete if and only if all of the following are true:

- [ ] `ed-lab/simulations/edsim/dm/disk_geometry.py` exists with four functions implemented.
- [ ] `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py` exists with five tests.
- [ ] All five tests pass under `pytest`.
- [ ] The module imports cleanly with no warnings or errors.
- [ ] All four functions have complete docstrings (Args, Returns, References).
- [ ] The directory structure is correct: `dm/`, `dm/tests/`, both with `__init__.py`.
- [ ] One-line entry added to the arc run log.
- [ ] Commit landed with message `Add disk_geometry.py and tests — DM Step 1 complete`.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not move to Step 2 until the checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 1 and must not be attempted:

- `activity_source.py`, `pde_solver.py`, or any other module beyond `disk_geometry.py`.
- The validation suite (Tests 1, 2, 3 of DM.4 §2). Those require `pde_solver.py`.
- Loading actual SPARC data. No SPARC galaxy is touched in Session 1.
- The notebook `05_dm2_sparc_fits.ipynb`.
- R_d auto-fitting from v_bar_sparc. Deferred to Session 1.5.
- Bulge or gas potential treatment. Deferred to Session 1.5.
- Vectorized or cached Bessel-integral implementation. Deferred to a performance-optimization session if profiling shows it's needed.
- Any module-level pre-computation, caching, or memoization beyond what is specified above.

If during the session a tempting deviation surfaces ("while I'm here, I might as well..."), record it in a TODO comment and move on. The scope of Session 1 is fixed at the start and not negotiated mid-session.

---

## 7. Risk inventory for Session 1

Three things most likely to consume more time than expected:

1. **`scipy.integrate.quad` convergence warnings on the Bessel integrand.** The integrand oscillates (J_0 is oscillatory); `quad` may warn even when the result is correct. Suppress with appropriate parameters; if numerical trouble persists, switch to `scipy.special.hankel_e` or a fixed Gauss-Legendre rule. Expected resolution time if it bites: 30–60 minutes.

2. **Reference values for Test 3.** The midplane Bessel-K-I form requires careful argument handling. For y = 5 (R = 30 kpc), the I_0 and K_0 values are at the edge of double-precision range without using the scaled forms `i0e`, `k0e`. Use the scaled forms throughout for safety. Expected resolution time: 15–30 minutes if missed initially.

3. **Unit conversion errors.** The most common bug in astrophysical-units code is a missing factor of G or a missing 2π. The Test 5 asymptotic-Keplerian check is specifically there to catch this — if Test 5 fails by a factor of order π or 2, the prefactor in `exponential_disk_potential` is wrong. Expected resolution time: 10–30 minutes if it bites.

If the session runs long because of any of these, do not skip writing tests or the commit. The completion checklist is the gate.

---

## 8. After the session

When Session 1 is complete (all checklist items satisfied):

- Step 2 (`activity_source.py`) is unblocked. Per DM.3 §1.1.2, it depends on shape and vorticity utilities applied to v(R) — no PDE solver required.
- Session 2 implements `activity_source.py` plus a parallel one-time SPARC ingestion utility (Session 1.5).
- The arc continues toward the validation gate.

The DM.5-TEMPLATE remains the verdict scaffold. Each completed session reduces the engineering distance to a real DM.5.

---

## End-of-turn summary

**What got done this turn:** the coding session is fully scoped. Every function signature, unit convention, validation rule, and edge case is specified. Every test has explicit inputs, expected outputs, and tolerances. The two-hour implementation plan and the one-hour test/commit block are sequenced. Anti-scope-creep guardrails name what is forbidden in the session. The session-complete checklist gates progress to Step 2.

**What did not get done:** no Python code has been written. The DM.7 memo is a session plan, not the session itself. The plan presupposes a future coding session in which the analyst executes per these specifications.

**What this means for the program:** the arc has converted "begin implementation" (DM.6) into "implement disk_geometry.py per this exact spec" (DM.7). The next move is keystrokes, not memos.

**Decision after this session:** Step 2 (`activity_source.py`) per DM.3 §1.1.2, scoped in DM.8 (a future coding-session-2 plan) when Session 1 lands.

---

## Recommended Next Step

Start the coding session: in `ed-lab/`, create `simulations/edsim/dm/__init__.py`, `simulations/edsim/dm/disk_geometry.py`, and `simulations/edsim/dm/tests/__init__.py`, then implement the four functions in the order specified in DM.7 §3.2–§3.5 (`baryonic_velocity` → `baryonic_potential_inplane` → `exponential_disk_potential` → `baryonic_potential_grid`), following the unit conventions in §1.2 and the validation rules in each subsection. Stop and run the test suite per §4.2 only after all four functions are implemented; do not attempt Step 2 until the §5 session-complete checklist is fully satisfied.
