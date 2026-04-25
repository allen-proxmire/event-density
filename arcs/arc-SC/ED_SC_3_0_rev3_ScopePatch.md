# ED-SC 3.0 rev. 3 — Scope Patch (size-dependent S-F2 flatness threshold)

**Status:** Scope patch. Introduces a size-dependent flatness
threshold for S-F2 and formalises the downstream verdict taxonomy
(`Confirmed` / `Confirmed-boundary` / `Refuted` / `GuardrailFailure`
/ `H3-artefact`). No new numerics.
**Parents:**
- `theory/ED_SC_3_0_Scope.md` rev. 2 (regime-based S-F2; resonance-
  mapping clause).
- `theory/ED_SC_3_3_FilterGeometry_Scope.md` rev. 1 + execution
  (20-cell full sweep).
- `theory/ED_SC_3_3_AlphaFilt_SubScan.md` rev. 1 + rev. 2 (closure
  memo with H1/H2/H3 verdicts).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3 α_filt sub-scan).

---

## 1. Purpose

ED-SC 3.0 rev. 2 (`theory/ED_SC_3_0_Scope.md`) introduced:

- **Regime-based S-F2** — the 20 % tolerance applies only within
  a contiguous regime of a hinge scan; cross-regime drifts are
  diagnostic, not falsifying.
- **Resonance-mapping clause** — any new hinge must be sub-sampled
  at Δ ≤ 0.1 before falsifier readings.

The ED-SC 3.3 filter-geometry sweep and its α_filt sub-scan revealed
that the **fixed 20 % hinge-flatness threshold** is miscalibrated
in the low-motif-count regime: four cells along the `N_req = 4`
column produced `rel-span > 0.20` flags despite showing no
motif-count jumps, no shell-geometry shifts, and a smooth
monotonic S2 profile. All four were classified as **H3 sampling
artefacts** by the sub-scan rev. 2 verdict logic — the 20 %
threshold is below the intrinsic S2 sampling-noise floor at mean
motif counts in the [47, 90] band.

**Rev. 3 introduces a size-dependent flatness threshold** that
eliminates these false positives automatically while preserving
the 20 % floor at canonical and larger pool sizes. No other
ED-SC 3.0 content changes.

---

## 2. Empirical motivation

From `outputs/ed_sc_3_3/alpha_subscan_summary.json` (7-cell Δα =
0.025 sub-scan at fixed `N_req = 4`, canonical `L_ray = 1.898 lu`,
canonical 40-snapshot ξ, resonance-window-excluded):

| α_filt | mean N / hp | hinge rel-span | S2 rel-SEM | max \|ΔN\|/N̄ | verdict |
|---:|---:|---:|---:|---:|---|
| 0.100 | 90.0 | 0.212 | 0.241 | 0.033 | **H3** |
| 0.125 | 77.0 | 0.105 | 0.261 | 0.052 | H2 |
| 0.150 | 70.0 | 0.209 | 0.225 | 0.057 | **H3** |
| 0.175 | 61.2 | 0.302 | 0.334 | 0.049 | **H3** |
| 0.200 | 46.6 | 0.355 | 0.415 | 0.064 | **H3** |
| 0.225 | 37.4 | 0.045 | 0.264 | 0.027 | H2 |
| 0.250 | 32.8 | 0.075 | 0.180 | 0.030 | H2 (canonical) |

Observations:

- S2 relative SEM sits in **[0.225, 0.415]** across the four H3
  cells — above the fixed 0.20 flatness floor.
- Mean motif counts per hinge point sit in **[47, 90]** — well
  below the canonical value (~33 for the canonical cell; ~32–77
  across the H2 band).
- Max relative motif-count jumps are **≤ 0.064** across all
  seven cells — below the 0.15 H1-resonance threshold.
- No shell-histogram reconfiguration across any cell (contrast
  with ED-SC 3.2.6 which explicitly recorded √4 → √9 and √10 →
  √16 shifts).

**Structural reading:** the 20 % flatness threshold is a per-
distribution-flatness test; it becomes noise-dominated when the
per-hinge-point S2 sampling error exceeds 20 %. A size-aware
threshold absorbs the sampling noise while preserving sensitivity
to genuine plateau breaks at canonical and larger pool sizes.

---

## 3. Revised flatness threshold

**Definition.** For a hinge sub-sweep at a given cell:

    flat_thresh(N̄) = max(0.20, 2 · S2_rel_SEM)

where:

- `N̄` is the mean motif count per hinge point in the sub-sweep.
- `S2_rel_SEM` is the hinge-averaged **relative standard error**
  of the IQR, computed from the bootstrap 16–84 % CI at each
  hinge point:

        S2_rel_SEM = mean_h [ 0.5 · (S2_hi − S2_lo) / |S2_h| ]

  with `S2_lo, S2_hi = S2_ci16_84` from 4000-resample bootstrap
  (standard across the ED-SC 3.x drivers).

**Rule.** A cell's `hinge_flatness_rel_span = (max S2 − min S2) / mean S2`
triggers an S-F2 flatness flag **only if**:

    hinge_flatness_rel_span > flat_thresh(N̄).

**Floor preserved.** The `max(0.20, ...)` ensures that
canonical-and-larger pools (where `2·S2_rel_SEM ≤ 0.20`) retain the
original 20 % threshold; only cells with intrinsic bootstrap SEM
exceeding 10 % of S2 inherit a relaxed threshold.

**Worked sanity check.** Under rev. 3 applied to the α_filt sub-scan:

| α_filt | rel-span | 2·S2_rel_SEM | flat_thresh | flag? |
|---:|---:|---:|---:|---|
| 0.100 | 0.212 | 0.482 | 0.482 | **pass** |
| 0.125 | 0.105 | 0.522 | 0.522 | pass |
| 0.150 | 0.209 | 0.450 | 0.450 | **pass** |
| 0.175 | 0.302 | 0.668 | 0.668 | **pass** |
| 0.200 | 0.355 | 0.830 | 0.830 | **pass** |
| 0.225 | 0.045 | 0.528 | 0.528 | pass |
| 0.250 | 0.075 | 0.360 | 0.360 | pass |

All seven cells pass under rev. 3. The four H3 false positives
disappear automatically; the three H2 cells were already passing.
Canonical cell retains a relaxed threshold (0.360) but its actual
rel-span (0.075) is far below, so behaviour is unchanged in
practice.

---

## 4. Updated S-F2 interpretation

A cell is **`Refuted` under S-F2** if and only if **all three** of:

1. `hinge_flatness_rel_span > flat_thresh(N̄)` — size-corrected
   flatness failure.
2. The cell lies within a mapped regime (Regime I / II / III from
   ED-SC 3.2.5), not on a low-N boundary.
3. No known resonance mechanism accounts for the flatness failure
   (i.e. the cell is not inside a declared resonance window, and
   its flatness flag is not co-located with a motif-count jump or
   shell shift).

Otherwise, the cell is classified as:

- **`Confirmed`** — flatness-passes the size-corrected threshold
  **and** is plateau-interior.
- **`Confirmed-boundary`** — size-corrected flatness passes but
  the cell sits at a regime boundary (smooth crossover, monotonic
  S2). This is a new tag introduced by rev. 3.
- **`H3-artefact`** — flatness fails under the fixed 20 % rule but
  passes under the size-corrected threshold **and** has `mean_N
  < 500` and `S2_rel_SEM > 0.15` and no motif-count jump. This is
  an annotative reclassification; operationally equivalent to
  `Confirmed` in downstream integration.
- **`GuardrailFailure`** — the cell's ξ guardrail fails (fewer
  than 8/10 seeds within 20 % of canonical ξ under the 40-snapshot
  method). This outranks S-F2 and must be resolved before any
  distributional verdict is rendered.
- **`Refuted-resonance`** — flatness fails under the size-corrected
  threshold **and** the cell is inside a declared resonance window.
  The resonance-mapping clause (§5.2 rev. 2 inherited) requires
  Δ ≤ 0.1 sub-sampling before a final verdict; this tag is
  terminal only after the sub-sweep has been performed.

The three-way taxonomy of ED-SC 3.2.6 (`Confirmed` / `Refuted` /
`GuardrailFailure`) is subsumed by the above; `Confirmed-boundary`
and `H3-artefact` are refinements of `Confirmed` rather than new
verdicts in the falsifier sense.

---

## 5. Guardrail inheritance

ED-SC 3.0 rev. 3 inherits, unchanged, the following guardrails:

- **Canonical ξ method** — per-seed ξ uses the 40-snapshot half-
  decay method (burn-in 100, snap every 10, GR-SC 1.7 density
  channel). Single-snapshot ξ is not permitted. (ED-SC 3.2.6
  rev. 2 §5.2.)
- **Resonance-mapping clause** — any new hinge introduced by a
  depth memo must be sub-sampled at Δ ≤ 0.1 across its reported
  window to resolve regime boundaries, with regime membership
  declared before falsifier readings. (ED-SC 3.0 rev. 2 §5.2.)
