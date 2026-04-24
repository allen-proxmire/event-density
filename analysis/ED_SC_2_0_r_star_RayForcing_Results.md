# ED-SC 2.0 r*: Ray-Forcing Monte-Carlo — Results

**Status.** Empirical results for the symmetry-broken Monte-Carlo pipeline
specified in
[`ED_SC_2_0_r_star_RayForcing_Design.md`](ED_SC_2_0_r_star_RayForcing_Design.md).
Headline: **the symmetry-broken-seed hypothesis is rejected.** A localised,
saddle-inducing quadrupolar forcing applied to the analytic-chain Scenario-D
SPDE, followed by relaxation under noise, produces a saddle population whose
curvature statistics are **indistinguishable from the isotropic MC
population** — κ⊥_med ∈ [0.010, 0.079] across σ ∈ {0.05, 0.20, 0.40}, s_med
≈ −2.76, r*_med ∈ [4×10⁻⁴, 0.028]. The pre-registered ED-SC 2.0 filter
admits zero motifs throughout. Combined with the
[Normalization Audit](ED_SC_2_0_r_star_Normalization_Audit.md), this
strongly supports the reading that `r* = −1.304` is a property of the R2
concave-PDE simulator (§5.2 of the audit), not of the analytic-chain
cubic-bistable SPDE under any seeding protocol tested so far.

**Companion scripts.**
- [`analysis/scripts/r_star_mc_rayforce.py`](scripts/r_star_mc_rayforce.py)
  — primary ray-forced MC with pre-registered filter.
- [`analysis/scripts/r_star_mc_rayforce_nofilter.py`](scripts/r_star_mc_rayforce_nofilter.py)
  — supplementary no-filter saddle-population measurement.

---

## 1. Design amendment: Gaussian-ridge → quadrupolar forcing

The Design memo §1.2 specified a Gaussian-ridge forcing

    F(x,y) = A · exp(−(x−x₀)² / 2σ_x²) · exp(−(y−y₀)² / 2σ_y²)

with σ_x ≫ σ_y. Implementation showed this seeds a local *maximum* at
(x₀, y₀) (both Hessian eigenvalues negative) rather than a saddle.
Because the pre-registered filter requires κ∥ · κ⊥ < 0 (saddle, indefinite
Hessian), a peak-shaped seed is rejected by construction. Additionally,
for a cubic-bistable penalty `P(δ) = δ − δ³/6`, amplitudes above √6 are
unstable and the forced steady state blows up for A ≳ 1.8 at the Design
memo's chosen widths (observed during the first run, seed-77 row; see
`rayforce_err.log`).

**Replacement forcing.** A clean Morse-saddle-seeding quadrupole:

    F(x,y) = A · (x̃²/σ_x² − ỹ²/σ_y²) · exp(−(x̃² + ỹ²) / 2σ²)           (1.1)

with `x̃ = x − x₀, ỹ = y − y₀, σ = min(σ_x, σ_y)`. At origin `F = 0`, and
the steady-state induced field has Hessian eigenvalues of opposite sign
along x̂ and ŷ — a textbook saddle. Widths `σ_x = σ_y = 3.0` produce
s_seed = −1 by symmetry (matching the Anisotropy-memo leading-order
closure); unequal widths tune s_seed away from −1 but were not needed
for this first test.

**Calibration (deterministic, noise off, 200 steps, seed 0):**

    A = 0.25  d_max = 0.129
    A = 0.50  d_max = 0.260
    A = 1.00  d_max = 0.530
    A = 1.50  d_max = 0.827
    A = 2.00  d_max = 1.186

All stable (no blowup). Largest tested amplitude `A = 2.0` gives
d_max ≈ 1.19 (about half of √6). Adopted for main runs.

---

## 2. Pre-registered filter run (3 seeds, aborted after null)

Main run `r_star_mc_rayforce.py` with filter enabled, σ = 0.20, A = 2.0,
T_seed = 300, T_relax = 800, T_burn = 100, snap_every = 20, 64×64
periodic grid:

| seed | d_centre end-of-seed | d_max end-of-seed | filter-admitted motifs | primary (r ≤ 4) |
|------|----------------------|-------------------|-------------------------|------------------|
| 77   | 0.085                | 1.341             | **0**                   | 0                |
| 123  | −0.033               | 1.279             | **0**                   | 0                |
| 456  | 0.016                | 1.294             | **0**                   | 0                |

