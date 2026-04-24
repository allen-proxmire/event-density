# ED-SC 2.0 r*: Symmetry-Broken Ray-Forcing Monte-Carlo — Design Memo

**Status.** Design memo for the third MC pipeline in the r* arc. Follows
on [`ED_SC_2_0_r_star_MonteCarlo_Results.md`](ED_SC_2_0_r_star_MonteCarlo_Results.md)
(null result — pre-registered filter admits zero saddles of the bare
Scenario-D SPDE at any tested σ) and
[`ED_SC_2_0_r_star_Normalization_Audit.md`](ED_SC_2_0_r_star_Normalization_Audit.md)
(the analytic chain's cubic-penalty Taylor truncation is not the PDE
ED-Arch-01 integrates; the R2 reproduction uses concave mobility + concave
penalty + ray-endpoint filter). This memo specifies an experiment that
*keeps* the analytic-chain SPDE (so the target κ⊥ ≈ 1.04 retains its
formal meaning) and *adds* a localised anisotropic forcing term `F(x,y,t)`
designed to seed ray-like motifs near the natural amplitude `δ_nat = √6`.
The question under test: does a symmetry-broken seed produce saddles with
`κ⊥ ≈ 1.04`, `s ≈ −1.3`, `r* ≈ −1.304` in the analytic-chain PDE?

**Companion implementation (to be written).**
`analysis/scripts/r_star_mc_rayforce.py`.

---

## 1. Ray-forcing model

### 1.1 Forced SPDE

The analytic-chain Scenario-D SPDE with an external forcing term:

    ∂_t δ = ∇·(M(δ) ∇δ) − P(δ) + ξ(x,t) + F(x,y,t)              (1.1)

with canonical couplings `M₀ = 1, M₂ = 0, P₀ = 1, P₃ = −1` (so
`M(δ) = 1`, `P(δ) = δ − δ³/6`), noise `ξ` white-in-space-and-time with
amplitude σ, and `F` the anisotropic seed.

### 1.2 Ray profile

Gaussian ridge centred at `(x₀, y₀)`, aligned with x̂, with short
transverse width `σ_y` and long longitudinal width `σ_x`:

    F(x,y; t) = A · w(t) · exp(−(x−x₀)² / (2 σ_x²)) · exp(−(y−y₀)² / (2 σ_y²))   (1.2)

Window `w(t) = 1` for `t ∈ [0, T_seed]`, 0 afterward.

### 1.3 Amplitude and width calibration to δ_nat = √6

Goal: steady-state forced solution at the ridge centre has `δ(x₀,y₀) ≈ √6 ≈ 2.449`.

Linearising (1.1) around the ridge centre at quasi-steady state (drop
∂_t, keep leading Laplacian + linear penalty + the forcing):

    ∇²δ − δ + F ≈ 0                                             (1.3)

Fourier solution: `δ̂(k) = F̂(k) / (1 + k²)`. At the centre,

    δ(x₀,y₀) = ∫ F̂(k)/(1+k²) · d²k/(2π)²
             = A · σ_x σ_y · I(σ_x, σ_y)                        (1.4)

with `I(σ_x, σ_y) = ∫ exp(−½(σ_x² k_x² + σ_y² k_y²)) / (1+k²) · dk / (2π)`.
For `σ_x, σ_y ≫ 1` the `1+k²` factor reduces to 1 on the Gaussian's
support and `δ(x₀,y₀) → A`; for `σ_x, σ_y ≪ 1` the Yukawa Green's
function dominates and `δ(x₀,y₀) ∼ A σ_x σ_y · O(log)`.

**Calibration choice:** `σ_x = 6` (longitudinal), `σ_y = 1.2` (transverse),
`A = 2.8`. This gives a narrow ray (L_transverse ≈ 2σ_y = 2.4, matching
L_ray = 2 in the motif filter) with longitudinal extent ≈ 12 lattice
units (on a 64×64 grid, ≈ 1/5 of the domain), and amplitude calibrated
so that the numerical forced steady state yields `δ(x₀,y₀) ≈ √6 ± 10%`.
The amplitude `A = 2.8` is an initial estimate to be tuned by a small
pre-sweep (see §2.4).

### 1.4 Why δ_nat = √6

At the cubic nullcline `δ² = −6P₀/P₃ = 6` the linear-plus-cubic penalty
vanishes identically: `P(√6) = √6 − 6·√6/6 = 0`. The Anisotropy memo
(§3) shows this amplitude forces `s = −1` (exact leading order) and the
target value `κ⊥ ≈ 1.04` corresponds to a small fractional shift
`ε = (δ²/6) − 1 ≈ +0.07` (from the χ-inversion `χ = 2.145`). The
protocol is to create a ridge pinned at or just above √6, then let noise
anisotropically relax the tails.

