# Dimensional Forcing / B2 Close-Out — NS-1 Scoping

**Date:** 2026-04-30
**Status:** Active scoping. NS-1 of the Navier-Stokes roadmap. Closes B2 either way (independently valuable).
**Companion:** [`Navier_Stokes_Roadmap_Scoping.md`](../Navier_Stokes_Roadmap_Scoping.md)

---

## 1. Purpose of NS-1 (Dimensional Forcing / B2 Close-Out)

NS-1 is architectural analysis, not a physics question. The question is:

> **Given ED's primitive set + the seven PDE-uniqueness axioms, is D = 3+1 forced, or is dimensionality an external input?**

This is not "is Navier-Stokes well-posed in 3+1" (that is the Clay problem, NS-3 territory). It is the prior structural question: which ED primitives survive a dimensional lift to D ≠ 3+1, which collapse, and does the surviving set still produce the canonical PDE? If the substrate primitives + uniqueness axioms admit no consistent lift away from 3+1, dimensionality is forced. If they admit a lift but the resulting effective theory is degenerate, dimensionality is forced *consistently with the substrate* but the forcing is internal-consistency-driven rather than axiom-driven.

The B2 question (Why 3+1 dimensions, PDE-level) is open in current inventory: R.2.4 forces Cl(3,1) on the spinor bundle, and R.2.2 / R.2.3 use D = 3+1 as input rather than deriving it. The seven PDE-uniqueness axioms do not include spacetime dimensionality. NS-1 closes this gap or reports honestly that it cannot.

NS-1 closes B2 regardless of whether NS-2/3/4 ever execute, which is why it is the recommended first executable arc among both Clay roadmaps.

---

## 2. The Four Candidate Forcing Routes

Three architectural layers are involved: representation-theoretic (spinor bundle), PDE/kernel-level, substrate-level. The four routes distribute across these layers.

### 2.1 Cl(3,1) Forcing Route (representation-theoretic)

**Architectural principle.** R.2.4 forces Cl(3,1) signature on the spinor bundle via Lorentz frame uniqueness. The spinor-bundle commitment fixes D = 3+1 *for spinor structure*. A forcing route to PDE-level dimensionality requires showing the PDE cannot be decoupled from the spinor bundle's signature commitment.

**What forcing would mean.** D = 3+1 inherited at PDE level via the structural inseparability of the spinor bundle and the PDE — the PDE's admissible solution class cannot be reformulated on a base manifold of different dimensionality without breaking the participation-measure / sign-flip / Lorentz-frame coupling.

**In inventory.**
- R.2.4 (Lorentz frame uniqueness → Cl(3,1) on spinor bundle): [`arcs/arc-B/arrow_implications.md §5.1`](../../arcs/arc-B/arrow_implications.md)
- R.2.2 / R.2.3 (spin ladder, anyon prohibition — *uses* D = 3+1 as input): [`arcs/arc-B/arrow_catalogue.md §5.3`](../../arcs/arc-B/arrow_catalogue.md)

**What still needs derivation.**
- The PDE↔spinor-bundle inseparability argument. Either: (a) show the PDE-level dynamics require spinor-bundle structure intrinsically (so R.2.4 propagates downward to PDE), or (b) show the participation-measure setup that grounds the PDE *is* the spinor-bundle setup at base-manifold level (the two are not independent strata).
- A failure mode audit: a "decoupled spinor bundle" interpretation in which R.2.4 fixes Cl(3,1) for matter content only and leaves the PDE on a d-dimensional base manifold formally admissible. This is the route's main risk.

**Independence.** Derivative of R.2.4. The route's load-bearing content is the propagation step from spinor-bundle to PDE; without that step, this route closes only the spinor sector and leaves the PDE-level question open.

### 2.2 Huygens-Preservation Route (PDE/kernel-level)

**Architectural principle.** The sharp form of Huygens' principle — wave propagation supported strictly *on* the light cone with no interior tail — holds for the standard wave operator only in odd spatial dimensions d ≥ 3, with d = 3 the canonical case. Even d and d = 1 produce Hadamard tails (interior support). T18 establishes V1 kernel retardation as kernel-level arrow of time. If T18's derivation requires *sharp* Huygens propagation (cone-supported retardation kernels, not interior-supported), then T18 forces d ∈ {3, 5, 7, …} at PDE/kernel level. Combined with substrate motif viability (route 2.3) ruling out d ≥ 4, d = 3 falls out.

