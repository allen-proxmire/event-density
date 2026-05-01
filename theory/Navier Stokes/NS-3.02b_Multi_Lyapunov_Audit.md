# NS-3.02b — Multi-Lyapunov Audit (Addendum to R2)

**Date:** 2026-04-30
**Status:** Audit complete. **Headline: the multi-Lyapunov audit does not strengthen NS-3 toward Path C+. Of the five independent Lyapunov functionals admitted by the canonical ED PDE, only the energy-class ones transfer cleanly to NS under the partial-vector-extension structure; the gradient-norm functional — which would deliver BKM-class strength if it transferred — is broken specifically by the advective convective derivative $(v \cdot \nabla)v$. This is structurally illuminating: the Clay smoothness question is equivalent, in the ED framing, to "the vector-extension of the gradient-norm Lyapunov is broken by the advective fluid-mechanical-addition." Same Intermediate verdict as NS-3.04, with the reason now sharpened.**
**Sources:** [`theory/PDE.md`](../PDE.md) §5 (five Lyapunov functionals statement), [`theory/Architectural_Canon.md`](../Architectural_Canon.md), [`Navier Stokes/NS-3.02_Holographic_Global_Bound.md`](NS-3.02_Holographic_Global_Bound.md), [`Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md), [`Navier Stokes/NS-3.04_Synthesis_Path_Verdict.md`](NS-3.04_Synthesis_Path_Verdict.md).

---

## 1. Purpose

NS-3.02 closed Route R2 with a clean failure: the holographic bound translates to a Leray-equivalent energy bound, not a BKM-class gradient bound. That audit treated the energy bound as the only Lyapunov-class bound available from ED.

But [`PDE.md`](../PDE.md) §5 explicitly states: *"The PDE admits five independent Lyapunov functionals (energy, mobility-weighted variance, penalty integral, gradient norm, L² norm), all monotonically decreasing along trajectories. The system is not a single gradient flow."*

NS-3.02 audited the energy-class one and stopped. The remaining four — and specifically the *gradient norm* — were not audited. The gradient norm is structurally the most relevant: it is enstrophy-class ($\int |\nabla v|^2$ ↔ enstrophy $\int |\omega|^2$ for vector NS), and a monotonically-decreasing enstrophy-class bound for 3D NS would close the Clay smoothness question affirmatively.

This memo executes the missing audit: under the partial-vector-extension of ED to NS (per NS-2.08), which of the five Lyapunov functionals transfer with their monotonicity intact, and do any reach BKM-class strength?

The answer is decisive but negative for Path C+, with a structurally illuminating reason.

---

## 2. The Five Lyapunov Functionals

[`PDE.md`](../PDE.md) §5 names five independent Lyapunov functionals admitted by the canonical ED PDE:

| # | Functional | Schematic form | Class |
|---|---|---|---|
| L1 | Energy | $\int E(\rho)\,dV$ | Energy-class |
| L2 | Mobility-weighted variance | $\int M(\rho)|\rho - \bar\rho|^2\,dV$ | Variance-class |
| L3 | Penalty integral | $\int \mathcal{P}(\rho)\,dV$, where $\mathcal{P}' = P$ | Equilibrium-distance-class |
| L4 | Gradient norm | $\int |\nabla\rho|^2\,dV$ | $H^1$-class / enstrophy-class for vector |
| L5 | $L^2$ norm | $\int \rho^2\,dV$ | Energy-class |

All five are monotonically decreasing along trajectories of the *canonical scalar PDE* per the canon. The audit question for NS: do they remain monotonically decreasing under the *vector-extended* NS structure that includes the advective convective derivative, pressure-coupling, and incompressibility constraint?

---

## 3. Audit Per Functional Under Vector-Extended NS

For each functional, evaluate transfer to NS via the vector-extended construction (NS-2.08 §5).

### 3.1 L1 (Energy) — transfers; gives Leray

For NS, the energy functional is $E(t) = \frac{1}{2}\int \rho |v|^2 dV$. Standard NS analysis (Leray): $\frac{dE}{dt} = -\nu \int |\nabla v|^2 dV + \int \rho \mathbf{v} \cdot \mathbf{f}^\mathrm{ext} dV$. The advective term $(v \cdot \nabla)v$ contributes zero to $\frac{dE}{dt}$ in incompressible flow (transport doesn't change L² norm); pressure gradient contributes zero by incompressibility; viscous term gives $-\nu \int|\nabla v|^2 \le 0$.

**Verdict for NS:** L1 transfers cleanly. Monotonicity preserved (in absence of forcing). **Gives Leray's energy inequality.** Already covered by NS-3.02; not new.

### 3.2 L2 (Mobility-weighted variance) — transfers; energy-class

For NS, mobility-weighted variance is $\int M(\rho_\mathrm{fluid}) |v_i - \bar v_i|^2 dV$ — viscosity-weighted spatial variance of velocity. With constant viscosity (Newtonian fluid), this reduces to a constant times the energy variance, which is energy-class. With $M$ depending on shared $\rho_\mathrm{fluid}$, the time-derivative analysis closely tracks L1's energy derivation; monotonicity preserved.

**Verdict for NS:** L2 transfers cleanly. **Energy-class strength; no improvement over Leray.** Does not reach BKM.

### 3.3 L3 (Penalty integral) — does not apply to incompressible NS; partial application to compressible

The penalty channel maps cleanly only to *density-equilibrium relaxation* in compressible NS (per NS-2.08 §4.2), not to incompressible velocity dynamics. For incompressible NS where the penalty channel doesn't apply, the L3 functional has no direct counterpart on velocity. For compressible NS, L3 would bound the penalty integral $\int \mathcal{P}(\rho_\mathrm{fluid}) dV$ — bounds how far fluid density has moved from equilibrium under the penalty.

**Verdict for NS:** L3 does not bound velocity gradients. For incompressible NS: doesn't apply. For compressible NS: bounds density excursions, not velocity. **Does not reach BKM.**

### 3.4 L4 (Gradient norm / enstrophy) — does NOT transfer in 3D NS

This is the load-bearing case. The gradient-norm functional applied component-wise to NS is:

$$L4_\mathrm{NS}(t) = \sum_i \int |\nabla v_i|^2\,dV = \int |\nabla v|^2\,dV.$$

This is precisely the enstrophy-class quantity (related to enstrophy $E_\Omega = \frac{1}{2}\int|\omega|^2 dV$ via integration by parts and incompressibility). A monotonically-decreasing enstrophy bound on NS solutions in 3D would imply BKM-class L² control of vorticity — and combined with standard regularity arguments, would close the Clay smoothness question affirmatively.

**The audit question:** does L4's monotonicity, established for the canonical ED PDE per [`PDE.md`](../PDE.md) §5, transfer to vector-extended NS?

**Time derivative analysis.** Compute $\frac{dL4_\mathrm{NS}}{dt}$ under NS dynamics. Using $\partial_t v_i = -(v \cdot \nabla)v_i - \frac{1}{\rho}\partial_i p + \nu \nabla^2 v_i + f_i^\mathrm{ext}$:

$$\frac{d}{dt}\int |\nabla v|^2 dV = 2 \int \nabla v_i \cdot \nabla(\partial_t v_i) dV.$$

The four contributions:
- **Viscous term** $\nu \nabla^2 v_i$: contributes $-2\nu \int |\nabla^2 v|^2 dV \le 0$ — *decreasing* contribution.
- **Pressure term** $-\partial_i p / \rho$: contributes zero in incompressible flow with constant ρ (integration by parts + ∇·v = 0).
- **External forcing** $f_i^\mathrm{ext}$: contributes a $\int \nabla v_i \cdot \nabla f_i^\mathrm{ext}$ term; sign depends on forcing structure.
- **Advective term** $-(v \cdot \nabla)v_i$: this is the load-bearing contribution. Direct calculation gives:
$$\frac{d}{dt}\bigg|_\mathrm{advective}\!\!\int |\nabla v|^2 dV = -2 \int (\nabla v_i)(\nabla v_j)(\partial_j v_i) dV = -2\int |\nabla v|^2 (\nabla \cdot v) dV - 2\int (\partial_j v_i)(\partial_i v_k)(\partial_k v_j) dV.$$

In incompressible flow ($\nabla \cdot v = 0$), the first term vanishes. The remaining triple-product term — the **vortex-stretching term** — does *not* have a fixed sign. In 3D it is generically positive, *increasing* L4. In 2D it vanishes identically (vortex stretching is a 3D phenomenon).

**Verdict on L4 transfer to 3D NS:**

$$\frac{dL4_\mathrm{NS}}{dt} = -2\nu \int |\nabla^2 v|^2 dV \;-\; 2\int (\partial_j v_i)(\partial_i v_k)(\partial_k v_j) dV \;+\; (\mathrm{forcing\ terms}),$$

with the first term ≤ 0 (viscous dissipation, monotonically decreasing) and the second term *of indefinite sign in 3D*. **L4's monotonicity is broken in 3D NS specifically by the advective convective derivative's vortex-stretching term.** In 2D the term vanishes and L4 transfers cleanly (consistent with global existence in 2D NS). In 3D the term can dominate viscous dissipation and L4 can grow.

**This is exactly the standard NS difficulty — the vortex-stretching term in 3D — recast in ED-Lyapunov language.**

### 3.5 L5 ($L^2$ norm) — transfers; energy-class

$L5_\mathrm{NS} = \int |v|^2 dV$ — total $L^2$ norm of velocity, which is essentially $L1$ up to a factor of ρ (constant in incompressible flow). Same analysis as §3.1: transfers cleanly, gives Leray-class bound, does not reach BKM.

**Verdict for NS:** L5 transfers. Energy-class. No improvement over Leray.

---

## 4. Aggregate Verdict

| Functional | Transfers to NS? | Strength |
|---|---|---|
| L1 (energy) | Yes | Leray-class |
| L2 (mobility-weighted variance) | Yes | Energy-class (Leray-like) |
| L3 (penalty integral) | Only compressible density; not velocity | N/A for velocity gradient |
| **L4 (gradient norm)** | **No in 3D — broken by advective vortex-stretching** | Would be BKM-class if it transferred |
| L5 ($L^2$ norm) | Yes | Energy-class (Leray-like) |

**Of the five Lyapunov functionals, four transfer to NS but at energy-class strength (Leray-equivalent or weaker for L3); the one that would deliver BKM-class strength (L4 gradient norm) does NOT transfer in 3D because the advective convective derivative breaks its monotonicity.**

**NS-3 verdict unchanged:** Intermediate. Multi-Lyapunov audit does not strengthen toward Path C+.

---

## 5. The Structurally Illuminating Finding

The negative result is structurally informative.

NS-2.08 §5 identified three NS structural features that lie *outside* the canonical ED architecture: pressure-as-Lagrange-multiplier, advective convective derivative, and incompressibility constraint. NS-2.08 §6 catalogued these as "fluid-mechanical-specific additions" not derivable from ED PDE channels.

This audit reveals: **of the three fluid-mechanical-additions, the advective convective derivative is *specifically* the one that breaks the gradient-norm Lyapunov.** Pressure (in incompressible flow) doesn't break L4; it contributes zero by integration by parts + incompressibility. Incompressibility itself doesn't break L4; it actually *helps* (it removes the $\int|\nabla v|^2 (\nabla \cdot v)$ contribution that would otherwise add another sign-indeterminate term).

**The advective term alone, via its vortex-stretching content in 3D, is what prevents ED's gradient-norm Lyapunov from delivering Clay-NS smoothness.**

This recasts the Clay smoothness question in ED-architectural terms:

> *The Clay smoothness question is equivalent to: "Can the advective fluid-mechanical-addition's vortex-stretching content be controlled by ED's substrate-scale stabilization (ℓ_P² ∇⁴ v from R1) before it overwhelms viscous dissipation and breaks the gradient-norm Lyapunov?"*

This is not a new mathematical statement — it is the standard framing of the Clay difficulty (vortex stretching in 3D vs. viscous regularization). What it provides is **ED-architectural language** for the same question: the obstruction to Path C+ closure is *exactly* the structural feature (advective term) that NS-2.08 already identified as non-ED-architectural.

The two findings are mutually reinforcing:

- **NS-2.08 §5 (architectural framing):** advection is a fluid-mechanical-addition not native to ED architecture.
- **NS-3.02b (this memo, dynamical framing):** advection is the specific obstruction to ED's gradient-norm Lyapunov delivering BKM-class strength.

Both point to the same structural feature, from different angles. **The advective term is where ED's architectural reach ends and fluid-mechanical-specific structure begins.** Resolving Clay-NS within ED would require either (a) extending ED architecture to absorb advection canonically, or (b) showing that R1's substrate-scale stabilization controls advection's vortex-stretching content quantitatively despite advection being non-architectural.

Neither (a) nor (b) is supplied by the multi-Lyapunov analysis directly; the analysis sharpens what would be needed.

---

## 6. What This Changes for NS-3 Verdict

**The aggregate NS-3 verdict (Intermediate) is unchanged.** The multi-Lyapunov audit closes another candidate Path-C+ route (the one I missed in NS-3.02) and confirms the route fails in 3D — which is consistent with the standard difficulty of Clay-NS.

**What the audit adds:**

- **Sharpens the obstruction.** NS-3.04 §5 framed the Intermediate verdict as "ED contains a real Clay-relevant mechanism but doesn't unconditionally guarantee smoothness due to inherited quantitative competition." This audit identifies the obstruction more precisely: it is the advective convective derivative's vortex-stretching content in 3D.
- **Connects NS-2.08 + NS-3 verdicts structurally.** The fluid-mechanical-addition that NS-2.08 identified as non-ED-architectural is the same structural feature that NS-3.02b identifies as breaking the Lyapunov-class Path-C+ route.
- **Refines the "three identification gaps" from NS-3.04 §7.** A fourth candidate path-to-Path-A-promotion is now identifiable: a substrate-level argument that ED's R1 stabilization *specifically* controls advective vortex-stretching, beyond the "dominates Burnett-class" framing already in NS-3.04 §7.1.

**What the audit does not add:** a closer-to-Path-C+ verdict. NS-3 remains Intermediate.

---

## 7. Recommended Next Steps

In priority order. This memo is an addendum to NS-3 closure; main NS roadmap work continues per NS-3.04 §9 / Architectural_Canon_Vector_Extension.md §8.

1. **Update NS-3.04 §6 verdict text and §7 identification-gap list** with the multi-Lyapunov audit's sharper obstruction framing. Specifically: add a fourth identification gap to §7 — "(R5) Substrate-level argument that ED's R1 stabilization controls advective vortex-stretching content in 3D NS" — parallel in character to the existing three gaps. This makes NS-3.04 reflect the full audit, not just R1/R2/R3. Editorial pass; no verdict change.

2. **Mention this audit in any external-facing material** (NS synthesis paper, public explainer). The structural finding — that the Clay obstruction equals the non-ED fluid-mechanical-addition — is genuinely new framing and worth communicating. It is a structurally clean way to articulate why Clay-NS is hard, in ED-architectural language.

3. **Flag for future Arc-D-class follow-on:** vortex-stretching control via substrate-scale regularization is a concrete substrate-level question that could be auditable independent of full Path A B2 promotion. Arc D's diffusion-limit machinery may or may not address it; speculative connection. Not load-bearing for current work; recorded for tracking.

4. **No additional NS-3 audit memos needed.** With L1, L2, L3, L4, L5 all examined, the multi-Lyapunov question is closed. The other three *unexamined* substrate-level-stabilization candidates I flagged in the prior conversation (triad coupling P7 ↔ turbulence; non-Newtonian via P4 saturation; configuration-space derivation via compositional rule directly) remain available as separate optional follow-ons but are not omissions in the same way — they are net-new directions, not missing pieces of NS-3 audit.

### Decisions for you

- **Confirm NS-3 verdict unchanged at Intermediate.** Multi-Lyapunov audit closes a route I should have audited in NS-3.02 but didn't; the route fails for the same structural reason that makes Clay hard. NS-3.04 verdict text stands; obstruction now sharpened.
- **Confirm structural finding worth communicating externally** (advective term = non-ED architectural addition = specific Clay obstruction). Not new mathematics; new ED-architectural framing of standard difficulty.
- **Confirm no further NS-3 audits needed** at the multi-Lyapunov level. Other candidate ED-routes-into-NS (turbulence P7, non-Newtonian P4, compositional rule direct) are net-new directions, not missing audits.

---

*NS-3.02b multi-Lyapunov audit. Of five Lyapunov functionals, four transfer to NS at energy-class strength (Leray-equivalent); the gradient-norm functional (which would deliver BKM-class) is broken in 3D specifically by the advective vortex-stretching term. NS-3 verdict unchanged at Intermediate. Structural finding: the advective convective derivative — identified in NS-2.08 as a fluid-mechanical-addition not native to ED architecture — is the same structural feature that breaks the gradient-norm Lyapunov, sharpening the Clay obstruction in ED-architectural language. Mutually reinforcing with NS-2.08 and NS-3.04 findings; closes the omission flagged in the prior conversation.*
