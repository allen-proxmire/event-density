# ED-NS Exploration Roadmap

**Date:** 2026-04-30
**Status:** Consolidating roadmap. Unifies all ED↔NS exploratory routes discovered through the NS-1/2/3 program closure, the Copilot fork-audit, the off-leash exploration, and the multi-Lyapunov + vector-extension findings.
**Purpose:** Single point of reference for ED-NS exploration priorities going forward.
**Companions:** [`NS-1.05_Synthesis_B2_Verdict.md`](NS-1.05_Synthesis_B2_Verdict.md), [`NS-2.07_Synthesis.md`](NS-2.07_Synthesis.md), [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md), [`NS-3.04_Synthesis_Path_Verdict.md`](NS-3.04_Synthesis_Path_Verdict.md), [`NS-3.02b_Multi_Lyapunov_Audit.md`](NS-3.02b_Multi_Lyapunov_Audit.md), [`../Architectural_Canon_Vector_Extension.md`](../Architectural_Canon_Vector_Extension.md).

---

## 1. Purpose

This roadmap consolidates the complete inventory of ED↔NS exploratory routes that have surfaced through:

- The three-arc NS roadmap closure (NS-1 Path B-strong B2 dimensional forcing; NS-2 Newtonian-fluid form derivation; NS-3 Intermediate Path C verdict).
- The ED-PDE-direct second-derivation (NS-2.08) and the partial-vector-extension framing of NS.
- The Architectural Canon Vector-Extension memo and its three-tier classification (canonical / fully ED-architectural / partially ED-architectural).
- The multi-Lyapunov audit (NS-3.02b) and its sharpening of the Clay-NS obstruction to "advective vortex-stretching."
- The Copilot fork-audit listing 6 categories of exploratory routes.
- The off-leash exploration of routes #1–#9 with structural rigor.

The roadmap is organized into a master table of all routes, category summaries, concordance with the closed NS arcs, recommended next arcs, and a parking lot for future work. It is intended as the single point of reference for prioritizing ED↔NS exploration going forward.

Routes are organized under six categories based on outcome:
- **A. Productive and memo-worthy.**
- **B. Productive but unfinished** (require substantive future work).
- **C. Partial but not memo-worthy** (structurally compatible, no novel prediction).
- **D. Negative but informative.**
- **E. Stuck on articulation gaps.**
- **F. Speculative future arcs.**

NS-1, NS-2, NS-3 dimensional forcing and form derivation are *closed*; the routes here are exploration *beyond* program closure.

---

## 2. Master Table of All Routes

| ID | Route | Source | Outcome | Empirical hook | Effort | Priority | Memo? |
|---|---|---|---|---|---|---|---|
| **#1** | Triad P7 ↔ turbulence cascade | Both | Productive but unfinished (definitional mapping needed) | Yes — direct (cascade statistics) | Hard | High | Yes (future arc) |
| **#1a** | ED-architectural turbulence closures | Copilot | Speculative; downstream of #1 | Indirect | Hard | Low | No |
| **#2** | Viscoelastic via V1/V5 memory kernel | Claude | Partial (V5 amplitude INHERITED → structural slot only) | Yes — direct (rheology) | Medium | Medium | Brief note |
| **#3** | Reynolds number from substrate | Claude | Stuck on articulation gap | Yes — direct (Re_c data) | Hard | Low | No |
| **#4** | P4 saturation → non-Newtonian (jamming + Krieger-Dougherty) | Both | **Productive and memo-worthy** — already empirically validated via Universal Mobility Law | Yes — direct (rheology, suspensions) | Medium | **High** | **Yes** |
| **#4a** | Advection as P7-class nonlinearity | Copilot | Negative — wrong nonlinearity type (transport vs. curvature) | No | Hard | Low | Documented in NS-3.02b |
| **#4b** | Pressure as penalty / participation | Copilot | Mismatched (pressure is constraint multiplier, not field-restoring) | No | Medium | Low | No |
| **#4c** | Incompressibility as ED participation | Copilot | Mis-aimed (incompressibility is a low-Mach limit, not fundamental) | Indirect | Medium | Low | Reframe → low-Mach-regime derivation |
| **#5** | Compressibility/shocks via P4 saturation | Claude | Inconclusive (consistency, not derivation) | Yes (gas dynamics) | Hard | Low | No |
| **#6** | Boundary-layer via compositional-rule boundary term | Both | Negative — opposite character (compositional rule smooths; BL concentrates) | Yes (Prandtl) | Medium | Low | Brief note |
| **#7** | Universal invariants ↔ fluid invariants | Claude | Mostly speculative; one promising case (Q ≈ 3.5 ↔ viscous-oscillator Q) | Yes for Q ≈ 3.5 specifically | Easy-Medium | Medium-Low | Brief note |
| **#8** | Compositional-rule direct derivation | Both | Same content as NS-2.08 vector-extension at different layer | No (no new content) | Medium | Low | No |
| **#9** | NS-3 R1/R2/R3 articulation strengthening | Both | Documented in NS-3.04 §7 as articulation gaps | Theoretical | Hard | Low | No (already documented) |
| **#10** | NS-3 R5: substrate-level control of advective vortex-stretching | Claude (NS-3.02b) | Identified obstruction; Path-A-promotion candidate | Theoretical | Hard | Medium | Already in NS-3.04 §7.4 |
| **#11** | Per-component vs. shared participation in vector PDEs | Copilot | Bookkeeping; relevant only if vector ED PDE arc opened | No | Easy | Low | No |
| **#12** | Vector compositional rule / canonical vector ED PDE arc | Copilot | Conceptually open; no specific use case beyond NS | Indirect | Hard | Low | No |
| **#13** | P6 fluid regime taxonomy (D_crit ≈ 0.896 ↔ flow regime) | Copilot | Suggestive; no clean dimensional mapping found | No | Medium | Low | No |

