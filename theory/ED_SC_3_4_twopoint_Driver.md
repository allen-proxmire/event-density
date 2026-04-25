# ED-SC 3.4 Two-Point — F4 Driver Specification

**Status:** Driver specification memo. Translates the F4
scoping architecture (`theory/ED_SC_3_4_twopoint_Scoping.md`)
into a concrete, executable driver specification. Pairs with
`analysis/scripts/ed_sc_3_4_twopoint_correlation.py` (to be
written in the same turn). No execution; scope-only for the
driver itself, but the memo is detailed enough that the driver
can be written in one pass.
**Parents:**
- `theory/ED_SC_3_4_twopoint_Scoping.md` (F4 scoping; r-grid,
  estimator definitions, uncertainty structure, follow-up
  memo chain).
- `theory/GR_SC_1_7_Redshift_MotifStatistics.md` (tenth-pass
  `C_redshift(r)` derivation; pooled-R2 half-rise compression
  prediction `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05`).
- `theory/GR_SC_2_0_Consolidation_Amendment.md` (sixteenth-pass
  ensemble-vs-single-seed guardrail).
- `analysis/scripts/ed_sc_3_4_sigma1_multiseed.py` (F2 driver;
  structural precedent — identical seed loop, IC-amplitude
  calibration, 40-snapshot cadence).
- `analysis/scripts/ed_sc_3_4_sigma1_model_verify.py` (F3-verify
  driver; precedent for post-processing on regenerated F2
  fields).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post F4 scoping).

---

## 1. Purpose

The F4 scoping memo (§5.1) requires a full driver specification
concrete enough to be implemented in a single pass. This memo
provides it:

- **Input definitions:** seed set, ξ_canonical, calibration
  schedule, r-grid, admissibility thresholds.
- **Driver architecture:** loop structure, data structures,
  pair enumeration, r-binning, correlation estimators,
  bootstrap, per-seed CoV.
- **Outputs:** three artefact files with exact column specs.
- **Verdict logic:** falsifier test against the GR-SC 1.7
  half-rise compression prediction.

The companion driver `analysis/scripts/ed_sc_3_4_twopoint_correlation.py`
implements the spec verbatim.

---

## 2. Inputs

| input | value | notes |
|---|---|---|
| Seed set | `{11, 22, 33, 44, 55, 66, 77, 88, 99, 111}` | matches F2 / F3-verify |
| `ξ_canonical` | 1.7575 lu | `r_½^{unfilt}` baseline (see §3.1) |
| Filter geometry | `α_filt = 0.25, N_req = 4` | canonical |
| Hinge | `L_ray = 1.08 · ξ_measured` per seed | canonical |
| Snapshot cadence | burn-in 100, snap every 10, 40 snaps/seed | F2 inherited |
| IC-amplitude calibration | 9-point w-sweep + monotone interpolant + 1-step bisection | F2/F3-verify inherited |
| r-grid | `{0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0}` | 10 points, Δr = 0.5 lu |
| r-bin width | `Δr = 0.5` | symmetric assignment `[r_k − 0.25, r_k + 0.25)` |
| Minimum pairs per ensemble r-bin | 20 | below: flagged `low-N` |
| Minimum pairs per per-seed r-bin | 10 | below: excluded from CoV |
| Periodic-boundary convention | minimum image on 64² torus | see §3.2 |
| r_diag guard | `round(0.707 · L_ray) = 1` per seed | ED-SC 3.0 rev. 3 |
| Resonance-window guard | `L_ray ∉ [2.50, 2.80] ∪ [3.50, 3.90]` | ED-SC 3.2.6 |
| Bootstrap resamples | 4000 per r-bin (pair-resample) | |
| RNG seed for bootstrap | 99 | for determinism |

### 2.1 Simulator constants (unchanged; inherited from `r2_grf_falsifier_tests`)

    alpha = 0.03, gamma = 0.5, noise_sigma = 0.0556,
    mobility_exp = 2.7, steps = 500, size = 64, dt = 0.05,
    p_min = 0.01, p_max = 1.0, boundary = "periodic".

