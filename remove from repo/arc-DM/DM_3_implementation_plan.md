# DM.3 — Implementation Plan for the Activity-Sourced PDE on SPARC

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — fourth memo
**Status:** Implementation plan complete. This memo specifies the code modules, numerical methods, fitting procedure, validation suite, and run protocol. It does **not** execute the implementation — that is DM.4.
**Predecessor:** DM.2 (simulation design committed).
**Successor:** see *Recommended Next Step*.
**Target codebase:** `ed-lab/simulations/edsim/dm/` and `ed-lab/analysis/scripts/dm2_sparc/`.
**Existing infrastructure leveraged:** `edsim/core`, `edsim/math`, `edsim/io`, `edsim/units`, `edsim/tests`. Pattern matched against existing scripts `btfr_activity_union.py` and the `ed_sc_3_*` series.

---

## 1. Code modules to create

All paths are relative to `ed-lab/`. Module names match repo conventions (snake_case, descriptive, terse).

### 1.1 `simulations/edsim/dm/`

A new submodule, eight files. Add `__init__.py` exposing the public API.

#### 1.1.1 `pde_solver.py`

**Purpose.** The 2D axisymmetric screened-Poisson solver. The physics core of DM.

**Public API.**
```
class ScreenedPoissonSolver:
    def __init__(self, grid: CylindricalGrid, D_T: float, lam: float):
        ...
    def solve(self, source: np.ndarray, bc: BoundaryConditions,
              method: str = "sor", tol: float = 1e-6, max_iter: int = 5000
              ) -> np.ndarray:
        """Returns T(R, z) on the grid."""

def yukawa_green(r: np.ndarray, L: float, D_T: float) -> np.ndarray:
    """Analytic Green's function for validation."""
```

**Inputs.** Source array S(R, z) on grid; D_T and λ from `edsim/phys/constants.py` (add ED-DM constants there if not present); boundary-condition object.

**Outputs.** T(R, z) array; iteration count; final residual.

**Dependencies.**
- `numpy` for arrays
- `scipy.sparse` and `scipy.sparse.linalg` for the multigrid fallback
- `edsim/math/laplacian.py` for the cylindrical-Laplacian stencil if it exists; otherwise add `cylindrical_laplacian()` here
- `edsim/units` for unit consistency

**Failure mode.** If the iteration does not converge in max_iter, raise `SolverConvergenceError` with diagnostics (final residual, max element).

#### 1.1.2 `activity_source.py`

**Purpose.** Build the activity scalar A(R) from a velocity profile, then convert to S(R, z) with disk geometry.

**Public API.**
```
def shear_squared(R: np.ndarray, v: np.ndarray) -> np.ndarray:
    """|dv/dR|^2 from a tabulated v(R)."""

def vorticity_squared(R: np.ndarray, v: np.ndarray) -> np.ndarray:
    """(v / R)^2 with regularization at R=0."""

def activity_index(R: np.ndarray, v: np.ndarray, alpha: float
                   ) -> np.ndarray:
    """A(R) = alpha * shear_squared + (1 - alpha) * vorticity_squared."""

def activity_source_3d(R_grid: np.ndarray, z_grid: np.ndarray,
                       A_R: np.ndarray, kappa_act: float,
                       h_disk: float = 0.3 * KPC) -> np.ndarray:
    """Returns S(R, z) = kappa_act * A(R) * sech^2(z/h_disk) / (2 h_disk)."""
```

**Inputs.** Radius and velocity arrays (1D); α; κ_act; disk thickness h_disk.

**Outputs.** S(R, z) on the 2D grid.

**Numerical detail.** dv/dR computed by centered differences with one-sided differences at endpoints. Vorticity at R=0 set to zero by symmetry (v(0) = 0 for non-rotating axis).

#### 1.1.3 `disk_geometry.py`

**Purpose.** Compute baryonic potential Φ_bar(R, z) and v_bar(R) from SPARC tabulated quantities.