**13 routes total** (9 from Copilot's enumeration + 4 from Claude's exploration).

---

## 3. Category Summaries

### A. Productive and memo-worthy (1 route)

**#4 P4 saturation → non-Newtonian (jamming + Krieger-Dougherty).** Cleanest single finding from the exploration. The Universal Mobility Law (PDE.md §4.1) already empirically validates ED's P4 mobility-saturation structure for 10 soft-matter systems with R² > 0.986. Extending the mobility argument from concentration to packing fraction or strain rate produces, at form-FORCED level, a Krieger-Dougherty-class divergence near jamming — $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ — matching the standard empirical model for suspension viscosity divergence near close-packing. ED structurally derives the *class* of behavior (jamming + shear-thickening); $\beta$ value is INHERITED. **Genuine substantive deliverable; ready for memo and ultimately for paper.**

### B. Productive but unfinished (1 route)

**#1 Triad P7 ↔ turbulence cascade.** ED's P7 specifies a 3–6% harmonic-amplitude ratio with weak coupling ~0.03 for the canonical scalar PDE under multiplicative perturbations. Turbulence has well-studied triad interactions in 3D NS Fourier space with energy transfer at rate set by dissipation rate ε. The qualitative structural compatibility is real (both involve weak nonlinear triad coupling), but a clean quantitative comparison requires careful Fourier-space analysis with specific assumptions about forcing structure, dissipation scale, and triad-amplitude definition. Multi-session work; not closeable in a single audit pass. **Future arc candidate.**

### C. Partial but not memo-worthy (1 route)

**#2 Viscoelastic via V5 memory kernel.** ED architecturally accommodates Maxwell-class viscoelastic fluids via V5 cross-chain correlations with finite memory time τ_R. Form-FORCED structure: memory-kernel viscous response. Value-INHERITED: amplitude (per arc-N N.2 §6.5) and relaxation time. *Honest issue:* V5's amplitude-INHERITED status means ED *accommodates* viscoelasticity but does not *predict* it — there's no novel ED-specific output, just a structural slot for empirical inputs. Unlike #4 which delivers a Krieger-Dougherty-class prediction, #2 delivers structural compatibility only. **Worth a brief note in any future synthesis paper, not a standalone memo.**

### D. Negative but informative (3 routes)

**#4a Advection as P7-class nonlinearity** — confirmed negative. P7 (curvature-class quadratic gradient self-coupling) and advection (transport-class bilinear field-times-gradient with directional preference) are structurally different *types* of nonlinearity. No constitutive choice for $M$ in P7 produces advective transport content. Documented in NS-3.02b §5: this confirms that advection is the non-ED fluid-mechanical addition that breaks the gradient-norm Lyapunov.

**#6 Boundary-layer via compositional-rule boundary term** — confirmed negative. Compositional-rule boundary $\gamma \int h(|\nabla p|) dS$ produces *smoothing* / horizon-class behavior; Prandtl boundary-layer theory has *enhanced* high-gradient activity at walls. Opposite character. The compositional-rule boundary does not derive boundary-layer dynamics.

