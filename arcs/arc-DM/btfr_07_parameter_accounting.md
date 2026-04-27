# BTFR.07 — Parameter Accounting and Structural Options

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, seventh memo
**Status:** Honest re-evaluation of the parameter accounting following BTFR.06's implementation work. The "zero new parameters" claim of BTFR.05 is corrected. Three structural options are compared (anisotropy + interpolation, derived anisotropy mechanism, nonlinear ED variant). **Verdict: there is no parameter-free BTFR-compatible extension of canonical ED. Each option introduces at least one structural commitment — either a free parameter, a new mechanism, or a major operator change. The cheapest option (A) is structurally MOND-equivalent and adds nothing over postulating MOND directly; the most ambitious (C) is the only one that could produce a genuinely ED-distinctive BTFR derivation, but requires non-trivial derivation work.**
**Predecessors:** BTFR.02–06.
**Successor:** BTFR.08 (sketch nonlinear ED variant) if Option C is pursued; otherwise the BTFR sub-arc closes here.

---

## 1. Inventory of ED constants

Before discussing extensions, fix the canonical-ED constants in their current standing:

| Constant | Role | Origin | Free? |
|---|---|---|---|
| **D_T** | diffusion coefficient (penalty channel) | cluster-calibrated from merger-lag observations | No (calibrated) |
| **λ** | screening rate | cosmological time-scale; t_H ≈ 13.8 Gyr | No (calibrated) |
| **L = √(D_T/λ)** | screening length | derived from D_T, λ | No (derived) |
| **κ_act** | activity coupling | dimensional anchor in galactic-natural units | No (universality-tested at σ/mean ≈ 2.1%, provisional) |
| **α** (shear vs vorticity weight) | activity index composition | DM.1 §2 | Effectively 1 (per universality result) |
| **a₀ ≡ λ² · D_T** | candidate embedded acceleration scale | dimensional combination | No (derived); but its *use* in the theory is a structural commitment |

These are the constants ED already has. Any "new parameter" introduced by the BTFR extension must be on top of these.

---

## 2. What BTFR.06 actually showed

Two specific findings invalidate BTFR.05's parameter-free claim:

### 2.1 Anisotropy: the disc-thickness ratio is insufficient

For the in-plane Green's function `T(R, 0)` to behave as a windowed log over galactic scales (1–50 kpc):

> L_z = √(D_z/λ) ≲ 1 kpc    ⟹    D_z/D_R ≲ 10⁻⁶

with D_R = D_T cluster-calibrated and λ unchanged. The disc-thickness ratio (h_disc/R_d)² ~ 10⁻² is **four orders of magnitude too large** to deliver this. The anisotropy must therefore come from some other mechanism (or be postulated as a new free parameter).

### 2.2 The dimensional a₀ does not automatically weight the coupling

a₀ = λ²·D_T has the right dimensions, but to satisfy C2 (M_eff ∝ √M_b) the source coupling must carry a specific functional weighting `ν(a_baryon/a₀)`. The naive `√(a/a₀)` overcorrects (predicts slope 6); the correct deep-regime form requires `ν(x) → √(1/x)` as `x → 0`, which is essentially MOND's interpolation function. The functional form of ν is a new structural commitment that is *not* dictated by ED's existing constants.

### 2.3 Honest accounting

> **The combined Route I + II-A extension introduces at minimum one new free parameter (D_z, or equivalently the anisotropy ratio) plus one new functional-form commitment (ν).** The sole "free" component is a₀ itself — but a₀ is only useful in the theory because of the additional ν specification, so its derived status doesn't reduce the total number of structural commitments.

This contradicts BTFR.05's "zero new parameters" claim. BTFR.05 should be read as *structurally optimistic*; BTFR.07 corrects to the honest count.

---

## 3. Three structural options

Three mutually-exclusive paths forward at the BTFR-extension level. Each is described in its minimal form, then evaluated.

### 3.1 Option A — Anisotropic ED + MOND-style interpolation

**Statement.** Adopt the BTFR.06 form directly:

> D_R · (1/R) ∂_R(R ∂_R T) + D_z · ∂_z² T − λ T = − ν(a_baryon/a₀) · κ_act · A(R, z),

with D_z postulated to satisfy D_z/D_R ≲ 10⁻⁶ and ν(x) chosen to match MOND's interpolation function (e.g. ν(x) = (1 + 1/x)^{1/2} or McGaugh's `μ(x) = 1 − exp(−√x)`).

**Parameter count.**
- 1 new free parameter: D_z (or the ratio D_z/D_R).
- 1 new functional commitment: choice of ν(x).

