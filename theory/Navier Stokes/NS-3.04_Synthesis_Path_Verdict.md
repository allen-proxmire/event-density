# NS-3.04 — Synthesis + Path C Verdict

**Date:** 2026-04-30
**Status:** NS-3 closed. **Final verdict: Intermediate.** ED's substrate framework contains a structurally significant, substrate-scale stabilizing mechanism (R1: form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v$ term from V1 finite-width); does not unconditionally resolve Clay-NS smoothness in the strict mathematical-rigor sense. Path C+ not achieved; Path C− not forced; ED contains real Clay-relevant mechanism with quantitative resolution INHERITED. Three articulation-extension tasks identified for path-to-Path-A-promotion.
**Audits integrated:** [`NS-3.01_LP4_Regularization_Survival.md`](NS-3.01_LP4_Regularization_Survival.md), [`NS-3.02_Holographic_Global_Bound.md`](NS-3.02_Holographic_Global_Bound.md), [`NS-3.03_V5_V1_Transport_Bound.md`](NS-3.03_V5_V1_Transport_Bound.md). Companion: [`NS-3_Scoping.md`](NS-3_Scoping.md), [`NS-2.07_Synthesis.md`](NS-2.07_Synthesis.md), [`NS-1.05_Synthesis_B2_Verdict.md`](NS-1.05_Synthesis_B2_Verdict.md).

---

## 1. Purpose

NS-3.04 aggregates the three NS-3 audits and delivers the final Path C verdict for ED's relationship to the Clay Navier-Stokes smoothness problem.

The three audits asked, each from a different structural angle: does ED's substrate framework provide a regularization mechanism that prevents finite-time blow-up of NS solutions on $\mathbb{R}^3$?

- **R1 (NS-3.01):** Does ED's substrate cutoff at ℓ_P produce a higher-derivative regularization term in the continuum momentum equation?
- **R2 (NS-3.02):** Does T19's holographic participation-count bound translate to a continuum gradient bound of BKM-class strength?
- **R3 (NS-3.03):** Do V5 cross-chain correlations or V1 finite-width transport limits impose a continuum strain-rate bound?

NS-3.04 reports the aggregate verdict and frames the program-level implication. NS-1 (closed Path B-strong) closed B2 dimensional forcing; NS-2 (closed) derived the standard NS form from substrate primitives; NS-3 closes here with the Clay-relevance verdict.

---

## 2. Summary of R1 (NS-3.01) — Form-FORCED Conditional

**Verdict: Form-FORCED stabilizing mechanism, value-INHERITED conditional.**

The V1 finite-width retarded vacuum kernel (Theorem N1 + T19's ℓ_ED = ℓ_P) acts as a low-pass filter at substrate scale. Multi-scale expansion of the V1-mediated stress contribution yields a higher-derivative term in the continuum momentum equation:

$$\rho \frac{D v_i}{Dt} = -\partial_i p_\mathrm{eff} + \mu_\mathrm{total} \nabla^2 v_i \;-\; \kappa \, \mu_\mathrm{V1} \, \ell_P^2 \, \nabla^4 v_i \;+\; \rho f_i^\mathrm{ext} + \mathrm{(other\ corrections)},$$

with κ > 0 (stabilizing) FORCED by V1's positive-smoothing-kernel structure; magnitude INHERITED via Theorem N1's G-function specific form (per arc-N N.4) and via μ_V1's INHERITED status.

The term **survives the continuum limit** (ℓ_P is fixed substrate constant; coefficient does not vanish), is **numerically negligible at NS scales** (suppression ratio $\le 10^{-60}$ at laboratory scales), and **becomes dominant at substrate scale** where it would activate to suppress blow-up.

**Honest concern that prevents clean Path C+:** standard kinetic-theory Chapman-Enskog produces Burnett-class ∇⁴ v terms at scale $\lambda_\mathrm{mfp}^2$ with destabilizing signs (Bobylev instability). For typical fluids, $\lambda_\mathrm{mfp}^2 / \ell_P^2 \sim 10^{50}$ — standard destabilizing Burnett quantitatively dominates ED's stabilizing V1 contribution at any scale where Burnett expansion applies. Whether ED's substrate-scale stabilization wins out over intermediate-scale destabilization in a putative blow-up trajectory depends on quantitative competition that is INHERITED on both sides.

**R1 is the only NS-3 route producing a non-trivial Path C+ contribution.** It is form-FORCED structurally significant; it is not unconditionally Path-C+-resolving.

---

## 3. Summary of R2 (NS-3.02) — Clean Failure

**Verdict: R2 fails for Path C+ purposes.**

The proposed identification chain — substrate participation count $N \le A/\ell_P^2$ → coarse-grained chain density → continuum energy density → enstrophy / strain-rate / vorticity — breaks at step (3) → (4). Energy-density bounds do not translate to gradient-distribution bounds.

The holographic bound supplies at most an alternative *substrate-level derivation* of an energy-class bound that is **approximately equivalent to standard Leray's energy inequality**. This is structurally interesting (Leray's bound has substrate origin in ED) but is not stronger than what standard NS already has.

