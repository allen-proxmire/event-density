# ED-SC 3.3.6 — Per-Seed Distributional-Collapse Test (40-snapshot)

**Status:** Pre-registration. Scope-only memo. No numerics.
**Parents:**
- `theory/ED_SC_3_3_5_PerSeedCollapse.md` rev. 1 (single-snapshot
  precursor; Broken-collapse verdict at low N per seed).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` (canonical
  operating point `(L_ray/ξ, α_filt, N_req) = (1.08, 0.25, 4)`).
- `theory/ED_SC_3_2_6_RayBudget_Resonance.md` rev. 2 (canonical
  40-snapshot ξ method + resonance-window exclusions).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness
  threshold; refined verdict taxonomy).
**Input artefact:** `outputs/ed_sc_3_1/xi_canonical.json`
  (`xi_per_seed` table).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.5 execution).

---

## 1. Purpose

ED-SC 3.3.5 executed the first direct test of the cross-scale
invariance claim on the 10-seed canonical field cache, using
per-seed `L_ray_i = 1.08 · ξ_i` on a single final-snapshot motif
collection. The verdict was **Broken-collapse**: 6 of 10 seeds
failed the ED-SC 3.0 rev. 3 size-corrected threshold, with two
seeds returning too few motifs for per-seed statistics (N = 1, 2).

**The failure was not conclusive.** Per-seed motif counts of 1–5
are below any reasonable bootstrap floor; per-seed S2 estimates
are single-motif IQRs in several cases. The pool-level statistics
reproduced canonical `(S1_pool = −1.913, S2_pool = 1.270, N_pool =
32)` almost exactly, confirming that pool-level ξ-invariance is
real; per-seed statistics are simply below the statistical-
power threshold of the test.

ED-SC 3.3.6 repeats ED-SC 3.3.5 with **40-snapshot pooling per
seed**, matching the canonical ξ-measurement protocol (burn-in 100,
snap every 10). This raises per-seed motif counts from ~3 to a
target **mean N ≈ 130–200** (scaling from the ED-SC 3.3.5 single-
snapshot mean of ~3.2 per seed), bringing bootstrap-stable per-
seed S1/S2/S3 within reach and distinguishing:

- **H-stat** (statistical underpower) — ED-SC 3.3.5 was too thin;
  at high per-seed N the distributions collapse cleanly.
- **H-coord** (dimensionless-coordinate mis-specification) — even
  at high per-seed N, per-seed distributions differ in a way that
  correlates with integer-lattice-shell geometry of `L_ray_i`.
- **H-shallow** (pool-level only invariance) — even at high
  per-seed N, per-seed distributions differ stably across seeds,
  with the pool-level match arising only from averaging.

This memo is pre-registration only. No numerics are presented.

---

## 2. Operating point

Unchanged from ED-SC 3.3.5 §2:

- ξ_i loaded from `xi_canonical.json` per seed (not re-measured).
- `L_ray_i = 1.08 · ξ_i` per seed.
- `α_filt = 0.25, N_req = 4` canonical, fixed.
- Canonical 10-seed set: `{77, 101, 123, 234, 456, 789, 1011,
  1213, 1415, 2021}`.

The concrete per-seed `L_ray_i` table from ED-SC 3.3.5 §2 applies
verbatim; all values remain safely below Window A's 2.50 edge
(max `L_ray = 2.37 lu` on seed 456).

---

## 3. Protocol

Per seed `i`:

1. **Evolve** the canonical ED-SIM mobility engine with the
   canonical parameters and the seed's RNG from scratch
   (alpha=0.03, gamma=0.5, noise_sigma=0.0556, mobility_exp=2.7,
   steps=500, size=64, dt=0.05, periodic boundary). This matches
   the ED-SC 3.2.6 v2 / ED-SC 3.3 / ED-SC 3.3 α_filt-sub-scan /
   ED-SC 3.3.5 field cache bit-identically.
2. **Snapshot cadence:** burn-in 100 steps, then record the
   field every 10 steps. Total **40 snapshots per seed** across
   the remaining 400 steps — the canonical ξ cadence of
   `ed_sc_3_1_xi_canonical.py` (verbatim).
3. **Motif extraction per snapshot.** At each of the 40
   snapshots, compute motifs under the canonical filter
   `(α_filt = 0.25, N_req = 4)` at the seed's own
   `L_ray_i = 1.08 · ξ_i`. Accumulate ρ-values into a per-seed
   pool.
4. **Per-seed statistics.** On the per-seed pool:
   - `N_i` — total motif count across the 40 snapshots.
   - `S1_i` — median ρ.
   - `S2_i` — IQR of ρ.
   - `S3_i` — upper-tail log-slope.
   - Bootstrap 16–84 % CIs (4000 resamples, matching the
     ED-SC 3.x convention).
5. **Pooled statistics.** Pool motifs across all 10 seeds and
   compute `(S1_pool, S2_pool, S3_pool)` with the same
   bootstrap procedure.
6. **Per-seed deviations** per ED-SC 3.3.5 §4:
   - `ΔS1_i = |S1_i − S1_pool| / |S1_pool|`
   - `ΔS2_i = |S2_i − S2_pool| / |S2_pool|`
7. **Cross-seed flatness threshold** per ED-SC 3.0 rev. 3:
   - `S2_rel_SEM_across_seeds = std(S2_i) / (|S2_pool| · √10)`
   - `flat_thresh = max(0.20, 2 · S2_rel_SEM_across_seeds)`
8. **Snapshot cadence diagnostic.** Per seed, record the
   snapshot-level motif count `N_i_per_snap[k]` and the
   per-snapshot S1/S2 (where computable), to expose any
   non-stationarity within the seed's evolution that would
   confound the per-seed pool.
9. **ξ guardrail.** Inherited from `xi_canonical.json`
   (≥ 8/10 seeds within 20 % of `ξ_canonical`). No re-measurement.

---

## 4. Verdict criteria

The three-way taxonomy of ED-SC 3.3.5 §5 applies verbatim:

- **`Collapsed`** iff:
  - `ΔS1_i < flat_thresh` for all 10 seeds, AND
  - `ΔS2_i < flat_thresh` for all 10 seeds, AND
  - ξ guardrail ≥ 8/10 pass, AND
  - no per-seed `L_ray_i` falls in Window A or Window B.
- **`Broken-collapse`** iff:
  - ξ guardrail passes, AND
  - at least one seed has `ΔS1_i ≥ flat_thresh` or
    `ΔS2_i ≥ flat_thresh`.
  The verdict enumerates failing seeds with their `(ξ_i, L_ray_i,
  S1_i, S2_i, ΔS1_i, ΔS2_i, N_i)` for H-coord / H-shallow
  discrimination (§5).
- **`GuardrailFailure`** iff:
  - ξ guardrail < 8/10 pass, OR
  - any per-seed `L_ray_i` intersects a resonance-forbidden
    window.

---

## 5. Interpretation taxonomy

The distinguishing of H-stat / H-coord / H-shallow from the
ED-SC 3.3.6 verdict:

- **If `Collapsed`** → **H-stat confirmed.** ED-SC 3.3.5's
  Broken-collapse was a statistical-power artefact of
  single-snapshot extraction. The cross-scale invariance claim is
  robust at per-seed N ≈ 130–200 across 35 % natural ξ variation.
  Downstream: ED-SC 3.4 (1D ξ-scan over an order of magnitude) +
  GR-SC 1.0+ open with substantive evidence.
- **If `Broken-collapse` with L_ray-shell correlation** →
  **H-coord confirmed.** Per-seed shell-histogram analysis
  (recorded in §3 step 3) will identify whether failing seeds have
  `L_ray_i` landing on different integer-lattice shells than
  passing seeds. If so, the dimensionless coordinate `L_ray/ξ` is
  not the correct ξ-invariance rescaling; a shell-corrected or
  lattice-aware coordinate may be required. This would reopen the
  ED-SC 3.x arc at the coordinate-definition level.
- **If `Broken-collapse` without L_ray-shell correlation** →
  **H-shallow confirmed.** Pool-level invariance is real but
  per-realisation variance is ~order-unity. The cross-scale
  statement of ED-SC 3.1 rev. 3 needs qualification: it is an
  **ensemble** claim, not a realisation claim. Downstream memos
  and any GR-SC ratio-class invariant must inherit this
  qualification.

**If the verdict is ambiguous** (e.g. a single seed fails while
nine pass), it is cast as `Broken-collapse` but annotated as a
candidate single-outlier failure, with seed 456 (ξ=2.19, the
canonical ξ-outlier) the prior candidate.

---

## 6. Deliverables

- `outputs/ed_sc_3_3_6/per_seed_40snap_pools.csv` — one row per
  motif: `(seed, xi_seed, L_ray_seed, snap_index, i, j, lam_neg,
  lam_pos, ratio)`.
- `outputs/ed_sc_3_3_6/per_seed_40snap_summary.json` — master
  summary:
  - Simulator of record (filename string).
  - Canonical filter geometry `(α_filt = 0.25, N_req = 4)` +
    per-seed L_ray.
  - 10-row per-seed table: `(seed, ξ_i, L_ray_i, N_i, S1_i, S2_i,
    S3_i, S1_CI_i, S2_CI_i, ΔS1_i, ΔS2_i, N_i_per_snap[])`.
  - Pooled stats.
  - Cross-seed flatness: `S2_rel_SEM_across_seeds, flat_thresh,
    max_dS1, max_dS2`.
  - ξ guardrail (inherited).
  - Resonance-window check (per-seed `L_ray` vs Windows A, B).
  - Snapshot diagnostic: per-seed `N_i_per_snap` list for
    stationarity inspection.
  - `verdict ∈ {Collapsed, Broken-collapse, GuardrailFailure}`.

Artefacts live under `outputs/ed_sc_3_3_6/` (new directory, created
by the driver if absent) alongside the ED-SC 3.3.5 artefacts at
`outputs/ed_sc_3_3_5/`.

---

## 7. Consequences

- **Collapsed.** ED-SC 3.3.5's verdict is reclassified as
  low-N artefact. The ED-SC 3.x arc is validated at 35 % natural
  ξ variation; ED-SC 3.4 narrows to a deliberate 1D ξ-scan over an
  order of magnitude; GR-SC 1.0+ proceeds.
- **Broken-collapse (H-coord).** The dimensionless coordinate is
  wrong. A new memo
  `theory/ED_SC_3_3_7_CoordinateReconsideration.md` is required to
  propose a shell-corrected or lattice-aware coordinate before any
  downstream work.
- **Broken-collapse (H-shallow).** The cross-scale claim is
  qualified to "ensemble-pool-level invariance." ED-SC 3.1 rev. 3
  is not retracted, but every downstream claim citing it must
  inherit the qualification — including the GR-SC 1.0+ ratio-class
  invariants, which are fundamentally realisation-wise quantities.
  This would substantially re-scope GR-SC.
- **GuardrailFailure.** Not expected under the current xi_canonical
  table; defensive.

---

## 8. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.6 as a
  high-power repetition of ED-SC 3.3.5 with 40-snapshot pooling
  per seed to raise per-seed motif counts from ~3 to ~130–200 and
  distinguish statistical-underpower, coordinate-mis-specification,
  and ensemble-only invariance as the three live readings of the
  ED-SC 3.3.5 Broken-collapse verdict. No numerics.