Run was aborted after three consecutive zero-motif realisations: the
rejection is systematic, not stochastic. The primary ridge saddle at the
seed centre has `d_pt ≈ 0` by the quadrupole's D₂ symmetry, failing the
`δ_thr = 0.10` amplitude gate before any other filter test runs. This
reveals an **internal incompatibility in the pre-registered filter as
specified**: the filter requires both (a) a saddle (κ∥·κ⊥ < 0, so the
field cannot have a simple peak at the centre) and (b) amplitude
`|d_pt| ≥ 0.10` at the saddle point. At a generic Morse saddle in a
zero-mean field, the field value at the saddle is approximately zero.
Requirement (b) is only compatible with (a) for saddles that sit on a
background field with nonzero local mean — which in the R2 reconstruction
is `p̂ ≈ 0.108`, the field's stationary-state mean (see
Normalization Audit §2).

**The pre-registered filter as copied from the R2 "ray-endpoint" test to
the Workflow memo's "α-contour D₂" form has lost the R2 baseline-mean
structure.** This is a filter-specification bug independent of the PDE
mismatch already diagnosed in the Normalization Audit.

---

## 3. Supplementary: no-filter saddle population (5 seeds × 3 σ)

Script `r_star_mc_rayforce_nofilter.py` drops the motif filter entirely
and measures the raw saddle statistics. "Primary" saddles are those
within radius R = 4 of the seed centre (x₀=y₀=32); "all" includes the
whole 64×64 grid.

### 3.1 Per-configuration totals

| σ    | A | saddles (all, 5 seeds) | saddles (primary, r ≤ 4) | d_peak after seed (median) |
|------|---|-------------------------|---------------------------|------------------------------|
| 0.05 | 2 | 77,367                  | 942                       | 1.21                         |
| 0.20 | 2 | 77,403                  | 938                       | 1.29                         |
| 0.40 | 2 | 77,394                  | 951                       | 1.44                         |

Primary density ≈ π · 4² / 64² ≈ 1.23% of total, matching the observed
~1.22% directly — primary region has the same saddle density as the
bulk, not an enhancement.

### 3.2 Curvature + r* medians with bootstrap-95 over realisations

| σ    | scope   | \|κ⊥\|_med | s_med  | r*_med  | d_pt_med | χ_med  |
|------|---------|------------|--------|---------|----------|--------|
| 0.05 | all     | 0.0099     | −2.75  | +3.9e−4 | +2.5e−4  | 0.0002 |
| 0.05 | primary | 0.0105     | −2.69  | +4.4e−4 | +3.1e−4  | 0.0002 |
| 0.20 | all     | 0.0396     | −2.76  | +6.3e−3 | +1.4e−3  | 0.0031 |
| 0.20 | primary | 0.0419     | −2.69  | +7.1e−3 | −2.3e−4  | 0.0035 |
| 0.40 | all     | 0.0794     | −2.76  | +2.6e−2 | +2.5e−4  | 0.0126 |
| 0.40 | primary | 0.0828     | −2.75  | +2.8e−2 | −1.2e−4  | 0.0137 |

**Bootstrap-95 CI over realisations (primary scope):**

| σ    | κ⊥ 95% CI                 | s 95% CI                   | r* 95% CI                    |
|------|---------------------------|----------------------------|-------------------------------|
| 0.05 | [0.0101, 0.0114]          | [−2.88, −2.48]             | [4.1e−4, 5.2e−4]              |
| 0.20 | [0.0403, 0.0453]          | [−2.85, −2.49]             | [6.5e−3, 8.3e−3]              |
| 0.40 | [0.0804, 0.0907]          | [−2.90, −2.49]             | [2.6e−2, 3.4e−2]              |

Per-realisation medians have 2-10% variation only — consistent with
~190 saddles per primary region per realisation giving tight medians.

### 3.3 Comparison to targets and previous runs

| population                                                        | \|κ⊥\|_med | s_med  | r*_med  |
|-------------------------------------------------------------------|------------|--------|---------|
| ED-SC 2.0 analytic target                                          | 1.04       | −1.30  | −1.304  |
| Deterministic 2D bounce (SaddleSolve)                              | 10.45      | +1.0   | −1.00   |
| Isotropic MC, σ = 0.0556 (MonteCarlo_Results)                      | 0.011      | −2.77  | +5e−4   |
| Isotropic MC, σ = 1.0 (MonteCarlo_Results)                         | 0.199      | −2.77  | +0.11   |
| **Ray-forced, σ = 0.05, primary (this memo)**                       | **0.011**  | **−2.69** | **+4e−4** |
| **Ray-forced, σ = 0.20, primary (this memo)**                       | **0.042**  | **−2.69** | **+7e−3** |
| **Ray-forced, σ = 0.40, primary (this memo)**                       | **0.083**  | **−2.75** | **+3e−2** |
| R2 canonical reproduction (concave PDE + ray-endpoint filter)      | n/a        | −1.304 | −1.304  |