**Theoretical naturalness.** Low. The anisotropy is postulated rather than derived. The interpolation function is imported from MOND. ED's distinctive content (activity source, screening length, cluster connection) is preserved but the *galactic* dynamics it produces are essentially MOND's, with extra screening at very large radii.

**Empirical viability.** High. By construction reproduces MOND's BTFR derivation, and inherits MOND's well-tested empirical successes in the deep-acceleration regime. The activity source distinguishes from MOND in transition regions and at cluster scales.

**Compatibility with existing arcs.**
- R, M, N, Q, B: Compatible. The modification is galactic-regime-localized.
- DM-arc cluster predictions: Preserved (anisotropy and ν deactivate at cluster scales).
- GR-arc, GR-SC, RG: Unaffected.

**Derived or fitted?** **Fitted at the structural level.** The slope-4 BTFR follows from the deep-regime asymptotic of ν, but ν itself is chosen to produce that asymptotic. There is no independent ED-internal reason for ν to take this form. This is the same epistemic status MOND holds: a chosen interpolation function that produces the right asymptotic.

**Bottom line.** BTFR works. But this option produces no theoretical advance over MOND — it only confirms that ED can host MOND-like structure if you postulate it. No reason to prefer this ED-extended-with-MOND-machinery over MOND itself.

### 3.2 Option B — Derive the anisotropy from a structural mechanism

**Statement.** Replace the postulated D_z with a derived quantity from a structural ED principle — typically a coupling of D_T to local matter density or local geometry. Candidate mechanism: matter-coupled diffusion,

> D_T(x) = D_0 + D_1 · ρ_b(x),

so D is large where baryonic matter is dense (in the disc plane) and small in vacuum (perpendicular to the disc). The effective `D_z` (averaged perpendicular to a thin disc) is then suppressed relative to `D_R` (averaged in-plane) by a factor that depends on the disc surface density and the column profile.

**Parameter count.**
- New constant D_0 (vacuum diffusion): 1 parameter.
- New constant D_1 (matter-coupling strength): 1 parameter.
- D_z is then derived (not postulated) from these.
- Cluster-calibrated D_T fixes one combination: `D_T_cluster = D_0 + D_1 · ρ_cluster`. This is one constraint on two parameters; net count is **1 new free parameter** (the ratio D_1/D_0, or equivalently any single independent observable that fixes one of them).
- ν(x) functional commitment: still needed for C2; **+1 functional commitment**.

So Option B has the same total structural commitment as Option A (1 free parameter + 1 functional choice), but the physical interpretation is different: instead of postulating disc-induced anisotropy, the anisotropy emerges from a more fundamental (and potentially testable) coupling.

**Theoretical naturalness.** Medium. Matter-coupled diffusion is a physically plausible mechanism (analogous to how electrical conductivity in plasmas depends on local density). It connects ED's diffusion structure to its source-density structure in a non-arbitrary way. But specifying D_1's value still requires fitting to one independent observation.

**Empirical viability.** Plausible but unverified. The matter-coupled D would have implications throughout ED, not just in galactic discs:
- In Arc N (vacuum kernel work), D_T appears in the V1 finite-width vacuum kernel. If D depends on local matter, V1's structure becomes spatially varying. This may or may not break the V1 theorem; needs explicit checking.
- In GR-arc (V1 with Synge world function), the same concern applies.
- In cluster physics, intercluster diffusion would proceed at D_0 (vacuum value), not at D_T_cluster. Cluster predictions would need re-derivation.

**Compatibility with existing arcs.**
- R, M, Q, B: probably unaffected (no D_T dependence).
- N: at risk. Theorem N1 may need re-evaluation with spatially-varying D.
- DM-arc cluster predictions: at risk. Re-derivation needed.
- GR-arc: at risk.
- GR-SC: probably unaffected.

So Option B is **not** structurally local to the DM-arc — it propagates upstream into the vacuum-kernel and gravitational-sector arcs that have already been closed. A genuine structural derivation of anisotropy via matter-coupled D is a multi-arc revision, not a one-memo extension.

**Derived or fitted?** Anisotropy is *derived* from the matter-coupled D, but D_1 is fitted to one observation (BTFR or another galactic relation). Better than Option A in that the anisotropy isn't postulated, but still requires one calibration. The ν functional is still chosen.

**Bottom line.** Option B has marginally better structural naturalness than Option A but at substantial cost: it requires re-evaluating the closed N and GR arcs. The payoff (parsimony) is small; the cost (re-derivation) is large. Probably not worth pursuing unless an *independent* prediction from matter-coupled D motivates it (e.g., an observable signature that distinguishes matter-coupled D from constant D in cluster or vacuum-kernel contexts).

