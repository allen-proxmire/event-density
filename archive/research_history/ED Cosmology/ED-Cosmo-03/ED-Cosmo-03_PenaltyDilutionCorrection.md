# ED-Cosmo-03: Correcting the Penalty-Dilution Coupling in ED Cosmology

**Author:** Allen Proxmire
**Series:** ED-Cosmo-03
**Date:** March 2026
**Status:** Theoretical derivation — corrected expansion equations

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| ED-5 (Foundational Paper) | Canonical PDE, constitutive channels, axiom P3 (mass conservation) |
| ED-I-012.0 (Compositional Rule) | Three-penalty compositional rule |
| ED-I-012.5 (Cosmology Specialization) | Epoch classification, horizon conditions |
| ED-Phys-05 (Participation Field) | $v(t)$ as mean velocity, Compton/Hubble anchoring |
| ED-Phys-06 (Phase Diagram) | $H/P_0$ stability, Lyapunov boundary |
| ED-Cosmo-01 (Homogeneous Limit) | 2-ODE telegraph system, F1 failure (H decays too fast) |
| ED-Cosmo-02 (Spatial Cosmology) | 1D PDE, F1 failure ($a < 1$), synchronization confirmed |

**Scope.** This paper resolves the F1 failure that appeared in both ED-Cosmo-01 and ED-Cosmo-02. The root cause is that the naive Hubble-dilution term $-\mathcal{H}\rho$ is incompatible with the penalty channel's relaxation toward $\rho^*$ when the two operate simultaneously. The resolution requires a careful derivation of how mass conservation, penalty relaxation, and expansion interact — leading to a corrected dilution operator that preserves all three channels while producing monotonic expansion ($a(t) > 1$ for all $t > 0$).

---

## Table of Contents