No simulator constants are mutated.

---

## 3. Driver architecture

### 3.1 Top-level control flow

```
main():
    1. Pre-flight guards
       - assert_no_resonance(xi_canonical)
       - ensure OUT_DIR exists

    2. Per-seed evolution + motif extraction
       for seed in SEEDS:
           calibration = run_calibration_for_seed(seed)
           w_target = interpolate_w(calibration, XI_CANONICAL)
           (snapshots, xis_measured) = evolve_40snap(seed, w_target)
           [bisection refinement if miss > 1%]
           xi_measured = mean(xis_measured)
           L_ray_seed = 1.08 * xi_measured
           assert r_diag(L_ray_seed) == 1
           motifs_per_snap = []
           for p in snapshots:
               motifs = extract_motifs_with_positions(p, L_ray_seed)
               motifs_per_snap.append(motifs)
           per_seed_results[seed] = (xi_measured, L_ray_seed,
                                      motifs_per_snap)

    3. Global pool ρ̄ computation
       - Pool all admitted motifs across seeds & snapshots
       - Compute ρ̄ = mean(ρ across pool)
       - Compute σ²_ρ = var(ρ across pool)

    4. Per-seed per-snapshot pair enumeration + r-binning
       pair_pool_per_seed = {seed: {r_bin: [(ρ_i, ρ_j)]}}
       for seed, (_, _, motifs_per_snap) in per_seed_results:
           for snap_motifs in motifs_per_snap:
               for i < j in enumerate(snap_motifs):
                   r = min_image_distance(pos_i, pos_j, L=SIZE)
                   bin_k = r_bin_assign(r, R_GRID)
                   if bin_k is None: continue
                   pair_pool_per_seed[seed][bin_k].append((ρ_i, ρ_j))

    5. Ensemble r-bin aggregation
       ensemble_pool[r_bin] = concat(pair_pool_per_seed[seed][r_bin]
                                      for seed in SEEDS)
       for r_bin:
           C_ensemble, C_lo, C_hi = bootstrap_C(ensemble_pool[r_bin])
           C_rank = spearman_C(ensemble_pool[r_bin])
           model_band_rel = |C_ensemble - C_rank| / |C_ensemble|

    6. Per-seed r-bin aggregation
       for seed, r_bin:
           C_seed = pearson_C(pair_pool_per_seed[seed][r_bin])
       for r_bin:
           CoV_across_seeds[r_bin] = std(C_seed) / mean(C_seed)

    7. Half-rise interpolation
       r_half_filt = linear_interp(C_ensemble(r) = 1, R_GRID)
       r_half_unfilt = XI_CANONICAL
       ratio = r_half_filt / r_half_unfilt
       bootstrap: ratio distribution via re-interpolating on
                  each of the 4000 ensemble resamples

    8. Verdict logic (§3.7)

    9. Write CSV + JSON outputs (§4)
```

### 3.2 Minimum-image periodic-boundary distance

For two motif positions `(i₁, j₁)` and `(i₂, j₂)` on the 64² torus:

```python
def min_image_distance(p1, p2, L=64):
    di = abs(p1[0] - p2[0])
    dj = abs(p1[1] - p2[1])
    di = min(di, L - di)
    dj = min(dj, L - dj)
    return math.sqrt(di * di + dj * dj)
```

Maximum representable distance: `√(32² + 32²) = 45.25 lu`.
Well above the 5.0 lu r-grid upper limit.

### 3.3 r-bin assignment

```python
def r_bin_assign(r, r_grid, dr=0.5):
    """Return bin index k such that |r - r_grid[k]| < dr/2,
    or None if r is outside all bins."""
    for k, r_k in enumerate(r_grid):
        if r_k - dr/2 <= r < r_k + dr/2:
            return k
    return None
```

Pre-registered policy: pairs at `r < 0.25` or `r ≥ 5.25` are
dropped (not assigned). The `r = 0.5` bin covers `[0.25, 0.75)`;
the `r = 5.0` bin covers `[4.75, 5.25)`.

### 3.4 Motif extraction with position