**Public API.**
```
def baryonic_velocity(R: np.ndarray, v_gas: np.ndarray,
                      v_disk: np.ndarray, v_bulge: np.ndarray
                      ) -> np.ndarray:
    """v_bar^2 = v_gas^2 + v_disk^2 + v_bulge^2."""

def baryonic_potential_grid(R_grid: np.ndarray, z_grid: np.ndarray,
                             R_sparc: np.ndarray, v_bar_sparc: np.ndarray
                             ) -> np.ndarray:
    """Reconstruct Phi_bar on the simulation grid by integration."""
```

**Inputs.** SPARC table-2 columns (radius, gas/disk/bulge velocities).

**Outputs.** v_bar(R) on the SPARC radii; Φ_bar(R, z) on the simulation grid.

**Detail.** Φ_bar in the disk plane comes from v_bar by integration (Φ_bar(R) = ∫ v²_bar/R' dR'). For the off-plane potential, use the standard exponential-disk Bessel-function form (Binney & Tremaine §2.6.1) parametrized by an effective R_d fit to the SPARC v_disk profile. The exact off-plane Φ_bar is not load-bearing for the in-plane v_pred; first implementation can use the in-plane potential with thin-disk approximation.

#### 1.1.4 `boundary_conditions.py`

**Purpose.** Define and apply boundary conditions for the screened-Poisson solver.

**Public API.**
```
@dataclass
class BoundaryConditions:
    inner_R: str = "neumann_zero"   # dT/dR = 0 at R = 0
    outer_R: str = "yukawa_far"     # T = (S_total / 4 pi D_T r) exp(-r/L)
    inner_z: str = "neumann_zero"   # dT/dz = 0 at z = 0
    outer_z: str = "dirichlet_zero" # T = 0 at z = z_max

def apply(T: np.ndarray, source: np.ndarray, bc: BoundaryConditions,
          grid: CylindricalGrid, D_T: float, L: float) -> np.ndarray:
    """In-place application of BCs after each relaxation sweep."""
```

**Detail on `yukawa_far`.** At R = R_max, set T to the analytic Yukawa value computed from the integrated source: T(R_max, z) = (∫ S d³x / 4π D_T r) · exp(−r/L), evaluated at r = √(R_max² + z²). This avoids spurious reflection from the truncation.

#### 1.1.5 `validation_tests.py`

**Purpose.** Three analytic test cases per DM.2 §5.3.

**Public API.**
```
def test_point_source(grid: CylindricalGrid, D_T: float, lam: float
                       ) -> dict:
    """Returns {'pass': bool, 'rel_err': float, 'expected': arr, 'computed': arr}."""

def test_uniform_source(grid: CylindricalGrid, D_T: float, lam: float
                         ) -> dict:
    """T should be uniform = S/lambda."""

def test_isothermal_source(grid: CylindricalGrid, D_T: float, lam: float
                            ) -> dict:
    """T should be logarithmic; v_T should be flat to 1%."""

def run_all(grid, D_T, lam) -> dict:
    """Runs all three; returns summary report."""
```

**Pass criteria.**
- Point source: relative error of computed T(r) vs. analytic Yukawa < 1% for r in [10 kpc, 500 kpc].
- Uniform source: T uniform to 0.1% across the central 90% of the grid.
- Isothermal: predicted v_T(R) flat to within 1% across r ∈ [5 kpc, 50 kpc] (the unscreened region).

**Run condition.** This file is run *before* any SPARC galaxy. CI gate: if any of the three fails, the SPARC pipeline is blocked.

#### 1.1.6 `run_single_galaxy.py`

**Purpose.** End-to-end pipeline for one SPARC galaxy.

**Public API.**
```
def run_single_galaxy(galaxy_data: SparcGalaxy,
                      kappa_act: float, alpha: float,
                      D_T: float, lam: float,
                      tier: int = 3, verbose: bool = False
                      ) -> SingleGalaxyResult:
    """Returns SingleGalaxyResult with v_pred, residuals, chi2, T(R,z)."""

@dataclass
class SingleGalaxyResult:
    galaxy_id: str
    R_obs: np.ndarray
    v_obs: np.ndarray
    sigma_v: np.ndarray
    v_pred: np.ndarray
    delta_v: np.ndarray
    chi2: float
    chi2_red: float
    T_field: np.ndarray  # full grid
    iterations_to_converge: int  # for tier 3
```