1. [Diagnosis of the F1 Failure](#1-diagnosis-of-the-f1-failure)
2. [Derivation of the Correct Dilution Term](#2-derivation-of-the-correct-dilution-term)
3. [Revised Cosmological Evolution Equation](#3-revised-cosmological-evolution-equation)
4. [Preservation of Synchronization-Driven Acceleration](#4-preservation-of-synchronization-driven-acceleration)
5. [Parameter Constraints](#5-parameter-constraints)
6. [Preparation for ED-Cosmo-04](#6-preparation-for-ed-cosmo-04)

---

# 1. Diagnosis of the F1 Failure

## 1.1 Two Distinct Failures

The F1 criterion requires $|\mathcal{H}_{\text{ED}}(t_0) - H_0|/H_0 < 20\%$. It failed in two different ways:

### ED-Cosmo-01 (homogeneous ODE)

The system:

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + Hv$$

relaxes $\bar{\rho} \to \rho^*$ on a timescale $\tau_{\text{relax}} = 1/\gamma \sim 5$--$22$ Gyr. By $t_0 = 13.8$ Gyr, the density has nearly reached $\rho^*$, so $\dot{\bar{\rho}} \approx 0$ and $\mathcal{H} = -\dot{\bar{\rho}}/(3\bar{\rho}) \approx 0$.

**Failure mode:** $\mathcal{H}$ decays to zero — the expansion finishes before the present time.

### ED-Cosmo-02 (spatial PDE)

The system:

$$\partial_t \rho = \frac{D}{a^2}\partial_x[M(\rho)\partial_x\rho] - DP_0(\rho - \rho^*) + Hv \underbrace{- \mathcal{H}\rho}_{\text{dilution}}$$

produced $a(t_0) < 1$ (contraction) for the two stable ICs.

**Failure mode:** $a(t)$ decreases — the universe contracts instead of expanding.

## 1.2 Mathematical Diagnosis of the Incompatibility

The conflict between the penalty channel and the dilution term can be seen directly. Consider the mean-density evolution in ED-Cosmo-02 (from equation 22 of that paper, with the mobility integral vanishing under periodic BCs):

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + H\bar{v} - \mathcal{H}\bar{\rho} \tag{1}$$

Substituting $\mathcal{H} = -\dot{\bar{\rho}}/\bar{\rho}$:

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + H\bar{v} + \frac{\dot{\bar{\rho}}}{\bar{\rho}}\bar{\rho} = -DP_0(\bar{\rho} - \rho^*) + H\bar{v} + \dot{\bar{\rho}}$$

This gives $0 = -DP_0(\bar{\rho} - \rho^*) + H\bar{v}$, which is the equilibrium condition, not a dynamical equation. **The self-consistent $\mathcal{H}$ term absorbs all the dynamics** — it exactly cancels the penalty and participation contributions to $\dot{\bar{\rho}}$.

This is the mathematical root of the failure: the naive dilution $-\mathcal{H}\rho$ with $\mathcal{H} = -\dot{\bar{\rho}}/\bar{\rho}$ creates a tautology. The mean-density equation becomes trivially satisfied regardless of the penalty strength, and the actual dynamics are governed entirely by a feedback loop between $\mathcal{H}$ and $\bar{\rho}$ that has no connection to the ED channels.

## 1.3 The Physical Origin of the Error

The error arises from conflating two distinct physical mechanisms:

1. **Penalty relaxation** ($-DP_0(\rho - \rho^*)$): an intrinsic ED channel that drives $\rho$ toward $\rho^*$. This is a material property of the density field.

2. **Cosmological dilution** ($-\mathcal{H}\rho$): a geometric effect from the expansion of space. This is a property of the metric, not of the density field.

In standard cosmology, these are separated by construction: the Friedmann equations govern the metric ($a(t)$) and the matter equations govern the density ($\rho$). The coupling goes one way: $a(t)$ appears in the matter equations through the dilution term, but $\rho$ affects $a(t)$ only through the Friedmann equations (the gravitational coupling).

In ED-Cosmo-02, both penalty and dilution act on $\rho$ simultaneously, and $a(t)$ is derived from $\bar{\rho}$ (not from a separate gravitational equation). This creates a circular dependency: $\rho$ determines $a$, which determines $\mathcal{H}$, which feeds back into $\rho$. The naive coupling produces a degenerate feedback loop.

**The resolution:** separate the penalty relaxation (which changes the *intrinsic* density field) from the cosmological dilution (which changes the *apparent* density due to volume expansion). The penalty operates on the comoving density; the dilution operates on the physical density. These are not the same operation.

---

# 2. Derivation of the Correct Dilution Term

## 2.1 Two Densities: Comoving vs. Physical

Define:
- $\rho_{\text{com}}(x,t)$: comoving density (the ED field, governed by the canonical PDE)
- $\rho_{\text{phys}}(x,t) = \rho_{\text{com}}(x,t) / a(t)^d$: physical (proper) density

In $d = 1$: $\rho_{\text{phys}} = \rho_{\text{com}} / a$.

**The ED PDE governs $\rho_{\text{com}}$.** The penalty channel, mobility channel, and participation channel operate on the comoving density — these are intrinsic material processes that occur in the comoving frame.

**The cosmological dilution is already accounted for** by the relationship $\rho_{\text{phys}} = \rho_{\text{com}}/a^d$. Adding an explicit $-\mathcal{H}\rho$ term to the comoving PDE *double-counts* the dilution.

## 2.2 Mass Conservation in the Comoving Frame

Axiom P3 of the ED Foundational Paper requires mass conservation. In the comoving frame with periodic boundary conditions:

$$\frac{d}{dt}\int_0^L \rho_{\text{com}}(x,t)\,dx = \int_0^L \partial_t\rho_{\text{com}}\,dx = 0 \tag{2}$$

The mobility channel conserves mass (divergence form + periodic BCs). The participation channel, integrated over the domain, gives $H\int v\,dx = HL\bar{v}$.

**The penalty channel does NOT conserve mass** in general: $\int -DP_0(\rho - \rho^*)\,dx = -DP_0 L(\bar{\rho} - \rho^*)$. This is nonzero whenever $\bar{\rho} \neq \rho^*$.

In the standard ED framework (non-cosmological), this mass non-conservation is correct: the penalty represents exchange with a reservoir (the environment). In cosmology, the "reservoir" is the expanding space itself. The mass that disappears from the comoving frame reappears as diluted physical density.

## 2.3 The Separation Principle

**Principle:** The ED PDE governs the comoving density $\rho_{\text{com}}$ without any explicit dilution term. The cosmological expansion enters *only* through the definition of the physical density and the scale factor:

$$\rho_{\text{phys}}(x,t) = \frac{\rho_{\text{com}}(x,t)}{a(t)^d} \tag{3}$$

The scale factor is determined by a *separate* equation — either the Friedmann equation (if gravitational coupling is included) or a self-consistency condition derived from the penalty channel's mass non-conservation.

## 2.4 The Scale Factor from Penalty Mass Flow

The key insight: the mass that the penalty channel removes from the comoving density field is the mass that goes into expanding the volume. Define the total comoving mass:

$$M_{\text{com}}(t) = \int_0^L \rho_{\text{com}}\,dx = L\bar{\rho}_{\text{com}}(t) \tag{4}$$

The penalty channel changes this mass at rate:

$$\dot{M}_{\text{com}} = -DP_0 L(\bar{\rho}_{\text{com}} - \rho^*) + HL\bar{v} \tag{5}$$

(mobility contribution vanishes under periodic BCs).

The physical mass must be conserved (total mass of the universe is constant):

$$M_{\text{phys}} = \frac{M_{\text{com}}}{a^d} = \text{const} \tag{6}$$

Differentiating (6):

$$\frac{\dot{M}_{\text{com}}}{a^d} - d\frac{M_{\text{com}}\dot{a}}{a^{d+1}} = 0$$

$$\dot{M}_{\text{com}} = d\frac{\dot{a}}{a}M_{\text{com}} = d\,\mathcal{H}\,M_{\text{com}} \tag{7}$$

Combining (5) and (7):

$$-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v} = d\,\mathcal{H}\,\bar{\rho}_{\text{com}} \tag{8}$$

Solving for the Hubble parameter:

$$\boxed{\mathcal{H}(t) = \frac{-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v}}{d\,\bar{\rho}_{\text{com}}}} \tag{9}$$

And the scale factor ODE:

$$\boxed{\dot{a} = a\,\mathcal{H} = \frac{a}{d\,\bar{\rho}_{\text{com}}}\bigl[-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v}\bigr]} \tag{10}$$

**This is the corrected coupling.** The Hubble parameter is determined by the rate at which the penalty channel (plus participation) removes mass from the comoving frame. There is no explicit $-\mathcal{H}\rho$ term in the comoving PDE — the dilution is already encoded in the $\rho_{\text{com}}/a^d$ relationship.

## 2.5 The Corrected Dilution Operator

The corrected system has **no dilution term** in the comoving PDE. The ED equation for the comoving density is simply:

$$\partial_t \rho_{\text{com}} = \frac{D}{a^2}\partial_x[M(\rho_{\text{com}})\partial_x\rho_{\text{com}}] - DP_0(\rho_{\text{com}} - \rho^*) + Hv \tag{11}$$

$$\partial_t v = \frac{1}{\tau}\Bigl(\frac{D}{a^2}\partial_x[M(\rho_{\text{com}})\partial_x\rho_{\text{com}}] - DP_0(\rho_{\text{com}} - \rho^*) - \zeta v\Bigr) \tag{12}$$

$$\dot{a} = \frac{a}{d\,\bar{\rho}_{\text{com}}}\bigl[-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v}\bigr] \tag{13}$$

The $1/a^2$ factor on the mobility remains (physical-to-comoving gradient transformation). The Hubble drag on $v$ (the $-\mathcal{H}v$ term from ED-Cosmo-02) is also removed — it was part of the same error. The participation field evolves in the comoving frame without geometric corrections.

**Comparison with ED-Cosmo-02:**

| Term | ED-Cosmo-02 (incorrect) | ED-Cosmo-03 (corrected) |
|------|------------------------|------------------------|
| Comoving $\rho$ PDE | $\partial_t\rho = \text{mobility} + \text{penalty} + Hv - \mathcal{H}\rho$ | $\partial_t\rho = \text{mobility} + \text{penalty} + Hv$ |
| Participation PDE | $\partial_t v = \frac{1}{\tau}(\ldots) - \mathcal{H}v$ | $\partial_t v = \frac{1}{\tau}(\ldots)$ |
| Scale factor | $a = \bar{\rho}(0)/\bar{\rho}(t)$ (from mean density) | $\dot{a}$ from penalty mass flow (eq. 13) |
| Physical density | $\rho_{\text{phys}} = \rho_{\text{com}}$ (conflated) | $\rho_{\text{phys}} = \rho_{\text{com}}/a^d$ |

---

# 3. Revised Cosmological Evolution Equation

## 3.1 The Mean-Density Evolution

Spatially averaging equation (11) under periodic BCs (mobility integral vanishes):

$$\dot{\bar{\rho}}_{\text{com}} = -DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v} \tag{14}$$

This is identical to the ED-Cosmo-01 equation (3) — **but now $\bar{\rho}_{\text{com}}$ is the comoving density, not the physical density.** The physical density is:

$$\bar{\rho}_{\text{phys}}(t) = \frac{\bar{\rho}_{\text{com}}(t)}{a(t)^d} \tag{15}$$

## 3.2 The Corrected Hubble Parameter

From equation (9), in $d = 1$:

$$\mathcal{H}(t) = \frac{-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v}}{\bar{\rho}_{\text{com}}} = -\frac{\dot{\bar{\rho}}_{\text{com}}}{\bar{\rho}_{\text{com}}} \tag{16}$$

