# ED-SC 3.1 rev. 3 — Canonical Operating Point Certification

**Status:** Scope patch — certification only. No new numerics.
**Parent:** `theory/ED_SC_3_1_rev2_Rectification.md`
**Inputs:** `theory/ED_SC_3_2_LrayXi_Scan.md` rev. 2 (coarse scan),
            `theory/ED_SC_3_2_5_G3_G4_Transition.md` (fine-grid plateau map),
            `theory/ED_SC_3_2_6_RayBudget_Resonance.md` (resonance confirmation).
**Simulator of record:** `r2_grf_falsifier_tests.py`
            + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post-ED-SC 3.2.6).

---

## 1. Purpose

ED-SC 3.1 rev. 2 (`ED_SC_3_1_rev2_Rectification.md`) corrected the
simulator-of-record attribution and anchored the canonical
correlation length at **ξ = 1.7575325729470939 lu** (10-seed,
40-snapshot mean, GR-SC 1.7 half-decay, density channel; artefact
`outputs/ed_sc_3_1/xi_canonical.json`).

Two downstream diagnostics now jointly certify the ED-SC 3.1
canonical operating point as **stable and interior to a Regime-I
plateau**, safely removed from the discrete ray-budget resonances
intrinsic to the motif filter on the 64² lattice:

- **ED-SC 3.2.5** mapped the hinge `L_ray/ξ ∈ [1.0, 2.5]` at
  Δ = 0.1 and identified a three-regime structure with sharp
  shoulders at `L_ray/ξ ≈ 1.50` and `≈ 2.10`.
- **ED-SC 3.2.6** resolved those shoulders at Δ(L_ray) = 0.02,
  confirmed the integer-lattice-shell hypothesis (√4 → √9 and
  √10 → √16 reassignments), and closed the guardrail under the
  canonical 40-snapshot ξ method with a 9/10 pass.

This memo is a scope-only patch. It does not introduce new
numerics; it **certifies** what the 3.2.x arc established.

---

## 2. Canonical operating point

- **Dimensionless hinge:** `L_ray/ξ = 1.08`.
- **Absolute ray length:** `L_ray = 1.08 × 1.7575 ≈ 1.898 lu`.
- **Filter geometry:** `α_filt = 0.25`, `N_req = 4` (unchanged
  from ED-SC 3.1 rev. 2).

**Canonical pool values (preserved from ED-SC 3.1 rev. 2):**

| statistic | value | notes |
|---|---|---|
| N (pool size) | 34 | 10 seeds, 500 steps |
| S1 (median ρ) | **−1.881** | 16–84 % CI [−2.341, −1.464] |
| S2 (IQR ρ) | **1.271** | from pooled ratios |
| S3 (upper-tail slope) | operational | shape reading only |

**Regime-I plateau (from ED-SC 3.2.5 fine scan):**
across `L_ray/ξ ∈ [1.0, 1.4]` — the plateau interior that contains
the canonical point — the simulator of record yields

| L_ray/ξ | S1 | S2 | N |
|---:|---:|---:|---:|
| 1.00 | −1.913 | 1.270 | 32 |
| 1.10 | −1.913 | 1.257 | 34 |
| 1.20 | −1.913 | 1.194 | 32 |
| 1.30 | −1.913 | 1.212 | 34 |
| 1.40 | −1.922 | 1.223 | 33 |

S1 and S2 are flat to ≤ 6 % across a 0.4-wide window bracketing
`L_ray/ξ = 1.08`. The canonical pool values lie **interior to this
plateau**, within sampling noise, and are not the result of a
local extremum or a boundary effect.

---

## 3. Resonance exclusion zones

ED-SC 3.2.6 (verdict: **Confirmed**) established that the motif
filter exhibits discrete ray-budget resonances at integer-lattice
shell crossings of the ray endpoints. Two such zones were mapped
at Δ(L_ray) = 0.02 resolution:

| zone | L_ray window (lu) | L_ray/ξ window | dominant shell transition |
|---|---|---|---|
| **Window A** | [2.50, 2.80] | [1.42, 1.59] | **√4 (2.000) → √9 (3.000)** |
| **Window B** | [3.50, 3.90] | [1.99, 2.22] | **√10 (3.162) → √16 (4.000)** |

**These windows are structural properties of the motif filter,
not of the field.** They are intrinsic to the 4-ray,
`N_req = 4`, integer-lattice geometry and must be excluded from
any canonical or near-canonical operating region.

Resonance mechanism (short): as `L_ray` grows, the four
principal-axis ray endpoints at `(round(e · L_ray_i),
round(e · L_ray_j))` transition through integer lattice shells
of radius `√(di² + dj²)`. Each transition reconfigures the
admitted-motif set in integer-valued jumps, producing step
changes in `f(ρ | ξ, filter)` that bracket two adjacent
Regime-I / Regime-II / Regime-III plateaus.

