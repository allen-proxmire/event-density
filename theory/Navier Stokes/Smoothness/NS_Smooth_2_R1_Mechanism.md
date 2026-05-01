# NS-Smooth-2 — R1 Mechanism Formalization: Gradient-Norm Lyapunov in ED-Only NS

**Date:** 2026-04-30
**Status:** NS-Smooth-2 of the Smoothness arc. **Headline: H1 succeeds.** ED's R1 mechanism — the form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4 v$ term in the continuum momentum equation — when combined with the standard viscous term $\nu\nabla^2 v$ in the absence of the advective convective derivative, produces an "ED-only NS" with a strictly monotonically-decaying gradient-norm Lyapunov $L(t) = \frac{1}{2}\|\nabla v(t)\|_2^2$. The decay rate has *two* manifestly negative contributions: $-\nu\|\nabla^2 v\|_2^2$ (viscous) and $-\kappa\mu_\mathrm{V1}\ell_P^2 \|\nabla^3 v\|_2^2$ (R1). No positive terms enter the gradient-norm Lyapunov derivative for ED-only NS. By standard parabolic-regularity theory, the resulting equation has global smooth solutions on $\mathbb{R}^3$ for finite-energy initial data — establishing the *positive side* of the Clay-relevance decomposition.
**Companions:** [`NS_Smooth_1_Opening.md`](NS_Smooth_1_Opening.md), [`../NS-3.01_LP4_Regularization_Survival.md`](../NS-3.01_LP4_Regularization_Survival.md), [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md).

---

## 1. Purpose

This memo establishes H1 (Structural) of the Smoothness arc:

> *ED's architectural R1 mechanism guarantees monotone decay of the gradient norm $\|\nabla v\|_2^2$ in an "ED-only NS" — i.e., NS with diffusion and the R1 substrate-scale stabilization term but without the advective convective derivative.*