**What forcing would mean.** A purely PDE-level dimensional forcing, structurally independent of spinor-bundle considerations. This is the strongest candidate for genuinely PDE-level dimensional forcing (the other three routes operate at neighboring strata).

**Substrate→continuum preservation.** "Sharp Huygens preserved under coarse-graining" means: the substrate-level retardation structure (kernel discrete-and-finite, supported on substrate light cones up to ℓ_P resolution) coarse-grains to a continuum kernel supported strictly on the continuum light cone, not its interior. The preservation question is whether substrate-scale support broadening (any process that smears retardation across small interior regions at scale ℓ_P) survives the continuum limit or scales to zero. T19's holographic participation-count bound is potentially relevant: if the bound forces tight kernel support under coarse-graining, sharp Huygens is preserved.

**In inventory.**
- T18 (V1 kernel retardation, kernel-level arrow of time): [`theorems/T18.md`](../../theorems/T18.md)
- Arc B retardation memos: [`arcs/arc-B/`](../../arcs/arc-B/)

**What still needs derivation.**
- **The single most consequential audit in NS-1:** does T18's derivation actually require *sharp* Huygens propagation, or does it tolerate Hadamard interior-supported retardation? Binary outcome. Determines whether any purely PDE-level forcing route exists.
- If sharp Huygens required → PDE-level forcing of odd d ≥ 3 is established.
- If Hadamard tails tolerated → route 2.2 dies; PDE-level route is closed off; substrate-level routes (2.3, 2.4) and representation route (2.1) carry the load alone.

**Independence.** Structurally independent of routes 2.1, 2.3, 2.4. Operates at PDE/kernel level. Highest value-per-effort because (a) the audit is small, (b) the outcome is binary, (c) it determines whether the only purely-PDE-level route exists.

### 2.3 Substrate-Motif Viability Route (substrate-level, upper bound)

**Architectural principle.** ED's architectural motifs — gradients, saddles, boundaries, horizons, participation neighborhoods — are local-discriminating structures on the substrate. In high d, neighborhood combinatorics dilute factorially (volume of unit d-ball ~ π^(d/2)/Γ(d/2+1) → 0 for d → ∞), and concentration of measure forces near-equidistance of points on bounded supports. Both effects collapse gradient discrimination, horizon stability, and motif coherence. By d ≥ 4 spatial, the architecture is too smooth to support the motifs that make ED ED.

**What forcing would mean.** A substrate-level upper bound: d ≤ 3 spatial. Not a lower bound — the route as currently sketched does not address d = 1 or d = 2.

**The d ≥ 3 lower bound (the harder half).**
- d = 2: T20's dipole-mode mechanism uses azimuthal 2π periodicity on the cosmic horizon's projection. In 2+1, the cosmic horizon is a 1-sphere; projection geometry degenerates; a₀ derivation breaks. *Internal-consistency forcing* — ED cannot host its own substrate-gravity arc at d ≤ 2.
- d = 1: chain primitive structure (P-class) presumably collapses — chains in 1D have no non-trivial neighborhood, no transverse gradient, no participation-mediated coupling. Needs explicit articulation against the relevant primitive statements.
- The lower bound currently lives mostly in T20 (d = 2 incompatibility) and chain-primitive-collapse (d = 1 incompatibility). Articulation needed in both cases.