### 1.5 Numerical notes on forcing implementation

- F is added in physical space, not Fourier, since the amplitude is
  O(1) and the profile is smooth on the lattice.
- For IMEX stability, F is added to the explicit source each step
  (does not modify the implicit linear part).
- Periodic wrap of the ridge is suppressed by placing `(x₀, y₀) = (32, 32)`
  at the grid centre and choosing `σ_x = 6 ≪ L/2 = 32` so tails at the
  boundary are `exp(−(L/2)²/2σ_x²) = exp(−14) ≈ 10⁻⁶`.

---

## 2. Protocol

### 2.1 Three-phase schedule

| phase         | steps                       | forcing  | noise  | purpose                          |
|---------------|-----------------------------|----------|--------|----------------------------------|
| 0 — IC        | n = 0                        | off      | off    | initial `δ ~ N(0, 0.01²)`        |
| 1 — seed      | 0 ≤ n < T_seed               | **on**   | on (σ) | forced ridge establishes motif   |
| 2 — relax     | T_seed ≤ n < T_seed + T_relax| off      | on (σ) | motif relaxes; noisy tails form  |
| 3 — sample    | T_seed + burn ≤ n < …        | off      | on (σ) | snapshot stationary points       |

with `T_seed = 400`, burn-in `T_burn = 100` after forcing turns off,
`T_relax` = 600 total post-forcing so sampling window is 500 steps,
snapshots every 25 steps → 20 snapshots/realisation. Total N_steps =
1000 per realisation. At `dt = 0.05` this is `t_phys = 50` — long enough
for relaxation, short enough that the motif has not yet fully decayed
(motif decay time τ_decay ≈ 1/κ⊥² ≈ 1 in canonical units, but a
*localised* structure at δ_nat is marginally stable because the cubic
nullcline kills the linear restoring force).

### 2.2 Parameters

- Grid: 64 × 64 periodic, dx = 1, dt = 0.05.
- Analytic-chain SPDE: M₀ = 1, M₂ = 0, P₀ = 1, P₃ = −1. IMEX Euler
  (same integrator as `r_star_montecarlo.py`).
- Noise σ: sweep {0.05, 0.10, 0.20, 0.40}; primary value σ = 0.20 (large
  enough to populate saddle structure, small enough that the forced
  ridge remains coherent).
- Initial condition: `δ₀ ~ N(0, 0.01²)` (small isotropic perturbation
  around zero; no secondary symmetry axis to compete with x̂).
- Forcing: `A = 2.8, σ_x = 6, σ_y = 1.2, x₀ = y₀ = 32`.
- N_realisations: 10 for the primary σ, 5 each for the sweep levels.
- Seeds: {77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021}.

### 2.3 Why turn off F before sampling

If F is on during sampling, the measured Hessian at the saddle is the
Hessian of the *forced* stationary solution, which is determined by the
forcing profile. We want the Hessian of the *relaxed* motif — a
meta-stable state that *remembers* the forcing's anisotropy but has
equilibrated under the full nonlinear SPDE. Post-force relaxation is
essential for the measured `κ∥, κ⊥` to be properties of the motif, not
of the forcing.

### 2.4 Pre-sweep for amplitude calibration

Run 3 realisations × 200 steps forced-only (no noise) at
`A ∈ {1.5, 2.0, 2.8, 4.0}` and measure `δ(x₀,y₀)` at t=10. Choose A
such that `δ(x₀,y₀) ∈ [√6·0.9, √6·1.1] ≈ [2.20, 2.69]`. Use that A for
the main sweep.

---

## 3. Motif filter

Apply the pre-registered ED-SC 2.0 filter from the Workflow memo,
unchanged:

- `δ_thr = 0.10` (amplitude threshold at the saddle point),
- `α = 0.25` (contour relative threshold),
- `L_ray = 2` (minimum major-axis half-length),
- `aspect ≥ 1.5` (PCA major/minor ratio of α-contour connected component),
- D₂ reflection-symmetry residual `≤ 0.20` (180° rotation about centre),
- orientation tolerance `≤ 15°` (major axis of α-cc vs κ∥ eigenvector
  of spatial Hessian).

**Difference from the isotropic MC run:** none. The filter is literally
re-used (imported from `r_star_montecarlo.py`). The question under test
is whether the *forcing* produces motifs that this *pre-registered
filter* admits — a null result here is meaningful because it would
indicate the filter is mis-specified even for deliberate anisotropic
seeds.

**Expectation:** under the forcing in §1, the primary motif at the ridge
centre has `aspect ≈ σ_x / σ_y = 5`, well above 1.5; its α-contour cc
is near-exactly D₂ symmetric (the forcing profile is D₂ symmetric in
(x,y) by construction); its major axis is exactly along x̂, which is
also the κ⊥ or κ∥ direction of the Hessian (determined by the sign of
the Laplacian along and across the ridge). N_motif_per_realisation
should be ≥ 1 (the primary ridge saddle) and possibly more from noise-
induced secondary structures along the ridge tails.

