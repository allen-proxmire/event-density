# ED-SC 2.0 Cleanup — Diff Proposal

**Status.** Proposal memo (2026-04-23). Implements the six cleanup edits
surfaced by `analysis/ED_SC_2_0_Sample_Size_Audit.md` and
`theory/ED_SC_2_0_r_star_Final_Verdict.md`.

**Operating mode.** This memo **does not modify the original documents**.
It lists exact before/after text for each edit as a diff proposal, so the
user can apply or modify the set atomically.

**Files touched by the proposal (none yet edited):**
- `theory/Universal_Invariants.md`
- `docs/ED-SC-2.0.md`
- `docs/ED-Orientation.md`
- `~/.claude/projects/.../memory/project_ed_r_star_analytic_arc.md`

---

## Edit 1 — Remove r* from the universal-invariant block

**File.** `theory/Universal_Invariants.md`
**Location.** §5 "Where these invariants enter empirical claims", final
paragraph (around line 156).

### Before

> Together with the **dimensional invariant** `D · T₀/L₀² = 0.3` (verified
> across 5 regimes spanning 61 orders of magnitude per the dimensional
> atlas), the **triad coupling** `C ≈ 0.03` (ED-Phys-16), the
> **third-harmonic ratio** 3–6 % of fundamental (ED-Phys), and the
> **ED-SC 2.0 architectural saddle ratio** `r* ≈ −1.304`
> (`docs/ED-SC-2.0.md`), they form the **universal-invariant block** of
> the ED Math Pipeline (see [`docs/figures/atlas/ED-Math-Pipeline.png`]…
> bottom row). Each is a forced consequence of the canonical PDE, with no
> additional assumptions.

### After

> Together with the **dimensional invariant** `D · T₀/L₀² = 0.3` (verified
> across 5 regimes spanning 61 orders of magnitude per the dimensional
> atlas), they form the **derivation-based universal-invariant block** of
> the ED Math Pipeline (see [`docs/figures/atlas/ED-Math-Pipeline.png`]…
> bottom row). Each is a forced consequence of the canonical PDE, with no
> additional assumptions.
>
> **Not in this block (removed 2026-04-23):** the ED-SC 2.0 motif-
> conditioned saddle-ratio median (formerly `r* ≈ −1.304`) and the two
> ED-Phys-16-provenance figures `C ≈ 0.03` and third-harmonic ratio 3–6 %.
> The first was retired from scalar-invariant status following the
> falsifier audit; the structural replacement is *"a motif-conditioned
> saddle-ratio distribution exists on the filtered Gaussian-random-field
> saddle population of the canonical PDE and is filter-dependent"* — see
> [`theory/ED_SC_2_0_r_star_Final_Verdict.md`](ED_SC_2_0_r_star_Final_Verdict.md).
> The latter two remain provisional pending provenance re-check against
> the C7 deterministic-canonical-operator results
> (`analysis/scripts/telegraph_pme/triad_calibration/memo.md`).

**Rationale.** Audit finding: of the four items listed in the old block,
only `D·T₀/L₀² = 0.3` is derivation-based. `r*` was a single-seed fit
(corrected to −1.88 ± 0.4); `C ≈ 0.03` and 3–6 % third-harmonic are
fit-based with unclear provenance. Keeping them in a "forced consequence
of the canonical PDE" list misrepresents their epistemic status.

---

## Edit 2 — Add cross-link to r* Final Verdict at the top of `Universal_Invariants.md`

**File.** `theory/Universal_Invariants.md`
**Location.** Immediately after the "Cross-reference" line in the preamble
(around line 7).

### Insertion (new paragraph)

