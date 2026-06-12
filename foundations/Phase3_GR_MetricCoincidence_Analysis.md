# Metric Coincidence: Does the Bandwidth Metric Realize the Postulated Acoustic Metric?

**Internal analysis memo — resolves §3A of the reconciliation memo. Not a publication paper.**
**Author:** Allen Proxmire · June 2026

**Question (path B).** Before any GR-I paper: do Phase-3's **bandwidth metric** `g_ij ~ b⁻¹` (P04) and the published arc's **acoustic metric** (Paper_033) describe the same spacetime geometry — in particular, do they agree on the *spatial* curvature that sets factor-of-2 vs half light bending? This memo answers as far as the corpus allows, and the answer reframes the whole "conflict."

---

## 1. The decisive fact: Paper_033's acoustic metric is *postulated*, not derived

Reading Paper_033's own load-bearing audit (§2.5) is clarifying. Its acoustic metric is **not a derived object**:

- `g^{αβ}` is introduced by **P-AcousticMetric** — labeled **P (postulate)**: "*substrate-graph kinematic-flow + cumulative-strain content produces a substrate-level metric*," with the explicit caveat "**Not derived from substrate primitives alone; substrate-level commitment.**"
- The Unruh acoustic-metric analogy is explicitly "**A→analogy, used for exposition only … illustrative, not a derivation.**"
- The scalar-tensor structure (`Φ` on `g`) is also **P** (P-Scalar-Tensor-Form), and the scalar `Φ` is a **"P-construction"** generalizing the flat-space potential (Round-8 relabel from D to P).
- The field equation is a **"P-construction matching standard scalar-tensor form."**

So Paper_033 **posits** an (unspecified-form) Lorentzian metric as a *background* and builds a MOND scalar-tensor theory on it. **It never gives the metric's explicit form, never pins the spatial part, and never computes light bending.** Its only metric-level constraint is the Newtonian limit (§3.5: `μ→1`, `∇²Φ = 4πGT`).

**Consequence:** there is **no "two derived metrics in conflict."** There is one *derived* metric (Phase-3's `g~b⁻¹`) and one *postulated, form-unspecified* metric (Paper_033's `g^{αβ}`). The right question is therefore not "do they conflict?" but "**can the derived bandwidth metric serve as the explicit realization of the postulated acoustic background?**"

## 2. Where they must agree — and do

Both are pinned at the Newtonian / high-acceleration limit, and they agree there:

- **Paper_033:** `μ→1 ⟹ ∇²Φ = 4πGT`, weak-field Newton (§3.5).
- **Phase-3:** `∇²b ~ ρ` (R9), `g_00 = −N² ~ −(1+2Φ)` with `b ~ 1+2Φ`.

Both give `g_00 = −(1+2Φ)`, `∇²Φ = 4πGρ`. Same Newtonian metric, same shared `G`/`ℓ_P` base (Paper_027/027.5). **At the level where Paper_033 actually constrains the metric, the bandwidth metric agrees.** No contradiction.

## 3. What Phase-3 *adds* where Paper_033 is silent

Phase-3 supplies exactly the content Paper_033 left open:

- **The spatial part.** `g_ij ~ b⁻¹ ~ (1−2Φ)δ_ij` — the spatial curvature equals the time potential (`g_00 g_rr ~ −1`, R8), i.e. the **Einstein** value, giving the **factor-of-2** light bending (R7/R8, simulated). Paper_033 never computed this; a *pure* scalar-tensor theory with a postulated background does not fix it (historically the failure mode that forced TeVeS to add a vector). **Phase-3 resolves an open question in Paper_033, favorably** (it lands on the GR value).
- **The lapse / preferred frame.** `N² ~ b` from the commitment-rate law (R8) carries the khronometric preferred-frame structure. So if `g~b⁻¹` *is* Paper_033's background, that background is **khronometric, not the implicitly-Lorentz-covariant scalar-tensor** Paper_033 assumed. Phase-3 thus *revises* Paper_033's Lorentz status — but since Paper_033 never specified the metric finely enough to assert covariance, this is a sharpening, not a contradiction.

