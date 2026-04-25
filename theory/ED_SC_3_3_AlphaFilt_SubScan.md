# ED-SC 3.3 — α_filt Sub-Scan (N_req = 4 anomaly)

**Status:** Pre-registration. Scope-only memo. No numerics.
**Parent:** `theory/ED_SC_3_3_FilterGeometry_Scope.md` rev. 1.
**Context driver:** `analysis/scripts/ed_sc_3_3_filter_geometry_scan.py`,
  full-run outputs `outputs/ed_sc_3_3/filter_geometry_summary.json`.
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3 full sweep).

---

## 1. Purpose

The full ED-SC 3.3 filter-geometry sweep (20 cells, 5 α_filt × 4
N_req, hinge sub-sweep L_ray/ξ ∈ {1.00, …, 1.20}) flagged **three
cells** under the hinge-flatness criterion (S2 relative span > 0.20):

| cell | α_filt | N_req | hinge-flatness rel-span |
|---|---|---|---|
| `alpha0.10_Nreq4` | 0.10 | 4 | 0.212 |
| `alpha0.15_Nreq4` | 0.15 | 4 | 0.209 |
| `alpha0.20_Nreq4` | 0.20 | 4 | 0.355 |

All three cluster along the **α_filt ≤ 0.20 × N_req = 4** edge of
the grid. The canonical cell `(α_filt=0.25, N_req=4)` flatness-passes
at 0.075; the `(α_filt=0.30, N_req=4)` cell also flatness-passes at
0.022 but exhibits a monotonic S2 drop from 1.288 (canonical) to
0.987 (≈ 22 % below canonical). The N_req = 5 column is empirically
empty (0 motifs) across all α_filt — a hard geometric exclusion by
the 4-ray filter.

Three hypotheses are live for the α_filt ≤ 0.20 × N_req = 4 flags:

- **H1 (resonance):** a discrete resonance in the
  `(α_filt, L_ray, N_req = 4)` subspace, analogous to the
  integer-lattice-shell resonances on the L_ray axis
  (ED-SC 3.2.6), now driven by the α_filt angular tolerance.
- **H2 (smooth boundary):** the N_req = 4 column transitions
  smoothly from a large-IQR regime (small α_filt, many motifs
  but wider distribution) into the canonical regime (0.25) and
  then into the N_req = 5 empty regime (large α_filt strictness
  → vanishing pool) — no discrete jumps, just a monotonic ramp
  that locally exceeds the 20 % flatness threshold.
- **H3 (sampling artefact):** the three flags are a consequence
  of low motif counts (N = 233–450 compared to 4000+ at
  N_req = 2), and the hinge-flatness threshold was set for the
  canonical pool size; at lower N the expected sampling-noise
  width in S2 alone can exceed 20 %.

This sub-scan pre-registers a **Δα_filt = 0.025** resolution scan
across `α_filt ∈ [0.10, 0.25]` at fixed `N_req = 4` to discriminate
among H1/H2/H3 before ED-SC 3.3 verdicts are finalised.

No numerics are presented in this memo. This is pre-registration only.

---

## 2. Operating point

All runs anchor at the certified canonical operating point:

| parameter | value | source |
|---|---|---|
| ξ (canonical) | **1.7575 lu** | `outputs/ed_sc_3_1/xi_canonical.json` |
| L_ray (canonical) | **1.898 lu** (L_ray/ξ = 1.08) | ED-SC 3.1 rev. 3 §2 |
| N_req | **4** (fixed) | subject of the sub-scan |
| α_filt | swept on a 7-point grid | this memo §3 |

All L_ray values used by the hinge sub-sweep lie **inside Regime I
[1.0, 1.4]** and **outside** the resonance-forbidden Windows A
(`L_ray ∈ [2.50, 2.80]`) and B (`L_ray ∈ [3.50, 3.90]`).

---

## 3. α_filt fine grid

Seven points at Δα_filt = 0.025:

    α_filt ∈ {0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250}

- Lower anchor 0.100 matches the lowest full-ED-SC-3.3 cell
  (flagged).
- Upper anchor 0.250 matches the canonical cell (flatness-passed).
- The three previously-flagged values (0.10, 0.15, 0.20) are
  re-run at identical geometry so flags can be reproduced.
- Four new points (0.125, 0.175, 0.225, 0.250) populate the gaps
  to resolve whether S2 exhibits discrete shoulders or a smooth ramp.

---

## 4. Hinge sub-sweep

Unchanged from ED-SC 3.3:

    L_ray/ξ ∈ {1.00, 1.05, 1.10, 1.15, 1.20}
    L_ray  ∈ {1.7575, 1.8454, 1.9333, 2.0212, 2.1090} lu

All five points inside Regime I; none in Windows A or B. Converted
to absolute L_ray using the canonical `ξ = 1.7575 lu`.

Per `(α_filt)` cell, 7 × 5 = 35 motif collections on the shared
field cache.

---

## 5. Simulator of record

- Driver: `r2_grf_falsifier_tests.py`
- Update: `ED_Update_Rule.ed_step_mobility`
- Canonical parameters (unchanged, inherited from `fr` module):
  `alpha=0.03, gamma=0.5, noise_sigma=0.0556, mobility_exp=2.7,
  steps=500, size=64, dt=0.05`.
- Canonical seeds (unchanged): `{77, 101, 123, 234, 456, 789, 1011,
  1213, 1415, 2021}`.
- No module globals or canonical parameters are mutated.
- Deterministic given seeds.

---

## 6. ξ guardrail