---

## 4. Certification statement

The canonical operating point

    (L_ray/ξ, α_filt, N_req) = (1.08, 0.25, 4),
    L_ray ≈ 1.898 lu at ξ = 1.7575 lu,

is hereby certified as:

1. **Interior to Regime I.** The canonical point lies at the
   centre of the `[1.0, 1.4]` plateau established by ED-SC 3.2.5.
   S1 and S2 are flat (≤ 6 %) across a 0.4-wide neighbourhood
   that brackets it.
2. **Far from resonance windows.** The nearest resonance zone
   (Window A, `L_ray ∈ [2.50, 2.80]`) begins at `L_ray/ξ ≈ 1.42`
   — **31 % above** the canonical hinge value. Window B is
   further still.
3. **Stable under ED-SC 3.2.5 and ED-SC 3.2.6.** Both diagnostics
   reproduce the canonical pool (`N ≈ 33`, `S1 ≈ −1.91`,
   `S2 ≈ 1.23`) at the canonical operating point within sampling
   noise.
4. **Suitable as the anchor for ED-SC 3.3.** Filter-geometry
   scans over `α_filt` and `N_req` may anchor at this point
   with the confidence that observed drifts are filter-geometry
   effects, not hinge or resonance confounds.

### 4.1 Resolution qualification (ED-SC 3.3.6 / 3.3.7 / 3.3.8 / 3.3.8a / 3.3.8b / 3.3.9 / 3.3.10)

The per-seed distributional-collapse arc (ED-SC 3.3.5 through
ED-SC 3.3.10) refined the certification above at two resolutions
and closed the shell-geometry coordinate question. The final
four-clause statement (from `theory/ED_SC_3_3_10_ArcClosure.md`
§3) applies:

- **(a) S1 (median ρ) is invariant at per-realisation resolution**
  across the canonical 10-seed ensemble spanning 35 % natural ξ
  variation. Max `ΔS1 = 0.115 < flat_thresh = 0.20`
  (ED-SC 3.0 rev. 3 size-corrected threshold). The canonical
  median carries over to individual realisations under the
  dimensionless hinge `L_ray/ξ = 1.08`. This is the strongest
  surviving ED-SC 3.x cross-scale result.
- **(b) S2 (IQR of ρ) is invariant at ensemble-pool resolution
  only.** Per-realisation S2 exhibits ~25 % irreducible spread
  across the canonical set that is **not explained by shell-
  geometry artefacts** (H-shallow; seeds 789 and 1213 in
  ED-SC 3.3.7 had JS-vs-pass-pool ≤ 0.007, within the passing-
  seed spread, yet still failed on ΔS2). The canonical `S2 =
  1.271` is an ensemble-pool value; single-realisation
  predictions built from S2 must carry the per-realisation
  spread as part of the claim. Any downstream S2-derived
  invariant (GR-SC 1.0+ ratio / quadratic / Rayleigh /
  correlation classes) inherits this spread as prediction
  uncertainty. See `theory/ED_SC_3_3_9_EnsembleVsRealisation.md`
  §4 for the formal rephrasing.
- **(c) Coordinate validity: `r_diag(L_ray) = 1`, equivalently
  `ξ ≲ 1.964 lu`.** The dimensionless hinge `L_ray/ξ = 1.08`
  applies to realisations whose diagonal ray endpoint lands on
  shell √2 (i.e. `round(0.707·L_ray) = 1`), equivalently
  `ξ < ξ_crossing = 1.5 / (0.707 · 1.08) ≈ 1.964 lu`.
  **Realisations with `r_diag = 2` (shell √8; e.g. canonical seed
  456 at ξ = 2.19 lu) are rescued by the shell-aware coordinate**
  `L_eff = √2 · r_diag(L_ray)` per ED-SC 3.3.8b: seed 456's ΔS2
  dropped from 0.518 (failing under the continuous hinge) to
  0.159 (passing under L_eff), and its ΔS1 was already passing.
  The shell-aware remediation was selected by ED-SC 3.3.8a
  (verdict D: monotone √8 shell admission across the crossing at
  ξ = 2.025 with S1 stable and S2 smooth). **The canonical
  operating point `(L_ray/ξ = 1.08, ξ_canonical = 1.7575 lu)`
  sits strictly inside `r_diag = 1`; the certification in §3 is
  unchanged.**
- **(d) Realisations with `r_diag(L_ray) ≥ 3` are not yet
  tested** and lie outside the current claim's domain. Pre-
  registration for any scan or calibration crossing into
  `r_diag ≥ 3` must either adopt L_eff with per-shell-class
  statistics reported separately or scope the new shell class
  explicitly.