---

## 4. Hypothesis test

### 4.1 Acceptance criteria (from Design §5.1)

Primary-saddle medians should fall in:
- `|κ⊥| ∈ [0.97, 1.10]`
- `s ∈ [−1.50, −1.10]`
- `r* ∈ [−1.50, −1.10]`

### 4.2 Observed

| quantity | σ=0.05 primary | σ=0.20 primary | σ=0.40 primary | in band? |
|----------|-----------------|-----------------|-----------------|-----------|
| \|κ⊥\|    | 0.011           | 0.042           | 0.083           | **no**    |
| s        | −2.69           | −2.69           | −2.75           | **no**    |
| r*       | +4e−4           | +7e−3           | +3e−2           | **no** (and wrong sign) |

All three quantities fall outside their acceptance bands at all three σ
levels. The forcing does not shift the saddle population toward the
target.

### 4.3 Mechanism of the null

The quadrupolar forcing creates a *deterministic* saddle at the centre
with exact s = −1 during the seeding phase (phase 1 of the protocol).
After T_seed = 300 steps of forcing + noise, the induced field has
`d_peak ≈ 1.2–1.7`, indicating the seeded motif is only about half the
natural amplitude √6 ≈ 2.45.

Once forcing is turned off (phase 2), the seeded motif *decays*
exponentially with timescale τ ≈ 1/P₀ = 1 (canonical units). Within
T_burn = 100 steps (physical time 5), the deterministic contribution has
decayed by `e^{−5} ≈ 0.007` relative to its seed-end amplitude, well
below the noise fluctuation level. The sampling window (steps 100–800
post-forcing) therefore contains *only noise-induced saddles*, which are
statistically indistinguishable from the isotropic-MC baseline.

**Comparison: σ=0.20 primary κ⊥ (ray-forced) = 0.042 vs σ=0.20 isotropic
would be ≈ 0.04 by linear-noise scaling (2× σ from σ=0.0556 gives
0.011 × (0.20/0.0556)² = 0.14? No — κ⊥ scales linearly with field std
which scales linearly with σ for linearised SPDE, so ≈ 0.040).** The
ray-forced primary region's κ⊥ ≈ 0.042 at σ=0.20 is essentially the
isotropic prediction — confirming the seeded structure has fully
decayed by the sampling window.

### 4.4 Decay diagnostic: σ=0.05 d_pt_med ≈ 3e−4 ≪ d_peak = 1.21

The median d_pt at saddles in the σ=0.05 primary region is 3×10⁻⁴ — six
orders of magnitude below the seed-phase peak amplitude. Even at
σ=0.40, the median d_pt at primary saddles is only ±10⁻⁴ vs seeded peak
1.44. This is the quantitative signature of complete decay of the
deterministic motif before sampling begins.

---

## 5. Interpretation

The χ < ½ branch question from Design §5 is answered clearly:

**All ray-forced primary-saddle populations tested sit in the χ < ½
branch**: χ_med ∈ [2×10⁻⁴, 1.4×10⁻²] across σ, far from the χ = 2.145
threshold needed for r* = −1.304 (or even the χ = 0.5 crossover). The
r*-formula `−2χ/(2χ−1)` on this branch gives small positive r*, just as
in the isotropic MC case.

**The noise-induced saddle population has a universal shape:** s_med
≈ −2.7 across all σ from 0.05 to 1.0, and across isotropic and
forced-then-relaxed protocols. This is the characteristic shape of
saddle points of a 2D Gaussian random field with the linearised SPDE's
dispersion `ω² = k² + 1`. It is not −1.30.

**The ridge persistence time τ_decay ≈ 1/P₀ = 1 at canonical M₀=P₀=1 is
too short relative to the sampling window.** A possible follow-up is
to sample *during* the seed phase (forcing on), capturing the seeded
saddle while it is still deterministic — but that measures the
forcing's curvature, not a relaxed motif's curvature.

### 5.1 Updated diagnosis

The three candidate readings from the Results §5 and Audit §5 of the
null-result memos reduce to one:

- Normalization mismatch (§5.1 of Results): *not the driver* — χ is
  dimensionless, Audit §1.5 showed r* is normalization-invariant.
- Symmetry-broken seeding (§5.2 of Results / §4 of Audit): *falsified
  by this memo* — ray forcing does not shift the population.
- R2-form PDE is the actual data-generating process (§5.2 of Audit):
  **supported by all three MC pipelines' null results**. The target
  r* = −1.304 is reproduced only by R2's concave mobility + concave
  penalty + ray-endpoint filter, not by the cubic-bistable analytic
  chain + α-contour D₂ filter at *any* noise level or seeding protocol.