Since $\bar{\rho}_{\text{com}}(0) > \rho^*$ and the penalty drives $\bar{\rho}_{\text{com}} \to \rho^*$, we have $\dot{\bar{\rho}}_{\text{com}} < 0$ (comoving density decreases), which gives $\mathcal{H} > 0$ (expansion).

**This resolves the sign problem.** In ED-Cosmo-02, the $-\mathcal{H}\rho$ term fought the penalty channel, potentially producing $\dot{\bar{\rho}} > 0$ (contraction). Without the explicit dilution term, the penalty channel *is* the expansion mechanism — the mass it removes from the comoving frame is the mass that dilutes the physical density.

## 3.3 The Corrected Scale Factor

From equation (10) in $d = 1$:

$$\dot{a} = \frac{a}{\bar{\rho}_{\text{com}}}\bigl[-DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v}\bigr] = -a\frac{\dot{\bar{\rho}}_{\text{com}}}{\bar{\rho}_{\text{com}}} \tag{17}$$

Integrating: $\ln a = -\ln\bar{\rho}_{\text{com}} + C$, so:

$$a(t) = \frac{\bar{\rho}_{\text{com}}(0)}{\bar{\rho}_{\text{com}}(t)} \tag{18}$$

This is the same formula as ED-Cosmo-01 equation (13) — but now it is *derived* from physical mass conservation rather than assumed. And because $\bar{\rho}_{\text{com}}$ is governed by the standard ED telegraph equation (14) without any dilution feedback, it behaves correctly: $\bar{\rho}_{\text{com}}$ decreases monotonically toward $\rho^*$, and $a(t)$ increases monotonically.