**In inventory.**
- ED-Phys-39 (4D case shown to be barely architectural — referenced in user notes; file location to be confirmed)
- Substrate primitives (P04 bandwidth-additivity; chain primitive; participation-measure setup) — primitive-level statements available across [`ED-primitives`](https://github.com/allen-proxmire/ED-primitives) repo

**What still needs derivation.**
- Explicit primitive-level derivation of the dilution function. Heuristic C(d) ~ 1/d! is not a derivation; it needs an anchor. Concentration-of-measure (Talagrand, Lévy) on the participation-measure setup is the cleaner formal foundation than informal volume-shrinkage heuristics. Identify which primitive(s) — P04 (bandwidth-additivity), participation-measure construction, chain primitive — generate the dilution at primitive-statement level.
- Lower-bound articulation: d = 2 forbidden via T20 dipole-mode degeneracy; d = 1 forbidden via chain-primitive collapse. Both need explicit derivation, not assertion.
- Verification that the relevant primitives are stated d-agnostically. If P04 / chain / participation-measure presuppose d = 3 in their statement, the route is partially circular.

**Independence.** Substrate-level. Independent of routes 2.1 (representation) and 2.2 (PDE/kernel). Partially overlapping with route 2.4 (also substrate-level), but the load-bearing content is different (motif viability vs. T19/T20 internal consistency).

### 2.4 T19/T20 Internal-Consistency Route (substrate-level, structural)

**Architectural principle.** T19 derives Newton's law via cumulative-strain reading + holographic participation-count bound on a 2-sphere boundary, forcing G = c³ℓ_P²/ℏ. T20 derives a₀ = c·H₀/(2π) via dipole-mode azimuthal periodicity on the cosmic horizon's projection. Both derivations use d = 3-specific geometric facts: a 2-sphere holographic boundary (T19) and 2π azimuthal periodicity on a (d−1) = 2-sphere horizon projection (T20). The framework cannot host its own substrate-gravity arc in d ≠ 3.

**What forcing would mean.** Internal-consistency forcing: d = 3 is required for the framework to be self-supporting. Not an axiom-level forcing but a structural one — ED at d ≠ 3 cannot reproduce the gravitational phenomenology its own substrate produces at d = 3.

**Dimension-sensitive parts.**
- T19 holographic bound: surface scales as ℓ_P^(d−1) · A_(d−1) where A_(d−1) is the area of the (d−1)-sphere boundary. The strain-reading-to-Newton derivation uses the d = 3 specific scaling 4πr². In d-spatial, the analogous bound yields a different "G" with different dimensions; whether it is compatible with the strain-reading derivation needs explicit audit.
- T20 dipole-mode geometry: 2π azimuthal periodicity assumes a 2-sphere horizon projection. In d-spatial, the cosmic horizon is a (d−1)-sphere; the dipole-mode geometry generalizes formally but the 2π factor is specific to d = 3.

**Dimension-agnostic parts.**
- The cumulative-strain reading mechanism (T19) and the chain-stability landscape (Combination Rule, T21) are formulated at substrate level without explicit d-dependence in their primitive statements. The dimensional sensitivity enters when these are coarse-grained against geometric boundaries.

**In inventory.**
- T19, T20, ED Combination Rule, T21: [`theorems/T19.md`](../../theorems/T19.md), [`theorems/T20.md`](../../theorems/T20.md), [`theorems/T21.md`](../../theorems/T21.md)
- Substrate gravity paper: [`papers/ED_substrate_gravity_foundations/`](../../papers/ED_substrate_gravity_foundations/)
- ED Combination Rule memo: [`arcs/arc-SG/ED_combination_rule.md`](../../arcs/arc-SG/ED_combination_rule.md)

**What still needs derivation.**
- Explicit dimensional audit of T19's holographic-bound derivation in arbitrary d. Show that the d ≠ 3 generalization either (a) yields a dimensionally inconsistent "G", or (b) breaks the strain-reading link, or (c) admits a d-dependent G with no constraint to ℏ. Any of (a)–(c) is internal-consistency forcing of d = 3.
- Explicit dimensional audit of T20's dipole-mode derivation in arbitrary d. The 2π factor is the obvious load-bearing dimension-specific element.
- Verification that substrate primitives feeding T19/T20 are themselves d-agnostic at primitive statement level (overlap with route 2.3's same audit).

**Independence.** Conditional. If the substrate primitives feeding T19/T20 are d-agnostic at the primitive level, route 2.4 is genuinely independent forcing (the framework forces d = 3 via internal consistency of its own gravity arc). If those primitives presuppose d = 3, the route is partially circular but still valuable as a coherence check. The conditional independence is documented; not a fatal weakness.

---

## 3. Cross-Route Dependencies

### Layer distribution

| Route | Layer | Independent? |
|---|---|---|
| 2.1 Cl(3,1) | Representation (spinor bundle) | Derivative of R.2.4; PDE-level extension is the load-bearing step |
| 2.2 Huygens | PDE / kernel | Fully independent of 2.1, 2.3, 2.4. Strongest standalone PDE-level route |
| 2.3 Motif viability | Substrate (combinatorial) | Independent of 2.1, 2.2; partial overlap with 2.4 |
| 2.4 T19/T20 consistency | Substrate (geometric) | Conditional independence relative to substrate primitives' d-status |

### Dependency edges and collapse modes

- **R.2.4 → 2.1.** If the PDE↔spinor-bundle inseparability argument fails, 2.1 collapses to "spinor sector forced; PDE sector independent."
- **T18 sharp-Huygens dependency → 2.2.** If T18's derivation tolerates Hadamard interior-supported retardation, 2.2 dies entirely. *Single point of failure for the only purely-PDE-level route.*
- **P04 / chain / participation-measure d-agnosticism → 2.3 and 2.4.** If any of these primitives presuppose d = 3 at primitive-statement level, 2.3 becomes partially trivial (motifs require d = 3 because primitives say so) and 2.4 becomes partially circular. Shared dependency.
- **T20 dipole-mode lower bound → 2.3 lower bound articulation.** Route 2.3's d ≥ 3 half depends on T20's d ≤ 2 incompatibility. Substrate-internal cross-link.

### Concordance picture

The routes span three layers; concordance across layers is the goal.

- **All four close →** B2 is overdetermined. D = 3+1 forced from representation, PDE, substrate-combinatorial, and substrate-geometric layers independently. Strongest possible result.
- **2.2 + (2.3 ∧ 2.4) close →** PDE-level + substrate-level concordance; 2.1 demoted to "spinor sector confirmation." Strong result.
- **Only 2.3 + 2.4 close →** substrate-level forcing only; D = 3+1 forced via internal consistency but not from PDE structure or representation theory standalone. Closes B2 in the substrate sense but the original B2-PDE question remains open. Reported honestly.
- **Only 2.1 closes →** dimensionality remains an external input at PDE level; spinor sector confirmed Cl(3,1). B2-PDE remains open.
- **Only 2.2 closes →** odd d ≥ 3 forced at PDE level; combined with motif viability informally → d = 3. PDE-level B2 closed.
- **None close →** dimensionality is an external input across all available layers. B2 negatively closed. NS-2 still proceeds but without dimensional-forcing structural backing (per the roadmap's PERMITTED-but-not-FORCED branch).

---

## 4. What NS-1 Must Deliver

NS-1 closes when the following are produced:

1. **Verdict on each of the four routes:** FORCED / PERMITTED-but-not-FORCED / REFUTED / REDUCED-to-X. The REDUCED case names the residual structural question (e.g., "T18 audit yields sharp-Huygens dependency conditional on participation-measure tightness; reduces to that tightness question").
2. **B2 verdict.** One of:
   - D = 3+1 FORCED (any route ≥ one layer closes affirmatively)
   - D = 3+1 PERMITTED-but-not-FORCED (no route closes; dimensionality is external input)
   - D = 3+1 REFUTED (any route forces a different D — major structural surprise; would force re-examination of R.2.4)
3. **Layer-attribution statement.** Which architectural layer(s) carry the forcing. This matters for the two-source/three-source/four-source phrasing in any downstream paper.
4. **Hand-off to NS-2.** Dimensional-forcing result in a form usable by substrate→NS coarse-graining: specifically, confirmation (or failure) that the substrate→continuum coarse-graining is well-posed at d = 3+1 and pathological / undefined at d ≠ 3+1. NS-2 needs this to safely assume d = 3+1 in the form-derivation step without re-litigating dimensionality.
5. **Sensitivity flags.** Any primitive whose dimensional status is load-bearing for a closed route is added to the program-level sensitivity-flag list (joining P09 U(1)-only, P04 bandwidth-additivity, P13 continuous-time, etc.).

---

## 5. Inventory Status

### Already in repo (assets)

| Asset | Location | Used by route |
|---|---|---|
| Seven PDE-uniqueness axioms | [`docs/ED_Accomplishments.md`](../../docs/ED_Accomplishments.md), [`theory/PDE.md`](../PDE.md) | All routes (frame the question) |
| R.2.4 (Cl(3,1) on spinor bundle) | [`arcs/arc-B/arrow_implications.md §5.1`](../../arcs/arc-B/arrow_implications.md) | 2.1 |
| R.2.2 / R.2.3 (spin ladder, anyon prohibition; uses D=3+1 as input) | [`arcs/arc-B/arrow_catalogue.md §5.3`](../../arcs/arc-B/arrow_catalogue.md) | 2.1 (context) |
| T18 (V1 kernel retardation, kernel arrow) | [`theorems/T18.md`](../../theorems/T18.md), [`arcs/arc-B/`](../../arcs/arc-B/) | 2.2 |
| T19 (Newton's law, holographic participation-count bound, ℓ_P) | [`theorems/T19.md`](../../theorems/T19.md) | 2.4 |
| T20 (a₀, dipole-mode mechanism) | [`theorems/T20.md`](../../theorems/T20.md) | 2.4, 2.3 lower bound |
| ED Combination Rule, T21 (BTFR slope-4) | [`arcs/arc-SG/ED_combination_rule.md`](../../arcs/arc-SG/ED_combination_rule.md), [`theorems/T21.md`](../../theorems/T21.md) | 2.4 (context) |
| Substrate gravity paper | [`papers/ED_substrate_gravity_foundations/`](../../papers/ED_substrate_gravity_foundations/) | 2.4 |
| Companion roadmap | [`theory/Navier_Stokes_Roadmap_Scoping.md`](../Navier_Stokes_Roadmap_Scoping.md) | NS-1 framing |
| ED-Phys-39 (4D case barely architectural) | Location to be confirmed (referenced in user working notes) | 2.3 |

### Must be produced in NS-1

| Memo | Title | Route | Status |
|---|---|---|---|
| NS-1.01 | PDE↔spinor-bundle dimensional consistency audit | 2.1 | not started |
| NS-1.02 | T18 sharp-Huygens dependency audit | 2.2 | not started |
| NS-1.03 | Substrate motif factorial dilution + concentration of measure: primitive-level derivation + d ≥ 3 lower bound | 2.3 | not started |
| NS-1.04 | T19/T20 dimensional sensitivity audit | 2.4 | not started |
| NS-1.05 | Cross-route concordance synthesis + B2 verdict | (synthesis) | not started |

---

## 6. Risk Assessment

### Primary stall risk: route 2.2 (T18 audit)

The T18 sharp-Huygens audit is the single most consequential move in NS-1 because it determines whether *any* purely PDE-level forcing route exists. Outcome is binary:

- T18 requires sharp Huygens → 2.2 closes; PDE-level forcing of odd d ≥ 3.
- T18 tolerates Hadamard interior-supported retardation → 2.2 dies; PDE-level B2 closed only if 2.1's PDE↔spinor-bundle propagation can be made to carry the load (uncertain).

If 2.2 dies and 2.1 cannot be strengthened, B2-PDE remains open and the route to closure is substrate-level only.

### Secondary risk: route 2.1 (PDE↔spinor-bundle propagation)

The propagation argument (R.2.4 → PDE-level Cl(3,1)) may simply not exist. The spinor bundle and the PDE may be structurally independent strata. If so, 2.1 closes only the spinor sector and contributes nothing to PDE-level B2.

### Substrate-route risks (2.3 and 2.4)

- **Primitive d-agnosticism.** If P04, chain primitive, or participation-measure primitives presuppose d = 3 in their statements, routes 2.3 and 2.4 become partially trivial / circular. The audit must verify primitive-level d-agnosticism before claiming route 2.3 or 2.4 forcing.
- **Heuristic vs. derivation.** "C(d) ~ 1/d!" must be replaced with a primitive-anchored derivation (concentration-of-measure on participation-measure setup is the most likely formal foundation). Without that anchor, route 2.3 is a heuristic, not a forcing argument.
- **Lower-bound under-articulation.** Route 2.3 currently has no articulated d ≥ 3 lower bound; it borrows from T20 (d = 2 incompatibility) and chain-primitive-collapse (d = 1 incompatibility). Both need explicit memos.

### What is *not* a risk for NS-1

- **The Clay smoothness question.** That is NS-3, not NS-1. NS-1 is pure structural / axiom-level analysis.
- **Continuum-limit machinery.** Not needed for NS-1.
- **Substrate→NS coarse-graining mechanics.** That is NS-2.

NS-1 is, comparatively, a low-risk arc. The four-route structure is overdetermined: even if 2.2 dies, partial closure (2.3 ∨ 2.4) gives substrate-level forcing and a PERMITTED-but-not-FORCED B2-PDE verdict, which is still a definitive answer to the open question.

---

## 7. Summary

Four routes spanning three architectural layers:

- **2.1 Cl(3,1)** — representation-theoretic; derivative of R.2.4; needs PDE-spinor-bundle propagation argument.
- **2.2 Huygens** — PDE/kernel-level; standalone; hinges on T18 sharp-Huygens dependency audit (binary outcome). *Strongest standalone PDE-level candidate.*
- **2.3 Motif viability** — substrate-combinatorial; provides d ≤ 3 upper bound; needs primitive-level derivation of dilution + d ≥ 3 lower bound articulation.
- **2.4 T19/T20 consistency** — substrate-geometric; internal-consistency forcing of d = 3 via existing closed substrate-gravity work; conditional on primitive d-agnosticism.

Concordance across layers is the goal. Three of four closing → B2 overdetermined. NS-1 closes either way: FORCED / PERMITTED-but-not-FORCED / REFUTED, with layer-attribution. Hand-off to NS-2 is the d = 3+1 forcing verdict in form usable by substrate→NS coarse-graining.

---

## 8. Recommended Next Steps

In strict priority order. Execute steps 1 and 2 first because they have the highest value-per-effort and resolve the binary status of the only purely-PDE-level route.

1. **Audit T18's sharp-Huygens dependency (route 2.2 load-bearing check).** Open [`theorems/T18.md`](../../theorems/T18.md) and [`arcs/arc-B/`](../../arcs/arc-B/) V1 retardation memos. Question: does the kernel-arrow derivation require *cone-supported* (sharp Huygens) retardation, or does it tolerate *interior-supported* (Hadamard) retardation? Binary outcome. *Highest priority because the verdict determines whether any purely PDE-level forcing route exists.*

2. **Draft Memo NS-1.02 with the verdict from step 1.** File: `theory/Navier Stokes/NS-1.02_Huygens_T18_Audit.md`. If sharp-Huygens dependency is established → route 2.2 closes; PDE-level forcing of odd d ≥ 3 documented. If not → route 2.2 dies; documented honestly.

3. **Draft Memo NS-1.04 (T19/T20 dimensional sensitivity audit).** File: `theory/Navier Stokes/NS-1.04_T19_T20_Dimensional_Audit.md`. Walk through T19's holographic-bound derivation in arbitrary d-spatial; identify where the 4πr² (d = 3) scaling becomes load-bearing. Walk through T20's dipole-mode derivation in arbitrary d; identify where the 2π factor is dimension-specific. Verdict: how strongly does internal consistency of the substrate-gravity arc force d = 3? Conditional on primitive d-agnosticism (audit needed).

4. **Draft Memo NS-1.03 (substrate motif viability + lower bound).** File: `theory/Navier Stokes/NS-1.03_Substrate_Motif_Viability.md`. Two subsections: (a) primitive-level derivation of factorial dilution / concentration of measure — identify which primitive (P04? participation-measure construction?) generates the dilution and write the explicit derivation, replacing the heuristic C(d) ~ 1/d! with a formal anchor; (b) d ≥ 3 lower bound articulation, citing T20 dipole-mode degeneracy at d = 2 and chain-primitive collapse at d = 1.

### Prerequisites and checks

- **Verify [`theorems/T18.md`](../../theorems/T18.md) exists** and contains the V1 retardation derivation in usable form. If only the arc-B memos contain the actual derivation, work from those directly.
- **Confirm location of ED-Phys-39** (referenced in user notes; not yet sighted in repo). If absent from current repo, work from the seven PDE-uniqueness axioms + substrate primitives directly without ED-Phys-39 as a foundation.
- **Audit primitive d-agnosticism.** Before claiming route 2.3 or 2.4 forcing, confirm that P04, chain primitive, and participation-measure primitives are stated d-agnostically at primitive-statement level. This is a small audit (one short memo or an appendix in NS-1.03).
- **Do not open NS-2 until at least one of routes 2.1–2.4 delivers a definite verdict.** NS-2 (substrate→NS coarse-graining) needs the dimensional-forcing result as input; opening it earlier risks re-litigation.

### Deferred (do after steps 1-4)

5. Memo NS-1.01 (PDE↔spinor-bundle propagation audit). Lowest urgency because route 2.1 is derivative and the most consequential question (does the PDE-level route exist) is settled by step 1.

6. Memo NS-1.05 (synthesis + B2 verdict). Last; it depends on outcomes of steps 1-4.

---

*Maintained at [`theory/Navier Stokes/Dimensional_Forcing_B2_Scoping.md`](Dimensional_Forcing_B2_Scoping.md). Update as routes close.*
