# ED-Cosmo-01: The Cosmological Limit of the ED Compositional Rule

**Author:** Allen Proxmire
**Series:** ED-Cosmo-01
**Date:** March 2026
**Status:** Theoretical foundation — conceptual and mathematical

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Foundational Paper (ED-5) | Canonical PDE, seven axioms, constitutive channels |
| ED-I-012.0 (Compositional Rule) | Three-penalty compositional rule, concave constraint |
| ED-I-012.5 (Cosmology Specialization) | Cosmological epoch classification, horizon conditions |
| ED-Phys-05 (Participation Field) | $v(t)$ as mean Madelung velocity, Compton anchoring, $\gamma$ interpretation |
| ED-Phys-06 (Universality + Phase Diagram) | $(\beta, H)$ phase diagram, $H/P_0$ stability criterion, Lyapunov boundary |
| ED-Dimensional-05 (Cosmological Regime) | Scale anchoring: $D = c^2/H_0$, $L_0 = c/H_0$, $R_0 = \rho_{\text{crit}}$ |

**Scope.** This paper derives the cosmological limit of the ED PDE — the dynamical system that results when the canonical ED equation is specialised to homogeneous, isotropic conditions at Hubble scales. It is not a simulation module. It is the theoretical bridge from the ED architecture to cosmological observables, grounded in the empirical results of ED-Phys-05 and ED-Phys-06.

---

## Table of Contents

