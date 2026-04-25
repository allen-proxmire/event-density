# ED-SC 3.4 — ξ Calibration within r_diag = 1

**Status:** Pre-registration + execution-ready. Opens ED-SC 3.4
as a narrow-scope ξ calibration inside the canonical invariance
domain. No falsifier verdict.
**Parents:**
- `theory/ED_SC_3_3_10_ArcClosure.md` §3 (four-clause final
  invariance statement: S1 per-realisation, S2 ensemble-only,
  `r_diag = 1` canonical, `r_diag = 2` rescued by L_eff).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (~25 %
  per-realisation S2 spread — to be quantified vs ξ here).
- `theory/ED_SC_3_3_8a_XiCrossing_Scan.md` (IC-amplitude ξ-
  control methodology inherited verbatim).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` §4.1
  (coordinate validity `r_diag = 1 ⇔ ξ ≲ 1.964 lu`).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` §5 (shell-class validity
  window guardrail).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.10).

---

## 1. Purpose

The ED-SC 3.3.x sub-arc established three results that ED-SC 3.4
inherits as starting assumptions, not as questions under test:

- **S1 (median ρ) is invariant at per-realisation resolution**
  across the canonical 10-seed ensemble spanning 35 % natural ξ
  variation.
- **S2 (IQR of ρ) is invariant at ensemble-pool resolution only**,
  with ~25 % irreducible per-realisation spread not attributable
  to shell geometry.
- **The canonical invariance domain is `r_diag(L_ray) = 1`**,
  equivalently `ξ ≲ 1.964 lu` under the canonical hinge
  `L_ray/ξ = 1.08`.

ED-SC 3.4 is therefore **not an invariance test**. Its purpose is
a calibration: quantify how S1 and S2 evolve with ξ **inside the
valid r_diag = 1 window**, produce a calibration curve
`ξ → (S1, S2, S3)`, and hand that curve forward to GR-SC 1.0+
so that curvature-invariant predictions at ξ values other than
`ξ_canonical = 1.7575 lu` carry the correct S1 / S2 values
rather than extrapolated guesses.

No pass/fail falsifier is pre-registered. The output is a
calibration dataset + interpretive reading per §6.

---

## 2. Operating point

- **Filter:** `α_filt = 0.25`, `N_req = 4` (canonical, fixed).
- **Hinge:** `L_ray = 1.08 · ξ_measured` per ξ point (canonical
  continuous hinge applies throughout; no shell-aware coordinate
  needed inside the r_diag = 1 window).
- **ξ window:** `ξ ∈ [1.60, 1.95] lu`. Lower bound is roughly
  the smallest canonical-seed ξ (seed 77 at 1.623 lu); upper
  bound is ~35 milliunits below `ξ_crossing ≈ 1.964 lu` to keep
  every scan point safely within `r_diag = 1`.
- **Snapshot cadence:** burn-in 100, snap every 10, **40
  snapshots per ξ** (canonical ξ measurement cadence; matches
  ED-SC 3.3.6 / 3.3.8a).
- **Fixed seed:** `77` (single-realisation calibration curve
  for reproducibility, per ED-SC 3.3.8a precedent).
