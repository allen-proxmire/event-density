# ED-SC 3.4-σ₁ Multi-Seed — Per-Realisation σ₁ Spread at Canonical ξ

**Status:** Pre-registration + execution-ready. Follow-up F2 from
GR-SC 1.3-Scoping §7. Targets replacement of the pessimistic ±25 %
per-realisation κ uncertainty band (inherited from ED-SC 3.3.9's S2
measurement) with a directly-measured σ₁ per-seed spread. No
falsifier verdict; pure calibration for downstream GR-SC 1.3
uncertainty refinement.
**Parents:**
- `theory/GR_SC_1_3_RayleighClass_Scoping.md` §7 F2 (pre-registered
  this scan as the follow-up to replace Rule R5 (iii)).
- `theory/GR_SC_1_3_RayleighClass_Predictions.md` §5.3 (per-realisation
  band currently inherits ED-SC 3.3.9's S2 spread as a conservative
  transfer; F2 measures it directly).
- `theory/ED_SC_3_4_sigma1_Calibration.md` (σ₁ ξ-calibration at
  single seed 77; this memo inherits its pipeline verbatim at a
  single ξ point).
- `theory/ED_SC_3_3_10_ArcClosure.md` §3 (four-clause invariance
  statement; r_diag = 1 canonical window).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness
  threshold; shell-class validity window).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post GR-SC 1.3-Predictions consolidation).

---

## 1. Purpose

The κ prediction in GR-SC 1.3-Predictions carries four
independent uncertainty bands. The **per-realisation ±25 %** band
(Rule R5 (iii)) dominates by a factor of 2.3× over the next-
largest component and is the single cheapest intervention to
tighten. Its current value is **inherited, not measured**: the
25 % figure comes from ED-SC 3.3.9's S2-spread characterisation
on the canonical 10-seed set and was provisionally transferred
to σ₁ as a conservative band.

**F2 replaces that transfer with a direct σ₁ measurement.** At
the canonical operating point `ξ = 1.7575 lu`, the ED-SC 3.4-σ₁
pipeline is re-run across a 10-seed set to obtain the per-seed
σ₁_std distribution, from which the true per-realisation spread
(mean, std, IQR, coefficient of variation) is computed.

Expected outcomes:

- **If measured σ₁ spread < 25 %**, Rule R5 (iii) band tightens,
  κ prediction improves, and the GR-SC 1.8 clearance `|N̂'| ≳ 78.6`
  envelope narrows. Most likely outcome based on ED-SC 3.3.9 S2
  spread of ~25 % being an upper-bound estimate.
- **If measured σ₁ spread ≈ 25 %**, Rule R5 (iii) band is
  validated at its current value; no quantitative κ change but
  the uncertainty structure is no longer provisional.
- **If measured σ₁ spread > 25 %**, Rule R5 (iii) band widens,
  κ prediction loosens. Structurally meaningful — would indicate
  σ₁ is noisier per-realisation than S2, requiring scope-level
  re-examination of the Rayleigh scaling's empirical precision.

No falsifier verdict is pre-registered. The output is a replacement
numerical band for Rule R5 (iii), quoted separately and handed
forward to a subsequent consolidation pass that will patch GR-SC
1.3-Predictions' four-band table.

---

## 2. Operating point

- **ξ:** single value `ξ = 1.7575 lu` (canonical; ED-SC 3.1 rev. 3).
  No ξ grid — F2 is a per-seed scan at fixed ξ.
- **Seed set:** `{11, 22, 33, 44, 55, 66, 77, 88, 99, 111}`
  (10 seeds; includes seed 77 for continuity with the single-seed
  ED-SC 3.4-σ₁ calibration). **Note:** this set is distinct from
  the ED-SC 3.x canonical 10-seed ensemble `{77, 101, 123, 234,
  456, 789, 1011, 1213, 1415, 2021}`. F2 uses a fresh set to
  avoid conflating the σ₁ per-realisation spread measurement with
  any per-seed idiosyncrasies of the canonical set.
