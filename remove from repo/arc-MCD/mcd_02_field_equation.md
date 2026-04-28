# MCD.2 — Field Equation for T from the Many-Chain Action

**Date:** 2026-04-27
**Arc:** Many-Chain Dynamics — third memo (variational derivation)
**Status:** Variational derivation of the field equation for T from the unified single-chain action embedded in the A4 Lagrangian framework. **Result: under the standard Lagrangian construction with quadratic kinetic term and quadratic potential, the field equation for T is linear**. The self-consistent activity coupling (BTFR.08-style) modifies the kernel structure (cancels the cylindrical-curvature term under the Einstein-like relation) but does not introduce genuine nonlinearity in T. **Many-chain coupling alone does not produce a nonlinear field equation**: the field equation is linear in T given the chain configuration, even though the full dynamical system (chains + field) is nonlinear in chain-configuration. **The DM-arc linearity wall therefore reappears at this stage of MCD**. Nonlinearity in the field equation requires explicit structural commitments not present in ED-07: either a non-quadratic kinetic term (MOND-style μ(|∇T|²) modification), a non-quadratic potential V(T), or a tensor-gravity construction beyond the slow-time scalar approximation. **Provisional verdict: MCD's single-chain principle is GR-equivalent (as established in MCD.1); its many-chain limit under the standard Lagrangian construction is canonical-ED-equivalent (linear screened-Poisson). The pivot point identified in MCD.0 §6.3 (whether the many-chain limit is nonlinear) resolves to "linear, by construction, unless additional structural commitments are made."** The arc continues to MCD.3 to determine whether a structurally-motivated commitment exists, or whether MCD must close with refutation.
**Predecessor:** MCD.1 (candidate-action survey; A1.c+A5 unified, A4 framework selected).
**Successor:** MCD.3 (many-chain coupling; structural test for whether nonlinearity can be derived rather than postulated).

---

## 1. The Lagrangian construction

### 1.1 The total action

Combining the A1.c chain action with the A4 field-theoretic framework:

> **S = S_chain + S_field + S_coupling**

with:

- **S_chain** = sum over chains i of `−m_i · c² · ∫(1 − T(γ_i(t))) dt` (single-chain proper-time-like action)
- **S_field** = `∫d⁴x · [(1/2)(∇T)² − V(T)]` (kinetic + potential for T)
- **S_coupling** = `∫d⁴x · [−κ_act · A(x, T)]` (activity-coupling term)

Each chain i has worldline γ_i(t) and rest mass m_i. The field T(x) is the slow-time field, dimensionless. V(T) is a potential function to be specified. A(x, T) is the activity functional, possibly dependent on T through self-consistent coupling to v_T.

### 1.2 Lagrangian density form

The chain action can be rewritten as a spacetime integral using delta functions:

> S_chain = −Σ_i m_i c² ∫d⁴x · δ³(x − γ_i(t)) · (1 − T(x)) · (1/γ_Lorentz_i)

In the non-relativistic limit (γ_Lorentz_i ≈ 1):

> S_chain ≈ −Σ_i m_i c² ∫d⁴x · δ³(x − γ_i(t)) + Σ_i m_i c² ∫d⁴x · δ³(x − γ_i(t)) · T(x)
>        = −M_total · c² · t_total + c² · ∫d⁴x · ρ_chain(x) · T(x)

where ρ_chain(x) = Σ_i m_i · δ³(x − γ_i(t)) is the chain mass density. The first term is constant (total rest mass over total time) and drops out of the variational principle. **The T-dependent part of the chain action is `c² · ∫d⁴x · ρ_chain(x) · T(x)`.**

This is the structurally important consequence of the single-chain action: in the non-relativistic limit, **chains source T through their mass density**, with coupling strength c². This is structurally equivalent to standard scalar-gravity coupling.

### 1.3 The total Lagrangian density

Combining all terms:

> **L = (1/2)(∇T)² − V(T) − κ_act · A(x, T) + c² · ρ_chain(x) · T(x)**

(Up to the constant ρ_chain·c² term that does not contribute to variation.)

The sign of the chain-source term is positive in front of T, meaning chains *increase* T in their vicinity (chains are sources of slow-time, or equivalently, slow-time accumulates near mass).

---

## 2. Euler-Lagrange derivations

### 2.1 Chain equation of motion

Variation with respect to chain coordinate γ_i(t) (treating T(x) as external):

> δS / δγ_i = 0    ⟹    m_i · γ̈_i = −m_i · c² · ∇T(γ_i)

This is the slow-time Newton-equivalent equation:

> **a_chain = −c² · ∇T**.

Sign convention: T larger near matter ⟹ ∇T points away from matter ⟹ a_chain points toward matter (attractive). This recovers the standard ED-07 §5.3 picture: **chains accelerate in the direction that minimizes their participation strain**, which in the slow-time interpretation is toward higher T (slower-time regions, equivalent to deeper gravitational wells).

