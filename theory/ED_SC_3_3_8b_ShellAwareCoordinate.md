# ED-SC 3.3.8b — Shell-Aware Effective Coordinate (remediation D)

**Status:** Pre-registration + execution-ready. Formalises the
shell-aware effective coordinate selected by ED-SC 3.3.8a (verdict
D) and pre-registers the per-seed re-test under this coordinate
to close the H-coord branch of ED-SC 3.3.7.
**Parents:**
- `theory/ED_SC_3_3_8_CoordinateReconsideration.md` (four
  candidate remediations; this memo formalises (D)).
- `theory/ED_SC_3_3_8a_XiCrossing_Scan.md` (selection experiment:
  **verdict D** at monotone √8 shell admission from ξ = 2.025
  with S2 varying smoothly across the transition).
- `theory/ED_SC_3_3_6_PerSeedCollapse_40Snapshot.md` (40-snapshot
  per-seed protocol inherited).
- `theory/ED_SC_3_3_7_ShellHistogram_Diagnostic.md` (H-coord
  classification of seed 456).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (S2 ensemble-only
  qualification — orthogonal axis unchanged by this memo).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.8a).

---

## 1. Purpose

ED-SC 3.3.8a selected **remediation D (shell-aware coordinate)**
because across the ξ ∈ [1.85, 2.10] scan the diagonal-ray shell
admission transitioned monotonically (first √8 endpoint at ξ =
2.025), S1 remained stable (max ΔS1 = 0.098 < 0.20), but S2
varied **smoothly** across the transition (max single-step
|ΔS2| = 0.257, below the discrete-jump threshold 0.489 = 0.20
· mean(S2)). Remediations (A) shell-binned and (B) ξ-restricted
are not selected; remediation (C) was disqualified a priori by
Regime-I compatibility in ED-SC 3.3.8 §4.