## 3.4 Proof: $a(t) > 1$ for All $t > 0$

From (14), when $\bar{\rho}_{\text{com}}(0) > \rho^*$ and $\bar{v}(0) = 0$:

$$\dot{\bar{\rho}}_{\text{com}}(0) = -DP_0(\bar{\rho}_{\text{com}}(0) - \rho^*) < 0$$

So $\bar{\rho}_{\text{com}}$ initially decreases. The attractor is $(\rho^*, 0)$ with $\rho^* < \bar{\rho}_{\text{com}}(0)$, so $\bar{\rho}_{\text{com}}(t) < \bar{\rho}_{\text{com}}(0)$ for all $t > 0$ (the telegraph trajectory from ED-Cosmo-01 always moves toward $\rho^*$ from above).

Therefore $a(t) = \bar{\rho}_{\text{com}}(0)/\bar{\rho}_{\text{com}}(t) > 1$ for all $t > 0$. $\square$

## 3.5 Proof: $\mathcal{H}(t) > 0$ for All $t > 0$

From (16), $\mathcal{H} = -\dot{\bar{\rho}}_{\text{com}}/\bar{\rho}_{\text{com}}$. Since $\bar{\rho}_{\text{com}}(t) > 0$ (density is positive) and $\dot{\bar{\rho}}_{\text{com}}(t) \leq 0$ (telegraph trajectory to $\rho^*$ from above), $\mathcal{H}(t) \geq 0$ for all $t$.

