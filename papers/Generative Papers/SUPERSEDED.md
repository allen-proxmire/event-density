# ⚠ SUPERSEDED — this folder is a frozen fork, not the live corpus

**Frozen 2026-07-05.** Marker written 2026-09-04.

**The canonical generative papers live in `ED Generative/physics-papers/`** (sibling repository). Read them there. Nothing in this folder has tracked the canonical copies since the freeze date, and 31 of the files here now state things the canonical versions have corrected.

---

## What is actually in here

133 files, in three groups:

| Group | Count | Status |
|---|---|---|
| **Identical to canonical** | 71 | Harmless. No reason to read them here rather than there. |
| **Stale — diverged from canonical** | 31 | **The hazard.** Listed below. |
| **No canonical counterpart** | 29 | Mostly process docs and the deliberately-archived M-series. **Six are not** — see the exception. |

## The 31 stale files

Do not cite these. Their canonical versions have moved.

```
Paper_004_GleasonUniqueness      Paper_073_DCGT
Paper_007_HilbertSpace           Paper_086_SoftMatter_Synthesis
Paper_015_T17_GaugeFields        Paper_087_13Primitives
Paper_027_Newtons_G              Paper_088_PrimitiveAudit
Paper_028_CosmicDecoupling       Paper_089_V1Kernel
Paper_029_a0                     Paper_095_FormForced_ValueInherited
Paper_030_CombinationRule        Paper_096_CrossScaleInvariance
Paper_031_BTFR                   Paper_097_RG_0p6_Problem
Paper_037_a0_Invariance          Paper_098_EDQFT_Overview
Paper_038_CosmologicalImplications  Paper_100_FiveSector_ProgramOverview
Paper_039_HorizonDecoupling      Paper_101_FalsificationRegister
Paper_042_NoSingularity          Paper_SCBU_SubstrateCosmologyBoundary
Paper_043_AreaLaw                README
Paper_056_ClassA_Wall            paper_ED_Framework_13_Primitive_Generative_System
Paper_058_ClassC_Plateau
Paper_060_Mcrit_Unification
Paper_065_Monogamy
Paper_066_NoSignaling
```

**Two concrete examples of what that means**, both from a single day's corrections (2026-09-04):

- `Paper_029_a0.md` here presents `a₀ = cH₀/(2π)` as settled. **It is not.** The canonical version carries a DISPUTED flag on the `1/(2π)`: the azimuthal-Fourier normalization cancels in `Paper_028` §6.3 and `Paper_029` §5.1's own displayed algebra. The *scale* `a₀ ~ cH₀` stands and is now reached four independent ways; the *coefficient* is Postulated/disputed.
- `Paper_030_CombinationRule.md` here still displays the three-term profile `a = a_N + a₀ + √(a_N a₀)`. **That standalone `a₀` was removed at source** in the canonical version: `Σ₀` is a content normalization, no gradient is taken, and the profile is `a = a_N + √(a_N a₀)`. The old form is dominated by the constant term in the deep field, which contradicts `Paper_030`'s own §3.4 and `Paper_031`.

The canonical audit trail for both is `ED Generative/physics-papers/gravity/Gravity_TieredClaims_Ledger.md`.

## The exception — six papers that exist ONLY here

**These are not superseded, because there is nothing to supersede them.** They have no counterpart in the canonical corpus:

```
Paper_ED_SC_4_1_BH_CosmicDecoupling   <-- MIGRATED 2026-09-04
Paper_ED_SC_4_2_xi_canonical_H0_derivation   <-- MIGRATED 2026-09-04
Paper_ED_SC_4_3_MOND_SCBU
Paper_ED_SC_4_4_QCompute_SCBU   <-- MIGRATED 2026-09-04
Paper_ED_SC_4_5_SoftMatter_SCBU   <-- MIGRATED 2026-09-04
Paper_ED_SC_4_6_UnifiedCrossScale
```

