# ED-SC 2.0 r*: Monte Carlo Workflow for Closing the κ⊥ Gap

**Status.** Workflow memo. Closes the final empirical gap in the analytic
r* chain by specifying the Monte-Carlo protocol for estimating κ⊥ (and
thus r*) from stationary-point statistics of the noisy Scenario-D SPDE
under the canonical ED-SC 2.0 motif filter.

**Inputs (fixed, not re-derived here):**

- Scenario-D canonical parameters: `M₀ = 1, M₂ ≈ 0 (leading), P₀ = 1, P₃ = −1, σ* = 0.0556`
- Motif filter: `α = 0.25, L_ray = 2, δ_thr = 0.10`
- Analytic r* formula (from `ED_SC_2_0_r_star_Anisotropy.md`): `r* = −2χ/(2χ−1)`, `χ = 2μκ⊥²/P₀`
- Leading-order trace closure (from Anisotropy memo): `s = κ∥/κ⊥ = −1`
- Target expectation: `κ⊥ ≈ 1.04`, `r* ≈ −1.304`
- Falsification window (ED-SC 2.0): `r* ∈ [−1.50, −1.10]`

---

## 1. SPDE discretization

### 1.1 Equation

    ∂_t δ(x, t) = ∇·(M(δ) ∇δ) − P(δ) + ξ(x, t)                       (1.1)

with

    M(δ) = M₀ + ½ M₂ δ²,     P(δ) = P₀ δ + (1/6) P₃ δ³,
    ⟨ξ(x, t) ξ(x′, t′)⟩ = 2 σ² δ²(x − x′) δ(t − t′).

### 1.2 Grid

- **Domain:** square `L × L` with periodic boundary conditions.
- **Reference size:** `L = 64` (ED-Arch-01 canonical), also run `L = 128, 256, 512` for finite-size diagnostics.
- **Grid spacing:** `Δx = 1` (natural units; `M₀ = P₀ = 1`).
- **Grid points:** `N = L/Δx` per side; total sites `N²`.
- **Rationale:** target curvature scale `κ⊥ ≈ 1.04` has width `w⊥ ≈ 1/√κ⊥ ≈ 0.98`; at `Δx = 1` this is marginally resolved. Run `Δx = 0.5` for discretisation diagnostics (§6.2).

### 1.3 Timestep

- **Canonical:** `dt = 0.05` (ED-Arch-01).
- **CFL constraint** for explicit diffusion in 2D: `dt ≤ Δx² / (4 M_eff)` where `M_eff = M₀ + ½ M₂ δ_max²`. At canonical parameters, `dt = 0.05 < 0.25` — safe by factor 5.
- **Stiff-penalty constraint:** `dt ≤ 1 / |P′(δ_max)|`. At the cubic nullcline, `|P′| = 2`, so `dt ≤ 0.5` — safe.

### 1.4 Scheme

**Semi-implicit Euler (IMEX):** treat the linear diffusion + linear penalty implicitly, nonlinear mobility/cubic + noise explicitly.

    (I − dt · [M₀ ∇² − P₀]) δ^{n+1}
        = δ^n + dt · [ ½ M₂ ∇·(δ²∇δ) − (P₃/6) δ³ ]^n
              + √(2 σ² dt / Δx²) · 𝒩^n                                 (1.2)

where `𝒩^n` is an i.i.d. standard-normal field drawn each step, independent across sites. The Laplacian `∇²` is the standard 5-point stencil on a periodic grid. The implicit linear solve is one 2D FFT (diagonal in Fourier), `O(N² log N)`.

**Why IMEX:** avoids the explicit-diffusion CFL bottleneck while keeping the nonlinear terms local in real space.

### 1.5 Noise injection

- **Spatial white:** noise drawn independently at each grid site per timestep.
- **Amplitude:** `√(2 σ² dt / Δx²) · 𝒩` with `𝒩 ∼ 𝒩(0, 1)`. The `1/Δx²` factor is the lattice regularisation of the delta function in 2D.
- **RNG:** NumPy `default_rng(seed)` with explicit per-realisation seeds for reproducibility.

### 1.6 Initialisation and equilibration

- **IC:** uniform random in [0.3, 0.7] (ED-Arch-01 canonical, seed 77 for the reference run).
- **Equilibration:** discard first `T_eq = 200` time units (~4000 steps at `dt = 0.05`) to reach the Scenario-D stationary noisy regime. Diagnostic: the field's spatial variance `⟨δ²⟩ − ⟨δ⟩²` should saturate before snapshots are taken.

