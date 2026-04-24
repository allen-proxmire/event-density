# ED-SC 3.3.10 — ED-SC 3.3.x Arc Closure

**Status:** Closure memo. Integrates ED-SC 3.3.8 / 3.3.8a / 3.3.8b
/ 3.3.9 into a single operational statement. No new execution; no
new numerics beyond the already-executed artefacts.
**Parents:**
- `theory/ED_SC_3_3_8_CoordinateReconsideration.md` (H-coord
  diagnosis + four candidate remediations).
- `theory/ED_SC_3_3_8a_XiCrossing_Scan.md` (selection experiment
  → verdict D).
- `theory/ED_SC_3_3_8b_ShellAwareCoordinate.md` (shell-aware
  re-test; seed 456 rescued; Class-1 seeds statistically starved).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (S1 per-realisation
  / S2 ensemble-only qualification).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` (canonical
  operating point being qualified in operational domain).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness
  threshold + refined verdict taxonomy).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.8b).

---

## 1. Purpose

The ED-SC 3.3.x sub-arc is hereby **declared closed**. This memo
integrates the four-memo resolution of the ED-SC 3.3.6 + 3.3.7
Broken-collapse / Mixed verdicts and states the final operational
invariance statement for the ED-SC 3.x cross-scale claim.

**Three findings stand as durable structural conclusions:**

- **H-coord is resolved.** The diagonal-ray shell-crossing
  identified in ED-SC 3.3.8 was empirically bracketed by
  ED-SC 3.3.8a (monotone √8 admission, no discrete S2 jump, S1
  stable across the transition — verdict **D**, shell-aware
  effective coordinate). The shell-aware re-test of ED-SC 3.3.8b
  then rescued seed 456: its ΔS2 dropped from 0.518 (failing
  under the continuous hinge) to **0.159** (passing under
  `L_eff = √8`), cleanly below the size-corrected flat_thresh.
- **H-shallow is intrinsic, not coordinate-remediable.** The
  ED-SC 3.3.7 diagnostic classified seeds 789 and 1213 as
  H-shallow based on shell-histogram overlap with the passing
  pool; ED-SC 3.3.9 formalised this as genuine per-realisation
  S2 variability. The ED-SC 3.3.8b re-test did not and cannot
  rescue H-shallow — it is the structural property of `f(ρ | ξ,
  filter)` when viewed over finite realisations, and remains as
  the ensemble-vs-realisation qualification on the invariance
  statement.
- **The canonical invariance domain is `r_diag(L_ray) = 1`.**
  Operationally equivalent to `ξ ≲ 1.964 lu` under the canonical
  hinge `L_ray/ξ = 1.08`. Remediations (B) ξ-restricted and (D)
  shell-aware converge on the same practical restriction when
  the canonical operating point is constrained to the Regime-I
  plateau: only one shell class contains it.

No ED-SC 3.1 rev. 3 certification content is retracted. The
canonical operating point `(L_ray/ξ, α_filt, N_req) = (1.08,
0.25, 4)` remains interior to Regime I, and its pool statistics
`(N = 34, S1 = −1.881, S2 = 1.271)` stand as ensemble-pool
values for realisations with `r_diag = 1`.

---

## 2. Empirical summary

### 2.1 ED-SC 3.3.8a — coordinate-selection scan

11-point Δξ = 0.025 scan across `ξ ∈ [1.85, 2.10]` on fixed
seed 77 with IC-amplitude ξ-control (all miss fractions < 0.2 %).
Key outcomes from `outputs/ed_sc_3_3_8a/xi_scan_summary.json`:

- **Monotone √8 shell admission** at scan index 7 (ξ = 2.025 lu,
  L_ray = 2.189 lu). No reversals; a clean False → True
  transition.
- **S1 stable across the scan.** Max ΔS1 = 0.098 < flat_thresh
  0.20.
- **S2 varies smoothly, no discrete jump.** Max single-step
  |ΔS2| = 0.257, below the discrete-jump threshold 0.489 =
  0.20·mean(S2).
- **Verdict: D — shell-aware effective coordinate selected.**

### 2.2 ED-SC 3.3.8b — shell-aware re-test

10-seed re-test of ED-SC 3.3.6 with
`L_eff_i = √2 · round(0.707 · 1.08 · ξ_i)`. From
`outputs/ed_sc_3_3_8b/per_seed_shellaware_summary.json`:

- **Seed 456 rescued.** N_456 = 99 (was 67 at L_ray), S1 =
  −2.086, S2 = **1.606** (was 2.988), **ΔS2 = 0.159** (was
  0.518) — passes the size-corrected flat_thresh 0.479.
- **Class-1 seeds statistically starved.** Nine seeds collapse
  to `L_eff = √2 ≈ 1.414 lu`, below the Regime-I plateau
  `[1.0, 1.4]`. Per-seed motif counts: 4 seeds at N < 3 (no
  bootstrap possible), 5 seeds at N ∈ [3, 6] (bootstrap wide,
  verdict logic hits None propagation).
- **Driver emits `Broken-collapse`** because `s1_ok = all(dS1_i
  < flat_thresh)` fails on the None dS1 values, not because any
  computed ΔS1 exceeded threshold (max computed ΔS1 = 0.236 <
  flat_thresh 0.479). Reported verdict message is technically
  correct but wording is misleading.
- **Honest reading.** Class-1 re-test is uninformative due to
  motif-count starvation; only seed 456 (Class 2) carries signal
  and it confirms H-coord rescue. The 9 Class-1 seeds are
  compatible with the canonical operating point under the
  continuous hinge and were never H-coord failures — their
  absence of signal under L_eff = √2 reflects the operating
  point being outside the plateau, not a failure of coordinate
  D.

### 2.3 ED-SC 3.3.9 — ensemble-vs-realisation qualification

Formal rephrasing of the ED-SC 3.1 rev. 3 claim at two
resolutions:

- **S1 (median ρ)** is invariant at per-realisation resolution
  across the canonical ensemble (max ΔS1 ≤ 0.115 in ED-SC 3.3.6,
  ≤ 0.098 in ED-SC 3.3.8a). This is the strongest surviving
  ED-SC 3.x cross-scale result.
- **S2 (IQR of ρ)** is invariant at ensemble-pool resolution
  only. Per-realisation S2 carries ~25 % irreducible spread that
  is not attributable to shell geometry (seeds 789 and 1213 had
  JS-vs-pass-pool ≤ 0.007 and still failed at ΔS2 ∈ [0.241,
  0.269]).
- **S3 (upper-tail log-slope)** is defined at N ≥ 8 per seed and
  no cross-scale claim has been promoted for it.

---

## 3. Final invariance statement

Superseding the preliminary statement of ED-SC 3.1 rev. 3 §4.1,
the operational cross-scale invariance claim for the distributional
invariant `f(ρ | ξ, L_ray, α_filt, N_req)` is:

> **At the canonical operating point `(L_ray/ξ, α_filt, N_req) =
> (1.08, 0.25, 4)`, for realisations with `r_diag(L_ray) = 1`
> (equivalently, `ξ ≲ 1.964 lu` under the canonical hinge):**
>
> **(a) S1 (median ρ) is invariant at per-realisation resolution
> across 35 % natural ξ variation (max ΔS1 < 0.20 under the
> ED-SC 3.0 rev. 3 size-corrected flatness threshold).**
>
> **(b) S2 (IQR of ρ) is invariant at ensemble-pool resolution
> only, with irreducible ~25 % per-realisation spread not
> attributable to shell-geometry artefacts.**
>
> **(c) Realisations with `r_diag(L_ray) = 2` (seed 456 in the
> canonical ensemble; ξ > 1.964 lu on the 4-ray filter) are
> rescued by the shell-aware effective coordinate
> `L_eff = √2 · r_diag(L_ray)`. Their per-realisation S1 and S2
> under L_eff pass the collapse threshold against the canonical
> reference.**
>
> **(d) Realisations with `r_diag(L_ray) ≥ 3` are not yet tested
> and lie outside the current claim's domain.**

Clauses (a) and (b) are the same ensemble-vs-realisation
qualification as ED-SC 3.3.9 §4, now with the coordinate-validity
restriction (c) absorbing the H-coord branch.

---

## 4. Operational consequences

**Canonical operating point.** Unchanged. `(L_ray/ξ, α_filt,
N_req) = (1.08, 0.25, 4)`, `L_ray = 1.898 lu` at
`ξ_canonical = 1.7575 lu`. The canonical point sits at
`r_diag = 1`, strictly interior to the shell-class validity
domain. No re-certification is required.

**ξ-window of validity.** `ξ ≲ 1.964 lu` under the canonical
hinge, equivalently `r_diag(L_ray) = 1`. This is now a formal
guardrail analogous to the L_ray-axis Windows A, B of ED-SC
3.2.6. Outside this window, either the shell-aware coordinate
`L_eff` must be used (for `r_diag = 2`, confirmed by
ED-SC 3.3.8b) or the realisation is out-of-scope for the current
claim (`r_diag ≥ 3`).

**ED-SC 3.4 (multi-parameter coupling).** Pre-registration must:

- Restrict scan points to `r_diag(L_ray) = 1` unless the
  shell-aware coordinate `L_eff` is adopted and the
  corresponding Class-2 data are reported separately.
- Treat S2 observables as **ensemble-pool** quantities;
  per-realisation ΔS2 must be reported as a calibration
  output, not used as a pass criterion.
- Inherit all ED-SC 3.3.x guardrails including the new
  r_diag window.

**GR-SC 1.0+ (curvature-invariant taxonomy).** S1-derived
invariants (`r*`, `ℛ_Ray`, `ℛ_G`, `ℛ_W` via the algebraic map)
inherit per-realisation certainty from clause (a) and can be
cited as point predictions. S2-derived invariants (`C²` Weyl
square, `det G`, Rayleigh-class `κ` where its width reads on
σ₁ coupling) inherit **ensemble-pool certainty with ~25 %
per-realisation spread** from clause (b). GR-SC 1.8's EIT-
Extremal error budget should absorb this spread into its
`σ₁/κ_M` clearance calculation where σ₁-derived quantities are
used.

**H-coord testing going forward.** Before any result is declared
on a realisation with `r_diag ≥ 2`, the shell-aware L_eff test
must be run. The canonical 10-seed set has exactly one such
realisation (seed 456); a broader ensemble may contain more
and must be partitioned by shell class before aggregation.

---

## 5. Recommended updates (deferred to a subsequent consolidation pass)

The following forward-pointer patches are **recommended** but are
**not applied by this memo** — they belong to a dedicated
consolidation pass that also updates project memory and the
living orientation documents together, to keep the audit trail
coherent.

**`theory/ED_SC_3_0_rev3_ScopePatch.md`** — extend the §5
guardrail inheritance list with a **shell-class guardrail**:

> `r_diag(L_ray) = round(0.707 · L_ray) = 1` is the canonical
> shell-class validity window for the dimensionless hinge
> `L_ray/ξ = 1.08`. Realisations with `r_diag = 2` are rescued
> by the shell-aware coordinate `L_eff = √2 · r_diag(L_ray)` per
> ED-SC 3.3.8b. Realisations with `r_diag ≥ 3` are outside the
> current claim's domain.

The current forward-pointer paragraph appended in the
thirteenth-pass consolidation already cites ED-SC 3.3.8 and
3.3.9; a fourteenth-pass update should replace "ED-SC 3.3.8a is
pre-registered" with the closure statement: **"ED-SC 3.3.8a
selected remediation D; ED-SC 3.3.8b confirmed seed 456 rescue;
ED-SC 3.3.10 closes the arc."**

**`theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` §4.1**
— replace the current "coordinate validity ξ ≲ 1.96 lu" prose
with the crisper formulation:

> Coordinate validity: the canonical hinge `L_ray/ξ = 1.08`
> applies to realisations with `r_diag(L_ray) = 1` (equivalently
> `ξ ≲ 1.964 lu`). Realisations with `r_diag = 2` (e.g. seed 456
> in the canonical ensemble at ξ = 2.19 lu) are rescued by the
> shell-aware coordinate `L_eff = √2 · r_diag(L_ray)`; their S1
> and S2 under L_eff pass the collapse threshold per ED-SC
> 3.3.8b. The canonical operating point at `ξ_canonical = 1.7575
> lu` sits strictly inside `r_diag = 1`; its certification is
> unchanged.

**`memory/project_ed_sc_3_arc.md`** — append a 3.3.10 entry to
the thirteenth-pass consolidation section; update the open-
threads block to remove "ED-SC 3.3.8a pending" (now closed) and
promote ED-SC 3.4 + GR-SC 1.0+ to the top of the queue.

**`memory/MEMORY.md`** — update the `project_ed_sc_3_arc`
one-liner to reflect arc closure: *"ED-SC 3.x fully consolidated
through ED-SC 3.3.10 arc closure; canonical invariance domain
is `r_diag = 1` (ξ ≲ 1.96 lu); shell-aware coordinate rescues
Class-2 realisations; ED-SC 3.4 + GR-SC 1.0+ unblocked."*

**`docs/ED-Orientation.md`** — add a top-of-stack fourteenth-pass
bullet recording the arc closure and listing the authoritative
memos now covering ED-SC 3.3.x.

**`docs/ED_Accomplishments.md`** — append an ED-SC 3.3.10 arc-
closure entry after the thirteenth-pass entry.

These updates are **flagged, not applied**. A dedicated
consolidation pass (as in the twelfth-pass and thirteenth-pass
closures) should bundle them.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** declares the ED-SC 3.3.x
  sub-arc closed.
  - Integrates the outcomes of ED-SC 3.3.8 (diagnosis),
    3.3.8a (coordinate selection → verdict D), 3.3.8b (shell-
    aware re-test; seed 456 rescued; Class-1 starvation noted
    honestly), and 3.3.9 (ensemble-vs-realisation
    qualification).
  - States the final four-clause invariance statement (a) S1
    per-realisation, (b) S2 ensemble-only, (c) shell-aware
    coordinate for r_diag = 2, (d) r_diag ≥ 3 out-of-scope.
  - Declares the canonical invariance domain `r_diag(L_ray) = 1`
    (equivalently `ξ ≲ 1.964 lu`); canonical operating point at
    `ξ_canonical = 1.7575 lu` is strictly interior.
  - Enumerates operational consequences for ED-SC 3.4 (S2 is
    ensemble-only, r_diag window inherited) and GR-SC 1.0+
    (S1-derived inherit per-realisation certainty; S2-derived
    carry ±25 % per-realisation spread).
  - Lists recommended forward-pointer patches to ED-SC 3.0
    rev. 3, ED-SC 3.1 rev. 3, project memory, and the living
    orientation + accomplishments docs. These are **flagged,
    not applied**; a subsequent consolidation pass should bundle
    them.
  - No new execution. No drivers modified. No simulator constants
    mutated.