- **Filter geometry:** `α_filt = 0.25`, `N_req = 4` (canonical,
  fixed).
- **Hinge:** `L_ray = 1.08 · ξ_measured` per seed (canonical
  continuous hinge).
- **Snapshot cadence:** burn-in 100, snap every 10, **40 snapshots
  per seed** (matches ED-SC 3.4-σ₁ cadence).
- **Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility` with canonical parameters
  unchanged.
- **ξ-control method:** IC-amplitude calibration pre-pass **per
  seed** (each seed has its own w ↔ ξ interpolant built from a
  9-point w sweep `{0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25,
  0.30, 0.35}`); interpolate to target ξ = 1.7575; one bisection
  refinement if `|ξ_measured − ξ_target| / ξ_target > 1 %`.
  Verbatim from ED-SC 3.4-σ₁ applied independently per seed.

---

## 3. Measurement

**Per-seed pipeline** (identical to ED-SC 3.4-σ₁ at its single ξ
target, repeated 10 times):

1. Calibration pre-pass on the seed: 9 evolutions over
   `CALIBRATION_W_GRID`; measure 40-snapshot ξ at each; build
   monotone interpolant `w(ξ)`.
2. Interpolate `w_target = w(ξ = 1.7575)`.
3. Evolve seed with `rng.uniform(0.5 − w_target, 0.5 + w_target)`
   for `fr.STEPS` timesteps.
4. Extract 40 snapshots (burn-in 100, snap every 10).
5. Measure `ξ_measured` via the canonical half-decay method;
   bisection refinement if miss > 1 %.
6. Compute `L_ray = 1.08 · ξ_measured`; guard against resonance
   windows A / B (hard-fail) and r_diag ≠ 1 (flag out-of-scope).
7. Collect motifs at each snapshot under
   `(α_filt = 0.25, N_req = 4, L_ray)`; pool `T_motif = λ_neg +
   λ_pos` across the 40 snapshots.
8. Per-seed statistics with bootstrap 16–84 CIs (4000 resamples):
   - `N_pool` — total admitted motif count.
   - `median_T` and CI.
   - `σ₁_std = std(T_motif)` and CI.
   - `σ₁_IQR_proxy = IQR(T_motif) / 1.349`.
   - Per-snapshot N, median, IQR (stationarity diagnostic).
   - Endpoint shell histogram (r_diag cross-check).

**Cross-seed aggregate statistics** (the F2 deliverables):

- `σ₁_std_values = [σ₁_std_seed_i for i in 1..10]` — the 10-point
  per-realisation population.
- `σ₁_std_mean` — arithmetic mean across seeds.
- `σ₁_std_std` — standard deviation across seeds (per-realisation
  spread, absolute).
- `σ₁_std_IQR` — IQR across seeds.
- `σ₁_std_CoV = σ₁_std_std / σ₁_std_mean` — **coefficient of
  variation**: the direct empirical counterpart to the ±25 %
  transfer band from ED-SC 3.3.9.
- `σ₁_std_range` — [min, max] per-seed values.
- **Per-seed relative deviation from seed 77**:
  `rel_dev_seed_i = (σ₁_std_seed_i − σ₁_std_seed_77) / σ₁_std_seed_77`.
  Anchors against the single-seed ED-SC 3.4-σ₁ value for
  continuity.

---

## 4. Outputs

**Per-seed rows in `sigma1_multiseed_table.csv`** (10 rows):

    seed, xi_target, xi_measured, miss_frac, w_used, refined,
    L_ray, r_diag, out_of_scope,
    N_pool,
    median_T, median_T_lo, median_T_hi,
    sigma1_std, sigma1_std_lo, sigma1_std_hi,
    sigma1_IQR_proxy,
    N_per_snap_mean,
    rel_dev_vs_seed77

**Master aggregate `sigma1_multiseed_summary.json`:**

- `method` string citing the simulator of record.
- Canonical parameters, filter geometry, snapshot schedule.
- `seeds`, `xi_target = 1.7575`.
- `per_seed[]` — full per-seed payload (calibration pre-pass,
  per-snapshot arrays, motif extraction stats).
- `cross_seed_aggregate`:
  - `sigma1_std_values[]` (10 numbers)
  - `sigma1_std_mean`, `sigma1_std_std`, `sigma1_std_IQR`,
    `sigma1_std_CoV`
  - `sigma1_std_range` (min, max)
  - `sigma1_IQR_proxy_values[]`, same aggregate stats
  - `median_T_values[]`, `median_T_mean`, rigid-zero-check
    across seeds
  - `rel_dev_vs_seed77[]` (10 numbers, one per seed)
- `r_diag_excursions[]`, `resonance_check` — expected empty.
- `wall_seconds_total`.

Artefacts live under `outputs/ed_sc_3_4_sigma1/` (existing
directory from the single-seed calibration).

---

## 5. Deliverables and downstream patching

**F2 emits a measured per-realisation band for σ₁:**

- Central replacement value for GR-SC 1.3-Scoping Rule R5 (iii):
  `δσ₁_per_real = σ₁_std_CoV · σ₁_std_mean`.
- Relative band for κ propagation: κ per-real band =
  `± σ₁_std_CoV × κ_central` (linear through `κ = |N̂'|·σ₁/(2√2)`).

