# Memo_ED_RouteA_Scoping_Wave3 — Scoping Memo for Route A (Substrate-Graph Derivation of $H_0$)

**Series:** Wave-3 Scoping Memo (Cosmology Arc + ED-SC Arc; addresses the single remaining load-bearing OPEN across the Cosmology Arc per ED_MEMORY anchors 7 + 15)
**Status:** Substrate-graph scoping of Route A — the derivation of the late-universe Hubble scale $H_0$ from ED substrate parameters, canonically via the V5 cross-chain kernel length $\ell_{V_5}$. Closure would supply value-DERIVED upgrade for **Paper_ED_Cos_01** (Inflation; M3) + **Paper_ED_Cos_05** (Dark Energy; M3 conditional on Route A) + **Paper_038_5** (Lambda_V1_Cosmological; M2 → M3 retroactive upgrade) within the M3 framing, and trigger the ED-SC 4.x arc-wide M3 → M2 upgrade (six projections simultaneously per ED_MEMORY anchor 7). **Not a derivation. No new primitives proposed. Negative results acceptable.**
**Date:** 2026-05-16
**Anchors:** ED_MEMORY anchor 7 (Route A as highest-leverage open derivation); ED_MEMORY anchor 15 (Q1Q2 + Chain-Class Identification Project context); Paper_087 (13 primitives — P02 + P03 + P04 + P11 + P12); Paper_073 (DCGT hydrodynamic-window); Paper_089 (V1 retarded kernel + Lorentz-covariance §3); Paper_090 (V5 cross-chain finite-memory; ~40 OOM cross-scale correlations); Paper_027 (Newton's $G$ via dimensional rearrangement); Paper_038_5 (Λ-smallness reframing — Λ reduces to Route A + Friedmann); Paper_ED_Cos_01 (M3; Q1A + Q2A + C3 + IC-INHERITED chain); Paper_ED_Cos_05 (M3 conditional on Route A); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + Hessian); Papers SC-4.x (scale-collapse + six projections); Paper_ED_CCC §3.6 + §3.7 (late-LDE asymptote + post-BBB ignition); Memo_ED_LoadBearingProgram_Overview (program-level Route A context).

> ⚠️ **Correction (2026-07-06):** This memo cites Θ_ED as "Paper_087 P12 (ED-threshold)." That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7, itself now flagged. This does not change this memo's tier verdicts (Θ_ED remains substrate-parameter-INHERITED throughout) — it only corrects the primitive citation. See `event-density/docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## §1 Restated Route A target

### §1.1 The Route A claim to close

**Derive $H_0$ (or equivalently $\ell_{V_5}$ given the substrate-c bound $\ell_{V_5} = c \tau_{V_5}$) from ED substrate parameters** such that DCGT translation yields the observed Hubble rate $H_0 \approx 70$ km/s/Mpc $\approx 2.2 \times 10^{-18}$ s$^{-1}$ corresponding to Hubble radius $R_H = c/H_0 \approx 1.4 \times 10^{26}$ m $\approx 14$ Gly.

The substrate-side scale targeted by the canonical Route A formulation (per ED_MEMORY anchor 7) is **$\ell_{V_5}$** — the V5 cross-chain kernel finite-memory length. Per Paper_090, V5 supplies cross-chain correlations across ~40 orders of magnitude of parameter scales, structurally bridging substrate-scale (Planck) and cosmological-scale phenomena. $\ell_{V_5}$ is therefore the natural substrate-side length whose value should determine cosmological-scale $H_0$.

### §1.2 Distinction from already-closed form-IDENTIFIED saturation

Critical distinction (per Memo_ED_Q1Q2_JointClosure_Construct + Memo_ED_ChainClass_C3_Construct + Paper_ED_Cos_01 §3.8):

| Aspect | Status | Closed by |
|---|---|---|
| **(i) form-IDENTIFIED saturation** — substrate-graph derivation that uniform-$\Psi$ substrate configuration gives vacuum-energy form continuum stress-energy with $w = -1$ → constant $H$ → de Sitter / exponential expansion | **CLOSED** at M3 form-IDENTIFIED + IC-INHERITED level | Q1A + Q2A + C3 + IC-INHERITED chain (Cos_01 §3.8) |
| **(ii) value-DERIVED $H_0$** — substrate-graph derivation of the specific numerical value of $H$ at the late-LDE saturation regime | **OPEN — Route A target** | (this memo's scope) |

The form-IDENTIFIED closure establishes that *whatever* the substrate-graph value of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ is at saturation, it determines a constant $H$ via Friedmann. **Route A asks: what determines $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ — or equivalently $\rho_\Lambda^{\mathrm{const}}$, or equivalently $\ell_{V_5}$ via the substrate-side dimensional structure?**

### §1.3 Λ-smallness inheritance per Paper_038_5

Per Paper_038_5 §3.7 reframing: $\rho_\Lambda^{\mathrm{substrate}} = (3/8\pi) H_0^2 \cdot M_P^2$ with $M_P^2$ via Paper_027 (Newton's $G$ via dimensional rearrangement) — *INHERITED*. The substrate-side closure of $\rho_\Lambda$ therefore reduces to closing $H_0$ via Route A. **Λ-smallness is a quantitative-magnitude question controlled by Route A, not a separate substrate-research gap.** Closing Route A closes both $\rho_\Lambda$ and the famous 120-OOM problem simultaneously.

### §1.4 Cross-arc reach of Route A closure

| Paper | Pre-Route-A | Post-Route-A closure |
|---|---|---|
| Paper_ED_Cos_01 (Inflation) | M3 form-IDENTIFIED + value-INHERITED | M3 with **value-DERIVED** (eliminates value-INHERITED component within M3) |
| Paper_ED_Cos_05 (Dark Energy) | M3 conditional on Route A | M3 **unconditional**; value-DERIVED |
| Paper_038_5 (Lambda_V1) | M2 conditional retroactive M3 pending Route A | M3 (retroactive upgrade per Paper_038_5 reframing) |
| ED-SC 4.x arc-wide | M3 (six projections) | **M3 → M2 simultaneously** (six-way upgrade per ED_MEMORY anchor 7) |
| Paper_ED_Dyn_02 + Dyn_03 | M2 pending Route C1 + C4 (chain-class identification) | unchanged — Route A doesn't address chain-class identification |

Route A is the **single load-bearing remaining OPEN across the Cosmology Arc** after Cos_01 + Cos_05 M3 closures. Its closure has the broadest cross-arc reach in the corpus.

---

## §2 Substrate-side scale candidates

Four candidate substrate-side quantities could set the long-distance scale $\ell_{V_5}$ (or equivalent cosmological-scale length).

### (i) V5 kernel decay length $\ell_{V_5} = c \tau_{V_5}$

Per Paper_090, V5 has finite-memory cross-chain coupling with characteristic memory time $\tau_{V_5}$; the associated length is $\ell_{V_5} = c \tau_{V_5}$ via substrate-c bound (Paper_012). V5's role in the corpus is bridging cross-scale correlations across ~40 OOM — exactly the scale range relevant to cosmological-vs-substrate-scale separation.

**Substrate-graph well-definedness:** STRONG structurally; Paper_090 supplies V5 with finite-memory structure as a primitive feature. The **specific value** of $\tau_{V_5}$ (and hence $\ell_{V_5}$) is **not** supplied by primitive content — it is the substrate-research-frontier OPEN.

### (ii) SC-4.x Hessian eigenvalue asymptotics

Per Paper_ED_SC_4_9 + Papers SC-4.x, the substrate-action saddle Hessian has eigenvalues whose magnitudes set characteristic scales. At saturation, all eigenvalues are equal (Hessian-degenerate, per Memo_ED_ChainClass_C3_Construct §3 analysis); this equal value is a candidate substrate-side scale.

**Substrate-graph well-definedness:** PARTIAL. Hessian eigenvalue magnitudes are substrate-graph computable per SC-4.9; the asymptotic value at late-LDE saturation requires explicit derivation from SC-4.x scale-collapse content.

### (iii) Post-SCBU $\Psi$ relaxation timescale

Per Paper_ED_CCC §3.6, the post-SCBU substrate asymptotes to uniform $\Psi$ via cosmological-expansion-driven dilution (per Paper_ED_Cos_05 §3.3 mechanism). The characteristic timescale of this relaxation is a candidate substrate-side scale; cosmologically it corresponds to the Hubble time $H_0^{-1}$.

**Substrate-graph well-definedness:** PARTIAL. The relaxation mechanism is structurally identified at composition-level (Paper_ED_Dyn_02 + Paper_073 + Paper_ED_CCC §3.6); the specific timescale requires substrate-graph derivation from V1 + V5 kernel dynamics.

### (iv) Substrate-action density asymptotic $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at saturation

Per Paper_ED_SC_4_9 + Memo_ED_Q1Q2_JointClosure_Construct §2, at saturation regime $\mathcal{L}_{\mathrm{sub}} = \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$. The value of this constant determines $\rho_\Lambda$ via DCGT translation and hence $H_0$ via Friedmann.

**Substrate-graph well-definedness:** PARTIAL. The constancy is established (Q1A + C3 closures); the **specific value** of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at saturation requires substrate-graph derivation — load-bearing for Route A.

**Note:** all four candidates are structurally related — they likely reduce to a single substrate-graph derivation question (what determines the saturation-regime characteristic scale on the substrate graph). The four candidates are different vocabulary entry-points to the same underlying question.

---

## §3 DCGT-side conversion mechanisms

Three candidate DCGT-side mechanisms could convert a substrate-side scale to the cosmological Hubble scale.

### (a) Coarse-graining radius $R_{\mathrm{cg}}$ as effective cosmological scale

Per Paper_073, DCGT operates within $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. At the late-universe saturation regime, $L_{\mathrm{flow}}$ approaches the Hubble radius $R_H$; the natural DCGT $R_{\mathrm{cg}}$ for cosmological-scale phenomena scales with $R_H$. If $R_{\mathrm{cg}}$ is set by $\ell_{V_5}$ (e.g., $R_{\mathrm{cg}} \sim \ell_{V_5}$ at the cosmological-scale coarse-graining), then $R_H \sim \ell_{V_5}$ and $H_0 \sim c/\ell_{V_5}$.

### (b) Effective metric scaling under DCGT

DCGT produces the continuum effective metric (Paper_073). The scaling of this effective metric determines cosmological distances; if the effective metric scale tracks $\ell_{V_5}$ (substrate-side characteristic length), then $R_H = c/H_0 \sim \ell_{V_5}$.

### (c) Long-time hydrodynamic limit

The DCGT long-time limit gives the asymptotic continuum hydrodynamic regime. At late-universe saturation, the hydrodynamic limit's characteristic timescale corresponds to $H_0^{-1}$ (the cosmological evolution timescale). If this timescale is set by $\tau_{V_5}$ (substrate-side characteristic time) via $H_0^{-1} \sim \tau_{V_5}$, then $H_0 \sim 1/\tau_{V_5} = c/\ell_{V_5}$.

**All three conversion mechanisms yield the same parametric relation $H_0 \sim c/\ell_{V_5}$.** This is structurally informative — the substrate-side length $\ell_{V_5}$ and continuum-side Hubble radius $R_H$ are parametrically equivalent under DCGT translation. The substrate-graph derivation of $\ell_{V_5}$ is therefore the load-bearing component of Route A.

---

## §4 Candidate closure routes

Four candidate substrate-graph derivation paths for $\ell_{V_5}$. Each must be evaluated for: closure plausibility; corpus-content support; load-bearing vs vocabulary-level distinction.

### §4.1 Route A1 — V5 kernel decay length → DCGT → $H_0$

**Mechanism:** $\ell_{V_5}$ is the V5 cross-chain finite-memory length per Paper_090. DCGT coarse-graining at scale $R_{\mathrm{cg}} \sim \ell_{V_5}$ produces continuum hydrodynamic-limit with characteristic length $R_H \sim \ell_{V_5}$ → $H_0 = c/R_H \sim c/\ell_{V_5}$.

**Substrate-graph derivation of $\ell_{V_5}$ from primitives:** Paper_090 establishes V5's finite-memory structure as a primitive feature but does not derive the specific memory length. Possible sub-derivation paths:
- $\ell_{V_5}$ via dimensional rearrangement from Paper_087 primitives + Paper_012 substrate-c + Paper_073 hydrodynamic-window parameters (analog of Paper_027's dimensional rearrangement for Newton's $G$)
- $\ell_{V_5}$ via cross-chain correlation-length analysis from V1 + V5 kernel composition
- $\ell_{V_5}$ as a posited primitive parameter (would require new primitive — outside scope)

**Plausibility:** MEDIUM. Direct framing of the question; closure requires explicit substrate-graph derivation of $\ell_{V_5}$ which is not currently in the corpus.

**Load-bearing:** YES — direct attack on the canonical Route A formulation.

### §4.2 Route A2 — SC-4.x Hessian eigenvalue asymptotics → effective curvature → $H_0$

**Mechanism:** at late-LDE saturation, SC-4.x scale-collapse drives Hessian eigenvalues to specific asymptotic values per Papers SC-4.x. These eigenvalues set an effective curvature scale; standard cosmology relates curvature to Hubble parameter via $H_0^2 \sim$ (curvature) modulo Friedmann.

**Substrate-graph derivation of Hessian asymptotic values:** Papers SC-4.x establish the scale-collapse content at SCBU; the late-LDE asymptote approach to SCBU is the boundary-approach regime. Hessian eigenvalue asymptotic values at this regime are derivable from SC-4.x content per the six-projection framework (one projection is $\xi_{\mathrm{canonical}}$ → Route A target).

**Plausibility:** MEDIUM-HIGH. SC-4.x + ED-SC 4.x framework supplies the structural target; the specific Hessian → curvature → $H_0$ mapping requires explicit derivation.

**Load-bearing:** YES — aligned with the ED-SC 4.x arc-wide upgrade pathway (one of the six projections is precisely $\xi_{\mathrm{canonical}}(H_0)$ per ED_MEMORY anchor 7).

### §4.3 Route A3 — $\Psi$ relaxation timescale → DCGT → $H_0$

**Mechanism:** post-SCBU substrate relaxation to uniform $\Psi$ takes characteristic time $\tau_{\mathrm{relax}}$; cosmologically this corresponds to the Hubble time $H_0^{-1}$ (the timescale over which the late universe asymptotes to pure de Sitter). DCGT translates $\tau_{\mathrm{relax}}$ to continuum cosmological time.

**Substrate-graph derivation of $\tau_{\mathrm{relax}}$:** the relaxation mechanism per Paper_ED_Cos_05 §3.3 (cosmological-expansion-driven dilution) is identified composition-level; the specific timescale requires substrate-graph derivation from V1 + V5 kernel dynamics under post-SCBU conditions.

**Plausibility:** LOW-MEDIUM. The mapping from relaxation timescale to cosmological Hubble time is non-obvious; would require substantive substrate-graph derivation that the relaxation timescale is exactly the cosmological-evolution timescale (not, e.g., the matter-Λ crossover timescale $z_\Lambda \approx 0.7$ which is shorter than $H_0^{-1}$).

**Load-bearing:** YES — provides an independent derivation pathway not subsumed by Route A1 or A2.

### §4.4 Route A4 — Substrate-action density asymptotic → Friedmann → $H_0$

**Mechanism:** substrate-action density $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at saturation determines $\rho_\Lambda$ via DCGT (Q2A) and hence $H_0^2 = (8\pi G/3)\rho_\Lambda$ via Friedmann. Substrate-graph derivation of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ from primitives closes Route A.

**Substrate-graph derivation of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$:** the constancy at saturation is established (Q1A + C3); the value at saturation requires substrate-graph derivation from primitive content. Possible sub-derivation: $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ via P12 ED-threshold value (the substrate-action density at saturation is the threshold value at which V1 + V5 + individuation reactivate per CCC §3.7) + dimensional analysis from Paper_087 primitives.

**Plausibility:** MEDIUM. Connects to Paper_087 P12 (ED-threshold) and Paper_027 (dimensional rearrangement) cleanly. The P12 ED-threshold value itself is a primitive-content question that may or may not be derivable from sub-primitive analysis.

**Load-bearing:** YES — provides a fourth independent pathway via the substrate-action density's characteristic value.

---

## §5 Load-bearing vs vocabulary-level routes

| Route | Load-bearing? | Note |
|---|---|---|
| **A1** (V5 kernel decay length → DCGT → $H_0$) | **YES** | Canonical Route A formulation per ED_MEMORY anchor 7 |
| **A2** (Hessian asymptotics → curvature → $H_0$) | **YES** | Aligned with ED-SC 4.x arc-wide upgrade; potentially closes via six-projection framework |
| **A3** ($\Psi$ relaxation timescale → DCGT → $H_0$) | YES (less likely to close cleanly) | Independent pathway; substantive substrate-graph derivation required |
| **A4** (substrate-action density asymptotic → Friedmann → $H_0$) | **YES** | Connects to Paper_087 P12 + Paper_027 dimensional rearrangement |

**All four routes are load-bearing** — none reduce to vocabulary-level reframings. The four routes are independent derivation pathways that may or may not produce identical $H_0$ predictions; if multiple pathways close consistently, the closure is tightened (multi-route convergence). If only one closes, that pathway is the substantive Route A closure.

**Net assessment:**

- **Best closure plausibility:** Route A2 (Hessian asymptotics + ED-SC 4.x framework) and Route A4 (substrate-action density + Paper_027 dimensional rearrangement) have the strongest corpus-content support; both connect to existing substrate-research-frontier content (SC-4.x + Paper_087 P12 + Paper_027).
- **Canonical formulation:** Route A1 (V5 kernel decay length) is the ED_MEMORY-anchor-7 canonical phrasing but requires substrate-graph derivation of $\ell_{V_5}$ that may itself need to reduce to A2 or A4 content.
- **Independent derivation pathway:** Route A3 ($\Psi$ relaxation timescale) is substantively distinct and would supply confirmatory cross-pathway closure if it closes; less likely to close cleanly.

**The four routes likely reduce to one substantive substrate-research question:** what substrate-graph primitive-content value sets the characteristic substrate-side scale at the late-LDE saturation regime? Different vocabulary entry-points (V5 kernel; Hessian asymptotics; relaxation timescale; substrate-action density) all converge on this single question.

---

## §6 OPEN subproblems

After this scoping, the load-bearing OPEN subproblems for Route A closure:

| Sub-OPEN | Description | Load-bearing for which route |
|---|---|---|
| **RA-OPEN-1** | Substrate-graph derivation of $\ell_{V_5}$ from Paper_087 primitives + Paper_012 + Paper_073 (dimensional rearrangement analog to Paper_027 for Newton's $G$) | Route A1 |
| **RA-OPEN-2** | Substrate-graph derivation of late-LDE asymptotic Hessian eigenvalue values from Papers SC-4.x + ED-SC 4.x six-projection framework | Route A2 |
| **RA-OPEN-3** | Substrate-graph derivation of post-SCBU $\Psi$ relaxation timescale $\tau_{\mathrm{relax}}$ from V1 + V5 kernel dynamics under post-SCBU conditions | Route A3 |
| **RA-OPEN-4** | Substrate-graph derivation of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ value at saturation from P12 ED-threshold + Paper_087 dimensional analysis | Route A4 |
| **RA-OPEN-5** | Substrate-graph derivation that the four candidate routes converge to the same $H_0$ prediction (multi-route convergence verification) | All four routes — confirmatory |

**Auxiliary OPEN (not load-bearing for Route A closure itself):**

- Substrate-graph derivation of matter-Λ crossover redshift $z_\Lambda \approx 0.7$ — tied to Route C1 (chain-class identification) + Route A; would supply additional cosmological-timing verification but not Route A's load-bearing content
- Substrate-graph derivation of inflation duration ~60 e-folds — tied to Route C1 + Route A
- Cyclic-vs-non-cyclic framework determination (CCC audit row 17) — independent of Route A but related to whether Route A's substrate-graph derivation extends across cycles

### Negative-finding possibilities (acceptable outcomes)

- **N1:** Paper_087 primitive content + existing corpus structure does **not** supply substrate-graph derivation of any of the four candidate scales ($\ell_{V_5}$, Hessian asymptotic, $\tau_{\mathrm{relax}}$, $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$) from primitive content alone. $H_0$ remains value-INHERITED permanently; Cos_01 + Cos_05 cap at M3 with value-INHERITED component permanent; ED-SC 4.x remains M3 with Route A permanent OPEN. **This would be a substantive substrate-ontology characterization:** ED's substrate ontology supports the form of standard cosmology phenomenology via DCGT inheritance but does not supply the quantitative magnitudes.

- **N2:** A subset of routes close (e.g., Route A1 closes via dimensional rearrangement; Route A2 fails to close substrate-graph) — partial closure; would partially upgrade value-INHERITED → value-DERIVED for the closing route's prediction, with explicit qualification about which routes succeeded/failed.

- **N3:** Routes close but predict inconsistent $H_0$ values (multi-route divergence) — substrate-research-frontier finding indicating that the routes are not equivalent at substrate-graph level; would force re-examination of the routes' substrate-graph content.

- **N4:** Routes close via standard-physics-analog inheritance rather than substrate-graph derivation (parallel to the load-bearing program's "approximately-X-analog" closure pattern that the Q1Q2 + chain-class identification project subsequently replaced with construction-uniqueness). Would partially close Route A but inherit a similar "approximately-substrate-graph" qualification.

All four outcomes are corpus-informative.

---

## §7 Recommended next steps

### §7.1 Path priority

**Path-A4-Construction (highest closure plausibility):** focused construction memo attempting RA-OPEN-4 — substrate-graph derivation of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ value at saturation from P12 ED-threshold + Paper_087 dimensional analysis. Connects directly to Paper_027's successful dimensional-rearrangement template for Newton's $G$; the analogous template applied to substrate-action density at the P12 threshold may produce $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ → $\rho_\Lambda$ → $H_0$.

**Path-A2-Construction (parallel; high-leverage):** focused construction memo attempting RA-OPEN-2 — substrate-graph derivation of late-LDE Hessian eigenvalue asymptotic values from Papers SC-4.x + ED-SC 4.x six-projection framework. The $\xi_{\mathrm{canonical}}(H_0)$ projection is precisely the Route A target per ED_MEMORY anchor 7; this pathway is the most corpus-aligned with the standing ED-SC 4.x arc-wide upgrade objective.

**Path-A1-Construction (canonical formulation):** focused construction memo attempting RA-OPEN-1 — substrate-graph derivation of $\ell_{V_5}$ via dimensional rearrangement. If A1 closes substantively rather than reducing to A2 or A4, supplies an independent pathway.

**Path-A3-Construction (independent pathway; lower priority):** attempt only if A1, A2, A4 don't deliver convergent closure. Substrate-graph derivation of $\tau_{\mathrm{relax}}$ from V1 + V5 kernel dynamics; substantively distinct.

**Path-Multi-Route-Convergence-Audit:** after individual route construction attempts, audit whether closing routes converge on the same $H_0$ prediction. Multi-route convergence is the tightening criterion for Route A's full closure.

### §7.2 My recommendation

**Path-A4-Construction + Path-A2-Construction in parallel.** Both have the strongest corpus-content support; A4 connects to the proven Paper_027 dimensional-rearrangement template; A2 connects to the standing ED-SC 4.x arc-wide upgrade objective. If both close convergently, Route A reaches substantive closure. Path-A1 + Path-A3 follow as tightening / confirmatory routes.

### §7.3 Cross-program impact summary

Best-case outcome (Route A4 + A2 close convergently + audits accept):
- **Cos_01 + Cos_05** upgrade to **M3 with value-DERIVED** (eliminating value-INHERITED component within M3 framing)
- **Paper_038_5** retroactive M2 → M3 upgrade
- **ED-SC 4.x arc-wide** M3 → M2 upgrade (six projections simultaneously)
- **Λ-smallness 120-OOM problem** quantitatively resolved at substrate-graph level
- **Single highest-leverage corpus contribution to date** per ED_MEMORY anchor 7

Mid-case (one route closes; others partial or N4-inheritance):
- Partial value-DERIVED upgrade with explicit qualification about closure pathway
- Substantive substrate-research finding documenting which routes work vs which need further substrate-research-frontier work

Worst-case (N1 negative — no route closes substrate-graph from existing primitives):
- $H_0$ permanently value-INHERITED across the Cosmology Arc
- Substrate-ontology characterization sharpens: substrate ontology supports standard cosmology form via DCGT inheritance but not quantitative magnitudes
- Substantive corpus finding (parallel to the load #2 chirality negative finding) — would honestly cap the Cosmology Arc's quantitative-magnitude content at INHERITED level

All outcomes corpus-informative. Route A's substantive substrate-research attack is the natural successor to the Q1Q2 + Chain-Class Identification Project's substrate-graph construction-uniqueness work, applied to the quantitative-magnitude component that the form-IDENTIFIED closures explicitly left INHERITED.

**Closure plausibility for full Route A:** MEDIUM. The corpus supplies the structural-content (Paper_087 primitives + Paper_073 DCGT + Paper_027 dimensional rearrangement template + Papers SC-4.x); the load-bearing question is whether existing primitive content + dimensional analysis + SC-4.x asymptotic structure together suffice to fix $\ell_{V_5}$ (or equivalent scale) without new primitive content. Substrate-research-frontier work but not substrate-research-discovery — closer to construction than to invention.

---

## §8 Substantive comparison with prior projects

| Project | Substrate-research target | Closure pattern | Outcome |
|---|---|---|---|
| Load-Bearing Program (2026-05-16) | Five qualitative-mechanism load-bearings | "Approximately-X-analog inheritance" closures | 3 closed + 1 negative + 1 reframed to Route A |
| Q1Q2 + Chain-Class Identification Project (2026-05-16 follow-on) | Construction-uniqueness for substrate-side Noether + DCGT mapping + chain-class identification | Substrate-graph construction-uniqueness (no standard-physics-analog inheritance) | Cos_01 re-upgraded M3; Cos_05 drafted M3 conditional on Route A; substrate-research-pattern shift |
| **Route A (this scoping; pending construction)** | **Quantitative-magnitude derivation of $H_0$ via $\ell_{V_5}$** | **Dimensional-rearrangement analog + SC-4.x asymptotic analysis + multi-route convergence** | **TBD — MEDIUM closure plausibility; corpus-content supports the structural target; substrate-graph derivation of scale value is the substantive substrate-research question** |

Route A is the **third substantive substrate-research project** in the chain. The first two projects delivered (i) qualitative-mechanism closures via standard-physics-analog inheritance, then (ii) substrate-graph construction-uniqueness without inheritance. Route A's target is (iii) quantitative-magnitude substrate-graph derivation using existing primitive content + dimensional analysis. The progression is substantively meaningful: from inheritance-level closures to construction-uniqueness closures to magnitude-derivation closures.

---

**End Memo_ED_RouteA_Scoping_Wave3.**