These are **qualifications of the resolution and coordinate
validity** at which the invariance statement applies, not
retractions of the certification. The canonical operating point
remains stable, interior to Regime I, interior to `r_diag = 1`,
and suitable as the anchor for all ED-SC 3.x downstream work —
including ED-SC 3.4 (ensemble-vs-realisation calibration along
ξ) and GR-SC 1.0+ (curvature-invariant taxonomy with the (a)/(b)
per-invariant inheritance).

---

## 5. Guardrail inheritance

ED-SC 3.1 rev. 3 inherits, by reference, the following guardrails
from sibling memos:

- **Regime-based S-F2** — ED-SC 3.0 rev. 2 §5.1. The 20 %
  tolerance applies only within a contiguous regime of the
  hinge scan; cross-regime drifts are diagnostic, not
  falsifying.
- **Resonance-mapping clause** — ED-SC 3.0 rev. 2 §5.2. Any new
  hinge introduced by a depth memo must be sub-sampled at
  Δ ≤ 0.1 across its reported window to resolve regime
  boundaries, with regime membership declared before falsifier
  readings are reported.
- **Simulator-of-record guardrail** — ED-SC 3.1 rev. 2 §6.
  Every ED-SC 3.x numerical claim must cite the simulator of
  record (`r2_grf_falsifier_tests.py` +
  `ED_Update_Rule.ed_step_mobility`) by filename. No module
  globals or canonical parameters are mutated.
- **Canonical ξ method** — ED-SC 3.2.6 rev. 2 §5.2. Per-seed
  ξ for any guardrail check uses the 40-snapshot average method
  (burn-in 100, snap every 10, GR-SC 1.7 half-decay on the
  density channel). Single-snapshot ξ is not permitted for
  guardrail evaluation.

No new guardrails are introduced here. The inheritance is
explicit so that ED-SC 3.3 can cite this memo as the source
list.

---

## 6. Consequences for ED-SC 3.3

ED-SC 3.3 is **unblocked**. Its pre-registration (forthcoming
`theory/ED_SC_3_3_FilterGeometry_*.md`) must include:

- **Resonance-window exclusion list.** No operating point may
  fall within `L_ray ∈ [2.50, 2.80]` or `L_ray ∈ [3.50, 3.90]`
  lattice units at the canonical ξ. Wider windows may be
  flagged if ED-SC 3.3 scans reveal further shell crossings
  under varied `α_filt` or `N_req`.
- **Canonical L_ray anchor.** The α_filt / N_req sweeps anchor
  at `L_ray ≈ 1.898 lu` (`L_ray/ξ = 1.08`), inside the
  certified Regime-I plateau.
- **Hinge sub-sampling requirement.** Δ ≤ 0.1 in the
  dimensionless coordinate of any new hinge introduced by
  ED-SC 3.3 (e.g. α_filt, N_req sweeps). Falsifier readings
  require regime membership to be declared explicitly.
- **Verdict taxonomy.** ED-SC 3.3 drivers must emit one of
  `{Confirmed, Refuted, GuardrailFailure}` for every
  pre-registered resonance or regime check, following the
  convention established in ED-SC 3.2.6.

No other ED-SC 3.1 content changes.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, early):** initial ED-SC 3.1 depth memo
  (`ED_SC_3_1_Distribution_Baselines.md`); included fabricated
  ξ ≈ 2.4 and exGauss parameters — superseded.
- **Rev. 2 (2026-04-23, mid):** rectification memo
  (`ED_SC_3_1_rev2_Rectification.md`) — fixed simulator-of-record
  attribution, anchored canonical ξ = 1.7575 lu from
  `xi_canonical.json` (10-seed 40-snapshot mean), re-derived the
  canonical pool (N = 34, S1 = −1.881, S2 = 1.271, CI
  [−2.341, −1.464]). Invalidated rev. 1 baselines.
- **Rev. 3 (2026-04-23, this memo):**
  - Certifies the canonical operating point
    `(L_ray/ξ, α_filt, N_req) = (1.08, 0.25, 4)` as interior to
    the Regime-I plateau `[1.0, 1.4]` established by ED-SC 3.2.5.
  - Incorporates the resonance-window exclusion list
    (Window A `L_ray ∈ [2.50, 2.80]`; Window B `L_ray ∈ [3.50,
    3.90]`) confirmed by ED-SC 3.2.6.
  - Declares guardrail inheritance from ED-SC 3.0 rev. 2,
    ED-SC 3.1 rev. 2, and ED-SC 3.2.6 rev. 2 explicitly.
  - Unblocks ED-SC 3.3 and specifies its pre-registration
    requirements.
  - No change to canonical pool values or ξ anchor — rev. 3 is
    certification only.