Equality holds only at the attractor ($\bar{\rho}_{\text{com}} = \rho^*$, $\bar{v} = 0$), which is approached asymptotically but never reached in finite time (for the underdamped telegraph, the trajectory spirals inward). Therefore $\mathcal{H}(t) > 0$ for all finite $t$. $\square$

## 3.6 The Corrected Homogeneous System

In the homogeneous limit ($\nabla\rho = 0$), the corrected system is:

$$\dot{\bar{\rho}}_{\text{com}} = -DP_0(\bar{\rho}_{\text{com}} - \rho^*) + H\bar{v} \tag{19}$$

$$\dot{\bar{v}} = \frac{1}{\tau}[-DP_0(\bar{\rho}_{\text{com}} - \rho^*) - \zeta\bar{v}] \tag{20}$$

$$a(t) = \bar{\rho}_{\text{com}}(0)/\bar{\rho}_{\text{com}}(t) \tag{21}$$

This is the same telegraph ODE as ED-Cosmo-01, equations (3)--(4). **The mean-density evolution is unchanged.** What changes is the *interpretation*: $\bar{\rho}_{\text{com}}$ is the comoving density, not the physical density. The physical density is $\bar{\rho}_{\text{phys}} = \bar{\rho}_{\text{com}}/a = \bar{\rho}_{\text{com}}^2/\bar{\rho}_{\text{com}}(0)$, which decreases faster than $\bar{\rho}_{\text{com}}$ alone.

The Hubble parameter from the corrected system is:

$$\mathcal{H}(t) = \frac{DP_0(\bar{\rho}_{\text{com}} - \rho^*) - H\bar{v}}{\bar{\rho}_{\text{com}}} \tag{22}$$

This is positive when $\bar{\rho}_{\text{com}} > \rho^*$ and $|H\bar{v}|$ is small — which is true at early and late times. During telegraph oscillations, $\mathcal{H}$ can dip (the oscillation modulates the expansion rate) but does not change sign as long as the oscillation amplitude is smaller than the penalty drive.

---

# 4. Preservation of Synchronization-Driven Acceleration

## 4.1 The Deceleration Parameter in the Corrected System

From $\mathcal{H} = -\dot{\bar{\rho}}_{\text{com}}/\bar{\rho}_{\text{com}}$ and $q = -1 - \dot{\mathcal{H}}/\mathcal{H}^2$:

$$\dot{\mathcal{H}} = -\frac{\ddot{\bar{\rho}}_{\text{com}}}{\bar{\rho}_{\text{com}}} + \frac{\dot{\bar{\rho}}_{\text{com}}^2}{\bar{\rho}_{\text{com}}^2} = -\frac{\ddot{\bar{\rho}}_{\text{com}}}{\bar{\rho}_{\text{com}}} + \mathcal{H}^2 \tag{23}$$

Therefore:

$$q = -1 - \frac{-\ddot{\bar{\rho}}/\bar{\rho} + \mathcal{H}^2}{\mathcal{H}^2} = \frac{\ddot{\bar{\rho}}_{\text{com}}}{\bar{\rho}_{\text{com}}\mathcal{H}^2} \tag{24}$$