The bound does not reach **BKM-class strength**. The integrability $\int_0^T \|\omega(t)\|_\infty dt < \infty$ that BKM requires for smoothness preservation is not derivable from any energy-class bound; this is exactly the obstacle that prevents standard NS analysis from closing the Clay problem, and ED's holographic bound does not get past it.

Three potential strengthening routes flagged in NS-3.02 §3.4 (velocity-gradient ↔ channel-capacity identification; vorticity-channel quantum identification; holographic + V5 joint bound) each have load-bearing identification gaps and are not closable on current substrate articulation.

---

## 4. Summary of R3 (NS-3.03) — Vacuous Failure

**Verdict: R3 fails vacuously for Path C+ purposes.**

The substrate-level maximum rate $c/\ell_P \approx 1.9 \times 10^{43}$ s⁻¹ is structurally real — forced by ED-07 (finite-c) + Q.8 (substrate cutoff) + ED-10 (relational adjacency) jointly. It exceeds any plausible NS strain rate by **at least 28 orders of magnitude**. The cell-resolution bound $c/\lambda_\mathrm{mfp} \approx 10^{18}$ s⁻¹ is a tautological coarse-graining-resolution constraint, not a substrate-derived dynamical bound. Step (3) → (4) propagation to pointwise $\|\nabla v\|_\infty$ structurally fails for the same reason as R2.

V5 amplitude-INHERITED status (per arc-N N.2 §6.5) prevents form-derivable continuum constraint from V5 cross-chain correlations. Three candidate strengthening arguments (causality bound on V5; holographic count bound on V5; V5 energy-content bound) each lead to either INHERITED bound, count-not-amplitude bound, or energy-not-amplitude bound. None form-closeable without articulation extension.

R3 produces no non-trivial Path C+ contribution.

---

## 5. Aggregate Analysis

### 5.1 The three audits in one picture

| Route | Mechanism | Verdict | Path C+ contribution |
|---|---|---|---|
| R1 | Substrate ℓ_P cutoff → continuum higher-derivative regularization | Form-FORCED-conditional | Yes — substrate-scale stabilization, value-INHERITED dominance |
| R2 | Holographic count bound → continuum gradient bound | Clean fail | None — Leray-equivalent only |
| R3 | Substrate transport rate → continuum strain-rate bound | Vacuous fail | None — bounds vacuous or INHERITED |

### 5.2 What ED delivers structurally

**ED provides a real stabilizing mechanism for NS at substrate scale.** R1's $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v$ term is structurally distinct from anything available in standard NS analysis. It is form-derivable from V1's finite-width kernel + multi-scale expansion. Its existence is not a hand-wave; the derivation goes through.

**But:**

**ED does not unconditionally guarantee smoothness.** The mechanism is *conditional* on quantitative competition: ED's substrate-scale stabilization vs. standard-kinetic-theory's destabilizing super-Burnett. Both magnitudes are INHERITED. Whether stabilization dominates destabilization in a putative blow-up trajectory is a value-level question not derivable from current primitives.

**The single-mechanism status matters.** With R2 and R3 failing, R1 carries the entire NS-3 Path-C+ load alone. There is no concordance across multiple routes; there is no fallback if R1's value-INHERITED dominance question goes the wrong way.

### 5.3 Why intermediate is the honest verdict

- Path C+ in the strict sense ("ED rigorously prevents finite-time blow-up of NS solutions on $\mathbb{R}^3$") is not delivered. R1's mechanism is conditional, R2 fails, R3 fails.
- Path C− in the strict sense ("ED's substrate framework provides no structural mechanism relevant to Clay-NS") is not forced. R1 produces a real, form-FORCED mechanism that is *not present in standard kinetic-theory NS*. ED has more structure than the standard framework.
- The honest intermediate verdict: **ED contains a structurally significant, substrate-scale stabilizing mechanism. Clay-NS smoothness remains unresolved due to inherited quantitative competition with standard destabilizing terms whose magnitudes are also inherited.**