---

## 4. Measurements

For each snapshot, detect saddles (2×2 plaquette + bilinear Newton,
same as `r_star_montecarlo.py`). For each saddle that passes the motif
filter, compute and record:

- `x₀, y₀` — refined saddle position.
- `d_pt` — interpolated `δ` at the saddle.
- `κ∥, κ⊥` — Hessian eigenvalues ordered by |·| (κ∥ larger).
- `s = κ∥ / κ⊥` — signed ratio.
- `μ = M₀ + ½M₂ d_pt² = 1.0` (since M₂ = 0).
- `π = P₀ + ½P₃ d_pt² = 1 − d_pt²/2`.
- `χ = 2 μ κ⊥² / P₀ = 2 κ⊥²`.
- `r*_pt = −2χ / (2χ − 1)` (NaN if |2χ−1| < 10⁻³).
- Diagnostic: distance from ridge centre `r_from_seed = √((x₀−32)² + (y₀−32)²)`.
- Diagnostic: alignment of κ⊥ eigenvector with ŷ (the transverse
  direction of the forcing) in degrees.

### 4.1 Aggregation

- **Pooled** medians + IQR across all filter-admitted saddles.
- **Per-realisation** medians for bootstrap CI over realisations.
- **Stratified** by `r_from_seed`: the *primary* ridge saddle(s)
  (within r_from_seed ≤ 4) vs *secondary* saddles (r_from_seed > 4).
  Expected: primary saddles dominate and carry the target-like
  curvature; secondary saddles are noise-induced and behave like the
  isotropic MC population.

### 4.2 Bootstrap

Bootstrap 95% CI over realisations on per-realisation medians of
`|κ⊥|, s, r*_pt`, with B = 2000 resamples, same as previous runs.

---

## 5. Hypothesis test

### 5.1 Acceptance criteria for "ray forcing reproduces ED-SC 2.0 r*"

Primary ridge saddle median over realisations must fall in:

- `|κ⊥| ∈ [0.97, 1.10]`  (SaddleSolve §8 falsification band),
- `s ∈ [−1.50, −1.10]`   (ED-SC 2.0 canonical band),
- `r*_pt ∈ [−1.50, −1.10]`.

### 5.2 Failure modes and their interpretation

| observed                                    | interpretation                                                                             |
|---------------------------------------------|--------------------------------------------------------------------------------------------|
| κ⊥ ∈ target band, s in band, r* in band     | ED-SC 2.0 target reproduced; motif needs symmetry-broken seed; arc closed experimentally.  |
| κ⊥ too small (~0.01–0.2), s ~ −2.8          | Forcing does not build curvature beyond isotropic level; need larger A or longer T_seed.   |
| κ⊥ ≈ 10, s ≈ +1 (radial)                    | Forced state is a deterministic bounce (SaddleSolve regime); need less-intense forcing.     |
| κ⊥ in band but s ≫ |1| or s > 0             | Ridge is a peak or ridge maximum, not a saddle; adjust forcing sign or profile geometry.   |
| N_motif = 0                                 | Filter still rejecting even D₂-symmetric ray; filter is mis-specified independently of SPDE.|

### 5.3 Comparison baseline

| population                                    | κ⊥_med      | s_med      | r*_med      |
|-----------------------------------------------|-------------|------------|-------------|
| ED-SC 2.0 analytic target                     | 1.04        | −1.30      | −1.304      |
| Deterministic 2D bounce (SaddleSolve)         | 10.45       | +1.0       | −1.002      |
| Isotropic MC, σ=0.0556 (MonteCarlo_Results)   | 0.011       | −2.77      | +5×10⁻⁴     |
| Isotropic MC, σ=1.0 (MonteCarlo_Results)      | 0.20        | −2.77      | +0.11       |
| R2 canonical reproduction (non-analytic PDE)  | n/a*        | −1.304     | −1.304      |
| **Ray-forced MC (this design, expected)**      | **≈ 1.0**  | **≈ −1.3** | **≈ −1.3**  |

*R2 reports the signed Hessian eigenvalue ratio directly; it does not
compute κ⊥ against P₀, which has no direct meaning in R2's concave
penalty.

### 5.4 Decision

- **Pass criteria met at primary saddles (r_from_seed ≤ 4):** ED-SC 2.0
  target is confirmed as a property of symmetry-broken analytic-chain
  motifs; the arc's "one remaining number" is empirically accessible.
- **Pass for κ⊥ but not r*:** curvature scale matches but the s- and
  r*-dependence disagree; suggests the χ-formula (Anisotropy memo) is
  not quantitatively accurate at the ray-forced state.