In the relativistic regime, the same derivation produces the geodesic equation in the slow-time metric `g_μν(T)`. This is the GR-3A eikonal-limit result, recovered as expected. **The chain equation of motion confirms MCD.1's finding that the single-chain principle is GR-equivalent.**

### 2.2 Field equation for T (variation of the field)

Variation with respect to T(x) (treating ρ_chain and the kinematic part of A as external):

> **δS / δT = 0**

Term-by-term:

- **Kinetic term:** δ[(1/2)(∇T)²]/δT integrated = `−∇²T` (after integration by parts, assuming boundary terms vanish).
- **Potential term:** δ[V(T)]/δT = `V'(T)`.
- **Coupling term:** δ[κ_act · A(x, T)]/δT = `κ_act · ∂A/∂T`.
- **Chain source:** δ[c² · ρ_chain · T]/δT = `c² · ρ_chain`.

Combining (with appropriate signs from the action):

> **−∇²T − V'(T) + κ_act · ∂A/∂T + c² · ρ_chain = 0**.

Rearranging into the conventional form:

> **∇²T = −V'(T) + κ_act · ∂A/∂T + c² · ρ_chain**.   (Eq. 1)

This is the field equation for T from the MCD Lagrangian, in fully general form before specifying V or A.

---

## 3. Specifying V(T) and A(γ, T)

The form of the field equation depends critically on what we choose for V(T) and A(γ, T). Three natural choices reflect different structural commitments:

### 3.1 Quadratic potential (canonical-ED choice)

> V(T) = (1/2) · λ² · T²    ⟹    V'(T) = λ² · T.

This is the canonical-ED choice (matching the screened term `−λT` in the canonical PDE). Substituting into Eq. 1:

> **∇²T − λ² · T = κ_act · ∂A/∂T + c² · ρ_chain**.   (Eq. 2)

**This is linear in T**, modulo the form of A.

### 3.2 Quartic potential (φ⁴-style nonlinearity)

> V(T) = (1/2) · λ² · T² + (1/4) · g · T⁴    ⟹    V'(T) = λ² · T + g · T³.

This gives a nonlinear field equation:

> ∇²T − λ² · T − g · T³ = κ_act · ∂A/∂T + c² · ρ_chain.   (Eq. 3)

**Genuinely nonlinear in T**, but the cubic term is structurally unmotivated by ED-07 or any other ED arc. Adding it would be a postulate.

### 3.3 Activity coupling with self-consistent T-dependence

The DM.G/BTFR.08 self-consistent activity:

> A(x, T) = (v_baryon² + v_T²) / R²,    v_T² = R · c² · |∂_R T|.

Then `∂A/∂T` is nonzero only through v_T², and after appropriate integration:

> κ_act · ∂A/∂T → linear in ∂_R T (a divergence-like term).

This is the BTFR.08 mechanism: self-consistent activity adds a term `(κ_act · c²/R) · ∂_R T` to the LHS of the field equation, which under the Einstein-like relation `D_T = c² · κ_act` cancels the cylindrical-curvature term and produces the 2D-Cartesian Helmholtz operator. **This modifies the kernel structure but is still linear in T.**

### 3.4 The key observation

**No combination of standard V(T) (quadratic) and A(x, T) (linear in v_T²) produces a nonlinear field equation in T.** The only routes to nonlinearity are:

- **Non-quadratic V(T)** (Eq. 3-style): produces polynomial nonlinearity but is structurally unmotivated.
- **Non-quadratic kinetic term** (replacing `(1/2)(∇T)²` with `F((∇T)²)` for some non-quadratic F): produces MOND-style nonlinearity. Also structurally unmotivated.
- **Higher-derivative terms** (like `(∇²T)²`): produces fourth-order field equations. Structurally unmotivated and produces ghost-like instabilities.

**None of these are forced by ED's canonical primitives.**

---

## 4. The structural status

### 4.1 What the canonical Lagrangian construction gives

Under V(T) = (1/2)λ²T² and A linear in v_T²:

> **∇²T − λ² · T − (κ_act · c² / R) · ∂_R T = c² · ρ_chain + κ_act · v_baryon² / R²**   (Eq. 4)

(after simplification of the activity-coupling term in cylindrical coordinates, using BTFR.08-style self-consistency).

This is **linear in T**. The LHS is the modified Helmholtz operator (BTFR.08); the RHS is the source built from chain mass density plus baryonic activity.

Comparison with the canonical-ED PDE (DM.0/1, with D_T included):

> D_T · ∇²T − λ T = − S    (canonical ED)
>
> ∇²T − λ² · T = (source)    (Eq. 4 with `D_T = 1` normalization)

