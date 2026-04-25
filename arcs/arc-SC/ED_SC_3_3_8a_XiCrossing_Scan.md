# ED-SC 3.3.8a — ξ-Crossing Selection Scan

**Status:** Pre-registration + execution-ready. Selects among the
coordinate remediations (A, B, D) proposed in ED-SC 3.3.8 §4.
**Parents:**
- `theory/ED_SC_3_3_8_CoordinateReconsideration.md` (predicts
  `ξ_crossing ≈ 1.964 lu` for the diagonal-ray `(1,1)→(2,2)`
  shell crossing under the canonical hinge `L_ray/ξ = 1.08`).
- `theory/ED_SC_3_3_6_PerSeedCollapse_40Snapshot.md` (40-snapshot
  per-seed protocol inherited).
- `theory/ED_SC_3_3_7_ShellHistogram_Diagnostic.md` (shell-
  histogram extraction + JS divergence methodology).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` §4.1
  (coordinate validity ξ ≲ 1.96 lu).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness
  + verdict taxonomy).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.8).

---

## 1. Purpose

ED-SC 3.3.8 predicted a diagonal-ray shell crossing
`(1, 1) → (2, 2)` at

    L_ray_crossing = 1.5 / 0.707 ≈ 2.121 lu,
    ξ_crossing     = L_ray_crossing / 1.08 ≈ 1.964 lu,

and proposed four candidate coordinate remediations (A shell-binned
hinge, B ξ-restricted invariance, D shell-aware effective
coordinate; C disqualified by Regime-I compatibility). The
selection requires an experiment that bridges the crossing.

**ED-SC 3.3.8a** executes an 11-point ξ scan across
`ξ ∈ [1.85, 2.10]` at Δξ = 0.025, bracketing `ξ_crossing ≈ 1.964`
with 5 points below and 5 points above (plus the crossing
neighbourhood at 1.95, 1.975, 2.00). The pass criteria and
verdict logic are pre-registered here; no free parameters remain.

---

## 2. Operating point

- **α_filt = 0.25** (canonical, fixed)
- **N_req = 4** (canonical, fixed)
- **L_ray_i = 1.08 · ξ_i** (canonical dimensionless hinge)
- **40 snapshots per ξ_i** (burn-in 100, snap every 10 —
  matches ED-SC 3.3.6 cadence; motifs pooled across 40 snapshots
  per scan point)
- **Fixed seed = 77** (the first canonical seed, providing
  reproducibility and a single-realisation signal at each ξ_i)
- **Simulator of record** unchanged: `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`; canonical parameters
  (alpha=0.03, gamma=0.5, noise_sigma=0.0556, mobility_exp=2.7,
  steps=500, size=64, dt=0.05, periodic boundary).

---

## 3. ξ-control method

Deliberate ξ-control via **initial-condition amplitude scaling**:

- Canonical IC is `rng.uniform(0.3, 0.7)` — half-width `w = 0.2`
  around mean 0.5. Smaller `w` → smoother IC → larger post-
  evolution coherence length ξ; larger `w` → noisier IC → smaller
  ξ.
- The driver performs a **calibration pre-pass** sweeping `w` over
  a coarse grid to measure the `w ↔ ξ` relationship on seed 77,
  then builds a monotone interpolant `w(ξ)` to select the IC
  half-width for each target ξ_target.
- Per scan point: evolve with the interpolated `w`; measure
  `ξ_measured` via the canonical 40-snapshot half-decay method;
  record `|ξ_measured − ξ_target| / ξ_target` as a miss fraction.
  If miss > 1 %, perform one bisection refinement of `w`.
- Fresh-seed sampling is rejected as an alternative: fresh seeds
  introduce uncontrolled variation in the motif-admission geometry
  (different spatial realisations). Amplitude-controlled IC on a
  single seed isolates ξ as the only varied quantity.

---

## 4. Measurements

For each of the 11 scan points `ξ_target ∈ {1.850, 1.875, 1.900,
1.925, 1.950, 1.975, 2.000, 2.025, 2.050, 2.075, 2.100}`:

1. Select `w = w_interp(ξ_target)` from the calibration
   interpolant.
2. Evolve with `rng.uniform(0.5 − w, 0.5 + w)` on seed 77 under
   the canonical parameters.
3. Extract 40 snapshots (burn-in 100, snap every 10).
4. Measure `ξ_measured = mean(xi_halfdecay(snapshot_k))`.
5. Compute `L_ray_i = 1.08 · ξ_measured`.
6. Collect motifs at `(α_filt = 0.25, N_req = 4, L_ray_i)` at
   each of the 40 snapshots; pool across snapshots.
7. Compute:
   - `N_i` — motif count
   - `S1_i, S2_i, S3_i` with bootstrap 16–84 CIs (4000 resamples)
   - endpoint shell histogram `H_i(r)` across all `4·N_i`
     endpoints
   - Jensen–Shannon divergence `JS(H_i, H_ref)` where `H_ref` is
     the ξ = 1.900 shell histogram (the reference point safely
     below the predicted crossing)
   - boolean `has_root8` — does shell √8 ≈ 2.828 appear in `H_i`?

The ξ = 1.900 point has `JS = 0` by construction (self-
comparison).

---

## 5. Pass/fail logic for remediations

Remediation selection is decided after all 11 points close:

### Remediation (B) — ξ-restricted invariance

**Selected iff all three hold:**

- `has_root8[i]` is False for all ξ_i < ξ_crossing and True for
  all ξ_i > ξ_crossing (monotone shell admission).
- `|S1_i − S1_ref|/|S1_ref| < 0.20` for all i (S1 stable across
  the crossing).
- `max_i (S2_i) − min_i (S2_i) > 0.20 · mean_i (S2_i)` **and**
  the max single-step finite difference `|S2_{i+1} − S2_i|`
  exceeds `0.20 · mean_i(S2_i)` at some `i = i*` with
  `ξ_{i*} ∈ [ξ_crossing − 0.05, ξ_crossing + 0.05]` (discrete
  S2 jump at the predicted crossing).

Interpretation: the coordinate `L_ray/ξ = 1.08` is sharp up to
`ξ_crossing` and breaks discretely above it; restricting the
invariance claim to ξ below the crossing (with a documented
exclusion analogous to L_ray Windows A, B) resolves the issue
without coordinate surgery.

### Remediation (A) — shell-binned hinge

**Selected iff:**

- `has_root8` is not monotone in ξ (appears / disappears
  intermittently across the scan), OR
- S2 does not show a clean single-threshold jump at the predicted
  crossing, OR
- S2 jumps appear at multiple ξ values correlated with multiple
  distinct shell-histogram reconfigurations.

Interpretation: the filter admits multiple shell-index classes
within the scanned range; a shell-binned coordinate is needed to
separate equivalence classes rather than a single continuous ξ
window.

### Remediation (D) — shell-aware coordinate

**Selected iff:**

- `has_root8` transitions monotonically near `ξ_crossing` (as in
  B), BUT
- S2 varies **smoothly** across the crossing (max single-step
  |ΔS2| ≤ 0.20 · mean_i(S2_i)); no discrete jump is detected.

Interpretation: shell geometry transitions discretely, but the
distributional invariant is smoothed by the 40-snapshot pool
averaging over snapshots in which different shell sets happen to
be admitted. A shell-aware piecewise-rescaling coordinate absorbs
the geometry without discarding the smoothness.

### Fallback

If none of the three verdicts applies (e.g. S1 varies
significantly across the scan, violating ED-SC 3.3.6's S1
invariance), the master verdict is **Inconsistent** and a new
memo is required to diagnose the broader S1 failure before any
remediation can be selected. This is a pre-registered escape
hatch; it should not trigger under the current state of the arc.

---

## 6. Deliverables

- `outputs/ed_sc_3_3_8a/xi_scan_summary.json` — master summary:
  - `xi_targets[]`, `xi_measured[]`, `xi_miss_fraction[]`
  - per-point `(N_i, S1_i, S2_i, S3_i, S1_CI, S2_CI)`
  - per-point `shell_histogram[]` (dict of shell → count)
  - per-point `has_root8[]`, `root8_count[]`, `root8_fraction[]`
  - per-point `JS_vs_ref[]` (ref = ξ = 1.900)
  - `crossing_index` — first `i` where `has_root8[i]` is True,
    or `null` if never admitted
  - `S2_discontinuity_index` — `i` where finite |S2_{i+1} − S2_i|
    is maximal, plus the amplitude
  - `remediation_verdict ∈ {A, B, D, Inconsistent}`
  - `calibration_pass` — w-grid, ξ-measured, interpolant
    coefficients (audit trail for the IC-amplitude method)
- `outputs/ed_sc_3_3_8a/xi_scan_table.csv` — one row per scan
  point with flat columns for downstream plotting.

Artefacts live under `outputs/ed_sc_3_3_8a/` (new directory,
created by the driver).

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.8a as the
  execution-ready selection experiment for the coordinate
  remediations of ED-SC 3.3.8. Pre-registers the 11-point
  Δξ = 0.025 scan across ξ ∈ [1.85, 2.10] bracketing
  `ξ_crossing ≈ 1.964`, the deliberate IC-amplitude ξ-control
  method, the fixed seed (77), the measurement list (including
  shell histograms and JS vs ξ = 1.900 reference), and the
  (A/B/D/Inconsistent) verdict logic. No free parameters remain;
  the driver is self-contained. No numerics.