This is parallel in character to the structurally-honest pattern across the program: NS-1.03's identification gaps; substrate_2pi_question's articulation diagnosis; V5's amplitude-INHERITED status; T19/T20's empirical-consistency forcing alongside primitive-level d-agnosticism. The Clay smoothness question is hard for the same reason these other questions hit articulation gaps: ED's substrate primitives establish form-FORCED structural content, while value-level resolution requires either articulation extension or empirical input.

---

## 6. Final Path C Verdict

**Path C verdict: Intermediate.**

Formal statement:

> *ED's substrate framework, applied to the Navier-Stokes equations on $\mathbb{R}^3$ at d = 3+1 (forced via NS-1's Path B-strong B2 closure), produces the standard Newtonian-fluid NS form at NS scales (per NS-2's substrate→continuum coarse-graining). The substrate cutoff at ℓ_P generates a structurally identified higher-derivative regularization term $-\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v$ in the continuum momentum equation (form-FORCED via Theorem N1 + T19; sign FORCED positive via V1's positive-smoothing-kernel structure; magnitude INHERITED). This regularization is dominant only at substrate scale and is conditional on quantitative competition with standard kinetic-theory destabilizing super-Burnett terms whose magnitude is also INHERITED. Holographic and V5/V1-transport routes (R2, R3) do not supply additional Path-C+-relevant mechanisms beyond R1.*
>
> *ED therefore neither unconditionally resolves the Clay-NS smoothness problem (Path C+) nor inherits the Clay-NS open status without structural contribution (Path C−). The correct characterization is that **ED contains a real, structurally distinct Clay-relevant mechanism that does not unconditionally guarantee smoothness**.*

**Sharpening from the multi-Lyapunov audit (NS-3.02b, added 2026-04-30).** The multi-Lyapunov audit confirms that the only Lyapunov functional that *could* have reached BKM-class strength — the gradient norm $\int|\nabla v|^2 dV$ (enstrophy-class) — is broken in 3D NS specifically by the advective convective derivative's vortex-stretching term $\int(\partial_j v_i)(\partial_i v_k)(\partial_k v_j) dV$. **Pressure-gradient (in incompressible flow) and incompressibility itself do not break the gradient-norm Lyapunov; advection alone does.** This aligns with NS-2.08's architectural finding that advection is the fluid-mechanical addition not native to the canonical ED PDE: the same structural feature that NS-2.08 identifies as non-ED-architectural is the specific feature that NS-3.02b identifies as breaking the BKM-class Lyapunov route. The Clay obstruction in ED-architectural language is therefore: *can ED's substrate-scale stabilization control the non-ED advective vortex-stretching term?* The two findings (architectural and dynamical) are mutually reinforcing and converge on the same structural feature.

### 6.1 Final a-priori distribution

The honest a-priori distribution moved through the audit cycle:

- Initial (NS-3 scoping): 30% C+ / 50% C− / 20% intermediate
- After R1 (partial-FORCED): 20% / 30% / 50%
- After R2 (clean fail): 10% / 30% / 60%
- After R3 (vacuous fail): 5% / 35% / 60%
- **Final NS-3.04 verdict: Intermediate.** Aligned with the post-R3 distribution's modal value.

### 6.2 What this verdict means quantitatively

ED makes no quantitative prediction *worse* than standard NS. The standard NS empirical match is preserved (per NS-2.07: ED reproduces standard Newtonian-fluid NS at NS scales). What ED adds is a *structural* mechanism (form-FORCED at substrate scale) that *might* resolve blow-up in a more rigorous treatment. The substantive empirical content of NS in ED is identical to standard NS; the substantive structural content is enriched by the substrate cutoff's regularization mechanism.

For practical NS applications (laboratory, engineering, atmospheric, geophysical), ED's NS form behaves identically to standard NS within all empirically accessible regimes. The Clay smoothness question is mathematical-rigor question; it has no operational consequence for NS predictions in any realizable application.

---

## 7. Identification Gaps and Future Work

Three articulation-extension tasks identified across the three audits. Each, if closed, could promote NS-3's intermediate verdict toward Path C+. **None is required for NS-3 closure;** they are queued as candidate Path-A-promotion-class follow-on work.