**Inputs.** A `SparcGalaxy` dataclass loaded from SPARC tables; (κ_act, α); inherited (D_T, λ); tier flag.

**Outputs.** Per-galaxy results object.

**Tier handling.**
- Tier 1: A built from v_bar, single solve.
- Tier 2: A built from v_pred(Tier 1), single solve.
- Tier 3: iterate to fixed point — A_n+1 = activity(v_pred,n), terminate when ‖v_pred,n+1 − v_pred,n‖_inf < 1 km/s or n = 50.

#### 1.1.7 `run_full_sample.py`

**Purpose.** Run the pipeline across the SPARC sample with global (κ_act, α). Parallelizable.

**Public API.**
```
def run_full_sample(galaxies: list[SparcGalaxy],
                     kappa_act: float, alpha: float,
                     D_T: float, lam: float,
                     n_jobs: int = -1
                     ) -> SampleResult:
    """Returns SampleResult with all per-galaxy outputs and global statistics."""
```

**Detail.** Parallelization with `joblib.Parallel`. Standard. Per-galaxy independent.

#### 1.1.8 `__init__.py`

Standard public-API exposure. No logic.

### 1.2 `analysis/scripts/dm2_sparc/`

Three files. Match the flat structure of existing analysis scripts.

#### 1.2.1 `fit_activity_parameters.py`

**Purpose.** Global fit of (κ_act, α) against the SPARC sample. Implements the universality test.

**Logic.**
- Define an objective: total χ² across all galaxies (sum of per-galaxy χ²).
- Use `scipy.optimize.minimize` (Nelder-Mead or L-BFGS) over (log κ_act, α) with α ∈ [0, 1].
- Cross-validation: 5-fold split. Fit on 80% of galaxies, evaluate on held-out 20%. Report mean held-out χ². Universality is supported if held-out and training χ² are comparable; broken if held-out χ² is systematically higher.

**Output.** `dm2_global_fit_results.json` with fitted (κ_act, α), per-fold statistics, sample-wide χ² distribution.

#### 1.2.2 `compute_residuals.py`

**Purpose.** Per-galaxy residual analysis and stratification per DM.2 §3.3.

**Logic.**
- Load `dm2_global_fit_results.json`.
- For each galaxy, recompute v_pred at fitted parameters and bin residuals.
- Stratify by mass (log M_b in 4 bins), morphology (T-type), surface brightness (SB_disk in 3 bins), activity (⟨A⟩ in 3 bins).
- Apply RC #1: median |⟨Δv(r)⟩| in each radial bin × each stratification.

**Output.** `dm2_residuals.csv` (per-galaxy) and `dm2_residuals_stratified.csv` (group statistics).

#### 1.2.3 `btfr_analysis.py`

**Purpose.** Extract BTFR slope from predicted curves; apply RC #3.

**Logic.**
- For each galaxy, compute v_∞ as median(v_pred) over the outer half of the disk.
- Fit log v_∞ vs. log M_b across the sample.
- Compare slope to MOND/empirical 4 ± 0.25.

**Output.** `dm2_btfr.json` with fitted slope, 1σ uncertainty, RC #3 verdict.

### 1.3 `analysis/notebooks/05_dm2_sparc_fits.ipynb`

**Purpose.** Reproducibility notebook in the pattern of `03_galaxy15_lag.ipynb`.

**Cells.**
1. Imports + path setup.
2. Load 10 representative SPARC galaxies (cross-section: dwarf, LSB, MW-class, massive spiral).
3. Run the validation suite. Display pass/fail for each test.
4. Run `run_full_sample` on the 10-galaxy subset with the globally-fitted (κ_act, α).
5. Plot: predicted vs. observed v(r) for each.
6. Plot: residual distribution.
7. Print: BTFR slope, χ² distribution.
8. Print: verdict against the three RCs.