### 3.3 Option C — Nonlinear ED variant

**Statement.** Drop the linear-PDE constraint. Replace the canonical screened-Poisson with a nonlinear operator, structurally analogous to MOND but sourced by activity:

> ∇ · [μ(|∇T| / T₀) · D_T · ∇T] − λ T = − κ_act · A(R, z),

where μ(x) is a nonlinear interpolation function with μ → 1 at large |∇T|/T₀ (recovering canonical ED) and μ → x at small |∇T|/T₀ (the deep-regime behavior). T₀ is a characteristic gradient scale of the field.

In the deep-regime limit (low gradients, large radii), the equation reduces to a MOND-like form sourced by the activity index. By the standard MOND derivation, this gives a logarithmic asymptotic `T(R) → const · ln R` and `v_T² ∝ √(activity-integrated charge)`. With the activity-source being intrinsically related to baryon kinematics, the derivation chain to BTFR can in principle close cleanly without postulating ν or D_z separately.

**Parameter count.**
- T₀: 1 new fundamental scale. Possibly derivable from existing constants — needs to be checked.
- μ(x) functional form: 1 new structural commitment.
- D_z, ν(a/a₀): not needed (the nonlinearity does double duty).

So **1 new functional commitment**, with potentially 0 new free parameters if T₀ derives from existing constants, or 1 new constant if it does not.

This is parametrically equivalent to MOND (1 functional + 1 constant a₀) but with the source structurally different (activity vs mass).

**Theoretical naturalness.** High. The nonlinearity does the same structural work as MOND's: simultaneously provides the log far-field (C1) and the √M_b coupling (C2). No need for separate anisotropy or interpolation. The single nonlinear operator is the simplest structural object that produces BTFR.

**Empirical viability.** Likely good in galactic regime (inherits MOND-like structure). Differentiates from MOND at:
- Cluster scales: the screening term λT cuts off large-R correlations at L ≈ Mpc, providing the cluster-scale cutoff that MOND requires an external-field-effect to mimic.
- Active vs quiet galaxies: the activity source (rather than mass source) predicts that dynamically-quiet galaxies have less T-charge and weaker rotation curves than dynamically-active ones at the same M_b. This is a *distinctive* prediction not present in MOND — and consistent with the ED-04.5 dwarf-comparison anchor.

**Compatibility with existing arcs.**
- R, M, N, Q, B: needs explicit checking. The vacuum-kernel theorem N1 was derived for the linear screened-Poisson. A nonlinear PDE may not produce the same V1 finite-width vacuum kernel. This is a non-trivial structural question.
- DM-arc canonical PDE (DM.0–DM.6): the entire derivation chain that argued for the linear screened-Poisson would need re-examination.
- GR-arc: V1 with Synge world function is built on linear V1 — would need re-examination if N1 changes.