For $q < 0$ we need $\ddot{\bar{\rho}}_{\text{com}} < 0$ — the comoving density must be *decelerating* (its rate of decrease is itself decreasing). This is equivalent to saying the expansion is accelerating: the density decrease is slowing down, so the Hubble parameter is sustained longer than a pure exponential would predict.

## 4.2 When Does $\ddot{\bar{\rho}}_{\text{com}} < 0$?

Differentiating (19):

$$\ddot{\bar{\rho}}_{\text{com}} = -DP_0\dot{\bar{\rho}}_{\text{com}} + H\dot{\bar{v}} \tag{25}$$

Substituting (20):

$$\ddot{\bar{\rho}}_{\text{com}} = -DP_0\dot{\bar{\rho}}_{\text{com}} + \frac{H}{\tau}[-DP_0(\bar{\rho}_{\text{com}} - \rho^*) - \zeta\bar{v}] \tag{26}$$

At early times ($\bar{v} \approx 0$, $\bar{\rho}_{\text{com}}$ decreasing so $\dot{\bar{\rho}} < 0$):

$$\ddot{\bar{\rho}}_{\text{com}} \approx DP_0|\dot{\bar{\rho}}| - \frac{HDP_0}{\tau}(\bar{\rho}_{\text{com}} - \rho^*) \tag{27}$$

The first term is positive (deceleration of density decrease — the density *wants* to slow its descent, producing $q > 0$). The second term is negative (the participation channel accelerates the density decrease — the telegraph forcing pushes harder, producing $q < 0$).

**The participation channel produces $q < 0$ when:**

$$\frac{H}{\tau}(\bar{\rho}_{\text{com}} - \rho^*) > |\dot{\bar{\rho}}_{\text{com}}| = DP_0(\bar{\rho}_{\text{com}} - \rho^*) - H\bar{v}$$

At early times with $\bar{v} \approx 0$: $H/\tau > DP_0$, i.e., $H > DP_0\tau$. For the cosmological parameters ($H = 0.3$, $D = 0.3$, $P_0 = 0.1$, $\tau = 1.0$): $H = 0.3 > DP_0\tau = 0.03$. **Condition satisfied.**

The participation channel is 10$\times$ stronger than the penalty-induced deceleration. $q < 0$ is the generic outcome at early-to-intermediate times.

## 4.3 Void-Filament Differential Preserved

The corrected PDE (11) still contains the mobility channel $(D/a^2)\partial_x[M(\rho)\partial_x\rho]$. This term:

- Produces zero flux in uniform regions
- Creates fronts at density contrasts (compact support from degenerate mobility)
- Shuts off diffusion near $\rho_{\max}$ (filaments resist smoothing)
- Allows rapid diffusion in underdense regions (voids expand freely)

None of these properties depend on the dilution term. The void-filament differential is intrinsic to the mobility channel and survives the correction unchanged.

## 4.4 Synchronization Preserved

The participation field $v(x,t)$ still couples local dynamics globally through the $Hv$ term in the density equation and the local-forcing term in the $v$ equation. The removal of the $-\mathcal{H}v$ Hubble-drag term from the $v$ equation actually *strengthens* the synchronization mechanism: without the drag, the participation field can build up larger amplitudes and synchronize more effectively.

## 4.5 Telegraph Quarter-Wave Preserved

The homogeneous system (19)--(20) is the same telegraph equation as ED-Cosmo-01. Its solutions are damped sinusoids:

$$\bar{\rho}_{\text{com}}(t) = \rho^* + \delta_0 e^{-\gamma t}\cos(\omega t + \phi)$$

The oscillation period at cosmological parameters is $T_{\text{osc}} \gg t_0$ (Section 4.3 of ED-Cosmo-01), so the observable effect is a quarter-wave — a single, slow deviation from monotonic relaxation. This is unaffected by the dilution correction because the mean-density ODE is unchanged.

---

# 5. Parameter Constraints

## 5.1 Matching $\mathcal{H}(t_0) \approx H_0$

From (22), at the present time:

$$\mathcal{H}(t_0) = \frac{DP_0(\bar{\rho}_{\text{com}}(t_0) - \rho^*) - H\bar{v}(t_0)}{\bar{\rho}_{\text{com}}(t_0)}$$

In physical units: $\mathcal{H}_{\text{phys}} = \mathcal{H}_{\text{nd}} / T_0$, and the target is $H_0 = 1/t_H = H_0$.

Since $T_0 = D_{\text{nd}}/H_0$:

$$\mathcal{H}_{\text{phys}} = \frac{\mathcal{H}_{\text{nd}}}{D_{\text{nd}}/H_0} = \frac{\mathcal{H}_{\text{nd}} \cdot H_0}{D_{\text{nd}}}$$

Setting $\mathcal{H}_{\text{phys}} = H_0$:

$$\mathcal{H}_{\text{nd}}(t_0) = D_{\text{nd}} = 0.3 \tag{28}$$

The nondimensional Hubble parameter at the present time must equal $D_{\text{nd}}$. From (22):

$$\frac{DP_0(\bar{\rho}_{\text{com}}(t_0) - \rho^*)}{\bar{\rho}_{\text{com}}(t_0)} = D_{\text{nd}} + \frac{H\bar{v}(t_0)}{\bar{\rho}_{\text{com}}(t_0)} \tag{29}$$

At late times in the telegraph trajectory, $\bar{v} \to 0$, so:

$$DP_0\frac{\bar{\rho}_{\text{com}}(t_0) - \rho^*}{\bar{\rho}_{\text{com}}(t_0)} \approx D_{\text{nd}} \tag{30}$$

Define $\eta(t_0) = (\bar{\rho}_{\text{com}}(t_0) - \rho^*)/\bar{\rho}_{\text{com}}(t_0)$ as the fractional density excess at $t_0$:

$$P_0 \cdot \eta(t_0) \approx 1 \tag{31}$$

## 5.2 Matching $q(t_0) \approx -0.55$

From (24), $q < 0$ requires $\ddot{\bar{\rho}} < 0$. The magnitude of $q$ depends on the telegraph parameters. For $|q| \sim 0.5$:

$$|\ddot{\bar{\rho}}| \sim 0.5 \cdot \bar{\rho} \cdot \mathcal{H}^2$$

This constrains the participation coupling relative to the penalty: $H/\tau$ must be sufficiently larger than $DP_0$ to produce significant acceleration but not so large as to produce wild oscillations.

## 5.3 Staying Inside the Lyapunov Region

From ED-Phys-06: the safe region requires $H/P_0 \lesssim 100$. For $H = D_{\text{nd}} = 0.3$, this gives $P_0 \gtrsim 0.003$. All candidate values satisfy this easily.

## 5.4 Parameter Table

| Parameter | Constraint | Allowed range | Canonical value | Source |
|-----------|-----------|---------------|-----------------|--------|
| $D$ | Fixed by regime | $0.3$ | $0.3$ | Dimensional-05 |
| $H$ | Compton/Hubble anchoring | $D_{\text{nd}} = 0.3$ | $0.3$ | ED-Phys-05 |
| $P_0$ | $P_0 \cdot \eta(t_0) \approx 1$; $P_0 > 0.003$ | $[0.01, 1.0]$ | Depends on $\eta(t_0)$ | Eq. (31); ED-Phys-06 |
| $\zeta$ | $\gamma = (DP_0 + \zeta/\tau)/2 \lesssim \omega_0$ (underdamped) | $[0.01, 1.0]$ | $0.1$ | Telegraph condition |
| $\tau$ | $\tau \sim T_0$ (participation responds on cosmological timescale) | $[0.5, 2.0]$ | $1.0$ | Dimensional |
| $\beta$ | Universal (from ED-Phys-06); irrelevant in homogeneous limit | $[1, 5]$ | $2.0$ | ED-Phys-06 |
| $\rho_0$ | $\rho_0 > \rho^*$ (expansion direction) | $(0.5, 1.0)$ | $0.8$--$0.95$ | IC |
| $\rho^*$ | Equilibrium (physical: $\sim\Omega_\Lambda \rho_{\text{crit}}$) | $(0.3, 0.7)$ | $0.5$ | Constitutive |
| $H/P_0$ | Lyapunov stability | $< 100$ | $0.3$--$30$ | ED-Phys-06 |