**Runtime.** Target < 5 minutes on Colab. Full-sample runs use the scripts.

---

## 2. Numerical methods — concrete

### 2.1 Grid

Cylindrical (R, z), axisymmetric.

- **R extent:** 0 to R_max = 5 Mpc.
- **R grid:** logarithmic in [0.01 kpc, 50 kpc] with 200 cells, linear in [50 kpc, 5 Mpc] with 100 cells. Total: 300 cells.
- **z extent:** 0 to z_max = 1.5 kpc (mid-plane symmetry).
- **z grid:** uniform with 30 cells.
- **Total grid:** 300 × 30 = 9000 cells per galaxy.

This is smaller than the 25,000-cell estimate in DM.2 §5.1; the design is tightened by using mid-plane symmetry and logarithmic R-spacing.

### 2.2 Finite-difference stencil

Cylindrical Laplacian in (R, z) with axisymmetry:

> ∇²T = (1/R) ∂_R(R ∂_R T) + ∂²_z T.

Discretized on a non-uniform R-grid:

> [(1/R_i) · (R_{i+1/2} (T_{i+1} − T_i) / ΔR_+ − R_{i−1/2} (T_i − T_{i−1}) / ΔR_−)] / [(ΔR_+ + ΔR_−)/2]
>   + (T_{j+1} − 2 T_j + T_{j−1}) / Δz²
>   − T_{i,j} / L²
> = − S_{i,j} / D_T,

with i indexing R, j indexing z. R_{i±1/2} are the cell-face values. At i = 0, the (1/R) ∂_R(R ∂_R) term is regularized using the limit form (4/ΔR²) (T_1 − T_0) — the standard pole treatment.

### 2.3 Solver choice

**Default: SOR (successive over-relaxation).**

- Initialization: T = 0 everywhere.
- Sweep order: R-major, z-minor, red-black (Gauss-Seidel pattern).
- Relaxation parameter ω = 1.7 (typical optimum for 2D Laplacian on this grid).
- Convergence: max relative change < 10⁻⁶ across two consecutive sweeps.
- Expected iterations: ~3000.

**Multigrid escalation criterion.** If wall-time per galaxy exceeds 60 s in benchmarking, migrate to a multigrid V-cycle solver. Implementation: PyAMG library. Expected speedup: 30–100×.

**Migration trigger.** Don't migrate preemptively. SOR first; multigrid only if the timing budget breaks.

### 2.4 Boundary conditions — explicit

- **R = 0:** T_{0,j} updated using the regularized stencil above. (Equivalent to ∂T/∂R = 0 by axisymmetry.)
- **R = R_max:** Dirichlet from the analytic Yukawa: T_{N_R, j} = (M_S / 4π D_T) · exp(−r/L) / r where M_S = ∫ S d³x and r = √(R_max² + z_j²).
- **z = 0:** Neumann (∂T/∂z = 0) by mid-plane symmetry. Implemented via ghost-cell mirror.
- **z = z_max:** Dirichlet T = 0.

### 2.5 Computing shear and vorticity

From the per-radius v(R) array (either v_bar or v_pred depending on tier):

- **Shear:** dv/dR via centered differences on the SPARC R-grid; one-sided at endpoints; smoothed with a 3-point box filter to reduce noise from sparse SPARC sampling.
- **Vorticity:** v(R) / R, regularized at the innermost SPARC point by linear interpolation to (R, v) → (0, 0).

Both are interpolated to the simulation R-grid via cubic spline before constructing A(R).

### 2.6 Convergence and stability

For Tier 3 self-consistency loop:
- Initial guess: v_pred = v_bar.
- Termination: max |v_pred,n+1 − v_pred,n| < 1 km/s across all SPARC radii.
- Maximum outer iterations: 50.
- Damping: if oscillation detected (residual stops decreasing for 3 consecutive iterations), switch to v_pred,n+1 = 0.5 (v_pred,new + v_pred,n).

Expected outer iterations: 5–15 for typical galaxies. If outer convergence fails (>50 iterations), flag the galaxy and exclude from global fit (separate diagnostic).

---

## 3. Parameter-fitting procedure