This provides the **positive side** of the Clay-relevance decomposition. The negative side (advection's vortex-stretching as the structural feature breaking the gradient-norm Lyapunov) is established in NS-Smooth-3.

The substantive content is a clean Lyapunov calculation showing that, in the ED-only NS setting, the gradient-norm time-derivative is the sum of two manifestly negative contributions — the standard viscous one and the new R1 contribution — with no positive terms that could amplify gradients. The resulting "ED-only NS" is parabolic-class with a higher-derivative regularization; standard analytical results give global smoothness for finite-energy data.

---

## 2. Inputs

| Input | Source |
|---|---|
| R1 form-FORCED term: $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v$ in continuum momentum equation | [`../NS-3.01_LP4_Regularization_Survival.md`](../NS-3.01_LP4_Regularization_Survival.md) §4 |
| Sign FORCED positive ($\kappa > 0$) by V1 being a positive smoothing kernel | [`../NS-3.01_LP4_Regularization_Survival.md`](../NS-3.01_LP4_Regularization_Survival.md) §4.1 |
| Coefficient INHERITED via V1's specific G-function | [`arcs/arc-N/non_markov_forced.md`](../../../arcs/arc-N/non_markov_forced.md) §6.5 |
| Gradient-norm Lyapunov $L(t) = \frac{1}{2}\|\nabla v\|_2^2$ — enstrophy-class | [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md) §3.4 (L4) |
| ED canonical PDE channels: V1 smoothing kernel, P4 mobility | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 |
| Standard NS diffusion term $\nu\nabla^2 v$ | Standard fluid mechanics |
| NS-Smooth-1 §5 framing: counterfactual smoothness in ED-only NS | [`NS_Smooth_1_Opening.md`](NS_Smooth_1_Opening.md) §5 |

---

## 3. Step 1 — The ED-Only NS Equation

Define the "ED-only NS" equation as the standard incompressible Navier-Stokes equation with the advective convective derivative *removed* and the R1 term *added*:

$$\boxed{\;\rho \, \partial_t v_i \;=\; \mu \nabla^2 v_i \;-\; \kappa\mu_\mathrm{V1}\ell_P^2 \, \nabla^4 v_i \;-\; \partial_i p \;+\; \rho f_i^\mathrm{ext}, \qquad \nabla \cdot \mathbf{v} = 0.\;}$$

This is *not* physical NS — the advective term $(v\cdot\nabla)v_i$ is structurally present in any real fluid mechanics. The ED-only NS is a counterfactual: the equation that would govern the velocity field *if* the canonical ED PDE's vector-extension content were the entire fluid equation, with no fluid-mechanical-specific additions beyond the architectural channels.

### 3.1 Components of the ED-only NS

- **Diffusion** $\mu\nabla^2 v_i$: standard kinematic-viscosity-class diffusion term, mapped from the canonical PDE mobility channel via NS-2.08 §4.1.
- **R1 stabilization** $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v_i$: form-FORCED higher-derivative regularization from V1 finite-width vacuum kernel + multi-scale expansion (NS-3.01 §4). Coefficient $\kappa > 0$ FORCED; magnitude INHERITED.
- **Pressure** $-\partial_i p$: Lagrange multiplier enforcing incompressibility $\nabla\cdot v = 0$. Not derived from ED architecture per NS-2.08 §5; included here as a fluid-mechanical structural addition required for coherence with the incompressibility constraint.
- **External forcing** $\rho f_i^\mathrm{ext}$: gravity (T19) + EM (T17, charged fluids) + boundary forcing.

### 3.2 What ED-only NS includes and excludes

**Includes:**
- ED canonical mobility channel (viscous diffusion).
- ED V1 substrate-scale R1 stabilization.
- Pressure as Lagrange multiplier for incompressibility.
- External forcing.

**Excludes (relative to full NS):**
- The advective convective derivative $(v\cdot\nabla)v_i$ — the structural feature identified in NS-2.08 §5 + NS-3.02b §3.4 + NS-Turb §6 as fluid-mechanical-addition / non-ED-architectural.

This counterfactual equation is the appropriate test bed for H1: does ED's architectural content guarantee smoothness if advection is removed?

---

## 4. Step 2 — Gradient-Norm Lyapunov Functional

### 4.1 Definition

Define the gradient-norm Lyapunov functional:

$$L(t) = \frac{1}{2} \, \|\nabla v(t)\|_2^2 = \frac{1}{2} \int_{\mathbb{R}^3} \partial_j v_i \, \partial_j v_i \; dV.$$

This is enstrophy-class (related to enstrophy $E_\Omega = \frac{1}{2}\int |\omega|^2 dV$ via integration by parts and incompressibility, with $|\nabla v|^2$ the natural $H^1$ semi-norm). A monotonically-decreasing enstrophy-class quantity in 3D, by the Beale-Kato-Majda regularity criterion combined with standard energy methods, implies global smooth solutions for finite-energy initial data.

### 4.2 Time derivative

Compute $dL/dt$ using $\partial_t (\partial_j v_i) = \partial_j (\partial_t v_i)$:

$$\frac{dL}{dt} = \int \partial_j v_i \, \partial_j (\partial_t v_i) \, dV.$$

Substitute the ED-only NS equation §3:

$$\frac{dL}{dt} = \int \partial_j v_i \, \partial_j \left[\frac{1}{\rho}\bigl(\mu\nabla^2 v_i - \kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v_i - \partial_i p + \rho f_i^\mathrm{ext}\bigr)\right] dV.$$

For incompressible flow with constant density, factor $1/\rho$ outside. Compute each contribution separately.

### 4.3 Diffusion contribution

$$\int \partial_j v_i \, \partial_j (\nu \nabla^2 v_i) \, dV = \nu \int \partial_j v_i \, \nabla^2 (\partial_j v_i) \, dV.$$

Apply integration by parts (twice; fields and derivatives decaying at infinity):

$$= -\nu \int \nabla(\partial_j v_i) \cdot \nabla(\partial_j v_i) \, dV = -\nu \int |\nabla \partial_j v_i|^2 \, dV = -\nu \int |\nabla^2 v|^2 \, dV \;\le\; 0.$$

This is the standard Laplacian-Lyapunov contribution: viscous diffusion strictly dissipates gradient-norm.

### 4.4 R1 contribution

$$\int \partial_j v_i \, \partial_j \bigl(-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v_i\bigr) \, dV = -\kappa\mu_\mathrm{V1}\ell_P^2 \int \partial_j v_i \, \nabla^4 (\partial_j v_i) \, dV.$$

Apply integration by parts (four times; fields decay at infinity):

$$\int u \, \nabla^4 u \, dV = \int |\nabla^2 u|^2 \, dV \quad \ge 0$$

(repeated integration by parts on $\int u \nabla^2(\nabla^2 u) dV$ gives $\int \nabla^2 u \cdot \nabla^2 u \, dV$).

Applied to $u = \partial_j v_i$:

$$\int \partial_j v_i \, \nabla^4 (\partial_j v_i) \, dV = \int |\nabla^2 \partial_j v_i|^2 \, dV = \int |\nabla^3 v|^2 \, dV \;\ge\; 0.$$

Therefore the R1 contribution to $dL/dt$:

$$-\kappa\mu_\mathrm{V1}\ell_P^2 \int |\nabla^3 v|^2 \, dV \;\le\; 0.$$

This is strictly non-positive (zero only if $\nabla^3 v = 0$ everywhere, i.e., $v$ is at most quadratic in space — which on $\mathbb{R}^3$ with finite-energy means $v$ is constant).

**The R1 contribution to gradient-norm decay is manifestly negative.** This is the substantive structural content of H1.

### 4.5 Pressure contribution

$$\int \partial_j v_i \, \partial_j (-\partial_i p) \, dV = -\int \partial_j v_i \, \partial_i \partial_j p \, dV.$$

Integrate by parts moving $\partial_i$ off pressure:

$$= \int \partial_i \partial_j v_i \, \partial_j p \, dV = \int (\partial_i v_i) \cdot \partial_j \partial_j p \, dV \cdot ... \text{wait, indices.}$$

More carefully: rearrange the indices. $-\int \partial_j v_i \, \partial_i \partial_j p \, dV$. Integrate by parts on $\partial_j$ to move it from $v_i$ to $\partial_i p$:

$$= +\int \partial_j (\partial_j v_i) \, \partial_i p \, dV = \int (\nabla^2 v_i) \, \partial_i p \, dV.$$

Now integrate by parts on $\partial_i$:

$$= -\int \partial_i(\nabla^2 v_i) \, p \, dV = -\int \nabla^2 (\partial_i v_i) \, p \, dV = -\int \nabla^2 (\nabla\cdot v) \, p \, dV.$$

By incompressibility $\nabla \cdot v = 0$:

$$\int \partial_j v_i \, \partial_j (-\partial_i p) \, dV = 0.$$

**Pressure contributes zero to the gradient-norm Lyapunov derivative in incompressible flow.** This was already noted in NS-3.02b §3.4 and is reconfirmed here. *Pressure does not break the Lyapunov.*

### 4.6 Forcing contribution

$$\int \partial_j v_i \, \partial_j f_i^\mathrm{ext} \, dV.$$

Sign-indefinite in general; depends on forcing structure. For the unforced case ($f^\mathrm{ext} = 0$) this contribution vanishes. For typical NS regularity-questions, the unforced (or finite-energy decaying-forcing) case is the relevant setting; forcing is set to zero in what follows.

### 4.7 Aggregate

$$\boxed{\;\frac{dL}{dt} = -\nu \int |\nabla^2 v|^2 \, dV \;-\; \kappa\mu_\mathrm{V1}\ell_P^2 \int |\nabla^3 v|^2 \, dV \;\le\; 0.\;}$$

**Both contributions are manifestly non-positive.** The gradient-norm Lyapunov decreases monotonically along trajectories of the ED-only NS, with strict negativity unless $v$ is spatially constant.

### 4.8 Fourier-space cross-check

In Fourier space (with the velocity field expressed as $\hat v(\mathbf{k}, t)$), the linearized ED-only NS dispersion relation is:

$$\partial_t \hat v_i(\mathbf{k}) = -\nu k^2 \hat v_i(\mathbf{k}) - \kappa\mu_\mathrm{V1}\ell_P^2 k^4 \hat v_i(\mathbf{k}) + \cdots$$

(omitting pressure and forcing). The mode-amplitude time-derivative:

$$\partial_t |\hat v(\mathbf{k})|^2 = 2 \, \mathrm{Re}\bigl[\hat v^* \cdot \partial_t \hat v\bigr] = -2 \bigl(\nu k^2 + \kappa\mu_\mathrm{V1}\ell_P^2 k^4\bigr)|\hat v(\mathbf{k})|^2.$$

By Plancherel, the gradient-norm in Fourier space is $L \sim \int k^2 |\hat v|^2 d^3k$. Time-derivative:

$$\frac{dL}{dt} = -2\int (\nu k^4 + \kappa\mu_\mathrm{V1}\ell_P^2 k^6) |\hat v(\mathbf{k})|^2 d^3k \le 0.$$

Confirms the real-space calculation: $\nu k^4$ corresponds to $\nu \int|\nabla^2 v|^2$ (after Plancherel); $\kappa\mu_\mathrm{V1}\ell_P^2 k^6$ corresponds to $\kappa\mu_\mathrm{V1}\ell_P^2 \int|\nabla^3 v|^2$. Both terms strictly damp every Fourier mode at every wavenumber.

---

## 5. Step 3 — Interpretation

### 5.1 Built-in smoothing mechanism

The aggregate result $dL/dt \le 0$ means ED-only NS has a **built-in smoothing mechanism** — gradient norm cannot grow under the dynamics. This is a strong structural property. Both terms (viscous + R1) push high-wavenumber modes toward zero, with R1 acting more strongly at high $k$ ($k^6$ scaling vs. $k^4$).

### 5.2 Higher-derivative control via R1

The R1 term controls $\|\nabla^3 v\|_2^2$ in the time-integrated sense. From the inequality

$$-\frac{dL}{dt} \ge \kappa\mu_\mathrm{V1}\ell_P^2 \int|\nabla^3 v|^2 dV,$$

integrating from $0$ to $T$:

$$L(0) - L(T) \ge \kappa\mu_\mathrm{V1}\ell_P^2 \int_0^T \|\nabla^3 v\|_2^2 \, dt.$$

Therefore $\int_0^T \|\nabla^3 v\|_2^2 dt$ is bounded above by $L(0)/(\kappa\mu_\mathrm{V1}\ell_P^2)$ — uniform-in-T third-derivative integrability. Combined with $\int_0^T \|\nabla^2 v\|_2^2 dt \le L(0)/\nu$ from the diffusion contribution alone, this gives:

$$v \in L^2([0,T]; H^3(\mathbb{R}^3)) \cap L^\infty([0,T]; H^1(\mathbb{R}^3))$$

— uniform-in-$T$ third-derivative L²-integrability and uniform-in-$T$ first-derivative L²-boundedness. This is significantly stronger regularity control than standard NS (which gives only $v \in L^2(H^1) \cap L^\infty(L^2)$ in 3D).

### 5.3 Strong regularizing structure absent in full NS

The gradient-norm monotonicity in ED-only NS is the structural property that, in *full* 3D NS, fails. In full 3D NS the advective term contributes a vortex-stretching term to $dL/dt$ that has indefinite sign and can amplify gradients (NS-3.02b §3.4). The structural difference between ED-only NS (smoothness guaranteed) and full NS (smoothness open) is exactly the presence or absence of the advective term.

---

## 6. Step 4 — Counterfactual Smoothness Result

### 6.1 Statement

**Counterfactual.** If 3D incompressible NS lacked the advective convective derivative — i.e., if the equation were the ED-only NS

$$\partial_t v_i = \frac{\mu}{\rho}\nabla^2 v_i - \frac{\kappa\mu_\mathrm{V1}\ell_P^2}{\rho} \nabla^4 v_i - \frac{1}{\rho}\partial_i p, \qquad \nabla\cdot v = 0$$

— then for every smooth, finite-energy initial datum $v_0 \in H^s(\mathbb{R}^3)$ with $s$ sufficiently large, the solution $v(t)$ would extend globally to $t \in [0, \infty)$ with $v(\cdot, t) \in C^\infty(\mathbb{R}^3)$ for all $t > 0$.

### 6.2 Justification

Standard parabolic-regularity theory for higher-derivative regularized parabolic equations (see, e.g., Lions 1969; Constantin & Foias 1988 for related NS-Burgers-class results). The ED-only NS equation is a *stable parabolic* equation: the linear part has dispersion relation $-\nu k^2 - \kappa\mu_\mathrm{V1}\ell_P^2 k^4$ with both terms negative for all $k > 0$. By standard heat-equation-class arguments adapted to the higher-derivative regularization:

1. Local well-posedness in $H^s$ for $s > 5/2$ (so that pressure is well-defined and incompressibility is preserved).
2. Global $H^s$ bound from the gradient-norm Lyapunov decay (§4.7) plus the energy-bound from the standard $L^2$ Lyapunov.
3. Bootstrap to higher regularity via repeated application of the parabolic regularity machinery; the $\nabla^4$ regularization makes each step strictly stronger than standard NS.

The argument is canonical for higher-derivative-regularized parabolic equations and parallels the proof of global smoothness for the *Navier-Stokes-Burgers* equation $\partial_t v + (v\cdot\nabla)v = \nu\Delta v - \epsilon \Delta^2 v$ in 3D for $\epsilon > 0$ (which has been analyzed extensively in the literature; see e.g., Cao-Titi-class works). In our case, with the *advective term removed entirely*, the smoothness result is *a fortiori* — the equation is parabolic-class without the obstructive nonlinearity.

### 6.3 Status

The counterfactual smoothness result for ED-only NS is **standard parabolic-regularity content**, not a new technical theorem of this paper. The substantive structural finding is that ED's R1 mechanism, *combined with* removal of the advective term, gives an equation in this canonical-parabolic class — i.e., ED's architectural content alone (without the fluid-mechanical-addition advection) is sufficient for global smoothness.

This establishes the **positive side** of the Clay-relevance decomposition: ED supplies a regularizing mechanism that would close Clay-NS were it not for the non-ED advective obstruction.

---

## 7. Provisional Verdict for H1

**H1 (Structural) succeeds cleanly.**

ED's architectural R1 mechanism — the form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4 v$ term in the continuum momentum equation — combined with standard viscous diffusion, produces an "ED-only NS" with a strictly monotonically-decaying gradient-norm Lyapunov in the absence of the advective convective derivative. The monotonicity is structurally robust:

- **Two manifestly negative contributions** to $dL/dt$ from diffusion ($-\nu\|\nabla^2 v\|_2^2$) and R1 ($-\kappa\mu_\mathrm{V1}\ell_P^2 \|\nabla^3 v\|_2^2$).
- **No positive terms** in the gradient-norm Lyapunov derivative for ED-only NS.
- **Pressure contributes zero** in incompressible flow (integration by parts + $\nabla\cdot v = 0$).
- **R1's coefficient is FORCED positive** by V1 being a positive smoothing kernel.

Standard parabolic-regularity theory, applied to the ED-only NS, gives global smooth solutions for finite-energy initial data on $\mathbb{R}^3$.

**H1 establishes the positive side of the Clay-relevance decomposition.** ED contains a clean architectural mechanism that would guarantee smoothness if the non-ED advective term were absent. The structural content is: ED supplies regularizing infrastructure; the obstacle to closing Clay-NS lies elsewhere (in advection, addressed in NS-Smooth-3).

---

## 8. Recommended Next Steps

1. **Proceed to NS-Smooth-3 (Advection Obstruction Analysis).** File: `theory/Navier Stokes/Smoothness/NS_Smooth_3_Advection_Obstruction.md`. Restore the advective term to the ED-only NS and compute its contribution to $dL/dt$. Explicit calculation: vortex-stretching term $-2\int(\partial_j v_i)(\partial_i v_k)(\partial_k v_j) dV$ with indefinite sign in 3D, vanishing in 2D. Show that this is the *only* contribution to $dL/dt$ that can be positive — confirming the obstruction localizes at advection specifically. Foundations: NS-3.02b §3.4 (already established the calculation; NS-Smooth-3 reframes it within the Clay-relevance decomposition).

2. **Use NS-3.02b §3.4 as the technical foundation for NS-Smooth-3.** The vortex-stretching analysis is already in place; NS-Smooth-3 references and integrates rather than rederives. The substantive new content of NS-Smooth-3 is the framing: "advection is the *unique* structural feature breaking the gradient-norm Lyapunov in ED-only-plus-advection NS, with three-angle convergence per NS-2.08 + NS-3.02b + NS-Turb-4."

3. **Use NS-Turb-4 §6 spectral analysis for the index-structure framing.** The spectral-level identification of advection's transport-directional + projection structure (versus P7-class symmetric-quadratic-in-gradients) provides the architectural-canon-level reason advection is non-ED. NS-Smooth-3 should invoke this for the architectural-decomposition framing.

### Decisions for you

- **Confirm H1 verdict.** ED's R1 mechanism produces strictly monotone gradient-norm decay in ED-only NS; standard parabolic-regularity gives global smoothness. Positive side of Clay-relevance decomposition established.
- **Confirm proceeding to NS-Smooth-3 next** (Advection Obstruction Analysis).
- **Confirm framing of the Clay-relevance decomposition.** ED supplies *regularizing infrastructure*; the obstruction lies in the *non-ED advective term*. The two halves of the decomposition (R1 mechanism + advection obstruction) jointly explain why Clay-NS is hard without claiming to close it.

---

*NS-Smooth-2 R1 mechanism formalized. **Headline: H1 succeeds cleanly.** ED-only NS has gradient-norm Lyapunov derivative $dL/dt = -\nu\|\nabla^2 v\|_2^2 - \kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3 v\|_2^2 \le 0$ — strictly monotone decay with two manifestly negative contributions and no positive terms. Pressure contributes zero in incompressible flow. R1's coefficient FORCED positive by V1 being a positive smoothing kernel. Standard parabolic-regularity theory gives global smoothness for ED-only NS on $\mathbb{R}^3$ with finite-energy data. Positive side of Clay-relevance decomposition established. NS-Smooth-3 (Advection Obstruction Analysis) is the next deliverable.*