```python
def extract_motifs_with_positions(snapshot, L_ray):
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    motifs = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        motifs.append({
            "i": int(s["i"]),
            "j": int(s["j"]),
            "rho": float(s["ratio"]),
        })
    return motifs
```

### 3.5 Correlation estimators

**Pearson (product-moment) estimator** at r-bin with pair pool
`P = [(x_k, y_k) for k = 1..N]`:

```python
def pearson_C(P, rho_bar, var_rho):
    if len(P) < 2:
        return None
    xs = np.array([p[0] for p in P])
    ys = np.array([p[1] for p in P])
    # Centred-product estimate of xi_phi(r) / sigma_0^2
    corr = np.mean((xs - rho_bar) * (ys - rho_bar)) / var_rho
    return 2.0 * (1.0 - corr)
```

Uses the **global pool** `ρ̄` and `σ²_ρ` (computed in step 3
of §3.1), matching the GR-SC 1.7 definition
`C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]`.

**Spearman (rank-correlation) estimator** at r-bin with pair
pool `P`:

```python
from scipy.stats import spearmanr

def spearman_C(P):
    if len(P) < 3:
        return None
    xs = np.array([p[0] for p in P])
    ys = np.array([p[1] for p in P])
    rho_s, _ = spearmanr(xs, ys)
    if not np.isfinite(rho_s):
        return None
    return 2.0 * (1.0 - rho_s)
```

The Spearman correlation replaces the Pearson correlation
coefficient with its rank-order equivalent, bypassing
distributional assumptions on ρ. Model-band relative difference
quantifies the sensitivity of `C(r)` to the Pearson assumption.

### 3.6 Bootstrap

```python
def bootstrap_C_ensemble(pair_pool, rho_bar, var_rho,
                         B=4000, rng_seed=99):
    rng = np.random.default_rng(rng_seed)
    N = len(pair_pool)
    if N < 20:  # low-N gate
        return {
            "C": None, "C_CI_lo": None, "C_CI_hi": None,
            "low_N": True,
        }
    xs = np.array([p[0] for p in pair_pool])
    ys = np.array([p[1] for p in pair_pool])
    C_values = []
    for _ in range(B):
        idx = rng.integers(0, N, size=N)
        resample_xs = xs[idx]
        resample_ys = ys[idx]
        corr = np.mean((resample_xs - rho_bar)
                        * (resample_ys - rho_bar)) / var_rho
        C_values.append(2.0 * (1.0 - corr))
    C_central = pearson_C(list(zip(xs, ys)), rho_bar, var_rho)
    return {
        "C": C_central,
        "C_CI_lo": float(np.quantile(C_values, 0.16)),
        "C_CI_hi": float(np.quantile(C_values, 0.84)),
        "bootstrap_values": C_values,  # needed for r_half bootstrap
        "low_N": False,
    }
```

### 3.7 Half-rise interpolation and verdict logic

```python
def linear_interp_halfrise(r_grid, C_values):
    """Find r such that C(r) = 1 via linear interpolation
    between bracketing grid points. Returns None if no crossing
    found in the grid range."""
    for k in range(len(r_grid) - 1):
        C_k, C_k1 = C_values[k], C_values[k+1]
        if C_k is None or C_k1 is None:
            continue
        if (C_k < 1) == (C_k1 < 1):
            continue  # same side, no crossing
        r_k, r_k1 = r_grid[k], r_grid[k+1]
        return r_k + (r_k1 - r_k) * (1 - C_k) / (C_k1 - C_k)
    return None

def compute_verdict(r_half_filt, r_half_unfilt=XI_CANONICAL):
    if r_half_filt is None:
        return "Inconclusive", "No C(r) = 1 crossing in grid range"
    ratio = r_half_filt / r_half_unfilt
    if 0.75 <= ratio <= 0.85:
        return "Confirmed", f"ratio = {ratio:.3f} ∈ [0.75, 0.85]"
    elif ratio < 0.70 or ratio > 0.90:
        return "Refuted", f"ratio = {ratio:.3f} ∉ [0.70, 0.90]"
    else:
        return "Inconclusive", (f"ratio = {ratio:.3f} in marginal "
                                 "band [0.70, 0.75) ∪ (0.85, 0.90]; "
                                 "Δr = 0.25 refinement recommended")
```