So Option C has the highest *theoretical* payoff but the largest *structural* cost: it potentially overturns Theorem N1, the V1 vacuum kernel result, and downstream GR-arc theorems. These are FORCED results in the canonical theory; replacing the linear PDE with a nonlinear one requires demonstrating that an analogous V1 theorem holds (or doesn't) for the nonlinear case.

**Derived or fitted?** BTFR is **derived** in Option C — the asymptotic v_T⁴ ∝ M_b emerges from the nonlinear operator structure, not from a separately-tuned ν function. The fit content is reduced to the choice of μ(x) and the value of T₀. This is structurally cleaner than Options A and B.

**Bottom line.** Option C is the only one that produces a genuinely ED-distinctive BTFR derivation (slope 4 with no fitting at the asymptotic level). It is also the only one that could plausibly differentiate from MOND empirically (via activity-source differentiation). But it is the most expensive option in terms of upstream consistency: it potentially invalidates closed theorems in arcs N and GR.

---

## 4. Decision table

| Option | New parameters | New functional choices | Structural elegance | BTFR viability | Compatibility cost | Notes |
|---|---|---|---|---|---|---|
| **A** — anisotropic + ν | 1 (D_z) | 1 (ν(a/a₀)) | Low (MOND-equivalent) | Yes, by construction | Low (galactic-regime-local) | No advance over postulating MOND |
| **B** — derived anisotropy | 1 (D_1) | 1 (ν(a/a₀)) | Medium | Plausible, unverified | Medium-high (re-evaluate Arc N, GR) | Marginal naturalness gain at substantial cost |
| **C** — nonlinear ED | 0–1 (T₀; possibly derived) | 1 (μ(x)) | High (single mechanism does both jobs) | High; derives slope 4 cleanly | High (potentially invalidates Theorem N1, V1) | Only option with genuine ED-distinctive BTFR; biggest theoretical risk |

The bare parameter counts are similar across options. The structural costs are not. **Option A is structurally easiest but conceptually weakest. Option C is conceptually strongest but structurally most disruptive.**

---

## 5. Recommended path forward

Three honest paths the DM-arc could take:

### 5.1 Accept the FAIL verdict, write DM.5, close the arc

The BTFR sub-arc has accomplished its purpose: it identified the structural reasons canonical ED cannot derive BTFR, and demonstrated that any extension that *does* derive BTFR requires either MOND-equivalent machinery or a substantive structural overhaul. The DM2 production-run FAIL is now interpretable: it is a structural failure, not a numerical artifact. DM.5 can be written honestly with this finding as the headline result, and the DM-arc can close with a refutation-and-explanation pairing.

This is the cleanest path. It does not commit to any extension. It preserves the structural integrity of arcs N, GR, and the canonical DM-arc.

### 5.2 Pursue Option C with explicit Arc-N/GR re-evaluation

If the user judges ED-distinctive BTFR derivation worth pursuing, Option C is the only path that produces a genuine theoretical advance. It requires:
- BTFR.08: Sketch the nonlinear ED variant explicitly. Write the modified PDE; identify candidate μ functional forms; check whether T₀ derives from D_T, λ, κ_act.
- Re-evaluation memo: examine whether Theorem N1 (V1 finite-width vacuum kernel) still holds (or has an analog) for the nonlinear PDE.
- Re-evaluation memo: similar for GR.5 (V1 with Synge world function).
- If both re-evaluations succeed (analogs of N1 and GR.5 hold), proceed to a numerical implementation. If either fails, the nonlinear variant is structurally incompatible with the established arcs.

This is a multi-week to multi-month commitment. The payoff, if it works, is large: a single ED structure that produces BTFR cleanly, distinguishes from MOND empirically (activity-source), and extends naturally to clusters via screening.

### 5.3 Defer the BTFR question; focus on other ED tests

A third path: accept that BTFR is a structural test ED currently fails, and pursue ED's other empirical predictions (merger-lag, weak-lensing, cluster outskirts, etc.) where its activity-source mechanism may have better predictions than mass-based alternatives. Return to BTFR after gathering more evidence about whether ED's activity-source mechanism has independent empirical support.

This is a strategic deferral, not a closure. The BTFR sub-arc closes with its current FAIL verdict; future evidence may justify revisiting.

---

## 6. Honest summary

> **There is no parameter-free BTFR-compatible extension of canonical ED.**
>
> - Option A (anisotropy + ν): adds 1 parameter + 1 functional choice; produces no advance over MOND.
> - Option B (derived anisotropy): same structural commitment as A, but at the cost of re-evaluating closed Arc-N and GR theorems.
> - Option C (nonlinear ED): potentially fewer parameters; produces ED-distinctive BTFR; but at the cost of substantial structural-arc re-evaluation.
>
> The cheapest honest summary of canonical ED + BTFR: **canonical ED does not derive BTFR, and the available extensions are either MOND-equivalent (no theoretical advance) or structurally expensive (requires re-opening closed arcs).**

The BTFR result is therefore a real refutation of canonical ED's gravitational-sector predictions, not a numerical artifact. DM.5 should be written with this as the central scientific finding. Whether to attempt Option C is a separate strategic decision about the DM-arc's research direction.

---

## 7. Recommended Next Steps

Three concrete next steps, ranked by expected value-to-cost ratio:

1. **Close the BTFR sub-arc and write DM.5.** Use the BTFR.02–07 chain as the structural-explanation context for the production-run FAIL verdict. Frame the universality success (σ/mean ≈ 2.1%) and the BTFR failure as the two empirical findings. This is the lowest-cost path and produces a publishable verdict memo. No new ED commitments required.

2. **Sketch Option C in a single exploratory memo (BTFR.08).** A bounded-scope exercise: write the proposed nonlinear PDE; identify whether T₀ derives from existing constants; estimate whether the deep-regime asymptotic gives slope-4 BTFR. *Do not* re-derive Arc N or GR theorems in this memo. Output: a go/no-go decision on whether Option C deserves the larger investment.

3. **Commit to a full Option-C arc (BTFR.08 onward).** Only if the BTFR.08 sketch suggests Option C is structurally viable. Includes Arc-N/GR re-evaluation memos, nonlinear-PDE solver implementation, and re-running DM2 with the nonlinear variant. Multi-month commitment.

The default recommendation, absent a strong push to pursue Option C: **do step 1**, close the BTFR sub-arc cleanly, write DM.5, and revisit the BTFR question only if independent empirical evidence motivates it.

Status: complete.