Per seed, ξ is computed via the canonical 40-snapshot half-decay
method (GR-SC 1.7 density channel): burn-in 100, snap every 10,
40 snapshots total per seed. Cell passes iff ≥ 8/10 seeds lie
within 20 % of `ξ_canonical = 1.7575 lu`. Single-snapshot ξ is not
permitted for guardrail evaluation (ED-SC 3.2.6 rev. 2 §5.2).

The ξ computation is done **once** at the start of the run and
reused across all 7 α_filt cells (the field evolution is
independent of filter geometry).

---

## 7. Deliverables

Per α_filt cell (7 cells total):

- `outputs/ed_sc_3_3/pool_alpha{α}_Nreq4_subscan.csv` — pooled ρ
  values across the 5-point hinge sub-sweep, one row per motif;
  columns `(L_ray, L_ray_over_xi, ratio)`.
- `outputs/ed_sc_3_3/summary_alpha{α}_Nreq4_subscan.json` — cell
  summary including:
  - `(α_filt, N_req = 4, L_ray_canonical)`
  - per-hinge-point `(N, S1, S2, S3, CIs)`
  - pooled `(N, S1, S2, S3, CIs)`
  - `hinge_flatness_rel_span` and `hinge_flatness_flag`
  - `motif_count_profile` (N_motifs per hinge point) for
    correlating S2 jumps with motif-count changes (see §8).

Master summary:

- `outputs/ed_sc_3_3/alpha_subscan_summary.json` — aggregates the
  7 cell summaries into a 7 × 5 grid of `(N, S1, S2)` indexed by
  `(α_filt, L_ray/ξ)` plus a top-level `resonance_verdict`,
  `alpha_profile[]` (S2 vs α_filt at each hinge point), and a
  `motif_count_table[]` (N vs α_filt at each hinge point).

Artefact filenames use `{α}` with decimals written as `0p100`,
`0p125`, etc., to match the ED-SC 3.3 `pool_alpha0p25_Nreq4.csv`
convention.

---

## 8. Registered interpretation

**Resonance verdict — H1 (Confirmed).** A discrete α_filt-axis
resonance is declared iff **both** of the following hold:

- any cell shows `hinge_flatness_rel_span > 0.20` (step in S2
  across the hinge sub-sweep), AND
- S2 jumps correlate with **discrete jumps in motif count N**
  across the hinge sub-sweep, specifically `|ΔN|/N_mean > 0.15`
  coincident with the S2 jump. (Shell transitions on the L_ray
  axis of ED-SC 3.2.6 exhibited this correlation; a geometry
  reconfiguration of the admitted-motif set produces joint
  jumps in pool size and IQR.)

**Smooth-boundary verdict — H2.** If all hinge-flatness values
are ≤ 0.20 **or** if flatness-flagged cells do not show coincident
motif-count jumps, and S2 varies **monotonically** across the
7-point α_filt grid, the α_filt ≤ 0.20 × N_req = 4 anomaly is
classified as a smooth boundary between the canonical Regime-I
interior and the N_req = 5 empty regime. In this case the full
ED-SC 3.3 verdicts for (α=0.10/0.15/0.20, N_req=4) are upgraded
from `Refuted` to `Confirmed-boundary` (a new tag under the
ED-SC 3.2.5 regime taxonomy), with a note that the 20 % flatness
threshold is calibrated for plateau interiors and is a
conservative false-positive at low-N boundary cells.

**Sampling-artefact verdict — H3.** If flatness-flagged cells
show S2 relative standard error `σ_S2 / S2_mean > 0.15` (derived
from the bootstrap CIs), and N < 500, the anomaly is classified as
a sampling artefact. In this case the flatness threshold is
re-specified as `max(0.20, 2·σ_S2/S2_mean)` prospectively, and
the three ED-SC 3.3 flags are retracted.

Exactly one verdict must be emitted. If the evidence is mixed
(e.g. H1 at one α_filt, H2 at another), the memo §10 changelog
will record a **Mixed** verdict with sub-cells labelled
individually, and ED-SC 3.3 integration will proceed per-cell.

---

## 9. Next steps

- After this sub-scan closes with a verdict, **integrate ED-SC 3.3**
  (`theory/ED_SC_3_3_FilterGeometry_Scope.md` rev. 2) with the
  corrected per-cell verdicts reflecting H1/H2/H3.
- If **H1 confirmed**, open a follow-up memo
  `theory/ED_SC_3_3_AlphaFilt_ShellMap.md` mapping the α_filt
  resonance mechanism to a specific geometric feature of the
  motif filter (analogous to the ED-SC 3.2.6 integer-lattice-shell
  explanation on the L_ray axis).
- If **H2 confirmed**, amend ED-SC 3.0 rev. 2 §5.1 S-F2 to exempt
  low-N boundary cells (N < 500) from the 20 % flatness threshold,
  OR introduce a size-dependent flatness threshold as
  standard guardrail.
- If **H3 confirmed**, amend the ED-SC 3.3 driver's flatness
  threshold prospectively and retract the three false-positive
  flags.
- In all cases, the **N_req = 5 empty column** — a hard geometric
  exclusion by the canonical 4-ray filter — must be documented
  as a constraint in the ED-SC 3.3 pre-registration (N_req ≤
  n_rays) and carried forward to ED-SC 3.4.

---

## 10. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens the α_filt sub-scan.
  Pre-registers the 7-point Δα = 0.025 grid at fixed N_req = 4
  across the shared 5-point hinge sub-sweep, inherits all
  guardrails from ED-SC 3.0 rev. 2 and 3.2.6 rev. 2, and commits
  to a three-way verdict taxonomy (H1 resonance / H2 smooth
  boundary / H3 sampling artefact, with Mixed as a fallback).
  No numerics.