**Verdict thresholds (pre-registered):**

- **Confirmed:** ratio ∈ [0.75, 0.85] (tenth-pass 0.80 ± 0.05 band).
- **Refuted:** ratio < 0.70 or ratio > 0.90 (outside double envelope).
- **Inconclusive:** ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90]
  (marginal band; triggers Δr = 0.25 refinement per scoping
  memo §3.1).

Bootstrap uncertainty on the ratio: the 4000 ensemble
resamples produce 4000 re-interpolated `r_half_filt` values,
from which the 16–84 band on the ratio is reported. If the
central ratio is Confirmed but the 16–84 band straddles 0.75
or 0.85, the verdict is downgraded to `Confirmed-marginal`.

---

## 4. Outputs

### 4.1 `correlation_twopoint_table.csv` (10 rows)

One row per r-bin. Columns (14):

    r_target, N_pairs_ensemble,
    C_ensemble, C_CI_lo, C_CI_hi,
    C_ensemble_rank, model_band_rel,
    CoV_across_seeds,
    N_seeds_in_CoV,
    N_pairs_per_seed_mean,
    low_N_ensemble, low_N_any_seed,
    Spearman_undefined, bootstrap_iterations

### 4.2 `correlation_twopoint_per_seed.csv` (100 rows = 10 r-bins × 10 seeds)

One row per (r, seed). Columns (7):

    seed, r_target, N_pairs_seed,
    C_seed, C_seed_low_N,
    xi_seed, L_ray_seed

### 4.3 `correlation_twopoint_summary.json`

```
{
  "method": "ED-SC 3.4 F4 two-point correlation at canonical ξ",
  "simulator_of_record": "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
  "xi_canonical": 1.7575325729470939,
  "xi_target": 1.7575,
  "alpha_filt": 0.25,
  "N_req": 4,
  "dimensionless_hinge": 1.08,
  "r_grid": [0.5, 1.0, 1.5, ..., 5.0],
  "dr_bin": 0.5,
  "seeds": [11, 22, ..., 111],
  "canonical_params": {...},
  "resonance_windows_excluded": {"A": [2.50, 2.80], "B": [3.50, 3.90]},
  "calibration_prepass_per_seed": {seed: [...w-sweep data...]},
  "per_seed": [
    {"seed": 11, "xi_measured": ..., "L_ray": ..., "r_diag": 1,
     "out_of_scope": false, "N_motifs_total": ..., ...},
    ...
  ],
  "global_pool": {
    "rho_bar": ...,
    "sigma2_rho": ...,
    "N_motifs_total": ...,
  },
  "r_bins": [
    {"r": 0.5,
     "N_pairs_ensemble": ...,
     "C_ensemble": ..., "C_CI_lo": ..., "C_CI_hi": ...,
     "C_ensemble_rank": ..., "model_band_rel": ...,
     "per_seed_C": [...], "CoV_across_seeds": ...,
     "low_N_ensemble": false, ...},
    ...
  ],
  "half_rise": {
    "r_half_filt_central": ...,
    "r_half_filt_bootstrap_16_84": [...],
    "r_half_unfilt": 1.7575325729470939,
    "ratio_central": ...,
    "ratio_bootstrap_16_84": [...]
  },
  "verdict": {
    "verdict": "Confirmed" | "Confirmed-marginal" | "Inconclusive" | "Refuted",
    "reason": "...",
    "tenth_pass_prediction": "0.80 ± 0.05",
    "confirmed_threshold": [0.75, 0.85],
    "refuted_threshold_low": 0.70,
    "refuted_threshold_high": 0.90
  },
  "diagnostics": {
    "r_diag_excursions": [],
    "resonance_window_intrusions": [],
    "rigid_endpoint_check_C_at_r_min": ...,
    "rigid_endpoint_check_C_at_r_max": ...,
    "N_pairs_total_across_all_bins": ...,
    "N_pairs_unbinned": ...,
  },
  "wall_seconds_total": ...
}
```