1. [Cosmological Limit of the ED Compositional Rule](#1-cosmological-limit-of-the-ed-compositional-rule)
2. [Identification of the Cosmological Point in Phase Space](#2-identification-of-the-cosmological-point-in-phase-space)
3. [ED to Friedmann Mapping](#3-ed-to-friedmann-mapping)
4. [Predictions for Cosmic Expansion](#4-predictions-for-cosmic-expansion)
5. [Cosmological Falsification Conditions](#5-cosmological-falsification-conditions)
6. [Conceptual Interpretation](#6-conceptual-interpretation)

---

# 1. Cosmological Limit of the ED Compositional Rule

## 1.1 The Full Canonical PDE

The ED canonical PDE (Foundational Paper, seven axioms P1--P7) is:

$$\partial_t \rho = D\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H\,v(t) \tag{1}$$

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr), \qquad \bar{F} = \bigl\langle D[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)]\bigr\rangle \tag{2}$$

with constitutive functions:

$$M(\rho) = M_0(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0(\rho - \rho^*)$$

## 1.2 The Homogeneity-Isotropy Reduction

At cosmological scales, the Copernican principle asserts that the universe is spatially homogeneous and isotropic on sufficiently large scales ($\gtrsim 100$ Mpc). The ED analogue is:

**Assumption C1 (Homogeneity):** $\rho(\mathbf{x}, t) = \bar{\rho}(t)$ — the density field is spatially uniform.

**Assumption C2 (Isotropy):** All spatial gradients vanish: $\nabla\rho = 0$, $\nabla^2\rho = 0$.

Under C1 and C2, the mobility channel vanishes identically:

$$M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 = 0$$

The spatial-average forcing simplifies to:

$$\bar{F} = D\bigl[0 - P_0(\bar{\rho} - \rho^*)\bigr] = -DP_0(\bar{\rho} - \rho^*)$$

## 1.3 The Reduced Cosmological System

The full PDE reduces to a system of two coupled ODEs:

$$\boxed{\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + Hv} \tag{3}$$

$$\boxed{\dot{v} = \frac{1}{\tau}\bigl[-DP_0(\bar{\rho} - \rho^*) - \zeta v\bigr]} \tag{4}$$

This is the **ED cosmological dynamical system** — a two-dimensional ODE in $(\bar{\rho}, v)$.

**Structural content:** At cosmological scales, only the penalty channel and the participation channel survive. The mobility channel (nonlinear diffusion, front propagation, compact support) is absent because there are no spatial gradients in the homogeneous limit. Cosmological ED is a penalty-participation system — exactly the regime described by the RC/RLC analogue (Analogue 1 in the Foundational Paper).

## 1.4 The Telegraph Form

Define $\delta(t) = \bar{\rho}(t) - \rho^*$ (deviation from equilibrium). Equations (3)--(4) become:

$$\dot{\delta} = -DP_0\,\delta + Hv \tag{5}$$

$$\dot{v} = -\frac{1}{\tau}\bigl(DP_0\,\delta + \zeta v\bigr) \tag{6}$$

Eliminating $v$ by differentiating (5) and substituting (6):

$$\ddot{\delta} + \underbrace{\Bigl(DP_0 + \frac{\zeta}{\tau}\Bigr)}_{2\gamma}\dot{\delta} + \underbrace{\Bigl[\frac{DP_0\zeta + HP_0}{\tau}\Bigr]}_{\omega_0^2}\delta = 0 \tag{7}$$

This is the **cosmological telegraph equation** — a damped harmonic oscillator for the density deviation. Its solutions are:

$$\delta(t) = \delta_0\,e^{-\gamma t}\cos(\omega t + \phi) \qquad (\omega_0 > \gamma,\;\text{underdamped}) \tag{8}$$

$$\delta(t) = \delta_0\,(A\,e^{-\lambda_+ t} + B\,e^{-\lambda_- t}) \qquad (\omega_0 < \gamma,\;\text{overdamped}) \tag{9}$$

where $\gamma = (DP_0 + \zeta/\tau)/2$, $\omega = \sqrt{\omega_0^2 - \gamma^2}$, and $\lambda_\pm = \gamma \pm \sqrt{\gamma^2 - \omega_0^2}$.

## 1.5 The Cosmological Anchoring

From ED-Dimensional-05, the cosmological-regime scales are:

| Quantity | Formula | Value |
|----------|---------|-------|
| $D_{\text{phys}}$ | $c^2/H_0$ | $4.115 \times 10^{34}$ m$^2$/s |
| $L_0$ | $c/H_0$ | $1.373 \times 10^{26}$ m (4.4 Gpc) |
| $T_0$ | $D_{\text{nd}}/H_0$ | $1.374 \times 10^{17}$ s (4.35 Gyr) |
| $R_0$ | $\rho_{\text{crit}}$ | $8.53 \times 10^{-27}$ kg/m$^3$ |
| $V_0$ | $c/D_{\text{nd}}$ | $3.333\,c$ |

## 1.6 The Participation Anchoring (from ED-Phys-05)

ED-Phys-05 established that requiring causal propagation speed $c_{\text{ED}} = c$ uniquely fixes:

$$H = \frac{c^2\tau}{D} \tag{10}$$

In the cosmological regime with $D = c^2/H_0$ and $\tau_{\text{phys}} = T_0 = D_{\text{nd}}/H_0$:

$$H_{\text{cosmo}} = \frac{c^2 \cdot (D_{\text{nd}}/H_0)}{c^2/H_0} = D_{\text{nd}} \tag{11}$$

In nondimensional units: $H_{\text{nd}} = D_{\text{nd}} = 0.3$. In physical units:

$$H_{\text{phys}} = H_{\text{nd}} \cdot V_0 = 0.3 \times 3.333\,c = c$$

**The cosmological participation coupling, when anchored by causality, equals the speed of light.** The telegraph propagation speed is then:

$$c_{\text{ED}} = \sqrt{D \cdot H/\tau} = \sqrt{\frac{c^2}{H_0} \cdot \frac{D_{\text{nd}}}{D_{\text{nd}}/H_0}} = \sqrt{\frac{c^2}{H_0} \cdot H_0} = c \;\checkmark$$

## 1.7 The $H/P_0$ Stability Check (from ED-Phys-06)

ED-Phys-06 established that the Lyapunov boundary is controlled by $H/P_0$, with the safe region at $H/P_0 \lesssim 100$--$1000$.

In the cosmological regime with $H_{\text{nd}} = 0.3$:

| $P_0$ | $H/P_0$ | Regime | Energy monotonicity |
|--------|---------|--------|---------------------|
| 1.0 | 0.3 | Deep safe region | **Holds** |
| 0.1 | 3.0 | Safe region | **Holds** |
| 0.01 | 30 | Safe region | **Holds** |
| 0.001 | 300 | Near Lyapunov boundary | **Marginal** |

For any reasonable penalty strength ($P_0 \geq 0.01$), cosmological ED is well inside the Lyapunov-stable region. The energy functional is a valid Lyapunov function for the cosmological dynamical system.

---

# 2. Identification of the Cosmological Point in Phase Space

## 2.1 The $(\beta, H)$ Phase Diagram Location

From ED-Phys-06, the five regions of the $(\beta, H)$ phase diagram are:

- Region I: PME-dominated ($H < H_c$, moderate $\beta$)
- Region II: Strongly degenerate ($H < H_c$, high $\beta$)
- Region III: Mixed ($H_c < H < H_{\text{Lyap}}$)
- Region IV: Telegraph-dominated ($H > H_{\text{Lyap}}$)
- Region V: Extreme ($H > H_{\text{Lyap}}$, high $\beta$)

The cosmological point is:

$$(\beta_{\text{cosmo}}, H_{\text{cosmo}}) = (2.0, 0.3)$$

This places cosmological ED in **Region III (mixed regime)** — above the participation threshold $H_c$ but well below the Lyapunov boundary $H_{\text{Lyap}}$.

## 2.2 But the Mobility Channel Is Absent

In the homogeneous limit, $\nabla\rho = 0$ and the mobility channel vanishes. The effective phase-diagram location depends not on $(\beta, H)$ but on $(P_0, H)$ alone. The relevant parameter is $H/P_0$, and the cosmological system operates as a pure penalty-participation oscillator.

This is a crucial distinction: while the full ED PDE at $(\beta = 2, H = 0.3)$ sits in Region III with active mobility, the **cosmological limit** (homogeneous) reduces to the penalty-participation subspace regardless of $\beta$.

## 2.3 Candidate Cosmological Parameter Points

The cosmological observables constrain $D$ and $L_0$ exactly. The remaining free parameters are $P_0$, $\beta$ (irrelevant in the homogeneous limit), $\zeta$, and $\tau$. Their values determine the telegraph parameters:

| Candidate | $P_0$ | $\zeta$ | $\tau$ (nd) | $\gamma$ (nd) | $\omega_0$ (nd) | $\gamma/\omega_0$ | Character |
|-----------|--------|---------|-------------|----------------|------------------|-------|-----------|
| A (canonical) | 1.0 | 0.1 | 1.0 | 0.200 | 0.361 | 0.554 | Underdamped |
| B (weak penalty) | 0.1 | 0.1 | 1.0 | 0.065 | 0.118 | 0.551 | Underdamped |
| C (strong damping) | 1.0 | 1.0 | 1.0 | 0.650 | 0.361 | 1.801 | **Overdamped** |
| D (matched) | 0.3 | 0.3 | 1.0 | 0.195 | 0.208 | 0.938 | Near-critical |
| E (Hubble-matched) | $H_0 T_0$ | 0.1 | 1.0 | 0.095 | 0.104 | 0.913 | Near-critical |

**Candidates A and B** are underdamped: the cosmological density oscillates around $\rho^*$ before settling. This produces oscillatory corrections to the expansion history.

**Candidate C** is overdamped: the density relaxes monotonically, producing a smooth expansion history similar to $\Lambda$CDM.

**Candidates D and E** are near the critical-damping boundary: the system is on the edge between oscillatory and monotonic. This is the most interesting regime physically, as it produces the largest single oscillation before settling.

## 2.4 The Physical Choice

The ED architecture does not uniquely fix $P_0$ or $\zeta$ in the cosmological regime (they are "Candidate" status in the dictionary). However, two physical arguments constrain the choice:

**Argument 1 (Hubble-time relaxation):** The penalty relaxation time in the RC limit ($H = 0$) is $\tau_{\text{RC}} = 1/(DP_0)$. If this equals the Hubble time ($\hat{t}_H = 1/D_{\text{nd}} \approx 3.33$), then $P_0 = D_{\text{nd}}/\hat{t}_H \cdot \hat{t}_H = 1/\hat{t}_H^2 \cdot D_{\text{nd}}$... more simply, $DP_0 = 1/\hat{t}_H$ gives $P_0 = 1/(D_{\text{nd}} \hat{t}_H) = 1/(0.3 \times 3.33) = 1.0$. **Candidate A** satisfies this.

**Argument 2 (Critical damping):** The most structurally interesting regime is near critical damping ($\gamma \approx \omega_0$), where the system transitions between oscillatory and monotonic with the smallest perturbation. **Candidate D** achieves this with $P_0 = \zeta = 0.3 = D_{\text{nd}}$.

---

# 3. ED to Friedmann Mapping

## 3.1 The Scale Factor Identification

In standard cosmology, the expansion of the universe is described by the scale factor $a(t)$, normalised so that $a(t_0) = 1$ at the present time. The mean density evolves as:

$$\bar{\rho}(t) = \frac{\rho_0}{a(t)^3} \qquad \text{(matter-dominated)} \tag{12}$$

In ED, the density $\bar{\rho}(t)$ is the dynamical variable. The scale factor is derived from it:

$$\boxed{a_{\text{ED}}(t) = \left(\frac{\rho_0}{\bar{\rho}(t)}\right)^{1/3}} \tag{13}$$

where $\rho_0 = \bar{\rho}(0)$ is the initial density. This identification is exact for a matter-dominated universe and approximate when radiation or dark energy contribute.

## 3.2 The ED Hubble Parameter

The Hubble parameter is $\mathcal{H}(t) = \dot{a}/a$. From (13):

$$\dot{a} = -\frac{1}{3}\,\frac{\rho_0^{1/3}}{\bar{\rho}^{4/3}}\,\dot{\bar{\rho}} = -\frac{a}{3\bar{\rho}}\,\dot{\bar{\rho}}$$

Therefore:

$$\boxed{\mathcal{H}_{\text{ED}}(t) = \frac{\dot{a}}{a} = -\frac{\dot{\bar{\rho}}}{3\bar{\rho}}} \tag{14}$$

Substituting the ED cosmological equation (3):

$$\mathcal{H}_{\text{ED}} = -\frac{-DP_0(\bar{\rho} - \rho^*) + Hv}{3\bar{\rho}} = \frac{DP_0(\bar{\rho} - \rho^*) - Hv}{3\bar{\rho}} \tag{15}$$

**Physical interpretation:** The ED Hubble parameter has two contributions:

1. **Penalty term** $DP_0(\bar{\rho} - \rho^*)/(3\bar{\rho})$: When $\bar{\rho} > \rho^*$, this is positive, driving expansion (density decrease). This is the ED analogue of dark energy — a restoring force that pushes the density toward $\rho^*$.

2. **Participation term** $-Hv/(3\bar{\rho})$: This can be positive or negative depending on $v(t)$. It modulates the expansion rate — the ED analogue of the interplay between matter and dark energy.

## 3.3 The ED Deceleration Parameter

The deceleration parameter is $q = -\ddot{a}a/\dot{a}^2$. Differentiating $\mathcal{H} = -\dot{\bar{\rho}}/(3\bar{\rho})$:

$$\dot{\mathcal{H}} = -\frac{\ddot{\bar{\rho}}}{3\bar{\rho}} + \frac{\dot{\bar{\rho}}^2}{3\bar{\rho}^2}$$

Using $q = -(1 + \dot{\mathcal{H}}/\mathcal{H}^2)$:

$$\boxed{q_{\text{ED}}(t) = -1 - \frac{\dot{\mathcal{H}}_{\text{ED}}}{\mathcal{H}_{\text{ED}}^2}} \tag{16}$$

For the telegraph solution (8) with $\bar{\rho}(t) = \rho^* + \delta_0 e^{-\gamma t}\cos(\omega t + \phi)$:

$$\dot{\bar{\rho}} = -\delta_0 e^{-\gamma t}\bigl[\gamma\cos(\omega t + \phi) + \omega\sin(\omega t + \phi)\bigr]$$

The deceleration parameter oscillates around a secular trend:

$$q_{\text{ED}}(t) = q_{\text{sec}}(t) + \Delta q\,e^{-\gamma t}\cos(\omega t + \psi) \tag{17}$$

where $q_{\text{sec}}$ is the smooth (envelope) deceleration and $\Delta q$ is the oscillatory correction amplitude.

## 3.4 The ED Equation of State

The effective equation-of-state parameter $w$ relates pressure to density: $p = w\rho c^2$. In the Friedmann framework:

$$q = \frac{1}{2}(1 + 3w)$$

Inverting:

$$\boxed{w_{\text{ED}}(t) = \frac{2q_{\text{ED}}(t) - 1}{3}} \tag{18}$$

**Key regimes:**

| ED state | $q_{\text{ED}}$ | $w_{\text{ED}}$ | Cosmological analogue |
|----------|------------------|------------------|----------------------|
| $\bar{\rho} \gg \rho^*$, $v \approx 0$ | $q > 0$ | $w > -1/3$ | Decelerating (matter-like) |
| $\bar{\rho} \approx \rho^*$, $v \approx 0$ | $q \to -1$ | $w \to -1$ | Accelerating (de Sitter-like) |
| $\bar{\rho} < \rho^*$, $v$ oscillating | $q$ oscillates | $w$ oscillates | Telegraph regime |

## 3.5 Mapping Summary

| Cosmological observable | ED formula | Source term |
|------------------------|-----------|-------------|
| Scale factor $a(t)$ | $(\rho_0/\bar{\rho})^{1/3}$ | Density evolution |
| Hubble parameter $\mathcal{H}(t)$ | $-\dot{\bar{\rho}}/(3\bar{\rho})$ | Penalty + participation |
| Deceleration $q(t)$ | $-1 - \dot{\mathcal{H}}/\mathcal{H}^2$ | Second derivative of $\bar{\rho}$ |
| Equation of state $w(t)$ | $(2q - 1)/3$ | From $q$ |
| Dark energy density | $DP_0\rho^*/(3\bar{\rho}) \cdot (3\bar{\rho})$ | Penalty equilibrium term |
| Oscillatory correction | $\Delta q \propto e^{-\gamma t}\cos\omega t$ | Telegraph dynamics |

---

# 4. Predictions for Cosmic Expansion

## 4.1 The Expansion Law $a(t)$

From (3) and (13), the scale factor satisfies:

$$\frac{\dot{a}}{a} = \frac{DP_0(\bar{\rho} - \rho^*)}{3\bar{\rho}} - \frac{Hv}{3\bar{\rho}} \tag{19}$$

### Late-time attractor ($t \to \infty$)

As $t \to \infty$, $\bar{\rho} \to \rho^*$ and $v \to 0$. The density approaches the penalty equilibrium from above (if $\bar{\rho}_0 > \rho^*$). The expansion rate approaches:

$$\mathcal{H}_\infty = 0$$

ED predicts that the universe approaches a **static state** at $\bar{\rho} = \rho^*$, not continued exponential expansion. This is fundamentally different from $\Lambda$CDM, where de Sitter expansion continues forever.

The timescale to reach this state is $\tau_{\text{relax}} \sim 1/\gamma$. In physical units with Candidate A: $\gamma = 0.2$ in nondimensional units, so $\tau_{\text{relax}} = 5 T_0 = 21.8$ Gyr. The universe would still be expanding at the present time ($t_0 = 13.8$ Gyr $= 3.17 T_0$) but decelerating toward the static attractor.

### Early-time regime ($\bar{\rho} \gg \rho^*$)

When $\bar{\rho} \gg \rho^*$, the penalty is approximately $-DP_0\bar{\rho}$, giving:

$$\dot{\bar{\rho}} \approx -DP_0\bar{\rho} \quad \Rightarrow \quad \bar{\rho}(t) \approx \bar{\rho}_0\,e^{-DP_0 t}$$

The scale factor grows exponentially:

$$a(t) \approx a_0\,e^{DP_0 t/3} \tag{20}$$

This is **de Sitter-like expansion** — the ED penalty channel drives exponential expansion when the density is far from equilibrium. The expansion rate is $\mathcal{H} = DP_0/3$.

For Candidate A ($D = 0.3$, $P_0 = 1.0$): $\mathcal{H}_{\text{early}} = 0.1$ per $T_0 = 4.35$ Gyr, or $\mathcal{H} \approx 2.3 \times 10^{-18}$ s$^{-1}$, comparable to $H_0 = 2.18 \times 10^{-18}$ s$^{-1}$.

### Intermediate regime (telegraph oscillation)

When the participation channel is active and the system is underdamped, the density oscillates:

$$\bar{\rho}(t) = \rho^* + \delta_0\,e^{-\gamma t}\cos(\omega t + \phi)$$

The scale factor is:

$$a(t) = \left(\frac{\rho_0}{\rho^* + \delta_0 e^{-\gamma t}\cos(\omega t + \phi)}\right)^{1/3}$$

This produces **oscillatory corrections to the expansion history**: the scale factor does not grow monotonically but has damped oscillations superimposed on the secular expansion.

## 4.2 Does ED Predict Monotonic Expansion?

**No, in general.** The telegraph structure introduces oscillations.

However, the oscillations are damped, and their amplitude depends on $\delta_0/\rho^*$ (the initial density contrast) and $\gamma$ (the damping rate). For physical cosmological parameters:

- If $\gamma > \omega_0$ (overdamped, Candidate C): expansion is monotonic.
- If $\gamma < \omega_0$ (underdamped, Candidates A, B): expansion has oscillatory corrections.
- If $\gamma \approx \omega_0$ (critical, Candidates D, E): one large oscillation, then monotonic.

The observation that the universe's expansion history is smooth (no detected oscillations in $H(z)$ or $q(z)$ at current precision) constrains the parameters: either the system is overdamped, or the damping is fast enough that oscillations have decayed by the present epoch.

## 4.3 Telegraph-Like Corrections

The oscillatory correction to the deceleration parameter has the form:

$$\Delta q(t) = \Delta q_0\,e^{-\gamma t}\cos(\omega t + \psi) \tag{21}$$

In redshift space ($z = a_0/a - 1$, $t = t(z)$):

$$\Delta q(z) = \Delta q_0\,e^{-\gamma t(z)}\cos[\omega t(z) + \psi]$$

The period of the oscillation in cosmic time is:

$$T_{\text{osc}} = \frac{2\pi}{\omega}$$

For Candidate A: $\omega = 0.30$ (nd), so $T_{\text{osc}} = 20.9$ (nd) $= 90.9$ Gyr. This is much longer than the age of the universe — the system has completed less than half a cycle. The observable signature would be a single, slow deviation from the smooth $\Lambda$CDM prediction, not a rapid oscillation.

For Candidate B: $\omega = 0.10$ (nd), $T_{\text{osc}} = 62.8$ (nd) $= 273$ Gyr. Even slower.

**The telegraph oscillation in cosmological ED operates on timescales much longer than the age of the universe.** The observable effect is not a rapid oscillation but a subtle, monotonic departure from $\Lambda$CDM — the first quarter-wave of a very slow oscillation.

## 4.4 Finite-Speed Horizon Propagation

ED-Phys-05 showed that the telegraph structure provides a finite propagation speed $c_{\text{ED}} = \sqrt{DH/\tau} = c$ in the cosmological regime (Section 1.6). This means:

1. **Density perturbations propagate at the speed of light.** The ED cosmological PDE, unlike pure diffusion, does not propagate information instantaneously. The causal structure is built into the participation channel.

2. **The particle horizon has a natural ED definition.** The maximum distance a density perturbation can travel from the Big Bang to time $t$ is:

$$d_H^{\text{ED}}(t) = \int_0^t c_{\text{ED}}\,dt' = c\,t$$

This is the standard particle horizon (for a static background). In an expanding background, the comoving horizon is:

$$\eta_H^{\text{ED}}(t) = \int_0^t \frac{c}{a(t')}\,dt'$$

which is formally identical to the Friedmann particle horizon. **ED's causal structure is consistent with standard cosmology when the Compton/Hubble anchoring is applied.**

## 4.5 Phase Portrait

The cosmological dynamical system (3)--(4) has a single fixed point at $(\bar{\rho}, v) = (\rho^*, 0)$. The Jacobian at the fixed point is:

$$J = \begin{pmatrix} -DP_0 & H \\ -DP_0/\tau & -\zeta/\tau \end{pmatrix}$$

The eigenvalues are $\lambda = -\gamma \pm i\omega$ (underdamped) or $\lambda = -\lambda_\pm$ (overdamped).

**The fixed point is always stable** (both eigenvalues have negative real parts, since $\gamma > 0$ for any positive $P_0$, $\zeta$, $\tau$). The cosmological attractor $\bar{\rho} = \rho^*$ is globally attracting — every initial condition relaxes to it.

**Phase portrait structure:**

- **Underdamped** ($\omega_0 > \gamma$): spiral attractor. Trajectories wind inward, producing oscillatory approach to $(\rho^*, 0)$.
- **Overdamped** ($\omega_0 < \gamma$): node attractor. Trajectories approach monotonically along the slow eigenvector.
- **Critically damped** ($\omega_0 = \gamma$): degenerate node. Fastest monotonic approach.

---

# 5. Cosmological Falsification Conditions

## 5.1 F_cosmo_1: ED-to-Friedmann Mismatch

**Statement:** The ED cosmological equations (3)--(4) must reduce to the Friedmann equations in an appropriate limit. Specifically, the ED Hubble parameter (15) must match $H_0 = 67.4$ km/s/Mpc at the present epoch when the parameters are anchored to $c$, $H_0$, $G$.

**Quantitative criterion:** $|\mathcal{H}_{\text{ED}}(t_0) - H_0| / H_0 < 20\%$ at $t_0 = 13.8$ Gyr for at least one candidate parameter set.

**What would falsify:** If no choice of $(P_0, \zeta, \tau)$ within the physically motivated range produces $\mathcal{H}_{\text{ED}}(t_0) \approx H_0$, the ED cosmological limit is quantitatively incompatible with the observed expansion rate.

**Connection to ED-Phys-05:** The Hubble parameter formula (15) depends on $H$ and $v(t)$, both of which are determined by the participation-field interpretation. If the Compton anchoring ($H = c^2\tau/D$) gives the wrong Hubble rate, the causality argument may not apply at cosmological scales.

## 5.2 F_cosmo_2: Wrong Sign of $q(t)$

**Statement:** The observed universe is currently accelerating ($q_0 < 0$, confirmed by Type Ia supernova data). ED must produce $q_{\text{ED}}(t_0) < 0$ at the present epoch.

**Quantitative criterion:** $q_{\text{ED}}(t_0) < 0$ for the selected parameter set.

**What would falsify:** If $q_{\text{ED}}(t_0) > 0$ for all physically motivated parameter sets, ED predicts a decelerating universe — contradicting the supernova observations.

**Connection to ED-Phys-06:** The deceleration parameter depends on the participation dynamics, which operate differently in the safe region ($H/P_0 \lesssim 100$) and the telegraph region. If the cosmological point is in the safe region (as Section 2 indicates), the energy functional is monotonic and the expansion should be monotonically decelerating at late times — which would make $q_0 < 0$ a challenge for ED.

## 5.3 F_cosmo_3: Incorrect Horizon Propagation

**Statement:** The ED particle horizon must be consistent with the observed CMB angular scale ($\theta_* \approx 1.04^\circ$, corresponding to the sound horizon at recombination).

**Quantitative criterion:** The ED comoving horizon at recombination ($z \approx 1100$) must equal $r_s \approx 150$ Mpc to within 30%.

**What would falsify:** If the ED propagation speed ($c_{\text{ED}} = c$ from the Compton/Hubble anchoring) produces a horizon that is grossly inconsistent with the observed sound horizon, the causal structure of ED cosmology is wrong.

**Note:** Since $c_{\text{ED}} = c$ exactly (Section 1.6), and the horizon integral has the same form as the Friedmann case, this criterion is expected to pass by construction. The test becomes nontrivial only if the ED expansion history $a(t)$ differs significantly from $\Lambda$CDM, changing the integrand.

## 5.4 F_cosmo_4: Instability Outside the $H/P_0$ Band

**Statement:** The cosmological parameter point must lie within the Lyapunov-stable region identified by ED-Phys-06 ($H/P_0 \lesssim 100$).

**Quantitative criterion:** $H_{\text{cosmo}}/P_0 < 100$ for the selected $P_0$.

**What would falsify:** If the only parameter sets that match observational constraints (F_cosmo_1, F_cosmo_2) require $H/P_0 > 100$, the cosmological limit lies outside the stable region and the energy functional does not provide a Lyapunov guarantee. The ED architecture would be mathematically consistent but structurally unstable at cosmological scales.

**Current status:** For $H_{\text{nd}} = 0.3$ and $P_0 \geq 0.01$, $H/P_0 \leq 30$. **This criterion is satisfied** for all candidate parameter sets.

## 5.5 F_cosmo_5: Failure to Reproduce Observed Expansion Scaling

**Statement:** The ED expansion law $a(t)$ must be consistent with the observed expansion history as measured by $H(z)$ from baryon acoustic oscillation (BAO) surveys and Type Ia supernovae.

**Quantitative criterion:** The ED prediction for $H(z)$ must agree with the DESI/Planck combined data to within $3\sigma$ at $z = 0, 0.5, 1.0, 2.0$.

**What would falsify:** If the ED expansion law produces $H(z)$ values that are systematically wrong (e.g., always too high or too low) at multiple redshifts, the cosmological telegraph equation does not describe the real universe.

**How to test:** Numerically integrate equations (3)--(4) for each candidate parameter set, compute $a(t)$, invert to get $H(z)$, and compare to observational data.

---

# 6. Conceptual Interpretation

## 6.1 What Cosmology "Is" Inside ED

In the ED framework, cosmological expansion is not a property of spacetime geometry. It is a consequence of **penalty-driven density relaxation**: the universe has density $\bar{\rho} > \rho^*$ (above equilibrium) and is relaxing toward $\rho^*$ via the penalty channel. The "expansion" is a density decrease, not a metric stretching.

The scale factor $a(t)$ is a derived quantity — defined by $a = (\rho_0/\bar{\rho})^{1/3}$ — not a fundamental degree of freedom. The fundamental dynamical variables are $\bar{\rho}(t)$ and $v(t)$.

This is a radical reinterpretation: dark energy is not a mysterious substance or a cosmological constant. It is the **penalty channel** — the constitutive tendency of the ED density field to relax toward $\rho^*$. The penalty strength $P_0$ plays the role of the cosmological constant $\Lambda$, and the equilibrium density $\rho^*$ plays the role of the dark energy density $\rho_\Lambda$.

## 6.2 Why the Participation Field Matters

Without the participation channel ($H = 0$), the cosmological ED equation is simply:

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*)$$

This is exponential relaxation — de Sitter expansion with no oscillatory corrections and no finite propagation speed. It is indistinguishable from a $\Lambda$CDM model with $\Lambda = 8\pi G \rho^* / c^2$.

The participation channel ($H > 0$) adds three things:

1. **Finite causal speed.** The telegraph structure gives $c_{\text{ED}} = c$, preventing superluminal density propagation.

2. **Oscillatory corrections.** The density and expansion rate have damped telegraph oscillations, producing subtle deviations from smooth $\Lambda$CDM.

3. **A dynamical dark energy.** The effective equation of state $w_{\text{ED}}(t)$ is not constant — it evolves as the telegraph oscillation damps out. This makes ED a dynamical dark energy model, not a cosmological constant model.

The participation field is what makes ED cosmology *distinguishable* from $\Lambda$CDM. Without it, ED reduces to $\Lambda$CDM. With it, ED predicts specific corrections that are, in principle, observable.

## 6.3 Why $H/P_0$ Controls Stability

The ratio $H/P_0$ measures the relative strength of the driving force (participation) to the restoring force (penalty). When the restoring force dominates ($H/P_0 \ll 1$), the system relaxes smoothly and the energy functional decreases monotonically. When the driving force dominates ($H/P_0 \gg 1$), the participation channel can transiently *increase* the energy, breaking the Lyapunov structure.

At cosmological scales, the ED-Phys-06 result places this boundary at $H/P_0 \sim 100$--$1000$. The cosmological point ($H/P_0 \leq 30$ for all candidate sets) is safely inside. This means:

- The energy functional is a valid Lyapunov function for cosmological ED.
- The fixed point $(\rho^*, 0)$ is globally attracting.
- The expansion history is guaranteed to converge (no runaway instabilities).

The stability of the cosmological limit is not assumed — it is *derived* from the ED-Phys-06 phase diagram.

## 6.4 How the Cosmological Limit Fits into the ED Architecture

```
ED Architecture (Foundational Paper)
    |
    |--- Seven Axioms P1-P7 → Canonical PDE
    |
    |--- Three Channels:
    |       Mobility   (PME, fronts, compact support)     ← absent in cosmo limit
    |       Penalty    (relaxation, restoring force)       ← drives expansion
    |       Participation (telegraph, oscillation, v(t))   ← provides causality + corrections
    |
    |--- ED-Phys-05: v(t) = mean Madelung velocity, H = 2*omega_C (quantum)
    |                                                   H = D_nd (cosmological)
    |
    |--- ED-Phys-06: (beta, H) phase diagram
    |       Safe region: H/P0 < 100
    |       Cosmo point: H/P0 = 0.3--30 → SAFE
    |
    |--- ED-Cosmo-01 (this paper):
            Homogeneous limit → 2-ODE system
            Telegraph equation for density
            Scale factor derived from rho(t)
            Friedmann mapping: H_ED, q_ED, w_ED
            Five falsification conditions
```

## 6.5 Connection to ED-Phys-05 and ED-Phys-06

**From ED-Phys-05:** The causality requirement uniquely fixes $H_{\text{cosmo}} = D_{\text{nd}} = 0.3$ in nondimensional units, giving $c_{\text{ED}} = c$. The damping $\gamma$ is the cosmological decoherence rate — the rate at which the universe loses "memory" of its initial conditions. The participation field $v(t)$ is the mean bulk flow at Hubble scales — the net peculiar velocity of the cosmic fluid.

**From ED-Phys-06:** The cosmological point lies in the safe region of the $(\beta, H)$ phase diagram. The Lyapunov boundary is far above the cosmological $H$, so the energy functional is valid. The $H/P_0$ stability criterion — the most important result of ED-Phys-06 — directly constrains the allowed cosmological parameter space.

**What ED-Cosmo-01 adds:** The explicit dynamical system (3)--(4) for the cosmological limit, the mapping to Friedmann observables ($\mathcal{H}$, $q$, $w$), the identification of the penalty channel with dark energy, the prediction of telegraph oscillatory corrections, and five quantitative falsification criteria.

**What comes next:** Numerical integration of (3)--(4) for each candidate parameter set, comparison of the predicted $H(z)$ with BAO/supernova data, and determination of which (if any) parameter set is consistent with the observed expansion history.

---

*ED-Cosmo-01 · Event Density Research Programme · March 2026*
