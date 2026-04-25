# ED-SC 3.3.8 — Coordinate Reconsideration (H-coord resolution)

**Status:** Diagnostic + pre-registration. Resolves the H-coord
component of the ED-SC 3.3.7 Mixed verdict. Proposes candidate
coordinate corrections; defers selection to the
pre-registered ED-SC 3.3.8a experiment.
**Parents:**
- `theory/ED_SC_3_3_7_ShellHistogram_Diagnostic.md` (shell-
  histogram diagnostic; Mixed verdict).
- `theory/ED_SC_3_3_6_PerSeedCollapse_40Snapshot.md` (40-snapshot
  collapse test; Broken-collapse).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (H-shallow twin).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` (canonical
  operating point).
- `theory/ED_SC_3_2_6_RayBudget_Resonance.md` rev. 2 (L_ray-axis
  shell-crossing resonance mechanism).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (sibling to ED-SC 3.3.9).

---

## 1. Purpose

ED-SC 3.3.7 classified **one** of the three ED-SC 3.3.6 S2
failures as **H-coord (seed 456)**: the per-seed collapse broke
because the seed's per-seed `L_ray_i` pushed the 4-ray filter into
a distinct integer-lattice shell set (`√8 = 2.828` shell admitted;
48 of 268 endpoints) that the other nine seeds never reach. Its
`JS_vs_pass_pool = 0.0716` sits **3.8× above** the
passing-seed spread threshold.

The two remaining failures (seeds 789, 1213) are H-shallow and
addressed in `theory/ED_SC_3_3_9_EnsembleVsRealisation.md`. This
memo addresses only the H-coord failure: a coordinate-system
issue, not a physics issue. The ED-SC 3.1 rev. 3 canonical
operating point and the ED-SC 3.x arc's structural findings are
unchanged by this memo; what is re-examined is only the
dimensionless coordinate `L_ray/ξ` itself, and whether it absorbs
the integer-lattice geometry of the 4-ray `N_req = 4` motif filter
on the 64² lattice.

This memo is a **coordinate-system reconsideration, not a physics
revision.** Its downstream effect is to select (or not) a revised
dimensionless hinge for ED-SC 3.4 scoping and GR-SC 1.0+
referencing. No new execution is performed; the sole new artefact
is the pre-registration of ED-SC 3.3.8a, the experiment to select
among the candidate remediations proposed in §4.

---

## 2. Empirical inputs

From `outputs/ed_sc_3_3_7/shell_summary.json`:

**Seed 456 shell histogram.** Three shells admitted:

| shell | count | fraction |
|---:|---:|---:|
| 2.000 | 124 | 0.463 |
| 2.236 (√5) | 96 | 0.358 |
| **2.828 (√8)** | **48** | **0.179** |

No other seed admits any endpoint on shell 2.828. Across the nine
other seeds (40 snapshots each, 9 × 780 ≈ 7 K endpoints), shell
√8 count is **0**. Pooled across all 10 seeds, all 48 √8 endpoints
come from seed 456 alone.

**Seed 456 JS divergences.**

- `JS_vs_pool = 0.0492` (per-seed vs 10-seed pooled histogram)
- `JS_vs_pass_pool = 0.0716` (per-seed vs 7-seed passing-pool
  histogram)
- Pass-pool max JS = 0.0187 on seed 101
- H-coord threshold (1.5×) = 0.0280
- Seed 456: 0.0716 > 0.0280 → H-coord confirmed

**Seed 456 L_ray.** `ξ_456 = 2.191 lu` (24.6 % above
`ξ_canonical = 1.7575 lu`) → `L_ray_456 = 1.08 · 2.191 = 2.366
lu`. This is the largest per-seed `L_ray_i` in the canonical set;
seed 101 is the second-largest at 2.008 lu (well below the
crossing threshold — see §3).

**S1 is unaffected.** The median of the motif-ratio distribution
on seed 456 is `S1_456 = −2.186`; the pool median is `S1_pool =
−1.961`; `ΔS1_456 = 0.115`, below the 0.20 threshold. H-coord
affects S2 and the distribution shape, not its centre.

---

## 3. Diagnosis

The dimensionless hinge `L_ray/ξ = 1.08` asserts that the
motif-filter geometry is equivalent across seeds when
`L_ray_i = 1.08·ξ_i` holds. This is **continuous invariance**: it
assumes the filter acts the same at every `(L_ray, ξ)` pair on the
line `L_ray/ξ = 1.08`.

The 4-ray motif filter is **not continuously invariant**. Its
admitted-shell set is discretised by integer-lattice rounding:

- Principal-axis ray (eigenvector `e = (1, 0)` or `(0, 1)`):
  endpoint at `(round(L_ray), 0)`. Shell = `round(L_ray)`.
- Diagonal ray (eigenvector `e = (√½, √½) ≈ (0.707, 0.707)`):
  endpoint at `(round(0.707·L_ray), round(0.707·L_ray))`.
  Shell = `√2 · round(0.707·L_ray)`.

The diagonal ray's shell changes discretely as `0.707·L_ray`
crosses half-integer boundaries:

- `0.707·L_ray < 1.5` → rounds to 1 → shell √2 ≈ 1.414
- `0.707·L_ray ≥ 1.5` → rounds to 2 → shell √8 ≈ 2.828
- `0.707·L_ray ≥ 2.5` → rounds to 3 → shell √18 ≈ 4.243, …

**The diagonal-shell crossing at `(1,1) → (2,2)` occurs at**

    L_ray_crossing = 1.5 / 0.707 ≈ 2.121 lu

corresponding, on the canonical hinge `L_ray = 1.08·ξ`, to

    ξ_crossing = 2.121 / 1.08 ≈ 1.964 lu.

**Empirical verification against the canonical seed set:**

| seed | ξ_i (lu) | L_ray_i (lu) | 0.707·L_ray_i | rounds to | diagonal shell |
|---:|---:|---:|---:|---:|---:|
| 77    | 1.6229 | 1.7527 | 1.2392 | 1 | √2 |
| 234   | 1.6365 | 1.7675 | 1.2497 | 1 | √2 |
| 2021  | 1.6415 | 1.7728 | 1.2534 | 1 | √2 |
| 789   | 1.6630 | 1.7960 | 1.2699 | 1 | √2 |
| 1415  | 1.7177 | 1.8551 | 1.3116 | 1 | √2 |
| 1011  | 1.7271 | 1.8653 | 1.3188 | 1 | √2 |
| 123   | 1.7456 | 1.8852 | 1.3330 | 1 | √2 |
| 1213  | 1.7717 | 1.9134 | 1.3529 | 1 | √2 |
| 101   | 1.8589 | 2.0076 | 1.4194 | 1 | √2 |
| **456** | **2.1905** | **2.3658** | **1.6726** | **2** | **√8** |

Nine of ten seeds have `0.707·L_ray_i ∈ [1.24, 1.42]`, all
rounding to 1 (shell √2). Seed 456 has `0.707·L_ray_i = 1.673`,
rounding to 2 (shell √8). The shell-crossing threshold
`0.707·L_ray = 1.5` separates the ensemble cleanly: seed 101 at
1.419 is the closest-approaching passing seed, but still 6 % below
threshold; seed 456 at 1.673 is 11 % above. No seed sits in the
ambiguous neighbourhood of the crossing — the split is sharp.

**Why `L_ray/ξ = 1.08` fails here.** The canonical hinge is a
**continuous** coordinate; shell crossings are **discrete**
events tied to the absolute value of `L_ray` in lattice units (or
equivalently, to `ξ` since `L_ray = 1.08·ξ`). The canonical
hinge cannot absorb a discrete threshold that lives in `ξ`-absolute
units. This is the same structural issue that ED-SC 3.2.6 mapped
on the L_ray axis (Windows A, B) — the motif filter has intrinsic
lattice resonances that the continuous hinge does not see. ED-SC
3.2.6 resolved this on the L_ray axis by **excluding** the
resonance windows; ED-SC 3.3.8 must either exclude an analogous
ξ-axis window or modify the coordinate.

---

## 4. Candidate remediations

Four candidates, ranked by invasiveness:

### (A) Shell-binned hinge

Define the dimensionless coordinate by the **shell-index class**
admitted by the filter rather than by continuous `L_ray/ξ`:

    C_shell(ξ) = (shell_axial(ξ), shell_diag(ξ))
    where shell_axial(ξ) = round(1.08·ξ)
          shell_diag(ξ)  = round(0.707·1.08·ξ)

Two ξ values are **coordinate-equivalent** iff their `C_shell`
matches. Under this rule, the canonical 10-seed set splits into
two classes:

- Class I: 9 seeds with `C_shell = (2, 1)` — dominant shells
  (2, √2).
- Class II: 1 seed (456) with `C_shell = (2, 2)` — dominant
  shells (2, √8).

**Pros:** cleanly lattice-aware; directly absorbs the crossing.
**Cons:** discretises the hinge; ED-SC 3.4 ξ-scan would need to
pre-register per-class reasoning rather than a continuous scan;
cross-class invariance is not claimed. Effectively admits that
invariance is class-local, not global.

### (B) ξ-restricted invariance (most conservative)

Restrict the ED-SC 3.1 rev. 3 cross-scale invariance claim to the
range

    ξ ∈ [1.6, ξ_crossing − margin]  where ξ_crossing ≈ 1.964 lu

yielding a valid range of roughly `[1.6, 1.85]` for the canonical
coordinate. All nine passing seeds sit inside this range; seed 456
is outside and is treated as a documented out-of-scope realisation
rather than a failure.

**Pros:** no coordinate changes; minimal memo churn; honest about
the canonical-set applicability; consistent with ED-SC 3.2.6's
L_ray-window exclusion precedent.
**Cons:** narrows the invariance claim; requires a new "ξ-window
exclusion list" analogous to the L_ray Windows A, B; ED-SC 3.4
must sub-sample near `ξ_crossing ≈ 1.964` to confirm crossing
behaviour experimentally.

### (C) Sub-integer correction

Shift the dimensionless hinge value to keep all seeds below the
crossing threshold:

    L_ray_i = c·ξ_i   with c < 1.08  chosen so that
    max_i (0.707 · c · ξ_i) < 1.5

At canonical max ξ (seed 456, 2.191 lu): the binding constraint is

    0.707 · c · 2.191 < 1.5 → c < 0.968.

This is a substantial reduction from 1.08; selecting `c = 0.95`
places all seeds at `0.707·L_ray ∈ [1.09, 1.47]`, safely below the
crossing.

**Pros:** preserves a single continuous hinge; no class structure.
**Cons:** the choice `c = 1.08` was certified in ED-SC 3.1 rev. 3
interior to the Regime-I plateau `L_ray/ξ ∈ [1.0, 1.4]`;
`c = 0.95` is outside this plateau on the low side (would require
re-certification per ED-SC 3.2.5) and may carry its own distinct
S1/S2 values. Changes the canonical operating point, which is a
heavier structural move than it looks.

### (D) Shell-aware effective coordinate

Define

    L_eff(L_ray) = L_ray · √2 · round(0.707·L_ray) / (0.707·L_ray)

or an analogous rescaling that snaps `L_ray` to the nearest shell.
Under this rule, two `L_ray` values are coordinate-equivalent iff
they share the same `(round(L_ray), round(0.707·L_ray))` pair,
which is equivalent to candidate (A) in information content but
implemented continuously via a piecewise rescaling.

**Pros:** continuous coordinate that absorbs shell geometry by
construction; preserves the look and feel of a single hinge.
**Cons:** algebraically awkward; `L_eff` is piecewise constant in
the shell-crossing neighbourhoods, introducing discontinuities at
the same boundaries; invariance testing is effectively identical
to (A) with extra formalism.

---

## 5. Evaluation criteria

A coordinate remediation is **valid** iff it satisfies all five:

1. **S1 invariance preserved.** The median of `f(ρ | ξ, filter)`
   remains `ΔS1 < 0.20` across the canonical 10-seed set under
   the revised coordinate. This is the strongest ED-SC 3.x result
   and must not regress.
2. **S2 collapse at ensemble level preserved.** `S2_rel_SEM
   across seeds` stays at or below the ED-SC 3.3.6 level (0.0697
   at per-seed 40-snapshot pooling), or equivalently the pool-
   level `S2_pool` stays within its 3.3.6 CI.
3. **No shell-crossing for any seed in the canonical set.** Under
   the revised coordinate, all 10 seeds admit the same shell set
   (ignoring per-seed realisation variance in which shells get
   populated how). Empirically: `JS_vs_pass_pool < 0.03` for all
   10 seeds.
4. **Continuity into ED-SC 3.4.** The coordinate must admit
   extension to ξ values outside the canonical [1.62, 2.19]
   range without introducing new resonance windows at the
   extension boundaries. If new crossings are unavoidable, the
   memo must name them explicitly (analogous to ED-SC 3.2.6
   Windows A, B).
5. **Consistency with ED-SC 3.1 rev. 3 canonical-point
   certification.** The canonical point `(L_ray/ξ, α_filt, N_req)
   = (1.08, 0.25, 4)` must remain within the valid coordinate
   region, or its re-certification under the new coordinate must
   be explicit and numerical. A remediation that invalidates the
   canonical point is a physics revision, not a coordinate
   reconsideration, and falls outside this memo's scope.

### Preliminary evaluation

| criterion | (A) Shell-binned | (B) ξ-restricted | (C) Sub-integer | (D) Shell-aware |
|---|:---:|:---:|:---:|:---:|
| S1 preserved | ✓ (no geometry change within class) | ✓ | re-cert needed | ✓ |
| S2 ensemble collapse | ✓ within-class | ✓ within restricted range | re-cert needed | ✓ within-class |
| No crossing in canonical set | ✓ (class I is uniform) | ✓ (seed 456 excluded) | ✓ | ✓ |
| ED-SC 3.4 continuity | partial — must pre-register class structure | ✓ with explicit window list | ✓ (below crossing) | partial — piecewise |
| ED-SC 3.1 rev. 3 canonical-point compatibility | ✓ (point is in class I) | ✓ | ✗ (outside Regime-I) | ✓ |

**Remediation (C) fails criterion 5 preliminarily and should be
dropped unless Regime-I is re-scanned at `c = 0.95` and the
canonical point moved.** Candidates (A), (B), (D) are all valid;
the selection is a scope-vs-cleanliness tradeoff. My preliminary
ordering: **(B) > (A) > (D)** — (B) is minimal, honest, and
precedent-consistent with ED-SC 3.2.6's window exclusion pattern;
(A) and (D) are functionally equivalent but add formalism without
a clear gain.

---

## 6. Next steps — ED-SC 3.3.8a pre-registration

**Experiment.** Select among remediations (A), (B), (D) by
running a single targeted 40-snapshot scan that crosses the
shell boundary. Pre-registered scope:

- **ξ-axis fine scan.** ξ ∈ [1.85, 2.10] at Δξ = 0.025 (11
  points). This brackets the predicted `ξ_crossing ≈ 1.964 lu`
  and extends 0.14 lu on either side. Implementation: vary the
  per-seed ξ target by deliberately rescaling the initial
  amplitude or the mobility prefactor (TBD in driver
  implementation; must preserve the simulator of record).
- **Alternative implementation.** If deliberate ξ-scan proves
  awkward, run the shell-histogram diagnostic on **10 fresh
  seeds** drawn to have ξ values densely sampling
  `[1.85, 2.10]` — bypasses the need for ξ-control.
- **Observables per ξ-point.** Shell histogram, dominant shell,
  JS divergence vs a passing-class reference, S1, S2, per-seed
  `(L_ray, 0.707·L_ray)` rounding analysis.
- **Pass criterion for remediation (B) ξ-restricted.** Shell
  histograms jump discretely at `ξ ≈ 1.964` (or wherever the
  crossing empirically lies) with the predicted √2 → √8
  reassignment. No other crossings detected in the scanned
  range. S1 remains continuous across the crossing.
- **Pass criterion for remediation (A) / (D) shell-binned.**
  Within each shell class (Class I: `C_shell = (2, 1)`; Class II:
  `C_shell = (2, 2)`) S1 and S2 collapse independently. Cross-
  class stats are distinct but internally flat.
- **Deliverables:** `outputs/ed_sc_3_3_8a/xi_crossing_scan.json`
  + per-ξ-point summaries + a selected-remediation tag
  `{B, A, D}`.

After ED-SC 3.3.8a closes:

- **If (B) selected:** amend ED-SC 3.0 rev. 3 to add a `ξ-window
  exclusion list` guardrail analogous to the L_ray Windows A, B.
  Amend ED-SC 3.1 rev. 3 to cite the ξ-range validity of the
  certification (`ξ ∈ [1.6, 1.95]` or the empirically-measured
  interval). Amend ED-SC 3.3.9 §4(c) to swap the 2.0 lu rough
  threshold for the measured value.
- **If (A) or (D) selected:** amend ED-SC 3.1 rev. 3 to carry
  the shell-binned coordinate; amend ED-SC 3.3.6, 3.3.7, 3.3.9
  to fold in class structure; expand the guardrail list in
  ED-SC 3.0 rev. 3.

**Current action.** This memo is diagnostic + pre-registration
only. No driver is written in this memo turn; the 3.3.8a driver
is a future work item. No existing memos are modified; the
forward-pointer lines recommended by ED-SC 3.3.9 §5 are still
pending dedicated revision memos.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.8 as the
  H-coord resolution of the ED-SC 3.3.7 Mixed verdict.
  - Identifies the diagonal-ray shell crossing `(1, 1) → (2, 2)`
    at `L_ray = 1.5/0.707 ≈ 2.121 lu`, equivalently
    `ξ = 1.964 lu` under the canonical hinge `L_ray/ξ = 1.08`.
  - Separates the canonical 10-seed set into two shell-index
    classes: Class I `C_shell = (2, 1)` (9 seeds), Class II
    `C_shell = (2, 2)` (seed 456 alone).
  - Proposes four candidate remediations (A shell-binned,
    B ξ-restricted, C sub-integer, D shell-aware). Preliminary
    ordering: B > A > D; C disqualified by criterion 5 unless
    Regime-I is re-certified.
  - Pre-registers ED-SC 3.3.8a (11-point Δξ = 0.025 scan around
    `ξ_crossing` to select among remediations).
  - No changes to existing memos or drivers; forward-pointer
    amendments to ED-SC 3.0 / 3.1 / 3.3.9 are flagged but not
    applied.