- **Fail on all three:** the ED-SC 2.0 target is *not* a property of
  analytic-chain-PDE motifs even under anisotropic seeding — forcing
  the arc to conclude the target is *specifically* a property of the
  R2 concave PDE (Normalization Audit §5.2). At that point the arc
  transitions from "analytic chain predicts a measurable number" to
  "analytic chain gives formal structural form; quantitative number
  requires R2-form PDE".

---

## 6. Deliverables

### 6.1 Files

- **This memo:** `analysis/ED_SC_2_0_r_star_RayForcing_Design.md`
  (saved).
- **Implementation (pending):** `analysis/scripts/r_star_mc_rayforce.py`
  — a companion script with:
  - `forcing(t, step) -> np.ndarray` implementing (1.2) with the
    calibrated profile.
  - `imex_step_forced(delta, dt, lap_sym, rng, F)` — variant of the
    IMEX step that adds F to the explicit source.
  - `run_realisation_forced(seed, sigma, A, sigma_x, sigma_y)` —
    3-phase driver (IC → seed → relax+sample).
  - Amplitude pre-sweep helper (see §2.4).
  - Motif-filter import from `r_star_montecarlo.py` unchanged.
  - Bootstrap CI over realisations, stratified by r_from_seed.
  - JSON output schema matching `r_star_mc_nofilter.py` for
    cross-comparison.
- **Results memo (pending):**
  `analysis/ED_SC_2_0_r_star_RayForcing_Results.md` — written after
  implementation, with tables for primary + secondary saddles, the
  hypothesis-test outcome, and arc update.

### 6.2 Computational budget

- Pre-sweep amplitude calibration: 3 realisations × 200 steps ×
  4 amplitudes = ~30s.
- Primary run: 10 realisations × 1000 steps × 64² grid with IMEX ≈
  7 min (comparable to previous MC runs).
- σ sweep: 4 levels × 5 realisations × 1000 steps ≈ 14 min.
- Total ≈ 22 min.

### 6.3 Implementation sequencing

1. Port forcing profile and verify via deterministic (noise-off) run
   that `δ(x₀,y₀) ≈ √6` at t = 10 with the chosen A.
2. Confirm ridge stays localised and D₂-symmetric at end of T_seed
   (plot heatmap).
3. Run primary σ = 0.20 job at 10 realisations, report filter-admitted
   N_motif and primary-saddle medians.
4. If N_motif ≥ 5 per realisation on average, proceed to σ sweep;
   otherwise diagnose via relaxed filter and update design.
5. Write results memo; update arc memory (project_ed_r_star_analytic_arc.md)
   with the outcome.

---

## 7. Expected outcome and falsifiability

**Primary prediction (strong form):** the primary ridge saddle at the
forced-then-relaxed state has Hessian eigenvalue ratio
`s = κ∥/κ⊥ ∈ [−1.50, −1.10]` and `|κ⊥| ∈ [0.97, 1.10]`, so
`r*_pt ≈ −1.30` within ±15%. If this holds, the ED-SC 2.0 canonical
r* is empirically accessible in the analytic-chain PDE under
symmetry-broken seeding, and the arc's analytic closure is confirmed
end-to-end.

**Fallback prediction (weak form):** the primary ridge saddle has
`s ∈ [−2, −1]` but `|κ⊥|` misses the target band, confirming that
the Anisotropy memo's *shape parameter* closure (s = −1 at leading
order, s ≈ −1.3 with O(ε) correction) is robust under anisotropic
forcing, but the *curvature scale* κ⊥ is set by forcing geometry and
is not intrinsic to the PDE. This would refine the arc's claims to
structural-form only.

**Null (falsification):** no saddle with s ∈ [−1.5, −1.1] is admitted
by the filter anywhere in the primary or secondary populations across
all σ and seeds. This would indicate the ED-SC 2.0 target is intrinsic
to the R2 concave-PDE ingredients (per Normalization Audit §5.2) and
cannot be reproduced in the analytic-chain SPDE at all, closing the
arc with a structural rather than quantitative match.

---

## 8. Related memos

- `analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md` — pre-registered
  isotropic MC workflow.
- `analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md` — isotropic null
  result.
- `analysis/ED_SC_2_0_r_star_Normalization_Audit.md` — R2 vs analytic
  chain PDE mismatch; motivation for symmetry-broken seeding.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — χ-formula and s = −1
  leading-order closure that this experiment tests.
- `theory/ED_SC_2_0_r_star_SaddleSolve.md` — deterministic bounce
  diagnostic; provides the κ⊥ ∈ [0.97, 1.10] falsification band.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory, to
  be updated with the ray-forcing outcome after implementation.