### 7.1 R1 gap — quantitative dominance of ED stabilization over Burnett destabilization

NS-3.01 §6.2 identified the load-bearing concern: ED's substrate-scale stabilization is quantitatively dominated by standard-kinetic-theory destabilizing super-Burnett at intermediate scales. R1's verdict became conditional rather than clean.

Closing this gap would require a structural argument that, in a putative blow-up trajectory, the trajectory through scales is dominated by ED's substrate-scale stabilization rather than by intermediate-scale Burnett destabilization. This is fundamentally a value-level competition that depends on parameters INHERITED on both sides; a *substrate-derivable* upper bound on Burnett-class destabilization (or lower bound on ED's stabilization) would close it.

**Estimated character:** difficult. Requires either deeper substrate articulation (V1 G-function specific form) or a global structural argument about scale trajectories that is currently unavailable.

### 7.2 R2 gap — velocity-gradient ↔ channel-capacity identification

NS-3.02 §3.4 (route 1) identified the cleanest strengthening route for R2: an identification of velocity-gradient magnitude with channel-capacity-usage rate. If this identification can be derived from substrate primitives, the holographic bound translates to a gradient distribution bound (not just energy bound), potentially reaching BKM-class strength.

**Estimated character:** moderate-difficult. Requires structural articulation of how participation-channel capacity is consumed by gradient features at substrate level. Not in current inventory; would be a primitive-level extension to ED-10 or substrate-rules-stability.

### 7.3 R3 gap — substrate-level upper bound on V5 amplitudes

NS-3.03 §5 identified that V5 amplitudes are INHERITED with no primitive-level upper bound. Closing this gap requires a primitive-level argument that bounds V5 amplitudes from above by a substrate-derivable quantity, even without pinning the value.

**Estimated character:** difficult. V5's INHERITED-amplitude status is a fundamental feature of arc-N's framework; tightening it would require a substantial substrate articulation extension parallel in scale to a sub-arc.

### 7.4 R5 gap — substrate-level control of advective vortex-stretching

Identified by the multi-Lyapunov audit (NS-3.02b, 2026-04-30). The sharpened form of the R1 dominance question (§7.1): **can ED's $\ell_P^2 \nabla^4 v$ substrate-scale stabilization control the specific non-ED advective vortex-stretching term that breaks the gradient-norm Lyapunov $\int |\nabla v|^2 dV$ in 3D NS?**