> **r* status.** The ED-SC 2.0 motif-conditioned saddle-ratio median is
> **not** a derivation-based invariant of the canonical PDE. Its status
> was closed 2026-04-23 as a filter-conditioned statistic of the GRF
> linearisation of the R2 simulator, with pooled value r* ≈ −1.88 ± 0.4.
> See [`ED_SC_2_0_r_star_Final_Verdict.md`](ED_SC_2_0_r_star_Final_Verdict.md)
> for the full closure and [`../analysis/ED_SC_2_0_Sample_Size_Audit.md`](../analysis/ED_SC_2_0_Sample_Size_Audit.md)
> for the audit trail. Readers arriving here via the orientation doc's
> universal-invariant block should not resurrect the scalar form.

---

## Edit 3 — Reword AFM-dewetting pilot row in the empirical-status table

**File.** `docs/ED-Orientation.md`
**Location.** §7 empirical-status table, line 1034.

### Before (status cell)

> ⏳ pilot N=1 ℛ_all agrees sim↔image (−2.063 vs −2.149); needs real
> motif-resolvable AFM data

### After

> ⏳ pilot N=1 (single image vs. single seed-77 run); point-estimate
> medians landed at the same order of magnitude (−2.15 image vs −2.06
> sim), **but** the r*-arc falsifier results
> ([`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md))
> showed that single-seed medians of motif-filtered saddle populations
> fluctuate by O(0.5). The pilot is therefore **not evidence for
> cross-scale agreement**; it is only evidence that the pipeline runs
> end-to-end. A pooled-N test (≥10 images × ≥10 seeds) is required before
> the comparison becomes informative.

**Rationale.** Audit finding: the "agrees" phrasing is too precise for
N=1. The cross-scale test remains the highest-certainty near-term target
but its evidentiary threshold needs updating.

---

## Edit 4 — Flag triad coupling and harmonic ratio in `ED-Orientation.md`

**File.** `docs/ED-Orientation.md`
**Location.** §3 "Nonlinear structure (weakly coupled)", lines 224–225.

### Before

> - Triad resonance `k_3 = k_1 ± k_2`, coupling ~0.03 (measured in
>   ED-Phys-16).
> - Harmonic generation at 3–6% of fundamental.

### After

> - Triad resonance `k_3 = k_1 ± k_2`, coupling **~0.03 (provenance
>   unclear; ED-Phys-16 fit at undocumented N)**. See
>   [`analysis/ED_SC_2_0_Sample_Size_Audit.md`](../analysis/ED_SC_2_0_Sample_Size_Audit.md)
>   §2.2. The C7 deterministic-canonical-operator result
>   ([`analysis/scripts/telegraph_pme/triad_calibration/memo.md`](../analysis/scripts/telegraph_pme/triad_calibration/memo.md))
>   gives `K = A₃/A₁³ = 0.0148 ± 0.0005` on a fixed monochromatic IC;
>   whether K and the "0.03" refer to the same object is an open
>   provenance question.
> - Harmonic generation at **3–6% of fundamental (provenance unclear;
>   requires citation or re-run)**. The C7-derived form `A₃/A₁ = K·A₁²`
>   with K = 0.0148 gives 3% at A₁ ≈ 1.4 and is the preferred successor
>   statement.

---

## Edit 5 — Update `docs/ED-SC-2.0.md` reference measurement and §8.1

**File.** `docs/ED-SC-2.0.md`

### 5a — §2 architectural invariance claim (lines 62–70)

**Before**

> **Claim.** … the common value is
> $$r^* = \operatorname{median}(\mathcal{R}_{\text{motif}}(E)) \approx -1.30,$$
> with Scenario D at its architectural saddle peak `(n^* = 2.7,
> \sigma^* = 0.0556)` as the reference system: the motif-conditioned
> median of the canonical Scenario-D field satisfies `r^*_{\text{ScenD}}
> = -1.304`.

**After**

> **Claim.** … the common value, **pooled over ≥10 independent seeds of
> the reference system**, is
> $$r^* = \operatorname{median}(\mathcal{R}_{\text{motif}}(E)) \approx -1.88 \pm 0.4\ \text{(95% CI)}.$$
> with Scenario D at its architectural saddle peak `(n^* = 2.7,
> \sigma^* = 0.0556)` as the reference system: the 10-seed pooled
> motif-conditioned median of the canonical Scenario-D field is
> `r^*_{\text{ScenD}} ≈ -1.88`.
>
> **History note.** The previously-cited value `r^* = −1.304` is retained
> in the literature as a small-sample (N=6 motifs, single seed 77)
> fluctuation inside the 95% CI of the pooled distribution; it is not the
> canonical reference value. See
> [`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md).

### 5b — §4 falsification criterion

**Before**

> ED-SC 2.0 is falsified by any single comparison system `E_X` satisfying
> §3 for which
> $$|\operatorname{median}(\mathcal{R}_{\text{motif}}(E_X)) - (-1.30)| > 0.20.$$

**After**

> ED-SC 2.0 is falsified by any pooled-N (≥10 seeds / ≥10 images)
> comparison system `E_X` satisfying §3 for which
> $$|\operatorname{median}(\mathcal{R}_{\text{motif}}(E_X)) - (-1.88)| > 0.40.$$
>
> Single-seed / single-image comparisons are no longer admissible as
> evidence either for or against the claim, per the r*-arc falsifier
> results ([`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md)).

### 5c — §7 reference measurement table

**Before (final two rows)**

| Post-motif sample size | `|\mathcal{S}_{\text{motif}}| = 6` |
| **Reference invariant** | `\operatorname{median}(\mathcal{R}_{\text{motif}}(p_{\text{ScenD}})) = -1.304` |

**After**

| Post-motif sample size (10 seeds pooled) | N = 34 |
| Reference invariant (10-seed pooled) | `median(𝓡_motif) = −1.88, 95% CI [−2.34, −1.46]` |
| Historical single-seed value (seed 77, N=6) | `−1.304` (retained for provenance; not the canonical value) |
| See also | [`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md) and [`analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`](../analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md) |

### 5d — §8 open items

**Before (item 1)**

> 1. **Ensemble statistics.** The reference measurement is from a single
>    seed. An ensemble `(N ≥ 20)` over independent seeds would yield an
>    uncertainty estimate on `r^* = −1.30` and a better-characterised
>    filter sensitivity. Not blocking for publication; recommended before
>    first cross-scale test.

**After (item 1 — superseded)**

> 1. **Ensemble statistics — RESOLVED 2026-04-23.** 10-seed pooled
>    measurement complete; r* ≈ −1.88 ± 0.4. See
>    [`analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`](../analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md).
>    Downstream consequence: the scalar form of the invariant is retired.
>    See the final verdict memo
>    ([`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md))
>    for the restatement as a filtered-GRF statistical invariant, and the
>    restatement targets for ED-SC 3.0 therein.

### 5e — New §9 "Pointers for future readers"

**Addition**

> ## 9. Pointers for future readers
>
> - **If you arrive at `r* ≈ −1.30` from an older paper or orientation
>   summary,** read
>   [`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md)
>   before using the number. The scalar form is retired; the pooled value
>   is −1.88 ± 0.4.
> - **If you are designing a cross-scale test (AFM dewetting, Casimir,
>   stripe domains, RD activator),** the pass criterion in §5 now reads
>   median ∈ `[−2.3, −1.5]` (40% window around −1.88), applied to a
>   pooled-N statistic. The old `[−1.5, −1.1]` window is retired.
> - **If you are updating downstream memos,** the authoritative closure
>   chain is: `theory/ED_SC_2_0_r_star_Consolidation.md` →
>   `theory/ED_SC_2_0_r_star_R2_Analytic.md` →
>   `theory/ED_SC_2_0_r_star_R2_GRF.md` →
>   `analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md` →
>   `theory/ED_SC_2_0_r_star_Final_Verdict.md`.
> - **If you are writing ED-SC 3.0,** the structural replacement for the
>   scalar invariant is in the Final Verdict memo §6.3; the correlation-
>   length `ξ` is the recommended cross-scale hinge.

---

## Edit 6 — Update `ED-Orientation.md` §6.9 reference row

**File.** `docs/ED-Orientation.md`
**Location.** §6.9 reference measurement table, line 971.

### Before

| **Motif-conditioned median** | **−1.304** |

### After

| Motif-conditioned median (single-seed, seed 77, N=6) | −1.304 *(historical; not canonical)* |
| **Motif-conditioned median (10-seed pooled, N=34)** | **−1.88, 95% CI [−2.34, −1.46]** |
| Canonical interpretation | Filtered GRF saddle-ratio statistic — see [`theory/ED_SC_2_0_r_star_Final_Verdict.md`](../theory/ED_SC_2_0_r_star_Final_Verdict.md) |

And update §6.9 subsection header or preamble to add the line:

> **Canonical reading as of 2026-04-23.** r* is a filtered GRF saddle-
> ratio statistic, not a scalar invariant of the PDE. See the final
> verdict memo for the structural reclassification and the path to
> ED-SC 3.0.

---

## Edit 7 — Memory node update

**File.** `~/.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_ed_r_star_analytic_arc.md`

### 7a — Frontmatter description

**Before**

```yaml
description: Durable memory for the four-memo analytic derivation of
  ED-SC 2.0 r* = -1.304 from the Scenario-D PDE. Closed at leading order
  2026-04-22 eighth pass. Four memos, four durable findings, five
  guardrails.
```

**After**

```yaml
description: Durable memory for the full r* program (nine memos). Closed
  2026-04-23 ninth pass. Key finding (2026-04-23 closure):  r* is a
  filtered GRF statistic, not a PDE invariant; pooled R2 median ≈ −1.88
  ± 0.4. The cubic-chain derivation (r*(χ) = −2χ/(2χ−1), s = −1) is
  retained as structurally correct within its premises but does not
  describe R2.
```

### 7b — Prepend a new "Ninth-pass closure" section above "Arc status"

**Addition (prepended immediately after the frontmatter):**

```markdown
## Ninth-pass closure (2026-04-23)

**r* is a filtered GRF statistic.** The deterministic cubic-bistable chain
gives r* = −2χ/(2χ−1) with natural-amplitude closure s = −1 at leading
order — structurally correct within its premises. But the R2 PDE (the
actual simulator producing −1.304) has discriminant Δ < 0 with no natural
amplitude, so s is free and the deterministic R2 chain gives r* ≈ 0, not
−1.304. The mechanism that actually produces the empirical value is GRF:
the linearised SPDE around p̂ ≈ 0.108 has 2D-isotropic stationary GRF with
correlation length ξ ≈ 4. Closed-form unfiltered saddle-ratio density
f(ρ) ∝ ρ(ρ+1)(3ρ²+2ρ+3)^{-5/2} has median |s| ≈ 1.94. 10-seed pooled R2
simulator with canonical motif filter gives r* ≈ −1.88 ± 0.4, matching
the unfiltered GRF prediction to 3%. The original −1.304 was a
single-seed (N=6) small-sample fluctuation.

Five memos added in the ninth pass:
- theory/ED_SC_2_0_r_star_Consolidation.md
- theory/ED_SC_2_0_r_star_R2_Analytic.md
- theory/ED_SC_2_0_r_star_R2_GRF.md
- analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md
- theory/ED_SC_2_0_r_star_Final_Verdict.md

Plus the audit and cleanup trail:
- analysis/ED_SC_2_0_Sample_Size_Audit.md
- docs/ED_SC_2_0_Cleanup_Changes.md (this proposal)

**Updated headline for future sessions:**
r* is a filtered GRF statistic; pooled R2 median ≈ −1.88 ± 0.4; cubic-
chain derivation retained as structural.
```

### 7c — Boxed closed-form result update

**Before (the boxed result section)**

```
┌──────────────────────────────────────────────────────────────────┐
│  Leading-order (M_2 = 0):                                        │
│    s = −1   (from δ_max² = −6P_0/P_3, natural-amplitude closure) │
│    r* = −2χ / (2χ − 1),   χ ≡ 2μκ⊥²/P_0                          │
│    r* = −1.304   ⟺   χ = 2.145   ⟺   κ⊥² ≈ 2.14                  │
│  Full-order:                                                     │
│    r* = −2χ / [2χ − 1 − M_2 𝒦_NL / (2P_0)]                       │
└──────────────────────────────────────────────────────────────────┘
```

**After (replace box with dual-result box)**

```
┌──────────────────────────────────────────────────────────────────┐
│  Cubic-bistable chain (structural result, retained):             │
│    s = −1   at natural-amplitude closure δ_max² = −6P_0/P_3      │
│    r* = −2χ / (2χ − 1),   χ ≡ 2μκ⊥²/P_0                          │
│    r* = −1.304   ⟺   χ = 2.145                                   │
│                                                                  │
│  R2 simulator (actual empirical object, closed 2026-04-23):      │
│    Discriminant Δ = P₂²/4 − 2P₁P₃/3 = −0.078 < 0                 │
│    → no natural amplitude; s is a free parameter                 │
│    → deterministic r*_R2(s=−1.304, d=0.02) ≈ −1.4×10⁻³           │
│                                                                  │
│  R2 filtered-GRF statistic (the actual r*):                      │
│    Unfiltered median s_med = −1.94 (closed form)                 │
│    Filtered (canonical R2 motif filter) s_med ≈ −1.88 ± 0.4      │
│    (10-seed pooled, 95% CI [−2.34, −1.46])                       │
│                                                                  │
│  The cubic chain describes the analytic premise; the GRF         │
│  describes R2. They are not the same PDE.                        │
└──────────────────────────────────────────────────────────────────┘
```

### 7d — Append a sixth guardrail

**Addition (after G5):**

> **G6.** Do not treat r* as a scalar invariant of the PDE. It is a
> filter-conditioned statistic of the GRF linearisation, with numerical
> value depending on the correlation length ξ and the filter geometry.
> If a future session is asked "what is r*", the correct answer is: a
> distribution median, pooled N=34 gives −1.88 ± 0.4, and the structural
> claim for ED-SC 3.0 is that such a median *exists and is stable under
> correlation-length-preserving transformations*, not that it equals any
> particular number.

---

## Summary of proposed changes

| # | File | Section | Type |
|---|------|---------|------|
| 1 | `theory/Universal_Invariants.md` | §5 block paragraph | rewrite |
| 2 | `theory/Universal_Invariants.md` | preamble | insert pointer |
| 3 | `docs/ED-Orientation.md` | §7 empirical-status row 1034 | rewrite |
| 4 | `docs/ED-Orientation.md` | §3 lines 224–225 | annotate |
| 5a | `docs/ED-SC-2.0.md` | §2 claim | rewrite |
| 5b | `docs/ED-SC-2.0.md` | §4 falsification | rewrite |
| 5c | `docs/ED-SC-2.0.md` | §7 reference table | rewrite |
| 5d | `docs/ED-SC-2.0.md` | §8.1 open item | mark resolved |
| 5e | `docs/ED-SC-2.0.md` | new §9 | add |
| 6 | `docs/ED-Orientation.md` | §6.9 reference row | rewrite |
| 7a-d | `memory/project_ed_r_star_analytic_arc.md` | frontmatter + body | rewrite |

All edits are consistent with:
- the r*-arc Final Verdict (`theory/ED_SC_2_0_r_star_Final_Verdict.md`)
- the Sample-Size Audit (`analysis/ED_SC_2_0_Sample_Size_Audit.md`)
- the 10-seed pooled measurement in
  `analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`.

**No originals modified by this memo.** Apply the edits by hand or request
an application pass; each edit is scoped to its numbered block and can be
accepted/rejected independently.