These are the same operator up to overall scaling and the BTFR.08 cylindrical-curvature cancellation. **MCD's many-chain field equation, under the canonical Lagrangian construction, is the same linear screened-Poisson PDE that the DM-arc treated.**

### 4.2 Why many-chain coupling does not produce nonlinearity

The chain action contributes a *linear* source `c²·ρ_chain` to the field equation, regardless of how many chains there are. Many-chain coupling enters in two places:

- **Chain dynamics:** each chain's path γ_i(t) depends on the field T, which is sourced by all other chains' positions. This is the *full* dynamical system being nonlinear in chain configurations (chains move on a field they collectively shape).
- **Field equation:** linear in T for any given chain configuration. The nonlinearity of the dynamical system is encoded in the back-reaction loop, not in the field equation itself.

**This distinction is crucial.** The DM-arc's slope-2 BTFR result followed from the linearity of the field equation, integrated over a disc-with-Keplerian-inner-region. MCD inherits this linearity at the field-equation level. The fact that the full dynamical system is nonlinear (chain configurations evolve on T which evolves with them) does not break the linearity wall: BTFR is determined by the asymptotic v_T at large R, which depends on the disc-integrated source through the linear Green's function — and the disc integration adds inner and outer contributions linearly, with inner dominance.

**MCD's many-chain limit, under the standard Lagrangian construction, reproduces the DM-arc result.**

### 4.3 What would force genuine nonlinearity

Three structural commitments could produce a nonlinear field equation:

- **(N1) Non-quadratic kinetic term.** Replace `(1/2)(∇T)²` with `F((∇T)²)` for some F whose derivative F' depends on `(∇T)²`. The variational derivative gives `∇·[F'((∇T)²) · ∇T]`, which is the MOND-style nonlinearity. Standard form: `F(x) = (1/2)x · μ(x/x_scale)` with μ → 1 for large argument and μ → √(x/x_scale) for small (giving F' → √x in deep regime, the deep-MOND limit).
- **(N2) Non-quadratic potential V(T).** As Eq. 3, with V' ∝ T^n for n > 1. Gives polynomial nonlinearity.
- **(N3) Tensor-gravity beyond weak-field.** If T is the time-time component of a metric perturbation rather than a scalar field, the full Einstein equation produces nonlinearity through the Christoffel-symbol structure. But in weak-field (galactic regime), this reduces to linear.

**None of N1, N2, N3 is forced by ED's canonical primitives or by ED-07.** Each would require an additional structural commitment.

---

## 5. Gravitational implications

### 5.1 If the field equation is linear (current verdict)

**Newtonian limit:** Eq. 4 with `λ → 0` and source `c²·ρ_chain` gives `∇²T = c²·ρ_chain`, which is Poisson's equation with `T` playing the role of the gravitational potential `Φ/c²`. Standard Newtonian gravity recovered. ✓

**GR limit:** in the eikonal regime, chains follow geodesics of the slow-time metric. Standard GR weak-field recovered. ✓

**Galactic limit:** the disc-integrated source, treated linearly, gives the DM-arc result. **Slope-2 BTFR (after self-consistency repairs C1) or slope-0.24 (without).** Either way, fails empirical slope-4. ✗

**Cluster limit:** preserved, since the cluster-scale anchor was set by D_T calibration which Eq. 4 reproduces with appropriate normalization.

### 5.2 If the field equation is nonlinear (under N1)

Adopting N1 with MOND-style F: in the deep-acceleration regime, the field equation becomes:

> `∇·[(|∇T|/T_scale) · ∇T] ∝ source`

producing the standard MOND deep-MOND derivation. The result is `v_flat⁴ = G · M_b · a₀_eq`, with `a₀_eq` derivable from `T_scale`. **Slope-4 BTFR by construction**, plus Newtonian limit at high acceleration. ✓

But this requires postulating `F`, which is structurally identical to postulating MOND's μ(x). **No theoretical advance over MOND.**

### 5.3 The structural choice

MCD faces the same epistemic choice that BTFR.07 identified:

- **Stay with the standard Lagrangian:** linear field equation, slope-2 BTFR, no theoretical advance, but minimal structural commitments.
- **Adopt N1, N2, or N3:** nonlinear field equation, potential slope-4 BTFR, but requires structural commitment that is not forced by ED's primitives — **same epistemic status as postulating MOND directly**.

---

## 6. Provisional structural verdict

> **MCD's many-chain field equation, under the canonical Lagrangian construction (quadratic V, quadratic kinetic term, BTFR.08-self-consistent activity coupling), is linear in T**.
>
> The DM-arc linearity wall therefore reappears at the field-equation level. The disc-integrated source produces M_b-linear scaling at leading order (inner-disc dominance), giving slope-2 BTFR.
>
> **MCD does not, in this construction, escape the DM-arc trap**. The single-chain principle is GR-equivalent (MCD.1 §6.1); the many-chain limit is canonical-ED-equivalent (this memo).
>
> **The arc has not yet refuted, because three structural escape routes (N1, N2, N3) remain open.** But none of these routes is forced by ED's primitives, and adopting any of them places MCD in the same epistemic position as MOND (postulated nonlinearity rather than derived).

---

## 7. Explicit assumptions

This memo's conclusions depend on the following:

| Assumption | Used in | Robustness |
|---|---|---|
| Slow-time interpretation: T dimensionless, `a = c²·∇T` | §2.1 chain equation | Standard ED-07 framing |
| Non-relativistic limit for chains | §1.2 | Galactic regime is non-relativistic; OK |
| Quadratic potential V = (1/2)λ²T² | §3.1, §4 | **Canonical assumption**; not forced by ED-07 but consistent with canonical PDE |
| Activity A linear in v_T² | §3.3 | Consistent with DM.1 / BTFR.08 |
| Continuum limit of many-chain configuration: ρ_chain smooth | §1.2, §4.2 | Standard mean-field-like; appropriate for large chain counts |
| Mean-field decoupling: chain i's motion on field T sourced by all chains | §4.2 | Standard; Vlasov-equation-equivalent |
| Boundary terms in variational derivation vanish | §2.2 | Standard; OK for compact-support field configurations |

**Conditional results:**
- The "linear in T" conclusion holds under assumption 3 (quadratic V). Adopting N1 or N2 would invalidate this.
- The "DM-arc wall reappears" conclusion holds under assumptions 3 and 4. The C1 repair via Einstein-like relation (BTFR.08 P2 reading) is still an open foundational question (BTFR.09).

**Unconditional results:**
- The chain equation of motion `a = −c²·∇T` is standard and follows from the chain action regardless of V or A.
- The structure of the field equation (kinetic + potential + source + coupling) is generic for any Lagrangian construction; specific forms of each term determine the linearity question.

---

## 8. The arc's pivot point

MCD.0 §6.3 identified MCD.3 as the structural pivot: whether the many-chain coupling produces nonlinearity. **The honest answer at this stage is: it does not, under the canonical Lagrangian construction.**

The pivot has therefore moved from "is the many-chain coupling nonlinear?" (answered: no, under standard L) to "is there a structurally-motivated reason to adopt N1, N2, or N3?" (open, and the focus of MCD.3).

Three sub-questions for MCD.3:

- **Does ED's substrate physics force a non-quadratic kinetic term?** I.e., is there something about how event-density propagates through the substrate that makes the natural Lagrangian non-quadratic in ∇T? This would be a substrate-derivation-style argument.
- **Does ED's substrate physics force a non-quadratic potential?** I.e., is the screening rate λ itself T-dependent in a way that produces an effective V(T) with higher-order terms?
- **Is the slow-time scalar an inadequate description, requiring tensor structure?** I.e., does ED really need a metric, not just a scalar T, and does the full tensor structure produce nonlinearity even at galactic scales?

If any of these has an affirmative substrate-derivation answer, MCD has a path forward. If all three are negative, MCD closes with the same verdict as DM.G: refuted by structural-linearity arguments.

---

## 9. Recommended Next Steps

Three concrete next steps, in priority order:

1. **MCD.3: Examine whether ED's substrate physics motivates any of N1, N2, or N3.** This is the structural-derivation task that determines MCD's fate. Specifically: (a) revisit ED's substrate event-propagation rules and ask whether the macroscopic Lagrangian inherited from coarse-graining is necessarily quadratic, or whether there are higher-order corrections that survive the continuum limit; (b) examine whether the screening rate λ has hidden T-dependence that would induce non-quadratic V; (c) examine whether the scalar-T approximation is fundamentally adequate or whether tensor structure is needed. **This is the immediate next step.** Each sub-question is bounded and produces a definite "yes / no / unresolved" answer.

2. **Read the existing AD evaluation of Event Density** before MCD.3. The AD evaluation may have established constraints on what kinds of field-theory constructions are consistent with ED's existing architecture. If certain Lagrangian forms are AD-disqualified or if the AD constraint census has identified slack in the existing constraints, that information should inform MCD.3.

3. **Begin scoping a parallel "natural a₀" memo as a fallback path.** Independent of the substrate-derivation question, the c·H_0 ≈ a₀ coincidence (from BTFR.09) is suggestive. If MCD.3 yields no substrate-forced nonlinearity but the natural-a₀ derivation succeeds, MCD could still produce a structurally-clean MOND-equivalent (rather than MOND-imported) version of ED's gravitational sector. This is not a primary path but a useful fallback if MCD.3 is unresolved.

The MCD arc is at its decisive structural moment. **MCD.3 will determine whether the arc adopts (substrate-derived nonlinearity), revises (parallel-path success), or rejects (linear field equation, DM-arc-equivalent failure).**

Status: complete.