### 3.1 Global fit

**Objective function.** Sum-of-squares total χ²:

> χ²_total(κ_act, α) = Σ_g Σ_i [(v_pred(R_i; g, κ_act, α) − v_obs(R_i; g)) / σ_v(R_i; g)]²,

where g indexes galaxies and i indexes radii.

**Optimizer.** `scipy.optimize.minimize`, method = "Nelder-Mead". Initial guess: log κ_act = midpoint of dimensional estimate (DM.1 §6.1 gives γ κ_act ≈ D_T → log κ_act ≈ log(D_T) + log(γ⁻¹), so κ_act ≈ 10⁻⁶ kg s/m³ as the dimensional anchor); α = 0.5.

**Bounds.** log κ_act free; α ∈ [0, 1].

**Cost per evaluation.** ~150 galaxies × 30 s/galaxy at Tier 3 = 1.25 hours per parameter trial. Optimizer takes ~30 trials → ~40 hours total.

**Practical strategy.** Run the optimizer on a 30-galaxy subset first (representative of mass range and morphology). Refine on full sample at the converged region.

### 3.2 Cross-validation (universality test)

5-fold split, stratified by log M_b to avoid mass-bias in folds. For each fold:
- Fit (κ_act, α) on training 80%.
- Evaluate held-out χ²/dof on the test 20% with no re-fitting.

**Metric.** Ratio R_cv = ⟨χ²_test⟩ / ⟨χ²_train⟩. Universality holds if R_cv ∈ [0.9, 1.3]. R_cv > 1.5 implies the global fit is overfitting; per-galaxy variation in true κ_act is required.

### 3.3 Per-galaxy κ_act distribution (RC #2)

After the global fit, re-fit each galaxy individually with α held at the global value, fitting only κ_act. This produces a per-galaxy distribution κ_act,g.

**Universality criterion.** σ(log κ_act,g) / mean(log κ_act,g) < 0.13 (corresponding to ±30% spread). And Spearman correlation with each of {log M_b, T-type, log SB, log sSFR} satisfies |ρ| < 0.3.

If both hold, RC #2 is cleared. If either is violated, RC #2 fires and the framework's parsimony claim has to be revisited.

---

## 4. Validation suite — pass/fail criteria

### 4.1 Test 1 — Point source

Set S(R, z) = M_test · δ(R) δ(z) / (2π R) (regularized as a Gaussian of width 0.5 kpc). Solve for T. Compare to analytic Yukawa T_analytic(r) = M_test exp(−r/L) / (4π D_T r).

**Pass:** max |T_computed − T_analytic| / |T_analytic| < 1% over r ∈ [10 kpc, 500 kpc].
**Fail:** any radius in this range exceeds 1% relative error.

### 4.2 Test 2 — Uniform source

Set S(R, z) = S_0 = constant on a finite grid. Solve. Expected T = S_0 / λ everywhere (zero-curvature solution, since ∇² · const = 0).

**Pass:** max |T − S_0 / λ| / (S_0 / λ) < 0.1% across the central 90% of the grid (excludes boundary cells).
**Fail:** > 0.1%.

### 4.3 Test 3 — Isothermal source

Set S(R, z) = S_0 / R² for R ∈ [1 kpc, 50 kpc] (mimicking the DM.1 fixed-point shear source), zero outside. Solve. Compute v_T(R) = √(R · ∂Φ_T/∂R) under Reading B (Φ_T = γ T with γ such that γ · κ_act = D_T).

**Expected:** v_T(R) flat at the value √(γ S_0 / D_T) across r ∈ [5 kpc, 30 kpc].
**Pass:** v_T(R) flat to within 1% across [5 kpc, 30 kpc].
**Fail:** > 1% deviation.

### 4.4 Validation gate

The SPARC pipeline does not run unless all three tests pass on the production grid. CI hook: `validation_tests.run_all()` is the first cell of the `05_dm2_sparc_fits.ipynb` notebook and the first call in any script.

---

## 5. Full SPARC run protocol

### 5.1 Sample selection