### 1.7 Snapshot schedule

- After equilibration, take snapshots at intervals `Δt_snap = 50` (decorrelation time). Estimated correlation time ≈ `1/|P′| ≈ 0.5` for bulk; use `Δt_snap = 50` for safety.
- **Reference ensemble:** 200 snapshots per realisation × 10 realisations = 2000 snapshots.

---

## 2. Stationary-point detection

### 2.1 Discrete gradient

At each interior site `(i, j)`, compute the centred discrete gradient:

    g_x(i, j) = [ δ(i+1, j) − δ(i−1, j) ] / (2 Δx)
    g_y(i, j) = [ δ(i, j+1) − δ(i, j−1) ] / (2 Δx).

### 2.2 Sub-grid zero crossings

A 2D stationary point generically sits between grid sites. Use a **2×2 plaquette test**: a stationary point lies inside the plaquette with corners `(i, j), (i+1, j), (i, j+1), (i+1, j+1)` iff `g_x` and `g_y` each change sign across the plaquette.

For accepted plaquettes, **bilinearly refine** the (g_x = 0, g_y = 0) pair to sub-grid precision:

- Fit `g_x(ξ, η) = a + b ξ + c η + d ξη` (four-parameter bilinear) to the four corner values, and similarly for `g_y`.
- Solve the 2-by-2 nonlinear system `g_x = 0, g_y = 0` in `(ξ, η) ∈ [0, 1]²` by Newton iteration (2–3 steps converge).
- Reject if solution lies outside the plaquette (ambiguous).

### 2.3 Spatial Hessian K

At each accepted stationary point `x_0 = (i + ξ, j + η)`, evaluate the 2×2 spatial Hessian by centred finite differences *at the nearest grid site*, corrected to second order:

    K_xx = [ δ(i+1, j) − 2 δ(i, j) + δ(i−1, j) ] / Δx²
    K_yy = [ δ(i, j+1) − 2 δ(i, j) + δ(i, j−1) ] / Δx²
    K_xy = [ δ(i+1, j+1) − δ(i+1, j−1) − δ(i−1, j+1) + δ(i−1, j−1) ] / (4 Δx²)

For sub-grid correction, evaluate the Hessian of the fitted bicubic (or by bilinear interpolation of the four plaquette Hessians). In practice the nearest-site Hessian is adequate at `Δx = 1` for `κ ~ 1`.

### 2.4 Principal-axis diagonalisation

Diagonalise K → `(κ_1, κ_2)` with `|κ_1| ≥ |κ_2|`. Label as `κ∥ = κ_1` (axis with larger curvature magnitude) and `κ⊥ = κ_2` (orthogonal axis). Record the eigenvector angle θ as the motif orientation.

### 2.5 Classification

A stationary point is a **saddle** iff `κ_1 · κ_2 < 0`. Retain only saddles.

---

## 3. Motif filter implementation

Apply the ED-SC 2.0 canonical filter to each candidate saddle:

### 3.1 Amplitude threshold `δ_thr = 0.10`

Reject if `|δ(x_0)| < δ_thr`. Eliminates small-amplitude noise fluctuations.

### 3.2 Ray-threshold crossing `α = 0.25`

Define the **α-contour** as the set `{x : δ(x) ≥ α · δ(x_0)}`. Compute by marching-squares on the snapshot field.

- Find the connected component of the α-contour containing `x_0`.
- Measure the **major axis** `L_maj` and **minor axis** `L_min` of this component by PCA on the boundary coordinates (or by the longest chord through `x_0` vs. the orthogonal chord).

### 3.3 Ray length `L_ray ≥ 2`

Reject if `L_maj < L_ray · Δx = 2 Δx`. Equivalently, the α-contour must extend ≥ 2 grid spacings along the major axis.

### 3.4 D₂ symmetry check

The motif must be two-fold symmetric (not a single blob, not a triangle). Verify:

- **Aspect ratio:** `L_maj / L_min ≥ R_min` with `R_min = 1.5` (ray elongation).
- **Reflection symmetry:** compute `Δ_sym = ∫ |δ(x) − δ(R·x)| dx / ∫ |δ(x)| dx` where R is 180° rotation about `x_0` on a neighbourhood of radius `L_maj`. Reject if `Δ_sym > 0.2`.