- **Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility` with canonical parameters
  (alpha=0.03, gamma=0.5, noise_sigma=0.0556, mobility_exp=2.7,
  steps=500, size=64, dt=0.05, periodic boundary).

---

## 3. ξ grid

Nine points covering the r_diag = 1 window, denser near the
canonical `ξ_canonical = 1.7575 lu`, with tighter spacing as
`ξ_crossing` is approached:

    ξ_target ∈ {1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.93, 1.95}

The last two points (1.93, 1.95) are intentionally close to the
ξ_crossing threshold to characterise the approach-behaviour of
S1/S2 as the coordinate validity window's upper edge is
approached.

**ξ-control method (inherited from ED-SC 3.3.8a §3).** A
calibration pre-pass sweeps IC half-width `w` on seed 77 over a
coarse grid `{0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30,
0.35}`, measures the 40-snapshot ξ at each w, and builds a
monotone interpolant `w(ξ)`. For each scan point, the driver
selects `w = w_interp(ξ_target)`, evolves, measures
`ξ_measured`, and applies one bisection refinement if
`|ξ_measured − ξ_target| / ξ_target > 1 %`.

**Resonance-window guard.** Hard-fail at launch if any
`L_ray_i = 1.08 · ξ_target` intersects Window A `[2.50, 2.80]`
or Window B `[3.50, 3.90]`. Under the scan grid the maximum
`L_ray` is `1.08 · 1.95 = 2.106 lu`, safely below Window A.

**r_diag window guard.** Per ξ point, compute
`r_diag_measured = round(0.707 · 1.08 · ξ_measured)`; refuse
to aggregate any point where `r_diag_measured ≠ 1` (flag as
out-of-scope for this memo's calibration). Under the nominal
grid, max `0.707 · 1.08 · 1.95 = 1.489 < 1.5`, so no point
crosses. Defensive guardrail for cases where calibration miss
pushes ξ_measured above target.

---

## 4. Measurements

For each of the 9 scan points:

1. **Evolve** seed 77 with `rng.uniform(0.5 − w, 0.5 + w)` using
   the interpolated `w`.
2. **Record** 40 snapshots (burn-in 100, snap every 10).
3. **Measure** `ξ_measured = mean(xi_halfdecay(snapshot_k))`
   across the 40 snapshots.
4. **Check** `r_diag_measured = round(0.707 · 1.08 ·
   ξ_measured)`; flag if != 1 and skip aggregation.
5. **Compute** `L_ray = 1.08 · ξ_measured`.
6. **Collect motifs** at each of the 40 snapshots under
   `(α_filt = 0.25, N_req = 4, L_ray)`; pool.
7. **Per-point statistics:**
   - `N_i` — total motif count across 40 snapshots.
   - `S1_i, S2_i, S3_i` with bootstrap 16–84 CIs (4000
     resamples).
   - **Shell histogram** `H_i(r)` across `4 · N_i` endpoints
     (for completeness; expected to be class-1 dominant).
   - **Jensen–Shannon divergence** `JS(H_i, H_ref)` where
     `H_ref` is the `ξ = 1.80` reference point (approximate
     midpoint of the scan; `JS_ref = 0` by construction).
   - **Per-snapshot diagnostic**: `N_per_snap[]` list and,
     where N ≥ 2, per-snapshot `median` and `IQR` — a
     stationarity check that the 40-snapshot pool is not
     dominated by a transient.

---

## 5. Outputs

**Calibration curve.** The primary deliverable is the five-
column curve

    ξ_measured  →  (N, S1, S2, S3)

at each of the 9 points, with bootstrap CIs on S1 and S2.
Plotted and/or interpolated downstream, this curve gives
GR-SC 1.0+ a lookup: "at working ξ = X, expect S1 = f(X),
S2 = g(X) with bootstrap uncertainty."

**Deliverables.**

- `outputs/ed_sc_3_4/xi_calibration_table.csv` — one row per
  scan point, flat columns:
  `ξ_target, ξ_measured, miss_frac, w_used, L_ray, r_diag,
  N, S1, S1_lo, S1_hi, S2, S2_lo, S2_hi, S3, JS_vs_ref, N_per_snap_mean`.
- `outputs/ed_sc_3_4/xi_calibration_summary.json` — master
  payload:
  - `method`, simulator-of-record string.
  - Canonical parameters.
  - `xi_targets`, calibration pre-pass audit trail
    (w grid, measured ξ, interpolant).
  - `xi_ref_index` (4, for ξ = 1.80), `H_ref` shell histogram.
  - `scan_points[]` — per point: measurements from §4 plus
    the snapshot-level diagnostic arrays.
  - **Derived summary:**
    - `S1_vs_xi_slope` and `S1_vs_xi_residual` (OLS fit to
      S1_i vs ξ_i; tests D6.1 per §6.1).
    - `S2_vs_xi_slope` and `S2_vs_xi_trend_direction` (sign
      of the OLS slope; tests D6.2).
    - `r_diag_excursions[]` (list of points where
      `r_diag_measured != 1`; ideally empty).
    - `resonance_check` (boolean + per-point list).
  - `wall_seconds_total`.

Artefacts live under `outputs/ed_sc_3_4/` (new directory).

---

## 6. Interpretation (pre-registered)

No pass/fail verdict. The calibration is read through three
pre-registered interpretive lenses:

### 6.1 S1 (median) — expect near-flat

The ED-SC 3.3.10 clause (a) claim predicts S1 stability across
ξ at per-realisation resolution. Quantify:

- **Residual slope** from an OLS fit of `S1_i` vs `ξ_i`. Expected
  magnitude: `|slope| · Δξ < 0.20 · |S1_ref|`, i.e. the implied
  total variation across the 0.35 lu scan width stays within the
  ED-SC 3.0 rev. 3 size-corrected flat_thresh at canonical N.
- **Residual scatter** around the fit. The ED-SC 3.3.10 clause
  (a) max ΔS1 = 0.115 sets a prior expectation; residuals should
  sit within this envelope.

If S1 shows a significant monotone ξ dependence at per-
realisation resolution inside `r_diag = 1`, that is **new
information**: it would indicate S1 is an ensemble-invariant
only claim was too strong, or that the single-seed-77
calibration differs systematically from the canonical ensemble.
Either outcome scopes tighter claims in downstream memos; no
retraction is triggered automatically.

### 6.2 S2 (IQR) — expect smooth ξ dependence

ED-SC 3.3.6 observed pool-level S2 varying from 1.969 (at the
canonical 35 % natural ξ spread) to 1.288 in ED-SC 3.1 rev. 3
(at narrower ξ spread); the 40-snapshot calibration scan
`xi_scan_summary.json` of ED-SC 3.3.8a showed S2 walking from
~2.05 to ~2.77 across ξ ∈ [1.85, 2.10]. Quantify on the new
scan:

- **OLS slope** of S2_i vs ξ_i and its sign.
- **Bootstrap-CI band** on the S2 curve.
- **JS vs ref** — shell-histogram stability across the scan
  (expected class-1 dominant throughout; deviations flag
  sub-shell reconfigurations within class 1 that were not
  visible on the ED-SC 3.3.8a coarse grid).

A smooth monotone S2(ξ) curve is the expected and desired
output — it is **the calibration** that downstream GR-SC
S2-derived invariants need.

### 6.3 S3 — exploratory only

No cross-scale claim is pre-registered for S3. Record the values
for completeness; discuss only if a strong and unexpected
pattern emerges.

### 6.4 Guidance for GR-SC 1.0+

Three concrete downstream directives follow from the
calibration regardless of which pattern emerges:

- **S1-derived invariants** (`r*`, `ℛ_W`, `ℛ_Ray`, `ℛ_G`) can
  use S1(ξ) directly as point predictions, with the
  calibration-band S1 uncertainty inherited as prediction
  uncertainty.
- **S2-derived invariants** (`C²` Weyl square, `det G`,
  correlation-length-involving quantities) require the full
  `S2(ξ) ± CI` curve plus the `±25 %` per-realisation spread
  from ED-SC 3.3.9. GR-SC predictions evaluated at any ξ inside
  `[1.60, 1.95]` should interpolate the calibration curve and
  quote the ensemble-pool CI **plus** the per-realisation spread
  as separate uncertainty components.
- **ξ-positioning** of a GR-SC evaluation must be specified
  explicitly. A GR-SC prediction "at the canonical operating
  point" means ξ = 1.7575; a prediction at a different ξ should
  cite the calibration row closest to that ξ or interpolate
  linearly between adjacent rows.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.4 as a
  narrow-scope ξ calibration inside the r_diag = 1 canonical
  window. Pre-registers the 9-point ξ grid `{1.60, 1.65, 1.70,
  1.75, 1.80, 1.85, 1.90, 1.93, 1.95}` on fixed seed 77 with
  40-snapshot pooling and IC-amplitude ξ-control (inherited from
  ED-SC 3.3.8a), the measurement list (N, S1, S2, S3, shell
  histogram, JS vs ξ=1.80 ref, per-snapshot stationarity
  diagnostic), and the three-lens interpretation (S1 near-flat,
  S2 smooth ξ-dependence, S3 exploratory, GR-SC guidance). No
  falsifier verdict. Inherits all guardrails of the closed
  ED-SC 3.3.x arc. No numerics.