- Source: SPARC tables 1 and 2 from Lelli, McGaugh, Schombert 2016.
- Quality cut: drop galaxies with quality flag Q > 2.
- Distance cut: drop galaxies with distance uncertainty > 30%.
- Inclination cut: drop galaxies with i < 30° (rotation-curve uncertainty grows).
- Expected sample size: ~150 galaxies.

### 5.2 Preprocessing

For each galaxy:
- Construct v_bar(R) on the SPARC R-grid.
- Identify R_min and R_max from the tabulated radii.
- Build the geometric ρ_geom(R, z) using h_disk = 0.3 kpc (sensitivity-tested).
- Set up the simulation grid (300 × 30) with appropriate R_min and R_max anchors.

### 5.3 Per-galaxy PDE solve

Tier 3 (self-consistent) per `run_single_galaxy.py`. Output stored as a JSON record + numpy file for the T-field.

### 5.4 Residual computation

For each galaxy, compute Δv(R) = v_pred(R) − v_obs(R) on the SPARC R-grid. Aggregate with mass/morphology stratification per `compute_residuals.py`.

### 5.5 BTFR extraction

For each galaxy, v_∞ is median(v_pred) over the outer half of the SPARC R range. Fit log v_∞ vs. log M_b across the sample with linear regression. Slope ± 1σ.

### 5.6 RC application

After the full run:
- **RC #1** (`compute_residuals.py`): is the median |⟨Δv(r)⟩| > 20 km/s in any radial bin in any stratum across > 30% of the sample? Or χ²_red distribution multimodal?
- **RC #2** (`fit_activity_parameters.py`): does the per-galaxy κ_act distribution have σ(log κ_act) > 0.13 of the mean? Or correlate with any galaxy property at |ρ| > 0.3?
- **RC #3** (`btfr_analysis.py`): is the BTFR slope outside [3.5, 4.5] at > 3σ?

If none of the three RCs fire, DM.3 returns PASS.

### 5.7 Output artifacts

- `dm2_global_fit_results.json` — fitted parameters, fold statistics
- `dm2_per_galaxy.csv` — one row per galaxy: ID, M_b, T-type, SB, R_d, v_∞_obs, v_∞_pred, χ², χ²_red, fitted κ_act
- `dm2_residuals.csv` — per-radius residuals for every galaxy
- `dm2_btfr.json` — BTFR slope and verdict
- `dm2_verdict.md` — summary memo with the four-way verdict architecture (PASS / PARTIAL-univ / PARTIAL-BTFR / FAIL)
- `dm2_T_fields.h5` — full T(R, z) for each galaxy (compressed HDF5)

---

## 6. Risk inventory

A short list of things that could go wrong in implementation, ordered by likelihood and severity:

1. **Validation Test 3 fails.** The solver produces flat curves to better than 1% in synthetic isothermal-source tests but real galaxies show offsets. Diagnostic: the failure is then physics, not numerics; proceed to RC analysis.

2. **Tier 3 outer loop fails to converge for a subset of galaxies.** Mitigation: damping in §2.6. If > 5% of galaxies fail to converge, fall back to Tier 2 for those galaxies and document; the universality test must then be conditioned on Tier 2 vs. 3 mixing.

3. **κ_act distribution is bimodal.** May indicate two populations (e.g., dwarfs vs. spirals) with different microphysics. Diagnostic: stratify by morphology and look for clean separation. If clean, structurally interesting; if scattered, RC #2 fires.

4. **BTFR slope correct but offset wrong.** RC #3 only tests slope. A systematic offset in v_∞ at fixed M_b would be invisible to the slope test. Add a per-stratum offset diagnostic to `btfr_analysis.py`.

5. **Solver instability at very small R (< 0.1 kpc).** The 1/R term in the cylindrical Laplacian can amplify noise. Mitigation: hard-coded R_min = 0.01 kpc; pole regularization in §2.2. Test with the validation suite.

6. **SPARC distance uncertainties propagating into M_b.** SPARC distances have 10–30% uncertainty for some galaxies. This translates into M_b uncertainty in BTFR fit. Use SPARC's "Distance method" flag to weight; high-quality distance galaxies dominate the slope.

