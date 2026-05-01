# Arc SG — Substrate Gravity Extension (Arc Opening)

**Date:** 2026-04-30
**Status:** Arc opening. **Arc SG (Substrate Gravity Extension)** — continues the closed substrate-gravity work (T19, T20, ECR, T21, GR1) within the flat-spacetime regime. Consolidates Newton + MOND-class + BTFR-slope-4 results under DCGT; identifies what is FORCED vs INHERITED in the substrate-gravity sector; prepares the ground for ED-10 (curvature emergence) without yet attempting it.
**Companions:** [`../../arcs/arc-SG/`](../../arcs/arc-SG/) (closed substrate-gravity arc memos: ED_combination_rule.md, substrate_a0_ed_native.md, substrate_holographic_bound.md, substrate_2pi_question.md, etc.), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md) (DCGT), [`../Yang-Mills/Arc_YM_6_Synthesis_And_Clay_Relevance.md`](../Yang-Mills/Arc_YM_6_Synthesis_And_Clay_Relevance.md) (parallel arc-extension scope template), [`../../papers/ED_QFT_Overview/ED_QFT_Unified_Overview.md`](../../papers/ED_QFT_Overview/ED_QFT_Unified_Overview.md) §10 (substrate-gravity preview).

---

## 1. Purpose

This memo opens the Substrate Gravity Extension Arc (**Arc SG**), the natural follow-on to the closed substrate-gravity arc work (T19, T20, ED Combination Rule, T21) and to the closed Phase-3 GR1 (curvature-like participation structure). Specifically, the arc:

- **Extends the substrate-gravity program beyond the initial results** of T19 (Newton's law from substrate primitives), T20 (transition acceleration $a_0 = c\,H_0/(2\pi)$), the ED Combination Rule ($a = \sqrt{a_N\,a_0}$), and T21 (slope-4 BTFR $v^4 = G\,M\,a_0$). The closed arc established the leading-order classical-gravitation content; the present extension consolidates these results and identifies their robustness and load-bearing structural conditions.
- **Consolidates the Newtonian + MOND-class + BTFR-slope-4 results** within a unified substrate-derivation framework. The closed arc produced these as separate but mutually consistent substrate consequences; the extension produces them as outputs of a single consolidated substrate-gravity field equation in the flat-background regime.
- **Analyzes substrate-gravity dynamics under DCGT.** With Arc D (DCGT, closed 2026-04-30) now in place, the substrate-to-continuum machinery is available for the gravitational sector. The extension audits how DCGT interacts with substrate-gravity participation-curvature content and which gravitational terms emerge form-FORCED vs INHERITED at the continuum level.
- **Identifies which gravitational effects are FORCED vs INHERITED.** Following the program's standard form-FORCED / value-INHERITED methodology, the extension catalogues every substrate-gravity content channel by structural status: form FORCED at substrate level, sign-FORCED by kernel-positivity properties, value-INHERITED at numerical level, or admissible-not-forced.
- **Prepares the ground for ED-10 (curvature emergence)** without yet attempting it. ED-10 is the queued long-horizon arc that would extend substrate-gravity from the flat-background regime to genuine spacetime-curvature emergence. The present extension produces the structural prerequisites that ED-10 will require: a DCGT-consistent flat-background substrate-gravity equation, a robustness analysis of the BTFR slope-4 result, a kernel-scaling analysis of $a_0$, and a synthesis memo identifying what ED-10 would need to extend.
- **Remains strictly within the flat-spacetime substrate regime.** No attempt to derive the Einstein equation; no curvature dynamics; no metric emergence; no cosmology beyond what $a_0 = c\,H_0/(2\pi)$ already supplies. The acoustic-metric guardrails of ED-Phys-10 are preserved throughout.

The arc is methodologically a *consolidation + extension* arc rather than a fundamental-derivation arc. Closed substrate-gravity work supplies the input results; the extension audits, consolidates, and DCGT-grounds them.

---

## 2. Upstream Foundations

The closed structural content this arc builds on:

**T19 (Newton's law from substrate, 2026-04-27).** $G = c^3\ell_P^2/\hbar$ derived from substrate participation-imbalance arguments via the cumulative-strain mechanism + holographic participation-count bound. Newton's law of universal gravitation is FORCED at substrate level. Closed in `arcs/arc-SG/`.

**T20 (Transition acceleration from kernel retardation, 2026-04-27).** $a_0 = c\,H_0/(2\pi)$ derived from substrate primitives via the cosmological-horizon participation-density connection. The MOND-class transition scale emerges as a substrate consequence; the $2\pi$ prefactor is derived rather than fitted. Closed in `arcs/arc-SG/substrate_a0_ed_native.md`.

**ED Combination Rule (ECR, 2026-04-28).** $a = \sqrt{a_N\,a_0}$ — geometric-mean composition of Newton-class and transition-class accelerations. Cross-term reading $\sqrt{G\,M\,a_0}\cdot\log(R/R_0)$ produces the deep-MOND regime. The substrate rule is *the ED Combination Rule* (no number; "P11" is reserved for Primitive 11). Closed in `arcs/arc-SG/ED_combination_rule.md`.

**T21 (slope-4 BTFR, 2026-04-28).** $v^4 = G\,M\,a_0$ — the baryonic Tully-Fisher relation slope-4 prediction, derived from T19 + T20 + ECR. Empirical galactic-rotation-curve content emerges as a structural consequence of substrate-gravity composition. Closed in `arcs/arc-SG/`.

**Theorem GR1 (V1 with Synge world function, Phase-3 closure 2026-04-24).** V1 vacuum response kernel lifted to curved spacetime via Hadamard parametrix construction. Establishes the *kernel-level* gravitational-sector content of ED while leaving Einstein equations themselves SPECULATIVE (GR-4A status per ED-Phys-10 acoustic-metric guardrails). Provides the gravitational analogue of T18's forward-cone causality.

**DCGT (Arc D closure, 2026-04-30).** Substrate-to-continuum coarse-graining theorem. Hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$; multi-scale expansion of substrate flux statistics; form-FORCED / value-INHERITED structural split. Required for SG-2 (DCGT-consistent Newtonian derivation) and SG-4 (substrate-gravity field equation in flat background).

**ED-I-06 (Fields and Forces in Event Density, Feb 2026).** Three field classes (directional / scalar / curvature-like). For substrate gravity specifically: **mass density $\rho$ is a scalar-field-class participation density** (§4); **gravitational potential $\Phi$ is a scalar-field gradient bias** (§4); **the curvature-like-field thread (§5)** is the bridge to ED-10 (deferred). The ontological reading places substrate gravity squarely in the scalar + curvature-like-field combined class, distinct from the directional-field structure of NS / MHD / YM.

These seven inputs supply the structural prerequisites. No new primitives or theorems are required as inputs; Arc SG builds entirely on closed content.

---

## 3. Scope of the Arc

The arc is scoped as a six-memo plan parallel to Arc D and Arc YM in structural form.

**SG-1 (this memo).** Arc opening; framing, scope, non-goals, inputs, plan.

**SG-2 — Newtonian Potential from DCGT-Consistent Coarse-Graining.** Re-derive Newton's gravitational potential $\Phi(r) = -GM/r$ from substrate primitives via DCGT methodology. Define the substrate participation-density field for a localized mass distribution; apply hydrodynamic-window coarse-graining; identify the leading-order $1/r$ falloff as the substrate-derivation analogue of Newtonian gravity. Confirm consistency with T19's substrate-derivation of $G = c^3\ell_P^2/\hbar$. Estimated 1–2 sessions.

**SG-3 — Transition Acceleration $a_0$ Under Kernel-Profile Scaling.** Audit the kernel-profile-rescaling behavior of $a_0$ under the continuum limit $\ell_P \to 0$. Working a-priori: $a_0 = c\,H_0/(2\pi)$ involves cosmological-horizon scales rather than substrate scales, so the kernel-profile dependence may be qualitatively different from the YM-3 mass-gap scaling. Identify the load-bearing structural conditions for $a_0$ stability under the continuum limit. Estimated 1 session.

**SG-4 — Substrate-Gravity Field Equation in Flat Background.** Produce the consolidated substrate-gravity field equation for the flat-spacetime regime. Working candidate form: a Poisson-class equation for the gravitational potential with substrate-cutoff modifications,

$$\nabla^2\Phi \;=\; 4\pi G\,\rho \;+\; \mathcal{O}(\ell_P^2)\text{ corrections} \;+\; \text{transition-regime terms involving } a_0.$$

Apply DCGT-style multi-scale expansion to the substrate participation-density gradient. Identify the leading-order Newtonian content + transition-regime corrections. Estimated 2 sessions.

**SG-5 — BTFR Slope-4 Robustness Under Kernel Variation.** Audit the slope-4 result $v^4 = G\,M\,a_0$ for robustness under variations of the V1 kernel profile, the participation-bandwidth modulation $\Gamma_0(\rho)$, and the substrate-discreteness assumptions. Identify the structural conditions under which slope-4 is preserved exactly versus the conditions under which it acquires kernel-dependent corrections. Empirical-anchor question: does the closed-arc slope-4 prediction match empirical galactic-rotation-curve data within typical observational uncertainties, and how does that constrain the kernel profile? Estimated 1–2 sessions.

**SG-6 — Synthesis + Implications for ED-10.** Aggregate the five sub-arc results; produce a consolidated structural picture of flat-background substrate gravity; identify the structural prerequisites and open questions that ED-10 (curvature emergence) would need to address. Honest framing on what Arc SG resolves and what remains open. Estimated 1 session.

**Total estimated effort:** 6 memos at the demonstrated pace; 6–8 effective sessions. Comparable scope to Arc D and Arc YM.

### Non-goals (explicit)

- **No attempt to derive full general relativity.** The Einstein equation $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ remains SPECULATIVE per ED-Phys-10 acoustic-metric guardrails; deriving it from substrate primitives is reserved for ED-10.
- **No curvature emergence.** Spacetime curvature is ED-I-06 §5 curvature-like-field-class content that emerges only in the ED-10 arc. The present extension stays in the flat-spacetime regime per the acoustic-metric-only baseline.
- **No cosmology or dark-energy modeling.** Cosmological-constant content, dark-energy modeling, inflation, and related cosmological-scale phenomena are out of scope. T20's $a_0 = c\,H_0/(2\pi)$ is included as a substrate consequence but its cosmological implications beyond the BTFR are deferred.
- **No metric dynamics.** The metric is treated as fixed (Minkowski) throughout; no metric-evolution equations; no graviton modes; no tensor-mode dynamics. These are ED-10 territory.
- **No new primitives.** The arc operates strictly within the closed thirteen-primitive substrate framework; no primitive amendments or new structural commitments.

---

## 4. Structural Questions to Resolve

Five load-bearing questions for the arc:

**(Q1) How does DCGT interact with substrate-gravity participation curvature?** DCGT was developed for the canonical-ED dynamical content of NS / MHD / YM; substrate gravity has different ontological status (scalar-field + curvature-like-field, per ED-I-06). The question is whether DCGT's hydrodynamic-window machinery generalizes cleanly to the gravitational sector, or whether the curvature-like-field aspect requires structural modifications. Working a-priori: scalar-field aspect of substrate gravity (mass density, potential gradient) should generalize cleanly via DCGT scalar-diffusion machinery (Arc_D_2); curvature-like aspect requires extension that ED-10 will supply in full.

**(Q2) Which gravitational terms are FORCED vs INHERITED?** Following NS-MHD-4 and YM-4 templates, classify substrate-gravity content channels:
- Newton's gravity ($-GM/r$ falloff) — likely FORCED at substrate level via DCGT scalar-diffusion + holographic-bound mechanism.
- Transition acceleration ($a_0 \sim c\,H_0/(2\pi)$) — FORCED form, INHERITED value? Or both INHERITED?
- ED Combination Rule ($a = \sqrt{a_N\,a_0}$) — FORCED at substrate level (closed result).
- BTFR slope-4 ($v^4 = G\,M\,a_0$) — FORCED form via T19 + T20 + ECR composition.
- Curvature-like content — SPECULATIVE; deferred to ED-10.

**(Q3) How robust is the BTFR slope-4 result under kernel variation?** SG-5's central question. Variations of the V1 kernel profile, the $\Gamma_0(\rho)$ modulation, and the substrate-discreteness assumptions may preserve slope-4 exactly or produce kernel-dependent corrections. The empirical signal (galactic rotation curves) is the constraint; the slope-4 robustness sets how strongly ED's substrate-gravity output is anchored.

**(Q4) How does the transition acceleration scale with $\ell_P$?** SG-3's central question. Unlike YM mass gap (which scales as $\ell_P^{-2}$ at substrate level and requires kernel-profile rescaling to survive), $a_0$ involves cosmological scales — does it scale with $\ell_P$ at all? Or is the substrate dependence fundamentally different from the YM-3 case? Identify the load-bearing structural conditions.

**(Q5) What substrate-gravity equation governs the flat-background regime?** SG-4's central question. The arc's deliverable is a consolidated equation that recovers Newton in the appropriate limit, transition-regime $a_0$ behavior in the appropriate limit, ECR composition in the cross-term regime, and BTFR slope-4 as the macroscopic galactic-dynamics consequence — all from substrate primitives via DCGT.

---

## 5. Deliverables

Final outputs of Arc SG:

- **A DCGT-consistent substrate-gravity field equation** (SG-4) governing the flat-spacetime regime. Form FORCED at substrate level via DCGT methodology; values INHERITED at value layer.
- **A derivation of Newtonian + MOND-class behavior from substrate primitives** (SG-2 + SG-3). Newton's potential derived cleanly via DCGT scalar-diffusion machinery; transition-regime $a_0$ behavior derived via kernel-profile scaling analysis.
- **A robustness analysis of BTFR slope-4** (SG-5). Identification of structural conditions under which slope-4 is preserved exactly vs. acquires kernel-dependent corrections. Empirical-anchor commentary on galactic-rotation-curve data.
- **A kernel-scaling analysis of $a_0$** (SG-3). Identification of how the transition acceleration scales with $\ell_P$ under the continuum limit.
- **A synthesis memo preparing ED-10** (SG-6). Identification of structural prerequisites and open questions for the curvature-emergence arc.

Once Arc SG closes, the substrate-gravity sector of the program will be DCGT-grounded end-to-end (parallel to NS / MHD / YM closure), with the structural prerequisites for ED-10 explicitly catalogued.

---

## 6. Recommended Next Step

After this opening memo, proceed to **Arc_SG_2 (Newtonian Potential from DCGT-Consistent Coarse-Graining)**. File: `theory/Substrate_Gravity/Arc_SG_2_Newtonian_From_DCGT.md`. Scope: define the substrate participation-density field for a localized mass distribution; apply DCGT-style hydrodynamic-window coarse-graining; identify the leading-order $1/r$ falloff as the substrate-derivation analogue of Newtonian gravity; confirm consistency with T19's $G = c^3\ell_P^2/\hbar$. Estimated 1–2 sessions.

### Decisions for you

- **Confirm arc framing.** Substrate Gravity Extension as the consolidation + DCGT-grounding arc for the closed substrate-gravity work (T19 / T20 / ECR / T21 / GR1); strictly flat-spacetime regime; preparatory for ED-10 but not attempting curvature emergence.
- **Confirm six-memo plan.** Estimated 6–8 effective sessions parallel in scope to Arc D / Arc YM.
- **Confirm proceeding to Arc_SG_2 (Newtonian potential from DCGT) as the next deliverable.**

---

*Arc SG opened. Substrate Gravity Extension as the natural follow-on to the closed substrate-gravity arc work (T19 / T20 / ECR / T21) and Phase-3 GR1 closure. Six-memo plan: SG-2 Newtonian potential from DCGT, SG-3 $a_0$ kernel-profile scaling, SG-4 substrate-gravity field equation in flat background, SG-5 BTFR slope-4 robustness, SG-6 synthesis + implications for ED-10. Strictly flat-spacetime substrate regime; ED-Phys-10 acoustic-metric guardrails preserved; no Einstein equation derivation, no curvature dynamics, no metric emergence, no cosmology / dark-energy modeling. Five load-bearing questions: DCGT × substrate-gravity interaction; FORCED-vs-INHERITED classification of gravitational content channels; BTFR slope-4 robustness under kernel variation; $a_0$ kernel-profile scaling; consolidated substrate-gravity field equation for flat-background regime. Builds on closed structural-foundation work (T17, T18, T19, T20, ECR, T21, Theorem N1, Theorem GR1, DCGT, ED-I-06). Arc_SG_2 (Newtonian potential from DCGT) is the next deliverable.*