**The critical free parameter is $P_0$.** Given $\eta(t_0)$, equation (31) determines $P_0$. The density excess $\eta(t_0)$ depends on the telegraph relaxation rate $\gamma$ and the time elapsed $t_0$:

$$\eta(t_0) \approx \eta_0\,e^{-\gamma t_0}\cos(\omega t_0 + \phi) + \frac{\rho^*}{\bar{\rho}_{\text{com}}(t_0)} - 1$$

For typical parameters, $\eta(t_0) \sim 0.1$--$0.5$, giving $P_0 \sim 2$--$10$. At $P_0 = 3$ and $H = 0.3$, $H/P_0 = 0.1$ — deep in the Lyapunov-safe region.

---

# 6. Preparation for ED-Cosmo-04

## 6.1 Implementation Tasks

ED-Cosmo-04 should implement the corrected system (equations 11--13) in the 1D spatial PDE solver and re-run the three ED-Cosmo-02 initial conditions. Specific tasks:

### Task 1: Corrected PDE solver

Modify the ED-Cosmo-02 solver:
- **Remove** the $-\mathcal{H}\rho$ dilution term from the $\rho$ equation.
- **Remove** the $-\mathcal{H}v$ Hubble drag from the $v$ equation.
- **Replace** the scale-factor computation: instead of $a = \bar{\rho}(0)/\bar{\rho}(t)$ computed from the current mean density, integrate $\dot{a}$ from equation (13) using the penalty mass flow.
- Verify that the two approaches ($a$ from mean density vs. $a$ from integrated ODE) agree to machine precision — they should, since they are algebraically equivalent in the corrected system.

### Task 2: $P_0$ sweep

Run the corrected system at $P_0 \in \{0.03, 0.1, 0.3, 1.0, 3.0, 10.0\}$ with IC1 (void-filament). For each:
- Compute $\mathcal{H}(t_0)$, $q(t_0)$, $a(t_0)$.
- Identify the $P_0$ that produces $\mathcal{H}(t_0) \approx H_0$.
- Check that $q(t_0) < 0$ at the same $P_0$.

### Task 3: Re-evaluate F1--F7

For the optimal $P_0$:
- Re-run all three ICs.
- Evaluate all seven falsification conditions.
- Confirm that the synchronization mechanism (F6) and void-filament differential (F7) survive.
- Verify that F1 now passes ($\mathcal{H}(t_0)$ within 20% of $H_0$).

### Task 4: Implicit integrator for IC2

Implement an implicit or semi-implicit scheme (e.g., Crank-Nicolson for the mobility channel, exact exponential for the penalty) to stabilise the Gaussian random field IC.

### Task 5: Physical density comparison

Compute $\bar{\rho}_{\text{phys}}(t) = \bar{\rho}_{\text{com}}(t)/a(t)$ and compare against the observed matter density history. This is the first direct comparison between ED cosmology and observational data.

## 6.2 Success Criteria for ED-Cosmo-04

| Criterion | Target | Source |
|-----------|--------|--------|
| $\mathcal{H}(t_0)$ matches $H_0$ | Within 20% | F1 |
| $q(t_0) < 0$ | Confirmed | F2 |
| $a(t_0) > 1$ | Confirmed | F5 (revised) |
| Synchronization | $\sigma^2_{\mathcal{H}}$ drops > 50% | F6 |
| Void > filament | Confirmed | F7 |
| $H/P_0 < 100$ | Satisfied | F4 |

If all six criteria are met simultaneously at a single $P_0$, ED produces a viable spatial cosmology with the correct expansion rate, apparent acceleration, and structure formation — all without a cosmological constant.

---

*ED-Cosmo-03 · Event Density Research Programme · March 2026*