### 3.5 Orientation alignment

The major axis of the α-contour should align (within 15°) with the eigenvector of K corresponding to `κ∥`. This enforces that the ray elongation and the spatial-curvature principal axis are the same direction. Reject otherwise.

### 3.6 Pre-registration

The five numerical filter parameters (`δ_thr = 0.10`, `α = 0.25`, `L_ray = 2`, `R_min = 1.5`, `Δ_sym ≤ 0.2`) are **pre-registered** per ED-SC 2.0 §1.4. They must not be retuned on the data. Variations are performed as **sensitivity analyses** only (§6.4), not as alternative canonical estimators.

---

## 4. Curvature extraction and r* computation

For each accepted motif:

### 4.1 Record

    δ_pt ≡ δ(x_0),     κ∥,     κ⊥,     s = κ∥/κ⊥,     θ (orientation).

### 4.2 Derived quantities

    μ = M₀ + ½ M₂ δ_pt²
    π = P₀ + ½ P₃ δ_pt²
    χ = 2 μ κ⊥² / P₀
    r*_pt = −2 χ / (2 χ − 1)        (per-motif r*; guard against |2χ−1| < 10⁻³).

### 4.3 Ensemble tables

Concatenate across all snapshots and realisations into a single table with columns
`(run_id, snapshot_id, x_0, δ_pt, κ∥, κ⊥, s, θ, μ, π, χ, r*_pt)`.

Expected table size at reference ensemble: `~10³–10⁴` accepted motifs.

---

## 5. Estimators

### 5.1 Point estimators

Over the ensemble table, compute:

    κ⊥*   ≡   median ( κ⊥ )                                           (5.1)
    s*    ≡   median ( κ∥ / κ⊥ )                                      (5.2)
    r*_motif ≡ median ( r*_pt )                                       (5.3)

(5.3) is the direct empirical analogue of the ED-SC 2.0 canonical r*.

### 5.2 Analytic-chain estimator

Alternatively, plug (5.1) into the closed-form asymptotic:

    χ*    =   2 μ* ( κ⊥* )² / P₀,   μ* = median(μ)
    r*_chain  ≡  −2 χ* / (2 χ* − 1).                                  (5.4)

Discrepancy between (5.3) and (5.4) diagnoses the validity of the leading-order asymptotic.

### 5.3 Confidence intervals

Bootstrap over **realisations** (not over motifs — motifs within a realisation are correlated):

- Resample the 10 realisations with replacement `B = 1000` times.
- Recompute (5.1)–(5.4) on each bootstrap sample.
- Report the 2.5% / 50% / 97.5% quantiles as the 95% CI.

### 5.4 Falsification decision

Report **PASS / FAIL / UNDECIDABLE** against the ED-SC 2.0 window `[−1.50, −1.10]`:

| Condition                                              | Verdict      |
|--------------------------------------------------------|--------------|
| Full 95% CI of `r*_motif` inside `[−1.50, −1.10]`      | PASS         |
| Full 95% CI outside `[−1.50, −1.10]`                   | FAIL         |
| CI straddles the boundary                              | UNDECIDABLE — extend ensemble |
| `r*_motif` and `r*_chain` disagree at > 2σ             | FLAG for analytic re-examination |

---

## 6. Diagnostics

### 6.1 Finite-size effects

Run at `L ∈ {64, 128, 256, 512}`. Report `r*_motif(L)` and test for a plateau as `L` grows. Extrapolate `L → ∞` by fitting `r*_motif(L) = r*_∞ + c/L²`.

Guardrail: `|r*_motif(512) − r*_motif(256)| < 0.02` before quoting the value.

### 6.2 Discretisation effects

Run at `Δx ∈ {1.0, 0.5, 0.25}` keeping `L` fixed. Test for a plateau as `Δx → 0`. Extrapolate via Richardson.

Guardrail: `|r*_motif(Δx=0.5) − r*_motif(Δx=0.25)| < 0.02`.

### 6.3 Noise-level effects

Run at `σ ∈ {0.03, 0.0556, 0.08, 0.12}` around canonical. Test ED-SC 2.0's claim that `r*` is σ-invariant within the motif-filter band. Expected: `r*_motif` is flat (within CI) across σ.