### 5.2 Pre-registered filter bug

Independently of the PDE mismatch, §2 of this memo uncovered an
**internal inconsistency in the α-contour D₂ filter as specified in the
Workflow memo**: the `δ_thr = 0.10` amplitude gate is incompatible with
Morse saddles in a zero-mean field, because a Morse saddle generically
has `d_pt ≈ 0`. In the R2 original, the analogous threshold is the
*ray-endpoint* test relative to the stationary field mean `p̂ ≈ 0.108`,
not the saddle-point amplitude itself. The Workflow memo's mistranslation
drops the baseline subtraction. Any future filter implementation should
re-derive the gate against the R2 ray-endpoint form.

---

## 6. Next-step options

Given the strong triple-null across isotropic, quadrupole-forced, and
R2-mismatch diagnostics, the arc's analytic closure at leading order
stands, but its empirical closure requires porting to the R2 form.
Three options, in order of invasiveness:

1. **R2-port of the MC pipeline** (most direct). Swap the SPDE to
   `p_{t+1} = p + dt[∇·(M(p)∇p) − α p^γ + σ η]` with
   `M(p) = ((1−p)/1)^{2.7}`, α=0.03, γ=0.5, σ=0.0556, periodic BCs,
   IC p₀ ~ U(0.3, 0.7). Apply the R2 ray-endpoint filter (from
   `r2_motif_filter.py`) and measure `λ₁/λ₂` at admitted saddles.
   Expected: N ≈ 6 per realisation, median −1.304. This is a
   reproduction test, not a prediction test.

2. **R2-form analytic chain** (most interesting). Re-derive the
   Anisotropy memo's closed form with concave mobility + concave
   penalty Taylor-expanded to O(δ²) about `p̂` rather than cubic-bistable
   about δ=0. Recover the analogue of `r* = −2χ/(2χ−1)` for R2 and
   check whether the χ-inversion gives a different empirical scalar
   consistent with R2's measured −1.304.

3. **Accept the arc as structurally closed** (most honest).
   Conclusion: the analytic chain derives the *form* of r* as a
   function of a single motif scalar (χ or equivalent); the
   *quantitative* target −1.304 is set by the R2 simulator's specific
   PDE + filter ingredients, not by the leading-order analytic SPDE.
   Update the arc memory with this as the final reading.

---

## 7. Closed result (update)

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │  Three MC pipelines on the analytic-chain (cubic-bistable)        │
    │  Scenario-D SPDE have been run:                                   │
    │                                                                  │
    │    (1) Isotropic noise + pre-registered D2 filter                 │
    │        → 0 motifs at all tested sigma                             │
    │    (2) Isotropic noise, no filter                                  │
    │        → |kappa_perp| ≈ 0.011–0.20,  s ≈ −2.77,  r* ≈ +5e−4..0.11 │
    │    (3) Quadrupolar forcing + relaxation, primary region           │
    │        → |kappa_perp| ≈ 0.011–0.083, s ≈ −2.70, r* ≈ +4e−4..3e−2 │
    │                                                                  │
    │  None reproduce the ED-SC 2.0 target:                            │
    │        |kappa_perp| ≈ 1.04,  s ≈ −1.3,  r* = −1.304              │
    │                                                                  │
    │  The R2 reproduction (concave mobility + concave penalty +       │
    │  ray-endpoint filter at sigma* = 0.0556) DOES reproduce r* =     │
    │  −1.304 with N_motif = 6. The target is a property of the R2     │
    │  simulator's specific PDE form, not of the analytic chain's      │
    │  cubic truncation under any seeding tested.                      │
    │                                                                  │
    │  Additionally, the Workflow memo's motif-filter specification    │
    │  has an internal inconsistency (delta_thr = 0.10 at a saddle     │
    │  whose generic d_pt = 0), traced to a mistranslation from the    │
    │  R2 ray-endpoint test.                                            │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

---

## 8. Related memos

- `analysis/ED_SC_2_0_r_star_RayForcing_Design.md` — design spec this
  memo implements (with the one amendment in §1 above).
- `analysis/ED_SC_2_0_r_star_Normalization_Audit.md` — the R2-vs-
  analytic-chain diagnosis that this memo's triple-null corroborates.
- `analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md` — isotropic null
  result.
- `analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md` — the motif filter
  specification whose §3.1 inconsistency is flagged in §5.2 above.
- `analysis/scripts/ed_arch_r2/R2_Motif_Verdict.md` — the R2 canonical
  reproduction that does match −1.304 under its own ingredients.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory,
  to be updated with the triple-null and R2 reading.