**#8 Compositional-rule direct derivation** — confirmed not structurally distinct from NS-2.08. The architectural canon (§1) explicitly states that "the compositional rule is the configuration-space statement; the PDE is its continuum-limit dynamics." A "compositional-rule direct" derivation of NS goes through the canonical PDE form (or its vector-extension) as an intermediate step — same content as NS-2.08, described one layer up.

These three negatives are structurally informative: they delineate where ED's canonical architecture *cannot* absorb fluid-mechanical structure, sharpening the partial-vector-extension framing of NS-2.08.

### E. Stuck on articulation gaps (3 routes)

**#3 Reynolds number from substrate.** Re = UL/ν is a dimensional flow parameter dependent on application; substrate-derivation of *critical* Reynolds numbers for laminar→turbulent transitions would require mapping ED's dimensionless D (channel weight) to NS's dimensional Re for specific flow geometries. Not derivable from current primitives.

**#5 Compressibility/shocks via P4 saturation.** Porous-medium-class compact-support / Barenblatt structure (parabolic) and Rankine-Hugoniot shock structure (hyperbolic) are mathematically different mechanisms despite both being "front formation." Structural consistency, not derivation.

**#9 NS-3 R1/R2/R3 articulation strengthening.** Documented in NS-3.04 §7 as Path-A-promotion-class articulation extensions. Each requires substantive new substrate articulation beyond current primitives. Not closeable on current inventory.

### F. Speculative future arcs (4 routes)

**#1a ED-architectural turbulence closures**, **#11 Per-component vs. shared participation**, **#12 Vector compositional rule / canonical vector ED PDE arc**, **#13 P6 fluid regime taxonomy.** Each has potential structural significance but lacks either (a) a concrete use case beyond NS or (b) a specific empirical hook. Tracked here for completeness; deferred until clearer motivation emerges.

**#7 Universal invariants ↔ fluid invariants** sits between F and C. The Q ≈ 3.5 case has plausible empirical content (matches viscous-fluid oscillation regime); other invariants ($D_\mathrm{nd}$, $D_\mathrm{crit}$, $N_\mathrm{osc}$) don't have clean fluid counterparts. Worth a brief note not a memo.

---

## 4. Concordance With NS-1 / NS-2 / NS-3

The exploration roadmap maps cleanly onto the closed NS arcs:

### 4.1 Concordance with NS-1 (B2 dimensional forcing)

NS-1 closed Path B-strong: D = 3+1 forced via architectural d ≥ 3 (T20 mechanism degeneracy at d ≤ 2) + architectural-suggestive d ≤ 3 (Polya recurrence + concentration of measure + decoupling-surface degeneration) + empirical-consistency d ≤ 3 (T19/T20 outputs match observed gravity).

The exploration's articulation-gap routes (#3 Reynolds, #9 R1/R2/R3) parallel NS-1.03's Polya identification gap. Same character: ED's substrate framework is structurally consistent with the empirical answer (d = 3+1 for NS-1; specific Re_c values for #3) but pinning quantitative content from primitives requires articulation extension. The diffusion-coarse-graining future arc (queued for NS-1's Path-A-promotion) is structurally adjacent to #3's needs.

### 4.2 Concordance with NS-2 (form derivation)

NS-2 closed two routes:
- **Chain-substrate route** (NS-2.01–NS-2.07): kinetic-theory-class coarse-graining producing standard Newtonian-fluid NS form at NS scales.
- **ED-PDE-direct route** (NS-2.08): vector-extension of ED canonical PDE channels mapping to NS's viscous content cleanly; pressure / advection / incompressibility flagged as fluid-mechanical-additions.

The exploration confirms and extends NS-2's findings:
- **#4 P4 → non-Newtonian** extends NS-2's Newtonian derivation to the non-Newtonian case via the same mobility channel that NS-2.01 §3.2 identified.
- **#2 Viscoelastic via V5** extends NS-2.05's stress-tensor decomposition to the finite-memory-time case.
- **#4a Advection-not-P7** confirms NS-2.08 §5's "fluid-mechanical addition" cataloging.

### 4.3 Concordance with NS-3 (smoothness / Path C)