If `r*_motif` varies strongly with σ, ED-SC 2.0's σ-invariance claim is falsified — a distinct failure mode from r* outside the window.

### 6.4 Filter-parameter sensitivity (pre-registered)

Re-run at `α ∈ {0.20, 0.25, 0.30}`, `L_ray ∈ {1, 2, 3}`, `δ_thr ∈ {0.08, 0.10, 0.12}`. Report sensitivity coefficients `∂r*/∂α`, `∂r*/∂L_ray`, `∂r*/∂δ_thr`. A sensitivity > 0.5 (ED-SC 2.0 window-width) per 20% parameter change is a red flag — the filter is tuned.

### 6.5 Timestep / scheme consistency

Compare IMEX (§1.4) against fully explicit Euler at `dt = 0.01`. Expect `r*_motif` agreement within bootstrap CI.

### 6.6 Shape parameter s diagnostic

Report median `s = κ∥/κ⊥`. Anisotropy-memo closures predict:
- `s ≈ −1` (natural-amplitude closure, cubic nullcline) — Anisotropy §3.2
- `s ≈ −1.304` (ED-Arch-01 numerical, matches ED-SC 2.0 reference) — Extended memo §2

Measured `s` tests which closure is operative in the noisy ensemble.

### 6.7 Expected Monte-Carlo values

| Quantity   | Analytic prediction | Acceptance band     |
|------------|---------------------|---------------------|
| `κ⊥*`      | ≈ 1.04              | `[0.95, 1.15]`      |
| `s*`       | between −1 and −1.3 | `[−1.4, −0.9]`      |
| `r*_motif` | ≈ −1.304            | `[−1.50, −1.10]` (ED-SC 2.0 window) |
| `r*_chain` | ≈ −1.304            | `[−1.40, −1.20]` (tight) |

If all four land in their bands, the analytic chain is closed end-to-end.

---

## 7. Computational budget

Per realisation at reference size `L = 64`:

- Equilibration: 4000 steps at `5 × 10⁻⁵ s/step` (vectorised NumPy + FFT) ≈ 0.2 s.
- Sampling: 200 snapshots × 1000 steps/snapshot × `5 × 10⁻⁵` ≈ 10 s.
- Per-snapshot stationary-point detection + filter: ≈ 0.1 s.
- Per realisation: ≈ 30 s wall-clock.

Reference ensemble (10 realisations × 4 sizes × 4 σ-values × 3 filter-sensitivity variants) ≈ 10 × 48 × 30 s ≈ 4 hours on a single core; trivially parallelisable.

---

## 8. Deliverables

1. **Code:** `analysis/scripts/r_star_montecarlo/`
   - `spde_solver.py` — IMEX solver (§1).
   - `stationary_points.py` — detection + Hessian (§2).
   - `motif_filter.py` — ED-SC 2.0 filter (§3).
   - `r_star_estimators.py` — estimators + bootstrap (§5).
   - `diagnostics.py` — §6 sensitivity runs.
   - `run_reference.py` — reference ensemble orchestrator.

2. **Data:** `analysis/data/r_star_mc/`
   - One HDF5 file per realisation with the ensemble motif table.
   - Aggregated `reference_ensemble.parquet`.

3. **Results memo:** `theory/ED_SC_2_0_r_star_MonteCarlo_Results.md` (to be written after the run completes) with:
   - Reference estimates `(κ⊥*, s*, r*_motif, r*_chain)` with 95% CIs.
   - Diagnostic plots (§6).
   - PASS/FAIL/UNDECIDABLE verdict.
   - Comparison to ED-Arch-01's reported `−1.304`.

---

## 9. Related memos

- `theory/ED_SC_2_0_r_star_SaddleSolve.md` — diagnoses why the pure-PDE bounce gives `r* ≈ −1` instead of `−1.304` and flags this MC workflow as the closure step.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — closed-form `r* = −2χ/(2χ−1)`, target inversion `χ = 2.145 ⟺ κ⊥ ≈ 1.04`.
- `theory/ED_SC_2_0_r_star_Local_Geometry.md` — symbolic r* formula.
- `theory/ED_SC_2_0_r_star_Derivation_Extended.md` — 4-mode ansatz benchmark (`s ≈ 0.13 ⟹ κ∥/κ⊥ ≈ −1.3`).
- `docs/ED-SC-2.0.md` — canonical invariance statement + filter pre-registration.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory.