This memo (a) formalises the shell-aware coordinate `L_eff`
exactly, (b) pre-registers the re-test ED-SC 3.3.8b which re-runs
the ED-SC 3.3.6 per-seed 40-snapshot collapse test at `L_eff_i`
instead of the canonical `L_ray_i = 1.08·ξ_i`, and (c) states
the expected outcome: seed 456 re-enters the passing class,
seeds 789 and 1213 remain H-shallow (unchanged, per ED-SC
3.3.9's orthogonal qualification).

---

## 2. Definition of the shell-aware coordinate

**Shell-index function.** For a candidate ray length `L > 0`,

    r_diag(L) ≡ round(0.707 · L)

is the integer diagonal endpoint index — the rounded value at
which a diagonal ray with eigenvector `e = (√½, √½)` terminates
on the lattice. `r_diag(L)` jumps at the half-integer rounding
boundaries `0.707·L ∈ {0.5, 1.5, 2.5, …}`.

**Shell-aware effective ray length.** Define

    L_eff(L) ≡ L · ( s / (0.707 · L) )     where s = r_diag(L)
             = s / 0.707
             = √2 · s                        (equivalent form)

Within each shell-index class `{L : r_diag(L) = s}`, `L_eff` takes
the single value `√2 · s`. The mapping `L ↦ L_eff` is **piecewise
constant**, discretised at the shell boundaries. This collapses
all realisations that share a diagonal shell onto a common
effective ray length, exactly absorbing the integer-lattice
geometry that the continuous hinge `L_ray/ξ = 1.08` does not
see.

**Shell-class labels** (for the canonical 10-seed set at
`L_ray_i = 1.08·ξ_i`):

    Class s = 1:   0.707·L ∈ [0.5, 1.5)   →  L_eff = √2  ≈ 1.4142
    Class s = 2:   0.707·L ∈ [1.5, 2.5)   →  L_eff = √8  ≈ 2.8284
    Class s = 3:   0.707·L ∈ [2.5, 3.5)   →  L_eff = √18 ≈ 4.2426
    …

In the canonical set, 9 seeds are Class 1 (L_eff = √2), 1 seed
(456) is Class 2 (L_eff = √8). No canonical seed is Class 3 or
higher.

**Resonance-window check.** Class-2 `L_eff = √8 ≈ 2.8284 lu`
sits just above Window A's upper edge `2.80 lu`; defensively, the
driver must hard-fail if any per-seed `L_eff` falls in Window A
(`[2.50, 2.80]`) or Window B (`[3.50, 3.90]`). Under the current
canonical ξ table the shell-aware L_eff avoids both windows by a
narrow margin (~0.03 lu above Window A's upper edge).

**Caveat.** L_eff is substantially smaller than the canonical
`L_ray = 1.898 lu` of ED-SC 3.1 rev. 3 (L_eff = 1.414 lu is 26 %
below canonical). This means the re-test operates at a ray length
outside the Regime-I plateau `L_ray/ξ ∈ [1.0, 1.4]` that was
certified in ED-SC 3.2.5 — L_eff/ξ_canonical = 1.414/1.7575 =
0.805, below the plateau lower edge. The **re-test should
therefore be interpreted as a shell-equivalence test, not a
canonical-plateau reproduction test.** Per-seed stats are
expected to differ from the canonical pool `(S1 = −1.881,
S2 = 1.271)`; what matters is collapse **across seeds** under
the new coordinate, not reproduction of the canonical numbers.

---

## 3. Operating point

- `α_filt = 0.25` (canonical, fixed)
- `N_req = 4` (canonical, fixed)
- For each seed `i` in the canonical set:
  - `ξ_i` loaded from `outputs/ed_sc_3_1/xi_canonical.json`
    (canonical 40-snapshot value — not recomputed).
  - `L_ray_i = 1.08 · ξ_i` (diagnostic only; not used for motif
    extraction here).
  - `r_diag_i = round(0.707 · L_ray_i)` — shell index class.
  - **`L_eff_i = √2 · r_diag_i`** — the per-seed motif-extraction
    ray length.
- Canonical seeds: `{77, 101, 123, 234, 456, 789, 1011, 1213,
  1415, 2021}` — same set as ED-SC 3.3.6.
- Simulator of record and canonical parameters unchanged.

**Concrete per-seed table** (derived from the
`xi_canonical.json` values):

| seed | ξ_i (lu) | L_ray_i (lu) | 0.707·L_ray_i | s = r_diag | L_eff_i (lu) |
|---:|---:|---:|---:|---:|---:|
| 77   | 1.6229 | 1.7527 | 1.2392 | 1 | 1.4142 |
| 101  | 1.8589 | 2.0076 | 1.4194 | 1 | 1.4142 |
| 123  | 1.7456 | 1.8852 | 1.3330 | 1 | 1.4142 |
| 234  | 1.6365 | 1.7675 | 1.2497 | 1 | 1.4142 |
| 456  | 2.1905 | 2.3658 | 1.6726 | **2** | **2.8284** |
| 789  | 1.6630 | 1.7960 | 1.2699 | 1 | 1.4142 |
| 1011 | 1.7271 | 1.8653 | 1.3188 | 1 | 1.4142 |
| 1213 | 1.7717 | 1.9134 | 1.3529 | 1 | 1.4142 |
| 1415 | 1.7177 | 1.8551 | 1.3116 | 1 | 1.4142 |
| 2021 | 1.6415 | 1.7728 | 1.2534 | 1 | 1.4142 |

Nine seeds collapse to `L_eff = √2`; seed 456 alone takes
`L_eff = √8`.

---

## 4. Protocol

Re-run the ED-SC 3.3.6 40-snapshot per-seed collapse test with
`L_eff_i` in place of `L_ray_i`:

1. **Evolve** each seed with canonical parameters (bit-identical
   to ED-SC 3.3.6); record 40 snapshots (burn-in 100, snap every
   10).
2. **Extract motifs** at each snapshot under
   `(α_filt = 0.25, N_req = 4, L_ray = L_eff_i)`; pool across
   snapshots.
3. **Per-seed statistics**: `N_i, S1_i, S2_i, S3_i` with
   bootstrap 16–84 CIs (4000 resamples).
4. **Pooled statistics**: across all 10 seeds.
5. **Per-seed deviations**: `ΔS1_i, ΔS2_i` vs pooled.
6. **Cross-seed flatness threshold** (ED-SC 3.0 rev. 3
   size-corrected):
   `flat_thresh = max(0.20, 2·S2_rel_SEM_across_seeds)`.
7. **Shell-aware L_eff guard**: hard-fail at launch if any
   `L_eff_i` intersects Window A or Window B.

---

## 5. Verdict criteria

Apply the ED-SC 3.3.5 / 3.3.6 three-way taxonomy, re-interpreted
for the shell-aware re-test:

- **`Collapsed`** — the primary pass criterion:
  - All 10 seeds have `ΔS1_i < flat_thresh`, AND
  - All 10 seeds have `ΔS2_i < flat_thresh`, AND
  - ξ guardrail ≥ 8/10 pass (inherited from xi_canonical.json).
  **Interpretation.** Remediation D resolves both H-coord
  (seed 456 re-enters the passing class) and, unexpectedly, also
  absorbs the H-shallow spread from seeds 789 and 1213. Would
  suggest the per-realisation S2 spread observed in ED-SC 3.3.6
  was partly an artefact of the continuous hinge and not purely
  ensemble noise.
- **`Collapsed-seed456-only`** — target pass criterion for this
  memo:
  - `ΔS1_i < flat_thresh` for all seeds (S1 invariance preserved).
  - Seed 456 now has `ΔS1, ΔS2 < flat_thresh` (H-coord resolved).
  - Seeds 789 and 1213 **still fail** (H-shallow remains per
    ED-SC 3.3.9; this is expected, not a remediation failure).
  **Interpretation.** H-coord branch closed cleanly; H-shallow
  branch unchanged. The two-resolution invariance statement of
  ED-SC 3.3.9 stands, now with coordinate-refined wording: S1
  invariant per-realisation under L_eff; S2 invariant
  ensemble-only under L_eff.
- **`Broken-collapse`** — the unexpected failure mode:
  - Seed 456 still fails after L_eff application, OR
  - S1 collapse breaks under the coordinate shift, OR
  - A new seed becomes a failure under L_eff that was passing
    under L_ray.
  **Interpretation.** Remediation D does not resolve H-coord; a
  fresh memo is required to explore remediations (A) shell-binned
  or hybrid approaches.
- **`GuardrailFailure`** — ξ guardrail < 8/10 OR any
  L_eff ∈ Windows A/B (the latter is structural, not statistical).

---

## 6. Deliverables

- `outputs/ed_sc_3_3_8b/per_seed_shellaware_pools.csv` — one row
  per motif: `(seed, xi_i, L_eff_i, s_index, snap_index, i, j,
  lam_neg, lam_pos, ratio)`.
- `outputs/ed_sc_3_3_8b/per_seed_shellaware_summary.json` —
  master summary:
  - Simulator of record.
  - Canonical filter `(α_filt=0.25, N_req=4)`.
  - 10-row per-seed table with ξ_i, L_ray_i, r_diag_i, L_eff_i,
    N_i, S1_i, S2_i, S3_i, CIs, ΔS1_i, ΔS2_i, per-seed verdict
    (pass / H-coord-still / H-shallow).
  - Pooled statistics.
  - Cross-seed flatness diagnostics.
  - ξ guardrail (inherited from xi_canonical.json).
  - Resonance-window check on all L_eff values.
  - Master verdict `{Collapsed, Collapsed-seed456-only,
    Broken-collapse, GuardrailFailure}`.

Artefacts live under `outputs/ed_sc_3_3_8b/` (new directory).

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.8b as the
  shell-aware re-test of ED-SC 3.3.6 under the coordinate
  selected by ED-SC 3.3.8a. Formalises L_eff = √2 · r_diag(L_ray)
  (equivalently `L · s / (0.707·L)` with `s = round(0.707·L)`),
  pre-registers the four-way verdict taxonomy including the new
  primary-target `Collapsed-seed456-only` class, and declares
  the canonical-plateau caveat: L_eff = 1.414 lu is outside the
  Regime-I plateau `[1.0, 1.4]`, so the re-test is a shell-
  equivalence test across seeds rather than a canonical-pool
  reproduction test. No numerics.