---

## 7. What DM.3 produces and what it does not

### 7.1 Produces
- A working, validated solver for the activity-sourced PDE.
- Per-galaxy v_pred for ~150 SPARC galaxies under universal (κ_act, α).
- A quantitative answer to whether (κ_act, α) can be universal.
- A measured BTFR slope from PDE-derived curves.
- A documented PASS / PARTIAL / FAIL verdict against the three refutation conditions.

### 7.2 Does not
- Derive κ_act from primitives. That remains an open structural question independent of DM.3 outcome.
- Test against galaxy clusters (already done in the merger-lag paper).
- Resolve Reading B vs. Reading C of T-to-gravity mapping.
- Address non-axisymmetric features (bars, warps).
- Test environmental dependence (would require environment metadata not in SPARC).

---

## Recommended Next Step

**DM.4 — full execution.**

The implementation plan is committed and concrete. The SPARC sample is in hand, the solver design is constrained by validation gates, the global fit procedure is specified, and the verdict architecture is built into the analysis scripts. There are no remaining design decisions; the next move is to write the code and run it.

Three sub-recommendations on execution order:

1. **Validation suite first.** Implement `pde_solver.py`, `boundary_conditions.py`, and `validation_tests.py` and run the three analytic tests before any galaxy work. If any test fails on the production grid, either the grid resolution is insufficient or the solver has a bug. Either way, no SPARC run is meaningful until the gate is cleared.

2. **One-galaxy proof of concept.** Pick a well-studied SPARC galaxy (NGC 3198 is canonical; large, well-resolved, mass ~6×10¹⁰ M☉). Run Tier 3 with κ_act = the dimensional-anchor value from §3.1. Inspect v_pred(R) qualitatively. If the curve is wildly wrong (off by > factor 3) at this stage, something fundamental is broken — solver bug, dimensional error in source, wrong T-to-gravity coupling. Diagnose before scaling up.

3. **30-galaxy global fit.** Fit (κ_act, α) on a stratified subset of 30 galaxies. This is the cheapest test of whether the global fit is well-conditioned. If the optimizer fails to converge on 30 galaxies, the full-sample fit will fail too, and that would be a structural finding (likely a sign that κ_act is not universal).

Steps 1, 2, and 3 together total ~3 days of implementation effort. Only after all three clear is the full-sample run worth the compute.

The alternative branches the user named are not appropriate at this stage:
- **Parameter-sensitivity analysis** is part of DM.4 (in the form of cross-validation and stratified residuals) but does not stand alone.
- **Branching to V₁ + acoustic-metric channel** is the right move *only if* DM.4 returns FAIL after validation passes and steps 1–3 clear cleanly. Speculative branching before the test is premature.

---

## End-of-turn summary

**What got done.** The implementation plan is fully specified. Eight Python modules in two locations are defined with public APIs, dependencies, inputs, and outputs. Numerical methods (grid, stencil, solver, BCs, shear/vorticity construction) are concrete. The fitting procedure (objective, optimizer, cross-validation, universality test) is specified. The validation suite is defined with quantitative pass/fail criteria. The full SPARC run protocol is described from sample selection through verdict.

**What did not get done.** Code has not been written. No SPARC galaxy has been run.

**What this means for the program.** The DM arc is now ready for execution. Three memos of structural argument (DM.0, DM.1, DM.2) and one memo of implementation plan (DM.3) sit in front of the empirical confrontation. The architecture is sound; the engineering is bounded.

**Compute envelope.** ~50 hours single-CPU for the full sample at Tier 3 with optimization. ~3 days of implementation effort for the eight modules and three analysis scripts. ~5 minutes for the reproducibility notebook (subset of 10 galaxies).

**Output cadence.** Validation pass within 1 day. One-galaxy proof of concept within 2 days. 30-galaxy fit within 3 days. Full sample within 1 week. Verdict within 1.5 weeks.

**Decision point.** DM.4 begins implementation. DM.5 is the verdict memo, written after DM.4 completes.
