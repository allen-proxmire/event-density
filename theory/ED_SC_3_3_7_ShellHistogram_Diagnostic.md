# ED-SC 3.3.7 — Shell-Histogram Diagnostic (H-coord vs H-shallow)

**Status:** Pre-registration. Scope-only memo. No numerics.
**Parents:**
- `theory/ED_SC_3_3_6_PerSeedCollapse_40Snapshot.md` (40-snapshot
  per-seed collapse; Broken-collapse verdict).
- `theory/ED_SC_3_3_5_PerSeedCollapse.md` (single-snapshot precursor).
- `theory/ED_SC_3_2_6_RayBudget_Resonance.md` rev. 2 (shell-crossing
  resonance mechanism on the L_ray axis; canonical shell-histogram
  analysis protocol).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` (canonical
  operating point).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.6 execution).

---

## 1. Purpose

ED-SC 3.3.6 executed the high-power (40-snapshot per seed)
distributional-collapse test at per-seed `L_ray_i = 1.08 · ξ_i` on
the 10 canonical seeds. The verdict was **Broken-collapse**, with a
narrow and structured pattern:

- **S1 collapses** cleanly across all 10 seeds (max ΔS1 = 0.115 at
  the ED-SC 3.0 rev. 3 threshold of 0.20).
- **S2 fails on three seeds** (max ΔS2 = 0.518 on seed 456).
  Failing seeds: 456 (S2 = 2.988, high outlier), 789 (S2 = 1.440,
  low), 1213 (S2 = 1.494, low). Passing seeds occupy S2 ∈ [1.68,
  2.15].

Two hypotheses remain live from ED-SC 3.3.6 §5:

- **H-coord** — the dimensionless coordinate `L_ray/ξ` is not the
  correct ξ-invariance rescaling. Per-seed S2 divergence correlates
  with integer-lattice-shell reassignment of the ray endpoints,
  analogous to the ED-SC 3.2.6 L_ray-axis resonance mechanism. A
  post-hoc rounding proxy in ED-SC 3.3.6's report suggested seed 456
  sits on a distinct diagonal-ray shell from the other nine seeds
  (`round(L/√2) = 2` vs `1`), but the proxy is coarse and cannot
  distinguish seeds 789 and 1213.
- **H-shallow** — the pool-level invariance is real but
  per-realisation variance is structural: S2 divergence is genuine
  ensemble spread that does not flatten at high per-seed N. The ED-
  SC 3.1 rev. 3 claim would then be ensemble-only, requiring
  qualification on every downstream cite including GR-SC 1.0+
  ratio-class invariants.

**This memo pre-registers a direct discriminator.** For each motif
admitted by the canonical filter at the seed's own L_ray, the 4
ray endpoints sit at integer-lattice positions `(di, dj)` on the
64² lattice; each endpoint has a shell radius `r = √(di² + dj²)`.
The set of admitted-motif shell radii is the direct diagnostic of
integer-lattice geometry selection by the filter. If failing seeds
have shell distributions systematically different from passing
seeds, H-coord is confirmed; if shell distributions overlap but
S2 still diverges, H-shallow is confirmed.

This is a pure diagnostic memo; no change to the ED-SC 3.x scope
or to the canonical operating point is proposed. The sole output is
a classification of the ED-SC 3.3.6 Broken-collapse verdict as
H-coord, H-shallow, or Mixed.

---

## 2. Definitions

For each admitted motif at saddle position `(i, j)` with
orthogonal eigenvectors `e_neg, e_pos` and filter L_ray:

- **4 ray endpoints** at `(round(sign · e · L_ray))` for
  `e ∈ {e_neg, e_pos}` and `sign ∈ {+1, −1}`. Each endpoint is a
  pair of signed integers `(di, dj)`.
- **Per-endpoint shell radius** `r = √(di² + dj²)`. Integer
  lattice shells are labelled by distinct values of `di² + dj²`:
  `√1 = 1, √2 ≈ 1.414, √4 = 2, √5 ≈ 2.236, √8 ≈ 2.828, √9 = 3, …`.
- **Per-motif mean shell radius** `r̄_m = mean_k r_k` for `k =
  1..4`. A scalar per motif that characterises the geometric
  `size` of the admitted quadrupole ensemble.

Per seed, over the 40-snapshot motif pool:

- **Shell histogram `H_seed(r)`** — count of endpoint shell radii.
  Length = total admitted motifs × 4.
- **Mean-shell histogram `M_seed(r̄)`** — count of per-motif mean
  shell radii. Length = total admitted motifs.
- **Dominant shell** — modal value of `H_seed(r)`.
- **Shell entropy** `S_seed = −Σ_r p(r) log p(r)` on `H_seed`
  (Shannon bits) — scalar summary of how concentrated the shell
  distribution is.

---

## 3. Protocol

1. **Re-run per-seed 40-snapshot evolution** exactly as in
   ED-SC 3.3.6: canonical parameters, canonical seeds, burn-in
   100, snap every 10, 40 snapshots per seed, per-seed
   `L_ray_i = 1.08 · ξ_i` from `xi_canonical.json`, canonical
   filter `(α_filt = 0.25, N_req = 4)`. Field evolution is
   deterministic and bit-equivalent to ED-SC 3.3.6.
2. **For each admitted motif**, compute the 4 ray endpoints
   and their shell radii. Record also the motif's ρ-ratio
   (preserved from ED-SC 3.3.6 for cross-indexing).
3. **Per seed**, accumulate `H_seed(r)` (shell histogram of
   4 × N_motifs entries) and `M_seed(r̄)` (mean-shell
   histogram of N_motifs entries). Compute dominant shell and
   shell entropy.
4. **Cross-seed comparison:** compute the Jensen–Shannon
   divergence `JS(H_i, H_pool)` between each seed's shell
   histogram and the pooled-across-seeds shell histogram. JS is a
   bounded [0, ln 2] symmetric divergence; high values indicate
   the seed draws from a distinct shell distribution.
5. **Per-seed vs per-seed cross-check:** compute the JS
   divergence matrix `JS(H_i, H_j)` across all pairs. If failing
   seeds cluster separately from passing seeds in shell-space,
   H-coord is confirmed.

---

## 4. Diagnostic criteria

Apply the following decision rule:

- **H-coord confirmed** iff **both**:
  - The three failing seeds (456, 789, 1213) show
    `JS(H_fail, H_pass_median) > JS_pass` where `JS_pass` is the
    maximum JS divergence among the seven passing seeds against
    the pooled-passing histogram; **or** the failing seeds admit a
    shell not admitted (or dramatically under-represented) by the
    passing seeds; **and**
  - The shell-distribution difference correlates with the S2
    divergence sign (seed 456 high-S2 ↔ larger shells; seeds 789,
    1213 low-S2 ↔ constrained or shifted shell subset).
- **H-shallow confirmed** iff:
  - All 10 seeds have JS divergence below the passing-seed spread
    `JS_pass` (shell distributions effectively identical), **and**
  - S2 divergence persists at its ED-SC 3.3.6 values
    (no shell-geometry explanation).
- **Mixed verdict** iff:
  - At least one failing seed is explained by shell geometry
    (H-coord) and at least one is not (H-shallow). Each failing
    seed is annotated individually.

---

## 5. Deliverables

- `outputs/ed_sc_3_3_7/shell_histograms_seed{seed}.json` (10
  files) — per-seed diagnostic:
  - `seed, xi_seed, L_ray_seed, N_motifs, N_endpoints`
  - `shell_histogram`: dict `{shell_str: count}` (endpoint shells,
    all 4 rays × motifs).
  - `mean_shell_histogram`: dict `{bin_center: count}` with fixed
    bin edges for cross-seed comparison (e.g. Δr̄ = 0.1).
  - `dominant_shell, shell_entropy_bits`.
  - `per_motif`: list of `{snap_index, i, j, ratio, r_1, r_2, r_3,
    r_4, mean_r}` for cross-indexing with ED-SC 3.3.6 pool.
- `outputs/ed_sc_3_3_7/shell_summary.json` — master aggregate:
  - 10-row per-seed table including dominant shell, entropy,
    `JS(H_seed, H_pool)`, ED-SC 3.3.6 S1/S2/ΔS1/ΔS2, fail flag.
  - JS divergence matrix `(10×10)` across all seed pairs.
  - Diagnostic verdict: `{H-coord, H-shallow, Mixed}`.
  - Pooled shell histogram (all 10 seeds) for reference.

---

## 6. Interpretation routing

- **H-coord confirmed.** The ED-SC 3.x cross-scale coordinate
  `L_ray/ξ` is insufficient on the 64² lattice — a shell-corrected
  or lattice-aware coordinate is required before the invariance
  claim can be sustained. This triggers
  `theory/ED_SC_3_3_8_CoordinateReconsideration.md` (not in
  scope of this memo) to propose either (a) shell-binned
  aggregation, (b) continuum-limit extrapolation via lattice
  rescaling, or (c) a redefined hinge that absorbs the shell
  geometry. Neither ED-SC 3.4 nor GR-SC 1.0+ proceeds until the
  coordinate is fixed.
- **H-shallow confirmed.** The cross-scale claim of ED-SC 3.1
  rev. 3 is qualified to ensemble-pool-level invariance; per-
  realisation invariance does not hold. Every downstream memo
  (including GR-SC 1.0+ ratio-class predictions) must inherit the
  qualification. ED-SC 3.4 is re-scoped from a narrow ξ-scan to
  an ensemble-vs-realisation calibration memo.
- **Mixed.** Each failing seed gets its own diagnosis. Seed 456
  is the prior H-coord candidate (its `L_ray = 2.37 lu` is close
  to Window A's 2.50 edge, and its `round(L/√2)` differs from the
  other nine seeds). Seeds 789 and 1213 might be H-shallow
  sub-class outliers. The Mixed verdict spawns two parallel
  downstream memos: H-coord remediation for seed 456, H-shallow
  qualification for seeds 789/1213.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens the shell-histogram
  diagnostic as a direct H-coord / H-shallow discriminator of the
  ED-SC 3.3.6 Broken-collapse verdict. Pre-registers endpoint
  shell extraction, per-seed histograms, Jensen–Shannon cross-
  seed divergence, and the three-way decision rule. No numerics.