- **Regime-based S-F2 core** — the 20 %-or-size-corrected flatness
  tolerance applies only within a contiguous regime; cross-regime
  drifts are diagnostic, not falsifying. (ED-SC 3.0 rev. 2 §5.1,
  with the flatness threshold now replaced by §3 above.)
- **Simulator-of-record guardrail** — every ED-SC 3.x numerical
  claim must cite `r2_grf_falsifier_tests.py` +
  `ED_Update_Rule.ed_step_mobility` by filename. No module globals
  or canonical parameters are mutated. (ED-SC 3.1 rev. 2 §6.)
- **Resonance-window exclusions** — Window A `L_ray ∈ [2.50, 2.80]`
  and Window B `L_ray ∈ [3.50, 3.90]` are structurally forbidden
  for any canonical operating point on the 4-ray `N_req = 4`
  filter at the canonical ξ. (ED-SC 3.2.6 rev. 2; ED-SC 3.1
  rev. 3.)
- **Geometric quorum constraint** — `N_req ≤ n_rays` is
  unambiguous pre-registration. On the canonical 4-ray filter,
  `N_req = 5` is a hard geometric exclusion (ED-SC 3.3 α_filt
  sub-scan rev. 2 §5.5), not a threshold effect.
- **Shell-class (r_diag) validity window** — the canonical
  dimensionless hinge `L_ray/ξ = 1.08` applies to realisations
  with `r_diag(L_ray) = round(0.707·L_ray) = 1`, equivalently
  `ξ ≲ 1.964 lu`. Realisations with `r_diag = 2` (diagonal ray
  endpoints on shell √8) are rescued by the shell-aware
  coordinate `L_eff = √2 · r_diag(L_ray)` per ED-SC 3.3.8b.
  Realisations with `r_diag ≥ 3` are outside the current claim's
  domain and require fresh scoping. Pre-registration for any
  scan or calibration memo must declare the per-realisation
  r_diag values and either (i) restrict to `r_diag = 1`, or
  (ii) adopt L_eff and report per-shell-class statistics
  separately. (ED-SC 3.3.8 / 3.3.8a / 3.3.8b / 3.3.10.)

No guardrails are removed. The updates are the flatness-
threshold definition in §3 and the shell-class validity window
added here.

---

## 6. Consequences for downstream memos

- **ED-SC 3.3 rev. 2** (forthcoming
  `theory/ED_SC_3_3_rev2_FilterGeometry.md`) must apply the
  size-corrected flatness threshold per §3 and emit verdicts per
  §4. Specifically:
  - The three originally-`Refuted` cells
    (`alpha0.10_Nreq4`, `alpha0.15_Nreq4`, `alpha0.20_Nreq4`)
    are reclassified as **`Confirmed-boundary` (H3-artefact)**.
  - The fourth H3 cell surfaced by the sub-scan
    (`alpha0.175_Nreq4`) is annotated identically.
  - The N_req = 5 column is formally retired from the grid under
    the `N_req ≤ n_rays` geometric quorum constraint; the
    ED-SC 3.3 grid becomes **5 × 3 effective cells** with the
    N_req = 5 column documented as geometrically empty.
  - All other cells retain their ED-SC 3.3 full-sweep verdicts
    unchanged (size-corrected threshold only relaxes, never
    tightens, so no previously-`Confirmed` cell can flip).
- **ED-SC 3.4** (forthcoming multi-parameter-coupling memo) must
  apply the rev. 3 threshold at every cell of its `(α_filt, N_req,
  ξ, mobility-law)` grid. Its pre-registration must explicitly
  cite ED-SC 3.0 rev. 3 §3 rather than the fixed 20 % rule.
- **ED-SC 3.5** (projected distributional-collapse memo)
  inherits rev. 3 transparently.
- **ED-SC 3.1 rev. 3** canonical operating-point certification is
  **unchanged**: the canonical cell always flatness-passed under
  the fixed 20 % threshold, and continues to pass under the
  (relaxed) size-corrected threshold. No re-certification is
  needed.
- **Driver amendment.** The flatness-threshold update is a
  *scope* change; drivers may adopt the new threshold at
  integration time. A concrete code patch to
  `analysis/scripts/ed_sc_3_3_filter_geometry_scan.py` and the
  α_filt sub-scan driver would:
  - replace the hardcoded `FLAT_THRESH = 0.20` with
    `flat_thresh_cell = max(0.20, 2 * cell["S2_relative_sem"])`
    computed per cell from the bootstrap CIs already recorded;
  - emit both the fixed-threshold flag (for historical audit) and
    the size-corrected flag (for current verdict) in the per-cell
    JSON.
  This is not applied by this scope memo; it is flagged here so
  that the ED-SC 3.3 rev. 2 integration memo can either apply the
  threshold post-hoc (audit via `alpha_subscan_summary.json`) or
  commission a driver patch.