### 4.4 Output directory

All three files under `outputs/ed_sc_3_4_twopoint/`.
Directory created by the driver if absent. No simulator
constants mutated.

---

## 5. Summary JSON contents (highlights)

The key fields in `correlation_twopoint_summary.json`, for
downstream citation:

- `r_grid[]` — the 10 pre-registered r values.
- `r_bins[k].C_ensemble` — canonical ensemble estimator per r-bin.
- `r_bins[k].C_CI_lo / C_CI_hi` — bootstrap 16–84 ensemble band.
- `r_bins[k].per_seed_C[i]` — per-seed local estimator at each r.
- `r_bins[k].CoV_across_seeds` — per-realisation spread.
- `r_bins[k].C_ensemble_rank, model_band_rel` —
  Pearson-vs-Spearman model-band pair.
- `half_rise.r_half_filt_central` — main quantitative output;
  linearly interpolated from C_ensemble(r) = 1.
- `half_rise.r_half_filt_bootstrap_16_84` — bootstrap-propagated
  uncertainty on the half-rise.
- `half_rise.ratio_central = r_half_filt / 1.7575` — compared
  against the GR-SC 1.7 pooled-R2 prediction 0.80 ± 0.05.
- `verdict.verdict` ∈ {`Confirmed`, `Confirmed-marginal`,
  `Inconclusive`, `Refuted`}.
- `verdict.reason` — human-readable verdict justification.
- `diagnostics.rigid_endpoint_check_C_at_r_min/max` — should be
  near 0 at smallest r (sub-motif scale) and near 2 at largest
  r (uncorrelated regime).

---

## 6. Deliverables

### 6.1 Complete driver specification

`analysis/scripts/ed_sc_3_4_twopoint_correlation.py` implements
§2–§4 verbatim. Structural precedent: inherits the evolution +
motif extraction + calibration pre-pass architecture from
`ed_sc_3_4_sigma1_multiseed.py`; adds the pair enumeration,
r-binning, correlation estimation, bootstrap, and verdict logic
blocks. Expected wall time: ~60 s (comparable to F2 / F3-verify).

### 6.2 Pre-registered falsifier logic

The tenth-pass GR-SC 1.7 prediction `r_½^{filt}/r_½^{unfilt} =
0.80 ± 0.05` is the canonical falsifier. Verdict taxonomy
thresholds per §3.7:

- **Confirmed:** ratio ∈ [0.75, 0.85] (within tenth-pass band).
- **Confirmed-marginal:** central ratio in [0.75, 0.85] **but**
  bootstrap 16–84 band straddles a threshold.
- **Inconclusive:** ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90]
  (marginal band; triggers Δr = 0.25 refinement).
- **Refuted:** ratio ∉ [0.70, 0.90] (outside double envelope).

### 6.3 Pre-registered uncertainty propagation rules

Four uncertainty components, quoted separately per r-bin in
the CSV/JSON (never combined in quadrature, per GR-SC 1.3
κ-prediction convention):

- **Ensemble CI** (bootstrap 16–84 on pair-resample at each
  r-bin).
- **Per-realisation CoV** (std / mean of per-seed local
  estimators at each r-bin).
- **Model band** (|Pearson − Spearman| / |Pearson| at each
  r-bin).
- **Calibration** (not computed at Δr = 0.5; `N/A` unless
  Δr = 0.25 refinement is run).

Low-N r-bins (ensemble N < 20 or per-seed N < 10) are flagged
and excluded from canonical citation.

### 6.4 Changelog

- **Rev. 1 (2026-04-23, this memo):** provides the full F4
  driver specification, translating F4 scoping into a concrete
  implementation. Pre-registers all data structures, guards,
  estimators, bootstrap details, verdict logic, and output
  format. Driver
  `analysis/scripts/ed_sc_3_4_twopoint_correlation.py` is
  implemented in the same turn as this memo per the pre-
  registered scoping-then-driver chain.