NS-3 closed at Intermediate verdict: ED contains a real Clay-relevant stabilizing mechanism (R1's substrate-scale $\ell_P^2 \nabla^4 v$) but does not unconditionally resolve Clay-NS smoothness due to value-INHERITED competition with destabilizing super-Burnett.

**The multi-Lyapunov audit (NS-3.02b) sharpened the obstruction:** of the five Lyapunov functionals admitted by ED's canonical PDE, four transfer to NS at energy-class strength (Leray-equivalent); the fifth — gradient norm $\int|\nabla v|^2 dV$, which would deliver BKM-class — is broken in 3D specifically by the advective vortex-stretching term. This identification is structurally significant because it converges with NS-2.08's vector-extension finding: the same fluid-mechanical-addition (advection) that NS-2.08 catalogues as non-ED is the same structural feature NS-3.02b identifies as breaking the Lyapunov-class Path-C+ route.

**The two findings (architectural + dynamical) are mutually reinforcing.** R5 (substrate-level control of advective vortex-stretching, NS-3.04 §7.4) is the sharpened form of R1's "dominance over destabilizing Burnett" framing.

### 4.4 What the exploration adds beyond NS-1/2/3

**Net new content beyond the closed arcs:**
- #4 productive finding (Krieger-Dougherty-class non-Newtonian) — substantive new prediction.
- #1 productive but unfinished (turbulence cascade) — future arc candidate.
- #6, #4a, #8 negative results — sharpening of NS-2.08's vector-extension framework.
- #7 Q ≈ 3.5 — one promising case for universal-invariant-to-fluid-invariant matching.

**The exploration does not change the closed-arc verdicts** (NS-1 Path B-strong, NS-2 closed, NS-3 Intermediate). It extends the NS-2 form-derivation to non-Newtonian fluids (#4), reinforces NS-3.02b's structural finding via the negative results, and identifies one unfinished future arc (#1).

---

## 5. Recommended Next Arcs

In priority order, with honest justification (some divergence from the order suggested in the user spec; explained below).

### 5.1 First arc: **#4 P4 → non-Newtonian (Krieger-Dougherty-class jamming)**

**Justification.** Cleanest single finding. Already empirically anchored via the Universal Mobility Law (PDE.md §4.1). Extends ED's empirical content from soft matter to fluid mechanics via a structural template that is form-FORCED at the architectural level. Memo-ready immediately; substantive paper achievable within a single short arc (estimated 3–5 sessions). High empirical value (rheology data is plentiful and well-measured); modest theoretical scope (one mechanism extended to a new domain).

**Note on ranking divergence:** The user's spec ordered viscoelastic (#2) first, turbulence (#1) second, P4 (#4) third. After honest exploration, the recommended ordering is reversed: P4 *delivers a prediction* (Krieger-Dougherty-class divergence with form-FORCED structure); viscoelastic is *structurally compatible* but doesn't predict beyond INHERITED inputs. Memo-readiness and empirical anchoring make P4 the strongest first deliverable.

**Recommended deliverable:** memo `theory/Navier Stokes/Future_Arc_P4_Non_Newtonian_Scoping.md` followed by 3–5 derivation memos under the same arc. Possible publication path: extend the Universal Mobility Law paper to a fluid-mechanical companion paper, or produce a standalone paper "ED Mobility Saturation Predicts Krieger-Dougherty-Class Non-Newtonian Rheology."

### 5.2 Second arc: **#1 Triad P7 ↔ turbulence cascade**

**Justification.** Highest empirical value of any unfinished route — turbulence is one of the deepest open problems in classical physics, and ED's P7 invariant 3–6% amplitude ratio is a *concrete number* that either matches measured turbulence triad statistics or doesn't. If it matches, the result is genuinely significant (ED supplies a structural prediction about turbulence cascade that standard NS doesn't). If it doesn't match, the result is also informative (rules out a specific structural identification).

**Honest caveat.** Substantive analytic work required to set up the comparison properly. ED's harmonic-amplitude ratio (steady-state response to multiplicative perturbations on scalar field) and turbulence's triad-energy-transfer rate (dimensional flux per unit time across scales) are different quantities; mapping between them requires Fourier-space analysis with specific assumptions. Estimated 2–3 sessions for the mapping setup before any quantitative comparison can be made.

**Recommended deliverable:** scoping memo `theory/Navier Stokes/Future_Arc_Triad_Turbulence_Scoping.md`, then a derivation arc (4–6 memos) producing the quantitative comparison. Possible publication path: standalone paper if the comparison closes affirmatively or with a clear partial result.

### 5.3 Third arc: **#2 Viscoelastic via V1/V5 memory kernel** (or the user's #1)

**Justification.** Structurally clean; direct empirical hook to rheology data; medium effort. ED accommodates Maxwell-class viscoelastic fluids via V5 cross-chain correlations with finite memory time. The form-FORCED content is "memory-kernel viscous response"; values INHERITED from polymer / biological-fluid molecular relaxation times.

**Honest caveat.** V5's amplitude-INHERITED status (per arc-N N.2 §6.5) limits what ED predicts here. The route delivers structural compatibility (ED can host Maxwell-class viscoelasticity) but does not produce an ED-specific prediction beyond what's INHERITED. Less productive than #4 in terms of novel ED content; more productive than #4 in terms of ease of memo-writing (the structural compatibility is a one-pass result).

**Recommended deliverable:** if pursued, one or two memos at most. Better integrated into the #4 arc as a sub-section "viscoelastic extension" rather than a standalone arc.

### 5.4 Honest aggregate framing

The strongest substantive new deliverable from this exploration is **#4 P4 → non-Newtonian.** The strongest unfinished prospective arc is **#1 triad → turbulence.** **#2 viscoelastic** is a structural slot, less productive as a standalone deliverable. Recommend pursuing the three in the order #4 → #1 → #2 (memo, scoping, integration), with #4 producing a standalone memo and possibly a paper, #1 producing a scoping document and an arc-cycle of analytic work, and #2 folded into #4 as an extension subsection.

---

## 6. Parking Lot (Future Work)

Routes deferred to indefinite future: not closeable on current articulation; speculative; lack of clear use case; or already documented elsewhere.

| Route | Reason for parking |
|---|---|
| #1a (ED-architectural turbulence closures) | Downstream of #1; speculative until #1 closes |
| #3 (Reynolds from substrate) | Articulation gap; parallel to NS-1.03 Polya gap; would need Arc-D-class follow-on |
| #4b (Pressure as penalty / participation) | Mismatched (pressure is constraint multiplier, not field-restoring); unlikely to close |
| #4c (Incompressibility as ED participation) | Mis-aimed; reframe as "low-Mach-regime derivation" if pursued |
| #5 (Compressibility/shocks via P4) | Inconclusive; consistency only; structural mismatch |
| #6 (Boundary-layer via compositional-rule) | Negative outcome documented; no further work |
| #7 (Universal invariants ↔ fluid, except Q ≈ 3.5) | Speculative; no clean dimensional matches |
| #8 (Compositional-rule direct) | Same content as NS-2.08; not distinct route |
| #9 (NS-3 R1/R2/R3 strengthening) | Articulation gaps; documented in NS-3.04 §7 |
| #10 (R5 advective vortex-stretching control) | Sharpened form of #9 R1; same articulation status; documented in NS-3.04 §7.4 |
| #11 (Per-component vs shared participation) | Bookkeeping; relevant only if vector ED PDE arc opens |
| #12 (Vector compositional rule arc) | No specific use case beyond NS; deferred |
| #13 (P6 fluid regime taxonomy) | Suggestive; no clean dimensional mapping found |

These routes are tracked here so they don't get rediscovered as net-new every time the program revisits ED-NS exploration.

---

## 7. Final Orientation

This roadmap is the canonical reference for ED↔NS exploration priorities. Use it to:

- **Avoid re-exploring already-closed routes.** The 13 routes catalogued are the result of two systematic enumeration passes (Copilot's fork-audit + Claude's off-leash exploration). New ED-NS exploration should reference this list and check whether a proposed route is already audited.
- **Prioritize next-arc selection.** §5 supplies the recommended ordering with honest justification; deviate only with explicit reason.
- **Track articulation-gap dependencies.** Routes #3, #9, #10 are parallel in character to NS-1.03's Polya gap and the queued diffusion-coarse-graining arc; they would close together if a substrate-articulation extension supplies the missing primitive-level argument.
- **Frame ED's relationship to NS for external-facing material.** ED reproduces NS form (NS-2); forces d = 3 (NS-1); contains a real Clay-relevant mechanism (NS-3 R1); and structurally derives non-Newtonian rheology classes (#4 P4 → Krieger-Dougherty). The exploration's aggregate finding is that ED's substrate framework is empirically rich for fluid mechanics beyond Clay-NS — the non-Newtonian rheology connection is the load-bearing finding for "ED on Earth" empirical applications.

The roadmap is intended to be updated as new routes surface or as future arcs close. Pull requests welcome; the canonical version of this document supersedes any informal exploration lists.

---

*ED-NS Exploration Roadmap. Thirteen routes catalogued from Copilot fork-audit + off-leash exploration. One memo-ready productive finding (#4 P4 → non-Newtonian / Krieger-Dougherty). One unfinished high-value prospect (#1 triad → turbulence). Four negative-but-informative results documented. Seven articulation-gap or speculative routes parked. NS-1/2/3 closed-arc verdicts unchanged; exploration extends ED's empirical reach into non-Newtonian fluid mechanics and identifies a candidate future arc for turbulence-cascade analysis.*