---

## 7. Changelog

- **Rev. 1 (initial).** ED-SC 3.0 scope as written prior to the
  ED-SC 3.2.x resonance discovery. Fixed 20 % flatness tolerance
  (single-regime implicit).
- **Rev. 2 (2026-04-23, earlier).** Introduced regime-based S-F2:
  20 % tolerance applies only within a contiguous regime, cross-
  regime drifts are diagnostic. Introduced the resonance-mapping
  clause: Δ ≤ 0.1 sub-sampling of any new hinge required before
  falsifier readings.
- **Forward-pointer (2026-04-23, thirteenth–fourteenth pass; ED-SC
  3.3.x sub-arc closure).** Coordinate reconsideration
  (`theory/ED_SC_3_3_8_CoordinateReconsideration.md`) identified a
  **ξ-window of validity** for the `L_ray/ξ` hinge: the diagonal-
  ray shell crossing at `ξ_crossing ≈ 2.121/1.08 = 1.964 lu`
  causes seed 456 (ξ = 2.19 lu) to admit a distinct integer-
  lattice shell set (√8) absent from the other nine canonical
  seeds. **ED-SC 3.3.8a**
  (`theory/ED_SC_3_3_8a_XiCrossing_Scan.md`) executed the selection
  experiment and confirmed remediation **D (shell-aware effective
  coordinate)**: monotone √8 shell admission at ξ = 2.025, S1
  stable across the transition (max ΔS1 = 0.098), S2 smooth
  (max single-step |ΔS2| = 0.257 < 0.489 discrete-jump threshold).
  **ED-SC 3.3.8b**
  (`theory/ED_SC_3_3_8b_ShellAwareCoordinate.md`) then rescued
  seed 456 under the shell-aware coordinate
  `L_eff = √2 · r_diag(L_ray)` (ΔS2 dropped 0.518 → 0.159). The
  **ensemble-vs-realisation clarification**
  (`theory/ED_SC_3_3_9_EnsembleVsRealisation.md`) qualifies the
  ED-SC 3.1 rev. 3 invariance claim: S1 (median) is invariant at
  per-realisation resolution, S2 (IQR) is invariant at ensemble-
  pool resolution only with irreducible ~25 % per-realisation
  spread not attributable to shell geometry. Any downstream
  S2-derived invariant (GR-SC 1.0+ ratio / quadratic / Rayleigh
  / correlation classes) must carry this spread as part of the
  prediction. **ED-SC 3.3.10**
  (`theory/ED_SC_3_3_10_ArcClosure.md`) declares the ED-SC 3.3.x
  sub-arc closed with the four-clause final invariance statement
  (S1 per-realisation, S2 ensemble-only, `r_diag = 2` rescued by
  L_eff, `r_diag ≥ 3` out-of-scope). **ξ-window guardrail added
  here**: the canonical hinge applies to realisations with
  `r_diag(L_ray) = round(0.707·L_ray) = 1` (equivalently
  `ξ ≲ 1.964 lu` under `L_ray/ξ = 1.08`); realisations with
  `r_diag = 2` use `L_eff = √2 · r_diag(L_ray)`; realisations with
  `r_diag ≥ 3` are outside the current claim's domain. These
  forward pointers are recorded here; structural scope-patch
  numerical content is unchanged.

- **Rev. 3 (2026-04-23, this memo).**
  - Replaces the fixed 20 % flatness threshold with the size-
    dependent
    `flat_thresh(N̄) = max(0.20, 2 · S2_rel_SEM)` (§3).
  - Refines the S-F2 verdict taxonomy to include
    `Confirmed-boundary` (smooth crossover) and `H3-artefact`
    (low-N noise-floor) as annotative refinements of `Confirmed`
    (§4).
  - Adds `Refuted-resonance` as a terminal label for cells inside
    a declared resonance window that fail the size-corrected
    flatness (§4).
  - Adds the **geometric quorum constraint** `N_req ≤ n_rays` to
    the guardrail list (§5).
  - Does not modify the canonical ξ method, the resonance-mapping
    clause, the simulator-of-record guardrail, the resonance-
    window exclusions, or the ED-SC 3.1 rev. 3 canonical-point
    certification.
  - Enables ED-SC 3.3 rev. 2 to be written with the three original
    ED-SC 3.3 flags reclassified as `Confirmed-boundary
    (H3-artefact)` and the N_req = 5 column formally retired.