R5 is structurally tighter than R1's "dominance over destabilizing super-Burnett" framing because it identifies the *exact* structural feature that needs to be controlled — the triple-product $\int (\partial_j v_i)(\partial_i v_k)(\partial_k v_j) dV$ from advection — rather than the broader Burnett-class destabilizing content. Closing R5 would require either (a) a substrate-level argument that ED's R1 stabilization dominates the advective triple-product specifically (rather than dominating Burnett-class generically), or (b) an ED-architectural absorption of the advective term as canonical ED content (per NS-2.08 §5's catalogue of fluid-mechanical-additions; would require a canon extension).

**Estimated character:** difficult. R5 is a refinement of R1 not an independent gap; closing R5 would close R1 *a fortiori*. Its value over R1 is precision: R5 names what specifically must be controlled, R1 only names that *something* must dominate Burnett-class destabilization. R5 is the form in which Path-C+ promotion via R1 is most cleanly stated.

**Connection to NS-2.08:** R5 directly inherits NS-2.08's "advection as fluid-mechanical-addition" finding. Both findings point to the advective convective derivative as the specific non-ED structural feature; R5 makes the dynamical statement of the same structural fact NS-2.08 made architecturally.

### 7.5 Connection to the queued Arc D (diffusion-coarse-graining)

Arc D (queued per [`Future_Arc_Diffusion_Coarse_Graining_Scoping.md`](Future_Arc_Diffusion_Coarse_Graining_Scoping.md)) was originally identified for **NS-1.03's Polya identification gap** — the path to clean Path A B2 closure. Arc D's machinery (chain-dynamics-as-diffusion identification, Polya-class boundary inheritance) is structurally adjacent to but distinct from the three NS-3 gaps above:

- Arc D would supply substrate-level diffusion machinery for the Einstein-relation-class identification $\mu \sim \rho D_\mathrm{eff}$, which would refine NS-2.06 territory but does not directly address any of the three NS-3 gaps.
- Arc D could *potentially* feed into R2's strengthening route 1 (velocity-gradient ↔ channel-capacity) if the diffusion-coarse-graining produces a substrate-level statement about capacity-usage rates. This connection is speculative.

**Net:** Arc D opening remains a Path-A-promotion (NS-1) + program-strengthening (NS-2.06 viscosity values) decision rather than a NS-3-resolving decision. Arc D's outputs would refine but not transform NS-3's verdict.

---

## 8. Program-Level Implications

NS-3 closure completes the Navier-Stokes roadmap. Aggregating across NS-1, NS-2, NS-3:

### 8.1 What ED has delivered for Navier-Stokes

- **NS-1 (closed):** B2 dimensional forcing closes on Path B-strong. d = 3+1 forced via architectural + empirical-consistency layers; Path A promotable via the queued diffusion-coarse-graining theorem (Arc D).
- **NS-2 (closed):** Standard Newtonian-fluid NS form derived from substrate primitives + d = 3 geometry. Form-FORCED; values INHERITED. ED-specific deviations identified but numerically negligible at NS scales.
- **NS-3 (closed):** ED contains a structurally significant Clay-relevant mechanism (R1's substrate-scale stabilization) but does not unconditionally resolve Clay-NS smoothness. Three identification gaps queued as articulation-extension follow-on work.

### 8.2 The program-level NS verdict

**ED reproduces NS form (NS-2). ED forces d = 3 (NS-1). ED contains a real Clay-relevant stabilizing mechanism (NS-3). ED does not resolve Clay-NS in the strict mathematical-rigor sense.**

This is a substantively positive program-level result. ED's substrate framework supplies a structural foundation for NS that standard analysis lacks; this foundation is not yet rigorous enough to close the Clay smoothness question, but it is structurally distinct from standard NS in identifiable ways. The Clay smoothness question moves, in the ED framing, from a *purely analytical* question (about continuum PDE behavior) to a *structural-empirical* question (about whether ED's identified substrate-scale stabilization dominates standard intermediate-scale destabilization quantitatively).

This relocation is itself a structural contribution, even though it is not a Clay resolution.

### 8.3 Connection to other ED structural-foundations results

The NS roadmap's Intermediate verdict for Clay-NS sits cleanly within the program's pattern of structurally-honest closures. Comparable cases:

- **B2 dimensional forcing** (NS-1, parallel program): closed Path B-strong rather than Path A; identification gap (chain-dynamics-as-diffusion) flagged for future Arc D.
- **Substrate gravity arc** (T19, T20, ED Combination Rule, T21): structurally complete derivation of empirical galactic-gravity phenomenology with substrate-rule articulation gaps explicitly noted (per substrate_2pi_question).
- **V5 cross-chain correlations** (arc-N): existence FORCED, amplitude INHERITED; structural significance preserved with value-content honestly INHERITED.

The Clay-NS verdict fits this pattern: form-FORCED structural content + identifiable identification gaps + value-INHERITED quantitative resolution. The program's methodological discipline is preserved; structural-foundations claims are ratified at the level the primitives support and articulated honestly where they don't.

### 8.4 What remains open in ED's NS framework

- Path A B2 promotion via Arc D (diffusion-coarse-graining theorem). NS-1 → Path A.
- Substrate-derivable refinement of $\mu_\mathrm{V1}$ value via Arc D's Einstein-relation identification. NS-2.06 territory.
- Three NS-3 identification gaps (R1 dominance, R2 gradient↔channel, R3 V5 upper bound) for Path C+ promotion.
- Empirical test program for ED's NS deviations from standard NS — primarily relevant in extreme regimes (high-frequency acoustic near $\tau_\mathrm{V1}$ scales; non-Newtonian fluids where V5-INHERITED amplitude could differ from kinetic-theory expectation; substrate-approaching gradient regimes inaccessible to current experiment).

None of these is *required* to close the NS roadmap as currently scoped. They are program-level strengthening + future-work items.

---

## 9. Recommended Next Steps

In priority order. NS-3 closure completes the Navier-Stokes roadmap; the immediate question is what the program does next.

1. **Prepare external-facing summary of NS-1 / NS-2 / NS-3 closure.** The Navier-Stokes roadmap's three substantive arcs are now closed. An external-facing artifact is recommended:
   - **Public-facing explainer** (Desktop `ED Public Overviews/`): "Why ED Reproduces Navier-Stokes, Forces d = 3, and Contains a Clay-Relevant Mechanism." Plain-language summary of the three-arc closure for non-specialist audience. Estimated 2–3 pages.
   - **Technical synthesis paper** (`papers/ED_Navier_Stokes_Foundations/`): comparable in scope and length to the substrate-gravity paper. Combines NS-1, NS-2, NS-3 closures into a single publication-grade artifact. Honest framing per §6 + §8: form-FORCED content, value-INHERITED parameters, three identification gaps queued. Estimated 20–30 pages at the substrate-gravity-paper template length.
   - **Derivation-architecture SVG**: parallel to ED_Theorem17_Derivation_Architecture.svg / ED_Substrate_Gravity_Derivation_Architecture.svg. Shows the full primitive → arc → theorem chain for NS roadmap closure. ~1 SVG.
   These artifacts can be produced sequentially (explainer first as the cheapest; paper second; SVG third) or in parallel.

2. **Decide on Arc D opening.** With NS-3 closed, the case for opening Arc D shifts. Originally Arc D was queued primarily for NS-1.03 Path A promotion (B2). With NS-3 also closing, Arc D's program-level value is:
   - Path A promotion for B2 (clean architectural d = 3+1 closure): primary motivation.
   - NS-2.06 viscosity-value refinement: secondary motivation.
   - NS-3 R2 strengthening (velocity-gradient ↔ channel-capacity): speculative connection.
   Recommend deciding on Arc D opening *now* that NS-3 is closed, since the Arc D timing decision was deferred to this point per NS-2.07 §8 / NS-3 scoping §7. Recommendation: open Arc D as the next derivation arc (after external-facing material in step 1 is produced), since it strengthens both NS-1 (Path A) and NS-2.06 (substrate-derivable viscosity) with one arc.

3. **Identify publication-ready artifacts and program-status update.** Beyond the NS-roadmap artifact in step 1, consider:
   - **Update `memory/project_navier_stokes_roadmap.md`** to reflect NS-1/2/3 closure with authoritative file pointers.
   - **Update `docs/ED-Orientation.md` / `C:\Users\allen\Desktop\ED_ORIENTATION.md`** with NS roadmap status (NS-1 Path B-strong / NS-2 closed / NS-3 Intermediate; Arc D queued; three identification gaps recorded).
   - **Update FORCED-theorem inventory** if applicable. Note: NS-2 produced no new theorem-rank result (form-derivation arc, methodology preserves existing theorems); NS-1 and NS-3 produced verdicts rather than theorems. So inventory ratifies existing Theorem 1–21 + ED Combination Rule; no new entries.
   - **Project memory update on B2 status:** B2 closure on Path B-strong is now the operative answer; NS-3 is closed; Arc D is the queued path-to-Path-A-promotion.

4. **Honest program-state characterization.** With NS-1/2/3 closed plus the existing 21-theorem-plus-ED-Combination-Rule structural-foundations program plus the empirical-test program (FRAP, optomechanics, retrodictions, BEC, etc.), the program-level honest state is: **structurally-foundational program is largely complete in form-FORCED content, with three queued articulation extensions (Arc D, R1 dominance, R2 gradient↔channel) and the empirical-test program as the load-bearing locus of continued progress.** Worth communicating this state explicitly in any external-facing material.

### Decisions for you

- **Confirm Intermediate verdict.** ED contains a real Clay-relevant stabilizing mechanism (R1 form-FORCED) but does not unconditionally resolve Clay-NS (R1 value-INHERITED dominance). Sharp, honest, structurally significant.
- **Confirm Arc D timing.** Open Arc D next (recommended, given NS-3 closure removes any uncertainty about Arc D's program value), or defer further (in favor of external-facing material first).
- **Confirm publication-ready artifact priorities.** Three candidates (explainer, paper, SVG); sequencing affects load on author. Recommend explainer first as cheapest; paper and SVG can follow when ready.
- **Update program memory and orientation documents** to reflect NS roadmap closure.

---

*NS-3 closed at Intermediate. ED contains a structurally significant Clay-NS-relevant stabilizing mechanism (R1: form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v$) that does not unconditionally guarantee smoothness due to value-INHERITED competition with standard destabilizing super-Burnett. R2 and R3 fail. Three identification gaps queued as Path-A-promotion candidates for future articulation extensions. NS roadmap closes: ED reproduces NS form (NS-2), forces d = 3 (NS-1), contains real Clay-relevant mechanism (NS-3), does not resolve Clay-NS in strict mathematical-rigor sense. Honest, structurally significant, methodologically continuous with program-wide form-FORCED / value-INHERITED pattern.*