**Symbolic κ update** (contingent on measured CoV, reported in
the execution summary):

    κ_per_real_new / |N̂'| ∈ [κ_central · (1 − CoV),
                              κ_central · (1 + CoV)]
                          × |N̂'|.

If `σ₁_std_CoV < 0.25`, the κ per-realisation band tightens;
dominance order among the four uncertainty components may shift.
If `σ₁_std_CoV ≥ 0.25`, the band persists or widens.

**GR-SC 1.3-Predictions patching is deferred to a subsequent
consolidation pass.** This memo emits the measured CoV; a
follow-up edit-only pass will update GR-SC 1.3-Predictions §5.3
and §6's prediction table, MEMORY.md's one-liner, and the arc
memory file. F2 alone does not modify any existing memo.

---

## 6. Diagnostic checks (pre-registered)

Analogous to ED-SC 3.4-σ₁ §7 but at the multi-seed level:

- **r_diag excursions** should be empty across all 10 seeds —
  each per-seed `L_ray = 1.08 · ξ_measured_seed` should sit at
  `r_diag = 1`. Defensive; expected to pass.
- **Rigid-zero aggregate** — does the cross-seed `median_T`
  distribution sit around zero, or is it systematically biased?
  Extends the ED-SC 3.4-σ₁ rigid-zero-check to a second
  ensemble. Positive confirmation at the canonical ξ would
  strengthen Reading (a) of GR-SC 1.3-Scoping Rule R3; large
  aggregate bias may trigger a follow-up memo.
- **Gaussianity aggregate** — the cross-seed ratio
  `mean(σ₁_std) / mean(σ₁_IQR_proxy)` should approximate the
  single-seed value (1.11 at canonical ξ from ED-SC 3.4-σ₁).
  Major deviation is a structural cross-check.
- **Calibration miss_frac** should be ≤ 1 % for all 10 seeds.
  If any seed misses, record and proceed — F2's scientific
  output is the measured σ₁_std_CoV, which is robust to small
  ξ misses.

No falsifier verdict. The diagnostic checks are reported in the
summary JSON but do not gate the CoV emission.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F2 as the multi-seed
  σ₁ spread measurement at canonical ξ. Pre-registers a 10-seed
  scan `{11, 22, 33, 44, 55, 66, 77, 88, 99, 111}` at single
  ξ = 1.7575 lu using the ED-SC 3.4-σ₁ pipeline verbatim at each
  seed's IC-amplitude-calibrated w. Emits the σ₁_std coefficient
  of variation (CoV) as the direct empirical replacement for
  GR-SC 1.3-Scoping Rule R5 (iii)'s ±25 % transfer band. Driver:
  `analysis/scripts/ed_sc_3_4_sigma1_multiseed.py`. GR-SC 1.3-
  Predictions patching is deferred to a subsequent consolidation
  pass. No numerics.