**DECIDED 2026-09-04: they are NOT superseded — the relation runs the other way.** Canonical `Paper_SCBU` says *“The corpus is ready for ED-SC 4.x development”* and its falsifier **F4** — does a third or fourth canon-internal anchor (`r_H`, `ℳ_crit`, NS-Q operating point) fail to anchor to `R_H = c/H₀`? — calls itself *“the bridge to ED-SC 4.x”*. **SCBU is upstream; this series is the development it calls for**, and `SC_4_6` reports all six projections (`r_H`, `R_H`, `ξ_canonical`, `a₀`, `ℳ_crit`, `Q ≈ 3.5`) landing in a unified four-regime structure. **So F4's discharge lives here while F4 stands open in the canonical corpus.** These six should be **migrated, not retired.**

**Three conditions on migration** — they were written before the 2026-09-04 corrections and would otherwise reintroduce them:

1. **The `2π`.** All six carry it — 32 occurrences, 14 in `SC_4_3` alone — and none is flagged. The coefficient in `a₀ = cH₀/(2π)` is **Postulated/disputed**; the scale `a₀ ~ cH₀` is not.
2. **`ξ_canonical = 1.7575`.** Appears in five of the six. The measured value is **1.76 ± 0.30** (`σ = 0.303`, ten seeds) and is processing-dependent (smoothed variant `3.05 ± 0.53`). Five significant figures are unsupported.
3. **`SC_4_2` does not close.** Its own status line says so. It must migrate as a **banked negative** on deriving `ξ_canonical(H₀)`, not as a derivation.

*Also: they add only **2** postulates the corpus census does not already count — `P-BTFR-Slope-4` and `P-Deep-MOND-Limit`, both in the MOND papers (`SC_4_3`, `SC_4_6`). They are not a hidden assumption reservoir.*

**Not yet audited.** No claim-strength pass has been run on these six.

**One of them is load-bearing and was being missed.** `Paper_ED_SC_4_2` attempts the substrate derivation of `ξ_canonical(H₀)` and reports that it **does not close** — *"value-INHERITED status preserved; structural setup is FORM-FORCED M3"* — naming the missing piece as either a substrate-derived `ℓ_V5(H₀)` relation or a substrate-derived scaling law. It calls itself the highest-leverage paper in the series.

That is a **banked negative**, and the canonical `Paper_096` did not cite it until 2026-09-04. Anyone attacking "derive `ξ_canonical` from the substrate" without reading it would repeat a failed attempt. A pointer now exists in `Paper_096`.

## Correctly absent, not lost

The rest of the 29 need no action:

- **Process/planning docs** — `UPDATE_PLAN_after_M1`–`M4`, `CONSOLIDATION_SUMMARY`, `CONSOLIDATION_SUMMARY_v2`, `DEPENDENCY_GRAPH_ED`, `PHASE1_APPLICATION_SUMMARY`, `PRIMITIVE_LOAD_BEARING_AUDIT`, `REVISIONS_PHASE1_abstracts_claims_scope`. Historical records of how the corpus was built.
- **The archived M-series** — `paper_M0`–`M4`, `paper_M_omnibus_closure`, and `ARCHIVED_M_SERIES_NOTICE.md`. **Deliberately archived**: canonical `Paper_087` supersedes them. Their "four-band" and "forcing" language is *not* current ED and should not be quoted.
- **Theorem entries** `T19`, `T20`, `T21`.
- **`Paper_093_KernelArrow`** — a rename artifact; canonical is `Paper_093_KernelArrow_of_Time.md`.

## What is left to do

The SC-4.x question is **decided** (above): they are live, upstream-sanctioned, and should be migrated. What remains:

1. **Migrate the SC-4.x six** into `ED Generative/physics-papers/`, applying the three conditions above. This is the only task with demonstrated cost — `SC_4_2`'s banked negative was invisible to the canonical corpus until 2026-09-04, and `SC_4_6` answers a falsifier (`Paper_SCBU` F4) that still stands open there.
2. **Run a claim-strength pass** on the six once migrated. They have never had one, and they were written before the `2π` dispute and the `Σ₀` rewrite.
3. **Then dispose of the remaining 102** — delete, or archive with this marker retained. Once the six are out, nothing here is irreplaceable and the 31 stale files are pure contradiction surface.

Recorded as gravity ledger Staleness #51 (the fork check) and #52 (the SC-4.x decision).