So Phase-3's bandwidth metric is **compatible with, and a more explicit realization of, Paper_033's postulated acoustic background** — agreeing on the only thing Paper_033 fixed (Newton) and filling in the spatial + lapse structure Paper_033 left blank.

## 4. The two genuine residuals

This reframing leaves two real open items (down from the apparent three-way conflict):

1. **Substrate-ingredient identification (the one true metric gap).** Phase-3 builds the metric from **P04 bandwidth**; Paper_033 says the metric comes from **P02/P03/P06 cumulative-strain + kinematic-flow**. Whether bandwidth `b` is a function of strain/flow — so the two *substrate routes* yield the same metric — is unproven. *But note:* Paper_033 never actually carried out the strain/flow→metric construction either (it postulated the result), so this is "two routes to an emergent metric, agreeing at Newtonian order," not "two incompatible explicit metrics." The clean resolution is to check whether `b` (P04) is determined by the strain/flow content (P02/P03/P06) at the substrate level.
2. **The MOND scalar.** Paper_033's MOND lives in a scalar `Φ` with interpolation `μ(|∇Φ|/a₀)` and `a₀=cH₀/2π`. Phase-3 has a khronon (foliation scalar) but did **not** derive `a₀`/BTFR. Unification requires the khronon to be (or source) the MOND scalar — the §3B reconciliation hypothesis, still open.

## 5. A bonus connection — the superluminal scalar

Paper_033 flagged **deep-MOND superluminality** as a structural "cost" — a scalar mode with superluminal phase velocity. Khronometric / Hořava gravity *characteristically* has a **superluminal (even instantaneous) khronon mode** — that is the origin of its "universal horizons." So Paper_033's superluminal-scalar "cost" is plausibly **the khronon of Phase-3**, reframed: not a defect of a scalar-tensor MOND theory, but the expected preferred-foliation scalar of a khronometric theory. (Plausible identification, not shown — but it points the same way as §4.2.)

## 6. Verdict on the metric question

**The bandwidth metric and the acoustic metric do not conflict.** Paper_033's acoustic metric is a *postulate* with unspecified form, pinned only at the Newtonian limit; Phase-3's `g~b⁻¹` is a *derived* metric that (i) agrees there, and (ii) supplies the spatial curvature (Einstein factor-of-2) and lapse (preferred-frame) structure Paper_033 left open. So the bandwidth metric is best read as **the explicit realization of the metric Paper_033 postulated**, sharpening it from "unspecified Lorentzian background" to "khronometric, Einstein-class at weak field." The metric-level "divergence" of the reconciliation memo §2 largely **dissolves**: it was a derived-vs-postulated asymmetry, not a contradiction.

**Two residuals remain, both well-posed:** (1) show `b` (P04) is fixed by the strain/flow content (P02/P03/P06), closing the substrate-route gap; (2) show the khronon reproduces `a₀`/BTFR, closing the MOND gap. Neither blocks a GR-I paper that is honest about them.

## 7. Implication for GR-I

The metric question being settled (no conflict; Phase-3 is the more-explicit realization), **GR-I becomes writable** as: *the explicit emergent metric and weak-field Einstein tests, realizing and sharpening the postulated acoustic-metric background of the published arc.* It must still carry an explicit positioning section (Phase-3 sharpens Paper_033's postulate; the strain↔bandwidth identification §4.1 and the MOND-scalar question §4.2 are declared open), and it must state the metric is khronometric (so the Lorentz status is correct from the start). With that framing, path (A) is now honest and available.

---

*Metric-coincidence analysis. Result: no contradiction — Paper_033's acoustic metric is postulated/form-unspecified, Phase-3's `g~b⁻¹` is derived and agrees at the Newtonian limit while supplying the spatial (factor-of-2) and lapse (preferred-frame) structure Paper_033 left open; the bandwidth metric is the explicit realization of the postulated background. Two well-posed residuals remain (bandwidth↔strain/flow identification; khronon↔MOND scalar). GR-I is now writable along path (A) with explicit positioning. No result overclaimed; the unifying reading rests on the two stated open derivations.*
